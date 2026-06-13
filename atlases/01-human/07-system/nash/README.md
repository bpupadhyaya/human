---
schema: human-scale-entry/v1
id: nash
name: NASH
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Metabolic liver disease from steatosis (NAFLD) through steatohepatitis (NASH) to fibrosis and HCC; driven by insulin resistance and hepatic lipid overload. TGF-beta activates stellate cells → fibrosis; semaglutide and resmetirom (THR-beta agonist) are approved treatments."
aliases: ["nonalcoholic steatohepatitis", "NAFLD", "nonalcoholic fatty liver disease", "MASLD", "MASH", "metabolic dysfunction-associated steatotic liver disease", "metabolic dysfunction-associated steatohepatitis", "hepatic steatosis"]
sources:
  - id: younossi-2016-nafld-epidemiology
    type: peer-reviewed
    cite: "Younossi ZM, Koenig AB, Abdelatif D, Fazel Y, Henry L, Wymer M. Global epidemiology of nonalcoholic fatty liver disease — meta-analytic assessment of prevalence, incidence, and outcomes. Hepatology. 2016;64(1):73-84."
    doi: "10.1002/hep.28431"
    pmid: "26707365"
    url: "https://doi.org/10.1002/hep.28431"
  - id: harrison-2024-resmetirom
    type: peer-reviewed
    cite: "Harrison SA, Bedossa P, Guy CD, et al. A phase 3, randomized, controlled trial of resmetirom in NAFLD. N Engl J Med. 2024;390(6):497-509."
    doi: "10.1056/NEJMoa2309000"
    pmid: "38324483"
    url: "https://doi.org/10.1056/NEJMoa2309000"
  - id: rinella-2023-masld-nomenclature
    type: peer-reviewed
    cite: "Rinella ME, Lazarus JV, Ratziu V, et al. A multisociety Delphi consensus statement on new fatty liver disease nomenclature. Hepatology. 2023;78(6):1966-1986."
    doi: "10.1097/HEP.0000000000000520"
    pmid: "37363821"
    url: "https://doi.org/10.1097/HEP.0000000000000520"
