---
schema: human-scale-entry/v1
id: myeloproliferative-neoplasms
name: Myeloproliferative Neoplasms
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Myeloproliferative neoplasms (PV, ET, MF) are driven by JAK2 V617F in >95% of PV and ~50-60% of ET/MF; CALR and MPL mutations account for remaining cases. Ruxolitinib (JAK1/2 inhibitor) is standard for myelofibrosis and PV; alloSCT is curative for high-risk MF."
aliases: ["myeloproliferative neoplasms", "MPN", "polycythemia vera", "PV", "essential thrombocythemia", "ET", "myelofibrosis", "MF", "primary myelofibrosis", "JAK2 V617F MPN", "Philadelphia-negative MPN"]
sources:
  - id: verstovsek-2012-comfort-i
    type: peer-reviewed
    cite: "Verstovsek S, Mesa RA, Gotlib J, et al. A double-blind, placebo-controlled trial of ruxolitinib for myelofibrosis. N Engl J Med. 2012;366(9):799-807."
    doi: "10.1056/NEJMoa1110557"
    pmid: "22375971"
    url: "https://doi.org/10.1056/NEJMoa1110557"
  - id: vannucchi-2015-response
    type: peer-reviewed
    cite: "Vannucchi AM, Kiladjian JJ, Griesshammer M, et al. Ruxolitinib versus standard therapy for the treatment of polycythemia vera. N Engl J Med. 2015;372(5):426-435."
    doi: "10.1056/NEJMoa1409002"
    pmid: "25426978"
    url: "https://doi.org/10.1056/NEJMoa1409002"
