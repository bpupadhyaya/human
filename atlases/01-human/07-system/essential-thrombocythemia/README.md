---
schema: human-scale-entry/v1
id: essential-thrombocythemia
name: Essential Thrombocythemia
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Essential thrombocythemia is a JAK2/CALR/MPL-driven MPN with megakaryocytic hyperplasia and thrombocytosis; JAK2 V617F ~55-60%; CALR ~20-25%; MPL ~5-8%; risk-stratified aspirin ± hydroxyurea; anagrelide second-line; post-ET MF (~1-2%) and AML (<1%) transformation risk."
aliases: ["essential thrombocythemia", "ET", "essential thrombocytosis", "primary thrombocythemia", "JAK2 thrombocythemia", "CALR ET"]
sources:
  - id: harrison-2005-pt1-et
    type: peer-reviewed
    cite: "Harrison CN, Campbell PJ, Buck G, et al. Hydroxyurea compared with anagrelide in high-risk essential thrombocythemia. N Engl J Med. 2005;353(1):33-45."
    doi: "10.1056/NEJMoa043800"
    pmid: "16000354"
    url: "https://doi.org/10.1056/NEJMoa043800"
  - id: barbui-2012-ipset
    type: peer-reviewed
    cite: "Barbui T, Finazzi G, Carobbio A, et al. Development and validation of an International Prognostic Score of thrombosis in World Health Organization-essential thrombocythemia (IPSET-thrombosis). Blood. 2012;120(26):5128-5133."
    doi: "10.1182/blood-2012-07-444067"
    pmid: "23086758"
    url: "https://doi.org/10.1182/blood-2012-07-444067"
