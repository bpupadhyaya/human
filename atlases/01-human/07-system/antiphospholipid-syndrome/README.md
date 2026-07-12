---
schema: human-scale-entry/v1
id: antiphospholipid-syndrome
name: Antiphospholipid Syndrome
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Antiphospholipid syndrome (APS) is an autoimmune thrombophilia from anti-B2GPI and antiphospholipid antibodies; thrombosis (DVT, stroke) and obstetric morbidity; triple-positive aPL = highest risk. Indefinite anticoagulation (warfarin INR 2-3); LMWH + aspirin for obstetric APS."
aliases: ["APS", "antiphospholipid syndrome", "Hughes syndrome", "antiphospholipid antibody syndrome", "APLS", "catastrophic APS", "CAPS", "obstetric APS"]
sources:
  - id: miyakis-2006-sydney-aps
    type: peer-reviewed
    cite: "Miyakis S, Lockshin MD, Atsumi T, et al. International consensus statement on an update of the classification criteria for definite antiphospholipid syndrome (APS). J Thromb Haemost. 2006;4(2):295-306."
    doi: "10.1111/j.1538-7836.2006.01753.x"
    pmid: "16420554"
    url: "https://doi.org/10.1111/j.1538-7836.2006.01753.x"
  - id: barbhaiya-2023-acreular-aps
    type: peer-reviewed
    cite: "Barbhaiya M, Zuily S, Naden R, et al. The 2023 ACR/EULAR antiphospholipid syndrome classification criteria. Ann Rheum Dis. 2023;82(10):1258-1270."
    doi: "10.1136/ard-2023-224609"
    pmid: "37643823"
    url: "https://doi.org/10.1136/ard-2023-224609"
