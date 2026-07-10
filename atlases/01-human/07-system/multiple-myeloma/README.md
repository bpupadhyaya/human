---
schema: human-scale-entry/v1
id: multiple-myeloma
name: Multiple Myeloma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Plasma cell malignancy driven by CCND1 translocations (t(11;14)), RAS-MAPK mutations, and MYC. Bortezomib, lenalidomide, and daratumumab transformed outcomes; venetoclax is active in t(11;14) MM; BCMA-targeted CAR-T (cilta-cel, ide-cel) and bispecifics (teclistamab) are approved."
aliases: ["MM", "myeloma", "plasma cell myeloma", "Kahler disease", "RRMM", "relapsed/refractory myeloma", "smoldering myeloma", "MGUS", "PCM"]
sources:
  - id: kumar-2022-imwg-criteria
    type: peer-reviewed
    cite: "Kumar SK, Callander NS, Adekola K, et al. Multiple myeloma, version 3.2021, NCCN clinical practice guidelines in oncology. J Natl Compr Canc Netw. 2020;18(12):1685-1717."
    doi: "10.6004/jnccn.2020.0057"
    pmid: "33285519"
    url: "https://doi.org/10.6004/jnccn.2020.0057"
  - id: moreau-2022-teclistamab
    type: peer-reviewed
    cite: "Moreau P, Garfall AL, van de Donk NWCJ, et al. Teclistamab in relapsed or refractory multiple myeloma. N Engl J Med. 2022;387(6):495-505."
    doi: "10.1056/NEJMoa2203478"
    pmid: "35661166"
    url: "https://doi.org/10.1056/NEJMoa2203478"
  - id: martin-2023-carvykti
    type: peer-reviewed
    cite: "San-Miguel J, Dhakal B, Yong K, et al. Cilta-cel or standard care in lenalidomide-refractory multiple myeloma. N Engl J Med. 2023;389(4):335-347."
    doi: "10.1056/NEJMoa2303379"
    pmid: "37285856"
    url: "https://doi.org/10.1056/NEJMoa2303379"
