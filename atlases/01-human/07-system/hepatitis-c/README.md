---
schema: human-scale-entry/v1
id: hepatitis-c
name: Hepatitis C
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "HCV (Hepacivirus; positive-sense ssRNA; genotypes 1-6) infects 58M people globally; NS3/4A cleaves MAVS → IRF3 not activated → chronicity in 80%; direct-acting antivirals (SOF/VEL, GLE/PIB) achieve >95% cure; cirrhosis → HCC risk 1-5%/year; no vaccine exists."
aliases: ["HCV", "hepatitis C virus", "chronic hepatitis C", "HCV cirrhosis", "HCV RNA", "NS3/4A", "sofosbuvir", "DAA", "direct-acting antiviral", "Epclusa", "Mavyret", "HCV genotype", "Hepacivirus"]
sources:
  - id: li-2005-hcv-mavs-cleavage
    type: peer-reviewed
    cite: "Li XD, Sun L, Seth RB, Pineda G, Chen ZJ. Hepatitis C virus protease NS3/4A cleaves mitochondrial antiviral signaling protein off the mitochondria to evade innate immunity. Proc Natl Acad Sci USA. 2005;102(49):17717-17722."
    doi: "10.1073/pnas.0508531102"
    pmid: "16301520"
    url: "https://doi.org/10.1073/pnas.0508531102"
    accessed: "2026-06-08"
  - id: ghany-2019-hcv-treatment
    type: peer-reviewed
    cite: "Ghany MG, Morgan TR; AASLD-IDSA HCV Guidance Panel. Hepatitis C Guidance 2019 Update: AASLD-IDSA Recommendations for Testing, Managing, and Treating Hepatitis C Virus Infection. Hepatology. 2020;71(2):686-721."
    doi: "10.1002/hep.31060"
    pmid: "31816268"
    url: "https://doi.org/10.1002/hep.31060"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/mavs
    relation: connects-to
    note: "HCV NS3/4A cleaves MAVS at Cys508 → soluble cytoplasmic MAVS cannot activate TBK1/IRF3 → no IFN-β; NS3/4A also cleaves TRIF → TLR3 signaling blocked; dual evasion of cytosolic and endosomal RNA sensing; MAVS cleavage is the primary reason HCV establishes chronicity."
  - target: 01-human/03-molecular/irf3
    relation: connects-to
    note: "HCV NS3/4A cleaves MAVS → TBK1-IRF3 not activated; NS5A additionally blocks TBK1 → IRF3 not phosphorylated; selective IRF3 inactivation while NF-κB persists → pro-survival hepatocyte signals; IRF3 pathway suppression is the key mechanism driving HCV chronicity."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "HCV evades type I IFN: NS3/4A blocks MAVS → no IFN-β; NS5A blocks PKR; high baseline ISG expression (ISG15, MX1 maximally induced by low-grade IFN) predicts pegIFN-α failure; DAAs bypass IFN-dependent antiviral mechanisms and achieve >95% cure regardless of IFN sensitivity."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "Chronic HCV drives ISG pre-activation via low-grade IFN-α → STAT1/STAT2/ISGF3 saturated → pegIFN-α fails to induce additional antiviral ISGs; IL28B TT genotype = high baseline ISG expression → pegIFN non-response; DAAs achieve SVR regardless of STAT1/ISG baseline."
  - target: 01-human/07-system/hcc
    relation: connects-to
    note: "HCV cirrhosis → HCC incidence 1-5%/year (surveillance required); chronic HCV inflammation → NF-κB/STAT3 → hepatocyte proliferation under oxidative DNA damage → driver mutations (TP53, TERT, CTNNB1); DAA cure reduces HCC risk ~70% but established cirrhosis retains HCC risk."
  - target: 02-pathogen/01-viruses/hepatitis-c-virus
    relation: connects-to
    note: "Hepatitis C virus is a positive-sense RNA flavivirus whose NS3/4A protease cleaves MAVS to silence interferon, persisting in ~80% of those infected; unlike HBV it makes no nuclear reservoir, so direct-acting antivirals cure >95% — yet no vaccine exists."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Chronic hepatitis C smolders in the liver, activating stellate cells via TGF-β and driving fibrosis to cirrhosis; DAA cure (SVR) cuts hepatocellular carcinoma risk ~70% but established cirrhosis still needs surveillance, and FibroScan has largely replaced biopsy for staging."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "HCV chronically stimulates B cells by binding CD81, driving type II mixed cryoglobulinemia (purpura, vasculitis, MPGN, neuropathy) and a raised risk of marginal-zone and other B-cell lymphomas; antiviral cure resolves cryoglobulinemia in ~80%."
  - target: 01-human/07-system/hepatitis-b
    relation: connects-to
    note: "HCV and HBV both cause chronic hepatitis → cirrhosis → HCC yet differ: HCV is an RNA flavivirus with no latent reservoir, cured >95% by DAAs, and has no vaccine; HBV is a DNA virus whose nuclear cccDNA reservoir antivirals suppress but cannot clear, and is vaccine-preventable."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Chronic HCV activates hepatic stellate cells via TGF-β1 → myofibroblast transdifferentiation → collagen I/III deposition → progressive fibrosis (METAVIR F0–F4) → cirrhosis; DAA-induced SVR slows fibrogenesis but established cirrhosis persists, retaining HCC risk."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "HCV is metabolically active: the core protein degrades IRS-1/IRS-2 via PI3K/mTOR and SOCS3 → hepatic insulin resistance → type 2 diabetes (2–3× risk), which in turn accelerates fibrosis and HCC; DAA-induced SVR improves glycemic control and lowers incident diabetes."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "HCV and HIV commonly coinfect through shared blood-borne spread: HIV accelerates HCV liver fibrosis and cirrhosis, so coinfected patients are prioritized for direct-acting antiviral cure, which now clears HCV in most regardless of HIV status."
  - target: 01-human/07-system/follicular-lymphoma
    relation: connects-to
    note: "Chronic hepatitis C drives B-cell non-Hodgkin lymphomas including follicular and marginal-zone types: persistent antigen stimulation expands clonal B cells (also causing mixed cryoglobulinemia), and antiviral cure can make some HCV-associated lymphomas regress."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "Hepatitis C replicates in hepatocytes and rewires their lipid metabolism: the virus assembles on lipid droplets and uses hepatocyte lipoproteins, causing steatosis and insulin resistance—injuring the liver cell metabolically as well as by immune inflammation."
  - target: 01-human/07-system/dlbcl
    relation: connects-to
    note: "Hepatitis C drives B-cell non-Hodgkin lymphoma: chronic antigenic stimulation of B cells can progress to marginal-zone and diffuse large B-cell lymphoma, and antiviral cure can induce remission—cancer from immune stimulation, not direct transformation."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Hepatitis C injures the kidney through cryoglobulinemia: immune complexes of HCV and antibody deposit in glomeruli, causing membranoproliferative glomerulonephritis—so HCV is a treatable cause of renal failure, and antiviral cure can stabilize the nephropathy."
  - target: 01-human/07-system/sjogrens-syndrome
    relation: connects-to
    note: "Hepatitis C can mimic and overlap Sjögren's syndrome: chronic HCV causes sicca symptoms resembling Sjögren's, plus shared cryoglobulinemia and lymphoma risk—so HCV should be excluded when sicca and autoimmune features appear, as antiviral therapy can improve them."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Cytotoxic T cells decide hepatitis C's outcome: a vigorous, broad CD8 response clears acute infection, but in chronic HCV these cells become exhausted, sustaining viremia while their smoldering attack on infected hepatocytes drives the fibrosis."
  - target: 01-human/07-system/nash
    relation: connects-to
    note: "Hepatitis C and NASH both scar the liver and often overlap: HCV (especially genotype 3) directly induces steatosis, and coexisting metabolic fatty liver speeds fibrosis—so even after antiviral cure, metabolic liver disease can keep progression going."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Hepatitis C can masquerade as rheumatoid arthritis: HCV polyarthralgia and cryoglobulinemic arthritis mimic RA, and rheumatoid factor is often positive in both, so HCV must be excluded before immunosuppressing presumed RA and screened before biologics."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Hepatitis C is a slow fibrotic disease: decades of low-grade inflammation drive progressive liver scarring to cirrhosis, but unlike most fibrosis it can stabilize or even regress once direct-acting antivirals cure the infection—so timing of treatment matters."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Hepatitis C leaves marks on the skin: it is linked to porphyria cutanea tarda (blistering on sun-exposed skin), lichen planus, and the palpable purpura of cryoglobulinemic vasculitis—so dermatologic clues can be the first hint of silent infection."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Natural killer cells shape hepatitis C's course: strong NK responses help clear acute infection, but the virus blunts them to persist, so the balance of innate NK activity versus viral evasion partly decides who spontaneously clears HCV and who becomes chronic."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "Hepatitis C injures the glomerulus through cryoglobulins: virus-driven immune complexes deposit in the kidney, causing membranoproliferative glomerulonephritis—a major extrahepatic complication that antiviral cure can reverse."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Hepatitis C cryoglobulinemia consumes complement: the cold-precipitating immune complexes activate and deplete complement, so low C3/C4 is a clue to active cryoglobulinemic vasculitis affecting skin, nerves and kidney."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Hepatitis C usually becomes chronic when T-helper cells fail: a vigorous, sustained CD4 response can clear the virus, but HCV evades it and the exhausted helper response permits lifelong infection—until direct-acting antivirals cure it."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Hepatitis C lives off cholesterol and lipids: it enters hepatocytes via the LDL receptor and travels as a lipo-viral particle wrapped in fat, hijacking cholesterol metabolism so deeply that the infection alters the body's lipid profile."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Hepatitis C loads the liver with iron: chronic infection raises hepatic iron, and that iron fuels oxidative damage that speeds fibrosis and cancer risk—why iron overload worsens the disease and was once reduced to help."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Hepatitis C inflames the liver through its macrophages: activated Kupffer cells sustain the chronic inflammation and secrete signals that drive the stellate-cell fibrosis turning hepatitis into cirrhosis."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Advanced hepatitis C starves the blood of oxygen: cirrhosis opens abnormal lung vessels (hepatopulmonary syndrome) that shunt blood past gas exchange, causing hypoxemia and breathlessness that worsens on standing."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Hepatitis C disarms dendritic cells: the virus blunts these antigen-presenting sentinels so they prime only weak T-cell responses, a key reason the infection so often slips into lifelong chronic persistence."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Hepatitis C cirrhosis bleeds through the gut: portal hypertension swells fragile veins in the esophagus and bowel (varices) that can rupture into massive gastrointestinal bleeding, a lethal complication of advanced scarring."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Hepatitis C needs imaging surveillance even after cure: ultrasound and CT/MRI photons watch the scarred liver for hepatocellular carcinoma, whose risk persists once cirrhosis is established."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Advanced hepatitis C cirrhosis retains sodium and water as ascites, and the dilutional low blood sodium that follows marks decompensation and predicts worse survival."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Hepatitis C drives B-cell and plasma-cell clones that make cryoglobulins: these cold-precipitating immune complexes inflame small vessels, causing the rash, neuropathy and kidney disease of mixed cryoglobulinemia."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy caught hepatitis C's disguise: the virus travels as a lipoviral particle, cloaked in host lipoproteins, slipping into liver cells through the LDL receptor it borrows along with cholesterol uptake."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "Hepatitis C unsettles the thyroid: it is associated with autoimmune thyroiditis on its own, and the interferon once used to treat it frequently triggered thyroid dysfunction, both over- and underactive."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D mattered in hepatitis C: low levels were tied to advanced fibrosis and, in the interferon era, to a poorer chance of clearing the virus, marking the vitamin's link to antiviral immunity."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Hepatitis C drives a misfiring antibody response: the anti-HCV antibody screens for exposure but does not clear the virus, and chronic B-cell stimulation churns out the cold-precipitating cryoglobulins behind much of its extrahepatic disease."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Hepatitis C can inflame the nerves: its mixed cryoglobulinemia deposits immune complexes in the small vessels feeding peripheral nerves, producing a painful sensory neuropathy or mononeuritis multiplex."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Hepatitis C lowers the platelet count two ways: an immune ITP-like destruction and, once cirrhosis sets in, splenic sequestration and reduced thrombopoietin combine to leave the blood short of platelets."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "The kidney is a classic extrahepatic target: hepatitis C drives membranoproliferative glomerulonephritis through cryoglobulin immune complexes, spilling protein and blood into the urine and sometimes progressing to renal failure."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "The old cure crushed the marrow: interferon-and-ribavirin therapy was strongly myelosuppressive, dropping neutrophils and forcing dose cuts — a toxicity swept away by the modern direct-acting antivirals that cure HCV in weeks."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Transmission and pregnancy intersect: hepatitis C spreads mainly through blood but can pass mother-to-child and, less often, sexually, so screening in pregnancy and treating before conception help prevent the next infection."
  - target: 01-human/07-system/waldenstrom-macroglobulinemia
    relation: connects-to
    note: "Chronic HCV can drive a B-cell cancer: relentless antigen stimulation of B cells underlies its mixed cryoglobulinemia and a raised risk of B-cell lymphomas including marginal-zone and lymphoplasmacytic Waldenström-type disease, some of which regress when the virus is cured."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "HCV cirrhosis backs up into the spleen: portal hypertension enlarges it and traps platelets and white cells through hypersplenism, the low counts often the first laboratory hint of advanced liver scarring."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "The liver's stellate cells lay down the scar: chronic HCV inflammation activates hepatic stellate cells into collagen-secreting myofibroblasts, the engine of the fibrosis that progresses to cirrhosis over decades."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "It deranges glucose handling: HCV directly impairs insulin signaling in the liver, so chronic infection causes insulin resistance and type 2 diabetes more often than other liver diseases — a metabolic effect that often improves after cure."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Immune complexes attack small vessels: HCV-driven cryoglobulins lodge in capillary walls and inflame endothelium, producing the cryoglobulinemic vasculitis that damages skin, nerves and kidneys far from the liver."
  - target: 01-human/07-system/mantle-cell-lymphoma
    relation: connects-to
    note: "Chronic B-cell stimulation can turn malignant: by relentlessly driving B cells, HCV raises the risk of several non-Hodgkin lymphomas, and antiviral cure can sometimes regress these virus-driven lymphoproliferative disorders."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 drives the inflamed liver toward cancer: HCV proteins and IL-6 activate STAT3 in hepatocytes, a survival and proliferation signal that contributes to the hepatocellular carcinoma that can arise even after the virus is cleared."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "The infection is also a vascular risk factor: chronic HCV promotes systemic inflammation and is independently linked to accelerated atherosclerosis, raising the risk of coronary and carotid disease beyond the liver."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Cirrhosis from HCV tilts toward clotting: advanced liver disease rebalances hemostasis toward thrombosis, raising the risk of portal vein thrombosis and venous thromboembolism despite the prolonged clotting times."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "It reaches the brain as well as the liver: HCV causes fatigue and cognitive 'brain fog' through low-grade neuroinflammation, and — with the stigma of chronic infection and historic interferon therapy — carries a high rate of depression."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Chronic infection and cirrhosis lower the count: persistent HCV inflammation raises hepcidin while a scarred liver and hypersplenism worsen it, adding an anemia of chronic disease to the hematologic picture."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Its vascular inflammation reaches the brain: the systemic inflammation and accelerated atherosclerosis of chronic HCV, together with cryoglobulinemic vasculitis, raise the risk of ischemic stroke beyond the liver disease."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Cryoglobulins inflame the peripheral nerves: HCV-driven mixed cryoglobulinemia deposits immune complexes in the vasa nervorum, causing a painful peripheral neuropathy as a classic extrahepatic manifestation."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Advanced liver disease weakens bone: chronic HCV and its cirrhosis cause hepatic osteodystrophy through impaired vitamin D metabolism and bone turnover, raising the risk of osteoporosis and fractures."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "The virus can injure the heart muscle: HCV is associated with myocarditis and a dilated cardiomyopathy, and its systemic inflammation contributes to cardiovascular disease that can progress to heart failure."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Cirrhosis wrecks the digestive organ: chronic hepatitis C scars the liver into cirrhosis with portal hypertension, oesophageal varices, ascites and the bleeding and malabsorption of advanced liver disease."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It writes itself on the skin: hepatitis C is linked to porphyria cutanea tarda, lichen planus and the palpable purpura of cryoglobulinaemic vasculitis, distinctive cutaneous markers of the infection."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A chronic, cancer-linked infection breeds worry: even after cure, the cirrhosis, HCC-surveillance and past stigma of hepatitis C foster chronic health anxiety alongside its well-documented depression."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It scars the kidney through cryoglobulins: hepatitis C is the classic cause of cryoglobulinaemic membranoproliferative glomerulonephritis, presenting with proteinuria, haematuria and declining renal function."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "It hijacks B cells: chronic hepatitis C drives type II mixed cryoglobulinaemia and clonal B-cell expansion, fuelling autoimmunity, vasculitis and the lymphomas it predisposes to."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It unsettles hormones and glucose: hepatitis C is linked to autoimmune thyroiditis and strongly promotes insulin resistance and type 2 diabetes, even before cirrhosis develops."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It drives B-cell lymphoma: chronic hepatitis C, through sustained B-cell stimulation, causes marginal-zone, follicular and diffuse large B-cell lymphomas, with lymphadenopathy."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It inflames the nerves and clouds the mind: cryoglobulinaemic vasculitis causes a painful peripheral neuropathy, and hepatitis C is associated with fatigue and cognitive 'brain fog'."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It aches the joints and muscles: hepatitis C commonly causes arthralgia and a non-erosive arthritis, along with myalgia, as extrahepatic manifestations."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Its cryoglobulins can scar the lungs: hepatitis-C-associated mixed cryoglobulinaemia can cause interstitial lung disease and pulmonary vasculitis among its extrahepatic effects."
  - target: 03-medicine/01-modern/02-respiratory/corticosteroids
    relation: connects-to
    note: "Steroids treat its vasculitis: corticosteroids, with rituximab and antivirals, control the cryoglobulinaemic vasculitis that hepatitis C drives through chronic B-cell stimulation."
  - target: 03-medicine/01-modern/11-biologics/adalimumab
    relation: connects-to
    note: "Unlike hepatitis B, it tolerates biologics: anti-TNF drugs like adalimumab are relatively safe in chronic hepatitis C and do not reactivate it as they do hepatitis B, though monitoring continues."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "It quietly scars the lobule: hepatitis C smoulders in hepatocytes for decades, with lobular inflammation and (in genotype 3) steatosis driving the fibrosis and cirrhosis that precede liver failure and cancer."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "It seeds B-cell lymphomas: chronic HCV antigen stimulation drives B-cell non-Hodgkin lymphomas treated with chemotherapy — and clearing the virus with antivirals can itself regress indolent HCV-associated lymphoma."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Immunotherapy for its liver cancer: HCV-related hepatocellular carcinoma, even after viral cure, is treated with checkpoint inhibitors such as atezolizumab with bevacizumab when it reaches the advanced stage."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "It attacks the nerves through cryoglobulins: chronic hepatitis C generates cryoglobulin immune complexes that inflame small vessels supplying peripheral nerves, causing a painful sensorimotor neuropathy or mononeuritis multiplex."
  - target: 01-human/07-system/anca-vasculitis
    relation: connects-to
    note: "Two routes to small-vessel vasculitis: hepatitis C causes an immune-complex (cryoglobulinemic) vasculitis, contrasting with the pauci-immune ANCA-associated vasculitides—different mechanisms damaging the same small vessels."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "Beyond the liver, it injures vessels: hepatitis C cryoglobulinemic vasculitis inflames small and medium artery walls, and chronic HCV also accelerates atherosclerosis, raising cardiovascular as well as hepatic risk."
  - target: 01-human/07-system/cholangiocarcinoma
    relation: connects-to
    note: "Not just hepatocellular cancer: chronic HCV also raises the risk of intrahepatic cholangiocarcinoma, the bile-duct cancer, broadening the virus's oncogenic reach within the cirrhotic liver."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Chronic antigen drives B cells: persistent HCV stimulation expands germinal-centre B-cell clones, the root of mixed cryoglobulinaemia and the HCV-associated B-cell lymphomas that can regress with antiviral cure."
  - target: 01-human/07-system/immune-thrombocytopenia
    relation: connects-to
    note: "A secondary cause of low platelets: chronic HCV is a recognised trigger of immune thrombocytopenia, distinct from hypersplenic sequestration, and antiviral cure often resolves the thrombocytopenia."
  - target: 01-human/07-system/iga-nephropathy
    relation: connects-to
    note: "Cirrhotic and viral glomerulonephritis: chronic hepatitis C—and the cirrhosis it causes—impairs hepatic clearance of IgA immune complexes, producing secondary IgA deposition in the glomerulus alongside its better-known cryoglobulinaemic nephritis."
  - target: 01-human/07-system/aplastic-anemia
    relation: connects-to
    note: "Hepatitis-associated aplastic anaemia: a severe marrow-failure syndrome can follow an acute hepatitis (HCV among the implicated viruses), where an aberrant immune response destroys haematopoietic stem cells weeks later."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Coinfection and disrupted care: COVID-19 strained hepatitis C elimination programmes and direct-acting-antiviral access, while coinfection adds inflammatory and hepatic burden in vulnerable patients."
  - target: 01-human/03-molecular/rig-i
    relation: connects-to
    note: "Sensing and evasion: RIG-I detects HCV RNA and signals through MAVS to induce interferon, but the HCV NS3/4A protease cleaves both sensor and adaptor to blunt the antiviral response."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "T-cell exhaustion: chronic hepatitis C drives PD-1-mediated exhaustion of antiviral T cells, contributing to viral persistence before direct-acting antivirals achieve cure."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Oncogenic progression: MYC activation contributes to the hepatocellular carcinoma that can arise from HCV-driven cirrhosis even after viral clearance."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Stellate-cell fibrosis: PDGF released in the chronically infected liver activates hepatic stellate cells into collagen-secreting myofibroblasts, the engine of HCV-driven fibrosis and cirrhosis."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Insulin resistance and injury: HCV core protein and TNF-α impair hepatic insulin signalling and drive hepatocyte injury, explaining the steatosis and type 2 diabetes strongly associated with chronic hepatitis C."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Telomerase reactivation: TERT promoter mutation is the commonest genetic event in the hepatocellular carcinoma arising from HCV cirrhosis, immortalising transformed hepatocytes."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 clearance: IFN-γ from HCV-specific CD4 and CD8 T cells drives the non-cytolytic and effector responses that achieve spontaneous clearance in the minority who clear the virus, while a weak response permits chronicity."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Cytotoxic immunopathology: perforin-mediated CD8 killing of infected hepatocytes clears HCV but also drives the necroinflammation, so the host T-cell response — not the virus directly — causes much of the liver injury."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Dual innate evasion: HCV NS3/4A protease cleaves STING as well as MAVS, disabling both the cytosolic DNA and RNA sensing pathways — a key mechanism by which the virus blunts interferon induction to persist."
  - target: 01-human/03-molecular/baff
    relation: connects-to
    note: "B-cell lymphoproliferation: chronic HCV stimulation of B cells, supported by BAFF, drives the clonal expansion behind mixed cryoglobulinaemia, its vasculitis and membranoproliferative glomerulonephritis, and the raised risk of B-cell non-Hodgkin lymphoma."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Hepatic fibrosis: persistent HCV inflammation activates hepatic stellate cells to deposit collagen, the progressive fibrosis that over decades builds the cirrhosis on which most HCV hepatocellular carcinoma arises."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Hepatocellular carcinoma: HCV cirrhosis is a major cause of HCC, and although direct-acting antivirals now cure the infection, the residual cirrhotic liver still grows VEGF-driven vascular tumours that require ongoing surveillance."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Inflammation to cancer: HCV-driven hepatic IL-6 sustains the acute-phase and inflammatory response of chronic hepatitis C and, via the STAT3 already mapped, promotes the fibrogenesis and hepatocellular-carcinoma development of the disease."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Tolerance and persistence: HCV induces regulatory IL-10 that dampens antiviral T-cell responses, contributing to the immune tolerance behind the high rate of chronic infection."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Inflammatory liver injury: HCV activates the hepatic NLRP3 inflammasome and IL-1β, driving the chronic inflammatory injury that progresses to fibrosis and cirrhosis."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Survival and HCC: HCV NS5A and core proteins activate PI3K-AKT-mTOR signalling, promoting hepatocyte survival and contributing to the hepatocellular carcinoma that can follow chronic hepatitis C even after viral cure."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Inflammatory signalling: HCV core protein activates NF-κB, driving the chronic inflammatory and pro-survival signalling that promotes fibrosis and carcinogenesis in the infected liver."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Oxidative stress: HCV induces marked hepatocyte oxidative stress and dysregulates NRF2 antioxidant signalling, contributing to liver injury, steatosis and transformation."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Interferon signalling through JAK-STAT (type-I IFN and STAT1 mapped) is the antiviral axis against HCV that interferon-based therapy formerly exploited and that the virus actively antagonises."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "TLR-MyD88-NF-κB innate signalling (NF-κB mapped) drives the hepatic inflammation sustaining chronic hepatitis C."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β mapped) drives the progressive hepatic fibrosis of chronic hepatitis C that advances to cirrhosis and hepatocellular carcinoma."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 amplifies hepatic stellate-cell activation and fibrosis and supports the immune evasion of the hepatocellular carcinoma that complicates chronic hepatitis C."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "EZH2-mediated polycomb repression silences tumour-suppressor genes and contributes to the hepatocarcinogenesis of chronic hepatitis C."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "PI3K-AKT-mTOR signalling, modulated by HCV proteins, drives the proliferative and metabolic reprogramming of hepatitis-C-associated hepatocellular carcinoma."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "HCV-induced PI3K-AKT signaling inactivates FOXO, promoting hepatocyte survival and the metabolic dysregulation of chronic hepatitis C."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HCV proteins induce HIF-1α, supporting the angiogenesis and metabolic reprogramming of hepatitis-C-associated steatosis and hepatocarcinogenesis."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "HCV core and NS proteins dysregulate the cyclin-D-CDK4/6-RB axis to drive hepatocyte cell-cycle entry in hepatitis-C-related hepatocellular carcinoma."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the Wnt/β-catenin and survival signaling implicated in HCV-driven hepatocarcinogenesis."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation contributes to the malignant progression of chronic hepatitis C."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins amplify the necroinflammatory liver injury of chronic hepatitis C."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) is co-opted by HCV to support hepatocyte survival and viral persistence."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "HCV induces and subverts host autophagy to support its replication in hepatocytes."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation and hepatocarcinogenesis of chronic hepatitis C."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the hepatocyte lipid metabolism exploited by HCV replication in hepatitis C."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment contributes to the immune-mediated liver inflammation of hepatitis C."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the hepatocyte signaling and fibrogenic and oncogenic pathways of hepatitis C."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the intrahepatic leukocyte recruitment and fibrosis of hepatitis C."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the hepatic inflammation of hepatitis C."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the hepatic immune responses and fibrosis of hepatitis C."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "B-cell lymphoproliferation: chronic HCV drives clonal expansion of CD20-positive B cells, causing mixed cryoglobulinaemia and marginal-zone lymphoma that often regress with viral cure or rituximab, a defining extrahepatic manifestation."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "T-cell clearance: MHC class II-restricted CD4 T-cell help is required to clear acute HCV, and its failure permits the CD8 exhaustion (PD-1 already mapped) that establishes lifelong chronic infection."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Hepatic iron: chronic HCV suppresses hepcidin and promotes hepatic iron accumulation, and this iron overload accelerates the oxidative injury and fibrosis progression that lead toward cirrhosis and hepatocellular carcinoma."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Cryoglobulinaemia: chronic HCV drives B-cell (already mapped) production of mixed cryoglobulins, cold-precipitating IgM-IgG immune complexes that cause a systemic vasculitis, the commonest extrahepatic manifestation of the infection."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Ribavirin haemolysis: the ribavirin used in older HCV regimens causes a dose-limiting haemolytic anaemia that lowers haemoglobin, a toxicity now largely avoided by the interferon- and ribavirin-free direct-acting antivirals."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Antiviral T-cell response: IL-2-driven T-cell expansion generates the HCV-specific T cells needed to clear the virus, and their functional exhaustion (PD-1 already mapped) is central to the establishment of chronic infection."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative hepatic injury: the iron accumulation (hepcidin already mapped), steatosis and inflammation of chronic hepatitis C generate reactive oxygen species, to which xanthine oxidase contributes, driving the fibrosis toward cirrhosis and cancer."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Portal hypertension: as chronic hepatitis C progresses to cirrhosis, dysregulated nitric oxide contributes to the splanchnic vasodilation and portal hypertension (collagen already mapped for fibrosis) that cause its life-threatening complications."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Steatosis and insulin resistance: hepatitis C drives hepatic steatosis and insulin resistance (insulin already mapped), and the fall in the insulin-sensitising adiponectin contributes to the metabolic dimension that accelerates its liver disease."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Th1/Th2 balance: IL-4 drives the Th2 arm, and the balance between it and the Th1 response (IFN-γ already mapped) helps determine whether hepatitis C is cleared or persists as the chronic infection that DAAs now cure."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "Th17 fibrogenesis: IL-17 from Th17 cells contributes to the immune-mediated liver injury and the fibrosis (TGF-β and collagen already mapped) of chronic hepatitis C, part of the inflammation driving cirrhosis."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Adipokine and steatosis: leptin, with the fall in adiponectin (already mapped), links the metabolic state to the hepatic steatosis and insulin resistance (already mapped) that accelerate the fibrosis of chronic hepatitis C."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Profibrotic type-2 arm: IL-13, with IL-4 (already mapped), drives the M2 macrophage and profibrotic (TGF-β and collagen already mapped) response in the liver fibrosis of chronic hepatitis C."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc in chronic liver disease: the zinc deficiency common in chronic hepatitis C and cirrhosis impairs immune function and hepatic metabolism, and zinc supplementation has been studied as an antiviral adjunct."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipokine milieu: resistin, with leptin and adiponectin (already mapped), links the adipose-inflammatory state to the steatosis and insulin resistance (already mapped) that accelerate the fibrosis of chronic hepatitis C."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Cryoglobulinaemia B cells: the chronic HCV drives the clonal B-cell (BAFF and CD20 already mapped) expansion causing the mixed cryoglobulinaemic vasculitis and the risk of B-cell lymphoma."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Hepatic iron overload: the chronic hepatitis C causes the hepatic iron overload (the hepcidin already-mapped suppression), the iron worsening the oxidative injury and the fibrosis."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Kupffer-cell inflammation: the liver-resident macrophages (Kupffer cells) sense the HCV and drive the innate inflammation (IL-6 and TNF already mapped) and the fibrogenic signalling of chronic hepatitis C."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 antiviral arm: IL-12 polarises the Th1 (IFN-γ already mapped) response of the cytotoxic T-cell (already mapped) clearance of the HCV-infected hepatocytes."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension balancing the antiviral Th1 (IFN-γ already mapped) drive of chronic hepatitis C."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 IgE: the IgE (with IL-4 and IL-13 already mapped) reflects the type-2 immune dimension of the dysregulated type-1/type-2 balance of chronic hepatitis C."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune-mediated liver (already mapped) inflammation of chronic hepatitis C."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Treg exhaustion axis: the regulatory T cells suppress the antiviral T-cell (already mapped) response, contributing to the T-cell exhaustion (PD-1 already mapped) and the viral persistence of chronic hepatitis C."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast-cell fibrosis: the hepatic mast cells contribute to the type-2 (IL-4 and IL-13 already mapped) inflammation and the fibrosis (TGF-β already mapped) of chronic hepatitis C."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Cryoglobulin complement: the complement C5 and its activation (with C3 already mapped) mediate the mixed-cryoglobulinaemic vasculitis, an immune-complex complication of chronic hepatitis C."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling links the complement to the myeloid recruitment in the hepatic inflammation and the cryoglobulinaemic vasculitis of chronic hepatitis C."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Iron overload: transferrin, the iron carrier, reflects the hepatic iron accumulation that, with the disordered hepcidin (already mapped), aggravates the oxidative liver injury and fibrosis of chronic hepatitis C."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) engaged by the immune complexes of the mixed cryoglobulinaemic vasculitis of chronic hepatitis C."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway activated by the cryoglobulin immune complexes (immunoglobulin already mapped) of the vasculitis of chronic hepatitis C."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Fibrosis progression: osteopontin, a matricellular cytokine produced by the injured liver, is a marker and mediator of the fibrosis progression (TGF-β already mapped) of chronic hepatitis C."
