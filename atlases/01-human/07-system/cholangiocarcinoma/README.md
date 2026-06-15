---
schema: human-scale-entry/v1
id: cholangiocarcinoma
name: Cholangiocarcinoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Cholangiocarcinoma includes intrahepatic (iCCA), perihilar, and distal subtypes; FGFR2 fusions and IDH1 mutations (~15% each) define iCCA. Gemcitabine/cisplatin+durvalumab (TOPAZ-1) is first-line; pemigatinib is approved for FGFR2-fusion iCCA; ivosidenib for IDH1-mutant CCA."
aliases: ["cholangiocarcinoma", "CCA", "intrahepatic cholangiocarcinoma", "iCCA", "perihilar cholangiocarcinoma", "Klatskin tumor", "biliary tract cancer", "BTC", "bile duct cancer", "FGFR2 fusion CCA"]
sources:
  - id: abou-alfa-2020-claridy
    type: peer-reviewed
    cite: "Abou-Alfa GK, Macarulla T, Javle MM, et al. Ivosidenib in IDH1-mutant, chemotherapy-refractory cholangiocarcinoma (ClarIDHy): a multicentre, randomised, double-blind, placebo-controlled, phase 3 study. Lancet Oncol. 2020;21(6):796-807."
    doi: "10.1016/S1470-2045(20)30157-1"
    pmid: "32416072"
    url: "https://doi.org/10.1016/S1470-2045(20)30157-1"
  - id: oh-2022-topaz1
    type: peer-reviewed
    cite: "Oh DY, He AR, Qin S, et al. Durvalumab plus Gemcitabine and Cisplatin in Biliary Tract Cancer. NEJM Evidence. 2022;1(8):EVIDoa2200015."
    doi: "10.1056/EVIDoa2200015"
    pmid: "38319282"
    url: "https://doi.org/10.1056/EVIDoa2200015"
