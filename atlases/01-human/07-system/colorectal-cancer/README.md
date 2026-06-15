---
schema: human-scale-entry/v1
id: colorectal-cancer
name: Colorectal Cancer
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Second leading cause of cancer deaths; driven by APC/Wnt loss → adenoma-carcinoma sequence, then KRAS, SMAD4, and TP53 mutations. EGFR blockade (cetuximab) for RAS-wild-type metastatic disease; KRAS/BRAF V600E inhibitors and pembrolizumab (MSI-H) are molecularly targeted."
aliases: ["CRC", "colon cancer", "rectal cancer", "colorectal carcinoma", "adenocarcinoma of colon", "mCRC", "Lynch syndrome", "FAP"]
sources:
  - id: siegel-2024-crc-statistics
    type: peer-reviewed
    cite: "Siegel RL, Giaquinto AN, Jemal A. Cancer statistics, 2024. CA Cancer J Clin. 2024;74(1):12-49."
    doi: "10.3322/caac.21820"
    pmid: "38230766"
    url: "https://doi.org/10.3322/caac.21820"
  - id: van-cutsem-2011-crystal-cetuximab
    type: peer-reviewed
    cite: "Van Cutsem E, Köhne CH, Láng I, et al. Cetuximab plus irinotecan, fluorouracil, and leucovorin as first-line treatment for metastatic colorectal cancer: updated analysis of overall survival according to tumor KRAS and BRAF mutation status. J Clin Oncol. 2011;29(15):2011-2019."
    doi: "10.1200/JCO.2010.33.5091"
    pmid: "21502544"
    url: "https://doi.org/10.1200/JCO.2010.33.5091"
  - id: kopetz-2019-beacon-crc
    type: peer-reviewed
    cite: "Kopetz S, Grothey A, Yaeger R, et al. Encorafenib, binimetinib, and cetuximab in BRAF V600E-mutated colorectal cancer. N Engl J Med. 2019;381(17):1632-1643."
    doi: "10.1056/NEJMoa1908075"
    pmid: "31566309"
    url: "https://doi.org/10.1056/NEJMoa1908075"
