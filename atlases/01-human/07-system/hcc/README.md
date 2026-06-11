---
schema: human-scale-entry/v1
id: hcc
name: Hepatocellular Carcinoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Primary liver malignancy arising on a background of cirrhosis (HBV, HCV, alcohol, NAFLD); VEGF-driven neoangiogenesis targeted by sorafenib and lenvatinib; atezolizumab+bevacizumab is preferred first-line; CTNNB1 mutations (~30%) and TP53 mutations (~30%) are most common."
aliases: ["HCC", "hepatocellular carcinoma", "liver cancer", "primary liver cancer", "hepatoma"]
sources:
  - id: llovet-2008-sorafenib
    type: peer-reviewed
    cite: "Llovet JM, Ricci S, Mazzaferro V, et al. Sorafenib in advanced hepatocellular carcinoma. N Engl J Med. 2008;359(4):378-390."
    doi: "10.1056/NEJMoa0708857"
    pmid: "18650514"
    url: "https://doi.org/10.1056/NEJMoa0708857"
  - id: finn-2020-imbrave150
    type: peer-reviewed
    cite: "Finn RS, Qin S, Ikeda M, et al. Atezolizumab plus bevacizumab in unresectable hepatocellular carcinoma. N Engl J Med. 2020;382(20):1894-1905."
    doi: "10.1056/NEJMoa1915745"
    pmid: "32402160"
    url: "https://doi.org/10.1056/NEJMoa1915745"
cross_links:
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "MET → HGF → PI3K and RAS → VEGF transcription via HIF-1alpha; sorafenib and lenvatinib target both VEGFR and RET/PDGFR in HCC; MET amplification in HCC mediates resistance to sorafenib; cabozantinib (MET+VEGFR inhibitor) approved as second-line HCC therapy."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "MET → PI3K-AKT → mTOR → protein synthesis and survival in HCC; PTEN loss (~40% of HCC) amplifies mTOR activation; everolimus (mTORC1 inhibitor) failed to show OS benefit in EVOLVE-1 trial for advanced HCC after sorafenib; mTOR remains an active combination target."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "CTNNB1 mutations in ~30% of HCC → β-catenin nuclear accumulation → TCF/LEF → MYC, cyclin D1 → proliferation; CTNNB1-mutant HCC shows distinct metabolic phenotype and may be resistant to PD-1 immunotherapy via Wnt-driven immune exclusion — an emerging predictive biomarker."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Atezolizumab (anti-PD-L1) + bevacizumab → first-line HCC (IMbrave150): OS 19.2 vs. 13.4 months; preferred over sorafenib in most patients without autoimmune contraindications; pembrolizumab (KEYNOTE-240) and nivolumab (CheckMate 459) also active in second-line HCC."
  - target: 01-human/07-system/hepatitis-c
    relation: connects-to
    note: "HCV cirrhosis → HCC incidence 1-5%/year; HCV Core activates Wnt/β-catenin; chronic HCV inflammation → NF-κB/STAT3 → hepatocyte proliferation + driver mutations (TP53, TERT, CTNNB1); DAA cure reduces HCC risk ~70% but established cirrhosis retains annual HCC surveillance."
  - target: 01-human/07-system/hepatitis-b
    relation: connects-to
    note: "HBV causes ~50-55% of global HCC; integration near TERT/CCND1 → insertional mutagenesis; HBx transactivation → p53 inactivation, NF-κB, Wnt/β-catenin activation; HBsAg-positive cirrhosis has ~3-5%/year HCC incidence; antivirals reduce but do not eliminate HCC risk."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Hepatocellular carcinoma is almost unique among cancers in arising on a diseased organ: it grows from cirrhotic liver, so BCLC staging and treatment weigh tumour burden against residual liver function — from resection and ablation to transplant, TACE, and systemic therapy."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "HCC is a cancer of hepatocytes: the HGF-MET signaling that regenerates the liver after injury, running chronically in cirrhosis, drives the proliferation and accumulating mutations that transform hepatocytes into carcinoma."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "A TERT promoter mutation is the most common and earliest genetic event in hepatocellular carcinoma (~60%); the C228T/C250T hotspots reactivate telomerase, granting the replicative immortality that turns a dysplastic cirrhotic nodule into cancer."
