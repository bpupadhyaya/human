---
schema: human-scale-entry/v1
id: venous-thromboembolism
name: Venous Thromboembolism
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Venous thromboembolism (VTE; DVT + PE) affects ~1-2 per 1,000 adults/year; Virchow's triad (stasis, hypercoagulability, endothelial injury) drives pathogenesis. DOACs (apixaban, rivaroxaban) are first-line; catheter-directed thrombolysis and ECMO for massive PE."
aliases: ["VTE", "venous thromboembolism", "DVT", "deep vein thrombosis", "PE", "pulmonary embolism", "deep venous thrombosis", "thrombosis venous", "venous clot"]
sources:
  - id: agnelli-2013-amplify-apixaban-vte
    type: peer-reviewed
    cite: "Agnelli G, Buller HR, Cohen A, et al. Oral apixaban for the treatment of acute venous thromboembolism. N Engl J Med. 2013;369(9):799-808."
    doi: "10.1056/NEJMoa1302507"
    pmid: "23808982"
    url: "https://doi.org/10.1056/NEJMoa1302507"
  - id: bauersachs-2010-einstein-rivaroxaban
    type: peer-reviewed
    cite: "EINSTEIN Investigators. Oral rivaroxaban for symptomatic venous thromboembolism. N Engl J Med. 2010;363(26):2499-2510."
    doi: "10.1056/NEJMoa1007903"
    pmid: "21128814"
    url: "https://doi.org/10.1056/NEJMoa1007903"
  - id: konstantinides-2020-esc-pe
    type: peer-reviewed
    cite: "Konstantinides SV, Meyer G, Becattini C, et al. 2019 ESC Guidelines for the diagnosis and management of acute pulmonary embolism. Eur Heart J. 2020;41(4):543-603."
    doi: "10.1093/eurheartj/ehz405"
    pmid: "31504429"
    url: "https://doi.org/10.1093/eurheartj/ehz405"