cross_links:
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "KRAS mutations (~40% of CRC) are acquired in the adenoma-carcinoma sequence; KRAS G12V/G12D-mutant CRC is resistant to EGFR inhibitors (cetuximab, panitumumab); KRAS G12C-mutant CRC → adagrasib + cetuximab (KRYSTAL-10, ORR 34%) — first targeted therapy for CRC with KRAS."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "APC loss is the founding mutation in >80% of sporadic CRC; APC → destruction complex collapse → beta-catenin nuclear accumulation → MYC, cyclin D1 → hyperproliferation; germline APC mutation causes FAP → thousands of colonic polyps → obligate CRC."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "EGFR is overexpressed in >80% of CRC; cetuximab and panitumumab improve OS in RAS-wild-type metastatic CRC (CRYSTAL: cetuximab + FOLFIRI vs. FOLFIRI, PFS 9.9 vs. 8.4 months in KRAS-wt); RAS/RAF-wild-type biomarker required for EGFR inhibitor benefit."
  - target: 01-human/03-molecular/braf
    relation: connects-to
    note: "BRAF V600E mutations (~8-10% of CRC) confer poor prognosis and EGFR inhibitor resistance; BEACON CRC: encorafenib + cetuximab → OS 9.3 vs. 5.9 months vs. control in BRAF V600E mCRC; BRAF V600E CRC is enriched in MSI-H tumors and right-sided cancers."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "FN-integrin α5β1/αvβ3 signaling drives EMT in CRC → vimentin, N-cadherin, MMP production → invasion and liver metastasis; EDB-FN is overexpressed in CRC stroma; tumor FN correlates with lymph node metastasis and worse prognosis in stage II-III CRC."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Most colorectal cancers arise in the large intestine via the adenoma-carcinoma sequence, so colonoscopy with polypectomy is preventive; right-sided tumors bleed occultly (→ anemia) while left-sided ones obstruct, and rectal cancer is resected by total mesorectal excision."
  - target: 01-human/07-system/lynch-syndrome
    relation: connects-to
    note: "Lynch syndrome (germline MMR loss) causes ~3% of colorectal cancer, producing dMMR/MSI-H tumors that are hypermutated and exquisitely sensitive to PD-1 blockade — pembrolizumab is now first-line for MSI-H metastatic CRC; universal MMR/MSI testing of all CRC is recommended."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 loss (~75% of CRC) is the rate-limiting step that converts an advanced adenoma into invasive carcinoma: 17p loss plus TP53 mutation removes the DNA-damage checkpoint, unleashing the chromosomal instability that lets cells breach the muscularis mucosae."
  - target: 01-human/07-system/prostate-cancer
    relation: connects-to
    note: "Colorectal and prostate cancers are two of the commonest adult solid tumours; both have hereditary drivers—Lynch raises both, BRCA2 raises prostate—and microsatellite-unstable CRC and DNA-repair-deficient prostate cancer both respond to checkpoint or PARP-based therapy."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver is the dominant site of colorectal metastasis via portal venous drainage: ~50% of CRC patients develop liver mets, and resection or ablation of oligometastatic liver disease can be curative; this portal route makes CRC liver-metastasis management central to oncology."
  - target: 01-human/07-system/fap
    relation: connects-to
    note: "Familial adenomatous polyposis, from germline APC mutation, carpets the colon with hundreds-to-thousands of adenomas and guarantees colorectal cancer by mid-adulthood without prophylactic colectomy; APC loss is also the founding event in >80% of sporadic CRC."
  - target: 01-human/07-system/mutyh-associated-polyposis
    relation: connects-to
    note: "MUTYH-associated polyposis is a recessive hereditary cause of colorectal cancer: biallelic MUTYH loss fails to repair oxidative DNA damage, producing G:C→T:A mutations and multiple adenomas, so a FAP-like polyposis with negative APC testing prompts MUTYH analysis."
  - target: 01-human/07-system/inflammatory-bowel-disease
    relation: connects-to
    note: "Long-standing inflammatory bowel disease drives colitis-associated colorectal cancer: chronic inflammation accelerates the dysplasia-carcinoma sequence (often p53 early, APC late—reversed from sporadic CRC), so colitis warrants surveillance colonoscopy."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "The MSI-high subset of colorectal cancer is exquisitely immunotherapy-responsive: mismatch-repair deficiency generates abundant neoantigens that draw cytotoxic CD8+ T cells, so anti-PD-1 (pembrolizumab) works in MSI-high tumors while microsatellite-stable CRC remains resistant."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "The gut microbiome shapes colorectal cancer risk: dysbiosis enriches pro-carcinogenic bacteria (e.g. Fusobacterium) that inflame mucosa and damage DNA, while a healthy fiber-fermenting flora is protective—linking the microbial ecosystem to tumorigenesis."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Obesity is a major modifiable colorectal cancer risk factor: visceral adiposity drives insulin/IGF-1 signaling and chronic inflammation that promote colonic tumorigenesis, so rising early-onset CRC parallels obesity—weight and diet are key prevention levers."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Radiotherapy is central to rectal (not colon) cancer: neoadjuvant chemoradiation with photon beams shrinks locally advanced rectal tumors before surgery, sometimes enough for watch-and-wait—colon cancer, by contrast, is treated with surgery and chemotherapy."
  - target: 01-human/03-molecular/apc
    relation: connects-to
    note: "APC loss is the gatekeeper mutation that starts colorectal cancer: inactivating APC unleashes Wnt/beta-catenin to form the first adenoma, so it initiates the adenoma-carcinoma sequence—mutated in FAP and in most sporadic colorectal cancers."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: targets
    note: "Colorectal cancer arises stepwise from the intestinal epithelium: normal crypt cells acquire APC, then KRAS, then p53 hits, progressing through adenoma to carcinoma—the textbook adenoma-carcinoma sequence that makes screening colonoscopy preventive."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "PD-1 is the checkpoint that MSI-high colorectal tumors exploit to evade attack: blocking it produced the first tissue-agnostic FDA approval (pembrolizumab for any MSI-high cancer), so dMMR/MSI status is now tested at diagnosis to guide immunotherapy."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Type 2 diabetes raises colorectal cancer risk: high insulin and IGF-1 from insulin resistance promote colonocyte proliferation, and shared risks like obesity and inactivity compound it—so metabolic health is part of colorectal cancer prevention."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "After the liver, the lung is colorectal cancer's next metastatic stop: tumor cells reach it via the systemic circulation, and isolated lung metastases are sometimes surgically resected for cure—so chest imaging is routine in staging and follow-up."
  - target: 01-human/03-molecular/her2
    relation: connects-to
    note: "A subset of colorectal cancers are HER2-amplified: like in breast and gastric cancer, this drives growth and predicts resistance to anti-EGFR drugs, but responds to HER2-targeted combinations—so HER2 testing now guides therapy in metastatic disease."
  - target: 01-human/07-system/iron-deficiency-anemia
    relation: connects-to
    note: "Right-sided colorectal cancer often presents as iron-deficiency anemia: a slow-bleeding tumor depletes iron long before obstruction, so unexplained iron-deficiency anemia in an adult mandates colonoscopy to exclude colon cancer."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D and calcium intake are linked to colorectal risk: higher levels associate with lower incidence, and vitamin D's effects on colonocyte growth make it a studied (if unproven) chemopreventive alongside fiber and aspirin."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Cancer-associated fibroblasts drive colorectal progression: they remodel the tumor stroma, supply growth and survival signals, and promote chemoresistance and metastasis—a major reason the desmoplastic, fibroblast-rich CMS4 subtype carries a worse prognosis."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Colorectal cancer is treated by starving its vessels of VEGF: the tumor secretes VEGF to build a blood supply, so anti-VEGF bevacizumab is a mainstay added to chemotherapy in metastatic colorectal cancer."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "Colorectal cancer turns aggressive when it loses SMAD4: this late hit in the adenoma-carcinoma sequence disables TGF-β's growth restraint, driving invasion and metastasis and predicting a worse prognosis and poorer chemo response."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Most colorectal cancers are immune-cold, walled off by regulatory T cells: unlike MSI-high tumors, microsatellite-stable CRC has few neoantigens and Treg-rich stroma, which is why checkpoint immunotherapy works in only a minority."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Dietary calcium helps guard against colorectal cancer: it binds bile acids and fatty acids in the gut and signals colon cells to differentiate, so adequate calcium is one of the better-supported dietary protections against the disease."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Tumor-associated macrophages shape colorectal cancer: depending on their polarization they can promote or restrain the tumor, and a macrophage-rich, suppressive stroma helps the common microsatellite-stable cancers evade immunity."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Colorectal cancer can reach the brain late: though it spreads first to liver and lung, advanced disease occasionally seeds brain metastases, a sign of widespread disease that shifts care toward palliative and systemic treatment."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron deficiency is often the first clue to colorectal cancer: right-sided tumors bleed slowly into the stool, so unexplained iron-deficiency anemia in an older adult is a red flag that should prompt a colonoscopy."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Colorectal tumors build their own blood supply: VEGF recruits endothelial cells to sprout new vessels, and blocking this with bevacizumab is a mainstay of treating metastatic disease."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "A dense fibrotic stroma walls off colorectal cancer: the tumor provokes desmoplastic scar tissue that shields it from immune cells and drugs, part of why microsatellite-stable disease resists immunotherapy."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reads colorectal cancer's grade in its glands: well-differentiated tumor cells keep orderly microvilli and tight junctions making lumina, while poorly differentiated ones lose this architecture — ultrastructure that tracks how aggressive the cancer is."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Colorectal cancer pushes platelets up: a paraneoplastic thrombocytosis appears in many patients and signals worse prognosis, while the platelets themselves help circulating tumor cells survive and seed the liver."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Late colorectal cancer can reach the bone: after seeding the liver and lungs, advanced disease occasionally spreads to the marrow-filled skeleton, an uncommon but ominous site marking widespread metastasis."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "FOLFOX chemotherapy bites the nerves: oxaliplatin, a backbone of colorectal cancer treatment, injures peripheral sensory neurons, causing a distinctive cold-triggered tingling and numbness that can force dose reductions and outlast therapy."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Targeted therapy wastes magnesium: the anti-EGFR antibodies cetuximab and panitumumab, used in RAS-wild-type colorectal cancer, block EGFR in the kidney tubule, so magnesium leaks into the urine and must be monitored and replaced."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "The skin reports on EGFR-blocking drugs: cetuximab and panitumumab provoke an acneiform facial rash, and its severity actually tracks with how well the colorectal tumor is responding, making the rash a visible biomarker."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies monitor and steer colorectal cancer: the CEA blood marker, read by immunoassay, tracks recurrence, while mismatch-repair (MMR) stains flag the MSI-high tumors that respond to checkpoint immunotherapy and prompt Lynch testing."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "The FOLFOX backbone empties the marrow: the oxaliplatin-and-fluorouracil chemotherapy is myelosuppressive, dropping neutrophil counts between cycles so that febrile neutropenia is a recurring hazard of colorectal-cancer treatment."
  - target: 03-medicine/03-food/dietary-fiber
    relation: connects-to
    note: "Fiber guards the colon: gut bacteria ferment dietary fiber into butyrate that nourishes colonocytes and curbs malignant change, so a fiber-rich diet lowers colorectal-cancer risk while red and processed meat raise it."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Colorectal cancer thickens the blood: tumor procoagulants, surgery, and chemotherapy combine to make deep-vein thrombosis and pulmonary embolism common, so clot prophylaxis is routine around treatment of this cancer."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "The 5-FU backbone can stun the heart: fluoropyrimidine chemotherapy (5-FU, capecitabine) provokes coronary vasospasm and direct cardiomyocyte injury, causing chest pain and even infarction that interrupts colorectal cancer treatment."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PIK3CA links the tumor to aspirin: mutations in this gene activate PI3K signaling in a subset of colorectal cancers, and the chemopreventive benefit of aspirin appears concentrated in these PIK3CA-mutant tumors."