cross_links:
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "FGFR2 fusions/rearrangements in ~15-20% of iCCA; pemigatinib (FIGHT-202: ORR 36%, FDA 2020) and futibatinib (FOENIX-CCA2: ORR 42%, FDA 2023) are approved; FGFR2 inhibitors are the leading targeted therapy in iCCA; erdafitinib active in FGFR-altered CCA."
  - target: 01-human/03-molecular/idh1
    relation: connects-to
    note: "IDH1 mutations in ~15-20% of iCCA; IDH1 R132C/L → 2-HG → TET2 inhibition → DNA hypermethylation; ivosidenib (ClarIDHy: PFS 2.7 vs 1.4 months) is FDA-approved for IDH1-mutant CCA; IDH2 mutations occur in ~5% of iCCA."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Durvalumab (PD-L1) + gemcitabine/cisplatin (TOPAZ-1: OS 12.8 vs 11.5 months, FDA 2022) is first-line for advanced CCA; pembrolizumab + gem/cis (KEYNOTE-966: OS 12.7 vs 10.9 months, FDA 2023) also approved; PD-L1 CPS predicts benefit."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "KRAS mutations in ~10-20% of iCCA and ~30-40% of extrahepatic CCA; KRAS G12C targetable with sotorasib/adagrasib (early data); KRAS mutations associate with poor prognosis; CCA is among the major RAS-driven GI cancers lacking standard targeted therapy."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Cholangiocarcinoma arises from cholangiocytes within or adjacent to the liver; iCCA is the 2nd most common primary liver cancer after HCC; PSC, HBV/HCV, and cirrhosis elevate CCA risk 2-3×; hepatic resection with negative margins is the only curative approach for iCCA."
  - target: 01-human/03-molecular/braf
    relation: connects-to
    note: "BRAF V600E mutations in ~5% of all CCA; dabrafenib + trametinib (BRAF+MEK inhibition) approved tumor-agnostically (FDA 2022) with ~50% ORR in BRAF V600E CCA; BRAF V600E CCA responds similarly to BRAF-mutant melanoma/NSCLC; concomitant IDH or FGFR alterations are rare."
  - target: 01-human/03-molecular/her2
    relation: connects-to
    note: "HER2 amplification or overexpression in ~5-10% of biliary tract cancers; trastuzumab deruxtecan (DESTINY-PanTumor02) ORR 22% in HER2 IHC 2+/3+ BTC; zanidatamab active in HER2+ BTC; HER2 testing recommended in all advanced BTC per ESMO 2023 guidelines."
  - target: 01-human/07-system/gastric-cancer
    relation: connects-to
    note: "Cholangiocarcinoma and gastric cancer are both GI adenocarcinomas converging on shared targets — HER2, PD-1/PD-L1 blockade, and FGFR alterations — yet differ in origin: CCA from biliary cholangiocytes (FGFR2 fusions, IDH1), gastric cancer from stomach epithelium (H. pylori, EBV)."
  - target: 01-human/07-system/hcc
    relation: connects-to
    note: "Cholangiocarcinoma and hepatocellular carcinoma are the two primary liver cancers, distinguished by cell of origin — cholangiocytes versus hepatocytes; combined HCC-CCA tumors exist, both share cirrhosis and viral hepatitis as risks, but their targeted therapies differ entirely."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "Cholangiocarcinoma and pancreatic cancer are pancreaticobiliary neighbors blending at the ampulla: distal CCA and pancreatic-head adenocarcinoma both cause painless obstructive jaundice, share KRAS-driven biology and the gemcitabine/cisplatin backbone, and carry grim outcomes."
  - target: 01-human/07-system/inflammatory-bowel-disease
    relation: connects-to
    note: "Cholangiocarcinoma is the feared malignancy of inflammatory bowel disease via primary sclerosing cholangitis: PSC, strongly linked to ulcerative colitis, scars the bile ducts and carries a high lifetime risk of bile-duct cancer—so PSC-IBD patients need biliary surveillance."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "Cholangiocarcinoma and colorectal cancer are both GI adenocarcinomas linked through PSC-IBD: ulcerative colitis with primary sclerosing cholangitis raises both colorectal and bile-duct cancer risk, and both can harbor actionable BRAF or mismatch-repair-deficient subtypes."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Cholangiocarcinoma is defined by its desmoplastic stroma: cancer-associated fibroblasts build a dense fibrous matrix that surrounds the tumor, supplies growth and survival signals, and physically impedes drug delivery—one reason this bile-duct cancer is so chemoresistant."
  - target: 01-human/07-system/idh-mutant-glioma
    relation: connects-to
    note: "Cholangiocarcinoma and IDH-mutant glioma are united by IDH1 mutation and the oncometabolite 2-HG: ~15-20% of intrahepatic cholangiocarcinomas carry IDH1 R132, and ivosidenib—first for IDH-mutant leukemia and glioma—now treats IDH1-mutant cholangiocarcinoma."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "Cholangiocarcinoma arises from biliary epithelium, not hepatocytes, distinguishing it from HCC: it springs from cholangiocytes lining bile ducts, so it lacks AFP and hepatocyte markers and expresses biliary cytokeratins—a key distinction for a liver mass."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Cholangiocarcinoma is mostly immunologically cold but responds in a subset: a dense desmoplastic, immunosuppressive stroma keeps cytotoxic T cells out, yet mismatch-repair-deficient or PD-L1-high tumors respond to checkpoint blockade now added to chemotherapy first-line."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 mutation is common in cholangiocarcinoma: loss of p53, alongside KRAS and FGFR/IDH alterations, removes a key checkpoint in bile-duct epithelium, so chronic inflammation plus p53 loss drives the malignant transformation behind this hard-to-treat cancer."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "A macrophage-rich desmoplastic stroma defines cholangiocarcinoma: tumor-associated macrophages and fibroblasts build a dense, immunosuppressive matrix that walls the tumor off, helping explain its chemoresistance and limited response to immunotherapy."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Cholangiocarcinoma relies on VEGF-driven angiogenesis: the tumor secretes VEGF to vascularize its desmoplastic mass, high levels predict worse outcome, and anti-angiogenic agents are studied alongside the chemotherapy and targeted FGFR/IDH inhibitors used in treatment."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Cholangiocarcinoma arises from chronically inflamed, fibrotic bile ducts: primary sclerosing cholangitis, liver fluke and stones scar the biliary tree, and this fibrosis-inflammation milieu is the soil in which the cancer develops—mirroring HCC arising in cirrhosis."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Radiotherapy has a role in cholangiocarcinoma: photon-based external-beam or stereotactic radiation, often with chemo, treats unresectable bile-duct tumors and the perihilar disease that obstructs the ducts—palliating jaundice and sometimes downstaging for surgery."
  - target: 01-human/07-system/hepatitis-c
    relation: connects-to
    note: "Hepatitis C is a recognized risk factor for cholangiocarcinoma: chronic viral inflammation and the cirrhosis it causes raise the risk of intrahepatic bile-duct cancer as well as HCC, so the two primary liver cancers share this viral driver."
  - target: 01-human/07-system/hepatitis-b
    relation: connects-to
    note: "Hepatitis B raises cholangiocarcinoma risk: chronic HBV inflames the liver and bile ducts, and like its link to hepatocellular cancer, the virus is an established risk factor for intrahepatic bile-duct cancer—so viral hepatitis spans both primary liver cancers."
  - target: 01-human/07-system/nash
    relation: connects-to
    note: "Fatty liver disease is a rising cause of cholangiocarcinoma: NASH-driven inflammation and fibrosis increasingly underlie intrahepatic bile-duct cancer, so the metabolic epidemic is expanding a tumor once tied mainly to flukes and bile-duct disease."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Cholangiocarcinoma grows out of chronic biliary inflammation: neutrophils and other immune cells in inflamed, infected, or stone-laden bile ducts release IL-6 and reactive species that drive the DNA damage transforming cholangiocytes—inflammation as carcinogen."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Cholangiocarcinoma arises amid copper-retaining cholestasis: the liver normally excretes copper into bile, so blocked or inflamed ducts trap copper in the liver—a marker of the chronic cholestasis (as in PSC) that breeds this bile-duct cancer."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Cholangiocarcinoma reactivates Notch signaling: the pathway that tells liver progenitors to become bile-duct cells is hijacked to drive tumor formation, so aberrant Notch can even push hepatocytes toward a malignant biliary fate."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Cholangiocarcinoma builds an immunosuppressive niche with regulatory T cells: Tregs accumulate in its dense desmoplastic stroma and blunt anti-tumor immunity, helping explain why checkpoint therapy alone often disappoints in this cancer."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "Cholangiocarcinoma sits on the bile highway to the small intestine: bile normally drains into the duodenum, so the tumor blocks that flow, causing jaundice and fat malabsorption, and distal duct cancers arise where the duct meets the gut."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 stokes the inflammation that breeds cholangiocarcinoma: chronically inflamed bile ducts pour out IL-6, which via STAT3 pushes cholangiocytes to proliferate and resist death, linking conditions like PSC and fluke infection to the cancer."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Cholangiocarcinoma hides in a hypoxic, dense stroma: its thick desmoplastic tissue chokes off oxygen, and the resulting hypoxia drives survival signaling and blunts drug delivery, part of why this cancer resists chemotherapy."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "Cholangiocarcinoma near the duct's end involves the pancreas: distal tumors sit where the bile duct passes through the pancreatic head, so removing them requires a Whipple operation that takes part of the pancreas too."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Cholangiocarcinoma builds its blood supply through endothelial cells: VEGF from the tumor drives these vessel-lining cells to form new vasculature feeding the cancer, a target of anti-angiogenic therapy."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium-laden bile stones breed cholangiocarcinoma: intrahepatic stones (hepatolithiasis), rich in calcium and pigment, chronically inflame and obstruct the ducts, a recognized precursor to bile-duct cancer."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Cholangiocarcinoma is tied to the bowel: primary sclerosing cholangitis with inflammatory bowel disease is a major risk factor, linking colonic inflammation to cancer of the bile ducts."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Natural killer cells patrol the liver against cholangiocarcinoma: abundant in hepatic tissue, they can kill tumor cells, and boosting their dampened activity is an immunotherapy strategy against this resistant cancer."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β drives cholangiocarcinoma's dense scar: it activates fibroblasts to build the desmoplastic stroma that armors the tumor against drugs and immune cells, a hallmark of bile-duct cancer."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reads cholangiocarcinoma as a gland-maker: its cells form duct-like lumina with microvilli and secrete mucin, the adenocarcinoma ultrastructure embedded in the dense fibrous stroma that defines bile-duct cancer."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Cholangiocarcinoma spreads outward to the lung: beyond invading the liver it is around, the tumor metastasizes hematogenously to the lungs and bones, marking the advanced disease that surgery can no longer cure."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "The bile-duct cancer can seed the skeleton: bone metastases, reaching the marrow-filled vertebrae and pelvis, are a painful late manifestation of its hematogenous spread."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Immunotherapy and antibodies entered biliary cancer: adding the anti-PD-L1 antibody durvalumab to gemcitabine-cisplatin is now standard for advanced disease, and IHC antibody stains (CK7/CK19) help distinguish it from liver-cell cancer."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "The chemotherapy bites the nerves: the gemcitabine-cisplatin and oxaliplatin regimens used against cholangiocarcinoma injure peripheral sensory neurons, causing the tingling, numbness, and cold sensitivity of a platinum neuropathy."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Platinum chemotherapy drains magnesium: cisplatin injures the kidney's tubules so they waste the mineral, making magnesium monitoring and replacement part of biliary cancer treatment."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "The bile carries a microbial signal: gut and biliary bacteria reshape the bile-acid pool and fuel the chronic inflammation that promotes cholangiocarcinoma, a microbiome-bile-acid axis now studied as a driver and possible target in biliary cancer."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "Perihilar tumors can dam the portal vein: invasion or compression at the liver hilum raises portal pressure, enlarging the spleen and dropping platelet and white-cell counts through hypersplenism on top of the obstructive jaundice."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Biliary cancer is intensely pro-thrombotic: like other pancreatobiliary tumors it carries a high risk of venous thromboembolism, and paraneoplastic thrombocytosis often accompanies it and marks a worse outlook."