cross_links:
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 is the primary myeloma cell survival cytokine; BMSCs produce IL-6 in response to myeloma adhesion → JAK1/2-STAT3 → MCL-1 and BCL-XL → anti-apoptosis; serum IL-6 and CRP correlate with disease activity; tocilizumab has limited clinical activity in MM."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "MYC is dysregulated in ~50-80% of relapsed MM via chr 8q24 amplification and MMSET-driven histone methylation; MYC drives plasma cell proliferation and immunoglobulin switch recombination; MYC transcription is sensitive to BET bromodomain inhibitors in MM models."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "BCL-2 is selectively overexpressed in t(11;14) MM (~15%); t(11;14) juxtaposes CCND1 near the IgH enhancer and correlates with BCL-2-high/BCL-XL-low expression; venetoclax achieves ORR ~40% in t(11;14) relapsed MM; CANOVA trial evaluated venetoclax + dexamethasone."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "VEGF is produced by myeloma cells and BMSCs → bone marrow angiogenesis → disease progression; VEGF promotes myeloma survival via VEGFR → PI3K-AKT; thalidomide and lenalidomide exert anti-angiogenic effects via VEGF suppression; bortezomib reduces VEGF secretion."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "MM cells secrete RANKL → osteoclast hyperactivation → osteolytic lesions and hypercalcemia; MM cells exploit OPG TRAIL-decoy function for survival; Xgeva (denosumab 120 mg Q4W) reduces skeletal-related events in MM bone disease."
  - target: 01-human/03-molecular/sclerostin
    relation: connects-to
    note: "MM-secreted DKK1 and osteocyte sclerostin synergistically block osteoblast Wnt → uncoupled osteolysis; sclerostin inhibition in MM preclinical models restores osteoblast function and reduces lytic lesions; anti-DKK1 antibody (BHQ880) is in clinical trials for MM bone disease."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "MM plasma cells use CXCL12/CXCR4 for bone marrow homing and survival; plerixafor (AMD3100, CXCR4 antagonist) + G-CSF mobilizes HSC for ASCT in MM (AMBER trial: superior day-1 CD34+ yield); CXCR4 expression on MM cells associates with marrow retention and drug resistance."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Multiple myeloma is a malignancy of plasma cells — antibody-secreting terminal B cells — that clonally expand in the marrow and pour out a single monoclonal immunoglobulin (M-protein); their prolific secretory machinery makes them exquisitely sensitive to proteasome inhibitors."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Multiple myeloma lives in the bone marrow, where malignant plasma cells co-opt stromal cells for IL-6 and CXCL12 survival signals and tip the RANKL/OPG balance toward osteoclasts; marrow plasma cells ≥10% (or a biopsy-proven plasmacytoma) plus CRAB features define the diagnosis."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "The kidney is a major myeloma target: filtered monoclonal free light chains precipitate with Tamm-Horsfall protein into obstructing tubular casts (cast nephropathy), and with hypercalcemia cause the renal failure of CRAB — reversible if light-chain production is cut quickly."
  - target: 01-human/07-system/waldenstrom-macroglobulinemia
    relation: connects-to
    note: "Multiple myeloma and Waldenström macroglobulinemia are both monoclonal plasma-cell/B-cell dyscrasias secreting a paraprotein but differ: myeloma makes IgG/IgA with lytic bone disease and renal failure, WM makes IgM with hyperviscosity and the MYD88 L265P mutation."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "Myeloma bone disease uncouples bone remodeling: tumor cells secrete DKK-1 and sclerostin that suppress osteoblasts and RANKL that activates osteoclasts, so the pure lytic lesions show no reactive new bone (cold on bone scan)—anti-RANKL agents aim to reset this."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Multiple myeloma is defined by a monoclonal immunoglobulin: the plasma-cell clone secretes a single intact IgG (or IgA) or free light chain—the M-protein seen as a serum spike—whose level tracks disease, while suppression of normal immunoglobulins causes myeloma's infection risk."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium is central to myeloma's CRAB complications: tumor-driven RANKL activates osteoclasts that dissolve bone, releasing calcium into blood—hypercalcemia causes confusion, constipation and kidney injury, treated urgently with hydration and bisphosphonates."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Myeloma bone disease and osteoporosis both fracture vertebrae but differ: myeloma carves discrete lytic 'punched-out' lesions, while osteoporosis is diffuse low bone density—new vertebral fractures in an older adult warrant a myeloma work-up."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photon radiotherapy is a key palliative tool in myeloma: though systemic, the disease responds to localized radiation that relieves bone pain and treats impending fractures, and is curative for solitary plasmacytoma—complementing the drugs that control marrow disease."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Multiple myeloma is the malignant end of B-cell maturation: it arises when a B cell becomes a clonal plasma cell, evolving from MGUS through smoldering myeloma—a step beyond the B cell, secreting monoclonal immunoglobulin instead of fighting infection."
  - target: 01-human/04-cellular/osteoclast
    relation: connects-to
    note: "Myeloma hijacks osteoclasts to destroy bone: malignant plasma cells secrete RANKL and cytokines that overactivate osteoclasts while suppressing osteoblasts, carving the punched-out lytic lesions, hypercalcemia and fractures that define myeloma bone disease."
  - target: 01-human/07-system/dlbcl
    relation: connects-to
    note: "Multiple myeloma and DLBCL are B-lineage cancers at opposite maturation ends: DLBCL is an aggressive nodal large B-cell lymphoma, myeloma a marrow plasma-cell tumor secreting monoclonal protein—and rarely a plasmablastic lymphoma blurs the line between them."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Anemia is a defining feature of multiple myeloma: plasma cells crowd the marrow and their cytokines suppress red-cell production, so falling hemoglobin (one of the CRAB criteria) is a common presenting sign alongside bone pain and renal failure."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Multiple myeloma cripples the immune system: as it expands one plasma-cell clone, normal antibody production collapses (immunoparesis), so recurrent infection is a top cause of death—and CD38-targeting and T-cell therapies now turn immunity back against the tumor."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Multiple myeloma is the malignant end of the B-cell lineage of the lymphatic system: it arises from plasma cells—the antibody factories that B cells become—so it produces a monoclonal immunoglobulin (M-protein) while crowding out normal immunity."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Multiple myeloma is a frontier for engineered T cells: BCMA-directed CAR-T cells and T-cell-engaging bispecific antibodies redirect cytotoxic T cells to kill plasma cells, producing deep remissions in disease that has relapsed after every drug class."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Antibody therapy for myeloma works through NK cells: daratumumab against CD38 and elotuzumab tag plasma cells for natural-killer-cell killing (ADCC), making these antibodies a backbone of modern treatment."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Myeloma plasma cells depend on NF-kB for survival: the bone-marrow niche and genetic lesions keep this pathway switched on, and proteasome inhibitors like bortezomib work partly by blocking NF-kB activation—starving the cell of its survival signal."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Multiple myeloma cells lean on autophagy to survive their own output: churning out immunoglobulin floods them with misfolded protein, so they use autophagy alongside the proteasome to clear it—which is why proteasome inhibitors like bortezomib are so lethal to them."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Multiple myeloma is nursed by marrow macrophages: these cells in the bone-marrow niche secrete survival signals and shield myeloma cells from drugs and immune attack, part of the supportive microenvironment the cancer depends on."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Multiple myeloma cripples dendritic cells: the tumor impairs these antigen-presenters, weakening immunity and helping it evade the T-cell response—so dendritic-cell vaccines are explored to rebuild anti-myeloma immunity."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Multiple myeloma starves the body of oxygen through anemia: plasma cells crowding the marrow choke red-cell production, so falling hemoglobin and fatigue—the 'A' of the CRAB criteria—are common presenting signs."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Myeloma can poison the heart via amyloid: misfolded light chains from the plasma cells deposit as AL amyloid in the heart muscle, stiffening it into a restrictive cardiomyopathy that is a major cause of death in the disease."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Myeloma reaches the liver in advanced disease: extramedullary plasma-cell deposits and light-chain amyloid can infiltrate it, causing hepatomegaly and organ dysfunction beyond the marrow where the cancer begins."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Myeloma's anemia is the 'A' of CRAB: marrow crowded with plasma cells and chronic inflammation suppress red-cell production and lock iron away, so fatigue from anemia is a common presenting symptom."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Myeloma frays the peripheral nerves: amyloid light chains deposit in nerves and the drug bortezomib is neurotoxic, so a painful peripheral neuropathy is both a feature and a treatment limit."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Myeloma's amyloid shows on the skin: AL amyloid from the plasma cells deposits in skin and soft tissue, causing periorbital purpura ('raccoon eyes') and an enlarged tongue, telltale signs of the disease."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy captures the myeloma plasma cell at work: its cytoplasm swells with rough endoplasmic reticulum churning out antibody, often packed into Russell bodies, while misfolded light chains form the fibrils of AL amyloid seen as a tangled mesh."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Myeloma can fake low sodium: the flood of monoclonal protein displaces water in the blood sample, so older analyzers report a spuriously low sodium — pseudohyponatremia — a lab artifact that signals the heavy paraprotein burden."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "Myeloma occasionally escapes the marrow into the spleen: extramedullary plasmacytomas and AL amyloid can lodge there, a sign of aggressive, treatment-resistant disease that has broken out of its usual bone-marrow home."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Myeloma leaves the lungs defenseless and can invade them: suppressed normal antibodies bring recurrent pneumonias, while plasmacytomas and AL amyloid occasionally deposit in the lung itself."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Myeloma's thick blood and rare CNS spread threaten the brain: heavy paraprotein can sludge the circulation into hyperviscosity with confusion and stroke, and dural or leptomeningeal plasmacytomas occasionally invade the nervous system."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Myeloma's kidney damage unsettles potassium: cast nephropathy and renal failure disturb its balance, and rapid tumor breakdown under treatment can spill potassium into the blood, threatening the heart."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Myeloma is a rogue antibody factory: a single plasma-cell clone floods the blood with one monoclonal protein (the M-spike) seen on electrophoresis while the other antibodies fall silent, and the CD38 on its surface is the bullseye for daratumumab therapy."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Infection is the great killer in myeloma: the crowded marrow and the silenced normal antibodies (immunoparesis) leave neutrophils few and ineffective, a vulnerability that proteasome-inhibitor and chemotherapy regimens only deepen."
  - target: 01-human/03-molecular/albumin
    relation: connects-to
    note: "Albumin helps stage the disease: low serum albumin together with high beta-2-microglobulin defines the higher tiers of the International Staging System, the simple blood pair that grades a new myeloma's prognosis."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Its mainstay drugs are powerfully prothrombotic: the immunomodulators lenalidomide and thalidomide sharply raise the risk of deep-vein thrombosis and pulmonary embolism, so every patient on them needs aspirin or anticoagulant prophylaxis."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "A defining translocation switches on cyclin D1: t(11;14) juxtaposes CCND1 to the immunoglobulin enhancer in a major myeloma subtype, and these cyclin-D1-driven, BCL-2-dependent tumors are the ones that respond to venetoclax."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "The same plasma-cell clone can poison the heart: misfolded light chains deposit as AL amyloid between cardiomyocytes, stiffening the wall into a restrictive cardiomyopathy that is a leading cause of death in myeloma-associated amyloidosis."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Myeloma cells lean on a survival hub: PI3K-AKT-mTOR signaling driven by marrow cytokines keeps the malignant plasma cells growing and resistant, so mTOR inhibitors are studied to choke this axis alongside proteasome and immune therapies."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "The kidney is a frequent casualty: free light chains precipitate as casts that clog the tubules ('myeloma kidney'), and with hypercalcemia and amyloid they push many patients into chronic kidney disease, sometimes the first sign of the cancer."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "The marrow's fat cells feed the tumor: bone-marrow adipocytes secrete factors that nourish myeloma plasma cells and blunt drug response, helping explain why obesity raises myeloma risk and why the fatty marrow of aging is fertile ground."
  - target: 02-pathogen/02-bacteria/streptococcus-pneumoniae
    relation: connects-to
    note: "Myeloma silences normal antibody: the malignant clone suppresses healthy immunoglobulin production (immunoparesis), leaving patients open to encapsulated bacteria like pneumococcus — infection is a leading cause of death, prompting vaccination and prophylaxis."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Pain comes from bone and from the drugs: lytic vertebral lesions and the bortezomib and thalidomide used to treat myeloma both cause severe pain — the chemotherapy a classic dose-limiting peripheral neuropathy."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Light chains can poison the heart: AL amyloidosis from myeloma's free light chains deposits in the myocardium, causing a restrictive cardiomyopathy and heart failure that drives much of the disease's mortality."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6 from the marrow niche signals through STAT3: bone-marrow stromal IL-6 activates STAT3 in myeloma plasma cells, a survival pathway central to their dependence on the microenvironment and resistance to therapy."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Immune paralysis makes infection the great killer: myeloma suppresses normal antibody production and its therapy adds neutropenia, so overwhelming infection and sepsis are a leading cause of death."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "The marrow and inflammation both blunt the blood: plasma-cell crowding of the marrow plus the inflammatory cytokines and kidney disease of myeloma produce a prominent anemia of chronic disease."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: connects-to
    note: "Hypogammaglobulinemia and its therapy open the lung: myeloma's suppressed normal antibodies plus high-dose steroids and novel agents leave patients at risk of Pneumocystis pneumonia, often warranting prophylaxis."
  - target: 02-pathogen/01-viruses/hepatitis-b-virus
    relation: connects-to
    note: "Anti-CD38 and immunosuppression can reactivate it: daratumumab and the deep immunosuppression of myeloma therapy can reawaken latent hepatitis B, so screening and antiviral prophylaxis precede treatment."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "An incurable, painful cancer weighs on mood: the relentless bone pain, fractures and relapsing course of multiple myeloma, plus steroid mood effects, carry a substantial burden of depression."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "Its therapy reawakens shingles: bortezomib and daratumumab used for multiple myeloma characteristically reactivate latent varicella-zoster, so antiviral prophylaxis is standard during treatment."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Profound immune suppression opens the lung to mold: the immune paresis of myeloma plus high-dose steroids, transplant and novel agents can permit invasive aspergillosis."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "An incurable relapsing cancer breeds worry: the lifelong cycle of remission and relapse, fracture risk and continuous therapy in multiple myeloma fosters chronic health anxiety alongside depression."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It dissolves the skeleton: multiple myeloma drives osteoclasts to carve lytic bone lesions, causing pathological fractures, vertebral collapse and bone pain — the 'B' of its defining CRAB features."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It compresses and poisons the nerves: vertebral collapse causes spinal cord compression, and AL amyloid and bortezomib produce peripheral neuropathy, while hyperviscosity and hypercalcaemia cloud the brain."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Bone breakdown floods the blood with calcium: the osteolysis of multiple myeloma releases calcium, causing the hypercalcaemia — the 'C' of CRAB — that disturbs the calcium-PTH endocrine axis."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its light chains and drugs strike the heart: AL amyloidosis infiltrates the myocardium causing restrictive cardiomyopathy, and the proteasome inhibitor carfilzomib is cardiotoxic."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It shows on the skin through amyloid: AL amyloid deposits cause periorbital purpura and waxy skin papules, and cutaneous plasmacytomas can appear in advanced disease."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Amyloid and drugs disturb the gut: amyloid deposition causes macroglossia, malabsorption and hepatomegaly, while proteasome inhibitors commonly cause diarrhoea and nausea."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It leaves the lungs exposed and can invade them: the immunoparesis of myeloma invites recurrent pneumonia, and plasmacytomas or amyloid can cause pleural effusions and lung infiltration."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "It is treated by precision immunotherapies: anti-CD38 antibodies like daratumumab, proteasome inhibitors, immunomodulators and BCMA-directed CAR-T cells have transformed myeloma care."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Treatment threatens fertility: the alkylators and high-dose therapy with stem-cell transplant used in myeloma can impair fertility, relevant to younger patients."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "It eats holes in the skeleton: myeloma plasma cells activate osteoclasts and suppress osteoblasts, producing the punched-out lytic bone lesions, pathological fractures and hypercalcaemia of CRAB."
  - target: 03-medicine/01-modern/02-respiratory/corticosteroids
    relation: connects-to
    note: "Dexamethasone anchors every regimen: high-dose corticosteroids are directly cytotoxic to plasma cells and form the backbone of nearly all myeloma drug combinations."
  - target: 01-human/07-system/cll
    relation: connects-to
    note: "A fellow clonal B-lineage cancer: like chronic lymphocytic leukaemia, multiple myeloma is a clonal expansion of the mature B/plasma-cell lineage in older adults, the two among the commonest blood cancers."
  - target: 03-medicine/01-modern/13-cancer/car-t
    relation: connects-to
    note: "Engineered cells against the plasma cell: BCMA-directed CAR-T therapies (idecabtagene and ciltacabtagene) achieve deep remissions in relapsed multiple myeloma, targeting the B-cell maturation antigen that marks malignant plasma cells."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "Beyond the tubules, it scars the filter: monoclonal light chains and AL amyloid deposit in the glomerulus as light-chain deposition disease and amyloidosis, adding glomerular injury and proteinuria to the cast nephropathy of myeloma kidney."
  - target: 01-human/07-system/mds
    relation: connects-to
    note: "The late cost of its alkylators: melphalan and other DNA-damaging drugs used in myeloma, especially with autologous transplant, raise the risk of therapy-related myelodysplastic syndrome and acute leukaemia years later."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Cardiac amyloid and cardiotoxicity: AL amyloid from myeloma light chains infiltrates and stiffens the myocardium into a restrictive cardiomyopathy, and proteasome inhibitors like carfilzomib add further cardiotoxicity."
  - target: 01-human/07-system/cytokine-storm
    relation: connects-to
    note: "CRS from the newest therapies: BCMA-directed CAR-T cells and bispecific antibodies, now central to relapsed myeloma, commonly trigger cytokine release syndrome managed with tocilizumab."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Liver involvement: extramedullary myeloma and AL amyloid can deposit in the hepatic lobule, causing hepatomegaly and, with amyloid, cholestatic liver dysfunction."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Profound immunoparesis: myeloma suppresses normal antibody production, and anti-CD38 and BCMA-directed therapies deepen the deficit, leaving patients with severe COVID-19 and poor vaccine responses."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "Therapy-related leukaemia: alkylators such as melphalan and prolonged lenalidomide raise the risk of secondary myelodysplasia and acute myeloid leukaemia, a late complication in long-surviving myeloma patients."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Thrombosis and viscosity: high paraprotein levels can cause hyperviscosity with neurological symptoms, while immunomodulatory drugs like lenalidomide markedly raise the risk of arterial and venous thrombosis including stroke."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Niche survival signal: PI3K-AKT-mTOR signalling driven by the marrow microenvironment sustains myeloma plasma-cell survival and drug resistance."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Stromal crosstalk: Notch signalling between myeloma cells and bone-marrow stroma promotes survival, drug resistance and the osteoclast activation behind lytic bone disease."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Epigenetic dependence: EZH2 is overexpressed in multiple myeloma and contributes to its progression, an emerging epigenetic therapeutic target."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "Cyclin D dysregulation: nearly all myelomas dysregulate a cyclin D gene, partnering CDK4/6 to drive plasma-cell proliferation—the rationale for CDK4/6 inhibition."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Marrow microenvironment: TNF-α within the bone-marrow niche supports myeloma cell survival and, with RANKL, drives the osteoclast activation behind its lytic bone disease."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Hypoxic marrow: HIF-1α stabilised in the hypoxic myeloma marrow drives the VEGF angiogenesis and glycolytic metabolism that support the malignant plasma-cell clone."
  - target: 01-human/03-molecular/baff
    relation: connects-to
    note: "Plasma-cell survival: BAFF and APRIL from the marrow microenvironment sustain malignant plasma cells through BCMA, the survival axis now targeted by anti-BCMA CAR-T and bispecific antibodies in myeloma."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Proteostatic apoptosis: the heavy immunoglobulin output of myeloma cells makes them dependent on the proteasome, so bortezomib triggers terminal ER stress and caspase-3-mediated apoptosis."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Marrow macrophage support: CCL2 recruits macrophages into the myeloma marrow niche, where they protect the plasma-cell clone and contribute to drug resistance."
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "t(4;14) translocation: the t(4;14) translocation of multiple myeloma overexpresses FGFR3, a recurrent high-risk cytogenetic event that drives a more aggressive disease course and is a candidate therapeutic target."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Smouldering-to-active drive: IL-1β from the marrow microenvironment induces the IL-6 that fuels plasma-cell growth and bone disease, and blocking it slows the progression of smouldering to active multiple myeloma."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Anaemia of myeloma: inflammation-driven hepcidin elevation, alongside marrow infiltration, causes the functional iron-restricted anaemia that is among the most common presenting features of multiple myeloma."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Cellular immunotherapy: BCMA-directed CAR-T cells and bispecific antibodies (teclistamab), and the ADCC of daratumumab, redirect cytotoxic T and NK cells to kill myeloma plasma cells through perforin and granzyme, transforming relapsed disease."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement-dependent killing: the anti-CD38 antibody daratumumab kills myeloma cells partly through complement-dependent cytotoxicity, fixing C3 and the membrane-attack complex, one of its several immune effector mechanisms."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Hypercalcaemia of CRAB: the osteoclast-driven bone destruction of myeloma releases calcium, producing the hypercalcaemia — the C of the CRAB criteria — that causes confusion, constipation and the renal impairment defining symptomatic disease."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "RAS-MAPK driver: activating KRAS and NRAS mutations are among the commonest drivers in multiple myeloma, engaging the RAS-MAPK pathway to sustain plasma-cell proliferation."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "High-risk disease: TP53 deletion or mutation (del17p) defines high-risk multiple myeloma with poor response to therapy and shortened survival."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "Survival signalling: the PI3K-AKT-mTOR axis (AKT and mTOR already mapped) supports myeloma-cell survival downstream of IL-6 and the bone-marrow microenvironment."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Central survival axis: IL-6 from the bone-marrow microenvironment signals through JAK-STAT3 (IL-6 and STAT3 already mapped) as the central survival and proliferation axis of malignant plasma cells in multiple myeloma."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Proteasome-inhibitor resistance: NRF2 antioxidant signalling counters the proteasome-inhibitor-induced oxidative and proteotoxic stress, contributing to bortezomib resistance in multiple myeloma."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "RAS proliferation: RAS-ERK signalling (KRAS already mapped) is among the most frequently activated proliferative pathways in multiple myeloma."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β in the marrow microenvironment suppresses osteoblast differentiation — contributing to myeloma bone disease — and dampens antitumour immunity in multiple myeloma."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 supports myeloma-cell survival and adhesion within the protective bone-marrow niche."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "Loss of PTEN restraint on PI3K-AKT-mTOR signalling (AKT, PIK3CA and mTOR mapped) promotes survival and drug resistance in multiple myeloma."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the antitumour immune response of multiple myeloma, relevant to its CAR-T and bispecific-antibody immunotherapy."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING modulates the inflammatory bone-marrow microenvironment of multiple myeloma."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling in the bone-marrow niche contributes to the immunosuppression and bone disease of multiple myeloma."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "PI3K-AKT-driven FOXO inactivation (AKT and PIK3CA already mapped) supports the survival of the malignant plasma cells of multiple myeloma."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the survival and proteostasis signaling of multiple myeloma cells, a candidate therapeutic target."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in multiple myeloma."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of the plasma-cell and cytokine receptors supports the survival of multiple myeloma cells."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of multiple myeloma."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the inflammatory bone-marrow microenvironment of multiple myeloma."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of the malignant plasma cells of multiple myeloma."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-family chemokine signaling (CXCL12/CXCR4 already mapped) participates in the bone-marrow homing of multiple myeloma."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic dysregulation of multiple myeloma."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the inflammatory bone-marrow microenvironment of multiple myeloma."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the myeloma-cell growth and osteoclast-driven bone disease of multiple myeloma."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "IL-10-mediated immunosuppression participates in the immune evasion of multiple myeloma."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the plasma-cell survival signaling of multiple myeloma."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine (CD38/CD73-adenosine) signaling participates in the immunosuppressive bone-marrow microenvironment of multiple myeloma."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin participates in the myeloma-bone-disease and bone-marrow-microenvironment interactions of multiple myeloma."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Anaemia (the A of CRAB): marrow replacement by plasma cells and inflammation (hepcidin already mapped) suppress erythropoiesis, and the resulting anaemia with fatigue is often the presenting feature of multiple myeloma."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "BCMA CAR-T: IL-2-driven T-cell expansion powers the BCMA-directed CAR-T and bispecific-antibody therapies (perforin already mapped) that have transformed treatment of relapsed multiple myeloma."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immune microenvironment: multiple myeloma progressively suppresses T-cell immunity and antigen presentation, and MHC-based recognition underlies both the immune escape of the plasma-cell clone and the response to its immunotherapies."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Tumour lysis: treating a high-burden multiple myeloma can trigger tumour-lysis syndrome, releasing purines that xanthine oxidase converts to uric acid, adding to the renal risk (kidney already mapped) already posed by light-chain cast nephropathy."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Cardiac risk: carfilzomib can be cardiotoxic and coexisting AL amyloid can infiltrate the myocardium, so troponin elevation marks the cardiac injury that complicates multiple myeloma and its treatment."
  - target: 01-human/03-molecular/secretory-iga
    relation: connects-to
    note: "Immunoparesis: the expanding plasma-cell clone suppresses normal immunoglobulin production including secretory IgA (IgG already mapped), the immunoparesis that impairs mucosal defence and causes the recurrent infections central to myeloma mortality."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Osteolytic inflammation: prostaglandins from the myeloma and its marrow microenvironment amplify the osteoclast-driven bone resorption (RANKL and sclerostin already mapped), contributing to the lytic bone disease of multiple myeloma."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 marrow niche: IL-4 polarises the marrow macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), the nurturing niche cells that support the survival of the malignant plasma cells of multiple myeloma."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Marrow angiogenesis: nitric oxide with VEGF (already mapped) supports the increased bone-marrow (already mapped) angiogenesis of multiple myeloma, part of the vascular microenvironment sustaining the plasma-cell clone."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 marrow niche: IL-13, with IL-4 (already mapped), supports the M2 marrow-macrophage niche that nurtures the malignant plasma cells of multiple myeloma."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Marrow adipose support: the marrow adipocytes and their adipokine leptin support the myeloma plasma cells, and obesity — a leptin-high state — is an established risk factor for multiple myeloma."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Protective adipokine: adiponectin is low in obesity, and its fall (leptin already mapped) removes a brake on the plasma-cell clone, part of the marrow-adipose crosstalk linking obesity to multiple myeloma."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Marrow-adipose adipokine: resistin, with leptin and adiponectin (already mapped), is part of the marrow-adipocyte adipokine crosstalk of the obesity-myeloma link and the metabolic niche of the plasma-cell clone."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Interferon maintenance: type-I interferon was a historical maintenance therapy of multiple myeloma, and its signalling shapes the immune (NK cell already mapped) microenvironment of the marrow."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Immunosuppressive Tregs: the regulatory T cells of the myeloma marrow microenvironment (IL-10 and TGF-β already mapped) dampen the anti-myeloma immunity, a barrier to the T-cell (already mapped) therapies."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-myeloma immunity opposed by the immunosuppressive (Tregs already mapped) marrow microenvironment."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-myeloma response, opposing the immunosuppressive marrow microenvironment of multiple myeloma."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 arm of the immune microenvironment of the myeloma marrow."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Myeloma anaemia: the relative erythropoietin deficiency (the renal — kidney already mapped — impairment and the marrow infiltration) underlies the anaemia (haemoglobin already mapped) of the 'A' of the CRAB features of multiple myeloma."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immunosuppressive marrow microenvironment of multiple myeloma."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the myeloma marrow microenvironment (and the rare IgE myeloma)."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells of the marrow are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immunosuppressive myeloma microenvironment."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) shapes the myeloid and immunosuppressive dimension of the myeloma marrow microenvironment."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Bone/prognostic vitamin: the vitamin D deficiency is common in multiple myeloma, worsens the bone (RANKL already mapped) disease, and is associated with a poorer prognosis."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Daratumumab CDC: the complement C5 (with C3 and C5aR1 already mapped) is the effector of the complement-dependent cytotoxicity by which the anti-CD38 daratumumab kills the myeloma plasma cells (already mapped)."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement evasion: the myeloma cells recruit factor H (with the CD55/CD59 regulators) to restrain the alternative complement pathway (C3, C5 and C5aR1 already mapped), a resistance mechanism to the daratumumab complement-dependent killing."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Anaemia iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the anaemia of the marrow-replacing multiple myeloma."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Bone marrow stroma alarmin: TSLP from bone-marrow stromal cells promotes the plasma-cell (already mapped) survival and IMiD-resistance in multiple myeloma; TSLP-driven STAT3 (already mapped) signalling augments the bone-marrow niche support for the malignant plasma-cell clone."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell angiogenesis: histamine from the bone-marrow mast cells promotes VEGF (already mapped) angiogenesis and osteoclast activation in myeloma; H2 receptor signalling amplifies the NF-kB (already mapped) survival axis of the malignant plasma cells (already mapped)."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Bone marrow ECM: periostin in the myeloma bone-marrow stroma, downstream of TGF-β (already mapped), promotes integrin αV-mediated plasma-cell (already mapped) homing and adhesion-mediated drug resistance; elevated myeloma-stroma periostin correlates with disease progression."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Myeloma bone pain: bradykinin, via B2 receptor, amplifies prostaglandin (already mapped) and VEGF-driven (already mapped) bone pain and osteolysis in the myeloma bone microenvironment; kinins enhance osteoclast (already mapped) activation in myeloma bone lesions."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Myeloma complement regulation: C1-INH controls the classical-pathway arm (C3, C5 and C5aR1 already mapped) in the myeloma bone-marrow microenvironment, complementing factor H (already mapped) to limit complement-mediated bystander lysis of bone-marrow stromal cells."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Anti-myeloma melatonin: melatonin, via MT1 receptors on plasma cells (already mapped), triggers mitochondrial apoptosis (caspase-3 already mapped), reduces IL-6 (already mapped) signalling and augments NK-cell (already mapped) cytotoxicity against multiple myeloma."
