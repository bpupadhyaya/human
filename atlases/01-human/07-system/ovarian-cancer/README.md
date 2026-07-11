---
schema: human-scale-entry/v1
id: ovarian-cancer
name: Ovarian Cancer
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "HGSOC accounts for ~70% of ovarian cancer; BRCA1/2 mutations in ~15-20%; TP53 mutations in ~96%; olaparib and niraparib approved as maintenance; bevacizumab improves PFS; carboplatin+paclitaxel is standard frontline; PARP inhibitor maintenance is standard for HRD+ tumors."
aliases: ["ovarian cancer", "HGSOC", "high-grade serous ovarian cancer", "LGSOC", "clear cell ovarian cancer", "epithelial ovarian cancer", "EOC", "ovarian carcinoma"]
sources:
  - id: burger-2011-gog0218
    type: peer-reviewed
    cite: "Burger RA, Brady MF, Bookman MA, et al. Incorporation of bevacizumab in the primary treatment of ovarian cancer. N Engl J Med. 2011;365(26):2473-2483."
    doi: "10.1056/NEJMoa1104390"
    pmid: "22204724"
    url: "https://doi.org/10.1056/NEJMoa1104390"
  - id: moore-2018-olaparib-solo1
    type: peer-reviewed
    cite: "Moore K, Colombo N, Scambia G, et al. Maintenance olaparib in patients with newly diagnosed advanced ovarian cancer. N Engl J Med. 2018;379(26):2495-2505."
    doi: "10.1056/NEJMoa1810858"
    pmid: "30345884"
    url: "https://doi.org/10.1056/NEJMoa1810858"
