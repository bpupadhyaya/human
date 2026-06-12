---
schema: human-scale-entry/v1
id: gastric-cancer
name: Gastric Cancer
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "HER2 overexpression (~15-20%) and MSI-H (~10-15%) define actionable subsets; pembrolizumab is first-line for PD-L1+ gastric cancer; trastuzumab+chemotherapy is standard for HER2+ disease; ramucirumab (VEGFR2) and zolbetuximab (CLDN18.2) are approved in later lines."
aliases: ["gastric cancer", "stomach cancer", "gastric adenocarcinoma", "GEJ cancer", "gastroesophageal junction cancer", "gastric carcinoma", "GC"]
sources:
  - id: bang-2010-toga
    type: peer-reviewed
    cite: "Bang YJ, Van Cutsem E, Feyereislova A, et al. Trastuzumab in combination with chemotherapy versus chemotherapy alone for treatment of HER2-positive advanced gastric or gastro-oesophageal junction cancer (ToGA): a phase 3, open-label, randomised controlled trial. Lancet. 2010;376(9742):687-697."
    doi: "10.1016/S0140-6736(10)61121-X"
    pmid: "20728210"
    url: "https://doi.org/10.1016/S0140-6736(10)61121-X"
  - id: janjigian-2021-checkmate649
    type: peer-reviewed
    cite: "Janjigian YY, Shitara K, Moehler M, et al. First-line nivolumab plus chemotherapy versus chemotherapy alone for advanced gastric, gastro-oesophageal junction, and oesophageal adenocarcinoma (CheckMate 649). Lancet. 2021;398(10294):27-40."
    doi: "10.1016/S0140-6736(21)00797-2"
    pmid: "34102137"
    url: "https://doi.org/10.1016/S0140-6736(21)00797-2"
cross_links:
  - target: 01-human/03-molecular/her2
    relation: connects-to
    note: "HER2 overexpression in ~15-20% of gastric/GEJ cancer; trastuzumab+cisplatin+fluoropyrimidine is first-line for HER2+ disease (ToGA trial); T-DXd (trastuzumab deruxtecan) active in HER2-low and HER2-overexpressing gastric cancer (DESTINY-Gastric01)."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Ramucirumab (anti-VEGFR2) + paclitaxel is standard second-line for advanced gastric cancer (RAINBOW trial: OS 9.6 vs. 7.4 months); ramucirumab monotherapy also approved; bevacizumab failed to improve OS in AVAGAST; VEGFR2 is the validated antiangiogenic target in gastric cancer."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Pembrolizumab + chemotherapy is first-line for PD-L1 CPS ≥5 advanced gastric/GEJ adenocarcinoma (KEYNOTE-590/811); nivolumab + chemotherapy approved in many regions (CheckMate 649); MSI-H/dMMR gastric cancer (~10-15%) has particularly high response to PD-1 blockade (ORR >40%)."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "EGFR overexpression in ~30-40% of gastric cancer but EGFR-targeted therapy (cetuximab, panitumumab) failed in unselected gastric cancer trials; EGFR amplification in a subset → potential biomarker; FGFR2 amplification (~5-10%) responds to bemarituzumab (anti-FGFR2b)."
  - target: 02-pathogen/02-bacteria/helicobacter-pylori
    relation: connects-to
    note: "H. pylori is the dominant cause of non-cardia intestinal-type gastric cancer via the Correa cascade (gastritis → atrophy → metaplasia → dysplasia → carcinoma); CagA hijacks SHP-2/RAS-ERK and disrupts E-cadherin/β-catenin; eradication cuts GC incidence ~35-40%."
  - target: 02-pathogen/01-viruses/epstein-barr-virus
    relation: connects-to
    note: "EBV defines a distinct ~9% gastric cancer subtype (TCGA) with viral integration, near-universal PIK3CA mutation, CDKN2A silencing, and amplified CD274/PDCD1LG2 → very high PD-L1 → strong response to PD-1 blockade; EBER in-situ hybridization confirms it."
  - target: 01-human/07-system/hereditary-diffuse-gastric-cancer
    relation: connects-to
    note: "Germline CDH1 (E-cadherin) loss causes hereditary diffuse gastric cancer — signet-ring/poorly cohesive tumors with ~70% lifetime diffuse-GC risk plus elevated lobular breast cancer risk; prophylactic total gastrectomy is recommended for CDH1 carriers aged 18-40."
  - target: 01-human/07-system/cholangiocarcinoma
    relation: connects-to
    note: "Gastric cancer and cholangiocarcinoma are GI adenocarcinomas sharing actionable targets — HER2, PD-1/PD-L1, and FGFR2 — but arise differently: gastric cancer from stomach epithelium (H. pylori, EBV, germline CDH1), CCA from biliary cholangiocytes (FGFR2 fusions, IDH1 mutations)."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "Gastric cancer arises from the stomach's mucosal epithelium, usually via the Correa cascade of H. pylori gastritis → atrophy → metaplasia → dysplasia → intestinal-type carcinoma; the diffuse type (CDH1 loss) instead infiltrates the wall as signet-ring cells (linitis plastica)."
  - target: 01-human/07-system/esophageal-cancer
    relation: connects-to
    note: "Gastric and esophageal cancers merge at the gastroesophageal junction, where Siewert-classified adenocarcinomas are treated as one entity; both share HER2 amplification, PD-1 blockade, and reflux/obesity risk, while distal gastric and esophageal squamous cancers diverge by cause."