cross_links:
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-beta is the primary pro-fibrogenic signal in NASH: macrophage- and hepatocyte-derived TGF-beta → hepatic stellate cell activation → alpha-SMA and collagen I deposition → fibrosis and cirrhosis; TGF-beta also promotes hepatocyte EMT and NASH-HCC progression."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Kupffer cells and recruited monocytes drive NASH: LPS-TLR4 → NF-kB → TNF-alpha, IL-1beta, IL-6 → hepatocyte injury and stellate cell activation; M1 macrophage polarization correlates with NASH histological activity; macrophage depletion attenuates experimental NASH fibrosis."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "Hepatocytes are the primary NASH target: lipid overload → ER stress, mitochondrial dysfunction, ROS → hepatocyte ballooning and lipoapoptosis; dying hepatocytes release DAMPs → Kupffer cell activation; hepatocyte SREBP-1c drives lipogenesis under insulin resistance."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "Hepatic insulin resistance is the core NASH driver: impaired insulin signaling → failure to suppress hepatic glucose output and VLDL; hyperinsulinemia → SREBP-1c → lipogenesis → steatosis and lipotoxicity; GLP-1 agonists and PPAR-gamma agonists improve insulin sensitivity."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "Semaglutide resolved NASH histology in 59% vs 17% placebo (Phase 2); GLP-1R activation reduces hepatic lipogenesis, liver inflammation, and oxidative stress; semaglutide ESSENCE Phase 3 NASH trial is ongoing; GLP-1R agonists are promising disease-modifying agents for NASH."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Adiponectin deficiency impairs hepatic AMPK → reduced fatty acid oxidation → steatosis; adiponectin suppresses TNF-α and NF-κB in Kupffer cells → reduced hepatic inflammation; pioglitazone (PPARγ agonist) raises adiponectin, reduces NASH steatohepatitis, and slows fibrosis."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Resistin (primarily monocyte/macrophage-derived in humans) activates NF-κB in Kupffer cells → TNF-α and IL-6 → NASH inflammation; resistin correlates with NASH histological severity; resistin inhibits adiponectin → impairs hepatic AMPK → steatosis and fibrosis."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Hepatocyte lipotoxicity + DAMPs → Kupffer cell CCL2; elevated hepatic CCL2 → CCR2+ monocyte-derived macrophage recruitment → NLRP3 → IL-1β + TNF-α → stellate cell activation → fibrosis; cenicriviroc (CCR2/CCR5 dual antagonist) studied in CENTAUR/AURORA trials."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "IL-10 from Kupffer cells and hepatic Tregs restrains NLRP3 inflammasome activation and stellate cell activation in NASH; IL-10 KO mice develop spontaneous steatohepatitis on high-fat diet; IL-10 deficiency correlates with fibrosis stage in human NASH biopsies."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "TGF-β1 → periostin in hepatic stellate cells → integrin αvβ3 → FAK/PI3K → collagen I/III deposition → hepatic fibrosis in NASH; periostin correlates with fibrosis stage; periostin-null mice develop less hepatic fibrosis in NASH models; periostin marks activated stellate cells."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "EDA-FN is upregulated in NASH liver via TGF-β1 → activates integrin α4β7 and TLR4 on HSCs → myofibroblast differentiation → collagen I/III → hepatic fibrosis; serum EDA-FN correlates with NASH fibrosis stage; FN matrix stiffness amplifies TGF-β activation in fibrotic liver."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "NASH is the hepatic face of type 2 diabetes and metabolic syndrome: insulin resistance floods the liver with fatty acids and drives lipotoxic inflammation, so most NASH patients are diabetic or pre-diabetic, and the two accelerate each other toward cirrhosis."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Obesity is the leading driver of NASH: excess visceral fat delivers free fatty acids and inflammatory adipokines to the liver, causing steatosis that progresses to steatohepatitis—so weight loss (diet, GLP-1 agonists, bariatric surgery) is the most effective treatment."
  - target: 01-human/07-system/hcc
    relation: connects-to
    note: "NASH is now a leading cause of hepatocellular carcinoma: chronic steatohepatitis drives fibrosis and cirrhosis that can become liver cancer—and uniquely, NASH-related HCC can arise even without cirrhosis, so rising fatty-liver prevalence is reshaping HCC epidemiology."
---

# NASH

## Overview

**NASH (non-alcoholic steatohepatitis)** — now formally renamed **MASH (metabolic dysfunction-associated steatohepatitis)** in 2023 consensus nomenclature [^rinella-2023-masld-nomenclature] — is the progressive inflammatory subtype of **NAFLD/MASLD (metabolic dysfunction-associated steatotic liver disease)**. NAFLD/MASLD affects approximately **32% of adults globally** (>1.9 billion people), making it the most common chronic liver disease worldwide [^younossi-2016-nafld-epidemiology]. Of those with NAFLD, ~25% develop NASH/MASH, which carries risk of progression to cirrhosis (~15-20% over 20 years) and hepatocellular carcinoma (HCC).

**2023 nomenclature update:**
- NAFLD → **MASLD** (metabolic dysfunction-associated steatotic liver disease)
- NASH → **MASH** (metabolic dysfunction-associated steatohepatitis)
- New cardiometabolic criteria required: steatosis + ≥1 of 5 metabolic risk factors (overweight/obesity, prediabetes/T2DM, hypertension, dyslipidemia, or elevated waist circumference); replaces "non-alcoholic" (exclusion criterion) with a positive metabolic definition
- "NASH" and "NAFLD" terms remain dominant in existing literature and clinical practice; both naming systems are used below

