---
schema: human-scale-entry/v1
id: inherited-thrombophilia
name: Inherited Thrombophilia
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Inherited thrombophilias are genetic risk factors for VTE; Factor V Leiden R506Q (5% Europeans; APC resistance) and prothrombin G20210A are most common; protein C/S and antithrombin deficiencies are rarer but higher-risk. Duration of anticoagulation is the main clinical impact."
aliases: ["inherited thrombophilia", "hereditary thrombophilia", "thrombophilia", "factor V Leiden", "FVL", "prothrombin G20210A", "APC resistance", "thrombophilic disorder"]
sources:
  - id: dahlback-2008-protein-c-review
    type: peer-reviewed
    cite: "Dahlbäck B. Advances in understanding pathogenic mechanisms of thrombophilic disorders. Blood. 2008;112(1):19-27."
    doi: "10.1182/blood-2008-01-077909"
    pmid: "18574048"
    url: "https://doi.org/10.1182/blood-2008-01-077909"
  - id: bertina-1994-factor-v-leiden
    type: peer-reviewed
    cite: "Bertina RM, Koeleman BP, Koster T, et al. Mutation in blood coagulation factor V associated with resistance to activated protein C. Nature. 1994;369(6475):64-67."
    doi: "10.1038/369064a0"
    pmid: "8164741"
    url: "https://doi.org/10.1038/369064a0"
  - id: kearon-2016-antithrombotic-therapy
    type: clinical-guideline
    cite: "Kearon C, Akl EA, Ornelas J, et al. Antithrombotic therapy for VTE disease: CHEST guideline and expert panel report. Chest. 2016;149(2):315-352."
    doi: "10.1016/j.chest.2015.11.026"
    pmid: "26867832"
    url: "https://doi.org/10.1016/j.chest.2015.11.026"
