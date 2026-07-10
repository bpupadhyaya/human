---
schema: human-scale-entry/v1
id: myelofibrosis
name: Myelofibrosis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Myelofibrosis is a MPN with BM fibrosis, megakaryocyte dysplasia, and splenomegaly; drivers JAK2 V617F ~60%, CALR exon 9 ~20-25%, MPL ~8%; ruxolitinib (COMFORT-I/II), fedratinib, pacritinib, momelotinib (MOMENTUM) approved; allo-SCT is the only curative option."
aliases: ["myelofibrosis", "MF", "PMF", "primary myelofibrosis", "post-ET MF", "post-PV MF", "myeloproliferative neoplasm fibrosis", "JAK inhibitor myelofibrosis"]
sources:
  - id: verstovsek-2012-comfort1
    type: peer-reviewed
    cite: "Verstovsek S, Mesa RA, Gotlib J, et al. A double-blind, placebo-controlled trial of ruxolitinib for myelofibrosis. N Engl J Med. 2012;366(9):799-807."
    doi: "10.1056/NEJMoa1110557"
    pmid: "22375971"
    url: "https://doi.org/10.1056/NEJMoa1110557"
  - id: harrison-2012-comfort2
    type: peer-reviewed
    cite: "Harrison C, Kiladjian JJ, Al-Ali HK, et al. JAK inhibition with ruxolitinib versus best available therapy for myelofibrosis. N Engl J Med. 2012;366(9):787-798."
    doi: "10.1056/NEJMoa1110556"
    pmid: "22375970"
    url: "https://doi.org/10.1056/NEJMoa1110556"
