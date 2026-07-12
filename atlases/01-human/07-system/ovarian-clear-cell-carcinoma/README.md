---
schema: human-scale-entry/v1
id: ovarian-clear-cell-carcinoma
name: Ovarian Clear Cell Carcinoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Ovarian clear cell carcinoma (OCCC) is an endometriosis-derived subtype; ARID1A (~50%) and PIK3CA (~50%) are hallmark mutations; platinum-resistant; no FDA-approved targeted therapy; higher incidence in Asian women; mTOR inhibitors and EZH2 inhibitors under investigation."
aliases: ["OCCC", "ovarian clear cell carcinoma", "clear cell ovarian cancer", "endometriosis-associated ovarian cancer", "ARID1A ovarian cancer", "PIK3CA ovarian clear cell", "clear cell adenocarcinoma ovary", "endometrioid-related ovarian cancer", "ovarian cancer clear cell", "CCC ovarian"]
sources:
  - id: jones-2010-arid1a-occc
    type: peer-reviewed
    cite: "Jones S, Wang TL, Shih IeM, et al. Frequent mutations of chromatin remodeling gene ARID1A in ovarian clear cell carcinoma. Science. 2010;330(6001):228-231."
    doi: "10.1126/science.1196333"
    pmid: "20826764"
    url: "https://doi.org/10.1126/science.1196333"
  - id: kim-2015-arid1a-ezh2
    type: peer-reviewed
    cite: "Kim KH, Kim W, Howard TP, et al. SWI/SNF-mutant cancers depend on catalytic and non-catalytic activity of EZH2. Nat Med. 2015;21(12):1491-1496."
    doi: "10.1038/nm.3968"
    pmid: "26552009"
    url: "https://doi.org/10.1038/nm.3968"