cross_links:
  - target: 01-human/03-molecular/protein-c
    relation: connects-to
    note: "Protein C deficiency is the third most common inherited thrombophilia (0.3% prevalence; 5-10× VTE risk); APC pathway inactivates FVa/FVIIIa → thrombosis risk from impaired anticoagulant mechanism; warfarin-induced skin necrosis risk on protein C–deficient patients."
  - target: 01-human/03-molecular/thrombin
    relation: connects-to
    note: "Factor V Leiden (R506Q) causes APC resistance: thrombin-activated FVa at Arg506 cannot be cleaved → uncontrolled prothrombinase complex → excess thrombin; thrombomodulin-bound thrombin activates protein C → the central anticoagulant checkpoint that FVL undermines."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "VTE (DVT/PE) is the primary manifestation of inherited thrombophilia; risk is multiplicative (FVL + OCP = 35× VTE risk); thrombophilia guides anticoagulation duration (indefinite for AT deficiency, homozygous FVL, compound heterozygous); do not test during acute VTE."
  - target: 01-human/07-system/antiphospholipid-syndrome
    relation: connects-to
    note: "APS is the most important acquired thrombophilia, causing indistinguishable VTE and arterial thrombosis to inherited thrombophilia; combined APS + inherited thrombophilia (e.g., FVL + triple-positive aPL) confers extreme thrombotic risk; APS is excluded by thrombophilia workup."
  - target: 01-human/03-molecular/antithrombin
    relation: connects-to
    note: "Antithrombin deficiency (0.02-0.04% prevalence; 25-50× VTE risk) is the highest-risk inherited thrombophilia; type IIa reactive-site mutations (Arg393His) most thrombogenic; UFH/LMWH require AT for efficacy; AT concentrate needed peri-surgery/delivery."
  - target: 01-human/07-system/hemophilia-a
    relation: connects-to
    note: "Inherited thrombophilia is the mirror image of hemophilia — a clotting excess versus a bleeding deficiency; the contrast is mechanistic, since factor V Leiden makes FVa resist shutdown by activated protein C, whose downstream targets are missing or weak in hemophilia."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver synthesizes nearly all coagulation proteins, including the anticoagulants protein C, protein S, and antithrombin whose inherited deficiencies cause thrombophilia; hepatic failure causes a mixed coagulopathy, and warfarin blocks vitamin-K-dependent factor synthesis."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Inherited thrombophilias (factor V Leiden, prothrombin G20210A) cause venous, not arterial, thrombosis — so they are not established risk factors for ischemic stroke or MI and do not warrant anticoagulation for arterial events; antiphospholipid syndrome is the exception."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Healthy endothelium is antithrombotic, displaying thrombomodulin that activates protein C and heparan sulfate for antithrombin; inherited thrombophilias (factor V Leiden, protein C/S or antithrombin deficiency) cripple these endothelial-anchored brakes, tilting toward clotting."
  - target: 01-human/07-system/heparin-induced-thrombocytopenia
    relation: connects-to
    note: "Both are prothrombotic but differ in origin: inherited thrombophilia is a germline anticoagulant defect, HIT an acquired antibody-mediated platelet activation; a thrombophilic patient who develops HIT faces compounded clot risk, and both demand non-heparin anticoagulation."
  - target: 01-human/07-system/pnh
    relation: connects-to
    note: "PNH is an acquired thrombophilia: loss of GPI-anchored complement regulators drives hemolysis and platelet activation → thrombosis in unusual sites (hepatic, cerebral); like inherited thrombophilias it presents with unexplained VTE, but its mechanism is complement, not factors."
  - target: 01-human/07-system/polycythemia-vera
    relation: connects-to
    note: "Inherited thrombophilia and polycythemia vera are inherited versus acquired prothrombotic states: thrombophilia (factor V Leiden, prothrombin G20210A) tilts toward clotting, while PV's JAK2 thickens the blood—both raise venous thrombosis, including splanchnic clots."
  - target: 01-human/07-system/disseminated-intravascular-coagulation
    relation: connects-to
    note: "Inherited thrombophilia and DIC are opposite ends of clotting dysregulation: thrombophilia is a stable inherited tilt toward thrombosis, while DIC is acute systemic coagulation activation consuming factors and platelets—paradoxically causing both clotting and bleeding."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Inherited thrombophilia mainly raises venous, not arterial, thrombosis—unlike atherosclerosis: factor V Leiden and prothrombin mutations drive DVT and PE, while atherosclerotic thrombosis is plaque-driven, so thrombophilia testing is reserved for venous events."
  - target: 01-human/07-system/myeloproliferative-neoplasms
    relation: connects-to
    note: "Myeloproliferative neoplasms are a major acquired thrombophilia: JAK2-mutant blood is intrinsically prothrombotic, causing arterial and venous (including splanchnic) clots like inherited thrombophilias—so unexplained thrombosis at unusual sites warrants JAK2 testing."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "Inherited thrombophilia can cause pulmonary hypertension: recurrent pulmonary emboli that fail to resolve organize into fibrotic obstruction, causing chronic thromboembolic pulmonary hypertension (CTEPH)—a complication surgically curable by endarterectomy."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Platelets are central to the arterial thrombosis of thrombophilia: while inherited thrombophilias mainly drive venous clots, platelet activation drives arterial events—so antiplatelet and anticoagulant therapy target different arms of clot formation."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Estrogen multiplies the clot risk of inherited thrombophilia: oral contraceptives, hormone therapy and pregnancy raise clotting factors, so a factor V Leiden carrier faces sharply higher venous thrombosis risk on estrogen—central to contraceptive counseling."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Pulmonary embolism is the feared endpoint of inherited thrombophilia: deep vein clots break off and lodge in the lungs, so a young or recurrent unprovoked PE prompts thrombophilia testing—and the risk guides how long anticoagulation continues."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Inherited thrombophilia causes clots in unusual sites like the cerebral veins: prothrombotic mutations, especially with estrogen, predispose to cerebral venous sinus thrombosis—so an unexplained young stroke or sinus thrombosis warrants a thrombophilia workup."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "Inherited thrombophilia threatens the placenta: clots in the placental circulation are linked to recurrent miscarriage, pre-eclampsia, growth restriction, and stillbirth—so obstetric complications are a major reason thrombophilia is tested for in women."
  - target: 01-human/03-molecular/fibrinogen
    relation: connects-to
    note: "Fibrinogen ties to thrombophilia at both ends: rare inherited dysfibrinogenemia can make a clot-prone fibrin, and high fibrinogen levels are themselves prothrombotic—so the very protein that forms clots can be a hereditary or acquired thrombosis risk."
  - target: 01-human/07-system/sickle-cell-disease
    relation: connects-to
    note: "Sickle cell disease is a hypercoagulable state in its own right: chronic hemolysis, activated platelets, and endothelial damage tip blood toward clotting, so it compounds inherited thrombophilia and raises venous thromboembolism risk beyond its vaso-occlusive crises."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium is coagulation Factor IV, central to the clotting that thrombophilia tips toward excess: it bridges clotting-factor complexes to membranes, so it underlies the cascade—and citrate that chelates it keeps lab tubes and stored blood from clotting."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "The liver's hepatocytes make both sides of the clotting balance: they synthesize procoagulant factors and the natural anticoagulants protein C, protein S and antithrombin—so inherited deficiencies of these hepatocyte products cause thrombophilia."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Obesity compounds inherited thrombophilia: excess adipose tissue raises clotting factors and inflammation and impairs fibrinolysis, so it multiplies the venous-thrombosis risk of a Factor V Leiden or prothrombin variant—gene meets environment."
  - target: 01-human/03-molecular/von-willebrand-factor
    relation: connects-to
    note: "High von Willebrand factor is itself a thrombophilia: elevated vWF—from genes, inflammation, or aging—makes platelets stickier and raises clot risk, adding to the inherited deficiencies of natural anticoagulants behind familial thrombosis."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Thrombophilia is amplified by neutrophil NETs: neutrophils cast out DNA webs (NETs) that scaffold platelets and clotting factors into clots, so this immunothrombosis turns inflammation into the venous thrombi that thrombophilia predisposes to."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Low oxygen and stasis tip thrombophilia into clots: immobility and hypoxia (long flights, illness) slow venous flow and switch on procoagulant signals, providing the trigger that turns an inherited clotting tendency into an actual thrombosis."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Thrombophilia can clot the kidney's veins: renal vein thrombosis is a classic unusual-site clot, abruptly causing flank pain, blood in the urine, and swelling as the kidney's venous drainage is blocked."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "Thrombophilia drives clots in the splanchnic veins: thrombosis of the splenic and portal veins draining the spleen and gut is a hallmark unusual-site event, causing splenomegaly and portal hypertension."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "Thrombophilia can infarct the adrenal glands: thrombosis of their veins triggers hemorrhagic adrenal infarction, which can precipitate life-threatening adrenal failure—a rare but lethal unusual-site complication."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Confirming thrombophilia's clots relies on imaging: CT angiography and lung scans read in X-ray photons locate the deep-vein thromboses and pulmonary emboli that prompt a hypercoagulable workup."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Red cells thicken thrombophilic blood: in polycythemia and sickle cell disease, excess or misshapen erythrocytes raise viscosity and slow flow, promoting the clotting these prothrombotic states are known for."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Some thrombophilias are born in the bone marrow: JAK2-driven myeloproliferative neoplasms overproduce blood cells that clot readily, so marrow output itself becomes a cause of thrombosis."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows the clot that won't quit: in factor V Leiden, the mutated factor resists shutdown by activated protein C, so thrombin keeps firing and weaves an extra-dense, stable fibrin mesh that resists dissolving."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Thrombophilia can reach arteries through a back door: a venous clot can cross a patent foramen ovale in the heart and shoot to the brain as a paradoxical embolism, an unexpected cause of stroke in the young."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Old clots leave lasting scar: when a deep vein thrombosis only partly clears, the vein wall fibroses into post-thrombotic syndrome, and unresolved lung clots organize into the fibrotic obstruction of chronic thromboembolic pulmonary hypertension."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Protein C deficiency writes itself on the skin: starting warfarin can trigger paradoxical skin necrosis as protein C falls fastest, and homozygous deficiency causes neonatal purpura fulminans, dark patches of skin infarction in the newborn."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Thrombophilia can clot the eye's veins: retinal vein occlusion, especially in the young, prompts a search for an inherited hypercoagulable state, the clot in the retina blurring or dimming vision suddenly."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Clots in the brain's drainage threaten neurons: inherited thrombophilia is a leading cause of cerebral venous sinus thrombosis, where backed-up pressure and infarction injure neurons, causing headache, seizures, and focal deficits."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "The workup must separate genes from antibodies: inherited thrombophilia is gene-driven, so its diagnosis hinges on ruling out the acquired antiphospholipid antibody syndrome, whose autoantibodies cause an indistinguishable clotting tendency by a different mechanism."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "It surfaces most often in women's reproductive lives: thrombophilia drives recurrent miscarriage and placental clots, and the estrogen of the pill or pregnancy multiplies the clot risk, making it a key consideration in contraception and obstetric care."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "It can clot the gut's circulation: inherited hypercoagulability is a leading cause of mesenteric vein thrombosis, choking the bowel's drainage into ischemia with severe abdominal pain out of proportion to the exam."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Clotting and complement amplify each other: thrombin cleaves C5 and terminal complement spurs tissue-factor and platelet activation, so inherited hypercoagulability shares a thrombo-inflammatory loop with complement-driven thrombosis like PNH and aHUS."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages drive a clot's fate: they invade an organizing thrombus, express tissue factor that seeds clotting, and orchestrate the remodeling that either resolves a deep vein thrombosis or scars the vein into post-thrombotic syndrome."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "The kidney can manufacture an acquired thrombophilia: nephrotic syndrome leaks antithrombin into the urine while raising clotting factors, and layered on an inherited defect it sharply raises the risk of renal vein thrombosis and VTE."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "Cancer is the great acquired thrombophilia: tumors — pancreatic cancer especially — pour out tissue factor and mucins that ignite clotting, the migratory Trousseau thrombophlebitis whose unexplained appearance can be the first clue to an occult malignancy."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Severe infection flips on clotting: COVID-19 drives an intense acquired prothrombotic state through endothelial injury and inflammation, multiplying thrombosis risk in patients who may also carry an inherited predisposition."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Overwhelming infection consumes the clotting system: sepsis-induced coagulopathy activates clotting bodywide toward microthrombi and DIC, an acquired hypercoagulable state that an underlying inherited thrombophilia can worsen."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Inflammation turns the vessel wall procoagulant: NF-κB activation induces tissue factor and suppresses anticoagulant pathways on the endothelium, the thromboinflammatory link by which inflammation amplifies an inherited clotting tendency into overt thrombosis."
  - target: 01-human/07-system/hcc
    relation: connects-to
    note: "It can clot the liver's own outflow: thrombophilia is a leading cause of Budd-Chiari syndrome, hepatic vein thrombosis that congests the liver into cirrhosis and, over years, can give rise to hepatocellular carcinoma."
  - target: 01-human/07-system/essential-thrombocythemia
    relation: connects-to
    note: "An acquired cousin works through platelets: JAK2-mutant essential thrombocythemia raises clot risk via overproduced, hyperreactive platelets — an acquired thrombophilia distinct from the clotting-factor defects of the inherited forms that can compound them when both coexist."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "It threatens the failing heart's chambers and veins: low-flow stasis in heart failure plus an inherited clotting tendency raises the risk of intracardiac thrombus and venous thromboembolism, complicating an already congested circulation."
  - target: 01-human/07-system/ovarian-cancer
    relation: connects-to
    note: "An unprovoked clot can unmask hidden cancer: ovarian and other adenocarcinomas are themselves prothrombotic, and a venous thrombosis in someone with inherited thrombophilia can be the event that prompts the workup uncovering an occult tumor."
  - target: 01-human/07-system/gastric-cancer
    relation: connects-to
    note: "It compounds Trousseau's syndrome: gastric adenocarcinoma classically causes migratory thrombophlebitis through tumor procoagulants, and a coexisting inherited thrombophilia magnifies the already high cancer-associated clotting risk."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Recurrent leg clots leave chronic ulcers: deep vein thromboses in thrombophilia damage venous valves, and the resulting post-thrombotic syndrome and chronic venous insufficiency produce slow-healing venous leg ulcers."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Long anticoagulation can cost bone: the prolonged heparin used in thrombophilic pregnancies and during recurrent clotting lowers bone density, a recognized cause of treatment-related osteoporosis."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Lifelong clot risk and anticoagulation weigh on mood: recurrent thrombotic events, pregnancy loss and the burden of indefinite blood thinners contribute to depression in inherited thrombophilia."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It clots the veins draining the gut and liver: inherited thrombophilia is a leading cause of splanchnic, portal and mesenteric vein thrombosis and Budd-Chiari syndrome, threatening the bowel and liver."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It can clot the brain's veins: thrombophilia predisposes to cerebral venous sinus thrombosis, a stroke-like event causing headache, seizures and raised intracranial pressure, often in young patients."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Lifelong clot risk and pregnancy worry breed anxiety: the threat of recurrent thrombosis, fear of pregnancy loss and the demands of indefinite anticoagulation foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Its clots travel to the lungs: pulmonary embolism from a deep-vein thrombosis is the most life-threatening consequence of inherited thrombophilia, causing breathlessness, chest pain and sudden death."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Severe deficiency strikes the skin: profound protein C or S deficiency causes neonatal purpura fulminans, and starting warfarin can trigger warfarin-induced skin necrosis from transient protein C drop."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It can clot the renal veins: inherited thrombophilia predisposes to renal vein thrombosis, a risk compounded when nephrotic syndrome adds acquired antithrombin loss in the urine."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "A venous clot can cross to the arteries: through a patent foramen ovale a clot can paradoxically embolise to cause arterial stroke or limb ischaemia, and large pulmonary emboli strain the right heart."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Oestrogen multiplies its danger: combined contraceptives, HRT and pregnancy sharply raise thrombosis risk in carriers, the key hormonal interaction guiding contraceptive and obstetric decisions."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Chronic deep clots overwhelm lymph drainage: recurrent and post-thrombotic deep-vein obstruction outpaces lymphatic clearance, contributing to persistent limb swelling."
  - target: 03-medicine/01-modern/09-hematology/warfarin
    relation: connects-to
    note: "Lifelong anticoagulation may be needed: those with recurrent venous thromboembolism from inherited thrombophilia often require long-term warfarin or a direct oral anticoagulant."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Inflammation and clotting intertwine: 'immunothrombosis' links infection and inflammation to the coagulation cascade, compounding the baseline risk of inherited thrombophilia."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Surgery and immobility tip it over: major orthopaedic surgery, fractures and prolonged immobilisation are powerful thrombosis triggers that compound inherited thrombophilia, demanding prophylaxis."
  - target: 03-medicine/01-modern/04-cardio/aspirin
    relation: connects-to
    note: "Antiplatelet cover in select cases: low-dose aspirin (often with heparin) is used in thrombophilia complicated by recurrent pregnancy loss or arterial events, and for extended venous-thromboembolism prophylaxis after initial anticoagulation."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "The liver makes the anticoagulants: protein C, protein S and antithrombin — the very factors deficient in inherited thrombophilia — are synthesised in the hepatic lobule, where warfarin also acts, so liver disease confounds thrombophilia testing."
  - target: 03-medicine/01-modern/04-cardio/statins
    relation: connects-to
    note: "They modestly lower clot risk: beyond cholesterol, statins reduce venous-thromboembolism incidence (as shown in JUPITER) through anti-inflammatory and endothelial effects, a useful adjunct in some thrombophilic patients."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Its clots reach the lungs: inherited thrombophilias predispose to deep vein thrombosis that embolises to the pulmonary vasculature, lodging clots in the alveolar capillary bed as pulmonary embolism."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "The kidney both causes and suffers clotting: nephrotic syndrome loses antithrombin in the urine to create an acquired thrombophilia and renal-vein thrombosis, while inherited thrombophilia adds to that glomerular-disease clotting risk."
  - target: 01-human/07-system/ahus
    relation: connects-to
    note: "Two genetic prothrombotic disorders: inherited thrombophilia thromboses through coagulation-factor defects, while atypical haemolytic uraemic syndrome causes microvascular thrombosis through uncontrolled complement—different cascades, shared clotting."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "Mostly venous, sometimes arterial: inherited thrombophilias clot chiefly in veins, but a venous clot crossing a patent foramen ovale can reach the arterial wall and brain, causing paradoxical embolic stroke."
  - target: 01-human/07-system/inflammatory-bowel-disease
    relation: connects-to
    note: "Inflammation amplifies clotting: inflammatory bowel disease is itself strongly prothrombotic, so an inherited thrombophilia on top sharply raises the venous-thrombosis risk during active flares."
  - target: 01-human/07-system/glioblastoma
    relation: connects-to
    note: "Brain tumours and clots: glioblastoma carries one of the highest cancer-associated venous-thrombosis rates, and a background inherited thrombophilia further raises the peri-operative and treatment clot risk."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Arterial events too: while inherited thrombophilias mainly cause venous clots, several contribute to arterial thrombosis and myocardial infarction in young patients, especially combined with smoking or oestrogen exposure."
  - target: 01-human/07-system/thalassemia
    relation: connects-to
    note: "A hypercoagulable haemoglobinopathy: thalassaemia, especially the non-transfusion-dependent intermedia form and after splenectomy, carries a high thrombotic risk that stacks with any inherited thrombophilia."
  - target: 01-human/07-system/myelofibrosis
    relation: connects-to
    note: "Acquired on inherited risk: JAK2-mutant myelofibrosis is a powerful acquired prothrombotic state causing splanchnic-vein thrombosis, often unmasked or worsened when an inherited thrombophilia coexists."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Inflammation-coagulation crosstalk: IL-6 induces fibrinogen and tissue factor, so inflammatory states compound an inherited thrombophilia to tip the balance toward clotting."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Immunothrombosis: NLRP3-inflammasome activation links inflammation to clotting through tissue-factor expression and neutrophil traps, amplifying the risk in inherited thrombophilia."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Endothelial dysfunction: endothelin-1-driven endothelial activation and vasoconstriction add a vascular-wall contribution to the thrombotic tendency of inherited thrombophilia."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Lost antithrombotic tone: endothelial nitric oxide normally inhibits platelet aggregation and adhesion, so reduced NO bioavailability removes a key brake and compounds the prothrombotic state of inherited thrombophilia."
  - target: 01-human/03-molecular/pf4
    relation: connects-to
    note: "Platelet activation: platelet factor 4 released from activated platelets neutralises heparin-like glycosaminoglycans on the endothelium, locally favouring coagulation atop the inherited procoagulant defect."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "Thrombus scaffold: plasma fibronectin is cross-linked into the fibrin meshwork of forming clots, stabilising the thrombi that arise more readily in inherited thrombophilia."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Stasis to thrombosis: hypoxia in the low-flow valve pockets of veins stabilises endothelial HIF-1α, which upregulates procoagulant factors — the molecular link between Virchow's stasis and the venous thrombi that inherited thrombophilia accelerates."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Monocyte tissue factor: CCL2 recruits monocytes to the forming venous thrombus, where their tissue-factor expression amplifies thrombin generation, tying inflammation to the clot propagation that compounds an inherited procoagulant state."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Eicosanoid balance: the platelet thromboxane A2/endothelial prostacyclin balance governs platelet aggregation, and a shift toward thromboxane favours the clot propagation that worsens thrombotic risk in inherited thrombophilia."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "NET immunothrombosis: neutrophils releasing S100A8/A9 and extracellular traps (NETs) provide a scaffold that ignites and amplifies venous thrombosis, an innate-immune amplifier that interacts with the inherited clotting-factor defects to precipitate clots."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Innate-immune thrombosis: TLR4 sensing of DAMPs on endothelium and monocytes promotes tissue-factor expression and the immunothrombosis that, layered on a genetic hypercoagulable state, helps tip thrombophilic patients into clinical thrombosis."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement-coagulation crosstalk: complement activation generating C3 and its fragments amplifies coagulation and platelet activation, an inflammatory contributor that compounds the inherited clotting tendency and links thrombosis to immune activation."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Endothelial activation: Angiopoietin-2/Tie2 signalling shifts the endothelium toward a procoagulant, permeable phenotype that, on inflammatory triggers, compounds the baseline hypercoagulability of inherited thrombophilia."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Thromboinflammation: IL-1β induces endothelial and monocyte tissue factor and downregulates anticoagulant pathways, the cytokine arm (with the IL-6 already mapped) that converts inflammation into the thrombosis triggered in thrombophilic patients."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Procoagulant endothelium: TNF-α induces endothelial tissue factor and suppresses thrombomodulin and the protein-C pathway, tipping the haemostatic balance toward clotting that precipitates events in inherited thrombophilia."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "Thromboinflammation: complement C5a acting through C5aR1 (C3 and C5 mapped) induces tissue factor and activates platelets, amplifying the thrombotic tendency that becomes clinically manifest in inherited thrombophilia."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Platelet amplifier: serotonin released from platelet dense granules promotes further platelet aggregation and vasoconstriction, propagating the thrombus growth that underlies events in thrombophilic patients."
  - target: 01-human/03-molecular/thrombopoietin
    relation: connects-to
    note: "Platelet supply: thrombopoietin sets the circulating platelet mass available for thrombus formation, a quantitative contributor to thrombotic risk in inherited thrombophilia."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Endothelial PI3K-AKT signalling sustains eNOS-derived nitric oxide and the protein-C anticoagulant axis (NO and protein C mapped); its impairment shifts the endothelium toward the prothrombotic state that compounds inherited thrombophilia."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Thrombin acting through PAR receptors engages ERK-MAPK in platelets and endothelium (thrombin mapped), amplifying the prothrombotic activation state in inherited thrombophilia."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "VEGF-driven endothelial activation and permeability contributes to the prothrombotic endothelial phenotype, complementing the angiopoietin-Tie axis already mapped."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 promotes the neutrophil-extracellular-trap-driven thromboinflammation that amplifies the venous thrombotic risk of inherited thrombophilia."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "DNA within neutrophil extracellular traps engages cGAS-STING, linking NET-driven sterile inflammation to the prothrombotic state of inherited thrombophilia."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K-AKT signalling (AKT already mapped) in platelets and endothelium supports the activated, procoagulant phenotype that drives thrombosis in inherited thrombophilia."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK1/2-STAT cytokine signaling (IL-6 already mapped) links inflammatory tone to the endothelial procoagulant phenotype that potentiates venous thrombosis in inherited thrombophilia."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signaling modulates the endothelial activation that contributes to thrombotic risk in inherited thrombophilia."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO downstream of PI3K-AKT signaling (AKT and PIK3CA already mapped) regulates the endothelial quiescence-versus-activation balance relevant to inherited thrombophilia."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the platelet-activation and endothelial signaling that shape the prothrombotic tendency of inherited thrombophilia."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signaling (IL-6 already mapped) links the inflammatory state to the hypercoagulability of inherited thrombophilia."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTOR signaling in platelets and endothelium participates in the prothrombotic vascular phenotype of inherited thrombophilia."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of platelet and endothelial receptors participates in the platelet activation and thrombus formation of inherited thrombophilia."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked endothelial metabolic signaling modulates the vascular homeostasis relevant to the thrombotic tendency of inherited thrombophilia."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven monocyte recruitment contributes to the inflammation-linked thrombosis of inherited thrombophilia."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the endothelial and platelet homeostasis relevant to the hypercoagulable state of inherited thrombophilia."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic modulation of the coagulation and endothelial gene expression relevant to inherited thrombophilia."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the endothelial and leukocyte interactions of the thrombo-inflammation of inherited thrombophilia."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the endothelial activation and thromboinflammation relevant to inherited thrombophilia."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the thromboinflammatory processes relevant to inherited thrombophilia."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine signaling provides platelet-inhibitory and vascular modulation relevant to inherited thrombophilia."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Androgen risk: exogenous testosterone therapy raises venous thromboembolism risk partly by inducing erythrocytosis, a modifiable exposure that compounds the baseline hypercoagulability of an inherited thrombophilia."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Hyperviscosity: a raised haemoglobin and haematocrit increase blood viscosity and thrombosis risk, so polycythaemia, whether from JAK2-driven disease or other causes, acts synergistically with an inherited thrombophilia to precipitate clots."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Obesity multiplier: obesity is a strong independent risk factor for venous thrombosis, and the adipokine leptin promotes platelet activation and a prothrombotic state that multiplies the risk conferred by an inherited thrombophilia."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Pregnancy risk: pregnancy is a hypercoagulable state driven by progesterone and estrogen (already mapped), and an inherited thrombophilia sharply raises the risk of pregnancy-associated venous thromboembolism and placental thrombotic complications."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Pulmonary embolism strain: a large pulmonary embolism from an inherited thrombophilia strains the right ventricle, and troponin elevation marks the myocardial injury that identifies high-risk PE needing more aggressive treatment."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Metabolic hypercoagulability: insulin resistance and the metabolic syndrome raise PAI-1 and fibrinogen (already mapped) to create an acquired prothrombotic state that compounds the risk of an inherited thrombophilia."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative thrombogenesis: reactive oxygen species, to which xanthine oxidase contributes, promote the endothelial dysfunction and platelet activation (already mapped) that tip the balance toward thrombosis in an inherited thrombophilia."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Thrombo-inflammation balance: coagulation and inflammation are intertwined, and the anti-inflammatory IL-10 opposes the pro-inflammatory signals (IL-6, TNF and IL-1 already mapped) that amplify thrombus formation in inherited thrombophilia."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "Metabolic-thrombotic axis: the insulin resistance (already mapped) that adds an acquired prothrombotic risk disturbs the incretin GLP-1 axis, part of the metabolic-syndrome hypercoagulability compounding an inherited thrombophilia."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Thrombo-inflammation balance: IL-4 and the M2 anti-inflammatory arm (IL-10 already mapped) counter the pro-inflammatory signals (IL-6, TNF and IL-1 already mapped) of the thrombo-inflammation that amplifies clot formation in inherited thrombophilia."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Metabolic prothrombotic risk: dyslipidaemia and the metabolic syndrome (insulin and leptin already mapped) add an acquired hypercoagulable state, and the raised cholesterol contributes to the arterial as well as venous thrombotic risk in inherited thrombophilia."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Platelet zinc and contact activation: zinc released from activated platelets (already mapped) promotes the contact pathway and fibrin formation (fibrinogen and thrombin already mapped), adding to the thrombotic tendency of inherited thrombophilia."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Antiphospholipid antibodies: the IgG antiphospholipid antibodies (anti-cardiolipin, anti-β2-glycoprotein-I) of the antiphospholipid syndrome are the major acquired thrombophilia that mimics and compounds the inherited forms."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Autoimmune prothrombotic state: the type-I interferon of the autoimmune diseases (lupus, antiphospholipid syndrome) promotes the prothrombotic endothelial (already mapped) state, the acquired thrombophilia that adds to the inherited risk."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic hypercoagulability: the fall in adiponectin, with leptin (already mapped), of the metabolic syndrome (cholesterol and insulin already mapped) adds an acquired hypercoagulable state to the inherited thrombophilia."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Metabolic hypercoagulability: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the metabolic hypercoagulable state that adds an acquired thrombotic risk to the inherited thrombophilia."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Pulmonary embolism: the deep-vein thrombi of the inherited thrombophilias embolise to the lung, the pulmonary embolism the life-threatening complication."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Coagulation-factor synthesis: the liver synthesises the clotting factors and the natural anticoagulants (protein C, antithrombin already mapped) whose inherited deficiency causes thrombophilia."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Immunothrombosis: the NK cells (perforin already mapped) are part of the innate immune contribution to the immunothrombosis that amplifies the thrombotic tendency of the inherited thrombophilias."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 immunothrombosis: the IFN-γ of the T cells is the type-II interferon arm (with the type-I interferon already mapped) of the inflammatory dimension that potentiates the thrombosis of thrombophilia."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immunothrombotic inflammation accompanying the inherited thrombophilias."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 cytokine: IL-13, with IL-4 (already mapped), is part of the type-2 immune dimension of the inflammatory milieu that modulates the immunothrombosis of the inherited thrombophilias."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the inflammatory milieu accompanying the inherited thrombophilias."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immunothrombotic inflammation of the inherited thrombophilias."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the inflammatory milieu accompanying the inherited thrombophilias."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the immunothrombotic inflammation accompanying the inherited thrombophilias."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) at the interface of the complement and coagulation systems relevant to the immunothrombosis of the inherited thrombophilias."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement/coagulation crosstalk: the C1-esterase inhibitor regulates both the complement (C3, C5, C5aR1 and factor H already mapped) and the contact-coagulation systems at the interface of immunothrombosis relevant to the inherited thrombophilias."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Thromboinflammation: osteopontin, released by the activated platelets (already mapped), is a matricellular mediator that links the inflammation to the thrombosis of the inherited thrombophilias."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Iron/thrombosis: transferrin, the iron carrier, reflects the disordered iron handling that, with the dysregulated haemostasis, is part of the thrombotic-risk context of the inherited thrombophilias."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Endothelial alarmin: TSLP, released from endothelial cells (already mapped) and mast cells (already mapped) at sites of vascular wall stress, amplifies the thromboinflammatory milieu that converts the prothrombotic genotype into the overt thrombosis of inherited thrombophilia."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Contact-kinin thrombosis amplifier: bradykinin, generated by the contact activation (kallikrein-kinin) pathway co-activated with the coagulation cascade, amplifies the endothelial permeability and the prothrombotic milieu of inherited thrombophilia."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Erythrocyte rheology: erythropoietin, driving the erythropoiesis (erythrocyte already mapped), modulates haematocrit and blood viscosity — factors that interact with the prothrombotic genotypes of inherited thrombophilia to determine clinical thrombotic risk."
