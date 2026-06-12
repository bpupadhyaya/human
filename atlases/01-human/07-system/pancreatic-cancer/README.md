---
schema: human-scale-entry/v1
id: pancreatic-cancer
name: Pancreatic Cancer
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Aggressive exocrine malignancy; KRAS mutations in >90%, TP53 in ~75%, CDKN2A and SMAD4 in ~50%; desmoplastic stroma limits drug delivery. FOLFIRINOX and gemcitabine+nab-paclitaxel are standards; KRAS inhibitors (sotorasib for G12C) and BRCA-mutant PARP inhibitors are active."
aliases: ["PDAC", "pancreatic ductal adenocarcinoma", "pancreatic adenocarcinoma", "exocrine pancreatic cancer", "metastatic PDAC", "borderline resectable pancreatic cancer"]
sources:
  - id: conroy-2011-folfirinox
    type: peer-reviewed
    cite: "Conroy T, Desseigne F, Ychou M, et al. FOLFIRINOX versus gemcitabine for metastatic pancreatic cancer. N Engl J Med. 2011;364(19):1817-1825."
    doi: "10.1056/NEJMoa1011923"
    pmid: "21561347"
    url: "https://doi.org/10.1056/NEJMoa1011923"
  - id: golan-2019-polo
    type: peer-reviewed
    cite: "Golan T, Hammel P, Reni M, et al. Maintenance olaparib for germline BRCA-mutated metastatic pancreatic cancer. N Engl J Med. 2019;381(4):317-327."
    doi: "10.1056/NEJMoa1903387"
    pmid: "31157963"
    url: "https://doi.org/10.1056/NEJMoa1903387"
  - id: von-hoff-2013-abraxane
    type: peer-reviewed
    cite: "Von Hoff DD, Ervin T, Arena FP, et al. Increased survival in pancreatic cancer with nab-paclitaxel plus gemcitabine. N Engl J Med. 2013;369(18):1691-1703."
    doi: "10.1056/NEJMoa1304369"
    pmid: "24131140"
    url: "https://doi.org/10.1056/NEJMoa1304369"
cross_links:
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "KRAS is mutated in >90% of PDAC (G12D ~40%, G12V ~33%, G12R ~16%); constitutive RAS → RAF-MEK-ERK drives proliferation and survival; KRAS G12C inhibitors show modest activity in the rare G12C subset; pan-KRAS and KRAS G12D inhibitors are under active clinical development."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-beta drives pancreatic desmoplasia via stellate cell activation → dense stroma limits chemo delivery; SMAD4 loss (~50% of PDAC) → TGF-beta loses tumor suppression; TGF-beta becomes pro-invasive and immunosuppressive in SMAD4-null PDAC; anti-TGF-beta combinations under study."
  - target: 01-human/03-molecular/brca1
    relation: connects-to
    note: "BRCA1/2 germline mutations occur in ~5-10% of PDAC; olaparib maintenance (POLO trial) improved PFS in BRCA-mutant platinum-responsive mPDAC (7.4 vs. 3.8 months); somatic BRCA mutations in ~3%; homologous recombination deficiency testing guides PARP inhibitor selection."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "EGFR is overexpressed in ~60% of PDAC; erlotinib + gemcitabine modestly improves OS vs. gemcitabine alone (NCIC PA.3: OS 6.24 vs. 5.91 months; HR 0.82) — the only approved targeted therapy before KRAS inhibitors; anti-EGFR antibodies (cetuximab) are ineffective in PDAC."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "CDKN2A (p16/INK4a) deleted/silenced in ~95% of PDAC; second earliest driver after KRAS; p16 loss → CDK4/6-RB hyperphosphorylation → unrestricted S-phase entry; ARF co-deletion → MDM2 unchecked → p53 suppressed; CDK4/6 inhibitors (palbociclib) evaluated in p16-null PDAC."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 mutations in ~70-75% of PDAC; p53 LOF → G2/M checkpoint failure and apoptosis evasion; late PanIN-3→PDAC transition event (vs KRAS = early); gain-of-function mutants (R175H, R248W) promote invasion; APR-246 (mutant p53 reactivator) in early PDAC trials."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "SMAD4 (DPC4) loss in ~55% of PDAC switches TGF-β from tumor suppressor to pro-invasive driver; SMAD4 loss predicts systemic metastasis vs local recurrence in SMAD4-intact; TGF-β → non-SMAD (RAS-ERK, PI3K) → EMT; SMAD4 IHC predicts spread in resected PDAC."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "Pancreatic ductal adenocarcinoma arises from the pancreas's exocrine ductal epithelium, growing silently until it obstructs the bile duct (painless jaundice) or invades vessels; deep location and early spread mean only ~20% are resectable, survival near 12% at 5 years."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Pancreatic cancer is defined by its stroma: KRAS-driven tumor cells activate stellate cells into cancer-associated fibroblasts that build a dense, hypovascular desmoplastic matrix starving the tumor of drugs and excluding T cells — why PDAC resists chemo and immunotherapy."
  - target: 01-human/07-system/hereditary-pancreatitis
    relation: connects-to
    note: "Hereditary pancreatitis (germline PRSS1, SPINK1) is a major pancreatic cancer risk: decades of recurring autodigestion and inflammation create a field of injury that, with smoking, drives a ~40-50× lifetime risk of pancreatic adenocarcinoma — among the highest predispositions."
