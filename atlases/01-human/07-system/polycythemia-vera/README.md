---
schema: human-scale-entry/v1
id: polycythemia-vera
name: Polycythemia Vera
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Polycythemia vera is a JAK2-driven MPN with erythrocytosis, thrombocytosis, and leukocytosis; JAK2 V617F ~99%; phlebotomy + low-dose aspirin for all; hydroxyurea or ropeginterferon alfa-2b for high-risk; ruxolitinib for HU-resistant; MF/AML transformation risk."
aliases: ["polycythemia vera", "PV", "polycythaemia vera", "primary polycythemia", "JAK2 V617F polycythemia", "polycythemia rubra vera"]
sources:
  - id: vannucchi-2015-response
    type: peer-reviewed
    cite: "Vannucchi AM, Kiladjian JJ, Griesshammer M, et al. Ruxolitinib versus standard therapy for the treatment of polycythemia vera. N Engl J Med. 2015;372(5):426-435."
    doi: "10.1056/NEJMoa1409630"
    pmid: "25577388"
    url: "https://doi.org/10.1056/NEJMoa1409630"
  - id: gisslinger-2020-proud-pv
    type: peer-reviewed
    cite: "Gisslinger H, Gotic M, Holowiecki J, et al. Ropeginterferon alfa-2b versus standard therapy for polycythaemia vera (PROUD-PV and CONTINUATION-PV): a randomised, non-inferiority, phase 3 trial and its extension study. Lancet Haematol. 2020;7(3):e196-e208."
    doi: "10.1016/S2352-3026(19)30236-4"
    pmid: "32046833"
    url: "https://doi.org/10.1016/S2352-3026(19)30236-4"