---

# Hepatitis C

## Overview

**Hepatitis C** is a chronic liver disease caused by the **hepatitis C virus (HCV)** — a positive-sense single-stranded RNA virus of the family *Flaviviridae* (genus *Hepacivirus*). With an estimated **58 million people chronically infected** globally and ~1.5 million new infections per year (WHO), HCV remains a major cause of liver-related morbidity and mortality despite the existence of curative therapy. The virus causes chronic infection in approximately 80% of acutely infected individuals, eventually leading to liver fibrosis, cirrhosis, and hepatocellular carcinoma (HCC) in a significant proportion.

The defining feature of HCV biology is its extraordinary capacity for **innate immune evasion**: the HCV NS3/4A serine protease cleaves MAVS from the outer mitochondrial membrane [^li-2005-hcv-mavs-cleavage], selectively disabling the TBK1-IRF3-IFN-β axis while leaving NF-κB-driven pro-survival signaling intact. This molecular strategy underlies the virus's ability to establish lifelong infection in a fully immunocompetent host.

The discovery of **direct-acting antivirals (DAAs)** — agents targeting HCV-specific NS3/4A, NS5A, and NS5B — transformed HCV from an incurable chronic disease into one with >95% cure rates with 8–12 weeks of oral therapy [^ghany-2019-hcv-treatment]. This transformation represents one of the most dramatic successes in antiviral drug development, though global elimination targets remain constrained by diagnosis and access gaps.