**Disease spectrum:**
- **Simple steatosis (NAFL/MASL):** Hepatic fat ≥5% on biopsy or imaging; minimal inflammation; low risk of progression (<3% → cirrhosis over 20 years); treat underlying metabolic disease
- **NASH/MASH:** Steatosis + hepatocyte ballooning (lipoapoptosis) + lobular inflammation ± fibrosis; NAS (NAFLD Activity Score ≥5) or MASH pattern on biopsy; ~15-20% → cirrhosis; HCC risk increased 5-17× vs. simple steatosis
- **NASH cirrhosis:** Compensated → decompensated (ascites, variceal bleed, hepatic encephalopathy, hepatorenal syndrome); leading indication for liver transplantation in the US alongside alcohol-related liver disease
- **NASH-HCC:** 10-20% of NASH-HCC develops without cirrhosis (non-cirrhotic HCC); distinct biology — more often HCC in metabolically active liver without the cirrhosis-driven regeneration trigger; worse survival due to late diagnosis

**Epidemiology and risk factors:**
- **Obesity:** BMI >30 → NAFLD in ~60-80%; visceral adiposity drives free fatty acid flux to liver (via portal vein from omental fat lipolysis)
- **Type 2 diabetes:** NAFLD in 70-80% of T2DM; NASH in 20-30%; T2DM + NASH → dramatically accelerated fibrosis progression
- **Metabolic syndrome:** Dyslipidemia (elevated TG, low HDL), hypertension — all independently associated
- **Genetic modifiers:** PNPLA3 I148M (patatin-like phospholipase domain containing 3; rs738409) → most common genetic variant affecting NASH susceptibility and fibrosis severity; TM6SF2 E167K → reduced VLDL secretion → hepatic lipid accumulation; HSD17B13 splice variant → protective (associated with reduced fibrosis); MBOAT7 intronic variant → NAFLD risk

## Structure

### Pathophysiology — "Multiple Hit" model

NASH pathogenesis is driven by multiple simultaneous and sequential hits, not a simple two-hit model:

**Hit 1 — Hepatic steatosis (lipid accumulation):**
- **Insulin resistance → lipid flux:** Adipose tissue insulin resistance → unrestrained lipolysis → elevated plasma FFAs → hepatic FFA uptake via CD36 and FATP
- **De novo lipogenesis (DNL):** Hyperinsulinemia → hepatic SREBP-1c activation → fatty acid synthase (FASN), acetyl-CoA carboxylase (ACC) → palmitate and other saturated FAs; fructose (from fructose-sweetened beverages) → hepatic DNL via ChREBP → triglyceride accumulation
- **Impaired VLDL secretion:** Reduced apoB100 lipidation → failed triglyceride export from hepatocytes → lipid trapping; TM6SF2 and APOB variants
- **Dietary FFA input:** Saturated FAs from diet → direct hepatic lipotoxicity

**Hit 2 — Lipotoxic hepatocyte injury:**
- **Saturated FFAs (palmitate, stearate):** Trigger ER stress (UPR: IRE1alpha, PERK, ATF6) → CHOP → hepatocyte apoptosis; also increase ceramide and diacylglycerol (DAG) → PKCε activation → IRS-1 serine phosphorylation → further insulin resistance (lipotoxicity-insulin resistance loop)
- **Mitochondrial dysfunction:** Excess FFA → beta-oxidation saturation → incomplete oxidation → ROS, lipid peroxidation products (4-HNE, MDA) → mitochondrial DNA damage → impaired OXPHOS → energy deficit → hepatocyte injury
- **Ballooning degeneration:** Swollen pale hepatocytes with Mallory-Denk bodies (ubiquitinated K8/K18 aggregates + p62) → histological hallmark of NASH; ballooned hepatocytes release DAMPs (HMGB1, mtDNA, extracellular vesicles)