cross_links:
  - target: 01-human/03-molecular/beta2-glycoprotein-1
    relation: connects-to
    note: "Anti-B2GPI IgG (domain I-specific; R39-R43 epitope) are the highest-risk pathogenic antibody in APS; B2GPI on phospholipid surfaces is the cofactor for anti-cardiolipin binding; triple aPL positivity (LA + aCL + anti-B2GPI) confers >10% annual thrombotic risk."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "APS is driven by IgG antiphospholipid antibodies (anti-B2GPI IgG, anti-cardiolipin IgG, lupus anticoagulant); IgG titers correlate with thrombotic risk; NOACs (rivaroxaban, dabigatran) are inferior to warfarin in APS (TRAPS trial); FcRn inhibitors under investigation."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Complement activation is central to APS thrombosis: anti-B2GPI → C3b deposition → C5a → neutrophil/platelet priming and TF expression; C5 inhibition (eculizumab) is used off-label for catastrophic APS (CAPS; ~37% mortality) refractory to anticoagulation and plasmapheresis."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "Secondary APS occurs in ~30% of SLE patients with persistent aPL; SLE+APS patients have higher stroke/DVT risk than either condition alone; hydroxychloroquine is recommended in all SLE+aPL patients; the 2023 ACR/EULAR APS criteria incorporate SLE as a risk modifier."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "APS causes recurrent DVT/PE in young adults; triple-positive aPL (LA + aCL + anti-B2GPI) confers >10% annual VTE risk; warfarin INR 2-3 is superior to DOACs in APS (TRAPS: rivaroxaban doubled arterial event risk in triple-positive patients); indefinite anticoagulation."
  - target: 01-human/07-system/inherited-thrombophilia
    relation: connects-to
    note: "APS and inherited thrombophilias (FV Leiden, prothrombin G20210A, protein C/S or AT deficiency) both cause recurrent VTE in young adults; co-existing aPL with thrombophilic mutations compounds risk multiplicatively; test for both in young patients with unexplained DVT/PE."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Antiphospholipid antibodies turn the endothelium prothrombotic: anti-β2GPI immune complexes engage endothelial TLR4 → NF-κB → tissue factor, converting the vessel lining from anticoagulant to clot-promoting — one of three converging hits driving APS thrombosis."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Antiphospholipid syndrome is a leading cause of stroke in the young: arterial APS produces ischemic stroke and TIA, so aPL testing is mandatory in stroke under 50, and arterial APS is anticoagulated to a higher INR (2.5-3.5), with warfarin beating DOACs."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "Half of APS is obstetric: antiphospholipid antibodies injure the placenta through both decidual-vessel thrombosis and direct, complement-(C5a)-mediated trophoblast damage, causing recurrent miscarriage, fetal loss, and pre-eclampsia — treated with LMWH plus low-dose aspirin."
  - target: 01-human/07-system/heparin-induced-thrombocytopenia
    relation: connects-to
    note: "APS and HIT are antibody-mediated acquired thrombophilias that clot despite thrombocytopenia: APS antiphospholipid antibodies and HIT anti-PF4 IgG each activate platelets and endothelium via Fc engagement, threatening arteries and veins; both can be catastrophic."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Platelets are central effectors in antiphospholipid syndrome: anti-β2GPI antibodies cluster on the platelet surface and, with complement, activate it via GPIbα/FcγRIIA → aggregation and thrombosis; mild thrombocytopenia is common, and the platelet is the aspirin target."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "APS injures the heart: antiphospholipid antibodies cause Libman-Sacks nonbacterial valvular vegetations (especially mitral) that can embolize or need surgery, accelerate coronary thrombosis, and in catastrophic APS produce myocardial thrombotic microangiopathy."
  - target: 01-human/07-system/disseminated-intravascular-coagulation
    relation: connects-to
    note: "Catastrophic antiphospholipid syndrome can resemble DIC: it floods small vessels with thrombi causing multi-organ failure, but unlike DIC it is antibody-driven with preserved clotting factors—so anticoagulation plus immunosuppression, not factor replacement, treats it."
  - target: 01-human/07-system/immune-thrombocytopenia
    relation: connects-to
    note: "Antiphospholipid syndrome pairs thrombosis with thrombocytopenia, a distinguishing clue: unlike isolated ITP, the low platelets accompany a prothrombotic state, so clots and a moderately low count plus lupus anticoagulant point to APS, not simple immune thrombocytopenia."
  - target: 01-human/07-system/sjogrens-syndrome
    relation: connects-to
    note: "Antiphospholipid syndrome often arises secondary to autoimmune disease like Sjögren's and lupus: the same loss of tolerance that produces anti-Ro or ANA can generate antiphospholipid antibodies, so thrombosis or pregnancy loss in such patients warrants APS testing."
  - target: 01-human/07-system/thrombotic-thrombocytopenic-purpura
    relation: connects-to
    note: "APS and TTP are both thrombotic microangiopathies: catastrophic APS (CAPS) mimics TTP with multi-organ microthrombi, but APS is driven by antiphospholipid antibodies and TTP by ADAMTS13 deficiency—antibody testing separates these clotting emergencies."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Antiphospholipid syndrome accelerates arterial disease beyond venous clots: the antibodies activate endothelium and platelets, promoting atherosclerosis and arterial thrombosis—so APS causes cardiovascular events in young patients, not just venous thromboembolism."
  - target: 01-human/07-system/migraine
    relation: connects-to
    note: "Migraine is a common neurological feature of antiphospholipid syndrome: antiphospholipid antibodies are associated with migraine and other neuro symptoms, and severe headache in a young patient with clots or miscarriage should prompt APS testing."
  - target: 01-human/03-molecular/thrombin
    relation: connects-to
    note: "Antiphospholipid syndrome tips coagulation toward thrombin: antiphospholipid antibodies activate endothelium, platelets and complement and impair natural anticoagulants, so thrombin generation runs unchecked—driving the venous and arterial clots that define the disease."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Antiphospholipid syndrome is driven by autoreactive B cells: they produce the antiphospholipid antibodies (against beta-2-glycoprotein I and cardiolipin) that cause clotting and pregnancy loss, so B-cell-directed therapy like rituximab is explored for refractory cases."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Antiphospholipid syndrome is a leading treatable cause of recurrent pregnancy loss: antibodies injure the placenta through thrombosis and complement, so obstetric APS—miscarriage, stillbirth, preeclampsia—is managed with aspirin and heparin to protect the pregnancy."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "The skin flags antiphospholipid syndrome: livedo reticularis—a netlike purple mottling—is a classic sign, and skin ulcers or digital gangrene can appear when small-vessel clots block flow, so dermatologic clues often precede a major thrombotic event."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "APS attacks the kidney as APS nephropathy: clots in glomerular capillaries and small renal arteries cause a thrombotic microangiopathy with hypertension and declining function, a renal manifestation distinct from the immune-complex nephritis of lupus."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils help APS clot through NETosis: antiphospholipid antibodies prime neutrophils to cast DNA extracellular traps that scaffold thrombi and activate platelets and complement, so this neutrophil pathway links autoimmunity to the syndrome's clotting."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "Antiphospholipid syndrome scars the glomerulus: a thrombotic microangiopathy clots the kidney's tiny vessels (APS nephropathy), causing hypertension and kidney impairment distinct from the immune-complex lupus nephritis it can accompany."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement turns antiphospholipid antibodies into thrombosis and miscarriage: the antibodies activate complement (C3 and beyond) on cells and placenta, so complement drives both the clotting and the pregnancy loss—and blocking it helps catastrophic APS."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Antiphospholipid syndrome is sustained by T-helper cells: they license B cells to produce the anti-beta2-glycoprotein-I antibodies that define the disease, so the autoimmune help behind the autoantibodies is a target for deeper therapy."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Clotting needs calcium, the cofactor APS exploits: the coagulation cascade APS tips toward thrombosis depends on calcium to anchor clotting factors to phospholipid membranes, the very surfaces the antiphospholipid antibodies target."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "APS strikes the brain through clots: antiphospholipid antibodies promote arterial thrombosis that causes stroke in the young, plus migraine, seizures and cognitive decline, making the brain one of the syndrome's most consequential targets."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "APS endangers the lungs with clots: antiphospholipid antibodies drive pulmonary emboli and, in catastrophic APS, widespread small-vessel thrombosis that can flood the lungs and cause respiratory failure."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "APS can clot the adrenal glands: thrombosis of their veins triggers hemorrhagic infarction, and bilateral adrenal failure—presenting as an Addisonian crisis—is a recognized, life-threatening way the syndrome announces itself."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "APS clots starve tissues of oxygen: by blocking arteries and veins—and, in catastrophic APS, the small vessels of many organs at once—the antibodies cause the ischemic infarcts that damage brain, kidney, and limbs."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "APS is sustained by plasma cells: these antibody factories pour out the anti-β2-glycoprotein-I antibodies that drive the clotting, so therapies aimed at B cells and plasma cells seek to shut the autoantibody supply off."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "APS is mapped by imaging: CT and MRI photons find its strokes, pulmonary emboli and deep-vein clots, and brain MRI reveals the silent infarcts behind its cognitive and neurological toll."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "APS clots the liver's veins: hepatic vein thrombosis (Budd-Chiari) and portal vein clots are among its unusual-site events, congesting and scarring the organ."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "APS damages vessels through mTOR: the antibodies activate this growth pathway in the vessel lining, driving the proliferative vasculopathy of APS nephropathy that mTOR inhibitors like sirolimus may slow."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows APS clots are bland: the vessels fill with platelet-fibrin thrombi without the inflammatory cell infiltrate of a vasculitis, the hallmark of an antibody-driven clotting disease rather than a vessel-wall inflammation."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "APS can suddenly blind: retinal artery and vein occlusions and ischemic optic neuropathy from the clotting tendency can steal vision, sometimes as the first sign of the syndrome."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "The spleen takes its share of APS clots: splenic infarction from thrombosed vessels causes left-upper-abdomen pain and is one of the abdominal-organ infarcts that mark widespread, sometimes catastrophic, disease."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "APS is defined by three antibodies: lupus anticoagulant, anticardiolipin, and anti-β2-glycoprotein-I, which paradoxically prolong clotting tests in the lab while driving thrombosis in the body — the serology that, with a clot or loss, makes the diagnosis."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "APS clots strike the brain young: it is a major cause of stroke and cerebral venous thrombosis in the under-50s, and beyond frank infarcts the antibodies are tied to cognitive impairment, seizures, and chorea."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "The antibodies can turn on the red cells: APS, especially with lupus, causes Coombs-positive autoimmune hemolytic anemia, and in its catastrophic form a microangiopathy shreds erythrocytes as clots fill the small vessels."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Clots can starve the bone: APS causes avascular necrosis, classically of the femoral head, when microthrombi cut off the blood supply to bone, collapsing the joint and adding orthopedic ruin to its vascular toll."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "It scars the heart's valves and muscle: APS drives Libman-Sacks endocarditis, sterile thrombotic vegetations on the valves, and coronary microthrombi that injure cardiomyocytes, a cardiac face beyond the large-vessel clots."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Catastrophic APS can infarct the gut: when clots storm the small vessels of many organs at once, mesenteric thrombosis starves the bowel into ischemia and infarction, part of the multi-organ failure that makes the catastrophic form so lethal."
  - target: 01-human/03-molecular/protein-c
    relation: connects-to
    note: "The antibodies sabotage a key brake on clotting: they interfere with the activated protein C pathway, creating an acquired APC resistance that, alongside their many other hits, tips the blood toward thrombosis."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "The antibodies switch on the clot-starters: binding β2-glycoprotein I on monocytes and macrophages, they drive these cells to express tissue factor, a central way antiphospholipid antibodies ignite thrombosis."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "Old clots can choke the lung's circulation: recurrent pulmonary emboli in APS may organize into chronic thromboembolic pulmonary hypertension, the scarred, narrowed arteries straining the right heart."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "The autoantibody switches cells into a clotting mode: anti-β2-glycoprotein-I antibodies signal through TLR4 on endothelial cells and monocytes, driving tissue factor and the prothrombotic activation behind APS thrombosis."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "It scars the heart valves: APS causes Libman-Sacks endocarditis with sterile valve vegetations, and that valve damage plus microthrombi in the myocardium can drift toward heart failure."
  - target: 01-human/07-system/ahus
    relation: connects-to
    note: "Catastrophic APS becomes a thrombotic microangiopathy: in its fulminant form, widespread small-vessel clotting and organ failure overlap atypical HUS, a complement-amplified emergency that must be told apart from it."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "The antibodies switch endothelium to clot mode through NF-κB: antiphospholipid antibodies signal via TLR4 to activate NF-κB in endothelial cells and monocytes, driving the tissue factor expression that makes APS relentlessly prothrombotic."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "It clots the kidney's small vessels: APS nephropathy is a thrombotic microangiopathy of the renal microcirculation that, with recurrent renal vein or artery thrombosis, can erode kidney function into chronic kidney disease."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "It can spark seizures directly: beyond stroke, antiphospholipid antibodies are linked to epilepsy through microthrombi and possible direct binding to neuronal tissue, one of the disease's range of neurological manifestations."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Infection can ignite its deadliest form: catastrophic antiphospholipid syndrome — widespread small-vessel thrombosis and multiorgan failure — is frequently triggered by infection and clinically overlaps with sepsis."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "It reaches the mind as well as the vessels: cerebral microthrombi and direct antibody effects contribute to cognitive impairment and depression in APS, beyond the burden of a chronic relapsing thrombotic disease."
  - target: 01-human/07-system/ovarian-cancer
    relation: connects-to
    note: "Cancer can drive the antibodies: antiphospholipid antibodies and thrombosis can arise as a paraneoplastic phenomenon, so a new APS-like clotting state — particularly with adenocarcinomas like ovarian cancer — prompts a malignancy search."
  - target: 01-human/07-system/alzheimers-disease
    relation: connects-to
    note: "Repeated small clots erode cognition: recurrent cerebral microthrombi and strokes in antiphospholipid syndrome cause multi-infarct vascular cognitive impairment that overlaps with and accelerates Alzheimer-type dementia."
  - target: 01-human/07-system/multiple-sclerosis
    relation: connects-to
    note: "It can masquerade as demyelination: the white-matter lesions and neurological deficits of antiphospholipid syndrome can mimic multiple sclerosis, an important differential since the treatments diverge sharply."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Its clots starve the skin: small-vessel thrombosis in antiphospholipid syndrome causes livedo, leg ulcers and digital ischemia that heal poorly as occluded vessels deprive the tissue of blood."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It clots the veins draining the gut and liver: antiphospholipid syndrome causes hepatic vein thrombosis (Budd-Chiari) and mesenteric thrombosis with bowel ischaemia, threatening the abdominal organs."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Beyond stroke it disturbs the brain directly: antiphospholipid syndrome causes chorea, cognitive dysfunction, transverse myelitis and seizures, neurological features distinct from its frank thrombotic strokes."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Recurrent clots and pregnancy loss breed worry: the threat of unpredictable thrombosis, miscarriage and the demands of lifelong anticoagulation in antiphospholipid syndrome foster chronic health anxiety."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "It is an autoimmune clotting disease: antiphospholipid antibodies — lupus anticoagulant, anti-cardiolipin and anti-β2-glycoprotein-I — activate platelets, endothelium and complement to drive its thromboses and pregnancy loss."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It is written on the skin: livedo reticularis is a hallmark, with skin ulcers, splinter haemorrhages and digital gangrene reflecting the small-vessel thrombosis of antiphospholipid syndrome."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "It scars the heart valves and arteries: antiphospholipid syndrome causes Libman-Sacks non-bacterial valvular vegetations and coronary thrombosis, adding cardiac disease to its accelerated atherosclerosis."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "APS nephropathy attacks the kidney: thrombotic microangiopathy in renal arterioles plus renal artery or vein thrombosis drives hypertension and progressive renal impairment."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It throws clots to the lungs: recurrent pulmonary embolism and, in catastrophic APS, diffuse alveolar haemorrhage and chronic thromboembolic pulmonary hypertension can result."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Adrenal vein thrombosis can trigger bilateral adrenal infarction and haemorrhage — a recognised antiphospholipid cause of acute primary adrenal insufficiency."
  - target: 03-medicine/01-modern/09-hematology/warfarin
    relation: connects-to
    note: "Lifelong anticoagulation is its mainstay: warfarin at INR 2-3 prevents recurrent thrombosis in APS and outperforms direct oral anticoagulants, which are avoided especially in triple-antibody-positive disease."
  - target: 03-medicine/01-modern/04-cardio/aspirin
    relation: connects-to
    note: "Low-dose aspirin protects pregnancy and arteries: combined with heparin it prevents obstetric APS losses, and it is used for primary prevention in asymptomatic antiphospholipid-antibody carriers."
  - target: 02-pathogen/01-viruses/epstein-barr-virus
    relation: connects-to
    note: "Infection can raise the antibodies: transient antiphospholipid antibodies appear after Epstein-Barr and other infections through molecular mimicry, usually without thrombosis, a key cause of false-positive testing."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "It clots arteries, not just veins: APS uniquely causes both venous and arterial thrombosis — stroke, MI and limb ischaemia — and accelerates atherosclerosis of the arterial wall through antibody-driven endothelial activation."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Biologics rescue catastrophic disease: rituximab and the complement inhibitor eculizumab, with hydroxychloroquine as an antithrombotic adjunct, are used in refractory and catastrophic antiphospholipid syndrome beyond standard anticoagulation."
  - target: 01-human/05-tissue/endocardium
    relation: connects-to
    note: "It scars the heart valves: APS causes Libman-Sacks endocarditis, sterile fibrin-platelet vegetations on the valve endocardium that can embolise to the brain or require valve surgery."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "It clots and bleeds the lung: antiphospholipid syndrome causes pulmonary embolism and, in catastrophic APS, diffuse alveolar haemorrhage—two ways its prothrombotic immunity injures the alveolar bed."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "A virus that mimics it: severe COVID-19 induces antiphospholipid antibodies and a complement-driven prothrombotic state resembling antiphospholipid syndrome, though usually transient."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "It clots the liver's veins: antiphospholipid syndrome causes hepatic and portal vein thrombosis (Budd-Chiari), congesting the hepatic lobule and threatening liver failure."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "It clots the coronary arteries: antiphospholipid syndrome causes myocardial infarction in young patients and microthrombi within the myocardium, a cardiac face beyond its Libman-Sacks valve disease."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Where the autoantibodies form: the anti-β2-glycoprotein-I and anticardiolipin antibodies driving APS arise from germinal-centre B-cell responses, which is why B-cell depletion is tried in refractory disease."
  - target: 01-human/07-system/nmo
    relation: connects-to
    note: "Clustering autoimmunity: antiphospholipid syndrome co-occurs with other autoantibody diseases including neuromyelitis optica and lupus, reflecting a shared tendency to break B-cell tolerance."
  - target: 01-human/07-system/polycythemia-vera
    relation: connects-to
    note: "Unusual-site thrombosis workup: antiphospholipid syndrome and JAK2-mutant myeloproliferative neoplasms like polycythaemia vera are both sought in Budd-Chiari and cerebral-vein thrombosis, two acquired causes of clots in odd places."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Osteonecrosis: antiphospholipid microthrombi—and the corticosteroids often used with it—starve the blood supply to bone, causing avascular necrosis (osteonecrosis) of the femoral head and other cortical bone."
  - target: 01-human/07-system/systemic-sclerosis
    relation: connects-to
    note: "Overlapping connective-tissue autoimmunity: antiphospholipid antibodies and a thrombotic vasculopathy occur in systemic sclerosis and other connective-tissue diseases, compounding their own microvascular injury."
  - target: 01-human/03-molecular/von-willebrand-factor
    relation: connects-to
    note: "Endothelial activation: antiphospholipid antibodies activate endothelium to release von Willebrand factor, promoting the platelet adhesion that contributes to APS thrombosis."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "eNOS inhibition: antiphospholipid antibodies suppress endothelial nitric oxide synthase, cutting the vasodilator, antithrombotic nitric oxide that normally protects the vessel wall in APS."
  - target: 01-human/03-molecular/fibrinogen
    relation: connects-to
    note: "Clot substrate: the thrombin generation driven by antiphospholipid antibodies converts fibrinogen to fibrin, building the venous and arterial clots that define the syndrome."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "NETosis-driven thrombosis: antiphospholipid antibodies prime neutrophils to release extracellular traps rich in S100A8/A9, a key thrombo-inflammatory mechanism propagating clots in antiphospholipid syndrome."
  - target: 01-human/03-molecular/pf4
    relation: connects-to
    note: "Platelet activation: antiphospholipid antibodies activate platelets to release PF4 and procoagulant granules, lowering the threshold for the arterial and venous thrombosis of APS."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Vasculopathy: aPL-activated endothelium releases endothelin-1, whose vasoconstriction adds to the non-inflammatory intimal proliferation and organ ischaemia of antiphospholipid-associated vasculopathy."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "Complement amplification: aPL antibodies activate complement, and C5a acting on C5aR1 drives the thrombosis and placental injury of APS — the basis for complement (eculizumab) treatment of catastrophic antiphospholipid syndrome."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Monocyte tissue factor: aPL antibodies bind β2GPI on monocytes and, with CCL2-driven recruitment, induce tissue-factor expression that ignites the thrombin generation central to antiphospholipid thrombosis."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Placental insufficiency: antiphospholipid antibodies impair trophoblast VEGF signalling and angiogenesis, producing the defective placentation behind the recurrent pregnancy loss and pre-eclampsia of obstetric APS."
  - target: 01-human/03-molecular/baff
    relation: connects-to
    note: "Autoantibody source: BAFF supports the autoreactive B cells that produce the anti-β2-glycoprotein-I and anticardiolipin antibodies defining APS, the humoral origin of the disease and a rationale for B-cell-directed therapy in refractory cases."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Trophoblast apoptosis: antiphospholipid antibodies binding β2-glycoprotein-I on trophoblast trigger caspase-3-mediated apoptosis and impair invasion, a direct cellular mechanism of the placental failure in obstetric APS beyond thrombosis."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Genetic predisposition: particular HLA class II alleles predispose to producing antiphospholipid antibodies by favouring presentation of β2-glycoprotein-I peptides to helper T cells, linking the genetic risk to the breaking of tolerance."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Vasculopathy signalling: anti-β2GPI antibodies activate endothelial PI3K-AKT-mTOR signalling (mTOR already mapped), driving the intimal hyperplasia of APS vasculopathy and nephropathy that mTOR inhibitors like sirolimus can treat."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Obstetric inflammation: TNF-α is a key mediator of the placental inflammation and thrombosis of obstetric antiphospholipid syndrome, linking the autoantibodies to recurrent fetal loss."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Thrombo-inflammation: antiphospholipid antibodies engage TLR4 (already mapped) to activate the NLRP3 inflammasome and IL-1β in monocytes and endothelium, amplifying the thrombo-inflammatory state of APS."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Tissue-factor induction: anti-β2-glycoprotein-1 antibodies (β2GPI and TLR4 mapped) signal through MyD88 to NF-κB (mapped) in endothelium and monocytes, inducing the tissue factor that drives the prothrombotic state of APS."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Platelet amplification: serotonin released from antibody-activated platelet dense granules promotes further aggregation and vasoconstriction, propagating the thrombosis of antiphospholipid syndrome."
  - target: 01-human/03-molecular/thrombopoietin
    relation: connects-to
    note: "Platelet turnover: thrombopoietin sets the platelet mass available for thrombus formation, relevant to both the thrombocytopenia and the thrombosis that characterise antiphospholipid syndrome."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Antiphospholipid antibodies engaging β2-glycoprotein-1 (mapped) on endothelium, platelets and monocytes activate ERK-MAPK, inducing tissue factor and the prothrombotic phenotype of APS."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "aPL signalling recruits PI3K (PIK3CA) upstream of the AKT-mTOR axis (AKT and mTOR mapped) that drives endothelial activation and the vasculopathy of antiphospholipid syndrome."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 amplifies the monocyte and endothelial inflammatory response to antiphospholipid antibodies, contributing to APS thromboinflammation."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling transduces the inflammatory cytokine response of monocytes and endothelium activated by antiphospholipid antibodies in APS."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "DNA within antiphospholipid-antibody-triggered neutrophil extracellular traps engages cGAS-STING, linking NET-driven inflammation to the thrombosis of APS."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling contributes to the placental dysfunction and decidual remodelling underlying the pregnancy morbidity of obstetric APS."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK1/2-STAT cytokine signaling (IL-6-STAT3 already mapped) amplifies the endothelial and monocyte inflammatory activation that drives the thrombosis of antiphospholipid syndrome."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signaling, reflecting the type-I interferon signature of APS, shapes the immune activation underlying antiphospholipid syndrome."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO downstream of antiphospholipid-antibody-triggered PI3K-AKT-mTOR signaling (AKT, PIK3CA, and mTOR already mapped) regulates the endothelial activation balance in antiphospholipid syndrome."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the platelet-activation and mTOR-linked endothelial signaling that drive the thrombosis of antiphospholipid syndrome."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of β2GPI-antibody engagement of platelet and endothelial receptors contributes to the prothrombotic activation of antiphospholipid syndrome."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α in the ischemic placenta contributes to the pregnancy morbidity of obstetric antiphospholipid syndrome."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked endothelial metabolic signaling modulates the vascular homeostasis relevant to the thrombosis of antiphospholipid syndrome."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the endothelial, platelet, and trophoblast responses relevant to antiphospholipid syndrome."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven monocyte recruitment contributes to the inflammation-linked thrombosis of antiphospholipid syndrome."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the autoreactive immune response of antiphospholipid syndrome."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the endothelial and leukocyte interactions of the thrombo-inflammation of antiphospholipid syndrome."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammasome activation participates in the prothrombotic and placental inflammation of antiphospholipid syndrome."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the endothelial and immune activation of antiphospholipid syndrome."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the thromboinflammatory immune response of antiphospholipid syndrome."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the T-cell help driving the anti-β2GPI autoantibody response of antiphospholipid syndrome."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "B-cell depletion: refractory and catastrophic antiphospholipid syndrome is treated with the anti-CD20 antibody rituximab to deplete the B cells producing anti-β2GPI antibodies (immunoglobulin G already mapped), a targeted immunotherapy beyond anticoagulation."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell help: IL-2-driven expansion of the T cells that help autoreactive B cells sustains the antiphospholipid antibody response, and impaired regulatory-T-cell control contributes to the persistence of the autoimmunity."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Autoreactive survival: anti-apoptotic BCL-2 family proteins prolong the survival of the autoreactive B cells producing antiphospholipid antibodies, helping the autoimmune clone persist despite the normal checkpoints that should delete it."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Pregnancy morbidity: antiphospholipid syndrome causes recurrent pregnancy loss and placental thrombosis, and the oestrogen-rich prothrombotic state of pregnancy (and of oestrogen contraception) heightens the thrombotic risk it confers."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Cardiac thrombosis: antiphospholipid syndrome causes coronary thrombosis, myocardial infarction and Libman-Sacks valve lesions, and troponin elevation marks the myocardial injury of these cardiac thrombotic manifestations."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Microangiopathic haemolysis: catastrophic antiphospholipid syndrome and its thrombotic microangiopathy fragment red cells and, with autoimmune haemolysis, lower haemoglobin, adding a haematological dimension to the widespread thrombosis."
  - target: 01-human/03-molecular/adamts13
    relation: connects-to
    note: "Microangiopathy differential: the thrombotic microangiopathy of catastrophic antiphospholipid syndrome occurs with normal ADAMTS13 (von Willebrand factor already mapped), distinguishing its antibody-driven mechanism from thrombotic thrombocytopenic purpura."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Thromboxane-prostacyclin balance: antiphospholipid antibodies shift the endothelial and platelet (already mapped) prostaglandin balance toward the prothrombotic thromboxane, part of why low-dose aspirin is used in antiphospholipid syndrome."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative antigenicity: oxidative stress, to which xanthine oxidase contributes, generates the oxidised beta-2-glycoprotein-1 (already mapped) that is the key target of the pathogenic antibodies, linking oxidation to the antigenicity of antiphospholipid syndrome."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "B-cell autoantibody help: IL-4 and the Th2 response support the B cells (BAFF and CD20 already mapped) that produce the anti-β2-glycoprotein-1 and anticardiolipin antibodies driving antiphospholipid syndrome."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 humoral arm: IL-13, with IL-4 (already mapped), completes the type-2 cytokine support for the autoantibody-producing B cells of antiphospholipid syndrome, the humoral autoimmunity behind the pathogenic antibodies."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Platelet zinc and coagulation: zinc released from the activated platelets (already mapped) promotes the contact pathway and fibrin formation (fibrinogen and thrombin already mapped), adding to the prothrombotic state of antiphospholipid syndrome."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Autoimmune signature: the type-I interferon of the autoimmune (lupus already mapped) background promotes the endothelial (already mapped) prothrombotic state and the autoantibody production of antiphospholipid syndrome."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Checkpoint tolerance: the PD-1 checkpoint and peripheral-tolerance mechanisms, when dysfunctional, permit the anti-β2-glycoprotein-I (already mapped) autoreactivity that drives antiphospholipid syndrome."
  - target: 01-human/03-molecular/ctla-4
    relation: connects-to
    note: "Co-inhibitory checkpoint: CTLA-4, with PD-1 (already mapped), regulates the autoreactive T cells that help the B cells (CD20 and BAFF already mapped) produce the pathogenic antibodies of antiphospholipid syndrome."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Immune-metabolic adipokine: leptin is the adipokine of the immune-metabolic milieu that modulates the thrombo-inflammatory autoimmunity of antiphospholipid syndrome."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic-inflammatory milieu of antiphospholipid syndrome."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the thrombo-inflammatory milieu (IL-6 and TNF already mapped) of antiphospholipid syndrome."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Innate immune modulation: the NK cells (perforin already mapped) are part of the innate immune dysregulation of the thrombo-inflammatory autoimmunity of antiphospholipid syndrome."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 autoimmunity: the IFN-γ of the T cells is the type-II interferon arm (with the type-I interferon already mapped) of the immune dysregulation driving the anti-β2GPI (already mapped) autoantibodies of antiphospholipid syndrome."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the autoimmune response of antiphospholipid syndrome."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation of antiphospholipid syndrome."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the autoimmune response driving the anti-β2GPI (already mapped) autoantibodies of antiphospholipid syndrome."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the autoimmune response of antiphospholipid syndrome."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) whose activation on the anti-β2GPI (already mapped) immune complexes drives the thrombosis of antiphospholipid syndrome."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement/contact regulation: the C1-esterase inhibitor regulates the classical complement and the contact-coagulation systems at the interface driving the thromboinflammation of antiphospholipid syndrome."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Antigen presentation: the dendritic cells present the β2-glycoprotein-1 (already mapped) to the T cells (already mapped), priming the autoantibody response of antiphospholipid syndrome."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Thromboinflammation: osteopontin, released by the activated platelets (already mapped), is a matricellular mediator amplifying the neutrophil (already mapped) and endothelial thromboinflammation of antiphospholipid syndrome."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Haemolytic/thrombotic iron: transferrin, the iron carrier, reflects the disordered iron handling of the haemolysis and the microvascular thrombosis of antiphospholipid syndrome."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Adaptive arm: the cytotoxic T cells (perforin pathway), with the T-helper (already mapped) support of the anti-β2GP1 response, are part of the adaptive-immune dimension of antiphospholipid syndrome."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-thromboinflammatory axis: TSLP, from inflamed endothelium (already mapped) and placental (already mapped) tissue, primes dendritic cells (already mapped) and mast cells (already mapped) and amplifies the Th2/B-cell bias driving the anti-β2GP1 antibody production of APS."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-thrombosis axis: bradykinin, generated by the kallikrein-kinin system activated via the contact pathway on aPL-coated endothelium, amplifies vascular permeability and the prothrombotic milieu of antiphospholipid syndrome."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Haemolytic anaemia support: erythropoietin drives red-cell regeneration to counteract the autoimmune haemolytic anaemia (already mapped) and the thrombotic microangiopathy-driven haemolysis of antiphospholipid syndrome."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell vascular effector: histamine, released by mast cells (already mapped) at sites of aPL-driven vascular inflammation, amplifies endothelial permeability and the prothrombotic cytokine milieu (TNF-α and IL-6 already mapped) of antiphospholipid syndrome."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "ECM remodelling in placenta and vessels: periostin, expressed in the placenta (already mapped) and vascular adventitia under thromboinflammatory injury, modulates the fibrotic remodelling of decidual vessels and contributes to the obstetric morbidity of APS."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian antithrombotic protection: melatonin, via MT1/MT2 receptors on platelets (already mapped) and endothelial cells (already mapped), suppresses the NF-κB-driven (already mapped) prothrombotic cytokine surge and attenuates the nocturnal thrombosis risk of APS."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "APS testosterone: testosterone, via androgen receptors on endothelial cells (already mapped) and platelets (already mapped), attenuates NF-κB (already mapped) and complement-C5 (already mapped) thromboinflammation and the aPL-driven thrombotic risk of APS."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "APS prolactin: prolactin, via PRLR on endothelial cells (already mapped) and platelets (already mapped), promotes prothrombotic cytokine release and the NF-κB (already mapped) anti-β2GP1 response; prolactin amplifies the complement-C5 (already mapped) thromboinflammation of APS."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "APS oxytocin: oxytocin, via OXTR on endothelial cells (already mapped) and platelets (already mapped), suppresses NF-κB (already mapped) and complement-C5 (already mapped) thromboinflammation; oxytocin also attenuates aPL-driven placenta (already mapped) injury of APS."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "APS vasopressin: vasopressin, via V1a receptors on platelets (already mapped) and endothelial cells (already mapped), promotes prothrombotic platelet activation; vasopressin amplifies NF-κB (already mapped) and complement-C5 (already mapped) thromboinflammatory cascade of APS."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "APS selenium: selenium-dependent GPx suppresses the ROS amplifying NF-κB (already mapped) and complement-C5 (already mapped) endothelial injury in APS; selenium deficiency promotes platelet (already mapped) hyperreactivity and the thromboinflammatory vascular injury of APS."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "APS iodine: iodine-dependent thyroid hormones modulate endothelial cell (already mapped) function and platelet (already mapped) reactivity; hypothyroidism, common in autoimmune patients, amplifies NF-κB (already mapped) thromboinflammation and aPL coagulation risk of APS."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "APS sodium: excess sodium promotes macrophage (already mapped) and neutrophil (already mapped) pro-inflammatory skewing; sodium-induced NF-κB (already mapped) amplifies endothelial-cell (already mapped) and platelet (already mapped) thromboinflammatory cascade of APS."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "APS potassium: potassium regulates endothelial-cell (already mapped) and platelet (already mapped) membrane excitability; potassium dysregulation amplifies NLRP3 (already mapped) and NF-κB (already mapped) and complement-C3 (already mapped) thromboinflammatory cascade in APS."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "APS magnesium: magnesium stabilises endothelial-cell (already mapped) function and attenuates platelet (already mapped) aggregation; magnesium deficiency amplifies NF-κB (already mapped) and thrombin (already mapped) and complement-C5 (already mapped) procoagulant cascade in APS."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "APS copper: copper, via SOD in endothelial cells (already mapped) and macrophages (already mapped), scavenges ROS; copper deficiency amplifies NF-κB (already mapped) and NLRP3 (already mapped) and complement-C3 (already mapped) thromboinflammatory cascade in APS."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "iron-driven ferroptosis in endothelial cells (already mapped) amplifies oxidative stress on platelet (already mapped) activation and complement-C3 (already mapped) deposition; iron excess amplifies NF-κB (already mapped) and thrombin (already mapped) procoagulant cascade in APS."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "phosphorus-driven ATP in platelets (already mapped) and endothelial cells (already mapped) sustains anti-thrombotic signalling; phosphorus deficiency amplifies NF-κB (already mapped) and thrombin (already mapped) and complement-C5 (already mapped) procoagulant cascade in APS."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "nitric oxide from iNOS in endothelial cells (already mapped) and macrophages (already mapped) modulates vascular tone; NO deficiency amplifies thrombin (already mapped) and complement-C5 (already mapped) and NF-κB (already mapped) procoagulant cascade in APS."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "APS carbon: carbon backbone of lipids in platelets (already mapped) and endothelial cells (already mapped) sustains thrombostasis; carbon dysregulation amplifies NF-κB (already mapped) and thrombin (already mapped) and complement-C3 (already mapped) procoagulant cascade in APS."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "APS chloride: chloride channels in endothelial cells (already mapped) and platelets (already mapped) modulate vascular tone; chloride dysregulation amplifies NF-κB (already mapped) and thrombin (already mapped) and complement-C5 (already mapped) thrombotic cascade in APS."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "APS hydrogen: hydrogen via ROS balance in endothelial cells (already mapped) and macrophages (already mapped) modulates oxidative stress; hydrogen excess amplifies NF-κB (already mapped) and thrombin (already mapped) and complement-C3 (already mapped) procoagulant cascade in APS."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "APS sulfur: H2S from sulfur-amino acids in endothelial cells (already mapped) and platelets (already mapped) modulates vascular tone; sulfur deficiency amplifies NF-κB (already mapped) and thrombin (already mapped) and complement-C5 (already mapped) thrombotic cascade in APS."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "APS GLP-1: GLP-1 receptor signalling in macrophages (already mapped) and endothelial cells (already mapped) modulates vascular homeostasis; GLP-1 dysregulation amplifies NF-κB (already mapped) and thrombin (already mapped) and complement-C5 (already mapped) cascade in APS."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "APS angiotensin-II: angiotensin-II in endothelial cells (already mapped) and macrophages (already mapped) promotes vascular inflammation; angiotensin-II excess amplifies NF-κB (already mapped) and thrombin (already mapped) and complement-C5 (already mapped) cascade of APS."