---

# Hepatocellular Carcinoma

## Overview

**Hepatocellular carcinoma (HCC)** is the most common primary liver cancer and the third leading cause of cancer-related death worldwide. Unlike most solid tumors, HCC arises almost exclusively in the context of **hepatic fibrosis or cirrhosis** — a consequence of chronic liver injury from hepatitis B virus (HBV), hepatitis C virus (HCV), alcohol-associated liver disease (ALD), or non-alcoholic/metabolic-associated fatty liver disease (NAFLD/MAFLD). The cirrhotic microenvironment — characterized by portal hypertension, hepatic stellate cell activation, and chronic inflammation — provides a pro-tumorigenic niche that must be carefully considered in treatment planning [^llovet-2008-sorafenib].

**Epidemiology:**
- ~900,000 new cases/year worldwide (5th most common cancer globally); ~40,000/year in the United States
- Incidence rising in Western countries (driven by NAFLD); declining in East Asia with HBV vaccination
- Male predominance (M:F ~2.5:1)
- 5-year survival: ~18% overall; 70-80% for resected early-stage disease; <10% for advanced/metastatic disease

**Etiology and risk factors:**

| Risk factor | Relative risk | Mechanism |
|------------|---------------|-----------|
| HBV (HBsAg+, HBeAg+) | 100× | HBx oncoprotein → p53 inactivation, HBV DNA integration → genome instability |
| HCV (chronic) | 17× | Viral protein-driven steatosis + chronic inflammation → cirrhosis |
| Alcohol-related cirrhosis | 5× | ROS, acetaldehyde → DNA damage; gut dysbiosis → LPS → hepatic inflammation |
| NAFLD/NASH cirrhosis | 5× | Insulin resistance → lipotoxicity → stellate cell activation → fibrosis |
| Aflatoxin B1 exposure | 4× | TP53 R249S hotspot mutation (aflatoxin adduct) + HBV synergism |
| Hereditary hemochromatosis | 20× | Iron deposition → oxidative stress → cirrhosis |
| Alpha-1 antitrypsin deficiency | 5× | Protein aggregation in hepatocytes → ER stress → injury |

**HCC without cirrhosis (~15%):**
HBV-related HCC in non-cirrhotic liver (especially in Asian populations with perinatal HBV); also NAFLD-HCC in non-cirrhotic livers; fibrolamellar HCC (FL-HCC) — a distinct entity in young adults without underlying liver disease, driven by DNAJB1-PRKACA fusion.

## Structure

### Tumor anatomy and liver function

**Barcelona Clinic Liver Cancer (BCLC) staging:**
HCC staging uniquely combines tumor burden with liver function (Child-Pugh/ALBI score) and performance status — the BCLC system is most widely used:

| BCLC Stage | Tumor characteristics | Liver function | Treatment |
|------------|----------------------|----------------|-----------|
| 0 (Very early) | Single <2 cm | Child-Pugh A | Resection, ablation, transplant |
| A (Early) | Single or ≤3×≤3 cm | Child-Pugh A-B | Resection, transplant, ablation |
| B (Intermediate) | Multinodular, no vascular invasion | Child-Pugh A-B | TACE |
| C (Advanced) | Vascular invasion or extrahepatic spread | Child-Pugh A-B | Systemic therapy |
| D (End-stage) | Any | Child-Pugh C | Supportive care |

**Liver function metrics:**
- **Child-Pugh score:** Albumin, bilirubin, PT/INR, ascites, encephalopathy → Class A/B/C
- **ALBI score (albumin-bilirubin):** Objective metric using just albumin + bilirubin; discriminates Child-Pugh A subgroups
- **Barcelona score:** Preserves portal vein patency as a key treatment eligibility criterion

### Molecular landscape of HCC

**Signaling pathways altered in HCC:**