cross_links:
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Ruxolitinib (JAK1/2 inhibitor, COMFORT-I/II) reduces spleen volume >35% in ~40% of MF patients and prolongs OS; ruxolitinib also standard for PV (RESPONSE: reduced HCT and spleen); fedratinib and pacritinib are alternative JAK2 inhibitors for MF with cytopenias."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "JAK2 V617F → constitutive STAT5 phosphorylation → EPO-independent erythropoiesis in PV; STAT5 is the primary effector of JAK2 → BCL-XL, CCND1, MYC → erythroid survival; STAT3 mediates inflammatory cytokine production in MF (IL-6, IL-8)."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "EPO → EPOR → JAK2 → STAT5 is the normal erythropoiesis axis; JAK2 V617F bypasses EPO requirement → autonomous red cell production → polycythemia in PV; serum EPO is suppressed in PV (EPO-independent erythropoiesis) and elevated in secondary polycythemia."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β1 secreted by MPN megakaryocytes drives collagen deposition → bone marrow fibrosis in MF; TGF-β/SMAD pathway activation is central to MF fibrosis; luspatercept (activin receptor ligand trap targeting SMAD2/3) approved for MF-associated anemia (INDEPENDENCE trial)."
  - target: 01-human/07-system/polycythemia-vera
    relation: connects-to
    note: "Polycythemia vera is the erythroid-predominant MPN — JAK2 V617F (often homozygous via 9p uniparental disomy) drives EPO-independent erythrocytosis, raising thrombosis risk; managed with phlebotomy to HCT <45% and aspirin, and it can evolve to post-PV myelofibrosis."
  - target: 01-human/03-molecular/jak2
    relation: connects-to
    note: "The JAK2 V617F mutation in the JH2 pseudokinase domain unifies the MPNs — present in ~95% of PV and ~55-60% of ET and MF — by removing autoinhibition for constitutive JAK-STAT signaling; allele burden tracks phenotype (heterozygous→ET, homozygous→PV)."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "MPNs are clonal stem-cell diseases of the bone marrow: panmyeloid hypercellularity in PV, megakaryocytic hyperplasia in ET, and progressive reticulin/collagen fibrosis (MF-0 to MF-3) in myelofibrosis that drives marrow failure and extramedullary hematopoiesis with splenomegaly."
  - target: 01-human/07-system/cmml
    relation: connects-to
    note: "Chronic myelomonocytic leukemia is the MDS/MPN-overlap cousin of the classic myeloproliferative neoplasms: it shares their JAK2/RAS-driven proliferation, splenomegaly, and JAK-inhibitor responsiveness, but adds the peripheral monocytosis and dysplasia of MDS."
  - target: 01-human/07-system/myelofibrosis
    relation: connects-to
    note: "Myelofibrosis is the most aggressive classic MPN: JAK2/CALR/MPL-driven megakaryocytes secrete TGF-β that scars the marrow with reticulin and collagen, forcing extramedullary hematopoiesis (splenomegaly) and marrow failure; it arises de novo or evolves from PV or ET."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "Splenomegaly is the clinical signature of the myeloproliferative neoplasms, most extreme in myelofibrosis where the spleen takes over blood production (extramedullary hematopoiesis) and can fill the abdomen; JAK inhibitors (ruxolitinib) shrink it, splenectomy a last resort."
  - target: 01-human/07-system/essential-thrombocythemia
    relation: connects-to
    note: "Essential thrombocythemia is one of the three classic BCR-ABL-negative myeloproliferative neoplasms, alongside polycythemia vera and myelofibrosis: a JAK2, CALR, or MPL mutation drives clonal megakaryocyte overproduction and a high platelet count, with thrombosis the main risk."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Platelets are central to MPN morbidity: clonal megakaryocytes overproduce platelets that are also qualitatively abnormal, so essential thrombocythemia and polycythemia vera cause both thrombosis and—at very high counts—bleeding from acquired von Willebrand defects."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Thrombosis is the leading cause of death in myeloproliferative neoplasms: JAK2-mutant blood is prothrombotic, producing arterial and venous clots including splanchnic-vein thromboses (Budd-Chiari, portal vein)—so cytoreduction and aspirin aim to prevent VTE."
  - target: 01-human/07-system/cml
    relation: connects-to
    note: "CML is the classic BCR-ABL-positive myeloproliferative neoplasm, set apart from the JAK2/CALR/MPL-driven 'Philadelphia-negative' MPNs: all overproduce mature myeloid cells, but CML's defining t(9;22) kinase makes it uniquely controllable with imatinib."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "Myeloproliferative neoplasms can transform into acute myeloid leukemia: chronic clonal proliferation accumulates mutations until differentiation fails and blasts take over—post-MPN AML carries a grim prognosis, the feared endpoint of these diseases."
  - target: 01-human/07-system/gout
    relation: connects-to
    note: "MPNs commonly cause secondary gout: the high cell turnover floods the blood with purines that break down to uric acid, so hyperuricemia and gout flares accompany polycythemia vera and myelofibrosis—sometimes the first clue to an underlying MPN."
  - target: 01-human/03-molecular/calr
    relation: connects-to
    note: "CALR mutation is a major MPN driver alongside JAK2: in JAK2-negative essential thrombocythemia and myelofibrosis, calreticulin mutations activate the same thrombopoietin-receptor pathway, so CALR testing completes the molecular workup of myeloproliferative neoplasms."
  - target: 01-human/03-molecular/mpl
    relation: connects-to
    note: "MPL, the thrombopoietin receptor, is the third classic MPN driver: activating MPL mutations switch on JAK-STAT signaling in a minority of essential thrombocythemia and myelofibrosis, so JAK2, CALR and MPL together explain most myeloproliferative neoplasms."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Overproduction of red cells defines polycythemia vera within the MPN family: JAK2-driven erythroid expansion thickens the blood and raises clot risk, illustrating how each MPN over-makes one lineage—red cells here, platelets in ET, fibrosis in myelofibrosis."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Myeloproliferative neoplasms overproduce mature myeloid cells including neutrophils: the JAK2/CALR/MPL-driven clone expands granulocytes along with red cells and platelets, so leukocytosis is common and itself contributes to the thrombotic risk that defines MPN morbidity."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Thrombosis is the leading complication of myeloproliferative neoplasms: thick, sticky blood from excess cells and an activated, inflammatory clone causes arterial events including stroke, so cytoreduction and antiplatelet therapy aim to prevent these clots."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Myeloproliferative neoplasms classically cause splanchnic vein thrombosis: the prothrombotic clone clots the hepatic or portal veins (Budd-Chiari), so unexplained abdominal-vein thrombosis should prompt JAK2 testing—sometimes the first sign of an occult MPN."
  - target: 01-human/03-molecular/thrombopoietin
    relation: connects-to
    note: "MPNs hijack thrombopoietin signaling: CALR and MPL mutations make blood cells respond as if flooded with thrombopoietin even when levels are normal, driving the runaway platelet and megakaryocyte production of essential thrombocythemia and myelofibrosis."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Myelofibrosis is the scarring face of MPNs: clonal megakaryocytes pour out cytokines that drive fibroblasts to lay down marrow fibrosis, choking blood production and forcing the spleen and liver to take over—the hallmark of advanced disease."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Polycythemia vera ties MPNs to iron: overproduction of red cells consumes iron and therapeutic phlebotomy deliberately induces iron deficiency to limit red-cell mass, so iron balance is both a consequence and a lever of treatment."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Myeloproliferative neoplasms smolder with IL-6 and inflammation: the JAK2-mutant clone pumps out IL-6 and other cytokines that cause fevers, weight loss, and itching and drive progression to fibrosis—why JAK inhibitors relieve symptoms so well."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Immune surveillance by NK cells shapes myeloproliferative neoplasms: natural killer cells help police the mutant clone, and their exhaustion or dysfunction may let the disease expand—an angle for immune-based approaches alongside JAK inhibitors."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "MPN stem cells use autophagy to persist through treatment: the clonal cells recycle their contents to survive stress and JAK inhibition, so blocking autophagy is studied as a way to deepen responses and target the disease at its root."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "High blood counts in MPN can fake high potassium: the huge numbers of platelets and white cells leak potassium after the sample clots, producing pseudohyperkalemia—a lab artifact to recognize before treating a number that isn't real."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "MPNs threaten the brain with clots: thickened, sticky blood from too many cells raises the risk of stroke and cerebral vein thrombosis, so controlling counts and using aspirin aim to protect against these neurologic catastrophes."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Inflammation via NF-kB fuels the myeloproliferative clone: alongside JAK-STAT, the mutated stem cells drive NF-kB signaling that pours out cytokines, feeding the symptoms, marrow fibrosis and clonal expansion of these neoplasms."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "MPNs itch through the skin: aquagenic pruritus—intense itching minutes after a warm shower—is a classic symptom, especially of polycythemia vera, sometimes appearing before the diagnosis."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "MPN itching is driven by mast cells: the expanded clone's basophils and mast cells release histamine, which fires skin itch nerves to cause the aquagenic pruritus that torments these patients."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Polycythemia overrides the body's oxygen control: normally low oxygen raises erythropoietin to make red cells, but the JAK2 clone churns them out regardless, thickening the blood independent of oxygen need."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Radioactive phosphorus once tamed these clones with electrons: P-32 concentrates in marrow and emits beta particles — fast electrons — that suppress the overactive blood-cell factory, a historic polycythemia treatment now reserved for select older patients."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Myeloproliferative disease can choke the lungs: extramedullary hematopoiesis and microvascular thrombosis raise pulmonary pressures, so pulmonary hypertension and clots are recognized complications, especially in myelofibrosis."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "The kidney bears the brunt of high cell turnover: the massive production and breakdown of blood cells floods the blood with uric acid, which crystallizes in the tubules and can drive urate nephropathy and stones."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Myeloproliferative disease clots the arteries too: the thick, sticky blood and activated platelets drive arterial thrombosis, so heart attacks join the strokes and venous clots that menace these patients."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "MPN is a leading cause of unusual-site clots: thrombosis of the splanchnic veins draining the gut — portal, mesenteric, and the hepatic veins of Budd-Chiari — can be the first sign, sometimes before the blood counts even rise."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "The frenzied cell turnover spills phosphorus: the constant birth and death of blood cells, and their lysis under treatment, release phosphate and urate, the metabolic overflow that strains the kidneys and provokes gout."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Thrombosis is the central danger of MPN: the JAK2-mutant, thickened blood plus an activated, sticky endothelial-cell lining drives clots in both arteries and veins, the strokes and heart attacks that are the leading cause of death in these disorders."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "A maddening itch after a warm bath marks polycythemia vera: basophils and mast cells expanded by the MPN clone dump histamine, the aquagenic pruritus that water triggers being one of the disease's most distinctive complaints."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Sludgy blood blurs the vision: the hyperviscosity of a high red-cell or platelet count slows retinal flow, causing visual disturbances and engorged retinal veins, while erythromelalgia's burning can be matched by ocular symptoms in advanced disease."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "MPNs complicate pregnancy: the prothrombotic clone, especially JAK2-mutant, raises the risk of miscarriage, placental thrombosis and maternal clots, so affected women are managed with aspirin, low-molecular-weight heparin and pregnancy-safe interferon."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "The marrow can turn to bone: in the myelofibrosis subtype the fibrotic drive spills into osteosclerosis, where osteoblasts lay down excess bone that further crowds out blood production and shows as dense marrow on imaging."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "The overgrown marrow grows its own vessels: MPNs, especially myelofibrosis, raise VEGF and marrow microvessel density, an angiogenic drive that supports the expanding malignant clone and tracks with disease burden."
  - target: 01-human/03-molecular/tet2
    relation: connects-to
    note: "The driver mutation rarely acts alone: epigenetic hits like TET2 (with DNMT3A and ASXL1) often precede or accompany the JAK2 driver, shaping which MPN appears, how it evolves, and its risk of turning into acute leukemia."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "The mutant clone inflames the arteries: JAK2-mutated blood cells, a form of clonal hematopoiesis, accelerate atherosclerosis and arterial thrombosis, so MPNs raise heart-attack and stroke risk beyond what their high cell counts alone would predict."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Clonal macrophages help scar the marrow: monocytes and macrophages derived from the malignant clone pour out TGF-β and other fibrogenic signals that drive the reticulin and collagen fibrosis of myelofibrosis, remodeling the marrow they grow in."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "Epigenetic mutations layer onto the driver: DNMT3A, TET2 and other clonal-hematopoiesis mutations co-occur with JAK2/CALR/MPL in MPNs, shaping clonal evolution and the risk of progression to myelofibrosis or leukemia."
  - target: 01-human/07-system/mds
    relation: connects-to
    note: "The clone can drift toward dysplasia: MPNs sit on the myeloid spectrum and can evolve into MDS/MPN-overlap or acquire dysplastic, MDS-like features, especially as they accumulate secondary mutations."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Fibroblasts lay down the marrow scar: responding to clone-derived TGF-β and PDGF, marrow stromal fibroblasts deposit the reticulin and collagen that obliterate the marrow space in myelofibrosis."
  - target: 01-human/07-system/hcc
    relation: connects-to
    note: "They clot the liver's own veins: MPNs are the leading cause of Budd-Chiari syndrome and portal vein thrombosis, congesting the liver toward cirrhosis and, over years, hepatocellular carcinoma — often the first clue to an occult MPN."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "The lung circulation stiffens: MPNs raise pulmonary artery pressure through chronic thromboembolism, extramedullary hematopoiesis and high-output flow, a recognized and under-appreciated complication."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Advanced disease strips the defenses: progression to myelofibrosis or blast phase, and the cytoreductive and JAK-inhibitor therapy used, cause cytopenias and immune compromise that make infection and sepsis a danger."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Marrow fibrosis and inflammation lower the count: as MPNs evolve toward a spent, myelofibrotic phase, marrow scarring and chronic inflammation replace the cellular excess with an anemia of chronic disease."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "JAK inhibitors open the lung to mold: ruxolitinib used for myelofibrosis and polycythemia vera suppresses immunity and, with disease-related neutropenia, raises the risk of invasive aspergillosis and other opportunistic infections."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A chronic clonal disease wears on mood: the heavy constitutional symptom burden — fatigue, itch, night sweats — and the lifelong thrombosis-and-transformation risk of MPNs contribute to depression and reduced quality of life."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "JAK inhibition reawakens shingles: ruxolitinib used for myelofibrosis and polycythemia vera dampens T-cell immunity and characteristically reactivates latent varicella-zoster, a recognised risk during therapy."
  - target: 01-human/07-system/iron-deficiency-anemia
    relation: connects-to
    note: "Treating polycythemia drains the iron stores: the repeated therapeutic phlebotomy used to control the red-cell mass in polycythemia vera deliberately induces iron deficiency to limit erythropoiesis."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Lifelong clot-and-transformation risk breeds worry: the constant threat of thrombosis and progression to acute leukaemia in MPNs, plus relentless symptoms, fosters chronic health anxiety alongside low mood."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "They clot the gut's veins and swell the spleen: MPNs are a leading cause of splanchnic, portal and hepatic vein thrombosis (Budd-Chiari), and massive splenomegaly from extramedullary haematopoiesis causes early satiety."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Excess blood cells torment the skin: polycythemia vera causes the intense aquagenic pruritus after bathing, and essential thrombocythemia produces the burning red erythromelalgia of the extremities."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Sludgy, clot-prone blood strains the circulation: the raised cell mass and platelet activation of MPNs cause arterial thrombosis with myocardial infarction, hypertension and a high-output cardiovascular burden."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "They swell the spleen: extramedullary haematopoiesis and pooling of blood cells enlarge the spleen, often massively in myelofibrosis, with a risk of splenic infarction and early satiety."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Thick blood disturbs the brain: hyperviscosity and microvascular thrombosis in MPNs cause headache, visual disturbance, transient ischaemic attacks and stroke."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "They burden bone and joints: marrow expansion and the osteosclerosis of myelofibrosis cause bone pain, while high cell turnover raises uric acid and precipitates gout."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Clots and blood-making reach the lungs: MPNs cause pulmonary embolism and pulmonary hypertension, and extramedullary haematopoiesis can rarely involve the lungs."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "High cell turnover taxes the kidney: hyperuricaemia causes urate nephropathy, an MPN-associated glomerulopathy occurs, and renal vein thrombosis can complicate the prothrombotic state."
  - target: 03-medicine/01-modern/04-cardio/aspirin
    relation: connects-to
    note: "Low-dose aspirin counters the clotting: by inhibiting the overactive platelets of myeloproliferative neoplasms, aspirin reduces thrombosis and microvascular symptoms, alongside cytoreduction."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "JAK inhibition is the targeted backbone: ruxolitinib and fedratinib block the JAK2-STAT pathway driving myeloproliferative neoplasms, shrinking the spleen and easing symptoms in myelofibrosis and polycythaemia vera."
  - target: 02-pathogen/02-bacteria/mycobacterium-tuberculosis
    relation: connects-to
    note: "JAK inhibitors reawaken latent infection: ruxolitinib suppresses immunity enough to reactivate tuberculosis and other opportunists, requiring screening before treatment."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Hydroxyurea cytoreduces: the oral chemotherapy hydroxyurea lowers excess blood counts in high-risk myeloproliferative neoplasms, a long-standing cytoreductive mainstay."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "It clots the liver and seeds it with blood-making: myeloproliferative neoplasms are a leading cause of Budd-Chiari and portal vein thrombosis, and their excess progenitors lodge in the hepatic lobules as extramedullary haematopoiesis, enlarging the liver."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "Thrombosis is its chief killer: JAK2-mutant blood cells inflame and adhere to the arterial wall, promoting endothelial dysfunction and the arterial thrombosis—heart attack and stroke—that drives mortality in polycythaemia vera and essential thrombocythaemia."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "It also wears down the kidney: myeloproliferative neoplasms impair renal function through hyperuricaemia, microvascular thrombosis and an MPN-associated glomerulopathy, so chronic kidney disease accumulates as the clone persists."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Arterial thrombosis and the heart: MPN hyperviscosity and reactive platelets cause arterial thrombi including myocardial infarction, a leading cause of death in polycythaemia vera and essential thrombocythaemia."
  - target: 01-human/07-system/antiphospholipid-syndrome
    relation: connects-to
    note: "Two causes of unexplained thrombosis: MPN and antiphospholipid syndrome both cause arterial and unusual-site venous thrombosis (splanchnic, cerebral), key differentials in a young patient with a clot."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Osteosclerosis of myelofibrosis: as the marrow fibroses, reactive new bone formation thickens and scleroses the cortical bone, the radiographic counterpart of the fibrotic marrow."
  - target: 01-human/03-molecular/von-willebrand-factor
    relation: connects-to
    note: "Bleeding amid thrombosis: extreme thrombocytosis in essential thrombocythaemia adsorbs and clears high-molecular-weight von Willebrand multimers, causing an acquired von Willebrand syndrome that bleeds paradoxically in a prothrombotic disease."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "MPN nephropathy: chronic myeloproliferative neoplasms cause a distinctive glomerulopathy with mesangial sclerosis and proteinuria, megakaryocytes and platelet-derived factors injuring the glomerulus over time."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Stacked thrombotic risk: the JAK2-driven hypercoagulable state of myeloproliferative neoplasms compounds the thrombo-inflammation of COVID-19, raising the risk of arterial and venous clots during infection."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Clone-reducing therapy: pegylated interferon-alpha is a disease-modifying treatment for myeloproliferative neoplasms that can shrink the JAK2/CALR-mutant clone and induce molecular responses."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Epigenetic progression: EZH2 and other epigenetic-regulator mutations accumulate in myeloproliferative neoplasms and drive progression toward myelofibrosis and acute leukaemia."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Inflammatory niche: IL-1β secreted by the mutant clone damages the bone-marrow stroma, promoting the fibrosis and clonal advantage that mark myeloproliferative neoplasm progression."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Clonal advantage: TNF-α from the JAK2-mutant clone is preferentially tolerated by the mutant cells while suppressing normal haematopoiesis, helping the neoplastic clone dominate the marrow."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Inflammasome activation: JAK2-driven NLRP3-inflammasome activation amplifies the chronic inflammation of myeloproliferative neoplasms, contributing to their symptoms and thrombotic risk."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Marrow hypoxia: HIF-1α stabilised in the hypercellular, hypoxic MPN marrow supports the survival and angiogenic signalling of the expanded clone."
  - target: 01-human/03-molecular/pf4
    relation: connects-to
    note: "Thrombotic risk: PF4 released from the expanded, activated platelet mass of myeloproliferative neoplasms marks the platelet hyperreactivity behind their characteristic arterial and venous thrombosis."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "Myeloid alarmin: S100A8/A9 from the expanded myeloid compartment amplifies the chronic inflammation of myeloproliferative neoplasms, driving constitutional symptoms and disease progression."
  - target: 01-human/03-molecular/runx1
    relation: connects-to
    note: "Leukaemic transformation: acquired RUNX1 mutations mark the progression of myeloproliferative neoplasms toward acute myeloid leukaemia, a feared terminal evolution."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Marrow fibrosis: PDGF released by the clonal megakaryocytes of myeloproliferative neoplasms stimulates marrow fibroblasts, driving the reticulin and collagen fibrosis of primary and secondary myelofibrosis."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Thromboxane and aspirin: the hyperreactive platelets of myeloproliferative neoplasms generate thromboxane A2, the target of the low-dose aspirin used to reduce the thrombosis that is their leading cause of morbidity."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "High cell turnover: the massive haematopoietic turnover of myeloproliferative neoplasms floods purine catabolism through xanthine oxidase, raising urate and causing the secondary hyperuricaemia and gout that complicate them."
  - target: 01-human/03-molecular/sf3b1
    relation: connects-to
    note: "Progression comutations: spliceosome mutations such as SF3B1, acquired alongside the JAK2/CALR/MPL driver, mark the myeloproliferative neoplasms more likely to progress to myelofibrosis or acute leukaemia, refining prognosis beyond the driver alone."
  - target: 01-human/03-molecular/thrombin
    relation: connects-to
    note: "Thrombotic state: the raised cell counts and activated platelets and leukocytes of myeloproliferative neoplasms promote thrombin generation and hyperviscosity, making arterial and venous thrombosis — including unusual splanchnic-vein clots — their leading cause of morbidity."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "Stem-cell maintenance: FOXO transcription factors are paradoxically active in JAK2-mutant myeloproliferative neoplasms, maintaining the malignant haematopoietic stem cells that sustain the clone and resist JAK-inhibitor therapy."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "MAPK limb: JAK2, CALR and MPL (all already mapped) activate the RAS-MAPK-ERK cascade alongside JAK-STAT, a parallel proliferative driver in myeloproliferative neoplasms."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K limb: the same constitutively active receptor-kinase signalling engages PI3K-AKT as a third effector pathway supporting myeloid proliferation and survival in MPN."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "Leukaemic transformation: TP53 inactivation drives the progression of myeloproliferative neoplasms, particularly myelofibrosis, to acute myeloid leukaemia."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Downstream proliferation: the PI3K-AKT axis (PIK3CA already mapped) operates downstream of constitutive JAK2 signalling to drive the proliferation and survival of myeloproliferative-neoplasm clones."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Inflammatory milieu: TLR-MyD88-NF-κB innate signalling (NF-κB already mapped) sustains the chronic inflammatory milieu that characterises and propels myeloproliferative neoplasms."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "Transformation lesion: CDKN2A loss is among the cooperating lesions in the leukaemic transformation of myeloproliferative neoplasms to acute myeloid leukaemia."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "JAK2-driven PI3K-AKT-mTOR signalling (JAK2 and AKT mapped) supports clonal proliferation in myeloproliferative neoplasms, a target of mTOR-inhibitor combinations."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "Type-I-interferon signalling through STAT1 (type-I-interferon mapped) underlies the disease-modifying activity of interferon therapy across the myeloproliferative neoplasms."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 expressed by megakaryocytes contributes to the marrow microenvironment and the fibrotic progression of myeloproliferative neoplasms."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING amplifies the chronic inflammatory marrow milieu (type-I interferon already mapped) of myeloproliferative neoplasms."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β already mapped) released by clonal megakaryocytes drives the bone-marrow fibrosis of myeloproliferative neoplasms."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6-cyclin-D activity (CDKN2A already mapped) drives the JAK2-fuelled myeloproliferative cell-cycle progression of myeloproliferative neoplasms."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β misregulation contributes to the aberrant hematopoietic stem-cell self-renewal of myeloproliferative neoplasms."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis and contributes to the leukemic evolution of myeloproliferative neoplasms."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated cytotoxic immunosurveillance targets the neoantigen-bearing CALR-mutant clone of myeloproliferative neoplasms."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family and LYN kinase signaling cooperates with JAK2-STAT to support the survival of the clonal myeloid cells of myeloproliferative neoplasms."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of the clonal hematopoietic stem cells of myeloproliferative neoplasms."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A and the broader chromatin machinery contribute to the epigenetic dysregulation of myeloproliferative neoplasms."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-family chemokine signaling participates in the aberrant myeloid trafficking and inflammatory bone-marrow niche of myeloproliferative neoplasms."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling in the bone-marrow niche participates in the clonal hematopoiesis and megakaryocyte-driven fibrosis of myeloproliferative neoplasms."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "NOTCH signaling participates in the megakaryocyte and stromal biology contributing to the myelofibrosis of myeloproliferative neoplasms."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the inflammatory bone-marrow microenvironment of myeloproliferative neoplasms."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory bone-marrow microenvironment of myeloproliferative neoplasms."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory and thrombotic microenvironment of myeloproliferative neoplasms."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the megakaryocyte and clonal-myeloproliferation signaling of myeloproliferative neoplasms."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine signaling participates in the immunosuppressive bone-marrow microenvironment of myeloproliferative neoplasms."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin participates in the bone-marrow-fibrosis and stromal interactions of myeloproliferative neoplasms."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Erythrocytosis: in polycythaemia vera the JAK2-driven erythroid overproduction (erythropoietin already mapped) raises haemoglobin and haematocrit, thickening the blood and driving the thrombosis managed with phlebotomy and cytoreduction."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Arterial thrombosis: myeloproliferative neoplasms markedly raise the risk of arterial events including myocardial infarction and stroke, and troponin elevation marks the cardiac injury of these thrombotic complications that dominate their morbidity."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Endothelial-platelet imbalance: impaired endothelial nitric-oxide function, with the excess activated blood cells of myeloproliferative neoplasms, tips the vascular balance toward the thrombosis (vWF already mapped) that is a leading cause of death."
  - target: 01-human/03-molecular/adamts13
    relation: connects-to
    note: "Acquired von Willebrand syndrome: extreme thrombocytosis clears the high-molecular-weight von Willebrand multimers (already mapped), causing the acquired von Willebrand syndrome and the paradoxical bleeding that coexists with thrombosis in these neoplasms."
  - target: 01-human/03-molecular/protein-c
    relation: connects-to
    note: "Prothrombotic tilt: the thrombosis of myeloproliferative neoplasms reflects a shift toward coagulation, and reduced activity of the natural anticoagulant protein C (thrombin already mapped) further raises the risk that drives cytoreduction and antithrombotic therapy."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Inflammatory milieu: myeloproliferative neoplasms carry a chronic inflammatory state, and the anti-inflammatory IL-10 counterbalances the TNF, IL-6 and IL-1 (already mapped) driven by JAK-STAT signalling that shapes their phenotype and symptoms."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Microvascular vasoconstriction: endothelin-1 and the platelet-derived vasoactive mediators contribute to the microvascular vasoconstriction behind the erythromelalgia and neurological symptoms of the myeloproliferative neoplasms."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Platelet serotonin: serotonin released from the abnormal, activated platelets (PF4 already mapped) causes vasoconstriction and amplifies aggregation, contributing to the microvascular symptoms and thrombosis of the myeloproliferative neoplasms."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Endothelial activation: the angiopoietin-Tie2 axis reflects the endothelial activation of the prothrombotic state of the myeloproliferative neoplasms, part of the endothelium's contribution (von Willebrand factor already mapped) to their thrombosis."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Iron restriction and anaemia: the hepcidin-mimetic rusfertide restricts iron (already mapped) to control the erythrocytosis of polycythaemia vera, while the raised hepcidin of chronic inflammation (IL-6 already mapped) contributes to the anaemia of myelofibrosis."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Inflammatory milieu: IL-4 and the M2 macrophage arm (IL-10 already mapped) shape the chronic inflammation (IL-6 and TNF already mapped) of the myeloproliferative marrow, part of the disease biology of the myeloproliferative neoplasms."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Marrow adipose crosstalk: the marrow adipocytes and their adipokine leptin signal to the clonal myeloid cells, part of the bone-marrow (already mapped) microenvironment of the myeloproliferative neoplasms."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "M2 inflammatory arm: IL-13, with IL-4 (already mapped), drives the M2 macrophage arm of the chronic inflammation (IL-6 and TNF already mapped) of the myeloproliferative marrow."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Marrow-adipocyte adipokine: adiponectin, with leptin (already mapped), from the marrow adipose tissue signals to the clonal myeloid cells of the bone-marrow (already mapped) microenvironment of the myeloproliferative neoplasms."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the inflammatory milieu of the myeloproliferative neoplasms."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Clonal immunosurveillance: the cytotoxic T cells (perforin already mapped) provide the immune surveillance of the JAK2 (already mapped)-mutant clone, augmented by the interferon (type-I interferon already mapped) therapy of the myeloproliferative neoplasms."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 arm: the IFN-γ of the T cells (with the type-I interferon already mapped) is the type-II interferon arm of the anti-clonal immunity and the inflammatory milieu of the myeloproliferative neoplasms."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) response of the anti-clonal immunity of the myeloproliferative neoplasms."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the inflammatory milieu of the myeloproliferative neoplasms (and the driver of the eosinophilic MPN variants)."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the chronic inflammatory milieu of the myeloproliferative neoplasms."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the inflammatory milieu of the myeloproliferative neoplasms."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Antigen presentation: the dendritic cells present antigen to the T cells (already mapped) within the inflammatory clonal-haematopoiesis microenvironment of the myeloproliferative neoplasms."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the chronic inflammatory milieu that drives the constitutional symptoms of the myeloproliferative neoplasms."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Thromboinflammation: the complement C5 and its C5a (with C3 already mapped) contribute to the complement-driven thromboinflammation and the thrombotic risk of the myeloproliferative neoplasms."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) links the complement to the myeloid inflammation and the immunothrombosis of the myeloproliferative neoplasms."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) whose dysregulation amplifies the thromboinflammation of the myeloproliferative neoplasms."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "MPN iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the iron deficiency of polycythaemia vera and the anaemia of myelofibrosis."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Bone-marrow stroma alarmin: TSLP from the inflamed JAK2-mutant (already mapped) myeloproliferative bone marrow activates the stromal dendritic cells and mast cells, amplifying the NF-kB (already mapped) and STAT3 (already mapped) pro-inflammatory microenvironment of MPN."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Thrombosis amplifier: bradykinin activates B2 receptors on the platelets (already mapped) and vascular endothelium (already mapped), amplifying the hypercoagulability and microvascular thrombotic complications (VTE already mapped) of the JAK2-mutant myeloproliferative neoplasms."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Myelofibrosis stroma: periostin, downstream of TGF-β (already mapped) and megakaryocyte-derived growth factors, drives the collagen deposition and fibroblast activation of the bone marrow (already mapped) fibrosis that characterises the myeloproliferative neoplasms."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "MPN complement regulation: C1-INH controls the classical-pathway arm (C3, C5 and C5aR1 already mapped) in the MPN microenvironment, complementing factor H (already mapped) to limit complement-driven thrombosis and JAK2 (already mapped) neutrophil activation."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Oncostatic melatonin in MPN: melatonin inhibits the JAK2 (already mapped)/STAT3 (already mapped) signalling cascade in myeloproliferative neoplasm progenitor cells, attenuates mast-cell (already mapped) histamine release and reduces the thrombo-inflammatory burden of MPN."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Prolactin-JAK2 axis: prolactin, via PRLR-mediated JAK2 (already mapped)/STAT5 activation, amplifies the constitutive JAK2V617F signalling of polycythaemia-vera and essential thrombocythaemia; elevated prolactin levels correlate with the inflammatory cytokine burden of MPN."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Androgen-erythrocyte axis: testosterone, via androgen receptor on JAK2-V617F-mutant (already mapped) erythroid progenitor cells (already mapped), potentiates the erythrocytosis and myeloid proliferative drive of the polycythemia vera spectrum of myeloproliferative neoplasms."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Haematopoietic neuropeptide: oxytocin, via OXT-R on bone-marrow stromal cells (already mapped) and megakaryocytes (already mapped), modulates haematopoietic niche signalling and the thrombopoiesis dysregulated in essential thrombocythemia of myeloproliferative neoplasms."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "Platelet-vasopressin axis: vasopressin, via V1a receptors on platelets (already mapped) and endothelial cells (already mapped), amplifies the thrombotic risk and platelet activation of the essential-thrombocythemia and polycythemia-vera spectrum of myeloproliferative neoplasms."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "MPN selenium antioxidant: selenium, via GPx/TrxR selenoproteins in JAK2-V617F-mutant (already mapped) cells and macrophages (already mapped), quenches oxidative stress that amplifies NF-κB (already mapped) and IL-6 (already mapped) signalling in myeloproliferative neoplasms."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "MPN iodine thyroid: iodine, as the key substrate for thyroid hormone biosynthesis, supports bone-marrow (already mapped) haematopoiesis; iodine insufficiency amplifies the IL-6 (already mapped) and NF-κB (already mapped) myeloid drive of myeloproliferative neoplasms."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "MPN sodium inflammatory: sodium, at supraphysiological concentrations in the myeloid marrow, activates macrophage (already mapped) NF-κB (already mapped) and IL-6 (already mapped) signalling, promoting the pro-inflammatory myeloid shift in myeloproliferative neoplasms."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "MPN magnesium: magnesium, as cofactor of JAK2 regulatory enzymes in macrophages (already mapped) and erythrocytes (already mapped), supports haematopoiesis; magnesium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) myeloproliferative cascade."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "MPN copper: copper, as cofactor of SOD1 in macrophages (already mapped) and neutrophils (already mapped), neutralises ROS; copper deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) myeloproliferative oxidative cascade."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "MPN zinc: zinc, as cofactor of antioxidant enzymes in macrophages (already mapped) and platelets (already mapped), attenuates oxidative stress; zinc deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) haematopoietic myeloproliferative cascade."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "MPN calcium: calcium, as second messenger in macrophages (already mapped) and mast cells (already mapped), regulates myeloid cell activation; calcium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) haematopoietic cascade of myeloproliferative neoplasms."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "MPN chloride: chloride channels regulate macrophage (already mapped) and neutrophil (already mapped) ion homeostasis in the myeloproliferative bone marrow; chloride imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "MPN sulfur: sulfur-containing amino acids in macrophages (already mapped) and mast cells (already mapped) maintain redox buffering; sulfur depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) myeloproliferative oxidative cascade."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "MPN carbon: carbon as backbone of JAK2 (already mapped) and calreticulin structural proteins in megakaryocytes (already mapped) sustains clonal myeloid expansion; carbon depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) myeloproliferative cascade."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "MPN hydrogen: hydrogen, via redox homeostasis in macrophages (already mapped) and neutrophils (already mapped), supports JAK2 (already mapped) signalling in myeloproliferative bone marrow; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "MPN nitrogen: nitrogen in amino-acid scaffold of JAK2 (already mapped) and CALR proteins in megakaryocytes (already mapped) sustains clonal haematopoiesis; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) myeloproliferative cascade."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "MPN PD-1: PD-1 checkpoint on T-cytotoxic cells (already mapped) and NK cells (already mapped) in clonal bone marrow modulates immune escape; PD-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) myeloproliferative cascade."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "MPN GLP-1: GLP-1 receptor agonism on megakaryocytes (already mapped) and macrophages (already mapped) modulates clonal marrow inflammation; GLP-1 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) myeloproliferative cascade."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "MPN angiotensin-II: angiotensin-II via AT1R on bone-marrow stromal cells (already mapped) and macrophages (already mapped) drives fibrotic remodelling; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) myeloproliferative cascade."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "MPN wnt-beta-catenin: WNT/β-catenin on macrophages (already mapped) and fibroblasts (already mapped) regulates clonal marrow expansion; wnt-beta-catenin dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and smad4 (already mapped) cascade of MPN."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "MPN rankl: RANKL from macrophages (already mapped) and osteoblasts (already mapped) promotes clonal myeloid immune evasion; rankl excess amplifies nf-kb (already mapped) and il-6 (already mapped) and smad4 (already mapped) myeloproliferative cascade."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "MPN il-2: IL-2 from t-cytotoxic cells (already mapped) and macrophages (already mapped) regulates clonal myeloid immune tone; il-2 dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and smad4 (already mapped) myeloproliferative cascade."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "MPN fibronectin: fibronectin in macrophages (already mapped) and fibroblasts (already mapped) promotes clonal marrow ECM remodelling; fibronectin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and smad4 (already mapped) myeloproliferative cascade."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "MPN igf-1: IGF-1 from macrophages (already mapped) and fibroblasts (already mapped) promotes clonal myeloid cell survival; igf-1 dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and smad4 (already mapped) myeloproliferative cascade."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "MPN activin-a: activin-A from macrophages (already mapped) and fibroblasts (already mapped) drives clonal marrow fibrosis; activin-a excess amplifies nf-kb (already mapped) and il-6 (already mapped) and smad4 (already mapped) myeloproliferative cascade."