---

# Antiphospholipid Syndrome

## Overview

**Antiphospholipid syndrome (APS; Hughes syndrome)** is an **autoimmune thrombophilia** defined by the combination of:
1. **Clinical criteria**: arterial or venous thrombosis, OR pregnancy morbidity
2. **Laboratory criteria**: persistent antiphospholipid antibodies (aPL) — lupus anticoagulant (LA), anti-cardiolipin IgG/IgM (aCL), or anti-beta-2 glycoprotein I IgG/IgM (anti-B2GPI) — on ≥2 occasions ≥12 weeks apart [^miyakis-2006-sydney-aps]

APS is the most common acquired thrombophilia in young adults and the leading identifiable cause of recurrent early pregnancy loss. It exists in two forms:
- **Primary APS:** No underlying systemic autoimmune disease
- **Secondary APS:** Associated with systemic lupus erythematosus (SLE; ~30% of aPL-positive SLE patients), other autoimmune conditions, or infections

**Key statistics:**
- Prevalence: ~40-50 per 100,000 population; F:M ratio ~3:1 for primary APS
- Annual thrombotic risk: ~1-5% per year in aPL-positive patients; up to >10% per year in triple-positive patients
- Recurrence: ~50% thrombotic recurrence without anticoagulation; recurrence rate drops to 5-10% with warfarin INR 2-3
- **Catastrophic APS (CAPS):** <1% of APS patients; multi-organ thrombosis within days; mortality ~37%