cross_links:
  - target: 01-human/03-molecular/calr
    relation: connects-to
    note: "CALR exon 9 frameshift mutations drive ~20-25% of PMF; type 1 del52 → PMF phenotype with higher fibrosis grade and AML transformation risk; type 2 ins5 → ET phenotype; CALR-mutant MF responds to ruxolitinib with similar spleen/symptom benefit as JAK2 V617F MF."
  - target: 01-human/03-molecular/jak2
    relation: connects-to
    note: "JAK2 V617F occurs in ~60% of PMF and drives constitutive JAK-STAT signaling; JAK2 V617F allele burden correlates with splenomegaly and constitutional symptoms; ruxolitinib and other JAK inhibitors all target JAK2 kinase activity; JAK2 V617F is the primary molecular target in MF."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Ruxolitinib is first-line standard of care for intermediate-2 and high-risk MF; momelotinib inhibits JAK1/JAK2 plus ACVR1 → reduces hepcidin → anemia benefit; JAK1 inhibition reduces inflammatory cytokine burden (IL-6, TNF-α) driving constitutional symptoms."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β1 secreted by CALR/JAK2-mutant megakaryocytes is the primary driver of BM fibrosis in MF; TGF-β activates fibroblasts → collagen/reticulin deposition; serum TGF-β1 correlates with MF grade; TGF-β pathway inhibition is a therapeutic target in preclinical MF models."
  - target: 01-human/03-molecular/thrombopoietin
    relation: connects-to
    note: "MPL W515L/K activates JAK2 constitutively independent of TPO → megakaryocyte dysplasia and marrow fibrosis; ruxolitinib suppresses JAK-STAT; thrombocytopenia in high-risk MF limits JAK inhibitor dosing; pacritinib/momelotinib approved for MF with thrombocytopenia."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Myelofibrosis fills the bone marrow with reticulin then collagen fibrosis (MF-0 to MF-3), driven paracrine by TGF-β from mutant megakaryocytes onto polyclonal fibroblasts; as fibrosis evicts hematopoietic stem cells the blood shows teardrop cells and leukoerythroblastosis."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "Displaced from the fibrotic marrow, hematopoiesis relocates to the spleen (extramedullary hematopoiesis), producing the massive splenomegaly that defines myelofibrosis; cutting spleen volume (the SVR35 endpoint) is the main benefit of ruxolitinib."
  - target: 01-human/07-system/myeloproliferative-neoplasms
    relation: connects-to
    note: "Myelofibrosis is the most aggressive classic myeloproliferative neoplasm, arising de novo (primary MF) or evolving from polycythemia vera or essential thrombocythemia; like its siblings it is JAK2/CALR/MPL-driven, but only MF shows marrow fibrosis and only allo-SCT cures it."
  - target: 01-human/07-system/mds
    relation: connects-to
    note: "Myelofibrosis and MDS are overlapping clonal marrow disorders sharing mutations (ASXL1, SRSF2, U2AF1, TP53) and AML transformation risk; marrow fibrosis can appear in MDS and MDS/MPN overlap syndromes sit between them; both cause cytopenias graded by blast percentage."
  - target: 01-human/07-system/polycythemia-vera
    relation: connects-to
    note: "Polycythemia vera can evolve into post-PV myelofibrosis (~10-20% at 15 years): the JAK2 V617F clone exhausts marrow, fibrosis accumulates, and the picture converges with primary myelofibrosis — splenomegaly, leukoerythroblastosis and cytopenias; ruxolitinib treats both."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Myelofibrosis disrupts red-cell production: marrow fibrosis forces extramedullary hematopoiesis and yields a leukoerythroblastic film with teardrop cells (dacrocytes); progressive anemia is a core prognostic feature, and momelotinib uniquely improves it by lowering hepcidin."
  - target: 01-human/07-system/essential-thrombocythemia
    relation: connects-to
    note: "Essential thrombocythemia and polycythemia vera can both evolve into secondary (post-ET, post-PV) myelofibrosis: years of JAK2/CALR/MPL proliferation give way to a fibrotic, failing marrow with cytopenias and splenomegaly—a shared late fate of the chronic MPNs."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "Myelofibrosis carries the highest leukemic-transformation risk of the classic MPNs: ~10-20% progress to a treatment-resistant blast-phase AML as the clone acquires TP53 and other lesions, so high-risk patients are considered for allogeneic transplant, the only cure."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "The marrow fibrosis of myelofibrosis is reactive, not clonal: malignant megakaryocytes pour out TGF-β and PDGF that drive resident fibroblasts to deposit collagen and reticulin, crowding out hematopoiesis—the scarring cells are normal bystanders recruited by the clone."
  - target: 01-human/07-system/cml
    relation: connects-to
    note: "Myelofibrosis and CML are both chronic myeloproliferative neoplasms with marrow fibrosis but different drivers: CML's BCR-ABL is targeted by imatinib, while myelofibrosis's JAK2/CALR/MPL mutations are treated with JAK inhibitors—both can transform to leukemia."
  - target: 01-human/07-system/gout
    relation: connects-to
    note: "Myelofibrosis commonly causes secondary gout: the high cell turnover of the proliferating clone floods the blood with purines that become uric acid, so hyperuricemia and gout flares accompany the disease—sometimes a clue to an underlying myeloproliferative neoplasm."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Myelofibrosis drives extramedullary hematopoiesis in the liver: as marrow fibrosis crowds out blood production, hematopoiesis relocates to spleen and liver, enlarging them—and the displaced blood-forming tissue can cause portal hypertension."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Myelofibrosis is bone marrow turned to scar: malignant megakaryocytes secrete TGF-beta that drives fibroblasts to fill the marrow with fibrosis, so blood production fails and shifts to liver and spleen (extramedullary hematopoiesis)—the disease's defining lesion."
  - target: 01-human/03-molecular/mpl
    relation: connects-to
    note: "MPL is one of myelofibrosis's three driver mutations: activating the thrombopoietin receptor MPL (like JAK2 and CALR) switches on JAK-STAT to drive the clone, so testing JAK2/CALR/MPL classifies the disease and rare triple-negative cases carry worse prognosis."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Myelofibrosis causes anemia despite high erythropoietin: marrow scarring crowds out red-cell production so EPO rises but cannot be answered, leaving transfusion-dependent anemia—a key driver of symptoms that JAK inhibitors and newer agents try to relieve."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Myelofibrosis warps platelet production: clonal megakaryocytes first overproduce platelets, but as the marrow scars they fail, so patients swing from thrombosis-prone thrombocytosis to dangerous thrombocytopenia—platelet count tracking the march to marrow failure."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Myelofibrosis is named for the collagen it lays down: cytokines from the malignant clone drive marrow fibroblasts to flood the marrow with reticulin and collagen, crowding out blood production—so the fibrosis, though reactive, is the disease's defining lesion."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Myelofibrosis is in part an inflammatory disease: the JAK-STAT-driven clone pours out cytokines that cause fevers, weight loss, and night sweats, so JAK inhibitors like ruxolitinib ease symptoms by dampening this inflammatory storm more than by killing the clone."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Myelofibrosis scars the marrow through PDGF: the clonal megakaryocytes pour out PDGF and TGF-beta that drive fibroblasts to lay down the collagen replacing blood-forming marrow—so anti-fibrotic targeting of these cytokines is explored beyond JAK inhibition."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "The only cure for myelofibrosis is allogeneic transplant via donor T cells: cytotoxic T cells from the graft mount a graft-versus-leukemia attack on the clone, the lone therapy that can reverse marrow fibrosis—at the cost of transplant risk."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Progressive anemia defines advancing myelofibrosis: marrow fibrosis and ineffective erythropoiesis cause worsening transfusion-dependent anemia, a key prognostic factor and the reason new agents target the anemia, not just the spleen."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Myelofibrosis wastes the body through IL-6 and inflammation: the malignant clone and marrow stroma pour out IL-6 and other cytokines that cause the fevers, weight loss, and cachexia, and drive the fibrosis—why JAK inhibitors ease symptoms so well."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "Myelofibrosis pushes blood-making into the liver: as scarred marrow fails, hematopoiesis relocates to the liver and spleen (extramedullary hematopoiesis), enlarging them around the hepatocytes—the massive organomegaly typical of advanced disease."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Myelofibrosis is fueled by an inflammatory marrow rich in macrophages: monocytes and macrophages, with abnormal megakaryocytes, secrete the TGF-β and cytokines that drive fibroblasts to scar the marrow."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Myelofibrosis distorts the body's iron: transfusion-dependent anemia delivers iron the body cannot shed, building toxic overload, while inflammation also locks iron away from red-cell making—worsening the very anemia driving the transfusions."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Severe myelofibrosis anemia overworks the heart: to ship enough oxygen with too few red cells, the heart pumps harder in a high-output state, and transfusional iron can deposit in the muscle, together straining it toward failure."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Myelofibrosis spills immature cells into the blood: a scarred marrow forces a leukoerythroblastic picture, releasing early neutrophil precursors alongside teardrop red cells—a blood smear that flags hematopoiesis under siege."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Myelofibrosis shows up in imaging: X-ray photons can reveal osteosclerosis from the fibrotic marrow, and low-dose splenic irradiation is one way to shrink a massively enlarged, painful spleen."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "Myelofibrosis can harden bone as well as marrow: activated osteoblasts lay down osteosclerosis that thickens the cavity walls, a bony counterpart to the reticulin and collagen scarring inside."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Myelofibrosis can colonize the chest: extramedullary hematopoiesis and the disease's clotting tendency drive pulmonary hypertension, adding breathlessness to its anemia and splenomegaly."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy catches the cell driving the scarring: dysplastic megakaryocytes spill their granule contents — TGF-β and PDGF — that goad marrow fibroblasts into laying down the collagen and reticulin choking out blood production."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Myelofibrosis can turn marrow to stone: as fibrosis advances it often brings osteosclerosis, a thickening of the bone with extra calcium-phosphate mineral that shows as dense, sclerotic bones on X-ray."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "The kidney feels the disease's overflow: extramedullary blood formation can settle there, and the rapid cell turnover floods the blood with uric acid that crystallizes in the tubules, threatening urate nephropathy."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Myelofibrosis builds a dense new vasculature in the marrow: the malignant clone drives VEGF, and the resulting marrow neoangiogenesis — a rise in microvessel density — is part of the pathology pathologists grade alongside the scarring."
  - target: 01-human/03-molecular/albumin
    relation: connects-to
    note: "The disease wastes the body: drenching night sweats, fevers, and weight loss are hallmark constitutional symptoms, and the cachexia they cause lowers albumin — a marker of the burden that figures into prognosis."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Even as it scars the marrow, myelofibrosis stays prothrombotic: like its sister myeloproliferative neoplasms it raises the risk of venous and arterial clots, especially with a JAK2 mutation and a high blood count earlier in the disease."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "The churning marrow spills minerals: high cell turnover, and its lysis under treatment, release phosphate and urate into the blood, fueling the gout and hyperuricemia that often accompany myelofibrosis."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Blood-making strays into the gut, and the swollen spleen backs up its veins: extramedullary hematopoiesis can stud the bowel, while massive splenomegaly raises portal pressure into varices that bleed into the GI tract."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Blood-forming masses can squeeze the cord: paraspinal extramedullary hematopoiesis is a rare but urgent complication of myelofibrosis, the tissue pressing on the spinal cord and its neurons to cause weakness and sensory loss."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Myelofibrosis spills blood-making into the vessels: the malignant clone also marks endothelial cells, which help home extramedullary hematopoiesis to spleen and liver and contribute to the thrombosis that complicates the disease."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Myelofibrosis smolders with inflammation: the mutant clone switches on NF-κB, driving the inflammatory cytokine flood behind its fevers and weight loss and the fibrosis-promoting signals that scar the marrow."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "Blood-making can settle in the lungs: extramedullary hematopoiesis and clot showers from myelofibrosis can raise pulmonary artery pressure, a recognized complication that strains the right heart."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "A homing signal goes awry: disrupted CXCL12-CXCR4 signaling lets hematopoietic stem cells escape the fibrotic marrow into the blood, where they seed the spleen and liver — the extramedullary hematopoiesis behind the massive splenomegaly."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Clonal mast cells join the fibrotic crowd: mast cells are expanded in myelofibrosis marrow and, like the driver megakaryocytes, secrete profibrotic mediators that help lay down the collagen and reticulin scar."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "The failing marrow leaves patients defenseless: falling neutrophil counts and the immunosuppression of advanced disease and its treatment make infection and sepsis a leading cause of death in myelofibrosis."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "The disease runs on JAK-STAT: the JAK2/CALR/MPL drivers funnel into constitutive STAT signaling, with STAT3 supporting the clone's proliferation and the inflammatory cytokine output — the pathway that ruxolitinib's JAK inhibition reins in."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "The JAK2 clone inflames the arteries: like other JAK2-driven blood disorders and clonal hematopoiesis, myelofibrosis accelerates atherosclerosis, its inflamed clonal leukocytes worsening plaque and cardiovascular risk."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Sticky blood throws arterial clots: the hyperviscosity and activated platelets of myelofibrosis raise the risk of arterial thrombosis, including ischemic stroke, alongside its better-known venous clotting."
  - target: 01-human/07-system/tuberculosis
    relation: connects-to
    note: "Its JAK inhibitor can wake latent TB: ruxolitinib, the mainstay drug for myelofibrosis, suppresses interferon-γ signaling and impairs the granuloma, so latent tuberculosis can reactivate during treatment."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Neutropenia and JAK blockade open the lung to mold: cytopenias from marrow fibrosis plus the immunosuppression of ruxolitinib leave patients prone to invasive aspergillosis and other opportunistic infections."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Transfusion iron and chronic anemia burden the heart: the lifelong red-cell support for myelofibrosis anemia deposits iron in the myocardium, and the sustained anemia adds high-output strain, together risking heart failure."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "Its JAK-inhibitor therapy reawakens shingles: ruxolitinib, a mainstay for myelofibrosis, suppresses immunity and characteristically reactivates latent varicella-zoster as herpes zoster, prompting vaccination and vigilance."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: connects-to
    note: "JAK inhibition opens the lung to Pneumocystis: ruxolitinib's immunosuppression, atop the immune dysfunction of myelofibrosis, can permit opportunistic Pneumocystis pneumonia."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A heavy symptom burden weighs on mood: the relentless fatigue, pruritus, drenching sweats and massive splenomegaly of myelofibrosis erode quality of life and contribute to depression."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Extramedullary haematopoiesis swells the gut organs: when the scarred marrow pushes blood-making into the spleen and liver, the massive splenomegaly causes early satiety and portal hypertension with varices."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Transfusion iron overload poisons the glands: transfusion-dependent myelofibrosis accumulates iron that deposits in the pancreas, pituitary and thyroid, causing diabetes and other endocrinopathies."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A progressive marrow cancer breeds worry: the worsening cytopenias, transfusion dependence and threat of leukaemic transformation in myelofibrosis foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It hardens and pains the bones: the marrow fibrosis of myelofibrosis is accompanied by osteosclerosis seen on imaging and by deep, debilitating bone pain as the skeleton's blood factory is replaced by scar."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Its blood-making can crush the cord: extramedullary haematopoiesis in the epidural space can compress the spinal cord, a neurological emergency presenting with back pain, weakness and sensory loss."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It can itch and surface on the skin: myelofibrosis causes intractable aquagenic pruritus and, rarely, cutaneous extramedullary haematopoiesis appearing as red-brown skin nodules."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It massively swells the spleen: extramedullary haematopoiesis enlarges the spleen, often hugely, causing early satiety and splenic infarction, and may require splenectomy or splenic irradiation."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Blood-making spreads to the chest: extramedullary haematopoiesis in the lungs and pleura causes effusions and contributes to the pulmonary hypertension of advanced disease."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It strains the kidney: extramedullary haematopoiesis and hyperuricaemia from high cell turnover can impair renal function, and a rare myelofibrosis-associated glomerulopathy occurs."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "JAK inhibitors are its mainstay drug: ruxolitinib and other JAK1/2 inhibitors shrink the spleen and ease symptoms of myelofibrosis, the first targeted therapy for the disease."
  - target: 03-medicine/01-modern/04-cardio/aspirin
    relation: connects-to
    note: "Low-dose aspirin counters the clotting: like other myeloproliferative neoplasms, myelofibrosis carries a thrombotic risk that low-dose aspirin helps reduce in lower-risk patients."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Treatment threatens fertility: cytoreductive drugs and the allogeneic stem-cell transplant that can cure myelofibrosis impair fertility, relevant to younger patients."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Cytoreduction and conditioning: hydroxyurea controls the splenomegaly and high counts of myelofibrosis, and intensive conditioning chemotherapy precedes the allogeneic stem-cell transplant that is its only cure."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "It can harden the bone: advanced myelofibrosis often brings osteosclerosis, thickening the bony trabeculae as marrow fibrosis spills into a denser skeleton visible on imaging."
  - target: 01-human/07-system/aplastic-anemia
    relation: connects-to
    note: "Two routes to marrow failure: myelofibrosis cytopenias come from a fibrosed, crowded marrow, whereas aplastic anaemia leaves an empty hypocellular marrow — opposite histology converging on pancytopenia."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Blood-making relocates to the liver: as marrow fibrosis fails haematopoiesis, extramedullary blood formation sets up in the spleen and the hepatic lobules, enlarging the liver alongside the massive spleen."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "It still thromboses: like other myeloproliferative neoplasms, myelofibrosis's JAK2-mutant blood cells inflame the arterial wall and raise the risk of arterial thrombosis, stroke and heart attack."
  - target: 01-human/07-system/leishmaniasis
    relation: connects-to
    note: "An infectious mimic of the big spleen: visceral leishmaniasis produces massive splenomegaly, pancytopenia and marrow change that imitate myelofibrosis, a key infectious differential in endemic regions."
  - target: 01-human/07-system/gvhd
    relation: connects-to
    note: "The only cure, and its cost: allogeneic stem-cell transplant is the sole curative therapy for myelofibrosis, but graft-versus-host disease is a major source of its transplant-related mortality."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Hidden in the lungs: extramedullary haematopoiesis and microvascular megakaryocyte emboli in myelofibrosis can lodge in the alveolar capillaries, contributing to the pulmonary hypertension that worsens prognosis."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "A mimic to exclude: marrow infiltration by metastatic cancer such as breast cancer causes reactive fibrosis and a leukoerythroblastic blood film that can imitate primary myelofibrosis."
  - target: 01-human/03-molecular/von-willebrand-factor
    relation: connects-to
    note: "Bleeding amid clotting: high platelet counts in myelofibrosis can adsorb and clear high-molecular-weight von Willebrand multimers, causing an acquired von Willebrand syndrome and paradoxical bleeding in a prothrombotic disease."
  - target: 01-human/07-system/inherited-thrombophilia
    relation: connects-to
    note: "Layered thrombotic risk: myelofibrosis is an acquired JAK2-driven prothrombotic state prone to splanchnic-vein thrombosis, a risk amplified when an inherited thrombophilia coexists."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Extramedullary haematopoiesis: blood-forming tissue colonises sites outside the marrow in myelofibrosis, and masses of epidural EMH can compress the spinal cord and nerve roots, a rare neurological emergency."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Disease-modifying therapy: pegylated interferon-alpha can reduce the JAK2/CALR-mutant clone and even reverse marrow fibrosis in early myelofibrosis, unlike purely palliative JAK inhibitors."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "High-risk mutation: loss-of-function EZH2 mutations are recurrent in myelofibrosis and mark a poorer prognosis among its epigenetic driver lesions."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Hypoxic fibrotic niche: HIF-1α-driven angiogenesis and hypoxia characterise the densely fibrotic, neovascularised marrow of myelofibrosis."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Niche-damaging cytokine: IL-1β secreted by the mutant clone injures the bone-marrow mesenchymal niche and drives the inflammatory cytokine milieu that promotes fibrosis in myelofibrosis."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Clonal selective advantage: TNF-α in the myelofibrosis marrow suppresses normal progenitors while JAK2-mutant cells resist it, giving the malignant clone a growth edge amid chronic inflammation."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Matrix and osteosclerosis: osteopontin released by megakaryocytes and stroma contributes to the marrow fibrosis and the osteosclerosis that thickens trabecular bone in advanced myelofibrosis."
  - target: 01-human/03-molecular/pf4
    relation: connects-to
    note: "Profibrotic chemokine: platelet factor 4 (CXCL4) released by the abnormal megakaryocytes of myelofibrosis is a direct driver of fibroblast activation and collagen deposition, central to the reticulin and collagen marrow fibrosis."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Apoptotic dependency: the malignant clone of myelofibrosis depends on BCL-xL/BCL-2 for survival, the rationale for adding the BCL-2/BCL-xL inhibitor navitoclax to ruxolitinib in JAK-inhibitor-refractory disease."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "Osteosclerosis: dysregulated RANKL-driven osteoclast and osteoblast activity contributes to the osteosclerosis that thickens and remodels trabecular bone in advanced myelofibrosis, narrowing the marrow space."
  - target: 01-human/03-molecular/sf3b1
    relation: connects-to
    note: "High-risk comutations: spliceosome mutations such as SF3B1, U2AF1 and SRSF2, acquired alongside the JAK2/CALR/MPL driver, mark the higher-risk myelofibrosis more likely to progress to leukaemia and inform prognostic scoring."
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "Fibrogenic growth factor: clonal megakaryocytes release basic FGF that, with PDGF and TGF-β, signals through FGFR on marrow fibroblasts to drive the reticulin and collagen fibrosis that progressively replaces the haematopoietic marrow."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "Inflammatory niche: S100A8/A9 alarmins released in the myelofibrotic marrow amplify the chronic inflammation that both drives the constitutional symptoms and feeds the fibrotic, cytokine-rich niche supporting the malignant clone."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "MAPK arm: JAK2 V617F signals through the MAPK-ERK1/2 pathway as well as STAT5, contributing to the clonal myeloproliferation of myelofibrosis and to incomplete responses to JAK inhibition."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "Progression mutations: high-molecular-risk epigenetic and splicing mutations (with the SF3B1 already mapped) accumulate on the JAK2/CALR/MPL driver in myelofibrosis, accelerating its progression to leukaemic transformation."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Inflammatory fibrosis: chronic NLRP3-inflammasome activation and IL-1β (already mapped) sustain the inflammatory milieu that drives the marrow fibrosis and constitutional symptoms of myelofibrosis."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "Fibrosis effector: TGF-β released by the clonal megakaryocytes signals through SMAD4 (TGF-β mapped) to activate marrow fibroblasts that lay down the collagen (mapped) reticulin fibrosis defining myelofibrosis."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K limb: JAK2 (mapped) also engages PI3K-AKT-mTOR, a parallel survival-and-proliferation pathway supporting the myelofibrosis clone alongside JAK-STAT."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "Leukaemic transformation: TP53 inactivation drives the progression of myelofibrosis to the blast phase, a secondary acute myeloid leukaemia with dismal prognosis."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "JAK2-driven PI3K-AKT-mTOR signalling (JAK2 and AKT mapped) supports clonal proliferation in myelofibrosis and is a target of mTOR-inhibitor trials."
  - target: 01-human/03-molecular/runx1
    relation: connects-to
    note: "Acquisition of RUNX1 mutations marks clonal evolution of myelofibrosis toward blast-phase (secondary AML) transformation."
  - target: 01-human/03-molecular/idh1
    relation: connects-to
    note: "IDH1 mutations are recurrent high-risk lesions driving epigenetic dysregulation and leukaemic transformation in myelofibrosis, complementing the EZH2/DNMT3A lesions already mapped."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 secreted by the clonal megakaryocytes is a key driver of the bone-marrow fibrosis that defines myelofibrosis."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling (type-I interferon already mapped) shapes the inflammatory bone-marrow milieu and contributes to the cytopenias of myelofibrosis."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING amplifies the chronic inflammatory bone-marrow microenvironment that drives the fibrosis of myelofibrosis."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors regulate hematopoietic stem-cell quiescence and oxidative-stress handling disrupted in the clonal myeloproliferation of myelofibrosis."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β dysregulation contributes to the aberrant megakaryocyte and progenitor signaling that drives the marrow fibrosis of myelofibrosis."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6 cell-cycle activity supports the clonal proliferation of JAK2/CALR/MPL-mutant progenitors in myelofibrosis."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated cytotoxic immunosurveillance targets the neoantigen-bearing CALR-mutant clone of myelofibrosis."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis and contributes to the leukemic evolution of myelofibrosis."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family and LYN kinase signaling downstream of the constitutively active JAK2 axis supports the megakaryocyte and progenitor survival of myelofibrosis."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped), downstream of JAK2, supports the survival of the clonal cells of myelofibrosis."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the survival of the megakaryocytes and clonal cells of myelofibrosis."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of the clonal hematopoietic cells of myelofibrosis."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-family chemokine signaling participates in the bone-marrow niche and immune interactions of myelofibrosis."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of myelofibrosis."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the inflammatory bone-marrow microenvironment and fibrosis of myelofibrosis."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory and fibrotic bone-marrow microenvironment of myelofibrosis."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory bone-marrow microenvironment of myelofibrosis."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the megakaryocyte and stromal-cell signaling contributing to the marrow fibrosis of myelofibrosis."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "Anaemia and fibrosis: activin A signalling through ACVR2 both suppresses erythropoiesis, the target of luspatercept and momelotinib for myelofibrosis anaemia, and promotes fibroblast activation, giving it a dual role in the disease."
  - target: 01-human/03-molecular/sclerostin
    relation: connects-to
    note: "Osteosclerosis: advanced myelofibrosis develops osteosclerosis with increased bone density, and dysregulated Wnt signalling with altered sclerostin contributes to the bone remodelling that accompanies the marrow fibrosis."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Iron and anaemia: chronic inflammation in myelofibrosis raises IL-6-driven hepcidin (IL-6 already mapped), contributing to the anaemia of inflammation, while transfusion dependence adds iron overload requiring chelation."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Progressive anaemia: worsening anaemia with falling haemoglobin, from marrow failure, splenic sequestration and JAK-inhibitor therapy, is a defining feature of myelofibrosis driving transfusion dependence and momelotinib or luspatercept use."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Marrow neoangiogenesis: myelofibrosis shows increased bone-marrow microvascular density supported by angiopoietin-Tie2 signalling alongside VEGF (already mapped), part of the disordered fibrotic microenvironment created by the clone."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Urate overproduction: the high cell turnover of myelofibrosis raises purine catabolism through xanthine oxidase, producing hyperuricaemia and gout that are managed with allopurinol alongside the disease-directed therapy."
  - target: 01-human/03-molecular/ferroportin
    relation: connects-to
    note: "Iron-restricted anaemia: the chronic inflammation of myelofibrosis raises hepcidin (already mapped), which degrades ferroportin to trap iron in macrophages, contributing to the iron-restricted anaemia that adds to the marrow-failure anaemia."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Cytokine milieu: IL-10 among the cytokines of the inflammatory myelofibrosis microenvironment counters the IL-6, TNF and IL-1 (already mapped) that drive the constitutional symptoms and fibrosis, part of the dysregulated cytokine balance of the disease."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Splenomegaly and portal flow: the massive splenomegaly of myelofibrosis raises portal blood flow, and dysregulated nitric oxide contributes to the splanchnic vasodilation and portal hypertension that can complicate the extramedullary haematopoiesis."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage niche: IL-4 polarises the marrow macrophages toward an M2 phenotype (IL-10 already mapped), part of the inflammatory, fibrotic microenvironment (TGF-β and PDGF already mapped) of the myelofibrosis marrow."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Marrow adipokine signalling: leptin from the marrow adipose tissue signals to the clonal and stromal cells, part of the metabolic microenvironment of the fibrotic myelofibrosis marrow."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Marrow-adipocyte crosstalk: adiponectin, with leptin (already mapped), links the marrow adipocytes to the haematopoietic and stromal cells, part of the altered marrow microenvironment that accompanies the fibrosis of myelofibrosis."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Profibrotic type-2 arm: IL-13, with IL-4 (already mapped), contributes to the M2 macrophage (already mapped) and profibrotic (TGF-β already mapped) signalling that drives the marrow fibrosis of myelofibrosis."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Marrow adipokine: resistin, with leptin and adiponectin (already mapped), is part of the marrow-adipocyte adipokine crosstalk of the fibrotic marrow microenvironment of myelofibrosis."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc and haematopoiesis: zinc is required for the haematopoiesis disrupted in myelofibrosis, and the zinc-copper balance is part of the trace-metal milieu of the altered marrow microenvironment."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Pro-fibrotic macrophages: the marrow macrophages and the monocyte-derived fibrocytes contribute to the reactive fibrosis (TGF-β and PDGF already mapped) of myelofibrosis."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "Blast-phase transformation: myelofibrosis carries the risk of blast-phase transformation to acute myeloid leukaemia (the increasing blasts; TP53 and RUNX1 already mapped), the terminal event."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Transfusion iron overload: the transfusion-dependent anaemia (haemoglobin already mapped) of myelofibrosis causes the iron overload (hepcidin and ferroportin already mapped), needing chelation."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Clonal immunosurveillance: the NK cells (perforin already mapped) provide the immune surveillance of the JAK2/CALR (already mapped)-mutant clone of myelofibrosis, an arm augmented by the interferon (type-I interferon already mapped) therapy."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 inflammatory MF: the IFN-γ of the T cells (with the type-I interferon already mapped) is the type-II interferon arm of the chronic inflammation (IL-6 and TNF already mapped) that drives the fibrosis of myelofibrosis."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the inflammatory microenvironment of myelofibrosis."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the inflammatory bone-marrow (already mapped) microenvironment of myelofibrosis."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the chronic inflammation (IL-6 and TNF already mapped) that drives the fibrosis of myelofibrosis."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the inflammatory microenvironment of myelofibrosis."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the chronic inflammatory marrow niche that drives the fibrosis (TGF-β and PDGF already mapped) of myelofibrosis."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its activation (with C3 already mapped) contribute to the inflammasome (NLRP3 already mapped)-linked chronic inflammation and the thrombotic risk of myelofibrosis."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling links the complement to the neutrophil and platelet (PF4 already mapped) activation of the thromboinflammatory dimension of myelofibrosis."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the thromboinflammatory marrow niche of myelofibrosis."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Transfusional iron overload: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin and ferroportin already mapped) of the anaemia and the transfusional iron overload of myelofibrosis."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Marrow fibrosis: periostin, downstream of the TGF-β (already mapped) signalling, is a matricellular mediator of the reactive marrow fibrosis (with osteopontin and collagen already mapped) that defines myelofibrosis."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Marrow alarmin: TSLP, released from the dysplastic marrow stroma and megakaryocytes (thrombopoietin already mapped) under JAK2 (already mapped) and cytokine stress, activates the dendritic cells and mast cells in the fibrotic marrow niche of myelofibrosis."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-marrow axis: bradykinin, generated by the contact-kinin pathway in the extramedullary haematopoiesis sites (liver and spleen already mapped), amplifies the endothelial permeability and the inflammatory cytokine (TNF-α and IL-1β already mapped) milieu of myelofibrosis."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement/kinin gate: C1-esterase inhibitor limits the classical complement (complement C3, C5 and C5aR1 already mapped) and contact-kinin (bradykinin already mapped) cascades in the fibrotic marrow and splenic extramedullary haematopoiesis sites of myelofibrosis."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Marrow mast-cell effector: histamine, released by mast cells in the fibrotic marrow niche of myelofibrosis, amplifies the inflammatory cytokine (TNF-α and IL-1β already mapped) signalling and the JAK2-driven (already mapped) proliferative cascade of the disease."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Antioxidant haematopoietic protection: melatonin, via MT1/MT2 receptors on haematopoietic progenitors (already mapped), scavenges ROS (already mapped) from dysfunctional mitochondria and may attenuate oxidative damage driving the clonal evolution of myelofibrosis."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Immune-endocrine coupling: prolactin, elevated during chronic myeloproliferation, potentiates the macrophage (already mapped) and NK-cell (already mapped) signalling and may amplify the inflammatory cytokine milieu (TNF-α and IL-6 already mapped) of myelofibrosis."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "MF testosterone: androgen signalling on haematopoietic progenitors attenuates the TGF-β (already mapped) fibrotic drive in the marrow; testosterone deficiency worsens the JAK2 (already mapped) MPN anaemia and bone-marrow (already mapped) failure of myelofibrosis."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "MF serotonin: platelet (already mapped) serotonin amplifies the thrombopoietin (already mapped) megakaryocyte hyperplasia and thrombotic risk; 5-HT2 signalling on fibroblasts (already mapped) potentiates the TGF-β (already mapped) fibrotic cascade of myelofibrosis."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "MF oxytocin: oxytocin receptors on bone-marrow (already mapped) stromal cells modulate the immune-inflammatory microenvironment of myelofibrosis; oxytocin attenuates the macrophage (already mapped) and fibroblast (already mapped) TGF-β (already mapped) fibrotic signalling."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "MF vasopressin: vasopressin (ADH) modulates the bone-marrow (already mapped) stromal microenvironment via V1/V2 receptor signalling; vasopressin amplifies NF-κB (already mapped) and TGF-β (already mapped) driven fibroblast (already mapped) activation in the myelofibrotic marrow."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "MF selenium: selenoproteins suppress ROS-driven NF-κB (already mapped) and TGF-β (already mapped) fibrotic signalling in myelofibrosis; selenium deficiency amplifies macrophage (already mapped) inflammatory cytokine release and bone-marrow (already mapped) oxidative stress."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "MF iodine: thyroid-hormone signalling modulates bone-marrow (already mapped) erythropoiesis and macrophage (already mapped) immune surveillance; iodine deficiency amplifies NF-κB (already mapped) and TGF-β (already mapped) driven fibroblast (already mapped) fibrotic activity."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "MF magnesium: magnesium supports bone-marrow (already mapped) haematopoiesis and macrophage (already mapped) anti-inflammatory resolution; magnesium deficiency amplifies NF-κB (already mapped) and TGF-β (already mapped) fibrotic signalling in myelofibrosis."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "MF copper: copper, via ceruloplasmin and SOD, scavenges ROS in bone-marrow (already mapped) macrophages (already mapped) and fibroblasts (already mapped); copper deficiency amplifies NF-κB (already mapped) and TGF-β (already mapped) fibrotic signalling in myelofibrosis."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "MF sodium: high dietary sodium promotes macrophage (already mapped) and mast-cell (already mapped) pro-inflammatory activation; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) amplifies the neutrophil (already mapped) fibrotic cascade of myelofibrosis."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "MF potassium: potassium channels regulate macrophage (already mapped) and mast-cell (already mapped) ion homeostasis in the myelofibrosis bone marrow; potassium depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) fibrotic cascade of myelofibrosis."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "MF chloride: chloride channels regulate macrophage (already mapped) and neutrophil (already mapped) ion homeostasis in the myelofibrosis bone marrow; chloride imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) fibrotic cascade of myelofibrosis."