---

# Gastric Cancer

## Overview

**Gastric cancer (GC)** is the 5th most common cancer and 4th leading cause of cancer death worldwide, with the highest burden in East Asia, Eastern Europe, and South America. The majority (~95%) are **gastric adenocarcinomas** arising from the gastric mucosa. Gastric cancer biology is shaped by two major environmental exposures: *Helicobacter pylori* infection (the dominant etiological factor for non-cardia, intestinal-type GC) and Epstein-Barr virus (EBV, in a distinct molecular subtype). Modern molecular profiling has revealed actionable subsets — particularly HER2-overexpressing (~15-20%), MSI-H (~10-15%), and CLDN18.2-expressing (~30-40%) tumors — that are transforming treatment paradigms [^bang-2010-toga].

**Epidemiology:**
- ~1 million new cases/year globally (5th most common); declining incidence in Western countries (H. pylori eradication, dietary changes)
- ~30,000 new cases/year in the United States; much higher incidence in Japan/Korea (~40× higher than US)
- Male predominance (M:F ~2:1)
- 5-year survival: ~33% overall (US); <15% for metastatic disease; >90% for localized resected disease
- Risk factors: H. pylori infection (~80% of intestinal-type GC), high salt/nitrite diet, smoking, obesity (GERD → cardia GC), atrophic gastritis, intestinal metaplasia

**Gastroesophageal junction (GEJ) cancer:**
GEJ adenocarcinoma (Siewert type I-III) is biologically closer to distal esophageal/gastric cancer than esophageal squamous cell carcinoma; treated similarly to gastric cancer in most trials.

## Structure

### Molecular classification (TCGA 2014)

The TCGA classified gastric cancer into four molecular subtypes:

**EBV+ (~9%):**
- EBV viral integration → host gene silencing + PIK3CA mutations (~80%, highest frequency of any GC subtype) + amplification of JAK2, CD274 (PD-L1), PDCD1LG2 (PD-L2) → extreme PD-L1 expression → high PD-1 IO sensitivity; CDKN2A promoter hypermethylation (100%)
- Most frequently at gastric fundus/body; male predominance
- Highest PD-L1 expression → may benefit most from anti-PD-1 therapy

**MSI-H (~22%):**
- Hypermutation from microsatellite instability (MLH1 silencing by promoter methylation in sporadic MSI-H GC; MMR germline mutations in Lynch syndrome-associated GC)
- Good prognosis; most frequently in antrum; female, elderly
- High tumor mutational burden (TMB) → high neoantigen load → very high PD-1 response (ORR >40%)
- KRAS/NRAS/BRAF, PIK3CA mutations enriched; POLE mutations in some
- Pembrolizumab: accelerated approval for MSI-H/TMB-H solid tumors (2017) → MSI-H GC

**Genomically stable (GS, ~20%):**
- Diffuse histology (Signet ring/poorly cohesive); CDH1 mutations → E-cadherin loss → cell dissociation; RHOA mutations (~15%) → altered cytoskeletal dynamics; CLDN18-ARHGAP6/26 fusions; poorest prognosis; early peritoneal dissemination
- HER2-negative, MSI-stable; least responsive to current targeted therapy