**Epidemiology:**
- 58 million chronic infections worldwide; 290,000 HCV-attributable deaths/year
- Highest prevalence: Egypt (15%+, historical iatrogenic), Pakistan, Central Asia, East/North Africa, injection drug use populations globally
- Genotypes 1–6: GT1a/1b (North America, Europe — historically hardest to treat with IFN), GT2/3 (global), GT4 (Middle East, Africa), GT5/6 (South Africa, Southeast Asia)
- Modes of transmission: Blood-to-blood (injection drug use — dominant in high-income countries; unsafe healthcare injections — dominant globally); sexual transmission (low risk except HIV co-infection or rectal mucosa exposure); perinatal transmission (~5%)

## Structure

### HCV biology

HCV is an enveloped virus (~55-65 nm diameter) with a **9.6 kb positive-sense ssRNA genome** encoding a single polyprotein (~3,000 aa) cleaved by host and viral proteases:

| Protein | Type | Function |
|---------|------|----------|
| Core (C) | Structural | Nucleocapsid assembly; promotes lipid droplet association; suppresses apoptosis |
| E1, E2 | Structural | Envelope glycoproteins; E2 binds CD81 receptor; target of neutralizing antibodies; hypervariable region 1 (HVR1) of E2 mutates rapidly → immune evasion |
| p7 | Viroporin | Ion channel; facilitates virion maturation and release |
| NS2 | Non-structural | Cysteine protease; cleaves NS2-NS3 junction |
| NS3 | Non-structural | N-terminal serine protease (cleaves NS3-NS5B region with NS4A cofactor); C-terminal NTPase/helicase; target of protease inhibitors (glecaprevir, voxilaprevir, grazoprevir) |
| NS4A | Non-structural | NS3 protease cofactor and membrane anchor |
| NS4B | Non-structural | Induces ER-derived membranous web (replication organelle) |
| NS5A | Non-structural | RNA binding; replication complex assembly; IFN resistance; target of NS5A inhibitors (velpatasvir, pibrentasvir, daclatasvir) |
| NS5B | Non-structural | RNA-dependent RNA polymerase (RdRp); target of NS5B inhibitors (sofosbuvir, dasabuvir) |

