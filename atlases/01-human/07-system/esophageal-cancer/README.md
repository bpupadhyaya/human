---
schema: human-scale-entry/v1
id: esophageal-cancer
name: Esophageal Cancer
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Esophageal cancer includes ESCC (squamous, smoking/alcohol) and EAC (adenocarcinoma, Barrett's/HER2+ ~15%); nivolumab+chemotherapy (CheckMate 648) is first-line for ESCC; trastuzumab+chemotherapy (ToGA) and T-DXd for HER2+ EAC; 5-year OS ~20%."
aliases: ["esophageal cancer", "ESCC", "esophageal squamous cell carcinoma", "EAC", "esophageal adenocarcinoma", "Barrett's esophagus cancer", "GEJ cancer", "gastroesophageal junction cancer", "CheckMate 648", "ATTRACTION-3"]
sources:
  - id: doki-2022-checkmate648
    type: peer-reviewed
    cite: "Doki Y, Ajani JA, Kato K, et al. Nivolumab combination therapy in advanced esophageal squamous-cell carcinoma. N Engl J Med. 2022;386(5):449-462."
    doi: "10.1056/NEJMoa2111380"
    pmid: "35108470"
    url: "https://doi.org/10.1056/NEJMoa2111380"
  - id: kato-2019-attraction3
    type: peer-reviewed
    cite: "Kato K, Cho BC, Takahashi M, et al. Nivolumab versus chemotherapy in patients with advanced oesophageal squamous cell carcinoma refractory or intolerant to previous chemotherapy (ATTRACTION-3): a multicentre, randomised, open-label, phase 3 trial. Lancet Oncol. 2019;20(11):1506-1517."
    doi: "10.1016/S1470-2045(19)30626-6"
    pmid: "31582355"
    url: "https://doi.org/10.1016/S1470-2045(19)30626-6"
cross_links:
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "NFE2L2/NRF2 gain-of-function mutations in ~15% of ESCC; NRF2 activation → chemotherapy/platinum resistance; may predict IO benefit via altered immune microenvironment; KEAP1 loss also activates NRF2; no approved targeted NRF2 inhibitor for esophageal."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Nivolumab + cisplatin/5-FU (CheckMate 648: OS 13.2 vs 10.7 months, CPS≥1; FDA 2022) and pembrolizumab + chemo (KEYNOTE-590) are first-line for ESCC; nivolumab monotherapy (ATTRACTION-3: OS 10.9 vs 8.4 months) is second-line; PD-L1 CPS≥10 enriches benefit."
  - target: 01-human/03-molecular/her2
    relation: connects-to
    note: "HER2 overexpression in ~15-20% of EAC; trastuzumab + cisplatin/5-FU (ToGA: OS 13.8 vs 11.1 months, FDA 2010) first-line; trastuzumab deruxtecan (T-DXd, DESTINY-Gastric02) for HER2+ 2nd-line; pembrolizumab+trastuzumab+chemo (KEYNOTE-811) also approved."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Ramucirumab (VEGFR2 monoclonal) + paclitaxel is second-line standard for gastric/GEJ/EAC (REGARD, RAINBOW trials); bevacizumab studied but not approved for esophageal; VEGF overexpression common in ESCC (~40%) and EAC; angiogenesis contributes to poor prognosis."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "EGFR overexpression in ~70% of ESCC; EGFR amplification in ~10%; cetuximab (anti-EGFR) failed in unselected ESCC (SCOPE1, REAL3); anti-EGFR combinations being re-examined in EGFR-amplified ESCC; afatinib (pan-HER) showed modest activity in EGFR-overexpressing ESCC."
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "FGFR2 amplification in ~5% of EAC/GEJ tumors; FGFR1 amplification in ~3-5% of ESCC; pemigatinib and futibatinib (FGFR2 inhibitors) explored in FGFR2-amplified EAC/GEJ; selective FGFR2 inhibitors showed ORR ~25% in FGFR2-amplified GEJ (FIGHT-101 trial)."
  - target: 01-human/07-system/gastric-cancer
    relation: connects-to
    note: "EAC and gastric cancer share molecular features (HER2 amplification, MSI, VEGFR2); GEJ tumors classified/treated as both esophageal and gastric; ToGA regimen (trastuzumab+cisplatin/5-FU) applies to HER2+ GEJ and gastric; nivolumab (CheckMate 649) approved for gastric/GEJ."
  - target: 01-human/07-system/hnscc
    relation: connects-to
    note: "Esophageal and head-and-neck squamous cell carcinomas share field cancerization from alcohol and tobacco: the whole aerodigestive squamous mucosa is mutagenized, so these cancers co-occur as second primaries, and both are TP53-driven tumors responsive to PD-1 blockade."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "Esophageal adenocarcinoma blends into gastric cancer at the gastroesophageal junction, where Siewert-classified tumors are managed as one disease; chronic reflux drives Barrett metaplasia of the lower esophagus into adenocarcinoma, while the upper esophagus gives squamous cancer."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Both esophageal squamous and adenocarcinoma are immunotherapy-responsive: anti-PD-1 (nivolumab, pembrolizumab) reactivating cytotoxic CD8+ T cells is first-line with chemotherapy (CheckMate 648, KEYNOTE-590) and adjuvant after chemoradiation (CheckMate 577), per PD-L1 CPS."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Obesity drives the rising incidence of esophageal adenocarcinoma: central adiposity promotes gastroesophageal reflux and metabolic inflammation → Barrett's metaplasia of the lower esophagus → adenocarcinoma; this contrasts with the squamous type tied to smoking and alcohol."
  - target: 01-human/07-system/alcohol-use-disorder
    relation: connects-to
    note: "Alcohol is a primary cause of esophageal squamous cell carcinoma: acetaldehyde is a direct carcinogen (especially with ALDH2-deficiency flushing), synergizing strongly with tobacco; this contrasts with esophageal adenocarcinoma, which is driven instead by reflux and obesity."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Tobacco smoke is a shared carcinogen for both esophageal cancer types: its carbon-based polycyclic aromatic hydrocarbons and nitrosamines damage esophageal DNA, raising risk of squamous cell carcinoma (with alcohol) and, to a lesser degree, adenocarcinoma; cessation lowers risk."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "Esophageal and pancreatic cancers are both lethal GI adenocarcinomas usually caught late: each tends to present with advanced disease and dismal survival, shares risk from smoking and obesity, and depends on chemoradiation or chemotherapy since surgical cure is the exception."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "Esophageal and colorectal cancers illustrate the metaplasia-dysplasia-carcinoma sequence: chronic injury (reflux/Barrett's vs adenoma) drives stepwise mutation toward adenocarcinoma, and both are screened endoscopically to catch precursor lesions before invasion."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photon radiotherapy is central to esophageal cancer: chemoradiation can be definitive for squamous tumors or neoadjuvant before surgery for adenocarcinoma, exploiting the tumor's radiosensitivity while sparing heart and lung—a mainstay where surgery alone often fails."
  - target: 02-pathogen/02-bacteria/helicobacter-pylori
    relation: connects-to
    note: "Helicobacter pylori has a paradoxical link to esophageal cancer: by causing atrophic gastritis that lowers stomach acid, H. pylori reduces reflux and protects against esophageal adenocarcinoma—so its decline in wealthy countries partly explains that cancer's rise."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 mutation is an early, near-universal driver of esophageal cancer: loss of p53 occurs in Barrett's progression to adenocarcinoma and in most squamous tumors, letting damaged cells evade death—so p53 status tracks malignant transformation in the esophagus."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Esophageal cancer threatens the lung directly: the esophagus lies against the airway, so tumors can erode into the trachea forming a tracheoesophageal fistula, and aspiration and lung metastases are common—linking esophageal disease to fatal respiratory complications."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Esophageal cancer is a lethal cancer of the upper digestive system: it blocks the swallowing tube, so progressive dysphagia and weight loss are the hallmark, and because symptoms appear late it is usually advanced at diagnosis—often beyond cure."
  - target: 02-pathogen/01-viruses/hpv-16
    relation: connects-to
    note: "HPV may contribute to some esophageal cancers: the same high-risk types that cause cervical and oropharyngeal cancer are detected in a subset of esophageal squamous-cell carcinomas, though tobacco, alcohol and reflux remain the dominant drivers."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Esophageal cancer spreads early through the lymphatic system: the esophagus has a rich submucosal lymphatic network, so tumors seed regional nodes even when shallow, which is why nodal involvement heavily shapes staging and the dismal prognosis."
  - target: 01-human/07-system/iron-deficiency-anemia
    relation: connects-to
    note: "Iron-deficiency anemia can precede esophageal cancer: in Plummer-Vinson syndrome, chronic iron deficiency forms esophageal webs and raises the risk of squamous cell carcinoma, so dysphagia with anemia warrants endoscopy to catch early disease."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver is a common esophageal cancer metastasis site: hematogenous spread seeds the liver in advanced disease, marking incurable stage IV cancer, so liver imaging is part of staging that shifts treatment from surgery to systemic therapy."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "Esophageal smooth muscle ties to cancer risk: achalasia—failure of the smooth-muscle lower sphincter to relax—causes food stasis and chronic irritation that raises squamous cell carcinoma risk decades later, so long-standing achalasia needs surveillance."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "Esophageal cancer often begins by losing CDKN2A (p16): inactivating this tumor suppressor is an early step as Barrett's esophagus progresses toward adenocarcinoma and in squamous tumors, releasing the cell-cycle brake before other mutations pile on."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Esophageal cancer recruits cancer-associated fibroblasts: they build the dense desmoplastic stroma around the tumor and secrete factors that promote invasion and resistance, making the fibroblast-rich microenvironment a driver of aggressive behavior."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Esophageal tumors evade immunity with regulatory T cells: Tregs accumulate and suppress the cytotoxic response, dampening the anti-tumor attack that PD-1 checkpoint therapy—now standard in esophageal cancer—aims to reawaken."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "Nitrogen-based nitrosamines are key esophageal carcinogens: found in preserved, pickled and smoked foods common in high-incidence regions, these DNA-damaging compounds drive squamous esophageal cancer, a dietary risk distinct from smoking and alcohol."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Chronic reflux drives esophageal cancer through NF-kB: acid and bile injury keep this inflammatory switch active in the lining, fueling the Barrett's metaplasia and survival signaling that progress toward adenocarcinoma."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Tumor-associated macrophages help esophageal cancer spread: drawn into the stroma, they secrete factors that promote invasion, angiogenesis and immune suppression, supporting a tumor already hard to treat once it grows beyond the wall."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron deficiency can seed esophageal cancer: chronic lack of iron causes Plummer-Vinson webs in the upper esophagus, a recognized precursor to squamous cell carcinoma, so the metal's absence raises cancer risk."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Esophageal cancer chokes the gullet with fibrosis: the tumor's dense desmoplastic stroma and the scarring from radiation stiffen and narrow the esophagus, worsening the dysphagia that defines the disease."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Esophageal cancer recruits endothelial cells to grow: VEGF from the tumor drives these vessel-lining cells to build new blood supply, fueling invasion and spread of an already aggressive cancer."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc deficiency is linked to esophageal squamous cancer: common in the high-incidence 'esophageal cancer belt,' low zinc impairs the lining's defense and repair, raising the risk of malignancy."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "Esophageal adenocarcinoma grows from gut-type lining: chronic acid reflux turns the esophageal squamous epithelium into intestinal-type epithelium (Barrett's), the metaplastic step that precedes the cancer."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Natural killer cells help police esophageal cancer: their innate killing of tumor cells shapes outcome, and reviving their dampened activity is part of the immunotherapy that now extends survival."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy separates the two esophageal cancers: squamous cell carcinoma keeps desmosomes and keratin bundles, while adenocarcinoma arising from Barrett's metaplasia forms mucin-filled glands with microvilli."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Esophageal cancer reaches the skeleton late: after seeding the liver and lungs, advanced disease metastasizes to the marrow-bearing bones, painful deposits that mark its widespread, incurable stage."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "The colon can rebuild a lost esophagus: when surgery removes the cancerous esophagus, a segment of large intestine is sometimes transposed into the chest as a conduit to restore the path from mouth to stomach."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "The cancer and its cure both strike nerves: a tumor near the upper esophagus invades the recurrent laryngeal nerve into hoarseness, while the cisplatin of chemoradiation injures peripheral sensory neurons."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies now target esophageal cancer: trastuzumab against HER2 in adenocarcinomas, and the checkpoint antibodies pembrolizumab and nivolumab, add immunotherapy to the chemoradiation backbone."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Esophageal cancer bleeds and starves: chronic oozing from the tumor and the dysphagia that blocks eating leave patients iron-deficient and anemic, the low red cells compounding the weight loss it causes."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "The tumor and its treatment sit on the heart: a mid-esophageal cancer lies against the heart and great vessels, so the radiation that treats it irradiates the myocardium and the major esophagectomy that removes it carries real cardiac risk."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "NOTCH1 is a frequent casualty in esophageal squamous cancer: inactivating NOTCH1 mutations are among its commonest events, removing a brake on squamous-cell growth — one of the genetic hallmarks separating it from the lower-esophagus adenocarcinoma."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Esophageal cancer runs the clotting risk hot: like other gastrointestinal tumors it drives paraneoplastic thrombocytosis and a high rate of venous thromboembolism, complicating the chemotherapy and major surgery its treatment requires."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Cyclin D1 pushes the squamous tumor's cycle: CCND1 amplification is among the commonest events in esophageal squamous-cell carcinoma, releasing the G1 checkpoint to drive the rapid proliferation of the cancer."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Tumor-driving inflammation shows in the blood: esophageal cancer recruits neutrophils that promote invasion and angiogenesis, and a high neutrophil-to-lymphocyte ratio is a marker of worse prognosis."
  - target: 01-human/07-system/systemic-sclerosis
    relation: connects-to
    note: "Scleroderma scars the esophagus into cancer risk: systemic sclerosis paralyzes the lower esophagus, and the relentless reflux that follows drives Barrett's metaplasia and a raised risk of adenocarcinoma."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K signaling drives the esophageal tumor: PIK3CA mutation and amplification are recurrent in both squamous and adenocarcinoma, switching on the AKT-mTOR growth pathway and offering a targetable vulnerability."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells set the immunotherapy stage: their antigen presentation shapes the T-cell response esophageal cancer must evade, and their dysfunction underlies the immune escape that PD-1 blockade aims to reverse."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Surgery and obstruction open the door to sepsis: aspiration past an obstructing tumor and anastomotic leak after esophagectomy can seed mediastinitis and bloodstream infection, a leading cause of post-operative death."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "Chronic reflux and inflammation drive STAT3: IL-6-fueled STAT3 signaling promotes the survival and proliferation of esophageal cells along the Barrett's-to-adenocarcinoma path, tying inflammation to the cancer."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "A cancer and an operation that both clot: esophageal cancer's hypercoagulability plus the long, complex esophagectomy make venous thromboembolism a major perioperative and disease-related risk."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Chronic bleeding and inflammation drain the blood: beyond the iron loss of tumor bleeding, the inflammatory cytokines of esophageal cancer suppress erythropoiesis, adding an anemia of chronic disease that weakens patients before surgery."
  - target: 02-pathogen/03-fungi/candida-albicans
    relation: connects-to
    note: "The obstructed, stented esophagus invites the yeast: tumor narrowing, stents and the malnutrition and immunosuppression of esophageal cancer favor Candida esophagitis, worsening the dysphagia the cancer already causes."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Its chemo and poor intake strain the kidney: the cisplatin central to esophageal-cancer chemoradiation is nephrotoxic, and obstruction-driven dehydration adds prerenal injury, together threatening chronic kidney disease."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Losing the ability to eat weighs heavily: progressive dysphagia, weight loss, dependence on feeding tubes and a poor prognosis give esophageal cancer a substantial burden of depression."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Tumor and chemo injure the nerves: the cisplatin and taxane chemotherapy for esophageal cancer causes peripheral neuropathy, and tumor invasion of mediastinal nerves adds neuropathic pain."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Its therapy can wound the heart: the 5-fluorouracil used for esophageal cancer can provoke coronary vasospasm and cardiotoxicity, and adjacent thoracic radiation damages the heart, risking heart failure."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Chemoradiation opens the lung to mold: the neutropenia from esophageal-cancer chemoradiation, plus aspiration through a compromised swallow, can let inhaled Aspergillus invade as pulmonary aspergillosis."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Oesophagectomy is among the highest-risk surgeries: rebuilding the swallowing tube after removing the oesophagus leaves a chest anastomosis notorious for leak and slow, complicated healing."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It opens onto the airway: oesophageal cancer can erode into the trachea forming a tracheo-oesophageal fistula, causes aspiration through a failing swallow, and frequently brings pulmonary complications."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Choking dysphagia and grim odds breed worry: the progressive difficulty swallowing, weight loss and poor prognosis of oesophageal cancer foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "It can erode into the great vessels: locally invasive oesophageal cancer can create a catastrophic aorto-oesophageal fistula with massive haemorrhage, or invade the pericardium."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It silences the voice: tumour invasion of the recurrent laryngeal nerve causes hoarseness, a clinical sign of mediastinal spread of oesophageal cancer."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It can raise the blood calcium: squamous-cell oesophageal cancer can secrete parathyroid-hormone-related peptide, causing paraneoplastic hypercalcaemia."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Immunotherapy now treats it: PD-1 checkpoint inhibitors are used in advanced and adjuvant oesophageal cancer, while chronic reflux-driven inflammation underlies the adenocarcinoma."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "The skin can flag it: the hereditary palmoplantar keratoderma tylosis (Howel-Evans) strongly predisposes to oesophageal squamous-cell cancer, and paraneoplastic acanthosis nigricans can appear."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It links to muscle and bone: oesophageal cancer can present with paraneoplastic dermatomyositis, and advanced disease metastasises to the skeleton."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Immunotherapy now treats it: PD-1 inhibitors (nivolumab, pembrolizumab) are used adjuvantly after chemoradiation and for advanced oesophageal and gastro-oesophageal cancer."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Chemoradiation is the backbone: platinum and fluoropyrimidine chemotherapy with radiation (the CROSS regimen) precedes surgery for resectable oesophageal cancer."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Molecular subsets gain drugs: HER2-positive oesophageal adenocarcinoma responds to trastuzumab, and FGFR and other targets are emerging in this hard-to-treat cancer."
  - target: 01-human/07-system/nsclc
    relation: connects-to
    note: "Smoking links them in the chest: oesophageal squamous-cell carcinoma and lung cancer share tobacco and alcohol carcinogenesis and mediastinal proximity, so they co-occur and invade across the chest cavity."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "It invades mediastinal nerves: oesophageal cancer can engulf the recurrent laryngeal nerve, causing hoarseness, and infiltrate other mediastinal nerves — local nerve invasion marking unresectable disease."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "It spreads to the skeleton: advanced oesophageal cancer metastasises to bone as painful osteolytic lesions, one of the distant sites — with liver and lung — that mark incurable disease."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Airway erosion and aspiration: oesophageal cancer can erode into the trachea, forming a tracheo-oesophageal fistula that floods the alveoli with saliva and food, causing recurrent aspiration pneumonia."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Immunotherapy and the immune microenvironment: oesophageal squamous carcinoma can harbour tertiary lymphoid structures with germinal-centre activity, and checkpoint inhibitors now extend survival in advanced disease."
  - target: 01-human/07-system/bladder-cancer
    relation: connects-to
    note: "Smoking's shared field: tobacco and alcohol drive oesophageal squamous cancer, and the same carcinogens raise the risk of bladder cancer—a field effect across smoke-exposed epithelia."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Liver as a metastatic site: oesophageal cancer spreads to the liver, seeding the hepatic lobules, a common site of distant metastasis that marks incurable disease."
  - target: 01-human/07-system/copd
    relation: connects-to
    note: "Shared smoking carcinogenesis: oesophageal squamous cancer and COPD both arise from tobacco and shared field injury, and COPD's hypoxia and frailty worsen surgical and chemoradiation outcomes."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Radiation's cardiac cost: chemoradiation for oesophageal cancer irradiates the adjacent heart, causing late myocardial fibrosis, coronary disease and cardiomyopathy of the myocardium."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "MYC amplification: gains of MYC are common in both oesophageal adenocarcinoma and squamous cell carcinoma, driving the proliferation of these aggressive tumours."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "RAS in adenocarcinoma: KRAS mutation and amplification arise in oesophageal and gastro-oesophageal junction adenocarcinoma, activating MAPK signalling that fuels growth."
  - target: 01-human/03-molecular/yap1
    relation: connects-to
    note: "Hippo amplicon: YAP1 amplification on 11q22 is a recurrent driver of oesophageal squamous cell carcinoma, an oncogenic Hippo-pathway lesion promoting tumour growth."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K/AKT growth: PIK3CA mutation activates AKT in oesophageal cancer, driving survival and proliferation and contributing to resistance to chemoradiotherapy."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Tumour hypoxia: HIF-1α stabilised in hypoxic oesophageal tumours drives angiogenesis and an invasive, treatment-resistant phenotype linked to poor prognosis."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Epigenetic driver: EZH2 overexpression silences tumour-suppressor genes in oesophageal cancer, promoting proliferation and invasion as a candidate therapeutic target."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Telomerase immortalisation: TERT reactivation maintains telomeres in oesophageal cancer cells, granting the limitless replicative capacity that complements its p53 and cell-cycle lesions."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "EMT and stroma: TGF-beta drives epithelial-mesenchymal transition and a desmoplastic, immunosuppressive stroma in oesophageal cancer, promoting the invasion and spread of advanced disease."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Macrophage recruitment: CCL2 draws tumour-associated macrophages into the oesophageal cancer microenvironment, supporting angiogenesis and immune evasion in this aggressive cancer."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Reflux inflammation: chronic IL-6/STAT3 inflammation from gastro-oesophageal reflux and Barrett's oesophagus drives the metaplasia-dysplasia-carcinoma sequence behind oesophageal adenocarcinoma."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Nodal metastasis: CXCR4 on oesophageal cancer cells follows CXCL12 gradients to lymph nodes and distant organs, driving the early nodal spread that makes the cancer so often incurable at diagnosis."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Mutational immunogenicity: the high tobacco- and reflux-driven mutational burden of oesophageal cancer generates cytosolic DNA and neoantigens that engage cGAS-STING, underlying its responsiveness to checkpoint inhibitors."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Bile-acid reflux: chronic reflux of acid and bile acids, which derive from cholesterol, into the lower oesophagus drives the Barrett's metaplasia-dysplasia sequence behind oesophageal adenocarcinoma, the histology rising sharply in Western countries."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Chemoradiation apoptosis: neoadjuvant chemoradiation and perioperative chemotherapy kill oesophageal-cancer cells through caspase-3-mediated apoptosis, the cytotoxic backbone whose effect on the primary tumour predicts surgical outcome."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Obesity-driven risk: central obesity raises both mechanical reflux and leptin, which promotes oesophageal epithelial proliferation, two ways the obesity epidemic drives the rising incidence of oesophageal adenocarcinoma."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "MAPK convergence: EGFR, HER2, KRAS and FGFR (all already mapped) funnel into the MAPK-ERK cascade, the proliferative hub driving both squamous-cell and adenocarcinoma forms of oesophageal cancer."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Growth axis: mTOR completes the PI3K-AKT-mTOR pathway (PIK3CA and AKT already mapped) that sustains growth and survival signalling in oesophageal carcinoma."
  - target: 01-human/03-molecular/cdh1
    relation: connects-to
    note: "EMT and invasion: loss of E-cadherin during epithelial-mesenchymal transition releases oesophageal-carcinoma cells from their junctions, enabling the invasion and nodal spread that worsen prognosis."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Reflux-driven inflammation: chronic reflux- and inflammation-driven TLR-MyD88-NF-κB signalling (NF-κB already mapped) promotes the Barrett's-metaplasia-to-adenocarcinoma sequence of oesophageal cancer."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Inflammatory microenvironment: IL-6 signalling through JAK-STAT3 (IL-6 and STAT3 already mapped) sustains the inflammatory, pro-tumorigenic microenvironment of oesophageal cancer."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Cell-cycle restraint: the RB1-E2F checkpoint (CDKN2A and cyclin-D1 already mapped) restrains cell-cycle entry, and its disruption contributes to the proliferation of oesophageal cancer."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD4 signalling (TGF-β mapped) is a context-dependent tumour suppressor whose loss promotes progression in oesophageal cancer, particularly the Barrett-adenocarcinoma sequence."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 promotes invasion and immune evasion in oesophageal cancer."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "Loss of PTEN restraint on PI3K-AKT-mTOR signalling (AKT, PIK3CA and mTOR mapped) drives proliferation and survival in oesophageal cancer."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the antitumour immune response of oesophageal cancer, relevant to its checkpoint immunotherapy."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6-cyclin-D activity (cyclin-D1, CDKN2A and RB1 already mapped) drives the cell-cycle progression of oesophageal cancer."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO tumour-suppressor activity, restrained by the PI3K-AKT axis, is lost in the proliferative progression of oesophageal cancer."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-delivered cytotoxic killing by CD8 T and NK cells mediates the immune clearance that the immunotherapy-treated esophageal cancer must evade."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the inflammatory, reflux- and Barrett's-associated microenvironment of esophageal cancer."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in esophageal cancer."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β regulates the Wnt/β-catenin and survival signaling of esophageal cancer."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of EGFR and HER2 (both already mapped) drives the invasion of esophageal cancer."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic silencing of tumor-suppressor genes in esophageal cancer."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of esophageal cancer."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival and therapy resistance of esophageal cancer cells."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the immunosuppressive microenvironment of esophageal cancer."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of esophageal cancer."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the reflux/Barrett's-linked inflammation and tumor microenvironment of esophageal cancer."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of esophageal cancer."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory tumor microenvironment of esophageal cancer."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory tumor microenvironment of esophageal cancer."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the tumor microenvironment and immune signaling of esophageal cancer."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Acid reflux carcinogenesis: chronic reflux of gastric acid (protons) drives Barrett's metaplasia and oesophageal adenocarcinoma, the mechanism linking GERD and obesity (leptin already mapped) to the rising incidence of the lower-oesophageal tumour."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immunotherapy: checkpoint inhibitors (PD-1 already mapped) are now standard in oesophageal cancer, and MHC class II antigen presentation shapes the T-cell response that determines benefit, especially in the squamous subtype."
  - target: 01-human/03-molecular/axl-receptor
    relation: connects-to
    note: "Invasion and resistance: the AXL receptor tyrosine kinase drives the epithelial-mesenchymal transition and treatment resistance of oesophageal cancer, a mechanism of progression beyond the HER2 and FGFR targets already mapped."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Dysphagia and bleeding: progressive dysphagia with weight loss is the hallmark presentation of oesophageal cancer, and chronic tumour bleeding lowers haemoglobin, the iron-deficiency anaemia that often prompts the diagnosis."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell immunity: IL-2-driven T-cell expansion (PD-1 and perforin already mapped) supports the anti-tumour response that checkpoint inhibitors unleash, now standard in oesophageal cancer, especially the squamous subtype."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative carcinogenesis: chronic reflux, alcohol and tobacco generate reactive oxygen species, to which xanthine oxidase contributes, and this oxidative DNA damage (NRF2 already mapped) drives the carcinogenesis of both oesophageal cancer subtypes."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "COX-2 and Barrett's: cyclooxygenase-2 and prostaglandin E2 rise in Barrett's oesophagus and the adenocarcinoma it precedes, promoting the inflammation and proliferation of carcinogenesis, and aspirin is studied for chemoprevention."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive microenvironment: IL-10 in the tumour microenvironment dampens the anti-tumour T-cell response (PD-1 and perforin already mapped), part of the immune escape that the checkpoint inhibitors now standard in oesophageal cancer aim to reverse."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Fistula and metastasis: locally advanced oesophageal cancer can erode into the airway to form a tracheo-oesophageal fistula, and the lung is a common site of the metastases of advanced disease."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises the tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the microenvironment the checkpoint inhibitors now standard in oesophageal cancer must overcome."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Desmoplastic stroma: the cancer-associated fibroblasts lay down the desmoplastic stroma (TGF-β already mapped) of oesophageal cancer, supporting the invasion and the treatment resistance of the tumour."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron-deficiency anaemia: the chronic occult bleeding of the oesophageal tumour and the dysphagia-related malnutrition cause the iron-deficiency anaemia (haemoglobin already mapped) common at presentation."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Obesity-adenocarcinoma adipokine: adiponectin, with leptin (already mapped), links the obesity (already mapped) that drives the oesophageal adenocarcinoma to the metabolic-inflammatory milieu of the tumour."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "M2 desmoplastic arm: IL-13, with IL-4 (already mapped), drives the M2 macrophage (already mapped) arm of the immunosuppressive desmoplastic (fibroblast already mapped) stroma of oesophageal cancer."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the obesity-associated oesophageal adenocarcinoma."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Selenium-deficiency risk: the dietary selenium deficiency (the Linxian region) is a risk factor for the oesophageal squamous-cell carcinoma, the antioxidant selenoprotein protection being chemopreventive."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "GI-bleed anaemia: the chronic tumour blood loss and the inflammation (IL-6 already mapped)-driven hepcidin produce the iron-restricted anaemia (haemoglobin already mapped) of oesophageal cancer."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate antitumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune tumour microenvironment relevant to the immunotherapy of oesophageal cancer."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity, exploited by the checkpoint (PD-1 already mapped) immunotherapy of oesophageal cancer."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of oesophageal cancer."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of oesophageal cancer."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the tumour-promoting inflammation of oesophageal cancer."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the oesophageal-cancer microenvironment."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of oesophageal cancer."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of oesophageal cancer."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, associates with the nivolumab (PD-1 already mapped) immunotherapy response of oesophageal cancer."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the oesophageal-cancer stroma."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) contribute to the inflammatory dimension of the oesophageal-cancer microenvironment."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement evasion: the oesophageal-cancer cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), tempering the complement attack within the tumour stroma."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Haemorrhage/tumour iron: transferrin, the iron carrier, reflects the iron demand of the tumour and the iron-deficiency anaemia of the chronic blood loss of oesophageal cancer."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-oesophageal axis: TSLP, from the Barrett's-epithelium and the oesophageal tumour stroma, primes dendritic cells (already mapped) and mast cells (already mapped), amplifying the Th2 immunosuppressive microenvironment of oesophageal cancer."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-oesophageal axis: bradykinin, via B1/B2 receptors on tumour endothelium (already mapped) and mast cells (already mapped), augments the vascular permeability, tumour oedema, and the pro-inflammatory stromal milieu of oesophageal cancer."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "EPO-oesophageal axis: erythropoietin, induced by the HIF-1α (already mapped) hypoxia and anaemia of oesophageal cancer, activates the EPOR on tumour cells (already mapped) and modulates macrophage (already mapped) polarisation in the tumour microenvironment."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Histamine-oesophageal axis: histamine, released by mast cells in the Barrett's-oesophagus and oesophageal-tumour stroma, signals via H1/H2 receptors on tumour cells and endothelium, modulating angiogenesis, immune evasion, and the pro-tumourigenic milieu of oesophageal cancer."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Melatonin-oesophageal axis: melatonin, produced by enterochromaffin cells in the oesophageal mucosa, suppresses acid-reflux-driven oxidative stress, limits Barrett's-oesophagus progression, and enhances apoptotic sensitivity in oesophageal-cancer cells."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Androgen-oesophageal axis: testosterone, via androgen receptor signalling on oesophageal squamous and adenocarcinoma cells, modulates tumour proliferation, immune evasion, and the well-established male sex bias in oesophageal-cancer incidence and mortality."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "EC prolactin: prolactin, via PRLR on macrophages (already mapped) and mast cells (already mapped), modulates the immune TME; hyperprolactinaemia amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of esophageal cancer."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "EC oxytocin: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates tumour-promoting inflammation; oxytocin deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of esophageal cancer."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "EC vasopressin: vasopressin, via V1aR on macrophages (already mapped) and mast cells (already mapped), modulates the TME; vasopressin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of esophageal cancer."