---

# Myelofibrosis

## Overview

**Myelofibrosis (MF)** is a BCR-ABL1-negative myeloproliferative neoplasm (MPN) characterized by clonal hematopoiesis, progressive bone marrow fibrosis, extramedullary hematopoiesis (splenomegaly, hepatomegaly), and constitutional symptoms (fatigue, night sweats, weight loss, pruritus). MF arises as **primary myelofibrosis (PMF)** de novo or as **post-ET MF** and **post-PV MF** from prior essential thrombocythemia or polycythemia vera. Incidence: ~1-2/100,000/year; median age at diagnosis ~65 years; male slight predominance. MF carries the worst prognosis among the classic MPNs — median OS ~5-7 years for intermediate/high-risk disease — and is uniquely characterized by profound constitutional symptom burden often exceeding that of solid organ malignancies. **JAK2 V617F** (~60%), **CALR exon 9 mutations** (~20-25%), and **MPL W515L/K** (~8%) are the three canonical driver mutations, all converging on constitutive JAK-STAT pathway activation [^verstovsek-2012-comfort1][^harrison-2012-comfort2]. JAK inhibitors (ruxolitinib, fedratinib, pacritinib, momelotinib) have transformed symptom management; **allogeneic SCT** remains the only potentially curative therapy.

**MF subtypes:**
- **Primary MF (PMF):** De novo; no antecedent MPN; median OS ~5-7 years (high-risk)
- **Post-ET MF:** ~0.5-1%/year transformation rate from ET; overall ~10-15% at 15 years; better prognosis than PMF
- **Post-PV MF:** ~0.5-0.8%/year transformation rate from PV; OS slightly worse than post-ET MF