cross_links:
  - target: 01-human/03-molecular/brca1
    relation: connects-to
    note: "BRCA1 germline mutations in ~10% and BRCA2 in ~5-10% of HGSOC; somatic BRCA1/2 mutations in additional ~7%; PARP inhibitors (olaparib, niraparib, rucaparib) active in BRCA-mutant ovarian cancer (SOLO-1, NOVA, ARIEL3); BRCA testing is standard in all ovarian cancer."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Pembrolizumab active in MSI-H/dMMR ovarian cancer (~5%); atezolizumab + bevacizumab + chemotherapy (IMagyn050) failed to show OS benefit vs. bev+chemo; PD-L1 expression enriched in clear cell and mucinous ovarian cancer; mirvetuximab-soravtansine + pembro under study."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Bevacizumab (anti-VEGF) + carboplatin/paclitaxel → maintenance bevacizumab (GOG-0218, ICON7 trials) → PFS improvement ~4 months; bevacizumab approved for frontline and platinum-resistant ovarian cancer; lenvatinib+pembrolizumab active in platinum-resistant ovarian cancer."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "PI3K pathway mutations (PIK3CA, PTEN, AKT1) in ~50% of clear cell and endometrioid ovarian cancer → mTOR activation; everolimus + letrozole studied in ER+ endometrioid ovarian cancer; mTOR inhibitors + PARP inhibitors studied to overcome PARP resistance via AKT pathway."
  - target: 01-human/07-system/hereditary-breast-ovarian-cancer
    relation: connects-to
    note: "Hereditary breast and ovarian cancer (germline BRCA1/2) causes ~15-20% of HGSOC and raises lifetime ovarian-cancer risk to ~40-60% (BRCA1) or ~10-30% (BRCA2); risk-reducing salpingo-oophorectomy is the best prevention, and BRCA status guides PARP-inhibitor maintenance."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 mutation is near-universal in high-grade serous ovarian carcinoma (~96%) and is the defining, initiating event — a TP53 signature appears in Fallopian-tube secretory cells (STIC lesions) decades before invasion; its ubiquity is why HGSOC lacks a single targetable hotspot."
  - target: 01-human/03-molecular/brca2
    relation: connects-to
    note: "BRCA2 loss (germline or somatic in ~8% of HGSOC) cripples homologous-recombination repair, creating the synthetic-lethal vulnerability PARP inhibitors exploit; BRCA2-mutant tumors are especially platinum-sensitive with the best maintenance outcomes."
  - target: 01-human/07-system/ovarian-clear-cell-carcinoma
    relation: connects-to
    note: "Ovarian cancer is not one disease: high-grade serous carcinoma (TP53-universal, BRCA/HRD, platinum-sensitive) dominates, but ovarian clear cell carcinoma is a distinct subtype (ARID1A/PIK3CA, endometriosis-linked, platinum-resistant) — histotype guides treatment."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Ovarian cancer is the deadliest gynecologic cancer because it grows silently in the pelvis and spreads transcoelomically across the peritoneum before symptoms appear; most high-grade serous tumors originate in the fallopian tube fimbriae (STIC), making it a tubo-ovarian cancer."
  - target: 01-human/07-system/endometrial-cancer
    relation: connects-to
    note: "Ovarian and endometrial cancers are linked: endometrioid and clear-cell ovarian cancers share histology and ARID1A mutations with their uterine counterparts and present synchronously, and Lynch syndrome raises the risk of both — so a dual primary prompts germline testing."
  - target: 01-human/07-system/lynch-syndrome
    relation: connects-to
    note: "Lynch syndrome is the second major hereditary cause of ovarian cancer after BRCA: mismatch-repair loss (MLH1/MSH2) raises ovarian risk—often endometrioid or clear-cell histology—alongside its colorectal and endometrial cancers, so MMR/MSI testing guides workup."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "Ovarian and breast cancer are linked through BRCA1/2: germline mutations sharply raise both, defining hereditary breast-ovarian cancer syndrome, and the homologous-recombination defect they create makes both tumors sensitive to platinum and PARP inhibitors."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Tumor-associated macrophages drive ovarian cancer's spread: the omentum and ascites are rich in immunosuppressive M2 macrophages that help cells implant on peritoneal surfaces and resist immunity, a target alongside the limited success of checkpoint blockade."
  - target: 01-human/07-system/mesothelioma
    relation: connects-to
    note: "Ovarian cancer and peritoneal mesothelioma can be hard to tell apart: both stud the peritoneum as serous-looking tumors and may carry BAP1 changes, so carcinomatosis needs immunostaining to distinguish high-grade serous ovarian cancer from mesothelioma."
  - target: 01-human/07-system/gorlin-syndrome
    relation: connects-to
    note: "Ovarian fibromas are a feature of Gorlin syndrome: PTCH1 loss and unchecked Hedgehog signaling produce these benign, often bilateral calcified ovarian tumors, so they warrant Gorlin evaluation—distinct from the epithelial carcinomas that dominate ovarian cancer."
  - target: 01-human/07-system/peutz-jeghers-syndrome
    relation: connects-to
    note: "Peutz-Jeghers syndrome raises ovarian tumor risk: STK11 loss predisposes to sex cord tumors with annular tubules (SCTAT) and mucinous ovarian tumors, alongside its GI hamartomas and breast cancer risk—so PJS is part of the hereditary differential for ovarian neoplasms."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Estrogen exposure shapes ovarian cancer risk: more lifetime ovulatory cycles and unopposed estrogen raise risk, while pregnancy, breastfeeding and contraceptives that suppress ovulation lower it—so reproductive and hormonal history strongly modulates this cancer."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Tumor-infiltrating cytotoxic T cells predict ovarian cancer outcome: high CD8 T-cell infiltration of high-grade serous tumors correlates with markedly better survival, evidence the immune system restrains the cancer—a rationale for immunotherapy in ovarian cancer."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Ovarian cancer spreads across the peritoneum to the liver surface: it sheds cells that seed the omentum and coat the liver capsule rather than invading the parenchyma early, so debulking these surface deposits is central to surgery, and ascites is common."
  - target: 01-human/03-molecular/rad51
    relation: connects-to
    note: "Ovarian cancer's BRCA/RAD51 defect is its therapeutic Achilles' heel: ~half of high-grade serous tumors have homologous-recombination deficiency (BRCA, RAD51 pathway), so PARP inhibitors kill them by synthetic lethality—a major advance in maintenance therapy."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Ovarian cancer spreads through the abdomen onto the digestive tract: it sheds cells that coat the peritoneum, omentum and bowel surface, so it presents late with bloating and ascites and often causes bowel obstruction—dictating debulking surgery."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Ovarian cancer is strongly prothrombotic: tumor tissue factor and the bulky pelvic mass make venous thromboembolism common (a Trousseau-type hypercoagulability), so clots can be the presenting sign and prophylaxis is routine around surgery and chemo."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A loss defines the endometriosis-linked ovarian cancers: this chromatin-remodeling gene is frequently mutated in clear-cell and endometrioid tumors that arise from endometriosis, giving them biology distinct from the BRCA-driven high-grade serous type."
  - target: 01-human/03-molecular/atm
    relation: connects-to
    note: "ATM extends ovarian cancer's homologous-repair story beyond BRCA: germline or tumor ATM loss impairs DNA repair, marking some non-BRCA tumors as homologous-recombination deficient and potentially sensitive to platinum and PARP inhibitors."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Cancer-associated fibroblasts build ovarian cancer's metastatic niche: in the omentum they remodel the stroma, supply growth factors and promote chemoresistance, making this stromal cell a driver of the peritoneal spread that defines advanced disease."
  - target: 01-human/03-molecular/albumin
    relation: connects-to
    note: "Ovarian cancer betrays itself through albumin-rich ascites: spreading across the peritoneum, it leaks fluid that swells the abdomen and drains albumin, so new ascites in a woman is a red flag and paracentesis both relieves and diagnoses it."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Ovarian cancer was the first tumor shown to use regulatory T cells to predict death: Tregs flood the malignant ascites and tumor, suppressing immunity—a landmark finding that helped launch the field of cancer immunosuppression."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Ovarian cancer disables NK cells in its ascites: the fluid around the tumor blunts natural killer cytotoxicity, helping floating tumor clusters survive—so restoring NK function is explored to fight peritoneal spread."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Ovarian cancer spreads across the gut: it sheds cells that seed the omentum and bowel surface as peritoneal carcinomatosis, so abdominal bloating and bowel obstruction—not pelvic symptoms—are often what finally brings the late-stage disease to light."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Ovarian cancer reaches the chest as malignant effusions: tumor spread to the pleura fills the space around the lungs with fluid, causing breathlessness, a common sign of advanced disease that upstages it and guides drainage and systemic therapy."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells shape the immune fight against ovarian cancer: as antigen-presenters they prime the T-cell response, and their dysfunction in the tumor and ascites helps it evade immunity—so dendritic-cell vaccines are explored to rebuild it."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "A rare ovarian cancer spikes blood calcium: the small-cell carcinoma of hypercalcemic type (SCCOHT) drives a paraneoplastic hypercalcemia, so high calcium in a young woman with an ovarian mass is a warning."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Ovarian cancer can back up the kidneys: a bulky pelvic mass or nodal spread compresses the ureters, causing hydronephrosis and post-renal kidney injury in advanced disease."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "Ovarian cancer feeds on the omentum's fat cells: it spreads to the fatty omentum, where adipocytes supply fatty acids that fuel tumor growth—the 'omental caking' typical of advanced disease."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photons hunt this silent cancer: transvaginal ultrasound probes a suspicious mass, CT maps the peritoneal spread and ascites that mark advanced disease, and PET tracks recurrence — imaging that, with CA-125, guides every step of management."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "Ovarian cancer studs the spleen's surface: spreading through the peritoneal fluid, it seeds the splenic capsule and nearby diaphragm, so splenectomy is sometimes part of the aggressive debulking surgery that aims to leave no visible tumor."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Ovarian cancer commandeers platelets: tumor-driven IL-6 and thrombopoietin spark a paraneoplastic thrombocytosis, and these elevated platelets in turn shield circulating tumor cells and fuel growth, marking more aggressive, advanced disease."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "First-line chemotherapy stings the nerves: paclitaxel, the taxane paired with carboplatin against ovarian cancer, damages peripheral sensory neurons, leaving a stocking-glove numbness and tingling that can outlast the treatment."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy traces ovarian cancer to its source: most high-grade serous tumors begin not in the ovary but in the fallopian tube's secretory cells, distinguished by EM from their ciliated neighbors at the fimbrial end."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Platinum chemotherapy drains magnesium: carboplatin injures the kidney's tubules, which then waste magnesium, so blood levels are watched and replaced through the months of ovarian cancer treatment."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies track and treat the disease: the CA-125 tumor marker is measured by an antibody immunoassay to follow response and relapse, while anti-VEGF bevacizumab is added to chemotherapy to starve the tumor's blood supply."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "The carboplatin-paclitaxel backbone hammers the marrow: both drugs are myelosuppressive, so the neutrophil count falls between cycles and febrile neutropenia is one of the recurring hazards of ovarian-cancer chemotherapy."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Anemia shadows the long course: chronic disease, repeated chemotherapy, and the slow ooze of peritoneal disease deplete red cells, the fatigue of low erythrocytes often needing transfusion across months of treatment."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "Even the gentler anthracycline touches the heart: pegylated liposomal doxorubicin, a mainstay for recurrent ovarian cancer, still injures cardiomyocytes in a cumulative dose-dependent way, so cardiac function is tracked across repeated lines of therapy."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "The malignant ascites runs on IL-6-STAT3: cytokines in the peritoneal fluid activate STAT3 in tumor and stromal cells, fueling growth, immune evasion and the relentless fluid build-up that distends the abdomen of advanced disease."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "The immune infiltrate predicts survival: ovarian tumors rich in tumor-infiltrating T cells, including CD4 helpers that marshal the response, carry a markedly better prognosis — the biology behind efforts to make this cancer respond to immunotherapy."
  - target: 01-human/03-molecular/palb2
    relation: connects-to
    note: "The BRCA story extends beyond BRCA: germline PALB2 mutations, which partner BRCA2 in homologous-recombination repair, also raise ovarian cancer risk and leave the tumor sensitive to platinum and PARP inhibitors, widening who benefits from genetic testing."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "It is a famously vascular tumor: ovarian cancer drives endothelial cells to sprout new vessels and leak fluid, fueling the malignant ascites that swells the abdomen — the rationale for adding the anti-VEGF drug bevacizumab to its treatment."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "It travels in a shared hereditary cluster: the same BRCA and PALB2 mutations that drive ovarian cancer also raise pancreatic cancer risk, so a family history can span both organs and flag relatives for combined surveillance."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12 guides the spread to the omentum: the chemokine, abundant in peritoneal fat, draws CXCR4-bearing ovarian cancer cells to seed the omentum and peritoneum, the characteristic transcoelomic metastasis of the disease."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Advanced disease invites sepsis: malignant bowel obstruction and perforation from peritoneal spread, plus chemotherapy neutropenia, expose ovarian-cancer patients to intra-abdominal infection and sepsis."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells populate the tumor and ascites: they accumulate in the ovarian tumor microenvironment and peritoneal fluid, releasing angiogenic and immunomodulatory mediators that support growth and vessel formation."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "The inflamed peritoneal milieu runs on NF-κB: ovarian cancer's ascites is rich in cytokines that activate NF-κB, driving the tumor-cell survival, chemoresistance and immune evasion behind its peritoneal spread."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Pelvic disease and platinum strain the kidneys: bulky tumor obstructing the ureters causes hydronephrosis, and the cisplatin used to treat ovarian cancer is nephrotoxic — together a real risk of chronic kidney disease."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Chronic disease and chemo drain the blood: the inflammatory cytokines of ovarian cancer and its marrow-suppressing platinum chemotherapy produce a prominent anemia of chronic disease."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Removing the ovaries strips away bone-protective estrogen: surgical oophorectomy and chemotherapy throw younger patients into abrupt menopause, and the loss of estrogen accelerates bone loss toward osteoporosis."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Its liposomal anthracycline can weaken the heart: pegylated liposomal doxorubicin, widely used in recurrent ovarian cancer, carries cumulative cardiotoxicity that can erode cardiac function into heart failure."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Late diagnosis and high relapse weigh on mood: ovarian cancer's frequent advanced-stage presentation, repeated recurrences and abrupt surgical menopause contribute to substantial depression and anxiety."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Its taxane-platinum chemo numbs the nerves: the paclitaxel and carboplatin central to ovarian-cancer treatment cause a dose-dependent, often persistent peripheral neuropathy with painful paraesthesiae."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "Years of DNA-damaging therapy can seed leukaemia: the platinum chemotherapy and PARP inhibitors used in ovarian cancer carry a small but real risk of therapy-related myelodysplasia and acute myeloid leukaemia."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A relapsing cancer watched by a blood marker breeds worry: the recurrent course of ovarian cancer and the dread of a rising CA-125 between scans foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Cytoreductive surgery is extensive: ovarian-cancer debulking removes peritoneal and bowel disease in long operations, leaving large abdominal wounds and anastomoses prone to leak and slow healing."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It floods the chest with fluid: advanced ovarian cancer spreads across the diaphragm to cause malignant pleural effusions, a common marker of stage IV disease and a source of breathlessness."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Removing the ovaries forces menopause: bilateral salpingo-oophorectomy for ovarian cancer abruptly ends ovarian oestrogen, causing surgical menopause with its hormonal, bone and vasomotor effects."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It spreads to the deep nodes: ovarian cancer disseminates to pelvic and para-aortic lymph nodes, so lymphadenectomy is part of its surgical staging."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It can attack the brain by autoimmunity: ovarian cancer causes paraneoplastic anti-Yo cerebellar degeneration, and ovarian teratomas are the classic trigger of anti-NMDA-receptor encephalitis."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Its drugs blister the hands and feet: pegylated liposomal doxorubicin causes hand-foot syndrome (palmar-plantar erythrodysesthesia), and bevacizumab impairs wound healing."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "PARP inhibitors transformed its care: olaparib and other PARP inhibitors exploit the homologous-recombination defect of BRCA-mutant ovarian cancer, with bevacizumab adding anti-angiogenic benefit."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It obstructs and its drugs poison the kidney: bulky pelvic and retroperitoneal ovarian cancer can block the ureters causing hydronephrosis, and cisplatin chemotherapy is nephrotoxic."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "It clots and its treatment strains the heart: ovarian cancer is strongly prothrombotic, and bevacizumab causes hypertension with thromboembolic and bleeding risks."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Platinum-taxane is the backbone: carboplatin with paclitaxel after debulking surgery is the chemotherapy foundation, and platinum sensitivity guides treatment at relapse."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Largely resistant despite immune cells: although ovarian cancer harbours tumour-infiltrating lymphocytes that predict prognosis, its immunosuppressive microenvironment has left checkpoint inhibitors mostly ineffective."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Its immune infiltrate predicts survival: the density of tumour-infiltrating lymphocytes strongly predicts outcome in ovarian cancer, yet regulatory T cells and an immunosuppressive milieu blunt the antitumour response."
  - target: 01-human/07-system/prostate-cancer
    relation: connects-to
    note: "Shared BRCA vulnerability across the sexes: like high-grade serous ovarian cancer, BRCA-mutant prostate cancer carries homologous-recombination deficiency and responds to PARP inhibitors, placing both in the HBOC spectrum despite opposite organs."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "B-cell islands sharpen the prognosis: high-grade serous ovarian cancers that build tertiary lymphoid structures with germinal-centre B cells and plasma cells show stronger antitumour immunity and better survival than those with T cells alone."
  - target: 01-human/07-system/gastric-cancer
    relation: connects-to
    note: "The source of a Krukenberg tumour: metastatic gastric and other GI signet-ring carcinomas seed the ovaries as Krukenberg tumours, a classic ovarian metastasis that mimics primary ovarian cancer and must be distinguished from it."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "Peritoneal spread and bowel obstruction: ovarian cancer disseminates across the peritoneum, encasing the bowel ('omental caking') and infiltrating the intestinal epithelium, so bowel obstruction becomes a leading cause of death."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Liver and capsular involvement: ovarian cancer studs the liver capsule with perihepatic implants and metastasises to the hepatic lobule in advanced disease."
  - target: 01-human/03-molecular/wt1
    relation: connects-to
    note: "A diagnostic marker: high-grade serous ovarian carcinoma characteristically expresses WT1, an immunohistochemical marker that helps confirm its tubal/serous origin over other gynaecological cancers."
  - target: 01-human/07-system/mds
    relation: connects-to
    note: "Late cost of treatment: platinum chemotherapy and PARP inhibitors used for ovarian cancer damage haematopoietic stem cells, raising the risk of therapy-related myelodysplasia and acute leukaemia years later."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "Differential of an ovarian mass: colorectal cancer can metastasise to the ovary (Krukenberg-type spread) and seed the peritoneum like advanced ovarian cancer, while Lynch syndrome predisposes to both tumours."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "A vascular target: high-grade serous ovarian carcinoma is intensely angiogenic, and the anti-VEGF antibody bevacizumab attacks the tumour's arterial supply, a mainstay added to chemotherapy in advanced disease."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Amplified oncogene: MYC amplification is common in high-grade serous ovarian carcinoma, driving the proliferation of this genomically unstable tumour."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "Cell-cycle dysregulation: CCNE1 amplification and CDK4/6-cyclin activity disrupt the cell cycle in a subset of ovarian cancers, an avenue for cell-cycle-targeted therapy."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Notch3 driver: NOTCH3 amplification and Notch signalling recur in ovarian cancer, promoting growth and contributing to platinum chemoresistance."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K/AKT survival: AKT-pathway activation drives ovarian cancer growth and survival and contributes to chemoresistance, a targetable node in combination therapy."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Ascites and hypoxia: HIF-1α stabilised in the hypoxic ovarian tumour and its ascitic spheroids drives angiogenesis and the peritoneal spread of high-grade serous cancer."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Epigenetic driver: EZH2 overexpression silences tumour-suppressor genes in ovarian cancer, promoting proliferation and an emerging epigenetic therapeutic target."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Malignant ascites: IL-6 is abundant in ovarian-cancer ascites, where it drives JAK-STAT3 signalling that sustains tumour-cell survival, spheroid formation and the cachexia that marks advanced peritoneal disease."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Peritoneal spread: TGF-β in the omental microenvironment drives the mesothelial-to-mesenchymal transition that prepares the peritoneum for ovarian-cancer implantation, while excluding T cells to blunt immunotherapy."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "HRD immunogenicity: BRCA-mutant, homologous-recombination-deficient ovarian cancers accumulate cytosolic DNA that activates cGAS-STING, the innate-immune basis for combining PARP inhibitors with checkpoint blockade."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Platinum-induced apoptosis: carboplatin-paclitaxel kills ovarian carcinoma through caspase-3-mediated apoptosis, and the eventual evasion of this death programme defines the platinum-resistant relapse that is the lethal phase of high-grade serous disease."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "Histotype-specific driver: PTEN loss activates PI3K-AKT signalling in the endometriosis-associated endometrioid and clear-cell ovarian carcinomas, the histotypes distinct from BRCA-driven high-grade serous disease."
  - target: 01-human/03-molecular/mlh1
    relation: connects-to
    note: "Mismatch-repair deficiency: MLH1 silencing produces the microsatellite-instable endometrioid and clear-cell ovarian cancers seen in Lynch syndrome, a DNA-repair defect distinct from BRCA-related homologous-recombination loss and a basis for checkpoint blockade."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "MAPK pathway: KRAS-activating mutations define the low-grade serous and mucinous ovarian carcinomas, a biology distinct from the p53/BRCA-driven high-grade serous disease and the rationale for MEK inhibitors in these chemo-resistant histotypes."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K activation: PIK3CA mutation and amplification activate the PI3K-AKT-mTOR axis already mapped here through AKT and PTEN, sustaining ovarian cancer survival signalling and supporting combination strategies with PI3K-pathway inhibitors."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Ascites macrophages: CCL2 secreted by ovarian tumour cells recruits monocytes that become the tumour-associated macrophages dominating malignant ascites, building the immunosuppressive peritoneal niche that drives chemoresistance and spread."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "MAPK in low-grade disease: KRAS and BRAF mutations (KRAS mapped) activate the MAPK-ERK cascade that drives low-grade serous and mucinous ovarian cancers, a MEK-inhibitor-responsive subset distinct from high-grade serous disease."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Cell-cycle drive: cyclin-E and the CDK4/6 axis (mapped) release E2F1 to force the G1-S transition, with CCNE1 amplification a recurrent proliferative driver of high-grade serous ovarian cancer."
  - target: 01-human/03-molecular/her2
    relation: connects-to
    note: "Targetable subset: a fraction of ovarian carcinomas overexpress HER2, feeding the PI3K and MAPK pathways (mapped) and offering a target for HER2-directed antibody-drug conjugates."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Ascites microenvironment: IL-6-JAK-STAT3 signalling (IL-6 and STAT3 already mapped), abundant in malignant ascites, supports the survival and chemoresistance of ovarian-cancer cells."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Cell-cycle drive: RB-pathway dysregulation, including the CCNE1 amplification frequent in high-grade serous ovarian cancer, drives cell-cycle progression released through E2F1 (already mapped)."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "Alternative p53 loss: MDM2 amplification offers an alternative route to inactivation of the near-universally dysfunctional p53 (already mapped) in high-grade serous ovarian cancer."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 promotes ovarian-cancer cell adhesion, spheroid formation and the peritoneal dissemination of metastatic disease."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β mapped) drives EMT and the peritoneal-metastatic, immunosuppressive microenvironment of ovarian cancer."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "CDKN2A loss releases CDK4/6-cyclin-D control of the cell cycle, a recurrent lesion in high-grade serous ovarian cancer."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "BRCA/HRD-driven cytosolic DNA activates cGAS-STING (mapped) and IFN-STAT1 signalling, shaping the immunogenicity of high-grade serous ovarian cancer."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO tumour-suppressor activity, antagonised by PI3K-AKT signalling, is lost in the proliferative progression of ovarian cancer."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated CD8 cytotoxicity drives the antitumour immune response whose magnitude predicts outcome in high-grade serous ovarian cancer."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the survival and Wnt/β-catenin signaling of ovarian cancer."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the immunosuppressive, ascites-associated microenvironment of ovarian cancer."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-kinase signaling drives the peritoneal dissemination and invasion of ovarian cancer."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of ovarian cancer."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival and chemoresistance of ovarian cancer cells, particularly in dormant peritoneal micrometastases."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of ovarian cancer within the omental adipose niche."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven macrophage recruitment shapes the immunosuppressive ascites microenvironment of ovarian cancer."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation in the peritoneal microenvironment participates in the progression of ovarian cancer."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Endothelin-1 autocrine signaling participates in the proliferation, angiogenesis, and invasion of ovarian cancer."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of ovarian cancer."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory tumor microenvironment of ovarian cancer."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory tumor microenvironment and ascites of ovarian cancer."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immune prognosis: intratumoral T-cell infiltration is one of the strongest prognostic factors in ovarian cancer, and MHC class II antigen presentation shapes the CD4 help behind that response, with loss of presentation a route to immune escape and immunotherapy resistance."
  - target: 01-human/03-molecular/axl-receptor
    relation: connects-to
    note: "Platinum resistance: the AXL receptor tyrosine kinase drives epithelial-mesenchymal transition, peritoneal metastatic spread and acquired platinum resistance in ovarian cancer, positioning AXL inhibition as a strategy against the chemoresistant relapse that defines the disease."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Apoptotic evasion: high-grade serous ovarian cancer resists chemotherapy partly through anti-apoptotic BCL-2 family proteins that raise the threshold for caspase activation (caspase-3 already mapped), a target of BH3-mimetic sensitisation strategies."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Cellular immunotherapy: IL-2-driven T-cell expansion supports the adoptive and tumour-infiltrating-lymphocyte therapies being explored for ovarian cancer, whose response to single-agent checkpoint blockade (PD-1 already mapped) has been modest."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Anaemia: ovarian cancer lowers haemoglobin through chronic disease, occult blood loss and platinum-chemotherapy myelosuppression, contributing to the fatigue that burdens patients and often requiring transfusion or growth-factor support."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Treatment cardiotoxicity: the anti-angiogenic bevacizumab (VEGF already mapped) and chemotherapy used in ovarian cancer can injure the heart, and troponin elevation helps detect the cardiac toxicity that complicates prolonged treatment."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "Bowel obstruction: transcoelomic spread of ovarian cancer over the small intestine and its mesentery causes the malignant bowel obstruction (large intestine already mapped) that is a common and difficult terminal complication."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive ascites: IL-10 in the malignant ascites and its tumour-associated macrophages (already mapped) dampens the anti-tumour T-cell response (CD8 already mapped), part of the immune evasion of ovarian cancer."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative and lysis stress: platinum chemotherapy and rapid cell turnover in ovarian cancer generate oxidative stress and release purines that xanthine oxidase converts to uric acid, adding oxidative and tumour-lysis burden."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises the tumour-associated macrophages (already mapped) of the malignant ascites toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the immune-evasive microenvironment of ovarian cancer."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Anaemia and transfusion: the chronic disease and the platinum chemotherapy of ovarian cancer cause anaemia (haemoglobin already mapped) that can require transfusion, whose repeated support can load the body with iron."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Tumour vasculature and ascites: nitric oxide with VEGF and endothelin-1 (already mapped) regulates the angiogenesis and vascular permeability that drive the malignant ascites of ovarian cancer."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage (already mapped) and type-2 milieu of the immunosuppressive ascites and omental microenvironment of ovarian cancer."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Omental adipose niche: leptin links obesity to ovarian-cancer risk, and the adipocyte-rich omentum — a favoured metastatic site — supplies the fatty acids and adipokines that fuel the peritoneal spread."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin sequesters iron and adds an anaemia of chronic disease to the platinum-chemotherapy anaemia (iron and haemoglobin already mapped) of ovarian cancer."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Omental adipokine: adiponectin, with leptin (already mapped), of the omental adipose niche modulates the ovarian-cancer growth and the peritoneal (large intestine already mapped) spread."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the omental adipose-inflammatory adipokine of the peritoneal niche of ovarian cancer."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "HRD immunogenicity: the homologous-recombination-deficient (BRCA already mapped) ovarian cancer activates the cGAS-STING (already mapped) pathway to produce the type-I interferon that drives the immunogenicity and the checkpoint (PD-1 already mapped) response."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity of the immunogenic HRD ovarian cancer."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response of the ovarian-cancer immune microenvironment."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 arm of the immune microenvironment of the ovarian-cancer peritoneal niche."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Tertiary lymphoid B-cell response: the plasma cells and B cells of the tumour tertiary lymphoid structures produce antibody (already mapped) and, with the CD8 TILs (already mapped), predict a favourable prognosis in ovarian cancer."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the ovarian-cancer peritoneal microenvironment."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2/AllergoOncology arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), is the antibody arm explored in the AllergoOncology anti-tumour response against ovarian cancer."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Tertiary lymphoid structures: the B cells organise the intratumoural tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, predicts a favourable prognosis in ovarian cancer."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Prognostic vitamin: the vitamin D status is associated with the ovarian-cancer risk and outcome and modulates the tumour immune microenvironment."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) recruits and polarises the myeloid cells to an immunosuppressive phenotype in the ovarian-cancer peritoneal microenvironment."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its activation (with C3 and C5aR1 already mapped) contribute to the complement-driven inflammation of the ovarian-cancer peritoneal microenvironment."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement evasion: the ovarian-cancer cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), evading the complement attack in the peritoneal microenvironment."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Ascites iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the anaemia and the iron-rich malignant ascites of ovarian cancer."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Peritoneal alarmin: TSLP released by ovarian epithelial and stromal cells activates mast cells and dendritic cells, promoting the type-2 microenvironment of the peritoneal cavity that suppresses anti-tumour cytotoxicity."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Peritoneal metastasis scaffold: periostin, upregulated in the ovarian cancer stroma and malignant ascites, promotes the peritoneal adhesion and omental colonisation that characterise the widespread intraperitoneal dissemination of this cancer."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell histamine: stromal mast-cell-derived histamine promotes VEGF-driven angiogenesis and suppresses NK and T-cell cytotoxicity in the ovarian cancer ascites, contributing to the immunosuppressive peritoneal microenvironment."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Peritoneal kinin: bradykinin accumulates in the malignant ascites of ovarian cancer, activating B1/B2 receptors on peritoneal mesothelium and sensory fibres, amplifying pain and vascular permeability of the peritoneal microenvironment."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement regulation: C1-esterase inhibitor restrains the classical complement pathway in the ovarian-cancer peritoneal milieu, limiting the C3/C5/C5aR1 (all already mapped) cascade driving the immunosuppressive ascites microenvironment."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Treatment anaemia: erythropoietin corrects the chemotherapy-induced anaemia of ovarian cancer; EPOR expression on tumour cells raises the question of direct EPO-driven signalling influencing platinum- and taxane-based regimen responses."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Peritoneal melatonin: melatonin inhibits ovarian cancer proliferation and ascites formation by suppressing VEGF (already mapped)-driven angiogenesis via MT1/MT2-mediated cAMP reduction and by enhancing NK-cell (already mapped) cytotoxicity against peritoneal deposits."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Ovarian cancer androgen axis: testosterone via androgen receptor promotes epithelial ovarian cancer proliferation (particularly low-grade serous histology) and amplifies KRAS (already mapped) and PI3K/AKT (already mapped)-driven tumour growth."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Ascites serotonin signalling: serotonin accumulates in ovarian cancer ascites, activating 5-HT2 receptors on peritoneal deposits to promote adhesion and VEGF (already mapped)-driven angiogenesis, amplifying the immunosuppressive malignant peritoneal microenvironment."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Ovarian cancer prolactin: prolactin via JAK2/STAT3 (already mapped) activates ovarian cancer cells and macrophages (already mapped), promoting VEGF (already mapped) expression and NF-κB (already mapped)-driven immunosuppression in the peritoneal ascites microenvironment."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Ovarian cancer oxytocin: oxytocin receptors on ovarian cancer epithelial cells couple to Gαq-IP3-PKC, cross-activating PI3K/AKT (already mapped) and VEGF (already mapped) signalling to promote peritoneal implantation and ascites formation."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "Ovarian cancer vasopressin: vasopressin via V1a receptors on ovarian cancer and stromal cells activates Gαq-PKC and PKA signalling, promoting VEGF (already mapped)-driven ascites angiogenesis and NF-κB (already mapped)-mediated peritoneal invasion."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Ovarian cancer selenium: selenium, as GPx in macrophages (already mapped) and T-cytotoxic cells (already mapped), scavenges ROS in the ovarian tumour microenvironment; selenium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) pro-tumour cascade."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "Ovarian cancer iodine: iodine-dependent thyroid hormones regulate macrophage (already mapped) polarisation and T-cytotoxic (already mapped) immune surveillance; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) pro-tumour cascade of ovarian cancer."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Ovarian cancer sodium: excess sodium promotes macrophage (already mapped) and mast-cell (already mapped) pro-inflammatory activation; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) skewing amplifies T-cytotoxic (already mapped) suppression in ovarian cancer."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Ovarian cancer copper: copper enzymes in macrophages (already mapped) and mast-cell (already mapped) sustain tumour-immune balance; copper excess amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade suppressing T-cytotoxic (already mapped) killing in ovarian cancer."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Ovarian cancer potassium: potassium efflux gates macrophage (already mapped) NLRP3; potassium loss amplifies NF-κB (already mapped) and IL-6 (already mapped) inflammation and suppresses mast-cell (already mapped) and T-cytotoxic (already mapped) responses in ovarian cancer."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Ovarian cancer phosphorus: phosphorus-dependent ATP in macrophages (already mapped) and T-cytotoxic cells (already mapped) sustains tumour immune surveillance; phosphorus dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of ovarian cancer."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Ovarian cancer carbon: carbon as backbone of VEGF (already mapped) and NF-κB (already mapped) proteins in tumour cells and macrophages (already mapped) sustains signalling; carbon depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of ovarian cancer."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "Ovarian cancer chloride: chloride channels in macrophages (already mapped) and tumour cells modulate cell-volume and invasive potential; chloride imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade of ovarian cancer."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "Ovarian cancer hydrogen: hydrogen, via redox homeostasis in tumour cells and macrophages (already mapped), supports VEGF (already mapped) signalling; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) oxidative cascade of ovarian cancer."