---

# Colorectal Cancer

## Overview

**Colorectal cancer (CRC)** is the **third most common cancer** and **second leading cause of cancer-related death** worldwide, with approximately 1.9 million new diagnoses and 930,000 deaths globally in 2022 [^siegel-2024-crc-statistics]. In the United States, CRC is the second leading cause of cancer death among men and women combined, accounting for ~53,000 deaths in 2024. The lifetime risk is ~1 in 23 for men and 1 in 26 for women.

**CRC is highly preventable** — colonoscopy with polypectomy prevents cancer by removing adenomatous precursor lesions; population-based screening programs have led to ~25-30% declines in CRC mortality in countries with high screening uptake. Yet incidence is paradoxically rising in adults under 50 ("early-onset CRC"), a trend whose causes are under active investigation (altered gut microbiome, dietary changes, obesity).

**Hereditary CRC syndromes:**
- **Lynch syndrome (Hereditary Non-Polyposis CRC, HNPCC, ~3% of all CRC):** Autosomal dominant; germline mutations in mismatch repair (MMR) genes — MLH1, MSH2, MSH6, PMS2, EPCAM; 40-70% lifetime CRC risk; also endometrial (40-60%), ovarian, gastric, urinary tract cancers; Amsterdam II criteria / revised Bethesda guidelines for identification; universal MMR IHC/MSI testing of all CRC tumors recommended; Lynch CRCs: MSI-H (microsatellite instability-high) → high TMB → highly immunogenic → respond dramatically to pembrolizumab
- **Familial adenomatous polyposis (FAP, ~1% of CRC):** Germline APC mutations (typically truncating) → hundreds to thousands of colorectal polyps → near-obligate CRC by age 40 without colectomy; attenuated FAP (AFAP): APC mutations at 5' end → fewer polyps, later onset; MUTYH-associated polyposis (MAP): biallelic germline MUTYH mutations → attenuated polyposis
- **Serrated polyposis syndrome (SPS):** Multiple serrated polyps (sessile serrated lesions) → BRAF-mutant, CpG island methylation phenotype (CIMP) tumors; MSI-H via MLH1 promoter methylation (epigenetic — not hereditary)