cross_links:
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A (BAF250A) is mutated in ~50% of OCCC; biallelic ARID1A LOF → cBAF disruption; ARID1A IHC (BAF250A, clone PSG3) protein loss is a surrogate diagnostic marker in OCCC; ARID1A + PIK3CA co-mutation in ~25-30% OCCC defines the highest-risk molecular subgroup."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "ARID1A LOF disrupts cBAF → EZH2/PRC2 accesses ARID1A-target loci → H3K27me3 accumulation; OCCC with ARID1A LOF shows EZH2 dependency in preclinical models; tazemetostat under investigation in ARID1A-mutant OCCC; EZH2 + PARP inhibitor combination explored."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "ARID1A + PIK3CA co-mutation defines ~25-30% of ovarian clear cell carcinomas; PIK3CA → PI3K/AKT/mTOR → OCCC proliferation; ARID1A LOF + PIK3CA creates synthetic vulnerability to dual PI3K/mTOR inhibition; temsirolimus active in PIK3CA-mutant OCCC Phase 2."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "ARID1A LOF in OCCC → PD-L1 upregulation via MLH1 suppression and IFN-γ signaling pathway enhancement; OCCC has higher PD-L1 expression than high-grade serous ovarian cancer; pembrolizumab + bevacizumab shows activity in PD-L1+ OCCC; durvalumab combination trials ongoing."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "PIK3CA mutations (~40-50%) in OCCC → PI3K/AKT → mTOR activation; temsirolimus Phase 2 in OCCC: ORR ~10-15%; alpelisib (PIK3CA inhibitor) explored in PIK3CA-mutant OCCC; PI3K/mTOR dual inhibitors studied; ARID1A LOF + PIK3CA → synthetic vulnerability to PI3K/mTOR inhibition."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "KRAS G12D/V mutations in ~15% of OCCC, enriched in endometriosis-associated OCCC; KRAS + ARID1A co-mutation in ~8-10%; MEK pathway activated in KRAS-mutant OCCC → MEK inhibitors explored; KRAS mutation is more prevalent in OCCC than HGSOC or endometrioid ovarian cancer."
  - target: 01-human/07-system/ovarian-cancer
    relation: connects-to
    note: "OCCC is distinct from HGSOC: OCCC (ARID1A/PIK3CA-driven, platinum-resistant, stage I-II at ~35-40%) vs HGSOC (TP53-universal, platinum-sensitive, stage III-IV at ~75%); OCCC lacks HRD enrichment; 5-year OS in advanced OCCC is worse than HGSOC despite identical chemotherapy."
  - target: 01-human/07-system/endometrial-cancer
    relation: connects-to
    note: "Ovarian clear cell carcinoma and endometrioid endometrial cancer are both endometriosis/endometrium-derived tumors driven by ARID1A and PIK3CA; clear-cell and endometrioid histologies recur across ovary and uterus, and both can arise in Lynch syndrome — unlike serous cancers."
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "Ovarian clear cell carcinoma and clear-cell renal cell carcinoma are unrelated organs sharing a look and biology: both have glycogen-rich clear cytoplasm, both upregulate HIF/VEGF, and OCCC borrows RCC anti-angiogenics like sunitinib for this platinum-resistant tumor."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Ovarian clear cell carcinoma is more immunogenic than high-grade serous cancer: ARID1A loss raises neoantigens and PD-L1, so it draws cytotoxic CD8+ T cells and responds better to PD-1 blockade — pembrolizumab + bevacizumab is studied in PD-L1+ OCCC."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Ovarian clear cell carcinoma has the highest venous thromboembolism rate of any ovarian cancer—up to a quarter of patients: the tumor is strongly prothrombotic (tissue factor, IL-6), so DVT and pulmonary embolism are watched and often prophylaxed throughout treatment."
  - target: 01-human/07-system/lynch-syndrome
    relation: connects-to
    note: "Clear-cell and endometrioid ovarian cancers are the histologies linked to Lynch syndrome: mismatch-repair deficiency underlies a share of OCCC, so MMR/MSI testing both flags a germline syndrome and identifies tumors that may respond to checkpoint blockade."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Ovarian clear cell carcinoma is the ovarian cancer most tied to endometriosis: ectopic endometrial tissue, under oxidative iron-rich stress, acquires ARID1A and PIK3CA mutations and transforms—making endometriosis a recognized precursor in the reproductive tract."
  - target: 01-human/07-system/gastric-cancer
    relation: connects-to
    note: "Ovarian clear-cell carcinoma and gastric cancer share ARID1A loss: this SWI/SNF chromatin-remodeler tumor suppressor is among the most mutated genes in both, showing how chromatin disruption—not classic oncogenes—drives diverse epithelial cancers."
  - target: 01-human/07-system/cholangiocarcinoma
    relation: connects-to
    note: "Ovarian clear-cell carcinoma and cholangiocarcinoma converge on chromatin-remodeling defects: both frequently lose ARID1A, and both are relatively chemoresistant epithelial cancers—making epigenetic vulnerabilities (EZH2 inhibition) a shared therapeutic avenue."
  - target: 01-human/07-system/hereditary-breast-ovarian-cancer
    relation: connects-to
    note: "Ovarian clear-cell carcinoma differs from the BRCA-driven cancers of HBOC: unlike high-grade serous ovarian cancer, clear-cell is rarely BRCA/HRD-related (it's ARID1A/PIK3CA-driven), so it responds poorly to platinum and PARP inhibitors—a key treatment distinction."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "OCCC is driven by PI3K-pathway and chromatin gene mutations: ARID1A loss with PIK3CA or PTEN alterations activates PI3K/AKT/mTOR growth signaling, distinguishing clear cell carcinoma's biology—and rationale for mTOR/PI3K-targeted trials—from high-grade serous cancer."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "OCCC tends to be immunologically distinct and PD-L1-expressing: among ovarian cancers, clear cell carcinoma more often shows mismatch-repair/ARID1A features and immune infiltration, so NK and T-cell-engaging immunotherapy is of interest in this platinum-resistant subtype."
  - target: 01-human/07-system/vhl-disease
    relation: connects-to
    note: "OCCC shares clear-cell morphology and biology with renal clear cell carcinoma: glycogen-rich clear cytoplasm and HIF/VEGF-driven angiogenesis link it to VHL-associated kidney cancer, so anti-angiogenic agents are explored across these histologically similar tumors."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "Ovarian clear cell carcinoma is characteristically p53-wildtype: unlike high-grade serous ovarian cancer, which is defined by TP53 mutation, OCCC is driven instead by ARID1A and PIK3CA—so p53 status helps distinguish these biologically distinct ovarian cancers."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Ovarian clear cell carcinoma resists platinum chemo but its ARID1A loss links to immunotherapy: ARID1A-mutant or mismatch-repair-deficient tumors can respond to checkpoint blockade, offering an option in this otherwise chemoresistant subtype."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "OCCC's clear cytoplasm reflects HIF-driven metabolism: a stabilized hypoxia program reprograms cells toward glycolysis and glycogen storage (the 'clear' look), and this metabolic state contributes to the platinum chemoresistance that makes OCCC hard to treat."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Clear-cell ovarian cancer is the gynecologic tumor most linked to hypercalcemia: it can drive paraneoplastic high calcium (via PTH-related peptide), so an ovarian mass with unexplained hypercalcemia points toward this histotype."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Clear-cell ovarian cancer often overproduces IL-6: this cytokine drives paraneoplastic fever, thrombocytosis and an inflammatory state, contributing to the thrombosis risk and the relative chemoresistance that set this subtype apart."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Clear-cell ovarian cancer grows from an endometriotic niche rich in fibroblasts: the cyst's reactive stroma and chronic inflammation foster ARID1A-mutant transformation, so the fibroblast-laden microenvironment is part of how this cancer begins."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Ovarian clear cell carcinoma is forged in iron: it arises from endometriosis, where repeated bleeding dumps iron into cysts, and the resulting oxidative stress damages DNA and drives the ARID1A-mutant cancer—linking menstrual iron to a tumor."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Ovarian clear cell carcinoma is intensely angiogenic via VEGF: HIF-driven VEGF feeds its blood supply, so anti-VEGF bevacizumab is among the few systemic options for a tumor notoriously resistant to standard chemotherapy."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Iron-laden macrophages haunt clear cell carcinoma's origin: in the endometriotic cysts it springs from, macrophages gorge on blood-derived iron and pump out inflammatory signals, building the oxidative, pro-tumor niche the cancer exploits."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Clear cell ovarian carcinoma behaves as if starved of oxygen: its glycogen-packed clear cells run a HIF-driven pseudohypoxic program even when oxygen is present, fueling growth and the chemoresistance that makes this subtype so hard to treat."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Clear cell ovarian carcinoma spreads across the peritoneum: like other ovarian cancers it studs the omentum and bowel surface, so abdominal disease and bowel involvement shape its presentation and the surgery aimed at removing all visible tumor."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells matter most in the immunogenic subset of clear cell ovarian carcinoma: some tumors carry mismatch-repair defects and neoantigens, and antigen-presenting dendritic cells help mount the response that checkpoint therapy can amplify."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Clear cell ovarian carcinoma mirrors kidney cancer: it shares the HIF-driven clear-cell biology of renal clear cell carcinoma, and as a pelvic mass it can obstruct the ureters and kidneys."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Clear cell ovarian carcinoma is hypervascular: HIF and VEGF drive endothelial cells to build a rich blood supply, like its renal counterpart, a feature anti-angiogenic therapy targets."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Clear cell ovarian carcinoma is born in endometriosis: it arises within fibrotic, blood-stained endometriotic cysts, whose chronic inflammation and scarring set the stage for malignant transformation."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy explains the 'clear' in clear cell: the cytoplasm is packed with glycogen that dissolves away in processing, leaving the empty, water-clear cells and bulging hobnail nuclei that name the tumor."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Clear cell carcinoma is the great clotter of ovarian cancers: it carries the highest rate of venous thromboembolism, activating platelets and the clotting cascade so strongly that a deep vein thrombosis can be the first sign of the tumor."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "When clear cell carcinoma spreads beyond the pelvis, the liver is a frequent target: hematogenous metastases lodge there, and liver involvement marks the advanced, chemoresistant disease that makes this subtype so hard to treat."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Even a platinum-resistant tumor exacts a neural toll: OCCC is treated up front with carboplatin and paclitaxel, and the taxane in particular injures peripheral sensory neurons, leaving lasting numbness despite the subtype's poor chemo response."
  - target: 01-human/03-molecular/albumin
    relation: connects-to
    note: "OCCC announces itself with fluid: like other ovarian cancers it seeds the peritoneum and produces malignant ascites, while tumor burden and poor nutrition drive down blood albumin, a marker that tracks with worse outcomes."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "OCCC can reach the chest: advanced disease produces malignant pleural effusions and lung metastases, the thoracic spread that defines stage IV and signals the hard-to-treat end of this subtype."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibody stains pin down the subtype: HNF1B and Napsin A staining with loss of ARID1A confirm clear-cell histology and its endometriosis origin, separating OCCC from the high-grade serous tumors that demand different treatment."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "This subtype resists platinum, so the marrow still pays: the carboplatin-paclitaxel given despite OCCC's chemoresistance is myelosuppressive, dropping neutrophils between cycles, while a high neutrophil-to-lymphocyte ratio flags its poorer prognosis."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Platinum therapy wastes magnesium: carboplatin injures the kidney tubule that reclaims it, so blood magnesium and potassium fall and must be replaced through the cycles, even as OCCC responds less well to that platinum than other ovarian cancers."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "OCCC turns up its antioxidant defenses: chronically bathed in oxidative stress, the tumor activates the NRF2 pathway to neutralize reactive oxygen, an adaptation that also helps explain its notorious resistance to platinum chemotherapy."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT is OCCC's growth engine: frequent PIK3CA mutations and PTEN loss funnel through AKT to mTOR, a dominant signaling axis in clear cell ovarian cancer and a target for PI3K-pathway inhibitors in this hard-to-treat subtype."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "ARID1A loss makes OCCC visible to the immune system: the resulting mutational and microsatellite instability draws in T cells, so clear cell ovarian cancer responds to checkpoint immunotherapy more often than the commoner serous type."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "It is born from an estrogen-driven lesion: clear cell ovarian cancer arises within endometriosis, where estrogen-fueled ectopic endometrial tissue and its iron-rich bleeding create the inflamed, mutagenic niche that gives rise to the tumor."
  - target: 01-human/03-molecular/met
    relation: connects-to
    note: "A receptor kinase offers a handle on a chemoresistant tumor: MET amplification and activation help drive clear cell ovarian cancer, which resists standard platinum chemotherapy, so MET and its PI3K-pathway partners are pursued as targets."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "The tumor balances its immune visibility with suppression: even as ARID1A loss recruits T cells, regulatory T cells and an immunosuppressive microenvironment temper the response, shaping which clear cell tumors actually benefit from checkpoint blockade."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 marks the clear-cell subtype: OCCC is notably IL-6-high, and the downstream STAT3 activation drives growth, the paraneoplastic inflammation, and the platinum resistance that distinguish it from serous ovarian cancer."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Chronic inflammation switches on NF-κB: born in an inflamed endometriotic niche, OCCC carries constitutive NF-κB activity that supports survival and contributes to its resistance to chemotherapy."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Advanced pelvic disease invites sepsis: bowel obstruction and perforation from peritoneal spread, plus chemotherapy neutropenia, expose patients to intra-abdominal infection and sepsis."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Lost SWI/SNF control drives the cell cycle: ARID1A loss in OCCC dysregulates cyclin D1 and cell-cycle entry, contributing to the proliferation of this chemoresistant clear-cell subtype."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Pelvic disease and platinum strain the kidneys: tumor obstructing the ureters causes hydronephrosis, and the cisplatin used against this resistant cancer is nephrotoxic, together risking chronic kidney disease."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Chronic inflammation and chemo drain the blood: born of inflamed endometriosis and treated with marrow-suppressing platinum, OCCC commonly produces an anemia of chronic disease."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Removing the ovaries withdraws bone-protective estrogen: surgery and chemotherapy for OCCC throw younger patients into abrupt menopause, and the estrogen loss accelerates bone thinning toward osteoporosis."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A chemoresistant cancer in young women weighs on mood: OCCC's poor response to platinum at recurrence, frequent advanced presentation and abrupt surgical menopause contribute to substantial depression and anxiety."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Salvage anthracyclines can weaken the heart: because OCCC resists platinum, recurrent disease is often treated with pegylated liposomal doxorubicin, whose cumulative cardiotoxicity can erode cardiac function into heart failure."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Its taxane-platinum chemo numbs the nerves: the paclitaxel and carboplatin used first-line in OCCC cause a dose-dependent, often lasting peripheral neuropathy with painful paraesthesiae."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Cytoreductive surgery heals slowly: the staging and debulking surgery for OCCC, sometimes extensive and in malnourished patients, leaves abdominal wounds prone to dehiscence and delayed closure."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A chemoresistant cancer breeds worry: the platinum resistance, recurrence risk and tumour-marker surveillance of OCCC foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It classically raises the calcium: ovarian clear cell carcinoma is the gynaecological tumour most associated with paraneoplastic hypercalcaemia, and its oophorectomy forces surgical menopause."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It reaches the chest: advanced OCCC causes malignant pleural effusions through diaphragmatic spread, and its strong thrombotic tendency raises the risk of pulmonary embolism."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It arises from endometriosis and spreads on the peritoneum: OCCC develops from endometriotic cysts and, as it advances, seeds the peritoneum to cause ascites and bowel obstruction."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It spreads to the deep nodes: ovarian clear cell carcinoma disseminates to pelvic and para-aortic lymph nodes, so lymphadenectomy is part of its surgical staging."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "It is intensely prothrombotic: OCCC carries one of the highest venous thromboembolism rates of any cancer, straining the circulation with deep-vein thrombosis and pulmonary embolism."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Its high calcium and chemo reach the nerves: severe paraneoplastic hypercalcaemia causes confusion and lethargy, and the platinum chemotherapy it resists also causes peripheral neuropathy."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "A clear-cell cousin of kidney cancer, treated near the kidney: ovarian clear cell carcinoma shares clear-cell histology with renal cancer, and bulky pelvic spread plus cisplatin chemotherapy threaten the kidneys."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Chemoresistance drives a search for targets: ARID1A-mutant ovarian clear cell carcinoma resists platinum, so trials pursue immunotherapy and ATR or other targeted inhibitors."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Paraneoplastic hypercalcaemia draws on bone: ovarian clear cell carcinoma can secrete PTHrP causing hypercalcaemia that mobilises calcium from the skeleton."
  - target: 01-human/07-system/bladder-cancer
    relation: connects-to
    note: "A fellow ARID1A-driven cancer: like a subset of bladder cancer, ovarian clear cell carcinoma is frequently driven by ARID1A loss disrupting the SWI/SNF chromatin-remodelling complex."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "It still receives the standard regimen: carboplatin-paclitaxel is given after surgery, though ovarian clear cell carcinoma's relative platinum resistance makes complete response less common than in serous cancer."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Biomarkers favour immunotherapy here: ovarian clear cell carcinoma more often shows microsatellite instability and PD-L1 expression, making PD-1 checkpoint inhibitors a more promising option than in serous ovarian cancer."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "B-cell islands beyond the T cells: clear cell ovarian cancers that organise tertiary lymphoid structures with germinal-centre B cells mount a broader antitumour response and tend to fare better, adding to the T-cell infiltrate that already shapes ovarian-cancer outcome."
  - target: 01-human/07-system/hcc
    relation: connects-to
    note: "A shared chromatin-remodeller defect: ARID1A, the SWI/SNF subunit mutated in roughly half of clear cell ovarian cancers, is also among the commonest mutations in hepatocellular carcinoma—one epigenetic machinery failing across two organs."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "Driven by the same oncogenes: clear cell ovarian cancers frequently carry KRAS and PIK3CA mutations that also drive colorectal cancer, so the RAS-PI3K signalling these tumours share guides targeted-therapy thinking across both."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "Peritoneal and bowel spread: like other ovarian cancers, clear-cell carcinoma seeds the peritoneum and infiltrates the bowel wall, though it more often presents as an early-stage pelvic mass arising from endometriosis."
  - target: 01-human/07-system/hlrcc
    relation: connects-to
    note: "Clear cells and HIF across organs: OCCC, like HLRCC's renal cancer and clear-cell RCC, shows glycogen-rich clear cytoplasm and constitutive HIF/pseudohypoxia—a convergent clear-cell phenotype in different organs."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Lung and pleural metastasis: clear-cell ovarian carcinoma can spread to the lungs and pleura, seeding the alveolar bed in its chemoresistant advanced course."
  - target: 01-human/07-system/disseminated-intravascular-coagulation
    relation: connects-to
    note: "The most thrombogenic ovarian cancer: clear-cell carcinoma carries the highest venous thromboembolism rate of the ovarian subtypes and can trigger Trousseau-type consumptive coagulopathy and DIC."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "HIF-driven vasculature: like clear-cell renal cancer, ovarian clear-cell carcinoma is intensely angiogenic through HIF and VEGF, building abnormal tumour arterial walls that antiangiogenic drugs target."
  - target: 01-human/07-system/mesothelioma
    relation: connects-to
    note: "A peritoneal differential: peritoneal mesothelioma produces serosal masses, effusions and ascites that overlap with the peritoneal spread of ovarian clear-cell carcinoma, a distinction made on biopsy and markers."
  - target: 01-human/03-molecular/yap1
    relation: connects-to
    note: "Hippo-YAP activation: ARID1A loss in ovarian clear-cell carcinoma deregulates the Hippo-YAP pathway, contributing to its growth and treatment resistance."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Notch signalling: dysregulated Notch signalling participates in ovarian clear-cell carcinoma, an additional pathway alongside its ARID1A and PI3K alterations."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Replicative immortality: TERT reactivation maintaining telomeres supports the persistent proliferation of ovarian clear-cell carcinoma, a notably chemoresistant tumour."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Proliferative oncogene: MYC activation drives the proliferation of ovarian clear-cell carcinoma, cooperating with its ARID1A and PIK3CA lesions."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "Cell-cycle drive: cyclin D-CDK4/6 activity propels ovarian clear-cell carcinoma cells through the G1 checkpoint, a candidate vulnerability in this chemoresistant tumour."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Fibrosis and EMT: TGF-β signalling promotes the epithelial-mesenchymal transition and stromal remodelling that aid the invasion of ovarian clear-cell carcinoma."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Endometriosis-derived TAMs: OCCC arises in an endometriotic, inflamed niche where CCL2 recruits monocytes that become the M2 tumour-associated macrophages sustaining this chemoresistant tumour."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Inflammatory origin: chronic IL-1β signalling in endometriotic cysts drives the inflammatory microenvironment from which ovarian clear-cell carcinoma emerges, linking benign endometriosis to malignant transformation."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "ARID1A and immunity: ARID1A loss in OCCC impairs mismatch repair and DNA-damage handling, raising mutational burden and cytosolic DNA that engage cGAS-STING — a rationale for checkpoint blockade in this typically immunotherapy-responsive subtype."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Intrinsic chemoresistance: OCCC resists the platinum chemotherapy that controls high-grade serous disease, evading caspase-3-mediated apoptosis — the biological basis for its notoriously poor response and the search for non-cytotoxic strategies."
  - target: 01-human/03-molecular/pth
    relation: connects-to
    note: "Paraneoplastic hypercalcaemia: OCCC is the gynaecological cancer most associated with humoral hypercalcaemia of malignancy, secreting PTHrP that mimics parathyroid hormone to drive the elevated calcium seen at presentation."
  - target: 01-human/03-molecular/thrombin
    relation: connects-to
    note: "Venous thromboembolism: OCCC carries the highest rate of venous thromboembolism among ovarian histotypes, its tissue-factor-rich tumour cells triggering thrombin generation and the deep-vein thromboses and pulmonary emboli that complicate the disease."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Platinum resistance: ovarian clear-cell carcinoma is notoriously chemoresistant, and upregulation of anti-apoptotic BCL-2-family proteins raises the threshold for the caspase-mediated death triggered by platinum chemotherapy, underpinning its poor response."
  - target: 01-human/03-molecular/mlh1
    relation: connects-to
    note: "Mismatch-repair subset: a fraction of ovarian clear-cell carcinomas are MLH1-deficient and microsatellite-instable, often Lynch-associated, generating the high neoantigen load that makes this histotype subset responsive to checkpoint blockade."
  - target: 01-human/03-molecular/epas1
    relation: connects-to
    note: "Hypoxia and clear-cell phenotype: HIF-2α/EPAS1 stabilisation drives the angiogenic, glycogen-laden clear-cell morphology of OCCC, the hypoxic transcriptional programme it shares with clear-cell renal carcinoma."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Cell-cycle progression: the cyclin-D1-CDK4/6 axis (both mapped) releases E2F1 to drive the proliferation of ovarian clear cell carcinoma."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "MAPK signalling: KRAS and MET (both mapped) activate the MAPK-ERK cascade contributing to the growth of ovarian clear cell carcinoma."
  - target: 01-human/03-molecular/cdh1
    relation: connects-to
    note: "EMT and invasion: loss of E-cadherin during epithelial-mesenchymal transition promotes the invasion of ovarian clear cell carcinoma, a tumour arising from endometriotic epithelium."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Endometriosis inflammation: IL-6-JAK-STAT3 signalling (IL-6 and STAT3 already mapped) from the endometriosis-associated inflammatory milieu drives the development and chemoresistance of ovarian clear cell carcinoma."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Iron-driven innate inflammation: TLR-MyD88-NF-κB innate signalling (NF-κB already mapped), driven by the iron and inflammation of endometriotic cysts, contributes to the malignant transformation underlying ovarian clear cell carcinoma."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Cell-cycle drive: RB-pathway dysregulation (CDK4/6, cyclin-D1 and E2F1 already mapped) contributes to the cell-cycle progression of ovarian clear cell carcinoma."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 contributes to the adhesion, chemoresistance and immune evasion of ovarian clear cell carcinoma."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β mapped) modulates invasion and the immunosuppressive microenvironment of ovarian clear cell carcinoma."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "PDGF signalling drives the stromal and angiogenic responses of the endometriosis-associated ovarian clear cell carcinoma."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the immune microenvironment of the often chemoresistant ovarian clear cell carcinoma, relevant to its immunotherapy."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors, antagonised by the PIK3CA-AKT signalling characteristic of this subtype, modulate the survival of ovarian clear cell carcinoma."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "CDKN2A loss releases CDK4/6-cyclin-D control (cyclin-D1 and RB1 already mapped) of the cell cycle in ovarian clear cell carcinoma."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the survival and Wnt signaling of the ARID1A-deficient ovarian clear cell carcinoma."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in ovarian clear cell carcinoma."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the endometriosis-associated inflammatory microenvironment of ovarian clear cell carcinoma."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of MET and growth-factor receptors (MET already mapped) contributes to the invasion of ovarian clear cell carcinoma."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation, alongside ARID1A loss (ARID1A already mapped), of ovarian clear cell carcinoma."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival of the ARID1A-deficient, oxidative-stress-adapted cells of ovarian clear cell carcinoma."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of ovarian clear cell carcinoma."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the immunosuppressive microenvironment of ovarian clear cell carcinoma."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated cytotoxic immunosurveillance is a component of the immune response to ovarian clear cell carcinoma."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the tumor-stromal interactions of ovarian clear cell carcinoma."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the endometriosis-associated inflammatory tumor microenvironment of ovarian clear cell carcinoma."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory tumor microenvironment of ovarian clear cell carcinoma."
  - target: 01-human/03-molecular/axl-receptor
    relation: connects-to
    note: "Chemoresistance driver: ovarian clear cell carcinoma is notoriously platinum-resistant, and the AXL receptor tyrosine kinase promotes the mesenchymal, drug-tolerant phenotype behind that resistance, a rational target where conventional cytotoxics underperform."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immunotherapy subset: a fraction of clear cell carcinomas are mismatch-repair-deficient and microsatellite-unstable, generating neoantigens presented on MHC class II that render this subset responsive to checkpoint blockade despite the tumour's general chemoresistance."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Endometriosis origin: clear cell carcinoma arises from endometriosis, an estrogen-driven lesion whose growth progesterone opposes, so the progesterone-signalling axis that governs endometriotic precursors underlies the tumour's characteristic epidemiology and hormonal context."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "MSI immunotherapy: IL-2-driven T-cell expansion underlies the immunotherapy of the mismatch-repair-deficient clear cell carcinomas (MHC class II already mapped) that respond to checkpoint blockade despite the tumour's general chemoresistance."
  - target: 01-human/03-molecular/ctla-4
    relation: connects-to
    note: "Checkpoint combination: CTLA-4 blockade, combined with PD-1 inhibition (already mapped), is being tested to boost responses in the immunogenic microsatellite-unstable subset of ovarian clear cell carcinoma."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Treatment cardiotoxicity: the platinum, taxane and anti-angiogenic therapy used in ovarian clear cell carcinoma can injure the heart, and troponin elevation helps detect the cardiac toxicity that complicates treatment of this chemoresistant tumour."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Anaemia: chronic disease, occult loss and platinum chemotherapy lower haemoglobin in ovarian clear cell carcinoma, and the anaemia adds to the fatigue that burdens patients with this often chemoresistant tumour."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive microenvironment: IL-10 in the tumour microenvironment dampens the anti-tumour T-cell response (CD8 and PD-1 already mapped), part of the immune evasion opposing the checkpoint therapy tested in the microsatellite-unstable subset."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Endometriosis oxidative stress: the endometriotic cysts from which ovarian clear cell carcinoma arises are iron-rich, and the oxidative stress (NRF2 already mapped), to which xanthine oxidase contributes, drives the carcinogenesis of this subtype."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Endometriosis inflammation: cyclooxygenase-2 and prostaglandin E2 drive the inflammation of the endometriotic cysts (IL-6 and IL-1 already mapped) from which ovarian clear cell carcinoma arises, part of its inflammation-driven carcinogenesis."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises the tumour-associated macrophages (already mapped) toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the immune microenvironment of the chemoresistant ovarian clear cell carcinoma."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Tumour vasculature: nitric oxide with VEGF (already mapped) regulates the vascular tone and angiogenesis of ovarian clear cell carcinoma, part of the stromal biology of this hypoxia-driven (HIF and EPAS1 already mapped) tumour."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage (already mapped) and type-2 milieu of the immunosuppressive microenvironment of the chemoresistant ovarian clear cell carcinoma."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Endometriosis iron and carcinogenesis: the cyclical haemorrhage of the endometriosis from which ovarian clear cell carcinoma arises loads the cyst with iron, whose iron-catalysed oxidative stress (xanthine oxidase already mapped) drives the malignant transformation."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Adipose and endometriosis: leptin links the obesity and the endometriosis-associated adipose milieu to the pathogenesis of ovarian clear cell carcinoma, part of the metabolic dimension of the tumour."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Endometriosis-adipose adipokine: adiponectin, with leptin (already mapped), is part of the adipose/endometriosis-associated adipokine dimension of the metabolic pathogenesis of ovarian clear cell carcinoma."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the endometriosis-associated adipose milieu of ovarian clear cell carcinoma."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Iron-regulatory anaemia: hepcidin, driven by the IL-6 (already mapped), governs the iron handling that, with the endometriosis iron (already mapped), contributes to the anaemia of ovarian clear cell carcinoma."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate antitumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment relevant to the immunotherapy of the (MSI/ARID1A-mutant already mapped) ovarian clear cell carcinoma."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm exploited by the checkpoint (PD-1 already mapped) immunotherapy of ovarian clear cell carcinoma."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response of the ovarian-clear-cell-carcinoma immune microenvironment."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of ovarian clear cell carcinoma."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the endometriosis-associated inflammatory microenvironment of ovarian clear cell carcinoma."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the ovarian-clear-cell-carcinoma microenvironment."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Endometriosis-associated mast cells: the mast cells, abundant in the endometriotic lesions from which the tumour arises, contribute to the angiogenesis (VEGF already mapped) and type-2 microenvironment of ovarian clear cell carcinoma."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 already mapped) contribute to the endometriosis-associated inflammatory microenvironment of ovarian clear cell carcinoma."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling recruits and polarises the myeloid cells to an immunosuppressive phenotype in the ovarian-clear-cell-carcinoma microenvironment."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Endometriosis iron: transferrin, the iron carrier, reflects the disordered handling of the free iron and haem of the endometriotic cysts whose oxidative DNA damage drives the ARID1A-mutant (already mapped) carcinogenesis of ovarian clear cell carcinoma."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement evasion: the ovarian-clear-cell-carcinoma cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped) within the endometriosis-associated inflammatory microenvironment."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, may mark the immune response of ovarian clear cell carcinoma."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Treatment anaemia: erythropoietin corrects the platinum- and taxane-induced anaemia in ovarian clear cell carcinoma therapy; EPOR expression on tumour cells raises the question of direct EPO-driven growth signalling."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Ascites pain mediator: bradykinin accumulates in the malignant ascites of ovarian clear cell carcinoma, activating B1/B2 receptors on the peritoneal mesothelium and sensory fibres to drive the pelvic pain that often delays diagnosis."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement brake: C1-esterase inhibitor modulates the classical complement pathway within the endometriosis-associated peritoneal milieu of ovarian clear cell carcinoma, limiting the C3/C5 (already mapped) complement cascade."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Stroma alarmin: TSLP released by the endometriosis-derived epithelium and peritoneal stroma activates mast cells (already mapped) and dendritic cells to shape the type-2 microenvironment of ovarian clear cell carcinoma."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Endometriosis mast-cell mediator: histamine released by mast cells (already mapped) in endometriotic lesions promotes VEGF angiogenesis and prostaglandin-mediated immune evasion in the ovarian-clear-cell-carcinoma peritoneal microenvironment."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Endometriosis stroma scaffold: periostin, upregulated in the endometriosis-derived stroma, promotes tumour cell adhesion, peritoneal invasion and desmoplastic ECM remodelling of ovarian clear cell carcinoma."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "OCCC melatonin: melatonin suppresses ovarian-clear-cell-carcinoma proliferation by inhibiting the PI3K/AKT (already mapped) and mTOR (already mapped) pathways through MT1/MT2-mediated cAMP suppression, counteracting the ARID1A-driven (already mapped) carcinogenesis."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "OCCC androgen axis: testosterone via androgen receptor promotes ovarian-clear-cell-carcinoma proliferation and intersects the PI3K/AKT (already mapped) and mTOR (already mapped) pathways upregulated in the ARID1A (already mapped)-mutant clear cell carcinoma."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "OCCC ascites serotonin: serotonin accumulates in the clear-cell-carcinoma peritoneal ascites and activates 5-HT receptors on peritoneal deposits to promote adhesion and mTOR (already mapped)-driven proliferation in the ovarian-clear-cell-carcinoma microenvironment."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "OCCC prolactin: prolactin via JAK2/STAT3 activates ovarian-clear-cell-carcinoma cells and macrophages (already mapped), amplifying mTOR (already mapped) and NF-κB (already mapped)-driven proliferation in the ARID1A (already mapped)-deficient microenvironment."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "OCCC oxytocin: oxytocin receptors on ovarian-clear-cell-carcinoma cells couple to Gαq-PKC, cross-activating mTOR (already mapped) and PI3K/AKT (already mapped) proliferative cascades in the chemoresistant ARID1A (already mapped)-mutant microenvironment."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "OCCC vasopressin: vasopressin via V1a receptors on ovarian-clear-cell-carcinoma stroma activates Gαq-PKC-IP3 signalling, converging on mTOR (already mapped) and NF-κB (already mapped) pro-survival cascades in the peritoneal implantation microenvironment."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "OCCC selenium: selenium, as GPx in macrophages (already mapped) and T-cytotoxic cells (already mapped), scavenges ROS in the OCCC tumour microenvironment; selenium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) pro-tumour cascade."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "OCCC iodine: iodine-dependent thyroid hormones regulate macrophage (already mapped) polarisation and T-cytotoxic (already mapped) immune surveillance; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) pro-tumour cascade of OCCC."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "OCCC sodium: excess sodium promotes macrophage (already mapped) and mast-cell (already mapped) pro-inflammatory activation; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) skewing amplifies the T-cytotoxic (already mapped) anti-tumour suppression in OCCC."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "OCCC copper: copper-dependent enzymes in macrophages (already mapped) and T-cytotoxic cells (already mapped) sustain tumour-immune crosstalk; copper excess amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade and mast-cell (already mapped) skewing in OCCC."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "OCCC potassium: potassium efflux gates the macrophage (already mapped) and mast-cell (already mapped) NLRP3 inflammasome; potassium loss amplifies NF-κB (already mapped) and IL-6 (already mapped) pro-tumour cascade and suppresses T-cytotoxic (already mapped) killing in OCCC."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "OCCC phosphorus: phosphorus-dependent ATP in macrophages (already mapped) and T-cytotoxic cells (already mapped) sustains immune surveillance; phosphorus dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) pro-tumour signalling cascade in OCCC."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "OCCC carbon: carbon, as metabolic backbone of lipids and HIF-1α (already mapped) signalling in clear-cell tumour and macrophages (already mapped), drives tumour metabolism; carbon dysregulation amplifies IL-6 (already mapped) and VEGF (already mapped) cascade in OCCC."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "OCCC chloride: chloride channels in macrophages (already mapped) and T-cytotoxic-cell (already mapped) modulate tumour-immune homeostasis; chloride dysregulation amplifies IL-6 (already mapped) and VEGF (already mapped) pro-tumour cascade in OCCC."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "OCCC hydrogen: hydrogen, via redox homeostasis in macrophages (already mapped) and T-cytotoxic-cell (already mapped), quenches tumour ROS; hydrogen dysregulation amplifies HIF-1α (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in OCCC."
---

# Ovarian Clear Cell Carcinoma

## Overview

**Ovarian clear cell carcinoma (OCCC)** is a distinct histological and molecular subtype of epithelial ovarian cancer characterized by clear cytoplasm (glycogen-rich), hobnail cells, and a unique molecular profile dominated by **ARID1A** and **PIK3CA** mutations. OCCC is strongly associated with endometriosis (~40% of cases arise from endometriotic cysts) and is relatively resistant to standard platinum-based chemotherapy compared to high-grade serous ovarian carcinoma (HGSOC). It has a unique geographic distribution with significantly higher incidence in East Asian women, and remains one of the most therapeutically challenging gynecologic malignancies due to the absence of FDA-approved targeted therapies [^jones-2010-arid1a-occc].

**Epidemiology:**
- Frequency: ~10-12% of all epithelial ovarian cancers in Western populations; ~15-25% in Japan and East Asia
- Geographic/ethnic disparity: Japanese women: ~25% of ovarian cancers are clear cell; Caucasian women: ~5-8%; genetic predisposition and endometriosis prevalence differences explain part of this disparity
- Incidence: ~2,000-2,500 cases/year USA; ~5,000-6,000 in Japan
- Median age: ~50-55 years (younger than HGSOC, median ~60 years)
- Association with endometriosis: ~40% of OCCC arise within or adjacent to endometriotic cysts (endometriomas); endometriosis-associated OCCC: slightly better prognosis; lower CA-125 at presentation
- Germline predisposition: BRCA1/2 pathogenic variants confer HGSOC risk, not OCCC-specific risk; Lynch syndrome (MSH2) predisposes to endometrioid and OCCC subtypes

**Contrast with HGSOC:**

| Feature | OCCC | HGSOC |
|---|---|---|
| BRCA1/2 mutations | ~2-5% | ~15-20% |
| TP53 mutations | ~5-10% | ~95% |
| ARID1A mutations | ~50-55% | <5% |
| PIK3CA mutations | ~40-50% | ~3-5% |
| HER2 amplification | <5% | ~20% |
| Platinum sensitivity | ~20-30% | ~70-80% |
| Taxane sensitivity | Moderate | High |
| CA-125 at diagnosis | Often normal | Usually elevated |
| Stage at diagnosis | Often early (I-II) | Usually late (III-IV) |

## Structure

### Molecular landscape of OCCC

**Hallmark mutations:**

**ARID1A (~50-55%):** [^jones-2010-arid1a-occc]
Truncating mutations in exons 8-18; biallelic LOF in most cases; BAF250A protein lost by IHC; disrupts cBAF complex → EZH2/PRC2 gains access → H3K27me3 accumulation → silencing of differentiation and tumor suppressor genes; ARID1A-mutant tumors are EZH2-dependent; enriched in endometriosis-associated OCCC

**PIK3CA (~40-50%):**
Activating mutations: E542K, E545K (helical domain) and H1047R/L (kinase domain); → PI3K p110α activation → AKT/mTOR → proliferation and survival; co-mutation with ARID1A in ~25-30% of OCCC; PIK3CA mutation is the main kinase driver in OCCC (in contrast to HGSOC which lacks PIK3CA-activating mutations)

**KRAS (~15%):**
G12D/V activating mutations; KRAS + ARID1A co-mutation in ~8-10%; KRAS-mutant OCCC: MEK/ERK pathway driven; MEK inhibitors explored; KRAS mutations more common in endometriosis-associated OCCC

**PPP2R1A (~5-8%):**
Regulatory subunit of PP2A phosphatase; mutations → PP2A inactivation → AKT/mTOR persistence; less common than HGSOC (PPP2R1A ~15% in HG endometrioid)

**TP53 (~5-10%):**
Strikingly lower than HGSOC (~95%); TP53 wildtype is a key molecular feature of OCCC; helps distinguish from HGSOC in ambiguous cases

**TERT promoter mutations (~15%):**
Activating TERT promoter mutations; longer telomere maintenance; associated with more aggressive OCCC behavior

**MYC amplification (~10%):**
Associates with ARID1A-mutant OCCC; predicts worse outcomes; MYC overexpression through CTNNB1-independent mechanisms

### Histology

**Classic OCCC features:**
- **Clear cell pattern**: large polyhedral cells with abundant clear cytoplasm (glycogen by PAS staining); nuclear pleomorphism moderate; "fried egg" nuclei with prominent single nucleolus
- **Hobnail pattern**: cells with bulging nuclei protruding into glandular lumina; nuclei appear above the cytoplasm plane
- **Papillary/tubulocystic pattern**: papillae with hyalinized cores lined by hobnail cells; characteristic of OCCC
- Low mitotic rate; necrosis variable; psammoma bodies absent (unlike serous tumors)

**IHC for OCCC:**
- **Napsin A**: positive in ~80-90% of OCCC; most sensitive single marker; also positive in lung adenocarcinoma (helpful for primary site)
- **HNF1β**: positive in ~80-85% of OCCC; nuclear; also expressed in some endometrioid tumors
- **ARID1A (BAF250A)**: LOST in ~50% (protein loss = ARID1A mutation)
- **WT1**: negative in OCCC (contrast HGSOC: strongly WT1-positive)
- **ER/PR**: negative/focal (contrast endometrioid: often ER/PR-positive)
- **p53**: wild-type pattern (contrast HGSOC: aberrant p53 overexpression or complete null)
- **PAX8**: positive in most OCCC (Müllerian origin marker)

## Function

### Endometriosis → OCCC carcinogenesis

The transition from endometriosis to OCCC follows a defined molecular sequence:
1. **Ectopic endometrium** (endometriotic cyst/endometrioma): cyclic hemorrhage → iron deposition → oxidative stress → mutagenic environment
2. **Atypical endometriosis**: ARID1A mutation + PIK3CA mutation appear first; early clonal expansion without overt malignancy; transition lesion
3. **OCCC in situ** (clear cell glandular neoplasia): increasing nuclear atypia; stromal invasion begins
4. **Invasive OCCC**: full OCCC; additional mutations in TERT, MYC amplification, TP53 (rare late event)

**Iron-mediated mutagenesis:**
Endometrioma fluid contains high concentrations of free iron (from RBC hemoglobin degradation) → Fenton reaction → hydroxyl radical production → oxidative DNA damage → ARID1A and PIK3CA mutations preferentially acquired (mechanism of mutagenic specificity incompletely understood)

**HIF-1α in endometriosis:**
Ectopic endometrium is hypoxic → HIF-1α activation → VEGF, PDGF → angiogenesis and survival; endometriosis-derived OCCC expresses HIF-1α targets constitutively

## Pathology

### Staging and treatment

**Staging:** FIGO staging (same as all epithelial ovarian cancers)
- Stage I (~35-40% of OCCC at diagnosis — higher than HGSOC due to endometrioma detection): best prognosis; 5-year OS ~80-90%
- Stage II (~10-15%): 5-year OS ~60-70%
- Stage III (~35-40%): 5-year OS ~25-40%
- Stage IV (~10-15%): 5-year OS ~15-25%

**Surgery:**
Comprehensive surgical staging (TAH-BSO, omentectomy, pelvic/para-aortic lymphadenectomy, peritoneal biopsy) for apparent early-stage disease; cytoreductive surgery for advanced stage; complete cytoreduction (R0) critical for improved OS; OCCC tends to have fewer peritoneal implants than HGSOC → surgical debulking feasible in more cases

**First-line chemotherapy:**
- **Standard**: carboplatin + paclitaxel × 6 cycles (as per HGSOC)
- **Platinum resistance**: ~40-60% of OCCC are platinum-resistant or -refractory (vs ~20% in HGSOC); especially stage III-IV
- **Irinotecan + cisplatin** (irinotecan-cisplatin, IC): Japanese GCIG trial showed IC equivalent to CP in OCCC; IC preferred in Japan for OCCC; irinotecan may exploit OCCC-specific DNA repair defect
- **Bevacizumab**: benefit in OCCC less established than HGSOC; GOG-218 and ICON7 included OCCC but subgroup benefit unclear; used in some guidelines for stage III-IV

**PARP inhibitors:**
- BRCA1/2 mutation rare in OCCC (~2-5%); HRD (homologous recombination deficiency) low in OCCC (~15-20% vs ~50% in HGSOC)
- ARIEL3 (rucaparib maintenance): OCCC had lowest benefit among epithelial ovarian subtypes
- However, ARID1A LOF → partial HR defect → exploratory role for PARP inhibitors in ARID1A-mutant OCCC

**EZH2 inhibitors:** [^kim-2015-arid1a-ezh2]
- Tazemetostat: Phase 2 trials in ARID1A-mutant solid tumors including OCCC ongoing; ORR data pending (NCT04171700); rationale from ARID1A LOF → EZH2 dependency
- Combination tazemetostat + PARP inhibitor (olaparib): Phase 1/2 being explored

**mTOR inhibitors:**
- Rationale: PIK3CA mutations in ~40-50% → mTOR pathway hyperactivation
- Temsirolimus monotherapy Phase 2 (OCCC-enriched): ORR ~10-15%; DCR ~30-40%
- Combination mTOR + MEK (for KRAS-PIK3CA co-mutation): exploratory
- Alpelisib (PIK3CA inhibitor): breast cancer-approved; being explored in PIK3CA-mutant OCCC

**Immunotherapy:**
- OCCC TMB: moderate (~5-8 mut/Mb); PD-L1: expressed in ~30-40%
- KEYNOTE-100 (pembrolizumab in recurrent OC): OCCC subgroup ORR ~15-17% (higher than HGSOC ~8%)
- ARID1A-mutant OCCC → PD-L1 upregulated → higher ICB response: preclinical rationale supported
- Pembrolizumab + bevacizumab: Phase 2 showing activity in recurrent OCCC; ORR ~25-30% in PD-L1+ cases
- Durvalumab + olaparib combination: GOG 3032 (MEDUSA) includes OCCC cohort

**CDK4/6 inhibitors:**
- OCCC co-expresses CDK4/6 via CCND1 upregulation; palbociclib Phase 2 in OCCC with CDK pathway activation

**Prognosis by stage and molecular subtype:**
- Early-stage (I-II): 5-year OS ~70-85%; early detection via endometrioma surveillance recommended
- Advanced (III-IV): 5-year OS ~20-35%; significantly worse than HGSOC at same stage due to platinum resistance
- ARID1A-mutant vs WT: ARID1A mutation alone not independently prognostic; combined with PIK3CA → worse prognosis
- Endometriosis-associated OCCC: slightly better prognosis than de novo OCCC (detected at earlier stage)
- Recurrent disease: median PFS 2nd line ~4-6 months; few effective options; clinical trial enrollment strongly recommended

## Connections

- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A (BAF250A) is mutated in ~50% of OCCC; biallelic ARID1A LOF → cBAF disruption; ARID1A IHC (BAF250A, clone PSG3) protein loss is a surrogate diagnostic marker in OCCC; ARID1A + PIK3CA co-mutation in ~25-30% OCCC defines the highest-risk molecular subgroup.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — ARID1A LOF disrupts cBAF → EZH2/PRC2 accesses ARID1A-target loci → H3K27me3 accumulation; OCCC with ARID1A LOF shows EZH2 dependency in preclinical models; tazemetostat under investigation in ARID1A-mutant OCCC; EZH2 + PARP inhibitor combination explored.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — ARID1A + PIK3CA co-mutation defines ~25-30% of ovarian clear cell carcinomas; PIK3CA → PI3K/AKT/mTOR → OCCC proliferation; ARID1A LOF + PIK3CA creates synthetic vulnerability to dual PI3K/mTOR inhibition; temsirolimus active in PIK3CA-mutant OCCC Phase 2.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — ARID1A LOF in OCCC → PD-L1 upregulation via MLH1 suppression and IFN-γ signaling pathway enhancement; OCCC has higher PD-L1 expression than high-grade serous ovarian cancer; pembrolizumab + bevacizumab shows activity in PD-L1+ OCCC; durvalumab combination trials ongoing.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — PIK3CA mutations (~40-50%) in OCCC → PI3K/AKT → mTOR activation; temsirolimus Phase 2 in OCCC: ORR ~10-15%; alpelisib (PIK3CA inhibitor) explored in PIK3CA-mutant OCCC; PI3K/mTOR dual inhibitors studied; ARID1A LOF + PIK3CA → synthetic vulnerability to PI3K/mTOR inhibition.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — KRAS G12D/V mutations in ~15% of OCCC, enriched in endometriosis-associated OCCC; KRAS + ARID1A co-mutation in ~8-10%; MEK pathway activated in KRAS-mutant OCCC → MEK inhibitors explored; KRAS mutation is more prevalent in OCCC than HGSOC or endometrioid ovarian cancer.
- `connects-to` → **[Ovarian Cancer](../ovarian-cancer/README.md)** — OCCC is distinct from HGSOC: OCCC (ARID1A/PIK3CA-driven, platinum-resistant, stage I-II at ~35-40%) vs HGSOC (TP53-universal, platinum-sensitive, stage III-IV at ~75%); OCCC lacks HRD enrichment; 5-year OS in advanced OCCC is worse than HGSOC despite identical chemotherapy.
- `connects-to` → **[Endometrial Cancer](../endometrial-cancer/README.md)** — Ovarian clear cell carcinoma and endometrioid endometrial cancer are both endometriosis/endometrium-derived tumors driven by ARID1A and PIK3CA; clear-cell and endometrioid histologies recur across ovary and uterus, and both can arise in Lynch syndrome — unlike serous cancers.
- `connects-to` → **[Renal Cell Carcinoma](../renal-cell-carcinoma/README.md)** — Ovarian clear cell carcinoma and clear-cell renal cell carcinoma are unrelated organs sharing a look and biology: both have glycogen-rich clear cytoplasm, both upregulate HIF/VEGF, and OCCC borrows RCC anti-angiogenics like sunitinib for this platinum-resistant tumor.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Ovarian clear cell carcinoma is more immunogenic than high-grade serous cancer: ARID1A loss raises neoantigens and PD-L1, so it draws cytotoxic CD8+ T cells and responds better to PD-1 blockade — pembrolizumab + bevacizumab is studied in PD-L1+ OCCC.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Ovarian clear cell carcinoma has the highest venous thromboembolism rate of any ovarian cancer—up to a quarter of patients: the tumor is strongly prothrombotic (tissue factor, IL-6), so DVT and pulmonary embolism are watched and often prophylaxed throughout treatment.
- `connects-to` → **[Lynch Syndrome](../lynch-syndrome/README.md)** — Clear-cell and endometrioid ovarian cancers are the histologies linked to Lynch syndrome: mismatch-repair deficiency underlies a share of OCCC, so MMR/MSI testing both flags a germline syndrome and identifies tumors that may respond to checkpoint blockade.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Ovarian clear cell carcinoma is the ovarian cancer most tied to endometriosis: ectopic endometrial tissue, under oxidative iron-rich stress, acquires ARID1A and PIK3CA mutations and transforms—making endometriosis a recognized precursor in the reproductive tract.
- `connects-to` → **[Gastric Cancer](../gastric-cancer/README.md)** — Ovarian clear-cell carcinoma and gastric cancer share ARID1A loss: this SWI/SNF chromatin-remodeler tumor suppressor is among the most mutated genes in both, showing how chromatin disruption—not classic oncogenes—drives diverse epithelial cancers.
- `connects-to` → **[Cholangiocarcinoma](../cholangiocarcinoma/README.md)** — Ovarian clear-cell carcinoma and cholangiocarcinoma converge on chromatin-remodeling defects: both frequently lose ARID1A, and both are relatively chemoresistant epithelial cancers—making epigenetic vulnerabilities (EZH2 inhibition) a shared therapeutic avenue.
- `connects-to` → **[Hereditary Breast and Ovarian Cancer](../hereditary-breast-ovarian-cancer/README.md)** — Ovarian clear-cell carcinoma differs from the BRCA-driven cancers of HBOC: unlike high-grade serous ovarian cancer, clear-cell is rarely BRCA/HRD-related (it's ARID1A/PIK3CA-driven), so it responds poorly to platinum and PARP inhibitors—a key treatment distinction.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — OCCC is driven by PI3K-pathway and chromatin gene mutations: ARID1A loss with PIK3CA or PTEN alterations activates PI3K/AKT/mTOR growth signaling, distinguishing clear cell carcinoma's biology—and rationale for mTOR/PI3K-targeted trials—from high-grade serous cancer.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — OCCC tends to be immunologically distinct and PD-L1-expressing: among ovarian cancers, clear cell carcinoma more often shows mismatch-repair/ARID1A features and immune infiltration, so NK and T-cell-engaging immunotherapy is of interest in this platinum-resistant subtype.
- `connects-to` → **[VHL Disease](../vhl-disease/README.md)** — OCCC shares clear-cell morphology and biology with renal clear cell carcinoma: glycogen-rich clear cytoplasm and HIF/VEGF-driven angiogenesis link it to VHL-associated kidney cancer, so anti-angiogenic agents are explored across these histologically similar tumors.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — Ovarian clear cell carcinoma is characteristically p53-wildtype: unlike high-grade serous ovarian cancer, which is defined by TP53 mutation, OCCC is driven instead by ARID1A and PIK3CA—so p53 status helps distinguish these biologically distinct ovarian cancers.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Ovarian clear cell carcinoma resists platinum chemo but its ARID1A loss links to immunotherapy: ARID1A-mutant or mismatch-repair-deficient tumors can respond to checkpoint blockade, offering an option in this otherwise chemoresistant subtype.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — OCCC's clear cytoplasm reflects HIF-driven metabolism: a stabilized hypoxia program reprograms cells toward glycolysis and glycogen storage (the 'clear' look), and this metabolic state contributes to the platinum chemoresistance that makes OCCC hard to treat.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Clear-cell ovarian cancer is the gynecologic tumor most linked to hypercalcemia: it can drive paraneoplastic high calcium (via PTH-related peptide), so an ovarian mass with unexplained hypercalcemia points toward this histotype.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — Clear-cell ovarian cancer often overproduces IL-6: this cytokine drives paraneoplastic fever, thrombocytosis and an inflammatory state, contributing to the thrombosis risk and the relative chemoresistance that set this subtype apart.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Clear-cell ovarian cancer grows from an endometriotic niche rich in fibroblasts: the cyst's reactive stroma and chronic inflammation foster ARID1A-mutant transformation, so the fibroblast-laden microenvironment is part of how this cancer begins.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Ovarian clear cell carcinoma is forged in iron: it arises from endometriosis, where repeated bleeding dumps iron into cysts, and the resulting oxidative stress damages DNA and drives the ARID1A-mutant cancer—linking menstrual iron to a tumor.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Ovarian clear cell carcinoma is intensely angiogenic via VEGF: HIF-driven VEGF feeds its blood supply, so anti-VEGF bevacizumab is among the few systemic options for a tumor notoriously resistant to standard chemotherapy.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Iron-laden macrophages haunt clear cell carcinoma's origin: in the endometriotic cysts it springs from, macrophages gorge on blood-derived iron and pump out inflammatory signals, building the oxidative, pro-tumor niche the cancer exploits.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Clear cell ovarian carcinoma behaves as if starved of oxygen: its glycogen-packed clear cells run a HIF-driven pseudohypoxic program even when oxygen is present, fueling growth and the chemoresistance that makes this subtype so hard to treat.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Clear cell ovarian carcinoma spreads across the peritoneum: like other ovarian cancers it studs the omentum and bowel surface, so abdominal disease and bowel involvement shape its presentation and the surgery aimed at removing all visible tumor.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells matter most in the immunogenic subset of clear cell ovarian carcinoma: some tumors carry mismatch-repair defects and neoantigens, and antigen-presenting dendritic cells help mount the response that checkpoint therapy can amplify.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Clear cell ovarian carcinoma mirrors kidney cancer: it shares the HIF-driven clear-cell biology of renal clear cell carcinoma, and as a pelvic mass it can obstruct the ureters and kidneys.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Clear cell ovarian carcinoma is hypervascular: HIF and VEGF drive endothelial cells to build a rich blood supply, like its renal counterpart, a feature anti-angiogenic therapy targets.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Clear cell ovarian carcinoma is born in endometriosis: it arises within fibrotic, blood-stained endometriotic cysts, whose chronic inflammation and scarring set the stage for malignant transformation.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy explains the 'clear' in clear cell: the cytoplasm is packed with glycogen that dissolves away in processing, leaving the empty, water-clear cells and bulging hobnail nuclei that name the tumor.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Clear cell carcinoma is the great clotter of ovarian cancers: it carries the highest rate of venous thromboembolism, activating platelets and the clotting cascade so strongly that a deep vein thrombosis can be the first sign of the tumor.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — When clear cell carcinoma spreads beyond the pelvis, the liver is a frequent target: hematogenous metastases lodge there, and liver involvement marks the advanced, chemoresistant disease that makes this subtype so hard to treat.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Even a platinum-resistant tumor exacts a neural toll: OCCC is treated up front with carboplatin and paclitaxel, and the taxane in particular injures peripheral sensory neurons, leaving lasting numbness despite the subtype's poor chemo response.
- `connects-to` → **[Albumin](../../03-molecular/albumin/README.md)** — OCCC announces itself with fluid: like other ovarian cancers it seeds the peritoneum and produces malignant ascites, while tumor burden and poor nutrition drive down blood albumin, a marker that tracks with worse outcomes.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — OCCC can reach the chest: advanced disease produces malignant pleural effusions and lung metastases, the thoracic spread that defines stage IV and signals the hard-to-treat end of this subtype.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibody stains pin down the subtype: HNF1B and Napsin A staining with loss of ARID1A confirm clear-cell histology and its endometriosis origin, separating OCCC from the high-grade serous tumors that demand different treatment.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — This subtype resists platinum, so the marrow still pays: the carboplatin-paclitaxel given despite OCCC's chemoresistance is myelosuppressive, dropping neutrophils between cycles, while a high neutrophil-to-lymphocyte ratio flags its poorer prognosis.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Platinum therapy wastes magnesium: carboplatin injures the kidney tubule that reclaims it, so blood magnesium and potassium fall and must be replaced through the cycles, even as OCCC responds less well to that platinum than other ovarian cancers.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — OCCC turns up its antioxidant defenses: chronically bathed in oxidative stress, the tumor activates the NRF2 pathway to neutralize reactive oxygen, an adaptation that also helps explain its notorious resistance to platinum chemotherapy.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT is OCCC's growth engine: frequent PIK3CA mutations and PTEN loss funnel through AKT to mTOR, a dominant signaling axis in clear cell ovarian cancer and a target for PI3K-pathway inhibitors in this hard-to-treat subtype.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — ARID1A loss makes OCCC visible to the immune system: the resulting mutational and microsatellite instability draws in T cells, so clear cell ovarian cancer responds to checkpoint immunotherapy more often than the commoner serous type.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — It is born from an estrogen-driven lesion: clear cell ovarian cancer arises within endometriosis, where estrogen-fueled ectopic endometrial tissue and its iron-rich bleeding create the inflamed, mutagenic niche that gives rise to the tumor.
- `connects-to` → **[MET](../../03-molecular/met/README.md)** — A receptor kinase offers a handle on a chemoresistant tumor: MET amplification and activation help drive clear cell ovarian cancer, which resists standard platinum chemotherapy, so MET and its PI3K-pathway partners are pursued as targets.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — The tumor balances its immune visibility with suppression: even as ARID1A loss recruits T cells, regulatory T cells and an immunosuppressive microenvironment temper the response, shaping which clear cell tumors actually benefit from checkpoint blockade.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 marks the clear-cell subtype: OCCC is notably IL-6-high, and the downstream STAT3 activation drives growth, the paraneoplastic inflammation, and the platinum resistance that distinguish it from serous ovarian cancer.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Chronic inflammation switches on NF-κB: born in an inflamed endometriotic niche, OCCC carries constitutive NF-κB activity that supports survival and contributes to its resistance to chemotherapy.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Advanced pelvic disease invites sepsis: bowel obstruction and perforation from peritoneal spread, plus chemotherapy neutropenia, expose patients to intra-abdominal infection and sepsis.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Lost SWI/SNF control drives the cell cycle: ARID1A loss in OCCC dysregulates cyclin D1 and cell-cycle entry, contributing to the proliferation of this chemoresistant clear-cell subtype.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Pelvic disease and platinum strain the kidneys: tumor obstructing the ureters causes hydronephrosis, and the cisplatin used against this resistant cancer is nephrotoxic, together risking chronic kidney disease.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Chronic inflammation and chemo drain the blood: born of inflamed endometriosis and treated with marrow-suppressing platinum, OCCC commonly produces an anemia of chronic disease.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Removing the ovaries withdraws bone-protective estrogen: surgery and chemotherapy for OCCC throw younger patients into abrupt menopause, and the estrogen loss accelerates bone thinning toward osteoporosis.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A chemoresistant cancer in young women weighs on mood: OCCC's poor response to platinum at recurrence, frequent advanced presentation and abrupt surgical menopause contribute to substantial depression and anxiety.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Salvage anthracyclines can weaken the heart: because OCCC resists platinum, recurrent disease is often treated with pegylated liposomal doxorubicin, whose cumulative cardiotoxicity can erode cardiac function into heart failure.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Its taxane-platinum chemo numbs the nerves: the paclitaxel and carboplatin used first-line in OCCC cause a dose-dependent, often lasting peripheral neuropathy with painful paraesthesiae.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Cytoreductive surgery heals slowly: the staging and debulking surgery for OCCC, sometimes extensive and in malnourished patients, leaves abdominal wounds prone to dehiscence and delayed closure.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A chemoresistant cancer breeds worry: the platinum resistance, recurrence risk and tumour-marker surveillance of OCCC foster chronic health anxiety alongside depression.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It classically raises the calcium: ovarian clear cell carcinoma is the gynaecological tumour most associated with paraneoplastic hypercalcaemia, and its oophorectomy forces surgical menopause.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It reaches the chest: advanced OCCC causes malignant pleural effusions through diaphragmatic spread, and its strong thrombotic tendency raises the risk of pulmonary embolism.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It arises from endometriosis and spreads on the peritoneum: OCCC develops from endometriotic cysts and, as it advances, seeds the peritoneum to cause ascites and bowel obstruction.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It spreads to the deep nodes: ovarian clear cell carcinoma disseminates to pelvic and para-aortic lymph nodes, so lymphadenectomy is part of its surgical staging.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — It is intensely prothrombotic: OCCC carries one of the highest venous thromboembolism rates of any cancer, straining the circulation with deep-vein thrombosis and pulmonary embolism.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Its high calcium and chemo reach the nerves: severe paraneoplastic hypercalcaemia causes confusion and lethargy, and the platinum chemotherapy it resists also causes peripheral neuropathy.
- `connects-to` → **[Renal System](../renal-system/README.md)** — A clear-cell cousin of kidney cancer, treated near the kidney: ovarian clear cell carcinoma shares clear-cell histology with renal cancer, and bulky pelvic spread plus cisplatin chemotherapy threaten the kidneys.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Chemoresistance drives a search for targets: ARID1A-mutant ovarian clear cell carcinoma resists platinum, so trials pursue immunotherapy and ATR or other targeted inhibitors.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Paraneoplastic hypercalcaemia draws on bone: ovarian clear cell carcinoma can secrete PTHrP causing hypercalcaemia that mobilises calcium from the skeleton.
- `connects-to` → **[Bladder Cancer](../bladder-cancer/README.md)** — A fellow ARID1A-driven cancer: like a subset of bladder cancer, ovarian clear cell carcinoma is frequently driven by ARID1A loss disrupting the SWI/SNF chromatin-remodelling complex.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — It still receives the standard regimen: carboplatin-paclitaxel is given after surgery, though ovarian clear cell carcinoma's relative platinum resistance makes complete response less common than in serous cancer.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Biomarkers favour immunotherapy here: ovarian clear cell carcinoma more often shows microsatellite instability and PD-L1 expression, making PD-1 checkpoint inhibitors a more promising option than in serous ovarian cancer.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — B-cell islands beyond the T cells: clear cell ovarian cancers that organise tertiary lymphoid structures with germinal-centre B cells mount a broader antitumour response and tend to fare better, adding to the T-cell infiltrate that already shapes ovarian-cancer outcome.
- `connects-to` → **[HCC](../hcc/README.md)** — A shared chromatin-remodeller defect: ARID1A, the SWI/SNF subunit mutated in roughly half of clear cell ovarian cancers, is also among the commonest mutations in hepatocellular carcinoma—one epigenetic machinery failing across two organs.
- `connects-to` → **[Colorectal Cancer](../colorectal-cancer/README.md)** — Driven by the same oncogenes: clear cell ovarian cancers frequently carry KRAS and PIK3CA mutations that also drive colorectal cancer, so the RAS-PI3K signalling these tumours share guides targeted-therapy thinking across both.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — Peritoneal and bowel spread: like other ovarian cancers, clear-cell carcinoma seeds the peritoneum and infiltrates the bowel wall, though it more often presents as an early-stage pelvic mass arising from endometriosis.
- `connects-to` → **[HLRCC](../hlrcc/README.md)** — Clear cells and HIF across organs: OCCC, like HLRCC's renal cancer and clear-cell RCC, shows glycogen-rich clear cytoplasm and constitutive HIF/pseudohypoxia—a convergent clear-cell phenotype in different organs.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Lung and pleural metastasis: clear-cell ovarian carcinoma can spread to the lungs and pleura, seeding the alveolar bed in its chemoresistant advanced course.
- `connects-to` → **[Disseminated Intravascular Coagulation](../disseminated-intravascular-coagulation/README.md)** — The most thrombogenic ovarian cancer: clear-cell carcinoma carries the highest venous thromboembolism rate of the ovarian subtypes and can trigger Trousseau-type consumptive coagulopathy and DIC.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — HIF-driven vasculature: like clear-cell renal cancer, ovarian clear-cell carcinoma is intensely angiogenic through HIF and VEGF, building abnormal tumour arterial walls that antiangiogenic drugs target.
- `connects-to` → **[Mesothelioma](../mesothelioma/README.md)** — A peritoneal differential: peritoneal mesothelioma produces serosal masses, effusions and ascites that overlap with the peritoneal spread of ovarian clear-cell carcinoma, a distinction made on biopsy and markers.
- `connects-to` → **[YAP1](../../03-molecular/yap1/README.md)** — Hippo-YAP activation: ARID1A loss in ovarian clear-cell carcinoma deregulates the Hippo-YAP pathway, contributing to its growth and treatment resistance.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — Notch signalling: dysregulated Notch signalling participates in ovarian clear-cell carcinoma, an additional pathway alongside its ARID1A and PI3K alterations.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — Replicative immortality: TERT reactivation maintaining telomeres supports the persistent proliferation of ovarian clear-cell carcinoma, a notably chemoresistant tumour.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Proliferative oncogene: MYC activation drives the proliferation of ovarian clear-cell carcinoma, cooperating with its ARID1A and PIK3CA lesions.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — Cell-cycle drive: cyclin D-CDK4/6 activity propels ovarian clear-cell carcinoma cells through the G1 checkpoint, a candidate vulnerability in this chemoresistant tumour.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — Fibrosis and EMT: TGF-β signalling promotes the epithelial-mesenchymal transition and stromal remodelling that aid the invasion of ovarian clear-cell carcinoma.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — OCCC arises in an endometriotic, inflamed niche where CCL2 recruits monocytes that become the M2 tumor-associated macrophages sustaining this chemoresistant tumor—an immune-microenvironment driver beyond its ARID1A/PIK3CA genetics.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Chronic IL-1β signaling in endometriotic cysts drives the inflammatory microenvironment from which ovarian clear-cell carcinoma emerges, linking benign endometriosis to the malignant transformation that seeds this cancer.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — ARID1A loss in OCCC impairs mismatch repair and DNA-damage handling, raising mutational burden and cytosolic DNA that engage cGAS-STING—a rationale for the checkpoint blockade to which this subtype is relatively responsive.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — OCCC resists the platinum chemotherapy that controls high-grade serous disease, evading caspase-3-mediated apoptosis—the biological basis for its notoriously poor response and the search for non-cytotoxic strategies.
- `connects-to` → **[PTH](../../03-molecular/pth/README.md)** — OCCC is the gynecological cancer most associated with humoral hypercalcemia of malignancy, secreting PTHrP that mimics parathyroid hormone to drive the elevated calcium seen at presentation.
- `connects-to` → **[Thrombin](../../03-molecular/thrombin/README.md)** — OCCC carries the highest rate of venous thromboembolism among ovarian histotypes, its tissue-factor-rich tumor cells triggering thrombin generation and the deep-vein thromboses and pulmonary emboli that complicate the disease.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — Ovarian clear-cell carcinoma is notoriously chemoresistant, and upregulation of anti-apoptotic BCL-2-family proteins raises the threshold for the caspase-mediated death triggered by platinum chemotherapy, underpinning its poor treatment response.
- `connects-to` → **[MLH1](../../03-molecular/mlh1/README.md)** — A fraction of ovarian clear-cell carcinomas are MLH1-deficient and microsatellite-instable, often Lynch-associated, generating the high neoantigen load that makes this histotype subset responsive to checkpoint blockade.
- `connects-to` → **[EPAS1](../../03-molecular/epas1/README.md)** — HIF-2α/EPAS1 stabilization drives the angiogenic, glycogen-laden clear-cell morphology of OCCC, the hypoxic transcriptional program it shares with clear-cell renal carcinoma.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — The cyclin-D1-CDK4/6 axis (both mapped) releases E2F1 to drive the proliferation of ovarian clear cell carcinoma.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — KRAS and MET (both mapped) activate the MAPK-ERK cascade contributing to the growth of ovarian clear cell carcinoma.
- `connects-to` → **[CDH1](../../03-molecular/cdh1/README.md)** — Loss of E-cadherin during epithelial-mesenchymal transition promotes the invasion of ovarian clear cell carcinoma, a tumor arising from endometriotic epithelium.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — IL-6-JAK-STAT3 signaling (IL-6 and STAT3 already mapped) from the endometriosis-associated inflammatory milieu drives the development and chemoresistance of ovarian clear cell carcinoma.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR-MyD88-NF-κB innate signaling (NF-κB already mapped), driven by the iron and inflammation of endometriotic cysts, contributes to the malignant transformation underlying ovarian clear cell carcinoma.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — RB-pathway dysregulation (CDK4/6, cyclin-D1 and E2F1 already mapped) contributes to the cell-cycle progression of ovarian clear cell carcinoma.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 contributes to the adhesion, chemoresistance and immune evasion of ovarian clear cell carcinoma.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β mapped) modulates invasion and the immunosuppressive microenvironment of ovarian clear cell carcinoma.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — PDGF signaling drives the stromal and angiogenic responses of the endometriosis-associated ovarian clear cell carcinoma.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the immune microenvironment of the often chemoresistant ovarian clear cell carcinoma, relevant to its immunotherapy.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors, antagonized by the PIK3CA-AKT signaling characteristic of this subtype, modulate the survival of ovarian clear cell carcinoma.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A loss releases CDK4/6-cyclin-D control (cyclin-D1 and RB1 already mapped) of the cell cycle in ovarian clear cell carcinoma.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the survival and Wnt signaling of the ARID1A-deficient ovarian clear cell carcinoma.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in ovarian clear cell carcinoma.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the endometriosis-associated inflammatory microenvironment of ovarian clear cell carcinoma.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of MET and growth-factor receptors (MET already mapped) contributes to the invasion of ovarian clear cell carcinoma.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation, alongside ARID1A loss (ARID1A already mapped), of ovarian clear cell carcinoma.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival of the ARID1A-deficient, oxidative-stress-adapted cells of ovarian clear cell carcinoma.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of ovarian clear cell carcinoma.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the immunosuppressive microenvironment of ovarian clear cell carcinoma.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated cytotoxic immunosurveillance is a component of the immune response to ovarian clear cell carcinoma.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the tumor-stromal interactions of ovarian clear cell carcinoma.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the endometriosis-associated inflammatory tumor microenvironment of ovarian clear cell carcinoma.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory tumor microenvironment of ovarian clear cell carcinoma.
- `connects-to` → **[AXL receptor](../../03-molecular/axl-receptor/README.md)** — Chemoresistance driver: ovarian clear cell carcinoma is notoriously platinum-resistant, and the AXL receptor tyrosine kinase promotes the mesenchymal, drug-tolerant phenotype behind that resistance, a rational target where conventional cytotoxics underperform.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Immunotherapy subset: a fraction of clear cell carcinomas are mismatch-repair-deficient and microsatellite-unstable, generating neoantigens presented on MHC class II that render this subset responsive to checkpoint blockade despite the tumour's general chemoresistance.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — Endometriosis origin: clear cell carcinoma arises from endometriosis, an estrogen-driven lesion whose growth progesterone opposes, so the progesterone-signalling axis that governs endometriotic precursors underlies the tumour's characteristic epidemiology and hormonal context.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — MSI immunotherapy: IL-2-driven T-cell expansion underlies the immunotherapy of the mismatch-repair-deficient clear cell carcinomas (MHC class II already mapped) that respond to checkpoint blockade despite the tumour's general chemoresistance.
- `connects-to` → **[CTLA-4](../../03-molecular/ctla-4/README.md)** — Checkpoint combination: CTLA-4 blockade, combined with PD-1 inhibition (already mapped), is being tested to boost responses in the immunogenic microsatellite-unstable subset of ovarian clear cell carcinoma.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Treatment cardiotoxicity: the platinum, taxane and anti-angiogenic therapy used in ovarian clear cell carcinoma can injure the heart, and troponin elevation helps detect the cardiac toxicity that complicates treatment of this chemoresistant tumour.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Anaemia: chronic disease, occult loss and platinum chemotherapy lower haemoglobin in ovarian clear cell carcinoma, and the anaemia adds to the fatigue that burdens patients with this often chemoresistant tumour.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive microenvironment: IL-10 in the tumour microenvironment dampens the anti-tumour T-cell response (CD8 and PD-1 already mapped), part of the immune evasion opposing the checkpoint therapy tested in the microsatellite-unstable subset.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Endometriosis oxidative stress: the endometriotic cysts from which ovarian clear cell carcinoma arises are iron-rich, and the oxidative stress (NRF2 already mapped), to which xanthine oxidase contributes, drives the carcinogenesis of this subtype.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Endometriosis inflammation: cyclooxygenase-2 and prostaglandin E2 drive the inflammation of the endometriotic cysts (IL-6 and IL-1 already mapped) from which ovarian clear cell carcinoma arises, part of its inflammation-driven carcinogenesis.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises the tumour-associated macrophages (already mapped) toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the immune microenvironment of the chemoresistant ovarian clear cell carcinoma.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Tumour vasculature: nitric oxide with VEGF (already mapped) regulates the vascular tone and angiogenesis of ovarian clear cell carcinoma, part of the stromal biology of this hypoxia-driven (HIF and EPAS1 already mapped) tumour.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage (already mapped) and type-2 milieu of the immunosuppressive microenvironment of the chemoresistant ovarian clear cell carcinoma.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Endometriosis iron and carcinogenesis: the cyclical haemorrhage of the endometriosis from which ovarian clear cell carcinoma arises loads the cyst with iron, whose iron-catalysed oxidative stress (xanthine oxidase already mapped) drives the malignant transformation.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Adipose and endometriosis: leptin links the obesity and the endometriosis-associated adipose milieu to the pathogenesis of ovarian clear cell carcinoma, part of the metabolic dimension of the tumour.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Endometriosis-adipose adipokine: adiponectin, with leptin (already mapped), is part of the adipose/endometriosis-associated adipokine dimension of the metabolic pathogenesis of ovarian clear cell carcinoma.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the endometriosis-associated adipose milieu of ovarian clear cell carcinoma.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Iron-regulatory anaemia: hepcidin, driven by the IL-6 (already mapped), governs the iron handling that, with the endometriosis iron (already mapped), contributes to the anaemia of ovarian clear cell carcinoma.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate antitumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment relevant to the immunotherapy of the (MSI/ARID1A-mutant already mapped) ovarian clear cell carcinoma.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm exploited by the checkpoint (PD-1 already mapped) immunotherapy of ovarian clear cell carcinoma.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response of the ovarian-clear-cell-carcinoma immune microenvironment.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of ovarian clear cell carcinoma.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the endometriosis-associated inflammatory microenvironment of ovarian clear cell carcinoma.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the ovarian-clear-cell-carcinoma microenvironment.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Endometriosis-associated mast cells: the mast cells, abundant in the endometriotic lesions from which the tumour arises, contribute to the angiogenesis (VEGF already mapped) and type-2 microenvironment of ovarian clear cell carcinoma.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 already mapped) contribute to the endometriosis-associated inflammatory microenvironment of ovarian clear cell carcinoma.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling recruits and polarises the myeloid cells to an immunosuppressive phenotype in the ovarian-clear-cell-carcinoma microenvironment.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Endometriosis iron: transferrin, the iron carrier, reflects the disordered handling of the free iron and haem of the endometriotic cysts whose oxidative DNA damage drives the ARID1A-mutant (already mapped) carcinogenesis of ovarian clear cell carcinoma.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement evasion: the ovarian-clear-cell-carcinoma cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped) within the endometriosis-associated inflammatory microenvironment.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, may mark the immune response of ovarian clear cell carcinoma.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Treatment anaemia: erythropoietin corrects the platinum- and taxane-induced anaemia in ovarian clear cell carcinoma therapy; EPOR expression on tumour cells raises the question of direct EPO-driven growth signalling.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Ascites pain mediator: bradykinin accumulates in the malignant ascites of ovarian clear cell carcinoma, activating B1/B2 receptors on the peritoneal mesothelium and sensory fibres to drive the pelvic pain that often delays diagnosis.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement brake: C1-esterase inhibitor modulates the classical complement pathway within the endometriosis-associated peritoneal milieu of ovarian clear cell carcinoma, limiting the C3/C5 (already mapped) complement cascade.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Stroma alarmin: TSLP released by the endometriosis-derived epithelium and peritoneal stroma activates mast cells (already mapped) and dendritic cells to shape the type-2 microenvironment of ovarian clear cell carcinoma.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Endometriosis mast-cell mediator: histamine released by mast cells (already mapped) in endometriotic lesions promotes VEGF angiogenesis and prostaglandin-mediated immune evasion in the ovarian-clear-cell-carcinoma peritoneal microenvironment.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Endometriosis stroma scaffold: periostin, upregulated in the endometriosis-derived stroma, promotes tumour cell adhesion, peritoneal invasion and desmoplastic ECM remodelling of ovarian clear cell carcinoma.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — OCCC melatonin: melatonin suppresses ovarian-clear-cell-carcinoma proliferation by inhibiting the PI3K/AKT (already mapped) and mTOR (already mapped) pathways through MT1/MT2-mediated cAMP suppression, counteracting the ARID1A-driven (already mapped) carcinogenesis.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — OCCC androgen axis: testosterone via androgen receptor promotes ovarian-clear-cell-carcinoma proliferation and intersects the PI3K/AKT (already mapped) and mTOR (already mapped) pathways upregulated in the ARID1A (already mapped)-mutant clear cell carcinoma.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — OCCC ascites serotonin: serotonin accumulates in the clear-cell-carcinoma peritoneal ascites and activates 5-HT receptors on peritoneal deposits to promote adhesion and mTOR (already mapped)-driven proliferation in the ovarian-clear-cell-carcinoma microenvironment.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — OCCC prolactin: prolactin via JAK2/STAT3 activates ovarian-clear-cell-carcinoma cells and macrophages (already mapped), amplifying mTOR (already mapped) and NF-κB (already mapped)-driven proliferation in the ARID1A (already mapped)-deficient microenvironment.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — OCCC oxytocin: oxytocin receptors on ovarian-clear-cell-carcinoma cells couple to Gαq-PKC, cross-activating mTOR (already mapped) and PI3K/AKT (already mapped) proliferative cascades in the chemoresistant ARID1A (already mapped)-mutant microenvironment.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — OCCC vasopressin: vasopressin via V1a receptors on ovarian-clear-cell-carcinoma stroma activates Gαq-PKC-IP3 signalling, converging on mTOR (already mapped) and NF-κB (already mapped) pro-survival cascades in the peritoneal implantation microenvironment.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — OCCC selenium: selenium, as GPx in macrophages (already mapped) and T-cytotoxic cells (already mapped), scavenges ROS in the OCCC tumour microenvironment; selenium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) pro-tumour cascade.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — OCCC iodine: iodine-dependent thyroid hormones regulate macrophage (already mapped) polarisation and T-cytotoxic (already mapped) immune surveillance; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) pro-tumour cascade of OCCC.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — OCCC sodium: excess sodium promotes macrophage (already mapped) and mast-cell (already mapped) pro-inflammatory activation; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) skewing amplifies the T-cytotoxic (already mapped) anti-tumour suppression in OCCC.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — OCCC copper: copper-dependent enzymes in macrophages (already mapped) and T-cytotoxic cells (already mapped) sustain tumour-immune crosstalk; copper excess amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade and mast-cell (already mapped) skewing in OCCC.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — OCCC potassium: potassium efflux gates the macrophage (already mapped) and mast-cell (already mapped) NLRP3 inflammasome; potassium loss amplifies NF-κB (already mapped) and IL-6 (already mapped) pro-tumour cascade and suppresses T-cytotoxic (already mapped) killing in OCCC.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — OCCC phosphorus: phosphorus-dependent ATP in macrophages (already mapped) and T-cytotoxic cells (already mapped) sustains immune surveillance; phosphorus dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) pro-tumour signalling cascade in OCCC.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — OCCC carbon: carbon, as metabolic backbone of lipids and HIF-1α (already mapped) signalling in clear-cell tumour and macrophages (already mapped), drives tumour metabolism; carbon dysregulation amplifies IL-6 (already mapped) and VEGF (already mapped) cascade in OCCC.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — OCCC chloride: chloride channels in macrophages (already mapped) and T-cytotoxic-cell (already mapped) modulate tumour-immune homeostasis; chloride dysregulation amplifies IL-6 (already mapped) and VEGF (already mapped) pro-tumour cascade in OCCC.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — OCCC hydrogen: hydrogen, via redox homeostasis in macrophages (already mapped) and T-cytotoxic-cell (already mapped), quenches tumour ROS; hydrogen dysregulation amplifies HIF-1α (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in OCCC.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^jones-2010-arid1a-occc]: Jones S, Wang TL, Shih IeM, et al. Frequent mutations of chromatin remodeling gene ARID1A in ovarian clear cell carcinoma. *Science.* 2010;330(6001):228-231. [doi:10.1126/science.1196333](https://doi.org/10.1126/science.1196333) · [PubMed 20826764](https://pubmed.ncbi.nlm.nih.gov/20826764/)
[^kim-2015-arid1a-ezh2]: Kim KH, Kim W, Howard TP, et al. SWI/SNF-mutant cancers depend on catalytic and non-catalytic activity of EZH2. *Nat Med.* 2015;21(12):1491-1496. [doi:10.1038/nm.3968](https://doi.org/10.1038/nm.3968) · [PubMed 26552009](https://pubmed.ncbi.nlm.nih.gov/26552009/)