cross_links:
  - target: 01-human/03-molecular/epas1
    relation: connects-to
    note: "HIF-2α (EPAS1) drives EPO transcription; VHL loss or EPAS1 GOF mutations → secondary/hereditary erythrocytosis; PHD2/EGLN1 mutations stabilize HIF-2α; PV distinguished from secondary erythrocytosis by low serum EPO + JAK2 V617F mutation."
  - target: 01-human/03-molecular/jak2
    relation: connects-to
    note: "JAK2 V617F is present in ~99% PV; GOF in JH2 pseudokinase domain → constitutive JAK2/STAT5 → EPO-independent erythroid proliferation; ruxolitinib (RESPONSE: Hct control 21% vs 1%) FDA-approved for HU-resistant/intolerant PV."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Serum EPO is suppressed in PV (WHO minor criterion) due to constitutive JAK2 erythropoiesis; secondary erythrocytosis (hypoxia, VHL mutation) shows elevated EPO; EPO level distinguishes primary from secondary polycythemia; ropeginterferon reduces EPO-driven clonal expansion."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "PV transforms to post-PV myelofibrosis (~10-15% at 10 years); megakaryocyte-derived TGF-β1 → collagen deposition → reticulin/collagen fibrosis; momelotinib and luspatercept address TGF-β-driven anemia in post-PV MF."
  - target: 01-human/07-system/myeloproliferative-neoplasms
    relation: connects-to
    note: "Polycythemia vera is the erythroid-dominant member of the BCR-ABL-negative myeloproliferative neoplasms (with ET and myelofibrosis), nearly always JAK2-driven (~99% V617F); it shares their thrombosis risk and capacity to evolve into post-PV myelofibrosis or AML."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "JAK2 V617F makes erythroid progenitors expand without EPO (endogenous erythroid colonies), raising red-cell mass and blood viscosity → arterial and venous thrombosis; phlebotomy to hematocrit <45% cuts cardiovascular events ~45% (CYTO-PV) by lowering that viscosity."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "Splenomegaly affects ~70% of PV from extramedullary hematopoiesis, causing early satiety and, when massive, infarction risk; it worsens as disease evolves toward post-PV myelofibrosis, and the JAK1/2 inhibitor ruxolitinib reduces spleen volume in HU-resistant patients."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Thrombosis is the leading cause of death in polycythemia vera, arterial events dominating: raised red-cell mass, JAK2 hyperviscosity, and activated platelets cause stroke, MI, and Budd-Chiari/splanchnic-vein thrombosis; phlebotomy to hematocrit <45% and aspirin cut these events."
  - target: 01-human/07-system/essential-thrombocythemia
    relation: connects-to
    note: "Polycythemia vera and essential thrombocythemia are sibling JAK2-driven myeloproliferative neoplasms on a continuum: PV expands the erythroid lineage (high hematocrit) and ET the megakaryocytic (high platelets), but both carry thrombosis risk and can evolve to myelofibrosis."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Polycythemia vera is a clonal bone marrow stem-cell disease: a JAK2 V617F-mutant hematopoietic stem cell produces panmyelosis — hypercellular marrow with trilineage (especially erythroid) proliferation — and a low EPO; over years the marrow can scar into post-PV myelofibrosis."
  - target: 01-human/07-system/myelofibrosis
    relation: connects-to
    note: "Polycythemia vera can burn out into post-PV myelofibrosis: after years of JAK2-driven erythrocytosis, the marrow becomes fibrotic and counts fall, with massive splenomegaly—one of PV's two main long-term fates, the other being acute leukemia."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Thrombosis is the chief danger of polycythemia vera: high hematocrit and JAK2-mutant, hyperviscous blood drive arterial and venous clots, including splanchnic-vein thromboses that can be the presenting clue—so phlebotomy and aspirin aim to prevent them."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "Polycythemia vera carries a small but serious risk of leukemic transformation: the JAK2-mutant clone can acquire further mutations and evolve into acute myeloid leukemia, a feared, largely chemo-resistant end-stage—so cytoreduction choice weighs leukemogenic risk."
  - target: 01-human/07-system/gout
    relation: connects-to
    note: "Polycythemia vera commonly causes secondary gout: the high turnover of overproduced red cells releases purines that become uric acid, so hyperuricemia and gout flares are frequent—sometimes the presenting clue to an unsuspected myeloproliferative neoplasm."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Polycythemia vera must be distinguished from the secondary erythrocytosis of kidney disease: PV is JAK2-driven red-cell overproduction with low EPO, while renal pathology drives high-EPO secondary polycythemia—measuring erythropoietin separates primary from secondary."
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "Renal cell carcinoma is a classic cause of secondary polycythemia: the tumor ectopically secretes erythropoietin, raising red-cell mass without the JAK2 mutation of true polycythemia vera—so unexplained erythrocytosis warrants imaging to exclude an EPO-producing tumor."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Polycythemia vera must be told from oxygen-driven secondary polycythemia: PV makes red cells autonomously via JAK2 with LOW erythropoietin, whereas chronic hypoxia (lung disease, altitude) raises EPO appropriately—so a low EPO points to primary disease."
  - target: 01-human/07-system/iron-deficiency-anemia
    relation: connects-to
    note: "Chronic phlebotomy treatment makes PV patients iron-deficient: removing blood to control the hematocrit depletes iron, producing microcytosis without anemia—an intentional iron-restricted state that curbs red-cell overproduction in polycythemia vera."
  - target: 01-human/07-system/cml
    relation: connects-to
    note: "PV and CML are both myeloproliferative neoplasms but molecularly opposite: PV is JAK2-driven with red-cell excess, CML is BCR-ABL-driven with granulocyte excess—testing for these mutations separates the chronic myeloid overproductions and picks the right targeted drug."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Polycythemia vera paradoxically depletes iron: the marrow's relentless red-cell overproduction—and the phlebotomy used to treat it—consume iron, so PV patients are typically iron-deficient with microcytic cells, and iron supplements can worsen the polycythemia."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Polycythemia vera overproduces platelets along with red cells: the JAK2 clone expands all myeloid lines, so thrombocytosis adds to the hyperviscosity, compounding the thrombotic risk that is the disease's main threat—mitigated by aspirin and cytoreduction."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Polycythemia vera is dangerous mainly through the cardiovascular system: too many red cells thicken the blood, so hyperviscosity and an activated clotting state cause heart attacks, strokes and clots—why keeping hematocrit below 45% is the central treatment goal."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Polycythemia vera classically clots the hepatic veins: the thick, hyperviscous, prothrombotic blood causes Budd-Chiari syndrome and other splanchnic-vein thromboses, so unexplained liver-vein clots should prompt JAK2 testing for an occult PV."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "PV causes aquagenic pruritus through mast cells: the clonal disease primes basophils and mast cells to release histamine, triggering the intense itching after warm water that is a classic and miserable symptom of polycythemia vera."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "JAK2 drives polycythemia vera by switching on STAT signaling: the V617F mutation makes JAK2 constitutively active, firing STAT3/STAT5 to push red-cell production without erythropoietin—the rationale for JAK inhibitors like ruxolitinib."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Polycythemia vera is too much hemoglobin: the JAK2-mutant marrow overproduces red cells, thickening the blood with hemoglobin until it sludges and clots, so treatment phlebotomizes patients to a target hematocrit to cut stroke and thrombosis risk."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Polycythemia vera itches through histamine: the disease expands mast cells and basophils whose histamine release causes the maddening itch after a warm shower (aquagenic pruritus), a hallmark symptom that antihistamines and JAK inhibitors target."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Polycythemia vera raises neutrophils too, not just red cells: as a panmyelosis it often drives leukocytosis, and a high neutrophil count is itself a predictor of the clots that are the disease's main danger."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Polycythemia vera endangers the brain with sludgy blood: too many red cells thicken the blood, slowing flow and raising the risk of stroke and cerebral vein clots, so lowering the red-cell count protects against these neurologic catastrophes."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Polycythemia vera causes a maddening water-triggered itch: contact with warm water releases mediators from the expanded mast-cell population, producing aquagenic pruritus—an unusual but characteristic clue to the disease."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "PV's high cell counts can fake high potassium: the swollen mass of cells leaks potassium after the blood sample clots, producing pseudohyperkalemia—a lab artifact to recognize before treating a number that isn't real in the body."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Polycythemia vera overworks and clots the heart: blood thickened with excess red cells raises the risk of heart attacks and strains cardiac pumping, a major driver of its mortality."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "PV shows in the eyes: hyperviscous blood engorges and slows the retinal veins, causing blurred vision and visual disturbances that can signal dangerously thick blood."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "PV primes the vessel lining to clot: sluggish hyperviscous blood and JAK2-mutant cells activate endothelial cells, tipping the balance toward the arterial and venous thromboses that define the disease."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Radioactive phosphorus tames PV with electrons: P-32 lodges in the marrow and showers it with beta particles — fast electrons — to throttle the runaway red-cell production, a once-standard therapy now kept for older patients who can't manage other drugs."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "The kidney both mimics and suffers PV: a tumor or cyst making excess erythropoietin must be excluded as a cause of high red cells, while PV's own urate overload from rapid cell turnover scars the kidney with gout-related nephropathy."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "PV's thick blood threatens the lungs: the hyperviscous, clot-prone circulation throws pulmonary emboli and raises pulmonary pressures, so breathlessness and chronic thromboembolic pulmonary hypertension can complicate the disease."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Sluggish, crowded blood torments the nerves: PV causes headache, dizziness, and visual blurring from hyperviscosity, plus the burning red hands and feet of erythromelalgia, where platelet plugs in small vessels inflame sensory neurons."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "The driver mutation is also the drug target: ruxolitinib, a JAK1/2 inhibitor, calms the overactive JAK-STAT signaling of PV, shrinking the spleen and easing symptoms in patients who can't tolerate or fail hydroxyurea."
  - target: 01-human/07-system/vhl-disease
    relation: connects-to
    note: "Other paths can also overfill the blood: where PV makes red cells with the EPO switch off, germline VHL defects (Chuvash polycythemia) stabilize HIF and drive EPO up — high versus low erythropoietin separating these causes of erythrocytosis."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Furious cell turnover spills minerals: the relentless birth and death of blood cells in PV, and their lysis under cytoreductive therapy, release phosphate and urate, the metabolic overflow that fuels the gout and hyperuricemia these patients suffer."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "PV is the great cause of Budd-Chiari: clots in the hepatic veins back blood up into the liver, congesting and killing hepatocytes, so an unexplained hepatic-vein thrombosis should always prompt a hunt for the JAK2 mutation."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Pregnancy magnifies PV's clotting danger: the thickened blood plus pregnancy's hypercoagulability raise the risk of miscarriage, placental thrombosis, and venous clots, managed with low-dose aspirin and careful control of the hematocrit."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "PV's clots strike the arteries too: the thickened blood and hyperactive platelets drive arterial thrombosis on top of atherosclerotic plaque, so heart attack and stroke — not just venous clots — are leading causes of death and the reason for aspirin and hematocrit control."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "When PV burns out it can turn marrow to bone: progression to post-polycythemic myelofibrosis brings osteosclerosis, where osteoblasts lay down excess bone that crowds out the very blood production the disease once drove into overdrive."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "JAK2 fans out beyond STAT: the V617F mutation fires not only JAK-STAT but the PI3K-AKT pathway, an extra survival and proliferation signal that helps the erythroid clone expand and a node targeted to complement JAK inhibition."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "The iron gate stays wide open: the ravenous erythropoiesis of PV releases erythroferrone that suppresses hepcidin, so the gut keeps absorbing iron to feed red-cell production — part of why the disease runs iron-deficient yet overproduces cells."
  - target: 01-human/03-molecular/tet2
    relation: connects-to
    note: "JAK2 rarely acts alone: co-occurring epigenetic mutations like TET2 shape PV's course, sometimes preceding the JAK2 hit and influencing how readily the clone progresses toward myelofibrosis or leukemia."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "The thickened blood strains the lungs' vessels: the hyperviscosity and clotting tendency of PV, along with megakaryocyte-driven remodeling, can raise pulmonary artery pressure, one of the circulatory complications of an overcrowded bloodstream."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "JAK2 inflames as it proliferates: the mutant clone drives NLRP3-inflammasome activation and IL-1β release, the chronic inflammation that fuels PV's thrombosis risk and constitutional symptoms beyond the raised cell counts."
  - target: 01-human/07-system/mds
    relation: connects-to
    note: "The clone can shift toward dysplasia: as it accumulates secondary mutations, polycythemia vera can transform into a myelodysplastic/MDS-like phase on the path to leukemia, especially after cytoreductive therapy."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "Overcrowded blood pushes the pressure up: the raised red-cell mass and viscosity of PV increase vascular resistance, contributing to hypertension that compounds the disease's cardiovascular and thrombotic risk."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "The cytokine that lets the mutant clone win: JAK2-V617F cells are resistant to TNF-α while normal progenitors are suppressed by it, so the high TNF-α of PV actively selects for the malignant clone — inflammation feeding the neoplasm."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Constitutive JAK2 signaling fires it up: the V617F mutation drives chronic NF-κB activation in PV, sustaining the inflammatory cytokine milieu that underlies symptoms, thrombosis risk and fibrotic progression."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "The polycythemia can flip to anemia: as PV exhausts into a spent, myelofibrotic phase, marrow fibrosis and chronic inflammation replace the red-cell excess with an anemia carrying a chronic-disease component."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Thick blood and clots overburden the heart: PV's hyperviscosity raises cardiac workload, and its arterial thromboses cause myocardial infarctions, both routes by which the disease can drive the heart toward failure."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Relentless itch and fatigue erode mood: the disabling aquagenic pruritus, chronic fatigue and lifelong thrombosis anxiety of PV substantially impair quality of life and contribute to depression."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Its cytoreductive drugs blunt immune defense: ruxolitinib and hydroxyurea used to control PV suppress immunity and predispose to opportunistic and reactivated infections that can escalate to sepsis."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "JAK inhibition reawakens shingles: ruxolitinib used for polycythemia vera dampens T-cell immunity and characteristically reactivates latent varicella-zoster, a recognised risk during therapy."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Deep immune suppression opens the lung to mould: ruxolitinib for advanced PV, with disease-related immune dysfunction, can permit invasive aspergillosis and other opportunistic fungal infection."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Lifelong clot-and-transformation risk breeds worry: the constant threat of thrombosis and progression to myelofibrosis or leukaemia in PV, plus relentless itch and fatigue, fosters chronic health anxiety."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Excess red cells torment the skin: polycythemia vera causes the intense aquagenic pruritus after warm water, the burning red erythromelalgia of the extremities and a ruddy, plethoric complexion."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It clots the gut's veins and swells the spleen: PV is a leading cause of splanchnic, portal and hepatic vein thrombosis (Budd-Chiari), enlarges the spleen and, via raised histamine, causes peptic ulcers."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Hyperviscosity disturbs the brain: the thickened blood of PV causes headaches, dizziness, visual disturbance and transient ischaemic attacks, and cerebral vein thrombosis can occur."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It swells the spleen: extramedullary haematopoiesis and pooling of the expanded red-cell mass enlarge the spleen in polycythaemia vera, often markedly, with risk of infarction."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Lung disease must be ruled out: chronic hypoxic lung disease causes secondary polycythaemia, the key differential that a true diagnosis of polycythaemia vera must exclude."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It makes red cells without the hormone: polycythaemia vera is an erythropoietin-independent, autonomous erythrocytosis, so a low EPO level distinguishes it from EPO-driven secondary polycythaemia."
  - target: 03-medicine/01-modern/04-cardio/aspirin
    relation: connects-to
    note: "Low-dose aspirin is standard: it reduces the arterial and microvascular thrombosis that dominates polycythaemia vera, alongside venesection and cytoreduction."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "High cell turnover and marrow disease reach bone: PV raises uric acid causing gout, the expanded marrow brings bone discomfort, and progression to myelofibrosis adds skeletal symptoms."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Thick blood and urate strain the kidney: hyperviscosity and hyperuricaemia impair renal function, and PV is a classic cause of renal vein and Budd-Chiari thrombosis."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "JAK inhibition for refractory disease: ruxolitinib blocks the JAK2 V617F-driven JAK-STAT signalling of polycythaemia vera, controlling the red-cell count and spleen in those who fail or cannot tolerate hydroxyurea."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Hydroxyurea cytoreduces the marrow: this oral chemotherapy lowers the red-cell mass in higher-risk polycythaemia vera, used with phlebotomy and low-dose aspirin to prevent the thrombosis that drives most PV deaths."
  - target: 02-pathogen/02-bacteria/mycobacterium-tuberculosis
    relation: connects-to
    note: "Its JAK inhibitor reawakens infection: ruxolitinib used in PV suppresses immunity enough to reactivate tuberculosis and other opportunists, so latent TB should be screened before and during therapy."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "Its chief danger is the clot: hyperviscosity and JAK2-mutant blood cells inflame and adhere to the arterial wall, driving the strokes and heart attacks that are the leading cause of death in polycythaemia vera."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Where its clots and overflow land: polycythaemia vera's JAK2-mutant clone thromboses the hepatic and portal veins and can seed extramedullary haematopoiesis in the hepatic lobules, so liver enlargement and splanchnic thrombosis both flag the disease."
  - target: 01-human/07-system/copd
    relation: connects-to
    note: "Primary versus secondary thick blood: polycythaemia vera makes too many red cells autonomously through JAK2, whereas COPD's chronic hypoxia raises erythropoietin to cause a secondary erythrocytosis—the key distinction when haematocrit is high."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Arterial thrombosis and MI: PV's raised red-cell mass causes hyperviscosity and arterial thrombosis including myocardial infarction, the leading cardiovascular cause of death in the disease."
  - target: 01-human/07-system/antiphospholipid-syndrome
    relation: connects-to
    note: "Two causes of unusual-site thrombosis: PV—the leading cause of Budd-Chiari—and antiphospholipid syndrome both cause arterial and splanchnic or cerebral venous thrombosis, key differentials in a young patient with a clot."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Erythromelalgia and itch: PV's platelet excess causes erythromelalgia—burning, red, painful extremities from microvascular sensory-nerve involvement—dramatically relieved by low-dose aspirin."
  - target: 01-human/03-molecular/von-willebrand-factor
    relation: connects-to
    note: "Bleeding from too many cells: very high blood counts in polycythaemia vera adsorb and clear high-molecular-weight von Willebrand multimers, causing an acquired von Willebrand syndrome and a paradoxical bleeding risk."
  - target: 01-human/07-system/hcc
    relation: connects-to
    note: "Secondary polycythaemia mimic: EPO-secreting tumours such as hepatocellular carcinoma (and renal cancer) cause a paraneoplastic erythrocytosis that must be distinguished from primary, JAK2-driven polycythaemia vera."
  - target: 01-human/07-system/pheochromocytoma-paraganglioma
    relation: connects-to
    note: "The HIF connection: EPAS1 (HIF-2alpha) gain-of-function links polycythaemia with paraganglioma in the Pacak-Zhuang syndrome, the same hypoxia-sensing pathway that JAK2 amplifies in polycythaemia vera."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Clone-reducing therapy: pegylated interferon-alpha is a disease-modifying treatment for polycythaemia vera that can lower the JAK2-mutant allele burden and induce molecular responses."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Oxygen-sensing axis: HIF/oxygen-sensing signalling underlies erythrocytosis, and HIF2A, PHD2 and VHL defects cause polycythaemia-vera-like erythrocytosis distinct from JAK2-driven disease."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Epigenetic progression: EZH2 and other epigenetic-regulator mutations accumulate in polycythaemia vera and contribute to its progression toward myelofibrosis and leukaemia."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Clonal inflammation: IL-6 from the JAK2-mutant clone fuels the chronic inflammation of polycythaemia vera, contributing to its symptoms and thrombotic risk."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Inflammatory marrow: IL-1β secreted by the mutant clone damages the bone-marrow niche, promoting the clonal advantage and progression of polycythaemia vera."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Marrow angiogenesis: elevated VEGF increases bone-marrow microvessel density in polycythaemia vera, part of the proliferative MPN microenvironment."
  - target: 01-human/03-molecular/pf4
    relation: connects-to
    note: "Thrombotic risk: the expanded, hyperreactive platelets of polycythaemia vera release platelet factor 4 on activation, contributing to the arterial and venous thrombosis that is the leading cause of morbidity in the disease."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "High cell turnover: the massive haematopoietic turnover of polycythaemia vera floods purine catabolism through xanthine oxidase, raising urate and causing the secondary hyperuricaemia and gout that complicate the MPN."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Fibrotic progression: PDGF released by the clonal megakaryocytes stimulates marrow fibroblasts, driving the reticulin fibrosis of post-polycythaemia-vera myelofibrosis as the disease evolves."
  - target: 01-human/03-molecular/calr
    relation: connects-to
    note: "MPN driver landscape: polycythaemia vera is almost universally JAK2-driven, which distinguishes it from the CALR- and MPL-mutant essential thrombocythaemia and primary myelofibrosis — the three classic Philadelphia-negative myeloproliferative neoplasms defined by their driver."
  - target: 01-human/03-molecular/thrombin
    relation: connects-to
    note: "Thrombotic risk: the raised red-cell mass and activated platelets of PV promote thrombin generation and hyperviscosity, making arterial and venous thrombosis — including Budd-Chiari and splanchnic-vein clots — the leading cause of death, the rationale for phlebotomy and aspirin."
  - target: 01-human/03-molecular/sf3b1
    relation: connects-to
    note: "Progression-predicting comutations: spliceosome mutations such as SF3B1, acquired alongside the JAK2 driver, mark the higher-risk PV that is more likely to transform into myelofibrosis or acute myeloid leukaemia."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "MAPK arm: JAK2 V617F signals not only through STAT5 but the RAS-ERK MAPK pathway, broadening the cytokine-independent proliferation of polycythemia vera and a reason JAK inhibition alone fails to eradicate the clone."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "Clonal-hematopoiesis comutation: epigenetic-regulator mutations in DNMT3A, acquired with the TET2 already mapped here, can precede or accompany the JAK2 driver and shape the clonal evolution and progression risk of polycythemia vera."
  - target: 01-human/03-molecular/ferroportin
    relation: connects-to
    note: "Iron supply: the high erythropoietic drive of PV suppresses hepcidin, leaving ferroportin active to feed iron into red-cell production; hepcidin-mimetics (rusfertide) exploit this by degrading ferroportin to starve the clone of iron and control erythrocytosis."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K limb: constitutive JAK2 signalling (mapped) engages PI3K (AKT already mapped) as a parallel effector pathway supporting the erythroid expansion of polycythemia vera."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Growth axis: mTOR completes the PI3K-AKT-mTOR pathway (AKT already mapped) downstream of JAK2, and mTOR inhibition has been explored to control the clone in polycythemia vera."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "Leukaemic transformation: TP53 inactivation drives the progression of polycythemia vera to post-PV myelofibrosis and acute myeloid leukaemia."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Inflammatory milieu: TLR-MyD88-NF-κB innate signalling (NF-κB already mapped) sustains the chronic inflammatory milieu that drives symptoms and clonal progression in polycythemia vera."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "Transformation lesion: CDKN2A loss is among the cooperating lesions in the leukaemic transformation of polycythemia vera to acute myeloid leukaemia."
  - target: 01-human/03-molecular/runx1
    relation: connects-to
    note: "Leukaemic progression: acquired RUNX1 mutations mark the transformation of polycythemia vera to secondary acute myeloid leukaemia."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "Type-I-interferon signalling through STAT1 (type-I-interferon mapped) underlies the disease-modifying activity of ropeginterferon in polycythemia vera."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 expressed by megakaryocytes contributes to the marrow microenvironment and the fibrotic potential of polycythemia vera."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN restraint of PI3K-AKT-mTOR signalling (AKT, PIK3CA and mTOR mapped) downstream of JAK2-driven activation shapes the clonal proliferation of polycythemia vera."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING amplifies the chronic inflammatory marrow milieu (type-I interferon already mapped) of polycythemia vera."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β already mapped) drives the marrow fibrosis underlying the progression of polycythemia vera toward post-PV myelofibrosis."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6-cyclin-D activity (CDKN2A already mapped) drives the JAK2-fuelled erythroid and myeloid cell-cycle progression of polycythemia vera."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "JAK2-STAT5-PI3K-AKT signaling (AKT already mapped) inactivates FOXO, supporting the survival of the clonal erythroid progenitors of polycythemia vera."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β misregulation contributes to the aberrant hematopoietic stem-cell self-renewal of polycythemia vera."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins reflect the inflammatory myeloid activation of polycythemia vera."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family and LYN kinase signaling cooperates with JAK2-STAT to support the survival of the clonal erythroid cells of polycythemia vera."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-p53 signaling (p53 already mapped) participates in the clonal survival and leukemic-evolution risk of polycythemia vera."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated cytotoxic immunosurveillance targets the neoantigen-bearing JAK2-mutant clone of polycythemia vera."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of the clonal hematopoietic cells of polycythemia vera."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the survival of the JAK2-mutant clone of polycythemia vera."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-family chemokine signaling participates in the aberrant myeloid trafficking and inflammatory niche of polycythemia vera."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the bone-marrow-niche and megakaryocyte interactions of polycythemia vera."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic dysregulation of polycythemia vera."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the inflammatory bone-marrow microenvironment of polycythemia vera."
  - target: 01-human/03-molecular/egln1
    relation: connects-to
    note: "Erythrocytosis differential: loss-of-function EGLN1/PHD2 stabilises HIF to cause hereditary erythrocytosis, the germline oxygen-sensing counterpart to JAK2-driven polycythaemia vera (HIF/EPAS1 already mapped), a key distinction in the erythrocytosis workup."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Iron-restricted erythropoiesis: the expanded red-cell production of polycythaemia vera consumes iron and repeated phlebotomy induces deficiency, so transferrin-bound iron delivery becomes rate-limiting, the physiologic rationale behind therapeutic iron restriction."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Hyperviscosity thrombosis: the raised haematocrit of polycythaemia vera increases blood viscosity and shear, impairing endothelial nitric-oxide bioavailability and promoting the arterial and venous thrombosis that is the leading cause of death."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Arterial thrombosis: polycythaemia vera markedly raises the risk of arterial events including myocardial infarction and stroke (nitric oxide already mapped), and troponin elevation marks the cardiac injury of these thromboses."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Platelet-mediated microvascular events: platelets are the body's main serotonin store, released on aggregation to constrict vessels, so the excess and activated platelets of polycythaemia vera contribute to the erythromelalgia and microvascular symptoms it causes."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Endothelial vasoconstriction: the hyperviscous, inflamed circulation of polycythaemia vera favours endothelin-1-driven vasoconstriction over nitric-oxide vasodilation (already mapped), tipping the vascular balance further toward its characteristic thrombosis."
  - target: 01-human/03-molecular/adamts13
    relation: connects-to
    note: "Acquired von Willebrand syndrome: when polycythaemia vera raises platelet counts markedly, the high-molecular-weight von Willebrand multimers (already mapped) are cleared, and this acquired von Willebrand syndrome causes the bleeding that can coexist with the thrombosis."
  - target: 01-human/03-molecular/protein-c
    relation: connects-to
    note: "Prothrombotic tilt: the thrombosis of polycythaemia vera reflects a shift toward coagulation, and reduced activity of the natural anticoagulant protein C (thrombin already mapped) adds to the risk that drives phlebotomy, aspirin and cytoreduction."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Inflammatory milieu: polycythaemia vera carries a chronic inflammatory state, and the anti-inflammatory IL-10 counterbalances the TNF, IL-6 and IL-1 (already mapped) driven by JAK2-STAT signalling that shapes its symptoms and progression."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Thromboxane and platelets: activated platelets (PF4 and serotonin already mapped) generate thromboxane A2 to amplify aggregation, the eicosanoid pathway blocked by the low-dose aspirin used to reduce thrombosis in polycythaemia vera."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Endothelial activation: the angiopoietin-Tie2 axis reflects the endothelial activation of the prothrombotic state of polycythaemia vera, part of the endothelium's contribution (von Willebrand factor already mapped) to its thrombosis."
  - target: 01-human/03-molecular/fibrinogen
    relation: connects-to
    note: "Hyperviscosity and coagulation: the raised haematocrit (haemoglobin already mapped) and fibrinogen increase blood viscosity and coagulation (thrombin already mapped), compounding the thrombotic risk that drives phlebotomy in polycythaemia vera."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Inflammatory milieu: IL-4 and the M2 macrophage arm (IL-10 already mapped) shape the chronic inflammation (IL-6 and TNF already mapped) of the myeloproliferative marrow, part of the disease biology of polycythaemia vera."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Marrow adipose crosstalk: the marrow adipocytes and their adipokine leptin signal to the clonal erythroid cells, part of the bone-marrow (already mapped) microenvironment of polycythaemia vera."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Adipokine microenvironment: adiponectin, with leptin (already mapped), from the marrow adipose tissue signals to the myeloproliferative clone, part of the metabolic microenvironment of polycythaemia vera."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "M2 inflammatory arm: IL-13, with IL-4 (already mapped), drives the M2 macrophage arm of the inflammatory (IL-6 and TNF already mapped) microenvironment of the polycythaemia vera marrow."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Marrow-adipocyte adipokine: resistin, with leptin and adiponectin (already mapped), is the marrow-adipocyte adipokine of the metabolic microenvironment of polycythaemia vera."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Erythroblastic-island macrophages: the marrow macrophages (M2, IL-4 and IL-13 already mapped) support the erythropoiesis of the erythroblastic islands and recycle the iron (ferroportin already mapped) of polycythaemia vera."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Clonal immunosurveillance: the cytotoxic T cells (perforin already mapped) provide the immune surveillance of the JAK2 (already mapped)-mutant clone, augmented by the interferon (type-I interferon already mapped) therapy of polycythaemia vera."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 arm: the IFN-γ of the T cells (with the type-I interferon already mapped) is the type-II interferon arm of the anti-clonal immunity and the inflammatory milieu of polycythaemia vera."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) response of the anti-clonal immunity of polycythaemia vera."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the inflammatory milieu of polycythaemia vera."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the chronic inflammatory milieu of polycythaemia vera."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2/pruritus arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped) and the histamine (already mapped), reflects the type-2 dimension of the aquagenic pruritus and inflammatory milieu of polycythaemia vera."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Antigen presentation: the dendritic cells present antigen to the T cells (already mapped) within the chronic inflammatory clonal-haematopoiesis milieu of polycythaemia vera."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Thromboinflammation: the complement C5 and the terminal MAC contribute to the complement-driven thromboinflammation and the elevated thrombotic risk of polycythaemia vera."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the C5 already mapped) links the complement to the neutrophil and platelet (already mapped) activation of the thrombotic milieu of polycythaemia vera."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Central complement: the complement C3, upstream of the C5 and C5aR1 (already mapped), is the pivot of the complement-driven thromboinflammation of polycythaemia vera."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) whose dysregulation amplifies the thromboinflammation of polycythaemia vera."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Innate surveillance: the NK cells (perforin already mapped) are part of the immune surveillance against the JAK2-mutant (already mapped) clone of polycythaemia vera."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Marrow alarmin: TSLP released by bone marrow stromal cells activates mast cells and dendritic cells, promoting the inflammatory myeloproliferative niche that sustains the JAK2-mutant clone of polycythaemia vera."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Thrombotic kinin: bradykinin from the kallikrein-kinin system is amplified by the polycythaemia-vera-associated erythrocytosis and thrombosis (JAK2 already mapped), promoting the vasodilatory response to the hypercoagulable state."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical-pathway brake: C1-esterase inhibitor modulates the classical complement pathway (complement C3, C5 and C5aR1 already mapped) that contributes to the thromboinflammatory state of polycythaemia vera."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Marrow fibrosis ECM: periostin, a TGF-β-induced ECM component, contributes to the marrow fibrosis (TGF-β already mapped) in polycythaemia vera progression toward myelofibrosis (already mapped), reinforcing the desmoplastic niche of the JAK2-mutant clone."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian erythropoiesis modulator: melatonin regulates the circadian rhythm of erythropoiesis (EPO already mapped) and platelet (already mapped) production, with circadian disruption amplifying the JAK2-mutant erythrocytosis and thrombotic risk of polycythaemia vera."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "JAK2 cross-activation: prolactin signals through the JAK2 (already mapped) receptor, directly intersecting the pathogenic JAK2-V617F hyperactivation; prolactin also stimulates erythropoiesis (EPO already mapped), amplifying the clonal erythrocytosis of polycythaemia vera."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "PV androgen axis: testosterone via androgen receptor modulates erythropoiesis and iron metabolism (transferrin already mapped); the male sex predominance of polycythaemia vera reflects androgen-driven amplification of the JAK2-V617F (already mapped) erythroid clone."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "PV oxytocin: oxytocin via OXTR on megakaryocytes (platelet already mapped) and bone-marrow (already mapped) progenitors modulates platelet production and thrombopoiesis, intersecting the JAK2 (already mapped)-driven thrombocytosis of polycythaemia vera."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "PV vasopressin: vasopressin via V2R on collecting-duct cells (kidney already mapped) and megakaryocytes (platelet already mapped) modulates blood viscosity and platelet activation, amplifying the thrombotic risk of the erythrocytosis of polycythaemia vera."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "PV selenium: selenium-dependent glutathione peroxidase (GPX) quenches reactive-oxygen-species generated by JAK2-V617F (already mapped) hyperactivated erythroid cells in polycythaemia vera, reducing oxidative DNA damage and the clonal erythrocytosis."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "PV iodine: iodine-dependent thyroid hormones modulate erythropoiesis (EPO already mapped) and bone-marrow (already mapped) progenitor proliferation; hypothyroidism blunts and hyperthyroidism amplifies JAK2 (already mapped)-driven erythrocytosis in polycythaemia vera."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "PV sodium: sodium homeostasis via RAAS (aldosterone already mapped) and vasopressin (already mapped) is disrupted by the erythrocytosis-driven hyperviscosity of polycythaemia vera, contributing to hypertension and the cardiovascular thrombotic risk."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "PV magnesium: magnesium, as ATP cofactor in erythrocytes (already mapped) and platelets (already mapped), supports JAK2 (already mapped) kinase fidelity; magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of polycythaemia vera."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "PV copper: copper, as ceruloplasmin cofactor in hepatocytes (already mapped) and neutrophils (already mapped), supports iron (already mapped) recycling; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) haematopoietic cascade of polycythaemia vera."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "PV calcium: calcium, as second-messenger in JAK2 (already mapped)-activated erythroid progenitors and platelets (already mapped), modulates thrombopoiesis; calcium dysregulation amplifies IL-6 (already mapped) and NF-κB (already mapped) thrombotic risk of PV."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "PV zinc: zinc, as metalloproteinase cofactor in neutrophils (already mapped) and platelets (already mapped), modulates thrombo-inflammatory remodelling; zinc deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) haematopoietic cascade of polycythaemia vera."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "PV chloride: chloride, via erythrocyte (already mapped) anion exchangers, maintains CO₂ transport and osmotic balance; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) haematological cascade of polycythaemia vera."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "PV sulfur: sulfur, as component of glutathione in erythrocytes (already mapped) and neutrophils (already mapped), limits oxidative haemolysis; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) haematopoietic inflammatory cascade of polycythaemia vera."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "PV carbon: carbon as backbone of JAK2 and NF-κB (already mapped) proteins in erythrocytes (already mapped) and neutrophils (already mapped) sustains myeloproliferative signalling; carbon depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of PV."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "PV hydrogen: hydrogen, via redox homeostasis in erythrocytes (already mapped) and macrophages (already mapped), supports haemoglobin function; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) oxidative cascade of polycythaemia vera."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "PV nitrogen: nitrogen in amino-acid scaffold of JAK2 and erythropoietin (already mapped) proteins in erythrocytes (already mapped) sustains erythropoietic signalling; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of PV."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "PV PD-1: PD-1 on T-cells (already mapped) and macrophages (already mapped) in bone marrow (already mapped) modulates immune surveillance of JAK2-mutant clones; PD-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) erythroid expansion cascade of PV."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "PV GLP-1: GLP-1 receptor signalling in macrophages (already mapped) and platelets (already mapped) modulates thrombotic and metabolic risk in PV; GLP-1 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and erythropoietin (already mapped) cascade of PV."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "PV angiotensin-II: angiotensin-II in bone marrow vasculature promotes erythroid progenitor expansion; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and erythropoietin (already mapped) erythrocytosis cascade of polycythemia vera."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "PV wnt-beta-catenin: WNT/β-catenin on stem cells (already mapped) and macrophages (already mapped) drives erythroid expansion; wnt-beta-catenin loss amplifies nf-kb (already mapped) and il-6 (already mapped) and erythropoietin (already mapped) erythrocytosis cascade of PV."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "PV rankl: RANKL from macrophages (already mapped) and fibroblasts (already mapped) modulates myeloproliferative bone marrow niche; rankl excess amplifies nf-kb (already mapped) and il-6 (already mapped) and erythropoietin (already mapped) erythrocytosis cascade of PV."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "PV il-2: IL-2 from T-cells (already mapped) and macrophages (already mapped) regulates PV immune surveillance; il-2 dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and erythropoietin (already mapped) erythrocytosis cascade of PV."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "PV fibronectin: fibronectin in macrophages (already mapped) and erythroid progenitors (already mapped) promotes marrow ECM remodelling in PV; fibronectin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of polycythemia vera."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "PV notch: Notch signalling in macrophages (already mapped) and erythroid progenitors (already mapped) regulates haematopoietic cell fate in PV; notch dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of polycythemia vera."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "PV igf-1: IGF-1 from macrophages (already mapped) and erythroid progenitors (already mapped) promotes haematopoietic cell survival in PV; igf-1 dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of polycythemia vera."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "PV activin-a: activin-A from macrophages (already mapped) and erythroid progenitors (already mapped) modulates haematopoietic inflammatory tone; activin-a excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of polycythemia vera."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "PV cgrp: CGRP from macrophages (already mapped) and erythroid progenitors (already mapped) modulates haematopoietic neuroimmune tone; cgrp excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of polycythemia vera."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "PV calcitonin: calcitonin from macrophages (already mapped) and erythroid progenitors (already mapped) modulates calcium balance in PV; calcitonin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of polycythemia vera."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "PV substance-p: substance-P from macrophages (already mapped) and erythroid progenitors (already mapped) modulates haematopoietic neuroimmune tone; substance-p excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of PV."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "PV insulin-receptor: insulin receptor on macrophages (already mapped) and erythroid progenitors (already mapped) drives haematopoietic metabolic repair; insulin-receptor loss amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of PV."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "PV aldosterone: aldosterone from macrophages (already mapped) and erythroid progenitors (already mapped) modulates haematopoietic ion balance; aldosterone excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of PV."