| Pathway | Frequency | Key drivers |
|---------|-----------|-------------|
| Wnt/β-catenin | ~40% | CTNNB1 (~30% activating), AXIN1/2 (~10% loss), APC (~2%) |
| p53/cell cycle | ~30% | TP53 mutation (~30%), CDKN2A deletion (~15%), RB1 deletion (~10%) |
| PI3K-AKT-mTOR | ~50% | PIK3CA (~10%), PTEN loss (~40%), TSC1/2 (~5%), RPS6KA3 (~5%) |
| Telomere | ~60% | TERT promoter (~60%) → nearly universal in HCC |
| Chromatin | ~30% | ARID1A (~10%), ARID2 (~5%), KMT2A/B, KDM6A |
| Oxidative stress | ~10% | NFE2L2/KEAP1 → antioxidant induction |
| HBV integration | ~90% (HBV+) | TERT, MLL4, CCNA2 integration sites → gene dysregulation |

**TERT promoter mutation:**
The single most frequent somatic alteration in HCC (~60%); occurs early in HCC development (found in cirrhotic nodules); activates TERT transcription → telomere maintenance → replicative immortality; C228T/C250T hotspots are the same ones found in GBM and thyroid cancer, confirming tissue-agnostic selection pressure.

**Wnt/β-catenin (CTNNB1) mutations:**
CTNNB1 mutations (exon 3 hotspots: D32-S45 cluster including S45, T41, S37, D32) → impaired GSK3β phosphorylation → β-catenin stabilization → nuclear TCF/LEF target gene transcription → MYC, cyclin D1, AXIN2 → proliferation; CTNNB1-mutant HCC is metabolically distinct (glutamine addicted, low-immunogenic) → potential resistance to PD-1/PD-L1 immunotherapy (multiple retrospective analyses suggest worsened IO outcomes in β-catenin-mutant HCC).

## Function

### Normal liver biology and HCC pathogenesis

**Hepatocyte homeostasis:**
The liver has remarkable regenerative capacity — removal of 70% of liver mass triggers compensatory hyperplasia via HGF-MET (primary) and EGF-EGFR → hepatocyte proliferation restoring original mass within 7-10 days. In cirrhosis, this regenerative capacity is impaired → compensatory increase in growth factor signaling → cumulative oncogenic mutation pressure.

**Angiogenesis in HCC:**
HCC is among the most vascular solid tumors — a direct consequence of VEGF overexpression in the hypoxic, cirrhotic microenvironment. HCC neovascularization provides the rationale for sorafenib, lenvatinib, and bevacizumab therapy. **TACE (transarterial chemoembolization)** exploits the hepatic arterial supply of HCC (vs. portal venous supply of normal liver) → selective ischemic kill + drug delivery; residual viable tumor after TACE typically shows VEGF upregulation → rationale for TACE + antiangiogenic combination (e.g., TACE + atezolizumab + bevacizumab in LEAP-012 trial).

### Immune evasion

**HCC immune microenvironment:**
The liver is an immunologically tolerogenic organ (tolerizes T cells via Kupffer cells and sinusoidal endothelial cells → prevents chronic immune activation against gut-derived antigens). HCC exploits this:
- High PD-L1 on tumor cells (~30-50% of HCC) and immunosuppressive Kupffer cells
- TGF-β and IDO → T cell exclusion and Treg induction
- Tregs (~20-40% of intratumoral T cells in HCC) → suppress CD8+ effectors
- NK cell dysfunction in HCC (TGF-β, IL-10, TIGIT upregulation)

**CTNNB1 and immune exclusion:**
β-catenin nuclear activity → transcriptional repression of CCL5 and CXCL10 (T cell chemokines) → "cold" immune excluded phenotype; this may explain inferior IO outcomes in CTNNB1-mutant HCC — an active area of research for combination strategies (Wnt inhibitor + IO).

## Pathology

### Diagnosis

**Imaging diagnosis (non-biopsy):**
In cirrhotic patients: if nodule ≥1 cm shows arterial phase hyperenhancement + washout (venous/delayed) on contrast-enhanced CT or MRI → LI-RADS 5 → HCC diagnosis without biopsy (>95% specificity). Biopsy required for atypical imaging or non-cirrhotic liver.