---

# Multiple Myeloma

## Overview

**Multiple myeloma (MM)** is a hematologic malignancy of terminally differentiated **plasma cells** — long-lived antibody-secreting B cells resident in the bone marrow. Malignant plasma cells accumulate in the bone marrow → monoclonal immunoglobulin (M-protein) production → end-organ damage (**CRAB criteria**: hyperCalcemia, Renal failure, Anemia, Bone lesions). MM accounts for ~10% of all hematologic malignancies and ~1-2% of all cancers — approximately 35,000 new cases and 12,000 deaths annually in the United States [^kumar-2022-imwg-criteria].

MM evolves from precursor conditions through a well-defined continuum:
- **MGUS (monoclonal gammopathy of undetermined significance):** M-protein <3 g/dL, <10% plasma cells in marrow, no CRAB; prevalent (~3% of adults >50); risk of progression to MM/WM/lymphoma ~1%/year
- **Smoldering multiple myeloma (SMM):** M-protein ≥3 g/dL OR ≥10-60% plasma cells, no CRAB; higher progression risk (10-15%/year in high-risk SMM); treatment of high-risk SMM actively studied (AQUILA trial: daratumumab delays progression)
- **Active MM:** CRAB criteria or biomarkers of near-inevitable end-organ damage (>60% plasma cells, involved/uninvolved FLC ratio >100, >1 focal lesion on MRI)