---

# Polycythemia Vera

## Overview

**Polycythemia vera (PV)** is a BCR-ABL1-negative **myeloproliferative neoplasm (MPN)** characterized by clonal expansion of a hematopoietic stem cell driven by **JAK2 gain-of-function mutations** in virtually all cases (~99% JAK2 V617F; ~1% JAK2 exon 12 mutations). PV presents with absolute erythrocytosis (elevated red cell mass), variable thrombocytosis and leukocytosis, splenomegaly, and the pathognomonic symptom of **aquagenic pruritus**. The principal clinical risks are thrombosis (arterial and venous), bleeding, and long-term transformation to post-PV myelofibrosis (PPV-MF, ~10-15% at 10 years) or acute myeloid leukemia (AML, ~2-5% at 10 years). Treatment is risk-stratified: all patients receive phlebotomy (target Hematocrit <45%) and low-dose aspirin; high-risk patients (age ≥60 or prior thrombosis) additionally receive cytoreductive therapy with **hydroxyurea** (first-line) or **ropeginterferon alfa-2b** (Besremi, FDA approved 2021) — PROUD-PV/CONTINUATION-PV showed superior molecular response for ropeginterferon at 36 months [^gisslinger-2020-proud-pv]. **Ruxolitinib** (JAK1/2 inhibitor, Jakafi) is approved for hydroxyurea-resistant/intolerant PV — RESPONSE trial: Hct control 21% vs 1%, spleen volume reduction ≥35% 38% vs 1% [^vannucchi-2015-response].