---

# Cholangiocarcinoma

## Overview

**Cholangiocarcinoma (CCA)** is a malignancy arising from the epithelial cells of the bile ducts and is the second most common primary liver cancer after hepatocellular carcinoma. CCA is classified by anatomical location into three subtypes with distinct molecular profiles, clinical behavior, and treatment: **intrahepatic CCA (iCCA, ~10-15%)**, arising from bile ducts within the liver parenchyma; **perihilar CCA (~50-60%)**, also called Klatskin tumor, arising at the biliary confluence (hepatic duct bifurcation); and **distal extrahepatic CCA (~25-30%)**, arising from the common bile duct distal to the cystic duct. Most patients present with unresectable or metastatic disease, yielding 5-year overall survival of <5% for advanced disease. The molecular revolution in iCCA — driven by discovery of **FGFR2 fusions** (~15-20%) and **IDH1 mutations** (~15-20%) as actionable targets — has transformed second-line treatment; the first-line immunotherapy addition (TOPAZ-1 trial: durvalumab + gemcitabine/cisplatin) represents the first major first-line advance in a decade [^abou-alfa-2020-claridy] [^oh-2022-topaz1].

**Epidemiology and risk factors:**
- Incidence: ~8,000 cases/year in the USA; rising incidence of iCCA; male > female (1.5:1); median age at diagnosis ~70 years
- **Primary sclerosing cholangitis (PSC):** Lifetime risk of CCA ~10-15%; PSC-associated CCA is often multifocal and early-onset; surveillance with CA 19-9 + MRCP annually
- **Liver flukes (Opisthorchis viverrini, Clonorchis sinensis):** Major risk factor in Southeast Asia (Thailand, Laos) and East Asia; WHO Group 1 carcinogens; fluke-associated CCA is predominantly iCCA and often occurs at younger age
- **Hepatitis B and C, cirrhosis:** RR ~2-3 for HBV/HCV-associated iCCA; viral hepatitis is a stronger risk factor for iCCA than perihilar/distal CCA
- **Biliary cysts (Caroli disease, choledochal cyst):** Lifetime risk of CCA ~10-30%; biliary-enteric drainage anomalies → bile stasis → malignant transformation
- **Primary biliary cholangitis:** Modest increased risk; distinguishable from PSC by anti-mitochondrial antibodies