**Molecular classification:**
- **Consensus Molecular Subtypes (CMS 1-4):**
  - **CMS1 (MSI immune, ~14%):** MSI-H, BRAF mutation, high TIL infiltration, immune activation; best prognosis after stage adjustment; pembrolizumab highly active
  - **CMS2 (canonical, ~37%):** Microsatellite stable (MSS), WNT/MYC activation, EGFR amplification; standard FOLFOX + anti-EGFR (RAS-wt)
  - **CMS3 (metabolic, ~13%):** KRAS/NRAS mutations, metabolic dysregulation, mixed phenotype; worse response to anti-EGFR
  - **CMS4 (mesenchymal, ~23%):** TGF-beta activation, stromal invasion, worst prognosis; resistance to most therapies; stromal/mesenchymal gene signature
  - ~13% mixed/intermediate → no single CMS assignment

## Structure

### Adenoma-carcinoma sequence (Fearon-Vogelstein model)

The step-wise genetic progression from normal epithelium to carcinoma in CRC was first systematically described by Fearon and Vogelstein (1990) and remains the paradigm for solid tumor progression:

**Stage 0 → Normal epithelium:**
- Normal crypt stem cells (ASCL2+, LGR5+ at crypt base); Wnt gradient (high at base → low at tip) → stem cell proliferation vs. differentiation

**Stage 1 → Early adenoma (polyp initiation):**
- **APC loss (first hit):** APC biallelic inactivation (mutation/deletion) → destruction complex (APC-AXIN-CK1-GSK3beta) collapses → beta-catenin accumulates → nuclear translocation → MYC, CCND1, AXIN2, LGR5 → crypt-like hyperproliferation → tubular adenoma formation; ~5-10 years for normal epithelium → small adenoma

**Stage 2 → Intermediate adenoma (early progression):**
- **KRAS activation (second hit, ~40%):** G12D/G12V/G12C mutations → RAS GTP-locked → RAF-MEK-ERK constitutive → proliferation amplification; adenoma grows from <1 cm → 1-2 cm; KRAS mutation found in ~40% of intermediate adenomas

**Stage 3 → Advanced adenoma (dysplasia):**
- **SMAD4/TGF-beta loss (~30%):** Biallelic SMAD4 (DPC4) loss → loss of TGF-beta growth inhibition → villous adenoma with high-grade dysplasia; also TGFBR2 mutations (especially in MSI-H tumors where repeat sequences in TGFBR2 are mutation hotspots)
- **PIK3CA mutations (~15%):** Activate PI3K-AKT → enhanced survival
- **Chromosome 18q loss (DCC, SMAD2, SMAD4):** Deleted in colorectal cancer (DCC) gene region; 18q LOH predicts poor prognosis

**Stage 4 → Invasive carcinoma:**
- **TP53 mutation/loss (~75%):** CIN (chromosomal instability) → 17p loss → TP53 mutation → loss of DNA damage checkpoint → rapid genomic instability → invasion through muscularis mucosae → T1 cancer; TP53 mutation is the rate-limiting step from adenoma to carcinoma
- **Additional alterations:** SMAD4 (metastatic phenotype), PI3K amplification, BRAF V600E (serrated pathway), MLH1 epigenetic silencing (MSI-H serrated carcinoma)

**Serrated pathway (alternative to adenoma-carcinoma):**
- Normal epithelium → hyperplastic polyp → sessile serrated lesion (SSL, formerly SSA/P) → SSL with dysplasia → CRC; BRAF V600E + CpG island methylator phenotype (CIMP) + MLH1 promoter methylation → MSI-H carcinoma; accounts for ~15-20% of sporadic CRC; biologically and therapeutically distinct from conventional adenoma pathway

## Function

### Clinical presentation

**Symptoms (variable by location):**
- **Right colon (cecum, ascending):** Occult blood loss → iron deficiency anemia (hypochromic microcytic anemia); mass palpable in right lower quadrant; often presents late due to paucity of obstructive symptoms (large lumen)
- **Left colon and sigmoid:** Pencil-thin stools, change in bowel habits, bright rectal bleeding; obstructive symptoms (left colon has smaller lumen and formed stool → higher obstruction risk)
- **Rectal cancer:** Rectal bleeding (bright red), tenesmus (incomplete evacuation feeling), urgency, mucus; distal rectal tumors may be palpable by digital exam
- **Metastatic:** Liver metastases → hepatomegaly, right upper quadrant pain, elevated LFTs; lung metastases → cough, hemoptysis; peritoneal carcinomatosis → ascites, abdominal distension; bone metastases (less common)