**Epidemiology:**
- Incidence: ~2-3 per 100,000/year; prevalence ~22 per 100,000
- Median age at diagnosis: ~60 years; rare in patients <40 years
- Male predominance (male:female ~2:1)
- Median overall survival: 14-19 years from diagnosis with modern treatment; shortened by thrombotic events and transformation

## Structure

### WHO 2022 diagnostic criteria

**Major criteria:**
1. Hemoglobin >16.5 g/dL (men) or >16.0 g/dL (women), OR Hematocrit >49% (men) or >48% (women), OR elevated red cell mass (>25% above predicted)
2. Bone marrow biopsy: hypercellularity for age with trilineage growth (panmyelosis) — prominent erythroid, granulocytic, and megakaryocytic proliferation; megakaryocytes are pleomorphic (large and small, hyperlobated and hypolobated nuclei)
3. Presence of JAK2 V617F or JAK2 exon 12 mutation

**Minor criterion:**
4. Subnormal serum erythropoietin level (EPO below normal reference range)

**Diagnosis:** All three major criteria, OR first two major + minor criterion.

*Note: Bone marrow biopsy is required except if Hgb >18.5 g/dL (men)/16.5 g/dL (women) with JAK2 mutation and subnormal EPO.*

### Molecular landscape

**JAK2 V617F (Val617Phe, ~98-99%):**
Exon 14 point mutation in the JH2 pseudokinase (regulatory) domain; normally JH2 auto-inhibits JH1 kinase; V617F disrupts JH2 auto-inhibition → constitutive JAK2 kinase activity → STAT5/STAT3 phosphorylation → proliferative and anti-apoptotic gene programs → erythroid, megakaryocytic, and granulocytic expansion independent of cytokine ligands. Homozygous JAK2 V617F (~25% of PV cases, via mitotic recombination) correlates with higher allele burden, more erythrocytosis, more frequent aquagenic pruritus, and higher MF transformation risk.

**JAK2 exon 12 mutations (~1-2%):**
In-frame deletions/insertions in exon 12 of JAK2 → isolated erythrocytosis (predominantly erythroid phenotype, unlike V617F which causes panhyperplasia); subnormal EPO; JAK2 V617F negative; require exon 12 sequencing; clinically similar prognosis to JAK2 V617F PV.

**Co-mutations:**
Additional somatic mutations in ~30-50% PV at diagnosis: TET2 (most common, ~16%), DNMT3A (~7%), ASXL1 (~5%), SRSF2 (~4%), IDH2 (<5%); ASXL1/SRSF2/IDH1/2/EZH2 co-mutations → increased MF and AML transformation risk; molecular profiling (NGS) increasingly used to assess transformation risk.

**JAK2 allele burden (VAF):**
JAK2 V617F variant allele frequency (VAF): PV typically VAF 25-100% (compared to ET typically VAF 1-50%); higher allele burden in PV → more symptomatic disease; cytoreductive therapy (interferon, ruxolitinib) lowers VAF; complete molecular response (CMR, VAF <1%) achievable with sustained ropeginterferon therapy; CMR correlates with reduced clonal burden and possibly reduced transformation risk.

## Function

### JAK2-driven pathophysiology

**EPO-independent erythropoiesis:**
JAK2 V617F → constitutive EPOR/JAK2/STAT5 signaling → erythroid progenitors (BFU-E, CFU-E) proliferate without EPO → endogenous erythroid colony (EEC) formation in semi-solid media without added EPO — a diagnostic functional assay. Elevated red cell mass → increased blood viscosity → sludging → thrombosis risk; phlebotomy reduces Hct to target <45% → reduces thrombotic risk by ~45% (CYTO-PV trial).

**Thromboembolic risk:**
Both arterial (MI, stroke) and venous (DVT, PE, splanchnic vein thrombosis — Budd-Chiari, portal vein) events occur at high rates. JAK2 V617F platelets are activated; JAK2 V617F neutrophils release NETs (neutrophil extracellular traps) → endothelial activation → thrombosis. Splanchnic vein thrombosis (Budd-Chiari syndrome, portal vein thrombosis) in young women → screen for JAK2 V617F as PV may be the underlying diagnosis. Low-dose aspirin (100 mg/day) reduces thrombosis risk in PV (ECLAP trial: RR 0.41, p=0.02).

**Aquagenic pruritus:**
~40-65% of PV patients; generalized pruritus triggered by water contact (bathing, shower) regardless of temperature; pathophysiology: JAK2 V617F → mast cell JAK2 activation → histamine release + prostaglandin production → cutaneous pruritic stimuli; treatment: antihistamines (limited efficacy), aspirin, SSRIs (paroxetine effective), JAK inhibitors (ruxolitinib highly effective for pruritus).

**Splenomegaly:**
~70% at diagnosis; caused by extramedullary hematopoiesis; correlates with disease burden; ruxolitinib reduces spleen volume; symptomatic splenomegaly → early satiety, pain; massive splenomegaly → concerns for splenic infarct or rupture.

## Pathology

### Risk stratification