### HCV entry

1. **CD81 binding**: HCV E2 hypervariable region binds tetraspanin **CD81** on hepatocytes (primary receptor); also binds SR-BI (scavenger receptor class B type I)
2. **Tight junction proteins**: Claudin-1 and occludin at hepatocyte tight junctions are essential co-receptors
3. **Endocytosis**: Clathrin-mediated → endosomal acidification → E1/E2 fusion → RNA release into cytoplasm
4. **Replication**: NS4B-induced **membranous web** (ER-derived replication compartment) → NS5B RdRp synthesizes negative-sense antigenome → new positive-sense genomes
5. **Assembly/release**: Core associates with lipid droplets → nucleocapsid assembled; virions bud into ER → trans-Golgi → secretion with VLDL pathway (lipoprotein association)

## Function

### Innate immune evasion (multi-layered)

HCV suppresses innate immunity at multiple nodes:

| Target | HCV protein | Mechanism |
|--------|------------|-----------|
| MAVS (TLR3-TRIF adaptor also) | NS3/4A protease | Cleavage of MAVS at Cys508 → releases MAVS from OMM; cleavage of TRIF at Cys372 → disrupts TLR3 → IRF3 |
| TBK1/IRF3 | NS5A | Binds TBK1 → blocks IRF3 phosphorylation; mechanism of ISG pre-activation without IFN-β induction |
| PKR | NS5A, E2 | Blocks PKR-mediated eIF2α phosphorylation → maintains hepatocyte translation despite dsRNA |
| JAK-STAT | NS5A, core | Blocks STAT1 phosphorylation; core protein activates SOCS3 → suppresses JAK-STAT |
| Apoptosis | Core, NS5A | Core activates Wnt/β-catenin; NS5A inhibits Bax-mediated apoptosis → hepatocyte survival despite viral damage |