cross_links:
  - target: 01-human/03-molecular/mpl
    relation: connects-to
    note: "MPL W515L/K mutations (~5-8% ET) cause constitutive JAK2/STAT5 activation independent of TPO; MPL-mutant ET is clinically similar to CALR-mutant ET (lower thrombosis risk vs JAK2); TPO-receptor agonists (eltrombopag, romiplostim) act on wild-type MPL."
  - target: 01-human/03-molecular/jak2
    relation: connects-to
    note: "JAK2 V617F (~55-60% ET) causes constitutive erythroid/megakaryocytic/granulocytic proliferation; JAK2-positive ET has higher thrombosis risk than CALR-mutant ET; ruxolitinib is active in JAK2 V617F ET but is not FDA-approved for ET."
  - target: 01-human/03-molecular/calr
    relation: connects-to
    note: "CALR mutations (~20-25% ET); type 2 ins5bp is predominant in ET (vs type 1 del52bp in PMF); CALR-mutant ET has lower thrombosis risk, younger age, and longer OS than JAK2-mutant ET; JAK2/CALR/MPL mutations are mutually exclusive."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "ET transforms to post-ET MF (~1-2% at 10 years); megakaryocyte-derived TGF-β1 → reticulin → collagen fibrosis; co-mutations (ASXL1, EZH2, SRSF2) accelerate MF transformation; momelotinib targets ACVR1 to address anemia in post-ET MF."
  - target: 01-human/03-molecular/von-willebrand-factor
    relation: connects-to
    note: "At platelet counts >1,500 ×10⁹/L, ET causes acquired von Willebrand syndrome — platelet GPIb adsorbs high-molecular-weight VWF multimers and depletes them, impairing primary hemostasis → paradoxical bleeding; aspirin is contraindicated until cytoreduction normalizes the count."
  - target: 01-human/07-system/polycythemia-vera
    relation: connects-to
    note: "PV and ET are both JAK2-driven MPNs on a phenotypic continuum; PV (JAK2 nearly 100%, often homozygous) skews erythroid while ET skews megakaryocytic; JAK2 V617F-ET can drift toward a PV phenotype; ET has lower post-MF and AML transformation risk than PV."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Clonal megakaryocytic hyperplasia drives sustained thrombocytosis; JAK2 V617F platelets are constitutively activated (resting P-selectin) → platelet-leukocyte aggregates and thrombosis; erythromelalgia from platelet microvascular occlusion responds rapidly to aspirin."
  - target: 01-human/07-system/disseminated-intravascular-coagulation
    relation: connects-to
    note: "Essential thrombocythemia and DIC are opposite poles of platelet pathology: ET clonally overproduces platelets causing thrombosis (and, at extreme counts, acquired von Willebrand bleeding), while DIC systemically consumes platelets and clotting factors — too many versus too few."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Essential thrombocythemia is a clonal bone marrow disease: a JAK2, CALR, or MPL mutation drives autonomous megakaryocyte hyperplasia, so the marrow shows large, mature, clustered megakaryocytes without the dense fibrosis of primary myelofibrosis — a key WHO distinction."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "Mild splenomegaly is common in essential thrombocythemia from extramedullary hematopoiesis and pooling; progressive splenic enlargement signals transformation to post-ET myelofibrosis, and prior splenectomy paradoxically raises platelet counts and thrombosis risk."
  - target: 01-human/07-system/myeloproliferative-neoplasms
    relation: connects-to
    note: "Essential thrombocythemia is one of the three classic Philadelphia-negative myeloproliferative neoplasms (with PV and PMF): a JAK2/CALR/MPL-driven clonal overproduction—here of platelets—sharing thrombosis risk and the capacity to evolve into myelofibrosis or AML."
  - target: 01-human/07-system/myelofibrosis
    relation: connects-to
    note: "Essential thrombocythemia can progress to post-ET myelofibrosis: over years the clone drives marrow reticulin fibrosis, so the platelet-rich blood picture gives way to splenomegaly, cytopenias and a leukoerythroblastic film, converging with primary myelofibrosis."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Thrombosis—not bleeding—is the main danger of essential thrombocythemia: the dysfunctional excess platelets and JAK2 mutation create a prothrombotic state causing arterial and venous events, including VTE and unusual-site (splanchnic) thrombosis; aspirin lowers risk."
  - target: 01-human/07-system/cml
    relation: connects-to
    note: "ET and CML are both chronic myeloproliferative neoplasms but driven differently: CML by the BCR-ABL fusion tyrosine kinase (treatable with imatinib), ET by JAK2/CALR/MPL mutations driving platelet overproduction—both can progress to fibrosis or acute leukemia."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "ET predisposes to stroke: the excess, often dysfunctional platelets promote arterial thrombosis, so TIAs and stroke are feared complications—low-dose aspirin and cytoreduction lower this risk, a rare case where too many platelets cause clots, not bleeding."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "ET and polycythemia vera show how one marrow can overproduce different lineages: ET expands megakaryocytes and platelets while PV expands erythrocytes, yet both arise from JAK2-pathway mutations—lineage skewing of a shared clonal stem-cell defect sets the phenotype."
  - target: 01-human/03-molecular/thrombin
    relation: connects-to
    note: "Excess platelets in essential thrombocythemia tip toward thrombin-driven clotting: the high, often dysfunctional platelet mass promotes both arterial and venous thrombosis, so low-dose aspirin and cytoreduction lower the clotting risk that dominates ET's morbidity."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "Essential thrombocythemia carries a small but real risk of transforming to AML: as a clonal myeloproliferative neoplasm, ET can evolve through myelofibrosis to acute leukemia, a risk raised by some cytoreductive drugs—the feared long-term endpoint."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Essential thrombocythemia often raises neutrophils too: the JAK2-driven clone expands multiple myeloid lineages, so leukocytosis often accompanies the thrombocytosis and itself predicts higher thrombosis risk—ET is a panmyeloid, not platelet-only, disease."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Essential thrombocythemia clots at the endothelium: excess, often dysfunctional platelets interact with the vessel lining to cause microvascular and large-vessel thrombosis, so antiplatelet therapy targeting this platelet-endothelial interface prevents the main complication."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Essential thrombocythemia is a classic cause of splanchnic vein thrombosis: the prothrombotic platelet excess can clot the hepatic or portal veins (Budd-Chiari), so unexplained abdominal vein thrombosis should prompt testing for JAK2 and an underlying MPN."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Essential thrombocythemia produces distinctive neurovascular symptoms: microvascular platelet plugging causes headaches, visual disturbance and erythromelalgia, and it raises stroke and TIA risk—so the nervous system often signals the disease before a major clot occurs."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "Essential thrombocythemia complicates pregnancy through the placenta: the thrombotic tendency causes placental clots, miscarriage, and growth restriction, so pregnant patients are managed with low-dose aspirin and sometimes heparin to protect the placenta."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Essential thrombocythemia announces itself in the skin as erythromelalgia: platelet microthrombi in small vessels cause burning, red, painful hands and feet, a near-specific symptom that dramatically improves with low-dose aspirin."
  - target: 01-human/07-system/gout
    relation: connects-to
    note: "Essential thrombocythemia's high cell turnover can cause gout: rapid platelet and cell production raises uric acid, so hyperuricemia and gout flares accompany this and other myeloproliferative neoplasms."
  - target: 01-human/03-molecular/thrombopoietin
    relation: connects-to
    note: "Essential thrombocythemia hijacks thrombopoietin signaling: TPO normally tells the marrow how many platelets to make through the MPL receptor, but ET's JAK2, CALR, and MPL mutations switch that pathway on permanently, churning out platelets without the hormone's command."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "All of ET's driver mutations converge on STAT: JAK2, CALR, and MPL defects all end up activating STAT transcription factors, the shared switch that turns on the genes driving runaway platelet production—why JAK-STAT inhibitors are used in the disease."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Platelets in essential thrombocythemia clot through calcium: calcium signaling triggers platelet activation and aggregation, so the vast excess of platelets, primed to release and respond to calcium, tips patients toward the thromboses that menace them."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Platelet-rich blood in essential thrombocythemia can fake high potassium: the enormous platelet mass leaks potassium after the sample clots, producing pseudohyperkalemia—a lab artifact to recognize before treating a number that isn't real."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Essential thrombocythemia strikes the brain's small vessels: excess platelets cause headaches, visual disturbance, TIAs and burning red extremities (erythromelalgia), microvascular symptoms that low-dose aspirin often relieves."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 marks the line between reactive and clonal thrombocytosis: this cytokine drives platelet production in inflammation, so a high count from infection or cancer must be told apart from the clonal overproduction that defines essential thrombocythemia."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Essential thrombocythemia starves fingertips of oxygen: clumps of excess platelets plug tiny vessels, causing the burning, red, oxygen-starved hands and feet of erythromelalgia and risking digital ischemia."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Essential thrombocythemia threatens the heart: its thrombotic tendency raises the risk of coronary clots and heart attacks, part of why even symptom-free patients may need aspirin and cytoreduction."
  - target: 01-human/03-molecular/fibrinogen
    relation: connects-to
    note: "Essential thrombocythemia turns fibrinogen into clots: the swollen platelet mass, activating with fibrinogen, builds the thromboses—strokes, heart attacks, and vein clots—that are the disease's main danger."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "ET is confirmed under the microscope: the marrow biopsy shows clusters of enlarged, staghorn megakaryocytes, the clue that with JAK2 and CALR testing distinguishes it from reactive thrombocytosis."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "ET clots the gut's veins: splanchnic and mesenteric vein thrombosis can be the first sign, so an unprovoked abdominal-vein clot prompts testing for the JAK2 mutation behind the disease."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "ET can scar into myelofibrosis: over years, reticulin and collagen fibrosis gradually replace the marrow, the feared post-ET transformation that brings cytopenias and splenomegaly."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows ET's overgrown platelet factory: the marrow swells with large, mature megakaryocytes with deeply lobulated nuclei, churning out the giant, abnormal platelets that flood the blood."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "ET can briefly blind: clumps of excess platelets sludge through the retinal microvessels, causing fleeting visual disturbances and amaurosis that warn of the disease's thrombotic risk."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "The kidney feels ET's high cell turnover: a surplus of uric acid from rapid platelet production crystallizes in the tubules toward gout and urate nephropathy, while microthrombi can impair renal blood flow."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "ET pesters the nervous system in miniature: platelet plugs in small vessels cause headache, visual blurring, transient ischemic attacks, and the burning red hands and feet of erythromelalgia — symptoms that often ease with aspirin."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "High platelets complicate pregnancy: ET raises the risk of miscarriage and placental thrombosis, so affected women are managed with aspirin and sometimes heparin to protect the pregnancy."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "At extreme counts ET paradoxically bleeds: very high platelets soak up von Willebrand factor into an acquired deficiency, so gastrointestinal bleeding can occur even as the disease otherwise drives clotting."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "ET's clots are mostly arterial: its hyperactive platelets favor arterial thrombosis on top of any atherosclerotic plaque, which is why heart attack and stroke dominate its risk and why low-dose aspirin and cardiovascular-risk control are central to management."
  - target: 01-human/03-molecular/tet2
    relation: connects-to
    note: "Extra mutations shape the course: TET2 and other clonal-hematopoiesis genes often sit alongside the JAK2 or CALR driver, expanding the malignant clone and adding to the thrombotic risk and the chance of progression to myelofibrosis or leukemia."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron tells the true thrombocytosis from the false: iron deficiency itself drives a reactive rise in platelets that mimics ET, so checking iron status is a basic step in deciding whether a high platelet count is clonal disease or simple deficiency."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Chronic inflammation drives the MPN clone: JAK2-activated NF-κB signaling fuels the inflammatory cytokine state behind ET's symptoms and its prothrombotic tendency, a target of interferon and JAK-inhibitor therapy."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Marrow macrophages support the overgrowth: they help build the inflammatory niche that favors the mutant megakaryocyte clone in ET, part of the microenvironment that sustains the disease."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "The clotting disorder can choke the lungs: ET raises the risk of pulmonary hypertension through in-situ microthrombi, chronic thromboembolism, and extramedullary hematopoiesis, straining the right heart."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "Epigenetic mutations stack on the driver: DNMT3A and other clonal-hematopoiesis mutations co-occur with JAK2/CALR/MPL in ET, shaping clonal evolution and the risk of progression to myelofibrosis or leukemia."
  - target: 01-human/07-system/mds
    relation: connects-to
    note: "The clone can shift toward dysplasia: ET sits on the myeloid spectrum and can evolve into a myelodysplastic/myeloproliferative overlap or secondary MDS, especially after cytotoxic therapy."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Arterial clots can wreck the heart: ET's thrombotic risk includes coronary events whose myocardial damage leads to heart failure, the cardiac counterpart of its stroke and limb-ischemia complications."
  - target: 01-human/07-system/hcc
    relation: connects-to
    note: "It clots the liver's veins: ET is a leading cause of Budd-Chiari syndrome, hepatic vein thrombosis that congests the liver toward cirrhosis and, over years, hepatocellular carcinoma — sometimes the first sign of the MPN."
  - target: 01-human/07-system/inherited-thrombophilia
    relation: connects-to
    note: "An acquired thrombophilia stacked on inherited ones: ET's overproduced, hyperreactive platelets create an acquired prothrombotic state that multiplies clot risk when a co-existing inherited thrombophilia is also present."
  - target: 01-human/07-system/pnh
    relation: connects-to
    note: "It shares the unusual-site clotting puzzle: like paroxysmal nocturnal hemoglobinuria, ET is an acquired clonal disorder that causes thrombosis in unusual sites such as the splanchnic veins, both considered when such clots appear unexplained."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "It can burn out into anemia: as ET evolves toward a spent, myelofibrotic phase, marrow fibrosis and chronic inflammation replace the platelet excess with an anemia carrying a chronic-disease component."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Its cytoreductive drugs can strip defenses: hydroxyurea and other agents used to lower the platelet count in ET can cause neutropenia, leaving patients more vulnerable to serious infection and sepsis."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A chronic clonal disease weighs on mood: living with the thrombosis-and-transformation risk of a lifelong myeloproliferative neoplasm, plus its constitutional symptoms, contributes to depression and reduced quality of life."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Microvascular platelet plugs burn the extremities: erythromelalgia — red, hot, painful hands and feet from platelet microthrombi — is a classic symptom of essential thrombocythemia, relieved by aspirin."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Its hydroxyurea ulcerates the skin: the cytoreductive drug hydroxyurea used in essential thrombocythemia characteristically causes painful, slow-healing leg ulcers, often forcing a change of therapy."
  - target: 01-human/07-system/basal-cell-carcinoma
    relation: connects-to
    note: "Long-term hydroxyurea raises skin-cancer risk: prolonged hydroxyurea therapy for essential thrombocythemia is associated with non-melanoma skin cancers, including basal and squamous cell carcinomas."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Platelet excess burns the extremities: essential thrombocythemia classically causes erythromelalgia — red, hot, painful hands and feet from microvascular platelet plugging — and digital ischaemia, relieved by aspirin."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It clots the gut's veins yet also bleeds it: ET causes splanchnic and portal vein thrombosis with splenomegaly, while at very high platelet counts an acquired von Willebrand defect causes GI bleeding."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Clot-and-transformation risk breeds worry: the lifelong threat of thrombosis and bleeding and the small risk of progression to myelofibrosis or leukaemia in ET foster chronic health anxiety."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It can enlarge the spleen: mild to moderate splenomegaly from extramedullary haematopoiesis and splenic platelet sequestration occurs in essential thrombocythemia."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Its clots can reach the lungs: the thrombotic tendency of ET causes pulmonary embolism, and microvascular pulmonary thrombosis can contribute to pulmonary hypertension."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Clots and urate strain the kidney: microvascular thrombosis and hyperuricaemia from high cell turnover can impair renal function, and renal vein thrombosis can occur in ET."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its platelets clot the arteries: essential thrombocythemia causes arterial and venous thrombosis — stroke, myocardial infarction and the burning erythromelalgia of digital microvascular occlusion."
  - target: 03-medicine/01-modern/04-cardio/aspirin
    relation: connects-to
    note: "Low-dose aspirin is standard: by inhibiting the excess platelets, aspirin reduces the thrombotic and erythromelalgia risk of essential thrombocythemia, alongside cytoreduction in high-risk disease."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "The myeloproliferative marrow reaches bone: the expanded marrow can cause bone discomfort, and progression to myelofibrosis brings a bulky spleen and skeletal symptoms."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Cytoreduction with hydroxyurea: in high-risk essential thrombocythaemia, hydroxyurea lowers the platelet count to prevent thrombosis, the main cytoreductive chemotherapy alongside interferon."
  - target: 01-human/07-system/antiphospholipid-syndrome
    relation: connects-to
    note: "Two causes of clots that overlap: like antiphospholipid syndrome, essential thrombocythaemia drives both arterial and venous thrombosis, and the two can coexist and compound the risk."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "JAK inhibition for resistant disease: ruxolitinib and other JAK inhibitors, exploiting the JAK2 V617F mutation, treat essential thrombocythaemia that resists hydroxyurea, with interferon a non-mutagenic alternative."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "Activated platelets clot the arteries: essential thrombocythaemia drives arterial thrombosis — stroke, MI and digital ischaemia (erythromelalgia) — through hyperreactive platelets acting on the arterial wall, the target of low-dose aspirin."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "It clots the splanchnic veins: like other myeloproliferative neoplasms, essential thrombocythaemia characteristically causes hepatic- and portal-vein thrombosis (Budd-Chiari), congesting the liver lobule, sometimes before the platelet count rises."
  - target: 01-human/07-system/heparin-induced-thrombocytopenia
    relation: connects-to
    note: "Platelet count, then platelet activation: essential thrombocythaemia thromboses with a high platelet count, whereas heparin-induced thrombocytopenia thromboses as platelets fall — opposite counts united by pathological platelet activation."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Arterial thrombosis and the heart: ET's hyperreactive platelets cause arterial thrombi including myocardial infarction, a leading cause of morbidity that aspirin and cytoreduction aim to prevent."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "Microvascular thrombosis: beyond large arteries, ET causes microvascular occlusion—erythromelalgia and renal microthrombi reaching the glomerulus—relieved promptly by low-dose aspirin."
  - target: 01-human/07-system/cmml
    relation: connects-to
    note: "Across the myeloid-neoplasm family: ET is a classic myeloproliferative neoplasm of platelets, while CMML is a myelodysplastic/myeloproliferative overlap of monocytes—neighbouring clonal marrow diseases that can transform to AML."
  - target: 01-human/07-system/hemophilia-a
    relation: connects-to
    note: "Paradoxical bleeding: extreme thrombocytosis in ET adsorbs and clears von Willebrand factor, causing an acquired von Willebrand syndrome—a bleeding tendency despite high platelets, reached differently than in haemophilia."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Erythromelalgia: platelet microthrombi in small vessels cause burning, red, painful extremities and acrocyanosis—a microvascular and small-fibre disturbance dramatically relieved by aspirin."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Compounded thrombosis risk: the prothrombotic state of essential thrombocythemia adds to the hypercoagulability of COVID-19, raising the risk of arterial and venous clots during infection."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Clone-reducing therapy: pegylated interferon-alpha is a disease-modifying treatment for essential thrombocythemia that can shrink the JAK2- or CALR-mutant clone, unlike purely cytoreductive drugs."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Epigenetic co-mutation: EZH2 and other epigenetic-regulator mutations co-occur with the driver lesions of essential thrombocythemia and contribute to progression toward myelofibrosis."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Downstream of JAK2: the driver mutations of essential thrombocythemia activate JAK-STAT and the parallel PI3K-AKT pathway, together sustaining clonal megakaryocyte proliferation."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Clonal inflammation: TNF-α from the malignant clone gives essential thrombocythemia cells a survival advantage over normal progenitors and drives the constitutional symptoms of the MPN."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Inflammasome activation: JAK2-driven NLRP3-inflammasome activation contributes to the chronic inflammatory state of essential thrombocythemia and its thrombotic risk."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Marrow angiogenesis: elevated VEGF increases bone-marrow microvessel density in essential thrombocythemia, part of the proliferative MPN microenvironment."
  - target: 01-human/03-molecular/pf4
    relation: connects-to
    note: "Platelet activation: PF4 released from the markedly expanded, activated platelet mass of essential thrombocythemia marks the platelet hyperreactivity behind its characteristic thrombotic risk."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "MPN inflammation: S100A8/A9 from the expanded myeloid compartment amplifies the chronic inflammation of essential thrombocythemia, contributing to its thrombotic and constitutional symptoms."
  - target: 01-human/03-molecular/runx1
    relation: connects-to
    note: "Leukaemic transformation: acquired RUNX1 mutations mark the progression of essential thrombocythemia toward myelofibrosis and acute myeloid leukaemia, a feared late evolution."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Thromboxane and aspirin: the hyperreactive platelets of essential thrombocythemia generate thromboxane A2, the target of the low-dose aspirin used to reduce the arterial thrombosis and erythromelalgia of the disease."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Fibrotic progression: PDGF released by the clonal megakaryocytes stimulates marrow fibroblasts, driving the reticulin fibrosis of post-ET myelofibrosis as the disease evolves."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "High cell turnover: the increased haematopoietic turnover of essential thrombocythemia raises urate through xanthine oxidase, causing the secondary hyperuricaemia and gout that can complicate the MPN."
  - target: 01-human/03-molecular/sf3b1
    relation: connects-to
    note: "Transformation risk: spliceosome mutations such as SF3B1, acquired alongside the JAK2/CALR/MPL driver, mark the essential thrombocythemia more likely to progress to myelofibrosis or acute leukaemia, refining its otherwise indolent prognosis."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Apoptotic resistance: should essential thrombocythemia transform to acute leukaemia, the blasts become dependent on anti-apoptotic BCL-2, a vulnerability targeted by venetoclax in the otherwise dismal post-MPN leukaemia."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Thrombo-inflammation: complement activation generating C3 fragments amplifies the platelet and neutrophil activation of essential thrombocythemia, an inflammatory limb of the prothrombotic state that drives its arterial and venous thrombosis."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "MAPK limb: the JAK2, CALR and MPL driver mutations (all already mapped) activate the MAPK-ERK cascade alongside JAK-STAT, driving the megakaryocyte proliferation that produces the thrombocytosis of essential thrombocythemia."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K limb: the same constitutively active receptor-kinase signalling engages PI3K (AKT already mapped) as a third effector pathway supporting megakaryocyte growth and survival in essential thrombocythemia."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "Leukaemic transformation: TP53 inactivation drives the transformation of essential thrombocythemia to acute myeloid leukaemia, a feared progression alongside the RUNX1 lesions already mapped."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Downstream growth axis: the PI3K-AKT-mTOR axis (AKT and PIK3CA already mapped) operates downstream of constitutive JAK2 signalling to drive the megakaryocyte proliferation of essential thrombocythemia."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Inflammatory clonal drive: IL-1β-driven inflammation contributes to the clonal expansion and disease progression of the myeloproliferative neoplasm essential thrombocythemia."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Innate inflammatory milieu: TLR-MyD88-NF-κB innate signalling (NF-κB already mapped) sustains the chronic inflammatory milieu that characterises and propels myeloproliferative neoplasms including essential thrombocythemia."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "Type-I-interferon signalling through STAT1 (type-I-interferon mapped) underlies the disease-modifying activity of interferon therapy in essential thrombocythemia."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 expressed by megakaryocytes contributes to the marrow microenvironment and fibrotic potential of essential thrombocythemia."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN restraint of PI3K-AKT-mTOR signalling (AKT, PIK3CA and mTOR mapped) downstream of JAK2-driven activation shapes the clonal proliferation of essential thrombocythemia."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING amplifies the chronic inflammatory marrow milieu and NET-driven thrombosis risk of essential thrombocythemia."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β already mapped) drives the marrow fibrosis underlying the progression of essential thrombocythemia toward myelofibrosis."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors, restrained by JAK2-PI3K-AKT signalling, modulate the survival and quiescence of the clonal stem cells of essential thrombocythemia."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK1/2 signaling (alongside the mapped JAK2) transduces the constitutive thrombopoietin-receptor activation driving megakaryocyte proliferation in essential thrombocythemia."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the megakaryocyte and clonal stem-cell signaling of essential thrombocythemia."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α shapes the bone-marrow niche and metabolic state of the clonal megakaryocytes of essential thrombocythemia."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis and contributes to the leukemic evolution of essential thrombocythemia."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated cytotoxic immunosurveillance targets the neoantigen-bearing CALR-mutant clone of essential thrombocythemia."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6-cyclin-D cell-cycle activity drives the JAK2-fueled megakaryocyte and progenitor proliferation of essential thrombocythemia."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of the clonal hematopoietic cells of essential thrombocythemia."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the survival of the JAK2/CALR-mutant clone of essential thrombocythemia."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of the thrombopoietin receptor (MPL already mapped) participates in the megakaryocyte proliferation of essential thrombocythemia."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-family chemokine signaling participates in the bone-marrow niche and inflammatory interactions of essential thrombocythemia."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the megakaryocyte and bone-marrow-niche interactions of essential thrombocythemia."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the inflammatory bone-marrow microenvironment of essential thrombocythemia."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory bone-marrow microenvironment of essential thrombocythemia."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the clonal hematopoiesis of essential thrombocythemia."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the megakaryocyte and immune signaling of essential thrombocythemia."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Endothelial-platelet balance: nitric oxide normally restrains platelet activation and keeps vessels dilated, so impaired endothelial nitric-oxide function alongside the excess platelets of essential thrombocythaemia tips the balance toward the thrombosis that dominates its risk."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Arterial thrombosis: the thrombocytosis of essential thrombocythaemia predisposes to arterial events including myocardial infarction and stroke, and troponin elevation marks the cardiac injury of these thrombotic complications."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Platelet mediator: platelets are the body's main store of serotonin, released on aggregation to cause vasoconstriction, so the excess dysfunctional platelets of essential thrombocythaemia contribute to microvascular events such as erythromelalgia."
  - target: 01-human/03-molecular/adamts13
    relation: connects-to
    note: "Acquired von Willebrand syndrome: at extreme platelet counts the high-molecular-weight von Willebrand multimers (already mapped) are adsorbed and cleared, and this acquired von Willebrand syndrome causes the paradoxical bleeding of essential thrombocythaemia."
  - target: 01-human/03-molecular/protein-c
    relation: connects-to
    note: "Thrombotic risk: the thrombosis of essential thrombocythaemia reflects a prothrombotic tilt, and coexisting deficiency of the natural anticoagulant protein C (thrombin already mapped) further raises the risk that drives cytoreduction and antiplatelet therapy."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Inflammatory milieu: essential thrombocythaemia carries a chronic inflammatory state, and the anti-inflammatory IL-10 counterbalances the TNF, IL-6 and IL-1 (already mapped) driven by JAK-STAT signalling that shapes the myeloproliferative phenotype."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Microvascular vasoconstriction: endothelin-1 and the platelet-derived vasoactive mediators (serotonin already mapped) contribute to the microvascular vasoconstriction behind the erythromelalgia and neurological symptoms of essential thrombocythaemia."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Endothelial activation: the angiopoietin-Tie2 axis reflects the endothelial activation of the prothrombotic state of essential thrombocythaemia, part of the endothelium's contribution (von Willebrand factor already mapped) to its thrombosis."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Pulmonary thrombosis: essential thrombocythaemia predisposes to pulmonary embolism and, over time, chronic thromboembolic pulmonary hypertension, part of the venous and arterial thrombotic burden of the disease."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Inflammatory milieu: IL-4 and the M2 macrophage arm (IL-10 already mapped) shape the chronic inflammation (IL-6 and TNF already mapped) of the myeloproliferative marrow, part of the disease biology of essential thrombocythaemia."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Marrow adipose crosstalk: the marrow adipocytes and their adipokine leptin signal to the clonal megakaryocytes, part of the bone-marrow (already mapped) microenvironment of essential thrombocythaemia."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Adipokine microenvironment: adiponectin, with leptin (already mapped), from the marrow adipose tissue signals to the myeloproliferative clone, part of the metabolic microenvironment of essential thrombocythaemia."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipokine milieu: resistin, with leptin and adiponectin (already mapped), completes the marrow-adipocyte adipokine signalling of the metabolic microenvironment of essential thrombocythaemia."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "Leukaemic transformation: essential thrombocythaemia can transform to acute myeloid leukaemia (the blast phase, RUNX1 already mapped), a feared outcome of the myeloproliferative neoplasm."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron deficiency and PV masking: coexisting iron deficiency can lower the haemoglobin and mask an underlying polycythaemia vera (already mapped) as essential thrombocythaemia, and drives the microcytosis of the disorder."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "M2 marrow microenvironment: IL-13, with IL-4 (already mapped), drives the M2 macrophage arm of the inflammatory (IL-6 already mapped) marrow microenvironment of essential thrombocythaemia."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Immune surveillance: the NK cells contribute to the immune surveillance of the JAK2 (already mapped)-mutant clone, and the interferon (type-I interferon already mapped) therapy augments the anti-clonal immunity of essential thrombocythaemia."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "Thrombopoietin source: the hepatocytes are the main source of the thrombopoietin (already mapped), the MPL (already mapped) ligand whose signalling is dysregulated in essential thrombocythaemia."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 anti-clonal arm: the IFN-γ of the T and NK (already mapped) cells is the type-II interferon arm of the anti-clonal immunity (type-I interferon therapy already mapped) of the JAK2-mutant essential thrombocythaemia."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune surveillance of the essential-thrombocythaemia clone."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the inflammatory milieu of essential thrombocythaemia."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the chronic inflammation (IL-6 and TNF already mapped) of the essential-thrombocythaemia clone."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the inflammatory milieu of essential thrombocythaemia."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Clone immune surveillance: the cytotoxic T cells (perforin already mapped) provide the anti-clonal immune surveillance of the JAK2/CALR (already mapped) mutant clone, an arm engaged by the interferon (type-I interferon already mapped) therapy of essential thrombocythaemia."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the cytokines of the chronic inflammation and support the anti-clonal immunity engaged by the interferon (already mapped) therapy of essential thrombocythaemia."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) links the complement to the myeloid inflammation and the immunothrombosis of essential thrombocythaemia."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its activation (with C3 already mapped) contribute to the chronic inflammation and the thrombotic risk of essential thrombocythaemia."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the thromboinflammatory milieu of essential thrombocythaemia."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement/coagulation crosstalk: the C1-esterase inhibitor regulates both the complement (C3, C5, C5aR1 and factor H already mapped) and the contact-coagulation systems at the interface of the immunothrombosis of essential thrombocythaemia."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Thromboinflammation: osteopontin, released by the activated platelets (already mapped), is a matricellular mediator linking the inflammation to the thrombosis of essential thrombocythaemia."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-ET axis: TSLP, from the JAK2/CALR/MPL-mutant (already mapped) megakaryocyte-stromal niche, primes dendritic-cell Th2 polarisation and amplifies the inflammatory dimension of the essential-thrombocythaemia microenvironment."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-thrombosis axis: bradykinin, via B1/B2 receptors on the activated endothelium (already mapped) and platelets (already mapped), amplifies the vasomotor dysregulation and the thromboinflammation of essential thrombocythaemia."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "EPO-ET axis: erythropoietin, in the JAK2V617F (already mapped) haematopoietic niche, modulates erythroid/megakaryocyte lineage bias and macrophage (already mapped) polarisation in the bone marrow (already mapped) of essential thrombocythaemia."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Histamine-ET axis: histamine, released by the expanded mast-cell compartment in JAK2V617F-driven essential thrombocythaemia, signals via H2 receptors on megakaryocytes and bone-marrow stroma, modulating thrombopoiesis and the inflammatory milieu of the myeloproliferative niche."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Melatonin-ET axis: melatonin, via MT1/MT2 receptors on megakaryocyte precursors and bone-marrow stromal cells, modulates circadian haematopoietic rhythms, antioxidant defence, and the JAK2/STAT5-driven proliferative signalling of essential thrombocythaemia."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Androgen-ET axis: testosterone, via androgen receptor signalling on haematopoietic progenitors and bone-marrow stromal cells, modulates megakaryopoiesis, thrombopoietin sensitivity, and the sex-biased thrombotic risk of essential thrombocythaemia."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "ET prolactin: prolactin, via PRLR on macrophages (already mapped) and T-cytotoxic cells (already mapped), modulates the bone-marrow immune milieu; hyperprolactinaemia amplifies the NF-κB (already mapped) and TNF-α (already mapped) megakaryoproliferative cascade of ET."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "ET oxytocin: oxytocin, via OXTR on macrophages (already mapped) and neutrophils (already mapped), attenuates bone-marrow inflammation; oxytocin deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) thrombocythaemic cascade of essential thrombocythemia."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "ET vasopressin: vasopressin, via V2R on macrophages (already mapped) and neutrophils (already mapped), modulates vascular haemostasis; vasopressin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) megakaryoproliferative cascade of ET."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "ET selenium: selenium, as GPx in macrophages (already mapped) and neutrophils (already mapped), scavenges ROS; selenium deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) oxidative megakaryoproliferative cascade of essential thrombocythemia."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "ET iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) polarisation and thrombopoiesis; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) megakaryoproliferative cascade of essential thrombocythemia."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "ET sodium: high dietary sodium promotes macrophage (already mapped) and neutrophil (already mapped) activation; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) skewing amplifies the megakaryoproliferative thrombotic cascade of essential thrombocythemia."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "ET magnesium: magnesium cofactors kinase signalling in macrophages (already mapped) and neutrophils (already mapped); magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) megakaryoproliferative cascade of ET."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "ET copper: copper supports macrophage (already mapped) and neutrophil (already mapped) antioxidant function; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) oxidative megakaryoproliferative cascade of ET."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "ET zinc: zinc cofactors macrophage (already mapped) and neutrophil (already mapped) immune function; zinc deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) megakaryoproliferative thrombotic cascade of ET."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "ET phosphorus: phosphorus, as ATP in macrophages (already mapped) and neutrophils (already mapped), fuels megakaryocyte-platelet signalling; phosphorus dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) thrombotic cascade of ET."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "ET chloride: chloride channels on macrophages (already mapped) and neutrophils (already mapped) regulate ionic homeostasis; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) megakaryoproliferative cascade of ET."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "ET nitrogen: nitric oxide from iNOS in macrophages (already mapped) and neutrophils (already mapped) modulates platelet activation; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) thrombotic cascade of ET."