**Biomarker:**
- **AFP (alpha-fetoprotein):** Diagnostic and monitoring biomarker; sensitivity ~60% at threshold 20 ng/mL; highly elevated AFP (>400 ng/mL) essentially diagnostic in context
- **AFP-L3 fraction:** Lectin-reactive AFP; more specific for HCC vs. chronic liver disease
- **DCP (des-gamma-carboxyprothrombin, PIVKA-II):** Complementary to AFP; approved in Japan for HCC screening; captures AFP-low tumors

**HCC surveillance:**
In high-risk patients (cirrhosis, HBV regardless of cirrhosis): ultrasound ± AFP every 6 months → early detection → 3-fold higher curative therapy rates

### Treatment

**Curative options (early-stage HCC):**

- **Surgical resection:** Preferred if: single nodule, preserved liver function (Child-Pugh A, portal pressure <10 mmHg), no portal hypertension; 5-year OS ~70-80% for well-selected patients; recurrence rate ~50-70% at 5 years (intrahepatic recurrence from new primary or metastasis)
- **Liver transplantation (OLT):** Milan criteria (single ≤5 cm or ≤3×≤3 cm without vascular invasion/extrahepatic disease) → 5-year OS ~70% with transplant; down-staging possible with locoregional therapy; UNOS exception points for MELD score
- **Ablation:** Radiofrequency ablation (RFA) or microwave ablation (MWA) for tumors ≤3 cm; comparable outcomes to resection for small HCC; TACE+RFA combination for 3-5 cm lesions

**Locoregional therapy (intermediate stage BCLC B):**

- **TACE (transarterial chemoembolization):** Embolic particles ± doxorubicin/cisplatin/lipiodol → OS ~20-26 months (from 16 months untreated); conventional TACE vs. drug-eluting beads (DEB-TACE) — similar efficacy but DEB better safety
- **TARE (transarterial radioembolization, SIRT with Y-90):** Y-90 microspheres via hepatic artery → high-dose radiation to HCC; non-inferior to sorafenib in advanced HCC with portal vein thrombosis (Child-Pugh A); SORAMIC and SARAH trials showed comparable OS to sorafenib

**Systemic therapy (advanced stage BCLC C):**

*First-line:*
- **Atezolizumab + bevacizumab (IMbrave150):** [^finn-2020-imbrave150] OS 19.2 vs. 13.4 months vs. sorafenib; PFS 6.8 vs. 4.3 months; **preferred first-line** for patients without autoimmune disease or high variceal bleeding risk (bevacizumab contraindicated with high-risk varices → pre-screen with endoscopy)
- **Durvalumab + tremelimumab (HIMALAYA):** PD-L1+CTLA-4 combination; OS 16.4 vs. 13.8 months vs. sorafenib; option for patients who cannot receive bevacizumab
- **Sorafenib (SHARP trial):** [^llovet-2008-sorafenib] OS 10.7 vs. 7.9 months; first systemic therapy shown to improve OS in HCC (2007); still used when IO is contraindicated
- **Lenvatinib (REFLECT trial):** Non-inferior to sorafenib (OS 13.6 vs. 12.3 months, non-inferiority met); higher ORR (24% vs. 9%); alternative first-line

*Second-line:*
- Regorafenib (OS 10.6 vs. 7.8 months after sorafenib; approved 2017)
- Cabozantinib (OS 10.2 vs. 8.0 months; approved 2019) [^abou-alfa-2018-cabozantinib-hcc-ref]
- Ramucirumab (anti-VEGFR2; approved for AFP ≥400 ng/mL subgroup; REACH-2 trial)
- Pembrolizumab (KEYNOTE-240; OS 13.9 vs. 10.6 months; approved accelerated 2018; full approval pending)
- Nivolumab ± ipilimumab (CheckMate 459/040; approved accelerated; no Phase 3 OS superiority over sorafenib)

