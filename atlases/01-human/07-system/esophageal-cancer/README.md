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

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^doki-2022-checkmate648]: Doki Y, Ajani JA, Kato K, et al. Nivolumab combination therapy in advanced esophageal squamous-cell carcinoma. *N Engl J Med.* 2022;386(5):449-462. [doi:10.1056/NEJMoa2111380](https://doi.org/10.1056/NEJMoa2111380) · [PubMed 35108470](https://pubmed.ncbi.nlm.nih.gov/35108470/)
[^kato-2019-attraction3]: Kato K, Cho BC, Takahashi M, et al. Nivolumab versus chemotherapy in patients with advanced oesophageal squamous cell carcinoma refractory or intolerant to previous chemotherapy (ATTRACTION-3). *Lancet Oncol.* 2019;20(11):1506-1517. [doi:10.1016/S1470-2045(19)30626-6](https://doi.org/10.1016/S1470-2045(19)30626-6) · [PubMed 31582355](https://pubmed.ncbi.nlm.nih.gov/31582355/)