---

# Essential Thrombocythemia

## Overview

**Essential thrombocythemia (ET)** is a **BCR-ABL1-negative myeloproliferative neoplasm (MPN)** defined by clonal megakaryocytic hyperplasia with sustained thrombocytosis (platelet count ≥450 × 10⁹/L) driven by gain-of-function mutations in JAK2 (~55-60%), CALR (~20-25%), or MPL (~5-8%) — the three major mutually exclusive MPN driver mutations that all constitutively activate the JAK2→STAT5 megakaryopoietic axis. ET is characterized by a generally favorable prognosis with median overall survival approaching that of the general population, but with significant morbidity from **thrombosis** (arterial and venous), **microvascular symptoms** (erythromelalgia, headache, visual disturbances), and **bleeding** at extreme platelet counts. Treatment is risk-stratified using the revised IPSET-Thrombosis score: all high-risk patients (age ≥60 or prior thrombosis) receive aspirin plus cytoreductive therapy — **hydroxyurea** is first-line (PT-1 trial: superior to anagrelide in arterial thrombosis prevention, MF rate, and bleeding) [^harrison-2005-pt1-et]; low-risk and very low-risk patients receive observation or aspirin alone. Long-term complications include post-ET myelofibrosis (~1-2% at 10 years) and AML transformation (<1% at 10 years) [^barbui-2012-ipset].