cross_links:
  - target: 01-human/03-molecular/thrombin
    relation: connects-to
    note: "Thrombin (FIIa) generates fibrin at the core of venous thrombi; stasis → contact activation → FXI → FIXa → FX → thrombin → fibrin-rich clot; DOACs (dabigatran, rivaroxaban, apixaban) target thrombin or FXa → prevent and treat VTE; LMWH inhibits thrombin via antithrombin."
  - target: 01-human/07-system/antiphospholipid-syndrome
    relation: connects-to
    note: "APS causes recurrent DVT/PE in young adults; triple-positive aPL (LA + aCL + anti-B2GPI) confers >10% annual thrombotic risk; warfarin INR 2-3 is superior to DOACs for VTE in APS; rivaroxaban doubled arterial event risk in triple-positive APS (TRAPS trial)."
  - target: 01-human/03-molecular/von-willebrand-factor
    relation: connects-to
    note: "Elevated VWF promotes venous thrombosis by augmenting platelet recruitment and fibrin network formation; VWF is an acute-phase protein elevated in surgery, infection, cancer → increased VTE risk; ABO blood group affects VWF level (type O ~25% lower VWF → lower baseline VTE risk)."
  - target: 01-human/03-molecular/protein-c
    relation: connects-to
    note: "Protein C deficiency (PROC mutations) is a rare but high-risk inherited thrombophilia (0.3% prevalence; 5-10× VTE risk); APC inactivates FVa/FVIIIa; warfarin-induced skin necrosis is uniquely dangerous in protein C-deficient patients starting warfarin without heparin bridge."
  - target: 01-human/07-system/inherited-thrombophilia
    relation: connects-to
    note: "Inherited thrombophilia testing guides anticoagulation duration in VTE: FV Leiden and prothrombin G20210A heterozygotes require 3-6 months for first provoked VTE; high-risk deficiencies (AT, protein C/S) or recurrent unprovoked VTE → indefinite anticoagulation."
  - target: 01-human/07-system/heparin-induced-thrombocytopenia
    relation: connects-to
    note: "HIT causes paradoxical DVT/PE (venous) and arterial thrombosis (HITT); occurs 5-10 days after heparin exposure; anti-PF4/heparin IgG → platelet activation → thrombin; argatroban, bivalirudin, and fondaparinux replace heparin in HIT; DOACs used for bridging to warfarin."
  - target: 01-human/03-molecular/antithrombin
    relation: connects-to
    note: "Antithrombin deficiency (SERPINC1 mutations; 1:2,000-5,000) is the most severe inherited thrombophilia (25-50× lifetime VTE risk); UFH/LMWH efficacy requires AT → AT-deficient patients may need AT concentrate; functional AT assay needed for diagnosis."
  - target: 01-human/07-system/hemophilia-a
    relation: connects-to
    note: "Severe HA (FVIII <1%) confers significant VTE protection; historical VTE rate in HA ~0.5/1000 PY vs. ~1.5-3/1000 general population; emicizumab reconstitutes intrinsic tenase; avoid high-dose APCC with emicizumab → TMA; gene therapy raising FVIII >150% increases VTE risk."
  - target: 03-medicine/01-modern/09-hematology/warfarin
    relation: treated-by
    note: "Warfarin treats DVT/PE at INR 2.0–3.0 × 3–6 months for provoked VTE; indefinite for unprovoked high-risk; largely superseded by DOACs for most VTE; remains first-line for antiphospholipid syndrome; LMWH bridging required at initiation."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Endothelial injury is one arm of Virchow's triad driving VTE: damaged endothelium loses its antithrombotic surface (thrombomodulin, heparan sulfate) and exposes tissue factor and von Willebrand factor, nucleating clot—why surgery, inflammation and indwelling lines provoke it."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "The lung is where venous thromboembolism turns deadly: a deep-vein thrombus that breaks loose lodges in the pulmonary arteries as a pulmonary embolism, causing hypoxia, acute right-heart strain and sudden death; CT angiography diagnoses it and large clots may need thrombolysis."
  - target: 01-human/07-system/sickle-cell-disease
    relation: connects-to
    note: "Sickle cell disease is a strong, often overlooked VTE risk factor: chronic hemolysis, phosphatidylserine exposure and inflammation create a hypercoagulable state, so VTE and pulmonary embolism rates are markedly raised, overlapping with in-situ pulmonary vaso-occlusion."
  - target: 01-human/07-system/polycythemia-vera
    relation: connects-to
    note: "Polycythemia vera is a major acquired cause of venous thromboembolism: high hematocrit and JAK2-mutant prothrombotic blood drive clots, including splanchnic-vein thromboses (Budd-Chiari, portal vein) that can be the first sign—so unusual-site VTE prompts JAK2 testing."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "Cancer is a leading cause of venous thromboembolism, and pancreatic cancer is the classic high-risk tumor (Trousseau syndrome): mucin and tissue factor make the blood intensely prothrombotic, so migratory or unprovoked VTE can be the presenting clue to an occult malignancy."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "COVID-19 dramatically raises venous thromboembolism risk: SARS-CoV-2 endothelial injury and intense inflammation drive immunothrombosis, so hospitalized patients develop DVT and pulmonary embolism at high rates and receive thromboprophylaxis, with D-dimer marking severity."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Platelets help build venous thrombi: though VTE is a fibrin-rich red clot, activated platelets still seed and propagate it, which is why some antiplatelet therapy reduces recurrence—blurring the old line between arterial and venous clots."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Estrogen is a leading reversible cause of VTE: oral contraceptives, hormone therapy and pregnancy raise clotting factors and lower anticoagulant proteins, multiplying thrombosis risk—especially when combined with factor V Leiden or other inherited thrombophilias."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Obesity steadily raises VTE risk: adipose-driven inflammation, higher clotting factors and venous stasis from immobility combine to promote thrombosis, so weight is an independent, modifiable risk factor that compounds surgery, pregnancy and hormonal triggers."
  - target: 01-human/03-molecular/fibrinogen
    relation: connects-to
    note: "Fibrinogen is the raw material of the venous clot: thrombin cleaves it into fibrin strands that mesh trapped red cells into the gelatinous thrombus characteristic of veins, and high fibrinogen levels independently raise venous thromboembolism risk."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Pulmonary embolism stresses the heart acutely: a large clot lodging in the pulmonary arteries suddenly raises right-ventricular afterload, so the right heart can fail and collapse—making PE a cardiovascular emergency, not just a lung problem."
  - target: 01-human/07-system/pnh
    relation: connects-to
    note: "PNH is a striking cause of unusual venous thrombosis: complement-driven hemolysis and platelet activation provoke clots at odd sites (hepatic, cerebral veins), so unexplained venous thromboembolism with hemolysis should prompt testing for PNH."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils help build venous clots: in sluggish veins they cast neutrophil extracellular traps (NETs) that scaffold red cells and platelets into a thrombus, so this immunothrombosis links inflammation and infection to the risk of deep-vein clots."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "Pregnancy is a hypercoagulable state centered on the placenta: clotting factors rise to limit delivery bleeding, but this makes venous thromboembolism a leading cause of maternal death—so prophylaxis is considered in high-risk pregnancy and postpartum."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Hormones make VTE a reproductive-health issue: estrogen-containing contraceptives and hormone therapy raise clotting-factor levels and thrombosis risk, so VTE history shapes contraceptive choices and prompts caution with hormonal treatments."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "Unresolved clots can scar into pulmonary hypertension: when pulmonary emboli fail to dissolve, organized thrombus narrows lung arteries causing chronic thromboembolic pulmonary hypertension (CTEPH)—a potentially curable cause treated by surgically removing the old clot."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium is clotting Factor IV, central to forming venous thrombi: the cascade that builds a clot requires calcium at multiple steps, which is why citrate that binds calcium is used to keep donated and lab blood from clotting."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Venous clots are red because they trap erythrocytes: unlike platelet-rich arterial clots, the slow-flow 'red thrombi' of veins are packed with red cells and fibrin—why stasis (immobility, long flights) is a key part of venous thromboembolism."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "A venous clot becomes deadly when it starves the lungs of oxygen: a leg clot can break off and lodge in the pulmonary arteries, blocking blood flow so the lungs cannot oxygenate—the hypoxemia of pulmonary embolism."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Veins can clot in the brain too: cerebral venous sinus thrombosis is an unusual form of venous thromboembolism, striking young women on estrogen or in pregnancy and causing headache, seizures and stroke-like deficits."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Venous clots also strike the abdomen's great veins: thrombosis of the portal or hepatic veins (Budd-Chiari) links venous thromboembolism to myeloproliferative disorders and PNH, so unusual-site clots prompt a search for hidden causes."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Veins can clot at the kidney: renal vein thrombosis is a venous thromboembolic event classically tied to nephrotic syndrome, whose urinary loss of anticoagulant proteins tips blood toward clotting."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages clean up venous clots: they invade the thrombus to break it down and remodel the vein, so when this resolution fails the clot organizes and scars, causing the post-thrombotic syndrome."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Unresolved clots turn to fibrosis in the lungs: emboli that fail to clear organize into fibrous webs that narrow pulmonary arteries, causing chronic thromboembolic pulmonary hypertension, a late and treatable consequence."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "VTE is confirmed by imaging: CT pulmonary angiography in X-ray photons finds the lung clot, and nuclear V/Q scans map blocked blood flow when contrast can't be used."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Clots can strike the gut's veins: mesenteric and portal vein thrombosis chokes the bowel's drainage, causing severe abdominal pain and, if unrelieved, bowel infarction."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Some clots are born in the marrow: JAK2-driven myeloproliferative neoplasms overproduce blood cells and are a major cause of unprovoked and unusual-site venous thrombosis."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reveals the venous clot's layered build: alternating bands of pale platelet-fibrin and red-cell-rich layers — the lines of Zahn — mark a thrombus that formed in flowing blood before death, distinguishing it from a postmortem clot."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "A deep vein clot announces itself through the skin: the leg swells, warms, and reddens, and in the dreaded phlegmasia cerulea dolens it turns tense and blue as the blocked outflow threatens the limb."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "Clots can strike unusual veins: splanchnic thrombosis of the splenic, portal, or mesenteric veins is a recognized form of VTE, often the first clue to a hidden clotting disorder or abdominal cancer."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies can tip the blood toward clotting: antiphospholipid antibodies are a leading acquired cause of VTE, and the HIT antibody against PF4-heparin paradoxically clots while dropping the platelet count."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "A clot can form in the brain's own veins: cerebral venous sinus thrombosis is a VTE of the cranial drainage, backing up pressure and infarcting neurons to cause headache, seizures, and focal deficits."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Most VTE begins in the legs: a deep vein thrombosis forms in the calf and thigh veins, often after immobility or surgery, and leaves the post-thrombotic limb swollen and aching long after the clot."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "The vein wall is part of the problem: stasis and damage to the smooth-muscle-lined vein and its valves let clot form, and after a DVT the scarred, incompetent valves drive the chronic swelling of post-thrombotic syndrome."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "A leg clot can reach the brain: through a patent foramen ovale a venous thrombus crosses to the arterial side as a paradoxical embolism, a recognized cause of cryptogenic stroke in younger patients."
  - target: 01-human/07-system/multiple-myeloma
    relation: connects-to
    note: "Cancer and its drugs ignite clotting: malignancy is a major VTE risk, and multiple myeloma is especially thrombogenic — its immunomodulatory drugs (thalidomide, lenalidomide) demand routine anticoagulant prophylaxis."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Stasis and strain tie the clot to the failing heart: the sluggish circulation of heart failure breeds venous clots, while a large pulmonary embolism can acutely overwhelm the right heart into failure — a two-way danger."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "The healthy vessel resists clotting with nitric oxide: endothelial NO keeps platelets quiet and vessels open, so when endothelial dysfunction cuts NO, the balance tips toward the thrombosis of VTE."
  - target: 01-human/07-system/inflammatory-bowel-disease
    relation: connects-to
    note: "Gut inflammation clots the veins: active inflammatory bowel disease is a strong acquired risk for VTE, the systemic inflammation raising clotting factors and platelets, so hospitalized flares get thromboprophylaxis."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Sepsis clots the small and large veins alike: systemic inflammation activates coagulation (immunothrombosis), so septic patients face both DIC and limb and pulmonary VTE — one reason thromboprophylaxis is standard in critical illness."
  - target: 01-human/07-system/glioblastoma
    relation: connects-to
    note: "Few cancers clot like glioblastoma: brain tumors express abundant tissue factor and carry one of the highest VTE rates of any malignancy, posing the hard problem of anticoagulating a patient prone to intracranial bleeding."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Inflammation seeds the venous clot: NLRP3-driven IL-1β and the neutrophil extracellular traps it promotes provide the scaffold for immunothrombosis, linking the inflammasome to the pathogenesis of venous thromboembolism."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Inflammation makes the vein wall clot: NF-κB activation in endothelium and monocytes induces tissue factor and adhesion molecules, the thromboinflammatory switch that converts an inflamed vessel into a site of venous thrombosis."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "A common cancer that clots: colorectal cancer is a frequent driver of cancer-associated thrombosis, its tumor tissue factor and the surgery and chemotherapy it requires all raising venous thromboembolism risk."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Failing kidneys tip toward clotting: chronic kidney disease, and especially nephrotic-range protein loss, creates a hypercoagulable state that raises the risk of deep-vein thrombosis and pulmonary embolism."
  - target: 01-human/07-system/ovarian-cancer
    relation: connects-to
    note: "An unprovoked clot can herald it: ovarian and other adenocarcinomas are strongly prothrombotic, so a venous thromboembolism without obvious cause can be the presenting sign that prompts the search uncovering the tumor."
  - target: 01-human/07-system/nash
    relation: connects-to
    note: "The fatty liver leans toward clotting: NASH raises fibrinogen and PAI-1 and lowers fibrinolysis, an under-recognized prothrombotic state that increases the risk of venous thromboembolism and portal vein thrombosis."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Surviving a clot leaves a mental mark: many people develop persistent anxiety and depression after a pulmonary embolism or DVT, a post-thrombotic psychological distress akin to post-traumatic stress."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Damaged veins leave chronic ulcers: deep vein thrombosis injures venous valves, and the resulting post-thrombotic syndrome and venous hypertension produce slow-healing venous leg ulcers."
  - target: 01-human/07-system/gastric-cancer
    relation: connects-to
    note: "An unprovoked clot can herald hidden cancer: Trousseau's syndrome of migratory thrombosis points to occult malignancy, and adenocarcinomas like gastric cancer are classic culprits found on the ensuing search."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Its long anticoagulation can cost bone: prolonged heparin used to treat venous thromboembolism, especially in pregnancy, lowers bone mineral density, a recognized treatment-related bone loss."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Half of it lands in the lungs: a deep-vein clot that breaks loose travels to the pulmonary arteries as pulmonary embolism, abruptly blocking gas exchange and straining the right heart, the lethal face of VTE."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It clots the gut's veins and its drugs bleed it: VTE includes splanchnic, portal and mesenteric vein thrombosis threatening the bowel, while the anticoagulants treating it raise the risk of GI haemorrhage."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Old clots scar the skin: post-thrombotic syndrome after a DVT causes chronic venous stasis with pigmentation and leg ulcers, and warfarin can rarely cause acute skin necrosis."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "A large clot can stop the heart: massive pulmonary embolism causes acute right-heart strain and obstructive shock, and via a patent foramen ovale a venous clot can cause paradoxical arterial embolism."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Clots strike the brain's veins too: cerebral venous sinus thrombosis is venous thromboembolism within the skull, causing headache, seizures and raised intracranial pressure."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Hormones tip the balance toward clotting: oestrogen in combined contraceptives and HRT, and cortisol excess, raise clotting factors and are major hormonal drivers of venous thromboembolism."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "The leaky kidney clots: nephrotic syndrome loses antithrombin in the urine, creating a hypercoagulable state that classically causes renal vein thrombosis and other venous clots."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Inflammation and clotting are intertwined: 'immunothrombosis' sees neutrophil extracellular traps and inflammatory cytokines trigger coagulation, linking infection and autoimmunity to venous thrombosis."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It leaves a lasting swelling: after a deep-vein thrombosis, valve damage and impaired drainage cause the post-thrombotic syndrome, a chronic oedema that mimics lymphatic failure."
  - target: 03-medicine/01-modern/04-cardio/aspirin
    relation: connects-to
    note: "An option for prevention: aspirin gives modest protection against recurrent venous thromboembolism and is used for prophylaxis after some orthopaedic surgery, though anticoagulants are more effective."
  - target: 02-pathogen/01-viruses/sars-cov-2
    relation: connects-to
    note: "A virus that clots the veins: severe COVID-19 markedly raises venous thromboembolism risk through endothelial injury, inflammation and immobility, prompting routine thromboprophylaxis in hospital."
  - target: 01-human/07-system/nsclc
    relation: connects-to
    note: "Cancer drives clotting: lung adenocarcinoma and other cancers create a hypercoagulable Trousseau state, making venous thromboembolism a common and dangerous complication of malignancy."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "A large PE fails the right heart: pulmonary embolism abruptly raises pulmonary pressure, straining and dilating the right ventricle — acute RV failure is the mechanism of death in massive PE, tracked by troponin and echo."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Chemo adds to the clot risk: beyond the cancer's own hypercoagulability, agents like cisplatin and thalidomide-class drugs are prothrombotic, so cancer-associated VTE is managed with LMWH or direct oral anticoagulants."
  - target: 01-human/07-system/essential-thrombocythemia
    relation: connects-to
    note: "Too many platelets clot the veins: essential thrombocythemia and other myeloproliferative neoplasms cause venous thromboembolism, including unusual-site clots like splanchnic and cerebral vein thrombosis, despite the high platelet count."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Pulmonary embolism at the gas-exchange unit: a clot lodging in the pulmonary arteries creates alveolar dead space—ventilated but not perfused—causing the hypoxaemia and, occasionally, pulmonary infarction of PE."
  - target: 01-human/07-system/thalassemia
    relation: connects-to
    note: "A prothrombotic anaemia: thalassaemia, especially after splenectomy, carries a hypercoagulable state with procoagulant red-cell membranes and thrombocytosis that raises venous thrombosis risk."
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "Tumour thrombus in the vein: renal cell carcinoma characteristically grows as a tumour thrombus up the renal vein and inferior vena cava, and its cancer-associated hypercoagulability adds to VTE risk."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Paradoxical embolism: a venous clot can cross a patent foramen ovale into the arterial circulation and lodge in the brain, turning a deep-vein thrombosis into a paradoxical stroke."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "Cancer-associated thrombosis: breast cancer raises VTE risk through tumour procoagulants, chemotherapy and hormonal therapy like tamoxifen, a common Trousseau-type complication."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Surgery and fracture provoke clots: major orthopaedic surgery and long-bone fractures of the cortical bone are among the strongest provokers of deep-vein thrombosis, driving routine post-operative prophylaxis."
  - target: 01-human/07-system/myelofibrosis
    relation: connects-to
    note: "Myeloproliferative thrombosis: like polycythaemia vera and essential thrombocythaemia, myelofibrosis is strongly thrombogenic and a leading cause of splanchnic (portal and hepatic vein) thrombosis."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Splanchnic vein clots: thrombosis of the portal vein or the hepatic veins (Budd-Chiari syndrome) draining the hepatic lobule is a distinct, often MPN-driven form of venous thromboembolism."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "Renal vein thrombosis: nephrotic-range proteinuria from glomerular disease loses antithrombin in the urine, creating a hypercoagulable state that classically thromboses the renal vein."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Immunothrombosis: IL-6 drives the inflammation-coagulation crosstalk that raises VTE risk in infection, cancer and inflammatory disease, linking acute illness to clot formation."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Prothrombotic inflammation: TNF-α activates endothelium to express tissue factor and downregulate anticoagulant pathways, a mechanism connecting systemic inflammation to venous thrombosis."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Stasis hypoxia: venous stasis creates local hypoxia that stabilises HIF-1α and upregulates procoagulant factors, part of why immobility and stasis precipitate deep-vein thrombosis."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "NETosis initiation: neutrophil extracellular traps rich in S100A8/A9 provide the scaffold and trigger for venous thrombus formation, a core mechanism of immunothrombosis behind deep-vein thrombosis."
  - target: 01-human/03-molecular/pf4
    relation: connects-to
    note: "Platelet activation: PF4 released from activated platelets within the forming venous thrombus promotes aggregation and, in HIT and VITT, drives the antibody-mediated thrombosis that VTE workups must exclude."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "Thrombus scaffold: plasma fibronectin is cross-linked into the fibrin meshwork of venous clots, stabilising the thrombus that obstructs the vein or embolises to the lung."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Monocyte immunothrombosis: CCL2 recruits monocytes to the forming venous thrombus, where their tissue-factor expression amplifies thrombin generation — the inflammation arm of the immunothrombosis that initiates deep-vein thrombosis."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Innate thrombus trigger: TLR4 sensing of DAMPs on the activated venous endothelium and leukocytes promotes the tissue-factor and NET release that nucleate venous thrombi, linking sterile inflammation to clotting."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Platelet eicosanoid balance: the platelet thromboxane A2/endothelial prostacyclin balance governs the platelet activation that propagates a venous thrombus, the balance aspirin shifts to lower recurrent VTE risk."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Contact-pathway thrombosis: the intrinsic contact system — factor XII and kallikrein, which also generates bradykinin — feeds venous thrombus growth, making factor XI/XII the targets of the new anticoagulants that aim to block clotting without causing bleeding."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement-coagulation crosstalk: complement activation generating C3 fragments amplifies platelet activation and tissue factor, an inflammatory limb of immunothrombosis that compounds the stasis and hypercoagulability driving venous thromboembolism."
  - target: 01-human/03-molecular/rage
    relation: connects-to
    note: "Thrombo-inflammation: DAMPs such as HMGB1 signalling through RAGE on endothelium and leukocytes promote the tissue-factor expression and NET formation that knit together the immunothrombosis of venous clot."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Endothelial injury arm: endothelial Angiopoietin-2 activation shifts the vein-wall endothelium to a procoagulant, permeable phenotype, part of the endothelial-injury limb of Virchow's triad in venous thromboembolism."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Thromboinflammation: IL-1β, downstream of the NLRP3 inflammasome already mapped, induces endothelial and monocyte tissue factor that initiates the coagulation of venous thrombosis."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Complement crosstalk: complement activation (C3 already mapped, through C5) amplifies platelet and endothelial activation in venous thromboembolism, part of the thromboinflammatory crosstalk that promotes clot formation."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Immunothrombosis: TLR-MyD88-NF-κB innate signalling (TLR4 and NF-κB already mapped) underlies the immunothrombosis in which activated neutrophils and monocytes — through NETs and tissue factor — seed venous thrombus formation."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Endothelial dysfunction: raised endothelin-1 from a dysfunctional endothelium shifts the vessel wall toward the vasoconstricted, procoagulant state that, with venous stasis, completes Virchow's triad in venous thromboembolism."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Thrombus remodelling: VEGF-driven angiogenesis participates in thrombus organisation and recanalisation, the vascular remodelling that determines resolution versus the post-thrombotic syndrome after venous thromboembolism."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signalling in platelets and endothelium amplifies the activation responses that initiate venous thrombosis."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Endothelial and platelet PI3K-AKT signalling regulates the procoagulant and adhesive phenotype that drives venous thromboembolism."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 promotes the neutrophil-extracellular-trap-driven thromboinflammation central to venous thrombus formation."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "DNA within neutrophil extracellular traps engages cGAS-STING, linking NET-driven sterile inflammation to the thrombus formation of venous thromboembolism."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling transduces the inflammatory cytokine response that promotes the procoagulant endothelial phenotype of venous thromboembolism."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K-AKT signalling (AKT already mapped) in platelets and endothelium supports the activated, procoagulant phenotype that drives venous thromboembolism."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO downstream of PI3K-AKT signaling (AKT and PIK3CA already mapped) regulates the endothelial quiescence-versus-activation balance relevant to venous thromboembolism."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signaling modulates the endothelial inflammatory activation that contributes to venous thrombosis."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK1/2-STAT cytokine signaling (IL-6-STAT3 already mapped) amplifies the inflammatory endothelial and platelet activation driving the thromboinflammation of venous thromboembolism."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the platelet-activation and endothelial signaling relevant to the thrombus formation of venous thromboembolism."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTOR signaling in activated endothelium and immune cells participates in the immunothrombosis of venous thromboembolism."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK metabolic signaling in endothelial cells modulates the vascular homeostasis whose disruption promotes venous thromboembolism."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the endothelial and leukocyte responses relevant to the thrombo-inflammation of venous thromboembolism."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the platelet activation and endothelial responses driving venous thromboembolism."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven monocyte recruitment contributes to the thrombo-inflammation and thrombus resolution of venous thromboembolism."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic modulation of the coagulation and endothelial gene expression relevant to venous thromboembolism."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the endothelial and leukocyte interactions of the thrombo-inflammation of venous thromboembolism."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the endothelial activation and thrombo-inflammation of venous thromboembolism."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the thromboinflammation of venous thromboembolism."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the endothelial and coagulation gene programs relevant to venous thromboembolism."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine signaling provides platelet-inhibitory and vascular modulation relevant to venous thromboembolism."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Pulmonary embolism strain: a large pulmonary embolism strains the right ventricle, and troponin release marking that myocardial injury identifies the intermediate-to-high-risk patients who may need thrombolysis rather than anticoagulation alone."
  - target: 01-human/03-molecular/bnp
    relation: connects-to
    note: "Right-ventricular stretch: BNP released from the pressure-loaded right ventricle in pulmonary embolism complements troponin in risk stratification, flagging the ventricular dysfunction that predicts adverse outcomes."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Obesity risk: obesity is a strong independent risk factor for venous thromboembolism through venous stasis and a prothrombotic state, and the adipokine leptin promotes platelet activation and coagulation."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Pregnancy hypercoagulability: pregnancy, sustained by progesterone and estrogen (already mapped), is a strongly prothrombotic state with venous stasis, making venous thromboembolism a leading cause of maternal death and a target for prophylaxis."
  - target: 01-human/07-system/myeloproliferative-neoplasms
    relation: connects-to
    note: "Clonal thrombophilia: JAK2-driven myeloproliferative neoplasms create an acquired hypercoagulable state, often presenting as venous thrombosis at unusual sites such as the splanchnic or cerebral veins, an important cause to screen for."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Metabolic prothrombotic state: insulin resistance and the metabolic syndrome raise PAI-1 and fibrinogen (already mapped), an acquired prothrombotic tendency that compounds the venous-thromboembolism risk of the obesity (leptin already mapped) it accompanies."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative thrombogenesis: the stasis and hypoxia of the venous thrombus generate reactive oxygen species, to which xanthine oxidase contributes, promoting the endothelial (already mapped) dysfunction and thrombo-inflammation that propagate venous thromboembolism."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Thrombo-inflammation balance: coagulation and inflammation are intertwined, and the anti-inflammatory IL-10 opposes the pro-inflammatory signals (IL-6, TNF and IL-1 already mapped) that amplify the immunothrombosis of venous thromboembolism."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Platelet serotonin: serotonin released from activated platelets (PF4 already mapped) causes vasoconstriction and amplifies platelet aggregation, contributing to the thrombus formation and propagation of venous thromboembolism."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Thrombo-inflammation balance: IL-4 and the M2 anti-inflammatory arm (IL-10 already mapped) counter the pro-inflammatory signals (IL-6, TNF and IL-1 already mapped) of the immunothrombosis that amplifies venous thromboembolism."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Platelet zinc and coagulation: zinc released from the activated platelets (already mapped) promotes the contact pathway and fibrin formation (fibrinogen and thrombin already mapped), adding to the clotting tendency in venous thromboembolism."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Metabolic prothrombotic risk: dyslipidaemia and the metabolic syndrome (leptin and insulin already mapped) add an acquired hypercoagulable state, and raised cholesterol contributes to the venous as well as arterial thrombotic risk."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Antiphospholipid antibodies: the IgG antiphospholipid antibodies of the antiphospholipid syndrome are a major acquired thrombophilia causing venous (and arterial) thromboembolism, testing for which is part of the workup of unprovoked VTE."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 inflammation: IL-13, with IL-4 (already mapped), is part of the type-2 immune arm of the inflammation (IL-6 already mapped) that contributes to the venous-thrombus resolution and the post-thrombotic remodelling."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Obesity and hypercoagulability: the fall in adiponectin, with leptin (already mapped), of the obesity that is a major risk factor for venous thromboembolism promotes the prothrombotic and inflammatory state."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the obesity (a major VTE risk) and the prothrombotic inflammatory state."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "CTEPH: the chronic thromboembolic pulmonary hypertension is a long-term complication of the unresolved pulmonary embolism of venous thromboembolism."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Right-heart strain: the pulmonary embolism strains the right heart (troponin and BNP already mapped), the acute RV failure the cause of the PE death."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate immunothrombosis: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, is part of the innate immune contribution to the immunothrombosis (neutrophils already mapped) of venous thromboembolism."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 immunothrombosis: the IFN-γ of the T cells is the type-II interferon arm of the inflammatory dimension (IL-6 and TNF already mapped) that potentiates the venous thrombosis."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immunothrombotic inflammation of venous thromboembolism."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the inflammatory milieu of the immunothrombosis of venous thromboembolism."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immunothrombotic inflammation of venous thromboembolism."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the inflammatory milieu of venous thromboembolism."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the myeloid tissue-factor expression and the neutrophil (already mapped) NETosis of the immunothrombosis of venous thromboembolism."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) at the complement–coagulation interface of the immunothrombosis of venous thromboembolism."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Contact/complement regulation: the C1-esterase inhibitor regulates both the classical complement and the contact (intrinsic-coagulation) pathways, a key brake at the complement–coagulation interface of venous thromboembolism."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Thromboinflammation: osteopontin, released by the activated platelets (already mapped), is a matricellular mediator amplifying the neutrophil (already mapped) NET-driven immunothrombosis of venous thromboembolism."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Thrombotic iron: transferrin, the iron carrier, reflects the disordered iron handling that, with the venous stasis and hypercoagulability, is part of the thrombotic-risk context of venous thromboembolism."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Adaptive immunothrombosis: the CD4 T-helper cells contribute to the adaptive-immune dimension of the inflammation that primes the venous endothelium (already mapped) for the immunothrombosis of venous thromboembolism."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-thromboinflammation axis: TSLP, from activated endothelium (already mapped) and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2/eosinophil imbalance of the thromboinflammation of venous thromboembolism."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Thrombogenic erythropoiesis: erythropoietin drives erythrocytosis and increases blood viscosity, amplifying the venous stasis and the hypercoagulability of the thrombotic-risk context of venous thromboembolism."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell venous inflammation: histamine, from mast cells (already mapped), increases venous endothelial permeability and primes the coagulation–inflammation interface of the immunothrombosis of venous thromboembolism."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian coagulation: melatonin has antithrombotic and antioxidant effects, reducing platelet (already mapped) activation and the endothelial (already mapped) oxidative stress that prime the nocturnal hypercoagulability and the thrombotic risk of venous thromboembolism."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Sex-hormone coagulation: testosterone promotes erythropoiesis (EPO already mapped) and haematocrit elevation, increases blood viscosity and venous stasis; male sex-hormone levels and androgen-therapy are recognised risk factors for venous thromboembolism."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Thrombus organisation matrix: periostin, from fibroblasts and endothelial cells (already mapped) at the organising thrombus, contributes to the ECM remodelling and the fibrous transformation of the venous thrombus in venous thromboembolism."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "VTE prolactin: prolactin, via PRLR on endothelial cells (already mapped) and macrophages (already mapped), promotes platelet (already mapped) activation; hyperprolactinaemia amplifies the thrombin (already mapped) and IL-6 (already mapped) thrombosis of venous thromboembolism."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "VTE oxytocin: oxytocin, via OXTR on endothelial cells (already mapped) and macrophages (already mapped), attenuates thromboinflammation; oxytocin deficiency amplifies the thrombin (already mapped) and NF-κB (already mapped) coagulation cascade of venous thromboembolism."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "VTE vasopressin: vasopressin, via V1aR on endothelial cells (already mapped) and smooth-muscle cells (already mapped), modulates vascular tone; vasopressin dysregulation amplifies the thrombin (already mapped) and platelet (already mapped) coagulation cascade of VTE."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "VTE selenium: selenium, as GPx in endothelial cells (already mapped) and platelets (already mapped), scavenges ROS driving thromboinflammation; selenium deficiency amplifies the thrombin (already mapped) and NF-κB (already mapped) coagulation cascade of venous thromboembolism."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "VTE iodine: iodine-dependent thyroid hormones modulate haemostatic factor expression (fibrinogen already mapped) and endothelial (already mapped) function; iodine deficiency impairs thyroid-mediated regulation of the thrombin (already mapped) cascade of venous thromboembolism."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "VTE sodium: high dietary sodium promotes endothelial (already mapped) dysfunction and a prothrombotic state; sodium-induced aldosterone elevation amplifies the platelet (already mapped) and NF-κB (already mapped) thromboinflammatory cascade of venous thromboembolism."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "VTE magnesium: magnesium stabilises endothelial cell (already mapped) function and attenuates platelet (already mapped) aggregation; magnesium deficiency amplifies NF-κB (already mapped) and thrombin (already mapped) and fibrinogen (already mapped) procoagulant cascade in VTE."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "VTE iron: iron overload promotes endothelial cell (already mapped) and platelet (already mapped) oxidative activation; iron-induced NF-κB (already mapped) and thrombin (already mapped) amplify fibrinogen (already mapped) and coagulation cascade of venous thromboembolism."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "VTE copper: copper-dependent SOD in endothelial cells (already mapped) and macrophages (already mapped) quenches ROS; copper deficiency amplifies NF-κB (already mapped) and thrombin (already mapped) and fibrinogen (already mapped) procoagulant cascade of venous thromboembolism."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "VTE potassium: potassium efflux in endothelial cells (already mapped) and platelets (already mapped) modulates vascular tone; potassium dysregulation amplifies NF-κB (already mapped) and thrombin (already mapped) thromboinflammatory cascade of VTE."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "VTE carbon: carbon, as metabolic backbone of clotting factors in endothelial cells (already mapped) and macrophages (already mapped), drives coagulation; carbon dysregulation amplifies NF-κB (already mapped) and thrombin (already mapped) procoagulant cascade of VTE."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "VTE chloride: chloride channels in endothelial cells (already mapped) and macrophages (already mapped) regulate vascular tone; chloride dysregulation amplifies NF-κB (already mapped) and thrombin (already mapped) and fibrinogen (already mapped) cascade of VTE."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "VTE hydrogen: hydrogen, via redox homeostasis in endothelial cells (already mapped) and macrophages (already mapped), quenches procoagulant ROS; hydrogen dysregulation amplifies NF-κB (already mapped) and thrombin (already mapped) and fibrinogen (already mapped) cascade of VTE."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "VTE nitrogen: nitric oxide from endothelial cells (already mapped) and macrophages (already mapped) modulates vascular tone; nitrogen imbalance amplifies NF-κB (already mapped) and thrombin (already mapped) and fibrinogen (already mapped) procoagulant cascade of VTE."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "VTE sulfur: hydrogen sulfide from endothelial cells (already mapped) and macrophages (already mapped) modulates vascular tone; sulfur deficiency amplifies NF-κB (already mapped) and thrombin (already mapped) and fibrinogen (already mapped) cascade of VTE."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "VTE PD-1: PD-1 on macrophages (already mapped) and T-helper-cell (already mapped) modulates vascular immune homeostasis; PD-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and thrombin (already mapped) procoagulant cascade of VTE."
