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
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy confirms a tumor is liver-born: HCC cells still make bile, retain canaliculi between them, and trap Mallory-Denk bodies and fat — ultrastructure that betrays hepatocyte origin when a metastasis must be ruled out."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Copper overload can end in liver cancer: untreated Wilson disease loads the liver with copper until it cirrhoses, and the chronic injury and scarring raise the long-term risk of hepatocellular carcinoma."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "HCC plays both ways with platelets: it can drive a paraneoplastic thrombocytosis via thrombopoietin, yet the underlying cirrhosis often leaves platelets low — and tumor invasion of the portal vein seeds dangerous clots."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "HCC arises on a failing liver that poisons the brain: as cirrhosis and tumor crowd out function, ammonia builds up to cloud neurons into hepatic encephalopathy — confusion, asterixis, and at worst coma."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "HCC can thicken the blood paradoxically: despite arising in a failing liver, it sometimes secretes erythropoietin ectopically, driving a paraneoplastic erythrocytosis of excess red cells."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "HCC can spike the blood calcium: a paraneoplastic hypercalcemia from tumor-secreted PTHrP appears in some patients, causing confusion, constipation, and thirst independent of any bone metastasis."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies screen and treat HCC: the AFP blood marker is read by immunoassay to flag and follow tumors, and atezolizumab with the anti-VEGF antibody bevacizumab is now first-line immunotherapy for advanced disease."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "The blood count forecasts the course: a high neutrophil-to-lymphocyte ratio predicts poorer survival in HCC, reflecting the tumor-promoting inflammation of the chronically injured, cirrhotic liver it grows in."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "HCC is a man's cancer, and androgens are why: it strikes men two-to-four times more often, testosterone signaling promotes its growth, and anabolic-steroid abuse can itself spawn hepatic tumors."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "The scar-making cell sets the stage for cancer: activated hepatic stellate cells and cancer-associated fibroblasts lay down the fibrosis that precedes HCC and then build the tumor stroma that shelters and feeds it."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β plays both fibrosis and tumor: it drives the stellate-cell scarring that breeds HCC, then in the tumor switches to promoting invasion and suppressing the immune attack, a dual role that makes it a therapeutic target."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "A mold's toxin scars its signature into the genome: Aspergillus growing on stored grain makes aflatoxin, which causes the hallmark p53 R249S mutation, a major driver of HCC where contamination and hepatitis B overlap."
  - target: 01-human/03-molecular/ctnnb1
    relation: connects-to
    note: "One subclass runs on Wnt: activating CTNNB1 (β-catenin) mutations define a major group of liver cancers — and these tumors are typically immune-cold, resisting the checkpoint immunotherapy that helps other HCCs."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Reawakening the immune attack is the new strategy: dendritic cells must present tumor antigens to mount the T-cell response that atezolizumab-bevacizumab unleashes, the immunotherapy that reshaped advanced HCC treatment."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "It famously invades the veins: HCC has a strong tendency to grow into the portal and hepatic veins and to provoke cancer-associated venous thromboembolism, complicating both staging and anticoagulation decisions."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6 drives the inflamed liver to cancer through STAT3: chronic hepatitis raises IL-6, whose STAT3 signaling pushes hepatocyte survival and proliferation — a central link from inflammation to hepatocellular carcinoma."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "The cirrhotic liver beneath it invites infection: most HCC arises in cirrhosis, where impaired immunity and bacterial translocation make spontaneous bacterial peritonitis and sepsis frequent, life-threatening events."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Chronic liver disease and cancer blunt the marrow: the inflammation of HCC and its underlying cirrhosis raises hepcidin and cytokines that suppress erythropoiesis, layering an anemia of chronic disease onto any bleeding or hypersplenism."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "The failing liver drags the kidney down: advanced HCC and its cirrhosis precipitate hepatorenal syndrome, and the VEGF-targeted kinase inhibitors used to treat it add nephrotoxicity, together threatening chronic kidney disease."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "Its targeted drugs spike the pressure: the antiangiogenic kinase inhibitors sorafenib and lenvatinib, mainstays of advanced HCC therapy, cause prominent hypertension as an on-target VEGF-pathway effect."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Cancer atop chronic liver disease weighs on mood: a poor-prognosis diagnosis layered on the fatigue and stigma of cirrhosis and viral hepatitis gives HCC a substantial burden of depression."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Its targeted drugs strain the heart: the multikinase inhibitors sorafenib and lenvatinib used for advanced HCC raise blood pressure and are cardiotoxic, capable of precipitating heart failure."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Cirrhosis behind it weakens bone: the impaired vitamin D metabolism and hepatic osteodystrophy of the cirrhosis that underlies most HCC — compounded by post-transplant steroids — drive bone loss."
  - target: 01-human/07-system/type-1-diabetes
    relation: connects-to
    note: "Its checkpoint immunotherapy can trigger autoimmune diabetes: the PD-L1 inhibitor atezolizumab used for advanced HCC can unleash autoimmunity against pancreatic islets, causing insulin-dependent diabetes."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It is a cancer of a digestive organ on a failing one: HCC almost always arises in a cirrhotic liver, so portal hypertension, oesophageal varices and ascites dominate its course alongside the tumour."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "A failing tumour-bearing liver poisons the brain: as the cirrhosis underlying HCC decompensates, ammonia and toxins it can no longer clear accumulate, producing hepatic encephalopathy with confusion and coma."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A grim cancer watched on a sick liver breeds worry: the poor prognosis, surveillance imaging and decompensation risk of HCC on cirrhosis foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It spreads first to the lungs: the lungs are the commonest site of extrahepatic metastasis in hepatocellular carcinoma, appearing as nodules on staging and follow-up imaging."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It makes hormones it shouldn't: HCC causes paraneoplastic hypoglycaemia from IGF-II, erythrocytosis from erythropoietin and hypercalcaemia from PTHrP."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "It grows into the great veins: HCC characteristically invades the hepatic vein and inferior vena cava, with tumour thrombus that can extend into the right atrium."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It spreads to bone and wastes muscle: HCC commonly metastasises to the skeleton with painful lytic lesions, while the sarcopenia of cirrhosis erodes muscle and worsens prognosis."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "A failing liver drags down the kidney: advanced HCC and its cirrhosis precipitate hepatorenal syndrome, a functional kidney failure driven by splanchnic vasodilation."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "The skin betrays the diseased liver: jaundice, intractable cholestatic pruritus and the spider naevi of cirrhosis accompany HCC, and HCV-related disease can bring porphyria cutanea tarda."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Immunotherapy now leads first-line care: atezolizumab (anti-PD-L1) with bevacizumab, and dual nivolumab-ipilimumab, have overtaken kinase inhibitors as first-line treatment for advanced hepatocellular carcinoma."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Multikinase inhibitors target its vasculature: sorafenib and lenvatinib block VEGFR and other kinases to slow advanced HCC, with cabozantinib and regorafenib used after progression."
  - target: 02-pathogen/01-viruses/hepatitis-b-virus
    relation: connects-to
    note: "The leading global cause: chronic hepatitis B drives most hepatocellular carcinoma worldwide, integrating into the genome and causing cancer even without cirrhosis, which vaccination now prevents."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Systemically chemoresistant, locoregionally treated: HCC responds poorly to conventional systemic chemotherapy, so treatment relies on TACE — delivering doxorubicin or cisplatin directly into the tumour's hepatic-arterial supply — plus targeted and immune therapy."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "It grows out of the cirrhotic lobule: hepatocellular carcinoma arises within the disturbed architecture of the cirrhotic liver, where regenerative nodules become dysplastic and then malignant, distorting the normal hepatic lobule."
  - target: 03-medicine/01-modern/04-cardio/aspirin
    relation: connects-to
    note: "Aspirin may lower its risk: regular aspirin use is associated with reduced hepatocellular carcinoma incidence in chronic viral hepatitis and metabolic liver disease, studied as chemoprevention through anti-inflammatory and antiplatelet effects."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Where it spreads: the lung is the commonest site of extrahepatic HCC metastasis, tumour emboli lodging in the alveolar capillary bed to seed pulmonary nodules."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Why it is so vascular: hypoxia stabilises HIF-1alpha, which drives the VEGF-fuelled angiogenesis behind HCC's brisk arterial enhancement on imaging and the rationale for anti-angiogenic therapy."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Hepatorenal syndrome: advanced HCC and its underlying cirrhosis cause functional kidney failure through splanchnic vasodilation and renal vasoconstriction—the kidney failing though structurally intact."
  - target: 01-human/07-system/uveal-melanoma
    relation: connects-to
    note: "Liver-directed therapy unites them: like hepatocellular carcinoma, liver-confined uveal melanoma metastases are treated with hepatic perfusion, radioembolization and resection—both cancers managed by targeting the liver."
  - target: 01-human/07-system/polycythemia-vera
    relation: connects-to
    note: "Paraneoplastic erythrocytosis: HCC can secrete erythropoietin, raising the red-cell mass—an acquired, tumour-driven polycythaemia distinct from the JAK2-driven polycythaemia vera."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Bone metastasis: though it spreads mainly within the liver and to the lung, HCC also metastasises to bone, producing painful, often osteolytic lesions in the cortical bone."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "A hypervascular tumour: HCC's intense arterial neovascularity from HIF and VEGF underlies its diagnostic arterial-phase enhancement, trans-arterial chemoembolisation (TACE) and antiangiogenic therapy."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "Portopulmonary hypertension: the cirrhosis and portal hypertension that breed HCC can also drive pulmonary arterial hypertension, a complication that critically affects liver-transplant candidacy."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "The focal-liver-lesion differential: the liver is the dominant metastatic site for colorectal cancer, so a liver mass raises HCC in a cirrhotic but metastasis in others—distinguishing primary from secondary is pivotal."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Amplified oncogene: MYC amplification is a frequent driver of hepatocellular carcinoma, fuelling the ribosome biogenesis and proliferation that mark its more aggressive tumours."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K/AKT survival: AKT activation, often through PTEN loss, cooperates with mTOR to drive HCC growth and survival, part of the pathway exploited by targeted and combination therapy."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Cell-cycle drive: cyclin D1, often amplified downstream of Wnt/β-catenin signalling, pushes hepatocytes through the G1 checkpoint to drive the proliferation of hepatocellular carcinoma."
  - target: 01-human/03-molecular/met
    relation: connects-to
    note: "Invasive RTK: c-MET signalling drives HCC proliferation, invasion and angiogenesis, and is one of the kinases blocked by the multi-target inhibitor cabozantinib used in advanced disease."
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "FGF19-FGFR4 axis: amplification of the FGF19-FGFR4 signalling axis defines a subset of hepatocellular carcinomas and is a targetable driver under investigation with selective FGFR4 inhibitors."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Immunosuppressive niche: CCL2 secreted by HCC recruits tumour-associated macrophages and myeloid-derived suppressor cells, building the immunosuppressive microenvironment that blunts response to immunotherapy."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "Chromatin-remodeler driver: inactivating mutations in the SWI/SNF subunit ARID1A are recurrent in hepatocellular carcinoma, disrupting chromatin regulation of tumour-suppressor and differentiation genes."
  - target: 01-human/03-molecular/axl-receptor
    relation: connects-to
    note: "Invasion and resistance: GAS6-AXL signalling promotes the epithelial-mesenchymal transition and invasion of HCC and drives resistance to sorafenib and immunotherapy, an emerging combination target."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Gut-liver carcinogenesis: gut-derived LPS reaching the cirrhotic liver via the portal vein activates TLR4 on Kupffer cells, sustaining the inflammation that promotes hepatocarcinogenesis on a background of chronic liver disease."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Immunogenic instability: the chromosomal instability of HCC generates cytosolic DNA that activates cGAS-STING, part of the innate-immune context behind the responses to atezolizumab-bevacizumab and other checkpoint-based regimens now standard in advanced disease."
  - target: 01-human/03-molecular/androgen-receptor
    relation: connects-to
    note: "Male predominance: hepatocellular carcinoma is two-to-four times commoner in men, and androgen-receptor signalling promotes hepatocarcinogenesis, a hormonal contributor to the striking sex bias of the disease beyond differences in risk-factor exposure."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Iron-overload carcinogenesis: hepatic iron loading — in hereditary haemochromatosis and dysmetabolic overload — generates oxidative stress that drives hepatocarcinogenesis, with hepcidin dysregulation central to the iron accumulation that raises HCC risk."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Sorafenib pathway: the RAF-MEK-ERK MAPK cascade is a key proliferative pathway in hepatocellular carcinoma and the target of the multikinase inhibitor sorafenib, a backbone of systemic HCC therapy."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K survival axis: PI3K-AKT-mTOR signalling (AKT and mTOR already mapped) is recurrently activated in HCC, supporting growth and providing a resistance route to anti-angiogenic therapy."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Stromal angiogenesis: PDGF signalling drives the tumour stroma and angiogenesis of HCC, a target of the lenvatinib and regorafenib multikinase inhibitors used in its treatment."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Oxidative-stress oncogenesis: recurrent NFE2L2/KEAP1 mutations constitutively activate NRF2 in HCC, conferring antioxidant and metabolic advantages that promote hepatocyte survival and tumour progression on a background of chronic liver oxidative injury."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Inflammation-driven cancer: TLR-MyD88-NF-κB signalling, fuelled by gut-derived microbial products reaching the injured liver, sustains the chronic inflammation that links cirrhosis to hepatocarcinogenesis (TLR4 and NF-κB already mapped)."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Invasion and prognosis: osteopontin is overexpressed in HCC, promoting tumour-cell invasion, metastasis, and angiogenesis, and serving as a circulating biomarker of aggressive disease and poor prognosis."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β mapped) plays a dual tumour-suppressive and pro-invasive role in hepatocellular carcinoma, with SMAD4 loss promoting progression."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "IL-6-JAK-STAT3 signalling (IL-6 and STAT3 mapped) links chronic hepatic inflammation to the proliferation and survival of hepatocellular carcinoma."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "CDKN2A silencing releases CDK4/6-cyclin-D control (cyclin-D1 mapped) of the cell cycle, a recurrent epigenetic lesion in hepatocellular carcinoma."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 supports immune evasion and the metastatic progression of hepatocellular carcinoma."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the antitumour immune response of hepatocellular carcinoma, relevant to its checkpoint-immunotherapy responsiveness."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "EZH2-mediated polycomb repression silences tumour-suppressor genes and drives the epigenetic dysregulation of hepatocellular carcinoma."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "PI3K-AKT-mTOR-driven FOXO inactivation (AKT, PIK3CA, and mTOR already mapped) removes a pro-apoptotic brake, favoring hepatocyte survival in hepatocellular carcinoma."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6 acting on the cyclin-D1-RB axis (cyclin-D1 and CDKN2A already mapped) drives the cell-cycle progression of hepatocellular carcinoma."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-delivered cytotoxic killing by CD8 T and NK cells mediates the immune clearance that the checkpoint-immunotherapy-treated hepatocellular carcinoma must evade."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β regulates β-catenin stability (CTNNB1/Wnt already mapped), the axis frequently activated in hepatocellular carcinoma."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in hepatocellular carcinoma."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins from the chronically inflamed, cirrhotic liver shape the tumor-promoting microenvironment of hepatocellular carcinoma."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of MET and AXL (both already mapped) drives the invasion of hepatocellular carcinoma."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of hepatocellular carcinoma."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival and therapy resistance of hepatocellular carcinoma cells."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the hepatocyte metabolic reprogramming of hepatocellular carcinoma."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the immunosuppressive microenvironment of hepatocellular carcinoma."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the tumor angiogenesis and leukocyte trafficking of hepatocellular carcinoma."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment of hepatocellular carcinoma."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of hepatocellular carcinoma."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory tumor microenvironment of hepatocellular carcinoma."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immunotherapy: the checkpoint-inhibitor combination atezolizumab-bevacizumab is now first-line for advanced hepatocellular carcinoma, and MHC class II antigen presentation shapes the T-cell response that determines immunotherapy benefit."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Male predominance: hepatocellular carcinoma is far more common in men, and estrogen is thought to protect the female liver by dampening IL-6-driven inflammation (androgen receptor already mapped), contributing to the sex difference in incidence."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Growth-factor axis: reactivation of IGF-2 and IGF-1R signalling is common in hepatocellular carcinoma, driving proliferation and survival, and links the tumour to the metabolic and NASH pathways that increasingly cause it."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Cirrhotic field: most hepatocellular carcinoma arises in cirrhosis, the collagen scarring laid down by activated stellate cells (TGF-beta and PDGF already mapped), and the degree of this fibrosis governs both cancer risk and treatment tolerance."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Immunotherapy: IL-2-driven T-cell responses underlie the checkpoint immunotherapy (PD-1 and CTLA-4 already mapped) that, with anti-VEGF, is now first-line for advanced hepatocellular carcinoma, reflecting its immunogenic biology."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Bleeding and anaemia: hepatocellular carcinoma on cirrhosis causes variceal and tumour bleeding, and the anaemia of chronic liver disease (hepcidin already mapped) lowers haemoglobin, both contributing to the morbidity of advanced disease."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive microenvironment: IL-10 in the tumour microenvironment dampens the anti-tumour T-cell response (PD-1 and CD8 already mapped), part of the immune evasion that shapes the response to the checkpoint immunotherapy of hepatocellular carcinoma."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Portal hypertension and vasculature: dysregulated nitric oxide drives the splanchnic vasodilation and portal hypertension of the underlying cirrhosis, and with VEGF (already mapped) shapes the vasculature of the hypervascular hepatocellular carcinoma."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative hepatocarcinogenesis: the chronic inflammation and iron overload (hepcidin already mapped) of the diseased liver generate reactive oxygen species, to which xanthine oxidase contributes, driving the oxidative DNA damage of hepatocellular carcinogenesis."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises the Kupffer cells and tumour-associated macrophages (already mapped) toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the tolerogenic liver microenvironment of hepatocellular carcinoma."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Adipokine hepatocarcinogenesis: leptin, rising in the obesity and NASH (already mapped) that increasingly cause hepatocellular carcinoma, promotes hepatocyte proliferation and the fibro-inflammatory (TGF-β already mapped) drive of the tumour."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "COX-2 inflammation: prostaglandins from cyclooxygenase-2 in the chronically inflamed cirrhotic liver (IL-6 already mapped) promote the proliferation and angiogenesis of hepatocellular carcinoma, part of the inflammation-cancer link."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune milieu: IL-13, with IL-4 (already mapped), supports the M2 macrophage (already mapped) immunosuppressive milieu of hepatocellular carcinoma that limits the checkpoint immunotherapy."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Hepatoprotective adipokine: the fall in adiponectin, a hepatoprotective adipokine (leptin already mapped), with obesity and NASH (already mapped) removes a brake on the hepatocarcinogenesis of hepatocellular carcinoma."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Copper and hepatocarcinogenesis: the hepatic copper overload of Wilson's disease raises the HCC risk, and copper's role in angiogenesis (VEGF already mapped) and oxidative injury contributes to the cirrhotic-liver carcinogenesis."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Cirrhotic stellate cells: the activated hepatic stellate cells (myofibroblasts; TGF-β and PDGF already mapped) drive the cirrhosis (collagen already mapped) that is the field for the hepatocellular carcinoma."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Checkpoint immunity: the cytotoxic T cells (perforin and PD-1 already mapped) are unleashed by the atezolizumab (PD-L1) in the immunotherapy of hepatocellular carcinoma."
  - target: 01-human/07-system/hepatitis-c
    relation: connects-to
    note: "Viral cause: the chronic hepatitis C is a leading cause of HCC (via the cirrhosis), the DAA cure reducing but not eliminating the risk."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity exploited by the checkpoint (PD-1 already mapped) immunotherapy of hepatocellular carcinoma."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response of the hepatocellular-carcinoma immune microenvironment."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "NASH-metabolic adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the NASH (already mapped) metabolic milieu that drives hepatocellular carcinoma."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of hepatocellular carcinoma."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the tumour-promoting inflammation of hepatocellular carcinoma."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the hepatocellular-carcinoma microenvironment."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of hepatocellular carcinoma."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune balance of the hepatocellular-carcinoma microenvironment."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Tertiary lymphoid structures: the B cells organise the intratumoural tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, associates with the immunotherapy (PD-1 already mapped) response of hepatocellular carcinoma."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Tumour complement: the complement C3, produced by the hepatocytes and within the tumour, contributes to the inflammatory and immunosuppressive dimension of the hepatocellular-carcinoma microenvironment."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid (macrophage already mapped) recruitment and immunosuppression of the hepatocellular-carcinoma microenvironment."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Hepatic iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the hepatic iron overload that promotes the oxidative carcinogenesis of hepatocellular carcinoma."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-tumour axis: TSLP, from cancer-associated fibroblasts (already mapped) and the cirrhotic stroma (liver already mapped), primes dendritic cells (already mapped) and mast cells (already mapped) toward the Th2 immunosuppressive bias of the HCC microenvironment."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-tumour axis: bradykinin, via the kallikrein-kinin system in the cirrhotic and tumour microenvironment, amplifies the vascular permeability and the myeloid (macrophage already mapped) recruitment in hepatocellular carcinoma."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Anaemia of cancer: erythropoietin corrects the cancer-related anaemia (hepcidin already mapped) of hepatocellular carcinoma; EpoR expression on hepatoma cells also modulates a potential direct proliferative signal."
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
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy confirms a tumor is liver-born: HCC cells still make bile, retain canaliculi between them, and trap Mallory-Denk bodies and fat — ultrastructure that betrays hepatocyte origin when a metastasis must be ruled out.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Copper overload can end in liver cancer: untreated Wilson disease loads the liver with copper until it cirrhoses, and the chronic injury and scarring raise the long-term risk of hepatocellular carcinoma.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — HCC plays both ways with platelets: it can drive a paraneoplastic thrombocytosis via thrombopoietin, yet the underlying cirrhosis often leaves platelets low — and tumor invasion of the portal vein seeds dangerous clots.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — HCC commonly spreads to the adrenal glands: after the lungs, the adrenals are among its favored metastatic sites, so imaging of these glands is part of staging advanced liver cancer.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — HCC arises on a failing liver that poisons the brain: as cirrhosis and tumor crowd out function, ammonia builds up to cloud neurons into hepatic encephalopathy — confusion, asterixis, and at worst coma.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — HCC can thicken the blood paradoxically: despite arising in a failing liver, it sometimes secretes erythropoietin ectopically, driving a paraneoplastic erythrocytosis of excess red cells.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — HCC can spike the blood calcium: a paraneoplastic hypercalcemia from tumor-secreted PTHrP appears in some patients, causing confusion, constipation, and thirst independent of any bone metastasis.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies screen and treat HCC: the AFP blood marker is read by immunoassay to flag and follow tumors, and atezolizumab with the anti-VEGF antibody bevacizumab is now first-line immunotherapy for advanced disease.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — The blood count forecasts the course: a high neutrophil-to-lymphocyte ratio predicts poorer survival in HCC, reflecting the tumor-promoting inflammation of the chronically injured, cirrhotic liver it grows in.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — HCC is a man's cancer, and androgens are why: it strikes men two-to-four times more often, testosterone signaling promotes its growth, and anabolic-steroid abuse can itself spawn hepatic tumors.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — The scar-making cell sets the stage for cancer: activated hepatic stellate cells and cancer-associated fibroblasts lay down the fibrosis that precedes HCC and then build the tumor stroma that shelters and feeds it.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-β plays both fibrosis and tumor: it drives the stellate-cell scarring that breeds HCC, then in the tumor switches to promoting invasion and suppressing the immune attack, a dual role that makes it a therapeutic target.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — A mold's toxin scars its signature into the genome: Aspergillus growing on stored grain makes aflatoxin, which causes the hallmark p53 R249S mutation, a major driver of HCC where contamination and hepatitis B overlap.
- `connects-to` → **[CTNNB1](../../03-molecular/ctnnb1/README.md)** — One subclass runs on Wnt: activating CTNNB1 (β-catenin) mutations define a major group of liver cancers — and these tumors are typically immune-cold, resisting the checkpoint immunotherapy that helps other HCCs.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Reawakening the immune attack is the new strategy: dendritic cells must present tumor antigens to mount the T-cell response that atezolizumab-bevacizumab unleashes, the immunotherapy that reshaped advanced HCC treatment.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — It famously invades the veins: HCC has a strong tendency to grow into the portal and hepatic veins and to provoke cancer-associated venous thromboembolism, complicating both staging and anticoagulation decisions.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6 drives the inflamed liver to cancer through STAT3: chronic hepatitis raises IL-6, whose STAT3 signaling pushes hepatocyte survival and proliferation — a central link from inflammation to hepatocellular carcinoma.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — The cirrhotic liver beneath it invites infection: most HCC arises in cirrhosis, where impaired immunity and bacterial translocation make spontaneous bacterial peritonitis and sepsis frequent, life-threatening events.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Chronic liver disease and cancer blunt the marrow: the inflammation of HCC and its underlying cirrhosis raises hepcidin and cytokines that suppress erythropoiesis, layering an anemia of chronic disease onto any bleeding or hypersplenism.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — The failing liver drags the kidney down: advanced HCC and its cirrhosis precipitate hepatorenal syndrome, and the VEGF-targeted kinase inhibitors used to treat it add nephrotoxicity, together threatening chronic kidney disease.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — Its targeted drugs spike the pressure: the antiangiogenic kinase inhibitors sorafenib and lenvatinib, mainstays of advanced HCC therapy, cause prominent hypertension as an on-target VEGF-pathway effect.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Cancer atop chronic liver disease weighs on mood: a poor-prognosis diagnosis layered on the fatigue and stigma of cirrhosis and viral hepatitis gives HCC a substantial burden of depression.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Its targeted drugs strain the heart: the multikinase inhibitors sorafenib and lenvatinib used for advanced HCC raise blood pressure and are cardiotoxic, capable of precipitating heart failure.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Cirrhosis behind it weakens bone: the impaired vitamin D metabolism and hepatic osteodystrophy of the cirrhosis that underlies most HCC — compounded by post-transplant steroids — drive bone loss.
- `connects-to` → **[Type 1 Diabetes](../type-1-diabetes/README.md)** — Its checkpoint immunotherapy can trigger autoimmune diabetes: the PD-L1 inhibitor atezolizumab used for advanced HCC can unleash autoimmunity against pancreatic islets, causing insulin-dependent diabetes.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It is a cancer of a digestive organ on a failing one: HCC almost always arises in a cirrhotic liver, so portal hypertension, oesophageal varices and ascites dominate its course alongside the tumour.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — A failing tumour-bearing liver poisons the brain: as the cirrhosis underlying HCC decompensates, ammonia and toxins it can no longer clear accumulate, producing hepatic encephalopathy with confusion and coma.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A grim cancer watched on a sick liver breeds worry: the poor prognosis, surveillance imaging and decompensation risk of HCC on cirrhosis foster chronic health anxiety alongside depression.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It spreads first to the lungs: the lungs are the commonest site of extrahepatic metastasis in hepatocellular carcinoma, appearing as nodules on staging and follow-up imaging.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It makes hormones it shouldn't: HCC causes paraneoplastic hypoglycaemia from IGF-II, erythrocytosis from erythropoietin and hypercalcaemia from PTHrP.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — It grows into the great veins: HCC characteristically invades the hepatic vein and inferior vena cava, with tumour thrombus that can extend into the right atrium.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It spreads to bone and wastes muscle: HCC commonly metastasises to the skeleton with painful lytic lesions, while the sarcopenia of cirrhosis erodes muscle and worsens prognosis.
- `connects-to` → **[Renal System](../renal-system/README.md)** — A failing liver drags down the kidney: advanced HCC and its cirrhosis precipitate hepatorenal syndrome, a functional kidney failure driven by splanchnic vasodilation.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — The skin betrays the diseased liver: jaundice, intractable cholestatic pruritus and the spider naevi of cirrhosis accompany HCC, and HCV-related disease can bring porphyria cutanea tarda.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Immunotherapy now leads first-line care: atezolizumab (anti-PD-L1) with bevacizumab, and dual nivolumab-ipilimumab, have overtaken kinase inhibitors as first-line treatment for advanced hepatocellular carcinoma.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Multikinase inhibitors target its vasculature: sorafenib and lenvatinib block VEGFR and other kinases to slow advanced HCC, with cabozantinib and regorafenib used after progression.
- `connects-to` → **[Hepatitis B Virus](../../../02-pathogen/01-viruses/hepatitis-b-virus/README.md)** — The leading global cause: chronic hepatitis B drives most hepatocellular carcinoma worldwide, integrating into the genome and causing cancer even without cirrhosis, which vaccination now prevents.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Systemically chemoresistant, locoregionally treated: HCC responds poorly to conventional systemic chemotherapy, so treatment relies on TACE — delivering doxorubicin or cisplatin directly into the tumour's hepatic-arterial supply — plus targeted and immune therapy.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — It grows out of the cirrhotic lobule: hepatocellular carcinoma arises within the disturbed architecture of the cirrhotic liver, where regenerative nodules become dysplastic and then malignant, distorting the normal hepatic lobule.
- `connects-to` → **[Aspirin](../../../03-medicine/01-modern/04-cardio/aspirin/README.md)** — Aspirin may lower its risk: regular aspirin use is associated with reduced hepatocellular carcinoma incidence in chronic viral hepatitis and metabolic liver disease, studied as chemoprevention through anti-inflammatory and antiplatelet effects.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Where it spreads: the lung is the commonest site of extrahepatic HCC metastasis, tumour emboli lodging in the alveolar capillary bed to seed pulmonary nodules.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — Why it is so vascular: hypoxia stabilises HIF-1alpha, which drives the VEGF-fuelled angiogenesis behind HCC's brisk arterial enhancement on imaging and the rationale for anti-angiogenic therapy.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Hepatorenal syndrome: advanced HCC and its underlying cirrhosis cause functional kidney failure through splanchnic vasodilation and renal vasoconstriction—the kidney failing though structurally intact.
- `connects-to` → **[Uveal Melanoma](../uveal-melanoma/README.md)** — Liver-directed therapy unites them: like hepatocellular carcinoma, liver-confined uveal melanoma metastases are treated with hepatic perfusion, radioembolization and resection—both cancers managed by targeting the liver.
- `connects-to` → **[Polycythemia Vera](../polycythemia-vera/README.md)** — Paraneoplastic erythrocytosis: HCC can secrete erythropoietin, raising the red-cell mass—an acquired, tumour-driven polycythaemia distinct from the JAK2-driven polycythaemia vera.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Bone metastasis: though it spreads mainly within the liver and to the lung, HCC also metastasises to bone, producing painful, often osteolytic lesions in the cortical bone.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — A hypervascular tumour: HCC's intense arterial neovascularity from HIF and VEGF underlies its diagnostic arterial-phase enhancement, trans-arterial chemoembolisation (TACE) and antiangiogenic therapy.
- `connects-to` → **[Pulmonary Arterial Hypertension](../pulmonary-arterial-hypertension/README.md)** — Portopulmonary hypertension: the cirrhosis and portal hypertension that breed HCC can also drive pulmonary arterial hypertension, a complication that critically affects liver-transplant candidacy.
- `connects-to` → **[Colorectal Cancer](../colorectal-cancer/README.md)** — The focal-liver-lesion differential: the liver is the dominant metastatic site for colorectal cancer, so a liver mass raises HCC in a cirrhotic but metastasis in others—distinguishing primary from secondary is pivotal.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Amplified oncogene: MYC amplification is a frequent driver of hepatocellular carcinoma, fuelling the ribosome biogenesis and proliferation that mark its more aggressive tumours.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K/AKT survival: AKT activation, often through PTEN loss, cooperates with mTOR to drive HCC growth and survival, part of the pathway exploited by targeted and combination therapy.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Cell-cycle drive: cyclin D1, often amplified downstream of Wnt/β-catenin signalling, pushes hepatocytes through the G1 checkpoint to drive the proliferation of hepatocellular carcinoma.
- `connects-to` → **[MET](../../03-molecular/met/README.md)** — Invasive RTK: c-MET signalling drives HCC proliferation, invasion and angiogenesis, and is one of the kinases blocked by the multi-target inhibitor cabozantinib used in advanced disease.
- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — FGF19-FGFR4 axis: amplification of the FGF19-FGFR4 signalling axis defines a subset of hepatocellular carcinomas and is a targetable driver under investigation with selective FGFR4 inhibitors.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Immunosuppressive niche: CCL2 secreted by HCC recruits tumour-associated macrophages and myeloid-derived suppressor cells, building the immunosuppressive microenvironment that blunts response to immunotherapy.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — Inactivating mutations in the SWI/SNF subunit ARID1A are recurrent in hepatocellular carcinoma, disrupting chromatin regulation of tumor-suppressor and differentiation genes—one of the chromatin-remodeler lesions defining HCC genomics.
- `connects-to` → **[AXL receptor](../../03-molecular/axl-receptor/README.md)** — GAS6-AXL signaling promotes the epithelial-mesenchymal transition and invasion of HCC and drives resistance to sorafenib and immunotherapy, making AXL an emerging combination target in advanced disease.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — Gut-derived LPS reaching the cirrhotic liver through the portal vein activates TLR4 on Kupffer cells, sustaining the chronic inflammation that promotes hepatocarcinogenesis on the background of cirrhosis from which most HCC arises.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — The chromosomal instability of HCC generates cytosolic DNA that activates cGAS-STING, part of the innate-immune context behind the responses to atezolizumab-bevacizumab and other checkpoint-based regimens now standard in advanced disease.
- `connects-to` → **[Androgen receptor](../../03-molecular/androgen-receptor/README.md)** — Hepatocellular carcinoma is two-to-four times commoner in men, and androgen-receptor signaling promotes hepatocarcinogenesis, a hormonal contributor to the striking sex bias of the disease beyond differences in risk-factor exposure.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Hepatic iron loading—in hereditary hemochromatosis and dysmetabolic overload—generates oxidative stress that drives hepatocarcinogenesis, with hepcidin dysregulation central to the iron accumulation that raises HCC risk.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — The RAF-MEK-ERK MAPK cascade is a key proliferative pathway in hepatocellular carcinoma and the target of the multikinase inhibitor sorafenib, a backbone of systemic HCC therapy.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K-AKT-mTOR signaling (AKT and mTOR already mapped) is recurrently activated in HCC, supporting growth and providing a resistance route to anti-angiogenic therapy.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — PDGF signaling drives the tumor stroma and angiogenesis of HCC, a target of the lenvatinib and regorafenib multikinase inhibitors used in its treatment.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — Recurrent NFE2L2/KEAP1 mutations constitutively activate NRF2 in HCC, conferring antioxidant and metabolic advantages that promote hepatocyte survival and tumor progression on a background of chronic liver oxidative injury.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR-MyD88-NF-κB signaling, fueled by gut-derived microbial products reaching the injured liver, sustains the chronic inflammation that links cirrhosis to hepatocarcinogenesis (TLR4 and NF-κB already mapped).
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin is overexpressed in HCC, promoting tumor-cell invasion, metastasis, and angiogenesis, and serving as a circulating biomarker of aggressive disease and poor prognosis.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β mapped) plays a dual tumor-suppressive and pro-invasive role in hepatocellular carcinoma, with SMAD4 loss promoting progression.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — IL-6-JAK-STAT3 signaling (IL-6 and STAT3 mapped) links chronic hepatic inflammation to the proliferation and survival of hepatocellular carcinoma.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A silencing releases CDK4/6-cyclin-D control (cyclin-D1 mapped) of the cell cycle, a recurrent epigenetic lesion in hepatocellular carcinoma.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 supports immune evasion and the metastatic progression of hepatocellular carcinoma.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the antitumor immune response of hepatocellular carcinoma, relevant to its checkpoint-immunotherapy responsiveness.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — EZH2-mediated polycomb repression silences tumor-suppressor genes and drives the epigenetic dysregulation of hepatocellular carcinoma.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — PI3K-AKT-mTOR-driven FOXO inactivation (AKT, PIK3CA, and mTOR already mapped) removes a pro-apoptotic brake, favoring hepatocyte survival in hepatocellular carcinoma.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6 acting on the cyclin-D1-RB axis (cyclin-D1 and CDKN2A already mapped) drives the cell-cycle progression of hepatocellular carcinoma.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-delivered cytotoxic killing by CD8 T and NK cells mediates the immune clearance that the checkpoint-immunotherapy-treated hepatocellular carcinoma must evade.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β regulates β-catenin stability (CTNNB1/Wnt already mapped), the axis frequently activated in hepatocellular carcinoma.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in hepatocellular carcinoma.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins from the chronically inflamed, cirrhotic liver shape the tumor-promoting microenvironment of hepatocellular carcinoma.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of MET and AXL (both already mapped) drives the invasion of hepatocellular carcinoma.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of hepatocellular carcinoma.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival and therapy resistance of hepatocellular carcinoma cells.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the hepatocyte metabolic reprogramming of hepatocellular carcinoma.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the immunosuppressive microenvironment of hepatocellular carcinoma.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the tumor angiogenesis and leukocyte trafficking of hepatocellular carcinoma.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment of hepatocellular carcinoma.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of hepatocellular carcinoma.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory tumor microenvironment of hepatocellular carcinoma.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Immunotherapy: the checkpoint-inhibitor combination atezolizumab-bevacizumab is now first-line for advanced hepatocellular carcinoma, and MHC class II antigen presentation shapes the T-cell response that determines immunotherapy benefit.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Male predominance: hepatocellular carcinoma is far more common in men, and estrogen is thought to protect the female liver by dampening IL-6-driven inflammation (androgen receptor already mapped), contributing to the sex difference in incidence.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — Growth-factor axis: reactivation of IGF-2 and IGF-1R signalling is common in hepatocellular carcinoma, driving proliferation and survival, and links the tumour to the metabolic and NASH pathways that increasingly cause it.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Cirrhotic field: most hepatocellular carcinoma arises in cirrhosis, the collagen scarring laid down by activated stellate cells (TGF-beta and PDGF already mapped), and the degree of this fibrosis governs both cancer risk and treatment tolerance.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Immunotherapy: IL-2-driven T-cell responses underlie the checkpoint immunotherapy (PD-1 and CTLA-4 already mapped) that, with anti-VEGF, is now first-line for advanced hepatocellular carcinoma, reflecting its immunogenic biology.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Bleeding and anaemia: hepatocellular carcinoma on cirrhosis causes variceal and tumour bleeding, and the anaemia of chronic liver disease (hepcidin already mapped) lowers haemoglobin, both contributing to the morbidity of advanced disease.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive microenvironment: IL-10 in the tumour microenvironment dampens the anti-tumour T-cell response (PD-1 and CD8 already mapped), part of the immune evasion that shapes the response to the checkpoint immunotherapy of hepatocellular carcinoma.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Portal hypertension and vasculature: dysregulated nitric oxide drives the splanchnic vasodilation and portal hypertension of the underlying cirrhosis, and with VEGF (already mapped) shapes the vasculature of the hypervascular hepatocellular carcinoma.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative hepatocarcinogenesis: the chronic inflammation and iron overload (hepcidin already mapped) of the diseased liver generate reactive oxygen species, to which xanthine oxidase contributes, driving the oxidative DNA damage of hepatocellular carcinogenesis.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises the Kupffer cells and tumour-associated macrophages (already mapped) toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the tolerogenic liver microenvironment of hepatocellular carcinoma.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Adipokine hepatocarcinogenesis: leptin, rising in the obesity and NASH (already mapped) that increasingly cause hepatocellular carcinoma, promotes hepatocyte proliferation and the fibro-inflammatory (TGF-β already mapped) drive of the tumour.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — COX-2 inflammation: prostaglandins from cyclooxygenase-2 in the chronically inflamed cirrhotic liver (IL-6 already mapped) promote the proliferation and angiogenesis of hepatocellular carcinoma, part of the inflammation-cancer link.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune milieu: IL-13, with IL-4 (already mapped), supports the M2 macrophage (already mapped) immunosuppressive milieu of hepatocellular carcinoma that limits the checkpoint immunotherapy.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Hepatoprotective adipokine: the fall in adiponectin, a hepatoprotective adipokine (leptin already mapped), with obesity and NASH (already mapped) removes a brake on the hepatocarcinogenesis of hepatocellular carcinoma.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Copper and hepatocarcinogenesis: the hepatic copper overload of Wilson's disease raises the HCC risk, and copper's role in angiogenesis (VEGF already mapped) and oxidative injury contributes to the cirrhotic-liver carcinogenesis.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Cirrhotic stellate cells: the activated hepatic stellate cells (myofibroblasts; TGF-β and PDGF already mapped) drive the cirrhosis (collagen already mapped) that is the field for the hepatocellular carcinoma.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Checkpoint immunity: the cytotoxic T cells (perforin and PD-1 already mapped) are unleashed by the atezolizumab (PD-L1) in the immunotherapy of hepatocellular carcinoma.
- `connects-to` → **[Hepatitis C](../hepatitis-c/README.md)** — Viral cause: the chronic hepatitis C is a leading cause of HCC (via the cirrhosis), the DAA cure reducing but not eliminating the risk.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity exploited by the checkpoint (PD-1 already mapped) immunotherapy of hepatocellular carcinoma.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response of the hepatocellular-carcinoma immune microenvironment.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — NASH-metabolic adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the NASH (already mapped) metabolic milieu that drives hepatocellular carcinoma.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of hepatocellular carcinoma.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the tumour-promoting inflammation of hepatocellular carcinoma.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the hepatocellular-carcinoma microenvironment.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of hepatocellular carcinoma.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune balance of the hepatocellular-carcinoma microenvironment.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Tertiary lymphoid structures: the B cells organise the intratumoural tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, associates with the immunotherapy (PD-1 already mapped) response of hepatocellular carcinoma.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Tumour complement: the complement C3, produced by the hepatocytes and within the tumour, contributes to the inflammatory and immunosuppressive dimension of the hepatocellular-carcinoma microenvironment.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid (macrophage already mapped) recruitment and immunosuppression of the hepatocellular-carcinoma microenvironment.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Hepatic iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the hepatic iron overload that promotes the oxidative carcinogenesis of hepatocellular carcinoma.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-tumour axis: TSLP, from cancer-associated fibroblasts (already mapped) and the cirrhotic stroma (liver already mapped), primes dendritic cells (already mapped) and mast cells (already mapped) toward the Th2 immunosuppressive bias of the HCC microenvironment.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-tumour axis: bradykinin, via the kallikrein-kinin system in the cirrhotic and tumour microenvironment, amplifies the vascular permeability and the myeloid (macrophage already mapped) recruitment in hepatocellular carcinoma.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Anaemia of cancer: erythropoietin corrects the cancer-related anaemia (hepcidin already mapped) of hepatocellular carcinoma; EpoR expression on hepatoma cells also modulates a potential direct proliferative signal.

[^llovet-2008-sorafenib]: Llovet JM, Ricci S, Mazzaferro V, et al. Sorafenib in advanced hepatocellular carcinoma. *N Engl J Med.* 2008;359(4):378-390. [doi:10.1056/NEJMoa0708857](https://doi.org/10.1056/NEJMoa0708857) · [PubMed 18650514](https://pubmed.ncbi.nlm.nih.gov/18650514/)
[^finn-2020-imbrave150]: Finn RS, Qin S, Ikeda M, et al. Atezolizumab plus bevacizumab in unresectable hepatocellular carcinoma. *N Engl J Med.* 2020;382(20):1894-1905. [doi:10.1056/NEJMoa1915745](https://doi.org/10.1056/NEJMoa1915745) · [PubMed 32402160](https://pubmed.ncbi.nlm.nih.gov/32402160/)