**Epidemiology:**
- Incidence: ~0.6-2.5 per 100,000/year; prevalence ~30-40 per 100,000
- Median age at diagnosis: ~60 years; bimodal distribution with a younger peak in women aged 30-50 (CALR-associated)
- Slight female predominance overall; younger ET predominantly female (CALR-driven)
- Median OS: approaching general population for low/intermediate risk; high-risk has shortened OS due to thrombotic events and transformation

## Structure

### WHO 2022 diagnostic criteria

All four criteria must be met:

1. **Platelet count ≥450 × 10⁹/L persistently** (sustained on ≥2 measurements at least 1 month apart)
2. **Bone marrow biopsy:** Proliferation of the megakaryocytic lineage with large, mature megakaryocytes with hyperlobated "staghorn" nuclei; no significant increase or left shift in neutrophil granulopoiesis or erythropoiesis; rarely any minor reticulin fibrosis (Grade 1)
3. **Not meeting WHO criteria for:** BCR-ABL1+ CML, PV, PMF, MDS, or other myeloid neoplasms
4. **Presence of JAK2 V617F, CALR exon 9 (del/ins), or MPL exon 10 mutation;** OR in absence of mutation: exclusion of secondary thrombocytosis (reactive: infection, inflammation, iron deficiency, splenectomy) and clonal marker by NGS

### Molecular landscape

**JAK2 V617F (~55-60% of ET):**
Exon 14 GOF mutation in JH2 pseudokinase → constitutive JAK2/STAT5; in ET, JAK2 V617F allele burden (VAF) is typically 25-50% (lower than in PV where VAF is often >50% and frequently homozygous); heterozygous JAK2 in ET → preferential megakaryocytic phenotype (compared to erythroid in PV); JAK2-positive ET has higher thrombosis risk (arterial) than CALR-mutant ET.

**CALR exon 9 mutations (~20-25% of ET):**
Frameshift insertions/deletions generating a novel positively charged C-terminus that binds MPL ECD → constitutive JAK2/STAT5; **type 2 ins5bp** is the predominant CALR mutation in ET (vs type 1 del52bp which predominates in PMF); type 2 CALR → weaker MPL activation → milder megakaryocytic phenotype → ET (not PMF); CALR-mutant ET: younger patients, higher platelet counts, lower thrombosis risk, longer overall survival than JAK2-mutant ET; lower risk of transformation to AML.

**MPL exon 10 mutations (~5-8% of ET):**
W515L, W515K, S505, Y591 — transmembrane/juxtatransmembrane domain GOF → constitutive JAK2 activation without TPO; clinically similar to CALR-mutant ET (younger age, higher platelets, lower thrombosis risk); less common and may be underdiagnosed due to limited panel coverage.

**Triple-negative ET (~15%):**
JAK2/CALR/MPL wild-type; requires careful exclusion of reactive thrombocytosis, early MDS, and atypical CML; if truly clonal (demonstrated by NGS identifying other somatic mutations), prognosis generally good; higher proportion may represent polyclonal reactive conditions.

**Co-mutations:**
Additional mutations in ~20-30% at diagnosis: TET2 (~11%), DNMT3A (~6%), ASXL1 (~5%), SF3B1 (<5%); ASXL1 co-mutation → increased MF transformation risk; SF3B1 co-mutation with JAK2 or CALR → consider whether MDS overlap (ring sideroblasts + thrombocytosis → WHO entity "MDS/MPN with ring sideroblasts and thrombocytosis").

## Function

### Pathophysiology of megakaryocytic expansion

**JAK2/STAT5 → megakaryopoiesis:**
Constitutive JAK2 activation (via JAK2 V617F, CALR/MPL) → STAT5 phosphorylation → BCL-XL (megakaryocyte survival), CCND1 (proliferation), MPL itself (positive feedback) → expanded CFU-MK pool → increased endomitosis → large hyperlobated megakaryocytes → excessive proplatelet formation → sustained thrombocytosis (platelet count 450-2,000+ × 10⁹/L).

**Thrombosis mechanisms:**
- Platelet activation: JAK2 V617F platelets have surface P-selectin expression at rest → activated state → platelet-leukocyte interactions → thrombosis
- NETosis: Neutrophil JAK2 V617F → increased NET formation → endothelial activation → venous thrombosis (DVT, PE, splanchnic vein)
- Platelet count contribution: Platelet count correlates weakly with thrombosis risk — JAK2 allele burden, leukocyte count, and cardiovascular risk factors are better predictors (IPSET model)

**Bleeding at high platelet counts:**
Platelet count >1,500 × 10⁹/L → acquired von Willebrand syndrome (AVWS): platelet surface GPIb absorbs large VWF multimers → depletion of high-molecular-weight VWF → impaired primary hemostasis → paradoxical bleeding (GI bleeding, epistaxis); aspirin contraindicated at platelet count >1,500 × 10⁹/L; cytoreduction first (reduce platelets to safe range); AVWS improves with platelet count normalization.