**Molecular subtyping (especially iCCA):**
- FGFR2 fusions/rearrangements: ~15-20% of iCCA; multiple fusion partners (BICC1 most common); targetable with pemigatinib, futibatinib, infigratinib
- IDH1 mutations: ~15-20% of iCCA (R132C, R132L, R132G); targetable with ivosidenib; IDH2 mutations ~5% (not yet an approved target)
- KRAS mutations: ~10-20% of iCCA; ~30-40% of extrahepatic CCA; G12V most common in CCA; not yet standardly targetable
- BRAF V600E: ~5% of all CCA; targetable with dabrafenib + trametinib (tumor-agnostic; FDA 2022 basket approval)
- HER2 amplification/overexpression: ~5-10% of biliary tract cancers; trastuzumab deruxtecan (DESTINY-PanTumor02) and zanidatamab active
- NTRK fusions: Rare (<2%); tumor-agnostically targetable (larotrectinib, entrectinib)
- MSI-H/dMMR: ~2% of CCA; pembrolizumab (tumor-agnostic)
- ARID1A, BAP1, PBRM1 mutations: Common in iCCA; chromatin remodeling; not directly targetable

## Structure

### Anatomical subtypes and pathological features

**Intrahepatic CCA (iCCA):**
iCCA arises within the hepatic parenchyma from the second-order bile ducts or more peripheral radicles. Macroscopically: mass-forming (most common), periductal-infiltrating, and intraductal-growing subtypes. Mass-forming iCCA is a firm, pale, desmoplastic mass with satellite lesions. Microscopically: adenocarcinoma with glandular or tubular architecture; desmoplastic stroma; mucin production variable. IHC: CK7+, CK19+, CA19-9+; CK20 variably positive; Hep-1 and arginase-1 negative (distinguishes from HCC). AFP: typically negative (elevated in HCC, not CCA). Imaging: peripheral rim enhancement with progressive central fill-in on contrast CT/MRI; MRCP shows biliary anatomic relationship.

**Perihilar CCA (Klatskin tumor):**
Perihilar CCA originates at the hepatic duct bifurcation (confluence) → obstructs both right and left hepatic ducts → biliary obstruction → jaundice. Classified by Bismuth-Corlette system: Type I (below confluence), Type II (at confluence), Type III (involving one first-order duct), Type IV (bilateral first-order duct involvement). Periductal-infiltrating growth pattern predominates; small mass relative to obstruction → often missed on early imaging. EUS-guided or ERCP brushing for tissue diagnosis. ERCP with biliary stenting for drainage. CA 19-9 elevation (>100 U/mL has ~90% specificity in PSC patients).

**Distal extrahepatic CCA:**
Distal CCA arises in the common bile duct below the cystic duct insertion. Shares features with pancreatic head adenocarcinoma (adjacent anatomy, similar surgical management: Whipple procedure or pancreaticoduodenectomy). Distinguished from pancreatic head cancer by imaging and IHC (CCA: CK7+/CK19+/CA19-9+; pancreatic: similar, but SMAD4/DPC4 loss in ~50% of pancreatic vs rare in CCA).

### Biomarker testing in CCA

