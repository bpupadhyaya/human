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
  - target: 01-human/07-system/alcohol-use-disorder
    relation: connects-to
    note: "Chronic heavy alcohol use is a leading cause of HCC: alcoholic cirrhosis provides the inflamed, fibrotic background on which HCC arises, and alcohol synergizes with hepatitis B/C and obesity to multiply risk; abstinence and HCC surveillance in cirrhosis are key."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Obesity drives a rising share of HCC through MASLD/MASH (fatty liver): hepatic steatosis, insulin resistance and inflammation progress to cirrhosis and HCC—and uniquely, MASH-HCC can arise even without cirrhosis, complicating surveillance as obesity rates climb."
  - target: 01-human/07-system/cholangiocarcinoma
    relation: connects-to
    note: "HCC and cholangiocarcinoma are the two main primary liver cancers but differ in origin: HCC arises from hepatocytes (often in cirrhosis, AFP-secreting, treated with TACE and atezolizumab/bevacizumab), cholangiocarcinoma from bile-duct epithelium; combined tumors blur the line."
  - target: 01-human/07-system/nash
    relation: connects-to
    note: "NASH is a leading and fast-rising cause of hepatocellular carcinoma: metabolic-syndrome fatty liver inflames into steatohepatitis, fibrosis, and cirrhosis that turns malignant—and NASH-related HCC can arise even without cirrhosis, reshaping who needs surveillance."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Type 2 diabetes independently raises hepatocellular carcinoma risk: insulin resistance and hyperinsulinemia promote hepatocyte proliferation and fatty-liver inflammation, compounding viral and alcoholic causes—so diabetes drives much of the surging non-viral HCC."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Hepatocellular carcinoma is now treated by reactivating cytotoxic T cells: the liver's tolerogenic, immunosuppressive milieu lets HCC evade immunity, so PD-L1 blockade plus anti-VEGF (atezolizumab + bevacizumab) restores T-cell attack and is first-line for advanced disease."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Radiotherapy has a growing role in hepatocellular carcinoma: stereotactic body radiation and radioembolization (Y-90 microspheres delivering internal radiation) treat tumors unsuitable for resection or ablation—an option in a cancer long considered radioresistant."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages shape hepatocellular carcinoma's microenvironment: liver Kupffer cells and tumor-associated macrophages fuel chronic inflammation and suppress anti-tumor immunity, contributing to the immunosuppressive milieu that checkpoint inhibitors must overcome."
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "Hepatocellular and renal cell carcinoma are both highly vascular, VEGF-driven cancers treated alike: antiangiogenic tyrosine-kinase inhibitors and checkpoint inhibitors form the backbone for both, reflecting their shared dependence on a rich blood supply."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "p53 is one of the most mutated genes in liver cancer: it is inactivated in many HCCs, and aflatoxin B1 leaves a signature R249S TP53 mutation, so this tumor-suppressor loss links chemical carcinogens and viral hepatitis to malignant transformation."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "HCC almost always arises on a background of fibrosis: chronic injury scars the liver into cirrhosis, and the distorted, regenerating, inflamed tissue is the soil from which most hepatocellular carcinomas grow—why cirrhotic patients are screened with imaging."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron overload is a potent driver of HCC: in hereditary hemochromatosis, hepatocyte iron accumulation generates oxidative DNA damage and cirrhosis, so unchecked iron substantially raises liver-cancer risk—linking a single metal's metabolism to malignancy."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "The lung is HCC's commonest distant spread: liver tumor cells invade veins and seed the lungs, so pulmonary metastases mark advanced disease and prompt systemic therapy rather than local liver-directed treatment."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "HCC is intensely vascular, built around endothelial cells: it recruits abnormal new vessels (driven by VEGF), which is why anti-angiogenic drugs and trans-arterial embolization that targets its blood supply are mainstays of treatment."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "HCC is now treated by unleashing the immune system: arising in a chronically inflamed liver, it responds to checkpoint inhibitors, and atezolizumab plus bevacizumab became first-line therapy for advanced disease—immunotherapy paired with anti-angiogenesis."
  - target: 01-human/03-molecular/ctla-4
    relation: connects-to
    note: "HCC immunotherapy combines checkpoint blockers: the STRIDE regimen pairs anti-CTLA-4 (tremelimumab) with anti-PD-L1 (durvalumab), and atezolizumab+bevacizumab is another standard—so dual immune and anti-VEGF therapy now front-lines advanced liver cancer."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "The liver is NK-cell territory that HCC must evade: natural killer cells normally patrol the liver and kill transformed hepatocytes, so HCC's suppression of NK function is part of how it escapes immune control—and a target for therapy."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Carbon-ion radiotherapy is an option for liver cancer: heavy-ion beams deposit dose precisely in the tumor while sparing surrounding cirrhotic liver, offering a focal treatment for HCC unsuitable for surgery or ablation."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "HCC's cirrhotic background enlarges the spleen: scarring raises portal-vein pressure, which backs up into the spleen, causing splenomegaly and trapping platelets, so a big spleen and low platelets often signal the cirrhosis underlying liver cancer."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Chronic liver inflammation drives HCC through NF-kB: persistent hepatitis keeps this master switch active in hepatocytes, promoting survival and proliferation of damaged cells, so the inflammation-to-cancer path runs largely through NF-kB."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 helps explain why HCC favors men: Kupffer-cell IL-6 fuels tumor growth via STAT3, and because estrogen suppresses IL-6, women are partly protected, a link that also ties obesity and fatty-liver inflammation to liver cancer."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "HCC grows in a low-oxygen tumor: outpacing its blood supply, the cancer turns hypoxic, which switches on HIF and VEGF to sprout new vessels and makes it resistant to therapy—why anti-angiogenic drugs are central to treatment."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "HCC shelters behind regulatory T cells: the liver tumor accumulates Tregs that suppress the antitumor attack, a key reason it resists immunity and why checkpoint drugs aim to lift this brake on the immune system."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "HCC commonly spreads to the adrenal glands: after the lungs, the adrenals are among its favored metastatic sites, so imaging of these glands is part of staging advanced liver cancer."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "HCC arises in a cirrhotic liver that retains sodium as ascites, and worsening ascites or a falling blood sodium can signal tumor progression or portal-vein invasion."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "HCC can grow up the bloodstream: tumor thrombus extends through the hepatic veins into the inferior vena cava and even the right atrium of the heart, a finding that reshapes treatment."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "HCC can stir the bone marrow: it sometimes secretes erythropoietin as a paraneoplastic syndrome, driving polycythemia, and in advanced disease it metastasizes to bone."
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
- `connects-to` → **[Alcohol Use Disorder](../alcohol-use-disorder/README.md)** — Chronic heavy alcohol use is a leading cause of HCC: alcoholic cirrhosis provides the inflamed, fibrotic background on which HCC arises, and alcohol synergizes with hepatitis B/C and obesity to multiply risk; abstinence and HCC surveillance in cirrhosis are key.
- `connects-to` → **[Obesity](../obesity/README.md)** — Obesity drives a rising share of HCC through MASLD/MASH (fatty liver): hepatic steatosis, insulin resistance and inflammation progress to cirrhosis and HCC—and uniquely, MASH-HCC can arise even without cirrhosis, complicating surveillance as obesity rates climb.
- `connects-to` → **[Cholangiocarcinoma](../cholangiocarcinoma/README.md)** — HCC and cholangiocarcinoma are the two main primary liver cancers but differ in origin: HCC arises from hepatocytes (often in cirrhosis, AFP-secreting, treated with TACE and atezolizumab/bevacizumab), cholangiocarcinoma from bile-duct epithelium; combined tumors blur the line.
- `connects-to` → **[NASH](../nash/README.md)** — NASH is a leading and fast-rising cause of hepatocellular carcinoma: metabolic-syndrome fatty liver inflames into steatohepatitis, fibrosis, and cirrhosis that turns malignant—and NASH-related HCC can arise even without cirrhosis, reshaping who needs surveillance.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Type 2 diabetes independently raises hepatocellular carcinoma risk: insulin resistance and hyperinsulinemia promote hepatocyte proliferation and fatty-liver inflammation, compounding viral and alcoholic causes—so diabetes drives much of the surging non-viral HCC.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Hepatocellular carcinoma is now treated by reactivating cytotoxic T cells: the liver's tolerogenic, immunosuppressive milieu lets HCC evade immunity, so PD-L1 blockade plus anti-VEGF (atezolizumab + bevacizumab) restores T-cell attack and is first-line for advanced disease.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Radiotherapy has a growing role in hepatocellular carcinoma: stereotactic body radiation and radioembolization (Y-90 microspheres delivering internal radiation) treat tumors unsuitable for resection or ablation—an option in a cancer long considered radioresistant.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages shape hepatocellular carcinoma's microenvironment: liver Kupffer cells and tumor-associated macrophages fuel chronic inflammation and suppress anti-tumor immunity, contributing to the immunosuppressive milieu that checkpoint inhibitors must overcome.
- `connects-to` → **[Renal Cell Carcinoma](../renal-cell-carcinoma/README.md)** — Hepatocellular and renal cell carcinoma are both highly vascular, VEGF-driven cancers treated alike: antiangiogenic tyrosine-kinase inhibitors and checkpoint inhibitors form the backbone for both, reflecting their shared dependence on a rich blood supply.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — p53 is one of the most mutated genes in liver cancer: it is inactivated in many HCCs, and aflatoxin B1 leaves a signature R249S TP53 mutation, so this tumor-suppressor loss links chemical carcinogens and viral hepatitis to malignant transformation.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — HCC almost always arises on a background of fibrosis: chronic injury scars the liver into cirrhosis, and the distorted, regenerating, inflamed tissue is the soil from which most hepatocellular carcinomas grow—why cirrhotic patients are screened with imaging.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron overload is a potent driver of HCC: in hereditary hemochromatosis, hepatocyte iron accumulation generates oxidative DNA damage and cirrhosis, so unchecked iron substantially raises liver-cancer risk—linking a single metal's metabolism to malignancy.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — The lung is HCC's commonest distant spread: liver tumor cells invade veins and seed the lungs, so pulmonary metastases mark advanced disease and prompt systemic therapy rather than local liver-directed treatment.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — HCC is intensely vascular, built around endothelial cells: it recruits abnormal new vessels (driven by VEGF), which is why anti-angiogenic drugs and trans-arterial embolization that targets its blood supply are mainstays of treatment.
- `connects-to` → **[Immune System](../immune-system/README.md)** — HCC is now treated by unleashing the immune system: arising in a chronically inflamed liver, it responds to checkpoint inhibitors, and atezolizumab plus bevacizumab became first-line therapy for advanced disease—immunotherapy paired with anti-angiogenesis.
- `connects-to` → **[CTLA-4](../../03-molecular/ctla-4/README.md)** — HCC immunotherapy combines checkpoint blockers: the STRIDE regimen pairs anti-CTLA-4 (tremelimumab) with anti-PD-L1 (durvalumab), and atezolizumab+bevacizumab is another standard—so dual immune and anti-VEGF therapy now front-lines advanced liver cancer.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — The liver is NK-cell territory that HCC must evade: natural killer cells normally patrol the liver and kill transformed hepatocytes, so HCC's suppression of NK function is part of how it escapes immune control—and a target for therapy.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Carbon-ion radiotherapy is an option for liver cancer: heavy-ion beams deposit dose precisely in the tumor while sparing surrounding cirrhotic liver, offering a focal treatment for HCC unsuitable for surgery or ablation.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — HCC's cirrhotic background enlarges the spleen: scarring raises portal-vein pressure, which backs up into the spleen, causing splenomegaly and trapping platelets, so a big spleen and low platelets often signal the cirrhosis underlying liver cancer.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Chronic liver inflammation drives HCC through NF-kB: persistent hepatitis keeps this master switch active in hepatocytes, promoting survival and proliferation of damaged cells, so the inflammation-to-cancer path runs largely through NF-kB.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6 helps explain why HCC favors men: Kupffer-cell IL-6 fuels tumor growth via STAT3, and because estrogen suppresses IL-6, women are partly protected, a link that also ties obesity and fatty-liver inflammation to liver cancer.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — HCC grows in a low-oxygen tumor: outpacing its blood supply, the cancer turns hypoxic, which switches on HIF and VEGF to sprout new vessels and makes it resistant to therapy—why anti-angiogenic drugs are central to treatment.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — HCC shelters behind regulatory T cells: the liver tumor accumulates Tregs that suppress the antitumor attack, a key reason it resists immunity and why checkpoint drugs aim to lift this brake on the immune system.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — HCC arises in a cirrhotic liver that retains sodium as ascites, and worsening ascites or a falling blood sodium can signal tumor progression or portal-vein invasion.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — HCC can grow up the bloodstream: tumor thrombus extends through the hepatic veins into the inferior vena cava and even the right atrium of the heart, a finding that reshapes treatment.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — HCC can stir the bone marrow: it sometimes secretes erythropoietin as a paraneoplastic syndrome, driving polycythemia, and in advanced disease it metastasizes to bone.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — HCC commonly spreads to the adrenal glands: after the lungs, the adrenals are among its favored metastatic sites, so imaging of these glands is part of staging advanced liver cancer.

[^llovet-2008-sorafenib]: Llovet JM, Ricci S, Mazzaferro V, et al. Sorafenib in advanced hepatocellular carcinoma. *N Engl J Med.* 2008;359(4):378-390. [doi:10.1056/NEJMoa0708857](https://doi.org/10.1056/NEJMoa0708857) · [PubMed 18650514](https://pubmed.ncbi.nlm.nih.gov/18650514/)
[^finn-2020-imbrave150]: Finn RS, Qin S, Ikeda M, et al. Atezolizumab plus bevacizumab in unresectable hepatocellular carcinoma. *N Engl J Med.* 2020;382(20):1894-1905. [doi:10.1056/NEJMoa1915745](https://doi.org/10.1056/NEJMoa1915745) · [PubMed 32402160](https://pubmed.ncbi.nlm.nih.gov/32402160/)