---

# Inherited Thrombophilia

## Overview

**Inherited thrombophilias** are genetic conditions that increase susceptibility to venous thromboembolism (VTE) — primarily deep vein thrombosis (DVT) and pulmonary embolism (PE) — due to constitutional imbalances in the coagulation system. The discovery of **Factor V Leiden** in 1994 [^bertina-1994-factor-v-leiden] established the molecular basis for the most common inherited thrombophilia and transformed understanding of thrombosis genetics.

Inherited thrombophilias collectively account for an identifiable cause in ~30-50% of patients with unprovoked VTE, and identifying them influences counseling, duration of anticoagulation, and screening of family members. However, **many individuals with thrombophilia never develop VTE** — additional risk factors (surgery, immobility, pregnancy, hormonal therapy, malignancy) are usually required to trigger the first event. Conversely, most VTE events occur in people without identified thrombophilia.

**Population prevalence and VTE risk:**

| Condition | Mechanism | Prevalence | Heterozygous VTE risk | Notes |
|:----------|:----------|:-----------|:---------------------|:------|
| **Factor V Leiden (FVL)** | F5 R506Q → APC resistance | ~5% Caucasians; 1-2% African, <1% Asian | 4-8× | Most common; predominantly venous (not arterial) |
| **Prothrombin G20210A** | F2 3'-UTR → ↑prothrombin levels | ~2-3% Caucasians | 2-3× | Second most common; associated with cerebral vein thrombosis |
| **Protein C deficiency** | PROC loss-of-function | ~0.3% | 5-10× | Warfarin-induced skin necrosis risk; neonatal purpura fulminans (homozygous) |
| **Protein S deficiency** | PROS1 mutations | ~0.1% | 5-10× | Type I (antigen + activity low), II (activity low), III (free PS low) |
| **Antithrombin deficiency** | SERPINC1 mutations | ~0.05% | 10-20× | Most severe; heparin requires AT → heparin resistance |
| **Homozygous FVL** | Both alleles R506Q | ~0.02% | 50-80× | High-risk; often warrants indefinite anticoagulation |
| **Compound heterozygous** | FVL + PT G20210A | ~0.01% | 10-20× | High-risk; very high with additional triggers |