Per ESMO/ASCO guidelines, all unresectable/metastatic CCA should undergo:
- **Next-generation sequencing (NGS):** FGFR2 fusions (RNA-seq preferred for fusion detection), IDH1, KRAS, BRAF, NTRK, HER2; tumor mutational burden (TMB)
- **MSI/MMR testing:** IHC or PCR; MSI-H → pembrolizumab
- **PD-L1:** Not required for standard durvalumab/pembrolizumab + chemotherapy (benefit observed regardless of PD-L1)
- **FISH for FGFR2:** If NGS fails or inconclusive; RNA-based assay is gold standard for fusion detection

## Function

### Normal biliary epithelium physiology

Cholangiocytes (bile duct epithelial cells) line the intrahepatic and extrahepatic bile ducts and are responsible for: bile modification (addition of water and bicarbonate via CFTR and AE2 Cl⁻/HCO₃⁻ exchanger → "biliary bicarbonate umbrella" protecting cholangiocytes from bile acid toxicity); ductular bile secretion (~40% of total bile volume, rest from hepatocytes); hormone-responsive secretion (secretin via SSTR → cAMP → CFTR activation → ductal bile flow). Normal cholangiocyte turnover is slow (months); hepatocyte-to-cholangiocyte transdifferentiation occurs under conditions of severe ductal injury (ductular reaction in PSC, PBC).

**Oncogenic transformation pathway:**
Chronic biliary injury (from PSC, fluke infection, bile acid reflux, biliary stasis) → cholangiocyte inflammation → NF-κB/IL-6/STAT3 → proliferation → accumulated mutations (KRAS → RAF/MEK/ERK; IDH1/2 → 2-HG → epigenetic silencing; FGFR2 fusions → constitutive FGFR2 kinase) → escape from ductular senescence → invasive CCA.

## Pathology

### Diagnosis and staging

**Clinical presentation:**
- iCCA: Often asymptomatic until large; right upper quadrant pain, weight loss, jaundice (late); CA 19-9 elevation; incidentally found on liver imaging
- Perihilar/distal CCA: Painless obstructive jaundice is the presenting feature (dark urine, pale stools, pruritus); biliary obstruction on imaging; cholangitis if superinfected

**CA 19-9:** Elevated (>37 U/mL) in ~80% of CCA; not specific (also elevated in pancreatitis, biliary obstruction without cancer, benign biliary disease); combined with CEA or IgG4/autoimmune markers in PSC surveillance.

**Staging (AJCC 8th edition):**
- iCCA T1a: ≤5 cm, no vascular invasion; T1b: >5 cm, no vascular invasion; T2: vascular invasion or multifocal; T3: periductal invasion; T4: biliary, hepatic artery, or PV invasion; N1: regional nodes; M1: distant mets
- Perihilar CCA: Bismuth-Corlette modified + separate AJCC 8th; T3/T4 involve portal vein or hepatic artery → unresectable; hilar involvement → liver ± bile duct resection required
- Liver transplantation: Mayo protocol for perihilar CCA (stage T1/T2, lesion ≤3 cm, neoadjuvant chemoradiation) in PSC patients → 5-year OS ~70% in select centers

**Resectability criteria:**
- iCCA: Resectable if negative margins achievable with ≥20-25% residual liver volume; hilar involvement, bilateral duct involvement, vascular invasion = contraindications
- Adjuvant capecitabine: BILCAP trial (Primrose 2019): Capecitabine vs. observation after resection of biliary tract cancer → OS 53 vs 36 months (ITT, p=0.097; per protocol, significant) → standard of care post-resection in many centers despite borderline p-value

### Systemic treatment

**First-line advanced/metastatic:**
- **Gemcitabine + cisplatin (GemCis):** ABC-02 trial (Valle 2010, NEJM): OS 11.7 vs 8.1 months vs gemcitabine alone; established as first-line standard for a decade
- **GemCis + durvalumab (TOPAZ-1):** [^oh-2022-topaz1] OS 12.8 vs 11.5 months; HR 0.80; 2-year OS rate 24.9% vs 10.4%; FDA approved 2022; added to standard of care; PD-L1 status not required for selection
- **GemCis + pembrolizumab (KEYNOTE-966):** OS 12.7 vs 10.9 months; HR 0.83; FDA approved 2023; second PD-1/L1 + chemo regimen approved
- **FOLFOX:** Second-line after GemCis (ABC-06 trial: OS 6.2 vs 5.3 months); limited activity