**Adjuvant therapy:**
- Atezolizumab + bevacizumab after resection/ablation (IMbrave050): 12-month RFS improved at interim (72% vs. 63%); pending final analysis; emerging as adjuvant option in high-risk HCC post-curative therapy

## Connections

- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — MET → HGF → PI3K and RAS → VEGF transcription via HIF-1alpha; sorafenib and lenvatinib target both VEGFR and RET/PDGFR in HCC; MET amplification in HCC mediates resistance to sorafenib; cabozantinib (MET+VEGFR inhibitor) approved as second-line HCC therapy.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — MET → PI3K-AKT → mTOR → protein synthesis and survival in HCC; PTEN loss (~40% of HCC) amplifies mTOR activation; everolimus (mTORC1 inhibitor) failed to show OS benefit in EVOLVE-1 trial for advanced HCC after sorafenib; mTOR remains an active combination target.
- `connects-to` → **[Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — CTNNB1 mutations in ~30% of HCC → β-catenin nuclear accumulation → TCF/LEF → MYC, cyclin D1 → proliferation; CTNNB1-mutant HCC shows distinct metabolic phenotype and may be resistant to PD-1 immunotherapy via Wnt-driven immune exclusion — an emerging predictive biomarker.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Atezolizumab (anti-PD-L1) + bevacizumab → first-line HCC (IMbrave150): OS 19.2 vs. 13.4 months; preferred over sorafenib in most patients without autoimmune contraindications; pembrolizumab (KEYNOTE-240) and nivolumab (CheckMate 459) also active in second-line HCC.
- `connects-to` → **[Hepatitis C](../hepatitis-c/README.md)** — HCV cirrhosis → HCC incidence 1-5%/year; HCV Core activates Wnt/β-catenin; chronic HCV inflammation → NF-κB/STAT3 → hepatocyte proliferation under oxidative DNA damage → driver mutations (TP53, TERT, CTNNB1); DAA cure reduces HCC risk ~70% but established cirrhosis retains HCC surveillance requirement.
- `connects-to` → **[Hepatitis B](../hepatitis-b/README.md)** — HBV is the leading viral cause of HCC (~50-55% of global cases); mechanisms include insertional mutagenesis near TERT/CCND1 → telomerase activation; HBx transactivation → p53 inactivation, NF-κB and Wnt/β-catenin activation; aflatoxin B1 co-exposure → TP53 R249S; HBsAg-positive cirrhosis carries ~3-5%/year HCC incidence; antiviral therapy reduces but does not eliminate HCC risk.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Hepatocellular carcinoma is almost unique among cancers in arising on a diseased organ: it grows from cirrhotic liver, so BCLC staging and treatment weigh tumour burden against residual liver function — from resection and ablation to transplant, TACE, and systemic therapy.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — HCC is a cancer of hepatocytes: the HGF-MET signaling that regenerates the liver after injury, running chronically in cirrhosis, drives the proliferation and accumulating mutations that transform hepatocytes into carcinoma.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — A TERT promoter mutation is the most common and earliest genetic event in hepatocellular carcinoma (~60%); the C228T/C250T hotspots reactivate telomerase, granting the replicative immortality that turns a dysplastic cirrhotic nodule into cancer.

[^llovet-2008-sorafenib]: Llovet JM, Ricci S, Mazzaferro V, et al. Sorafenib in advanced hepatocellular carcinoma. *N Engl J Med.* 2008;359(4):378-390. [doi:10.1056/NEJMoa0708857](https://doi.org/10.1056/NEJMoa0708857) · [PubMed 18650514](https://pubmed.ncbi.nlm.nih.gov/18650514/)
[^finn-2020-imbrave150]: Finn RS, Qin S, Ikeda M, et al. Atezolizumab plus bevacizumab in unresectable hepatocellular carcinoma. *N Engl J Med.* 2020;382(20):1894-1905. [doi:10.1056/NEJMoa1915745](https://doi.org/10.1056/NEJMoa1915745) · [PubMed 32402160](https://pubmed.ncbi.nlm.nih.gov/32402160/)