**Hit 3 — Inflammatory amplification:**
- Lipotoxic DAMPs → activate Kupffer cells via TLR4, TLR9, NLRP3 → IL-1beta, IL-6, TNF-alpha → hepatocyte injury amplification; gut microbiome-derived LPS (via leaky gut / increased intestinal permeability → portal LPS) → TLR4-driven Kupffer cell activation (gut-liver axis)
- **Recruited monocytes/macrophages:** CXCL2/CCL2 → circulating monocytes infiltrate liver → differentiate into inflammatory macrophages → amplify IL-6, TNF-alpha, IL-1beta → hepatocyte necroapoptosis → stellate cell activation
- **NLRP3 inflammasome:** Lipotoxicity → NLRP3 → caspase-1 → IL-1beta → fibrogenic and inflammatory amplification in Kupffer cells; emerging therapeutic target in NASH (selnoflast, a covalent NLRP3 inhibitor, in NASH trials)

**Hit 4 — Hepatic fibrosis (stellate cell activation):**
- Lipotoxic hepatocytes → paracrine signals (TGF-beta1, PDGF, SHH, CXCL16) → hepatic stellate cells (HSCs) activation → loss of lipid droplets → myofibroblast phenotype (alpha-SMA+) → collagen I/III/IV deposition → fibrosis
- **Fibrosis stages (NASH):** F0 (none), F1 (perisinusoidal or periportal), F2 (perisinusoidal + periportal), F3 (bridging), F4 (cirrhosis); liver-related mortality rises sharply at F3-F4
- **HSC activation pathways:** TGF-beta1 → SMAD2/3 → alpha-SMA, type I collagen gene transcription; PDGF → HSC proliferation; Hedgehog (SHH from hepatocytes) → HSC survival and fibrogenesis

## Function

### Clinical presentation

**Symptoms:** Predominantly asymptomatic until advanced fibrosis or cirrhosis; may present with right upper quadrant discomfort, fatigue, or incidentally on imaging (hepatic steatosis on US/CT/MRI)

## Pathology

### Diagnosis

**Non-invasive assessment:**
- **Liver function tests:** ALT elevated in NASH (but can be normal in cirrhosis); AST:ALT ratio >1 → advanced fibrosis (hepatic reserve depleted); GGT elevation (lipotoxicity, oxidative stress)
- **FibroScan (transient elastography):** Liver stiffness (kPa) → fibrosis staging; controlled attenuation parameter (CAP) → steatosis grade; FDA-cleared, widely used first-line assessment
- **MRI-PDFF (proton density fat fraction):** Gold standard non-invasive steatosis quantification; MR elastography (MRE) → fibrosis
- **Serum biomarkers:** FIB-4 score (age × AST / [platelets × ALT^0.5]) → fibrosis risk; NAFLD Fibrosis Score; ELF (Enhanced Liver Fibrosis) panel (P3NP, TIMP1, HA) → advanced fibrosis; PRO-C3 (type III collagen neoepitope) → fibrogenesis activity
- **Liver biopsy (gold standard):** NAS scoring: steatosis (0-3), lobular inflammation (0-3), hepatocyte ballooning (0-2); NAS ≥5 = NASH; fibrosis stage (0-4) assessed separately via Brunt/NASH CRN criteria; reserved for uncertain diagnosis, clinical trials, or pre-treatment fibrosis staging

**HCC surveillance:**
- Every 6 months ultrasound ± AFP in NASH cirrhosis; non-cirrhotic NASH-HCC surveillance less well-defined; MRI preferred over US in obese patients (poor US penetration)

### Treatment [^harrison-2024-resmetirom]

**Lifestyle modification (foundation of all NASH treatment):**
- **Weight loss:** 7-10% body weight loss → NASH resolution in ~50%; ≥10% → significant fibrosis regression; Mediterranean diet reduces hepatic fat independent of calories; structured exercise (aerobic + resistance) reduces hepatic lipid even without weight loss
- **Bariatric surgery:** Most effective intervention for morbidly obese NASH; Roux-en-Y gastric bypass or sleeve gastrectomy → 80-90% NASH resolution, significant fibrosis regression; also reduces T2DM, cardiovascular events; dedicated NASH bariatric trials ongoing

**Pharmacological — approved (2024):**