The **net immunological state** in chronic HCV: low-grade IFN-α (from pDC sensing of circulating virus) drives baseline ISG expression (ISG15, MX1, OAS1) without IFN-β; NF-κB-driven inflammatory signals promote hepatocyte survival; T cell exhaustion (Tim-3, PD-1 upregulation) prevents viral clearance.

### IL28B/IFNL3 genetics

Polymorphisms near the *IL28B* gene (encoding IFN-λ3) predict spontaneous clearance and pegIFN/ribavirin response:
- **CC genotype** (rs12979860): ~45% spontaneous clearance; ~80% sustained virological response (SVR) with pegIFN/ribavirin (GT1)
- **TT genotype**: <15% spontaneous clearance; ~30-40% SVR; high baseline ISG expression (ISG15, OAS1) due to constitutive IFN-λ signaling → ISGF3 pathway already "exhausted" → pegIFN cannot induce additional response
- IL28B genotype is irrelevant for DAA therapy (>95% SVR regardless of genotype)

## Pathology

### Hepatic fibrosis and cirrhosis

Chronic HCV → portal triad inflammation → hepatic stellate cell (HSC) activation → TGF-β → collagen deposition → fibrosis (F0-F4 by METAVIR); cirrhosis (F4) develops in ~20% of patients after 20 years; accelerated by alcohol, HIV co-infection, male sex, age of infection acquisition.

**Assessment:** FibroScan (liver stiffness by transient elastography) has largely replaced liver biopsy; APRI and FIB-4 scores as non-invasive surrogate markers.

### Hepatocellular carcinoma (HCC)

HCV cirrhosis → HCC risk 1–5% per year (annual ultrasound surveillance ± AFP required):
- **Mechanism**: Chronic inflammation → NF-κB → compensatory hepatocyte proliferation under oxidative DNA damage → driver mutations (TP53, CTNNB1 — β-catenin, TERT promoter); HCV Core directly activates Wnt/β-catenin
- DAA-achieved SVR reduces HCC risk by ~70% but does not eliminate it — established cirrhosis retains surveillance requirement

### Extrahepatic manifestations

- **Type II cryoglobulinemia**: HCV binds CD81 on B cells → polyclonal → then monoclonal RF-producing B cell expansion → IgM RF + polyclonal IgG immune complexes → cryoprecipitate at low temperatures → vasculitis, purpura, membranoproliferative glomerulonephritis, peripheral neuropathy; treatment: DAA cure resolves cryoglobulinemia in ~80%
- **Lymphoma**: Chronic HCV B cell stimulation → marginal zone lymphoma, splenic lymphoma, DLBCL; cure rates higher after SVR
- **Insulin resistance / type 2 diabetes**: HCV Core activates IRS-1 degradation via PI3K/mTOR; improves after SVR
- **Thyroid disease**: Thyroiditis (autoimmune); aggravated by IFN-α treatment

### Diagnosis

- **Anti-HCV antibody** (ELISA): Screening; positive from ~6 weeks post-infection; persists after cure (not a marker of active infection)
- **HCV RNA (RT-PCR)**: Quantitative viral load (IU/mL); confirms active infection; used for treatment monitoring (week 4, end of treatment, 12 weeks post-treatment SVR12)
- **Genotype**: HCV genotyping assay (NS5B sequencing or line probe); important for some regimens but irrelevant for pan-genotypic DAAs
- **HCV core antigen**: Less sensitive than RNA PCR but simpler; useful in resource-limited settings

### Treatment

**Direct-acting antivirals (DAAs):**

| Regimen | Targets | Genotypes | Duration | SVR12 |
|---------|---------|-----------|----------|-------|
| SOF/VEL (Epclusa) | NS5B + NS5A | Pan-genotypic (GT1-6) | 12 weeks | >97% |
| GLE/PIB (Mavyret) | NS3/4A + NS5A | Pan-genotypic (GT1-6) | 8 weeks | >97% |
| LDV/SOF (Harvoni) | NS5A + NS5B | GT1/4/5/6 | 8–12 weeks | >94% |
| GZR/EBR (Zepatier) | NS3/4A + NS5A | GT1/4 | 12 weeks | >92% |

- **SVR12** (undetectable HCV RNA 12 weeks after end of treatment) = cure; durable in >99% of cases
- **Decompensated cirrhosis**: SOF/VEL ± ribavirin (GLE/PIB contraindicated)
- **DAA resistance**: NS5A resistance-associated substitutions (RASs) can reduce efficacy; voxilaprevir overcomes most NS5B/NS5A RASs
- **Monitoring**: LFT, CBC, renal function (sofosbuvir — dose adjust if eGFR <30 for certain regimens)
- **Drug interactions**: Rifampicin, carbamazepine, proton pump inhibitors (reduce ledipasvir absorption), amiodarone + sofosbuvir (bradycardia)

**No HCV vaccine exists** — high genetic diversity of E1/E2 hypervariable regions prevents broadly effective vaccine development; this remains a major gap in WHO elimination strategy.

### Prevention

- Harm reduction (needle exchange, opioid substitution therapy)
- Universal blood product screening (eliminated transfusion-acquired HCV in high-income settings)
- Healthcare injection safety (primary driver of HCV in low/middle-income settings)
- Treatment as prevention: DAA cure eliminates onward transmission

## Connections

**→ [MAVS](../../../03-molecular/mavs/)**: HCV NS3/4A serine protease cleaves MAVS at Cys508 → releases MAVS from outer mitochondrial membrane → soluble cytoplasmic MAVS cannot activate TBK1/IRF3 → no IFN-β → viral persistence; TRIF (TLR3 adaptor) is also cleaved by NS3/4A → dual evasion of endosomal and cytosolic RNA sensing.

**→ [IRF3](../../../03-molecular/irf3/)**: HCV NS3/4A cleaves MAVS upstream of TBK1-IRF3; NS5A additionally blocks TBK1 activity → IRF3 not phosphorylated → IFN-β not transcribed; selective IRF3 inactivation while NF-κB persists → pro-survival hepatocyte signaling; IRF3 pathway suppression is the key mechanism of HCV chronicity.

**→ [Type I Interferon](../../../03-molecular/type-i-interferon/)**: HCV evades type I IFN at multiple levels: NS3/4A blocks MAVS → no IFN-β induction; NS5A and NS5B block PKR and OAS; high baseline ISG expression (from chronic low-grade IFN) predicts pegIFN-α treatment failure (ISG15, MX1 already maximally induced); DAAs replaced IFN-based therapy.

**→ [STAT1](../../../03-molecular/stat1/)**: Chronic HCV establishes a state of ISG pre-activation via low-grade IFN-α: baseline STAT1/STAT2 signaling saturates the ISGF3 pathway → pegIFN-α/ribavirin fails to induce additional antiviral ISGs; elevated pretreatment ISG expression (IL28B genotype CC) predicts pegIFN non-response; DAA therapy bypasses STAT1-dependent IFN resistance.

**→ [HCC](../hcc/)**: HCV cirrhosis → HCC incidence 1-5% per year; HCV-driven HCC: chronic inflammation → NF-κB, TGF-β, IL-6/STAT3 → hepatocyte regeneration under oxidative stress → driver mutations; DAA cure reduces HCC risk by ~70% but does not eliminate it in established cirrhosis — surveillance continues.