## Structure

### Driver mutations and molecular architecture

**JAK2 V617F (~60% PMF, ~55% post-PV MF, ~50% post-ET MF):**
Acquired point mutation (V617F) in the pseudokinase domain of JAK2 → releases autoinhibition → constitutive kinase activity → downstream STAT3/STAT5, PI3K-AKT, MAPK activation; higher allele burden (>50% VAF) in PV and MF vs. ET; homozygosity through mitotic recombination correlates with fibrosis progression.

**CALR exon 9 mutations (~20-25% PMF, ~25% ET→MF):**
Type 1 (del52bp) predominates in PMF (3:1 over type 2 ins5bp); type 1 confers stronger MPL activation and HSC self-renewal → PMF phenotype; both respond to JAK inhibitors; allele burden trackable by ddPCR/NGS. See [CALR](../../03-molecular/calr/README.md) for detailed mechanism.

**MPL W515L/K (~8% PMF):**
Activating mutations in the juxtamembrane domain of the thrombopoietin receptor MPL → constitutive JAK2 activation independent of TPO; clinically similar to JAK2-mutant MF; responds to ruxolitinib.

**Triple-negative MF (~8-10%):**
Absence of JAK2, CALR, and MPL mutations; higher rate of IDH1/2, ASXL1 adverse mutations; worst prognosis among driver mutation groups; allo-SCT strongly indicated.

### High-risk co-mutations (MIPSS70 adverse molecular markers)

| Gene | Frequency | Effect |
|------|-----------|--------|
| ASXL1 | ~35-40% | Epigenetic dysregulation; adverse prognosis |
| SRSF2 | ~15-20% | Aberrant splicing; monocytic skewing; adverse |
| EZH2 | ~7-10% | PRC2 loss; adverse |
| IDH1/2 | ~5% | 2-HG production; AML transformation risk |
| U2AF1 Q157 | ~8-10% | Splicing; Q157 is specifically adverse (vs S34) |
| TP53 | ~5% | Bi-allelic → very adverse; blastic transformation |

**MIPSS70 (Mutation-Enhanced IPSS at age 70):** Incorporates driver mutation type, adverse co-mutations, and karyotype; stratifies PMF into 5 risk tiers; guides allo-SCT timing.

### Bone marrow pathology

**WHO 2022 criteria for PMF:**
Major: (1) megakaryocytic proliferation + atypia (cloud-like nuclei, bulbous nuclear lobes, bare megakaryocyte nuclei in sinusoids) WITH reticulin and/or collagen fibrosis grade 1-3; (2) WHO criteria not met for another MPN, MDS, or BCR-ABL1+ CML; (3) JAK2/CALR/MPL mutation or other clonal marker.
Minor: (1) anemia; (2) leukocytosis ≥11×10⁹/L; (3) palpable splenomegaly; (4) elevated LDH; (5) leukoerythroblastosis (teardrop cells/dacrocytes + nucleated RBCs + immature myeloid cells).

**Fibrosis grading (European consensus):**
- MF-0 (prefibrotic): Scattered linear reticulin, no coarse fibers (→ pre-PMF, often misdiagnosed as ET)
- MF-1: Loose network of reticulin with some intersections
- MF-2: Diffuse dense reticulin + coarse collagen bundles
- MF-3: Dense reticulin + collagen + osteosclerosis

**Prefibrotic PMF (pre-PMF):** Megakaryocyte atypia without significant fibrosis (MF-0/1); mimics ET; prognosis intermediate between ET and overt MF; important to distinguish clinically because transformation risk is higher than true ET.

### Peripheral blood and clinical findings

- **Leukoerythroblastosis:** Teardrop cells (dacrocytes), nucleated RBCs (nRBC), immature myeloid cells (myelocytes, metamyelocytes) → hallmark of extramedullary hematopoiesis
- **Anemia:** Multifactorial — ineffective erythropoiesis, splenomegaly (hypersplenism), hepcidin upregulation (JAK-IL-6 axis) → transfusion dependence in ~40-50% high-risk MF
- **Splenomegaly:** Near-universal; massive (>5 cm below costal margin) in ~50% symptomatic; splenic sequestration + EMH; portal hypertension in severe cases
- **Cytokine storm:** Elevated IL-6, TNF-α, IL-8, CXCL10 → constitutional symptoms; inflammatory cytokines are the primary drivers of MF symptom burden (NOT blast proliferation)