**CIN (chromosomal instability, ~50%):**
- Intestinal histology; enriched in GEJ and fundus; aneuploidy; TP53 mutations (~70%); HER2 amplification enriched here; receptor tyrosine kinase amplification (VEGFR2, EGFR, FGFR2, MET)
- Most common subtype; most HER2-positive GC here

### Lauren classification (histology)

- **Intestinal type:** Gland-forming; associated with H. pylori, atrophic gastritis → intestinal metaplasia → dysplasia → carcinoma; better prognosis
- **Diffuse type:** Non-cohesive cells (signet-ring); CDH1 loss → E-cadherin-mediated adhesion lost; younger patients; early dissemination; hereditary diffuse GC (CDH1 germline mutation); worse prognosis
- **Mixed type:** Both patterns

### Hereditary gastric cancer

**Hereditary diffuse gastric cancer (HDGC):**
- Caused by germline CDH1 mutation (~40% of HDGC families)
- Lifetime risk of diffuse GC: ~70% (male), ~56% (female)
- Also elevated risk of lobular breast cancer
- **Prophylactic total gastrectomy** recommended for CDH1 pathogenic variant carriers (usually age 18-40) — confirmed HDGC at pathology in >80% of prophylactic gastrectomies

**Lynch syndrome:**
- MSI-H gastric cancer in ~1-5% of Lynch syndrome carriers (MLH1, MSH2, MSH6, PMS2 germline mutations)
- GC is the second most common Lynch-associated cancer after colorectal

## Function

### Helicobacter pylori carcinogenesis

**H. pylori molecular mechanisms:**
- **CagA (cytotoxin-associated gene A):** Injected into gastric epithelial cells via T4SS → CagA phosphorylation by Src/Abl kinases → CagA-SHP-2 interaction → RAS-ERK activation → proliferation; CagA also disrupts E-cadherin-β-catenin complex → Wnt/β-catenin activation → MYC; EPIYA motifs (Western vs. East Asian CagA) correlate with oncogenic potency
- **VacA (vacuolating cytotoxin A):** Forms ion channels → mitochondrial damage → apoptosis evasion; immune suppression (T cell inhibition); VacA+/CagA+ H. pylori strains → highest GC risk
- **Inflammatory cascade:** H. pylori → NFκB → IL-8, IL-1β, TNF-α → chronic gastritis → reactive oxygen species → DNA damage → epithelial-to-mesenchymal transition

**Correa cascade (intestinal-type pathway):**
Normal mucosa → superficial gastritis (H. pylori) → atrophic gastritis → intestinal metaplasia → dysplasia → intestinal-type GC

H. pylori eradication: Reduces GC incidence by ~35-40% (meta-analyses); most benefit when treated before atrophic changes develop.

### CLDN18.2 as a therapeutic target

**Claudin-18 isoform 2 (CLDN18.2):**
- A tight junction protein normally expressed exclusively on differentiated gastric mucosa cells (limited expression in normal organs)
- In GC, dedifferentiation → aberrant surface exposure of CLDN18.2 → targetable antigen
- **Zolbetuximab (IMAB362):** Anti-CLDN18.2 monoclonal antibody; **SPOTLIGHT trial** (zolbetuximab + mFOLFOX6): PFS 10.6 vs. 8.7 months and **GLOW trial** (zolbetuximab + CAPOX): PFS 8.2 vs. 6.8 months; FDA approved May 2024 for CLDN18.2+ HER2-negative GC/GEJ — first approved CLDN18.2-targeted therapy

## Pathology

### Staging and diagnosis

**Endoscopy:**
- Biopsy is essential; EGD with multiple biopsies for any suspicious lesion
- EUS (endoscopic ultrasound): T staging (T1 vs. T2-4) and regional node assessment → determines resectability and neoadjuvant chemotherapy need

**Imaging:**
- CT chest/abdomen/pelvis + PET/CT: Staging, detection of M1 disease; peritoneal metastasis often PET-negative → diagnostic laparoscopy for potentially resectable GC

**Biomarker testing (required for all advanced GC):**
- HER2 IHC ± FISH (IHC 3+ or IHC 2+/FISH+)
- MSI by PCR or dMMR by IHC (MLH1/MSH2/MSH6/PMS2)
- PD-L1 CPS (combined positive score)
- CLDN18.2 by IHC (≥75% of tumor cells with moderate-to-strong membranous staining = CLDN18.2+)
- HER2, FGFR2, and MET copy number and mutation by NGS
- TMB by NGS