---

# Pancreatic Cancer

## Overview

**Pancreatic ductal adenocarcinoma (PDAC)** is the most common and deadly form of pancreatic cancer, arising from ductal epithelial cells of the exocrine pancreas. Despite accounting for only ~3% of new cancer diagnoses in the United States (~65,000 cases/year), PDAC is the **third leading cause of cancer death** (~50,000 deaths/year; 5-year OS ~13%) due to late-stage diagnosis, rapid disease progression, and deep intrinsic resistance to most cytotoxic agents and immunotherapy. Median OS in metastatic PDAC was <6 months before 2011; modern combination chemotherapy (FOLFIRINOX) improved median OS to ~11 months in fit patients [^conroy-2011-folfirinox].

**Incidence, risk, and epidemiology:**
- **Age:** Median diagnosis age ~70; rare before 45; increasing incidence in younger adults correlating with obesity and T2DM
- **Risk factors:** Smoking (2-3× RR; 25% of PDAC attributable to tobacco), obesity (BMI >35: 1.5× RR), chronic pancreatitis (10-15× lifetime risk), new-onset diabetes (possible early PDAC marker — DM developing in elderly patients without risk factors), heavy alcohol use
- **Hereditary risk (~10-15% of PDAC):**
  - *BRCA2* mutation (3-10× RR; ~5-8% of PDAC), BRCA1 (~2-3× RR)
  - *PALB2* mutation (~3× RR)
  - *ATM* mutation (~3× RR)
  - *CDKN2A* mutation (Familial atypical multiple mole melanoma; FAMMM syndrome — lifetime PCa risk ~17%)
  - *PRSS1* (hereditary pancreatitis) → ~40% lifetime PDAC risk
  - *STK11* (Peutz-Jeghers syndrome) → ~35% lifetime PDAC risk
  - *MLH1/MSH2/MSH6* (Lynch syndrome) → modest PDAC risk increase
  - Familial pancreatic cancer (FPC): ≥2 first-degree relatives → 4-6× RR; genetic basis not always identified
- **Germline testing:** Recommended for all patients with PDAC regardless of family history (NCCN guidelines) — identifies therapy implications (PARP inhibitors, platinum sensitivity) and enables family counseling

**PDAC vs. other pancreatic malignancies:**
- **PDAC (~85%):** The dominant lethal form; duct cells → mucin-producing adenocarcinoma
- **Neuroendocrine tumors (PanNETs, ~10%):** Often indolent; surgery curative for localized; everolimus and sunitinib for advanced; often functional (insulinoma, glucagonoma, VIPoma); well-differentiated (Grade 1-2) vs. poorly differentiated (Grade 3/NEPC); KRAS-wildtype; good prognosis in low-grade disease
- **Acinar cell carcinoma (~1%):** Lipase-secreting; BRCA2 mutations common; responds to platinum; better prognosis than PDAC
- **Intraductal papillary mucinous neoplasm (IPMN):** Precursor lesion → variable malignant potential; main duct IPMN has high (~50-70%) malignant potential → resection; branch duct IPMN followed by MRI unless features of high risk (solid component, main duct involvement)