**What is NOT a high-yield inherited thrombophilia (no longer routinely tested):**
- **MTHFR C677T/A1298C:** Mild hyperhomocysteinemia; NOT an independent VTE risk factor; not recommended for testing (ACCP, ASH guidelines)
- **PAI-1 4G/5G polymorphism:** Population data weak; not tested routinely

## Structure

### Molecular mechanisms of inherited thrombophilias

**1. Factor V Leiden — APC resistance**

Factor V (F5) has three main functional roles:
- **Pro-coagulant:** As FVa (activated by thrombin or FXa), acts as co-factor for FXa in the prothrombinase complex → 300,000× acceleration of thrombin generation
- **Anticoagulant:** Intact FV (non-activated) acts as APC co-factor for FVIIIa cleavage → amplifies APC anticoagulant function
- **APC cleavage sites in FVa:** Arg506 (primary, rapid; abolishes most prothrombinase activity), Arg306 (secondary, slow; requires protein S), Arg679 (minor)

**FVL R506Q effect:**
- Prevents APC cleavage at Arg506 → FVa 10-20× more stable → prolonged prothrombinase → sustained thrombin
- Also impairs FV anticoagulant function → reduces APC-mediated FVIIIa inactivation
- Result: doubly impaired anticoagulation → hypercoagulability

**2. Prothrombin G20210A — elevated prothrombin**

The G20210A mutation is in the **3'-untranslated region (3'-UTR)** of the prothrombin (F2) gene, specifically at the polyadenylation cleavage site:
- G→A transition → increased mRNA stability/efficiency → 20-30% higher plasma prothrombin (factor II) levels
- More prothrombin → more thrombin potential → greater thrombin burst when coagulation is triggered
- Less dramatic APC resistance effect than FVL; primarily quantitative hypercoagulability

**3. Protein C deficiency (PROC)**

See [Protein C molecular entry](../../03-molecular/protein-c/README.md) for full detail.
- Type I (80%): Low antigen + low activity (quantitative deficiency)
- Type II (20%): Normal antigen + low activity (dysfunctional protein)
- APC cannot shut down FVa/FVIIIa → thrombin generation unchecked

**4. Protein S deficiency (PROS1)**

Protein S has three clinical subtypes:
- Type I: Low total antigen, low free antigen, low activity (quantitative loss)
- Type II: Normal antigen (total + free), low activity (qualitative)
- Type III: Normal total antigen, low **free** protein S (increased binding to C4BP); most common type
- Free protein S is the active APC co-factor; bound (to C4BP) is inactive
- Normal in pregnancy: C4BP rises → free PS falls → physiological acquired thrombophilia

**5. Antithrombin deficiency (SERPINC1)**

Antithrombin (ATIII) is the primary plasma inhibitor of thrombin, FXa, FIXa, and FXIa:
- Type I (quantitative): Low antigen + low activity; more severe
- Type II (qualitative): Normal antigen, low activity; specific subtypes affecting heparin binding site (HBS) vs. reactive site (RS)
- **AT deficiency + heparin resistance:** Heparin works by accelerating AT-mediated thrombin inactivation (~1000-fold); if AT is severely depleted → heparin is less effective → clinical heparin resistance → may need AT concentrate first
- Most severe inherited thrombophilia: unprovoked DVT often at young age, frequent recurrence; typically warrants indefinite anticoagulation