**Epidemiology and risk factors:**
- African American populations have 2-3× higher incidence than white populations (higher MGUS prevalence); men slightly > women; median age at diagnosis ~69; rare <40
- Occupational exposures (ionizing radiation, benzene, herbicides) modestly increase risk
- Monoclonal B cell lineage origin: MM arises from post-germinal center, class-switched memory B cells that home to bone marrow → undergo somatic hypermutation → differentiate toward plasma cell fate but accumulate oncogenic events preventing terminal differentiation arrest

**Molecular subtypes (by primary cytogenetic event):**
- **Hyperdiploid MM (HRD, ~55%):** Odd-numbered chromosomal trisomies (3, 5, 7, 9, 11, 15, 19, 21); relatively favorable prognosis; commonly activates CCND1/D2/D3 via trisomy
- **Translocation-based MM (~45%):**
  - **t(11;14)(q13;q32) (~15-20%):** CCND1 → IgH enhancer; low grade, CD20+, lymphoplasmacytic morphology; BCL-2-high → venetoclax-sensitive; best prognosis among translocations
  - **t(4;14)(p16;q32) (~15%):** FGFR3 and MMSET (NSD2 histone methyltransferase) → H3K36me2 → global chromatin opening → MYC upregulation; intermediate prognosis; bortezomib partially overcomes poor prognosis; FGFR3 targeted (infigratinib) under study
  - **t(14;16)(q32;q23) (~5%):** MAF → cyclin D2, integrin β7, CCND2; worst prognosis; novel agents improving outcomes; MAF target gene upregulation drives adhesion and drug resistance
  - **t(14;20)(q32;q12) (~1%):** MAFB; similar biology to t(14;16); poor prognosis
  - **t(6;14)(p21;q32) (~2%):** CCND3 → IgH; favorable prognosis

**High-risk genomic features:**
- **del(17p13)/TP53 loss:** Most adverse prognostic factor; ~10% at diagnosis, ~30% in RRMM; monoallelic deletion → residual TP53 haplo-insufficient; biallelic → complete p53 loss; extremely poor prognosis; clinical trials specifically targeting del(17p) MM needed
- **t(4;14), t(14;16), t(14;20), del(1p), gain(1q21):** ISS (International Staging System) criteria for high risk; R-ISS (Revised ISS) incorporates LDH + del(17p) + t(4;14) + t(14;16) for stage I-III risk stratification
- **Gain(1q21)/amplification:** Most common secondary event (~40% at diagnosis, ~70% RRMM); correlates with disease progression; 1q21 contains CKS1B (CDK substrate) and MCL-1; 1q amp correlates with shorter PFS with standard therapy
- **Chromothripsis:** Catastrophic chromosomal rearrangement in ~10% of RRMM → rapid clonal evolution and drug resistance

## Structure

### Bone marrow microenvironment and myeloma biology

**Myeloma-bone marrow stromal cell (BMSC) interactions:**
- MM cells home to bone marrow via CXCL12 (SDF-1)-CXCR4 axis; CXCR4 is highly expressed on MM cells → marrow homing and retention; CXCR4 inhibitors (plerixafor) mobilize MM cells out of protective marrow niche → sensitization to chemotherapy (hypothetical)
- **VLA-4 (integrin α4β1)-VCAM-1 axis:** MM cell VLA-4 binds BMSC VCAM-1 → cell adhesion-mediated drug resistance (CAM-DR); integrin signaling → NF-kB → MCL-1 and BCL-XL → anti-apoptosis; this explains why in vitro drug sensitivity often overestimates clinical efficacy
- **IL-6 paracrine circuit:** MM-BMSC contact → BMSC IL-6 secretion (10-100× basal) → JAK1/2 → STAT3 → MCL-1, BCL-XL, VEGF → MM survival; elevated serum IL-6 and CRP (acute phase reactant) are MM disease activity biomarkers

**Plasma cell biology:**
- **IRF4, BLIMP1 (PRDM1), XBP1:** Master transcription factors of plasma cell identity; IRF4 is required for MM survival (IRF4 knockdown → MM apoptosis); BLIMP1 drives terminal differentiation and immunoglobulin secretion; XBP1 is the unfolded protein response (UPR) regulator of the ER secretory pathway — essential for managing massive Ig production
- **Immunoproteasome:** Plasma cells have extremely high proteasome activity to clear misfolded Ig chains; this dependence on proteasome → vulnerability to bortezomib (proteasome inhibitor → accumulation of misfolded proteins → UPR → CHOP → apoptosis); MM is uniquely sensitive among hematologic malignancies

**BCMA (B-cell maturation antigen, TNFRSF17):**
- BCMA is expressed selectively on plasma cells and MM cells (minimal normal tissue expression); binds APRIL and BAFF → NF-kB → plasma cell survival
- BCMA is the dominant target for new-generation MM immunotherapy: CAR-T cells (cilta-cel, ide-cel), bispecific T cell engagers (teclistamab, elranatamab), ADCs (belantamab mafodotin); BCMA is internalized rapidly after antibody binding → BCMA shedding (gamma-secretase cleavage → soluble BCMA) can compete for BCMA-targeting agents

**Osteolytic bone disease:**
- MM cells produce DKK1 (Wnt antagonist) and RANKL → osteoblast suppression + osteoclast activation → net bone destruction → lytic lesions, fractures, hypercalcemia
- Osteoclast-derived IL-6 and SDF-1 provide additional MM survival signals → bidirectional bone-myeloma crosstalk
- Bisphosphonates (zoledronic acid) and denosumab (anti-RANKL) are standard for all symptomatic MM — reduce skeletal-related events (SREs) and may have direct anti-myeloma effects (zoledronate inhibits osteoclast-derived IL-6)

## Function

### Clinical presentation and staging

**CRAB criteria (active MM requiring treatment):**
- **C** (Calcium): Serum calcium >11 mg/dL (>1 mg/dL above ULN)
- **R** (Renal): Creatinine >2 mg/dL or CrCl <40 mL/min attributable to myeloma (typically cast nephropathy from Ig light chains)
- **A** (Anemia): Hgb <10 g/dL or >2 g/dL below LLN; normochromic normocytic (bone marrow failure + EPO suppression)
- **B** (Bone): One or more lytic lesions on skeletal survey, CT, or PET-CT; or compression fractures