---

# Venous Thromboembolism

## Overview

**Venous thromboembolism (VTE)** is the collective term for **deep vein thrombosis (DVT)** — thrombosis in the proximal or distal veins of the leg (or upper extremity) — and **pulmonary embolism (PE)** — occlusion of the pulmonary arterial tree by thrombus, typically originating from DVT. They represent a single disease on a pathophysiological spectrum: ~50% of proximal DVTs embolize to the pulmonary circulation [^konstantinides-2020-esc-pe].

**Epidemiology:**
- Incidence: ~1-2 per 1,000 adults per year in the general population; third most common cardiovascular disease after MI and stroke
- Recurrence: ~30% within 5-10 years after stopping anticoagulation
- Mortality: Massive PE (hemodynamic instability) → ~15-30% in-hospital mortality; untreated proximal DVT → ~15-25% risk of symptomatic PE; fatal PE risk ~0.2-0.5% with anticoagulation

**Virchow's Triad** (1856) — three interacting mechanisms:
1. **Venous stasis:** Reduced blood flow (immobilization, heart failure, air travel, varicose veins) → thrombin accumulation, activated clotting factor pooling
2. **Hypercoagulability:** Inherited thrombophilias (Factor V Leiden, prothrombin G20210A, protein C/S deficiency, antithrombin deficiency, APS) or acquired (cancer, pregnancy, OCP, HRT, inflammation)
3. **Endothelial injury:** Surgery, central venous catheters, trauma → exposed subendothelial TF → FVIIa/TF → extrinsic pathway activation → thrombin → fibrin