---

# Esophageal Cancer

## Overview

**Esophageal cancer** is the seventh most common cancer worldwide and sixth leading cause of cancer mortality (~600,000 deaths/year globally), with striking geographic heterogeneity and two biologically distinct histological subtypes: **esophageal squamous cell carcinoma (ESCC)** and **esophageal adenocarcinoma (EAC)**. ESCC predominates globally (~85% worldwide) and is especially common in the **"esophageal cancer belt"** spanning Iran, Central Asian countries, and China's Taihang Mountain corridor, where environmental factors (hot tea drinking, nutritional deficiencies, aflatoxin, tobacco) conspire with genetic susceptibility. EAC predominates in Western countries (~70% of USA cases) and arises from **Barrett's esophagus** — intestinal metaplasia of the lower esophagus driven by chronic gastroesophageal reflux disease (GERD). Both subtypes are treated with platinum/fluoropyrimidine-based chemotherapy, but molecular profiling has revealed distinct targetable alterations: **NFE2L2/KEAP1** in ESCC; **HER2 amplification (~15-20%)** and **FGFR2** in EAC. The addition of immunotherapy (PD-1/PD-L1 blockade) to first-line chemotherapy has become standard for advanced ESCC [^doki-2022-checkmate648] [^kato-2019-attraction3].