**Biomarkers of near-inevitable end-organ damage (SLiM-CRAB):**
- **S**ixty percent (≥60%) plasma cells in bone marrow
- **Li**ght chain ratio: Involved/uninvolved serum FLC ratio ≥100
- **M**RI: >1 focal lesion (≥5 mm) on MRI (independent of skeletal survey)

**M-protein characterization:**
- SPEP (serum protein electrophoresis) → M-spike quantification; immunofixation → M-protein isotype (IgG most common ~55%, IgA ~25%, IgD rare, IgE rare, non-secretory ~3%)
- **Serum free light chains (sFLC):** Kappa or lambda free light chains; FLC ratio (kappa/lambda or lambda/kappa) abnormal → diagnostic and monitoring value; FLC-only MM and non-secretory MM monitored exclusively by sFLC
- **Bence Jones protein (BJP):** Urinary light chains; 24-hour urine protein electrophoresis in all MM patients at diagnosis

**ISS and R-ISS staging:**
- **ISS:** Serum β2-microglobulin + albumin → Stage I (β2M <3.5, alb ≥3.5), II, III (β2M ≥5.5)
- **R-ISS:** ISS + del(17p)/t(4;14)/t(14;16) + LDH → Stage I-III; R-ISS III: 5-year OS ~40%

**Imaging:**
- Whole-body low-dose CT (WBLD-CT): Standard; detects lytic lesions ≥5 mm; superior to skeletal survey (plain X-ray); does not detect active marrow infiltration without lysis
- FDG-PET/CT: Detects active lesions (FDG-avid plasma cells); useful for staging, response assessment (complete metabolic response = good prognostic marker), and identifying extramedullary disease
- MRI: Best modality for spine involvement and bone marrow infiltration; diffuse low T1 signal → extensive marrow replacement; useful in smoldering MM for progression risk assessment

## Pathology

### Diagnosis

**Bone marrow biopsy and aspirate:** Required for diagnosis; clonal plasma cells identified by CD138+, CD38+, CD19- (unlike normal plasma cells — CD19+); light chain restriction (kappa or lambda clonal); flow cytometry and FISH (fluorescence in situ hybridization) for cytogenetic risk stratification

**FISH panel:** del(17p13), t(4;14), t(14;16), t(14;20), t(11;14), gain(1q21), del(1p32) — all at diagnosis; determines risk category and targeted therapy eligibility (t(11;14) → venetoclax)

**Minimal residual disease (MRD) assessment:**
- Next-generation flow (NGF, EuroFlow) or next-generation sequencing (NGS, clonoSEQ): Sensitivity 10^-5 to 10^-6; MRD negativity is a strong surrogate for PFS and OS in MM; FDA-approved as a clinical trial endpoint; MRD-guided treatment strategies (stopping therapy in MRD-neg patients, intensifying in MRD-pos) under active study (MASTER, MIDAS trials)

### Treatment

**Newly diagnosed multiple myeloma (NDMM) — transplant eligible:**
- **Induction (4-6 cycles):** VRd (bortezomib-lenalidomide-dexamethasone) or DaraVRd (daratumumab + VRd; PERSEUS trial: PFS benefit → FDA approved 2024)
- **Autologous stem cell transplant (ASCT):** High-dose melphalan (200 mg/m²) → stem cell rescue; PFS benefit vs. no transplant maintained in lenalidomide era (DETERMINATION trial); depth of response (MRD negativity) post-ASCT is key prognostic factor
- **Consolidation:** 2 additional cycles VRd (optional)
- **Maintenance:** Lenalidomide (10 mg/day) until progression (MYELOMA XI, CALGB 100104); daratumumab + lenalidomide if DaraVRd induction (AURIGA trial ongoing); bortezomib-based maintenance for del(17p)

**Newly diagnosed MM — transplant ineligible:**
- **DaraVMP** (daratumumab + bortezomib + melphalan + prednisone; ALCYONE): PFS and OS benefit; FDA approved
- **DaraRd** (daratumumab + lenalidomide + dexamethasone; MAIA): OS benefit vs. Rd; FDA approved for non-transplant NDMM
- **VRd-lite:** Bortezomib + lenalidomide + low-dose dexamethasone; standard for frail/elderly patients

**Relapsed/refractory myeloma (RRMM):**
- **Second-line after 1-3 prior lines (with daratumumab exposure):**
  - Carfilzomib (next-gen proteasome inhibitor, irreversible) + Rd (KRd; ASPIRE trial)
  - Isatuximab (anti-CD38) + carfilzomib + Rd (IsaKRd)
  - Elotuzumab (anti-SLAMF7) + Rd (ELOQUENT-2)
  - Ixazomib (oral proteasome inhibitor) + Rd (TOURMALINE-MM1)
- **Venetoclax:** t(11;14) MM; ORR ~40% in monotherapy; venetoclax + dexamethasone (CANOVA trial); BCL-2 dependence in t(11;14) due to low MCL-1/low BCL-XL expression; venetoclax + bortezomib (BELLINI trial showed OS detriment in non-t(11;14) → restrict to t(11;14))
- **BCMA-directed therapies [^moreau-2022-teclistamab] [^martin-2023-carvykti]:**
  - **Teclistamab (Tecvayli):** Anti-BCMA × anti-CD3 bispecific; ORR 63% in RRMM ≥3 prior lines (MajesTEC-1); FDA approved 2022; CRS (step-up dosing) and infections are key toxicities
  - **Elranatamab (Elrexfio):** Anti-BCMA × anti-CD3; ORR 61% (MagnetisMM-3); FDA approved 2023
  - **Idecabtagene vicleucel (ide-cel, Abecma):** BCMA-directed CAR-T; ORR 73% in triple-class refractory MM (KarMMa); FDA approved 2021; CRS and neurotoxicity; 4-1BB costimulatory domain
  - **Ciltacabtagene autoleucel (cilta-cel, Carvykti):** BCMA-targeted CAR-T; ORR 98% in RRMM ≥3 prior lines (CARTITUDE-1); PFS 27.7 months; FDA approved 2022; FDA approved in 2nd-line (CARTITUDE-4: superior PFS vs. standard therapy in 1-3 prior lines) [^martin-2023-carvykti]
  - **Belantamab mafodotin (Blenrep):** ADC; corneal toxicity (keratopathy → blurred vision) led to initial FDA withdrawal; restored conditional approval 2023 with DREAMM-3 data vs. pomalidomide
- **GPRC5D-directed bispecifics:** Talquetamab (anti-GPRC5D × anti-CD3); ORR 73% in RRMM (MonumenTAL-1); GPRC5D expressed on plasma cells and hair follicles → skin/nail toxicity; FDA approved 2023
- **Sequencing:** With multiple classes available, optimal sequencing depends on prior exposures, toxicity, t(11;14) status, and performance status; BCMA CAR-T preferred early in eligible patients (manufacturing lead time ~4-6 weeks)

**Supportive care:**
- **VTE prophylaxis:** Lenalidomide/thalidomide + steroids → thrombogenic; aspirin or LMWH based on risk score (IMWG risk model)
- **Infection prophylaxis:** Anti-viral (acyclovir), anti-Pneumocystis (TMP-SMX or dapsone), anti-fungal for high-dose steroids; IVIG for IgG <4 g/dL with recurrent infections
- **Bone protection:** Denosumab (preferred) or zoledronic acid × 2 years; calcium/vitamin D supplementation
- **EPO agents:** For anemia not corrected by disease therapy; ESAs avoid transfusion dependency

## Connections

- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — IL-6 is the primary myeloma cell survival cytokine; BMSCs produce IL-6 in response to myeloma adhesion → JAK1/2-STAT3 → MCL-1 and BCL-XL → anti-apoptosis; serum IL-6 and CRP correlate with disease activity; tocilizumab has limited clinical activity in MM.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — MYC is dysregulated in ~50-80% of relapsed MM via chr 8q24 amplification and MMSET-driven histone methylation; MYC drives plasma cell proliferation and immunoglobulin switch recombination; MYC transcription is sensitive to BET bromodomain inhibitors in MM models.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — BCL-2 is selectively overexpressed in t(11;14) MM (~15%); t(11;14) juxtaposes CCND1 near the IgH enhancer and correlates with BCL-2-high/BCL-XL-low expression; venetoclax achieves ORR ~40% in t(11;14) relapsed MM; CANOVA trial evaluated venetoclax + dexamethasone.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — VEGF is produced by myeloma cells and BMSCs → bone marrow angiogenesis → disease progression; VEGF promotes myeloma survival via VEGFR → PI3K-AKT; thalidomide and lenalidomide exert anti-angiogenic effects via VEGF suppression; bortezomib reduces VEGF secretion.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — MM cells secrete RANKL → osteoclast hyperactivation → osteolytic lesions and hypercalcemia; MM cells exploit OPG TRAIL-decoy function for survival; Xgeva (denosumab 120 mg Q4W) reduces skeletal-related events in MM bone disease.
- `connects-to` → **[Sclerostin](../../03-molecular/sclerostin/README.md)** — MM-secreted DKK1 and osteocyte sclerostin synergistically block osteoblast Wnt → uncoupled osteolysis; sclerostin inhibition in MM preclinical models restores osteoblast function and reduces lytic lesions; anti-DKK1 antibody (BHQ880) is in clinical trials for MM bone disease.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — MM plasma cells use CXCL12/CXCR4 for bone marrow homing and survival; plerixafor (AMD3100, CXCR4 antagonist) + G-CSF mobilizes HSC for ASCT in MM (AMBER trial: superior day-1 CD34+ yield); CXCR4 expression on MM cells associates with marrow retention and drug resistance.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — Multiple myeloma is a malignancy of plasma cells — antibody-secreting terminal B cells — that clonally expand in the marrow and pour out a single monoclonal immunoglobulin (M-protein); their prolific secretory machinery makes them exquisitely sensitive to proteasome inhibitors.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Multiple myeloma lives in the bone marrow, where malignant plasma cells co-opt stromal cells for IL-6 and CXCL12 survival signals and tip the RANKL/OPG balance toward osteoclasts; marrow plasma cells ≥10% (or a biopsy-proven plasmacytoma) plus CRAB features define the diagnosis.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — The kidney is a major myeloma target: filtered monoclonal free light chains precipitate with Tamm-Horsfall protein into obstructing tubular casts (cast nephropathy), and with hypercalcemia cause the renal failure of CRAB — reversible if light-chain production is cut quickly.
- `connects-to` → **[Waldenström Macroglobulinemia](../waldenstrom-macroglobulinemia/README.md)** — Multiple myeloma and Waldenström macroglobulinemia are both monoclonal plasma-cell/B-cell dyscrasias secreting a paraprotein but differ: myeloma makes IgG/IgA with lytic bone disease and renal failure, WM makes IgM with hyperviscosity and the MYD88 L265P mutation.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — Myeloma bone disease uncouples bone remodeling: tumor cells secrete DKK-1 and sclerostin that suppress osteoblasts and RANKL that activates osteoclasts, so the pure lytic lesions show no reactive new bone (cold on bone scan)—anti-RANKL agents aim to reset this.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — Multiple myeloma is defined by a monoclonal immunoglobulin: the plasma-cell clone secretes a single intact IgG (or IgA) or free light chain—the M-protein seen as a serum spike—whose level tracks disease, while suppression of normal immunoglobulins causes myeloma's infection risk.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium is central to myeloma's CRAB complications: tumor-driven RANKL activates osteoclasts that dissolve bone, releasing calcium into blood—hypercalcemia causes confusion, constipation and kidney injury, treated urgently with hydration and bisphosphonates.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Myeloma bone disease and osteoporosis both fracture vertebrae but differ: myeloma carves discrete lytic 'punched-out' lesions, while osteoporosis is diffuse low bone density—new vertebral fractures in an older adult warrant a myeloma work-up.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photon radiotherapy is a key palliative tool in myeloma: though systemic, the disease responds to localized radiation that relieves bone pain and treats impending fractures, and is curative for solitary plasmacytoma—complementing the drugs that control marrow disease.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — Multiple myeloma is the malignant end of B-cell maturation: it arises when a B cell becomes a clonal plasma cell, evolving from MGUS through smoldering myeloma—a step beyond the B cell, secreting monoclonal immunoglobulin instead of fighting infection.
- `connects-to` → **[Osteoclast](../../04-cellular/osteoclast/README.md)** — Myeloma hijacks osteoclasts to destroy bone: malignant plasma cells secrete RANKL and cytokines that overactivate osteoclasts while suppressing osteoblasts, carving the punched-out lytic lesions, hypercalcemia and fractures that define myeloma bone disease.
- `connects-to` → **[Diffuse Large B-Cell Lymphoma](../dlbcl/README.md)** — Multiple myeloma and DLBCL are B-lineage cancers at opposite maturation ends: DLBCL is an aggressive nodal large B-cell lymphoma, myeloma a marrow plasma-cell tumor secreting monoclonal protein—and rarely a plasmablastic lymphoma blurs the line between them.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Anemia is a defining feature of multiple myeloma: plasma cells crowd the marrow and their cytokines suppress red-cell production, so falling hemoglobin (one of the CRAB criteria) is a common presenting sign alongside bone pain and renal failure.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Multiple myeloma cripples the immune system: as it expands one plasma-cell clone, normal antibody production collapses (immunoparesis), so recurrent infection is a top cause of death—and CD38-targeting and T-cell therapies now turn immunity back against the tumor.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Multiple myeloma is the malignant end of the B-cell lineage of the lymphatic system: it arises from plasma cells—the antibody factories that B cells become—so it produces a monoclonal immunoglobulin (M-protein) while crowding out normal immunity.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Multiple myeloma is a frontier for engineered T cells: BCMA-directed CAR-T cells and T-cell-engaging bispecific antibodies redirect cytotoxic T cells to kill plasma cells, producing deep remissions in disease that has relapsed after every drug class.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Antibody therapy for myeloma works through NK cells: daratumumab against CD38 and elotuzumab tag plasma cells for natural-killer-cell killing (ADCC), making these antibodies a backbone of modern treatment.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Myeloma plasma cells depend on NF-kB for survival: the bone-marrow niche and genetic lesions keep this pathway switched on, and proteasome inhibitors like bortezomib work partly by blocking NF-kB activation—starving the cell of its survival signal.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Multiple myeloma cells lean on autophagy to survive their own output: churning out immunoglobulin floods them with misfolded protein, so they use autophagy alongside the proteasome to clear it—which is why proteasome inhibitors like bortezomib are so lethal to them.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Multiple myeloma is nursed by marrow macrophages: these cells in the bone-marrow niche secrete survival signals and shield myeloma cells from drugs and immune attack, part of the supportive microenvironment the cancer depends on.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Multiple myeloma cripples dendritic cells: the tumor impairs these antigen-presenters, weakening immunity and helping it evade the T-cell response—so dendritic-cell vaccines are explored to rebuild anti-myeloma immunity.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Multiple myeloma starves the body of oxygen through anemia: plasma cells crowding the marrow choke red-cell production, so falling hemoglobin and fatigue—the 'A' of the CRAB criteria—are common presenting signs.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Myeloma can poison the heart via amyloid: misfolded light chains from the plasma cells deposit as AL amyloid in the heart muscle, stiffening it into a restrictive cardiomyopathy that is a major cause of death in the disease.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Myeloma reaches the liver in advanced disease: extramedullary plasma-cell deposits and light-chain amyloid can infiltrate it, causing hepatomegaly and organ dysfunction beyond the marrow where the cancer begins.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Myeloma's anemia is the 'A' of CRAB: marrow crowded with plasma cells and chronic inflammation suppress red-cell production and lock iron away, so fatigue from anemia is a common presenting symptom.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Myeloma frays the peripheral nerves: amyloid light chains deposit in nerves and the drug bortezomib is neurotoxic, so a painful peripheral neuropathy is both a feature and a treatment limit.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Myeloma's amyloid shows on the skin: AL amyloid from the plasma cells deposits in skin and soft tissue, causing periorbital purpura ('raccoon eyes') and an enlarged tongue, telltale signs of the disease.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy captures the myeloma plasma cell at work: its cytoplasm swells with rough endoplasmic reticulum churning out antibody, often packed into Russell bodies, while misfolded light chains form the fibrils of AL amyloid seen as a tangled mesh.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Myeloma can fake low sodium: the flood of monoclonal protein displaces water in the blood sample, so older analyzers report a spuriously low sodium — pseudohyponatremia — a lab artifact that signals the heavy paraprotein burden.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — Myeloma occasionally escapes the marrow into the spleen: extramedullary plasmacytomas and AL amyloid can lodge there, a sign of aggressive, treatment-resistant disease that has broken out of its usual bone-marrow home.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Myeloma leaves the lungs defenseless and can invade them: suppressed normal antibodies bring recurrent pneumonias, while plasmacytomas and AL amyloid occasionally deposit in the lung itself.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Myeloma's thick blood and rare CNS spread threaten the brain: heavy paraprotein can sludge the circulation into hyperviscosity with confusion and stroke, and dural or leptomeningeal plasmacytomas occasionally invade the nervous system.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Myeloma's kidney damage unsettles potassium: cast nephropathy and renal failure disturb its balance, and rapid tumor breakdown under treatment can spill potassium into the blood, threatening the heart.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Myeloma is a rogue antibody factory: a single plasma-cell clone floods the blood with one monoclonal protein (the M-spike) seen on electrophoresis while the other antibodies fall silent, and the CD38 on its surface is the bullseye for daratumumab therapy.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Infection is the great killer in myeloma: the crowded marrow and the silenced normal antibodies (immunoparesis) leave neutrophils few and ineffective, a vulnerability that proteasome-inhibitor and chemotherapy regimens only deepen.
- `connects-to` → **[Albumin](../../03-molecular/albumin/README.md)** — Albumin helps stage the disease: low serum albumin together with high beta-2-microglobulin defines the higher tiers of the International Staging System, the simple blood pair that grades a new myeloma's prognosis.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Its mainstay drugs are powerfully prothrombotic: the immunomodulators lenalidomide and thalidomide sharply raise the risk of deep-vein thrombosis and pulmonary embolism, so every patient on them needs aspirin or anticoagulant prophylaxis.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — A defining translocation switches on cyclin D1: t(11;14) juxtaposes CCND1 to the immunoglobulin enhancer in a major myeloma subtype, and these cyclin-D1-driven, BCL-2-dependent tumors are the ones that respond to venetoclax.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — The same plasma-cell clone can poison the heart: misfolded light chains deposit as AL amyloid between cardiomyocytes, stiffening the wall into a restrictive cardiomyopathy that is a leading cause of death in myeloma-associated amyloidosis.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Myeloma cells lean on a survival hub: PI3K-AKT-mTOR signaling driven by marrow cytokines keeps the malignant plasma cells growing and resistant, so mTOR inhibitors are studied to choke this axis alongside proteasome and immune therapies.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — The kidney is a frequent casualty: free light chains precipitate as casts that clog the tubules ('myeloma kidney'), and with hypercalcemia and amyloid they push many patients into chronic kidney disease, sometimes the first sign of the cancer.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — The marrow's fat cells feed the tumor: bone-marrow adipocytes secrete factors that nourish myeloma plasma cells and blunt drug response, helping explain why obesity raises myeloma risk and why the fatty marrow of aging is fertile ground.
- `connects-to` → **[Streptococcus pneumoniae](../../../02-pathogen/02-bacteria/streptococcus-pneumoniae/README.md)** — Myeloma silences normal antibody: the malignant clone suppresses healthy immunoglobulin production (immunoparesis), leaving patients open to encapsulated bacteria like pneumococcus — infection is a leading cause of death, prompting vaccination and prophylaxis.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Pain comes from bone and from the drugs: lytic vertebral lesions and the bortezomib and thalidomide used to treat myeloma both cause severe pain — the chemotherapy a classic dose-limiting peripheral neuropathy.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Light chains can poison the heart: AL amyloidosis from myeloma's free light chains deposits in the myocardium, causing a restrictive cardiomyopathy and heart failure that drives much of the disease's mortality.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6 from the marrow niche signals through STAT3: bone-marrow stromal IL-6 activates STAT3 in myeloma plasma cells, a survival pathway central to their dependence on the microenvironment and resistance to therapy.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Immune paralysis makes infection the great killer: myeloma suppresses normal antibody production and its therapy adds neutropenia, so overwhelming infection and sepsis are a leading cause of death.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — The marrow and inflammation both blunt the blood: plasma-cell crowding of the marrow plus the inflammatory cytokines and kidney disease of myeloma produce a prominent anemia of chronic disease.
- `connects-to` → **[Pneumocystis jirovecii](../../../02-pathogen/03-fungi/pneumocystis-jirovecii/README.md)** — Hypogammaglobulinemia and its therapy open the lung: myeloma's suppressed normal antibodies plus high-dose steroids and novel agents leave patients at risk of Pneumocystis pneumonia, often warranting prophylaxis.
- `connects-to` → **[Hepatitis B Virus](../../../02-pathogen/01-viruses/hepatitis-b-virus/README.md)** — Anti-CD38 and immunosuppression can reactivate it: daratumumab and the deep immunosuppression of myeloma therapy can reawaken latent hepatitis B, so screening and antiviral prophylaxis precede treatment.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — An incurable, painful cancer weighs on mood: the relentless bone pain, fractures and relapsing course of multiple myeloma, plus steroid mood effects, carry a substantial burden of depression.
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — Its therapy reawakens shingles: bortezomib and daratumumab used for multiple myeloma characteristically reactivate latent varicella-zoster, so antiviral prophylaxis is standard during treatment.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Profound immune suppression opens the lung to mold: the immune paresis of myeloma plus high-dose steroids, transplant and novel agents can permit invasive aspergillosis.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — An incurable relapsing cancer breeds worry: the lifelong cycle of remission and relapse, fracture risk and continuous therapy in multiple myeloma fosters chronic health anxiety alongside depression.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It dissolves the skeleton: multiple myeloma drives osteoclasts to carve lytic bone lesions, causing pathological fractures, vertebral collapse and bone pain — the 'B' of its defining CRAB features.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It compresses and poisons the nerves: vertebral collapse causes spinal cord compression, and AL amyloid and bortezomib produce peripheral neuropathy, while hyperviscosity and hypercalcaemia cloud the brain.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Bone breakdown floods the blood with calcium: the osteolysis of multiple myeloma releases calcium, causing the hypercalcaemia — the 'C' of CRAB — that disturbs the calcium-PTH endocrine axis.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its light chains and drugs strike the heart: AL amyloidosis infiltrates the myocardium causing restrictive cardiomyopathy, and the proteasome inhibitor carfilzomib is cardiotoxic.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It shows on the skin through amyloid: AL amyloid deposits cause periorbital purpura and waxy skin papules, and cutaneous plasmacytomas can appear in advanced disease.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Amyloid and drugs disturb the gut: amyloid deposition causes macroglossia, malabsorption and hepatomegaly, while proteasome inhibitors commonly cause diarrhoea and nausea.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It leaves the lungs exposed and can invade them: the immunoparesis of myeloma invites recurrent pneumonia, and plasmacytomas or amyloid can cause pleural effusions and lung infiltration.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — It is treated by precision immunotherapies: anti-CD38 antibodies like daratumumab, proteasome inhibitors, immunomodulators and BCMA-directed CAR-T cells have transformed myeloma care.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Treatment threatens fertility: the alkylators and high-dose therapy with stem-cell transplant used in myeloma can impair fertility, relevant to younger patients.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — It eats holes in the skeleton: myeloma plasma cells activate osteoclasts and suppress osteoblasts, producing the punched-out lytic bone lesions, pathological fractures and hypercalcaemia of CRAB.
- `connects-to` → **[Corticosteroids](../../../03-medicine/01-modern/02-respiratory/corticosteroids/README.md)** — Dexamethasone anchors every regimen: high-dose corticosteroids are directly cytotoxic to plasma cells and form the backbone of nearly all myeloma drug combinations.
- `connects-to` → **[CLL](../cll/README.md)** — A fellow clonal B-lineage cancer: like chronic lymphocytic leukaemia, multiple myeloma is a clonal expansion of the mature B/plasma-cell lineage in older adults, the two among the commonest blood cancers.
- `connects-to` → **[CAR-T](../../../03-medicine/01-modern/13-cancer/car-t/README.md)** — Engineered cells against the plasma cell: BCMA-directed CAR-T therapies (idecabtagene and ciltacabtagene) achieve deep remissions in relapsed multiple myeloma, targeting the B-cell maturation antigen that marks malignant plasma cells.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — Beyond the tubules, it scars the filter: monoclonal light chains and AL amyloid deposit in the glomerulus as light-chain deposition disease and amyloidosis, adding glomerular injury and proteinuria to the cast nephropathy of myeloma kidney.
- `connects-to` → **[MDS](../mds/README.md)** — The late cost of its alkylators: melphalan and other DNA-damaging drugs used in myeloma, especially with autologous transplant, raise the risk of therapy-related myelodysplastic syndrome and acute leukaemia years later.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Cardiac amyloid and cardiotoxicity: AL amyloid from myeloma light chains infiltrates and stiffens the myocardium into a restrictive cardiomyopathy, and proteasome inhibitors like carfilzomib add further cardiotoxicity.
- `connects-to` → **[Cytokine Storm](../cytokine-storm/README.md)** — CRS from the newest therapies: BCMA-directed CAR-T cells and bispecific antibodies, now central to relapsed myeloma, commonly trigger cytokine release syndrome managed with tocilizumab.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Liver involvement: extramedullary myeloma and AL amyloid can deposit in the hepatic lobule, causing hepatomegaly and, with amyloid, cholestatic liver dysfunction.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Profound immunoparesis: myeloma suppresses normal antibody production, and anti-CD38 and BCMA-directed therapies deepen the deficit, leaving patients with severe COVID-19 and poor vaccine responses.
- `connects-to` → **[AML](../aml/README.md)** — Therapy-related leukaemia: alkylators such as melphalan and prolonged lenalidomide raise the risk of secondary myelodysplasia and acute myeloid leukaemia, a late complication in long-surviving myeloma patients.
- `connects-to` → **[Stroke](../stroke/README.md)** — Thrombosis and viscosity: high paraprotein levels can cause hyperviscosity with neurological symptoms, while immunomodulatory drugs like lenalidomide markedly raise the risk of arterial and venous thrombosis including stroke.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Niche survival signal: PI3K-AKT-mTOR signalling driven by the marrow microenvironment sustains myeloma plasma-cell survival and drug resistance.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — Stromal crosstalk: Notch signalling between myeloma cells and bone-marrow stroma promotes survival, drug resistance and the osteoclast activation behind lytic bone disease.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Epigenetic dependence: EZH2 is overexpressed in multiple myeloma and contributes to its progression, an emerging epigenetic therapeutic target.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — Cyclin D dysregulation: nearly all myelomas dysregulate a cyclin D gene, partnering CDK4/6 to drive plasma-cell proliferation—the rationale for CDK4/6 inhibition.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Marrow microenvironment: TNF-α within the bone-marrow niche supports myeloma cell survival and, with RANKL, drives the osteoclast activation behind its lytic bone disease.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Hypoxic marrow: HIF-1α stabilised in the hypoxic myeloma marrow drives the VEGF angiogenesis and glycolytic metabolism that support the malignant plasma-cell clone.
- `connects-to` → **[BAFF](../../03-molecular/baff/README.md)** — Plasma-cell survival: BAFF and APRIL from the marrow microenvironment sustain malignant plasma cells through BCMA, the survival axis now targeted by anti-BCMA CAR-T and bispecific antibodies in myeloma.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Proteostatic apoptosis: the heavy immunoglobulin output of myeloma cells makes them dependent on the proteasome, so bortezomib triggers terminal ER stress and caspase-3-mediated apoptosis.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Marrow macrophage support: CCL2 recruits macrophages into the myeloma marrow niche, where they protect the plasma-cell clone and contribute to drug resistance.
- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — The t(4;14) translocation of multiple myeloma overexpresses FGFR3, a recurrent high-risk cytogenetic event that drives a more aggressive disease course and is a candidate target for FGFR-directed therapy.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β from the marrow microenvironment induces the IL-6 that fuels plasma-cell growth and osteolytic bone disease, and blocking it slows the progression of smoldering to active multiple myeloma in trials.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Inflammation-driven hepcidin elevation, alongside marrow infiltration by plasma cells, causes the functional iron-restricted anemia that is among the most common presenting features of multiple myeloma.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — BCMA-directed CAR-T cells and bispecific antibodies (teclistamab), and the ADCC of daratumumab, redirect cytotoxic T and NK cells to kill myeloma plasma cells through perforin and granzyme, transforming relapsed disease.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — The anti-CD38 antibody daratumumab kills myeloma cells partly through complement-dependent cytotoxicity, fixing C3 and the membrane-attack complex, one of its several immune effector mechanisms.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — The osteoclast-driven bone destruction of myeloma releases calcium, producing the hypercalcemia—the C of the CRAB criteria—that causes confusion, constipation and the renal impairment defining symptomatic disease.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — Activating KRAS and NRAS mutations are among the commonest drivers in multiple myeloma, engaging the RAS-MAPK pathway to sustain plasma-cell proliferation.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 deletion or mutation (del17p) defines high-risk multiple myeloma with poor response to therapy and shortened survival.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — The PI3K-AKT-mTOR axis (AKT and mTOR already mapped) supports myeloma-cell survival downstream of IL-6 and the bone-marrow microenvironment.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — IL-6 from the bone-marrow microenvironment signals through JAK-STAT3 (IL-6 and STAT3 already mapped) as the central survival and proliferation axis of malignant plasma cells in multiple myeloma.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — NRF2 antioxidant signaling counters the proteasome-inhibitor-induced oxidative and proteotoxic stress, contributing to bortezomib resistance in multiple myeloma.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — RAS-ERK signaling (KRAS already mapped) is among the most frequently activated proliferative pathways in multiple myeloma.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-β in the marrow microenvironment suppresses osteoblast differentiation — contributing to myeloma bone disease — and dampens antitumor immunity in multiple myeloma.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 supports myeloma-cell survival and adhesion within the protective bone-marrow niche.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — Loss of PTEN restraint on PI3K-AKT-mTOR signaling (AKT, PIK3CA and mTOR mapped) promotes survival and drug resistance in multiple myeloma.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the antitumor immune response of multiple myeloma, relevant to its CAR-T and bispecific-antibody immunotherapy.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING modulates the inflammatory bone-marrow microenvironment of multiple myeloma.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling in the bone-marrow niche contributes to the immunosuppression and bone disease of multiple myeloma.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — PI3K-AKT-driven FOXO inactivation (AKT and PIK3CA already mapped) supports the survival of the malignant plasma cells of multiple myeloma.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the survival and proteostasis signaling of multiple myeloma cells, a candidate therapeutic target.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in multiple myeloma.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of the plasma-cell and cytokine receptors supports the survival of multiple myeloma cells.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of multiple myeloma.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the inflammatory bone-marrow microenvironment of multiple myeloma.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of the malignant plasma cells of multiple myeloma.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-family chemokine signaling (CXCL12/CXCR4 already mapped) participates in the bone-marrow homing of multiple myeloma.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic dysregulation of multiple myeloma.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the inflammatory bone-marrow microenvironment of multiple myeloma.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the myeloma-cell growth and osteoclast-driven bone disease of multiple myeloma.
- `connects-to` → **[Interleukin-10](../../03-molecular/il-10/README.md)** — IL-10-mediated immunosuppression participates in the immune evasion of multiple myeloma.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the plasma-cell survival signaling of multiple myeloma.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine (CD38/CD73-adenosine) signaling participates in the immunosuppressive bone-marrow microenvironment of multiple myeloma.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin participates in the myeloma-bone-disease and bone-marrow-microenvironment interactions of multiple myeloma.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Anaemia (the A of CRAB): marrow replacement by plasma cells and inflammation (hepcidin already mapped) suppress erythropoiesis, and the resulting anaemia with fatigue is often the presenting feature of multiple myeloma.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — BCMA CAR-T: IL-2-driven T-cell expansion powers the BCMA-directed CAR-T and bispecific-antibody therapies (perforin already mapped) that have transformed treatment of relapsed multiple myeloma.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Immune microenvironment: multiple myeloma progressively suppresses T-cell immunity and antigen presentation, and MHC-based recognition underlies both the immune escape of the plasma-cell clone and the response to its immunotherapies.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Tumour lysis: treating a high-burden multiple myeloma can trigger tumour-lysis syndrome, releasing purines that xanthine oxidase converts to uric acid, adding to the renal risk (kidney already mapped) already posed by light-chain cast nephropathy.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Cardiac risk: carfilzomib can be cardiotoxic and coexisting AL amyloid can infiltrate the myocardium, so troponin elevation marks the cardiac injury that complicates multiple myeloma and its treatment.
- `connects-to` → **[Secretory IgA](../../03-molecular/secretory-iga/README.md)** — Immunoparesis: the expanding plasma-cell clone suppresses normal immunoglobulin production including secretory IgA (IgG already mapped), the immunoparesis that impairs mucosal defence and causes the recurrent infections central to myeloma mortality.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Osteolytic inflammation: prostaglandins from the myeloma and its marrow microenvironment amplify the osteoclast-driven bone resorption (RANKL and sclerostin already mapped), contributing to the lytic bone disease of multiple myeloma.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 marrow niche: IL-4 polarises the marrow macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), the nurturing niche cells that support the survival of the malignant plasma cells of multiple myeloma.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Marrow angiogenesis: nitric oxide with VEGF (already mapped) supports the increased bone-marrow (already mapped) angiogenesis of multiple myeloma, part of the vascular microenvironment sustaining the plasma-cell clone.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 marrow niche: IL-13, with IL-4 (already mapped), supports the M2 marrow-macrophage niche that nurtures the malignant plasma cells of multiple myeloma.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Marrow adipose support: the marrow adipocytes and their adipokine leptin support the myeloma plasma cells, and obesity — a leptin-high state — is an established risk factor for multiple myeloma.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Protective adipokine: adiponectin is low in obesity, and its fall (leptin already mapped) removes a brake on the plasma-cell clone, part of the marrow-adipose crosstalk linking obesity to multiple myeloma.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Marrow-adipose adipokine: resistin, with leptin and adiponectin (already mapped), is part of the marrow-adipocyte adipokine crosstalk of the obesity-myeloma link and the metabolic niche of the plasma-cell clone.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Interferon maintenance: type-I interferon was a historical maintenance therapy of multiple myeloma, and its signalling shapes the immune (NK cell already mapped) microenvironment of the marrow.
- `connects-to` → **[Regulatory T cell](../../04-cellular/regulatory-t-cell/README.md)** — Immunosuppressive Tregs: the regulatory T cells of the myeloma marrow microenvironment (IL-10 and TGF-β already mapped) dampen the anti-myeloma immunity, a barrier to the T-cell (already mapped) therapies.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-myeloma immunity opposed by the immunosuppressive (Tregs already mapped) marrow microenvironment.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-myeloma response, opposing the immunosuppressive marrow microenvironment of multiple myeloma.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 arm of the immune microenvironment of the myeloma marrow.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Myeloma anaemia: the relative erythropoietin deficiency (the renal — kidney already mapped — impairment and the marrow infiltration) underlies the anaemia (haemoglobin already mapped) of the 'A' of the CRAB features of multiple myeloma.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immunosuppressive marrow microenvironment of multiple myeloma.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the myeloma marrow microenvironment (and the rare IgE myeloma).
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells of the marrow are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immunosuppressive myeloma microenvironment.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) shapes the myeloid and immunosuppressive dimension of the myeloma marrow microenvironment.
- `connects-to` → **[Vitamin D](../../../03-medicine/03-food/vitamin-d/README.md)** — Bone/prognostic vitamin: the vitamin D deficiency is common in multiple myeloma, worsens the bone (RANKL already mapped) disease, and is associated with a poorer prognosis.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Daratumumab CDC: the complement C5 (with C3 and C5aR1 already mapped) is the effector of the complement-dependent cytotoxicity by which the anti-CD38 daratumumab kills the myeloma plasma cells (already mapped).
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement evasion: the myeloma cells recruit factor H (with the CD55/CD59 regulators) to restrain the alternative complement pathway (C3, C5 and C5aR1 already mapped), a resistance mechanism to the daratumumab complement-dependent killing.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Anaemia iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the anaemia of the marrow-replacing multiple myeloma.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Bone marrow stroma alarmin: TSLP from bone-marrow stromal cells promotes the plasma-cell (already mapped) survival and IMiD-resistance in multiple myeloma; TSLP-driven STAT3 (already mapped) signalling augments the bone-marrow niche support for the malignant plasma-cell clone.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell angiogenesis: histamine from the bone-marrow mast cells promotes VEGF (already mapped) angiogenesis and osteoclast activation in myeloma; H2 receptor signalling amplifies the NF-kB (already mapped) survival axis of the malignant plasma cells (already mapped).
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Bone marrow ECM: periostin in the myeloma bone-marrow stroma, downstream of TGF-β (already mapped), promotes integrin αV-mediated plasma-cell (already mapped) homing and adhesion-mediated drug resistance; elevated myeloma-stroma periostin correlates with disease progression.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Myeloma bone pain: bradykinin, via B2 receptor, amplifies prostaglandin (already mapped) and VEGF-driven (already mapped) bone pain and osteolysis in the myeloma bone microenvironment; kinins enhance osteoclast (already mapped) activation in myeloma bone lesions.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Myeloma complement regulation: C1-INH controls the classical-pathway arm (C3, C5 and C5aR1 already mapped) in the myeloma bone-marrow microenvironment, complementing factor H (already mapped) to limit complement-mediated bystander lysis of bone-marrow stromal cells.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Anti-myeloma melatonin: melatonin, via MT1 receptors on plasma cells (already mapped), triggers mitochondrial apoptosis (caspase-3 already mapped), reduces IL-6 (already mapped) signalling and augments NK-cell (already mapped) cytotoxicity against multiple myeloma.