**Microvascular symptoms:**
- **Erythromelalgia:** Burning, redness, warmth of extremities (hands/feet); caused by platelet-mediated microvascular occlusion + prostaglandin release; aspirin highly effective (within 48 hours)
- **Headache, visual disturbances:** Platelet microthrombi in cerebral microvasculature → transient neurological symptoms; aspirin provides relief
- **Pruritus:** Less prominent than in PV but can occur with JAK2-positive ET

## Pathology

### Risk stratification — revised IPSET-Thrombosis

| Risk Category | Criteria | Annual Thrombosis Rate | Treatment |
|---|---|---|---|
| Very low | Age <60, JAK2-negative, no prior thrombosis | ~0.5%/year | Observation vs aspirin |
| Low | Age <60, JAK2-positive, no prior thrombosis | ~1.5%/year | Aspirin 81-100 mg/day |
| Intermediate | Age ≥60, JAK2-negative, no prior thrombosis | ~2%/year | Aspirin ± cytoreduction (debated) |
| High | Prior thrombosis (any age) OR age ≥60 + JAK2-positive | ~3-5%/year | Aspirin + cytoreduction |

Cardiovascular risk factors (hypertension, diabetes, smoking, dyslipidemia) multiplicatively increase thrombosis risk; leukocytosis (WBC >11 × 10⁹/L) is an additional adverse factor.

### Treatment

**Aspirin:**
Low-dose aspirin 81-100 mg/day is the foundation of ET treatment for symptomatic and JAK2-positive patients; mechanism: irreversible COX-1 inhibition → reduced thromboxane A2 → reduced platelet aggregation; effective for microvascular symptoms (erythromelalgia, headache) and reduces thrombotic events; aspirin carries bleeding risk (especially GI) — balance against thrombosis risk; contraindicated when platelet count >1,500 × 10⁹/L (AVWS → bleeding risk outweighs thrombosis prevention).

**Hydroxyurea (first-line cytoreduction):**
Ribonucleotide reductase inhibitor; reduces all lineages; effective platelet reduction within weeks; PT-1 trial: hydroxyurea + aspirin vs anagrelide + aspirin in high-risk ET; HU arm: fewer arterial thromboses (3.6% vs 9.3% at 2 years), less MF transformation (7.0% vs 13.7%), less bleeding [^harrison-2005-pt1-et]; dose: 500-2,000 mg/day titrated to platelet target <400 × 10⁹/L; standard target: platelet <400 × 10⁹/L + WBC 2-10 × 10⁹/L; toxicities: leg ulcers (~5%), myelosuppression, mucositis; resistance criteria (ELN): platelet >600 × 10⁹/L at ≥2 g/day, or toxicity.

**Anagrelide (second-line):**
Phosphodiesterase 3A (PDE3A) inhibitor → specifically impairs megakaryocyte differentiation → reduces platelet count without significantly affecting other lineages; mechanism unique (not cytotoxic, not RNR inhibition); dose: 0.5-3 mg/day orally in divided doses; PT-1 demonstrated anagrelide inferiority to HU in high-risk ET (more arterial thromboses, more MF, more bleeding); preferred in HU-intolerant patients or women of childbearing age (HU teratogenic); cardiovascular side effects: palpitations, fluid retention, headache (PDE3A also expressed in cardiac tissue).

**Interferon-alpha (IFN-α):**
Pegylated IFN-α (ropeginterferon alfa-2b, peginterferon alfa-2a): suppresses JAK2-mutant clone via STAT1 upregulation → anti-proliferative → preferred in younger patients (<60) and pregnant/potentially pregnant women (safety data better than HU); IFN is not teratogenic (recommended for ET in pregnancy); achieves molecular responses (JAK2 VAF reduction); adverse effects: flu-like symptoms, autoimmune thyroiditis, depression; not FDA-approved specifically for ET (off-label use; approved for PV).

**Ruxolitinib:**
JAK1/2 inhibitor; active in ET (reduces platelet count and spleen) but not FDA-approved for ET; may be considered for HU-intolerant patients in clinical trial settings; RESPONSE-2 trial focused on PV, not ET; ongoing trials evaluating ruxolitinib in ET with high burden.

**Busulfan:**
For elderly HU-intolerant patients; short courses achieve prolonged platelet reduction; limited by mutagenic potential.

### Post-ET myelofibrosis (post-ET MF)

**Transformation rate:** ~1-2% at 10 years (much lower than PV → post-PV MF); ~4-6% at 15-20 years; defined by new BM reticulin fibrosis ≥2, new anemia, leukoerythroblastic blood film, splenomegaly; co-mutations (ASXL1, SRSF2, EZH2) accelerate transformation; CALR-mutant ET has lower MF risk than JAK2-mutant ET.

**Treatment of post-ET MF:**
Similar to PMF: ruxolitinib for symptomatic splenomegaly; fedratinib; momelotinib (ACVR1/JAK1/2, addresses TGF-β-driven anemia); luspatercept for anemia; allo-SCT for eligible intermediate/high-risk post-ET MF.

### AML/blast transformation

**Rate:** <1-2% lifetime risk from ET (lowest of the MPNs); substantially higher in anaplastic progression or with HU-induced myelosuppression in retrospective series (debated); prior alkylator exposure (busulfan, pipobroman) → higher AML risk; JAK2-mutant ET → higher AML risk than CALR-mutant ET; AML from ET: TP53 mutations acquired at transformation; treated as secondary AML (poor prognosis with standard induction; azacitidine+venetoclax if eligible; allo-SCT).

### ET in pregnancy

ET carries risks of:
- **Maternal:** First-trimester miscarriage (placental microvascular thrombosis), thrombosis
- **Fetal:** Placental insufficiency, IUGR, stillbirth
Management:
- Low-risk ET in pregnancy: aspirin 81 mg/day throughout; heparin peri-delivery
- High-risk (prior thrombosis, prior pregnancy loss ×2): add IFN-α (not HU — teratogenic); aspirin + LMWH peri-delivery
- Platelet count typically falls in second trimester (hemodilution) → may not require cytoreduction
- Avoid anagrelide (crosses placenta), HU (teratogenic), ruxolitinib (insufficient data) in pregnancy

## Connections