**Second-line targeted (biomarker-selected):**
- **Pemigatinib (FGFR2 fusions, FDA 2020):** FIGHT-202: ORR 35.5%, mPFS 6.9 months, mOS 17.5 months; first approved targeted therapy in CCA
- **Futibatinib (FGFR2 fusions, FDA 2023):** FOENIX-CCA2: ORR 41.7%, mPFS 9.0 months; covalent FGFR1-4 inhibitor (vs. reversible pemigatinib)
- **Ivosidenib (IDH1 mutations, FDA 2021):** ClarIDHy: [^abou-alfa-2020-claridy] PFS 2.7 vs 1.4 months; OS 10.8 vs 9.7 months (crossover-adjusted); first IDH1-targeted CCA therapy
- **Dabrafenib + trametinib (BRAF V600E, FDA 2022 basket):** ORR ~50% in BRAF V600E CCA in basket trial
- **Larotrectinib/entrectinib (NTRK fusions, tumor-agnostic):** ORR ~75%; rare in CCA but highly active
- **Trastuzumab deruxtecan (HER2, DESTINY-PanTumor02):** ORR 22% in biliary tract cancers (IHC 2+/3+); activity in HER2-amplified CCA
- **Pembrolizumab (MSI-H/TMB-H, tumor-agnostic):** Standard of care for MSI-H CCA

**FGFR2 inhibitor resistance:**
- FGFR2 kinase domain secondary mutations (gatekeeper: V565I, N550 family): Acquired resistance; RLY-4008 (lirafugratinib) highly selective FGFR2 inhibitor active against secondary resistance mutations; ongoing Phase 2 (RAGNAR trial)
- PIK3CA/AKT/MAPK bypass: Alternative signaling → FGFR inhibitor escape

## Connections

- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — FGFR2 fusions/rearrangements in ~15-20% of iCCA; pemigatinib (FIGHT-202: ORR 36%, FDA 2020) and futibatinib (FOENIX-CCA2: ORR 42%, FDA 2023) are approved; FGFR2 inhibitors are the leading targeted therapy in iCCA; erdafitinib active in FGFR-altered CCA.
- `connects-to` → **[IDH1](../../03-molecular/idh1/README.md)** — IDH1 mutations in ~15-20% of iCCA; IDH1 R132C/L → 2-HG → TET2 inhibition → DNA hypermethylation; ivosidenib (ClarIDHy: PFS 2.7 vs 1.4 months) is FDA-approved for IDH1-mutant CCA; IDH2 mutations occur in ~5% of iCCA.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Durvalumab (PD-L1) + gemcitabine/cisplatin (TOPAZ-1: OS 12.8 vs 11.5 months, FDA 2022) is first-line for advanced CCA; pembrolizumab + gem/cis (KEYNOTE-966: OS 12.7 vs 10.9 months, FDA 2023) also approved; PD-L1 CPS predicts benefit.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — KRAS mutations in ~10-20% of iCCA and ~30-40% of extrahepatic CCA; KRAS G12C targetable with sotorasib/adagrasib (early data); KRAS mutations associate with poor prognosis; CCA is among the major RAS-driven GI cancers lacking standard targeted therapy.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Cholangiocarcinoma arises from cholangiocytes within or adjacent to the liver; iCCA is the 2nd most common primary liver cancer after HCC; PSC, HBV/HCV, and cirrhosis elevate CCA risk 2-3×; hepatic resection with negative margins is the only curative approach for iCCA.
- `connects-to` → **[BRAF](../../03-molecular/braf/README.md)** — BRAF V600E mutations in ~5% of all CCA; dabrafenib + trametinib (BRAF+MEK inhibition) approved tumor-agnostically (FDA 2022) with ~50% ORR in BRAF V600E CCA; BRAF V600E CCA responds similarly to BRAF-mutant melanoma/NSCLC; concomitant IDH or FGFR alterations are rare.
- `connects-to` → **[HER2](../../03-molecular/her2/README.md)** — HER2 amplification or overexpression in ~5-10% of biliary tract cancers; trastuzumab deruxtecan (DESTINY-PanTumor02) ORR 22% in HER2 IHC 2+/3+ BTC; zanidatamab active in HER2+ BTC; HER2 testing recommended in all advanced BTC per ESMO 2023 guidelines.
- `connects-to` → **[Gastric Cancer](../gastric-cancer/README.md)** — Cholangiocarcinoma and gastric cancer are both GI adenocarcinomas converging on shared targets — HER2, PD-1/PD-L1 blockade, and FGFR alterations — yet differ in origin: CCA from biliary cholangiocytes (FGFR2 fusions, IDH1), gastric cancer from stomach epithelium (H. pylori, EBV).
- `connects-to` → **[Hepatocellular Carcinoma](../hcc/README.md)** — Cholangiocarcinoma and hepatocellular carcinoma are the two primary liver cancers, distinguished by cell of origin — cholangiocytes versus hepatocytes; combined HCC-CCA tumors exist, both share cirrhosis and viral hepatitis as risks, but their targeted therapies differ entirely.
- `connects-to` → **[Pancreatic Cancer](../pancreatic-cancer/README.md)** — Cholangiocarcinoma and pancreatic cancer are pancreaticobiliary neighbors blending at the ampulla: distal CCA and pancreatic-head adenocarcinoma both cause painless obstructive jaundice, share KRAS-driven biology and the gemcitabine/cisplatin backbone, and carry grim outcomes.
- `connects-to` → **[Inflammatory Bowel Disease](../inflammatory-bowel-disease/README.md)** — Cholangiocarcinoma is the feared malignancy of inflammatory bowel disease via primary sclerosing cholangitis: PSC, strongly linked to ulcerative colitis, scars the bile ducts and carries a high lifetime risk of bile-duct cancer—so PSC-IBD patients need biliary surveillance.
- `connects-to` → **[Colorectal Cancer](../colorectal-cancer/README.md)** — Cholangiocarcinoma and colorectal cancer are both GI adenocarcinomas linked through PSC-IBD: ulcerative colitis with primary sclerosing cholangitis raises both colorectal and bile-duct cancer risk, and both can harbor actionable BRAF or mismatch-repair-deficient subtypes.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Cholangiocarcinoma is defined by its desmoplastic stroma: cancer-associated fibroblasts build a dense fibrous matrix that surrounds the tumor, supplies growth and survival signals, and physically impedes drug delivery—one reason this bile-duct cancer is so chemoresistant.
- `connects-to` → **[IDH-Mutant Glioma](../idh-mutant-glioma/README.md)** — Cholangiocarcinoma and IDH-mutant glioma are united by IDH1 mutation and the oncometabolite 2-HG: ~15-20% of intrahepatic cholangiocarcinomas carry IDH1 R132, and ivosidenib—first for IDH-mutant leukemia and glioma—now treats IDH1-mutant cholangiocarcinoma.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — Cholangiocarcinoma arises from biliary epithelium, not hepatocytes, distinguishing it from HCC: it springs from cholangiocytes lining bile ducts, so it lacks AFP and hepatocyte markers and expresses biliary cytokeratins—a key distinction for a liver mass.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Cholangiocarcinoma is mostly immunologically cold but responds in a subset: a dense desmoplastic, immunosuppressive stroma keeps cytotoxic T cells out, yet mismatch-repair-deficient or PD-L1-high tumors respond to checkpoint blockade now added to chemotherapy first-line.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 mutation is common in cholangiocarcinoma: loss of p53, alongside KRAS and FGFR/IDH alterations, removes a key checkpoint in bile-duct epithelium, so chronic inflammation plus p53 loss drives the malignant transformation behind this hard-to-treat cancer.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — A macrophage-rich desmoplastic stroma defines cholangiocarcinoma: tumor-associated macrophages and fibroblasts build a dense, immunosuppressive matrix that walls the tumor off, helping explain its chemoresistance and limited response to immunotherapy.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Cholangiocarcinoma relies on VEGF-driven angiogenesis: the tumor secretes VEGF to vascularize its desmoplastic mass, high levels predict worse outcome, and anti-angiogenic agents are studied alongside the chemotherapy and targeted FGFR/IDH inhibitors used in treatment.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Cholangiocarcinoma arises from chronically inflamed, fibrotic bile ducts: primary sclerosing cholangitis, liver fluke and stones scar the biliary tree, and this fibrosis-inflammation milieu is the soil in which the cancer develops—mirroring HCC arising in cirrhosis.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Radiotherapy has a role in cholangiocarcinoma: photon-based external-beam or stereotactic radiation, often with chemo, treats unresectable bile-duct tumors and the perihilar disease that obstructs the ducts—palliating jaundice and sometimes downstaging for surgery.
- `connects-to` → **[Hepatitis C](../hepatitis-c/README.md)** — Hepatitis C is a recognized risk factor for cholangiocarcinoma: chronic viral inflammation and the cirrhosis it causes raise the risk of intrahepatic bile-duct cancer as well as HCC, so the two primary liver cancers share this viral driver.
- `connects-to` → **[Hepatitis B](../hepatitis-b/README.md)** — Hepatitis B raises cholangiocarcinoma risk: chronic HBV inflames the liver and bile ducts, and like its link to hepatocellular cancer, the virus is an established risk factor for intrahepatic bile-duct cancer—so viral hepatitis spans both primary liver cancers.
- `connects-to` → **[NASH](../nash/README.md)** — Fatty liver disease is a rising cause of cholangiocarcinoma: NASH-driven inflammation and fibrosis increasingly underlie intrahepatic bile-duct cancer, so the metabolic epidemic is expanding a tumor once tied mainly to flukes and bile-duct disease.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Cholangiocarcinoma grows out of chronic biliary inflammation: neutrophils and other immune cells in inflamed, infected, or stone-laden bile ducts release IL-6 and reactive species that drive the DNA damage transforming cholangiocytes—inflammation as carcinogen.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Cholangiocarcinoma arises amid copper-retaining cholestasis: the liver normally excretes copper into bile, so blocked or inflamed ducts trap copper in the liver—a marker of the chronic cholestasis (as in PSC) that breeds this bile-duct cancer.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — Cholangiocarcinoma reactivates Notch signaling: the pathway that tells liver progenitors to become bile-duct cells is hijacked to drive tumor formation, so aberrant Notch can even push hepatocytes toward a malignant biliary fate.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Cholangiocarcinoma builds an immunosuppressive niche with regulatory T cells: Tregs accumulate in its dense desmoplastic stroma and blunt anti-tumor immunity, helping explain why checkpoint therapy alone often disappoints in this cancer.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — Cholangiocarcinoma sits on the bile highway to the small intestine: bile normally drains into the duodenum, so the tumor blocks that flow, causing jaundice and fat malabsorption, and distal duct cancers arise where the duct meets the gut.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6 stokes the inflammation that breeds cholangiocarcinoma: chronically inflamed bile ducts pour out IL-6, which via STAT3 pushes cholangiocytes to proliferate and resist death, linking conditions like PSC and fluke infection to the cancer.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Cholangiocarcinoma hides in a hypoxic, dense stroma: its thick desmoplastic tissue chokes off oxygen, and the resulting hypoxia drives survival signaling and blunts drug delivery, part of why this cancer resists chemotherapy.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — Cholangiocarcinoma near the duct's end involves the pancreas: distal tumors sit where the bile duct passes through the pancreatic head, so removing them requires a Whipple operation that takes part of the pancreas too.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Cholangiocarcinoma builds its blood supply through endothelial cells: VEGF from the tumor drives these vessel-lining cells to form new vasculature feeding the cancer, a target of anti-angiogenic therapy.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium-laden bile stones breed cholangiocarcinoma: intrahepatic stones (hepatolithiasis), rich in calcium and pigment, chronically inflame and obstruct the ducts, a recognized precursor to bile-duct cancer.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Cholangiocarcinoma is tied to the bowel: primary sclerosing cholangitis with inflammatory bowel disease is a major risk factor, linking colonic inflammation to cancer of the bile ducts.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Natural killer cells patrol the liver against cholangiocarcinoma: abundant in hepatic tissue, they can kill tumor cells, and boosting their dampened activity is an immunotherapy strategy against this resistant cancer.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-β drives cholangiocarcinoma's dense scar: it activates fibroblasts to build the desmoplastic stroma that armors the tumor against drugs and immune cells, a hallmark of bile-duct cancer.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reads cholangiocarcinoma as a gland-maker: its cells form duct-like lumina with microvilli and secrete mucin, the adenocarcinoma ultrastructure embedded in the dense fibrous stroma that defines bile-duct cancer.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Cholangiocarcinoma spreads outward to the lung: beyond invading the liver it is around, the tumor metastasizes hematogenously to the lungs and bones, marking the advanced disease that surgery can no longer cure.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — The bile-duct cancer can seed the skeleton: bone metastases, reaching the marrow-filled vertebrae and pelvis, are a painful late manifestation of its hematogenous spread.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Immunotherapy and antibodies entered biliary cancer: adding the anti-PD-L1 antibody durvalumab to gemcitabine-cisplatin is now standard for advanced disease, and IHC antibody stains (CK7/CK19) help distinguish it from liver-cell cancer.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — The chemotherapy bites the nerves: the gemcitabine-cisplatin and oxaliplatin regimens used against cholangiocarcinoma injure peripheral sensory neurons, causing the tingling, numbness, and cold sensitivity of a platinum neuropathy.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Platinum chemotherapy drains magnesium: cisplatin injures the kidney's tubules so they waste the mineral, making magnesium monitoring and replacement part of biliary cancer treatment.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — The bile carries a microbial signal: gut and biliary bacteria reshape the bile-acid pool and fuel the chronic inflammation that promotes cholangiocarcinoma, a microbiome-bile-acid axis now studied as a driver and possible target in biliary cancer.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — Perihilar tumors can dam the portal vein: invasion or compression at the liver hilum raises portal pressure, enlarging the spleen and dropping platelet and white-cell counts through hypersplenism on top of the obstructive jaundice.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Biliary cancer is intensely pro-thrombotic: like other pancreatobiliary tumors it carries a high risk of venous thromboembolism, and paraneoplastic thrombocytosis often accompanies it and marks a worse outlook.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^abou-alfa-2020-claridy]: Abou-Alfa GK, Macarulla T, Javle MM, et al. Ivosidenib in IDH1-mutant, chemotherapy-refractory cholangiocarcinoma (ClarIDHy). *Lancet Oncol.* 2020;21(6):796-807. [doi:10.1016/S1470-2045(20)30157-1](https://doi.org/10.1016/S1470-2045(20)30157-1) · [PubMed 32416072](https://pubmed.ncbi.nlm.nih.gov/32416072/)
[^oh-2022-topaz1]: Oh DY, He AR, Qin S, et al. Durvalumab plus Gemcitabine and Cisplatin in Biliary Tract Cancer. *NEJM Evidence.* 2022;1(8):EVIDoa2200015. [doi:10.1056/EVIDoa2200015](https://doi.org/10.1056/EVIDoa2200015) · [PubMed 38319282](https://pubmed.ncbi.nlm.nih.gov/38319282/)