## Structure

### Classification of DVT

**By location:**
- **Proximal DVT** (popliteal, femoral, iliac veins): Higher risk of PE; anticoagulation mandatory
- **Distal DVT** (calf veins, tibial, peroneal): Controversial management; higher rate of spontaneous resolution; ~15-20% propagate to proximal if untreated; treat if symptomatic or if PE risk is high
- **Upper extremity DVT:** Effort thrombosis (Paget-Schroetter; subclavian vein; thoracic outlet syndrome) vs. catheter-related; treat with anticoagulation; thrombolysis for effort thrombosis

**By provocation:**
- **Provoked VTE:** Clear transient risk factor (surgery, immobilization, trauma, pregnancy) → lower recurrence after stopping anticoagulation (3-6 months); shorter treatment course
- **Unprovoked VTE:** No identifiable transient risk factor → recurrence risk ~30% at 5 years; long-term (indefinite) anticoagulation generally recommended after first unprovoked proximal DVT or PE
- **Cancer-associated VTE:** VTE in active malignancy; highest recurrence risk (~20% per year); LMWH (first-line historically) or DOAC (apixaban/rivaroxaban with caution for GI bleeding in GI cancers)

### Classification of PE

**2019 ESC risk stratification (by hemodynamic stability and RV dysfunction):**

| Risk | Hemodynamics | Imaging | Biomarkers | Mortality | Treatment |
|:-----|:------------|:--------|:-----------|:---------|:---------|
| **Massive/High** | Shock or arrest | RV dilation | Troponin+/BNP+ | ~15-30% | Systemic thrombolysis or catheter-directed therapy + anticoagulation |
| **Submassive/Intermediate-high** | Stable | RV dilation | Troponin+/BNP+ | ~5-15% | Anticoagulation; consider advanced therapy if deterioration |
| **Intermediate-low** | Stable | RV dilation OR biomarker+ | Either | ~2-5% | Anticoagulation |
| **Low** | Stable | No RV dilation | Both negative | <1% | DOAC; outpatient if low PESI |

**Simplified PESI score** (Pulmonary Embolism Severity Index): Predicts 30-day mortality; score ≥1 of: age >80, cancer, cardiopulmonary disease, HR ≥110, SBP <100, O2 sat <90% → inpatient management; score 0 → low risk, outpatient eligible.

## Function

### Inherited thrombophilias

| Thrombophilia | Prevalence (general pop.) | VTE lifetime risk | Recurrence risk | Notes |
|:-------------|:------------------------|:-----------------|:----------------|:------|
| Factor V Leiden (heterozygous) | ~5% Caucasian | ~3-5× increase | Moderate | R506Q; FVa resistant to APC; most common thrombophilia |
| Factor V Leiden (homozygous) | ~0.02% | ~50-80× increase | High | |
| Prothrombin G20210A (heterozygous) | ~2-3% Caucasian | ~2-3× increase | Moderate | ↑ prothrombin levels |
| Protein C deficiency | ~0.3% | ~8-10× increase | High | Autosomal dominant; warfarin-induced skin necrosis risk |
| Protein S deficiency | ~0.3% | ~5-8× increase | High | Cofactor for APC |
| Antithrombin deficiency | ~0.02-0.04% | ~25-50× increase | Very high | Most severe inherited thrombophilia |
| APS (acquired) | ~0.5% | High (varies) | Very high | Triple-positive: >10%/yr; warfarin superior to DOACs |

**Thrombophilia testing:** Not recommended during acute VTE (acute phase reactant changes confound results); test ≥3 months after anticoagulation stopped; screen in: unprovoked VTE <50 years, unusual location (cerebral, splanchnic, upper extremity), family history, recurrent VTE, APS suspicion.

## Pathology

### Clinical features

**DVT:**
- Classic: Unilateral leg swelling, warmth, erythema, tenderness along deep vein tract, Homans' sign (calf pain on dorsiflexion — poor specificity)
- **Wells score for DVT (pre-test probability):** Active cancer +1, paralysis/plaster +1, bedridden >3 days +1, tenderness along vein +1, swollen leg +1, calf >3 cm larger +1, pitting edema +1, previous DVT +1, alternative diagnosis equally likely −2; score ≤0 = low probability (treat as unlikely), score ≥2 = high probability (treat as likely)
- **D-dimer:** Negative D-dimer (<500 ng/mL; age-adjusted: 500 + age × 10 >50 years) effectively rules out DVT in low/intermediate probability patients; elevated D-dimer is non-specific (any fibrin turnover)
- **Duplex ultrasound:** Non-compressibility of vein = diagnostic for DVT; sensitivity ~95% for proximal, ~75% for distal