**Low-risk PV:** Age <60 years AND no prior thrombosis
- Treatment: Phlebotomy (Hct <45%) + low-dose aspirin 81-100 mg/day

**High-risk PV:** Age ≥60 years OR prior thrombosis (either arterial or venous)
- Treatment: Phlebotomy + aspirin + cytoreductive therapy

**Very high-risk features (no formal WHO category):** Extreme leukocytosis (WBC >15 × 10⁹/L), extreme thrombocytosis (platelet >1,500 × 10⁹/L — paradoxically ↑ bleeding from acquired von Willebrand syndrome), prior major bleeding; consider cytoreduction in low-risk patients with these features.

### Treatment

**Phlebotomy:**
Target Hct <45% in all patients (CYTO-PV: Hct <45% → 38% reduction in cardiovascular death/major thrombosis vs <50%); 1 unit (~450 mL) removed per session; iron deficiency induced by phlebotomy is intentional and not supplemented (limits erythropoiesis); frequency: initially weekly, then as needed to maintain Hct <45%; iron-deficiency symptoms may require iron supplementation titration.

**Low-dose aspirin:**
81-100 mg/day in all PV patients without contraindications; reduces major thrombosis (arterial events especially); caution at very high platelet counts (>1,500 × 10⁹/L) due to acquired von Willebrand syndrome → risk of bleeding; discontinue or adjust dose if platelet count >1,500 × 10⁹/L.

**Hydroxyurea (first-line cytoreduction):**
Ribonucleotide reductase inhibitor → reduces all cell lines; Hct control within weeks; dose: 500-2,000 mg/day orally; monitoring: CBC every 3-4 months; resistance criteria (ELN 2009): need phlebotomy despite ≥2 g/day HU; platelet >400 × 10⁹/L or WBC >10 × 10⁹/L at ≥2 g/day; toxicities: myelosuppression, skin ulcers (particularly leg ulcers), oral mucositis; long-term: HU slightly increases AML risk in some series (confounded by disease progression).

**Ropeginterferon alfa-2b (Besremi, FDA approved 2021):**
Mono-PEGylated IFN-α2b administered every 2 weeks subcutaneously; mechanism: suppresses JAK2-mutant clone via STAT1/2 upregulation → anti-proliferative → preferential elimination of JAK2 V617F HSCs; PROUD-PV (Phase 3, non-inferiority vs HU): similar control arm response at 12 months (non-inferior), superior molecular response (JAK2 allele burden reduction ≥50%: 61% vs 21% at 36 months in CONTINUATION-PV extension) [^gisslinger-2020-proud-pv]; PROUD-PV-2 randomized vs HU in low-risk PV (less common use); adverse effects: flu-like symptoms, fatigue, autoimmune thyroiditis, depression, neuropsychiatric effects; suitable for women of childbearing potential (preferred over HU in pregnancy considerations); achieves CMR (JAK2 VAF <1%) in ~15-20% with sustained therapy.

**Ruxolitinib (Jakafi, FDA approved 2014 for HU-resistant/intolerant PV):**
JAK1/JAK2 inhibitor; RESPONSE trial (Phase 3, N=222): ruxolitinib vs best available therapy (BAT); primary endpoint: Hct control without phlebotomy at week 32 + spleen volume reduction ≥35% → 21% vs 1% (p<0.001); secondary: Hct control 60% vs 20%; pruritus resolution ~51% vs ~5%; complete hematologic response 24% vs 9% [^vannucchi-2015-response]; dose: 10 mg BID (starting); adverse effects: anemia, thrombocytopenia, weight gain, herpes zoster reactivation (prophylaxis with valacyclovir), increased infection risk; does NOT achieve molecular remission as effectively as interferon; approved for HU-resistant/intolerant PV.

**Busulfan (third-line):**
Alkylating agent; used for elderly HU-intolerant patients; short courses (0.1 mg/kg/day × weeks) achieve prolonged remission; myelosuppressive; mutagenic potential limits use.

**Investigational agents:**
- Ropeginterferon combinations with ruxolitinib: Phase 2 trials
- Rusfertide (PTG-300, hepcidin mimetic): Phase 2/3 — reduces phlebotomy frequency by raising serum iron threshold; normalizes iron without phlebotomy burden
- Navitoclax (BCL-2/BCL-XL inhibitor): Phase 2 in combination with ruxolitinib
- Idasanutlin (MDM2 inhibitor): Phase 2 for MDM2-expressing PV

### MF/AML transformation

**Post-PV myelofibrosis (PPV-MF):**
~10-15% at 10 years; ~20-25% at 15 years; defined by WHO criteria: development of reticulin/collagen fibrosis + anemia requiring transfusion or cytoreduction discontinuation + splenomegaly + leukoerythroblastic blood film; treatment: ruxolitinib (most effective), fedratinib, pacritinib; allo-SCT is the only curative option for eligible patients; median OS after PPV-MF ~4-5 years.

**AML transformation:**
~2-5% at 10 years; higher risk with ASXL1/SRSF2/EZH2/IDH1-2 co-mutations; cytogenetic abnormalities frequent at transformation (del17p, +8, +9, complex); PV-associated AML is highly chemotherapy-resistant (>80% fail to achieve CR); allo-SCT after achieving blast control with azacitidine+venetoclax if eligible; prognosis poor (median OS <12 months).

**Monitoring:**
- CBC every 3-6 months; JAK2 VAF annually (molecular monitoring)
- BM biopsy if peripheral blood suggests MF (leukoerythroblastic picture, rising LDH, new splenomegaly, cytopenia)
- NGS panel at diagnosis; repeat at transformation
- Screen for VTE, cardiovascular events at each visit

### Secondary polycythemia — differential diagnosis

PV must be distinguished from secondary erythrocytosis (elevated EPO, JAK2 wild-type):
- **Hypoxia-driven:** Sleep apnea, COPD, cyanotic heart disease, high-altitude residence → elevated EPO → erythrocytosis
- **EPO-producing tumors:** RCC, HCC, uterine fibroid, cerebellar hemangioblastoma → elevated EPO
- **VHL disease/Chuvash polycythemia:** EPAS1 or VHL mutations → HIF-2α constitutive → EPO excess → erythrocytosis with low-normal EPO (partial VHL function loss allows some degradation)
- **EPAS1 GOF/PHD2 mutations:** Hereditary erythrocytosis; subnormal EPO, JAK2 negative, family history
- **Relative (spurious) polycythemia:** Dehydration, diuretics → plasma volume contraction → hemoconcentration; red cell mass normal; EPO normal/low

## Connections