**Colorectal cancer screening:**
- **Colonoscopy:** 10-year interval if normal; removes polyps at time of detection; 90-95% sensitive for adenomas >10 mm; gold standard
- **FIT (fecal immunochemical test, fecal occult blood):** Annual stool test; detects hemoglobin in stool → low-cost, high-compliance; used as primary screen in many European and Asian national programs; positive FIT → colonoscopy
- **CT colonography (virtual colonoscopy):** 5-year interval; comparable sensitivity to optical colonoscopy for polyps >6 mm; cannot do polypectomy → requires colonoscopy for positive findings
- **Multi-target stool DNA test (Cologuard):** Detects abnormal DNA (KRAS mutations, NDRG4/BMP3 methylation, hemoglobin) → 3-year interval; higher false-positive rate than FIT; used in average-risk patients
- Starting age: USPSTF recommends starting at 45 (previously 50) given rising early-onset CRC incidence

## Pathology

### Staging and prognosis

**TNM staging (AJCC 8th):**
- **Stage I:** T1-2 N0 M0 (tumor in mucosa/submucosa or muscularis propria, no nodes); 5-year OS >90%
- **Stage II:** T3-4 N0 M0 (through muscularis propria or into adjacent structures, no nodes); 5-year OS 70-85%; adjuvant chemotherapy benefit limited to high-risk features (T4, perforation, <12 lymph nodes examined, MSS)
- **Stage III:** Any T N1-2 M0 (1+ positive nodes); 5-year OS 40-70%; adjuvant FOLFOX × 3-6 months standard
- **Stage IV:** Any T, N, M1 (distant metastasis); 5-year OS ~15-25% for selected patients with resectable liver-only metastases; generally incurable but median OS improved from ~12 months (1990s) to ~30+ months with modern treatment

### Treatment [^van-cutsem-2011-crystal-cetuximab] [^kopetz-2019-beacon-crc]

**Curative intent (stages I-III + selected stage IV):**
- **Surgery:** Colectomy with adequate margins and regional lymph node dissection (minimum 12 nodes); laparoscopic approaches standard for colon; rectal cancer: total mesorectal excision (TME) — sharp dissection in areolar tissue plane → low local recurrence rates (<10%); robotic-assisted TME increasingly used
- **Adjuvant chemotherapy stage III:** FOLFOX (oxaliplatin + leucovorin + 5-FU) or CAPOX × 3-6 months; reduces recurrence risk ~25%; oxaliplatin adds benefit vs. 5-FU alone; adjuvant oxaliplatin not beneficial in stage II MSS or MSI-H tumors
- **Neoadjuvant rectal cancer:** Locally advanced rectal cancer (T3-4 or N+): long-course chemoradiation (5-FU + 45 Gy) OR short-course RT (5×5 Gy) followed by total neoadjuvant therapy (TNT: induction chemotherapy + CRT) → RAPIDO, PRODIGE-23 trials show higher pCR with TNT; "watch and wait" after clinical complete response increasingly considered for distal rectal cancer (non-operative management in ~25-30% of cCR patients)
- **Hepatic metastasectomy:** For resectable liver-only metastases; 5-year OS 30-50%; conversion chemotherapy (FOLFOX/FOLFIRI + bevacizumab or anti-EGFR) → downstage to resectability; repeat hepatectomy for recurrence

**Metastatic CRC (mCRC) — systemic therapy:**

*Backbone chemotherapy regimens:*
- **FOLFOX:** Oxaliplatin + leucovorin + 5-FU bolus + infusion (biweekly); first-line or adjuvant
- **FOLFIRI:** Irinotecan + leucovorin + 5-FU; equivalent first-line efficacy to FOLFOX; used second-line after FOLFOX failure
- **FOLFOXIRI:** Triple combination → higher ORR (66% in TRIBE trial) → for conversion chemotherapy for initially unresectable liver metastases

*Targeted therapies by biomarker:*

**RAS-wild-type (KRAS/NRAS codons 12/13/59/61/117/146 WT):**
- **Anti-EGFR:** Cetuximab (Erbitux) or panitumumab (Vectibix) + FOLFIRI → first-line; CRYSTAL trial: KRAS-wt patients, cetuximab + FOLFIRI: PFS 9.9 vs. 8.4 months vs. FOLFIRI alone; FIRE-3 head-to-head (cetuximab vs. bevacizumab with FOLFIRI): OS favored cetuximab in KRAS-wt (34.3 vs. 25.0 months) [^van-cutsem-2011-crystal-cetuximab]
- **Bevacizumab (anti-VEGFA):** Active in all mCRC regardless of RAS status; IFL: bevacizumab + IFL → PFS 10.6 vs. 6.2 months; OS 20.3 vs. 15.6 months; bevacizumab preferred in right-sided or BRAF-mutant mCRC (where EGFR inhibitors are ineffective)
- **Left vs. right primary site:** Left-sided (descending colon, sigmoid, rectum) RAS-wt mCRC → strongly prefer anti-EGFR first-line (OS ~33-36 months); right-sided (cecum, ascending, transverse) RAS-wt → anti-EGFR less effective (OS ~17-19 months); right-sided mCRC tends to be BRAF-mutant or MSI-H more often