## Structure

### Classification of aPL antibody profiles

**2006 Revised Sapporo/Sydney criteria** (clinical + laboratory):

**Clinical criteria:**
- Vascular thrombosis: ≥1 confirmed episode of arterial/venous/small vessel thrombosis
- Pregnancy morbidity: ≥1 fetal death ≥10 weeks; ≥3 unexplained consecutive losses <10 weeks; ≥1 premature birth <34 weeks due to eclampsia/IUGR

**Laboratory criteria (must be present on ≥2 occasions ≥12 weeks apart):**
- Lupus anticoagulant (LA) — detected by dRVVT or aPTT-based assay; most thrombogenic single test
- Anti-cardiolipin IgG/IgM ≥40 GPL/MPL units
- Anti-B2GPI IgG/IgM ≥40 units or >99th percentile

**2023 ACR/EULAR classification criteria** — major update introducing risk stratification [^barbhaiya-2023-acreular-aps]:
- Entry criterion: aPL positivity; exclusion of mimics (infection, drug-induced)
- Weighted domain scoring (aPL profile + clinical domains)
- Emphasizes **high-risk aPL profile**: LA positive, and/or triple positivity, and/or anti-B2GPI IgG >40 units
- Separates thrombotic APS, obstetric APS, and CAPS into distinct clinical domains

### Risk stratification by aPL profile

| aPL profile | Annual thrombotic risk | Clinical management |
|:-----------|:----------------------|:-------------------|
| Single aPL positive (low titer) | ~1-2% | Aspirin 100 mg/day; risk factor modification |
| Isolated LA positive | ~3-5% | Aspirin; consider warfarin in high-risk settings |
| Double positive (any 2 of 3) | ~5-8% | Warfarin INR 2-3; HCQ in SLE |
| **Triple positive (LA + aCL + anti-B2GPI)** | **>10%** | **Warfarin INR 2-3 indefinitely; aspirin** |

## Function

### Normal hemostasis disrupted in APS

B2GPI normally functions as an anticoagulant by:
- Inhibiting factor Xa and the tenase complex
- Competing with prothrombin for phospholipid binding
- Inhibiting ADP-induced platelet aggregation

In APS, anti-B2GPI IgG bound to B2GPI on phospholipid surfaces converts this anticoagulant into a pro-thrombotic surface activator — one of the most elegant mechanisms of autoimmune disease.

## Pathology

### Pathogenesis: three converging mechanisms

**Mechanism 1 — Endothelial activation:**
- Anti-B2GPI IgG + B2GPI on endothelial surface → TLR4 engagement → MyD88 → NF-κB → tissue factor (TF) upregulation, E-selectin, VCAM-1, ICAM-1
- Endothelial TF initiates extrinsic coagulation cascade → thrombin generation → fibrin → thrombus

**Mechanism 2 — Platelet activation:**
- B2GPI on activated platelet surface (PS exposed) + anti-B2GPI IgG → GPIbα receptor interaction → direct platelet activation
- FcγRIIA-dependent (Fc-mediated) platelet priming by anti-B2GPI IgG-B2GPI immune complexes

**Mechanism 3 — Complement activation:**
- Anti-B2GPI immune complexes → classical complement C1q → C3b → C5 → C5a
- C5a primes neutrophils and platelets → TF expression → thrombus amplification
- **Obstetric APS:** C5a at placental decidua → trophoblast injury independent of thrombosis → placental insufficiency, fetal loss, IUGR

### Clinical manifestations