---

# Ovarian Cancer

## Overview

**Ovarian cancer** encompasses a heterogeneous group of malignancies arising from the ovarian surface epithelium, Fallopian tube epithelium (increasingly recognized as the primary site of origin for most "ovarian" carcinomas), or ovarian stroma. **High-grade serous ovarian carcinoma (HGSOC)** is by far the most common and lethal subtype, accounting for ~70% of all ovarian cancers and nearly all ovarian cancer deaths. HGSOC is distinguished by near-universal *TP53* mutation (~96%), frequent *BRCA1/2* mutations (~15-20%), a homologous recombination deficiency (HRD) signature in ~50% of tumors, and exquisite platinum sensitivity — making PARP inhibitors after platinum-based chemotherapy the cornerstone of modern treatment [^moore-2018-olaparib-solo1].

**Epidemiology:**
- ~19,000 new cases/year in the United States; ~14,000 deaths/year; 5th most common cancer death in women
- Median age at diagnosis: ~63 years
- 5-year survival: ~49% overall; ~92% for localized disease (rare at diagnosis); ~30% for distant-stage disease
- Most patients (~75%) are diagnosed with advanced-stage disease (FIGO III-IV)
- Lifetime risk: ~1.3% in the general population; 40-60% in BRCA1 carriers; 10-30% in BRCA2 carriers