**Pulmonary embolism:**
- Classic: Pleuritic chest pain (peripheral infarct), hemoptysis (lung infarction), dyspnea (central/massive), tachycardia (most common sign), hypoxemia, right heart strain
- Massive PE: Syncope, hypotension (SBP <90 mmHg), right heart failure (elevated JVP, S3, RV heave), cyanosis, cardiac arrest (PEA)
- **Wells score for PE:** DVT symptoms +3, alternative less likely +3, HR >100 +1.5, immobilization/surgery +1.5, prior DVT/PE +1.5, hemoptysis +1, malignancy +1; score <2 = low probability, score ≥5 = high probability
- **CTPA (CT pulmonary angiography):** Diagnostic gold standard; RV/LV diameter ratio >0.9 on CT = RV dysfunction; sensitivity/specificity >95% for subsegmental and larger PE
- **Echocardiography:** McConnell's sign (RV free wall hypokinesis with apical sparing) in massive PE; right heart thrombus = surgical emergency; not diagnostic alone
- **Biomarkers:** Troponin (RV myocardial injury), BNP/NT-proBNP (RV wall stress) → prognostic in hemodynamically stable PE

### Diagnosis

**Diagnostic algorithm:**
1. Calculate Wells score + D-dimer (if low/intermediate probability)
2. Low probability + negative D-dimer → VTE excluded
3. High probability or positive D-dimer → imaging (ultrasound for DVT; CTPA for PE)
4. For PE with hemodynamic instability → bedside echo first (if CTPA not safe); systemic thrombolysis if massive PE confirmed

### Treatment

**Anticoagulation — acute VTE (first 3-6 months):**

**Direct oral anticoagulants (DOACs) — first-line:**
- **Apixaban (Eliquis; AMPLIFY trial):** 10 mg BID × 7 days → 5 mg BID; recurrent VTE 2.3% vs. 2.7% LMWH/VKA (non-inferior); major bleeding 0.6% vs. 1.8% (superior); FDA approved DVT/PE treatment [^agnelli-2013-amplify-apixaban-vte]; preferred in cancer (CARAVAGGIO trial non-inferior to dalteparin)
- **Rivaroxaban (Xarelto; EINSTEIN-DVT/PE):** 15 mg BID × 21 days → 20 mg QD with evening meal; non-inferior to LMWH/VKA for recurrent VTE; bleeding comparable; convenient single-drug approach [^bauersachs-2010-einstein-rivaroxaban]
- **Edoxaban (Savaysa; Hokusai-VTE):** 5-10 days LMWH run-in → edoxaban 60 mg QD; reduces dose to 30 mg if CrCl 15-50 mL/min or body weight ≤60 kg
- **Dabigatran (Pradaxa; RE-COVER):** 5-10 days LMWH run-in → dabigatran 150 mg BID; renal clearance ~80% → requires dose adjustment in CKD; reversed by idarucizumab

**LMWH (Low-molecular-weight heparin):**
- Dalteparin, enoxaparin, tinzaparin; SC injection; anti-Xa monitoring in renal impairment, obesity, pregnancy
- Preferred in pregnancy (DOACs teratogenic/unknown fetal safety) and cancer-associated VTE
- Cancer + VTE: Dalteparin (CLOT trial: 50% VTE recurrence reduction vs. warfarin) or DOAC (apixaban/rivaroxaban now preferred based on ADAM-VTE, CARAVAGGIO, SELECT-D trials)

**Anticoagulation duration:**
- Provoked VTE (major transient risk factor): 3 months
- Unprovoked proximal DVT or PE: ≥3 months; extend indefinitely if recurrence risk high and bleeding risk acceptable; D-dimer testing at 1 month off anticoagulation predicts recurrence risk (elevated D-dimer → higher recurrence)
- Cancer-associated VTE: Treat until cancer is in remission; typically indefinite during active cancer
- Extended prophylaxis: **Apixaban 2.5 mg BID** (AMPLIFY-EXT trial: 80% relative risk reduction of VTE vs. placebo over 12 additional months with minimal bleeding increase) — approved for extended treatment after ≥6 months initial therapy

**Massive PE (hemodynamic instability) — advanced therapy:**
- **Systemic thrombolysis:** Alteplase 100 mg IV over 2 hours (or 10 mg bolus + 90 mg over 2h); direct action on pulmonary artery thrombus → rapid hemodynamic improvement; 50% mortality reduction vs. anticoagulation alone in massive PE; major bleeding 10%; ICH 1-3% → contraindicated if recent surgery, stroke, or hemorrhage
- **Catheter-directed thrombolysis (CDT):** Lower-dose tPA (1-2 mg/h per catheter) directly into pulmonary artery; reduces systemic bleeding; PERFECT registry evidence; used for intermediate-high risk PE with contraindication to systemic thrombolysis
- **Surgical embolectomy:** Open cardiac surgery; for massive PE refractory to thrombolysis or immediate hemodynamic collapse; requires cardiopulmonary bypass; high mortality but may be lifesaving
- **ECMO (VA-ECMO):** Right heart failure + cardiac arrest → veno-arterial ECMO provides circulatory support while thrombolysis or embolectomy performed; emerging as bridge to definitive therapy

**VTE prophylaxis:**
- **Hospitalized surgical patients:** LMWH (enoxaparin 40 mg SC QD) or UFH (5,000 U SC TID) + mechanical compression (sequential compression devices); extended prophylaxis (LMWH × 28-35 days) for major abdominal/pelvic cancer surgery (FAME registry)
- **Medical patients:** LMWH or UFH for bed-bound patients with acute illness; DOAC prophylaxis (rivaroxaban, betrixaban, apixaban) inferior to LMWH in most hospitalized medical patients (excess bleeding); exception: extended prophylaxis post-hospitalization (MAGELLAN, APEX trials) shows modest VTE reduction
- **Travel thrombosis:** Flights >6 h + risk factors → aspirin and/or LMWH prophylaxis; graduated compression stockings; ambulation; hydration
- **Inferior vena cava (IVC) filter:** For VTE + absolute contraindication to anticoagulation; retrievable filters preferred; does not reduce mortality; prophylactic filters not recommended routinely

## Connections