- `connects-to` → **[EPAS1](../../03-molecular/epas1/README.md)** — HIF-2α (EPAS1) drives EPO transcription; VHL loss or EPAS1 GOF mutations → secondary/hereditary erythrocytosis; PHD2/EGLN1 mutations stabilize HIF-2α; PV distinguished from secondary erythrocytosis by low serum EPO + JAK2 V617F mutation.
- `connects-to` → **[JAK2](../../03-molecular/jak2/README.md)** — JAK2 V617F is present in ~99% PV; GOF in JH2 pseudokinase domain → constitutive JAK2/STAT5 → EPO-independent erythroid proliferation; ruxolitinib (RESPONSE: Hct control 21% vs 1%) FDA-approved for HU-resistant/intolerant PV.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Serum EPO is suppressed in PV (WHO minor criterion) due to constitutive JAK2 erythropoiesis; secondary erythrocytosis (hypoxia, VHL mutation) shows elevated EPO; EPO level distinguishes primary from secondary polycythemia; ropeginterferon reduces EPO-driven clonal expansion.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — PV transforms to post-PV myelofibrosis (~10-15% at 10 years); megakaryocyte-derived TGF-β1 → collagen deposition → reticulin/collagen fibrosis; momelotinib and luspatercept address TGF-β-driven anemia in post-PV MF.
- `connects-to` → **[Myeloproliferative Neoplasms](../myeloproliferative-neoplasms/README.md)** — Polycythemia vera is the erythroid-dominant member of the BCR-ABL-negative myeloproliferative neoplasms (with ET and myelofibrosis), nearly always JAK2-driven (~99% V617F); it shares their thrombosis risk and capacity to evolve into post-PV myelofibrosis or AML.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — JAK2 V617F makes erythroid progenitors expand without EPO (endogenous erythroid colonies), raising red-cell mass and blood viscosity → arterial and venous thrombosis; phlebotomy to hematocrit <45% cuts cardiovascular events ~45% (CYTO-PV) by lowering that viscosity.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — Splenomegaly affects ~70% of PV from extramedullary hematopoiesis, causing early satiety and, when massive, infarction risk; it worsens as disease evolves toward post-PV myelofibrosis, and the JAK1/2 inhibitor ruxolitinib reduces spleen volume in HU-resistant patients.
- `connects-to` → **[Stroke](../stroke/README.md)** — Thrombosis is the leading cause of death in polycythemia vera, arterial events dominating: raised red-cell mass, JAK2 hyperviscosity, and activated platelets cause stroke, MI, and Budd-Chiari/splanchnic-vein thrombosis; phlebotomy to hematocrit <45% and aspirin cut these events.
- `connects-to` → **[Essential Thrombocythemia](../essential-thrombocythemia/README.md)** — Polycythemia vera and essential thrombocythemia are sibling JAK2-driven myeloproliferative neoplasms on a continuum: PV expands the erythroid lineage (high hematocrit) and ET the megakaryocytic (high platelets), but both carry thrombosis risk and can evolve to myelofibrosis.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Polycythemia vera is a clonal bone marrow stem-cell disease: a JAK2 V617F-mutant hematopoietic stem cell produces panmyelosis — hypercellular marrow with trilineage (especially erythroid) proliferation — and a low EPO; over years the marrow can scar into post-PV myelofibrosis.
- `connects-to` → **[Myelofibrosis](../myelofibrosis/README.md)** — Polycythemia vera can burn out into post-PV myelofibrosis: after years of JAK2-driven erythrocytosis, the marrow becomes fibrotic and counts fall, with massive splenomegaly—one of PV's two main long-term fates, the other being acute leukemia.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Thrombosis is the chief danger of polycythemia vera: high hematocrit and JAK2-mutant, hyperviscous blood drive arterial and venous clots, including splanchnic-vein thromboses that can be the presenting clue—so phlebotomy and aspirin aim to prevent them.
- `connects-to` → **[AML](../aml/README.md)** — Polycythemia vera carries a small but serious risk of leukemic transformation: the JAK2-mutant clone can acquire further mutations and evolve into acute myeloid leukemia, a feared, largely chemo-resistant end-stage—so cytoreduction choice weighs leukemogenic risk.
- `connects-to` → **[Gout](../gout/README.md)** — Polycythemia vera commonly causes secondary gout: the high turnover of overproduced red cells releases purines that become uric acid, so hyperuricemia and gout flares are frequent—sometimes the presenting clue to an unsuspected myeloproliferative neoplasm.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Polycythemia vera must be distinguished from the secondary erythrocytosis of kidney disease: PV is JAK2-driven red-cell overproduction with low EPO, while renal pathology drives high-EPO secondary polycythemia—measuring erythropoietin separates primary from secondary.
- `connects-to` → **[Renal Cell Carcinoma](../renal-cell-carcinoma/README.md)** — Renal cell carcinoma is a classic cause of secondary polycythemia: the tumor ectopically secretes erythropoietin, raising red-cell mass without the JAK2 mutation of true polycythemia vera—so unexplained erythrocytosis warrants imaging to exclude an EPO-producing tumor.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Polycythemia vera must be told from oxygen-driven secondary polycythemia: PV makes red cells autonomously via JAK2 with LOW erythropoietin, whereas chronic hypoxia (lung disease, altitude) raises EPO appropriately—so a low EPO points to primary disease.
- `connects-to` → **[Iron Deficiency Anemia](../iron-deficiency-anemia/README.md)** — Chronic phlebotomy treatment makes PV patients iron-deficient: removing blood to control the hematocrit depletes iron, producing microcytosis without anemia—an intentional iron-restricted state that curbs red-cell overproduction in polycythemia vera.
- `connects-to` → **[Chronic Myeloid Leukemia](../cml/README.md)** — PV and CML are both myeloproliferative neoplasms but molecularly opposite: PV is JAK2-driven with red-cell excess, CML is BCR-ABL-driven with granulocyte excess—testing for these mutations separates the chronic myeloid overproductions and picks the right targeted drug.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Polycythemia vera paradoxically depletes iron: the marrow's relentless red-cell overproduction—and the phlebotomy used to treat it—consume iron, so PV patients are typically iron-deficient with microcytic cells, and iron supplements can worsen the polycythemia.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Polycythemia vera overproduces platelets along with red cells: the JAK2 clone expands all myeloid lines, so thrombocytosis adds to the hyperviscosity, compounding the thrombotic risk that is the disease's main threat—mitigated by aspirin and cytoreduction.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — Polycythemia vera is dangerous mainly through the cardiovascular system: too many red cells thicken the blood, so hyperviscosity and an activated clotting state cause heart attacks, strokes and clots—why keeping hematocrit below 45% is the central treatment goal.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Polycythemia vera classically clots the hepatic veins: the thick, hyperviscous, prothrombotic blood causes Budd-Chiari syndrome and other splanchnic-vein thromboses, so unexplained liver-vein clots should prompt JAK2 testing for an occult PV.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — PV causes aquagenic pruritus through mast cells: the clonal disease primes basophils and mast cells to release histamine, triggering the intense itching after warm water that is a classic and miserable symptom of polycythemia vera.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — JAK2 drives polycythemia vera by switching on STAT signaling: the V617F mutation makes JAK2 constitutively active, firing STAT3/STAT5 to push red-cell production without erythropoietin—the rationale for JAK inhibitors like ruxolitinib.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Polycythemia vera is too much hemoglobin: the JAK2-mutant marrow overproduces red cells, thickening the blood with hemoglobin until it sludges and clots, so treatment phlebotomizes patients to a target hematocrit to cut stroke and thrombosis risk.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Polycythemia vera itches through histamine: the disease expands mast cells and basophils whose histamine release causes the maddening itch after a warm shower (aquagenic pruritus), a hallmark symptom that antihistamines and JAK inhibitors target.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Polycythemia vera raises neutrophils too, not just red cells: as a panmyelosis it often drives leukocytosis, and a high neutrophil count is itself a predictor of the clots that are the disease's main danger.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Polycythemia vera endangers the brain with sludgy blood: too many red cells thicken the blood, slowing flow and raising the risk of stroke and cerebral vein clots, so lowering the red-cell count protects against these neurologic catastrophes.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Polycythemia vera causes a maddening water-triggered itch: contact with warm water releases mediators from the expanded mast-cell population, producing aquagenic pruritus—an unusual but characteristic clue to the disease.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — PV's high cell counts can fake high potassium: the swollen mass of cells leaks potassium after the blood sample clots, producing pseudohyperkalemia—a lab artifact to recognize before treating a number that isn't real in the body.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Polycythemia vera overworks and clots the heart: blood thickened with excess red cells raises the risk of heart attacks and strains cardiac pumping, a major driver of its mortality.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — PV shows in the eyes: hyperviscous blood engorges and slows the retinal veins, causing blurred vision and visual disturbances that can signal dangerously thick blood.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — PV primes the vessel lining to clot: sluggish hyperviscous blood and JAK2-mutant cells activate endothelial cells, tipping the balance toward the arterial and venous thromboses that define the disease.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Radioactive phosphorus tames PV with electrons: P-32 lodges in the marrow and showers it with beta particles — fast electrons — to throttle the runaway red-cell production, a once-standard therapy now kept for older patients who can't manage other drugs.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — The kidney both mimics and suffers PV: a tumor or cyst making excess erythropoietin must be excluded as a cause of high red cells, while PV's own urate overload from rapid cell turnover scars the kidney with gout-related nephropathy.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — PV's thick blood threatens the lungs: the hyperviscous, clot-prone circulation throws pulmonary emboli and raises pulmonary pressures, so breathlessness and chronic thromboembolic pulmonary hypertension can complicate the disease.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Sluggish, crowded blood torments the nerves: PV causes headache, dizziness, and visual blurring from hyperviscosity, plus the burning red hands and feet of erythromelalgia, where platelet plugs in small vessels inflame sensory neurons.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — The driver mutation is also the drug target: ruxolitinib, a JAK1/2 inhibitor, calms the overactive JAK-STAT signaling of PV, shrinking the spleen and easing symptoms in patients who can't tolerate or fail hydroxyurea.
- `connects-to` → **[VHL Disease](../vhl-disease/README.md)** — Other paths can also overfill the blood: where PV makes red cells with the EPO switch off, germline VHL defects (Chuvash polycythemia) stabilize HIF and drive EPO up — high versus low erythropoietin separating these causes of erythrocytosis.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Furious cell turnover spills minerals: the relentless birth and death of blood cells in PV, and their lysis under cytoreductive therapy, release phosphate and urate, the metabolic overflow that fuels the gout and hyperuricemia these patients suffer.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — PV is the great cause of Budd-Chiari: clots in the hepatic veins back blood up into the liver, congesting and killing hepatocytes, so an unexplained hepatic-vein thrombosis should always prompt a hunt for the JAK2 mutation.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Pregnancy magnifies PV's clotting danger: the thickened blood plus pregnancy's hypercoagulability raise the risk of miscarriage, placental thrombosis, and venous clots, managed with low-dose aspirin and careful control of the hematocrit.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — PV's clots strike the arteries too: the thickened blood and hyperactive platelets drive arterial thrombosis on top of atherosclerotic plaque, so heart attack and stroke — not just venous clots — are leading causes of death and the reason for aspirin and hematocrit control.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — When PV burns out it can turn marrow to bone: progression to post-polycythemic myelofibrosis brings osteosclerosis, where osteoblasts lay down excess bone that crowds out the very blood production the disease once drove into overdrive.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — JAK2 fans out beyond STAT: the V617F mutation fires not only JAK-STAT but the PI3K-AKT pathway, an extra survival and proliferation signal that helps the erythroid clone expand and a node targeted to complement JAK inhibition.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — The iron gate stays wide open: the ravenous erythropoiesis of PV releases erythroferrone that suppresses hepcidin, so the gut keeps absorbing iron to feed red-cell production — part of why the disease runs iron-deficient yet overproduces cells.
- `connects-to` → **[TET2](../../03-molecular/tet2/README.md)** — JAK2 rarely acts alone: co-occurring epigenetic mutations like TET2 shape PV's course, sometimes preceding the JAK2 hit and influencing how readily the clone progresses toward myelofibrosis or leukemia.
- `connects-to` → **[Pulmonary Arterial Hypertension](../pulmonary-arterial-hypertension/README.md)** — The thickened blood strains the lungs' vessels: the hyperviscosity and clotting tendency of PV, along with megakaryocyte-driven remodeling, can raise pulmonary artery pressure, one of the circulatory complications of an overcrowded bloodstream.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — JAK2 inflames as it proliferates: the mutant clone drives NLRP3-inflammasome activation and IL-1β release, the chronic inflammation that fuels PV's thrombosis risk and constitutional symptoms beyond the raised cell counts.
- `connects-to` → **[Myelodysplastic Syndromes](../mds/README.md)** — The clone can shift toward dysplasia: as it accumulates secondary mutations, polycythemia vera can transform into a myelodysplastic/MDS-like phase on the path to leukemia, especially after cytoreductive therapy.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — Overcrowded blood pushes the pressure up: the raised red-cell mass and viscosity of PV increase vascular resistance, contributing to hypertension that compounds the disease's cardiovascular and thrombotic risk.
- `connects-to` → **[TNF-α (Tumor Necrosis Factor-alpha)](../../03-molecular/tnf-alpha/README.md)** — The cytokine that lets the mutant clone win: JAK2-V617F cells are resistant to TNF-α while normal progenitors are suppressed by it, so the high TNF-α of PV actively selects for the malignant clone — inflammation feeding the neoplasm.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Constitutive JAK2 signaling fires it up: the V617F mutation drives chronic NF-κB activation in PV, sustaining the inflammatory cytokine milieu that underlies symptoms, thrombosis risk and fibrotic progression.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — The polycythemia can flip to anemia: as PV exhausts into a spent, myelofibrotic phase, marrow fibrosis and chronic inflammation replace the red-cell excess with an anemia carrying a chronic-disease component.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Thick blood and clots overburden the heart: PV's hyperviscosity raises cardiac workload, and its arterial thromboses cause myocardial infarctions, both routes by which the disease can drive the heart toward failure.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Relentless itch and fatigue erode mood: the disabling aquagenic pruritus, chronic fatigue and lifelong thrombosis anxiety of PV substantially impair quality of life and contribute to depression.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Its cytoreductive drugs blunt immune defense: ruxolitinib and hydroxyurea used to control PV suppress immunity and predispose to opportunistic and reactivated infections that can escalate to sepsis.
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — JAK inhibition reawakens shingles: ruxolitinib used for polycythemia vera dampens T-cell immunity and characteristically reactivates latent varicella-zoster, a recognised risk during therapy.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Deep immune suppression opens the lung to mould: ruxolitinib for advanced PV, with disease-related immune dysfunction, can permit invasive aspergillosis and other opportunistic fungal infection.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Lifelong clot-and-transformation risk breeds worry: the constant threat of thrombosis and progression to myelofibrosis or leukaemia in PV, plus relentless itch and fatigue, fosters chronic health anxiety.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Excess red cells torment the skin: polycythemia vera causes the intense aquagenic pruritus after warm water, the burning red erythromelalgia of the extremities and a ruddy, plethoric complexion.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It clots the gut's veins and swells the spleen: PV is a leading cause of splanchnic, portal and hepatic vein thrombosis (Budd-Chiari), enlarges the spleen and, via raised histamine, causes peptic ulcers.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Hyperviscosity disturbs the brain: the thickened blood of PV causes headaches, dizziness, visual disturbance and transient ischaemic attacks, and cerebral vein thrombosis can occur.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It swells the spleen: extramedullary haematopoiesis and pooling of the expanded red-cell mass enlarge the spleen in polycythaemia vera, often markedly, with risk of infarction.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Lung disease must be ruled out: chronic hypoxic lung disease causes secondary polycythaemia, the key differential that a true diagnosis of polycythaemia vera must exclude.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It makes red cells without the hormone: polycythaemia vera is an erythropoietin-independent, autonomous erythrocytosis, so a low EPO level distinguishes it from EPO-driven secondary polycythaemia.
- `connects-to` → **[Aspirin](../../../03-medicine/01-modern/04-cardio/aspirin/README.md)** — Low-dose aspirin is standard: it reduces the arterial and microvascular thrombosis that dominates polycythaemia vera, alongside venesection and cytoreduction.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — High cell turnover and marrow disease reach bone: PV raises uric acid causing gout, the expanded marrow brings bone discomfort, and progression to myelofibrosis adds skeletal symptoms.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — JAK inhibition for refractory disease: ruxolitinib blocks the JAK2 V617F-driven JAK-STAT signalling of polycythaemia vera, controlling the red-cell count and spleen in those who fail or cannot tolerate hydroxyurea.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Hydroxyurea cytoreduces the marrow: this oral chemotherapy lowers the red-cell mass in higher-risk polycythaemia vera, used with phlebotomy and low-dose aspirin to prevent the thrombosis that drives most PV deaths.
- `connects-to` → **[Mycobacterium tuberculosis](../../../02-pathogen/02-bacteria/mycobacterium-tuberculosis/README.md)** — Its JAK inhibitor reawakens infection: ruxolitinib used in PV suppresses immunity enough to reactivate tuberculosis and other opportunists, so latent TB should be screened before and during therapy.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Thick blood and urate strain the kidney: hyperviscosity and hyperuricaemia impair renal function, and PV is a classic cause of renal vein and Budd-Chiari thrombosis.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — Its chief danger is the clot: hyperviscosity and JAK2-mutant blood cells inflame and adhere to the arterial wall, driving the strokes and heart attacks that are the leading cause of death in polycythaemia vera.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Where its clots and overflow land: polycythaemia vera's JAK2-mutant clone thromboses the hepatic and portal veins and can seed extramedullary haematopoiesis in the hepatic lobules, so liver enlargement and splanchnic thrombosis both flag the disease.
- `connects-to` → **[COPD](../copd/README.md)** — Primary versus secondary thick blood: polycythaemia vera makes too many red cells autonomously through JAK2, whereas COPD's chronic hypoxia raises erythropoietin to cause a secondary erythrocytosis—the key distinction when haematocrit is high.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Arterial thrombosis and MI: PV's raised red-cell mass causes hyperviscosity and arterial thrombosis including myocardial infarction, the leading cardiovascular cause of death in the disease.
- `connects-to` → **[Antiphospholipid Syndrome](../antiphospholipid-syndrome/README.md)** — Two causes of unusual-site thrombosis: PV—the leading cause of Budd-Chiari—and antiphospholipid syndrome both cause arterial and splanchnic or cerebral venous thrombosis, key differentials in a young patient with a clot.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Erythromelalgia and itch: PV's platelet excess causes erythromelalgia—burning, red, painful extremities from microvascular sensory-nerve involvement—dramatically relieved by low-dose aspirin.
- `connects-to` → **[Von Willebrand Factor](../../03-molecular/von-willebrand-factor/README.md)** — Bleeding from too many cells: very high blood counts in polycythaemia vera adsorb and clear high-molecular-weight von Willebrand multimers, causing an acquired von Willebrand syndrome and a paradoxical bleeding risk.
- `connects-to` → **[HCC](../hcc/README.md)** — Secondary polycythaemia mimic: EPO-secreting tumours such as hepatocellular carcinoma (and renal cancer) cause a paraneoplastic erythrocytosis that must be distinguished from primary, JAK2-driven polycythaemia vera.
- `connects-to` → **[Pheochromocytoma & Paraganglioma](../pheochromocytoma-paraganglioma/README.md)** — The HIF connection: EPAS1 (HIF-2alpha) gain-of-function links polycythaemia with paraganglioma in the Pacak-Zhuang syndrome, the same hypoxia-sensing pathway that JAK2 amplifies in polycythaemia vera.
- `connects-to` → **[Type I Interferon](../../03-molecular/type-i-interferon/README.md)** — Clone-reducing therapy: pegylated interferon-alpha is a disease-modifying treatment for polycythaemia vera that can lower the JAK2-mutant allele burden and induce molecular responses.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Oxygen-sensing axis: HIF/oxygen-sensing signalling underlies erythrocytosis, and HIF2A, PHD2 and VHL defects cause polycythaemia-vera-like erythrocytosis distinct from JAK2-driven disease.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Epigenetic progression: EZH2 and other epigenetic-regulator mutations accumulate in polycythaemia vera and contribute to its progression toward myelofibrosis and leukaemia.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — Clonal inflammation: IL-6 from the JAK2-mutant clone fuels the chronic inflammation of polycythaemia vera, contributing to its symptoms and thrombotic risk.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Inflammatory marrow: IL-1β secreted by the mutant clone damages the bone-marrow niche, promoting the clonal advantage and progression of polycythaemia vera.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Marrow angiogenesis: elevated VEGF increases bone-marrow microvessel density in polycythaemia vera, part of the proliferative MPN microenvironment.
- `connects-to` → **[PF4](../../03-molecular/pf4/README.md)** — The expanded, hyperreactive platelets of polycythemia vera release platelet factor 4 on activation, contributing to the arterial and venous thrombosis that is the leading cause of morbidity—the reason cytoreduction and aspirin anchor treatment.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — The massive hematopoietic turnover of polycythemia vera floods purine catabolism through xanthine oxidase, raising urate and causing the secondary hyperuricemia and gout that complicate the MPN and warrant allopurinol.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — PDGF released by the clonal megakaryocytes stimulates marrow fibroblasts, driving the reticulin fibrosis of post-polycythemia-vera myelofibrosis—the spent-phase transformation that marks disease progression.
- `connects-to` → **[CALR](../../03-molecular/calr/README.md)** — Polycythemia vera is almost universally JAK2-driven, which distinguishes it from the CALR- and MPL-mutant essential thrombocythemia and primary myelofibrosis—the three classic Philadelphia-negative myeloproliferative neoplasms defined by their driver.
- `connects-to` → **[Thrombin](../../03-molecular/thrombin/README.md)** — The raised red-cell mass and activated platelets of PV promote thrombin generation and hyperviscosity, making arterial and venous thrombosis—including Budd-Chiari and splanchnic-vein clots—the leading cause of death and the rationale for phlebotomy and aspirin.
- `connects-to` → **[SF3B1](../../03-molecular/sf3b1/README.md)** — Spliceosome mutations such as SF3B1, acquired alongside the JAK2 driver, mark the higher-risk PV that is more likely to transform into myelofibrosis or acute myeloid leukemia.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — JAK2 V617F signals not only through STAT5 but the RAS-ERK MAPK pathway, broadening the cytokine-independent proliferation of polycythemia vera and a reason JAK inhibition alone fails to eradicate the clone.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — Epigenetic-regulator mutations in DNMT3A, acquired with the TET2 already mapped here, can precede or accompany the JAK2 driver and shape the clonal evolution and progression risk of polycythemia vera.
- `connects-to` → **[Ferroportin](../../03-molecular/ferroportin/README.md)** — The high erythropoietic drive of PV suppresses hepcidin, leaving ferroportin active to feed iron into red-cell production; hepcidin-mimetics (rusfertide) exploit this by degrading ferroportin to starve the clone of iron and control erythrocytosis.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — Constitutive JAK2 signaling (mapped) engages PI3K (AKT already mapped) as a parallel effector pathway supporting the erythroid expansion of polycythemia vera.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR completes the PI3K-AKT-mTOR pathway (AKT already mapped) downstream of JAK2, and mTOR inhibition has been explored to control the clone in polycythemia vera.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 inactivation drives the progression of polycythemia vera to post-PV myelofibrosis and acute myeloid leukemia.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR-MyD88-NF-κB innate signaling (NF-κB already mapped) sustains the chronic inflammatory milieu that drives symptoms and clonal progression in polycythemia vera.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A loss is among the cooperating lesions in the leukemic transformation of polycythemia vera to acute myeloid leukemia.
- `connects-to` → **[RUNX1](../../03-molecular/runx1/README.md)** — Acquired RUNX1 mutations mark the transformation of polycythemia vera to secondary acute myeloid leukemia.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — Type-I-interferon signaling through STAT1 (type-I-interferon mapped) underlies the disease-modifying activity of ropeginterferon in polycythemia vera.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 expressed by megakaryocytes contributes to the marrow microenvironment and the fibrotic potential of polycythemia vera.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN restraint of PI3K-AKT-mTOR signaling (AKT, PIK3CA and mTOR mapped) downstream of JAK2-driven activation shapes the clonal proliferation of polycythemia vera.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING amplifies the chronic inflammatory marrow milieu (type-I interferon already mapped) of polycythemia vera.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β already mapped) drives the marrow fibrosis underlying the progression of polycythemia vera toward post-PV myelofibrosis.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6-cyclin-D activity (CDKN2A already mapped) drives the JAK2-fueled erythroid and myeloid cell-cycle progression of polycythemia vera.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — JAK2-STAT5-PI3K-AKT signaling (AKT already mapped) inactivates FOXO, supporting the survival of the clonal erythroid progenitors of polycythemia vera.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β misregulation contributes to the aberrant hematopoietic stem-cell self-renewal of polycythemia vera.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins reflect the inflammatory myeloid activation of polycythemia vera.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family and LYN kinase signaling cooperates with JAK2-STAT to support the survival of the clonal erythroid cells of polycythemia vera.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-p53 signaling (p53 already mapped) participates in the clonal survival and leukemic-evolution risk of polycythemia vera.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated cytotoxic immunosurveillance targets the neoantigen-bearing JAK2-mutant clone of polycythemia vera.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of the clonal hematopoietic cells of polycythemia vera.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the survival of the JAK2-mutant clone of polycythemia vera.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-family chemokine signaling participates in the aberrant myeloid trafficking and inflammatory niche of polycythemia vera.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the bone-marrow-niche and megakaryocyte interactions of polycythemia vera.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic dysregulation of polycythemia vera.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the inflammatory bone-marrow microenvironment of polycythemia vera.
- `connects-to` → **[EGLN1 (PHD2)](../../03-molecular/egln1/README.md)** — Erythrocytosis differential: loss-of-function EGLN1/PHD2 stabilises HIF to cause hereditary erythrocytosis, the germline oxygen-sensing counterpart to JAK2-driven polycythaemia vera (HIF/EPAS1 already mapped), a key distinction in the erythrocytosis workup.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Iron-restricted erythropoiesis: the expanded red-cell production of polycythaemia vera consumes iron and repeated phlebotomy induces deficiency, so transferrin-bound iron delivery becomes rate-limiting, the physiologic rationale behind therapeutic iron restriction.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Hyperviscosity thrombosis: the raised haematocrit of polycythaemia vera increases blood viscosity and shear, impairing endothelial nitric-oxide bioavailability and promoting the arterial and venous thrombosis that is the leading cause of death.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Arterial thrombosis: polycythaemia vera markedly raises the risk of arterial events including myocardial infarction and stroke (nitric oxide already mapped), and troponin elevation marks the cardiac injury of these thromboses.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Platelet-mediated microvascular events: platelets are the body's main serotonin store, released on aggregation to constrict vessels, so the excess and activated platelets of polycythaemia vera contribute to the erythromelalgia and microvascular symptoms it causes.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Endothelial vasoconstriction: the hyperviscous, inflamed circulation of polycythaemia vera favours endothelin-1-driven vasoconstriction over nitric-oxide vasodilation (already mapped), tipping the vascular balance further toward its characteristic thrombosis.
- `connects-to` → **[ADAMTS13](../../03-molecular/adamts13/README.md)** — Acquired von Willebrand syndrome: when polycythaemia vera raises platelet counts markedly, the high-molecular-weight von Willebrand multimers (already mapped) are cleared, and this acquired von Willebrand syndrome causes the bleeding that can coexist with the thrombosis.
- `connects-to` → **[Protein C](../../03-molecular/protein-c/README.md)** — Prothrombotic tilt: the thrombosis of polycythaemia vera reflects a shift toward coagulation, and reduced activity of the natural anticoagulant protein C (thrombin already mapped) adds to the risk that drives phlebotomy, aspirin and cytoreduction.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Inflammatory milieu: polycythaemia vera carries a chronic inflammatory state, and the anti-inflammatory IL-10 counterbalances the TNF, IL-6 and IL-1 (already mapped) driven by JAK2-STAT signalling that shapes its symptoms and progression.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Thromboxane and platelets: activated platelets (PF4 and serotonin already mapped) generate thromboxane A2 to amplify aggregation, the eicosanoid pathway blocked by the low-dose aspirin used to reduce thrombosis in polycythaemia vera.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — Endothelial activation: the angiopoietin-Tie2 axis reflects the endothelial activation of the prothrombotic state of polycythaemia vera, part of the endothelium's contribution (von Willebrand factor already mapped) to its thrombosis.
- `connects-to` → **[Fibrinogen](../../03-molecular/fibrinogen/README.md)** — Hyperviscosity and coagulation: the raised haematocrit (haemoglobin already mapped) and fibrinogen increase blood viscosity and coagulation (thrombin already mapped), compounding the thrombotic risk that drives phlebotomy in polycythaemia vera.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Inflammatory milieu: IL-4 and the M2 macrophage arm (IL-10 already mapped) shape the chronic inflammation (IL-6 and TNF already mapped) of the myeloproliferative marrow, part of the disease biology of polycythaemia vera.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Marrow adipose crosstalk: the marrow adipocytes and their adipokine leptin signal to the clonal erythroid cells, part of the bone-marrow (already mapped) microenvironment of polycythaemia vera.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Adipokine microenvironment: adiponectin, with leptin (already mapped), from the marrow adipose tissue signals to the myeloproliferative clone, part of the metabolic microenvironment of polycythaemia vera.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — M2 inflammatory arm: IL-13, with IL-4 (already mapped), drives the M2 macrophage arm of the inflammatory (IL-6 and TNF already mapped) microenvironment of the polycythaemia vera marrow.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Marrow-adipocyte adipokine: resistin, with leptin and adiponectin (already mapped), is the marrow-adipocyte adipokine of the metabolic microenvironment of polycythaemia vera.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Erythroblastic-island macrophages: the marrow macrophages (M2, IL-4 and IL-13 already mapped) support the erythropoiesis of the erythroblastic islands and recycle the iron (ferroportin already mapped) of polycythaemia vera.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Clonal immunosurveillance: the cytotoxic T cells (perforin already mapped) provide the immune surveillance of the JAK2 (already mapped)-mutant clone, augmented by the interferon (type-I interferon already mapped) therapy of polycythaemia vera.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 arm: the IFN-γ of the T cells (with the type-I interferon already mapped) is the type-II interferon arm of the anti-clonal immunity and the inflammatory milieu of polycythaemia vera.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) response of the anti-clonal immunity of polycythaemia vera.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the inflammatory milieu of polycythaemia vera.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the chronic inflammatory milieu of polycythaemia vera.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2/pruritus arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped) and the histamine (already mapped), reflects the type-2 dimension of the aquagenic pruritus and inflammatory milieu of polycythaemia vera.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Antigen presentation: the dendritic cells present antigen to the T cells (already mapped) within the chronic inflammatory clonal-haematopoiesis milieu of polycythaemia vera.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Thromboinflammation: the complement C5 and the terminal MAC contribute to the complement-driven thromboinflammation and the elevated thrombotic risk of polycythaemia vera.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the C5 already mapped) links the complement to the neutrophil and platelet (already mapped) activation of the thrombotic milieu of polycythaemia vera.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Central complement: the complement C3, upstream of the C5 and C5aR1 (already mapped), is the pivot of the complement-driven thromboinflammation of polycythaemia vera.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) whose dysregulation amplifies the thromboinflammation of polycythaemia vera.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Innate surveillance: the NK cells (perforin already mapped) are part of the immune surveillance against the JAK2-mutant (already mapped) clone of polycythaemia vera.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Marrow alarmin: TSLP released by bone marrow stromal cells activates mast cells and dendritic cells, promoting the inflammatory myeloproliferative niche that sustains the JAK2-mutant clone of polycythaemia vera.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Thrombotic kinin: bradykinin from the kallikrein-kinin system is amplified by the polycythaemia-vera-associated erythrocytosis and thrombosis (JAK2 already mapped), promoting the vasodilatory response to the hypercoagulable state.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical-pathway brake: C1-esterase inhibitor modulates the classical complement pathway (complement C3, C5 and C5aR1 already mapped) that contributes to the thromboinflammatory state of polycythaemia vera.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Marrow fibrosis ECM: periostin, a TGF-β-induced ECM component, contributes to the marrow fibrosis (TGF-β already mapped) in polycythaemia vera progression toward myelofibrosis (already mapped), reinforcing the desmoplastic niche of the JAK2-mutant clone.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian erythropoiesis modulator: melatonin regulates the circadian rhythm of erythropoiesis (EPO already mapped) and platelet (already mapped) production, with circadian disruption amplifying the JAK2-mutant erythrocytosis and thrombotic risk of polycythaemia vera.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — JAK2 cross-activation: prolactin signals through the JAK2 (already mapped) receptor, directly intersecting the pathogenic JAK2-V617F hyperactivation; prolactin also stimulates erythropoiesis (EPO already mapped), amplifying the clonal erythrocytosis of polycythaemia vera.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — PV androgen axis: testosterone via androgen receptor modulates erythropoiesis and iron metabolism (transferrin already mapped); the male sex predominance of polycythaemia vera reflects androgen-driven amplification of the JAK2-V617F (already mapped) erythroid clone.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — PV oxytocin: oxytocin via OXTR on megakaryocytes (platelet already mapped) and bone-marrow (already mapped) progenitors modulates platelet production and thrombopoiesis, intersecting the JAK2 (already mapped)-driven thrombocytosis of polycythaemia vera.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — PV vasopressin: vasopressin via V2R on collecting-duct cells (kidney already mapped) and megakaryocytes (platelet already mapped) modulates blood viscosity and platelet activation, amplifying the thrombotic risk of the erythrocytosis of polycythaemia vera.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — PV selenium: selenium-dependent glutathione peroxidase (GPX) quenches reactive-oxygen-species generated by JAK2-V617F (already mapped) hyperactivated erythroid cells in polycythaemia vera, reducing oxidative DNA damage and the clonal erythrocytosis.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — PV iodine: iodine-dependent thyroid hormones modulate erythropoiesis (EPO already mapped) and bone-marrow (already mapped) progenitor proliferation; hypothyroidism blunts and hyperthyroidism amplifies JAK2 (already mapped)-driven erythrocytosis in polycythaemia vera.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — PV sodium: sodium homeostasis via RAAS (aldosterone already mapped) and vasopressin (already mapped) is disrupted by the erythrocytosis-driven hyperviscosity of polycythaemia vera, contributing to hypertension and the cardiovascular thrombotic risk.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — PV magnesium: magnesium, as ATP cofactor in erythrocytes (already mapped) and platelets (already mapped), supports JAK2 (already mapped) kinase fidelity; magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of polycythaemia vera.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — PV copper: copper, as ceruloplasmin cofactor in hepatocytes (already mapped) and neutrophils (already mapped), supports iron (already mapped) recycling; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) haematopoietic cascade of polycythaemia vera.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — PV calcium: calcium, as second-messenger in JAK2 (already mapped)-activated erythroid progenitors and platelets (already mapped), modulates thrombopoiesis; calcium dysregulation amplifies IL-6 (already mapped) and NF-κB (already mapped) thrombotic risk of PV.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — PV zinc: zinc, as metalloproteinase cofactor in neutrophils (already mapped) and platelets (already mapped), modulates thrombo-inflammatory remodelling; zinc deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) haematopoietic cascade of polycythaemia vera.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — PV chloride: chloride, via erythrocyte (already mapped) anion exchangers, maintains CO₂ transport and osmotic balance; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) haematological cascade of polycythaemia vera.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — PV sulfur: sulfur, as component of glutathione in erythrocytes (already mapped) and neutrophils (already mapped), limits oxidative haemolysis; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) haematopoietic inflammatory cascade of polycythaemia vera.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — PV carbon: carbon as backbone of JAK2 and NF-κB (already mapped) proteins in erythrocytes (already mapped) and neutrophils (already mapped) sustains myeloproliferative signalling; carbon depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of PV.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — PV hydrogen: hydrogen, via redox homeostasis in erythrocytes (already mapped) and macrophages (already mapped), supports haemoglobin function; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) oxidative cascade of polycythaemia vera.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — PV nitrogen: nitrogen in amino-acid scaffold of JAK2 and erythropoietin (already mapped) proteins in erythrocytes (already mapped) sustains erythropoietic signalling; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of PV.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — PV PD-1: PD-1 on T-cells (already mapped) and macrophages (already mapped) in bone marrow (already mapped) modulates immune surveillance of JAK2-mutant clones; PD-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) erythroid expansion cascade of PV.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — PV GLP-1: GLP-1 receptor signalling in macrophages (already mapped) and platelets (already mapped) modulates thrombotic and metabolic risk in PV; GLP-1 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and erythropoietin (already mapped) cascade of PV.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — PV angiotensin-II: angiotensin-II in bone marrow vasculature promotes erythroid progenitor expansion; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and erythropoietin (already mapped) erythrocytosis cascade of polycythemia vera.
- `connects-to` → **[WNT/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — PV wnt-beta-catenin: WNT/β-catenin on stem cells (already mapped) and macrophages (already mapped) drives erythroid expansion; wnt-beta-catenin loss amplifies nf-kb (already mapped) and il-6 (already mapped) and erythropoietin (already mapped) erythrocytosis cascade of PV.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — PV rankl: RANKL from macrophages (already mapped) and fibroblasts (already mapped) modulates myeloproliferative bone marrow niche; rankl excess amplifies nf-kb (already mapped) and il-6 (already mapped) and erythropoietin (already mapped) erythrocytosis cascade of PV.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — PV il-2: IL-2 from T-cells (already mapped) and macrophages (already mapped) regulates PV immune surveillance; il-2 dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and erythropoietin (already mapped) erythrocytosis cascade of PV.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — PV fibronectin: fibronectin in macrophages (already mapped) and erythroid progenitors (already mapped) promotes marrow ECM remodelling in PV; fibronectin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of polycythemia vera.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — PV notch: Notch signalling in macrophages (already mapped) and erythroid progenitors (already mapped) regulates haematopoietic cell fate in PV; notch dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of polycythemia vera.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — PV igf-1: IGF-1 from macrophages (already mapped) and erythroid progenitors (already mapped) promotes haematopoietic cell survival in PV; igf-1 dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of polycythemia vera.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — PV activin-a: activin-A from macrophages (already mapped) and erythroid progenitors (already mapped) modulates haematopoietic inflammatory tone; activin-a excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of polycythemia vera.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — PV cgrp: CGRP from macrophages (already mapped) and erythroid progenitors (already mapped) modulates haematopoietic neuroimmune tone; cgrp excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of polycythemia vera.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — PV calcitonin: calcitonin from macrophages (already mapped) and erythroid progenitors (already mapped) modulates calcium balance in PV; calcitonin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of polycythemia vera.
- `connects-to` → **[Substance P](../../03-molecular/substance-p/README.md)** — PV substance-p: substance-P from macrophages (already mapped) and erythroid progenitors (already mapped) modulates haematopoietic neuroimmune tone; substance-p excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of PV.
- `connects-to` → **[Insulin Receptor](../../03-molecular/insulin-receptor/README.md)** — PV insulin-receptor: insulin receptor on macrophages (already mapped) and erythroid progenitors (already mapped) drives haematopoietic metabolic repair; insulin-receptor loss amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of PV.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — PV aldosterone: aldosterone from macrophages (already mapped) and erythroid progenitors (already mapped) modulates haematopoietic ion balance; aldosterone excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of PV.

[^vannucchi-2015-response]: Vannucchi AM, Kiladjian JJ, Griesshammer M, et al. Ruxolitinib versus standard therapy for the treatment of polycythemia vera. *N Engl J Med.* 2015;372(5):426-435. [doi:10.1056/NEJMoa1409630](https://doi.org/10.1056/NEJMoa1409630) · [PubMed 25577388](https://pubmed.ncbi.nlm.nih.gov/25577388/)
[^gisslinger-2020-proud-pv]: Gisslinger H, Gotic M, Holowiecki J, et al. Ropeginterferon alfa-2b versus standard therapy for polycythaemia vera (PROUD-PV and CONTINUATION-PV): a randomised, non-inferiority, phase 3 trial and its extension study. *Lancet Haematol.* 2020;7(3):e196-e208. [doi:10.1016/S2352-3026(19)30236-4](https://doi.org/10.1016/S2352-3026(19)30236-4) · [PubMed 32046833](https://pubmed.ncbi.nlm.nih.gov/32046833/)