- **Resmetirom (Rezdiffra, THR-beta agonist):** FDA approved March 2024 — first NASH-specific pharmacological treatment; selective thyroid hormone receptor beta (THR-beta) agonist → liver-specific thyroid receptor activation → reduced DNL, increased beta-oxidation, reduced liver fat; MAESTRO-NASH Phase 3: 25.9% NASH resolution + ≥1 fibrosis stage improvement (vs. 9.7% placebo) at week 52; 24.2% ≥1 fibrosis improvement vs. 14.2% placebo; approved for adults with NASH/MASH + moderate-severe fibrosis (F2-F3) [^harrison-2024-resmetirom]
- **Semaglutide (Ozempic, Wegovy — GLP-1 agonist):** FDA approved for T2DM and obesity; NASH sub-study (PIONEER and ESSENCE-NASH): 59% NASH resolution at week 72 (vs. 17% placebo) but no significant fibrosis benefit in Phase 2; ESSENCE-NASH (Phase 3) in progress — largest NASH trial; semaglutide reduces body weight, hepatic DNL via GLP-1R activation, and improves insulin sensitivity; also reduces MACE in T2DM patients with established CVD (SUSTAIN-6, SELECT trials) — directly addresses the leading cause of death in NASH (cardiovascular disease)

**Pharmacological — investigational:**
- **Lanifibranor (PPAR-alpha/gamma/delta pan-agonist):** NATIVE trial (Phase 2b): significant improvement in NAS and fibrosis; Phase 3 NATIV3 ongoing
- **Obeticholic acid (OCA, FXR agonist):** REGENERATE trial: improvement in fibrosis at 18 months but no sustained benefit at 48 months; FDA declined approval due to safety (pruritus, LDL elevation) and limited efficacy; not currently approved
- **Selnoflast, DFV890 (NLRP3 inhibitors):** Phase 2 in NASH; mechanistically promising (inflammasome-fibrosis connection)
- **Combinations:** Semaglutide + resmetirom, semaglutide + ACC inhibitors — targeting multiple pathways simultaneously

## Connections