- `connects-to` → **[Thrombin](../../03-molecular/thrombin/README.md)** — Thrombin (FIIa) generates fibrin at the core of venous thrombi; stasis → contact activation → FXI → FIXa → FX → thrombin → fibrin-rich clot; DOACs (dabigatran, rivaroxaban, apixaban) target thrombin or FXa to prevent and treat VTE; LMWH inhibits thrombin via antithrombin.
- `connects-to` → **[Antiphospholipid Syndrome](../antiphospholipid-syndrome/README.md)** — APS is the most important thrombophilia causing recurrent DVT/PE in young adults; triple-positive aPL (LA + aCL + anti-B2GPI) confers >10% annual thrombotic risk; warfarin INR 2-3 is superior to DOACs for VTE in APS; rivaroxaban doubled arterial event risk in triple-positive APS (TRAPS trial).
- `connects-to` → **[Von Willebrand Factor](../../03-molecular/von-willebrand-factor/README.md)** — Elevated VWF promotes venous thrombosis by augmenting platelet recruitment and fibrin network formation; VWF is an acute-phase protein elevated in surgery, infection, cancer → increased VTE risk; ABO blood group affects VWF level (type O ~25% lower VWF → lower baseline VTE risk).
- `connects-to` → **[Protein C](../../03-molecular/protein-c/README.md)** — Protein C deficiency (PROC mutations) is a rare but high-risk inherited thrombophilia (0.3% prevalence; 5-10× VTE risk); APC inactivates FVa/FVIIIa; warfarin-induced skin necrosis is uniquely dangerous in protein C-deficient patients starting warfarin without heparin bridge.
- `connects-to` → **[Inherited Thrombophilia](../inherited-thrombophilia/README.md)** — Inherited thrombophilia testing guides anticoagulation duration in VTE: FV Leiden and prothrombin G20210A heterozygotes require 3-6 months for first provoked VTE; high-risk deficiencies (AT, protein C/S) or recurrent unprovoked VTE → indefinite anticoagulation.
- `connects-to` → **[Heparin-Induced Thrombocytopenia](../heparin-induced-thrombocytopenia/README.md)** — HIT causes paradoxical DVT/PE (venous) and arterial thrombosis (HITT); occurs 5-10 days after heparin exposure; anti-PF4/heparin IgG → platelet activation → thrombin; argatroban, bivalirudin, and fondaparinux replace heparin in HIT; DOACs used for bridging to warfarin.
- `connects-to` → **[Antithrombin](../../03-molecular/antithrombin/README.md)** — Antithrombin deficiency (SERPINC1 mutations; 1:2,000-5,000) is the most severe inherited thrombophilia (25-50× lifetime VTE risk); UFH/LMWH efficacy requires AT → AT-deficient patients may need AT concentrate; functional AT assay needed for diagnosis.
- `connects-to` → **[Hemophilia A](../hemophilia-a/README.md)** — Severe HA (FVIII <1%) confers significant VTE protection; historical VTE rate in HA ~0.5/1000 PY vs. ~1.5-3/1000 general population; emicizumab reconstitutes intrinsic tenase; avoid high-dose APCC with emicizumab → TMA; gene therapy raising FVIII >150% increases VTE risk.
- `treated-by` → **[Warfarin](../../../03-medicine/01-modern/09-hematology/warfarin/README.md)** — Warfarin treats DVT/PE at INR 2.0–3.0 × 3–6 months for provoked VTE; indefinite for unprovoked high-risk; largely superseded by DOACs; remains first-line for antiphospholipid syndrome; LMWH bridging required at initiation.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Endothelial injury is one arm of Virchow's triad driving VTE: damaged endothelium loses its antithrombotic surface (thrombomodulin, heparan sulfate) and exposes tissue factor and von Willebrand factor, nucleating clot—why surgery, inflammation and indwelling lines provoke it.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — The lung is where venous thromboembolism turns deadly: a deep-vein thrombus that breaks loose lodges in the pulmonary arteries as a pulmonary embolism, causing hypoxia, acute right-heart strain and sudden death; CT angiography diagnoses it and large clots may need thrombolysis.
- `connects-to` → **[Sickle Cell Disease](../sickle-cell-disease/README.md)** — Sickle cell disease is a strong, often overlooked VTE risk factor: chronic hemolysis, phosphatidylserine exposure and inflammation create a hypercoagulable state, so VTE and pulmonary embolism rates are markedly raised, overlapping with in-situ pulmonary vaso-occlusion.
- `connects-to` → **[Polycythemia Vera](../polycythemia-vera/README.md)** — Polycythemia vera is a major acquired cause of venous thromboembolism: high hematocrit and JAK2-mutant prothrombotic blood drive clots, including splanchnic-vein thromboses (Budd-Chiari, portal vein) that can be the first sign—so unusual-site VTE prompts JAK2 testing.
- `connects-to` → **[Pancreatic Cancer](../pancreatic-cancer/README.md)** — Cancer is a leading cause of venous thromboembolism, and pancreatic cancer is the classic high-risk tumor (Trousseau syndrome): mucin and tissue factor make the blood intensely prothrombotic, so migratory or unprovoked VTE can be the presenting clue to an occult malignancy.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — COVID-19 dramatically raises venous thromboembolism risk: SARS-CoV-2 endothelial injury and intense inflammation drive immunothrombosis, so hospitalized patients develop DVT and pulmonary embolism at high rates and receive thromboprophylaxis, with D-dimer marking severity.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Platelets help build venous thrombi: though VTE is a fibrin-rich red clot, activated platelets still seed and propagate it, which is why some antiplatelet therapy reduces recurrence—blurring the old line between arterial and venous clots.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Estrogen is a leading reversible cause of VTE: oral contraceptives, hormone therapy and pregnancy raise clotting factors and lower anticoagulant proteins, multiplying thrombosis risk—especially when combined with factor V Leiden or other inherited thrombophilias.
- `connects-to` → **[Obesity](../obesity/README.md)** — Obesity steadily raises VTE risk: adipose-driven inflammation, higher clotting factors and venous stasis from immobility combine to promote thrombosis, so weight is an independent, modifiable risk factor that compounds surgery, pregnancy and hormonal triggers.
- `connects-to` → **[Fibrinogen](../../03-molecular/fibrinogen/README.md)** — Fibrinogen is the raw material of the venous clot: thrombin cleaves it into fibrin strands that mesh trapped red cells into the gelatinous thrombus characteristic of veins, and high fibrinogen levels independently raise venous thromboembolism risk.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Pulmonary embolism stresses the heart acutely: a large clot lodging in the pulmonary arteries suddenly raises right-ventricular afterload, so the right heart can fail and collapse—making PE a cardiovascular emergency, not just a lung problem.
- `connects-to` → **[Paroxysmal Nocturnal Hemoglobinuria](../pnh/README.md)** — PNH is a striking cause of unusual venous thrombosis: complement-driven hemolysis and platelet activation provoke clots at odd sites (hepatic, cerebral veins), so unexplained venous thromboembolism with hemolysis should prompt testing for PNH.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Neutrophils help build venous clots: in sluggish veins they cast neutrophil extracellular traps (NETs) that scaffold red cells and platelets into a thrombus, so this immunothrombosis links inflammation and infection to the risk of deep-vein clots.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — Pregnancy is a hypercoagulable state centered on the placenta: clotting factors rise to limit delivery bleeding, but this makes venous thromboembolism a leading cause of maternal death—so prophylaxis is considered in high-risk pregnancy and postpartum.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Hormones make VTE a reproductive-health issue: estrogen-containing contraceptives and hormone therapy raise clotting-factor levels and thrombosis risk, so VTE history shapes contraceptive choices and prompts caution with hormonal treatments.
- `connects-to` → **[Pulmonary Arterial Hypertension](../pulmonary-arterial-hypertension/README.md)** — Unresolved clots can scar into pulmonary hypertension: when pulmonary emboli fail to dissolve, organized thrombus narrows lung arteries causing chronic thromboembolic pulmonary hypertension (CTEPH)—a potentially curable cause treated by surgically removing the old clot.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium is clotting Factor IV, central to forming venous thrombi: the cascade that builds a clot requires calcium at multiple steps, which is why citrate that binds calcium is used to keep donated and lab blood from clotting.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Venous clots are red because they trap erythrocytes: unlike platelet-rich arterial clots, the slow-flow 'red thrombi' of veins are packed with red cells and fibrin—why stasis (immobility, long flights) is a key part of venous thromboembolism.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — A venous clot becomes deadly when it starves the lungs of oxygen: a leg clot can break off and lodge in the pulmonary arteries, blocking blood flow so the lungs cannot oxygenate—the hypoxemia of pulmonary embolism.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Veins can clot in the brain too: cerebral venous sinus thrombosis is an unusual form of venous thromboembolism, striking young women on estrogen or in pregnancy and causing headache, seizures and stroke-like deficits.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Venous clots also strike the abdomen's great veins: thrombosis of the portal or hepatic veins (Budd-Chiari) links venous thromboembolism to myeloproliferative disorders and PNH, so unusual-site clots prompt a search for hidden causes.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Veins can clot at the kidney: renal vein thrombosis is a venous thromboembolic event classically tied to nephrotic syndrome, whose urinary loss of anticoagulant proteins tips blood toward clotting.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages clean up venous clots: they invade the thrombus to break it down and remodel the vein, so when this resolution fails the clot organizes and scars, causing the post-thrombotic syndrome.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Unresolved clots turn to fibrosis in the lungs: emboli that fail to clear organize into fibrous webs that narrow pulmonary arteries, causing chronic thromboembolic pulmonary hypertension, a late and treatable consequence.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — VTE is confirmed by imaging: CT pulmonary angiography in X-ray photons finds the lung clot, and nuclear V/Q scans map blocked blood flow when contrast can't be used.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Clots can strike the gut's veins: mesenteric and portal vein thrombosis chokes the bowel's drainage, causing severe abdominal pain and, if unrelieved, bowel infarction.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Some clots are born in the marrow: JAK2-driven myeloproliferative neoplasms overproduce blood cells and are a major cause of unprovoked and unusual-site venous thrombosis.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reveals the venous clot's layered build: alternating bands of pale platelet-fibrin and red-cell-rich layers — the lines of Zahn — mark a thrombus that formed in flowing blood before death, distinguishing it from a postmortem clot.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — A deep vein clot announces itself through the skin: the leg swells, warms, and reddens, and in the dreaded phlegmasia cerulea dolens it turns tense and blue as the blocked outflow threatens the limb.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — Clots can strike unusual veins: splanchnic thrombosis of the splenic, portal, or mesenteric veins is a recognized form of VTE, often the first clue to a hidden clotting disorder or abdominal cancer.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies can tip the blood toward clotting: antiphospholipid antibodies are a leading acquired cause of VTE, and the HIT antibody against PF4-heparin paradoxically clots while dropping the platelet count.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — A clot can form in the brain's own veins: cerebral venous sinus thrombosis is a VTE of the cranial drainage, backing up pressure and infarcting neurons to cause headache, seizures, and focal deficits.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Most VTE begins in the legs: a deep vein thrombosis forms in the calf and thigh veins, often after immobility or surgery, and leaves the post-thrombotic limb swollen and aching long after the clot.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — The vein wall is part of the problem: stasis and damage to the smooth-muscle-lined vein and its valves let clot form, and after a DVT the scarred, incompetent valves drive the chronic swelling of post-thrombotic syndrome.
- `connects-to` → **[Stroke](../stroke/README.md)** — A leg clot can reach the brain: through a patent foramen ovale a venous thrombus crosses to the arterial side as a paradoxical embolism, a recognized cause of cryptogenic stroke in younger patients.
- `connects-to` → **[Multiple Myeloma](../multiple-myeloma/README.md)** — Cancer and its drugs ignite clotting: malignancy is a major VTE risk, and multiple myeloma is especially thrombogenic — its immunomodulatory drugs (thalidomide, lenalidomide) demand routine anticoagulant prophylaxis.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Stasis and strain tie the clot to the failing heart: the sluggish circulation of heart failure breeds venous clots, while a large pulmonary embolism can acutely overwhelm the right heart into failure — a two-way danger.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — The healthy vessel resists clotting with nitric oxide: endothelial NO keeps platelets quiet and vessels open, so when endothelial dysfunction cuts NO, the balance tips toward the thrombosis of VTE.
- `connects-to` → **[Inflammatory Bowel Disease](../inflammatory-bowel-disease/README.md)** — Gut inflammation clots the veins: active inflammatory bowel disease is a strong acquired risk for VTE, the systemic inflammation raising clotting factors and platelets, so hospitalized flares get thromboprophylaxis.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Sepsis clots the small and large veins alike: systemic inflammation activates coagulation (immunothrombosis), so septic patients face both DIC and limb and pulmonary VTE — one reason thromboprophylaxis is standard in critical illness.
- `connects-to` → **[Glioblastoma](../glioblastoma/README.md)** — Few cancers clot like glioblastoma: brain tumors express abundant tissue factor and carry one of the highest VTE rates of any malignancy, posing the hard problem of anticoagulating a patient prone to intracranial bleeding.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Inflammation seeds the venous clot: NLRP3-driven IL-1β and the neutrophil extracellular traps it promotes provide the scaffold for immunothrombosis, linking the inflammasome to the pathogenesis of venous thromboembolism.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Inflammation makes the vein wall clot: NF-κB activation in endothelium and monocytes induces tissue factor and adhesion molecules, the thromboinflammatory switch that converts an inflamed vessel into a site of venous thrombosis.
- `connects-to` → **[Colorectal Cancer](../colorectal-cancer/README.md)** — A common cancer that clots: colorectal cancer is a frequent driver of cancer-associated thrombosis, its tumor tissue factor and the surgery and chemotherapy it requires all raising venous thromboembolism risk.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Failing kidneys tip toward clotting: chronic kidney disease, and especially nephrotic-range protein loss, creates a hypercoagulable state that raises the risk of deep-vein thrombosis and pulmonary embolism.
- `connects-to` → **[Ovarian Cancer](../ovarian-cancer/README.md)** — An unprovoked clot can herald it: ovarian and other adenocarcinomas are strongly prothrombotic, so a venous thromboembolism without obvious cause can be the presenting sign that prompts the search uncovering the tumor.
- `connects-to` → **[NASH](../nash/README.md)** — The fatty liver leans toward clotting: NASH raises fibrinogen and PAI-1 and lowers fibrinolysis, an under-recognized prothrombotic state that increases the risk of venous thromboembolism and portal vein thrombosis.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Surviving a clot leaves a mental mark: many people develop persistent anxiety and depression after a pulmonary embolism or DVT, a post-thrombotic psychological distress akin to post-traumatic stress.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Damaged veins leave chronic ulcers: deep vein thrombosis injures venous valves, and the resulting post-thrombotic syndrome and venous hypertension produce slow-healing venous leg ulcers.
- `connects-to` → **[Gastric Cancer](../gastric-cancer/README.md)** — An unprovoked clot can herald hidden cancer: Trousseau's syndrome of migratory thrombosis points to occult malignancy, and adenocarcinomas like gastric cancer are classic culprits found on the ensuing search.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Its long anticoagulation can cost bone: prolonged heparin used to treat venous thromboembolism, especially in pregnancy, lowers bone mineral density, a recognized treatment-related bone loss.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Half of it lands in the lungs: a deep-vein clot that breaks loose travels to the pulmonary arteries as pulmonary embolism, abruptly blocking gas exchange and straining the right heart, the lethal face of VTE.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It clots the gut's veins and its drugs bleed it: VTE includes splanchnic, portal and mesenteric vein thrombosis threatening the bowel, while the anticoagulants treating it raise the risk of GI haemorrhage.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Old clots scar the skin: post-thrombotic syndrome after a DVT causes chronic venous stasis with pigmentation and leg ulcers, and warfarin can rarely cause acute skin necrosis.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — A large clot can stop the heart: massive pulmonary embolism causes acute right-heart strain and obstructive shock, and via a patent foramen ovale a venous clot can cause paradoxical arterial embolism.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Clots strike the brain's veins too: cerebral venous sinus thrombosis is venous thromboembolism within the skull, causing headache, seizures and raised intracranial pressure.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Hormones tip the balance toward clotting: oestrogen in combined contraceptives and HRT, and cortisol excess, raise clotting factors and are major hormonal drivers of venous thromboembolism.
- `connects-to` → **[Renal System](../renal-system/README.md)** — The leaky kidney clots: nephrotic syndrome loses antithrombin in the urine, creating a hypercoagulable state that classically causes renal vein thrombosis and other venous clots.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Inflammation and clotting are intertwined: 'immunothrombosis' sees neutrophil extracellular traps and inflammatory cytokines trigger coagulation, linking infection and autoimmunity to venous thrombosis.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It leaves a lasting swelling: after a deep-vein thrombosis, valve damage and impaired drainage cause the post-thrombotic syndrome, a chronic oedema that mimics lymphatic failure.
- `connects-to` → **[Aspirin](../../../03-medicine/01-modern/04-cardio/aspirin/README.md)** — An option for prevention: aspirin gives modest protection against recurrent venous thromboembolism and is used for prophylaxis after some orthopaedic surgery, though anticoagulants are more effective.
- `connects-to` → **[SARS-CoV-2](../../../02-pathogen/01-viruses/sars-cov-2/README.md)** — A virus that clots the veins: severe COVID-19 markedly raises venous thromboembolism risk through endothelial injury, inflammation and immobility, prompting routine thromboprophylaxis in hospital.
- `connects-to` → **[NSCLC](../nsclc/README.md)** — Cancer drives clotting: lung adenocarcinoma and other cancers create a hypercoagulable Trousseau state, making venous thromboembolism a common and dangerous complication of malignancy.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — A large PE fails the right heart: pulmonary embolism abruptly raises pulmonary pressure, straining and dilating the right ventricle — acute RV failure is the mechanism of death in massive PE, tracked by troponin and echo.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Chemo adds to the clot risk: beyond the cancer's own hypercoagulability, agents like cisplatin and thalidomide-class drugs are prothrombotic, so cancer-associated VTE is managed with LMWH or direct oral anticoagulants.
- `connects-to` → **[Essential Thrombocythemia](../essential-thrombocythemia/README.md)** — Too many platelets clot the veins: essential thrombocythemia and other myeloproliferative neoplasms cause venous thromboembolism, including unusual-site clots like splanchnic and cerebral vein thrombosis, despite the high platelet count.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Pulmonary embolism at the gas-exchange unit: a clot lodging in the pulmonary arteries creates alveolar dead space—ventilated but not perfused—causing the hypoxaemia and, occasionally, pulmonary infarction of PE.
- `connects-to` → **[Thalassemia](../thalassemia/README.md)** — A prothrombotic anaemia: thalassaemia, especially after splenectomy, carries a hypercoagulable state with procoagulant red-cell membranes and thrombocytosis that raises venous thrombosis risk.
- `connects-to` → **[Renal Cell Carcinoma](../renal-cell-carcinoma/README.md)** — Tumour thrombus in the vein: renal cell carcinoma characteristically grows as a tumour thrombus up the renal vein and inferior vena cava, and its cancer-associated hypercoagulability adds to VTE risk.
- `connects-to` → **[Stroke](../stroke/README.md)** — Paradoxical embolism: a venous clot can cross a patent foramen ovale into the arterial circulation and lodge in the brain, turning a deep-vein thrombosis into a paradoxical stroke.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — Cancer-associated thrombosis: breast cancer raises VTE risk through tumour procoagulants, chemotherapy and hormonal therapy like tamoxifen, a common Trousseau-type complication.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Surgery and fracture provoke clots: major orthopaedic surgery and long-bone fractures of the cortical bone are among the strongest provokers of deep-vein thrombosis, driving routine post-operative prophylaxis.
- `connects-to` → **[Myelofibrosis](../myelofibrosis/README.md)** — Myeloproliferative thrombosis: like polycythaemia vera and essential thrombocythaemia, myelofibrosis is strongly thrombogenic and a leading cause of splanchnic (portal and hepatic vein) thrombosis.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Splanchnic vein clots: thrombosis of the portal vein or the hepatic veins (Budd-Chiari syndrome) draining the hepatic lobule is a distinct, often MPN-driven form of venous thromboembolism.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — Renal vein thrombosis: nephrotic-range proteinuria from glomerular disease loses antithrombin in the urine, creating a hypercoagulable state that classically thromboses the renal vein.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — Immunothrombosis: IL-6 drives the inflammation-coagulation crosstalk that raises VTE risk in infection, cancer and inflammatory disease, linking acute illness to clot formation.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Prothrombotic inflammation: TNF-α activates endothelium to express tissue factor and downregulate anticoagulant pathways, a mechanism connecting systemic inflammation to venous thrombosis.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Stasis hypoxia: venous stasis creates local hypoxia that stabilises HIF-1α and upregulates procoagulant factors, part of why immobility and stasis precipitate deep-vein thrombosis.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — NETosis initiation: neutrophil extracellular traps rich in S100A8/A9 provide the scaffold and trigger for venous thrombus formation, a core mechanism of immunothrombosis behind deep-vein thrombosis.
- `connects-to` → **[PF4](../../03-molecular/pf4/README.md)** — Platelet activation: PF4 released from activated platelets within the forming venous thrombus promotes aggregation and, in HIT and VITT, drives the antibody-mediated thrombosis that VTE workups must exclude.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — Thrombus scaffold: plasma fibronectin is cross-linked into the fibrin meshwork of venous clots, stabilising the thrombus that obstructs the vein or embolises to the lung.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — CCL2 recruits monocytes to the forming venous thrombus, where their tissue-factor expression amplifies thrombin generation—the inflammation arm of the immunothrombosis that initiates deep-vein thrombosis in the low-flow valve pockets.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — TLR4 sensing of DAMPs on activated venous endothelium and leukocytes promotes the tissue-factor and neutrophil-extracellular-trap release that nucleate venous thrombi, linking sterile inflammation to clotting.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — The platelet thromboxane A2/endothelial prostacyclin balance governs the platelet activation that propagates a venous thrombus, the balance that low-dose aspirin shifts to reduce recurrent VTE risk after anticoagulation ends.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — The intrinsic contact system—factor XII and kallikrein, which also generates bradykinin—feeds venous thrombus growth, making factor XI/XII the targets of the new anticoagulants that aim to block clotting without causing bleeding.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement activation generating C3 fragments amplifies platelet activation and tissue factor, an inflammatory limb of immunothrombosis that compounds the stasis and hypercoagulability driving venous thromboembolism.
- `connects-to` → **[RAGE](../../03-molecular/rage/README.md)** — DAMPs such as HMGB1 signaling through RAGE on endothelium and leukocytes promote the tissue-factor expression and NET formation that knit together the immunothrombosis of venous clot.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — Endothelial Angiopoietin-2 activation shifts the vein-wall endothelium to a procoagulant, permeable phenotype, part of the endothelial-injury limb of Virchow's triad in venous thromboembolism.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β, downstream of the NLRP3 inflammasome already mapped, induces endothelial and monocyte tissue factor that initiates the coagulation of venous thrombosis.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Complement activation (C3 already mapped, through C5) amplifies platelet and endothelial activation in venous thromboembolism, part of the thromboinflammatory crosstalk that promotes clot formation.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR-MyD88-NF-κB innate signaling (TLR4 and NF-κB already mapped) underlies the immunothrombosis in which activated neutrophils and monocytes — through NETs and tissue factor — seed venous thrombus formation.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Raised endothelin-1 from a dysfunctional endothelium shifts the vessel wall toward the vasoconstricted, procoagulant state that, with venous stasis, completes Virchow's triad in venous thromboembolism.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — VEGF-driven angiogenesis participates in thrombus organization and recanalization, the vascular remodeling that determines resolution versus the post-thrombotic syndrome after venous thromboembolism.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling in platelets and endothelium amplifies the activation responses that initiate venous thrombosis.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Endothelial and platelet PI3K-AKT signaling regulates the procoagulant and adhesive phenotype that drives venous thromboembolism.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 promotes the neutrophil-extracellular-trap-driven thromboinflammation central to venous thrombus formation.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — DNA within neutrophil extracellular traps engages cGAS-STING, linking NET-driven sterile inflammation to the thrombus formation of venous thromboembolism.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling transduces the inflammatory cytokine response that promotes the procoagulant endothelial phenotype of venous thromboembolism.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K-AKT signaling (AKT already mapped) in platelets and endothelium supports the activated, procoagulant phenotype that drives venous thromboembolism.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO downstream of PI3K-AKT signaling (AKT and PIK3CA already mapped) regulates the endothelial quiescence-versus-activation balance relevant to venous thromboembolism.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling modulates the endothelial inflammatory activation that contributes to venous thrombosis.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK1/2-STAT cytokine signaling (IL-6-STAT3 already mapped) amplifies the inflammatory endothelial and platelet activation driving the thromboinflammation of venous thromboembolism.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the platelet-activation and endothelial signaling relevant to the thrombus formation of venous thromboembolism.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR signaling in activated endothelium and immune cells participates in the immunothrombosis of venous thromboembolism.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK metabolic signaling in endothelial cells modulates the vascular homeostasis whose disruption promotes venous thromboembolism.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the endothelial and leukocyte responses relevant to the thrombo-inflammation of venous thromboembolism.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the platelet activation and endothelial responses driving venous thromboembolism.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven monocyte recruitment contributes to the thrombo-inflammation and thrombus resolution of venous thromboembolism.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic modulation of the coagulation and endothelial gene expression relevant to venous thromboembolism.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the endothelial and leukocyte interactions of the thrombo-inflammation of venous thromboembolism.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the endothelial activation and thrombo-inflammation of venous thromboembolism.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the thromboinflammation of venous thromboembolism.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the endothelial and coagulation gene programs relevant to venous thromboembolism.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine signaling provides platelet-inhibitory and vascular modulation relevant to venous thromboembolism.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Pulmonary embolism strain: a large pulmonary embolism strains the right ventricle, and troponin release marking that myocardial injury identifies the intermediate-to-high-risk patients who may need thrombolysis rather than anticoagulation alone.
- `connects-to` → **[BNP](../../03-molecular/bnp/README.md)** — Right-ventricular stretch: BNP released from the pressure-loaded right ventricle in pulmonary embolism complements troponin in risk stratification, flagging the ventricular dysfunction that predicts adverse outcomes.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Obesity risk: obesity is a strong independent risk factor for venous thromboembolism through venous stasis and a prothrombotic state, and the adipokine leptin promotes platelet activation and coagulation.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — Pregnancy hypercoagulability: pregnancy, sustained by progesterone and estrogen (already mapped), is a strongly prothrombotic state with venous stasis, making venous thromboembolism a leading cause of maternal death and a target for prophylaxis.
- `connects-to` → **[Myeloproliferative neoplasms](../myeloproliferative-neoplasms/README.md)** — Clonal thrombophilia: JAK2-driven myeloproliferative neoplasms create an acquired hypercoagulable state, often presenting as venous thrombosis at unusual sites such as the splanchnic or cerebral veins, an important cause to screen for.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Metabolic prothrombotic state: insulin resistance and the metabolic syndrome raise PAI-1 and fibrinogen (already mapped), an acquired prothrombotic tendency that compounds the venous-thromboembolism risk of the obesity (leptin already mapped) it accompanies.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative thrombogenesis: the stasis and hypoxia of the venous thrombus generate reactive oxygen species, to which xanthine oxidase contributes, promoting the endothelial (already mapped) dysfunction and thrombo-inflammation that propagate venous thromboembolism.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Thrombo-inflammation balance: coagulation and inflammation are intertwined, and the anti-inflammatory IL-10 opposes the pro-inflammatory signals (IL-6, TNF and IL-1 already mapped) that amplify the immunothrombosis of venous thromboembolism.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Platelet serotonin: serotonin released from activated platelets (PF4 already mapped) causes vasoconstriction and amplifies platelet aggregation, contributing to the thrombus formation and propagation of venous thromboembolism.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Thrombo-inflammation balance: IL-4 and the M2 anti-inflammatory arm (IL-10 already mapped) counter the pro-inflammatory signals (IL-6, TNF and IL-1 already mapped) of the immunothrombosis that amplifies venous thromboembolism.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Platelet zinc and coagulation: zinc released from the activated platelets (already mapped) promotes the contact pathway and fibrin formation (fibrinogen and thrombin already mapped), adding to the clotting tendency in venous thromboembolism.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Metabolic prothrombotic risk: dyslipidaemia and the metabolic syndrome (leptin and insulin already mapped) add an acquired hypercoagulable state, and raised cholesterol contributes to the venous as well as arterial thrombotic risk.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — Antiphospholipid antibodies: the IgG antiphospholipid antibodies of the antiphospholipid syndrome are a major acquired thrombophilia causing venous (and arterial) thromboembolism, testing for which is part of the workup of unprovoked VTE.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 inflammation: IL-13, with IL-4 (already mapped), is part of the type-2 immune arm of the inflammation (IL-6 already mapped) that contributes to the venous-thrombus resolution and the post-thrombotic remodelling.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Obesity and hypercoagulability: the fall in adiponectin, with leptin (already mapped), of the obesity that is a major risk factor for venous thromboembolism promotes the prothrombotic and inflammatory state.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the obesity (a major VTE risk) and the prothrombotic inflammatory state.
- `connects-to` → **[Pulmonary arterial hypertension](../pulmonary-arterial-hypertension/README.md)** — CTEPH: the chronic thromboembolic pulmonary hypertension is a long-term complication of the unresolved pulmonary embolism of venous thromboembolism.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Right-heart strain: the pulmonary embolism strains the right heart (troponin and BNP already mapped), the acute RV failure the cause of the PE death.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate immunothrombosis: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, is part of the innate immune contribution to the immunothrombosis (neutrophils already mapped) of venous thromboembolism.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 immunothrombosis: the IFN-γ of the T cells is the type-II interferon arm of the inflammatory dimension (IL-6 and TNF already mapped) that potentiates the venous thrombosis.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immunothrombotic inflammation of venous thromboembolism.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the inflammatory milieu of the immunothrombosis of venous thromboembolism.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immunothrombotic inflammation of venous thromboembolism.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the inflammatory milieu of venous thromboembolism.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the myeloid tissue-factor expression and the neutrophil (already mapped) NETosis of the immunothrombosis of venous thromboembolism.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) at the complement–coagulation interface of the immunothrombosis of venous thromboembolism.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Contact/complement regulation: the C1-esterase inhibitor regulates both the classical complement and the contact (intrinsic-coagulation) pathways, a key brake at the complement–coagulation interface of venous thromboembolism.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Thromboinflammation: osteopontin, released by the activated platelets (already mapped), is a matricellular mediator amplifying the neutrophil (already mapped) NET-driven immunothrombosis of venous thromboembolism.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Thrombotic iron: transferrin, the iron carrier, reflects the disordered iron handling that, with the venous stasis and hypercoagulability, is part of the thrombotic-risk context of venous thromboembolism.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — Adaptive immunothrombosis: the CD4 T-helper cells contribute to the adaptive-immune dimension of the inflammation that primes the venous endothelium (already mapped) for the immunothrombosis of venous thromboembolism.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-thromboinflammation axis: TSLP, from activated endothelium (already mapped) and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2/eosinophil imbalance of the thromboinflammation of venous thromboembolism.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Thrombogenic erythropoiesis: erythropoietin drives erythrocytosis and increases blood viscosity, amplifying the venous stasis and the hypercoagulability of the thrombotic-risk context of venous thromboembolism.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell venous inflammation: histamine, from mast cells (already mapped), increases venous endothelial permeability and primes the coagulation–inflammation interface of the immunothrombosis of venous thromboembolism.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian coagulation: melatonin has antithrombotic and antioxidant effects, reducing platelet (already mapped) activation and the endothelial (already mapped) oxidative stress that prime the nocturnal hypercoagulability and the thrombotic risk of venous thromboembolism.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Sex-hormone coagulation: testosterone promotes erythropoiesis (EPO already mapped) and haematocrit elevation, increases blood viscosity and venous stasis; male sex-hormone levels and androgen-therapy are recognised risk factors for venous thromboembolism.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Thrombus organisation matrix: periostin, from fibroblasts and endothelial cells (already mapped) at the organising thrombus, contributes to the ECM remodelling and the fibrous transformation of the venous thrombus in venous thromboembolism.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — VTE prolactin: prolactin, via PRLR on endothelial cells (already mapped) and macrophages (already mapped), promotes platelet (already mapped) activation; hyperprolactinaemia amplifies the thrombin (already mapped) and IL-6 (already mapped) thrombosis of venous thromboembolism.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — VTE oxytocin: oxytocin, via OXTR on endothelial cells (already mapped) and macrophages (already mapped), attenuates thromboinflammation; oxytocin deficiency amplifies the thrombin (already mapped) and NF-κB (already mapped) coagulation cascade of venous thromboembolism.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — VTE vasopressin: vasopressin, via V1aR on endothelial cells (already mapped) and smooth-muscle cells (already mapped), modulates vascular tone; vasopressin dysregulation amplifies the thrombin (already mapped) and platelet (already mapped) coagulation cascade of VTE.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Endothelial antioxidant: selenium, as GPx in endothelial cells (already mapped) and platelets (already mapped), scavenges ROS driving thromboinflammation; selenium deficiency amplifies the thrombin (already mapped) and NF-κB (already mapped) coagulation cascade of venous thromboembolism.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Haemostatic thyroid axis: iodine-dependent thyroid hormones modulate haemostatic factor expression (fibrinogen already mapped) and endothelial (already mapped) function; iodine deficiency impairs thyroid-mediated regulation of the thrombin (already mapped) cascade of venous thromboembolism.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Prothrombotic salt axis: high dietary sodium promotes endothelial (already mapped) dysfunction and a prothrombotic state; sodium-induced aldosterone elevation amplifies the platelet (already mapped) and NF-κB (already mapped) thromboinflammatory cascade of venous thromboembolism.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — VTE magnesium: magnesium stabilises endothelial cell (already mapped) function and attenuates platelet (already mapped) aggregation; magnesium deficiency amplifies NF-κB (already mapped) and thrombin (already mapped) and fibrinogen (already mapped) procoagulant cascade in VTE.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — VTE iron: iron overload promotes endothelial cell (already mapped) and platelet (already mapped) oxidative activation; iron-induced NF-κB (already mapped) and thrombin (already mapped) amplify fibrinogen (already mapped) and coagulation cascade of venous thromboembolism.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — VTE copper: copper-dependent SOD in endothelial cells (already mapped) and macrophages (already mapped) quenches ROS; copper deficiency amplifies NF-κB (already mapped) and thrombin (already mapped) and fibrinogen (already mapped) procoagulant cascade of venous thromboembolism.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — VTE potassium: potassium efflux in endothelial cells (already mapped) and platelets (already mapped) modulates vascular tone; potassium dysregulation amplifies NF-κB (already mapped) and thrombin (already mapped) thromboinflammatory cascade of VTE.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — VTE carbon: carbon, as metabolic backbone of clotting factors in endothelial cells (already mapped) and macrophages (already mapped), drives coagulation; carbon dysregulation amplifies NF-κB (already mapped) and thrombin (already mapped) procoagulant cascade of VTE.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — VTE chloride: chloride channels in endothelial cells (already mapped) and macrophages (already mapped) regulate vascular tone; chloride dysregulation amplifies NF-κB (already mapped) and thrombin (already mapped) and fibrinogen (already mapped) cascade of VTE.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — VTE hydrogen: hydrogen, via redox homeostasis in endothelial cells (already mapped) and macrophages (already mapped), quenches procoagulant ROS; hydrogen dysregulation amplifies NF-κB (already mapped) and thrombin (already mapped) and fibrinogen (already mapped) cascade of VTE.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — VTE nitrogen: nitric oxide from endothelial cells (already mapped) and macrophages (already mapped) modulates vascular tone; nitrogen imbalance amplifies NF-κB (already mapped) and thrombin (already mapped) and fibrinogen (already mapped) procoagulant cascade of VTE.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — VTE sulfur: hydrogen sulfide from endothelial cells (already mapped) and macrophages (already mapped) modulates vascular tone; sulfur deficiency amplifies NF-κB (already mapped) and thrombin (already mapped) and fibrinogen (already mapped) cascade of VTE.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — VTE PD-1: PD-1 on macrophages (already mapped) and T-helper-cell (already mapped) modulates vascular immune homeostasis; PD-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and thrombin (already mapped) procoagulant cascade of VTE.