## Structure

### Pancreatic anatomy and ductal architecture

**Anatomical regions:**
- **Head (right):** ~70% of PDAC; surrounds the common bile duct (CBD) and ampulla of Vater → early biliary obstruction → jaundice is often the presenting symptom; relationship to superior mesenteric artery (SMA), SMV/portal vein determines resectability
- **Body (center):** ~20% of PDAC; lies anterior to the aorta and posterior gastric surface; wraps superior mesenteric vessels; most vascular involvement is here
- **Tail (left):** ~10% of PDAC; extends to the hilum of the spleen; often silent until large — presents at later stage; most common site for PanNETs; distal pancreatectomy + splenectomy for resectable tail tumors

**Ductal anatomy:**
- Main pancreatic duct (duct of Wirsung): Runs length of pancreas → joins CBD at ampulla of Vater → major duodenal papilla; obstruction by pancreatic head tumors → upstream duct dilatation ("double duct sign" on CT/ERCP)
- Accessory duct (Santorini): Drains into minor papilla; anatomical variant (~30% of people)

**PDAC precursor lesions:**
- **Pancreatic intraepithelial neoplasia (PanIN):** Most common precursor; 3 grades (PanIN-1A, 1B, 2, 3 = carcinoma in situ); PanIN-1: KRAS mutation (earliest event); PanIN-2: CDKN2A loss; PanIN-3: TP53 and SMAD4 loss; progression takes ~20 years but is largely asymptomatic
- **IPMN:** Gross precursor (visible on imaging); main duct > branch duct risk; mucin-producing; KRAS, GNAS (camp/RAS signaling), SMAD4 mutations
- **Mucinous cystic neoplasm (MCN):** Exclusively in women (ovarian stroma); main duct not involved; resection recommended

**Molecular pathogenesis — genetic progression model:**
1. Normal ductal epithelium → KRAS mutation (PanIN-1): ~100% of PDAC carry KRAS mutation; earliest driver
2. CDKN2A (p16/INK4a) loss → PanIN-2: ~90% of PDAC; loss allows CDK4/6-driven cell cycle progression
3. TP53 mutation → PanIN-3: ~75% of PDAC; loss of G2/M checkpoint and apoptosis regulation
4. SMAD4 (DPC4) loss → metastasis: ~50% of PDAC; SMAD4 loss → TGF-beta switches from suppressor to promoter of invasion and immune exclusion

## Function

### Clinical presentation and diagnosis

**Symptoms (highly varied by location):**
- **Head PDAC:** Painless obstructive jaundice (bilirubin elevation → scleral icterus → dark urine, pale stools), weight loss, anorexia, pruritus (bile salt deposition); Courvoisier sign: palpable non-tender gallbladder + jaundice (suggests malignant obstruction rather than stone)
- **Body/tail PDAC:** Vague epigastric/back pain (celiac plexus invasion), weight loss, new-onset diabetes, migratory thrombophlebitis (Trousseau syndrome — hypercoagulability via tumor TF and mucin)
- **General:** Weight loss (often profound, >10% body weight), fatigue, depression (can precede diagnosis — depression as paraneoplastic); venous thromboembolic events (DVT, PE) — 15% of PDAC have VTE at or before diagnosis

**Biomarkers:**
- **CA 19-9:** Sialylated Lewis antigen; elevated in ~80% of PDAC; sensitivity ~79%, specificity ~82% for pancreatic cancer vs. benign conditions; normal in ~5-10% due to Lewis antigen negativity (Se antigen genotype → no CA 19-9 production regardless of PDAC); useful for monitoring response and detecting recurrence, not for screening
- **CEA:** Elevated in ~50% of PDAC; less specific than CA 19-9; combined CA 19-9 + CEA monitoring improves sensitivity