**Protective factors:** Oral contraceptive use (OCP reduces risk ~50% after 5 years of use → most effective ovarian cancer prevention in BRCA1/2 carriers); parity, breastfeeding; salpingectomy (removes Fallopian tube where HGSOC originates)

## Structure

### Ovarian cancer subtypes and molecular features

**Epithelial ovarian cancer (EOC) — Type I vs. Type II:**

**Type I (Low-grade, stepwise progression from benign precursors):**
- Low-grade serous carcinoma (LGSC): KRAS/BRAF mutations (~60%); wild-type TP53; indolent; MEK inhibitors (trametinib, binimetinib) active in BRAF-mutant LGSC
- Clear cell carcinoma (CCC): ARID1A mutations (~50%), PIK3CA mutations (~30%), ERBB2 amplification; platinum-resistant; HIF-1alpha-driven; mTOR-active; better prognosis in early stage
- Endometrioid carcinoma: CTNNB1 mutations (~30%), PTEN mutations (~20%), microsatellite instability (~12-20%); often endometriosis-associated; Lynch syndrome (MLH1/MSH2 mutations) → endometrioid OC
- Mucinous carcinoma: Rare; KRAS mutations (~60%); often platinum-resistant; borderline mucinous tumor → malignant transformation; HER2 amplification in some cases

**Type II (Aggressive, TP53-mutant):**
- **HGSOC:** TP53 mutation ~96%, BRCA1/2 mutation ~15-20%, CCNE1 amplification (~20%), NF1 mutations (~10%), RB1 loss; de novo, not from preexisting benign lesion; Fallopian tube origin (STIC — serous tubal intraepithelial carcinoma) → spreads to ovary and peritoneum
- High-grade endometrioid: Overlaps with HGSOC; TP53 often mutant; aggressive

**Molecular landscape of HGSOC (TCGA 2011):**
- TP53: ~96% (most any TP53 alteration, no specific hotspot dominant)
- BRCA1 (germline + somatic): ~13%
- BRCA2 (germline + somatic): ~8%
- BRCA1 methylation (epigenetic silencing): ~11%
- Total BRCA/HRD-positive: ~50% (using genomic scar scores)
- CCNE1 amplification: ~20% → cyclin E1 excess → CDK2 activation → HR inhibition (functional HRD without BRCA mutation)
- NF1 deletion: ~10% → RAS-MAPK derepression
- RB1 loss: ~10%

### Fallopian tube origin of HGSOC

The paradigm shift in understanding HGSOC biology:
- **Serous tubal intraepithelial carcinoma (STIC):** Premalignant lesion in Fallopian tube fimbriae (especially in BRCA carriers); TP53 signature present before invasion; STICs found in >50% of BRCA carrier tubes removed prophylactically
- **Implications:** Risk-reducing salpingo-oophorectomy (RRSO) in BRCA carriers → removes Fallopian tube primary → most effective risk reduction; risk-reducing salpingectomy alone (RRSO without oophorectomy) may partially reduce risk while preserving premenopausal hormonal function

## Function

### Normal ovarian and Fallopian tube biology

**Ovarian folliculogenesis:**
Each monthly cycle → dominant follicle → granulosa cell proliferation → ovulation → ruptured follicle → corpus luteum → progesterone → if no pregnancy → luteolysis → menstruation. Repeated ovulations → micro-trauma to ovarian surface epithelium → repair via proliferation → cumulative mutation opportunity; lifetime number of ovulations is proportional to OC risk.

**Fallopian tube secretory cells (FTSECs):**
FTSEC ciliated and secretory cells line the Fallopian tube; secretory cells are the likely precursor cells for HGSOC; TP53 mutations arise in FTSECs decades before HGSOC development; BRCA1/2 germline carriers → accelerated accumulation of TP53 mutations in FTSECs