---

# Myeloproliferative Neoplasms

## Overview

**Myeloproliferative neoplasms (MPN)** are a group of clonal hematopoietic stem cell disorders characterized by excessive production of mature blood cells — erythrocytes (polycythemia vera, PV), platelets (essential thrombocythemia, ET), or fibrotic marrow remodeling with panmyeloid dysregulation (myelofibrosis, MF) — without significant dysplasia (distinguishing MPN from MDS). The unifying molecular basis of "Philadelphia-negative MPN" (classical MPN — PV, ET, MF) is constitutive JAK-STAT pathway activation, most commonly via the **JAK2 V617F** somatic mutation (~95% of PV, ~55% of ET, ~60% of MF) or, in JAK2 V617F-negative cases, calreticulin (CALR) frameshift mutations (~25% of ET/MF) or MPL (thrombopoietin receptor) mutations (~5%). Ruxolitinib, a JAK1/2 inhibitor, is the primary targeted therapy for MF and refractory PV; allogeneic stem cell transplantation remains the only curative option for high-risk MF [^verstovsek-2012-comfort-i].

**Epidemiology:**
- PV: ~3 per 100,000/year; median age ~60; M:F ~1.2:1; JAK2 V617F ~95-97%
- ET: ~1-2.5 per 100,000/year; bimodal distribution (young women, older patients); JAK2 V617F ~55%
- Primary MF: ~0.5-1.5 per 100,000/year; most common older patients; median age ~67; worst prognosis of classical MPN
- MPN transformation: PV → post-PV MF (~15-20% at 15 years); ET → post-ET MF (~5-10% at 10 years); blast-phase (AML transformation) ~5-10% for MF, ~2-3% for PV/ET
- Post-PV MF and post-ET MF are treated like primary MF