- `connects-to` → **[TGF-beta](../../03-molecular/tgf-beta/README.md)** — TGF-beta is the primary pro-fibrogenic signal in NASH: macrophage- and hepatocyte-derived TGF-beta → hepatic stellate cell activation → alpha-SMA and collagen I deposition → fibrosis and cirrhosis; TGF-beta also promotes hepatocyte EMT and NASH-HCC progression.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Kupffer cells and recruited monocytes drive NASH: LPS-TLR4 → NF-kB → TNF-alpha, IL-1beta, IL-6 → hepatocyte injury and stellate cell activation; M1 macrophage polarization correlates with NASH histological activity; macrophage depletion attenuates experimental NASH fibrosis.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — Hepatocytes are the primary NASH target: lipid overload → ER stress, mitochondrial dysfunction, ROS → hepatocyte ballooning and lipoapoptosis; dying hepatocytes release DAMPs → Kupffer cell activation; hepatocyte SREBP-1c drives lipogenesis under insulin resistance.
- `connects-to` → **[Insulin Receptor](../../03-molecular/insulin-receptor/README.md)** — Hepatic insulin resistance is the core NASH driver: impaired insulin signaling → failure to suppress hepatic glucose output and VLDL; hyperinsulinemia → SREBP-1c → de novo lipogenesis → steatosis and lipotoxicity; GLP-1 agonists and PPAR-gamma agonists improve insulin sensitivity.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — Semaglutide resolved NASH histology in 59% vs 17% placebo (Phase 2); GLP-1R activation reduces hepatic lipogenesis, liver inflammation, and oxidative stress; semaglutide ESSENCE Phase 3 NASH trial is ongoing; GLP-1R agonists are promising disease-modifying agents for NASH.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — adiponectin deficiency impairs hepatic AMPK → reduced fatty acid oxidation → steatosis; adiponectin suppresses TNF-α and NF-κB in Kupffer cells → reduced hepatic inflammation; pioglitazone (PPARγ agonist) raises adiponectin, reduces NASH steatohepatitis, and slows fibrosis.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Resistin (primarily monocyte/macrophage-derived in humans) activates NF-κB in Kupffer cells → TNF-α and IL-6 → NASH inflammation; resistin correlates with NASH histological severity; resistin inhibits adiponectin → impairs hepatic AMPK → steatosis and fibrosis.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Hepatocyte lipotoxicity + DAMPs → Kupffer cell CCL2; elevated hepatic CCL2 → CCR2+ monocyte-derived macrophage recruitment → NLRP3 → IL-1β + TNF-α → stellate cell activation → fibrosis; cenicriviroc (CCR2/CCR5 dual antagonist) studied in CENTAUR/AURORA trials.
- `connects-to` → **[Interleukin-10](../../03-molecular/il-10/README.md)** — IL-10 from Kupffer cells and hepatic Tregs restrains NLRP3 inflammasome activation and stellate cell activation in NASH; IL-10 KO mice develop spontaneous steatohepatitis on high-fat diet; IL-10 deficiency correlates with fibrosis stage in human NASH biopsies.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — TGF-β1 → periostin in hepatic stellate cells → integrin αvβ3 → FAK/PI3K → collagen I/III deposition → hepatic fibrosis in NASH; periostin correlates with fibrosis stage; periostin-null mice develop less hepatic fibrosis in NASH models; periostin marks activated stellate cells.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — EDA-FN is upregulated in NASH liver via TGF-β1 → activates integrin α4β7 and TLR4 on HSCs → myofibroblast differentiation → collagen I/III → hepatic fibrosis; serum EDA-FN correlates with NASH fibrosis stage; FN matrix stiffness amplifies TGF-β activation in fibrotic liver.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — NASH is the hepatic face of type 2 diabetes and metabolic syndrome: insulin resistance floods the liver with fatty acids and drives lipotoxic inflammation, so most NASH patients are diabetic or pre-diabetic, and the two accelerate each other toward cirrhosis.
- `connects-to` → **[Obesity](../obesity/README.md)** — Obesity is the leading driver of NASH: excess visceral fat delivers free fatty acids and inflammatory adipokines to the liver, causing steatosis that progresses to steatohepatitis—so weight loss (diet, GLP-1 agonists, bariatric surgery) is the most effective treatment.
- `connects-to` → **[Hepatocellular Carcinoma](../hcc/README.md)** — NASH is now a leading cause of hepatocellular carcinoma: chronic steatohepatitis drives fibrosis and cirrhosis that can become liver cancer—and uniquely, NASH-related HCC can arise even without cirrhosis, so rising fatty-liver prevalence is reshaping HCC epidemiology.

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^younossi-2016-nafld-epidemiology]: Younossi ZM, Koenig AB, Abdelatif D, Fazel Y, Henry L, Wymer M. Global epidemiology of nonalcoholic fatty liver disease — meta-analytic assessment of prevalence, incidence, and outcomes. *Hepatology.* 2016;64(1):73-84. [doi:10.1002/hep.28431](https://doi.org/10.1002/hep.28431) · [PubMed 26707365](https://pubmed.ncbi.nlm.nih.gov/26707365/)
[^harrison-2024-resmetirom]: Harrison SA, Bedossa P, Guy CD, et al. A phase 3, randomized, controlled trial of resmetirom in NAFLD. *N Engl J Med.* 2024;390(6):497-509. [doi:10.1056/NEJMoa2309000](https://doi.org/10.1056/NEJMoa2309000) · [PubMed 38324483](https://pubmed.ncbi.nlm.nih.gov/38324483/)
[^rinella-2023-masld-nomenclature]: Rinella ME, Lazarus JV, Ratziu V, et al. A multisociety Delphi consensus statement on new fatty liver disease nomenclature. *Hepatology.* 2023;78(6):1966-1986. [doi:10.1097/HEP.0000000000000520](https://doi.org/10.1097/HEP.0000000000000520) · [PubMed 37363821](https://pubmed.ncbi.nlm.nih.gov/37363821/)