**Epidemiology:**
- Global: ~600,000 deaths/year; ESCC dominant globally (China, Iran, Sub-Saharan Africa, Eastern Africa); EAC dominant in USA, UK, Australia, Northern Europe
- USA: ~22,000 new cases/year; ~16,000 deaths/year; EAC ~70%, ESCC ~30%; 5-year OS ~20%
- ESCC risk factors: Cigarette smoking (RR ~4-8), alcohol (synergistic with tobacco; RR ~5 for heavy use), hot beverage consumption (>65°C), low intake of fruits/vegetables, nutritional deficiencies (retinol/β-carotene, zinc, selenium), HPV in a subset (~20% in high-incidence regions), tylosis (keratoderma palmoplantaris, RHBDF2 germline mutations → near 100% ESCC lifetime risk)
- EAC risk factors: Chronic GERD (OR ~5-6 for frequent/severe GERD → Barrett's → EAC), obesity/central adiposity (OR ~2-3 per 5 kg/m² BMI increase), smoking (~1.5-fold increased risk), H. pylori negative (paradoxically — H. pylori reduces GERD and is protective for EAC), male sex (male:female 8:1 for EAC)

**Molecular landscape by subtype:**

*ESCC-specific alterations:*
- TP53 mutations: ~90%
- NFE2L2 gain-of-function: ~15%; KEAP1 loss: ~5%
- PIK3CA: ~15%
- CDKN2A deletion/methylation: ~45%
- SOX2, TP63 amplification: ~15-30% (squamous lineage TFs)
- FGFR1 amplification: ~20%
- EGFR overexpression/amplification: ~30%
- CCND1 amplification: ~25%

*EAC-specific alterations:*
- TP53 mutations: ~65%
- CDKN2A deletion: ~35%
- ERBB2 (HER2) amplification: ~15-20%
- FGFR2 amplification: ~7%
- EGFR amplification: ~8%
- KRAS amplification: ~5%
- MYC amplification: ~10%
- Chromosomal instability (CIN): Very high in EAC (50+ chromosomal copy number changes/tumor); mutational signatures: SBS17 (5-FU-related), SBS2/13 (APOBEC)

## Structure

### Barrett's esophagus and EAC carcinogenesis

**Barrett's esophagus (BE):**
Replacement of normal stratified squamous esophageal epithelium with specialized intestinal metaplasia (SIM: columnar epithelium with goblet cells) in the distal esophagus in response to chronic acid (HCl) and bile reflux injury. BE affects ~5-6% of adults with GERD symptoms and ~2% of the general population. Annual risk of EAC from non-dysplastic BE: ~0.3-0.5%/year; low-grade dysplasia (LGD): ~0.7%/year; high-grade dysplasia (HGD): ~7-10%/year → ablation or resection. Barrett's surveillance: Upper endoscopy with 4-quadrant biopsies q2 cm (Seattle protocol) every 3-5 years for non-dysplastic BE, every 6-12 months for LGD, q3 months for confirmed HGD.

**Molecular progression of BE → EAC:**
TP53 mutation (early; present in ~65% of BE with HGD) → CDKN2A loss (methylation/deletion) → telomere dysfunction → chromosomal instability → amplification of 8q24 (MYC), 17q12 (HER2), 7p12 (EGFR) → KRAS activation → EAC. This mutational timeline (TP53 → CIN → amplifications) differs from ESCC (squamous field cancerization, TF amplification).

### ESCC tumor biology and NFE2L2/KEAP1

**Squamous field cancerization:**
ESCC arises in a background of diffuse squamous dysplasia throughout the esophagus (analogous to oral/oropharyngeal and lung squamous field cancerization from tobacco/alcohol); TP53 mutations are early events; NFE2L2, PIK3CA, NOTCH1 mutations follow; chromosomal instability occurs later; multisite ESCC (synchronous primary tumors) in ~5% — a challenge for staging and treatment.

**NFE2L2 mutations in ESCC:**
E79K hotspot (most common in ESCC) alters the Neh2-ETGE motif → impaired KEAP1 binding → constitutive NRF2 nuclear translocation → antioxidant target gene upregulation (SLC7A11, HO-1, NQO1, GCLC, GPX2) → resistance to cisplatin + 5-FU → platinum-containing regimens have reduced efficacy in NFE2L2-mutant ESCC; molecular testing for NFE2L2 mutations may inform first-line chemotherapy vs. immunotherapy selection.

**ESCC tumor microenvironment:**
- PD-L1: Expressed in ~30-45% of ESCC tumors (CPS ≥1); CPS ≥10 enriched for PD-1 immunotherapy benefit; expression driven by IFN-γ from CD8+ TILs and JAK-STAT signaling
- Mismatch repair (MMR) deficiency: ~2% of ESCC; pembrolizumab tumor-agnostic approved
- TMB-high (≥10 mutations/Mb): ~10-15% of ESCC

## Function

### Normal esophageal epithelium

The esophagus is lined by non-keratinizing stratified squamous epithelium from cricoid cartilage to the Z-line (squamocolumnar junction, SCJ) at the gastroesophageal junction; columnar gastric epithelium begins in the stomach. Physiological roles: Mechanical protection (stratified squamous withstands abrasion from food bolus); peristaltic transport (striated muscle in upper third, smooth muscle in lower two-thirds, coordinated by enteric/vagal input); lower esophageal sphincter (LES) prevents reflux (tone maintained by myogenic activity + gastrin/cholecystokinin hormones). Normal renewal: Stratified squamous epithelium turns over every 7-14 days from basal stem cells expressing TP63 and KRT5/14.

## Pathology

### Diagnosis and staging

**Clinical presentation:**
- Dysphagia (progressive solid then liquid): Cardinal symptom (~90% of presenting patients); indicates >50% luminal obstruction
- Odynophagia, weight loss, anorexia (systemic)
- Hematemesis or melena: Advanced or ulcerated tumor
- Voice hoarseness: Recurrent laryngeal nerve invasion (left RLN courses around aortic arch → locoregionally advanced ESCC)
- Horner's syndrome, pleural effusion, respiratory-GI fistula: T4b disease

**Staging workup:**
- Upper endoscopy (EGD) + biopsy: Endoscopic appearance; biopsy for histology; chromoendoscopy (Lugol's iodine for ESCC: normal squamous = brown, dysplastic = unstained "Lugol-voiding")
- CT chest/abdomen/pelvis: Locoregional extension, lung/liver/adrenal mets
- PET/CT: Mediastinal nodes, distant mets
- Endoscopic ultrasound (EUS): T and N staging; most accurate for depth of invasion (T1-T4); EUS-guided FNA of suspicious nodes
- Bronchoscopy: Upper/mid ESCC ≥26 cm from incisors → tracheobronchomal fistula risk assessment; biopsy subcarinal nodes
- MRI brain: Not routine unless neurological symptoms

**AJCC 8th staging:**
T1a: Lamina propria/muscularis mucosae; T1b: Submucosa; T2: Muscularis propria; T3: Adventitia; T4a: Resectable adjacent structures (pleura, pericardium, azygos, diaphragm, peritoneum); T4b: Unresectable (aorta, vertebral body, trachea, adjacent organ). N1: 1-2 regional nodes; N2: 3-6; N3: ≥7. M1: Distant metastases. Clinical staging (cTNM) differs from pathological (pTNM).

**Molecular testing recommendations:**
- HER2 IHC/FISH: All locally advanced/metastatic EAC and GEJ adenocarcinoma; HER2 IHC 3+ or IHC 2+/FISH+ → targeted therapy
- PD-L1 CPS: ESCC and EAC; CPS ≥1, ≥10 thresholds used for drug selection
- MMR/MSI: All patients
- TMB: Optional; pembrolizumab tumor-agnostic for TMB-H ≥10 mutations/Mb
- NGS panel: NFE2L2, KEAP1, PIK3CA, FGFR1 (ESCC); HER2, FGFR2, KRAS, TP53 (EAC) — informs clinical trial eligibility

### Treatment by stage and subtype

**Localized resectable disease (T1b-T3 N0-N1, potentially T4a):**
- **Perioperative chemotherapy (EAC/GEJ):** FLOT regimen (docetaxel + oxaliplatin + 5-FU/leucovorin × 4 cycles pre + 4 cycles post-surgery): FLOT4 trial: OS 50 vs 35 months vs ECF (European perioperative standard); preferred for gastric/GEJ/EAC
- **Preoperative chemoradiation (ESCC and EAC):** CROSS trial (carboplatin + paclitaxel + 41.4 Gy): OS 49.4 vs 24.0 months for EAC (NEJM 2012); also active in ESCC; trimodality therapy (CRT + surgery) is standard for T2+ ESCC in USA
- **Definitive CRT (ESCC, unresectable/refused surgery):** Cisplatin/5-FU + 50.4 Gy; salvage surgery after CRT failure in selected centers
- **Adjuvant nivolumab (CheckMate 577):** After neoadjuvant CRT + R0 resection with ypN+ or ypT1+ residual disease: DFS 22.4 vs 11.0 months; FDA approved 2021; 1 year nivolumab maintenance post-surgery

**Advanced/Metastatic ESCC — First-line:**

**Nivolumab + cisplatin/5-FU or paclitaxel (CheckMate 648, FDA 2022):** [^doki-2022-checkmate648]
- 970 patients advanced ESCC; nivolumab 240 mg q2w + cisplatin 80 mg/m² q3w + 5-FU 800 mg/m²/day (d1-5)
- PD-L1 CPS ≥1 (72% of patients): OS 13.2 vs 10.7 months (HR 0.76); CPS ≥1 PFS: 6.9 vs 4.4 months
- All comers: OS 13.3 vs 10.0 months; all PFS 6.0 vs 4.4 months
- FDA approved nivolumab + chemo (CPS ≥1) AND nivolumab + ipilimumab (CPS ≥1: OS 13.7 vs 9.1 months, HR 0.64) as first-line for ESCC
- **Pembrolizumab + cisplatin/5-FU (KEYNOTE-590):** ESCC (CPS ≥10): OS 13.9 vs 8.8 months; all ESCC: OS 12.6 vs 9.8 months; FDA 2021

**Advanced/Metastatic EAC — First-line:**
- **Pembrolizumab + chemotherapy (KEYNOTE-590/KEYNOTE-811):** Pembrolizumab + 5-FU/cisplatin for EAC/GEJ; HER2-negative: pembrolizumab + FOLFOX or FP
- **HER2+ EAC:** Trastuzumab + cisplatin/5-FU (ToGA trial: OS 13.8 vs 11.1 months); add pembrolizumab (KEYNOTE-811 triplet: nivolumab/pembrolizumab + trastuzumab + chemo); T-DXd for 2nd-line HER2+ (DESTINY-Gastric01: ORR 51%)
- **Nivolumab + chemo (CheckMate 649 includes GEJ/EAC):** CPS ≥5: OS 14.4 vs 11.1 months; CPS ≥1: 13.8 vs 11.6 months

**Second-line (post-platinum ESCC):**

**Nivolumab monotherapy (ATTRACTION-3, FDA 2019):** [^kato-2019-attraction3]
- 419 platinum-refractory ESCC; nivolumab 240 mg q2w vs. investigator-choice (taxane or irinotecan)
- OS 10.9 vs 8.4 months (HR 0.77); PFS similar; ORR 19.3% vs 22.2%; duration of response longer with nivolumab
- FDA approved for all ESCC patients post-platinum regardless of PD-L1 status

**Pembrolizumab (KEYNOTE-181):** CPS ≥10: OS 10.3 vs 6.7 months; FDA approved for CPS ≥10 ESCC 2nd+ line.

**Ramucirumab (VEGFR2) + paclitaxel:** RAINBOW trial (gastric/GEJ) extended to EAC; OS 9.6 vs 7.4 months; FDA approved for gastric/GEJ including EAC 2nd-line.

**Salvage/3rd-line:**
- Irinotecan (ORR ~10-15%)
- TAS-102 (trifluridine/tipiracil): Early data in ESCC
- Clinical trial: FGFR1 inhibitors in FGFR1-amplified ESCC (futibatinib, infigratinib); NRF2 pathway inhibitors

**Endoscopic resection for early ESCC/EAC:**
- T1a (lamina propria): Endoscopic mucosal resection (EMR) or endoscopic submucosal dissection (ESD) → curative for T1a ESCC; recurrence risk <3%
- T1b (submucosa): ~35-50% lymph node metastasis risk → surgical esophagectomy or esophagectomy preferred; close follow-up post-EMR/ESD for T1b sm1 (superficial submucosa)
- Barrett's with HGD: RFA (radiofrequency ablation) or cryoablation after eradication of visible lesions by EMR

## Connections

- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — NFE2L2/NRF2 gain-of-function mutations in ~15% of ESCC; NRF2 activation → chemotherapy/platinum resistance; may predict IO benefit via altered immune microenvironment; KEAP1 loss also activates NRF2; no approved targeted NRF2 inhibitor for esophageal.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Nivolumab + cisplatin/5-FU (CheckMate 648: OS 13.2 vs 10.7 months, CPS≥1; FDA 2022) and pembrolizumab + chemo (KEYNOTE-590) are first-line for ESCC; nivolumab monotherapy (ATTRACTION-3: OS 10.9 vs 8.4 months) is second-line; PD-L1 CPS≥10 enriches benefit.
- `connects-to` → **[HER2](../../03-molecular/her2/README.md)** — HER2 overexpression in ~15-20% of EAC; trastuzumab + cisplatin/5-FU (ToGA: OS 13.8 vs 11.1 months, FDA 2010) first-line; trastuzumab deruxtecan (T-DXd, DESTINY-Gastric02) for HER2+ 2nd-line; pembrolizumab+trastuzumab+chemo (KEYNOTE-811) also approved.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Ramucirumab (VEGFR2 monoclonal) + paclitaxel is second-line standard for gastric/GEJ/EAC (REGARD, RAINBOW trials); bevacizumab studied but not approved for esophageal; VEGF overexpression common in ESCC (~40%) and EAC; angiogenesis contributes to poor prognosis.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — EGFR overexpression in ~70% of ESCC; EGFR amplification in ~10%; cetuximab (anti-EGFR) failed in unselected ESCC (SCOPE1, REAL3); anti-EGFR combinations being re-examined in EGFR-amplified ESCC; afatinib (pan-HER) showed modest activity in EGFR-overexpressing ESCC.
- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — FGFR2 amplification in ~5% of EAC/GEJ tumors; FGFR1 amplification in ~3-5% of ESCC; pemigatinib and futibatinib (FGFR2 inhibitors) explored in FGFR2-amplified EAC/GEJ; selective FGFR2 inhibitors showed ORR ~25% in FGFR2-amplified GEJ (FIGHT-101 trial).
- `connects-to` → **[Gastric Cancer](../gastric-cancer/README.md)** — EAC and gastric cancer share molecular features (HER2 amplification, MSI, VEGFR2); GEJ tumors classified/treated as both esophageal and gastric; ToGA regimen (trastuzumab+cisplatin/5-FU) applies to HER2+ GEJ and gastric; nivolumab (CheckMate 649) approved for gastric/GEJ.
- `connects-to` → **[HNSCC](../hnscc/README.md)** — Esophageal and head-and-neck squamous cell carcinomas share field cancerization from alcohol and tobacco: the whole aerodigestive squamous mucosa is mutagenized, so these cancers co-occur as second primaries, and both are TP53-driven tumors responsive to PD-1 blockade.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — Esophageal adenocarcinoma blends into gastric cancer at the gastroesophageal junction, where Siewert-classified tumors are managed as one disease; chronic reflux drives Barrett metaplasia of the lower esophagus into adenocarcinoma, while the upper esophagus gives squamous cancer.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Both esophageal squamous and adenocarcinoma are immunotherapy-responsive: anti-PD-1 (nivolumab, pembrolizumab) reactivating cytotoxic CD8+ T cells is first-line with chemotherapy (CheckMate 648, KEYNOTE-590) and adjuvant after chemoradiation (CheckMate 577), per PD-L1 CPS.
- `connects-to` → **[Obesity](../obesity/README.md)** — Obesity drives the rising incidence of esophageal adenocarcinoma: central adiposity promotes gastroesophageal reflux and metabolic inflammation → Barrett's metaplasia of the lower esophagus → adenocarcinoma; this contrasts with the squamous type tied to smoking and alcohol.
- `connects-to` → **[Alcohol Use Disorder](../alcohol-use-disorder/README.md)** — Alcohol is a primary cause of esophageal squamous cell carcinoma: acetaldehyde is a direct carcinogen (especially with ALDH2-deficiency flushing), synergizing strongly with tobacco; this contrasts with esophageal adenocarcinoma, which is driven instead by reflux and obesity.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Tobacco smoke is a shared carcinogen for both esophageal cancer types: its carbon-based polycyclic aromatic hydrocarbons and nitrosamines damage esophageal DNA, raising risk of squamous cell carcinoma (with alcohol) and, to a lesser degree, adenocarcinoma; cessation lowers risk.
- `connects-to` → **[Pancreatic Cancer](../pancreatic-cancer/README.md)** — Esophageal and pancreatic cancers are both lethal GI adenocarcinomas usually caught late: each tends to present with advanced disease and dismal survival, shares risk from smoking and obesity, and depends on chemoradiation or chemotherapy since surgical cure is the exception.
- `connects-to` → **[Colorectal Cancer](../colorectal-cancer/README.md)** — Esophageal and colorectal cancers illustrate the metaplasia-dysplasia-carcinoma sequence: chronic injury (reflux/Barrett's vs adenoma) drives stepwise mutation toward adenocarcinoma, and both are screened endoscopically to catch precursor lesions before invasion.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photon radiotherapy is central to esophageal cancer: chemoradiation can be definitive for squamous tumors or neoadjuvant before surgery for adenocarcinoma, exploiting the tumor's radiosensitivity while sparing heart and lung—a mainstay where surgery alone often fails.
- `connects-to` → **[Helicobacter pylori](../../../02-pathogen/02-bacteria/helicobacter-pylori/README.md)** — Helicobacter pylori has a paradoxical link to esophageal cancer: by causing atrophic gastritis that lowers stomach acid, H. pylori reduces reflux and protects against esophageal adenocarcinoma—so its decline in wealthy countries partly explains that cancer's rise.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 mutation is an early, near-universal driver of esophageal cancer: loss of p53 occurs in Barrett's progression to adenocarcinoma and in most squamous tumors, letting damaged cells evade death—so p53 status tracks malignant transformation in the esophagus.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Esophageal cancer threatens the lung directly: the esophagus lies against the airway, so tumors can erode into the trachea forming a tracheoesophageal fistula, and aspiration and lung metastases are common—linking esophageal disease to fatal respiratory complications.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Esophageal cancer is a lethal cancer of the upper digestive system: it blocks the swallowing tube, so progressive dysphagia and weight loss are the hallmark, and because symptoms appear late it is usually advanced at diagnosis—often beyond cure.
- `connects-to` → **[HPV-16](../../../02-pathogen/01-viruses/hpv-16/README.md)** — HPV may contribute to some esophageal cancers: the same high-risk types that cause cervical and oropharyngeal cancer are detected in a subset of esophageal squamous-cell carcinomas, though tobacco, alcohol and reflux remain the dominant drivers.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Esophageal cancer spreads early through the lymphatic system: the esophagus has a rich submucosal lymphatic network, so tumors seed regional nodes even when shallow, which is why nodal involvement heavily shapes staging and the dismal prognosis.
- `connects-to` → **[Iron Deficiency Anemia](../iron-deficiency-anemia/README.md)** — Iron-deficiency anemia can precede esophageal cancer: in Plummer-Vinson syndrome, chronic iron deficiency forms esophageal webs and raises the risk of squamous cell carcinoma, so dysphagia with anemia warrants endoscopy to catch early disease.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver is a common esophageal cancer metastasis site: hematogenous spread seeds the liver in advanced disease, marking incurable stage IV cancer, so liver imaging is part of staging that shifts treatment from surgery to systemic therapy.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — Esophageal smooth muscle ties to cancer risk: achalasia—failure of the smooth-muscle lower sphincter to relax—causes food stasis and chronic irritation that raises squamous cell carcinoma risk decades later, so long-standing achalasia needs surveillance.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — Esophageal cancer often begins by losing CDKN2A (p16): inactivating this tumor suppressor is an early step as Barrett's esophagus progresses toward adenocarcinoma and in squamous tumors, releasing the cell-cycle brake before other mutations pile on.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Esophageal cancer recruits cancer-associated fibroblasts: they build the dense desmoplastic stroma around the tumor and secrete factors that promote invasion and resistance, making the fibroblast-rich microenvironment a driver of aggressive behavior.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Esophageal tumors evade immunity with regulatory T cells: Tregs accumulate and suppress the cytotoxic response, dampening the anti-tumor attack that PD-1 checkpoint therapy—now standard in esophageal cancer—aims to reawaken.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — Nitrogen-based nitrosamines are key esophageal carcinogens: found in preserved, pickled and smoked foods common in high-incidence regions, these DNA-damaging compounds drive squamous esophageal cancer, a dietary risk distinct from smoking and alcohol.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Chronic reflux drives esophageal cancer through NF-kB: acid and bile injury keep this inflammatory switch active in the lining, fueling the Barrett's metaplasia and survival signaling that progress toward adenocarcinoma.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Tumor-associated macrophages help esophageal cancer spread: drawn into the stroma, they secrete factors that promote invasion, angiogenesis and immune suppression, supporting a tumor already hard to treat once it grows beyond the wall.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron deficiency can seed esophageal cancer: chronic lack of iron causes Plummer-Vinson webs in the upper esophagus, a recognized precursor to squamous cell carcinoma, so the metal's absence raises cancer risk.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Esophageal cancer chokes the gullet with fibrosis: the tumor's dense desmoplastic stroma and the scarring from radiation stiffen and narrow the esophagus, worsening the dysphagia that defines the disease.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Esophageal cancer recruits endothelial cells to grow: VEGF from the tumor drives these vessel-lining cells to build new blood supply, fueling invasion and spread of an already aggressive cancer.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc deficiency is linked to esophageal squamous cancer: common in the high-incidence 'esophageal cancer belt,' low zinc impairs the lining's defense and repair, raising the risk of malignancy.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — Esophageal adenocarcinoma grows from gut-type lining: chronic acid reflux turns the esophageal squamous epithelium into intestinal-type epithelium (Barrett's), the metaplastic step that precedes the cancer.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Natural killer cells help police esophageal cancer: their innate killing of tumor cells shapes outcome, and reviving their dampened activity is part of the immunotherapy that now extends survival.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy separates the two esophageal cancers: squamous cell carcinoma keeps desmosomes and keratin bundles, while adenocarcinoma arising from Barrett's metaplasia forms mucin-filled glands with microvilli.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Esophageal cancer reaches the skeleton late: after seeding the liver and lungs, advanced disease metastasizes to the marrow-bearing bones, painful deposits that mark its widespread, incurable stage.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — The colon can rebuild a lost esophagus: when surgery removes the cancerous esophagus, a segment of large intestine is sometimes transposed into the chest as a conduit to restore the path from mouth to stomach.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — The cancer and its cure both strike nerves: a tumor near the upper esophagus invades the recurrent laryngeal nerve into hoarseness, while the cisplatin of chemoradiation injures peripheral sensory neurons.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies now target esophageal cancer: trastuzumab against HER2 in adenocarcinomas, and the checkpoint antibodies pembrolizumab and nivolumab, add immunotherapy to the chemoradiation backbone.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Esophageal cancer bleeds and starves: chronic oozing from the tumor and the dysphagia that blocks eating leave patients iron-deficient and anemic, the low red cells compounding the weight loss it causes.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — The tumor and its treatment sit on the heart: a mid-esophageal cancer lies against the heart and great vessels, so the radiation that treats it irradiates the myocardium and the major esophagectomy that removes it carries real cardiac risk.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — NOTCH1 is a frequent casualty in esophageal squamous cancer: inactivating NOTCH1 mutations are among its commonest events, removing a brake on squamous-cell growth — one of the genetic hallmarks separating it from the lower-esophagus adenocarcinoma.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Esophageal cancer runs the clotting risk hot: like other gastrointestinal tumors it drives paraneoplastic thrombocytosis and a high rate of venous thromboembolism, complicating the chemotherapy and major surgery its treatment requires.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Cyclin D1 pushes the squamous tumor's cycle: CCND1 amplification is among the commonest events in esophageal squamous-cell carcinoma, releasing the G1 checkpoint to drive the rapid proliferation of the cancer.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Tumor-driving inflammation shows in the blood: esophageal cancer recruits neutrophils that promote invasion and angiogenesis, and a high neutrophil-to-lymphocyte ratio is a marker of worse prognosis.
- `connects-to` → **[Systemic Sclerosis](../systemic-sclerosis/README.md)** — Scleroderma scars the esophagus into cancer risk: systemic sclerosis paralyzes the lower esophagus, and the relentless reflux that follows drives Barrett's metaplasia and a raised risk of adenocarcinoma.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K signaling drives the esophageal tumor: PIK3CA mutation and amplification are recurrent in both squamous and adenocarcinoma, switching on the AKT-mTOR growth pathway and offering a targetable vulnerability.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells set the immunotherapy stage: their antigen presentation shapes the T-cell response esophageal cancer must evade, and their dysfunction underlies the immune escape that PD-1 blockade aims to reverse.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Surgery and obstruction open the door to sepsis: aspiration past an obstructing tumor and anastomotic leak after esophagectomy can seed mediastinitis and bloodstream infection, a leading cause of post-operative death.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — Chronic reflux and inflammation drive STAT3: IL-6-fueled STAT3 signaling promotes the survival and proliferation of esophageal cells along the Barrett's-to-adenocarcinoma path, tying inflammation to the cancer.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — A cancer and an operation that both clot: esophageal cancer's hypercoagulability plus the long, complex esophagectomy make venous thromboembolism a major perioperative and disease-related risk.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Chronic bleeding and inflammation drain the blood: beyond the iron loss of tumor bleeding, the inflammatory cytokines of esophageal cancer suppress erythropoiesis, adding an anemia of chronic disease that weakens patients before surgery.
- `connects-to` → **[Candida albicans](../../../02-pathogen/03-fungi/candida-albicans/README.md)** — The obstructed, stented esophagus invites the yeast: tumor narrowing, stents and the malnutrition and immunosuppression of esophageal cancer favor Candida esophagitis, worsening the dysphagia the cancer already causes.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Its chemo and poor intake strain the kidney: the cisplatin central to esophageal-cancer chemoradiation is nephrotoxic, and obstruction-driven dehydration adds prerenal injury, together threatening chronic kidney disease.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Losing the ability to eat weighs heavily: progressive dysphagia, weight loss, dependence on feeding tubes and a poor prognosis give esophageal cancer a substantial burden of depression.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Tumor and chemo injure the nerves: the cisplatin and taxane chemotherapy for esophageal cancer causes peripheral neuropathy, and tumor invasion of mediastinal nerves adds neuropathic pain.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Its therapy can wound the heart: the 5-fluorouracil used for esophageal cancer can provoke coronary vasospasm and cardiotoxicity, and adjacent thoracic radiation damages the heart, risking heart failure.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Chemoradiation opens the lung to mold: the neutropenia from esophageal-cancer chemoradiation, plus aspiration through a compromised swallow, can let inhaled Aspergillus invade as pulmonary aspergillosis.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Oesophagectomy is among the highest-risk surgeries: rebuilding the swallowing tube after removing the oesophagus leaves a chest anastomosis notorious for leak and slow, complicated healing.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It opens onto the airway: oesophageal cancer can erode into the trachea forming a tracheo-oesophageal fistula, causes aspiration through a failing swallow, and frequently brings pulmonary complications.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Choking dysphagia and grim odds breed worry: the progressive difficulty swallowing, weight loss and poor prognosis of oesophageal cancer foster chronic health anxiety alongside depression.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — It can erode into the great vessels: locally invasive oesophageal cancer can create a catastrophic aorto-oesophageal fistula with massive haemorrhage, or invade the pericardium.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It silences the voice: tumour invasion of the recurrent laryngeal nerve causes hoarseness, a clinical sign of mediastinal spread of oesophageal cancer.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It can raise the blood calcium: squamous-cell oesophageal cancer can secrete parathyroid-hormone-related peptide, causing paraneoplastic hypercalcaemia.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Immunotherapy now treats it: PD-1 checkpoint inhibitors are used in advanced and adjuvant oesophageal cancer, while chronic reflux-driven inflammation underlies the adenocarcinoma.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — The skin can flag it: the hereditary palmoplantar keratoderma tylosis (Howel-Evans) strongly predisposes to oesophageal squamous-cell cancer, and paraneoplastic acanthosis nigricans can appear.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It links to muscle and bone: oesophageal cancer can present with paraneoplastic dermatomyositis, and advanced disease metastasises to the skeleton.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Immunotherapy now treats it: PD-1 inhibitors (nivolumab, pembrolizumab) are used adjuvantly after chemoradiation and for advanced oesophageal and gastro-oesophageal cancer.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Chemoradiation is the backbone: platinum and fluoropyrimidine chemotherapy with radiation (the CROSS regimen) precedes surgery for resectable oesophageal cancer.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Molecular subsets gain drugs: HER2-positive oesophageal adenocarcinoma responds to trastuzumab, and FGFR and other targets are emerging in this hard-to-treat cancer.
- `connects-to` → **[NSCLC](../nsclc/README.md)** — Smoking links them in the chest: oesophageal squamous-cell carcinoma and lung cancer share tobacco and alcohol carcinogenesis and mediastinal proximity, so they co-occur and invade across the chest cavity.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — It invades mediastinal nerves: oesophageal cancer can engulf the recurrent laryngeal nerve, causing hoarseness, and infiltrate other mediastinal nerves — local nerve invasion marking unresectable disease.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — It spreads to the skeleton: advanced oesophageal cancer metastasises to bone as painful osteolytic lesions, one of the distant sites — with liver and lung — that mark incurable disease.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Airway erosion and aspiration: oesophageal cancer can erode into the trachea, forming a tracheo-oesophageal fistula that floods the alveoli with saliva and food, causing recurrent aspiration pneumonia.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Immunotherapy and the immune microenvironment: oesophageal squamous carcinoma can harbour tertiary lymphoid structures with germinal-centre activity, and checkpoint inhibitors now extend survival in advanced disease.
- `connects-to` → **[Bladder Cancer](../bladder-cancer/README.md)** — Smoking's shared field: tobacco and alcohol drive oesophageal squamous cancer, and the same carcinogens raise the risk of bladder cancer—a field effect across smoke-exposed epithelia.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Liver as a metastatic site: oesophageal cancer spreads to the liver, seeding the hepatic lobules, a common site of distant metastasis that marks incurable disease.
- `connects-to` → **[COPD](../copd/README.md)** — Shared smoking carcinogenesis: oesophageal squamous cancer and COPD both arise from tobacco and shared field injury, and COPD's hypoxia and frailty worsen surgical and chemoradiation outcomes.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Radiation's cardiac cost: chemoradiation for oesophageal cancer irradiates the adjacent heart, causing late myocardial fibrosis, coronary disease and cardiomyopathy of the myocardium.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — MYC amplification: gains of MYC are common in both oesophageal adenocarcinoma and squamous cell carcinoma, driving the proliferation of these aggressive tumours.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — RAS in adenocarcinoma: KRAS mutation and amplification arise in oesophageal and gastro-oesophageal junction adenocarcinoma, activating MAPK signalling that fuels growth.
- `connects-to` → **[YAP1](../../03-molecular/yap1/README.md)** — Hippo amplicon: YAP1 amplification on 11q22 is a recurrent driver of oesophageal squamous cell carcinoma, an oncogenic Hippo-pathway lesion promoting tumour growth.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K/AKT growth: PIK3CA mutation activates AKT in oesophageal cancer, driving survival and proliferation and contributing to resistance to chemoradiotherapy.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Tumour hypoxia: HIF-1α stabilised in hypoxic oesophageal tumours drives angiogenesis and an invasive, treatment-resistant phenotype linked to poor prognosis.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Epigenetic driver: EZH2 overexpression silences tumour-suppressor genes in oesophageal cancer, promoting proliferation and invasion as a candidate therapeutic target.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — Telomerase immortalisation: TERT reactivation maintains telomeres in oesophageal cancer cells, granting the limitless replicative capacity that complements its p53 and cell-cycle lesions.
- `connects-to` → **[TGF-beta](../../03-molecular/tgf-beta/README.md)** — EMT and stroma: TGF-beta drives epithelial-mesenchymal transition and a desmoplastic, immunosuppressive stroma in oesophageal cancer, promoting the invasion and spread of advanced disease.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Macrophage recruitment: CCL2 draws tumour-associated macrophages into the oesophageal cancer microenvironment, supporting angiogenesis and immune evasion in this aggressive cancer.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — Chronic IL-6/STAT3 inflammation from gastro-esophageal reflux and Barrett's esophagus drives the metaplasia-dysplasia-carcinoma sequence behind esophageal adenocarcinoma, linking acid injury to malignant transformation.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCR4 on esophageal cancer cells follows CXCL12 gradients to lymph nodes and distant organs, driving the early nodal spread that makes this cancer so often incurable by the time of diagnosis.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — The high tobacco- and reflux-driven mutational burden of esophageal cancer generates cytosolic DNA and neoantigens that engage cGAS-STING, underlying the responsiveness of the disease to checkpoint-inhibitor immunotherapy.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Chronic reflux of acid and bile acids, which derive from cholesterol, into the lower esophagus drives the Barrett's metaplasia-dysplasia sequence behind esophageal adenocarcinoma, the histology rising sharply in Western countries.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Neoadjuvant chemoradiation and perioperative chemotherapy kill esophageal-cancer cells through caspase-3-mediated apoptosis, the cytotoxic backbone whose effect on the primary tumor predicts surgical outcome.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Central obesity raises both mechanical reflux and leptin, which promotes esophageal epithelial proliferation, two ways the obesity epidemic drives the rising incidence of esophageal adenocarcinoma.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — EGFR, HER2, KRAS and FGFR (all already mapped) funnel into the MAPK-ERK cascade, the proliferative hub driving both squamous-cell and adenocarcinoma forms of esophageal cancer.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR completes the PI3K-AKT-mTOR pathway (PIK3CA and AKT already mapped) that sustains growth and survival signaling in esophageal carcinoma.
- `connects-to` → **[CDH1](../../03-molecular/cdh1/README.md)** — Loss of E-cadherin during epithelial-mesenchymal transition releases esophageal-carcinoma cells from their junctions, enabling the invasion and nodal spread that worsen prognosis.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — Chronic reflux- and inflammation-driven TLR-MyD88-NF-κB signaling (NF-κB already mapped) promotes the Barrett's-metaplasia-to-adenocarcinoma sequence of esophageal cancer.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — IL-6 signaling through JAK-STAT3 (IL-6 and STAT3 already mapped) sustains the inflammatory, pro-tumorigenic microenvironment of esophageal cancer.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — The RB1-E2F checkpoint (CDKN2A and cyclin-D1 already mapped) restrains cell-cycle entry, and its disruption contributes to the proliferation of esophageal cancer.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD4 signaling (TGF-β mapped) is a context-dependent tumor suppressor whose loss promotes progression in esophageal cancer, particularly the Barrett-adenocarcinoma sequence.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 promotes invasion and immune evasion in esophageal cancer.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — Loss of PTEN restraint on PI3K-AKT-mTOR signaling (AKT, PIK3CA and mTOR mapped) drives proliferation and survival in esophageal cancer.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the antitumor immune response of esophageal cancer, relevant to its checkpoint immunotherapy.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6-cyclin-D activity (cyclin-D1, CDKN2A and RB1 already mapped) drives the cell-cycle progression of esophageal cancer.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO tumor-suppressor activity, restrained by the PI3K-AKT axis, is lost in the proliferative progression of esophageal cancer.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-delivered cytotoxic killing by CD8 T and NK cells mediates the immune clearance that the immunotherapy-treated esophageal cancer must evade.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the inflammatory, reflux- and Barrett's-associated microenvironment of esophageal cancer.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in esophageal cancer.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β regulates the Wnt/β-catenin and survival signaling of esophageal cancer.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of EGFR and HER2 (both already mapped) drives the invasion of esophageal cancer.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic silencing of tumor-suppressor genes in esophageal cancer.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of esophageal cancer.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival and therapy resistance of esophageal cancer cells.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the immunosuppressive microenvironment of esophageal cancer.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of esophageal cancer.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the reflux/Barrett's-linked inflammation and tumor microenvironment of esophageal cancer.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of esophageal cancer.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory tumor microenvironment of esophageal cancer.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory tumor microenvironment of esophageal cancer.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the tumor microenvironment and immune signaling of esophageal cancer.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Acid reflux carcinogenesis: chronic reflux of gastric acid (protons) drives Barrett's metaplasia and oesophageal adenocarcinoma, the mechanism linking GERD and obesity (leptin already mapped) to the rising incidence of the lower-oesophageal tumour.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Immunotherapy: checkpoint inhibitors (PD-1 already mapped) are now standard in oesophageal cancer, and MHC class II antigen presentation shapes the T-cell response that determines benefit, especially in the squamous subtype.
- `connects-to` → **[AXL receptor](../../03-molecular/axl-receptor/README.md)** — Invasion and resistance: the AXL receptor tyrosine kinase drives the epithelial-mesenchymal transition and treatment resistance of oesophageal cancer, a mechanism of progression beyond the HER2 and FGFR targets already mapped.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Dysphagia and bleeding: progressive dysphagia with weight loss is the hallmark presentation of oesophageal cancer, and chronic tumour bleeding lowers haemoglobin, the iron-deficiency anaemia that often prompts the diagnosis.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell immunity: IL-2-driven T-cell expansion (PD-1 and perforin already mapped) supports the anti-tumour response that checkpoint inhibitors unleash, now standard in oesophageal cancer, especially the squamous subtype.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative carcinogenesis: chronic reflux, alcohol and tobacco generate reactive oxygen species, to which xanthine oxidase contributes, and this oxidative DNA damage (NRF2 already mapped) drives the carcinogenesis of both oesophageal cancer subtypes.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — COX-2 and Barrett's: cyclooxygenase-2 and prostaglandin E2 rise in Barrett's oesophagus and the adenocarcinoma it precedes, promoting the inflammation and proliferation of carcinogenesis, and aspirin is studied for chemoprevention.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive microenvironment: IL-10 in the tumour microenvironment dampens the anti-tumour T-cell response (PD-1 and perforin already mapped), part of the immune escape that the checkpoint inhibitors now standard in oesophageal cancer aim to reverse.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Fistula and metastasis: locally advanced oesophageal cancer can erode into the airway to form a tracheo-oesophageal fistula, and the lung is a common site of the metastases of advanced disease.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises the tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the microenvironment the checkpoint inhibitors now standard in oesophageal cancer must overcome.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Desmoplastic stroma: the cancer-associated fibroblasts lay down the desmoplastic stroma (TGF-β already mapped) of oesophageal cancer, supporting the invasion and the treatment resistance of the tumour.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron-deficiency anaemia: the chronic occult bleeding of the oesophageal tumour and the dysphagia-related malnutrition cause the iron-deficiency anaemia (haemoglobin already mapped) common at presentation.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Obesity-adenocarcinoma adipokine: adiponectin, with leptin (already mapped), links the obesity (already mapped) that drives the oesophageal adenocarcinoma to the metabolic-inflammatory milieu of the tumour.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — M2 desmoplastic arm: IL-13, with IL-4 (already mapped), drives the M2 macrophage (already mapped) arm of the immunosuppressive desmoplastic (fibroblast already mapped) stroma of oesophageal cancer.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the obesity-associated oesophageal adenocarcinoma.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Selenium-deficiency risk: the dietary selenium deficiency (the Linxian region) is a risk factor for the oesophageal squamous-cell carcinoma, the antioxidant selenoprotein protection being chemopreventive.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — GI-bleed anaemia: the chronic tumour blood loss and the inflammation (IL-6 already mapped)-driven hepcidin produce the iron-restricted anaemia (haemoglobin already mapped) of oesophageal cancer.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate antitumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune tumour microenvironment relevant to the immunotherapy of oesophageal cancer.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity, exploited by the checkpoint (PD-1 already mapped) immunotherapy of oesophageal cancer.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of oesophageal cancer.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of oesophageal cancer.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the tumour-promoting inflammation of oesophageal cancer.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the oesophageal-cancer microenvironment.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of oesophageal cancer.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of oesophageal cancer.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, associates with the nivolumab (PD-1 already mapped) immunotherapy response of oesophageal cancer.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the oesophageal-cancer stroma.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) contribute to the inflammatory dimension of the oesophageal-cancer microenvironment.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement evasion: the oesophageal-cancer cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), tempering the complement attack within the tumour stroma.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Haemorrhage/tumour iron: transferrin, the iron carrier, reflects the iron demand of the tumour and the iron-deficiency anaemia of the chronic blood loss of oesophageal cancer.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-oesophageal axis: TSLP, from the Barrett's-epithelium and the oesophageal tumour stroma, primes dendritic cells (already mapped) and mast cells (already mapped), amplifying the Th2 immunosuppressive microenvironment of oesophageal cancer.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-oesophageal axis: bradykinin, via B1/B2 receptors on tumour endothelium (already mapped) and mast cells (already mapped), augments the vascular permeability, tumour oedema, and the pro-inflammatory stromal milieu of oesophageal cancer.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — EPO-oesophageal axis: erythropoietin, induced by the HIF-1α (already mapped) hypoxia and anaemia of oesophageal cancer, activates the EPOR on tumour cells (already mapped) and modulates macrophage (already mapped) polarisation in the tumour microenvironment.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Histamine-oesophageal axis: histamine, released by mast cells in the Barrett's-oesophagus and oesophageal-tumour stroma, signals via H1/H2 receptors on tumour cells and endothelium, modulating angiogenesis, immune evasion, and the pro-tumourigenic milieu of oesophageal cancer.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Melatonin-oesophageal axis: melatonin, produced by enterochromaffin cells in the oesophageal mucosa, suppresses acid-reflux-driven oxidative stress, limits Barrett's-oesophagus progression, and enhances apoptotic sensitivity in oesophageal-cancer cells.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Androgen-oesophageal axis: testosterone, via androgen receptor signalling on oesophageal squamous and adenocarcinoma cells, modulates tumour proliferation, immune evasion, and the well-established male sex bias in oesophageal-cancer incidence and mortality.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — EC prolactin: prolactin, via PRLR on macrophages (already mapped) and mast cells (already mapped), modulates the immune TME; hyperprolactinaemia amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of esophageal cancer.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — EC oxytocin: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates tumour-promoting inflammation; oxytocin deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of esophageal cancer.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — EC vasopressin: vasopressin, via V1aR on macrophages (already mapped) and mast cells (already mapped), modulates the TME; vasopressin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of esophageal cancer.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^doki-2022-checkmate648]: Doki Y, Ajani JA, Kato K, et al. Nivolumab combination therapy in advanced esophageal squamous-cell carcinoma. *N Engl J Med.* 2022;386(5):449-462. [doi:10.1056/NEJMoa2111380](https://doi.org/10.1056/NEJMoa2111380) · [PubMed 35108470](https://pubmed.ncbi.nlm.nih.gov/35108470/)
[^kato-2019-attraction3]: Kato K, Cho BC, Takahashi M, et al. Nivolumab versus chemotherapy in patients with advanced oesophageal squamous cell carcinoma refractory or intolerant to previous chemotherapy (ATTRACTION-3). *Lancet Oncol.* 2019;20(11):1506-1517. [doi:10.1016/S1470-2045(19)30626-6](https://doi.org/10.1016/S1470-2045(19)30626-6) · [PubMed 31582355](https://pubmed.ncbi.nlm.nih.gov/31582355/)