## Function

### Normal megakaryocyte and BM stromal biology

**Megakaryocyte-stromal crosstalk in MF:**
Normal megakaryocytes (MK) secrete TGF-β1 at controlled amounts → fibroblast activation in proportion to MK mass. In MF, CALR/JAK2-mutant MKs are hyperproliferative and release excess TGF-β1, PDGF, VEGF, and FGF from α-granules → fibroblast proliferation + collagen deposition → reticulin → collagen fibrosis → osteosclerosis. This is a paracrine (not cell-intrinsic) mechanism of fibrosis — the fibroblasts in MF are polyclonal (not part of the MPN clone); they respond to cytokine signals from malignant MKs.

**Extramedullary hematopoiesis:**
As BM fibrosis displaces hematopoietic stem/progenitor cells (HSPCs) → HSPCs mobilize to spleen, liver, lungs → massive splenomegaly; spleen becomes major site of blood production (erythropoiesis, myelopoiesis); spleen-derived hematopoiesis is dysplastic → peripheral blood leukoerythroblastosis.

## Pathology

### Prognostic scoring systems

**IPSS (International Prognostic Scoring System — diagnosis only):**
Points for: age >65, WBC >25×10⁹/L, Hgb <10 g/dL, blasts ≥1%, constitutional symptoms
Risk groups: Low (0), Int-1 (1), Int-2 (2), High (≥3); median OS: 135, 95, 48, 27 months

**DIPSS (Dynamic IPSS — any time point):**
Same variables with double weight for Hgb <10 g/dL; updated real-time assessment during follow-up.

**MIPSS70 (Molecular IPSS):**
Adds adverse co-mutations (ASXL1, SRSF2, EZH2, IDH1/2, U2AF1 Q157) + karyotype + BM fibrosis grade; 5 risk groups; guides allo-SCT decision in patients ≤70 years.

### Blast phase transformation (BP-MF / AML)

- AML transformation in MF: ~10-20% overall; ~3-5%/year in high-risk MIPSS; median OS post-transformation ~3.5 months with chemotherapy alone
- Molecular harbingers: IDH1/2 mutation acquisition, TP53 biallelic, RUNX1 mutation, NRAS mutation
- Treatment: venetoclax + azacitidine (preferred in fit patients); HMA alone; intensive chemotherapy rarely used; allo-SCT if CR/CRi achieved

### Treatment

**JAK inhibitors (first-line intermediate-2 / high-risk MF):**

| Drug | Mechanism | Key Trial | Key Result |
|------|-----------|-----------|------------|
| Ruxolitinib | JAK1/2 inhibitor | COMFORT-I (placebo) / COMFORT-II (BAT) | SVR35 ~42% vs 0-1%; symptom score ≥50% reduction ~46% vs 5%; OS benefit at 5-year follow-up |
| Fedratinib | JAK2-selective | JAKARTA | SVR35 ~47%; active after ruxolitinib failure (JAKARTA-2) |
| Pacritinib | JAK2/FLT3/ACVR1 | PERSIST-2 / PAC203 | Platelet-sparing; SVR35 ~29% in platelets <50×10⁹/L; FDA 2022 for cytopenic MF |
| Momelotinib | JAK1/2/ACVR1 | MOMENTUM | SVR35 ~23% vs 3%; TSS50 ~24% vs 9%; transfusion independence ~31% vs 20%; FDA 2023 for symptomatic + anemic MF |

**Ruxolitinib mechanism of anemia (adverse effect):**
JAK1/2 inhibition → reduced EPO signaling → anemia; also reduced ACVR1/hepcidin inhibition; momelotinib adds ACVR1 inhibition → reduced hepcidin → improved erythropoiesis → anemia benefit.

**Ruxolitinib discontinuation syndrome:**
Abrupt ruxolitinib cessation → cytokine rebound → fever, splenomegaly surge, hypotension, hemodynamic instability; always taper over 1-2 weeks; have steroids ready.

**Anemia-targeted agents:**
- **Luspatercept** (ACVR2B-Fc trap; traps TGF-β superfamily ligands → activin pathway inhibition → promotes late-stage erythropoiesis): EMPOWER-MF trial; transfusion independence in ~27% of MF patients with anemia; FDA pending
- **Danazol** (androgen): modest anemia benefit; hepatotoxicity
- **Thalidomide/lenalidomide** (immunomodulatory): anemia and splenomegaly; limited use due to toxicity

**Combination investigational strategies:**
- **Ruxolitinib + navitoclax (BCL-2/BCL-XL):** REFINE trial; SVR35 ~63% vs ~38% ruxolitinib; navitoclax causes thrombocytopenia (BCL-XL platelets)
- **Ruxolitinib + pelabresib (BET inhibitor, CPI-0610):** MANIFEST-2 (randomized Ph3): SVR35 primary endpoint met; bone marrow fibrosis improvement; spleen + symptom co-primary endpoints pending full publication
- **Imetelstat (telomerase inhibitor):** IMpact-MF (randomized Ph3, ruxolitinib-relapsed MF): anemia reduction; awaiting OS data

**Allogeneic SCT (only curative therapy):**
- Indicated for intermediate-2 / high-risk MF (MIPSS70) in eligible patients (typically age ≤70)
- 5-year OS post-allo-SCT: ~50-60% (myeloablative conditioning) vs ~35-45% (reduced intensity)
- BM fibrosis resolves post-engraftment over 3-6 months
- Timing: before blast phase transformation; higher-risk co-mutations (IDH, TP53) → earlier SCT
- Relapse post-SCT: ~20-30%; DLI and molecular monitoring (JAK2/CALR VAF)

## Connections