**Imaging:**
- **CT (triple phase pancreas protocol):** Defines tumor location, ductal/vascular involvement, liver metastases, peritoneal disease; thin-slice axial + MPR reconstructions; arteries (SMA, celiac, hepatic) and veins (SMV, portal vein) evaluated for contact, abutment, or encasement — determines resectability classification
- **MRI/MRCP:** Superior soft tissue contrast; useful for IPMN characterization, liver characterization, and perineural invasion detection
- **Endoscopic ultrasound (EUS):** Gold standard for diagnosis — fine needle aspiration (FNA) or biopsy (FNB/core); highest sensitivity for small pancreatic masses (<2 cm); provides tissue for pathology, molecular profiling, and KRAS G12D NGS
- **PET-CT:** Not standard for initial staging; useful for detecting occult metastases before surgery in high-risk cases; FDG-avid PDAC confirmed metastasis → changes surgery plan

**Resectability criteria (NCCN/AHPBA):**
- **Resectable:** No arterial (SMA, celiac, CHA) contact; ≤180° SMV/portal vein contact; no distant metastases
- **Borderline resectable (BRPC):** 180°-360° SMV/PV contact (reconstructable), ≤180° SMA contact, short CHA contact; requires preoperative chemotherapy → restaging → surgery if response
- **Locally advanced (LAPC):** >360° SMA or celiac involvement; SMA or celiac encasement; aorta involvement; typically unresectable; aggressive chemotherapy (FOLFIRINOX) → conversion resection in ~10-15%
- **Metastatic:** Liver, peritoneal, lung metastases; chemotherapy and supportive care only

## Pathology

### Diagnosis and molecular profiling

**Histopathology:** PDAC — duct-like glands surrounded by dense desmoplastic stroma (~90% stroma by volume in some tumors); perineural invasion, lymphovascular invasion, regional node involvement are common; R0 vs. R1 (positive margin) resection is the most important surgical quality metric

**Molecular profiling at diagnosis:**
- **KRAS genotyping:** Critical for KRAS-targeted therapy eligibility; G12C (~2-3% of PDAC) → sotorasib or adagrasib eligible; G12D (~40%) → MRTX1133, RMC-9805 under investigation
- **HRR (homologous recombination repair) genes:** BRCA1/2, PALB2, ATM, BRIP1, RAD51C/D — germline and somatic testing; HRR-deficient PDAC → platinum sensitivity + PARP inhibitor maintenance [^golan-2019-polo]
- **MSI/MMR:** Rare in PDAC (<2%); pembrolizumab eligible if MSI-H
- **NTRK fusions:** Rare (<1%); larotrectinib or entrectinib eligible
- **TMB-high:** Pembrolizumab (tissue-agnostic)

### Treatment

**Resectable PDAC:**
- **Surgery:** Pancreaticoduodenectomy (Whipple procedure) for head tumors; distal pancreatectomy + splenectomy for body/tail; total pancreatectomy (rare); robotic-assisted increasingly common; lymph node harvest ≥15 nodes required for adequate staging; mortality <3% at high-volume centers
- **Adjuvant chemotherapy (CONKO-001, ESPAC-4, PRODIGE 24/CCTG):**
  - Modified FOLFIRINOX (mFOLFIRINOX) × 24 weeks: DFS 21.4 vs. 12.8 months; OS 54.4 vs. 35.0 months (PRODIGE 24; preferred for fit patients)
  - Gemcitabine + capecitabine (GemCap; ESPAC-4): OS 28.0 vs. 25.5 months vs. gemcitabine alone
  - Gemcitabine alone: Historical standard (CONKO-001); now largely superseded

**Borderline resectable/locally advanced — neoadjuvant:**
- mFOLFIRINOX × 4-6 months → restaging CT → surgery if resectability criteria met; landmark Alliance A021101: feasibility established; LAP07 trial (chemo vs. CRT for LAPC): no OS difference; stereotactic body radiotherapy (SBRT) or MR-linac adaptive RT as consolidation for LAPC (SCALOP, CONKO-007)