**BRAF V600E-mutant mCRC:**
- **BEACON CRC:** Encorafenib (BRAF inhibitor) + cetuximab (anti-EGFR) → OS 9.3 vs. 5.9 months vs. control; also encorafenib + cetuximab + binimetinib (MEK inhibitor) triplet FDA approved; unlike melanoma BRAF-mutant, single-agent BRAF inhibition is ineffective in CRC due to EGFR-driven feedback reactivation [^kopetz-2019-beacon-crc]

**KRAS G12C-mutant mCRC:**
- **Adagrasib + cetuximab (KRYSTAL-10):** ORR 34%, PFS 6.9 months → FDA approved 2024; sotorasib + panitumumab (CodeBreaK 300): ORR 26% — both approved; KRAS G12C CRC accounts for ~3-4% of mCRC

**MSI-H/dMMR mCRC (~5% of mCRC):**
- **Pembrolizumab first-line (KEYNOTE-177):** PFS 16.5 vs. 8.2 months vs. chemotherapy; OS 77.8 vs. 36.7 months at 5 years — practice-changing; pembrolizumab now first-line for MSI-H mCRC (regardless of PD-L1)
- **Nivolumab + ipilimumab (CheckMate-142):** 58% ORR in MSI-H mCRC; approved second-line

**HER2 amplification/overexpression (~3-5% of RAS/RAF-wt mCRC):**
- Tucatinib + trastuzumab (MOUNTAINEER): ORR 38%, FDA approved 2023; pertuzumab + trastuzumab (MyPathway): ORR 38%

**Later-line therapies:**
- **Trifluridine + tipiracil (Lonsurf):** 5-FU prodrug combination; RECOURSE trial: OS 7.1 vs. 5.3 months vs. placebo; oral; approved 3L+
- **Regorafenib (Stivarga):** Multi-kinase inhibitor (VEGFR1-3, PDGFR, FGFR1, KIT, RET); CORRECT trial: OS 6.4 vs. 5.0 months; 3L+; tolerability challenging (hand-foot syndrome, liver toxicity)
- **Fruquintinib (Fruzaqla):** VEGFR1-3 inhibitor; FRESCO-2 trial: OS 7.4 vs. 4.8 months; approved 3L+ 2023

## Connections

- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — KRAS mutations (~40% of CRC) are acquired in the adenoma-carcinoma sequence; KRAS G12V/G12D-mutant CRC is resistant to EGFR inhibitors; KRAS G12C-mutant CRC → adagrasib + cetuximab (KRYSTAL-10, ORR 34%) — first targeted therapy for KRAS-mutant CRC.
- `connects-to` → **[Wnt/beta-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — APC loss is the founding mutation in >80% of sporadic CRC → destruction complex collapse → beta-catenin nuclear accumulation → MYC, cyclin D1 → hyperproliferation; germline APC mutation causes FAP → obligate CRC without colectomy.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — EGFR is overexpressed in >80% of CRC; cetuximab and panitumumab improve OS in RAS-wild-type mCRC (CRYSTAL: cetuximab + FOLFIRI, PFS 9.9 vs. 8.4 months); RAS/RAF-wild-type status required for EGFR inhibitor benefit; left-sided primary strongly predicts EGFR inhibitor response.
- `connects-to` → **[BRAF](../../03-molecular/braf/README.md)** — BRAF V600E mutations (~8-10% of CRC) confer poor prognosis and EGFR inhibitor resistance; BEACON CRC: encorafenib + cetuximab → OS 9.3 vs. 5.9 months in BRAF V600E mCRC; single-agent BRAF inhibition is ineffective in CRC due to EGFR-driven feedback reactivation.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — FN-integrin α5β1/αvβ3 signaling drives EMT in CRC → vimentin, N-cadherin, MMP production → invasion and liver metastasis; EDB-FN is overexpressed in CRC stroma; tumor FN correlates with lymph node metastasis and worse prognosis in stage II-III CRC.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Most colorectal cancers arise in the large intestine via the adenoma-carcinoma sequence, so colonoscopy with polypectomy is preventive; right-sided tumors bleed occultly (→ anemia) while left-sided ones obstruct, and rectal cancer is resected by total mesorectal excision.
- `connects-to` → **[Lynch Syndrome](../lynch-syndrome/README.md)** — Lynch syndrome (germline MMR loss) causes ~3% of colorectal cancer, producing dMMR/MSI-H tumors that are hypermutated and exquisitely sensitive to PD-1 blockade — pembrolizumab is now first-line for MSI-H metastatic CRC; universal MMR/MSI testing of all CRC is recommended.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 loss (~75% of CRC) is the rate-limiting step that converts an advanced adenoma into invasive carcinoma: 17p loss plus TP53 mutation removes the DNA-damage checkpoint, unleashing the chromosomal instability that lets cells breach the muscularis mucosae.
- `connects-to` → **[Prostate Cancer](../prostate-cancer/README.md)** — Colorectal and prostate cancers are two of the commonest adult solid tumours; both have hereditary drivers—Lynch raises both, BRCA2 raises prostate—and microsatellite-unstable CRC and DNA-repair-deficient prostate cancer both respond to checkpoint or PARP-based therapy.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver is the dominant site of colorectal metastasis via portal venous drainage: ~50% of CRC patients develop liver mets, and resection or ablation of oligometastatic liver disease can be curative; this portal route makes CRC liver-metastasis management central to oncology.
- `connects-to` → **[Familial Adenomatous Polyposis](../fap/README.md)** — Familial adenomatous polyposis, from germline APC mutation, carpets the colon with hundreds-to-thousands of adenomas and guarantees colorectal cancer by mid-adulthood without prophylactic colectomy; APC loss is also the founding event in >80% of sporadic CRC.
- `connects-to` → **[MUTYH-Associated Polyposis](../mutyh-associated-polyposis/README.md)** — MUTYH-associated polyposis is a recessive hereditary cause of colorectal cancer: biallelic MUTYH loss fails to repair oxidative DNA damage, producing G:C→T:A mutations and multiple adenomas, so a FAP-like polyposis with negative APC testing prompts MUTYH analysis.
- `connects-to` → **[Inflammatory Bowel Disease](../inflammatory-bowel-disease/README.md)** — Long-standing inflammatory bowel disease drives colitis-associated colorectal cancer: chronic inflammation accelerates the dysplasia-carcinoma sequence (often p53 early, APC late—reversed from sporadic CRC), so colitis warrants surveillance colonoscopy.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — The MSI-high subset of colorectal cancer is exquisitely immunotherapy-responsive: mismatch-repair deficiency generates abundant neoantigens that draw cytotoxic CD8+ T cells, so anti-PD-1 (pembrolizumab) works in MSI-high tumors while microsatellite-stable CRC remains resistant.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — The gut microbiome shapes colorectal cancer risk: dysbiosis enriches pro-carcinogenic bacteria (e.g. Fusobacterium) that inflame mucosa and damage DNA, while a healthy fiber-fermenting flora is protective—linking the microbial ecosystem to tumorigenesis.
- `connects-to` → **[Obesity](../obesity/README.md)** — Obesity is a major modifiable colorectal cancer risk factor: visceral adiposity drives insulin/IGF-1 signaling and chronic inflammation that promote colonic tumorigenesis, so rising early-onset CRC parallels obesity—weight and diet are key prevention levers.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Radiotherapy is central to rectal (not colon) cancer: neoadjuvant chemoradiation with photon beams shrinks locally advanced rectal tumors before surgery, sometimes enough for watch-and-wait—colon cancer, by contrast, is treated with surgery and chemotherapy.
- `connects-to` → **[APC](../../03-molecular/apc/README.md)** — APC loss is the gatekeeper mutation that starts colorectal cancer: inactivating APC unleashes Wnt/beta-catenin to form the first adenoma, so it initiates the adenoma-carcinoma sequence—mutated in FAP and in most sporadic colorectal cancers.
- `targets` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — Colorectal cancer arises stepwise from the intestinal epithelium: normal crypt cells acquire APC, then KRAS, then p53 hits, progressing through adenoma to carcinoma—the textbook adenoma-carcinoma sequence that makes screening colonoscopy preventive.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — PD-1 is the checkpoint that MSI-high colorectal tumors exploit to evade attack: blocking it produced the first tissue-agnostic FDA approval (pembrolizumab for any MSI-high cancer), so dMMR/MSI status is now tested at diagnosis to guide immunotherapy.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Type 2 diabetes raises colorectal cancer risk: high insulin and IGF-1 from insulin resistance promote colonocyte proliferation, and shared risks like obesity and inactivity compound it—so metabolic health is part of colorectal cancer prevention.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — After the liver, the lung is colorectal cancer's next metastatic stop: tumor cells reach it via the systemic circulation, and isolated lung metastases are sometimes surgically resected for cure—so chest imaging is routine in staging and follow-up.
- `connects-to` → **[HER2](../../03-molecular/her2/README.md)** — A subset of colorectal cancers are HER2-amplified: like in breast and gastric cancer, this drives growth and predicts resistance to anti-EGFR drugs, but responds to HER2-targeted combinations—so HER2 testing now guides therapy in metastatic disease.
- `connects-to` → **[Iron Deficiency Anemia](../iron-deficiency-anemia/README.md)** — Right-sided colorectal cancer often presents as iron-deficiency anemia: a slow-bleeding tumor depletes iron long before obstruction, so unexplained iron-deficiency anemia in an adult mandates colonoscopy to exclude colon cancer.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D and calcium intake are linked to colorectal risk: higher levels associate with lower incidence, and vitamin D's effects on colonocyte growth make it a studied (if unproven) chemopreventive alongside fiber and aspirin.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Cancer-associated fibroblasts drive colorectal progression: they remodel the tumor stroma, supply growth and survival signals, and promote chemoresistance and metastasis—a major reason the desmoplastic, fibroblast-rich CMS4 subtype carries a worse prognosis.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Colorectal cancer is treated by starving its vessels of VEGF: the tumor secretes VEGF to build a blood supply, so anti-VEGF bevacizumab is a mainstay added to chemotherapy in metastatic colorectal cancer.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — Colorectal cancer turns aggressive when it loses SMAD4: this late hit in the adenoma-carcinoma sequence disables TGF-β's growth restraint, driving invasion and metastasis and predicting a worse prognosis and poorer chemo response.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Most colorectal cancers are immune-cold, walled off by regulatory T cells: unlike MSI-high tumors, microsatellite-stable CRC has few neoantigens and Treg-rich stroma, which is why checkpoint immunotherapy works in only a minority.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Dietary calcium helps guard against colorectal cancer: it binds bile acids and fatty acids in the gut and signals colon cells to differentiate, so adequate calcium is one of the better-supported dietary protections against the disease.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Tumor-associated macrophages shape colorectal cancer: depending on their polarization they can promote or restrain the tumor, and a macrophage-rich, suppressive stroma helps the common microsatellite-stable cancers evade immunity.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Colorectal cancer can reach the brain late: though it spreads first to liver and lung, advanced disease occasionally seeds brain metastases, a sign of widespread disease that shifts care toward palliative and systemic treatment.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron deficiency is often the first clue to colorectal cancer: right-sided tumors bleed slowly into the stool, so unexplained iron-deficiency anemia in an older adult is a red flag that should prompt a colonoscopy.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Colorectal tumors build their own blood supply: VEGF recruits endothelial cells to sprout new vessels, and blocking this with bevacizumab is a mainstay of treating metastatic disease.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — A dense fibrotic stroma walls off colorectal cancer: the tumor provokes desmoplastic scar tissue that shields it from immune cells and drugs, part of why microsatellite-stable disease resists immunotherapy.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reads colorectal cancer's grade in its glands: well-differentiated tumor cells keep orderly microvilli and tight junctions making lumina, while poorly differentiated ones lose this architecture — ultrastructure that tracks how aggressive the cancer is.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Colorectal cancer pushes platelets up: a paraneoplastic thrombocytosis appears in many patients and signals worse prognosis, while the platelets themselves help circulating tumor cells survive and seed the liver.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Late colorectal cancer can reach the bone: after seeding the liver and lungs, advanced disease occasionally spreads to the marrow-filled skeleton, an uncommon but ominous site marking widespread metastasis.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — FOLFOX chemotherapy bites the nerves: oxaliplatin, a backbone of colorectal cancer treatment, injures peripheral sensory neurons, causing a distinctive cold-triggered tingling and numbness that can force dose reductions and outlast therapy.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Targeted therapy wastes magnesium: the anti-EGFR antibodies cetuximab and panitumumab, used in RAS-wild-type colorectal cancer, block EGFR in the kidney tubule, so magnesium leaks into the urine and must be monitored and replaced.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — The skin reports on EGFR-blocking drugs: cetuximab and panitumumab provoke an acneiform facial rash, and its severity actually tracks with how well the colorectal tumor is responding, making the rash a visible biomarker.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies monitor and steer colorectal cancer: the CEA blood marker, read by immunoassay, tracks recurrence, while mismatch-repair (MMR) stains flag the MSI-high tumors that respond to checkpoint immunotherapy and prompt Lynch testing.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — The FOLFOX backbone empties the marrow: the oxaliplatin-and-fluorouracil chemotherapy is myelosuppressive, dropping neutrophil counts between cycles so that febrile neutropenia is a recurring hazard of colorectal-cancer treatment.
- `connects-to` → **[Dietary Fiber](../../../03-medicine/03-food/dietary-fiber/README.md)** — Fiber guards the colon: gut bacteria ferment dietary fiber into butyrate that nourishes colonocytes and curbs malignant change, so a fiber-rich diet lowers colorectal-cancer risk while red and processed meat raise it.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Colorectal cancer thickens the blood: tumor procoagulants, surgery, and chemotherapy combine to make deep-vein thrombosis and pulmonary embolism common, so clot prophylaxis is routine around treatment of this cancer.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — The 5-FU backbone can stun the heart: fluoropyrimidine chemotherapy (5-FU, capecitabine) provokes coronary vasospasm and direct cardiomyocyte injury, causing chest pain and even infarction that interrupts colorectal cancer treatment.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PIK3CA links the tumor to aspirin: mutations in this gene activate PI3K signaling in a subset of colorectal cancers, and the chemopreventive benefit of aspirin appears concentrated in these PIK3CA-mutant tumors.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^siegel-2024-crc-statistics]: Siegel RL, Giaquinto AN, Jemal A. Cancer statistics, 2024. *CA Cancer J Clin.* 2024;74(1):12-49. [doi:10.3322/caac.21820](https://doi.org/10.3322/caac.21820) · [PubMed 38230766](https://pubmed.ncbi.nlm.nih.gov/38230766/)
[^van-cutsem-2011-crystal-cetuximab]: Van Cutsem E, Köhne CH, Láng I, et al. Cetuximab plus irinotecan, fluorouracil, and leucovorin as first-line treatment for metastatic colorectal cancer: updated analysis according to tumor KRAS and BRAF mutation status. *J Clin Oncol.* 2011;29(15):2011-2019. [doi:10.1200/JCO.2010.33.5091](https://doi.org/10.1200/JCO.2010.33.5091) · [PubMed 21502544](https://pubmed.ncbi.nlm.nih.gov/21502544/)
[^kopetz-2019-beacon-crc]: Kopetz S, Grothey A, Yaeger R, et al. Encorafenib, binimetinib, and cetuximab in BRAF V600E-mutated colorectal cancer. *N Engl J Med.* 2019;381(17):1632-1643. [doi:10.1056/NEJMoa1908075](https://doi.org/10.1056/NEJMoa1908075) · [PubMed 31566309](https://pubmed.ncbi.nlm.nih.gov/31566309/)