**Lauren histology and TCGA molecular subtype** are not formally required outside research settings but inform prognosis and emerging targeted strategies.

### Treatment

**Localized gastric cancer (Stage I-III):**

*Surgery:*
- **Distal gastrectomy** (subtotal): For antral/body GC with adequate proximal margin
- **Total gastrectomy:** Proximal GC, multi-focal GC, HDGC prophylaxis
- **D2 lymphadenectomy:** Standard of care in Eastern practice; recommended ≥15 lymph nodes for adequate staging
- Minimally invasive (laparoscopic/robotic) gastrectomy: Non-inferior to open for early-stage GC

*Perioperative (neoadjuvant + adjuvant) chemotherapy:*
- **FLOT (docetaxel + oxaliplatin + leucovorin + 5-FU):** FLOT4 trial → OS 50 vs. 35 months vs. ECF; now standard perioperative regimen in Western practice
- **CAPOX or FOLFOX adjuvant:** For East Asian patients (CLASSIC trial); post-surgical
- **Nivolumab adjuvant:** CheckMate 577 (for resected GEJ, post-neoadjuvant CRT, residual disease) → DFS 22.4 vs. 11.0 months; approved 2021 for resected GEJ/esophageal cancer; expanding to gastric cancer

**Advanced/metastatic gastric cancer:**

*HER2+ (trastuzumab first-line, then T-DXd):*
- **Trastuzumab + cisplatin + fluoropyrimidine (ToGA trial):** [^bang-2010-toga] OS 13.8 vs. 11.1 months; PFS 6.7 vs. 5.5 months; ORR 47% vs. 35%; FDA approved 2010 — **first targeted therapy in GC**
- **Trastuzumab + pembrolizumab + chemotherapy (KEYNOTE-811):** PFS 10.0 vs. 8.1 months in HER2+/CPS≥1; FDA approved 2023 for HER2+ gastric cancer; now preferred frontline for HER2+/PD-L1+
- **T-DXd (DESTINY-Gastric01):** ORR 51% vs. 14%; OS 12.5 vs. 8.4 months in HER2+ post-trastuzumab gastric cancer; FDA approved 2021 as second-line HER2+ GC

*HER2-negative first-line (pembrolizumab ± chemotherapy):*
- **Nivolumab + chemotherapy (CheckMate 649):** [^janjigian-2021-checkmate649] OS 14.4 vs. 11.1 months for CPS≥5 (HR 0.71); PFS 7.7 vs. 6.0 months; FDA approved 2021 for GC/GEJC/EAC
- **Pembrolizumab + chemotherapy (KEYNOTE-590/811):** Active in PD-L1 CPS≥10 population

*MSI-H GC:*
- Pembrolizumab (pan-tumor MSI-H/TMB-H approval)
- High ORR (~40-60%), durable responses; may avoid chemotherapy in MSI-H high-risk GC
- Consider pembrolizumab monotherapy as first-line in MSI-H GC (KEYNOTE-158)

*Second-line:*
- Ramucirumab + paclitaxel (RAINBOW trial: OS 9.6 vs. 7.4 months — largest GC phase III) → most commonly used 2nd-line option
- Trifluridine-tipiracil (TAS-102) for 3rd-line+
- Irinotecan monotherapy
- FOLFIRI

*Novel targets:*
- **CLDN18.2:** Zolbetuximab + chemotherapy (approved 2024 for CLDN18.2+ HER2-negative GC)
- **FGFR2b (bemarituzumab):** ORR 38% vs. 25%; PFS 9.5 vs. 7.4 months in FGFR2b+ GC (FIGHT trial); not yet approved
- **MET amplification:** Telisotuzumab vedotin (MET-directed ADC) in early trials

## Connections

