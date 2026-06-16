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

[^burger-2011-gog0218]: Burger RA, Brady MF, Bookman MA, et al. Incorporation of bevacizumab in the primary treatment of ovarian cancer. *N Engl J Med.* 2011;365(26):2473-2483. [doi:10.1056/NEJMoa1104390](https://doi.org/10.1056/NEJMoa1104390) · [PubMed 22204724](https://pubmed.ncbi.nlm.nih.gov/22204724/)
[^moore-2018-olaparib-solo1]: Moore K, Colombo N, Scambia G, et al. Maintenance olaparib in patients with newly diagnosed advanced ovarian cancer. *N Engl J Med.* 2018;379(26):2495-2505. [doi:10.1056/NEJMoa1810858](https://doi.org/10.1056/NEJMoa1810858) · [PubMed 30345884](https://pubmed.ncbi.nlm.nih.gov/30345884/)