## Pathology

### Staging and diagnosis

**FIGO staging:**
- Stage I: Confined to ovary/Fallopian tube
- Stage II: Pelvic extension
- Stage III: Peritoneal spread beyond pelvis; most common at diagnosis (~60%)
  - IIIC: Peritoneal implants >2 cm or retroperitoneal LN
- Stage IV: Distant metastasis (IV A: pleural effusion; IV B: parenchymal organ metastasis)

**Diagnosis:**
- CA-125: Elevated (>35 U/mL) in ~80% of HGSOC but low specificity in premenopausal women; useful for monitoring response and recurrence
- HE4 (human epididymis protein 4): Complementary to CA-125; ROMA score (CA-125 + HE4) → preoperative risk assessment
- Pelvic ultrasound: Morphology, septations, solid components, vascularity (ADNEX model)
- CT chest/abdomen/pelvis: Staging; peritoneal carcinomatosis pattern
- Definitive diagnosis: Pathological evaluation of surgical specimen

**Surgical principles:**
- **Primary debulking surgery (PDS):** The extent of cytoreduction is the most important surgical prognostic factor; goal: complete gross resection (R0) or residual disease <1 cm; achieved in ~70% of stage III by specialized gynecologic oncology centers
- **Neoadjuvant chemotherapy (NACT) + interval debulking surgery (IDS):** Alternative for patients who cannot achieve R0 at PDS (CHORUS/EORTC 55971 trials); equivalent OS to PDS in unresectable disease; higher rates of optimal cytoreduction at IDS
- **Secondary cytoreduction:** For platinum-sensitive recurrence with selected good-performance patients (SOC-1 trial — OS benefit in PFI ≥12 months, AGO score positive)

### Treatment

**Frontline (FIGO III-IV HGSOC):**

1. **Carboplatin (AUC5-6) + paclitaxel (175 mg/m²)** every 3 weeks × 6 cycles: Standard platinum-based chemotherapy backbone; ORR ~80%; majority relapse within 3 years despite response

2. **Bevacizumab + chemotherapy → maintenance bevacizumab (GOG-0218, ICON7):** [^burger-2011-gog0218] PFS improvement of ~3.8 months in GOG-0218; limited OS benefit; most benefit in highest-risk patients (stage IV or suboptimally debulked stage III); bevacizumab approved with carboplatin/paclitaxel for frontline advanced OC

3. **PARP inhibitor maintenance (HRD-guided):**
   - **Olaparib (SOLO-1):** [^moore-2018-olaparib-solo1] 3-year PFS 60% vs. 27% in BRCA1/2-mutant HGSOC; FDA approved 2018
   - **Niraparib (PRIMA trial):** 13.8 vs. 8.2 months PFS in HRD+ overall population; 21.9 vs. 10.4 months in BRCA-mutant; approved for all advanced OC regardless of BRCA
   - **Olaparib + bevacizumab (PAOLA-1):** PFS 22.1 vs. 16.6 months in HRD+ (including BRCA+); FDA approved 2020 for BRCA-mutant or HRD+ HGSOC after bevacizumab-containing chemotherapy

4. **HRD testing:** Myriad myChoice HRD Plus (genomic instability score ≥33 = HRD+) — FDA companion diagnostic for niraparib + olaparib + bevacizumab; BRCA1/2 testing required for olaparib; universal tumor testing recommended in all ovarian cancer

**Platinum-sensitive recurrence (PFI ≥6 months):**
- Re-challenge with platinum-based doublet (carboplatin + gemcitabine, or carboplatin + liposomal doxorubicin, or carboplatin + paclitaxel)
- PARP inhibitor maintenance after response: olaparib (STUDY 19/SOLO-2), niraparib (NOVA), rucaparib (ARIEL3) all approved for platinum-sensitive recurrence maintenance
- Bevacizumab + chemotherapy → maintenance bevacizumab (OCEANS trial)
- Secondary debulking in selected patients with PFI ≥12 months and positive AGO score

**Platinum-resistant recurrence (PFI <6 months):**
- Single-agent chemotherapy: liposomal doxorubicin (PEGylated, PLD), topotecan, gemcitabine, weekly paclitaxel
- **Mirvetuximab soravtansine (MIRV):** FRα-directed ADC (maytansinoid); MIRASOL trial → PFS 5.6 vs. 4.0 months vs. chemotherapy in FRα-high platinum-resistant OC; ORR 42%; FDA approved March 2023 — first ADC approved in ovarian cancer; FRα testing required (FOLR1 ≥75% by IHC)
- **Bevacizumab + chemotherapy:** AURELIA trial → PFS 6.7 vs. 3.4 months; standard option
- Clinical trials: PARP inhibitor + immune checkpoint (e.g., rucaparib + nivolumab), novel ADCs (upifitamab rilsodotin — NaPi2b-directed)

**Clear cell ovarian cancer (specific considerations):**
- Inherently platinum-resistant (~30% of CCC)
- mTOR inhibitors (everolimus) under study; PI3K pathway activation
- HER2-targeted therapy in HER2-amplified CCC
- Immunotherapy: moderate PD-L1 expression → pembrolizumab in MSI-H or TMB-high CCC

## Connections