**Metastatic PDAC:**
- **FOLFIRINOX (FFX):** Oxaliplatin + irinotecan + leucovorin + fluorouracil; first-line for ECOG PS 0-1, adequate biliary drainage, no neuropathy; OS 11.1 vs. 6.8 months vs. gemcitabine (PRODIGE 4/ACCORD 11); ORR 31.6%; diarrhea, fatigue, neutropenia, neuropathy are key toxicities [^conroy-2011-folfirinox]
- **Gemcitabine + nab-paclitaxel (gem-nabP):** First-line for ECOG PS 0-2; OS 8.5 vs. 6.7 months vs. gemcitabine alone; ORR 23% (MPACT trial); neurotoxicity and myelosuppression; preferred in PS 2 or comorbidity that precludes FFX [^von-hoff-2013-abraxane]
- **Olaparib maintenance (POLO trial):** For germline BRCA1/2-mutant mPDAC not progressed on ≥16 weeks platinum-based chemotherapy; PFS 7.4 vs. 3.8 months (HR 0.53); no OS benefit (may reflect crossover); FDA-approved December 2019 [^golan-2019-polo]
- **KRAS G12C-directed therapy:** Sotorasib and adagrasib have modest activity as monotherapy (ORR ~20%) in KRAS G12C-mutant PDAC; G12C represents only ~2-3% of PDAC; combinations with SHP2 inhibitors, MEK inhibitors, and anti-EGFR underway
- **Second-line chemotherapy:** Nanoliposomal irinotecan (nal-IRI) + 5-FU/LV (NAPOLI-1: OS 6.1 vs. 4.2 months) — FDA-approved for post-gemcitabine; FOLFIRINOX if gem-nabP first-line; oxaliplatin + 5-FU/LV (OFF) for third-line

**Immunotherapy in PDAC:**
- Largely ineffective due to: (1) dense immunosuppressive desmoplastic stroma; (2) low TMB and low neoantigen burden in KRAS-mutant PDAC; (3) abundant MDSCs, TAMs (M2), and Tregs; (4) CXCL17 and galectin → exclusion of CD8+ T cells
- **MSI-H/MMR-deficient PDAC (<2%):** Pembrolizumab (KEYNOTE-158: ORR 18.2%); pembrolizumab first-line for MSI-H PDAC
- **Combination strategies under study:** Anti-PD-1 + anti-LAG-3, anti-PD-1 + CD40 agonist, anti-PD-1 + TGF-beta blockade, STING agonists, CAR-T (mesothelin, CEA targets); stroma-depleting strategies (hyaluronidase, anti-FAP CAR-T)

**Supportive care:**
- **Pancreatic enzyme replacement (PERT):** Required for exocrine insufficiency → malabsorption → weight loss; Creon 40,000+ units per meal
- **Pain:** Celiac plexus neurolysis (EUS-guided or CT-guided) — effective for abdominal/back pain; early palliative care integration associated with improved QoL and OS
- **Biliary obstruction:** ERCP + metal biliary stent (preferred); percutaneous transhepatic cholangiography (PTC) if ERCP fails
- **Gastric outlet obstruction:** Duodenal stent or surgical bypass (gastrojejunostomy)
- **DVT/PE:** Anticoagulation (LMWH preferred in cancer; direct oral anticoagulants in selected patients); VTE prevention with LMWH in high-risk ambulatory patients (AVERT/CASSINI trials)

## Connections

- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — KRAS is mutated in >90% of PDAC (G12D ~40%, G12V ~33%, G12R ~16%); constitutive RAS → RAF-MEK-ERK drives proliferation and survival; KRAS G12C inhibitors show modest activity in the rare G12C subset; pan-KRAS and KRAS G12D inhibitors are under active clinical development.
- `connects-to` → **[TGF-beta](../../03-molecular/tgf-beta/README.md)** — TGF-beta drives pancreatic desmoplasia via stellate cell activation → dense stroma limits chemo delivery; SMAD4 loss (~50% of PDAC) → TGF-beta loses tumor suppression; TGF-beta becomes pro-invasive and immune-exclusionary in SMAD4-null PDAC; anti-TGF-beta combinations under study.
- `connects-to` → **[BRCA1](../../03-molecular/brca1/README.md)** — BRCA1/2 germline mutations occur in ~5-10% of PDAC; olaparib maintenance (POLO trial) improved PFS in BRCA-mutant platinum-responsive mPDAC (7.4 vs. 3.8 months); somatic BRCA mutations in ~3%; homologous recombination deficiency testing guides PARP inhibitor selection.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — EGFR is overexpressed in ~60% of PDAC; erlotinib + gemcitabine modestly improves OS vs. gemcitabine alone (NCIC PA.3: OS 6.24 vs. 5.91 months; HR 0.82) — the only approved targeted therapy before KRAS inhibitors; anti-EGFR monoclonal antibodies (cetuximab) are ineffective in PDAC.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A (p16/INK4a) deleted/silenced in ~95% of PDAC; second earliest driver after KRAS; p16 loss → CDK4/6-RB hyperphosphorylation → unrestricted S-phase entry; ARF co-deletion → MDM2 unchecked → p53 suppressed; CDK4/6 inhibitors (palbociclib) evaluated in p16-null PDAC.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 mutations in ~70-75% of PDAC; p53 LOF → G2/M checkpoint failure and apoptosis evasion; late PanIN-3→PDAC transition event (vs KRAS = early); gain-of-function mutants (R175H, R248W) promote invasion; APR-246 (mutant p53 reactivator) in early PDAC trials.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — SMAD4 (DPC4) loss in ~55% of PDAC switches TGF-β from tumor suppressor to pro-invasive driver; SMAD4 loss predicts systemic metastasis vs local recurrence in SMAD4-intact; TGF-β → non-SMAD (RAS-ERK, PI3K) → EMT; SMAD4 IHC predicts spread in resected PDAC.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — Pancreatic ductal adenocarcinoma arises from the pancreas's exocrine ductal epithelium, growing silently until it obstructs the bile duct (painless jaundice) or invades vessels; deep location and early spread mean only ~20% are resectable, survival near 12% at 5 years.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Pancreatic cancer is defined by its stroma: KRAS-driven tumor cells activate stellate cells into cancer-associated fibroblasts that build a dense, hypovascular desmoplastic matrix starving the tumor of drugs and excluding T cells — why PDAC resists chemo and immunotherapy.
- `connects-to` → **[Hereditary Pancreatitis](../hereditary-pancreatitis/README.md)** — Hereditary pancreatitis (germline PRSS1, SPINK1) is a major pancreatic cancer risk: decades of recurring autodigestion and inflammation create a field of injury that, with smoking, drives a ~40-50× lifetime risk of pancreatic adenocarcinoma — among the highest predispositions.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^conroy-2011-folfirinox]: Conroy T, Desseigne F, Ychou M, et al. FOLFIRINOX versus gemcitabine for metastatic pancreatic cancer. *N Engl J Med.* 2011;364(19):1817-1825. [doi:10.1056/NEJMoa1011923](https://doi.org/10.1056/NEJMoa1011923) · [PubMed 21561347](https://pubmed.ncbi.nlm.nih.gov/21561347/)
[^golan-2019-polo]: Golan T, Hammel P, Reni M, et al. Maintenance olaparib for germline BRCA-mutated metastatic pancreatic cancer. *N Engl J Med.* 2019;381(4):317-327. [doi:10.1056/NEJMoa1903387](https://doi.org/10.1056/NEJMoa1903387) · [PubMed 31157963](https://pubmed.ncbi.nlm.nih.gov/31157963/)
[^von-hoff-2013-abraxane]: Von Hoff DD, Ervin T, Arena FP, et al. Increased survival in pancreatic cancer with nab-paclitaxel plus gemcitabine. *N Engl J Med.* 2013;369(18):1691-1703. [doi:10.1056/NEJMoa1304369](https://doi.org/10.1056/NEJMoa1304369) · [PubMed 24131140](https://pubmed.ncbi.nlm.nih.gov/24131140/)