**Thrombotic APS:**
| Site | Manifestation | Notes |
|:-----|:-------------|:------|
| Venous (most common, ~60%) | DVT, PE, cerebral venous thrombosis | Often young patients; all without provoking factors should be tested for aPL |
| Arterial (~30%) | Stroke, TIA, MI, limb ischemia, retinal artery occlusion | Stroke in young patients <50 years: aPL testing mandatory |
| Microvascular | Livedo reticularis, Sneddon syndrome (livedo + stroke), thrombotic nephropathy | LA most strongly associated |

**Obstetric APS:**
- ≥3 consecutive early losses (<10 weeks): attributed to endometrial dysfunction + embryo implantation failure
- Fetal loss ≥10 weeks: placental thrombosis, decidual vasculopathy
- Preeclampsia, IUGR, placental abruption (≥34 weeks): placental inflammation + impaired placentation

**Catastrophic APS (CAPS):**
- Multi-organ thrombosis within <1 week; microvascular predominant
- Triggers: infection (most common), surgery, withdrawal of anticoagulation, OCP
- Organs: kidney (most common), lung, brain, heart, skin (livedo fulminans), adrenal (infarction → crisis)
- Mortality ~37% despite treatment; treated with anticoagulation + glucocorticoids + IVIG or plasma exchange; eculizumab (anti-C5) for refractory CAPS

**Non-criteria APS manifestations:**
- Thrombocytopenia (~30%): anti-B2GPI on platelet surfaces → immune destruction + FcγRIIa-mediated platelet activation
- Hemolytic anemia
- Cardiac: Libman-Sacks endocarditis (non-bacterial verrucous endocarditis; predisposes to embolic stroke)
- Cognitive dysfunction, migraine, chorea (CNS aPL deposition)
- Skin: livedo reticularis, superficial thrombophlebitis, skin necrosis

### Diagnosis

**Laboratory testing:**
- **Lupus anticoagulant (LA):** Most predictive of thrombosis; detected by phospholipid-dependent clotting assays (dRVVT, aPTT-based): prolonged clotting time that does NOT correct with mixing study + corrects with excess phospholipid
- **Anti-cardiolipin IgG/IgM:** ELISA ≥40 GPL/MPL or >99th percentile; IgG more clinically significant than IgM
- **Anti-B2GPI IgG/IgM:** ELISA ≥40 units or >99th percentile; domain I-specific assays available; IgG more clinically significant
- **Confirmation:** Must be positive on ≥2 occasions ≥12 weeks apart (transient aPL from infection does not qualify)

**Imaging:**
- Thrombosis: Doppler ultrasound (DVT), CT-PA (PE), MRI/MRA (stroke), echocardiography (Libman-Sacks)
- Placenta: pathology showing placental infarction, avascular villi, spiral artery thrombosis

### Treatment

**Thrombotic APS (indefinite anticoagulation):**
- **Warfarin (VKA) target INR 2.0-3.0:** First-line for venous APS; superior to NOACs (TRAPS trial: rivaroxaban vs. warfarin in triple-positive APS — rivaroxaban doubled arterial thrombosis risk)
- **INR 2.5-3.5:** For arterial APS (stroke, TIA, MI) or recurrent thrombosis on standard INR
- **NOACs (rivaroxaban, dabigatran, apixaban):** NOT recommended for high-risk aPL profiles; RAPS trial (rivaroxaban non-inferior in venous APS for primary outcomes but increased risk in triple-positive); avoid in triple-positive or LA-positive patients
- **Aspirin 75-100 mg/day:** Added to warfarin for arterial APS; or monotherapy for primary thromboprophylaxis in asymptomatic aPL positivity

**Obstetric APS:**
- **LMWH (prophylactic doses) + aspirin 75-100 mg/day** throughout pregnancy and 6-12 weeks post-partum
- Full-dose LMWH for prior thrombotic APS
- Refractory obstetric APS: IVIG, hydroxychloroquine, low-dose prednisone (evidence limited)
- Pravastatin: under investigation for obstetric APS (anti-inflammatory and anti-thrombotic effects)

**Catastrophic APS (CAPS):**
- **Immediate anticoagulation** (heparin IV → LMWH) — mainstay
- **High-dose corticosteroids** (methylprednisolone 500-1000 mg/day × 3 days then oral taper) — for immune component and adrenal insufficiency
- **IVIG** (2 g/kg over 5 days) — immunomodulation; removal of aPL
- **Plasmapheresis** — aPL removal + fresh frozen plasma replacement
- **Eculizumab** (anti-C5; off-label): case series support for refractory CAPS — blocks terminal complement
- **Rituximab** (anti-CD20; off-label): depletes aPL-producing B cells; used for refractory CAPS and chronic thrombocytopenia

**Secondary prophylaxis and risk reduction:**
- **Hydroxychloroquine (HCQ):** Reduces aPL titers and thrombotic risk in all SLE+aPL patients; reduces aPL levels in primary APS; recommended broadly
- **Statin therapy:** Modulates endothelial activation and aPL-mediated TF expression
- **Estrogen avoidance:** Combined OCP contraindicated in APS; progesterone-only or IUD preferred
- **Treat modifiable CV risk factors:** BP control, smoking cessation, weight loss

## Connections