- `connects-to` → **[BRCA1](../../03-molecular/brca1/README.md)** — BRCA1 germline mutations in ~10% and BRCA2 in ~5-10% of HGSOC; somatic BRCA1/2 mutations in additional ~7%; PARP inhibitors (olaparib, niraparib, rucaparib) active in BRCA-mutant ovarian cancer (SOLO-1, NOVA, ARIEL3 trials); BRCA mutation testing is standard in all ovarian cancer.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Pembrolizumab active in MSI-H/dMMR ovarian cancer (~5%); atezolizumab + bevacizumab + chemotherapy (IMagyn050) failed to show OS benefit vs. bevacizumab + chemotherapy; PD-L1 expression enriched in clear cell and mucinous ovarian cancer; mirvetuximab-soravtansine + pembro under study.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Bevacizumab (anti-VEGF) + carboplatin/paclitaxel → maintenance bevacizumab (GOG-0218, ICON7 trials) → PFS improvement ~4 months; bevacizumab approved for frontline and platinum-resistant ovarian cancer; lenvatinib+pembrolizumab active in platinum-resistant ovarian cancer.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — PI3K pathway mutations (PIK3CA, PTEN, AKT1) in ~50% of clear cell and endometrioid ovarian cancer → mTOR activation; everolimus + letrozole studied in ER+ endometrioid ovarian cancer; mTOR inhibitors + PARP inhibitors studied to overcome PARP resistance via AKT pathway.
- `connects-to` → **[Hereditary Breast and Ovarian Cancer](../hereditary-breast-ovarian-cancer/README.md)** — Hereditary breast and ovarian cancer (germline BRCA1/2) causes ~15-20% of HGSOC and raises lifetime ovarian-cancer risk to ~40-60% (BRCA1) or ~10-30% (BRCA2); risk-reducing salpingo-oophorectomy is the best prevention, and BRCA status guides PARP-inhibitor maintenance.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 mutation is near-universal in high-grade serous ovarian carcinoma (~96%) and is the defining, initiating event — a TP53 signature appears in Fallopian-tube secretory cells (STIC lesions) decades before invasion; its ubiquity is why HGSOC lacks a single targetable hotspot.
- `connects-to` → **[BRCA2](../../03-molecular/brca2/README.md)** — BRCA2 loss (germline or somatic in ~8% of HGSOC) cripples homologous-recombination repair, creating the synthetic-lethal vulnerability PARP inhibitors exploit; BRCA2-mutant tumors are especially platinum-sensitive with the best maintenance outcomes.
- `connects-to` → **[Ovarian Clear Cell Carcinoma](../ovarian-clear-cell-carcinoma/README.md)** — Ovarian cancer is not one disease: high-grade serous carcinoma (TP53-universal, BRCA/HRD, platinum-sensitive) dominates, but ovarian clear cell carcinoma is a distinct subtype (ARID1A/PIK3CA, endometriosis-linked, platinum-resistant) — histotype guides treatment.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Ovarian cancer is the deadliest gynecologic cancer because it grows silently in the pelvis and spreads transcoelomically across the peritoneum before symptoms appear; most high-grade serous tumors originate in the fallopian tube fimbriae (STIC), making it a tubo-ovarian cancer.
- `connects-to` → **[Endometrial Cancer](../endometrial-cancer/README.md)** — Ovarian and endometrial cancers are linked: endometrioid and clear-cell ovarian cancers share histology and ARID1A mutations with their uterine counterparts and present synchronously, and Lynch syndrome raises the risk of both — so a dual primary prompts germline testing.
- `connects-to` → **[Lynch Syndrome](../lynch-syndrome/README.md)** — Lynch syndrome is the second major hereditary cause of ovarian cancer after BRCA: mismatch-repair loss (MLH1/MSH2) raises ovarian risk—often endometrioid or clear-cell histology—alongside its colorectal and endometrial cancers, so MMR/MSI testing guides workup.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — Ovarian and breast cancer are linked through BRCA1/2: germline mutations sharply raise both, defining hereditary breast-ovarian cancer syndrome, and the homologous-recombination defect they create makes both tumors sensitive to platinum and PARP inhibitors.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Tumor-associated macrophages drive ovarian cancer's spread: the omentum and ascites are rich in immunosuppressive M2 macrophages that help cells implant on peritoneal surfaces and resist immunity, a target alongside the limited success of checkpoint blockade.
- `connects-to` → **[Mesothelioma](../mesothelioma/README.md)** — Ovarian cancer and peritoneal mesothelioma can be hard to tell apart: both stud the peritoneum as serous-looking tumors and may carry BAP1 changes, so carcinomatosis needs immunostaining to distinguish high-grade serous ovarian cancer from mesothelioma.
- `connects-to` → **[Gorlin Syndrome](../gorlin-syndrome/README.md)** — Ovarian fibromas are a feature of Gorlin syndrome: PTCH1 loss and unchecked Hedgehog signaling produce these benign, often bilateral calcified ovarian tumors, so they warrant Gorlin evaluation—distinct from the epithelial carcinomas that dominate ovarian cancer.
- `connects-to` → **[Peutz-Jeghers Syndrome](../peutz-jeghers-syndrome/README.md)** — Peutz-Jeghers syndrome raises ovarian tumor risk: STK11 loss predisposes to sex cord tumors with annular tubules (SCTAT) and mucinous ovarian tumors, alongside its GI hamartomas and breast cancer risk—so PJS is part of the hereditary differential for ovarian neoplasms.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Estrogen exposure shapes ovarian cancer risk: more lifetime ovulatory cycles and unopposed estrogen raise risk, while pregnancy, breastfeeding and contraceptives that suppress ovulation lower it—so reproductive and hormonal history strongly modulates this cancer.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Tumor-infiltrating cytotoxic T cells predict ovarian cancer outcome: high CD8 T-cell infiltration of high-grade serous tumors correlates with markedly better survival, evidence the immune system restrains the cancer—a rationale for immunotherapy in ovarian cancer.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Ovarian cancer spreads across the peritoneum to the liver surface: it sheds cells that seed the omentum and coat the liver capsule rather than invading the parenchyma early, so debulking these surface deposits is central to surgery, and ascites is common.
- `connects-to` → **[RAD51](../../03-molecular/rad51/README.md)** — Ovarian cancer's BRCA/RAD51 defect is its therapeutic Achilles' heel: ~half of high-grade serous tumors have homologous-recombination deficiency (BRCA, RAD51 pathway), so PARP inhibitors kill them by synthetic lethality—a major advance in maintenance therapy.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Ovarian cancer spreads through the abdomen onto the digestive tract: it sheds cells that coat the peritoneum, omentum and bowel surface, so it presents late with bloating and ascites and often causes bowel obstruction—dictating debulking surgery.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Ovarian cancer is strongly prothrombotic: tumor tissue factor and the bulky pelvic mass make venous thromboembolism common (a Trousseau-type hypercoagulability), so clots can be the presenting sign and prophylaxis is routine around surgery and chemo.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A loss defines the endometriosis-linked ovarian cancers: this chromatin-remodeling gene is frequently mutated in clear-cell and endometrioid tumors that arise from endometriosis, giving them biology distinct from the BRCA-driven high-grade serous type.
- `connects-to` → **[ATM](../../03-molecular/atm/README.md)** — ATM extends ovarian cancer's homologous-repair story beyond BRCA: germline or tumor ATM loss impairs DNA repair, marking some non-BRCA tumors as homologous-recombination deficient and potentially sensitive to platinum and PARP inhibitors.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Cancer-associated fibroblasts build ovarian cancer's metastatic niche: in the omentum they remodel the stroma, supply growth factors and promote chemoresistance, making this stromal cell a driver of the peritoneal spread that defines advanced disease.
- `connects-to` → **[Albumin](../../03-molecular/albumin/README.md)** — Ovarian cancer betrays itself through albumin-rich ascites: spreading across the peritoneum, it leaks fluid that swells the abdomen and drains albumin, so new ascites in a woman is a red flag and paracentesis both relieves and diagnoses it.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Ovarian cancer was the first tumor shown to use regulatory T cells to predict death: Tregs flood the malignant ascites and tumor, suppressing immunity—a landmark finding that helped launch the field of cancer immunosuppression.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Ovarian cancer disables NK cells in its ascites: the fluid around the tumor blunts natural killer cytotoxicity, helping floating tumor clusters survive—so restoring NK function is explored to fight peritoneal spread.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Ovarian cancer spreads across the gut: it sheds cells that seed the omentum and bowel surface as peritoneal carcinomatosis, so abdominal bloating and bowel obstruction—not pelvic symptoms—are often what finally brings the late-stage disease to light.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Ovarian cancer reaches the chest as malignant effusions: tumor spread to the pleura fills the space around the lungs with fluid, causing breathlessness, a common sign of advanced disease that upstages it and guides drainage and systemic therapy.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells shape the immune fight against ovarian cancer: as antigen-presenters they prime the T-cell response, and their dysfunction in the tumor and ascites helps it evade immunity—so dendritic-cell vaccines are explored to rebuild it.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — A rare ovarian cancer spikes blood calcium: the small-cell carcinoma of hypercalcemic type (SCCOHT) drives a paraneoplastic hypercalcemia, so high calcium in a young woman with an ovarian mass is a warning.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Ovarian cancer can back up the kidneys: a bulky pelvic mass or nodal spread compresses the ureters, causing hydronephrosis and post-renal kidney injury in advanced disease.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — Ovarian cancer feeds on the omentum's fat cells: it spreads to the fatty omentum, where adipocytes supply fatty acids that fuel tumor growth—the 'omental caking' typical of advanced disease.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photons hunt this silent cancer: transvaginal ultrasound probes a suspicious mass, CT maps the peritoneal spread and ascites that mark advanced disease, and PET tracks recurrence — imaging that, with CA-125, guides every step of management.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — Ovarian cancer studs the spleen's surface: spreading through the peritoneal fluid, it seeds the splenic capsule and nearby diaphragm, so splenectomy is sometimes part of the aggressive debulking surgery that aims to leave no visible tumor.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Ovarian cancer commandeers platelets: tumor-driven IL-6 and thrombopoietin spark a paraneoplastic thrombocytosis, and these elevated platelets in turn shield circulating tumor cells and fuel growth, marking more aggressive, advanced disease.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — First-line chemotherapy stings the nerves: paclitaxel, the taxane paired with carboplatin against ovarian cancer, damages peripheral sensory neurons, leaving a stocking-glove numbness and tingling that can outlast the treatment.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy traces ovarian cancer to its source: most high-grade serous tumors begin not in the ovary but in the fallopian tube's secretory cells, distinguished by EM from their ciliated neighbors at the fimbrial end.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Platinum chemotherapy drains magnesium: carboplatin injures the kidney's tubules, which then waste magnesium, so blood levels are watched and replaced through the months of ovarian cancer treatment.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies track and treat the disease: the CA-125 tumor marker is measured by an antibody immunoassay to follow response and relapse, while anti-VEGF bevacizumab is added to chemotherapy to starve the tumor's blood supply.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — The carboplatin-paclitaxel backbone hammers the marrow: both drugs are myelosuppressive, so the neutrophil count falls between cycles and febrile neutropenia is one of the recurring hazards of ovarian-cancer chemotherapy.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Anemia shadows the long course: chronic disease, repeated chemotherapy, and the slow ooze of peritoneal disease deplete red cells, the fatigue of low erythrocytes often needing transfusion across months of treatment.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — Even the gentler anthracycline touches the heart: pegylated liposomal doxorubicin, a mainstay for recurrent ovarian cancer, still injures cardiomyocytes in a cumulative dose-dependent way, so cardiac function is tracked across repeated lines of therapy.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — The malignant ascites runs on IL-6-STAT3: cytokines in the peritoneal fluid activate STAT3 in tumor and stromal cells, fueling growth, immune evasion and the relentless fluid build-up that distends the abdomen of advanced disease.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — The immune infiltrate predicts survival: ovarian tumors rich in tumor-infiltrating T cells, including CD4 helpers that marshal the response, carry a markedly better prognosis — the biology behind efforts to make this cancer respond to immunotherapy.
- `connects-to` → **[PALB2](../../03-molecular/palb2/README.md)** — The BRCA story extends beyond BRCA: germline PALB2 mutations, which partner BRCA2 in homologous-recombination repair, also raise ovarian cancer risk and leave the tumor sensitive to platinum and PARP inhibitors, widening who benefits from genetic testing.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — It is a famously vascular tumor: ovarian cancer drives endothelial cells to sprout new vessels and leak fluid, fueling the malignant ascites that swells the abdomen — the rationale for adding the anti-VEGF drug bevacizumab to its treatment.
- `connects-to` → **[Pancreatic Cancer](../pancreatic-cancer/README.md)** — It travels in a shared hereditary cluster: the same BRCA and PALB2 mutations that drive ovarian cancer also raise pancreatic cancer risk, so a family history can span both organs and flag relatives for combined surveillance.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12 guides the spread to the omentum: the chemokine, abundant in peritoneal fat, draws CXCR4-bearing ovarian cancer cells to seed the omentum and peritoneum, the characteristic transcoelomic metastasis of the disease.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Advanced disease invites sepsis: malignant bowel obstruction and perforation from peritoneal spread, plus chemotherapy neutropenia, expose ovarian-cancer patients to intra-abdominal infection and sepsis.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells populate the tumor and ascites: they accumulate in the ovarian tumor microenvironment and peritoneal fluid, releasing angiogenic and immunomodulatory mediators that support growth and vessel formation.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — The inflamed peritoneal milieu runs on NF-κB: ovarian cancer's ascites is rich in cytokines that activate NF-κB, driving the tumor-cell survival, chemoresistance and immune evasion behind its peritoneal spread.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Pelvic disease and platinum strain the kidneys: bulky tumor obstructing the ureters causes hydronephrosis, and the cisplatin used to treat ovarian cancer is nephrotoxic — together a real risk of chronic kidney disease.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Chronic disease and chemo drain the blood: the inflammatory cytokines of ovarian cancer and its marrow-suppressing platinum chemotherapy produce a prominent anemia of chronic disease.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Removing the ovaries strips away bone-protective estrogen: surgical oophorectomy and chemotherapy throw younger patients into abrupt menopause, and the loss of estrogen accelerates bone loss toward osteoporosis.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Its liposomal anthracycline can weaken the heart: pegylated liposomal doxorubicin, widely used in recurrent ovarian cancer, carries cumulative cardiotoxicity that can erode cardiac function into heart failure.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Late diagnosis and high relapse weigh on mood: ovarian cancer's frequent advanced-stage presentation, repeated recurrences and abrupt surgical menopause contribute to substantial depression and anxiety.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Its taxane-platinum chemo numbs the nerves: the paclitaxel and carboplatin central to ovarian-cancer treatment cause a dose-dependent, often persistent peripheral neuropathy with painful paraesthesiae.
- `connects-to` → **[Acute Myeloid Leukemia](../aml/README.md)** — Years of DNA-damaging therapy can seed leukaemia: the platinum chemotherapy and PARP inhibitors used in ovarian cancer carry a small but real risk of therapy-related myelodysplasia and acute myeloid leukaemia.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A relapsing cancer watched by a blood marker breeds worry: the recurrent course of ovarian cancer and the dread of a rising CA-125 between scans foster chronic health anxiety alongside depression.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Cytoreductive surgery is extensive: ovarian-cancer debulking removes peritoneal and bowel disease in long operations, leaving large abdominal wounds and anastomoses prone to leak and slow healing.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It floods the chest with fluid: advanced ovarian cancer spreads across the diaphragm to cause malignant pleural effusions, a common marker of stage IV disease and a source of breathlessness.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Removing the ovaries forces menopause: bilateral salpingo-oophorectomy for ovarian cancer abruptly ends ovarian oestrogen, causing surgical menopause with its hormonal, bone and vasomotor effects.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It spreads to the deep nodes: ovarian cancer disseminates to pelvic and para-aortic lymph nodes, so lymphadenectomy is part of its surgical staging.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It can attack the brain by autoimmunity: ovarian cancer causes paraneoplastic anti-Yo cerebellar degeneration, and ovarian teratomas are the classic trigger of anti-NMDA-receptor encephalitis.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Its drugs blister the hands and feet: pegylated liposomal doxorubicin causes hand-foot syndrome (palmar-plantar erythrodysesthesia), and bevacizumab impairs wound healing.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — PARP inhibitors transformed its care: olaparib and other PARP inhibitors exploit the homologous-recombination defect of BRCA-mutant ovarian cancer, with bevacizumab adding anti-angiogenic benefit.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It obstructs and its drugs poison the kidney: bulky pelvic and retroperitoneal ovarian cancer can block the ureters causing hydronephrosis, and cisplatin chemotherapy is nephrotoxic.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — It clots and its treatment strains the heart: ovarian cancer is strongly prothrombotic, and bevacizumab causes hypertension with thromboembolic and bleeding risks.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Platinum-taxane is the backbone: carboplatin with paclitaxel after debulking surgery is the chemotherapy foundation, and platinum sensitivity guides treatment at relapse.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Largely resistant despite immune cells: although ovarian cancer harbours tumour-infiltrating lymphocytes that predict prognosis, its immunosuppressive microenvironment has left checkpoint inhibitors mostly ineffective.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Its immune infiltrate predicts survival: the density of tumour-infiltrating lymphocytes strongly predicts outcome in ovarian cancer, yet regulatory T cells and an immunosuppressive milieu blunt the antitumour response.
- `connects-to` → **[Prostate Cancer](../prostate-cancer/README.md)** — Shared BRCA vulnerability across the sexes: like high-grade serous ovarian cancer, BRCA-mutant prostate cancer carries homologous-recombination deficiency and responds to PARP inhibitors, placing both in the HBOC spectrum despite opposite organs.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — B-cell islands sharpen the prognosis: high-grade serous ovarian cancers that build tertiary lymphoid structures with germinal-centre B cells and plasma cells show stronger antitumour immunity and better survival than those with T cells alone.
- `connects-to` → **[Gastric Cancer](../gastric-cancer/README.md)** — The source of a Krukenberg tumour: metastatic gastric and other GI signet-ring carcinomas seed the ovaries as Krukenberg tumours, a classic ovarian metastasis that mimics primary ovarian cancer and must be distinguished from it.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — Peritoneal spread and bowel obstruction: ovarian cancer disseminates across the peritoneum, encasing the bowel ('omental caking') and infiltrating the intestinal epithelium, so bowel obstruction becomes a leading cause of death.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Liver and capsular involvement: ovarian cancer studs the liver capsule with perihepatic implants and metastasises to the hepatic lobule in advanced disease.
- `connects-to` → **[WT1](../../03-molecular/wt1/README.md)** — A diagnostic marker: high-grade serous ovarian carcinoma characteristically expresses WT1, an immunohistochemical marker that helps confirm its tubal/serous origin over other gynaecological cancers.
- `connects-to` → **[MDS](../mds/README.md)** — Late cost of treatment: platinum chemotherapy and PARP inhibitors used for ovarian cancer damage haematopoietic stem cells, raising the risk of therapy-related myelodysplasia and acute leukaemia years later.
- `connects-to` → **[Colorectal Cancer](../colorectal-cancer/README.md)** — Differential of an ovarian mass: colorectal cancer can metastasise to the ovary (Krukenberg-type spread) and seed the peritoneum like advanced ovarian cancer, while Lynch syndrome predisposes to both tumours.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — A vascular target: high-grade serous ovarian carcinoma is intensely angiogenic, and the anti-VEGF antibody bevacizumab attacks the tumour's arterial supply, a mainstay added to chemotherapy in advanced disease.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Amplified oncogene: MYC amplification is common in high-grade serous ovarian carcinoma, driving the proliferation of this genomically unstable tumour.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — Cell-cycle dysregulation: CCNE1 amplification and CDK4/6-cyclin activity disrupt the cell cycle in a subset of ovarian cancers, an avenue for cell-cycle-targeted therapy.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — Notch3 driver: NOTCH3 amplification and Notch signalling recur in ovarian cancer, promoting growth and contributing to platinum chemoresistance.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K/AKT survival: AKT-pathway activation drives ovarian cancer growth and survival and contributes to chemoresistance, a targetable node in combination therapy.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Ascites and hypoxia: HIF-1α stabilised in the hypoxic ovarian tumour and its ascitic spheroids drives angiogenesis and the peritoneal spread of high-grade serous cancer.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Epigenetic driver: EZH2 overexpression silences tumour-suppressor genes in ovarian cancer, promoting proliferation and an emerging epigenetic therapeutic target.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — IL-6 is abundant in ovarian-cancer ascites, where it drives JAK-STAT3 signaling that sustains tumor-cell survival and spheroid formation and fuels the cachexia that marks advanced peritoneal disease—an inflammatory axis layered on the HRD genetics.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — TGF-β in the omental microenvironment drives the mesothelial-to-mesenchymal transition that prepares the peritoneum for ovarian-cancer implantation, while excluding T cells from the tumor to blunt immunotherapy in this otherwise "cold" cancer.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — BRCA-mutant, homologous-recombination-deficient ovarian cancers accumulate cytosolic DNA that activates cGAS-STING, generating type-I interferon—the innate-immune rationale for combining PARP inhibitors with checkpoint blockade in HRD disease.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Carboplatin-paclitaxel kills ovarian carcinoma through caspase-3-mediated apoptosis, and the eventual evasion of this death program defines the platinum-resistant relapse that is the lethal phase of high-grade serous disease.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN loss activates PI3K-AKT signaling in the endometriosis-associated endometrioid and clear-cell ovarian carcinomas, the histotypes distinct from BRCA-driven high-grade serous disease.
- `connects-to` → **[MLH1](../../03-molecular/mlh1/README.md)** — MLH1 silencing produces the microsatellite-instable endometrioid and clear-cell ovarian cancers seen in Lynch syndrome, a DNA-repair defect distinct from BRCA-related homologous-recombination loss and a basis for checkpoint blockade.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — KRAS-activating mutations define the low-grade serous and mucinous ovarian carcinomas, a biology distinct from the p53/BRCA-driven high-grade serous disease and the rationale for MEK inhibitors in these chemo-resistant histotypes.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PIK3CA mutation and amplification activate the PI3K-AKT-mTOR axis already mapped here through AKT and PTEN, sustaining ovarian cancer survival signaling and supporting combination strategies with PI3K-pathway inhibitors.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — CCL2 secreted by ovarian tumor cells recruits monocytes that become the tumor-associated macrophages dominating malignant ascites, building the immunosuppressive peritoneal niche that drives chemoresistance and spread.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — KRAS and BRAF mutations (KRAS mapped) activate the MAPK-ERK cascade that drives low-grade serous and mucinous ovarian cancers, a MEK-inhibitor-responsive subset distinct from high-grade serous disease.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — Cyclin-E and the CDK4/6 axis (mapped) release E2F1 to force the G1-S transition, with CCNE1 amplification a recurrent proliferative driver of high-grade serous ovarian cancer.
- `connects-to` → **[HER2](../../03-molecular/her2/README.md)** — A fraction of ovarian carcinomas overexpress HER2, feeding the PI3K and MAPK pathways (mapped) and offering a target for HER2-directed antibody-drug conjugates.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — IL-6-JAK-STAT3 signaling (IL-6 and STAT3 already mapped), abundant in malignant ascites, supports the survival and chemoresistance of ovarian-cancer cells.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — RB-pathway dysregulation, including the CCNE1 amplification frequent in high-grade serous ovarian cancer, drives cell-cycle progression released through E2F1 (already mapped).
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2 amplification offers an alternative route to inactivation of the near-universally dysfunctional p53 (already mapped) in high-grade serous ovarian cancer.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 promotes ovarian-cancer cell adhesion, spheroid formation and the peritoneal dissemination of metastatic disease.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β mapped) drives EMT and the peritoneal-metastatic, immunosuppressive microenvironment of ovarian cancer.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A loss releases CDK4/6-cyclin-D control of the cell cycle, a recurrent lesion in high-grade serous ovarian cancer.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — BRCA/HRD-driven cytosolic DNA activates cGAS-STING (mapped) and IFN-STAT1 signaling, shaping the immunogenicity of high-grade serous ovarian cancer.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO tumor-suppressor activity, antagonized by PI3K-AKT signaling, is lost in the proliferative progression of ovarian cancer.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated CD8 cytotoxicity drives the antitumor immune response whose magnitude predicts outcome in high-grade serous ovarian cancer.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the survival and Wnt/β-catenin signaling of ovarian cancer.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the immunosuppressive, ascites-associated microenvironment of ovarian cancer.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-kinase signaling drives the peritoneal dissemination and invasion of ovarian cancer.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of ovarian cancer.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival and chemoresistance of ovarian cancer cells, particularly in dormant peritoneal micrometastases.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of ovarian cancer within the omental adipose niche.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven macrophage recruitment shapes the immunosuppressive ascites microenvironment of ovarian cancer.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation in the peritoneal microenvironment participates in the progression of ovarian cancer.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Endothelin-1 autocrine signaling participates in the proliferation, angiogenesis, and invasion of ovarian cancer.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of ovarian cancer.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory tumor microenvironment of ovarian cancer.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory tumor microenvironment and ascites of ovarian cancer.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Immune prognosis: intratumoral T-cell infiltration is one of the strongest prognostic factors in ovarian cancer, and MHC class II antigen presentation shapes the CD4 help behind that response, with loss of presentation a route to immune escape and immunotherapy resistance.
- `connects-to` → **[AXL receptor](../../03-molecular/axl-receptor/README.md)** — Platinum resistance: the AXL receptor tyrosine kinase drives epithelial-mesenchymal transition, peritoneal metastatic spread and acquired platinum resistance in ovarian cancer, positioning AXL inhibition as a strategy against the chemoresistant relapse that defines the disease.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — Apoptotic evasion: high-grade serous ovarian cancer resists chemotherapy partly through anti-apoptotic BCL-2 family proteins that raise the threshold for caspase activation (caspase-3 already mapped), a target of BH3-mimetic sensitisation strategies.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Cellular immunotherapy: IL-2-driven T-cell expansion supports the adoptive and tumour-infiltrating-lymphocyte therapies being explored for ovarian cancer, whose response to single-agent checkpoint blockade (PD-1 already mapped) has been modest.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Anaemia: ovarian cancer lowers haemoglobin through chronic disease, occult blood loss and platinum-chemotherapy myelosuppression, contributing to the fatigue that burdens patients and often requiring transfusion or growth-factor support.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Treatment cardiotoxicity: the anti-angiogenic bevacizumab (VEGF already mapped) and chemotherapy used in ovarian cancer can injure the heart, and troponin elevation helps detect the cardiac toxicity that complicates prolonged treatment.
- `connects-to` → **[Small intestine](../../06-organ/small-intestine/README.md)** — Bowel obstruction: transcoelomic spread of ovarian cancer over the small intestine and its mesentery causes the malignant bowel obstruction (large intestine already mapped) that is a common and difficult terminal complication.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive ascites: IL-10 in the malignant ascites and its tumour-associated macrophages (already mapped) dampens the anti-tumour T-cell response (CD8 already mapped), part of the immune evasion of ovarian cancer.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative and lysis stress: platinum chemotherapy and rapid cell turnover in ovarian cancer generate oxidative stress and release purines that xanthine oxidase converts to uric acid, adding oxidative and tumour-lysis burden.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises the tumour-associated macrophages (already mapped) of the malignant ascites toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the immune-evasive microenvironment of ovarian cancer.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Anaemia and transfusion: the chronic disease and the platinum chemotherapy of ovarian cancer cause anaemia (haemoglobin already mapped) that can require transfusion, whose repeated support can load the body with iron.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Tumour vasculature and ascites: nitric oxide with VEGF and endothelin-1 (already mapped) regulates the angiogenesis and vascular permeability that drive the malignant ascites of ovarian cancer.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage (already mapped) and type-2 milieu of the immunosuppressive ascites and omental microenvironment of ovarian cancer.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Omental adipose niche: leptin links obesity to ovarian-cancer risk, and the adipocyte-rich omentum — a favoured metastatic site — supplies the fatty acids and adipokines that fuel the peritoneal spread.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin sequesters iron and adds an anaemia of chronic disease to the platinum-chemotherapy anaemia (iron and haemoglobin already mapped) of ovarian cancer.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Omental adipokine: adiponectin, with leptin (already mapped), of the omental adipose niche modulates the ovarian-cancer growth and the peritoneal (large intestine already mapped) spread.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the omental adipose-inflammatory adipokine of the peritoneal niche of ovarian cancer.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — HRD immunogenicity: the homologous-recombination-deficient (BRCA already mapped) ovarian cancer activates the cGAS-STING (already mapped) pathway to produce the type-I interferon that drives the immunogenicity and the checkpoint (PD-1 already mapped) response.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity of the immunogenic HRD ovarian cancer.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response of the ovarian-cancer immune microenvironment.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 arm of the immune microenvironment of the ovarian-cancer peritoneal niche.
- `connects-to` → **[Plasma cell](../../04-cellular/plasma-cell/README.md)** — Tertiary lymphoid B-cell response: the plasma cells and B cells of the tumour tertiary lymphoid structures produce antibody (already mapped) and, with the CD8 TILs (already mapped), predict a favourable prognosis in ovarian cancer.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the ovarian-cancer peritoneal microenvironment.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2/AllergoOncology arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), is the antibody arm explored in the AllergoOncology anti-tumour response against ovarian cancer.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Tertiary lymphoid structures: the B cells organise the intratumoural tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, predicts a favourable prognosis in ovarian cancer.
- `connects-to` → **[Vitamin D](../../../03-medicine/03-food/vitamin-d/README.md)** — Prognostic vitamin: the vitamin D status is associated with the ovarian-cancer risk and outcome and modulates the tumour immune microenvironment.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) recruits and polarises the myeloid cells to an immunosuppressive phenotype in the ovarian-cancer peritoneal microenvironment.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its activation (with C3 and C5aR1 already mapped) contribute to the complement-driven inflammation of the ovarian-cancer peritoneal microenvironment.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement evasion: the ovarian-cancer cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), evading the complement attack in the peritoneal microenvironment.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Ascites iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the anaemia and the iron-rich malignant ascites of ovarian cancer.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Peritoneal alarmin: TSLP released by ovarian epithelial and stromal cells activates mast cells and dendritic cells, promoting the type-2 microenvironment of the peritoneal cavity that suppresses anti-tumour cytotoxicity.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Peritoneal metastasis scaffold: periostin, upregulated in the ovarian cancer stroma and malignant ascites, promotes the peritoneal adhesion and omental colonisation that characterise the widespread intraperitoneal dissemination of this cancer.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell histamine: stromal mast-cell-derived histamine promotes VEGF-driven angiogenesis and suppresses NK and T-cell cytotoxicity in the ovarian cancer ascites, contributing to the immunosuppressive peritoneal microenvironment.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Peritoneal kinin: bradykinin accumulates in the malignant ascites of ovarian cancer, activating B1/B2 receptors on peritoneal mesothelium and sensory fibres, amplifying pain and vascular permeability of the peritoneal microenvironment.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement regulation: C1-esterase inhibitor restrains the classical complement pathway in the ovarian-cancer peritoneal milieu, limiting the C3/C5/C5aR1 (all already mapped) cascade driving the immunosuppressive ascites microenvironment.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Treatment anaemia: erythropoietin corrects the chemotherapy-induced anaemia of ovarian cancer; EPOR expression on tumour cells raises the question of direct EPO-driven signalling influencing platinum- and taxane-based regimen responses.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Peritoneal melatonin: melatonin inhibits ovarian cancer proliferation and ascites formation by suppressing VEGF (already mapped)-driven angiogenesis via MT1/MT2-mediated cAMP reduction and by enhancing NK-cell (already mapped) cytotoxicity against peritoneal deposits.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Ovarian cancer androgen axis: testosterone via androgen receptor promotes epithelial ovarian cancer proliferation (particularly low-grade serous histology) and amplifies KRAS (already mapped) and PI3K/AKT (already mapped)-driven tumour growth.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Ascites serotonin signalling: serotonin accumulates in ovarian cancer ascites, activating 5-HT2 receptors on peritoneal deposits to promote adhesion and VEGF (already mapped)-driven angiogenesis, amplifying the immunosuppressive malignant peritoneal microenvironment.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Ovarian cancer prolactin: prolactin via JAK2/STAT3 (already mapped) activates ovarian cancer cells and macrophages (already mapped), promoting VEGF (already mapped) expression and NF-κB (already mapped)-driven immunosuppression in the peritoneal ascites microenvironment.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Ovarian cancer oxytocin: oxytocin receptors on ovarian cancer epithelial cells couple to Gαq-IP3-PKC, cross-activating PI3K/AKT (already mapped) and VEGF (already mapped) signalling to promote peritoneal implantation and ascites formation.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Ovarian cancer vasopressin: vasopressin via V1a receptors on ovarian cancer and stromal cells activates Gαq-PKC and PKA signalling, promoting VEGF (already mapped)-driven ascites angiogenesis and NF-κB (already mapped)-mediated peritoneal invasion.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Ovarian cancer selenium: selenium, as GPx in macrophages (already mapped) and T-cytotoxic cells (already mapped), scavenges ROS in the ovarian tumour microenvironment; selenium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) pro-tumour cascade.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Ovarian cancer iodine: iodine-dependent thyroid hormones regulate macrophage (already mapped) polarisation and T-cytotoxic (already mapped) immune surveillance; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) pro-tumour cascade of ovarian cancer.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Ovarian cancer sodium: excess sodium promotes macrophage (already mapped) and mast-cell (already mapped) pro-inflammatory activation; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) skewing amplifies T-cytotoxic (already mapped) suppression in ovarian cancer.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Ovarian cancer copper: copper-dependent enzymes in macrophages (already mapped) and T-cytotoxic cells (already mapped) sustain tumour-immune crosstalk; copper excess amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade and mast-cell (already mapped) skewing in ovarian cancer.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Ovarian cancer potassium: potassium efflux gates the macrophage (already mapped) and mast-cell (already mapped) NLRP3 inflammasome; potassium loss amplifies NF-κB (already mapped) and IL-6 (already mapped) pro-tumour cascade and suppresses T-cytotoxic (already mapped) killing in ovarian cancer.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Ovarian cancer phosphorus: phosphorus-dependent ATP in macrophages (already mapped) and T-cytotoxic cells (already mapped) sustains tumour immune surveillance; phosphorus dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of ovarian cancer.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Ovarian cancer carbon: carbon as backbone of VEGF (already mapped) and NF-κB (already mapped) proteins in tumour cells and macrophages (already mapped) sustains signalling; carbon depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of ovarian cancer.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — Ovarian cancer chloride: chloride channels in macrophages (already mapped) and tumour cells modulate cell-volume and invasive potential; chloride imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade of ovarian cancer.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — Ovarian cancer hydrogen: hydrogen, via redox homeostasis in tumour cells and macrophages (already mapped), supports VEGF (already mapped) signalling; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) oxidative cascade of ovarian cancer.

[^burger-2011-gog0218]: Burger RA, Brady MF, Bookman MA, et al. Incorporation of bevacizumab in the primary treatment of ovarian cancer. *N Engl J Med.* 2011;365(26):2473-2483. [doi:10.1056/NEJMoa1104390](https://doi.org/10.1056/NEJMoa1104390) · [PubMed 22204724](https://pubmed.ncbi.nlm.nih.gov/22204724/)
[^moore-2018-olaparib-solo1]: Moore K, Colombo N, Scambia G, et al. Maintenance olaparib in patients with newly diagnosed advanced ovarian cancer. *N Engl J Med.* 2018;379(26):2495-2505. [doi:10.1056/NEJMoa1810858](https://doi.org/10.1056/NEJMoa1810858) · [PubMed 30345884](https://pubmed.ncbi.nlm.nih.gov/30345884/)
