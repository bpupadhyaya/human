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
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "EGFR drives the bile-duct cancer cell: the receptor is frequently overexpressed in cholangiocarcinoma, activating proliferation and survival pathways and offering one of the targeted handles in a cancer otherwise hard to treat."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "The dense desmoplastic tumor freezes out immunity: dysfunctional dendritic cells fail to prime an effective T-cell response in cholangiocarcinoma, part of the immune-cold microenvironment that blunts checkpoint therapy."
  - target: 01-human/07-system/lynch-syndrome
    relation: connects-to
    note: "Mismatch-repair failure can seed it: Lynch syndrome raises the risk of biliary tract cancer, and the resulting MSI-high cholangiocarcinomas are among the few that respond well to immune-checkpoint therapy."
  - target: 01-human/03-molecular/idh2
    relation: connects-to
    note: "IDH2, like IDH1, is a targetable driver: a subset of intrahepatic cholangiocarcinomas carry IDH2 mutations that generate the oncometabolite 2-hydroxyglutarate and reprogram the epigenome, defining a molecular subtype with emerging targeted therapy."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Blocked bile breeds biliary sepsis: tumor obstruction of the ducts causes cholangitis that can escalate to life-threatening Gram-negative sepsis, so urgent biliary drainage is often needed before any cancer treatment."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells stoke the desmoplastic tumor: recruited into cholangiocarcinoma they release angiogenic and fibrogenic mediators that feed the dense stroma and new vessels on which the bile-duct cancer depends."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Chronic biliary inflammation switches on NF-κB: the inflamed, fluke- or PSC-damaged bile ducts activate NF-κB in cholangiocytes, driving the survival and proliferation signals that turn chronic cholangitis into cancer."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6 from the inflamed ducts feeds STAT3: cholangiocarcinoma cells respond to IL-6 with STAT3 activation that drives proliferation and resistance, a central inflammation-to-cancer axis in the bile-duct epithelium."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "A cholestatic cancer that still clots: despite the deranged clotting of biliary obstruction, cholangiocarcinoma's tumor-driven hypercoagulability raises venous thromboembolism risk, compounded by biliary stenting and surgery."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Obstruction and chemo strain the kidney: deep cholestatic jaundice predisposes to a hepatorenal-type injury and post-procedure acute kidney injury, while cisplatin-gemcitabine chemotherapy adds nephrotoxicity threatening chronic kidney disease."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Chronic biliary inflammation blunts the marrow: the IL-6-rich inflammation of cholangiocarcinoma and its biliary disease raise hepcidin and suppress erythropoiesis, producing an anemia of chronic disease."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A grim prognosis weighs on mood: cholangiocarcinoma's late presentation, obstructive jaundice with intractable itch and poor survival impose a heavy psychological burden, with high rates of depression."
  - target: 01-human/07-system/prurigo-nodularis
    relation: connects-to
    note: "Biliary obstruction drives relentless itch: cholangiocarcinoma blocks bile flow, and the retained bile salts cause an intense cholestatic pruritus that scratching can turn into prurigo nodularis."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Tumor and chemo strain the nerves: invasion of the porta hepatis and the gemcitabine-cisplatin chemotherapy for cholangiocarcinoma produce visceral and chemotherapy-induced neuropathic pain."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Its chemotherapy opens the lung to mold: the neutropenia from gemcitabine-cisplatin therapy for cholangiocarcinoma can let inhaled Aspergillus invade as pulmonary aspergillosis."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It is a cancer of the biliary tree: cholangiocarcinoma obstructs the bile ducts, causing obstructive jaundice, pruritus, ascending cholangitis and fat malabsorption central to its presentation."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Its surgery is among the most demanding: curative resection means major hepatectomy or a Whipple with biliary reconstruction, leaving complex anastomoses prone to bile leak and slow healing."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A late-presenting, poor-prognosis cancer breeds worry: the obstructive jaundice, difficult surgery and grim survival of cholangiocarcinoma foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It paints the skin yellow and itchy: biliary obstruction by cholangiocarcinoma causes jaundice and intense cholestatic pruritus, often the presenting features that prompt diagnosis."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Lymph-node spread decides resectability: regional lymph-node metastasis is a major prognostic factor in cholangiocarcinoma, guiding whether surgery is possible and the need for adjuvant therapy."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It crawls along the nerves: cholangiocarcinoma is notorious for perineural invasion, spreading through the nerve sheaths around the bile ducts and raising the risk of pain and recurrence."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It spreads to the lungs: cholangiocarcinoma commonly metastasises to the lung and pleura, and high biliary obstruction in the porta can compromise breathing in advanced disease."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Immunotherapy joins the regimen: PD-L1 blockade with durvalumab added to gemcitabine-cisplatin is now standard for advanced biliary cancer, and primary sclerosing cholangitis provides its autoimmune backdrop."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Treatment and obstruction reach the kidney: cisplatin chemotherapy is nephrotoxic, and the deep jaundice of biliary obstruction predisposes to acute kidney injury during surgery."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "A precision-oncology showcase: cholangiocarcinoma is rich in actionable mutations — FGFR2 fusions (pemigatinib), IDH1 mutations (ivosidenib), and BRAF or HER2 alterations all have matched targeted drugs."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "The chemotherapy backbone: gemcitabine combined with cisplatin is the long-standing first-line chemotherapy foundation for advanced biliary tract cancer."
  - target: 02-pathogen/01-viruses/hepatitis-b-virus
    relation: connects-to
    note: "Chronic hepatitis seeds the bile ducts: hepatitis B, like hepatitis C and liver flukes, chronically inflames the liver and is an established risk factor for intrahepatic cholangiocarcinoma."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Immunotherapy joined first-line: adding durvalumab to gemcitabine-cisplatin (the TOPAZ-1 regimen) improved survival in advanced biliary tract cancer, bringing checkpoint blockade into cholangiocarcinoma care."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "It springs from the bile ductules: intrahepatic cholangiocarcinoma arises from the small bile ducts within the portal tracts of the liver lobule, and biliary obstruction causes the cholestasis and jaundice that dominate its presentation."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "A shared IDH vulnerability: IDH1 mutations occur in both cholangiocarcinoma and acute myeloid leukaemia, and the IDH1 inhibitor ivosidenib treats both — an unexpected link between a bile-duct cancer and a blood cancer."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Where it spreads: cholangiocarcinoma metastasises to the lungs, seeding tumour deposits in the alveolar capillary bed as part of advanced disease."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "When immunotherapy works: mismatch-repair-deficient and inflamed cholangiocarcinomas attract tertiary lymphoid structures with germinal centres and can respond to PD-1 checkpoint blockade."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "A chromatin-remodelling driver: ARID1A, part of the SWI/SNF complex, is recurrently mutated in cholangiocarcinoma alongside IDH and FGFR, shaping its distinctive and increasingly targetable genomic landscape."
  - target: 01-human/07-system/uveal-melanoma
    relation: connects-to
    note: "BAP1 across tumours: germline BAP1 mutations predispose to cholangiocarcinoma alongside uveal melanoma, mesothelioma and renal cell carcinoma—a hereditary BAP1 tumour syndrome."
  - target: 01-human/07-system/ovarian-clear-cell-carcinoma
    relation: connects-to
    note: "A shared chromatin driver: cholangiocarcinoma and ovarian clear cell carcinoma both frequently mutate ARID1A of the SWI/SNF complex, two adenocarcinomas converging on chromatin dysregulation."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "A metabolic risk factor: type 2 diabetes and obesity (via fatty liver) raise the risk of intrahepatic cholangiocarcinoma, adding metabolic disease to its classic biliary and parasitic causes."
  - target: 01-human/03-molecular/yap1
    relation: connects-to
    note: "Hippo-YAP driver: activation of the Hippo pathway effector YAP is a central oncogenic mechanism in cholangiocarcinoma, promoting biliary cell proliferation and a poor prognosis."
  - target: 01-human/03-molecular/met
    relation: connects-to
    note: "MET as a target: MET amplification and overexpression occur in a subset of cholangiocarcinomas, marking another actionable receptor tyrosine kinase alongside FGFR2 fusions."
  - target: 01-human/03-molecular/ntrk
    relation: connects-to
    note: "Rare actionable fusion: NTRK gene fusions, though uncommon, make some cholangiocarcinomas exquisitely sensitive to TRK inhibitors, part of its precision-oncology landscape."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K activation: PIK3CA mutations activate the PI3K/AKT pathway in a subset of cholangiocarcinomas, driving growth and contributing to therapy resistance."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Desmoplastic hypoxia: the dense, poorly vascularised stroma of cholangiocarcinoma is hypoxic, stabilising HIF-1α to drive angiogenesis, invasion and chemoresistance."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Oncogenic amplification: MYC activation downstream of growth-factor signalling drives the proliferation and metabolic reprogramming of cholangiocarcinoma."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Desmoplastic CAFs: PDGF from tumour cells activates cancer-associated fibroblasts that build the dense desmoplastic stroma characteristic of cholangiocarcinoma, supporting growth and drug resistance."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Macrophage recruitment: CCL2 draws tumour-associated macrophages into the cholangiocarcinoma stroma, fostering the immunosuppressive, pro-tumour microenvironment of this hard-to-treat cancer."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K survival: PI3K-AKT signalling, often through PIK3CA mutation or PTEN loss, sustains cholangiocarcinoma growth and survival alongside its FGFR and IDH driver lesions."
  - target: 01-human/03-molecular/bap1
    relation: connects-to
    note: "Chromatin tumour suppressor: inactivating BAP1 mutations are recurrent in cholangiocarcinoma, disrupting the deubiquitinase's chromatin and DNA-repair functions—one of the defining tumour-suppressor lesions of the disease."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Stromal CXCL12 axis: cancer-associated fibroblasts in the dense desmoplastic stroma secrete CXCL12 that signals through CXCR4 to drive cholangiocarcinoma invasion and the chemoresistance conferred by the stromal niche."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Inflammation-driven carcinogenesis: TLR4 sensing of gut- and biliary-derived bacterial products sustains the chronic biliary inflammation — from liver fluke or primary sclerosing cholangitis — that drives cholangiocarcinogenesis."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Immunotherapy rationale: genomic instability in cholangiocarcinoma generates cytosolic DNA that activates cGAS-STING, part of the innate-immune context behind adding the PD-L1 inhibitor durvalumab to gemcitabine-cisplatin, now first-line in advanced biliary cancer."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Chemotherapy apoptosis: gemcitabine-cisplatin, the cytotoxic backbone of advanced cholangiocarcinoma treatment, kills tumour cells through caspase-3-mediated apoptosis, the death pathway whose evasion underlies the chemoresistance of this aggressive cancer."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Bile-acid carcinogenesis: retained bile acids in chronic cholestasis activate signalling that promotes cholangiocyte proliferation and survival, a metabolic limb of the inflammation-and-cholestasis milieu from which cholangiocarcinoma arises."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "MAPK convergence: KRAS, BRAF, FGFR2 fusions and MET (all already mapped) funnel into the MAPK-ERK cascade, the central proliferative driver and a key therapeutic target in cholangiocarcinoma."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Growth axis: mTOR completes the PI3K-AKT-mTOR pathway (PIK3CA and AKT already mapped) that sustains growth and survival signalling in cholangiocarcinoma."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "Cell-cycle release: CDKN2A/p16 loss is a frequent event in cholangiocarcinoma, removing the brake on CDK4/6-cyclin-D-driven entry into the cell cycle."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "Tumour-suppressor loss: SMAD4 loss disables TGF-β tumour-suppressor signalling (TGF-β already mapped), a frequent and prognostically adverse event in cholangiocarcinoma."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Inflammation-driven growth: chronic biliary inflammation signals through IL-6-JAK-STAT3 (IL-6 and STAT3 already mapped) to drive the cholangiocyte proliferation and survival underlying cholangiocarcinoma."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Innate carcinogenesis: TLR-MyD88-NF-κB innate signalling (TLR4 and NF-κB already mapped), driven by liver-fluke infection and primary sclerosing cholangitis, sustains the inflammation that promotes cholangiocarcinogenesis."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 promotes the desmoplastic stroma and immune evasion of cholangiocarcinoma and serves as a marker of biliary malignancy."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "Loss of PTEN restraint on PI3K-AKT-mTOR signalling (AKT, PIK3CA and mTOR mapped) drives proliferation and survival in cholangiocarcinoma."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Wnt/β-catenin signalling contributes to cholangiocyte transformation and the progression of cholangiocarcinoma."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the antitumour immune response of cholangiocarcinoma, relevant to its limited checkpoint-immunotherapy responsiveness."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "EZH2-mediated polycomb repression cooperates with the IDH mutations (IDH1/IDH2 already mapped) in the epigenetic dysregulation of cholangiocarcinoma."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6-cyclin-D activity drives the cell-cycle progression of cholangiocarcinoma, often alongside CDKN2A loss."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "PI3K-AKT-driven FOXO inactivation (PTEN, AKT, and PIK3CA already mapped) removes a pro-apoptotic brake in cholangiocarcinoma."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-delivered cytotoxic killing by CD8 T and NK cells mediates the immune clearance that the desmoplastic, immune-evasive cholangiocarcinoma must evade."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins amplify the inflammatory, often cholangitis- and PSC-associated microenvironment of cholangiocarcinoma."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β regulates the Wnt/β-catenin and survival signaling (Wnt already mapped) of cholangiocarcinoma."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in cholangiocarcinoma."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of FGFR, MET, and EGFR (all already mapped) drives the invasion of cholangiocarcinoma."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of cholangiocarcinoma (interacting with the IDH-mutant metabolism; IDH1/2 already mapped)."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival and therapy resistance of cholangiocarcinoma cells."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the desmoplastic, immunosuppressive microenvironment of cholangiocarcinoma."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic dysregulation of cholangiocarcinoma."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the inflammation-driven tumorigenesis and microenvironment of cholangiocarcinoma."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the biliary inflammation and tumor microenvironment of cholangiocarcinoma."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory tumor microenvironment of cholangiocarcinoma."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory tumor microenvironment of cholangiocarcinoma."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the tumor microenvironment and biliary-inflammation-linked signaling of cholangiocarcinoma."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immunotherapy: adding the checkpoint inhibitor durvalumab to chemotherapy is now standard for advanced biliary tract cancer, and MHC class II antigen presentation shapes the T-cell response that determines the benefit."
  - target: 01-human/03-molecular/axl-receptor
    relation: connects-to
    note: "Invasion and resistance: the AXL receptor tyrosine kinase drives the epithelial-mesenchymal transition and treatment resistance of cholangiocarcinoma, a mechanism of progression beyond the FGFR and IDH targets already mapped."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell response: IL-2-driven T-cell expansion supports the anti-tumour immunity and adoptive-cell approaches under investigation for cholangiocarcinoma alongside checkpoint blockade (PD-1 already mapped)."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Desmoplastic fibrosis: the collagen-rich stroma laid down by cancer-associated fibroblasts (already mapped) forms the dense desmoplastic tumour characteristic of cholangiocarcinoma, obstructing bile ducts and limiting drug penetration."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Cholestasis and anaemia: biliary obstruction, chronic inflammation and gastrointestinal bleeding in cholangiocarcinoma lower haemoglobin, and the anaemia of chronic disease compounds the malaise of the advanced tumour."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative carcinogenesis: chronic biliary inflammation and cholestasis (from stones, flukes or sclerosing cholangitis) generate oxidative stress, to which xanthine oxidase contributes, driving the DNA damage that initiates cholangiocarcinoma."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Radiotherapy and photodynamic therapy: photon radiotherapy, including stereotactic body radiotherapy, and photodynamic therapy are used to control unresectable cholangiocarcinoma and relieve biliary obstruction, options for a tumour often diagnosed too late for surgery."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive microenvironment: IL-10 in the desmoplastic tumour microenvironment dampens the anti-tumour T-cell response (PD-1 already mapped), part of the immune evasion that limits immunotherapy in cholangiocarcinoma."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Inflammatory carcinogenesis: cyclooxygenase-2 and prostaglandin E2 from the chronic biliary inflammation (IL-6 already mapped) promote the proliferation and survival of transformed cholangiocytes, part of the inflammation-driven pathogenesis of cholangiocarcinoma."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises the tumour-associated macrophages (already mapped) toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the cold desmoplastic microenvironment that limits immunotherapy in cholangiocarcinoma."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Tumour-associated macrophages: the macrophages (CCL2 and TLR4 already mapped) infiltrate the desmoplastic stroma of cholangiocarcinoma, and their M2 polarisation supports the immunosuppression and progression of the biliary cancer."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Biliary copper: the liver (already mapped) excretes copper into bile, and the biliary obstruction of cholangiocarcinoma disrupts this excretion, linking copper handling to the cholestasis of the biliary cancer."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "M2 desmoplastic stroma: IL-13, with IL-4 (already mapped), drives the M2 macrophage (already mapped) arm of the immunosuppressive desmoplastic stroma (collagen already mapped) of cholangiocarcinoma."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Obesity and NAFLD risk: leptin is the obesity/NAFLD-related adipokine, a rising risk factor for the intrahepatic cholangiocarcinoma (liver already mapped) via the metabolic-inflammatory milieu."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic (cholesterol already mapped) risk of cholangiocarcinoma."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the obesity/NAFLD metabolic risk of cholangiocarcinoma."
  - target: 01-human/07-system/nash
    relation: connects-to
    note: "NAFLD/NASH risk: the non-alcoholic steatohepatitis (the obesity/metabolic — leptin and adiponectin already mapped) is a rising risk factor for the intrahepatic cholangiocarcinoma."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "Combined HCC-CCA: the hepatocytes and the cholangiocytes share the progenitor origin; the combined hepatocellular-cholangiocarcinoma reflects the plasticity of the liver (already mapped)."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity, relevant to the checkpoint (PD-1 already mapped) immunotherapy of cholangiocarcinoma."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the desmoplastic immune microenvironment of cholangiocarcinoma."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment of cholangiocarcinoma."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the desmoplastic immune microenvironment of cholangiocarcinoma."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the tumour-promoting inflammation of cholangiocarcinoma (often arising on a background of chronic biliary inflammation)."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the cholangiocarcinoma microenvironment."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the chronic biliary inflammation and tumour-promoting microenvironment of cholangiocarcinoma."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, may mark the immune response of the cholangiocarcinoma microenvironment."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the desmoplastic (fibroblast already mapped) stroma of cholangiocarcinoma."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) contribute to the inflammatory dimension of the desmoplastic cholangiocarcinoma microenvironment."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement evasion: the cholangiocarcinoma cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), tempering the complement attack within the tumour stroma."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Cholestatic iron: transferrin, the iron carrier, reflects the disordered iron handling of the chronic biliary inflammation and cholestasis that predispose to cholangiocarcinoma."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-TME axis: TSLP, from biliary epithelium (already mapped) and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2 immunosuppression of the biliary tumour microenvironment of cholangiocarcinoma."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-biliary axis: bradykinin, via B1/B2 receptors on biliary endothelium (already mapped) and tumour stromal cells, amplifies the vascular permeability and the inflammatory milieu of the cholangiocarcinoma stroma."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Tumour-EPO axis: erythropoietin, via the EPOR on biliary tumour cells (already mapped), modulates the survival, proliferation, and the angiogenic (already mapped) dimension of cholangiocarcinoma."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell biliary axis: histamine, from mast cells (already mapped) in the cholangiocarcinoma stroma, amplifies the angiogenesis (already mapped) and the immunosuppressive inflammatory milieu of the biliary tumour microenvironment."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian-biliary axis: melatonin, via MT1/MT2 receptors on biliary epithelium (already mapped), modulates the oxidative stress and the cholestasis-driven (already mapped) carcinogenesis of cholangiocarcinoma."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Sex-hormone biliary axis: testosterone, via androgen receptors on biliary tumour cells (already mapped), modulates the sex-differential cholangiocarcinoma risk (higher in males) and the immunosuppressive tumour microenvironment."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "CCA prolactin: prolactin, via PRLR on macrophages (already mapped) and mast cells (already mapped), promotes biliary tumour immune escape; hyperprolactinaemia amplifies the NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of cholangiocarcinoma."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "CCA oxytocin: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates biliary TME inflammation; oxytocin deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of cholangiocarcinoma."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "CCA vasopressin: vasopressin, via V2R on endothelial cells (already mapped) and macrophages (already mapped), modulates biliary vascular tone; vasopressin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) tumour-promoting cascade of cholangiocarcinoma."
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
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — EGFR drives the bile-duct cancer cell: the receptor is frequently overexpressed in cholangiocarcinoma, activating proliferation and survival pathways and offering one of the targeted handles in a cancer otherwise hard to treat.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — The dense desmoplastic tumor freezes out immunity: dysfunctional dendritic cells fail to prime an effective T-cell response in cholangiocarcinoma, part of the immune-cold microenvironment that blunts checkpoint therapy.
- `connects-to` → **[Lynch Syndrome](../lynch-syndrome/README.md)** — Mismatch-repair failure can seed it: Lynch syndrome raises the risk of biliary tract cancer, and the resulting MSI-high cholangiocarcinomas are among the few that respond well to immune-checkpoint therapy.
- `connects-to` → **[IDH2](../../03-molecular/idh2/README.md)** — IDH2, like IDH1, is a targetable driver: a subset of intrahepatic cholangiocarcinomas carry IDH2 mutations that generate the oncometabolite 2-hydroxyglutarate and reprogram the epigenome, defining a molecular subtype with emerging targeted therapy.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Blocked bile breeds biliary sepsis: tumor obstruction of the ducts causes cholangitis that can escalate to life-threatening Gram-negative sepsis, so urgent biliary drainage is often needed before any cancer treatment.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells stoke the desmoplastic tumor: recruited into cholangiocarcinoma they release angiogenic and fibrogenic mediators that feed the dense stroma and new vessels on which the bile-duct cancer depends.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Chronic biliary inflammation switches on NF-κB: the inflamed, fluke- or PSC-damaged bile ducts activate NF-κB in cholangiocytes, driving the survival and proliferation signals that turn chronic cholangitis into cancer.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6 from the inflamed ducts feeds STAT3: cholangiocarcinoma cells respond to IL-6 with STAT3 activation that drives proliferation and resistance, a central inflammation-to-cancer axis in the bile-duct epithelium.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — A cholestatic cancer that still clots: despite the deranged clotting of biliary obstruction, cholangiocarcinoma's tumor-driven hypercoagulability raises venous thromboembolism risk, compounded by biliary stenting and surgery.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Obstruction and chemo strain the kidney: deep cholestatic jaundice predisposes to a hepatorenal-type injury and post-procedure acute kidney injury, while cisplatin-gemcitabine chemotherapy adds nephrotoxicity threatening chronic kidney disease.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Chronic biliary inflammation blunts the marrow: the IL-6-rich inflammation of cholangiocarcinoma and its biliary disease raise hepcidin and suppress erythropoiesis, producing an anemia of chronic disease.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A grim prognosis weighs on mood: cholangiocarcinoma's late presentation, obstructive jaundice with intractable itch and poor survival impose a heavy psychological burden, with high rates of depression.
- `connects-to` → **[Prurigo Nodularis](../prurigo-nodularis/README.md)** — Biliary obstruction drives relentless itch: cholangiocarcinoma blocks bile flow, and the retained bile salts cause an intense cholestatic pruritus that scratching can turn into prurigo nodularis.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Tumor and chemo strain the nerves: invasion of the porta hepatis and the gemcitabine-cisplatin chemotherapy for cholangiocarcinoma produce visceral and chemotherapy-induced neuropathic pain.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Its chemotherapy opens the lung to mold: the neutropenia from gemcitabine-cisplatin therapy for cholangiocarcinoma can let inhaled Aspergillus invade as pulmonary aspergillosis.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It is a cancer of the biliary tree: cholangiocarcinoma obstructs the bile ducts, causing obstructive jaundice, pruritus, ascending cholangitis and fat malabsorption central to its presentation.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Its surgery is among the most demanding: curative resection means major hepatectomy or a Whipple with biliary reconstruction, leaving complex anastomoses prone to bile leak and slow healing.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A late-presenting, poor-prognosis cancer breeds worry: the obstructive jaundice, difficult surgery and grim survival of cholangiocarcinoma foster chronic health anxiety alongside depression.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It paints the skin yellow and itchy: biliary obstruction by cholangiocarcinoma causes jaundice and intense cholestatic pruritus, often the presenting features that prompt diagnosis.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Lymph-node spread decides resectability: regional lymph-node metastasis is a major prognostic factor in cholangiocarcinoma, guiding whether surgery is possible and the need for adjuvant therapy.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It crawls along the nerves: cholangiocarcinoma is notorious for perineural invasion, spreading through the nerve sheaths around the bile ducts and raising the risk of pain and recurrence.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It spreads to the lungs: cholangiocarcinoma commonly metastasises to the lung and pleura, and high biliary obstruction in the porta can compromise breathing in advanced disease.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Immunotherapy joins the regimen: PD-L1 blockade with durvalumab added to gemcitabine-cisplatin is now standard for advanced biliary cancer, and primary sclerosing cholangitis provides its autoimmune backdrop.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Treatment and obstruction reach the kidney: cisplatin chemotherapy is nephrotoxic, and the deep jaundice of biliary obstruction predisposes to acute kidney injury during surgery.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — A precision-oncology showcase: cholangiocarcinoma is rich in actionable mutations — FGFR2 fusions (pemigatinib), IDH1 mutations (ivosidenib), and BRAF or HER2 alterations all have matched targeted drugs.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — The chemotherapy backbone: gemcitabine combined with cisplatin is the long-standing first-line chemotherapy foundation for advanced biliary tract cancer.
- `connects-to` → **[Hepatitis B Virus](../../../02-pathogen/01-viruses/hepatitis-b-virus/README.md)** — Chronic hepatitis seeds the bile ducts: hepatitis B, like hepatitis C and liver flukes, chronically inflames the liver and is an established risk factor for intrahepatic cholangiocarcinoma.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Immunotherapy joined first-line: adding durvalumab to gemcitabine-cisplatin (the TOPAZ-1 regimen) improved survival in advanced biliary tract cancer, bringing checkpoint blockade into cholangiocarcinoma care.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — It springs from the bile ductules: intrahepatic cholangiocarcinoma arises from the small bile ducts within the portal tracts of the liver lobule, and biliary obstruction causes the cholestasis and jaundice that dominate its presentation.
- `connects-to` → **[AML](../aml/README.md)** — A shared IDH vulnerability: IDH1 mutations occur in both cholangiocarcinoma and acute myeloid leukaemia, and the IDH1 inhibitor ivosidenib treats both — an unexpected link between a bile-duct cancer and a blood cancer.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Where it spreads: cholangiocarcinoma metastasises to the lungs, seeding tumour deposits in the alveolar capillary bed as part of advanced disease.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — When immunotherapy works: mismatch-repair-deficient and inflamed cholangiocarcinomas attract tertiary lymphoid structures with germinal centres and can respond to PD-1 checkpoint blockade.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — A chromatin-remodelling driver: ARID1A, part of the SWI/SNF complex, is recurrently mutated in cholangiocarcinoma alongside IDH and FGFR, shaping its distinctive and increasingly targetable genomic landscape.
- `connects-to` → **[Uveal Melanoma](../uveal-melanoma/README.md)** — BAP1 across tumours: germline BAP1 mutations predispose to cholangiocarcinoma alongside uveal melanoma, mesothelioma and renal cell carcinoma—a hereditary BAP1 tumour syndrome.
- `connects-to` → **[Ovarian Clear Cell Carcinoma](../ovarian-clear-cell-carcinoma/README.md)** — A shared chromatin driver: cholangiocarcinoma and ovarian clear cell carcinoma both frequently mutate ARID1A of the SWI/SNF complex, two adenocarcinomas converging on chromatin dysregulation.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — A metabolic risk factor: type 2 diabetes and obesity (via fatty liver) raise the risk of intrahepatic cholangiocarcinoma, adding metabolic disease to its classic biliary and parasitic causes.
- `connects-to` → **[YAP1](../../03-molecular/yap1/README.md)** — Hippo-YAP driver: activation of the Hippo pathway effector YAP is a central oncogenic mechanism in cholangiocarcinoma, promoting biliary cell proliferation and a poor prognosis.
- `connects-to` → **[MET](../../03-molecular/met/README.md)** — MET as a target: MET amplification and overexpression occur in a subset of cholangiocarcinomas, marking another actionable receptor tyrosine kinase alongside FGFR2 fusions.
- `connects-to` → **[NTRK](../../03-molecular/ntrk/README.md)** — Rare actionable fusion: NTRK gene fusions, though uncommon, make some cholangiocarcinomas exquisitely sensitive to TRK inhibitors, part of its precision-oncology landscape.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K activation: PIK3CA mutations activate the PI3K/AKT pathway in a subset of cholangiocarcinomas, driving growth and contributing to therapy resistance.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Desmoplastic hypoxia: the dense, poorly vascularised stroma of cholangiocarcinoma is hypoxic, stabilising HIF-1α to drive angiogenesis, invasion and chemoresistance.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Oncogenic amplification: MYC activation downstream of growth-factor signalling drives the proliferation and metabolic reprogramming of cholangiocarcinoma.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — Desmoplastic CAFs: PDGF from tumour cells activates cancer-associated fibroblasts that build the dense desmoplastic stroma characteristic of cholangiocarcinoma, supporting growth and drug resistance.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Macrophage recruitment: CCL2 draws tumour-associated macrophages into the cholangiocarcinoma stroma, fostering the immunosuppressive, pro-tumour microenvironment of this hard-to-treat cancer.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K survival: PI3K-AKT signalling, often through PIK3CA mutation or PTEN loss, sustains cholangiocarcinoma growth and survival alongside its FGFR and IDH driver lesions.
- `connects-to` → **[BAP1](../../03-molecular/bap1/README.md)** — Inactivating BAP1 mutations are recurrent in cholangiocarcinoma, disrupting the deubiquitinase's chromatin-remodeling and DNA-repair functions—one of the defining tumor-suppressor lesions alongside IDH1 and FGFR2 alterations.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — Cancer-associated fibroblasts in the dense desmoplastic stroma secrete CXCL12 that signals through CXCR4 to drive cholangiocarcinoma invasion and the chemoresistance conferred by the protective stromal niche.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — TLR4 sensing of gut- and biliary-derived bacterial products sustains the chronic biliary inflammation—from liver-fluke infection or primary sclerosing cholangitis—that is the dominant driver of cholangiocarcinogenesis.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Genomic instability in cholangiocarcinoma generates cytosolic DNA that activates cGAS-STING, part of the innate-immune context behind adding the PD-L1 inhibitor durvalumab to gemcitabine-cisplatin, now first-line in advanced biliary cancer.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Gemcitabine-cisplatin, the cytotoxic backbone of advanced cholangiocarcinoma treatment, kills tumor cells through caspase-3-mediated apoptosis, the death pathway whose evasion underlies the chemoresistance of this aggressive cancer.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Retained bile acids in chronic cholestasis activate signaling that promotes cholangiocyte proliferation and survival, a metabolic limb of the inflammation-and-cholestasis milieu from which cholangiocarcinoma arises.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — KRAS, BRAF, FGFR2 fusions and MET (all already mapped) funnel into the MAPK-ERK cascade, the central proliferative driver and a key therapeutic target in cholangiocarcinoma.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR completes the PI3K-AKT-mTOR pathway (PIK3CA and AKT already mapped) that sustains growth and survival signaling in cholangiocarcinoma.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A/p16 loss is a frequent event in cholangiocarcinoma, removing the brake on CDK4/6-cyclin-D-driven entry into the cell cycle.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — SMAD4 loss disables TGF-β tumor-suppressor signaling (TGF-β already mapped), a frequent and prognostically adverse event in cholangiocarcinoma.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Chronic biliary inflammation signals through IL-6-JAK-STAT3 (IL-6 and STAT3 already mapped) to drive the cholangiocyte proliferation and survival underlying cholangiocarcinoma.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR-MyD88-NF-κB innate signaling (TLR4 and NF-κB already mapped), driven by liver-fluke infection and primary sclerosing cholangitis, sustains the inflammation that promotes cholangiocarcinogenesis.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 promotes the desmoplastic stroma and immune evasion of cholangiocarcinoma and serves as a marker of biliary malignancy.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — Loss of PTEN restraint on PI3K-AKT-mTOR signaling (AKT, PIK3CA and mTOR mapped) drives proliferation and survival in cholangiocarcinoma.
- `connects-to` → **[Wnt/beta-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Wnt/β-catenin signaling contributes to cholangiocyte transformation and the progression of cholangiocarcinoma.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the antitumor immune response of cholangiocarcinoma, relevant to its limited checkpoint-immunotherapy responsiveness.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — EZH2-mediated polycomb repression cooperates with the IDH mutations (IDH1/IDH2 already mapped) in the epigenetic dysregulation of cholangiocarcinoma.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6-cyclin-D activity drives the cell-cycle progression of cholangiocarcinoma, often alongside CDKN2A loss.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — PI3K-AKT-driven FOXO inactivation (PTEN, AKT, and PIK3CA already mapped) removes a pro-apoptotic brake in cholangiocarcinoma.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-delivered cytotoxic killing by CD8 T and NK cells mediates the immune clearance that the desmoplastic, immune-evasive cholangiocarcinoma must evade.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins amplify the inflammatory, often cholangitis- and PSC-associated microenvironment of cholangiocarcinoma.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β regulates the Wnt/β-catenin and survival signaling (Wnt already mapped) of cholangiocarcinoma.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in cholangiocarcinoma.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of FGFR, MET, and EGFR (all already mapped) drives the invasion of cholangiocarcinoma.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of cholangiocarcinoma (interacting with the IDH-mutant metabolism; IDH1/2 already mapped).
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival and therapy resistance of cholangiocarcinoma cells.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the desmoplastic, immunosuppressive microenvironment of cholangiocarcinoma.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic dysregulation of cholangiocarcinoma.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the inflammation-driven tumorigenesis and microenvironment of cholangiocarcinoma.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the biliary inflammation and tumor microenvironment of cholangiocarcinoma.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory tumor microenvironment of cholangiocarcinoma.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory tumor microenvironment of cholangiocarcinoma.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the tumor microenvironment and biliary-inflammation-linked signaling of cholangiocarcinoma.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Immunotherapy: adding the checkpoint inhibitor durvalumab to chemotherapy is now standard for advanced biliary tract cancer, and MHC class II antigen presentation shapes the T-cell response that determines the benefit.
- `connects-to` → **[AXL receptor](../../03-molecular/axl-receptor/README.md)** — Invasion and resistance: the AXL receptor tyrosine kinase drives the epithelial-mesenchymal transition and treatment resistance of cholangiocarcinoma, a mechanism of progression beyond the FGFR and IDH targets already mapped.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell response: IL-2-driven T-cell expansion supports the anti-tumour immunity and adoptive-cell approaches under investigation for cholangiocarcinoma alongside checkpoint blockade (PD-1 already mapped).
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Desmoplastic fibrosis: the collagen-rich stroma laid down by cancer-associated fibroblasts (already mapped) forms the dense desmoplastic tumour characteristic of cholangiocarcinoma, obstructing bile ducts and limiting drug penetration.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Cholestasis and anaemia: biliary obstruction, chronic inflammation and gastrointestinal bleeding in cholangiocarcinoma lower haemoglobin, and the anaemia of chronic disease compounds the malaise of the advanced tumour.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative carcinogenesis: chronic biliary inflammation and cholestasis (from stones, flukes or sclerosing cholangitis) generate oxidative stress, to which xanthine oxidase contributes, driving the DNA damage that initiates cholangiocarcinoma.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Radiotherapy and photodynamic therapy: photon radiotherapy, including stereotactic body radiotherapy, and photodynamic therapy are used to control unresectable cholangiocarcinoma and relieve biliary obstruction, options for a tumour often diagnosed too late for surgery.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive microenvironment: IL-10 in the desmoplastic tumour microenvironment dampens the anti-tumour T-cell response (PD-1 already mapped), part of the immune evasion that limits immunotherapy in cholangiocarcinoma.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Inflammatory carcinogenesis: cyclooxygenase-2 and prostaglandin E2 from the chronic biliary inflammation (IL-6 already mapped) promote the proliferation and survival of transformed cholangiocytes, part of the inflammation-driven pathogenesis of cholangiocarcinoma.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises the tumour-associated macrophages (already mapped) toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the cold desmoplastic microenvironment that limits immunotherapy in cholangiocarcinoma.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Tumour-associated macrophages: the macrophages (CCL2 and TLR4 already mapped) infiltrate the desmoplastic stroma of cholangiocarcinoma, and their M2 polarisation supports the immunosuppression and progression of the biliary cancer.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Biliary copper: the liver (already mapped) excretes copper into bile, and the biliary obstruction of cholangiocarcinoma disrupts this excretion, linking copper handling to the cholestasis of the biliary cancer.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — M2 desmoplastic stroma: IL-13, with IL-4 (already mapped), drives the M2 macrophage (already mapped) arm of the immunosuppressive desmoplastic stroma (collagen already mapped) of cholangiocarcinoma.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Obesity and NAFLD risk: leptin is the obesity/NAFLD-related adipokine, a rising risk factor for the intrahepatic cholangiocarcinoma (liver already mapped) via the metabolic-inflammatory milieu.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic (cholesterol already mapped) risk of cholangiocarcinoma.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the obesity/NAFLD metabolic risk of cholangiocarcinoma.
- `connects-to` → **[NASH](../nash/README.md)** — NAFLD/NASH risk: the non-alcoholic steatohepatitis (the obesity/metabolic — leptin and adiponectin already mapped) is a rising risk factor for the intrahepatic cholangiocarcinoma.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — Combined HCC-CCA: the hepatocytes and the cholangiocytes share the progenitor origin; the combined hepatocellular-cholangiocarcinoma reflects the plasticity of the liver (already mapped).
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity, relevant to the checkpoint (PD-1 already mapped) immunotherapy of cholangiocarcinoma.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the desmoplastic immune microenvironment of cholangiocarcinoma.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment of cholangiocarcinoma.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the desmoplastic immune microenvironment of cholangiocarcinoma.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the tumour-promoting inflammation of cholangiocarcinoma (often arising on a background of chronic biliary inflammation).
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the cholangiocarcinoma microenvironment.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the chronic biliary inflammation and tumour-promoting microenvironment of cholangiocarcinoma.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, may mark the immune response of the cholangiocarcinoma microenvironment.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the desmoplastic (fibroblast already mapped) stroma of cholangiocarcinoma.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) contribute to the inflammatory dimension of the desmoplastic cholangiocarcinoma microenvironment.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement evasion: the cholangiocarcinoma cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), tempering the complement attack within the tumour stroma.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Cholestatic iron: transferrin, the iron carrier, reflects the disordered iron handling of the chronic biliary inflammation and cholestasis that predispose to cholangiocarcinoma.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-TME axis: TSLP, from biliary epithelium (already mapped) and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2 immunosuppression of the biliary tumour microenvironment of cholangiocarcinoma.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-biliary axis: bradykinin, via B1/B2 receptors on biliary endothelium (already mapped) and tumour stromal cells, amplifies the vascular permeability and the inflammatory milieu of the cholangiocarcinoma stroma.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Tumour-EPO axis: erythropoietin, via the EPOR on biliary tumour cells (already mapped), modulates the survival, proliferation, and the angiogenic (already mapped) dimension of cholangiocarcinoma.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell biliary axis: histamine, from mast cells (already mapped) in the cholangiocarcinoma stroma, amplifies the angiogenesis (already mapped) and the immunosuppressive inflammatory milieu of the biliary tumour microenvironment.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian-biliary axis: melatonin, via MT1/MT2 receptors on biliary epithelium (already mapped), modulates the oxidative stress and the cholestasis-driven (already mapped) carcinogenesis of cholangiocarcinoma.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Sex-hormone biliary axis: testosterone, via androgen receptors on biliary tumour cells (already mapped), modulates the sex-differential cholangiocarcinoma risk (higher in males) and the immunosuppressive tumour microenvironment.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — CCA prolactin: prolactin, via PRLR on macrophages (already mapped) and mast cells (already mapped), promotes biliary tumour immune escape; hyperprolactinaemia amplifies the NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of cholangiocarcinoma.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — CCA oxytocin: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates biliary TME inflammation; oxytocin deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of cholangiocarcinoma.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — CCA vasopressin: vasopressin, via V2R on endothelial cells (already mapped) and macrophages (already mapped), modulates biliary vascular tone; vasopressin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) tumour-promoting cascade of cholangiocarcinoma.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^abou-alfa-2020-claridy]: Abou-Alfa GK, Macarulla T, Javle MM, et al. Ivosidenib in IDH1-mutant, chemotherapy-refractory cholangiocarcinoma (ClarIDHy). *Lancet Oncol.* 2020;21(6):796-807. [doi:10.1016/S1470-2045(20)30157-1](https://doi.org/10.1016/S1470-2045(20)30157-1) · [PubMed 32416072](https://pubmed.ncbi.nlm.nih.gov/32416072/)
[^oh-2022-topaz1]: Oh DY, He AR, Qin S, et al. Durvalumab plus Gemcitabine and Cisplatin in Biliary Tract Cancer. *NEJM Evidence.* 2022;1(8):EVIDoa2200015. [doi:10.1056/EVIDoa2200015](https://doi.org/10.1056/EVIDoa2200015) · [PubMed 38319282](https://pubmed.ncbi.nlm.nih.gov/38319282/)