## Function

### Clinical presentation of inherited thrombophilia

**When to suspect inherited thrombophilia:**
- **Unprovoked** VTE (DVT/PE without surgery, immobility, trauma, cancer, pregnancy)
- VTE at young age (<45-50 years)
- **Recurrent** VTE (2+ events)
- **Unusual site** thrombosis: cerebral vein thrombosis, portal vein thrombosis, splenic vein, Budd-Chiari syndrome — especially in young patients or those not receiving estrogen
- VTE during pregnancy or oral contraceptive use
- Strong **family history** of VTE (1st-degree relative with unprovoked VTE)
- **Warfarin-induced skin necrosis** → screen for protein C or S deficiency

**Risk amplification — multiplicative effects:**

| Combination | Approximate VTE risk (vs. baseline ~1/1000/year) |
|:-----------|:--------------------------------------------------|
| OCP use alone | 4× |
| FVL heterozygous alone | 7× |
| FVL + OCP | **35×** (multiplicative, not additive) |
| AT deficiency alone | 10-20× |
| Pregnancy alone | 4-5× |
| AT deficiency + pregnancy | 70-100× |
| Triple-positive APS | 100-200× |

### When NOT to test

- **During acute VTE event:** Coagulation factors are consumed/altered → falsely low protein C, S, AT; FVL and prothrombin G20210A genotype testing are unaffected (DNA-based)
- **While on anticoagulation:** Warfarin reduces protein C and S (vitamin K-dependent) → falsely low; heparin/LMWH may slightly affect AT; DOACs variably affect functional assays; wait 4-6 weeks after stopping warfarin, 24h after stopping DOACs
- **During pregnancy:** Protein S falls physiologically; test postpartum
- **Active infection/inflammation:** C4BP rises → free protein S falls (type III-like picture); AT may fall as acute-phase reactant

## Pathology

### Thrombophilia testing — what to order

**Standard thrombophilia workup:**
1. **FV Leiden genotype** (PCR, G1691A) — unaffected by anticoagulation
2. **Prothrombin G20210A genotype** (PCR) — unaffected by anticoagulation
3. **Protein C activity** (functional assay) — wait until off anticoagulation
4. **Protein S activity** (functional; free PS antigen) — wait; unreliable in pregnancy/OCP/warfarin
5. **Antithrombin activity** (functional) — wait; heparin may slightly lower AT
6. **Antiphospholipid antibodies** (lupus anticoagulant, anticardiolipin IgG/IgM, anti-β2GPI IgG/IgM) — always test; APS is most clinically actionable acquired thrombophilia

**NOT routinely recommended:**
- MTHFR genotype (not an independent VTE risk factor)
- Factor VIII levels (acute phase reactant; elevated transiently)
- Homocysteine levels (not proven to benefit from treatment)

### Treatment and duration of anticoagulation [^kearon-2016-antithrombotic-therapy]

**First event, provoked VTE (surgery, trauma, major transient risk):**
- 3 months anticoagulation — same as for patients without thrombophilia
- Thrombophilia testing rarely changes management here

**First event, unprovoked VTE + low-risk thrombophilia (FVL heterozygous, PT G20210A):**
- At least 3-6 months; extended (indefinite) therapy is debated — shared decision-making based on bleeding risk vs. benefit
- Men have higher recurrence risk after stopping anticoagulation than women — weight in decisions

**First event, unprovoked VTE + high-risk thrombophilia:**
- **AT deficiency:** Indefinite anticoagulation after first unprovoked VTE
- **Protein C or S deficiency:** Indefinite generally recommended after first unprovoked VTE
- **Homozygous FVL or compound heterozygous:** Indefinite anticoagulation after first unprovoked VTE

**Arterial thrombosis (stroke, MI) + thrombophilia:**
- Isolated inherited thrombophilias (FVL, PT G20210A) are **NOT** established risk factors for arterial thrombosis — anticoagulation not indicated for arterial events unless APS is concurrent
- APS (acquired) → warfarin for stroke; rivaroxaban/apixaban have higher recurrence rates in APS (TRAPS trial)

**Pregnancy management:**
- FVL or PT G20210A heterozygous + prior VTE: Prophylactic LMWH throughout pregnancy + postpartum 6 weeks
- AT deficiency + prior VTE: Therapeutic-dose LMWH throughout pregnancy; AT concentrate for delivery
- No prior VTE, but high-risk thrombophilia: Individualize risk — some use postpartum LMWH; avoid estrogen-containing OCP postpartum

**OCP/HRT counseling:**
- FVL heterozygous + OCP: ~35× VTE risk → avoid estrogen-containing OCP; use progestin-only, IUD, barrier methods
- AT deficiency: Avoid estrogen-containing OCP; progestin-only acceptable
- Screening relatives for thrombophilia before starting OCP: Not universally recommended (cost-effectiveness debated); consider for high-risk families

### Drug considerations

| Thrombophilia | Special drug consideration |
|:-------------|:--------------------------|
| AT deficiency | Heparin resistance (needs more heparin or AT concentrate); DOACs preferred for long-term |
| Protein C/S deficiency | Warfarin-induced skin necrosis risk — always bridge with parenteral anticoagulation when starting warfarin; DOACs do not cause skin necrosis |
| FVL + OCP | OCP is major modifiable risk factor — strongly counsel to switch contraception |
| APS | Warfarin superior to DOACs for arterial APS (rivaroxaban inferior in TRAPS trial); target INR 2.0-3.0 for venous APS; some centers use INR 3.0-4.0 for triple-positive APS |

## Connections