- `connects-to` → **[CALR](../../03-molecular/calr/README.md)** — CALR exon 9 frameshift mutations drive ~20-25% of PMF; type 1 del52 → PMF phenotype with higher fibrosis grade and AML transformation risk; type 2 ins5 → ET phenotype; CALR-mutant MF responds to ruxolitinib with similar spleen/symptom benefit as JAK2 V617F MF.
- `connects-to` → **[JAK2](../../03-molecular/jak2/README.md)** — JAK2 V617F occurs in ~60% of PMF and drives constitutive JAK-STAT signaling; JAK2 V617F allele burden correlates with splenomegaly and constitutional symptoms; ruxolitinib and other JAK inhibitors all target JAK2 kinase activity; JAK2 V617F is the primary molecular target in MF.
- `connects-to` → **[JAK1-2](../../03-molecular/jak1-2/README.md)** — Ruxolitinib is first-line standard of care for intermediate-2 and high-risk MF; momelotinib inhibits JAK1/JAK2 plus ACVR1 → reduces hepcidin → anemia benefit; JAK1 inhibition reduces inflammatory cytokine burden (IL-6, TNF-α) driving constitutional symptoms.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — TGF-β1 secreted by CALR/JAK2-mutant megakaryocytes is the primary driver of BM fibrosis in MF; TGF-β activates fibroblasts → collagen/reticulin deposition; serum TGF-β1 correlates with MF grade; TGF-β pathway inhibition is a therapeutic target in preclinical MF models.
- `connects-to` → **[Thrombopoietin](../../03-molecular/thrombopoietin/README.md)** — MPL W515L/K activates JAK2 constitutively independent of TPO → megakaryocyte dysplasia and marrow fibrosis; ruxolitinib suppresses JAK-STAT; thrombocytopenia in high-risk MF limits JAK inhibitor dosing; pacritinib/momelotinib approved for MF with thrombocytopenia.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Myelofibrosis fills the bone marrow with reticulin then collagen fibrosis (MF-0 to MF-3), driven paracrine by TGF-β from mutant megakaryocytes onto polyclonal fibroblasts; as fibrosis evicts hematopoietic stem cells the blood shows teardrop cells and leukoerythroblastosis.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — Displaced from the fibrotic marrow, hematopoiesis relocates to the spleen (extramedullary hematopoiesis), producing the massive splenomegaly that defines myelofibrosis; cutting spleen volume (the SVR35 endpoint) is the main benefit of ruxolitinib.
- `connects-to` → **[Myeloproliferative Neoplasms](../myeloproliferative-neoplasms/README.md)** — Myelofibrosis is the most aggressive classic myeloproliferative neoplasm, arising de novo (primary MF) or evolving from polycythemia vera or essential thrombocythemia; like its siblings it is JAK2/CALR/MPL-driven, but only MF shows marrow fibrosis and only allo-SCT cures it.
- `connects-to` → **[Myelodysplastic Syndromes](../mds/README.md)** — Myelofibrosis and MDS are overlapping clonal marrow disorders sharing mutations (ASXL1, SRSF2, U2AF1, TP53) and AML transformation risk; marrow fibrosis can appear in MDS and MDS/MPN overlap syndromes sit between them; both cause cytopenias graded by blast percentage.
- `connects-to` → **[Polycythemia Vera](../polycythemia-vera/README.md)** — Polycythemia vera can evolve into post-PV myelofibrosis (~10-20% at 15 years): the JAK2 V617F clone exhausts marrow, fibrosis accumulates, and the picture converges with primary myelofibrosis — splenomegaly, leukoerythroblastosis and cytopenias; ruxolitinib treats both.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Myelofibrosis disrupts red-cell production: marrow fibrosis forces extramedullary hematopoiesis and yields a leukoerythroblastic film with teardrop cells (dacrocytes); progressive anemia is a core prognostic feature, and momelotinib uniquely improves it by lowering hepcidin.
- `connects-to` → **[Essential Thrombocythemia](../essential-thrombocythemia/README.md)** — Essential thrombocythemia and polycythemia vera can both evolve into secondary (post-ET, post-PV) myelofibrosis: years of JAK2/CALR/MPL proliferation give way to a fibrotic, failing marrow with cytopenias and splenomegaly—a shared late fate of the chronic MPNs.
- `connects-to` → **[AML](../aml/README.md)** — Myelofibrosis carries the highest leukemic-transformation risk of the classic MPNs: ~10-20% progress to a treatment-resistant blast-phase AML as the clone acquires TP53 and other lesions, so high-risk patients are considered for allogeneic transplant, the only cure.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — The marrow fibrosis of myelofibrosis is reactive, not clonal: malignant megakaryocytes pour out TGF-β and PDGF that drive resident fibroblasts to deposit collagen and reticulin, crowding out hematopoiesis—the scarring cells are normal bystanders recruited by the clone.
- `connects-to` → **[Chronic Myeloid Leukemia](../cml/README.md)** — Myelofibrosis and CML are both chronic myeloproliferative neoplasms with marrow fibrosis but different drivers: CML's BCR-ABL is targeted by imatinib, while myelofibrosis's JAK2/CALR/MPL mutations are treated with JAK inhibitors—both can transform to leukemia.
- `connects-to` → **[Gout](../gout/README.md)** — Myelofibrosis commonly causes secondary gout: the high cell turnover of the proliferating clone floods the blood with purines that become uric acid, so hyperuricemia and gout flares accompany the disease—sometimes a clue to an underlying myeloproliferative neoplasm.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Myelofibrosis drives extramedullary hematopoiesis in the liver: as marrow fibrosis crowds out blood production, hematopoiesis relocates to spleen and liver, enlarging them—and the displaced blood-forming tissue can cause portal hypertension.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Myelofibrosis is bone marrow turned to scar: malignant megakaryocytes secrete TGF-beta that drives fibroblasts to fill the marrow with fibrosis, so blood production fails and shifts to liver and spleen (extramedullary hematopoiesis)—the disease's defining lesion.
- `connects-to` → **[MPL](../../03-molecular/mpl/README.md)** — MPL is one of myelofibrosis's three driver mutations: activating the thrombopoietin receptor MPL (like JAK2 and CALR) switches on JAK-STAT to drive the clone, so testing JAK2/CALR/MPL classifies the disease and rare triple-negative cases carry worse prognosis.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Myelofibrosis causes anemia despite high erythropoietin: marrow scarring crowds out red-cell production so EPO rises but cannot be answered, leaving transfusion-dependent anemia—a key driver of symptoms that JAK inhibitors and newer agents try to relieve.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Myelofibrosis warps platelet production: clonal megakaryocytes first overproduce platelets, but as the marrow scars they fail, so patients swing from thrombosis-prone thrombocytosis to dangerous thrombocytopenia—platelet count tracking the march to marrow failure.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Myelofibrosis is named for the collagen it lays down: cytokines from the malignant clone drive marrow fibroblasts to flood the marrow with reticulin and collagen, crowding out blood production—so the fibrosis, though reactive, is the disease's defining lesion.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Myelofibrosis is in part an inflammatory disease: the JAK-STAT-driven clone pours out cytokines that cause fevers, weight loss, and night sweats, so JAK inhibitors like ruxolitinib ease symptoms by dampening this inflammatory storm more than by killing the clone.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — Myelofibrosis scars the marrow through PDGF: the clonal megakaryocytes pour out PDGF and TGF-beta that drive fibroblasts to lay down the collagen replacing blood-forming marrow—so anti-fibrotic targeting of these cytokines is explored beyond JAK inhibition.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — The only cure for myelofibrosis is allogeneic transplant via donor T cells: cytotoxic T cells from the graft mount a graft-versus-leukemia attack on the clone, the lone therapy that can reverse marrow fibrosis—at the cost of transplant risk.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Progressive anemia defines advancing myelofibrosis: marrow fibrosis and ineffective erythropoiesis cause worsening transfusion-dependent anemia, a key prognostic factor and the reason new agents target the anemia, not just the spleen.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — Myelofibrosis wastes the body through IL-6 and inflammation: the malignant clone and marrow stroma pour out IL-6 and other cytokines that cause the fevers, weight loss, and cachexia, and drive the fibrosis—why JAK inhibitors ease symptoms so well.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — Myelofibrosis pushes blood-making into the liver: as scarred marrow fails, hematopoiesis relocates to the liver and spleen (extramedullary hematopoiesis), enlarging them around the hepatocytes—the massive organomegaly typical of advanced disease.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Myelofibrosis is fueled by an inflammatory marrow rich in macrophages: monocytes and macrophages, with abnormal megakaryocytes, secrete the TGF-β and cytokines that drive fibroblasts to scar the marrow.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Myelofibrosis distorts the body's iron: transfusion-dependent anemia delivers iron the body cannot shed, building toxic overload, while inflammation also locks iron away from red-cell making—worsening the very anemia driving the transfusions.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Severe myelofibrosis anemia overworks the heart: to ship enough oxygen with too few red cells, the heart pumps harder in a high-output state, and transfusional iron can deposit in the muscle, together straining it toward failure.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Myelofibrosis spills immature cells into the blood: a scarred marrow forces a leukoerythroblastic picture, releasing early neutrophil precursors alongside teardrop red cells—a blood smear that flags hematopoiesis under siege.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Myelofibrosis shows up in imaging: X-ray photons can reveal osteosclerosis from the fibrotic marrow, and low-dose splenic irradiation is one way to shrink a massively enlarged, painful spleen.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — Myelofibrosis can harden bone as well as marrow: activated osteoblasts lay down osteosclerosis that thickens the cavity walls, a bony counterpart to the reticulin and collagen scarring inside.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Myelofibrosis can colonize the chest: extramedullary hematopoiesis and the disease's clotting tendency drive pulmonary hypertension, adding breathlessness to its anemia and splenomegaly.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy catches the cell driving the scarring: dysplastic megakaryocytes spill their granule contents — TGF-β and PDGF — that goad marrow fibroblasts into laying down the collagen and reticulin choking out blood production.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Myelofibrosis can turn marrow to stone: as fibrosis advances it often brings osteosclerosis, a thickening of the bone with extra calcium-phosphate mineral that shows as dense, sclerotic bones on X-ray.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — The kidney feels the disease's overflow: extramedullary blood formation can settle there, and the rapid cell turnover floods the blood with uric acid that crystallizes in the tubules, threatening urate nephropathy.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Myelofibrosis builds a dense new vasculature in the marrow: the malignant clone drives VEGF, and the resulting marrow neoangiogenesis — a rise in microvessel density — is part of the pathology pathologists grade alongside the scarring.
- `connects-to` → **[Albumin](../../03-molecular/albumin/README.md)** — The disease wastes the body: drenching night sweats, fevers, and weight loss are hallmark constitutional symptoms, and the cachexia they cause lowers albumin — a marker of the burden that figures into prognosis.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Even as it scars the marrow, myelofibrosis stays prothrombotic: like its sister myeloproliferative neoplasms it raises the risk of venous and arterial clots, especially with a JAK2 mutation and a high blood count earlier in the disease.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — The churning marrow spills minerals: high cell turnover, and its lysis under treatment, release phosphate and urate into the blood, fueling the gout and hyperuricemia that often accompany myelofibrosis.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Blood-making strays into the gut, and the swollen spleen backs up its veins: extramedullary hematopoiesis can stud the bowel, while massive splenomegaly raises portal pressure into varices that bleed into the GI tract.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Blood-forming masses can squeeze the cord: paraspinal extramedullary hematopoiesis is a rare but urgent complication of myelofibrosis, the tissue pressing on the spinal cord and its neurons to cause weakness and sensory loss.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Myelofibrosis spills blood-making into the vessels: the malignant clone also marks endothelial cells, which help home extramedullary hematopoiesis to spleen and liver and contribute to the thrombosis that complicates the disease.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Myelofibrosis smolders with inflammation: the mutant clone switches on NF-κB, driving the inflammatory cytokine flood behind its fevers and weight loss and the fibrosis-promoting signals that scar the marrow.
- `connects-to` → **[Pulmonary Arterial Hypertension](../pulmonary-arterial-hypertension/README.md)** — Blood-making can settle in the lungs: extramedullary hematopoiesis and clot showers from myelofibrosis can raise pulmonary artery pressure, a recognized complication that strains the right heart.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — A homing signal goes awry: disrupted CXCL12-CXCR4 signaling lets hematopoietic stem cells escape the fibrotic marrow into the blood, where they seed the spleen and liver — the extramedullary hematopoiesis behind the massive splenomegaly.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Clonal mast cells join the fibrotic crowd: mast cells are expanded in myelofibrosis marrow and, like the driver megakaryocytes, secrete profibrotic mediators that help lay down the collagen and reticulin scar.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — The failing marrow leaves patients defenseless: falling neutrophil counts and the immunosuppression of advanced disease and its treatment make infection and sepsis a leading cause of death in myelofibrosis.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — The disease runs on JAK-STAT: the JAK2/CALR/MPL drivers funnel into constitutive STAT signaling, with STAT3 supporting the clone's proliferation and the inflammatory cytokine output — the pathway that ruxolitinib's JAK inhibition reins in.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — The JAK2 clone inflames the arteries: like other JAK2-driven blood disorders and clonal hematopoiesis, myelofibrosis accelerates atherosclerosis, its inflamed clonal leukocytes worsening plaque and cardiovascular risk.
- `connects-to` → **[Stroke](../stroke/README.md)** — Sticky blood throws arterial clots: the hyperviscosity and activated platelets of myelofibrosis raise the risk of arterial thrombosis, including ischemic stroke, alongside its better-known venous clotting.
- `connects-to` → **[Tuberculosis](../tuberculosis/README.md)** — Its JAK inhibitor can wake latent TB: ruxolitinib, the mainstay drug for myelofibrosis, suppresses interferon-γ signaling and impairs the granuloma, so latent tuberculosis can reactivate during treatment.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Neutropenia and JAK blockade open the lung to mold: cytopenias from marrow fibrosis plus the immunosuppression of ruxolitinib leave patients prone to invasive aspergillosis and other opportunistic infections.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Transfusion iron and chronic anemia burden the heart: the lifelong red-cell support for myelofibrosis anemia deposits iron in the myocardium, and the sustained anemia adds high-output strain, together risking heart failure.
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — Its JAK-inhibitor therapy reawakens shingles: ruxolitinib, a mainstay for myelofibrosis, suppresses immunity and characteristically reactivates latent varicella-zoster as herpes zoster, prompting vaccination and vigilance.
- `connects-to` → **[Pneumocystis jirovecii](../../../02-pathogen/03-fungi/pneumocystis-jirovecii/README.md)** — JAK inhibition opens the lung to Pneumocystis: ruxolitinib's immunosuppression, atop the immune dysfunction of myelofibrosis, can permit opportunistic Pneumocystis pneumonia.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A heavy symptom burden weighs on mood: the relentless fatigue, pruritus, drenching sweats and massive splenomegaly of myelofibrosis erode quality of life and contribute to depression.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Extramedullary haematopoiesis swells the gut organs: when the scarred marrow pushes blood-making into the spleen and liver, the massive splenomegaly causes early satiety and portal hypertension with varices.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Transfusion iron overload poisons the glands: transfusion-dependent myelofibrosis accumulates iron that deposits in the pancreas, pituitary and thyroid, causing diabetes and other endocrinopathies.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A progressive marrow cancer breeds worry: the worsening cytopenias, transfusion dependence and threat of leukaemic transformation in myelofibrosis foster chronic health anxiety alongside depression.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It hardens and pains the bones: the marrow fibrosis of myelofibrosis is accompanied by osteosclerosis seen on imaging and by deep, debilitating bone pain as the skeleton's blood factory is replaced by scar.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Its blood-making can crush the cord: extramedullary haematopoiesis in the epidural space can compress the spinal cord, a neurological emergency presenting with back pain, weakness and sensory loss.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It can itch and surface on the skin: myelofibrosis causes intractable aquagenic pruritus and, rarely, cutaneous extramedullary haematopoiesis appearing as red-brown skin nodules.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It massively swells the spleen: extramedullary haematopoiesis enlarges the spleen, often hugely, causing early satiety and splenic infarction, and may require splenectomy or splenic irradiation.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Blood-making spreads to the chest: extramedullary haematopoiesis in the lungs and pleura causes effusions and contributes to the pulmonary hypertension of advanced disease.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It strains the kidney: extramedullary haematopoiesis and hyperuricaemia from high cell turnover can impair renal function, and a rare myelofibrosis-associated glomerulopathy occurs.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — JAK inhibitors are its mainstay drug: ruxolitinib and other JAK1/2 inhibitors shrink the spleen and ease symptoms of myelofibrosis, the first targeted therapy for the disease.
- `connects-to` → **[Aspirin](../../../03-medicine/01-modern/04-cardio/aspirin/README.md)** — Low-dose aspirin counters the clotting: like other myeloproliferative neoplasms, myelofibrosis carries a thrombotic risk that low-dose aspirin helps reduce in lower-risk patients.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Treatment threatens fertility: cytoreductive drugs and the allogeneic stem-cell transplant that can cure myelofibrosis impair fertility, relevant to younger patients.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Cytoreduction and conditioning: hydroxyurea controls the splenomegaly and high counts of myelofibrosis, and intensive conditioning chemotherapy precedes the allogeneic stem-cell transplant that is its only cure.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — It can harden the bone: advanced myelofibrosis often brings osteosclerosis, thickening the bony trabeculae as marrow fibrosis spills into a denser skeleton visible on imaging.
- `connects-to` → **[Aplastic Anemia](../aplastic-anemia/README.md)** — Two routes to marrow failure: myelofibrosis cytopenias come from a fibrosed, crowded marrow, whereas aplastic anaemia leaves an empty hypocellular marrow — opposite histology converging on pancytopenia.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Blood-making relocates to the liver: as marrow fibrosis fails haematopoiesis, extramedullary blood formation sets up in the spleen and the hepatic lobules, enlarging the liver alongside the massive spleen.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — It still thromboses: like other myeloproliferative neoplasms, myelofibrosis's JAK2-mutant blood cells inflame the arterial wall and raise the risk of arterial thrombosis, stroke and heart attack.
- `connects-to` → **[Leishmaniasis](../leishmaniasis/README.md)** — An infectious mimic of the big spleen: visceral leishmaniasis produces massive splenomegaly, pancytopenia and marrow change that imitate myelofibrosis, a key infectious differential in endemic regions.
- `connects-to` → **[GvHD](../gvhd/README.md)** — The only cure, and its cost: allogeneic stem-cell transplant is the sole curative therapy for myelofibrosis, but graft-versus-host disease is a major source of its transplant-related mortality.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Hidden in the lungs: extramedullary haematopoiesis and microvascular megakaryocyte emboli in myelofibrosis can lodge in the alveolar capillaries, contributing to the pulmonary hypertension that worsens prognosis.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — A mimic to exclude: marrow infiltration by metastatic cancer such as breast cancer causes reactive fibrosis and a leukoerythroblastic blood film that can imitate primary myelofibrosis.
- `connects-to` → **[Von Willebrand Factor](../../03-molecular/von-willebrand-factor/README.md)** — Bleeding amid clotting: high platelet counts in myelofibrosis can adsorb and clear high-molecular-weight von Willebrand multimers, causing an acquired von Willebrand syndrome and paradoxical bleeding in a prothrombotic disease.
- `connects-to` → **[Inherited Thrombophilia](../inherited-thrombophilia/README.md)** — Layered thrombotic risk: myelofibrosis is an acquired JAK2-driven prothrombotic state prone to splanchnic-vein thrombosis, a risk amplified when an inherited thrombophilia coexists.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Extramedullary haematopoiesis: blood-forming tissue colonises sites outside the marrow in myelofibrosis, and masses of epidural EMH can compress the spinal cord and nerve roots, a rare neurological emergency.
- `connects-to` → **[Type I Interferon](../../03-molecular/type-i-interferon/README.md)** — Disease-modifying therapy: pegylated interferon-alpha can reduce the JAK2/CALR-mutant clone and even reverse marrow fibrosis in early myelofibrosis, unlike purely palliative JAK inhibitors.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — High-risk mutation: loss-of-function EZH2 mutations are recurrent in myelofibrosis and mark a poorer prognosis among its epigenetic driver lesions.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Hypoxic fibrotic niche: HIF-1α-driven angiogenesis and hypoxia characterise the densely fibrotic, neovascularised marrow of myelofibrosis.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Niche-damaging cytokine: IL-1β secreted by the mutant clone injures the bone-marrow mesenchymal niche and drives the inflammatory cytokine milieu that promotes fibrosis in myelofibrosis.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Clonal selective advantage: TNF-α in the myelofibrosis marrow suppresses normal progenitors while JAK2-mutant cells resist it, giving the malignant clone a growth edge amid chronic inflammation.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Matrix and osteosclerosis: osteopontin released by megakaryocytes and stroma contributes to the marrow fibrosis and the osteosclerosis that thickens trabecular bone in advanced myelofibrosis.
- `connects-to` → **[PF4](../../03-molecular/pf4/README.md)** — Platelet factor 4 (CXCL4) released by the abnormal megakaryocytes of myelofibrosis is a direct driver of fibroblast activation and collagen deposition—a key megakaryocyte-to-stroma signal behind the reticulin and collagen marrow fibrosis that defines the disease.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — The malignant clone of myelofibrosis depends on BCL-xL/BCL-2 for survival, the rationale for adding the BCL-2/BCL-xL inhibitor navitoclax to ruxolitinib in patients whose disease progresses on JAK inhibition alone.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — Dysregulated RANKL-driven osteoclast and osteoblast activity contributes to the osteosclerosis that thickens and remodels trabecular bone in advanced myelofibrosis, further narrowing the marrow space and worsening cytopenias.
- `connects-to` → **[SF3B1](../../03-molecular/sf3b1/README.md)** — Spliceosome mutations such as SF3B1, U2AF1 and SRSF2, acquired alongside the JAK2/CALR/MPL driver, mark the higher-risk myelofibrosis more likely to progress to leukemia and inform prognostic scoring.
- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — Clonal megakaryocytes release basic FGF that, with PDGF and TGF-β, signals through FGFR on marrow fibroblasts to drive the reticulin and collagen fibrosis that progressively replaces the hematopoietic marrow.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins released in the myelofibrotic marrow amplify the chronic inflammation that both drives the constitutional symptoms and feeds the fibrotic, cytokine-rich niche supporting the malignant clone.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — JAK2 V617F signals through the MAPK-ERK1/2 pathway as well as STAT5, contributing to the clonal myeloproliferation of myelofibrosis and to incomplete responses to JAK inhibition.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — High-molecular-risk epigenetic and splicing mutations (with the SF3B1 already mapped) accumulate on the JAK2/CALR/MPL driver in myelofibrosis, accelerating its progression to leukemic transformation.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Chronic NLRP3-inflammasome activation and IL-1β (already mapped) sustain the inflammatory milieu that drives the marrow fibrosis and constitutional symptoms of myelofibrosis.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β released by the clonal megakaryocytes signals through SMAD4 (TGF-β mapped) to activate marrow fibroblasts that lay down the collagen (mapped) reticulin fibrosis defining myelofibrosis.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — JAK2 (mapped) also engages PI3K-AKT-mTOR, a parallel survival-and-proliferation pathway supporting the myelofibrosis clone alongside JAK-STAT.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 inactivation drives the progression of myelofibrosis to the blast phase, a secondary acute myeloid leukemia with dismal prognosis.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — JAK2-driven PI3K-AKT-mTOR signaling (JAK2 and AKT mapped) supports clonal proliferation in myelofibrosis and is a target of mTOR-inhibitor trials.
- `connects-to` → **[RUNX1](../../03-molecular/runx1/README.md)** — Acquisition of RUNX1 mutations marks clonal evolution of myelofibrosis toward blast-phase (secondary AML) transformation.
- `connects-to` → **[IDH1](../../03-molecular/idh1/README.md)** — IDH1 mutations are recurrent high-risk lesions driving epigenetic dysregulation and leukemic transformation in myelofibrosis, complementing the EZH2/DNMT3A lesions already mapped.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 secreted by the clonal megakaryocytes is a key driver of the bone-marrow fibrosis that defines myelofibrosis.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling (type-I interferon already mapped) shapes the inflammatory bone-marrow milieu and contributes to the cytopenias of myelofibrosis.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING amplifies the chronic inflammatory bone-marrow microenvironment that drives the fibrosis of myelofibrosis.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors regulate hematopoietic stem-cell quiescence and oxidative-stress handling disrupted in the clonal myeloproliferation of myelofibrosis.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β dysregulation contributes to the aberrant megakaryocyte and progenitor signaling that drives the marrow fibrosis of myelofibrosis.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6 cell-cycle activity supports the clonal proliferation of JAK2/CALR/MPL-mutant progenitors in myelofibrosis.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated cytotoxic immunosurveillance targets the neoantigen-bearing CALR-mutant clone of myelofibrosis.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis and contributes to the leukemic evolution of myelofibrosis.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family and LYN kinase signaling downstream of the constitutively active JAK2 axis supports the megakaryocyte and progenitor survival of myelofibrosis.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped), downstream of JAK2, supports the survival of the clonal cells of myelofibrosis.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the survival of the megakaryocytes and clonal cells of myelofibrosis.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of the clonal hematopoietic cells of myelofibrosis.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-family chemokine signaling participates in the bone-marrow niche and immune interactions of myelofibrosis.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of myelofibrosis.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the inflammatory bone-marrow microenvironment and fibrosis of myelofibrosis.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory and fibrotic bone-marrow microenvironment of myelofibrosis.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory bone-marrow microenvironment of myelofibrosis.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the megakaryocyte and stromal-cell signaling contributing to the marrow fibrosis of myelofibrosis.
- `connects-to` → **[Activin A](../../03-molecular/activin-a/README.md)** — Anaemia and fibrosis: activin A signalling through ACVR2 both suppresses erythropoiesis, the target of luspatercept and momelotinib for myelofibrosis anaemia, and promotes fibroblast activation, giving it a dual role in the disease.
- `connects-to` → **[Sclerostin](../../03-molecular/sclerostin/README.md)** — Osteosclerosis: advanced myelofibrosis develops osteosclerosis with increased bone density, and dysregulated Wnt signalling with altered sclerostin contributes to the bone remodelling that accompanies the marrow fibrosis.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Iron and anaemia: chronic inflammation in myelofibrosis raises IL-6-driven hepcidin (IL-6 already mapped), contributing to the anaemia of inflammation, while transfusion dependence adds iron overload requiring chelation.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Progressive anaemia: worsening anaemia with falling haemoglobin, from marrow failure, splenic sequestration and JAK-inhibitor therapy, is a defining feature of myelofibrosis driving transfusion dependence and momelotinib or luspatercept use.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — Marrow neoangiogenesis: myelofibrosis shows increased bone-marrow microvascular density supported by angiopoietin-Tie2 signalling alongside VEGF (already mapped), part of the disordered fibrotic microenvironment created by the clone.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Urate overproduction: the high cell turnover of myelofibrosis raises purine catabolism through xanthine oxidase, producing hyperuricaemia and gout that are managed with allopurinol alongside the disease-directed therapy.
- `connects-to` → **[Ferroportin](../../03-molecular/ferroportin/README.md)** — Iron-restricted anaemia: the chronic inflammation of myelofibrosis raises hepcidin (already mapped), which degrades ferroportin to trap iron in macrophages, contributing to the iron-restricted anaemia that adds to the marrow-failure anaemia.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Cytokine milieu: IL-10 among the cytokines of the inflammatory myelofibrosis microenvironment counters the IL-6, TNF and IL-1 (already mapped) that drive the constitutional symptoms and fibrosis, part of the dysregulated cytokine balance of the disease.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Splenomegaly and portal flow: the massive splenomegaly of myelofibrosis raises portal blood flow, and dysregulated nitric oxide contributes to the splanchnic vasodilation and portal hypertension that can complicate the extramedullary haematopoiesis.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage niche: IL-4 polarises the marrow macrophages toward an M2 phenotype (IL-10 already mapped), part of the inflammatory, fibrotic microenvironment (TGF-β and PDGF already mapped) of the myelofibrosis marrow.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Marrow adipokine signalling: leptin from the marrow adipose tissue signals to the clonal and stromal cells, part of the metabolic microenvironment of the fibrotic myelofibrosis marrow.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Marrow-adipocyte crosstalk: adiponectin, with leptin (already mapped), links the marrow adipocytes to the haematopoietic and stromal cells, part of the altered marrow microenvironment that accompanies the fibrosis of myelofibrosis.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Profibrotic type-2 arm: IL-13, with IL-4 (already mapped), contributes to the M2 macrophage (already mapped) and profibrotic (TGF-β already mapped) signalling that drives the marrow fibrosis of myelofibrosis.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Marrow adipokine: resistin, with leptin and adiponectin (already mapped), is part of the marrow-adipocyte adipokine crosstalk of the fibrotic marrow microenvironment of myelofibrosis.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc and haematopoiesis: zinc is required for the haematopoiesis disrupted in myelofibrosis, and the zinc-copper balance is part of the trace-metal milieu of the altered marrow microenvironment.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Pro-fibrotic macrophages: the marrow macrophages and the monocyte-derived fibrocytes contribute to the reactive fibrosis (TGF-β and PDGF already mapped) of myelofibrosis.
- `connects-to` → **[AML](../aml/README.md)** — Blast-phase transformation: myelofibrosis carries the risk of blast-phase transformation to acute myeloid leukaemia (the increasing blasts; TP53 and RUNX1 already mapped), the terminal event.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Transfusion iron overload: the transfusion-dependent anaemia (haemoglobin already mapped) of myelofibrosis causes the iron overload (hepcidin and ferroportin already mapped), needing chelation.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Clonal immunosurveillance: the NK cells (perforin already mapped) provide the immune surveillance of the JAK2/CALR (already mapped)-mutant clone of myelofibrosis, an arm augmented by the interferon (type-I interferon already mapped) therapy.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 inflammatory MF: the IFN-γ of the T cells (with the type-I interferon already mapped) is the type-II interferon arm of the chronic inflammation (IL-6 and TNF already mapped) that drives the fibrosis of myelofibrosis.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the inflammatory microenvironment of myelofibrosis.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the inflammatory bone-marrow (already mapped) microenvironment of myelofibrosis.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the chronic inflammation (IL-6 and TNF already mapped) that drives the fibrosis of myelofibrosis.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the inflammatory microenvironment of myelofibrosis.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the chronic inflammatory marrow niche that drives the fibrosis (TGF-β and PDGF already mapped) of myelofibrosis.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its activation (with C3 already mapped) contribute to the inflammasome (NLRP3 already mapped)-linked chronic inflammation and the thrombotic risk of myelofibrosis.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling links the complement to the neutrophil and platelet (PF4 already mapped) activation of the thromboinflammatory dimension of myelofibrosis.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the thromboinflammatory marrow niche of myelofibrosis.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Transfusional iron overload: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin and ferroportin already mapped) of the anaemia and the transfusional iron overload of myelofibrosis.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Marrow fibrosis: periostin, downstream of the TGF-β (already mapped) signalling, is a matricellular mediator of the reactive marrow fibrosis (with osteopontin and collagen already mapped) that defines myelofibrosis.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Marrow alarmin: TSLP, released from the dysplastic marrow stroma and megakaryocytes (thrombopoietin already mapped) under JAK2 (already mapped) and cytokine stress, activates the dendritic cells and mast cells in the fibrotic marrow niche of myelofibrosis.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-marrow axis: bradykinin, generated by the contact-kinin pathway in the extramedullary haematopoiesis sites (liver and spleen already mapped), amplifies the endothelial permeability and the inflammatory cytokine (TNF-α and IL-1β already mapped) milieu of myelofibrosis.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement/kinin gate: C1-esterase inhibitor limits the classical complement (complement C3, C5 and C5aR1 already mapped) and contact-kinin (bradykinin already mapped) cascades in the fibrotic marrow and splenic extramedullary haematopoiesis sites of myelofibrosis.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Marrow mast-cell effector: histamine, released by mast cells in the fibrotic marrow niche of myelofibrosis, amplifies the inflammatory cytokine (TNF-α and IL-1β already mapped) signalling and the JAK2-driven (already mapped) proliferative cascade of the disease.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Antioxidant haematopoietic protection: melatonin, via MT1/MT2 receptors on haematopoietic progenitors (already mapped), scavenges ROS (already mapped) from dysfunctional mitochondria and may attenuate oxidative damage driving the clonal evolution of myelofibrosis.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Immune-endocrine coupling: prolactin, elevated during chronic myeloproliferation, potentiates the macrophage (already mapped) and NK-cell (already mapped) signalling and may amplify the inflammatory cytokine milieu (TNF-α and IL-6 already mapped) of myelofibrosis.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — MF testosterone: androgen signalling on haematopoietic progenitors attenuates the TGF-β (already mapped) fibrotic drive in the marrow; testosterone deficiency worsens the JAK2 (already mapped) MPN anaemia and bone-marrow (already mapped) failure of myelofibrosis.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — MF serotonin: platelet (already mapped) serotonin amplifies the thrombopoietin (already mapped) megakaryocyte hyperplasia and thrombotic risk; 5-HT2 signalling on fibroblasts (already mapped) potentiates the TGF-β (already mapped) fibrotic cascade of myelofibrosis.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — MF oxytocin: oxytocin receptors on bone-marrow (already mapped) stromal cells modulate the immune-inflammatory microenvironment of myelofibrosis; oxytocin attenuates the macrophage (already mapped) and fibroblast (already mapped) TGF-β (already mapped) fibrotic signalling.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — MF vasopressin: vasopressin (ADH) modulates the bone-marrow (already mapped) stromal microenvironment via V1/V2 receptor signalling; vasopressin amplifies NF-κB (already mapped) and TGF-β (already mapped) driven fibroblast (already mapped) activation in the myelofibrotic marrow.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — MF selenium: selenoproteins suppress ROS-driven NF-κB (already mapped) and TGF-β (already mapped) fibrotic signalling in myelofibrosis; selenium deficiency amplifies macrophage (already mapped) inflammatory cytokine release and bone-marrow (already mapped) oxidative stress.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — MF iodine: thyroid-hormone signalling modulates bone-marrow (already mapped) erythropoiesis and macrophage (already mapped) immune surveillance; iodine deficiency amplifies NF-κB (already mapped) and TGF-β (already mapped) driven fibroblast (already mapped) fibrotic activity.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — MF magnesium: magnesium supports bone-marrow (already mapped) haematopoiesis and macrophage (already mapped) anti-inflammatory resolution; magnesium deficiency amplifies NF-κB (already mapped) and TGF-β (already mapped) fibrotic signalling in myelofibrosis.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — MF copper: copper, via ceruloplasmin and SOD, scavenges ROS in bone-marrow (already mapped) macrophages (already mapped) and fibroblasts (already mapped); copper deficiency amplifies NF-κB (already mapped) and TGF-β (already mapped) fibrotic signalling in myelofibrosis.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — MF sodium: high dietary sodium promotes macrophage (already mapped) and mast-cell (already mapped) pro-inflammatory activation; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) amplifies the neutrophil (already mapped) fibrotic cascade of myelofibrosis.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — MF potassium: potassium channels regulate macrophage (already mapped) and mast-cell (already mapped) ion homeostasis in the myelofibrosis bone marrow; potassium depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) fibrotic cascade of myelofibrosis.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — MF chloride: chloride channels regulate macrophage (already mapped) and neutrophil (already mapped) ion homeostasis in the myelofibrosis bone marrow; chloride imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) fibrotic cascade of myelofibrosis.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^verstovsek-2012-comfort1]: Verstovsek S, Mesa RA, Gotlib J, et al. A double-blind, placebo-controlled trial of ruxolitinib for myelofibrosis. *N Engl J Med.* 2012;366(9):799-807. [doi:10.1056/NEJMoa1110557](https://doi.org/10.1056/NEJMoa1110557) · [PubMed 22375971](https://pubmed.ncbi.nlm.nih.gov/22375971/)
[^harrison-2012-comfort2]: Harrison C, Kiladjian JJ, Al-Ali HK, et al. JAK inhibition with ruxolitinib versus best available therapy for myelofibrosis. *N Engl J Med.* 2012;366(9):787-798. [doi:10.1056/NEJMoa1110556](https://doi.org/10.1056/NEJMoa1110556) · [PubMed 22375970](https://pubmed.ncbi.nlm.nih.gov/22375970/)