**Classification (WHO 2022):**
- Polycythemia vera (PV): Absolute erythrocytosis + JAK2 mutation (minor criterion: BM hypercellularity + low EPO)
- Essential thrombocythemia (ET): Platelets >450 × 10⁹/L + MPN driver mutation (JAK2/CALR/MPL) + BM megakaryocytic hyperplasia + no other MPN
- Primary myelofibrosis (PMF): Megakaryocytic atypia + BM fibrosis (MF grade 1-3) + MPN driver mutation + exclusion of ET/PV/CML
- Prefibrotic MF (pre-PMF): Early stage before significant fibrosis; megakaryocytic atypia without significant fibrosis; distinguishable from ET by BM findings

## Structure

### Molecular drivers of MPN

**JAK2 V617F (Val617→Phe in exon 14):**
Located in the pseudokinase domain (JH2) of JAK2 → abolishes JH2 autoinhibitory constraint on JH1 (active kinase domain) → constitutive JAK2 activity → autonomous STAT5/STAT3/PI3K/ERK activation independent of EPO/TPO/G-CSF binding. Allele burden correlates with MPN phenotype: heterozygous V617F (lower burden) → ET; homozygous V617F (uniparental disomy 9p, higher burden) → PV.

**JAK2 exon 12 mutations:**
Insertion/deletion mutations in exon 12 (in-frame); found in ~3% of PV (JAK2 V617F-negative); cause EPO-independent erythrocytosis specifically (less thrombocytosis/leukocytosis than V617F); STAT5 activation primarily erythroid-biased.

**CALR mutations (exon 9 frameshift):**
- Type I CALR: 52-bp deletion → generates novel C-terminus; activates MPL → TPO-independent megakaryopoiesis; ET and MF
- Type II CALR: 5-bp insertion; less potent MPL activation; predominantly ET
- CALR-mutant CALR protein binds and activates MPL via novel C-terminus; activates JAK2 downstream → STAT5; CALR-mutant ET: lower thrombosis risk than JAK2 V617F ET; CALR type I more associated with MF transformation

**MPL W515L/K (exon 10 mutations):**
Activating mutations in the thrombopoietin receptor (MPL); ~5% of JAK2/CALR-negative ET/MF; constitutive MPL → JAK2 → STAT5 activation; megakaryocyte-dominant phenotype.

**Co-mutations (MF prognosis):**
- ASXL1 mutations: ~25-35% of MF; poor prognosis; chromatin remodeling
- EZH2 mutations: ~5-10%; worst prognosis group with ASXL1 and IDH1/2
- IDH1/2: ~5%; associated with blast transformation
- SRSF2: Splicing factor; ~10%; poor prognosis
- TP53: ~5-10% of blast-phase MF; leukemic transformation
- U2AF1: Splicing factor; ~15%; clinical trials targeting splicing

**MIPSS70+ v2.0 (Mutation-enhanced International Prognostic Scoring System for MF):**
Integrates JAK2/CALR/MPL mutation status, co-mutations (ASXL1, EZH2, IDH1/2, SRSF2, U2AF1), karyotype, hemoglobin, platelets, leukocytes, symptoms, and age → stratifies MF into very low/low/intermediate/high/very high risk; informs alloSCT timing.

### MPN disease biology

**PV pathophysiology:**
JAK2 V617F → constitutive EPOR-JAK2-STAT5 signaling → erythroid progenitor expansion → absolute erythrocytosis (elevated Hgb/HCT) → increased blood viscosity → venous and arterial thrombosis (Budd-Chiari syndrome, CVA, MI, DVT/PE are leading causes of morbidity). EPO levels suppressed (EPO-independent erythropoiesis). Aquagenic pruritus (JAK2 → mast cell degranulation after water contact) characteristic.

**ET pathophysiology:**
Platelet hyperproduction → thrombocytosis (>450 × 10⁹/L) → paradoxical thrombosis (smaller platelets, acquired vWF deficiency at very high platelet counts >1500 × 10⁹/L → bleeding) and clot formation; large platelets; megakaryocytic hyperplasia in BM with stag-horn megakaryocytes.

**MF pathophysiology:**
Abnormal megakaryocytes → TGF-β1/PDGF secretion → fibroblast activation → collagen deposition → BM fibrosis → hematopoietic failure → extramedullary hematopoiesis in spleen/liver → massive splenomegaly → early satiety, weight loss, cachexia; cytopenia (anemia, thrombocytopenia); constitutional symptoms (night sweats, fatigue, pruritus).

## Function

### Normal megakaryocyte-platelet biology