[^agnelli-2013-amplify-apixaban-vte]: Agnelli G, Buller HR, Cohen A, et al. Oral apixaban for the treatment of acute venous thromboembolism. *N Engl J Med.* 2013;369(9):799-808. [doi:10.1056/NEJMoa1302507](https://doi.org/10.1056/NEJMoa1302507) · [PubMed 23808982](https://pubmed.ncbi.nlm.nih.gov/23808982/)
[^bauersachs-2010-einstein-rivaroxaban]: EINSTEIN Investigators. Oral rivaroxaban for symptomatic venous thromboembolism. *N Engl J Med.* 2010;363(26):2499-2510. [doi:10.1056/NEJMoa1007903](https://doi.org/10.1056/NEJMoa1007903) · [PubMed 21128814](https://pubmed.ncbi.nlm.nih.gov/21128814/)
[^konstantinides-2020-esc-pe]: Konstantinides SV, Meyer G, Becattini C, et al. 2019 ESC Guidelines for the diagnosis and management of acute pulmonary embolism. *Eur Heart J.* 2020;41(4):543-603. [doi:10.1093/eurheartj/ehz405](https://doi.org/10.1093/eurheartj/ehz405) · [PubMed 31504429](https://pubmed.ncbi.nlm.nih.gov/31504429/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