- `connects-to` → **[Beta-2 Glycoprotein I](../../03-molecular/beta2-glycoprotein-1/README.md)** — Anti-B2GPI IgG (domain I-specific; R39-R43 epitope) are the highest-risk pathogenic antibody in APS; B2GPI on phospholipid surfaces is the cofactor for anti-cardiolipin binding; triple aPL positivity (LA + aCL + anti-B2GPI) confers >10% annual thrombotic risk.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — APS is driven by IgG antiphospholipid antibodies (anti-B2GPI IgG, anti-cardiolipin IgG, lupus anticoagulant); IgG titers correlate with thrombotic risk; NOACs (rivaroxaban, dabigatran) are inferior to warfarin in APS (TRAPS trial); FcRn inhibitors under investigation.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Complement activation is central to APS thrombosis: anti-B2GPI → C3b deposition → C5a → neutrophil/platelet priming and TF expression; C5 inhibition (eculizumab) is used off-label for catastrophic APS (CAPS; ~37% mortality) refractory to anticoagulation and plasmapheresis.
- `connects-to` → **[Systemic Lupus Erythematosus](../../07-system/systemic-lupus-erythematosus/README.md)** — Secondary APS occurs in ~30% of SLE patients with persistent aPL; SLE+APS patients have higher stroke/DVT risk than either condition alone; hydroxychloroquine is recommended in all SLE+aPL patients; the 2023 ACR/EULAR APS classification criteria incorporate SLE as a risk modifier.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — APS causes recurrent DVT/PE in young adults; triple-positive aPL (LA + aCL + anti-B2GPI) confers >10% annual VTE risk; warfarin INR 2-3 is superior to DOACs in APS (TRAPS: rivaroxaban doubled arterial event risk vs. warfarin in triple-positive patients); indefinite anticoagulation recommended.
- `connects-to` → **[Inherited Thrombophilia](../inherited-thrombophilia/README.md)** — APS and inherited thrombophilias (FV Leiden, prothrombin G20210A, protein C/S or AT deficiency) both cause recurrent VTE in young adults; co-existing aPL with thrombophilic mutations compounds risk multiplicatively; test for both in young patients with unexplained DVT/PE.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Antiphospholipid antibodies turn the endothelium prothrombotic: anti-β2GPI immune complexes engage endothelial TLR4 → NF-κB → tissue factor, converting the vessel lining from anticoagulant to clot-promoting — one of three converging hits driving APS thrombosis.
- `connects-to` → **[Stroke](../stroke/README.md)** — Antiphospholipid syndrome is a leading cause of stroke in the young: arterial APS produces ischemic stroke and TIA, so aPL testing is mandatory in stroke under 50, and arterial APS is anticoagulated to a higher INR (2.5-3.5), with warfarin beating DOACs.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — Half of APS is obstetric: antiphospholipid antibodies injure the placenta through both decidual-vessel thrombosis and direct, complement-(C5a)-mediated trophoblast damage, causing recurrent miscarriage, fetal loss, and pre-eclampsia — treated with LMWH plus low-dose aspirin.
- `connects-to` → **[Heparin-Induced Thrombocytopenia](../heparin-induced-thrombocytopenia/README.md)** — APS and HIT are antibody-mediated acquired thrombophilias that clot despite thrombocytopenia: APS antiphospholipid antibodies and HIT anti-PF4 IgG each activate platelets and endothelium via Fc engagement, threatening arteries and veins; both can be catastrophic.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Platelets are central effectors in antiphospholipid syndrome: anti-β2GPI antibodies cluster on the platelet surface and, with complement, activate it via GPIbα/FcγRIIA → aggregation and thrombosis; mild thrombocytopenia is common, and the platelet is the aspirin target.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — APS injures the heart: antiphospholipid antibodies cause Libman-Sacks nonbacterial valvular vegetations (especially mitral) that can embolize or need surgery, accelerate coronary thrombosis, and in catastrophic APS produce myocardial thrombotic microangiopathy.
- `connects-to` → **[Disseminated Intravascular Coagulation](../disseminated-intravascular-coagulation/README.md)** — Catastrophic antiphospholipid syndrome can resemble DIC: it floods small vessels with thrombi causing multi-organ failure, but unlike DIC it is antibody-driven with preserved clotting factors—so anticoagulation plus immunosuppression, not factor replacement, treats it.
- `connects-to` → **[Immune Thrombocytopenia](../immune-thrombocytopenia/README.md)** — Antiphospholipid syndrome pairs thrombosis with thrombocytopenia, a distinguishing clue: unlike isolated ITP, the low platelets accompany a prothrombotic state, so clots and a moderately low count plus lupus anticoagulant point to APS, not simple immune thrombocytopenia.
- `connects-to` → **[Sjögren's Syndrome](../sjogrens-syndrome/README.md)** — Antiphospholipid syndrome often arises secondary to autoimmune disease like Sjögren's and lupus: the same loss of tolerance that produces anti-Ro or ANA can generate antiphospholipid antibodies, so thrombosis or pregnancy loss in such patients warrants APS testing.
- `connects-to` → **[Thrombotic Thrombocytopenic Purpura](../thrombotic-thrombocytopenic-purpura/README.md)** — APS and TTP are both thrombotic microangiopathies: catastrophic APS (CAPS) mimics TTP with multi-organ microthrombi, but APS is driven by antiphospholipid antibodies and TTP by ADAMTS13 deficiency—antibody testing separates these clotting emergencies.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Antiphospholipid syndrome accelerates arterial disease beyond venous clots: the antibodies activate endothelium and platelets, promoting atherosclerosis and arterial thrombosis—so APS causes cardiovascular events in young patients, not just venous thromboembolism.
- `connects-to` → **[Migraine](../migraine/README.md)** — Migraine is a common neurological feature of antiphospholipid syndrome: antiphospholipid antibodies are associated with migraine and other neuro symptoms, and severe headache in a young patient with clots or miscarriage should prompt APS testing.
- `connects-to` → **[Thrombin](../../03-molecular/thrombin/README.md)** — Antiphospholipid syndrome tips coagulation toward thrombin: antiphospholipid antibodies activate endothelium, platelets and complement and impair natural anticoagulants, so thrombin generation runs unchecked—driving the venous and arterial clots that define the disease.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — Antiphospholipid syndrome is driven by autoreactive B cells: they produce the antiphospholipid antibodies (against beta-2-glycoprotein I and cardiolipin) that cause clotting and pregnancy loss, so B-cell-directed therapy like rituximab is explored for refractory cases.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Antiphospholipid syndrome is a leading treatable cause of recurrent pregnancy loss: antibodies injure the placenta through thrombosis and complement, so obstetric APS—miscarriage, stillbirth, preeclampsia—is managed with aspirin and heparin to protect the pregnancy.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — The skin flags antiphospholipid syndrome: livedo reticularis—a netlike purple mottling—is a classic sign, and skin ulcers or digital gangrene can appear when small-vessel clots block flow, so dermatologic clues often precede a major thrombotic event.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — APS attacks the kidney as APS nephropathy: clots in glomerular capillaries and small renal arteries cause a thrombotic microangiopathy with hypertension and declining function, a renal manifestation distinct from the immune-complex nephritis of lupus.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Neutrophils help APS clot through NETosis: antiphospholipid antibodies prime neutrophils to cast DNA extracellular traps that scaffold thrombi and activate platelets and complement, so this neutrophil pathway links autoimmunity to the syndrome's clotting.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — Antiphospholipid syndrome scars the glomerulus: a thrombotic microangiopathy clots the kidney's tiny vessels (APS nephropathy), causing hypertension and kidney impairment distinct from the immune-complex lupus nephritis it can accompany.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement turns antiphospholipid antibodies into thrombosis and miscarriage: the antibodies activate complement (C3 and beyond) on cells and placenta, so complement drives both the clotting and the pregnancy loss—and blocking it helps catastrophic APS.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Antiphospholipid syndrome is sustained by T-helper cells: they license B cells to produce the anti-beta2-glycoprotein-I antibodies that define the disease, so the autoimmune help behind the autoantibodies is a target for deeper therapy.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Clotting needs calcium, the cofactor APS exploits: the coagulation cascade APS tips toward thrombosis depends on calcium to anchor clotting factors to phospholipid membranes, the very surfaces the antiphospholipid antibodies target.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — APS strikes the brain through clots: antiphospholipid antibodies promote arterial thrombosis that causes stroke in the young, plus migraine, seizures and cognitive decline, making the brain one of the syndrome's most consequential targets.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — APS endangers the lungs with clots: antiphospholipid antibodies drive pulmonary emboli and, in catastrophic APS, widespread small-vessel thrombosis that can flood the lungs and cause respiratory failure.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — APS can clot the adrenal glands: thrombosis of their veins triggers hemorrhagic infarction, and bilateral adrenal failure—presenting as an Addisonian crisis—is a recognized, life-threatening way the syndrome announces itself.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — APS clots starve tissues of oxygen: by blocking arteries and veins—and, in catastrophic APS, the small vessels of many organs at once—the antibodies cause the ischemic infarcts that damage brain, kidney, and limbs.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — APS is sustained by plasma cells: these antibody factories pour out the anti-β2-glycoprotein-I antibodies that drive the clotting, so therapies aimed at B cells and plasma cells seek to shut the autoantibody supply off.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — APS is mapped by imaging: CT and MRI photons find its strokes, pulmonary emboli and deep-vein clots, and brain MRI reveals the silent infarcts behind its cognitive and neurological toll.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — APS clots the liver's veins: hepatic vein thrombosis (Budd-Chiari) and portal vein clots are among its unusual-site events, congesting and scarring the organ.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — APS damages vessels through mTOR: the antibodies activate this growth pathway in the vessel lining, driving the proliferative vasculopathy of APS nephropathy that mTOR inhibitors like sirolimus may slow.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows APS clots are bland: the vessels fill with platelet-fibrin thrombi without the inflammatory cell infiltrate of a vasculitis, the hallmark of an antibody-driven clotting disease rather than a vessel-wall inflammation.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — APS can suddenly blind: retinal artery and vein occlusions and ischemic optic neuropathy from the clotting tendency can steal vision, sometimes as the first sign of the syndrome.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — The spleen takes its share of APS clots: splenic infarction from thrombosed vessels causes left-upper-abdomen pain and is one of the abdominal-organ infarcts that mark widespread, sometimes catastrophic, disease.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — APS is defined by three antibodies: lupus anticoagulant, anticardiolipin, and anti-β2-glycoprotein-I, which paradoxically prolong clotting tests in the lab while driving thrombosis in the body — the serology that, with a clot or loss, makes the diagnosis.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — APS clots strike the brain young: it is a major cause of stroke and cerebral venous thrombosis in the under-50s, and beyond frank infarcts the antibodies are tied to cognitive impairment, seizures, and chorea.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — The antibodies can turn on the red cells: APS, especially with lupus, causes Coombs-positive autoimmune hemolytic anemia, and in its catastrophic form a microangiopathy shreds erythrocytes as clots fill the small vessels.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Clots can starve the bone: APS causes avascular necrosis, classically of the femoral head, when microthrombi cut off the blood supply to bone, collapsing the joint and adding orthopedic ruin to its vascular toll.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — It scars the heart's valves and muscle: APS drives Libman-Sacks endocarditis, sterile thrombotic vegetations on the valves, and coronary microthrombi that injure cardiomyocytes, a cardiac face beyond the large-vessel clots.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Catastrophic APS can infarct the gut: when clots storm the small vessels of many organs at once, mesenteric thrombosis starves the bowel into ischemia and infarction, part of the multi-organ failure that makes the catastrophic form so lethal.
- `connects-to` → **[Protein C](../../03-molecular/protein-c/README.md)** — The antibodies sabotage a key brake on clotting: they interfere with the activated protein C pathway, creating an acquired APC resistance that, alongside their many other hits, tips the blood toward thrombosis.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — The antibodies switch on the clot-starters: binding β2-glycoprotein I on monocytes and macrophages, they drive these cells to express tissue factor, a central way antiphospholipid antibodies ignite thrombosis.
- `connects-to` → **[Pulmonary Arterial Hypertension](../pulmonary-arterial-hypertension/README.md)** — Old clots can choke the lung's circulation: recurrent pulmonary emboli in APS may organize into chronic thromboembolic pulmonary hypertension, the scarred, narrowed arteries straining the right heart.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — The autoantibody switches cells into a clotting mode: anti-β2-glycoprotein-I antibodies signal through TLR4 on endothelial cells and monocytes, driving tissue factor and the prothrombotic activation behind APS thrombosis.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — It scars the heart valves: APS causes Libman-Sacks endocarditis with sterile valve vegetations, and that valve damage plus microthrombi in the myocardium can drift toward heart failure.
- `connects-to` → **[Atypical HUS](../ahus/README.md)** — Catastrophic APS becomes a thrombotic microangiopathy: in its fulminant form, widespread small-vessel clotting and organ failure overlap atypical HUS, a complement-amplified emergency that must be told apart from it.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — The antibodies switch endothelium to clot mode through NF-κB: antiphospholipid antibodies signal via TLR4 to activate NF-κB in endothelial cells and monocytes, driving the tissue factor expression that makes APS relentlessly prothrombotic.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — It clots the kidney's small vessels: APS nephropathy is a thrombotic microangiopathy of the renal microcirculation that, with recurrent renal vein or artery thrombosis, can erode kidney function into chronic kidney disease.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — It can spark seizures directly: beyond stroke, antiphospholipid antibodies are linked to epilepsy through microthrombi and possible direct binding to neuronal tissue, one of the disease's range of neurological manifestations.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Infection can ignite its deadliest form: catastrophic antiphospholipid syndrome — widespread small-vessel thrombosis and multiorgan failure — is frequently triggered by infection and clinically overlaps with sepsis.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — It reaches the mind as well as the vessels: cerebral microthrombi and direct antibody effects contribute to cognitive impairment and depression in APS, beyond the burden of a chronic relapsing thrombotic disease.
- `connects-to` → **[Ovarian Cancer](../ovarian-cancer/README.md)** — Cancer can drive the antibodies: antiphospholipid antibodies and thrombosis can arise as a paraneoplastic phenomenon, so a new APS-like clotting state — particularly with adenocarcinomas like ovarian cancer — prompts a malignancy search.
- `connects-to` → **[Alzheimer's Disease](../alzheimers-disease/README.md)** — Repeated small clots erode cognition: recurrent cerebral microthrombi and strokes in antiphospholipid syndrome cause multi-infarct vascular cognitive impairment that overlaps with and accelerates Alzheimer-type dementia.
- `connects-to` → **[Multiple Sclerosis](../multiple-sclerosis/README.md)** — It can masquerade as demyelination: the white-matter lesions and neurological deficits of antiphospholipid syndrome can mimic multiple sclerosis, an important differential since the treatments diverge sharply.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Its clots starve the skin: small-vessel thrombosis in antiphospholipid syndrome causes livedo, leg ulcers and digital ischemia that heal poorly as occluded vessels deprive the tissue of blood.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It clots the veins draining the gut and liver: antiphospholipid syndrome causes hepatic vein thrombosis (Budd-Chiari) and mesenteric thrombosis with bowel ischaemia, threatening the abdominal organs.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Beyond stroke it disturbs the brain directly: antiphospholipid syndrome causes chorea, cognitive dysfunction, transverse myelitis and seizures, neurological features distinct from its frank thrombotic strokes.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Recurrent clots and pregnancy loss breed worry: the threat of unpredictable thrombosis, miscarriage and the demands of lifelong anticoagulation in antiphospholipid syndrome foster chronic health anxiety.
- `connects-to` → **[Immune System](../immune-system/README.md)** — It is an autoimmune clotting disease: antiphospholipid antibodies — lupus anticoagulant, anti-cardiolipin and anti-β2-glycoprotein-I — activate platelets, endothelium and complement to drive its thromboses and pregnancy loss.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It is written on the skin: livedo reticularis is a hallmark, with skin ulcers, splinter haemorrhages and digital gangrene reflecting the small-vessel thrombosis of antiphospholipid syndrome.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — It scars the heart valves and arteries: antiphospholipid syndrome causes Libman-Sacks non-bacterial valvular vegetations and coronary thrombosis, adding cardiac disease to its accelerated atherosclerosis.
- `connects-to` → **[Renal System](../renal-system/README.md)** — APS nephropathy attacks the kidney: thrombotic microangiopathy in renal arterioles plus renal artery or vein thrombosis drives hypertension and progressive renal impairment.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It throws clots to the lungs: recurrent pulmonary embolism and, in catastrophic APS, diffuse alveolar haemorrhage and chronic thromboembolic pulmonary hypertension can result.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Adrenal vein thrombosis can trigger bilateral adrenal infarction and haemorrhage — a recognised antiphospholipid cause of acute primary adrenal insufficiency.
- `connects-to` → **[Warfarin](../../../03-medicine/01-modern/09-hematology/warfarin/README.md)** — Lifelong anticoagulation is its mainstay: warfarin at INR 2-3 prevents recurrent thrombosis in APS and outperforms direct oral anticoagulants, which are avoided especially in triple-antibody-positive disease.
- `connects-to` → **[Aspirin](../../../03-medicine/01-modern/04-cardio/aspirin/README.md)** — Low-dose aspirin protects pregnancy and arteries: combined with heparin it prevents obstetric APS losses, and it is used for primary prevention in asymptomatic antiphospholipid-antibody carriers.
- `connects-to` → **[Epstein-Barr Virus](../../../02-pathogen/01-viruses/epstein-barr-virus/README.md)** — Infection can raise the antibodies: transient antiphospholipid antibodies appear after Epstein-Barr and other infections through molecular mimicry, usually without thrombosis, a key cause of false-positive testing.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — It clots arteries, not just veins: APS uniquely causes both venous and arterial thrombosis — stroke, MI and limb ischaemia — and accelerates atherosclerosis of the arterial wall through antibody-driven endothelial activation.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Biologics rescue catastrophic disease: rituximab and the complement inhibitor eculizumab, with hydroxychloroquine as an antithrombotic adjunct, are used in refractory and catastrophic antiphospholipid syndrome beyond standard anticoagulation.
- `connects-to` → **[Endocardium](../../05-tissue/endocardium/README.md)** — It scars the heart valves: APS causes Libman-Sacks endocarditis, sterile fibrin-platelet vegetations on the valve endocardium that can embolise to the brain or require valve surgery.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — It clots and bleeds the lung: antiphospholipid syndrome causes pulmonary embolism and, in catastrophic APS, diffuse alveolar haemorrhage—two ways its prothrombotic immunity injures the alveolar bed.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — A virus that mimics it: severe COVID-19 induces antiphospholipid antibodies and a complement-driven prothrombotic state resembling antiphospholipid syndrome, though usually transient.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — It clots the liver's veins: antiphospholipid syndrome causes hepatic and portal vein thrombosis (Budd-Chiari), congesting the hepatic lobule and threatening liver failure.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — It clots the coronary arteries: antiphospholipid syndrome causes myocardial infarction in young patients and microthrombi within the myocardium, a cardiac face beyond its Libman-Sacks valve disease.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Where the autoantibodies form: the anti-β2-glycoprotein-I and anticardiolipin antibodies driving APS arise from germinal-centre B-cell responses, which is why B-cell depletion is tried in refractory disease.
- `connects-to` → **[NMO](../nmo/README.md)** — Clustering autoimmunity: antiphospholipid syndrome co-occurs with other autoantibody diseases including neuromyelitis optica and lupus, reflecting a shared tendency to break B-cell tolerance.
- `connects-to` → **[Polycythemia Vera](../polycythemia-vera/README.md)** — Unusual-site thrombosis workup: antiphospholipid syndrome and JAK2-mutant myeloproliferative neoplasms like polycythaemia vera are both sought in Budd-Chiari and cerebral-vein thrombosis, two acquired causes of clots in odd places.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Osteonecrosis: antiphospholipid microthrombi—and the corticosteroids often used with it—starve the blood supply to bone, causing avascular necrosis (osteonecrosis) of the femoral head and other cortical bone.
- `connects-to` → **[Systemic Sclerosis](../systemic-sclerosis/README.md)** — Overlapping connective-tissue autoimmunity: antiphospholipid antibodies and a thrombotic vasculopathy occur in systemic sclerosis and other connective-tissue diseases, compounding their own microvascular injury.
- `connects-to` → **[Von Willebrand Factor](../../03-molecular/von-willebrand-factor/README.md)** — Endothelial activation: antiphospholipid antibodies activate endothelium to release von Willebrand factor, promoting the platelet adhesion that contributes to APS thrombosis.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — eNOS inhibition: antiphospholipid antibodies suppress endothelial nitric oxide synthase, cutting the vasodilator, antithrombotic nitric oxide that normally protects the vessel wall in APS.
- `connects-to` → **[Fibrinogen](../../03-molecular/fibrinogen/README.md)** — Clot substrate: the thrombin generation driven by antiphospholipid antibodies converts fibrinogen to fibrin, building the venous and arterial clots that define the syndrome.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — NETosis-driven thrombosis: antiphospholipid antibodies prime neutrophils to release extracellular traps rich in S100A8/A9, a key thrombo-inflammatory mechanism propagating clots in antiphospholipid syndrome.
- `connects-to` → **[PF4](../../03-molecular/pf4/README.md)** — Platelet activation: antiphospholipid antibodies activate platelets to release PF4 and procoagulant granules, lowering the threshold for the arterial and venous thrombosis of APS.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Vasculopathy: aPL-activated endothelium releases endothelin-1, whose vasoconstriction adds to the non-inflammatory intimal proliferation and organ ischaemia of antiphospholipid-associated vasculopathy.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — aPL antibodies activate complement, and C5a acting on C5aR1 drives both the thrombosis and the placental injury of APS—the basis for complement blockade (eculizumab) in catastrophic antiphospholipid syndrome.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — aPL antibodies bind β2-glycoprotein-1 on monocytes and, alongside CCL2-driven recruitment, induce the tissue-factor expression that ignites the thrombin generation central to antiphospholipid thrombosis.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Antiphospholipid antibodies impair trophoblast VEGF signaling and placental angiogenesis, producing the defective placentation that underlies the recurrent pregnancy loss and pre-eclampsia of obstetric APS.
- `connects-to` → **[BAFF](../../03-molecular/baff/README.md)** — BAFF supports the autoreactive B cells that produce the anti-β2-glycoprotein-I and anticardiolipin antibodies defining APS, the humoral origin of the disease and a rationale for B-cell-directed therapy in refractory cases.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Antiphospholipid antibodies binding β2-glycoprotein-I on trophoblast trigger caspase-3-mediated apoptosis and impair invasion, a direct cellular mechanism of the placental failure in obstetric APS beyond thrombosis.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Particular HLA class II alleles predispose to producing antiphospholipid antibodies by favoring presentation of β2-glycoprotein-I peptides to helper T cells, linking the genetic risk to the breaking of tolerance.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Anti-β2GPI antibodies activate endothelial PI3K-AKT-mTOR signaling (mTOR already mapped), driving the intimal hyperplasia of APS vasculopathy and nephropathy that mTOR inhibitors like sirolimus can treat.
- `connects-to` → **[TNF-α (Tumor Necrosis Factor-alpha)](../../03-molecular/tnf-alpha/README.md)** — TNF-α is a key mediator of the placental inflammation and thrombosis of obstetric antiphospholipid syndrome, linking the autoantibodies to recurrent fetal loss.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Antiphospholipid antibodies engage TLR4 (already mapped) to activate the NLRP3 inflammasome and IL-1β in monocytes and endothelium, amplifying the thrombo-inflammatory state of APS.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — Anti-β2-glycoprotein-1 antibodies (β2GPI and TLR4 mapped) signal through MyD88 to NF-κB (mapped) in endothelium and monocytes, inducing the tissue factor that drives the prothrombotic state of APS.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Serotonin released from antibody-activated platelet dense granules promotes further aggregation and vasoconstriction, propagating the thrombosis of antiphospholipid syndrome.
- `connects-to` → **[Thrombopoietin](../../03-molecular/thrombopoietin/README.md)** — Thrombopoietin sets the platelet mass available for thrombus formation, relevant to both the thrombocytopenia and the thrombosis that characterize antiphospholipid syndrome.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — Antiphospholipid antibodies engaging β2-glycoprotein-1 (mapped) on endothelium, platelets and monocytes activate ERK-MAPK, inducing tissue factor and the prothrombotic phenotype of APS.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — aPL signaling recruits PI3K (PIK3CA) upstream of the AKT-mTOR axis (AKT and mTOR mapped) that drives endothelial activation and the vasculopathy of antiphospholipid syndrome.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 amplifies the monocyte and endothelial inflammatory response to antiphospholipid antibodies, contributing to APS thromboinflammation.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling transduces the inflammatory cytokine response of monocytes and endothelium activated by antiphospholipid antibodies in APS.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — DNA within antiphospholipid-antibody-triggered neutrophil extracellular traps engages cGAS-STING, linking NET-driven inflammation to the thrombosis of APS.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling contributes to the placental dysfunction and decidual remodeling underlying the pregnancy morbidity of obstetric APS.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK1/2-STAT cytokine signaling (IL-6-STAT3 already mapped) amplifies the endothelial and monocyte inflammatory activation that drives the thrombosis of antiphospholipid syndrome.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling, reflecting the type-I interferon signature of APS, shapes the immune activation underlying antiphospholipid syndrome.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO downstream of antiphospholipid-antibody-triggered PI3K-AKT-mTOR signaling (AKT, PIK3CA, and mTOR already mapped) regulates the endothelial activation balance in antiphospholipid syndrome.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the platelet-activation and mTOR-linked endothelial signaling that drive the thrombosis of antiphospholipid syndrome.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of β2GPI-antibody engagement of platelet and endothelial receptors contributes to the prothrombotic activation of antiphospholipid syndrome.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α in the ischemic placenta contributes to the pregnancy morbidity of obstetric antiphospholipid syndrome.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked endothelial metabolic signaling modulates the vascular homeostasis relevant to the thrombosis of antiphospholipid syndrome.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the endothelial, platelet, and trophoblast responses relevant to antiphospholipid syndrome.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven monocyte recruitment contributes to the inflammation-linked thrombosis of antiphospholipid syndrome.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the autoreactive immune response of antiphospholipid syndrome.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the endothelial and leukocyte interactions of the thrombo-inflammation of antiphospholipid syndrome.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammasome activation participates in the prothrombotic and placental inflammation of antiphospholipid syndrome.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the endothelial and immune activation of antiphospholipid syndrome.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the thromboinflammatory immune response of antiphospholipid syndrome.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the T-cell help driving the anti-β2GPI autoantibody response of antiphospholipid syndrome.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — B-cell depletion: refractory and catastrophic antiphospholipid syndrome is treated with the anti-CD20 antibody rituximab to deplete the B cells producing anti-β2GPI antibodies (immunoglobulin G already mapped), a targeted immunotherapy beyond anticoagulation.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell help: IL-2-driven expansion of the T cells that help autoreactive B cells sustains the antiphospholipid antibody response, and impaired regulatory-T-cell control contributes to the persistence of the autoimmunity.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — Autoreactive survival: anti-apoptotic BCL-2 family proteins prolong the survival of the autoreactive B cells producing antiphospholipid antibodies, helping the autoimmune clone persist despite the normal checkpoints that should delete it.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Pregnancy morbidity: antiphospholipid syndrome causes recurrent pregnancy loss and placental thrombosis, and the oestrogen-rich prothrombotic state of pregnancy (and of oestrogen contraception) heightens the thrombotic risk it confers.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Cardiac thrombosis: antiphospholipid syndrome causes coronary thrombosis, myocardial infarction and Libman-Sacks valve lesions, and troponin elevation marks the myocardial injury of these cardiac thrombotic manifestations.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Microangiopathic haemolysis: catastrophic antiphospholipid syndrome and its thrombotic microangiopathy fragment red cells and, with autoimmune haemolysis, lower haemoglobin, adding a haematological dimension to the widespread thrombosis.
- `connects-to` → **[ADAMTS13](../../03-molecular/adamts13/README.md)** — Microangiopathy differential: the thrombotic microangiopathy of catastrophic antiphospholipid syndrome occurs with normal ADAMTS13 (von Willebrand factor already mapped), distinguishing its antibody-driven mechanism from thrombotic thrombocytopenic purpura.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Thromboxane-prostacyclin balance: antiphospholipid antibodies shift the endothelial and platelet (already mapped) prostaglandin balance toward the prothrombotic thromboxane, part of why low-dose aspirin is used in antiphospholipid syndrome.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative antigenicity: oxidative stress, to which xanthine oxidase contributes, generates the oxidised beta-2-glycoprotein-1 (already mapped) that is the key target of the pathogenic antibodies, linking oxidation to the antigenicity of antiphospholipid syndrome.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — B-cell autoantibody help: IL-4 and the Th2 response support the B cells (BAFF and CD20 already mapped) that produce the anti-β2-glycoprotein-1 and anticardiolipin antibodies driving antiphospholipid syndrome.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 humoral arm: IL-13, with IL-4 (already mapped), completes the type-2 cytokine support for the autoantibody-producing B cells of antiphospholipid syndrome, the humoral autoimmunity behind the pathogenic antibodies.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Platelet zinc and coagulation: zinc released from the activated platelets (already mapped) promotes the contact pathway and fibrin formation (fibrinogen and thrombin already mapped), adding to the prothrombotic state of antiphospholipid syndrome.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Autoimmune signature: the type-I interferon of the autoimmune (lupus already mapped) background promotes the endothelial (already mapped) prothrombotic state and the autoantibody production of antiphospholipid syndrome.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Checkpoint tolerance: the PD-1 checkpoint and peripheral-tolerance mechanisms, when dysfunctional, permit the anti-β2-glycoprotein-I (already mapped) autoreactivity that drives antiphospholipid syndrome.
- `connects-to` → **[CTLA-4](../../03-molecular/ctla-4/README.md)** — Co-inhibitory checkpoint: CTLA-4, with PD-1 (already mapped), regulates the autoreactive T cells that help the B cells (CD20 and BAFF already mapped) produce the pathogenic antibodies of antiphospholipid syndrome.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Immune-metabolic adipokine: leptin is the adipokine of the immune-metabolic milieu that modulates the thrombo-inflammatory autoimmunity of antiphospholipid syndrome.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic-inflammatory milieu of antiphospholipid syndrome.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the thrombo-inflammatory milieu (IL-6 and TNF already mapped) of antiphospholipid syndrome.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Innate immune modulation: the NK cells (perforin already mapped) are part of the innate immune dysregulation of the thrombo-inflammatory autoimmunity of antiphospholipid syndrome.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 autoimmunity: the IFN-γ of the T cells is the type-II interferon arm (with the type-I interferon already mapped) of the immune dysregulation driving the anti-β2GPI (already mapped) autoantibodies of antiphospholipid syndrome.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the autoimmune response of antiphospholipid syndrome.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation of antiphospholipid syndrome.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the autoimmune response driving the anti-β2GPI (already mapped) autoantibodies of antiphospholipid syndrome.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the autoimmune response of antiphospholipid syndrome.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) whose activation on the anti-β2GPI (already mapped) immune complexes drives the thrombosis of antiphospholipid syndrome.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement/contact regulation: the C1-esterase inhibitor regulates the classical complement and the contact-coagulation systems at the interface driving the thromboinflammation of antiphospholipid syndrome.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Antigen presentation: the dendritic cells present the β2-glycoprotein-1 (already mapped) to the T cells (already mapped), priming the autoantibody response of antiphospholipid syndrome.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Thromboinflammation: osteopontin, released by the activated platelets (already mapped), is a matricellular mediator amplifying the neutrophil (already mapped) and endothelial thromboinflammation of antiphospholipid syndrome.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Haemolytic/thrombotic iron: transferrin, the iron carrier, reflects the disordered iron handling of the haemolysis and the microvascular thrombosis of antiphospholipid syndrome.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Adaptive arm: the cytotoxic T cells (perforin pathway), with the T-helper (already mapped) support of the anti-β2GP1 response, are part of the adaptive-immune dimension of antiphospholipid syndrome.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-thromboinflammatory axis: TSLP, from inflamed endothelium (already mapped) and placental (already mapped) tissue, primes dendritic cells (already mapped) and mast cells (already mapped) and amplifies the Th2/B-cell bias driving the anti-β2GP1 antibody production of APS.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-thrombosis axis: bradykinin, generated by the kallikrein-kinin system activated via the contact pathway on aPL-coated endothelium, amplifies vascular permeability and the prothrombotic milieu of antiphospholipid syndrome.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Haemolytic anaemia support: erythropoietin drives red-cell regeneration to counteract the autoimmune haemolytic anaemia (already mapped) and the thrombotic microangiopathy-driven haemolysis of antiphospholipid syndrome.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell vascular effector: histamine, released by mast cells (already mapped) at sites of aPL-driven vascular inflammation, amplifies endothelial permeability and the prothrombotic cytokine milieu (TNF-α and IL-6 already mapped) of antiphospholipid syndrome.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — ECM remodelling in placenta and vessels: periostin, expressed in the placenta (already mapped) and vascular adventitia under thromboinflammatory injury, modulates the fibrotic remodelling of decidual vessels and contributes to the obstetric morbidity of APS.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian antithrombotic protection: melatonin, via MT1/MT2 receptors on platelets (already mapped) and endothelial cells (already mapped), suppresses the NF-κB-driven (already mapped) prothrombotic cytokine surge and attenuates the nocturnal thrombosis risk of APS.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Androgen thromboinflammation attenuation: testosterone, via androgen receptors on endothelial cells and platelets, attenuates NF-κB and complement-C5 thromboinflammation and reduces the aPL-driven thrombotic risk of APS.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Prothrombotic cytokine amplification: prolactin, via PRLR on endothelial cells and platelets, promotes NF-κB-driven anti-β2GP1 prothrombotic cytokine release and amplifies complement-C5 thromboinflammation of APS.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Complement thromboinflammation suppression: oxytocin, via OXTR on endothelial cells and platelets, suppresses NF-κB and complement-C5 thromboinflammation and attenuates aPL-driven placental injury of APS.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — APS vasopressin: vasopressin, via V1a receptors on platelets (already mapped) and endothelial cells (already mapped), promotes prothrombotic platelet activation; vasopressin amplifies NF-κB (already mapped) and complement-C5 (already mapped) thromboinflammatory cascade of APS.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — APS selenium: selenium-dependent GPx suppresses the ROS amplifying NF-κB (already mapped) and complement-C5 (already mapped) endothelial injury in APS; selenium deficiency promotes platelet (already mapped) hyperreactivity and the thromboinflammatory vascular injury of APS.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — APS iodine: iodine-dependent thyroid hormones modulate endothelial cell (already mapped) function and platelet (already mapped) reactivity; hypothyroidism, common in autoimmune patients, amplifies NF-κB (already mapped) thromboinflammation and aPL coagulation risk of APS.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — APS sodium: excess sodium promotes macrophage (already mapped) and neutrophil (already mapped) pro-inflammatory skewing; sodium-induced NF-κB (already mapped) amplifies endothelial-cell (already mapped) and platelet (already mapped) thromboinflammatory cascade of APS.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — APS potassium: potassium regulates endothelial-cell (already mapped) and platelet (already mapped) membrane excitability; potassium dysregulation amplifies NLRP3 (already mapped) and NF-κB (already mapped) and complement-C3 (already mapped) thromboinflammatory cascade in APS.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — APS magnesium: magnesium stabilises endothelial-cell (already mapped) function and attenuates platelet (already mapped) aggregation; magnesium deficiency amplifies NF-κB (already mapped) and thrombin (already mapped) and complement-C5 (already mapped) procoagulant cascade in APS.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — APS copper: copper, via SOD in endothelial cells (already mapped) and macrophages (already mapped), scavenges ROS; copper deficiency amplifies NF-κB (already mapped) and NLRP3 (already mapped) and complement-C3 (already mapped) thromboinflammatory cascade in APS.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — iron-driven ferroptosis in endothelial cells (already mapped) amplifies oxidative stress on platelet (already mapped) activation and complement-C3 (already mapped) deposition; iron excess amplifies NF-κB (already mapped) and thrombin (already mapped) procoagulant cascade in APS.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — phosphorus-driven ATP in platelets (already mapped) and endothelial cells (already mapped) sustains anti-thrombotic signalling; phosphorus deficiency amplifies NF-κB (already mapped) and thrombin (already mapped) and complement-C5 (already mapped) procoagulant cascade in APS.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — nitric oxide from iNOS in endothelial cells (already mapped) and macrophages (already mapped) modulates vascular tone; NO deficiency amplifies thrombin (already mapped) and complement-C5 (already mapped) and NF-κB (already mapped) procoagulant cascade in APS.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — APS carbon: carbon backbone of lipids in platelets (already mapped) and endothelial cells (already mapped) sustains thrombostasis; carbon dysregulation amplifies NF-κB (already mapped) and thrombin (already mapped) and complement-C3 (already mapped) procoagulant cascade in APS.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — APS chloride: chloride channels in endothelial cells (already mapped) and platelets (already mapped) modulate vascular tone; chloride dysregulation amplifies NF-κB (already mapped) and thrombin (already mapped) and complement-C5 (already mapped) thrombotic cascade in APS.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — APS hydrogen: hydrogen via ROS balance in endothelial cells (already mapped) and macrophages (already mapped) modulates oxidative stress; hydrogen excess amplifies NF-κB (already mapped) and thrombin (already mapped) and complement-C3 (already mapped) procoagulant cascade in APS.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — APS sulfur: H2S from sulfur-amino acids in endothelial cells (already mapped) and platelets (already mapped) modulates vascular tone; sulfur deficiency amplifies NF-κB (already mapped) and thrombin (already mapped) and complement-C5 (already mapped) thrombotic cascade in APS.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — APS GLP-1: GLP-1 receptor signalling in macrophages (already mapped) and endothelial cells (already mapped) modulates vascular homeostasis; GLP-1 dysregulation amplifies NF-κB (already mapped) and thrombin (already mapped) and complement-C5 (already mapped) cascade in APS.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — APS angiotensin-II: angiotensin-II in endothelial cells (already mapped) and macrophages (already mapped) promotes vascular inflammation; angiotensin-II excess amplifies NF-κB (already mapped) and thrombin (already mapped) and complement-C5 (already mapped) cascade of APS.

[^miyakis-2006-sydney-aps]: Miyakis S, Lockshin MD, Atsumi T, et al. International consensus statement on an update of the classification criteria for definite antiphospholipid syndrome (APS). *J Thromb Haemost.* 2006;4(2):295-306. [doi:10.1111/j.1538-7836.2006.01753.x](https://doi.org/10.1111/j.1538-7836.2006.01753.x) · [PubMed 16420554](https://pubmed.ncbi.nlm.nih.gov/16420554/)
[^barbhaiya-2023-acreular-aps]: Barbhaiya M, Zuily S, Naden R, et al. The 2023 ACR/EULAR antiphospholipid syndrome classification criteria. *Ann Rheum Dis.* 2023;82(10):1258-1270. [doi:10.1136/ard-2023-224609](https://doi.org/10.1136/ard-2023-224609) · [PubMed 37643823](https://pubmed.ncbi.nlm.nih.gov/37643823/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