**Thrombopoiesis:**
TPO (hepatic) → MPL on megakaryocyte precursors → JAK2 → STAT5 → megakaryocyte differentiation and endomitosis (polyploidization up to 128N) → proplatelet formation → platelet release into blood (~150,000-400,000 platelets/μL). Platelets are anucleate cytoplasmic fragments; lifespan ~7-10 days.

**Megakaryocyte niche:**
Megakaryocytes reside in the BM sinusoidal niche; proplatelet extensions penetrate sinusoidal endothelium → platelets released into blood. In MF, abnormal megakaryocytes secrete TGF-β1, PDGF → fibroblast activation → progressive marrow fibrosis.

### Leukocytosis and thrombotic risk

In PV and ET, JAK2 V617F also affects myeloid progenitors → granulocytosis and monocytosis. Leukocytosis (WBC >11 × 10⁹/L) is an independent thrombosis risk factor in PV, independent of HCT. JAK2 V617F-positive leukocytes have enhanced PI3K/AKT/NF-κB activity → pro-inflammatory/pro-thrombotic microenvironment.

## Pathology

### Diagnostic criteria and workup

**PV (WHO 2022 major/minor):**
- Major: (1) Hemoglobin >16.5 g/dL (M) / >16 g/dL (F) or HCT >49%/48%; (2) BM hypercellularity (panmyelosis) with megakaryocytic proliferation; (3) JAK2 V617F or JAK2 exon 12 mutation
- Minor: EPO below normal reference range
- PV diagnosis: All 3 major or 2 major + minor

**ET (WHO 2022 major):**
1. Platelet count >450 × 10⁹/L
2. BM: Megakaryocytic proliferation, mature large megakaryocytes with hyperlobated nuclei; no significant granulocyte or erythroid proliferation; no/minimal reticulin fibrosis
3. Criteria for PV, PMF, BCR-ABL1+ CML, MDS not met
4. Presence of JAK2 V617F, CALR exon 9, or MPL exon 10 mutation OR another clonal marker (or no reactive thrombocytosis)

**MF grading (WHO fibrosis grade):**
- MF-0: No reticulin fibrosis
- MF-1: Loose reticulin network; no collagen
- MF-2: Diffuse dense reticulin + collagen (confirmed by trichrome stain); no osteosclerosis
- MF-3: Dense reticulin + coarse collagen ± osteosclerosis

**Staging workup:**
- CBC with differential, reticulocyte count, LDH, uric acid, ferritin, EPO level
- Peripheral blood smear: Teardrop cells (dacrocytes) in MF; giant platelets in ET; immature myeloids (leukoerythroblastic pattern) in MF
- Bone marrow biopsy + aspirate: Morphology, reticulin/trichrome staining for fibrosis grade; cytogenetics
- Molecular: JAK2 V617F (allele-specific PCR or NGS); if negative → CALR exon 9, MPL exon 10; next-generation sequencing panel (ASXL1, IDH1/2, EZH2, SRSF2, TP53) for MF risk stratification
- Abdominal imaging (ultrasound/CT): Spleen and liver size; extramedullary hematopoiesis

### Treatment

**PV management:**
- **All patients:** Phlebotomy (target HCT <45%; CYTO-PV: HCT <45% vs. 45-50% → 4× lower cardiovascular events); low-dose aspirin (100 mg/day) for thrombosis prophylaxis
- **Low-risk (age <60, no thrombosis history):** Phlebotomy + aspirin; observe
- **High-risk (age ≥60 or prior thrombosis):** Cytoreduction with hydroxyurea (HU) first-line; interferon-α (pegylated: ropeginterferon alfa-2b — Besremi; disease-modifying, can induce molecular remission)
- **HU-resistant/intolerant:** Ruxolitinib (RESPONSE trial) [^vannucchi-2015-response]: HCT control + spleen reduction vs. standard; FDA approved 2014; ropeginterferon alfa-2b as alternative

**ET management:**
- **Risk stratification (IPSET-thrombosis revised):**
  - Low risk: Age <60, no thrombosis history, JAK2 V617F positive
  - Very low risk: Age <60, no thrombosis, JAK2 V617F negative
  - Intermediate risk: Age ≥60, no thrombosis history, JAK2 V617F negative
  - High risk: Age ≥60 or prior thrombosis (any JAK2 status)
- **Very low/low risk:** Observation or low-dose aspirin
- **Intermediate risk:** May observe or add aspirin; cytoreduction if symptomatic
- **High risk:** Cytoreduction with hydroxyurea first-line; anagrelide (platelet-selective) as alternative; interferon-α for young/fertile patients; ruxolitinib for HU-resistant/intolerant

**Myelofibrosis management:**

**Symptom-directed therapy:**
- **Ruxolitinib (COMFORT-I, COMFORT-II):** [^verstovsek-2012-comfort-i] Spleen volume reduction ≥35% at 24 weeks in ~41% vs. 0% placebo; OS benefit at 3 years; FDA approved 2011; starting dose based on platelet count (200 × 10⁹/L: 20 mg BID; 100-200 × 10⁹/L: 15 mg BID; 50-100 × 10⁹/L: 5 mg BID)
- **Fedratinib (JAKARTA trial):** FDA approved 2019; option for ruxolitinib-refractory/intolerant MF; caution for thiamine deficiency
- **Pacritinib (PERSIST-2, PAC203):** FDA approved 2022 for MF with platelets <50 × 10⁹/L; spares JAK1 → less cytopenia; option for severely thrombocytopenic MF
- **Momelotinib (MOMENTUM trial):** FDA approved 2023; superior transfusion independence vs. danazol; ACVR1 inhibition → reduced hepcidin → improves anemia

**Anemia-directed therapy:**
- Luspatercept (INDEPENDENCE trial): Activin receptor ligand trap → reduces SMAD2/3 signaling → improves erythroid maturation; approved for MF-associated anemia on ruxolitinib
- Danazol: Androgen; modest benefit for anemia in MF
- Erythropoiesis-stimulating agents (ESA): Limited utility in MF (EPO often elevated)
- Transfusion support for severe anemia

**Curative therapy (alloSCT):**
- Only curative approach for MF; indicated for intermediate-2 or high-risk disease (DIPSS-plus ≥4) in eligible patients
- Reduced-intensity conditioning (RIC) allows older patients to proceed; 5-year OS ~50% in DIPSS-plus intermediate-2/high risk
- Ruxolitinib pre-transplant → reduce spleen size → better engraftment; ruxolitinib tapering post-transplant under investigation

**Blast-phase MPN (AML transformation):**
- Standard induction chemotherapy (7+3) + venetoclax in eligible patients; IDH1/2 inhibitors for IDH-mutated cases; high allografting priority

## Connections

- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Ruxolitinib (JAK1/2 inhibitor, COMFORT-I/II) reduces spleen volume >35% in ~40% of MF patients and prolongs OS; ruxolitinib also standard for PV (RESPONSE: reduced HCT and spleen); fedratinib and pacritinib are alternative JAK2 inhibitors for MF with cytopenias.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — JAK2 V617F → constitutive STAT5 phosphorylation → EPO-independent erythropoiesis in PV; STAT5 is the primary effector of JAK2 → BCL-XL, CCND1, MYC → erythroid survival; STAT3 mediates inflammatory cytokine production in MF (IL-6, IL-8).
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — EPO → EPOR → JAK2 → STAT5 is the normal erythropoiesis axis; JAK2 V617F bypasses EPO requirement → autonomous red cell production → polycythemia in PV; serum EPO is suppressed in PV (EPO-independent erythropoiesis) and elevated in secondary polycythemia.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — TGF-β1 secreted by MPN megakaryocytes drives collagen deposition → bone marrow fibrosis in MF; TGF-β/SMAD pathway activation is central to MF fibrosis; luspatercept (activin receptor ligand trap targeting SMAD2/3) approved for MF-associated anemia (INDEPENDENCE trial).
- `connects-to` → **[Polycythemia Vera](../polycythemia-vera/README.md)** — Polycythemia vera is the erythroid-predominant MPN — JAK2 V617F (often homozygous via 9p uniparental disomy) drives EPO-independent erythrocytosis, raising thrombosis risk; managed with phlebotomy to HCT <45% and aspirin, and it can evolve to post-PV myelofibrosis.
- `connects-to` → **[JAK2](../../03-molecular/jak2/README.md)** — The JAK2 V617F mutation in the JH2 pseudokinase domain unifies the MPNs — present in ~95% of PV and ~55-60% of ET and MF — by removing autoinhibition for constitutive JAK-STAT signaling; allele burden tracks phenotype (heterozygous→ET, homozygous→PV).
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — MPNs are clonal stem-cell diseases of the bone marrow: panmyeloid hypercellularity in PV, megakaryocytic hyperplasia in ET, and progressive reticulin/collagen fibrosis (MF-0 to MF-3) in myelofibrosis that drives marrow failure and extramedullary hematopoiesis with splenomegaly.
- `connects-to` → **[Chronic Myelomonocytic Leukemia](../cmml/README.md)** — Chronic myelomonocytic leukemia is the MDS/MPN-overlap cousin of the classic myeloproliferative neoplasms: it shares their JAK2/RAS-driven proliferation, splenomegaly, and JAK-inhibitor responsiveness, but adds the peripheral monocytosis and dysplasia of MDS.
- `connects-to` → **[Myelofibrosis](../myelofibrosis/README.md)** — Myelofibrosis is the most aggressive classic MPN: JAK2/CALR/MPL-driven megakaryocytes secrete TGF-β that scars the marrow with reticulin and collagen, forcing extramedullary hematopoiesis (splenomegaly) and marrow failure; it arises de novo or evolves from PV or ET.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — Splenomegaly is the clinical signature of the myeloproliferative neoplasms, most extreme in myelofibrosis where the spleen takes over blood production (extramedullary hematopoiesis) and can fill the abdomen; JAK inhibitors (ruxolitinib) shrink it, splenectomy a last resort.
- `connects-to` → **[Essential Thrombocythemia](../essential-thrombocythemia/README.md)** — Essential thrombocythemia is one of the three classic BCR-ABL-negative myeloproliferative neoplasms, alongside polycythemia vera and myelofibrosis: a JAK2, CALR, or MPL mutation drives clonal megakaryocyte overproduction and a high platelet count, with thrombosis the main risk.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Platelets are central to MPN morbidity: clonal megakaryocytes overproduce platelets that are also qualitatively abnormal, so essential thrombocythemia and polycythemia vera cause both thrombosis and—at very high counts—bleeding from acquired von Willebrand defects.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Thrombosis is the leading cause of death in myeloproliferative neoplasms: JAK2-mutant blood is prothrombotic, producing arterial and venous clots including splanchnic-vein thromboses (Budd-Chiari, portal vein)—so cytoreduction and aspirin aim to prevent VTE.
- `connects-to` → **[Chronic Myeloid Leukemia](../cml/README.md)** — CML is the classic BCR-ABL-positive myeloproliferative neoplasm, set apart from the JAK2/CALR/MPL-driven 'Philadelphia-negative' MPNs: all overproduce mature myeloid cells, but CML's defining t(9;22) kinase makes it uniquely controllable with imatinib.
- `connects-to` → **[AML](../aml/README.md)** — Myeloproliferative neoplasms can transform into acute myeloid leukemia: chronic clonal proliferation accumulates mutations until differentiation fails and blasts take over—post-MPN AML carries a grim prognosis, the feared endpoint of these diseases.
- `connects-to` → **[Gout](../gout/README.md)** — MPNs commonly cause secondary gout: the high cell turnover floods the blood with purines that break down to uric acid, so hyperuricemia and gout flares accompany polycythemia vera and myelofibrosis—sometimes the first clue to an underlying MPN.
- `connects-to` → **[CALR](../../03-molecular/calr/README.md)** — CALR mutation is a major MPN driver alongside JAK2: in JAK2-negative essential thrombocythemia and myelofibrosis, calreticulin mutations activate the same thrombopoietin-receptor pathway, so CALR testing completes the molecular workup of myeloproliferative neoplasms.
- `connects-to` → **[MPL](../../03-molecular/mpl/README.md)** — MPL, the thrombopoietin receptor, is the third classic MPN driver: activating MPL mutations switch on JAK-STAT signaling in a minority of essential thrombocythemia and myelofibrosis, so JAK2, CALR and MPL together explain most myeloproliferative neoplasms.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Overproduction of red cells defines polycythemia vera within the MPN family: JAK2-driven erythroid expansion thickens the blood and raises clot risk, illustrating how each MPN over-makes one lineage—red cells here, platelets in ET, fibrosis in myelofibrosis.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Myeloproliferative neoplasms overproduce mature myeloid cells including neutrophils: the JAK2/CALR/MPL-driven clone expands granulocytes along with red cells and platelets, so leukocytosis is common and itself contributes to the thrombotic risk that defines MPN morbidity.
- `connects-to` → **[Stroke](../stroke/README.md)** — Thrombosis is the leading complication of myeloproliferative neoplasms: thick, sticky blood from excess cells and an activated, inflammatory clone causes arterial events including stroke, so cytoreduction and antiplatelet therapy aim to prevent these clots.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Myeloproliferative neoplasms classically cause splanchnic vein thrombosis: the prothrombotic clone clots the hepatic or portal veins (Budd-Chiari), so unexplained abdominal-vein thrombosis should prompt JAK2 testing—sometimes the first sign of an occult MPN.
- `connects-to` → **[Thrombopoietin](../../03-molecular/thrombopoietin/README.md)** — MPNs hijack thrombopoietin signaling: CALR and MPL mutations make blood cells respond as if flooded with thrombopoietin even when levels are normal, driving the runaway platelet and megakaryocyte production of essential thrombocythemia and myelofibrosis.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Myelofibrosis is the scarring face of MPNs: clonal megakaryocytes pour out cytokines that drive fibroblasts to lay down marrow fibrosis, choking blood production and forcing the spleen and liver to take over—the hallmark of advanced disease.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Polycythemia vera ties MPNs to iron: overproduction of red cells consumes iron and therapeutic phlebotomy deliberately induces iron deficiency to limit red-cell mass, so iron balance is both a consequence and a lever of treatment.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — Myeloproliferative neoplasms smolder with IL-6 and inflammation: the JAK2-mutant clone pumps out IL-6 and other cytokines that cause fevers, weight loss, and itching and drive progression to fibrosis—why JAK inhibitors relieve symptoms so well.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Immune surveillance by NK cells shapes myeloproliferative neoplasms: natural killer cells help police the mutant clone, and their exhaustion or dysfunction may let the disease expand—an angle for immune-based approaches alongside JAK inhibitors.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — MPN stem cells use autophagy to persist through treatment: the clonal cells recycle their contents to survive stress and JAK inhibition, so blocking autophagy is studied as a way to deepen responses and target the disease at its root.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — High blood counts in MPN can fake high potassium: the huge numbers of platelets and white cells leak potassium after the sample clots, producing pseudohyperkalemia—a lab artifact to recognize before treating a number that isn't real.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — MPNs threaten the brain with clots: thickened, sticky blood from too many cells raises the risk of stroke and cerebral vein thrombosis, so controlling counts and using aspirin aim to protect against these neurologic catastrophes.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Inflammation via NF-kB fuels the myeloproliferative clone: alongside JAK-STAT, the mutated stem cells drive NF-kB signaling that pours out cytokines, feeding the symptoms, marrow fibrosis and clonal expansion of these neoplasms.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — MPNs itch through the skin: aquagenic pruritus—intense itching minutes after a warm shower—is a classic symptom, especially of polycythemia vera, sometimes appearing before the diagnosis.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — MPN itching is driven by mast cells: the expanded clone's basophils and mast cells release histamine, which fires skin itch nerves to cause the aquagenic pruritus that torments these patients.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Polycythemia overrides the body's oxygen control: normally low oxygen raises erythropoietin to make red cells, but the JAK2 clone churns them out regardless, thickening the blood independent of oxygen need.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Radioactive phosphorus once tamed these clones with electrons: P-32 concentrates in marrow and emits beta particles — fast electrons — that suppress the overactive blood-cell factory, a historic polycythemia treatment now reserved for select older patients.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Myeloproliferative disease can choke the lungs: extramedullary hematopoiesis and microvascular thrombosis raise pulmonary pressures, so pulmonary hypertension and clots are recognized complications, especially in myelofibrosis.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — The kidney bears the brunt of high cell turnover: the massive production and breakdown of blood cells floods the blood with uric acid, which crystallizes in the tubules and can drive urate nephropathy and stones.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Myeloproliferative disease clots the arteries too: the thick, sticky blood and activated platelets drive arterial thrombosis, so heart attacks join the strokes and venous clots that menace these patients.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — MPN is a leading cause of unusual-site clots: thrombosis of the splanchnic veins draining the gut — portal, mesenteric, and the hepatic veins of Budd-Chiari — can be the first sign, sometimes before the blood counts even rise.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — The frenzied cell turnover spills phosphorus: the constant birth and death of blood cells, and their lysis under treatment, release phosphate and urate, the metabolic overflow that strains the kidneys and provokes gout.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Thrombosis is the central danger of MPN: the JAK2-mutant, thickened blood plus an activated, sticky endothelial-cell lining drives clots in both arteries and veins, the strokes and heart attacks that are the leading cause of death in these disorders.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — A maddening itch after a warm bath marks polycythemia vera: basophils and mast cells expanded by the MPN clone dump histamine, the aquagenic pruritus that water triggers being one of the disease's most distinctive complaints.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Sludgy blood blurs the vision: the hyperviscosity of a high red-cell or platelet count slows retinal flow, causing visual disturbances and engorged retinal veins, while erythromelalgia's burning can be matched by ocular symptoms in advanced disease.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — MPNs complicate pregnancy: the prothrombotic clone, especially JAK2-mutant, raises the risk of miscarriage, placental thrombosis and maternal clots, so affected women are managed with aspirin, low-molecular-weight heparin and pregnancy-safe interferon.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — The marrow can turn to bone: in the myelofibrosis subtype the fibrotic drive spills into osteosclerosis, where osteoblasts lay down excess bone that further crowds out blood production and shows as dense marrow on imaging.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — The overgrown marrow grows its own vessels: MPNs, especially myelofibrosis, raise VEGF and marrow microvessel density, an angiogenic drive that supports the expanding malignant clone and tracks with disease burden.
- `connects-to` → **[TET2](../../03-molecular/tet2/README.md)** — The driver mutation rarely acts alone: epigenetic hits like TET2 (with DNMT3A and ASXL1) often precede or accompany the JAK2 driver, shaping which MPN appears, how it evolves, and its risk of turning into acute leukemia.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — The mutant clone inflames the arteries: JAK2-mutated blood cells, a form of clonal hematopoiesis, accelerate atherosclerosis and arterial thrombosis, so MPNs raise heart-attack and stroke risk beyond what their high cell counts alone would predict.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Clonal macrophages help scar the marrow: monocytes and macrophages derived from the malignant clone pour out TGF-β and other fibrogenic signals that drive the reticulin and collagen fibrosis of myelofibrosis, remodeling the marrow they grow in.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — Epigenetic mutations layer onto the driver: DNMT3A, TET2 and other clonal-hematopoiesis mutations co-occur with JAK2/CALR/MPL in MPNs, shaping clonal evolution and the risk of progression to myelofibrosis or leukemia.
- `connects-to` → **[Myelodysplastic Syndromes](../mds/README.md)** — The clone can drift toward dysplasia: MPNs sit on the myeloid spectrum and can evolve into MDS/MPN-overlap or acquire dysplastic, MDS-like features, especially as they accumulate secondary mutations.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Fibroblasts lay down the marrow scar: responding to clone-derived TGF-β and PDGF, marrow stromal fibroblasts deposit the reticulin and collagen that obliterate the marrow space in myelofibrosis.
- `connects-to` → **[Hepatocellular Carcinoma](../hcc/README.md)** — They clot the liver's own veins: MPNs are the leading cause of Budd-Chiari syndrome and portal vein thrombosis, congesting the liver toward cirrhosis and, over years, hepatocellular carcinoma — often the first clue to an occult MPN.
- `connects-to` → **[Pulmonary Arterial Hypertension](../pulmonary-arterial-hypertension/README.md)** — The lung circulation stiffens: MPNs raise pulmonary artery pressure through chronic thromboembolism, extramedullary hematopoiesis and high-output flow, a recognized and under-appreciated complication.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Advanced disease strips the defenses: progression to myelofibrosis or blast phase, and the cytoreductive and JAK-inhibitor therapy used, cause cytopenias and immune compromise that make infection and sepsis a danger.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Marrow fibrosis and inflammation lower the count: as MPNs evolve toward a spent, myelofibrotic phase, marrow scarring and chronic inflammation replace the cellular excess with an anemia of chronic disease.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — JAK inhibitors open the lung to mold: ruxolitinib used for myelofibrosis and polycythemia vera suppresses immunity and, with disease-related neutropenia, raises the risk of invasive aspergillosis and other opportunistic infections.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A chronic clonal disease wears on mood: the heavy constitutional symptom burden — fatigue, itch, night sweats — and the lifelong thrombosis-and-transformation risk of MPNs contribute to depression and reduced quality of life.
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — JAK inhibition reawakens shingles: ruxolitinib used for myelofibrosis and polycythemia vera dampens T-cell immunity and characteristically reactivates latent varicella-zoster, a recognised risk during therapy.
- `connects-to` → **[Iron-Deficiency Anemia](../iron-deficiency-anemia/README.md)** — Treating polycythemia drains the iron stores: the repeated therapeutic phlebotomy used to control the red-cell mass in polycythemia vera deliberately induces iron deficiency to limit erythropoiesis.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Lifelong clot-and-transformation risk breeds worry: the constant threat of thrombosis and progression to acute leukaemia in MPNs, plus relentless symptoms, fosters chronic health anxiety alongside low mood.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — They clot the gut's veins and swell the spleen: MPNs are a leading cause of splanchnic, portal and hepatic vein thrombosis (Budd-Chiari), and massive splenomegaly from extramedullary haematopoiesis causes early satiety.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Excess blood cells torment the skin: polycythemia vera causes the intense aquagenic pruritus after bathing, and essential thrombocythemia produces the burning red erythromelalgia of the extremities.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Sludgy, clot-prone blood strains the circulation: the raised cell mass and platelet activation of MPNs cause arterial thrombosis with myocardial infarction, hypertension and a high-output cardiovascular burden.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — They swell the spleen: extramedullary haematopoiesis and pooling of blood cells enlarge the spleen, often massively in myelofibrosis, with a risk of splenic infarction and early satiety.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Thick blood disturbs the brain: hyperviscosity and microvascular thrombosis in MPNs cause headache, visual disturbance, transient ischaemic attacks and stroke.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — They burden bone and joints: marrow expansion and the osteosclerosis of myelofibrosis cause bone pain, while high cell turnover raises uric acid and precipitates gout.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Clots and blood-making reach the lungs: MPNs cause pulmonary embolism and pulmonary hypertension, and extramedullary haematopoiesis can rarely involve the lungs.
- `connects-to` → **[Renal System](../renal-system/README.md)** — High cell turnover taxes the kidney: hyperuricaemia causes urate nephropathy, an MPN-associated glomerulopathy occurs, and renal vein thrombosis can complicate the prothrombotic state.
- `connects-to` → **[Aspirin](../../../03-medicine/01-modern/04-cardio/aspirin/README.md)** — Low-dose aspirin counters the clotting: by inhibiting the overactive platelets of myeloproliferative neoplasms, aspirin reduces thrombosis and microvascular symptoms, alongside cytoreduction.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — JAK inhibition is the targeted backbone: ruxolitinib and fedratinib block the JAK2-STAT pathway driving myeloproliferative neoplasms, shrinking the spleen and easing symptoms in myelofibrosis and polycythaemia vera.
- `connects-to` → **[Mycobacterium tuberculosis](../../../02-pathogen/02-bacteria/mycobacterium-tuberculosis/README.md)** — JAK inhibitors reawaken latent infection: ruxolitinib suppresses immunity enough to reactivate tuberculosis and other opportunists, requiring screening before treatment.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Hydroxyurea cytoreduces: the oral chemotherapy hydroxyurea lowers excess blood counts in high-risk myeloproliferative neoplasms, a long-standing cytoreductive mainstay.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — It clots the liver and seeds it with blood-making: myeloproliferative neoplasms are a leading cause of Budd-Chiari and portal vein thrombosis, and their excess progenitors lodge in the hepatic lobules as extramedullary haematopoiesis, enlarging the liver.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — Thrombosis is its chief killer: JAK2-mutant blood cells inflame and adhere to the arterial wall, promoting endothelial dysfunction and the arterial thrombosis—heart attack and stroke—that drives mortality in polycythaemia vera and essential thrombocythaemia.
- `connects-to` → **[CKD](../ckd/README.md)** — It also wears down the kidney: myeloproliferative neoplasms impair renal function through hyperuricaemia, microvascular thrombosis and an MPN-associated glomerulopathy, so chronic kidney disease accumulates as the clone persists.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Arterial thrombosis and the heart: MPN hyperviscosity and reactive platelets cause arterial thrombi including myocardial infarction, a leading cause of death in polycythaemia vera and essential thrombocythaemia.
- `connects-to` → **[Antiphospholipid Syndrome](../antiphospholipid-syndrome/README.md)** — Two causes of unexplained thrombosis: MPN and antiphospholipid syndrome both cause arterial and unusual-site venous thrombosis (splanchnic, cerebral), key differentials in a young patient with a clot.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Osteosclerosis of myelofibrosis: as the marrow fibroses, reactive new bone formation thickens and scleroses the cortical bone, the radiographic counterpart of the fibrotic marrow.
- `connects-to` → **[Von Willebrand Factor](../../03-molecular/von-willebrand-factor/README.md)** — Bleeding amid thrombosis: extreme thrombocytosis in essential thrombocythaemia adsorbs and clears high-molecular-weight von Willebrand multimers, causing an acquired von Willebrand syndrome that bleeds paradoxically in a prothrombotic disease.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — MPN nephropathy: chronic myeloproliferative neoplasms cause a distinctive glomerulopathy with mesangial sclerosis and proteinuria, megakaryocytes and platelet-derived factors injuring the glomerulus over time.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Stacked thrombotic risk: the JAK2-driven hypercoagulable state of myeloproliferative neoplasms compounds the thrombo-inflammation of COVID-19, raising the risk of arterial and venous clots during infection.
- `connects-to` → **[Type I Interferon](../../03-molecular/type-i-interferon/README.md)** — Clone-reducing therapy: pegylated interferon-alpha is a disease-modifying treatment for myeloproliferative neoplasms that can shrink the JAK2/CALR-mutant clone and induce molecular responses.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Epigenetic progression: EZH2 and other epigenetic-regulator mutations accumulate in myeloproliferative neoplasms and drive progression toward myelofibrosis and acute leukaemia.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Inflammatory niche: IL-1β secreted by the mutant clone damages the bone-marrow stroma, promoting the fibrosis and clonal advantage that mark myeloproliferative neoplasm progression.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Clonal advantage: TNF-α from the JAK2-mutant clone is preferentially tolerated by the mutant cells while suppressing normal haematopoiesis, helping the neoplastic clone dominate the marrow.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Inflammasome activation: JAK2-driven NLRP3-inflammasome activation amplifies the chronic inflammation of myeloproliferative neoplasms, contributing to their symptoms and thrombotic risk.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Marrow hypoxia: HIF-1α stabilised in the hypercellular, hypoxic MPN marrow supports the survival and angiogenic signalling of the expanded clone.
- `connects-to` → **[PF4](../../03-molecular/pf4/README.md)** — Thrombotic risk: PF4 released from the expanded, activated platelet mass of myeloproliferative neoplasms marks the platelet hyperreactivity behind their characteristic arterial and venous thrombosis.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — Myeloid alarmin: S100A8/A9 from the expanded myeloid compartment amplifies the chronic inflammation of myeloproliferative neoplasms, driving constitutional symptoms and disease progression.
- `connects-to` → **[RUNX1](../../03-molecular/runx1/README.md)** — Leukaemic transformation: acquired RUNX1 mutations mark the progression of myeloproliferative neoplasms toward acute myeloid leukaemia, a feared terminal evolution.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — PDGF released by the clonal megakaryocytes of myeloproliferative neoplasms stimulates marrow fibroblasts, driving the reticulin and collagen fibrosis of primary and post-PV/ET myelofibrosis as the disease evolves.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — The hyperreactive platelets of myeloproliferative neoplasms generate thromboxane A2, the target of the low-dose aspirin used to reduce the arterial and venous thrombosis that is their leading cause of morbidity.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — The massive hematopoietic turnover of myeloproliferative neoplasms floods purine catabolism through xanthine oxidase, raising urate and causing the secondary hyperuricemia and gout that frequently complicate these disorders.
- `connects-to` → **[SF3B1](../../03-molecular/sf3b1/README.md)** — Spliceosome mutations such as SF3B1, acquired alongside the JAK2/CALR/MPL driver, mark the myeloproliferative neoplasms more likely to progress to myelofibrosis or acute leukemia, refining prognosis beyond the driver alone.
- `connects-to` → **[Thrombin](../../03-molecular/thrombin/README.md)** — The raised cell counts and activated platelets and leukocytes of myeloproliferative neoplasms promote thrombin generation and hyperviscosity, making arterial and venous thrombosis—including unusual splanchnic-vein clots—their leading cause of morbidity.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors are paradoxically active in JAK2-mutant myeloproliferative neoplasms, maintaining the malignant hematopoietic stem cells that sustain the clone and resist JAK-inhibitor therapy.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — JAK2, CALR and MPL (all already mapped) activate the RAS-MAPK-ERK cascade alongside JAK-STAT, a parallel proliferative driver in myeloproliferative neoplasms.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — The same constitutively active receptor-kinase signaling engages PI3K-AKT as a third effector pathway supporting myeloid proliferation and survival in MPN.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 inactivation drives the progression of myeloproliferative neoplasms, particularly myelofibrosis, to acute myeloid leukemia.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — The PI3K-AKT axis (PIK3CA already mapped) operates downstream of constitutive JAK2 signaling to drive the proliferation and survival of myeloproliferative-neoplasm clones.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR-MyD88-NF-κB innate signaling (NF-κB already mapped) sustains the chronic inflammatory milieu that characterizes and propels myeloproliferative neoplasms.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A loss is among the cooperating lesions in the leukemic transformation of myeloproliferative neoplasms to acute myeloid leukemia.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — JAK2-driven PI3K-AKT-mTOR signaling (JAK2 and AKT mapped) supports clonal proliferation in myeloproliferative neoplasms, a target of mTOR-inhibitor combinations.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — Type-I-interferon signaling through STAT1 (type-I-interferon mapped) underlies the disease-modifying activity of interferon therapy across the myeloproliferative neoplasms.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 expressed by megakaryocytes contributes to the marrow microenvironment and the fibrotic progression of myeloproliferative neoplasms.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING amplifies the chronic inflammatory marrow milieu (type-I interferon already mapped) of myeloproliferative neoplasms.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β already mapped) released by clonal megakaryocytes drives the bone-marrow fibrosis of myeloproliferative neoplasms.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6-cyclin-D activity (CDKN2A already mapped) drives the JAK2-fueled myeloproliferative cell-cycle progression of myeloproliferative neoplasms.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β misregulation contributes to the aberrant hematopoietic stem-cell self-renewal of myeloproliferative neoplasms.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis and contributes to the leukemic evolution of myeloproliferative neoplasms.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated cytotoxic immunosurveillance targets the neoantigen-bearing CALR-mutant clone of myeloproliferative neoplasms.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family and LYN kinase signaling cooperates with JAK2-STAT to support the survival of the clonal myeloid cells of myeloproliferative neoplasms.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of the clonal hematopoietic stem cells of myeloproliferative neoplasms.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A and the broader chromatin machinery contribute to the epigenetic dysregulation of myeloproliferative neoplasms.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-family chemokine signaling participates in the aberrant myeloid trafficking and inflammatory bone-marrow niche of myeloproliferative neoplasms.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling in the bone-marrow niche participates in the clonal hematopoiesis and megakaryocyte-driven fibrosis of myeloproliferative neoplasms.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — NOTCH signaling participates in the megakaryocyte and stromal biology contributing to the myelofibrosis of myeloproliferative neoplasms.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the inflammatory bone-marrow microenvironment of myeloproliferative neoplasms.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory bone-marrow microenvironment of myeloproliferative neoplasms.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory and thrombotic microenvironment of myeloproliferative neoplasms.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the megakaryocyte and clonal-myeloproliferation signaling of myeloproliferative neoplasms.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine signaling participates in the immunosuppressive bone-marrow microenvironment of myeloproliferative neoplasms.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin participates in the bone-marrow-fibrosis and stromal interactions of myeloproliferative neoplasms.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Erythrocytosis: in polycythaemia vera the JAK2-driven erythroid overproduction (erythropoietin already mapped) raises haemoglobin and haematocrit, thickening the blood and driving the thrombosis managed with phlebotomy and cytoreduction.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Arterial thrombosis: myeloproliferative neoplasms markedly raise the risk of arterial events including myocardial infarction and stroke, and troponin elevation marks the cardiac injury of these thrombotic complications that dominate their morbidity.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Endothelial-platelet imbalance: impaired endothelial nitric-oxide function, with the excess activated blood cells of myeloproliferative neoplasms, tips the vascular balance toward the thrombosis (vWF already mapped) that is a leading cause of death.
- `connects-to` → **[ADAMTS13](../../03-molecular/adamts13/README.md)** — Acquired von Willebrand syndrome: extreme thrombocytosis clears the high-molecular-weight von Willebrand multimers (already mapped), causing the acquired von Willebrand syndrome and the paradoxical bleeding that coexists with thrombosis in these neoplasms.
- `connects-to` → **[Protein C](../../03-molecular/protein-c/README.md)** — Prothrombotic tilt: the thrombosis of myeloproliferative neoplasms reflects a shift toward coagulation, and reduced activity of the natural anticoagulant protein C (thrombin already mapped) further raises the risk that drives cytoreduction and antithrombotic therapy.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Inflammatory milieu: myeloproliferative neoplasms carry a chronic inflammatory state, and the anti-inflammatory IL-10 counterbalances the TNF, IL-6 and IL-1 (already mapped) driven by JAK-STAT signalling that shapes their phenotype and symptoms.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Microvascular vasoconstriction: endothelin-1 and the platelet-derived vasoactive mediators contribute to the microvascular vasoconstriction behind the erythromelalgia and neurological symptoms of the myeloproliferative neoplasms.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Platelet serotonin: serotonin released from the abnormal, activated platelets (PF4 already mapped) causes vasoconstriction and amplifies aggregation, contributing to the microvascular symptoms and thrombosis of the myeloproliferative neoplasms.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — Endothelial activation: the angiopoietin-Tie2 axis reflects the endothelial activation of the prothrombotic state of the myeloproliferative neoplasms, part of the endothelium's contribution (von Willebrand factor already mapped) to their thrombosis.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Iron restriction and anaemia: the hepcidin-mimetic rusfertide restricts iron (already mapped) to control the erythrocytosis of polycythaemia vera, while the raised hepcidin of chronic inflammation (IL-6 already mapped) contributes to the anaemia of myelofibrosis.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Inflammatory milieu: IL-4 and the M2 macrophage arm (IL-10 already mapped) shape the chronic inflammation (IL-6 and TNF already mapped) of the myeloproliferative marrow, part of the disease biology of the myeloproliferative neoplasms.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Marrow adipose crosstalk: the marrow adipocytes and their adipokine leptin signal to the clonal myeloid cells, part of the bone-marrow (already mapped) microenvironment of the myeloproliferative neoplasms.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — M2 inflammatory arm: IL-13, with IL-4 (already mapped), drives the M2 macrophage arm of the chronic inflammation (IL-6 and TNF already mapped) of the myeloproliferative marrow.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Marrow-adipocyte adipokine: adiponectin, with leptin (already mapped), from the marrow adipose tissue signals to the clonal myeloid cells of the bone-marrow (already mapped) microenvironment of the myeloproliferative neoplasms.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the inflammatory milieu of the myeloproliferative neoplasms.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Clonal immunosurveillance: the cytotoxic T cells (perforin already mapped) provide the immune surveillance of the JAK2 (already mapped)-mutant clone, augmented by the interferon (type-I interferon already mapped) therapy of the myeloproliferative neoplasms.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 arm: the IFN-γ of the T cells (with the type-I interferon already mapped) is the type-II interferon arm of the anti-clonal immunity and the inflammatory milieu of the myeloproliferative neoplasms.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) response of the anti-clonal immunity of the myeloproliferative neoplasms.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the inflammatory milieu of the myeloproliferative neoplasms (and the driver of the eosinophilic MPN variants).
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the chronic inflammatory milieu of the myeloproliferative neoplasms.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the inflammatory milieu of the myeloproliferative neoplasms.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Antigen presentation: the dendritic cells present antigen to the T cells (already mapped) within the inflammatory clonal-haematopoiesis microenvironment of the myeloproliferative neoplasms.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the chronic inflammatory milieu that drives the constitutional symptoms of the myeloproliferative neoplasms.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Thromboinflammation: the complement C5 and its C5a (with C3 already mapped) contribute to the complement-driven thromboinflammation and the thrombotic risk of the myeloproliferative neoplasms.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) links the complement to the myeloid inflammation and the immunothrombosis of the myeloproliferative neoplasms.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) whose dysregulation amplifies the thromboinflammation of the myeloproliferative neoplasms.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — MPN iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the iron deficiency of polycythaemia vera and the anaemia of myelofibrosis.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Bone-marrow stroma alarmin: TSLP from the inflamed JAK2-mutant (already mapped) myeloproliferative bone marrow activates the stromal dendritic cells and mast cells, amplifying the NF-kB (already mapped) and STAT3 (already mapped) pro-inflammatory microenvironment of MPN.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Thrombosis amplifier: bradykinin activates B2 receptors on the platelets (already mapped) and vascular endothelium (already mapped), amplifying the hypercoagulability and microvascular thrombotic complications (VTE already mapped) of the JAK2-mutant myeloproliferative neoplasms.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Myelofibrosis stroma: periostin, downstream of TGF-β (already mapped) and megakaryocyte-derived growth factors, drives the collagen deposition and fibroblast activation of the bone marrow (already mapped) fibrosis that characterises the myeloproliferative neoplasms.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — MPN complement regulation: C1-INH controls the classical-pathway arm (C3, C5 and C5aR1 already mapped) in the MPN microenvironment, complementing factor H (already mapped) to limit complement-driven thrombosis and JAK2 (already mapped) neutrophil activation.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Oncostatic melatonin in MPN: melatonin inhibits the JAK2 (already mapped)/STAT3 (already mapped) signalling cascade in myeloproliferative neoplasm progenitor cells, attenuates mast-cell (already mapped) histamine release and reduces the thrombo-inflammatory burden of MPN.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Prolactin-JAK2 axis: prolactin, via PRLR-mediated JAK2 (already mapped)/STAT5 activation, amplifies the constitutive JAK2V617F signalling of polycythaemia-vera and essential thrombocythaemia; elevated prolactin levels correlate with the inflammatory cytokine burden of MPN.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Androgen-erythrocyte axis: testosterone, via androgen receptor on JAK2-V617F-mutant (already mapped) erythroid progenitor cells (already mapped), potentiates the erythrocytosis and myeloid proliferative drive of the polycythemia vera spectrum of myeloproliferative neoplasms.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Haematopoietic neuropeptide: oxytocin, via OXT-R on bone-marrow stromal cells (already mapped) and megakaryocytes (already mapped), modulates haematopoietic niche signalling and the thrombopoiesis dysregulated in essential thrombocythemia of myeloproliferative neoplasms.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Platelet-vasopressin axis: vasopressin, via V1a receptors on platelets (already mapped) and endothelial cells (already mapped), amplifies the thrombotic risk and platelet activation of the essential-thrombocythemia and polycythemia-vera spectrum of myeloproliferative neoplasms.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — MPN selenium antioxidant: selenium, via GPx/TrxR selenoproteins in JAK2-V617F-mutant (already mapped) cells and macrophages (already mapped), quenches oxidative stress that amplifies NF-κB (already mapped) and IL-6 (already mapped) signalling in myeloproliferative neoplasms.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — MPN iodine thyroid: iodine, as the key substrate for thyroid hormone biosynthesis, supports bone-marrow (already mapped) haematopoiesis; iodine insufficiency amplifies the IL-6 (already mapped) and NF-κB (already mapped) myeloid drive of myeloproliferative neoplasms.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — MPN sodium inflammatory: sodium, at supraphysiological concentrations in the myeloid marrow, activates macrophage (already mapped) NF-κB (already mapped) and IL-6 (already mapped) signalling, promoting the pro-inflammatory myeloid shift in myeloproliferative neoplasms.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — MPN magnesium: magnesium, as cofactor of JAK2 regulatory enzymes in macrophages (already mapped) and erythrocytes (already mapped), supports haematopoiesis; magnesium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) myeloproliferative cascade.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — MPN copper: copper, as cofactor of SOD1 in macrophages (already mapped) and neutrophils (already mapped), neutralises ROS; copper deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) myeloproliferative oxidative cascade.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — MPN zinc: zinc, as cofactor of antioxidant enzymes in macrophages (already mapped) and platelets (already mapped), attenuates oxidative stress; zinc deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) haematopoietic myeloproliferative cascade.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — MPN calcium: calcium, as second messenger in macrophages (already mapped) and mast cells (already mapped), regulates myeloid cell activation; calcium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) haematopoietic cascade of myeloproliferative neoplasms.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — MPN chloride: chloride channels regulate macrophage (already mapped) and neutrophil (already mapped) ion homeostasis in the myeloproliferative bone marrow; chloride imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — MPN sulfur: sulfur-containing amino acids in macrophages (already mapped) and mast cells (already mapped) maintain redox buffering; sulfur depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) myeloproliferative oxidative cascade.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — MPN carbon: carbon as backbone of JAK2 (already mapped) and calreticulin structural proteins in megakaryocytes (already mapped) sustains clonal myeloid expansion; carbon depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) myeloproliferative cascade.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — MPN hydrogen: hydrogen, via redox homeostasis in macrophages (already mapped) and neutrophils (already mapped), supports JAK2 (already mapped) signalling in myeloproliferative bone marrow; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — MPN nitrogen: nitrogen in amino-acid scaffold of JAK2 (already mapped) and CALR proteins in megakaryocytes (already mapped) sustains clonal haematopoiesis; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) myeloproliferative cascade.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — MPN PD-1: PD-1 checkpoint on T-cytotoxic cells (already mapped) and NK cells (already mapped) in clonal bone marrow modulates immune escape; PD-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) myeloproliferative cascade.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — MPN GLP-1: GLP-1 receptor agonism on megakaryocytes (already mapped) and macrophages (already mapped) modulates clonal marrow inflammation; GLP-1 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) myeloproliferative cascade.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — MPN angiotensin-II: angiotensin-II via AT1R on bone-marrow stromal cells (already mapped) and macrophages (already mapped) drives fibrotic remodelling; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) myeloproliferative cascade.
- `connects-to` → **[WNT-β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — MPN wnt-beta-catenin: WNT/β-catenin on macrophages (already mapped) and fibroblasts (already mapped) regulates clonal marrow expansion; wnt-beta-catenin dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and smad4 (already mapped) cascade of MPN.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — MPN rankl: RANKL from macrophages (already mapped) and osteoblasts (already mapped) promotes clonal myeloid immune evasion; rankl excess amplifies nf-kb (already mapped) and il-6 (already mapped) and smad4 (already mapped) myeloproliferative cascade.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — MPN il-2: IL-2 from t-cytotoxic cells (already mapped) and macrophages (already mapped) regulates clonal myeloid immune tone; il-2 dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and smad4 (already mapped) myeloproliferative cascade.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — MPN fibronectin: fibronectin in macrophages (already mapped) and fibroblasts (already mapped) promotes clonal marrow ECM remodelling; fibronectin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and smad4 (already mapped) myeloproliferative cascade.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — MPN igf-1: IGF-1 from macrophages (already mapped) and fibroblasts (already mapped) promotes clonal myeloid cell survival; igf-1 dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and smad4 (already mapped) myeloproliferative cascade.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — MPN activin-a: activin-A from macrophages (already mapped) and fibroblasts (already mapped) drives clonal marrow fibrosis; activin-a excess amplifies nf-kb (already mapped) and il-6 (already mapped) and smad4 (already mapped) myeloproliferative cascade.

[^verstovsek-2012-comfort-i]: Verstovsek S, Mesa RA, Gotlib J, et al. A double-blind, placebo-controlled trial of ruxolitinib for myelofibrosis. *N Engl J Med.* 2012;366(9):799-807. [doi:10.1056/NEJMoa1110557](https://doi.org/10.1056/NEJMoa1110557) · [PubMed 22375971](https://pubmed.ncbi.nlm.nih.gov/22375971/)
[^vannucchi-2015-response]: Vannucchi AM, Kiladjian JJ, Griesshammer M, et al. Ruxolitinib versus standard therapy for the treatment of polycythemia vera. *N Engl J Med.* 2015;372(5):426-435. [doi:10.1056/NEJMoa1409002](https://doi.org/10.1056/NEJMoa1409002) · [PubMed 25426978](https://pubmed.ncbi.nlm.nih.gov/25426978/)