- `connects-to` → **[MPL](../../03-molecular/mpl/README.md)** — MPL W515L/K mutations (~5-8% ET) cause constitutive JAK2/STAT5 activation independent of TPO; MPL-mutant ET is clinically similar to CALR-mutant ET (lower thrombosis risk vs JAK2); TPO-receptor agonists (eltrombopag, romiplostim) act on wild-type MPL.
- `connects-to` → **[JAK2](../../03-molecular/jak2/README.md)** — JAK2 V617F (~55-60% ET) causes constitutive erythroid/megakaryocytic/granulocytic proliferation; JAK2-positive ET has higher thrombosis risk than CALR-mutant ET; ruxolitinib is active in JAK2 V617F ET but is not FDA-approved for ET.
- `connects-to` → **[CALR](../../03-molecular/calr/README.md)** — CALR mutations (~20-25% ET); type 2 ins5bp is predominant in ET (vs type 1 del52bp in PMF); CALR-mutant ET has lower thrombosis risk, younger age, and longer OS than JAK2-mutant ET; JAK2/CALR/MPL mutations are mutually exclusive.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — ET transforms to post-ET MF (~1-2% at 10 years); megakaryocyte-derived TGF-β1 → reticulin → collagen fibrosis; co-mutations (ASXL1, EZH2, SRSF2) accelerate MF transformation; momelotinib targets ACVR1 to address anemia in post-ET MF.
- `connects-to` → **[Von Willebrand Factor](../../03-molecular/von-willebrand-factor/README.md)** — At platelet counts >1,500 ×10⁹/L, ET causes acquired von Willebrand syndrome — platelet GPIb adsorbs high-molecular-weight VWF multimers and depletes them, impairing primary hemostasis → paradoxical bleeding; aspirin is contraindicated until cytoreduction normalizes the count.
- `connects-to` → **[Polycythemia Vera](../polycythemia-vera/README.md)** — PV and ET are both JAK2-driven MPNs on a phenotypic continuum; PV (JAK2 nearly 100%, often homozygous) skews erythroid while ET skews megakaryocytic; JAK2 V617F-ET can drift toward a PV phenotype; ET has lower post-MF and AML transformation risk than PV.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Clonal megakaryocytic hyperplasia drives sustained thrombocytosis; JAK2 V617F platelets are constitutively activated (resting P-selectin) → platelet-leukocyte aggregates and thrombosis; erythromelalgia from platelet microvascular occlusion responds rapidly to aspirin.
- `connects-to` → **[Disseminated Intravascular Coagulation](../disseminated-intravascular-coagulation/README.md)** — Essential thrombocythemia and DIC are opposite poles of platelet pathology: ET clonally overproduces platelets causing thrombosis (and, at extreme counts, acquired von Willebrand bleeding), while DIC systemically consumes platelets and clotting factors — too many versus too few.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Essential thrombocythemia is a clonal bone marrow disease: a JAK2, CALR, or MPL mutation drives autonomous megakaryocyte hyperplasia, so the marrow shows large, mature, clustered megakaryocytes without the dense fibrosis of primary myelofibrosis — a key WHO distinction.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — Mild splenomegaly is common in essential thrombocythemia from extramedullary hematopoiesis and pooling; progressive splenic enlargement signals transformation to post-ET myelofibrosis, and prior splenectomy paradoxically raises platelet counts and thrombosis risk.
- `connects-to` → **[Myeloproliferative Neoplasms](../myeloproliferative-neoplasms/README.md)** — Essential thrombocythemia is one of the three classic Philadelphia-negative myeloproliferative neoplasms (with PV and PMF): a JAK2/CALR/MPL-driven clonal overproduction—here of platelets—sharing thrombosis risk and the capacity to evolve into myelofibrosis or AML.
- `connects-to` → **[Myelofibrosis](../myelofibrosis/README.md)** — Essential thrombocythemia can progress to post-ET myelofibrosis: over years the clone drives marrow reticulin fibrosis, so the platelet-rich blood picture gives way to splenomegaly, cytopenias and a leukoerythroblastic film, converging with primary myelofibrosis.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Thrombosis—not bleeding—is the main danger of essential thrombocythemia: the dysfunctional excess platelets and JAK2 mutation create a prothrombotic state causing arterial and venous events, including VTE and unusual-site (splanchnic) thrombosis; aspirin lowers risk.
- `connects-to` → **[Chronic Myeloid Leukemia](../cml/README.md)** — ET and CML are both chronic myeloproliferative neoplasms but driven differently: CML by the BCR-ABL fusion tyrosine kinase (treatable with imatinib), ET by JAK2/CALR/MPL mutations driving platelet overproduction—both can progress to fibrosis or acute leukemia.
- `connects-to` → **[Stroke](../stroke/README.md)** — ET predisposes to stroke: the excess, often dysfunctional platelets promote arterial thrombosis, so TIAs and stroke are feared complications—low-dose aspirin and cytoreduction lower this risk, a rare case where too many platelets cause clots, not bleeding.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — ET and polycythemia vera show how one marrow can overproduce different lineages: ET expands megakaryocytes and platelets while PV expands erythrocytes, yet both arise from JAK2-pathway mutations—lineage skewing of a shared clonal stem-cell defect sets the phenotype.
- `connects-to` → **[Thrombin](../../03-molecular/thrombin/README.md)** — Excess platelets in essential thrombocythemia tip toward thrombin-driven clotting: the high, often dysfunctional platelet mass promotes both arterial and venous thrombosis, so low-dose aspirin and cytoreduction lower the clotting risk that dominates ET's morbidity.
- `connects-to` → **[AML](../aml/README.md)** — Essential thrombocythemia carries a small but real risk of transforming to AML: as a clonal myeloproliferative neoplasm, ET can evolve through myelofibrosis to acute leukemia, a risk raised by some cytoreductive drugs—the feared long-term endpoint.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Essential thrombocythemia often raises neutrophils too: the JAK2-driven clone expands multiple myeloid lineages, so leukocytosis often accompanies the thrombocytosis and itself predicts higher thrombosis risk—ET is a panmyeloid, not platelet-only, disease.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Essential thrombocythemia clots at the endothelium: excess, often dysfunctional platelets interact with the vessel lining to cause microvascular and large-vessel thrombosis, so antiplatelet therapy targeting this platelet-endothelial interface prevents the main complication.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Essential thrombocythemia is a classic cause of splanchnic vein thrombosis: the prothrombotic platelet excess can clot the hepatic or portal veins (Budd-Chiari), so unexplained abdominal vein thrombosis should prompt testing for JAK2 and an underlying MPN.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Essential thrombocythemia produces distinctive neurovascular symptoms: microvascular platelet plugging causes headaches, visual disturbance and erythromelalgia, and it raises stroke and TIA risk—so the nervous system often signals the disease before a major clot occurs.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — Essential thrombocythemia complicates pregnancy through the placenta: the thrombotic tendency causes placental clots, miscarriage, and growth restriction, so pregnant patients are managed with low-dose aspirin and sometimes heparin to protect the placenta.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Essential thrombocythemia announces itself in the skin as erythromelalgia: platelet microthrombi in small vessels cause burning, red, painful hands and feet, a near-specific symptom that dramatically improves with low-dose aspirin.
- `connects-to` → **[Gout](../gout/README.md)** — Essential thrombocythemia's high cell turnover can cause gout: rapid platelet and cell production raises uric acid, so hyperuricemia and gout flares accompany this and other myeloproliferative neoplasms.
- `connects-to` → **[Thrombopoietin](../../03-molecular/thrombopoietin/README.md)** — Essential thrombocythemia hijacks thrombopoietin signaling: TPO normally tells the marrow how many platelets to make through the MPL receptor, but ET's JAK2, CALR, and MPL mutations switch that pathway on permanently, churning out platelets without the hormone's command.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — All of ET's driver mutations converge on STAT: JAK2, CALR, and MPL defects all end up activating STAT transcription factors, the shared switch that turns on the genes driving runaway platelet production—why JAK-STAT inhibitors are used in the disease.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Platelets in essential thrombocythemia clot through calcium: calcium signaling triggers platelet activation and aggregation, so the vast excess of platelets, primed to release and respond to calcium, tips patients toward the thromboses that menace them.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Platelet-rich blood in essential thrombocythemia can fake high potassium: the enormous platelet mass leaks potassium after the sample clots, producing pseudohyperkalemia—a lab artifact to recognize before treating a number that isn't real.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Essential thrombocythemia strikes the brain's small vessels: excess platelets cause headaches, visual disturbance, TIAs and burning red extremities (erythromelalgia), microvascular symptoms that low-dose aspirin often relieves.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6 marks the line between reactive and clonal thrombocytosis: this cytokine drives platelet production in inflammation, so a high count from infection or cancer must be told apart from the clonal overproduction that defines essential thrombocythemia.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Essential thrombocythemia starves fingertips of oxygen: clumps of excess platelets plug tiny vessels, causing the burning, red, oxygen-starved hands and feet of erythromelalgia and risking digital ischemia.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Essential thrombocythemia threatens the heart: its thrombotic tendency raises the risk of coronary clots and heart attacks, part of why even symptom-free patients may need aspirin and cytoreduction.
- `connects-to` → **[Fibrinogen](../../03-molecular/fibrinogen/README.md)** — Essential thrombocythemia turns fibrinogen into clots: the swollen platelet mass, activating with fibrinogen, builds the thromboses—strokes, heart attacks, and vein clots—that are the disease's main danger.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — ET is confirmed under the microscope: the marrow biopsy shows clusters of enlarged, staghorn megakaryocytes, the clue that with JAK2 and CALR testing distinguishes it from reactive thrombocytosis.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — ET clots the gut's veins: splanchnic and mesenteric vein thrombosis can be the first sign, so an unprovoked abdominal-vein clot prompts testing for the JAK2 mutation behind the disease.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — ET can scar into myelofibrosis: over years, reticulin and collagen fibrosis gradually replace the marrow, the feared post-ET transformation that brings cytopenias and splenomegaly.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows ET's overgrown platelet factory: the marrow swells with large, mature megakaryocytes with deeply lobulated nuclei, churning out the giant, abnormal platelets that flood the blood.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — ET can briefly blind: clumps of excess platelets sludge through the retinal microvessels, causing fleeting visual disturbances and amaurosis that warn of the disease's thrombotic risk.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — The kidney feels ET's high cell turnover: a surplus of uric acid from rapid platelet production crystallizes in the tubules toward gout and urate nephropathy, while microthrombi can impair renal blood flow.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — ET pesters the nervous system in miniature: platelet plugs in small vessels cause headache, visual blurring, transient ischemic attacks, and the burning red hands and feet of erythromelalgia — symptoms that often ease with aspirin.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — High platelets complicate pregnancy: ET raises the risk of miscarriage and placental thrombosis, so affected women are managed with aspirin and sometimes heparin to protect the pregnancy.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — At extreme counts ET paradoxically bleeds: very high platelets soak up von Willebrand factor into an acquired deficiency, so gastrointestinal bleeding can occur even as the disease otherwise drives clotting.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — ET's clots are mostly arterial: its hyperactive platelets favor arterial thrombosis on top of any atherosclerotic plaque, which is why heart attack and stroke dominate its risk and why low-dose aspirin and cardiovascular-risk control are central to management.
- `connects-to` → **[TET2](../../03-molecular/tet2/README.md)** — Extra mutations shape the course: TET2 and other clonal-hematopoiesis genes often sit alongside the JAK2 or CALR driver, expanding the malignant clone and adding to the thrombotic risk and the chance of progression to myelofibrosis or leukemia.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron tells the true thrombocytosis from the false: iron deficiency itself drives a reactive rise in platelets that mimics ET, so checking iron status is a basic step in deciding whether a high platelet count is clonal disease or simple deficiency.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Chronic inflammation drives the MPN clone: JAK2-activated NF-κB signaling fuels the inflammatory cytokine state behind ET's symptoms and its prothrombotic tendency, a target of interferon and JAK-inhibitor therapy.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Marrow macrophages support the overgrowth: they help build the inflammatory niche that favors the mutant megakaryocyte clone in ET, part of the microenvironment that sustains the disease.
- `connects-to` → **[Pulmonary Arterial Hypertension](../pulmonary-arterial-hypertension/README.md)** — The clotting disorder can choke the lungs: ET raises the risk of pulmonary hypertension through in-situ microthrombi, chronic thromboembolism, and extramedullary hematopoiesis, straining the right heart.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — Epigenetic mutations stack on the driver: DNMT3A and other clonal-hematopoiesis mutations co-occur with JAK2/CALR/MPL in ET, shaping clonal evolution and the risk of progression to myelofibrosis or leukemia.
- `connects-to` → **[Myelodysplastic Syndromes](../mds/README.md)** — The clone can shift toward dysplasia: ET sits on the myeloid spectrum and can evolve into a myelodysplastic/myeloproliferative overlap or secondary MDS, especially after cytotoxic therapy.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Arterial clots can wreck the heart: ET's thrombotic risk includes coronary events whose myocardial damage leads to heart failure, the cardiac counterpart of its stroke and limb-ischemia complications.
- `connects-to` → **[Hepatocellular Carcinoma](../hcc/README.md)** — It clots the liver's veins: ET is a leading cause of Budd-Chiari syndrome, hepatic vein thrombosis that congests the liver toward cirrhosis and, over years, hepatocellular carcinoma — sometimes the first sign of the MPN.
- `connects-to` → **[Inherited Thrombophilia](../inherited-thrombophilia/README.md)** — An acquired thrombophilia stacked on inherited ones: ET's overproduced, hyperreactive platelets create an acquired prothrombotic state that multiplies clot risk when a co-existing inherited thrombophilia is also present.
- `connects-to` → **[Paroxysmal Nocturnal Hemoglobinuria](../pnh/README.md)** — It shares the unusual-site clotting puzzle: like paroxysmal nocturnal hemoglobinuria, ET is an acquired clonal disorder that causes thrombosis in unusual sites such as the splanchnic veins, both considered when such clots appear unexplained.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — It can burn out into anemia: as ET evolves toward a spent, myelofibrotic phase, marrow fibrosis and chronic inflammation replace the platelet excess with an anemia carrying a chronic-disease component.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Its cytoreductive drugs can strip defenses: hydroxyurea and other agents used to lower the platelet count in ET can cause neutropenia, leaving patients more vulnerable to serious infection and sepsis.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A chronic clonal disease weighs on mood: living with the thrombosis-and-transformation risk of a lifelong myeloproliferative neoplasm, plus its constitutional symptoms, contributes to depression and reduced quality of life.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Microvascular platelet plugs burn the extremities: erythromelalgia — red, hot, painful hands and feet from platelet microthrombi — is a classic symptom of essential thrombocythemia, relieved by aspirin.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Its hydroxyurea ulcerates the skin: the cytoreductive drug hydroxyurea used in essential thrombocythemia characteristically causes painful, slow-healing leg ulcers, often forcing a change of therapy.
- `connects-to` → **[Basal Cell Carcinoma](../basal-cell-carcinoma/README.md)** — Long-term hydroxyurea raises skin-cancer risk: prolonged hydroxyurea therapy for essential thrombocythemia is associated with non-melanoma skin cancers, including basal and squamous cell carcinomas.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Platelet excess burns the extremities: essential thrombocythemia classically causes erythromelalgia — red, hot, painful hands and feet from microvascular platelet plugging — and digital ischaemia, relieved by aspirin.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It clots the gut's veins yet also bleeds it: ET causes splanchnic and portal vein thrombosis with splenomegaly, while at very high platelet counts an acquired von Willebrand defect causes GI bleeding.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Clot-and-transformation risk breeds worry: the lifelong threat of thrombosis and bleeding and the small risk of progression to myelofibrosis or leukaemia in ET foster chronic health anxiety.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It can enlarge the spleen: mild to moderate splenomegaly from extramedullary haematopoiesis and splenic platelet sequestration occurs in essential thrombocythemia.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Its clots can reach the lungs: the thrombotic tendency of ET causes pulmonary embolism, and microvascular pulmonary thrombosis can contribute to pulmonary hypertension.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Clots and urate strain the kidney: microvascular thrombosis and hyperuricaemia from high cell turnover can impair renal function, and renal vein thrombosis can occur in ET.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its platelets clot the arteries: essential thrombocythemia causes arterial and venous thrombosis — stroke, myocardial infarction and the burning erythromelalgia of digital microvascular occlusion.
- `connects-to` → **[Aspirin](../../../03-medicine/01-modern/04-cardio/aspirin/README.md)** — Low-dose aspirin is standard: by inhibiting the excess platelets, aspirin reduces the thrombotic and erythromelalgia risk of essential thrombocythemia, alongside cytoreduction in high-risk disease.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — The myeloproliferative marrow reaches bone: the expanded marrow can cause bone discomfort, and progression to myelofibrosis brings a bulky spleen and skeletal symptoms.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Cytoreduction with hydroxyurea: in high-risk essential thrombocythaemia, hydroxyurea lowers the platelet count to prevent thrombosis, the main cytoreductive chemotherapy alongside interferon.
- `connects-to` → **[Antiphospholipid Syndrome](../antiphospholipid-syndrome/README.md)** — Two causes of clots that overlap: like antiphospholipid syndrome, essential thrombocythaemia drives both arterial and venous thrombosis, and the two can coexist and compound the risk.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — JAK inhibition for resistant disease: ruxolitinib and other JAK inhibitors, exploiting the JAK2 V617F mutation, treat essential thrombocythaemia that resists hydroxyurea, with interferon a non-mutagenic alternative.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — Activated platelets clot the arteries: essential thrombocythaemia drives arterial thrombosis — stroke, MI and digital ischaemia (erythromelalgia) — through hyperreactive platelets acting on the arterial wall, the target of low-dose aspirin.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — It clots the splanchnic veins: like other myeloproliferative neoplasms, essential thrombocythaemia characteristically causes hepatic- and portal-vein thrombosis (Budd-Chiari), congesting the liver lobule, sometimes before the platelet count rises.
- `connects-to` → **[Heparin-Induced Thrombocytopenia](../heparin-induced-thrombocytopenia/README.md)** — Platelet count, then platelet activation: essential thrombocythaemia thromboses with a high platelet count, whereas heparin-induced thrombocytopenia thromboses as platelets fall — opposite counts united by pathological platelet activation.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Arterial thrombosis and the heart: ET's hyperreactive platelets cause arterial thrombi including myocardial infarction, a leading cause of morbidity that aspirin and cytoreduction aim to prevent.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — Microvascular thrombosis: beyond large arteries, ET causes microvascular occlusion—erythromelalgia and renal microthrombi reaching the glomerulus—relieved promptly by low-dose aspirin.
- `connects-to` → **[CMML](../cmml/README.md)** — Across the myeloid-neoplasm family: ET is a classic myeloproliferative neoplasm of platelets, while CMML is a myelodysplastic/myeloproliferative overlap of monocytes—neighbouring clonal marrow diseases that can transform to AML.
- `connects-to` → **[Hemophilia A](../hemophilia-a/README.md)** — Paradoxical bleeding: extreme thrombocytosis in ET adsorbs and clears von Willebrand factor, causing an acquired von Willebrand syndrome—a bleeding tendency despite high platelets, reached differently than in haemophilia.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Erythromelalgia: platelet microthrombi in small vessels cause burning, red, painful extremities and acrocyanosis—a microvascular and small-fibre disturbance dramatically relieved by aspirin.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Compounded thrombosis risk: the prothrombotic state of essential thrombocythemia adds to the hypercoagulability of COVID-19, raising the risk of arterial and venous clots during infection.
- `connects-to` → **[Type I Interferon](../../03-molecular/type-i-interferon/README.md)** — Clone-reducing therapy: pegylated interferon-alpha is a disease-modifying treatment for essential thrombocythemia that can shrink the JAK2- or CALR-mutant clone, unlike purely cytoreductive drugs.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Epigenetic co-mutation: EZH2 and other epigenetic-regulator mutations co-occur with the driver lesions of essential thrombocythemia and contribute to progression toward myelofibrosis.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Downstream of JAK2: the driver mutations of essential thrombocythemia activate JAK-STAT and the parallel PI3K-AKT pathway, together sustaining clonal megakaryocyte proliferation.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Clonal inflammation: TNF-α from the malignant clone gives essential thrombocythemia cells a survival advantage over normal progenitors and drives the constitutional symptoms of the MPN.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Inflammasome activation: JAK2-driven NLRP3-inflammasome activation contributes to the chronic inflammatory state of essential thrombocythemia and its thrombotic risk.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Marrow angiogenesis: elevated VEGF increases bone-marrow microvessel density in essential thrombocythemia, part of the proliferative MPN microenvironment.
- `connects-to` → **[PF4](../../03-molecular/pf4/README.md)** — Platelet activation: PF4 released from the markedly expanded, activated platelet mass of essential thrombocythemia marks the platelet hyperreactivity behind its characteristic thrombotic risk.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — MPN inflammation: S100A8/A9 from the expanded myeloid compartment amplifies the chronic inflammation of essential thrombocythemia, contributing to its thrombotic and constitutional symptoms.
- `connects-to` → **[RUNX1](../../03-molecular/runx1/README.md)** — Leukaemic transformation: acquired RUNX1 mutations mark the progression of essential thrombocythemia toward myelofibrosis and acute myeloid leukaemia, a feared late evolution.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — The hyperreactive platelets of essential thrombocythemia generate thromboxane A2, the target of the low-dose aspirin used to reduce the arterial thrombosis and the burning erythromelalgia characteristic of the disease.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — PDGF released by the clonal megakaryocytes stimulates marrow fibroblasts, driving the reticulin fibrosis of post-ET myelofibrosis—the fibrotic transformation that marks disease progression in a subset of patients.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — The increased hematopoietic turnover of essential thrombocythemia raises urate through xanthine oxidase, causing the secondary hyperuricemia and gout that can complicate this myeloproliferative neoplasm.
- `connects-to` → **[SF3B1](../../03-molecular/sf3b1/README.md)** — Spliceosome mutations such as SF3B1, acquired alongside the JAK2/CALR/MPL driver, mark the essential thrombocythemia more likely to progress to myelofibrosis or acute leukemia, refining its otherwise indolent prognosis.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — Should essential thrombocythemia transform to acute leukemia, the blasts become dependent on anti-apoptotic BCL-2, a vulnerability targeted by venetoclax in the otherwise dismal post-MPN leukemia.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement activation generating C3 fragments amplifies the platelet and neutrophil activation of essential thrombocythemia, an inflammatory limb of the prothrombotic state that drives its arterial and venous thrombosis.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — The JAK2, CALR and MPL driver mutations (all already mapped) activate the MAPK-ERK cascade alongside JAK-STAT, driving the megakaryocyte proliferation that produces the thrombocytosis of essential thrombocythemia.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — The same constitutively active receptor-kinase signaling engages PI3K (AKT already mapped) as a third effector pathway supporting megakaryocyte growth and survival in essential thrombocythemia.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 inactivation drives the transformation of essential thrombocythemia to acute myeloid leukemia, a feared progression alongside the RUNX1 lesions already mapped.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — The PI3K-AKT-mTOR axis (AKT and PIK3CA already mapped) operates downstream of constitutive JAK2 signaling to drive the megakaryocyte proliferation of essential thrombocythemia.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation contributes to the clonal expansion and disease progression of the myeloproliferative neoplasm essential thrombocythemia.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR-MyD88-NF-κB innate signaling (NF-κB already mapped) sustains the chronic inflammatory milieu that characterizes and propels myeloproliferative neoplasms including essential thrombocythemia.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — Type-I-interferon signaling through STAT1 (type-I-interferon mapped) underlies the disease-modifying activity of interferon therapy in essential thrombocythemia.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 expressed by megakaryocytes contributes to the marrow microenvironment and fibrotic potential of essential thrombocythemia.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN restraint of PI3K-AKT-mTOR signaling (AKT, PIK3CA and mTOR mapped) downstream of JAK2-driven activation shapes the clonal proliferation of essential thrombocythemia.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING amplifies the chronic inflammatory marrow milieu and NET-driven thrombosis risk of essential thrombocythemia.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β already mapped) drives the marrow fibrosis underlying the progression of essential thrombocythemia toward myelofibrosis.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors, restrained by JAK2-PI3K-AKT signaling, modulate the survival and quiescence of the clonal stem cells of essential thrombocythemia.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK1/2 signaling (alongside the mapped JAK2) transduces the constitutive thrombopoietin-receptor activation driving megakaryocyte proliferation in essential thrombocythemia.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the megakaryocyte and clonal stem-cell signaling of essential thrombocythemia.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α shapes the bone-marrow niche and metabolic state of the clonal megakaryocytes of essential thrombocythemia.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis and contributes to the leukemic evolution of essential thrombocythemia.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated cytotoxic immunosurveillance targets the neoantigen-bearing CALR-mutant clone of essential thrombocythemia.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6-cyclin-D cell-cycle activity drives the JAK2-fueled megakaryocyte and progenitor proliferation of essential thrombocythemia.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of the clonal hematopoietic cells of essential thrombocythemia.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the survival of the JAK2/CALR-mutant clone of essential thrombocythemia.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of the thrombopoietin receptor (MPL already mapped) participates in the megakaryocyte proliferation of essential thrombocythemia.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-family chemokine signaling participates in the bone-marrow niche and inflammatory interactions of essential thrombocythemia.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the megakaryocyte and bone-marrow-niche interactions of essential thrombocythemia.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the inflammatory bone-marrow microenvironment of essential thrombocythemia.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory bone-marrow microenvironment of essential thrombocythemia.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the clonal hematopoiesis of essential thrombocythemia.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the megakaryocyte and immune signaling of essential thrombocythemia.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Endothelial-platelet balance: nitric oxide normally restrains platelet activation and keeps vessels dilated, so impaired endothelial nitric-oxide function alongside the excess platelets of essential thrombocythaemia tips the balance toward the thrombosis that dominates its risk.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Arterial thrombosis: the thrombocytosis of essential thrombocythaemia predisposes to arterial events including myocardial infarction and stroke, and troponin elevation marks the cardiac injury of these thrombotic complications.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Platelet mediator: platelets are the body's main store of serotonin, released on aggregation to cause vasoconstriction, so the excess dysfunctional platelets of essential thrombocythaemia contribute to microvascular events such as erythromelalgia.
- `connects-to` → **[ADAMTS13](../../03-molecular/adamts13/README.md)** — Acquired von Willebrand syndrome: at extreme platelet counts the high-molecular-weight von Willebrand multimers (already mapped) are adsorbed and cleared, and this acquired von Willebrand syndrome causes the paradoxical bleeding of essential thrombocythaemia.
- `connects-to` → **[Protein C](../../03-molecular/protein-c/README.md)** — Thrombotic risk: the thrombosis of essential thrombocythaemia reflects a prothrombotic tilt, and coexisting deficiency of the natural anticoagulant protein C (thrombin already mapped) further raises the risk that drives cytoreduction and antiplatelet therapy.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Inflammatory milieu: essential thrombocythaemia carries a chronic inflammatory state, and the anti-inflammatory IL-10 counterbalances the TNF, IL-6 and IL-1 (already mapped) driven by JAK-STAT signalling that shapes the myeloproliferative phenotype.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Microvascular vasoconstriction: endothelin-1 and the platelet-derived vasoactive mediators (serotonin already mapped) contribute to the microvascular vasoconstriction behind the erythromelalgia and neurological symptoms of essential thrombocythaemia.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — Endothelial activation: the angiopoietin-Tie2 axis reflects the endothelial activation of the prothrombotic state of essential thrombocythaemia, part of the endothelium's contribution (von Willebrand factor already mapped) to its thrombosis.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Pulmonary thrombosis: essential thrombocythaemia predisposes to pulmonary embolism and, over time, chronic thromboembolic pulmonary hypertension, part of the venous and arterial thrombotic burden of the disease.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Inflammatory milieu: IL-4 and the M2 macrophage arm (IL-10 already mapped) shape the chronic inflammation (IL-6 and TNF already mapped) of the myeloproliferative marrow, part of the disease biology of essential thrombocythaemia.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Marrow adipose crosstalk: the marrow adipocytes and their adipokine leptin signal to the clonal megakaryocytes, part of the bone-marrow (already mapped) microenvironment of essential thrombocythaemia.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Adipokine microenvironment: adiponectin, with leptin (already mapped), from the marrow adipose tissue signals to the myeloproliferative clone, part of the metabolic microenvironment of essential thrombocythaemia.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipokine milieu: resistin, with leptin and adiponectin (already mapped), completes the marrow-adipocyte adipokine signalling of the metabolic microenvironment of essential thrombocythaemia.
- `connects-to` → **[AML](../aml/README.md)** — Leukaemic transformation: essential thrombocythaemia can transform to acute myeloid leukaemia (the blast phase, RUNX1 already mapped), a feared outcome of the myeloproliferative neoplasm.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron deficiency and PV masking: coexisting iron deficiency can lower the haemoglobin and mask an underlying polycythaemia vera (already mapped) as essential thrombocythaemia, and drives the microcytosis of the disorder.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — M2 marrow microenvironment: IL-13, with IL-4 (already mapped), drives the M2 macrophage arm of the inflammatory (IL-6 already mapped) marrow microenvironment of essential thrombocythaemia.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Immune surveillance: the NK cells contribute to the immune surveillance of the JAK2 (already mapped)-mutant clone, and the interferon (type-I interferon already mapped) therapy augments the anti-clonal immunity of essential thrombocythaemia.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — Thrombopoietin source: the hepatocytes are the main source of the thrombopoietin (already mapped), the MPL (already mapped) ligand whose signalling is dysregulated in essential thrombocythaemia.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 anti-clonal arm: the IFN-γ of the T and NK (already mapped) cells is the type-II interferon arm of the anti-clonal immunity (type-I interferon therapy already mapped) of the JAK2-mutant essential thrombocythaemia.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune surveillance of the essential-thrombocythaemia clone.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the inflammatory milieu of essential thrombocythaemia.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the chronic inflammation (IL-6 and TNF already mapped) of the essential-thrombocythaemia clone.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the inflammatory milieu of essential thrombocythaemia.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Clone immune surveillance: the cytotoxic T cells (perforin already mapped) provide the anti-clonal immune surveillance of the JAK2/CALR (already mapped) mutant clone, an arm engaged by the interferon (type-I interferon already mapped) therapy of essential thrombocythaemia.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the cytokines of the chronic inflammation and support the anti-clonal immunity engaged by the interferon (already mapped) therapy of essential thrombocythaemia.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) links the complement to the myeloid inflammation and the immunothrombosis of essential thrombocythaemia.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its activation (with C3 already mapped) contribute to the chronic inflammation and the thrombotic risk of essential thrombocythaemia.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the thromboinflammatory milieu of essential thrombocythaemia.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement/coagulation crosstalk: the C1-esterase inhibitor regulates both the complement (C3, C5, C5aR1 and factor H already mapped) and the contact-coagulation systems at the interface of the immunothrombosis of essential thrombocythaemia.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Thromboinflammation: osteopontin, released by the activated platelets (already mapped), is a matricellular mediator linking the inflammation to the thrombosis of essential thrombocythaemia.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-ET axis: TSLP, from the JAK2/CALR/MPL-mutant (already mapped) megakaryocyte-stromal niche, primes dendritic-cell Th2 polarisation and amplifies the inflammatory dimension of the essential-thrombocythaemia microenvironment.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-thrombosis axis: bradykinin, via B1/B2 receptors on the activated endothelium (already mapped) and platelets (already mapped), amplifies the vasomotor dysregulation and the thromboinflammation of essential thrombocythaemia.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — EPO-ET axis: erythropoietin, in the JAK2V617F (already mapped) haematopoietic niche, modulates erythroid/megakaryocyte lineage bias and macrophage (already mapped) polarisation in the bone marrow (already mapped) of essential thrombocythaemia.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Histamine-ET axis: histamine, released by the expanded mast-cell compartment in JAK2V617F-driven essential thrombocythaemia, signals via H2 receptors on megakaryocytes and bone-marrow stroma, modulating thrombopoiesis and the inflammatory milieu of the myeloproliferative niche.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Melatonin-ET axis: melatonin, via MT1/MT2 receptors on megakaryocyte precursors and bone-marrow stromal cells, modulates circadian haematopoietic rhythms, antioxidant defence, and the JAK2/STAT5-driven proliferative signalling of essential thrombocythaemia.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Androgen-ET axis: testosterone, via androgen receptor signalling on haematopoietic progenitors and bone-marrow stromal cells, modulates megakaryopoiesis, thrombopoietin sensitivity, and the sex-biased thrombotic risk of essential thrombocythaemia.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — ET prolactin: prolactin, via PRLR on macrophages (already mapped) and T-cytotoxic cells (already mapped), modulates the bone-marrow immune milieu; hyperprolactinaemia amplifies the NF-κB (already mapped) and TNF-α (already mapped) megakaryoproliferative cascade of ET.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — ET oxytocin: oxytocin, via OXTR on macrophages (already mapped) and neutrophils (already mapped), attenuates bone-marrow inflammation; oxytocin deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) thrombocythaemic cascade of essential thrombocythemia.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — ET vasopressin: vasopressin, via V2R on macrophages (already mapped) and neutrophils (already mapped), modulates vascular haemostasis; vasopressin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) megakaryoproliferative cascade of ET.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — ET selenium: selenium, as GPx in macrophages (already mapped) and neutrophils (already mapped), scavenges ROS; selenium deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) oxidative megakaryoproliferative cascade of essential thrombocythemia.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — ET iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) polarisation and thrombopoiesis; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) megakaryoproliferative cascade of essential thrombocythemia.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — ET sodium: high dietary sodium promotes macrophage (already mapped) and neutrophil (already mapped) activation; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) skewing amplifies the megakaryoproliferative thrombotic cascade of essential thrombocythemia.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — ET magnesium: magnesium cofactors kinase signalling in macrophages (already mapped) and neutrophils (already mapped); magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) megakaryoproliferative cascade of ET.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — ET copper: copper supports macrophage (already mapped) and neutrophil (already mapped) antioxidant function; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) oxidative megakaryoproliferative cascade of ET.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — ET zinc: zinc cofactors macrophage (already mapped) and neutrophil (already mapped) immune function; zinc deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) megakaryoproliferative thrombotic cascade of ET.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — ET phosphorus: phosphorus, as ATP in macrophages (already mapped) and neutrophils (already mapped), fuels megakaryocyte-platelet signalling; phosphorus dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) thrombotic cascade of ET.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — ET chloride: chloride channels on macrophages (already mapped) and neutrophils (already mapped) regulate ionic homeostasis; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) megakaryoproliferative cascade of ET.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — ET nitrogen: nitric oxide from iNOS in macrophages (already mapped) and neutrophils (already mapped) modulates platelet activation; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) thrombotic cascade of ET.

[^harrison-2005-pt1-et]: Harrison CN, Campbell PJ, Buck G, et al. Hydroxyurea compared with anagrelide in high-risk essential thrombocythemia. *N Engl J Med.* 2005;353(1):33-45. [doi:10.1056/NEJMoa043800](https://doi.org/10.1056/NEJMoa043800) · [PubMed 16000354](https://pubmed.ncbi.nlm.nih.gov/16000354/)
[^barbui-2012-ipset]: Barbui T, Finazzi G, Carobbio A, et al. Development and validation of an International Prognostic Score of thrombosis in World Health Organization-essential thrombocythemia (IPSET-thrombosis). *Blood.* 2012;120(26):5128-5133. [doi:10.1182/blood-2012-07-444067](https://doi.org/10.1182/blood-2012-07-444067) · [PubMed 23086758](https://pubmed.ncbi.nlm.nih.gov/23086758/)