- `connects-to` → **[Protein C](../../03-molecular/protein-c/README.md)** — Protein C deficiency (0.3% prevalence; 5-10× VTE risk) impairs APC-mediated FVa/FVIIIa inactivation → thrombosis; warfarin-induced skin necrosis risk on protein C–deficient patients.
- `connects-to` → **[Thrombin](../../03-molecular/thrombin/README.md)** — Factor V Leiden (R506Q) causes APC resistance: thrombin-activated FVa at Arg506 cannot be cleaved → uncontrolled prothrombinase complex → excess thrombin; thrombomodulin-bound thrombin activates protein C → the central anticoagulant checkpoint that FVL undermines.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — VTE (DVT/PE) is the primary manifestation of inherited thrombophilia; risk is multiplicative (FVL + OCP = 35× VTE risk); thrombophilia guides anticoagulation duration (indefinite for AT deficiency, homozygous FVL, compound heterozygous); do not test during acute VTE.
- `connects-to` → **[Antiphospholipid Syndrome](../antiphospholipid-syndrome/README.md)** — APS is the most important acquired thrombophilia, causing indistinguishable VTE and arterial thrombosis to inherited thrombophilia; combined APS + inherited thrombophilia (e.g., FVL + triple-positive aPL) confers extreme thrombotic risk; APS is excluded by thrombophilia workup.
- `connects-to` → **[Antithrombin](../../03-molecular/antithrombin/README.md)** — Antithrombin deficiency (0.02-0.04% prevalence; 25-50× VTE risk) is the highest-risk inherited thrombophilia; type IIa reactive-site mutations (Arg393His) most thrombogenic; UFH/LMWH require AT for efficacy; AT concentrate needed peri-surgery/delivery.
- `connects-to` → **[Hemophilia A](../hemophilia-a/README.md)** — Inherited thrombophilia is the mirror image of hemophilia — a clotting excess versus a bleeding deficiency; the contrast is mechanistic, since factor V Leiden makes FVa resist shutdown by activated protein C, whose downstream targets are missing or weak in hemophilia.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver synthesizes nearly all coagulation proteins, including the anticoagulants protein C, protein S, and antithrombin whose inherited deficiencies cause thrombophilia; hepatic failure causes a mixed coagulopathy, and warfarin blocks vitamin-K-dependent factor synthesis.
- `connects-to` → **[Stroke](../stroke/README.md)** — Inherited thrombophilias (factor V Leiden, prothrombin G20210A) cause venous, not arterial, thrombosis — so they are not established risk factors for ischemic stroke or MI and do not warrant anticoagulation for arterial events; antiphospholipid syndrome is the exception.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Healthy endothelium is antithrombotic, displaying thrombomodulin that activates protein C and heparan sulfate for antithrombin; inherited thrombophilias (factor V Leiden, protein C/S or antithrombin deficiency) cripple these endothelial-anchored brakes, tilting toward clotting.
- `connects-to` → **[Heparin-Induced Thrombocytopenia](../heparin-induced-thrombocytopenia/README.md)** — Both are prothrombotic but differ in origin: inherited thrombophilia is a germline anticoagulant defect, HIT an acquired antibody-mediated platelet activation; a thrombophilic patient who develops HIT faces compounded clot risk, and both demand non-heparin anticoagulation.
- `connects-to` → **[Paroxysmal Nocturnal Hemoglobinuria](../pnh/README.md)** — PNH is an acquired thrombophilia: loss of GPI-anchored complement regulators drives hemolysis and platelet activation → thrombosis in unusual sites (hepatic, cerebral); like inherited thrombophilias it presents with unexplained VTE, but its mechanism is complement, not factors.
- `connects-to` → **[Polycythemia Vera](../polycythemia-vera/README.md)** — Inherited thrombophilia and polycythemia vera are inherited versus acquired prothrombotic states: thrombophilia (factor V Leiden, prothrombin G20210A) tilts toward clotting, while PV's JAK2 thickens the blood—both raise venous thrombosis, including splanchnic clots.
- `connects-to` → **[Disseminated Intravascular Coagulation](../disseminated-intravascular-coagulation/README.md)** — Inherited thrombophilia and DIC are opposite ends of clotting dysregulation: thrombophilia is a stable inherited tilt toward thrombosis, while DIC is acute systemic coagulation activation consuming factors and platelets—paradoxically causing both clotting and bleeding.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Inherited thrombophilia mainly raises venous, not arterial, thrombosis—unlike atherosclerosis: factor V Leiden and prothrombin mutations drive DVT and PE, while atherosclerotic thrombosis is plaque-driven, so thrombophilia testing is reserved for venous events.
- `connects-to` → **[Myeloproliferative Neoplasms](../myeloproliferative-neoplasms/README.md)** — Myeloproliferative neoplasms are a major acquired thrombophilia: JAK2-mutant blood is intrinsically prothrombotic, causing arterial and venous (including splanchnic) clots like inherited thrombophilias—so unexplained thrombosis at unusual sites warrants JAK2 testing.
- `connects-to` → **[Pulmonary Arterial Hypertension](../pulmonary-arterial-hypertension/README.md)** — Inherited thrombophilia can cause pulmonary hypertension: recurrent pulmonary emboli that fail to resolve organize into fibrotic obstruction, causing chronic thromboembolic pulmonary hypertension (CTEPH)—a complication surgically curable by endarterectomy.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Platelets are central to the arterial thrombosis of thrombophilia: while inherited thrombophilias mainly drive venous clots, platelet activation drives arterial events—so antiplatelet and anticoagulant therapy target different arms of clot formation.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Estrogen multiplies the clot risk of inherited thrombophilia: oral contraceptives, hormone therapy and pregnancy raise clotting factors, so a factor V Leiden carrier faces sharply higher venous thrombosis risk on estrogen—central to contraceptive counseling.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Pulmonary embolism is the feared endpoint of inherited thrombophilia: deep vein clots break off and lodge in the lungs, so a young or recurrent unprovoked PE prompts thrombophilia testing—and the risk guides how long anticoagulation continues.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Inherited thrombophilia causes clots in unusual sites like the cerebral veins: prothrombotic mutations, especially with estrogen, predispose to cerebral venous sinus thrombosis—so an unexplained young stroke or sinus thrombosis warrants a thrombophilia workup.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — Inherited thrombophilia threatens the placenta: clots in the placental circulation are linked to recurrent miscarriage, pre-eclampsia, growth restriction, and stillbirth—so obstetric complications are a major reason thrombophilia is tested for in women.
- `connects-to` → **[Fibrinogen](../../03-molecular/fibrinogen/README.md)** — Fibrinogen ties to thrombophilia at both ends: rare inherited dysfibrinogenemia can make a clot-prone fibrin, and high fibrinogen levels are themselves prothrombotic—so the very protein that forms clots can be a hereditary or acquired thrombosis risk.
- `connects-to` → **[Sickle Cell Disease](../sickle-cell-disease/README.md)** — Sickle cell disease is a hypercoagulable state in its own right: chronic hemolysis, activated platelets, and endothelial damage tip blood toward clotting, so it compounds inherited thrombophilia and raises venous thromboembolism risk beyond its vaso-occlusive crises.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium is coagulation Factor IV, central to the clotting that thrombophilia tips toward excess: it bridges clotting-factor complexes to membranes, so it underlies the cascade—and citrate that chelates it keeps lab tubes and stored blood from clotting.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — The liver's hepatocytes make both sides of the clotting balance: they synthesize procoagulant factors and the natural anticoagulants protein C, protein S and antithrombin—so inherited deficiencies of these hepatocyte products cause thrombophilia.
- `connects-to` → **[Obesity](../obesity/README.md)** — Obesity compounds inherited thrombophilia: excess adipose tissue raises clotting factors and inflammation and impairs fibrinolysis, so it multiplies the venous-thrombosis risk of a Factor V Leiden or prothrombin variant—gene meets environment.
- `connects-to` → **[Von Willebrand Factor](../../03-molecular/von-willebrand-factor/README.md)** — High von Willebrand factor is itself a thrombophilia: elevated vWF—from genes, inflammation, or aging—makes platelets stickier and raises clot risk, adding to the inherited deficiencies of natural anticoagulants behind familial thrombosis.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Thrombophilia is amplified by neutrophil NETs: neutrophils cast out DNA webs (NETs) that scaffold platelets and clotting factors into clots, so this immunothrombosis turns inflammation into the venous thrombi that thrombophilia predisposes to.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Low oxygen and stasis tip thrombophilia into clots: immobility and hypoxia (long flights, illness) slow venous flow and switch on procoagulant signals, providing the trigger that turns an inherited clotting tendency into an actual thrombosis.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Thrombophilia can clot the kidney's veins: renal vein thrombosis is a classic unusual-site clot, abruptly causing flank pain, blood in the urine, and swelling as the kidney's venous drainage is blocked.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — Thrombophilia drives clots in the splanchnic veins: thrombosis of the splenic and portal veins draining the spleen and gut is a hallmark unusual-site event, causing splenomegaly and portal hypertension.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — Thrombophilia can infarct the adrenal glands: thrombosis of their veins triggers hemorrhagic adrenal infarction, which can precipitate life-threatening adrenal failure—a rare but lethal unusual-site complication.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Confirming thrombophilia's clots relies on imaging: CT angiography and lung scans read in X-ray photons locate the deep-vein thromboses and pulmonary emboli that prompt a hypercoagulable workup.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Red cells thicken thrombophilic blood: in polycythemia and sickle cell disease, excess or misshapen erythrocytes raise viscosity and slow flow, promoting the clotting these prothrombotic states are known for.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Some thrombophilias are born in the bone marrow: JAK2-driven myeloproliferative neoplasms overproduce blood cells that clot readily, so marrow output itself becomes a cause of thrombosis.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows the clot that won't quit: in factor V Leiden, the mutated factor resists shutdown by activated protein C, so thrombin keeps firing and weaves an extra-dense, stable fibrin mesh that resists dissolving.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Thrombophilia can reach arteries through a back door: a venous clot can cross a patent foramen ovale in the heart and shoot to the brain as a paradoxical embolism, an unexpected cause of stroke in the young.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Old clots leave lasting scar: when a deep vein thrombosis only partly clears, the vein wall fibroses into post-thrombotic syndrome, and unresolved lung clots organize into the fibrotic obstruction of chronic thromboembolic pulmonary hypertension.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Protein C deficiency writes itself on the skin: starting warfarin can trigger paradoxical skin necrosis as protein C falls fastest, and homozygous deficiency causes neonatal purpura fulminans, dark patches of skin infarction in the newborn.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Thrombophilia can clot the eye's veins: retinal vein occlusion, especially in the young, prompts a search for an inherited hypercoagulable state, the clot in the retina blurring or dimming vision suddenly.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Clots in the brain's drainage threaten neurons: inherited thrombophilia is a leading cause of cerebral venous sinus thrombosis, where backed-up pressure and infarction injure neurons, causing headache, seizures, and focal deficits.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — The workup must separate genes from antibodies: inherited thrombophilia is gene-driven, so its diagnosis hinges on ruling out the acquired antiphospholipid antibody syndrome, whose autoantibodies cause an indistinguishable clotting tendency by a different mechanism.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — It surfaces most often in women's reproductive lives: thrombophilia drives recurrent miscarriage and placental clots, and the estrogen of the pill or pregnancy multiplies the clot risk, making it a key consideration in contraception and obstetric care.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — It can clot the gut's circulation: inherited hypercoagulability is a leading cause of mesenteric vein thrombosis, choking the bowel's drainage into ischemia with severe abdominal pain out of proportion to the exam.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Clotting and complement amplify each other: thrombin cleaves C5 and terminal complement spurs tissue-factor and platelet activation, so inherited hypercoagulability shares a thrombo-inflammatory loop with complement-driven thrombosis like PNH and aHUS.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages drive a clot's fate: they invade an organizing thrombus, express tissue factor that seeds clotting, and orchestrate the remodeling that either resolves a deep vein thrombosis or scars the vein into post-thrombotic syndrome.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — The kidney can manufacture an acquired thrombophilia: nephrotic syndrome leaks antithrombin into the urine while raising clotting factors, and layered on an inherited defect it sharply raises the risk of renal vein thrombosis and VTE.
- `connects-to` → **[Pancreatic Cancer](../pancreatic-cancer/README.md)** — Cancer is the great acquired thrombophilia: tumors — pancreatic cancer especially — pour out tissue factor and mucins that ignite clotting, the migratory Trousseau thrombophlebitis whose unexplained appearance can be the first clue to an occult malignancy.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Severe infection flips on clotting: COVID-19 drives an intense acquired prothrombotic state through endothelial injury and inflammation, multiplying thrombosis risk in patients who may also carry an inherited predisposition.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Overwhelming infection consumes the clotting system: sepsis-induced coagulopathy activates clotting bodywide toward microthrombi and DIC, an acquired hypercoagulable state that an underlying inherited thrombophilia can worsen.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Inflammation turns the vessel wall procoagulant: NF-κB activation induces tissue factor and suppresses anticoagulant pathways on the endothelium, the thromboinflammatory link by which inflammation amplifies an inherited clotting tendency into overt thrombosis.
- `connects-to` → **[Hepatocellular Carcinoma](../hcc/README.md)** — It can clot the liver's own outflow: thrombophilia is a leading cause of Budd-Chiari syndrome, hepatic vein thrombosis that congests the liver into cirrhosis and, over years, can give rise to hepatocellular carcinoma.
- `connects-to` → **[Essential Thrombocythemia](../essential-thrombocythemia/README.md)** — An acquired cousin works through platelets: JAK2-mutant essential thrombocythemia raises clot risk via overproduced, hyperreactive platelets — an acquired thrombophilia distinct from the clotting-factor defects of the inherited forms that can compound them when both coexist.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — It threatens the failing heart's chambers and veins: low-flow stasis in heart failure plus an inherited clotting tendency raises the risk of intracardiac thrombus and venous thromboembolism, complicating an already congested circulation.
- `connects-to` → **[Ovarian Cancer](../ovarian-cancer/README.md)** — An unprovoked clot can unmask hidden cancer: ovarian and other adenocarcinomas are themselves prothrombotic, and a venous thrombosis in someone with inherited thrombophilia can be the event that prompts the workup uncovering an occult tumor.
- `connects-to` → **[Gastric Cancer](../gastric-cancer/README.md)** — It compounds Trousseau's syndrome: gastric adenocarcinoma classically causes migratory thrombophlebitis through tumor procoagulants, and a coexisting inherited thrombophilia magnifies the already high cancer-associated clotting risk.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Recurrent leg clots leave chronic ulcers: deep vein thromboses in thrombophilia damage venous valves, and the resulting post-thrombotic syndrome and chronic venous insufficiency produce slow-healing venous leg ulcers.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Long anticoagulation can cost bone: the prolonged heparin used in thrombophilic pregnancies and during recurrent clotting lowers bone density, a recognized cause of treatment-related osteoporosis.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Lifelong clot risk and anticoagulation weigh on mood: recurrent thrombotic events, pregnancy loss and the burden of indefinite blood thinners contribute to depression in inherited thrombophilia.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It clots the veins draining the gut and liver: inherited thrombophilia is a leading cause of splanchnic, portal and mesenteric vein thrombosis and Budd-Chiari syndrome, threatening the bowel and liver.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It can clot the brain's veins: thrombophilia predisposes to cerebral venous sinus thrombosis, a stroke-like event causing headache, seizures and raised intracranial pressure, often in young patients.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Lifelong clot risk and pregnancy worry breed anxiety: the threat of recurrent thrombosis, fear of pregnancy loss and the demands of indefinite anticoagulation foster chronic health anxiety alongside depression.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Its clots travel to the lungs: pulmonary embolism from a deep-vein thrombosis is the most life-threatening consequence of inherited thrombophilia, causing breathlessness, chest pain and sudden death.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Severe deficiency strikes the skin: profound protein C or S deficiency causes neonatal purpura fulminans, and starting warfarin can trigger warfarin-induced skin necrosis from transient protein C drop.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It can clot the renal veins: inherited thrombophilia predisposes to renal vein thrombosis, a risk compounded when nephrotic syndrome adds acquired antithrombin loss in the urine.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — A venous clot can cross to the arteries: through a patent foramen ovale a clot can paradoxically embolise to cause arterial stroke or limb ischaemia, and large pulmonary emboli strain the right heart.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Oestrogen multiplies its danger: combined contraceptives, HRT and pregnancy sharply raise thrombosis risk in carriers, the key hormonal interaction guiding contraceptive and obstetric decisions.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Chronic deep clots overwhelm lymph drainage: recurrent and post-thrombotic deep-vein obstruction outpaces lymphatic clearance, contributing to persistent limb swelling.
- `connects-to` → **[Warfarin](../../../03-medicine/01-modern/09-hematology/warfarin/README.md)** — Lifelong anticoagulation may be needed: those with recurrent venous thromboembolism from inherited thrombophilia often require long-term warfarin or a direct oral anticoagulant.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Inflammation and clotting intertwine: 'immunothrombosis' links infection and inflammation to the coagulation cascade, compounding the baseline risk of inherited thrombophilia.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Surgery and immobility tip it over: major orthopaedic surgery, fractures and prolonged immobilisation are powerful thrombosis triggers that compound inherited thrombophilia, demanding prophylaxis.
- `connects-to` → **[Aspirin](../../../03-medicine/01-modern/04-cardio/aspirin/README.md)** — Antiplatelet cover in select cases: low-dose aspirin (often with heparin) is used in thrombophilia complicated by recurrent pregnancy loss or arterial events, and for extended venous-thromboembolism prophylaxis after initial anticoagulation.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — The liver makes the anticoagulants: protein C, protein S and antithrombin — the very factors deficient in inherited thrombophilia — are synthesised in the hepatic lobule, where warfarin also acts, so liver disease confounds thrombophilia testing.
- `connects-to` → **[Statins](../../../03-medicine/01-modern/04-cardio/statins/README.md)** — They modestly lower clot risk: beyond cholesterol, statins reduce venous-thromboembolism incidence (as shown in JUPITER) through anti-inflammatory and endothelial effects, a useful adjunct in some thrombophilic patients.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Its clots reach the lungs: inherited thrombophilias predispose to deep vein thrombosis that embolises to the pulmonary vasculature, lodging clots in the alveolar capillary bed as pulmonary embolism.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — The kidney both causes and suffers clotting: nephrotic syndrome loses antithrombin in the urine to create an acquired thrombophilia and renal-vein thrombosis, while inherited thrombophilia adds to that glomerular-disease clotting risk.
- `connects-to` → **[aHUS](../ahus/README.md)** — Two genetic prothrombotic disorders: inherited thrombophilia thromboses through coagulation-factor defects, while atypical haemolytic uraemic syndrome causes microvascular thrombosis through uncontrolled complement—different cascades, shared clotting.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — Mostly venous, sometimes arterial: inherited thrombophilias clot chiefly in veins, but a venous clot crossing a patent foramen ovale can reach the arterial wall and brain, causing paradoxical embolic stroke.
- `connects-to` → **[Inflammatory Bowel Disease](../inflammatory-bowel-disease/README.md)** — Inflammation amplifies clotting: inflammatory bowel disease is itself strongly prothrombotic, so an inherited thrombophilia on top sharply raises the venous-thrombosis risk during active flares.
- `connects-to` → **[Glioblastoma](../glioblastoma/README.md)** — Brain tumours and clots: glioblastoma carries one of the highest cancer-associated venous-thrombosis rates, and a background inherited thrombophilia further raises the peri-operative and treatment clot risk.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Arterial events too: while inherited thrombophilias mainly cause venous clots, several contribute to arterial thrombosis and myocardial infarction in young patients, especially combined with smoking or oestrogen exposure.
- `connects-to` → **[Thalassemia](../thalassemia/README.md)** — A hypercoagulable haemoglobinopathy: thalassaemia, especially the non-transfusion-dependent intermedia form and after splenectomy, carries a high thrombotic risk that stacks with any inherited thrombophilia.
- `connects-to` → **[Myelofibrosis](../myelofibrosis/README.md)** — Acquired on inherited risk: JAK2-mutant myelofibrosis is a powerful acquired prothrombotic state causing splanchnic-vein thrombosis, often unmasked or worsened when an inherited thrombophilia coexists.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — Inflammation-coagulation crosstalk: IL-6 induces fibrinogen and tissue factor, so inflammatory states compound an inherited thrombophilia to tip the balance toward clotting.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Immunothrombosis: NLRP3-inflammasome activation links inflammation to clotting through tissue-factor expression and neutrophil traps, amplifying the risk in inherited thrombophilia.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Endothelial dysfunction: endothelin-1-driven endothelial activation and vasoconstriction add a vascular-wall contribution to the thrombotic tendency of inherited thrombophilia.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — Lost antithrombotic tone: endothelial nitric oxide normally inhibits platelet aggregation and adhesion, so reduced NO bioavailability removes a key brake and compounds the prothrombotic state of inherited thrombophilia.
- `connects-to` → **[PF4](../../03-molecular/pf4/README.md)** — Platelet activation: platelet factor 4 released from activated platelets neutralises heparin-like glycosaminoglycans on the endothelium, locally favouring coagulation atop the inherited procoagulant defect.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — Thrombus scaffold: plasma fibronectin is cross-linked into the fibrin meshwork of forming clots, stabilising the thrombi that arise more readily in inherited thrombophilia.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Hypoxia in the low-flow valve pockets of veins stabilizes endothelial HIF-1α, which upregulates procoagulant factors—the molecular link between Virchow's stasis and the venous thrombi that an inherited procoagulant defect accelerates.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — CCL2 recruits monocytes to the forming venous thrombus, where their tissue-factor expression amplifies thrombin generation, tying inflammation to the clot propagation that compounds an inherited procoagulant state into clinical thrombosis.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — The platelet thromboxane A2/endothelial prostacyclin balance governs platelet aggregation, and a shift toward thromboxane favors the platelet recruitment and clot propagation that worsen thrombotic risk in inherited thrombophilia.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — Neutrophils releasing S100A8/A9 and extracellular traps (NETs) provide a scaffold that ignites and amplifies venous thrombosis, an innate-immune amplifier that interacts with the inherited clotting-factor defects to precipitate clots.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — TLR4 sensing of DAMPs on endothelium and monocytes promotes tissue-factor expression and the immunothrombosis that, layered on a genetic hypercoagulable state, helps tip thrombophilic patients into clinical thrombosis.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement activation generating C3 and its fragments amplifies coagulation and platelet activation, an inflammatory contributor that compounds the inherited clotting tendency and links thrombosis to immune activation.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — Angiopoietin-2/Tie2 signaling shifts the endothelium toward a procoagulant, permeable phenotype that, on inflammatory triggers, compounds the baseline hypercoagulability of inherited thrombophilia.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β induces endothelial and monocyte tissue factor and downregulates anticoagulant pathways, the cytokine arm (with the IL-6 already mapped) that converts inflammation into the thrombosis triggered in thrombophilic patients.
- `connects-to` → **[TNF-α (Tumor Necrosis Factor-alpha)](../../03-molecular/tnf-alpha/README.md)** — TNF-α induces endothelial tissue factor and suppresses thrombomodulin and the protein-C pathway, tipping the hemostatic balance toward clotting that precipitates events in inherited thrombophilia.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — Complement C5a acting through C5aR1 (C3 and C5 mapped) induces tissue factor and activates platelets, amplifying the thrombotic tendency that becomes clinically manifest in inherited thrombophilia.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Serotonin released from platelet dense granules promotes further platelet aggregation and vasoconstriction, propagating the thrombus growth that underlies events in thrombophilic patients.
- `connects-to` → **[Thrombopoietin](../../03-molecular/thrombopoietin/README.md)** — Thrombopoietin sets the circulating platelet mass available for thrombus formation, a quantitative contributor to thrombotic risk in inherited thrombophilia.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Endothelial PI3K-AKT signaling sustains eNOS-derived nitric oxide and the protein-C anticoagulant axis (NO and protein C mapped); its impairment shifts the endothelium toward the prothrombotic state that compounds inherited thrombophilia.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — Thrombin acting through PAR receptors engages ERK-MAPK in platelets and endothelium (thrombin mapped), amplifying the prothrombotic activation state in inherited thrombophilia.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — VEGF-driven endothelial activation and permeability contributes to the prothrombotic endothelial phenotype, complementing the angiopoietin-Tie axis already mapped.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 promotes the neutrophil-extracellular-trap-driven thromboinflammation that amplifies the venous thrombotic risk of inherited thrombophilia.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — DNA within neutrophil extracellular traps engages cGAS-STING, linking NET-driven sterile inflammation to the prothrombotic state of inherited thrombophilia.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K-AKT signaling (AKT already mapped) in platelets and endothelium supports the activated, procoagulant phenotype that drives thrombosis in inherited thrombophilia.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK1/2-STAT cytokine signaling (IL-6 already mapped) links inflammatory tone to the endothelial procoagulant phenotype that potentiates venous thrombosis in inherited thrombophilia.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling modulates the endothelial activation that contributes to thrombotic risk in inherited thrombophilia.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO downstream of PI3K-AKT signaling (AKT and PIK3CA already mapped) regulates the endothelial quiescence-versus-activation balance relevant to inherited thrombophilia.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the platelet-activation and endothelial signaling that shape the prothrombotic tendency of inherited thrombophilia.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling (IL-6 already mapped) links the inflammatory state to the hypercoagulability of inherited thrombophilia.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR signaling in platelets and endothelium participates in the prothrombotic vascular phenotype of inherited thrombophilia.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of platelet and endothelial receptors participates in the platelet activation and thrombus formation of inherited thrombophilia.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked endothelial metabolic signaling modulates the vascular homeostasis relevant to the thrombotic tendency of inherited thrombophilia.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven monocyte recruitment contributes to the inflammation-linked thrombosis of inherited thrombophilia.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the endothelial and platelet homeostasis relevant to the hypercoagulable state of inherited thrombophilia.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic modulation of the coagulation and endothelial gene expression relevant to inherited thrombophilia.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the endothelial and leukocyte interactions of the thrombo-inflammation of inherited thrombophilia.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the endothelial activation and thromboinflammation relevant to inherited thrombophilia.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the thromboinflammatory processes relevant to inherited thrombophilia.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine signaling provides platelet-inhibitory and vascular modulation relevant to inherited thrombophilia.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Androgen risk: exogenous testosterone therapy raises venous thromboembolism risk partly by inducing erythrocytosis, a modifiable exposure that compounds the baseline hypercoagulability of an inherited thrombophilia.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Hyperviscosity: a raised haemoglobin and haematocrit increase blood viscosity and thrombosis risk, so polycythaemia, whether from JAK2-driven disease or other causes, acts synergistically with an inherited thrombophilia to precipitate clots.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Obesity multiplier: obesity is a strong independent risk factor for venous thrombosis, and the adipokine leptin promotes platelet activation and a prothrombotic state that multiplies the risk conferred by an inherited thrombophilia.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — Pregnancy risk: pregnancy is a hypercoagulable state driven by progesterone and estrogen (already mapped), and an inherited thrombophilia sharply raises the risk of pregnancy-associated venous thromboembolism and placental thrombotic complications.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Pulmonary embolism strain: a large pulmonary embolism from an inherited thrombophilia strains the right ventricle, and troponin elevation marks the myocardial injury that identifies high-risk PE needing more aggressive treatment.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Metabolic hypercoagulability: insulin resistance and the metabolic syndrome raise PAI-1 and fibrinogen (already mapped) to create an acquired prothrombotic state that compounds the risk of an inherited thrombophilia.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative thrombogenesis: reactive oxygen species, to which xanthine oxidase contributes, promote the endothelial dysfunction and platelet activation (already mapped) that tip the balance toward thrombosis in an inherited thrombophilia.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Thrombo-inflammation balance: coagulation and inflammation are intertwined, and the anti-inflammatory IL-10 opposes the pro-inflammatory signals (IL-6, TNF and IL-1 already mapped) that amplify thrombus formation in inherited thrombophilia.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — Metabolic-thrombotic axis: the insulin resistance (already mapped) that adds an acquired prothrombotic risk disturbs the incretin GLP-1 axis, part of the metabolic-syndrome hypercoagulability compounding an inherited thrombophilia.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Thrombo-inflammation balance: IL-4 and the M2 anti-inflammatory arm (IL-10 already mapped) counter the pro-inflammatory signals (IL-6, TNF and IL-1 already mapped) of the thrombo-inflammation that amplifies clot formation in inherited thrombophilia.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Metabolic prothrombotic risk: dyslipidaemia and the metabolic syndrome (insulin and leptin already mapped) add an acquired hypercoagulable state, and the raised cholesterol contributes to the arterial as well as venous thrombotic risk in inherited thrombophilia.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Platelet zinc and contact activation: zinc released from activated platelets (already mapped) promotes the contact pathway and fibrin formation (fibrinogen and thrombin already mapped), adding to the thrombotic tendency of inherited thrombophilia.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — Antiphospholipid antibodies: the IgG antiphospholipid antibodies (anti-cardiolipin, anti-β2-glycoprotein-I) of the antiphospholipid syndrome are the major acquired thrombophilia that mimics and compounds the inherited forms.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Autoimmune prothrombotic state: the type-I interferon of the autoimmune diseases (lupus, antiphospholipid syndrome) promotes the prothrombotic endothelial (already mapped) state, the acquired thrombophilia that adds to the inherited risk.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic hypercoagulability: the fall in adiponectin, with leptin (already mapped), of the metabolic syndrome (cholesterol and insulin already mapped) adds an acquired hypercoagulable state to the inherited thrombophilia.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Metabolic hypercoagulability: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the metabolic hypercoagulable state that adds an acquired thrombotic risk to the inherited thrombophilia.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Pulmonary embolism: the deep-vein thrombi of the inherited thrombophilias embolise to the lung, the pulmonary embolism the life-threatening complication.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Coagulation-factor synthesis: the liver synthesises the clotting factors and the natural anticoagulants (protein C, antithrombin already mapped) whose inherited deficiency causes thrombophilia.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Immunothrombosis: the NK cells (perforin already mapped) are part of the innate immune contribution to the immunothrombosis that amplifies the thrombotic tendency of the inherited thrombophilias.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 immunothrombosis: the IFN-γ of the T cells is the type-II interferon arm (with the type-I interferon already mapped) of the inflammatory dimension that potentiates the thrombosis of thrombophilia.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immunothrombotic inflammation accompanying the inherited thrombophilias.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 cytokine: IL-13, with IL-4 (already mapped), is part of the type-2 immune dimension of the inflammatory milieu that modulates the immunothrombosis of the inherited thrombophilias.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the inflammatory milieu accompanying the inherited thrombophilias.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immunothrombotic inflammation of the inherited thrombophilias.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the inflammatory milieu accompanying the inherited thrombophilias.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the immunothrombotic inflammation accompanying the inherited thrombophilias.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) at the interface of the complement and coagulation systems relevant to the immunothrombosis of the inherited thrombophilias.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement/coagulation crosstalk: the C1-esterase inhibitor regulates both the complement (C3, C5, C5aR1 and factor H already mapped) and the contact-coagulation systems at the interface of immunothrombosis relevant to the inherited thrombophilias.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Thromboinflammation: osteopontin, released by the activated platelets (already mapped), is a matricellular mediator that links the inflammation to the thrombosis of the inherited thrombophilias.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Iron/thrombosis: transferrin, the iron carrier, reflects the disordered iron handling that, with the dysregulated haemostasis, is part of the thrombotic-risk context of the inherited thrombophilias.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Endothelial alarmin: TSLP, released from endothelial cells (already mapped) and mast cells (already mapped) at sites of vascular wall stress, amplifies the thromboinflammatory milieu that converts the prothrombotic genotype into the overt thrombosis of inherited thrombophilia.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Contact-kinin thrombosis amplifier: bradykinin, generated by the contact activation (kallikrein-kinin) pathway co-activated with the coagulation cascade, amplifies the endothelial permeability and the prothrombotic milieu of inherited thrombophilia.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Erythrocyte rheology: erythropoietin, driving the erythropoiesis (erythrocyte already mapped), modulates haematocrit and blood viscosity — factors that interact with the prothrombotic genotypes of inherited thrombophilia to determine clinical thrombotic risk.

[^bertina-1994-factor-v-leiden]: Bertina RM, Koeleman BP, Koster T, et al. Mutation in blood coagulation factor V associated with resistance to activated protein C. *Nature.* 1994;369(6475):64-67. [doi:10.1038/369064a0](https://doi.org/10.1038/369064a0) · [PubMed 8164741](https://pubmed.ncbi.nlm.nih.gov/8164741/)
[^dahlback-2008-protein-c-review]: Dahlbäck B. Advances in understanding pathogenic mechanisms of thrombophilic disorders. *Blood.* 2008;112(1):19-27. [doi:10.1182/blood-2008-01-077909](https://doi.org/10.1182/blood-2008-01-077909) · [PubMed 18574048](https://pubmed.ncbi.nlm.nih.gov/18574048/)
[^kearon-2016-antithrombotic-therapy]: Kearon C, Akl EA, Ornelas J, et al. Antithrombotic therapy for VTE disease: CHEST guideline and expert panel report. *Chest.* 2016;149(2):315-352. [doi:10.1016/j.chest.2015.11.026](https://doi.org/10.1016/j.chest.2015.11.026) · [PubMed 26867832](https://pubmed.ncbi.nlm.nih.gov/26867832/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