- `connects-to` → **[Hepatitis C Virus](../../../02-pathogen/01-viruses/hepatitis-c-virus/README.md)** — Hepatitis C virus is a positive-sense RNA flavivirus whose NS3/4A protease cleaves MAVS to silence interferon, persisting in ~80% of those infected; unlike HBV it makes no nuclear reservoir, so direct-acting antivirals cure >95% — yet no vaccine exists.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Chronic hepatitis C smolders in the liver, activating stellate cells via TGF-β and driving fibrosis to cirrhosis; DAA cure (SVR) cuts hepatocellular carcinoma risk ~70% but established cirrhosis still needs surveillance, and FibroScan has largely replaced biopsy for staging.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — HCV chronically stimulates B cells by binding CD81, driving type II mixed cryoglobulinemia (purpura, vasculitis, MPGN, neuropathy) and a raised risk of marginal-zone and other B-cell lymphomas; antiviral cure resolves cryoglobulinemia in ~80%.
- `connects-to` → **[Hepatitis B](../hepatitis-b/README.md)** — HCV and HBV both cause chronic hepatitis → cirrhosis → HCC yet differ: HCV is an RNA flavivirus with no latent reservoir, cured >95% by DAAs, and has no vaccine; HBV is a DNA virus whose nuclear cccDNA reservoir antivirals suppress but cannot clear, and is vaccine-preventable.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — Chronic HCV activates hepatic stellate cells via TGF-β1 → myofibroblast transdifferentiation → collagen I/III deposition → progressive fibrosis (METAVIR F0–F4) → cirrhosis; DAA-induced SVR slows fibrogenesis but established cirrhosis persists, retaining HCC risk.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — HCV is metabolically active: the core protein degrades IRS-1/IRS-2 via PI3K/mTOR and SOCS3 → hepatic insulin resistance → type 2 diabetes (2–3× risk), which in turn accelerates fibrosis and HCC; DAA-induced SVR improves glycemic control and lowers incident diabetes.
- `connects-to` → **[HIV/AIDS](../hiv-aids/README.md)** — HCV and HIV commonly coinfect through shared blood-borne spread: HIV accelerates HCV liver fibrosis and cirrhosis, so coinfected patients are prioritized for direct-acting antiviral cure, which now clears HCV in most regardless of HIV status.
- `connects-to` → **[Follicular Lymphoma](../follicular-lymphoma/README.md)** — Chronic hepatitis C drives B-cell non-Hodgkin lymphomas including follicular and marginal-zone types: persistent antigen stimulation expands clonal B cells (also causing mixed cryoglobulinemia), and antiviral cure can make some HCV-associated lymphomas regress.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — Hepatitis C replicates in hepatocytes and rewires their lipid metabolism: the virus assembles on lipid droplets and uses hepatocyte lipoproteins, causing steatosis and insulin resistance—injuring the liver cell metabolically as well as by immune inflammation.
- `connects-to` → **[Diffuse Large B-Cell Lymphoma](../dlbcl/README.md)** — Hepatitis C drives B-cell non-Hodgkin lymphoma: chronic antigenic stimulation of B cells can progress to marginal-zone and diffuse large B-cell lymphoma, and antiviral cure can induce remission—cancer from immune stimulation, not direct transformation.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Hepatitis C injures the kidney through cryoglobulinemia: immune complexes of HCV and antibody deposit in glomeruli, causing membranoproliferative glomerulonephritis—so HCV is a treatable cause of renal failure, and antiviral cure can stabilize the nephropathy.
- `connects-to` → **[Sjögren's Syndrome](../sjogrens-syndrome/README.md)** — Hepatitis C can mimic and overlap Sjögren's syndrome: chronic HCV causes sicca symptoms resembling Sjögren's, plus shared cryoglobulinemia and lymphoma risk—so HCV should be excluded when sicca and autoimmune features appear, as antiviral therapy can improve them.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Cytotoxic T cells decide hepatitis C's outcome: a vigorous, broad CD8 response clears acute infection, but in chronic HCV these cells become exhausted, sustaining viremia while their smoldering attack on infected hepatocytes drives the fibrosis.
- `connects-to` → **[NASH](../nash/README.md)** — Hepatitis C and NASH both scar the liver and often overlap: HCV (especially genotype 3) directly induces steatosis, and coexisting metabolic fatty liver speeds fibrosis—so even after antiviral cure, metabolic liver disease can keep progression going.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Hepatitis C can masquerade as rheumatoid arthritis: HCV polyarthralgia and cryoglobulinemic arthritis mimic RA, and rheumatoid factor is often positive in both, so HCV must be excluded before immunosuppressing presumed RA and screened before biologics.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Hepatitis C is a slow fibrotic disease: decades of low-grade inflammation drive progressive liver scarring to cirrhosis, but unlike most fibrosis it can stabilize or even regress once direct-acting antivirals cure the infection—so timing of treatment matters.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Hepatitis C leaves marks on the skin: it is linked to porphyria cutanea tarda (blistering on sun-exposed skin), lichen planus, and the palpable purpura of cryoglobulinemic vasculitis—so dermatologic clues can be the first hint of silent infection.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Natural killer cells shape hepatitis C's course: strong NK responses help clear acute infection, but the virus blunts them to persist, so the balance of innate NK activity versus viral evasion partly decides who spontaneously clears HCV and who becomes chronic.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — Hepatitis C injures the glomerulus through cryoglobulins: virus-driven immune complexes deposit in the kidney, causing membranoproliferative glomerulonephritis—a major extrahepatic complication that antiviral cure can reverse.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Hepatitis C cryoglobulinemia consumes complement: the cold-precipitating immune complexes activate and deplete complement, so low C3/C4 is a clue to active cryoglobulinemic vasculitis affecting skin, nerves and kidney.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Hepatitis C usually becomes chronic when T-helper cells fail: a vigorous, sustained CD4 response can clear the virus, but HCV evades it and the exhausted helper response permits lifelong infection—until direct-acting antivirals cure it.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Hepatitis C lives off cholesterol and lipids: it enters hepatocytes via the LDL receptor and travels as a lipo-viral particle wrapped in fat, hijacking cholesterol metabolism so deeply that the infection alters the body's lipid profile.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Hepatitis C loads the liver with iron: chronic infection raises hepatic iron, and that iron fuels oxidative damage that speeds fibrosis and cancer risk—why iron overload worsens the disease and was once reduced to help.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Hepatitis C inflames the liver through its macrophages: activated Kupffer cells sustain the chronic inflammation and secrete signals that drive the stellate-cell fibrosis turning hepatitis into cirrhosis.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Advanced hepatitis C starves the blood of oxygen: cirrhosis opens abnormal lung vessels (hepatopulmonary syndrome) that shunt blood past gas exchange, causing hypoxemia and breathlessness that worsens on standing.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Hepatitis C disarms dendritic cells: the virus blunts these antigen-presenting sentinels so they prime only weak T-cell responses, a key reason the infection so often slips into lifelong chronic persistence.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Hepatitis C cirrhosis bleeds through the gut: portal hypertension swells fragile veins in the esophagus and bowel (varices) that can rupture into massive gastrointestinal bleeding, a lethal complication of advanced scarring.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Hepatitis C needs imaging surveillance even after cure: ultrasound and CT/MRI photons watch the scarred liver for hepatocellular carcinoma, whose risk persists once cirrhosis is established.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Advanced hepatitis C cirrhosis retains sodium and water as ascites, and the dilutional low blood sodium that follows marks decompensation and predicts worse survival.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — Hepatitis C drives B-cell and plasma-cell clones that make cryoglobulins: these cold-precipitating immune complexes inflame small vessels, causing the rash, neuropathy and kidney disease of mixed cryoglobulinemia.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy caught hepatitis C's disguise: the virus travels as a lipoviral particle, cloaked in host lipoproteins, slipping into liver cells through the LDL receptor it borrows along with cholesterol uptake.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — Hepatitis C unsettles the thyroid: it is associated with autoimmune thyroiditis on its own, and the interferon once used to treat it frequently triggered thyroid dysfunction, both over- and underactive.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D mattered in hepatitis C: low levels were tied to advanced fibrosis and, in the interferon era, to a poorer chance of clearing the virus, marking the vitamin's link to antiviral immunity.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Hepatitis C drives a misfiring antibody response: the anti-HCV antibody screens for exposure but does not clear the virus, and chronic B-cell stimulation churns out the cold-precipitating cryoglobulins behind much of its extrahepatic disease.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Hepatitis C can inflame the nerves: its mixed cryoglobulinemia deposits immune complexes in the small vessels feeding peripheral nerves, producing a painful sensory neuropathy or mononeuritis multiplex.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Hepatitis C lowers the platelet count two ways: an immune ITP-like destruction and, once cirrhosis sets in, splenic sequestration and reduced thrombopoietin combine to leave the blood short of platelets.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — The kidney is a classic extrahepatic target: hepatitis C drives membranoproliferative glomerulonephritis through cryoglobulin immune complexes, spilling protein and blood into the urine and sometimes progressing to renal failure.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — The old cure crushed the marrow: interferon-and-ribavirin therapy was strongly myelosuppressive, dropping neutrophils and forcing dose cuts — a toxicity swept away by the modern direct-acting antivirals that cure HCV in weeks.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Transmission and pregnancy intersect: hepatitis C spreads mainly through blood but can pass mother-to-child and, less often, sexually, so screening in pregnancy and treating before conception help prevent the next infection.
- `connects-to` → **[Waldenström Macroglobulinemia](../waldenstrom-macroglobulinemia/README.md)** — Chronic HCV can drive a B-cell cancer: relentless antigen stimulation of B cells underlies its mixed cryoglobulinemia and a raised risk of B-cell lymphomas including marginal-zone and lymphoplasmacytic Waldenström-type disease, some of which regress when the virus is cured.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — HCV cirrhosis backs up into the spleen: portal hypertension enlarges it and traps platelets and white cells through hypersplenism, the low counts often the first laboratory hint of advanced liver scarring.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — The liver's stellate cells lay down the scar: chronic HCV inflammation activates hepatic stellate cells into collagen-secreting myofibroblasts, the engine of the fibrosis that progresses to cirrhosis over decades.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — It deranges glucose handling: HCV directly impairs insulin signaling in the liver, so chronic infection causes insulin resistance and type 2 diabetes more often than other liver diseases — a metabolic effect that often improves after cure.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Immune complexes attack small vessels: HCV-driven cryoglobulins lodge in capillary walls and inflame endothelium, producing the cryoglobulinemic vasculitis that damages skin, nerves and kidneys far from the liver.
- `connects-to` → **[Mantle Cell Lymphoma](../mantle-cell-lymphoma/README.md)** — Chronic B-cell stimulation can turn malignant: by relentlessly driving B cells, HCV raises the risk of several non-Hodgkin lymphomas, and antiviral cure can sometimes regress these virus-driven lymphoproliferative disorders.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 drives the inflamed liver toward cancer: HCV proteins and IL-6 activate STAT3 in hepatocytes, a survival and proliferation signal that contributes to the hepatocellular carcinoma that can arise even after the virus is cleared.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — The infection is also a vascular risk factor: chronic HCV promotes systemic inflammation and is independently linked to accelerated atherosclerosis, raising the risk of coronary and carotid disease beyond the liver.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Cirrhosis from HCV tilts toward clotting: advanced liver disease rebalances hemostasis toward thrombosis, raising the risk of portal vein thrombosis and venous thromboembolism despite the prolonged clotting times.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — It reaches the brain as well as the liver: HCV causes fatigue and cognitive 'brain fog' through low-grade neuroinflammation, and — with the stigma of chronic infection and historic interferon therapy — carries a high rate of depression.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Chronic infection and cirrhosis lower the count: persistent HCV inflammation raises hepcidin while a scarred liver and hypersplenism worsen it, adding an anemia of chronic disease to the hematologic picture.
- `connects-to` → **[Stroke](../stroke/README.md)** — Its vascular inflammation reaches the brain: the systemic inflammation and accelerated atherosclerosis of chronic HCV, together with cryoglobulinemic vasculitis, raise the risk of ischemic stroke beyond the liver disease.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Cryoglobulins inflame the peripheral nerves: HCV-driven mixed cryoglobulinemia deposits immune complexes in the vasa nervorum, causing a painful peripheral neuropathy as a classic extrahepatic manifestation.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Advanced liver disease weakens bone: chronic HCV and its cirrhosis cause hepatic osteodystrophy through impaired vitamin D metabolism and bone turnover, raising the risk of osteoporosis and fractures.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — The virus can injure the heart muscle: HCV is associated with myocarditis and a dilated cardiomyopathy, and its systemic inflammation contributes to cardiovascular disease that can progress to heart failure.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Cirrhosis wrecks the digestive organ: chronic hepatitis C scars the liver into cirrhosis with portal hypertension, oesophageal varices, ascites and the bleeding and malabsorption of advanced liver disease.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It writes itself on the skin: hepatitis C is linked to porphyria cutanea tarda, lichen planus and the palpable purpura of cryoglobulinaemic vasculitis, distinctive cutaneous markers of the infection.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A chronic, cancer-linked infection breeds worry: even after cure, the cirrhosis, HCC-surveillance and past stigma of hepatitis C foster chronic health anxiety alongside its well-documented depression.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It scars the kidney through cryoglobulins: hepatitis C is the classic cause of cryoglobulinaemic membranoproliferative glomerulonephritis, presenting with proteinuria, haematuria and declining renal function.
- `connects-to` → **[Immune System](../immune-system/README.md)** — It hijacks B cells: chronic hepatitis C drives type II mixed cryoglobulinaemia and clonal B-cell expansion, fuelling autoimmunity, vasculitis and the lymphomas it predisposes to.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It unsettles hormones and glucose: hepatitis C is linked to autoimmune thyroiditis and strongly promotes insulin resistance and type 2 diabetes, even before cirrhosis develops.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It drives B-cell lymphoma: chronic hepatitis C, through sustained B-cell stimulation, causes marginal-zone, follicular and diffuse large B-cell lymphomas, with lymphadenopathy.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It inflames the nerves and clouds the mind: cryoglobulinaemic vasculitis causes a painful peripheral neuropathy, and hepatitis C is associated with fatigue and cognitive 'brain fog'.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It aches the joints and muscles: hepatitis C commonly causes arthralgia and a non-erosive arthritis, along with myalgia, as extrahepatic manifestations.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Its cryoglobulins can scar the lungs: hepatitis-C-associated mixed cryoglobulinaemia can cause interstitial lung disease and pulmonary vasculitis among its extrahepatic effects.
- `connects-to` → **[Corticosteroids](../../../03-medicine/01-modern/02-respiratory/corticosteroids/README.md)** — Steroids treat its vasculitis: corticosteroids, with rituximab and antivirals, control the cryoglobulinaemic vasculitis that hepatitis C drives through chronic B-cell stimulation.
- `connects-to` → **[Adalimumab](../../../03-medicine/01-modern/11-biologics/adalimumab/README.md)** — Unlike hepatitis B, it tolerates biologics: anti-TNF drugs like adalimumab are relatively safe in chronic hepatitis C and do not reactivate it as they do hepatitis B, though monitoring continues.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — It quietly scars the lobule: hepatitis C smoulders in hepatocytes for decades, with lobular inflammation and (in genotype 3) steatosis driving the fibrosis and cirrhosis that precede liver failure and cancer.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — It seeds B-cell lymphomas: chronic HCV antigen stimulation drives B-cell non-Hodgkin lymphomas treated with chemotherapy — and clearing the virus with antivirals can itself regress indolent HCV-associated lymphoma.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Immunotherapy for its liver cancer: HCV-related hepatocellular carcinoma, even after viral cure, is treated with checkpoint inhibitors such as atezolizumab with bevacizumab when it reaches the advanced stage.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — It attacks the nerves through cryoglobulins: chronic hepatitis C generates cryoglobulin immune complexes that inflame small vessels supplying peripheral nerves, causing a painful sensorimotor neuropathy or mononeuritis multiplex.
- `connects-to` → **[ANCA Vasculitis](../anca-vasculitis/README.md)** — Two routes to small-vessel vasculitis: hepatitis C causes an immune-complex (cryoglobulinemic) vasculitis, contrasting with the pauci-immune ANCA-associated vasculitides—different mechanisms damaging the same small vessels.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — Beyond the liver, it injures vessels: hepatitis C cryoglobulinemic vasculitis inflames small and medium artery walls, and chronic HCV also accelerates atherosclerosis, raising cardiovascular as well as hepatic risk.
- `connects-to` → **[Cholangiocarcinoma](../cholangiocarcinoma/README.md)** — Not just hepatocellular cancer: chronic HCV also raises the risk of intrahepatic cholangiocarcinoma, the bile-duct cancer, broadening the virus's oncogenic reach within the cirrhotic liver.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Chronic antigen drives B cells: persistent HCV stimulation expands germinal-centre B-cell clones, the root of mixed cryoglobulinaemia and the HCV-associated B-cell lymphomas that can regress with antiviral cure.
- `connects-to` → **[Immune Thrombocytopenia](../immune-thrombocytopenia/README.md)** — A secondary cause of low platelets: chronic HCV is a recognised trigger of immune thrombocytopenia, distinct from hypersplenic sequestration, and antiviral cure often resolves the thrombocytopenia.
- `connects-to` → **[IgA Nephropathy](../iga-nephropathy/README.md)** — Cirrhotic and viral glomerulonephritis: chronic hepatitis C—and the cirrhosis it causes—impairs hepatic clearance of IgA immune complexes, producing secondary IgA deposition in the glomerulus alongside its better-known cryoglobulinaemic nephritis.
- `connects-to` → **[Aplastic Anemia](../aplastic-anemia/README.md)** — Hepatitis-associated aplastic anaemia: a severe marrow-failure syndrome can follow an acute hepatitis (HCV among the implicated viruses), where an aberrant immune response destroys haematopoietic stem cells weeks later.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Coinfection and disrupted care: COVID-19 strained hepatitis C elimination programmes and direct-acting-antiviral access, while coinfection adds inflammatory and hepatic burden in vulnerable patients.
- `connects-to` → **[RIG-I](../../03-molecular/rig-i/README.md)** — Sensing and evasion: RIG-I detects HCV RNA and signals through MAVS to induce interferon, but the HCV NS3/4A protease cleaves both sensor and adaptor to blunt the antiviral response.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — T-cell exhaustion: chronic hepatitis C drives PD-1-mediated exhaustion of antiviral T cells, contributing to viral persistence before direct-acting antivirals achieve cure.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Oncogenic progression: MYC activation contributes to the hepatocellular carcinoma that can arise from HCV-driven cirrhosis even after viral clearance.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — Stellate-cell fibrosis: PDGF released in the chronically infected liver activates hepatic stellate cells into collagen-secreting myofibroblasts, the engine of HCV-driven fibrosis and cirrhosis.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Insulin resistance and injury: HCV core protein and TNF-α impair hepatic insulin signalling and drive hepatocyte injury, explaining the steatosis and type 2 diabetes strongly associated with chronic hepatitis C.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — Telomerase reactivation: TERT promoter mutation is the commonest genetic event in the hepatocellular carcinoma arising from HCV cirrhosis, immortalising transformed hepatocytes.
- `connects-to` → **[IFN-γ](../../03-molecular/ifn-gamma/README.md)** — IFN-γ from HCV-specific CD4 and CD8 T cells drives the responses that achieve spontaneous clearance in the minority who clear the virus, while a weak or exhausted T-cell response permits the chronicity seen in most.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated CD8 killing of infected hepatocytes clears HCV but also drives the necroinflammation—so the host T-cell response, not the virus directly, causes much of the liver injury that progresses to fibrosis and cirrhosis.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — HCV NS3/4A protease cleaves STING as well as MAVS, disabling both the cytosolic DNA and RNA sensing pathways—a key mechanism by which the virus blunts interferon induction to establish persistent infection.
- `connects-to` → **[BAFF](../../03-molecular/baff/README.md)** — Chronic HCV stimulation of B cells, supported by BAFF, drives the clonal expansion behind mixed cryoglobulinemia, its vasculitis and membranoproliferative glomerulonephritis, and the raised risk of B-cell non-Hodgkin lymphoma.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Persistent HCV inflammation activates hepatic stellate cells to deposit collagen, the progressive fibrosis that over decades builds the cirrhosis on which most HCV hepatocellular carcinoma arises.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — HCV cirrhosis is a major cause of HCC, and although direct-acting antivirals now cure the infection, the residual cirrhotic liver still grows VEGF-driven vascular tumors that require ongoing surveillance.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — HCV-driven hepatic IL-6 sustains the acute-phase and inflammatory response of chronic hepatitis C and, via the STAT3 already mapped, promotes the fibrogenesis and hepatocellular-carcinoma development of the disease.
- `connects-to` → **[Interleukin-10](../../03-molecular/il-10/README.md)** — HCV induces regulatory IL-10 that dampens antiviral T-cell responses, contributing to the immune tolerance behind the high rate of chronic infection.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — HCV activates the hepatic NLRP3 inflammasome and IL-1β, driving the chronic inflammatory injury that progresses to fibrosis and cirrhosis.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — HCV NS5A and core proteins activate PI3K-AKT-mTOR signaling, promoting hepatocyte survival and contributing to the hepatocellular carcinoma that can follow chronic hepatitis C even after viral cure.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — HCV core protein activates NF-κB, driving the chronic inflammatory and pro-survival signaling that promotes fibrosis and carcinogenesis in the infected liver.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — HCV induces marked hepatocyte oxidative stress and dysregulates NRF2 antioxidant signaling, contributing to liver injury, steatosis and transformation.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Interferon signaling through JAK-STAT (type-I IFN and STAT1 mapped) is the antiviral axis against HCV that interferon-based therapy formerly exploited and that the virus actively antagonizes.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR-MyD88-NF-κB innate signaling (NF-κB mapped) drives the hepatic inflammation sustaining chronic hepatitis C.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β mapped) drives the progressive hepatic fibrosis of chronic hepatitis C that advances to cirrhosis and hepatocellular carcinoma.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 amplifies hepatic stellate-cell activation and fibrosis and supports the immune evasion of the hepatocellular carcinoma that complicates chronic hepatitis C.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — EZH2-mediated polycomb repression silences tumor-suppressor genes and contributes to the hepatocarcinogenesis of chronic hepatitis C.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — PI3K-AKT-mTOR signaling, modulated by HCV proteins, drives the proliferative and metabolic reprogramming of hepatitis-C-associated hepatocellular carcinoma.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — HCV-induced PI3K-AKT signaling inactivates FOXO, promoting hepatocyte survival and the metabolic dysregulation of chronic hepatitis C.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HCV proteins induce HIF-1α, supporting the angiogenesis and metabolic reprogramming of hepatitis-C-associated steatosis and hepatocarcinogenesis.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — HCV core and NS proteins dysregulate the cyclin-D-CDK4/6-RB axis to drive hepatocyte cell-cycle entry in hepatitis-C-related hepatocellular carcinoma.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the Wnt/β-catenin and survival signaling implicated in HCV-driven hepatocarcinogenesis.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation contributes to the malignant progression of chronic hepatitis C.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins amplify the necroinflammatory liver injury of chronic hepatitis C.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) is co-opted by HCV to support hepatocyte survival and viral persistence.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — HCV induces and subverts host autophagy to support its replication in hepatocytes.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation and hepatocarcinogenesis of chronic hepatitis C.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the hepatocyte lipid metabolism exploited by HCV replication in hepatitis C.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte recruitment contributes to the immune-mediated liver inflammation of hepatitis C.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the hepatocyte signaling and fibrogenic and oncogenic pathways of hepatitis C.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the intrahepatic leukocyte recruitment and fibrosis of hepatitis C.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the hepatic inflammation of hepatitis C.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the hepatic immune responses and fibrosis of hepatitis C.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — B-cell lymphoproliferation: chronic HCV drives clonal expansion of CD20-positive B cells, causing mixed cryoglobulinaemia and marginal-zone lymphoma that often regress with viral cure or rituximab, a defining extrahepatic manifestation.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — T-cell clearance: MHC class II-restricted CD4 T-cell help is required to clear acute HCV, and its failure permits the CD8 exhaustion (PD-1 already mapped) that establishes lifelong chronic infection.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Hepatic iron: chronic HCV suppresses hepcidin and promotes hepatic iron accumulation, and this iron overload accelerates the oxidative injury and fibrosis progression that lead toward cirrhosis and hepatocellular carcinoma.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — Cryoglobulinaemia: chronic HCV drives B-cell (already mapped) production of mixed cryoglobulins, cold-precipitating IgM-IgG immune complexes that cause a systemic vasculitis, the commonest extrahepatic manifestation of the infection.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Ribavirin haemolysis: the ribavirin used in older HCV regimens causes a dose-limiting haemolytic anaemia that lowers haemoglobin, a toxicity now largely avoided by the interferon- and ribavirin-free direct-acting antivirals.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Antiviral T-cell response: IL-2-driven T-cell expansion generates the HCV-specific T cells needed to clear the virus, and their functional exhaustion (PD-1 already mapped) is central to the establishment of chronic infection.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative hepatic injury: the iron accumulation (hepcidin already mapped), steatosis and inflammation of chronic hepatitis C generate reactive oxygen species, to which xanthine oxidase contributes, driving the fibrosis toward cirrhosis and cancer.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Portal hypertension: as chronic hepatitis C progresses to cirrhosis, dysregulated nitric oxide contributes to the splanchnic vasodilation and portal hypertension (collagen already mapped for fibrosis) that cause its life-threatening complications.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Steatosis and insulin resistance: hepatitis C drives hepatic steatosis and insulin resistance (insulin already mapped), and the fall in the insulin-sensitising adiponectin contributes to the metabolic dimension that accelerates its liver disease.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Th1/Th2 balance: IL-4 drives the Th2 arm, and the balance between it and the Th1 response (IFN-γ already mapped) helps determine whether hepatitis C is cleared or persists as the chronic infection that DAAs now cure.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — Th17 fibrogenesis: IL-17 from Th17 cells contributes to the immune-mediated liver injury and the fibrosis (TGF-β and collagen already mapped) of chronic hepatitis C, part of the inflammation driving cirrhosis.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Adipokine and steatosis: leptin, with the fall in adiponectin (already mapped), links the metabolic state to the hepatic steatosis and insulin resistance (already mapped) that accelerate the fibrosis of chronic hepatitis C.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Profibrotic type-2 arm: IL-13, with IL-4 (already mapped), drives the M2 macrophage and profibrotic (TGF-β and collagen already mapped) response in the liver fibrosis of chronic hepatitis C.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc in chronic liver disease: the zinc deficiency common in chronic hepatitis C and cirrhosis impairs immune function and hepatic metabolism, and zinc supplementation has been studied as an antiviral adjunct.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipokine milieu: resistin, with leptin and adiponectin (already mapped), links the adipose-inflammatory state to the steatosis and insulin resistance (already mapped) that accelerate the fibrosis of chronic hepatitis C.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Cryoglobulinaemia B cells: the chronic HCV drives the clonal B-cell (BAFF and CD20 already mapped) expansion causing the mixed cryoglobulinaemic vasculitis and the risk of B-cell lymphoma.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Hepatic iron overload: the chronic hepatitis C causes the hepatic iron overload (the hepcidin already-mapped suppression), the iron worsening the oxidative injury and the fibrosis.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Kupffer-cell inflammation: the liver-resident macrophages (Kupffer cells) sense the HCV and drive the innate inflammation (IL-6 and TNF already mapped) and the fibrogenic signalling of chronic hepatitis C.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 antiviral arm: IL-12 polarises the Th1 (IFN-γ already mapped) response of the cytotoxic T-cell (already mapped) clearance of the HCV-infected hepatocytes.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension balancing the antiviral Th1 (IFN-γ already mapped) drive of chronic hepatitis C.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 IgE: the IgE (with IL-4 and IL-13 already mapped) reflects the type-2 immune dimension of the dysregulated type-1/type-2 balance of chronic hepatitis C.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune-mediated liver (already mapped) inflammation of chronic hepatitis C.
- `connects-to` → **[Regulatory T cell](../../04-cellular/regulatory-t-cell/README.md)** — Treg exhaustion axis: the regulatory T cells suppress the antiviral T-cell (already mapped) response, contributing to the T-cell exhaustion (PD-1 already mapped) and the viral persistence of chronic hepatitis C.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Mast-cell fibrosis: the hepatic mast cells contribute to the type-2 (IL-4 and IL-13 already mapped) inflammation and the fibrosis (TGF-β already mapped) of chronic hepatitis C.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Cryoglobulin complement: the complement C5 and its activation (with C3 already mapped) mediate the mixed-cryoglobulinaemic vasculitis, an immune-complex complication of chronic hepatitis C.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling links the complement to the myeloid recruitment in the hepatic inflammation and the cryoglobulinaemic vasculitis of chronic hepatitis C.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Iron overload: transferrin, the iron carrier, reflects the hepatic iron accumulation that, with the disordered hepcidin (already mapped), aggravates the oxidative liver injury and fibrosis of chronic hepatitis C.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) engaged by the immune complexes of the mixed cryoglobulinaemic vasculitis of chronic hepatitis C.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway activated by the cryoglobulin immune complexes (immunoglobulin already mapped) of the vasculitis of chronic hepatitis C.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Fibrosis progression: osteopontin, a matricellular cytokine produced by the injured liver, is a marker and mediator of the fibrosis progression (TGF-β already mapped) of chronic hepatitis C.