[^kumar-2022-imwg-criteria]: Kumar SK, Callander NS, Adekola K, et al. Multiple myeloma, version 3.2021, NCCN clinical practice guidelines in oncology. *J Natl Compr Canc Netw.* 2020;18(12):1685-1717. [doi:10.6004/jnccn.2020.0057](https://doi.org/10.6004/jnccn.2020.0057) · [PubMed 33285519](https://pubmed.ncbi.nlm.nih.gov/33285519/)
[^moreau-2022-teclistamab]: Moreau P, Garfall AL, van de Donk NWCJ, et al. Teclistamab in relapsed or refractory multiple myeloma. *N Engl J Med.* 2022;387(6):495-505. [doi:10.1056/NEJMoa2203478](https://doi.org/10.1056/NEJMoa2203478) · [PubMed 35661166](https://pubmed.ncbi.nlm.nih.gov/35661166/)
[^martin-2023-carvykti]: San-Miguel J, Dhakal B, Yong K, et al. Cilta-cel or standard care in lenalidomide-refractory multiple myeloma. *N Engl J Med.* 2023;389(4):335-347. [doi:10.1056/NEJMoa2303379](https://doi.org/10.1056/NEJMoa2303379) · [PubMed 37285856](https://pubmed.ncbi.nlm.nih.gov/37285856/)