- `connects-to` → **[HER2](../../03-molecular/her2/README.md)** — HER2 overexpression in ~15-20% of gastric/GEJ cancer; trastuzumab+cisplatin+fluoropyrimidine is first-line for HER2+ disease (ToGA trial); T-DXd (trastuzumab deruxtecan) active in HER2-low and HER2-overexpressing gastric cancer (DESTINY-Gastric01).
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Ramucirumab (anti-VEGFR2) + paclitaxel is standard second-line for advanced gastric cancer (RAINBOW trial: OS 9.6 vs. 7.4 months); ramucirumab monotherapy also approved; bevacizumab failed to improve OS in AVAGAST; VEGFR2 is the validated antiangiogenic target in gastric cancer.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Pembrolizumab + chemotherapy is first-line for PD-L1 CPS ≥5 advanced gastric/GEJ adenocarcinoma (KEYNOTE-590/811); nivolumab + chemotherapy approved in many regions (CheckMate 649); MSI-H/dMMR gastric cancer (~10-15%) has particularly high response to PD-1 blockade (ORR >40%).
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — EGFR overexpression in ~30-40% of gastric cancer but EGFR-targeted therapy (cetuximab, panitumumab) failed in unselected gastric cancer trials; EGFR amplification in a subset → potential biomarker; FGFR2 amplification (~5-10%) responds to bemarituzumab (anti-FGFR2b).
- `connects-to` → **[Helicobacter pylori](../../../02-pathogen/02-bacteria/helicobacter-pylori/README.md)** — H. pylori is the dominant cause of non-cardia intestinal-type gastric cancer via the Correa cascade (gastritis → atrophy → metaplasia → dysplasia → carcinoma); CagA hijacks SHP-2/RAS-ERK and disrupts E-cadherin/β-catenin; eradication cuts GC incidence ~35-40%.
- `connects-to` → **[Epstein-Barr Virus](../../../02-pathogen/01-viruses/epstein-barr-virus/README.md)** — EBV defines a distinct ~9% gastric cancer subtype (TCGA) with viral integration, near-universal PIK3CA mutation, CDKN2A silencing, and amplified CD274/PDCD1LG2 → very high PD-L1 → strong response to PD-1 blockade; EBER in-situ hybridization confirms it.
- `connects-to` → **[Hereditary Diffuse Gastric Cancer](../hereditary-diffuse-gastric-cancer/README.md)** — Germline CDH1 (E-cadherin) loss causes hereditary diffuse gastric cancer — signet-ring/poorly cohesive tumors with ~70% lifetime diffuse-GC risk plus elevated lobular breast cancer risk; prophylactic total gastrectomy is recommended for CDH1 carriers aged 18-40.
- `connects-to` → **[Cholangiocarcinoma](../cholangiocarcinoma/README.md)** — Gastric cancer and cholangiocarcinoma are GI adenocarcinomas sharing actionable targets — HER2, PD-1/PD-L1, and FGFR2 — but arise differently: gastric cancer from stomach epithelium (H. pylori, EBV, germline CDH1), CCA from biliary cholangiocytes (FGFR2 fusions, IDH1 mutations).
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — Gastric cancer arises from the stomach's mucosal epithelium, usually via the Correa cascade of H. pylori gastritis → atrophy → metaplasia → dysplasia → intestinal-type carcinoma; the diffuse type (CDH1 loss) instead infiltrates the wall as signet-ring cells (linitis plastica).
- `connects-to` → **[Esophageal Cancer](../esophageal-cancer/README.md)** — Gastric and esophageal cancers merge at the gastroesophageal junction, where Siewert-classified adenocarcinomas are treated as one entity; both share HER2 amplification, PD-1 blockade, and reflux/obesity risk, while distal gastric and esophageal squamous cancers diverge by cause.

[^bang-2010-toga]: Bang YJ, Van Cutsem E, Feyereislova A, et al. Trastuzumab in combination with chemotherapy versus chemotherapy alone for treatment of HER2-positive advanced gastric or gastro-oesophageal junction cancer (ToGA): a phase 3, open-label, randomised controlled trial. *Lancet.* 2010;376(9742):687-697. [doi:10.1016/S0140-6736(10)61121-X](https://doi.org/10.1016/S0140-6736(10)61121-X) · [PubMed 20728210](https://pubmed.ncbi.nlm.nih.gov/20728210/)
[^janjigian-2021-checkmate649]: Janjigian YY, Shitara K, Moehler M, et al. First-line nivolumab plus chemotherapy versus chemotherapy alone for advanced gastric, gastro-oesophageal junction, and oesophageal adenocarcinoma (CheckMate 649). *Lancet.* 2021;398(10294):27-40. [doi:10.1016/S0140-6736(21)00797-2](https://doi.org/10.1016/S0140-6736(21)00797-2) · [PubMed 34102137](https://pubmed.ncbi.nlm.nih.gov/34102137/)
