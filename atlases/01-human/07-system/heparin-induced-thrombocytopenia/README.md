---
schema: human-scale-entry/v1
id: heparin-induced-thrombocytopenia
name: Heparin-Induced Thrombocytopenia
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Heparin-induced thrombocytopenia (HIT type 2) is an immune thrombocytopenia from anti-PF4/heparin IgG; platelet activation → paradoxical thrombosis. Stop heparin; switch to argatroban/bivalirudin/fondaparinux; avoid warfarin initially. 4T score guides clinical probability."
aliases: ["HIT", "heparin-induced thrombocytopenia", "HIT type 2", "HITT", "heparin thrombocytopenia", "anti-PF4 antibody", "PF4-heparin antibody", "VITT"]
sources:
  - id: warkentin-2007-hit-review
    type: peer-reviewed
    cite: "Warkentin TE, Greinacher A. Heparin-induced thrombocytopenia: recognition, treatment, and prevention: the Seventh ACCP Conference on Antithrombotic and Thrombolytic Therapy. Chest. 2004;126(3 Suppl):311S-337S."
    doi: "10.1378/chest.126.3_suppl.311S"
    pmid: "15383477"
    url: "https://doi.org/10.1378/chest.126.3_suppl.311S"
  - id: greinacher-2021-vitt-nejm
    type: peer-reviewed
    cite: "Greinacher A, Thiele T, Warkentin TE, et al. Thrombotic thrombocytopenia after ChAdOx1 nCov-19 vaccination. N Engl J Med. 2021;384(22):2092-2101."
    doi: "10.1056/NEJMoa2104840"
    pmid: "33835769"
    url: "https://doi.org/10.1056/NEJMoa2104840"
  - id: linkins-2012-hit-chest
    type: clinical-guideline
    cite: "Linkins LA, Dans AL, Moores LK, et al. Treatment and prevention of heparin-induced thrombocytopenia: Antithrombotic Therapy and Prevention of Thrombosis, 9th ed: American College of Chest Physicians Evidence-Based Clinical Practice Guidelines. Chest. 2012;141(2 Suppl):e495S-e530S."
    doi: "10.1378/chest.11-2303"
    pmid: "22315270"
    url: "https://doi.org/10.1378/chest.11-2303"
cross_links:
  - target: 01-human/03-molecular/pf4
    relation: connects-to
    note: "Anti-PF4/heparin IgG (predominantly IgG4) is the diagnostic antigen of HIT; formed when PF4-heparin complex → neo-antigen → IgG production; ELISA detects anti-PF4/heparin IgG (sensitive, ~97%; not specific); SRA (serotonin release assay) is the confirmatory gold standard."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Anti-PF4/heparin IgG crosslinks FcγRIIA on platelets → Gαq → IP3/DAG → Ca²⁺ → dense granule release (ADP, serotonin) + TXA2 → further platelet activation loop; platelet activation fragments generate procoagulant microparticles → thrombin → arterial and venous thrombosis."
  - target: 01-human/03-molecular/thrombin
    relation: connects-to
    note: "HIT causes paradoxical thrombosis: activated platelets generate procoagulant microparticles → thrombin generation; argatroban (DTI) and bivalirudin block thrombin in HIT; warfarin is contraindicated initially (protein C drops first → warfarin-induced limb gangrene risk)."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "HIT causes paradoxical DVT/PE (venous) and arterial thrombosis (HITT); occurs 5-10 days after heparin exposure; anti-PF4/heparin IgG → platelet activation → thrombin; argatroban, bivalirudin, and fondaparinux replace heparin in HIT; DOACs used for bridging to warfarin."
  - target: 01-human/03-molecular/antithrombin
    relation: connects-to
    note: "UFH and LMWH anticoagulate via AT (heparin binds AT → 1000× accelerated thrombin/FXa inhibition); AT is bypassed by direct thrombin inhibitors (argatroban, bivalirudin) used in HIT; fondaparinux (FXa inhibitor via AT) is an alternative in HIT."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "HIT is driven by a transient IgG against the PF4-heparin complex; this antibody cross-links FcγRIIA on platelets to activate them, so detection rests on an anti-PF4/heparin IgG ELISA confirmed by a serotonin-release assay — and the IgG typically fades within 3-6 months."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Beyond platelets, anti-PF4/heparin IgG activates endothelial cells: PF4 binds endothelial heparan sulfate, and immune-complex engagement induces tissue factor expression, amplifying thrombin generation — why HIT is so intensely prothrombotic despite falling platelet counts."
  - target: 01-human/07-system/inherited-thrombophilia
    relation: connects-to
    note: "HIT is a severe acquired thrombophilia that, unlike most inherited thrombophilias, threatens arteries as well as veins and can take limbs; co-existing inherited thrombophilia or recent VTE further raises the risk of HIT-associated thrombosis."
  - target: 01-human/07-system/pnh
    relation: connects-to
    note: "HIT and PNH are acquired, intensely prothrombotic disorders with opposite mechanisms: HIT is anti-PF4/heparin IgG activating platelets, PNH is complement-mediated hemolysis from GPI-anchor loss; both clot despite platelet consumption and need targeted therapy, not heparin alone."
  - target: 01-human/07-system/antiphospholipid-syndrome
    relation: connects-to
    note: "HIT and antiphospholipid syndrome are antibody-mediated acquired thrombophilias threatening arteries and veins: anti-PF4 IgG and antiphospholipid antibodies each activate platelets and endothelium; both can cause catastrophic multisite thrombosis and avoid reliance on heparin."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Unlike most thrombophilias, HIT causes arterial as well as venous thrombosis: anti-PF4/heparin immune complexes activate platelets and endothelium → arterial 'white clots' causing stroke, MI and limb ischemia; suspected HIT mandates a non-heparin anticoagulant."
  - target: 01-human/07-system/immune-thrombocytopenia
    relation: connects-to
    note: "HIT and immune thrombocytopenia are both antibody-mediated low-platelet states with opposite effects: ITP antibodies destroy platelets and bleed, while HIT's anti-PF4 antibodies activate platelets and clot—so HIT means stopping heparin, not transfusing."
  - target: 01-human/07-system/disseminated-intravascular-coagulation
    relation: connects-to
    note: "HIT and DIC both cause inpatient thrombocytopenia but differ: DIC consumes factors and platelets with prolonged PT/PTT, while HIT activates platelets via antibody with normal clotting times—4T score and anti-PF4 testing distinguish them."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "HIT is the template for vaccine-induced thrombotic thrombocytopenia (VITT) after COVID-19 adenoviral vaccines: both feature anti-PF4 antibodies that activate platelets to cause thrombosis with thrombocytopenia, treated alike with non-heparin anticoagulation and IVIG."
  - target: 01-human/07-system/thrombotic-thrombocytopenic-purpura
    relation: connects-to
    note: "HIT and TTP are both life-threatening thrombocytopenias: HIT is antibody-mediated platelet activation by PF4-heparin complexes causing paradoxical thrombosis, while TTP is ADAMTS13 deficiency forming microthrombi—both drop platelets, but cause and treatment differ."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement amplifies the prothrombotic immunity of HIT: the IgG-PF4-heparin immune complexes that activate platelets also engage complement, fueling endothelial activation and thrombosis—linking an antibody reaction to heparin with the innate complement cascade."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "HIT is paradoxical—low platelets cause clots, not bleeds: PF4-heparin antibodies activate platelets and endothelium, triggering arterial and venous thrombosis across the cardiovascular system—so heparin is stopped and a non-heparin anticoagulant started."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages execute the paradox of HIT: Fc receptors on macrophages and platelets bind PF4-heparin-IgG immune complexes, clearing platelets (thrombocytopenia) while activating them to clot—so the same antibody both lowers the count and causes thrombosis."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Complement amplifies the thrombosis of HIT and its cousin VITT: PF4-antibody complexes activate complement on platelets and endothelium, boosting clot formation—so complement and the anti-PF4 antibody together explain why HIT clots despite a falling platelet count."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Pulmonary embolism is a major HIT complication: the paradoxical clotting strikes veins, throwing clots to the lung, so a heparin-treated patient with a falling platelet count and new dyspnea needs heparin stopped and a non-heparin anticoagulant urgently."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "HIT is driven by B-cell antibodies: B cells rapidly make IgG against platelet-factor-4/heparin complexes, and these antibodies cross-link platelet Fc receptors to trigger the paradoxical clotting—so the culprit is a transient, T-independent antibody response."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "The spleen helps cause HIT's low platelet count: its macrophages clear antibody-coated platelets from the circulation, so even as clots form, platelet numbers fall—the 'thrombocytopenia with thrombosis' paradox that defines the syndrome."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils amplify the thrombosis of HIT: activated by anti-PF4 immune complexes, they release neutrophil extracellular traps (NETs) that provide a scaffold for clot formation—linking HIT to the same NET-driven immunothrombosis seen in VITT and severe COVID."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "The serotonin release assay confirms HIT: activated platelets dump their serotonin stores, so measuring heparin-dependent serotonin release from donor platelets is the gold-standard functional test distinguishing true HIT from harmless anti-PF4 antibodies."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "HIT can announce itself in the skin: heparin injection sites may develop painful necrotic lesions from local thrombosis, a recognized skin sign of the paradoxical clotting that defines the syndrome despite falling platelets."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "HIT's anti-PF4/heparin antibodies arise with T-helper-cell support: helper T cells license B cells to produce the pathogenic IgG, an unusually rapid immune response that can recur on heparin re-exposure."
  - target: 01-human/03-molecular/fibrinogen
    relation: connects-to
    note: "HIT is a paradoxical clotting storm consuming fibrinogen: the activated platelets generate massive thrombin that converts fibrinogen to fibrin, so a low-platelet state causes thrombosis rather than bleeding—the trap that defines the disease."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "HIT platelets activate through a calcium surge: antibody clustering of platelet Fc receptors triggers calcium influx that drives the granule release and aggregation behind the prothrombotic state—the cellular step that makes HIT dangerous."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "HIT starts when dendritic cells flag PF4-heparin as foreign: heparin reshapes platelet factor 4 into a neo-antigen these sentinels recognize and present, kicking off the rapid immune reaction that turns a blood thinner into a clotting trigger."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "HIT clots can strike the brain: despite the falling platelet count it is a prothrombotic state, causing arterial strokes and cerebral vein thrombosis, so HIT is treated with non-heparin anticoagulants rather than transfusion."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "HIT can destroy the adrenal glands: bilateral adrenal vein thrombosis leads to hemorrhagic infarction and acute adrenal insufficiency, a rare but catastrophic complication of the syndrome's paradoxical clotting."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "HIT chokes tissues of oxygen through thrombosis: clots in arteries and veins block blood flow, causing limb ischemia that can require amputation, so the hypoxic damage—not bleeding—is HIT's central threat."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Once HIT is suspected, imaging hunts the clots: CT and lung scans read in X-ray photons find the pulmonary emboli and limb thromboses that make the syndrome dangerous despite the low platelets."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "HIT clots arteries as well as veins: coronary thrombosis can cause a heart attack, part of the arterial thrombosis that distinguishes this paradoxical, clot-prone low-platelet state."
  - target: 01-human/03-molecular/von-willebrand-factor
    relation: connects-to
    note: "HIT inflames the vessel wall: the immune complexes activate endothelium to release von Willebrand factor, which grabs platelets and amplifies the prothrombotic storm beyond the platelets' own activation."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "HIT's low platelets do not come from a failing marrow: the megakaryocytes keep producing normally, but the antibody-coated platelets are consumed in clots and cleared by the spleen, a destruction rather than a production problem."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "HIT's clotting can strike the kidney: thrombosis of the renal veins or microvasculature, part of the body-wide prothrombotic storm, can cause acute kidney injury even as the platelet count falls."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reveals HIT's trigger: heparin and platelet factor 4 assemble into large ultralarge complexes that the antibodies cross-link on the platelet surface, the molecular scaffolding that ignites the whole prothrombotic cascade."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "HIT is an antibody disease in disguise: IgG against the PF4-heparin complex clusters FcγRIIa on platelets to activate them en masse, the paradoxical immune mechanism that drops the count while driving clots."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "HIT's clots reach the gut's circulation: the prothrombotic storm can seed portal, hepatic, and mesenteric vein thrombosis, threatening the liver and bowel alongside the more familiar limb and lung clots."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "The brain is not spared: HIT can throw clots into cerebral arteries or the venous sinuses, causing strokes and cerebral venous thrombosis that injure neurons — part of why it is so dangerous despite the low platelet count."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "HIT clots the muscular arteries too: 'white clot syndrome' lodges platelet-rich thrombi in the limb arteries lined by smooth muscle, causing acute ischemia and the venous limb gangrene that can cost a leg despite full anticoagulation."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Even the retina's vessels can clot: HIT's prothrombotic state has caused retinal artery and vein occlusions with sudden visual loss, one more unexpected site of the paradoxical thrombosis that defines the syndrome."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Pregnancy complicates the choice of blood thinner: heparins are first-line for pregnancy clots because they don't cross the placenta, so HIT forces a switch to alternatives like fondaparinux, balancing maternal thrombosis against fetal safety."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "HIT clots the arteries too: paradoxically, the activated platelets drive arterial as well as venous thrombosis, so myocardial infarction from coronary occlusion is among its feared events, injuring cardiomyocytes in a patient who is also bleeding-prone."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Dialysis is a setup for HIT: hemodialysis patients are repeatedly exposed to heparin in the circuit, so they are among those who develop the PF4 antibodies, forcing a switch to alternative anticoagulants for their dialysis."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "The clots favor diseased arteries: HIT's arterial thromboses — the so-called white clots — tend to form on atherosclerotic plaque, turning a stable vessel into an acute occlusion of a limb, brain or heart."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "The culprit drug is a body molecule: heparin is naturally made and stored in mast cells, so the anticoagulant that triggers HIT is a pharmaceutical version of a mediator these immune cells release into tissues."
  - target: 01-human/03-molecular/fcrn
    relation: connects-to
    note: "The pathogenic antibody is long-lived: the anti-PF4/heparin IgG that drives HIT is recycled and kept in circulation by FcRn, sustaining the prothrombotic state for weeks after heparin is stopped."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "It hides among the critically ill: sepsis and its consumptive coagulopathy commonly drop platelets in the same patients receiving heparin, a key mimic that must be distinguished from HIT before stopping the drug and switching anticoagulants."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Plasma cells make the dangerous antibody: a rapid B-cell response matures into plasma cells secreting the anti-PF4/heparin IgG that drives HIT, an unusually fast antibody response that can appear within days of heparin exposure."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "The immune complexes light up the vessel wall: PF4-heparin-IgG complexes activate monocytes and endothelium through NF-κB, switching on tissue factor and adhesion molecules that turn HIT into a relentlessly prothrombotic state."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "Unresolved clots can stiffen the lung circulation: the pulmonary emboli thrown by HIT, if incompletely cleared, can organize into chronic thromboembolic pulmonary hypertension, a lasting rise in pulmonary artery pressure."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Large clots can buckle the right heart: a massive pulmonary embolism thrown by HIT acutely overloads the right ventricle into acute cor pulmonale, and HIT itself often arises after cardiac surgery in patients with limited cardiac reserve."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "It strikes the already critically ill: HIT typically develops in post-surgical and intensive-care patients who carry the anemia of chronic disease from their inflammatory state, compounding the hematologic complexity."
  - target: 01-human/07-system/polycythemia-vera
    relation: connects-to
    note: "It joins the differential of thrombosis with an odd platelet count: when clotting coincides with abnormal platelets, myeloproliferative disorders like polycythemia vera are weighed alongside HIT as drivers of an acquired prothrombotic state."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Its clots kill tissue and leave wounds: HIT thrombosis causes heparin-injection-site skin necrosis and limb ischemia that can progress to gangrene and amputation, leaving major wounds to heal."
  - target: 01-human/07-system/ptsd
    relation: connects-to
    note: "A sudden limb-threatening crisis can scar the mind: HIT often strikes critically ill patients, and surviving its abrupt thrombosis, amputation or ICU course can leave post-traumatic stress."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Limb loss and prolonged illness weigh on mood: the disability from HIT-related amputation and the protracted critical illness it accompanies contribute to depression in survivors."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It can necrose the skin at injection sites: HIT classically causes skin lesions ranging from erythematous plaques to frank necrosis where heparin is injected, a recognised marker of the syndrome."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It can infarct both adrenal glands: thrombosis of the adrenal veins in HIT causes bilateral haemorrhagic adrenal infarction, precipitating acute adrenal insufficiency that is easily missed."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A sudden paradoxical clotting crisis breeds worry: the abrupt limb- and life-threatening thrombosis of HIT and the lifelong need to avoid heparin foster chronic health anxiety alongside the PTSD and depression it leaves."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "It is an immune drug reaction at heart: IgG antibodies against platelet factor 4-heparin complexes cross-link platelet FcγRIIa receptors, activating platelets and the clotting cascade despite a falling platelet count."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It often clots the lungs: pulmonary embolism is a frequent thrombotic outcome of HIT, and a rapid intravenous heparin bolus can trigger an acute anaphylactoid reaction with dyspnoea and collapse."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It thromboses unusual sites: HIT can clot the mesenteric and portal veins, causing bowel ischaemia and abdominal pain, and adrenal vein thrombosis can lead to haemorrhagic adrenal infarction."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It clots the brain's vessels: cerebral venous sinus thrombosis and arterial stroke are serious neurological thrombotic complications of HIT."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It clots the renal vessels: renal vein and renal artery thrombosis in HIT cause acute kidney injury."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It can cost a limb: arterial thrombosis in HIT causes acute limb ischaemia and gangrene that may require amputation, the 'white clot syndrome'."
  - target: 03-medicine/01-modern/09-hematology/warfarin
    relation: connects-to
    note: "Warfarin is dangerous early in it: starting warfarin during acute HIT can precipitate venous limb gangrene by dropping protein C, so a non-heparin anticoagulant is used first."
  - target: 01-human/07-system/ahus
    relation: connects-to
    note: "A fellow antibody-driven thrombotic disorder: like atypical HUS, HIT is an antibody-mediated prothrombotic state, here from anti-PF4-heparin immune complexes that activate platelets."
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: connects-to
    note: "Infection can trigger anti-PF4 antibodies: 'spontaneous' or autoimmune HIT, occurring without heparin after infection or orthopaedic surgery, has been linked to bacterial triggers such as Staphylococcus aureus."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "White clots in the arteries: the platelet-activating PF4 antibodies of HIT seed platelet-rich 'white clot' thrombi not only in veins but in arteries, causing limb ischaemia, stroke and acute arterial occlusion."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Cardiac surgery is the danger zone: cardiopulmonary bypass exposes patients to massive heparin doses, making cardiac surgery the highest-incidence setting for HIT, where the antibodies can drive coronary thrombosis and myocardial infarction."
  - target: 01-human/07-system/essential-thrombocythemia
    relation: connects-to
    note: "Opposite counts, shared thrombosis: HIT thromboses while platelets fall as they are consumed by activation, whereas essential thrombocythemia thromboses with a high platelet count — a paradox of platelet number versus platelet activation."
  - target: 01-human/07-system/hemophilia-a
    relation: connects-to
    note: "Opposite poles of haemostasis: heparin-induced thrombocytopenia clots despite falling platelets, while haemophilia A bleeds from absent factor VIII—the thrombosis-versus-bleeding extremes of coagulation."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "Microthrombi reach the kidney: the intense prothrombotic state of HIT can seed microvascular thrombi that impair the renal glomeruli, adding acute kidney injury to its limb and organ thromboses."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "It clots the lungs: HIT's hypercoagulability drives venous thromboembolism and pulmonary embolism, lodging clots in the pulmonary vasculature feeding the alveoli—a leading cause of HIT death."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Splanchnic thrombosis: HIT can clot the portal and mesenteric veins, congesting the hepatic lobules and threatening bowel infarction—an under-recognised but dangerous site of HIT thrombosis."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "An unusual antibody response: HIT's anti-PF4/heparin IgG arises within days and is short-lived, reflecting a largely extrafollicular B-cell response that bypasses durable germinal-centre memory—why the antibodies wane within months."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "Cancer, clots and heparin: highly thrombogenic cancers like pancreatic adenocarcinoma (Trousseau syndrome) demand heavy heparin anticoagulation, the very setting in which heparin-induced thrombocytopenia can dangerously compound the clotting."
  - target: 01-human/03-molecular/protein-c
    relation: connects-to
    note: "Why warfarin is dangerous in HIT: starting warfarin during acute HIT depletes protein C faster than the procoagulant factors, tipping into venous limb gangrene—so warfarin is withheld until the platelet count recovers."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Limb-threatening ischaemia: HIT's arterial thromboses and venous limb gangrene starve the extremities, damaging peripheral nerves with ischaemic neuropathy and sometimes forcing amputation."
  - target: 01-human/07-system/myelofibrosis
    relation: connects-to
    note: "Thrombosis on thrombosis: myeloproliferative neoplasms like myelofibrosis are intrinsically prothrombotic and their patients receive heparin, a setting where HIT can stack a second, antibody-driven clotting risk on top."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "FcγR-triggered activation: cross-linking of platelet FcγRIIa by PF4-heparin immune complexes signals through PI3K-AKT to drive the explosive platelet activation behind HIT thrombosis."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Immunothrombosis: monocyte NLRP3-inflammasome activation contributes to the tissue-factor expression and immunothrombosis that make HIT so prothrombotic."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Inflammatory amplification: TNF-α in the inflammatory milieu of HIT upregulates endothelial and monocyte tissue factor, compounding the antibody-driven clotting."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Platelet activation product: FcγRIIa crosslinking by PF4–heparin–IgG immune complexes triggers platelet α-granule release of PDGF, a marker of the intense platelet activation that drives thrombosis in HIT."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "Thrombus scaffold: plasma and platelet α-granule fibronectin is incorporated into the platelet-rich arterial and venous clots characteristic of HIT, stabilising the prothrombotic aggregates."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Platelet chemokine: CXCL12 released from activated platelets reinforces the procoagulant, prothrombotic platelet phenotype amplified during HIT."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Thromboxane amplification: FcγRIIa-activated platelets in HIT generate thromboxane A2, a prostanoid that recruits and aggregates further platelets, amplifying the prothrombotic cascade beyond the initial immune trigger."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Monocyte procoagulant activation: PF4–heparin immune complexes engage monocyte FcγRIIa and CCL2-driven recruitment, inducing the tissue-factor expression that fuels the intense thrombin generation characteristic of HIT."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Endothelial tipping point: HIT antibodies activate endothelium and reduce its nitric-oxide output, removing a key antithrombotic brake and shifting the vessel wall toward the thrombosis that defines the syndrome."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "NET amplification: activated neutrophils releasing S100A8/A9 and extracellular traps (NETs) scaffold and amplify the immunothrombosis of HIT, adding an innate-immune amplifier to the platelet-driven clotting that makes the syndrome so prothrombotic."
  - target: 01-human/03-molecular/baff
    relation: connects-to
    note: "Transient antibody response: BAFF-supported B cells generate the anti-PF4/heparin IgG that drives HIT, an unusually rapid and transient antibody response without lasting memory, explaining why the antibodies wane and re-exposure can sometimes be tolerated."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Innate priming: PF4-heparin immune complexes engage innate receptors including TLR4 on monocytes, driving the tissue-factor expression and inflammatory state that couples the immune response to the thrombin generation behind HIT thrombosis."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Ischaemic sequelae: the limb- and organ-threatening arterial and venous thromboses of HIT cause tissue hypoxia that drives HIF-1α responses, the basis of the gangrene and infarction that make HIT thrombosis so dangerous."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Prothrombotic inflammation: the systemic inflammatory milieu of HIT includes IL-6, which amplifies the hypercoagulable, platelet- and endothelial-activating state underlying its paradoxical thrombosis despite falling platelet counts."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Procoagulant platelets: FcγRIIa-driven platelet activation in HIT triggers caspase-dependent procoagulant membrane changes and microparticle shedding, expanding the catalytic surface that accelerates thrombin generation."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "FcγRIIa signalling: clustering of platelet FcγRIIa by PF4-heparin immune complexes (PF4 and IgG mapped) triggers Src-family/Syk kinase signalling, the proximal step driving the platelet activation that causes HIT thrombosis."
  - target: 01-human/03-molecular/thrombopoietin
    relation: connects-to
    note: "Consumptive thrombocytopenia: as activated platelets aggregate and clear in HIT, the falling platelet count drives a compensatory thrombopoietin response reflecting the accelerated turnover."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "Complement amplification: complement activation on PF4-heparin complexes (C3 and C5 mapped) acting through C5aR1 amplifies the procoagulant, prothrombotic response of HIT."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Monocyte innate amplification: TLR-MyD88-NF-κB innate signalling (TLR4 and NF-κB already mapped) on monocytes amplifies the prothrombotic inflammatory response of heparin-induced thrombocytopenia."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "FcγRIIa platelet activation: FcγRIIa engagement by PF4-heparin immune complexes signals through Src and ERK1/2 (Src kinase already mapped) to drive the platelet activation central to heparin-induced thrombocytopenia."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K platelet signalling: PI3K (PIK3CA)-AKT signalling (AKT already mapped) downstream of FcγRIIa contributes to the platelet activation and aggregation of heparin-induced thrombocytopenia."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 promotes the neutrophil-extracellular-trap-driven thromboinflammation that amplifies the prothrombotic state of heparin-induced thrombocytopenia."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling transduces the inflammatory cytokine response of activated monocytes that contributes to the thrombosis of heparin-induced thrombocytopenia."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "DNA released within neutrophil extracellular traps engages cGAS-STING, linking NET-driven thromboinflammation to the prothrombotic milieu of heparin-induced thrombocytopenia."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK1/2 cytokine signaling (IL-6 already mapped) amplifies the inflammatory milieu accompanying the prothrombotic immune response of heparin-induced thrombocytopenia."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signaling shapes the immune activation underlying the anti-PF4/heparin antibody response in heparin-induced thrombocytopenia."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO downstream of PI3K-AKT signaling (AKT and PIK3CA already mapped) helps set the platelet and endothelial activation balance in heparin-induced thrombocytopenia."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β participates in the platelet-activation signaling downstream of FcγRIIa engagement in heparin-induced thrombocytopenia."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTOR signaling in activated platelets and immune cells participates in the prothrombotic immune activation of heparin-induced thrombocytopenia."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Endothelin-1 released by the activated endothelium contributes to the prothrombotic vascular tone of heparin-induced thrombocytopenia."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven monocyte recruitment contributes to the tissue-factor-bearing prothrombotic monocyte activation of heparin-induced thrombocytopenia."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the platelet and endothelial activation responses relevant to heparin-induced thrombocytopenia."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the platelet and immune-cell activation of heparin-induced thrombocytopenia."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the immune response generating anti-PF4/heparin antibodies in heparin-induced thrombocytopenia."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the prothrombotic inflammatory milieu of heparin-induced thrombocytopenia."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "CD20-expressing B cells produce the pathogenic anti-PF4/heparin antibodies of heparin-induced thrombocytopenia, a rationale for B-cell-depleting therapy in refractory cases."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the endothelial and immune activation relevant to heparin-induced thrombocytopenia."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the T-cell-mediated immune dysregulation of heparin-induced thrombocytopenia."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the T-cell help driving the anti-PF4/heparin antibody response of heparin-induced thrombocytopenia."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "T-cell help: the transient anti-PF4/heparin IgG response depends on MHC class II-restricted CD4 T-cell help (T-helper cells already mapped), so antigen presentation of the PF4-heparin complex is central to how HIT antibodies arise."
  - target: 01-human/03-molecular/ctla-4
    relation: connects-to
    note: "Immune regulation: the characteristically self-limited, transient nature of the HIT antibody response reflects immune checkpoints such as CTLA-4 restraining the autoreactive T-cell help, unlike the persistent antibodies of chronic autoimmunity."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Alpha-granule release: massive FcgammaRIIa-driven platelet activation in HIT discharges alpha-granule contents including PF4 (already mapped) and VEGF, contributing to the endothelial activation and inflammatory milieu of the prothrombotic state."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Arterial thrombosis: HIT causes arterial as well as venous thrombosis, including myocardial infarction and limb ischaemia, and troponin elevation marks the cardiac injury of the arterial events that complicate this prothrombotic disorder."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell help: IL-2-driven T-cell help supports the rapid but transient B-cell response that generates the anti-PF4/heparin antibodies (IgG already mapped), the T-cell dependence underlying the characteristically self-limited HIT antibody response."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Th2 antibody axis: IL-4 and type-2 T-cell help drive the B-cell production of the pathogenic anti-PF4/heparin antibodies of HIT, part of the humoral response that immune checkpoints (CTLA-4 already mapped) normally restrain."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immune counter-regulation: IL-10 helps restrain the transient anti-PF4/heparin antibody response of HIT (IL-6 and TNF already mapped), part of the immunoregulation that limits this typically self-limited immune reaction."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 cytokine axis: IL-13, with IL-4 (already mapped), completes the type-2 cytokine support for the B-cell production of the pathogenic anti-PF4/heparin antibodies of HIT."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative thrombo-inflammation: reactive oxygen species, to which xanthine oxidase contributes, are generated in the activated platelets and endothelium (already mapped) of HIT, adding oxidative stress to the prothrombotic, inflammatory state."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Platelet purinergic signalling: the ADP released from the activated platelets (already mapped) amplifies aggregation, while adenosine provides counter-regulatory inhibition, part of the purinergic control of the platelet activation that drives HIT."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Basophil activation: the anti-PF4/heparin antibodies (immunoglobulin G already mapped) activate basophils as well as platelets, releasing histamine, the basis of the basophil-activation test used to help diagnose HIT."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Platelet zinc and coagulation: zinc released from the activated platelets (already mapped) promotes the contact pathway and fibrin formation (fibrinogen and thrombin already mapped), contributing to the prothrombotic state of HIT."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Loss of tolerance: the regulatory T cells maintain tolerance to PF4 (already mapped), and the breakdown of this tolerance permits the transient anti-PF4/heparin antibody response that causes HIT."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Immune regulation: the PD-1 checkpoint and peripheral-tolerance mechanisms shape the self-limited nature of the anti-PF4 (already mapped) antibody response, which typically wanes over weeks in HIT."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate priming: the innate immune context (cGAS-STING already mapped), including type-I interferon, primes the rapid, T-cell-independent-like anti-PF4/heparin antibody response of HIT."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Immune-metabolic adipokine: leptin is the adipokine of the immune-metabolic milieu that modulates the immune-thrombotic response of heparin-induced thrombocytopenia."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic milieu of heparin-induced thrombocytopenia."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the immune-thrombotic milieu (IL-6 already mapped) of heparin-induced thrombocytopenia."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Innate immune modulation: the NK cells (perforin already mapped) contribute to the innate immune dysregulation of the immune-thrombotic response of heparin-induced thrombocytopenia."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 alloimmunity: the IFN-γ of the T cells is the type-II interferon arm (with the type-I interferon already mapped) of the immune response driving the anti-PF4/heparin IgG (immunoglobulin already mapped) of HIT."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the alloimmune response that generates the PF4 (already mapped) antibodies of heparin-induced thrombocytopenia."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the T-helper response generating the anti-PF4 antibodies of heparin-induced thrombocytopenia."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the alloimmune response of heparin-induced thrombocytopenia."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the alloimmune response of heparin-induced thrombocytopenia."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway activated on the PF4-heparin immune complexes (complement C3, C5 and C5aR1 already mapped) of heparin-induced thrombocytopenia."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Contact/kinin arm: the bradykinin-kinin system, activated alongside the coagulation (thrombin already mapped), contributes to the vascular and thromboinflammatory dimension of heparin-induced thrombocytopenia."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Adaptive arm: the cytotoxic T cells (perforin already mapped), alongside the T-helper (already mapped) support of the anti-PF4 B-cell response, are part of the transient alloimmune adaptive response of heparin-induced thrombocytopenia."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical/contact regulation: the C1-esterase inhibitor regulates the classical complement (C3, C5, C5aR1 and factor H already mapped) and the contact-kinin (bradykinin already mapped) systems co-activated in the thromboinflammation of heparin-induced thrombocytopenia."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Platelet thromboinflammation: osteopontin, released by the activated platelets (already mapped), is a matricellular mediator that amplifies the monocyte recruitment and the thromboinflammation of heparin-induced thrombocytopenia."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Consumptive iron: transferrin, the iron carrier, reflects the disordered iron handling accompanying the platelet consumption and the thrombotic microvascular injury of heparin-induced thrombocytopenia."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Thromboinflammatory alarmin: TSLP, released from endothelial cells (already mapped) and mast cells (already mapped) during the thromboinflammatory cascade, amplifies the type-2 immune polarisation at the platelet-thrombus interface of heparin-induced thrombocytopenia."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Platelet-EPO crosstalk: erythropoietin, secreted in response to the anaemia of the consumptive thrombocytopenia, also signals through EPOR on megakaryocytes to support the compensatory thrombopoiesis (thrombopoietin already mapped) in heparin-induced thrombocytopenia."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Vascular matricellular remodelling: periostin, induced by thromboinflammatory cytokines (IL-6 already mapped) in endothelial (already mapped) and smooth-muscle cells (already mapped), promotes vascular-wall fibrosis at thrombus sites in heparin-induced thrombocytopenia."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian platelet axis: melatonin, via MT1/MT2 receptors on platelets (already mapped), modulates platelet aggregation and the circadian oscillation of thrombotic risk, with overnight surges of coagulation (already mapped) activity amplifying HIT thrombosis."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Immune-endocrine coupling: prolactin, elevated during acute-phase inflammation (IL-6 already mapped) of HIT, potentiates B-cell (already mapped) autoantibody production (anti-PF4/heparin IgG) and may amplify the thromboinflammatory cascade."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Neuroimmune anti-thrombotic: oxytocin, via OXT receptors on platelets (already mapped) and endothelial cells (already mapped), modulates platelet activation and the thromboinflammatory signalling at the PF4-heparin antibody complex sites of HIT."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "HIT testosterone: testosterone suppresses NF-κB (already mapped) driven endothelial-cell (already mapped) activation in HIT; androgen receptor signalling also modulates platelet (already mapped) aggregation and thrombin (already mapped) generation in the HIT cascade."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "HIT vasopressin: vasopressin (ADH) potentiates platelet (already mapped) aggregation and thrombin (already mapped) generation via V1a receptor; vasopressin also amplifies the endothelial-cell (already mapped) prothrombotic NF-κB (already mapped) signalling in HIT."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "HIT selenium: selenoprotein antioxidants protect endothelial cells (already mapped) from the oxidative burst of platelet (already mapped) activation in HIT; selenium deficiency amplifies TNF-α (already mapped) driven NF-κB (already mapped) activation and the thrombotic cascade."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "HIT iodine: thyroid hormones (iodine-dependent) modulate platelet (already mapped) activation thresholds; iodine deficiency amplifies NF-κB (already mapped) endothelial cell (already mapped) prothrombotic activation and TNF-α (already mapped) thrombin (already mapped) cascade."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "HIT sodium: platelet (already mapped) ionic sodium modulates PF4 (already mapped) release and thrombin (already mapped) generation; sodium dysregulation amplifies NF-κB (already mapped) endothelial cell (already mapped) prothrombotic activation and IL-6 (already mapped) cascade."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "HIT magnesium: magnesium inhibits platelet (already mapped) activation and PF4 (already mapped) release; magnesium deficiency amplifies thrombin (already mapped) generation and NF-κB (already mapped) endothelial cell (already mapped) prothrombotic signalling in the HIT cascade."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "HIT copper: copper, via ceruloplasmin, modulates platelet (already mapped) activation and PF4 (already mapped) release; copper deficiency amplifies NF-κB (already mapped) endothelial cell (already mapped) prothrombotic signalling and thrombin (already mapped) cascade in HIT."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "HIT phosphorus: phosphate fuels platelet (already mapped) ATP and PF4 (already mapped) exocytosis; phosphorus deficiency amplifies thrombin (already mapped) generation and NF-κB (already mapped) endothelial cell (already mapped) prothrombotic cascade in HIT."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "HIT potassium: potassium regulates platelet (already mapped) and endothelial cell (already mapped) membrane potential; potassium dysregulation amplifies NF-κB (already mapped) and thrombin (already mapped) and PF4 (already mapped) prothrombotic cascade in HIT."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "HIT iron: iron, via ferritin in macrophages (already mapped) and platelet (already mapped) stores, modulates coagulation; iron dysregulation amplifies thrombin (already mapped) generation and NF-κB (already mapped) endothelial cell (already mapped) prothrombotic cascade in HIT."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "HIT chloride: chloride, as a key ionic regulator, maintains platelet (already mapped) and endothelial cell (already mapped) ion balance; chloride dysregulation amplifies NF-κB (already mapped) and thrombin (already mapped) and PF4 (already mapped) prothrombotic cascade in HIT."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "HIT carbon: carbon as backbone of PF4 (already mapped) and thrombin (already mapped) proteins anchors prothrombotic signalling; carbon-derived metabolites in platelets (already mapped) and endothelial cells (already mapped) amplify NF-κB (already mapped) cascade in HIT."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "HIT nitrogen: nitrogen as backbone of PF4 (already mapped) and thrombin (already mapped) sustains prothrombotic signalling; nitrogen-derived RNS from macrophages (already mapped) amplifies NF-κB (already mapped) and IL-6 (already mapped) endothelial damage in HIT."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "HIT sulfur: sulfur in disulfide bonds of PF4 (already mapped) and thrombin (already mapped) stabilises their prothrombotic conformations; sulfur-derived ROS in platelets (already mapped) amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade in HIT."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "HIT hydrogen: hydrogen via ROS from platelets (already mapped) and endothelial cells (already mapped) modulates prothrombotic oxidative stress; hydrogen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and PF4 (already mapped) prothrombotic cascade in HIT."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "HIT glp-1: GLP-1 from platelets (already mapped) and endothelial cells (already mapped) modulates thrombotic-metabolic tone; glp-1 dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) and PF4 (already mapped) and thrombin (already mapped) cascade in HIT."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "HIT angiotensin-ii: angiotensin-II from endothelial cells (already mapped) and platelets (already mapped) modulates vascular tone in HIT; angiotensin-ii dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and PF4 (already mapped) thrombotic cascade in HIT."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "HIT Wnt/β-catenin: Wnt/β-catenin in endothelium (already mapped) and platelets (already mapped) modulates HIT thrombotic vascular homeostasis; Wnt dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) thrombotic cascade of HIT."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "HIT RANKL: RANKL in macrophages (already mapped) and endothelium (already mapped) modulates HIT immune-thrombotic bone axis; RANKL excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) thrombotic cascade of heparin-induced thrombocytopenia."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "HIT SMAD4: SMAD4 in endothelium (already mapped) and macrophages (already mapped) modulates TGF-β-driven HIT vascular remodelling; SMAD4 loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) thrombotic cascade of HIT."
---

# Heparin-Induced Thrombocytopenia

## Overview

**Heparin-induced thrombocytopenia (HIT)** exists in two forms:
- **Type 1 HIT** (non-immune; "heparin effect"): Direct heparin-mediated platelet sequestration; mild thrombocytopenia (<30% drop) within 1-4 days of heparin; self-limited; no treatment needed; resolves despite continued heparin
- **Type 2 HIT** (immune-mediated; the clinically dangerous form): **Anti-PF4/heparin IgG** → platelet activation → severe thrombocytopenia (>50% drop) on days 5-10 + **paradoxical thrombosis**; life- and limb-threatening [^warkentin-2007-hit-review]

**The HIT paradox:** Unlike typical thrombocytopenias where low platelets → bleeding risk, HIT causes **thrombosis** — the IgG-activated platelets are procoagulant, and the thromboembolic risk (30-50% if untreated) vastly outweighs the bleeding risk.

**Epidemiology (Type 2 HIT):**
- Incidence: ~0.5-5% with UFH; ~0.1-0.5% with LMWH; <0.01% with fondaparinux
- Highest risk: Orthopedic and cardiac surgery patients receiving UFH for ≥5 days
- Temporal pattern: Platelet drop at days 5-10 after first heparin exposure (earlier — within 24h — if re-exposed within 3 months: "rapid-onset HIT")
- Anti-PF4/heparin seroconversion: ~7-17% of exposed surgical patients; only ~1-3% develop clinical HIT
- Female sex: ~2× risk vs. male (estrogen-related immune response?)

## Structure

### The 4T Score — Pre-test clinical probability

The **4T score** (0-8 points) stratifies HIT probability before diagnostic testing:

| Criterion | 2 points | 1 point | 0 points |
|:---------|:---------|:--------|:---------|
| **T**hrombocytopenia | >50% fall + nadir ≥20×10⁹/L | 30-50% fall OR nadir 10-19×10⁹/L | <30% fall OR nadir <10×10⁹/L |
| **T**iming of platelet fall | Days 5-10 (or ≤1 day if prior heparin in past 3 months) | >10 days OR timing unclear | ≤4 days without prior heparin exposure |
| **T**hrombosis | New thrombosis; skin necrosis at injection sites; acute anaphylactic reaction after IV UFH | Progressive/recurrent thrombosis; erythematous skin lesions | None |
| Other causes of **T**hrombocytopenia | None apparent | Possible other cause | Definite other cause |

**Score interpretation:**
- 0-3 (low): <5% HIT probability → HIT very unlikely, continue heparin
- 4-5 (intermediate): ~14% probability → start alternate anticoagulation, send HIT antibody testing
- 6-8 (high): >80% probability → stop heparin immediately, start non-heparin anticoagulant, send HIT testing

**Do NOT wait for lab results to stop heparin in high-probability patients.**

### Diagnostic testing

| Test | Sensitivity | Specificity | Role |
|:-----|:-----------|:------------|:-----|
| **Anti-PF4/heparin IgG ELISA** | ~97% | ~74% | First-line screening; negative ELISA virtually excludes HIT; high optical density (OD >2.0) strongly predictive |
| **Serotonin Release Assay (SRA)** | ~95% | ~97% | Gold standard confirmatory test; measures ¹⁴C-serotonin release from washed platelets in presence of patient serum + therapeutic heparin |
| **Heparin-Induced Platelet Activation (HIPA)** | ~95% | ~98% | Functional assay; visual assessment of platelet aggregation |
| **PIFA (platelet immunofluorescence assay)** | Variable | Variable | Less standardized; not preferred |

**Testing caveat:** SRA is available only at reference labs — results may take 3-5 days. Do NOT wait for SRA to treat high-probability HIT. Act on clinical probability + ELISA.

**The IgG-specific ELISA matters:** Total Ig (IgG + IgM + IgA) ELISA has higher sensitivity but lower specificity; IgG-specific ELISA correlates better with functional (SRA-positive) HIT and thrombotic risk.

## Function

### Pathophysiological cascade

**The HIT thrombosis paradox — step by step:**

```
Heparin (UFH/LMWH) administration
        ↓
PF4 released from platelet alpha-granules → binds heparin
        ↓
PF4-heparin complex → neo-antigen exposed on PF4
        ↓  (days 5-14: IgG production)
Anti-PF4/heparin IgG (predominantly IgG4)
        ↓
IgG-PF4-heparin → FcγRIIA (CD32a) on platelets
        ↓
Gαq → IP₃/DAG → Ca²⁺ flux
        ↓
Dense granule release: ADP, serotonin, PF4
TXA₂ synthesis (COX-1 → thromboxane A₂)
        ↓
Platelet activation loop: more PF4 → more complex → more IgG crosslinking
        ↓
Platelet microparticles (PS-exposing) → phospholipid surface for coagulation
        ↓
Prothrombin → THROMBIN → fibrin clot + platelet recruitment
        ↓
Arterial thrombi (limb, coronary, cerebral) + venous thrombi (DVT/PE, CVST)
  SIMULTANEOUSLY with
Platelet consumption → thrombocytopenia (paradox: clotting despite low platelets)
```

**Key consequence:** HIT can cause **any thrombotic event** — DVT/PE most common (HITT = HIT + thrombosis), but also arterial limb ischemia (often requiring amputation), MI, ischemic stroke, mesenteric ischemia, adrenal hemorrhage/necrosis (adrenal vein thrombosis).

### HIT without thrombosis vs. HITT

- **HIT without thrombosis:** Positive antibody + thrombocytopenia alone; thrombotic risk ~30% over next 30 days without treatment
- **HITT (HIT + Thrombosis):** ~50% of HIT cases; treatment urgency even higher; higher mortality (~5-10%) and amputation risk

## Pathology

### Acute treatment [^linkins-2012-hit-chest]

**Immediate (high-priority) actions:**
1. **STOP all heparin** — including heparin flushes, LMWH, heparin-coated catheters, heparin in TPN; heparin-bonded lines
2. **Start non-heparin anticoagulation IMMEDIATELY** — do not wait for lab confirmation in high-probability patients
3. **Do NOT give platelet transfusions** — adds "fuel to the fire" (more PF4 released) → may worsen thrombosis
4. **Do NOT start warfarin until platelets recover** (>150×10⁹/L) — warfarin-induced limb gangrene from protein C deficiency

**Non-heparin anticoagulants (choose based on clinical context):**

| Drug | Class | MOA | Half-life | Clearance | Monitoring | Notes |
|:-----|:------|:----|:----------|:----------|:-----------|:------|
| **Argatroban** (preferred) | Direct thrombin inhibitor | Reversible active-site DTI | ~45 min | Hepatic (safe in renal failure) | aPTT target 1.5-3× baseline | Falsely prolongs INR — challenge when bridging to warfarin |
| **Bivalirudin** | Direct thrombin inhibitor | Bivalent reversible DTI | ~25 min | 80% enzymatic (plasma); 20% renal | aPTT or ACT | Short half-life → useful in procedural settings (PCI, CABG) |
| **Fondaparinux** | Factor Xa inhibitor (indirect) | Anti-Xa via antithrombin | ~17-21 h | Renal (contraindicated CrCl <30) | Anti-Xa level (optional) | Very low HIT risk; not FDA-approved for HIT but widely used off-label |
| **Danaparoid** | Heparanoid (anti-Xa) | Inhibits Xa via antithrombin | ~24 h | Renal | Anti-Xa level | FDA-approved for HIT in Europe; ~5% cross-reactivity with HIT antibodies; monitor |
| **DOACs (rivaroxaban, apixaban)** | FXa inhibitors | Direct oral anti-Xa | 8-12 h | Renal + hepatic | Anti-Xa assay | Increasing use after acute phase; rivaroxaban has most HIT evidence (SWITCH study) |

**Transitioning to warfarin:**
- Wait until platelets recover to >150×10⁹/L before starting warfarin
- Overlap warfarin with non-heparin anticoagulant for ≥5 days AND until INR ≥2.0 for ≥2 consecutive days
- **Reason:** Warfarin drops protein C first (shortest half-life among vitamin K–dependent factors → 8h) → transient hypercoagulable state → warfarin-induced limb gangrene (venous limb gangrene) in HIT patients with already-thrombosed veins

**Duration:** At least 3 months anticoagulation for HITT; at least 1 month for HIT without thrombosis.

### Prevention and future heparin exposure

- **HIT antibodies typically become undetectable within 3-6 months** (IgG half-life)
- **Future heparin exposure after HIT:**
  - If SRA-negative and >3-6 months since prior HIT: brief re-exposure may be acceptable in life-saving situations (e.g., cardiac bypass) under monitoring
  - If SRA-positive: absolute avoidance of all heparin; use alternative anticoagulants; bivalirudin for cardiac bypass procedures
- **Document allergy in medical records:** Alert patient, future providers

### VITT (Vaccine-Induced Immune Thrombocytopenia with Thrombosis) [^greinacher-2021-vitt-nejm]

**Key differences from classic HIT:**
- Triggered by adenoviral vector COVID-19 vaccines (ChAdOx1, Ad26.COV2.S), NOT by heparin
- Anti-PF4 antibodies form without heparin — bind PF4 directly
- Onset: 4-28 days after vaccination
- Characteristic thromboses: CVST (cerebral venous sinus thrombosis), splanchnic vein thrombosis (portal, mesenteric), adrenal vein thrombosis — unusual sites
- Platelet count may be severely low (<30×10⁹/L); D-dimer markedly elevated

**VITT diagnosis:** Thrombocytopenia + unusual thrombosis + positive anti-PF4 antibody (ELISA or SRA) in appropriate post-vaccination time window; heparin NOT required

**VITT treatment:**
1. **High-dose IVIG (1 g/kg × 2 days):** Saturates FcγR on platelets + monocytes; provides anti-idiotypic antibodies → reduces platelet activation
2. **Non-heparin anticoagulation:** Fondaparinux, argatroban, or DOACs; **avoid heparin** (may worsen VITT by forming PF4-heparin-IgG triple complex)
3. **Avoid platelet transfusion** (worsens thrombosis)
4. **Avoid warfarin initially** (same protein C rationale as HIT)
5. **Corticosteroids:** Considered in refractory VITT

## Connections

- `connects-to` → **[PF4](../../03-molecular/pf4/README.md)** — Anti-PF4/heparin IgG (predominantly IgG4) is the diagnostic antigen of HIT; formed when PF4-heparin complex → neo-antigen → IgG production; ELISA detects anti-PF4/heparin IgG (sensitive, ~97%; not specific); SRA (serotonin release assay) is the confirmatory gold standard.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Anti-PF4/heparin IgG crosslinks FcγRIIA on platelets → Gαq → IP3/DAG → Ca²⁺ → dense granule release (ADP, serotonin) + TXA2 → further platelet activation loop; platelet activation fragments generate procoagulant microparticles → thrombin → arterial and venous thrombosis.
- `connects-to` → **[Thrombin](../../03-molecular/thrombin/README.md)** — HIT causes paradoxical thrombosis: activated platelets generate procoagulant microparticles → thrombin generation; argatroban (DTI) and bivalirudin block thrombin in HIT; warfarin is contraindicated initially (protein C drops first → warfarin-induced limb gangrene risk).
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — HIT causes paradoxical DVT/PE (venous) and arterial thrombosis (HITT); occurs 5-10 days after heparin exposure; anti-PF4/heparin IgG → platelet activation → thrombin; argatroban, bivalirudin, and fondaparinux replace heparin in HIT; DOACs used for bridging to warfarin.
- `connects-to` → **[Antithrombin](../../03-molecular/antithrombin/README.md)** — UFH and LMWH anticoagulate via AT (heparin binds AT → 1000× accelerated thrombin/FXa inhibition); AT is bypassed by direct thrombin inhibitors (argatroban, bivalirudin) used in HIT; fondaparinux (FXa inhibitor via AT) is an alternative in HIT.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — HIT is driven by a transient IgG against the PF4-heparin complex; this antibody cross-links FcγRIIA on platelets to activate them, so detection rests on an anti-PF4/heparin IgG ELISA confirmed by a serotonin-release assay — and the IgG typically fades within 3-6 months.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Beyond platelets, anti-PF4/heparin IgG activates endothelial cells: PF4 binds endothelial heparan sulfate, and immune-complex engagement induces tissue factor expression, amplifying thrombin generation — why HIT is so intensely prothrombotic despite falling platelet counts.
- `connects-to` → **[Inherited Thrombophilia](../inherited-thrombophilia/README.md)** — HIT is a severe acquired thrombophilia that, unlike most inherited thrombophilias, threatens arteries as well as veins and can take limbs; co-existing inherited thrombophilia or recent VTE further raises the risk of HIT-associated thrombosis.
- `connects-to` → **[Paroxysmal Nocturnal Hemoglobinuria](../pnh/README.md)** — HIT and PNH are acquired, intensely prothrombotic disorders with opposite mechanisms: HIT is anti-PF4/heparin IgG activating platelets, PNH is complement-mediated hemolysis from GPI-anchor loss; both clot despite platelet consumption and need targeted therapy, not heparin alone.
- `connects-to` → **[Antiphospholipid Syndrome](../antiphospholipid-syndrome/README.md)** — HIT and antiphospholipid syndrome are antibody-mediated acquired thrombophilias threatening arteries and veins: anti-PF4 IgG and antiphospholipid antibodies each activate platelets and endothelium; both can cause catastrophic multisite thrombosis and avoid reliance on heparin.
- `connects-to` → **[Stroke](../stroke/README.md)** — Unlike most thrombophilias, HIT causes arterial as well as venous thrombosis: anti-PF4/heparin immune complexes activate platelets and endothelium → arterial 'white clots' causing stroke, MI and limb ischemia; suspected HIT mandates a non-heparin anticoagulant.
- `connects-to` → **[Immune Thrombocytopenia](../immune-thrombocytopenia/README.md)** — HIT and immune thrombocytopenia are both antibody-mediated low-platelet states with opposite effects: ITP antibodies destroy platelets and bleed, while HIT's anti-PF4 antibodies activate platelets and clot—so HIT means stopping heparin, not transfusing.
- `connects-to` → **[Disseminated Intravascular Coagulation](../disseminated-intravascular-coagulation/README.md)** — HIT and DIC both cause inpatient thrombocytopenia but differ: DIC consumes factors and platelets with prolonged PT/PTT, while HIT activates platelets via antibody with normal clotting times—4T score and anti-PF4 testing distinguish them.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — HIT is the template for vaccine-induced thrombotic thrombocytopenia (VITT) after COVID-19 adenoviral vaccines: both feature anti-PF4 antibodies that activate platelets to cause thrombosis with thrombocytopenia, treated alike with non-heparin anticoagulation and IVIG.
- `connects-to` → **[Thrombotic Thrombocytopenic Purpura](../thrombotic-thrombocytopenic-purpura/README.md)** — HIT and TTP are both life-threatening thrombocytopenias: HIT is antibody-mediated platelet activation by PF4-heparin complexes causing paradoxical thrombosis, while TTP is ADAMTS13 deficiency forming microthrombi—both drop platelets, but cause and treatment differ.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement amplifies the prothrombotic immunity of HIT: the IgG-PF4-heparin immune complexes that activate platelets also engage complement, fueling endothelial activation and thrombosis—linking an antibody reaction to heparin with the innate complement cascade.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — HIT is paradoxical—low platelets cause clots, not bleeds: PF4-heparin antibodies activate platelets and endothelium, triggering arterial and venous thrombosis across the cardiovascular system—so heparin is stopped and a non-heparin anticoagulant started.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages execute the paradox of HIT: Fc receptors on macrophages and platelets bind PF4-heparin-IgG immune complexes, clearing platelets (thrombocytopenia) while activating them to clot—so the same antibody both lowers the count and causes thrombosis.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Complement amplifies the thrombosis of HIT and its cousin VITT: PF4-antibody complexes activate complement on platelets and endothelium, boosting clot formation—so complement and the anti-PF4 antibody together explain why HIT clots despite a falling platelet count.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Pulmonary embolism is a major HIT complication: the paradoxical clotting strikes veins, throwing clots to the lung, so a heparin-treated patient with a falling platelet count and new dyspnea needs heparin stopped and a non-heparin anticoagulant urgently.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — HIT is driven by B-cell antibodies: B cells rapidly make IgG against platelet-factor-4/heparin complexes, and these antibodies cross-link platelet Fc receptors to trigger the paradoxical clotting—so the culprit is a transient, T-independent antibody response.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — The spleen helps cause HIT's low platelet count: its macrophages clear antibody-coated platelets from the circulation, so even as clots form, platelet numbers fall—the 'thrombocytopenia with thrombosis' paradox that defines the syndrome.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Neutrophils amplify the thrombosis of HIT: activated by anti-PF4 immune complexes, they release neutrophil extracellular traps (NETs) that provide a scaffold for clot formation—linking HIT to the same NET-driven immunothrombosis seen in VITT and severe COVID.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — The serotonin release assay confirms HIT: activated platelets dump their serotonin stores, so measuring heparin-dependent serotonin release from donor platelets is the gold-standard functional test distinguishing true HIT from harmless anti-PF4 antibodies.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — HIT can announce itself in the skin: heparin injection sites may develop painful necrotic lesions from local thrombosis, a recognized skin sign of the paradoxical clotting that defines the syndrome despite falling platelets.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — HIT's anti-PF4/heparin antibodies arise with T-helper-cell support: helper T cells license B cells to produce the pathogenic IgG, an unusually rapid immune response that can recur on heparin re-exposure.
- `connects-to` → **[Fibrinogen](../../03-molecular/fibrinogen/README.md)** — HIT is a paradoxical clotting storm consuming fibrinogen: the activated platelets generate massive thrombin that converts fibrinogen to fibrin, so a low-platelet state causes thrombosis rather than bleeding—the trap that defines the disease.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — HIT platelets activate through a calcium surge: antibody clustering of platelet Fc receptors triggers calcium influx that drives the granule release and aggregation behind the prothrombotic state—the cellular step that makes HIT dangerous.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — HIT starts when dendritic cells flag PF4-heparin as foreign: heparin reshapes platelet factor 4 into a neo-antigen these sentinels recognize and present, kicking off the rapid immune reaction that turns a blood thinner into a clotting trigger.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — HIT clots can strike the brain: despite the falling platelet count it is a prothrombotic state, causing arterial strokes and cerebral vein thrombosis, so HIT is treated with non-heparin anticoagulants rather than transfusion.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — HIT can destroy the adrenal glands: bilateral adrenal vein thrombosis leads to hemorrhagic infarction and acute adrenal insufficiency, a rare but catastrophic complication of the syndrome's paradoxical clotting.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — HIT chokes tissues of oxygen through thrombosis: clots in arteries and veins block blood flow, causing limb ischemia that can require amputation, so the hypoxic damage—not bleeding—is HIT's central threat.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Once HIT is suspected, imaging hunts the clots: CT and lung scans read in X-ray photons find the pulmonary emboli and limb thromboses that make the syndrome dangerous despite the low platelets.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — HIT clots arteries as well as veins: coronary thrombosis can cause a heart attack, part of the arterial thrombosis that distinguishes this paradoxical, clot-prone low-platelet state.
- `connects-to` → **[Von Willebrand Factor](../../03-molecular/von-willebrand-factor/README.md)** — HIT inflames the vessel wall: the immune complexes activate endothelium to release von Willebrand factor, which grabs platelets and amplifies the prothrombotic storm beyond the platelets' own activation.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — HIT's low platelets do not come from a failing marrow: the megakaryocytes keep producing normally, but the antibody-coated platelets are consumed in clots and cleared by the spleen, a destruction rather than a production problem.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — HIT's clotting can strike the kidney: thrombosis of the renal veins or microvasculature, part of the body-wide prothrombotic storm, can cause acute kidney injury even as the platelet count falls.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reveals HIT's trigger: heparin and platelet factor 4 assemble into large ultralarge complexes that the antibodies cross-link on the platelet surface, the molecular scaffolding that ignites the whole prothrombotic cascade.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — HIT is an antibody disease in disguise: IgG against the PF4-heparin complex clusters FcγRIIa on platelets to activate them en masse, the paradoxical immune mechanism that drops the count while driving clots.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — HIT's clots reach the gut's circulation: the prothrombotic storm can seed portal, hepatic, and mesenteric vein thrombosis, threatening the liver and bowel alongside the more familiar limb and lung clots.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — The brain is not spared: HIT can throw clots into cerebral arteries or the venous sinuses, causing strokes and cerebral venous thrombosis that injure neurons — part of why it is so dangerous despite the low platelet count.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — HIT clots the muscular arteries too: 'white clot syndrome' lodges platelet-rich thrombi in the limb arteries lined by smooth muscle, causing acute ischemia and the venous limb gangrene that can cost a leg despite full anticoagulation.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Even the retina's vessels can clot: HIT's prothrombotic state has caused retinal artery and vein occlusions with sudden visual loss, one more unexpected site of the paradoxical thrombosis that defines the syndrome.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Pregnancy complicates the choice of blood thinner: heparins are first-line for pregnancy clots because they don't cross the placenta, so HIT forces a switch to alternatives like fondaparinux, balancing maternal thrombosis against fetal safety.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — HIT clots the arteries too: paradoxically, the activated platelets drive arterial as well as venous thrombosis, so myocardial infarction from coronary occlusion is among its feared events, injuring cardiomyocytes in a patient who is also bleeding-prone.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Dialysis is a setup for HIT: hemodialysis patients are repeatedly exposed to heparin in the circuit, so they are among those who develop the PF4 antibodies, forcing a switch to alternative anticoagulants for their dialysis.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — The clots favor diseased arteries: HIT's arterial thromboses — the so-called white clots — tend to form on atherosclerotic plaque, turning a stable vessel into an acute occlusion of a limb, brain or heart.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — The culprit drug is a body molecule: heparin is naturally made and stored in mast cells, so the anticoagulant that triggers HIT is a pharmaceutical version of a mediator these immune cells release into tissues.
- `connects-to` → **[FcRn](../../03-molecular/fcrn/README.md)** — The pathogenic antibody is long-lived: the anti-PF4/heparin IgG that drives HIT is recycled and kept in circulation by FcRn, sustaining the prothrombotic state for weeks after heparin is stopped.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — It hides among the critically ill: sepsis and its consumptive coagulopathy commonly drop platelets in the same patients receiving heparin, a key mimic that must be distinguished from HIT before stopping the drug and switching anticoagulants.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — Plasma cells make the dangerous antibody: a rapid B-cell response matures into plasma cells secreting the anti-PF4/heparin IgG that drives HIT, an unusually fast antibody response that can appear within days of heparin exposure.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — The immune complexes light up the vessel wall: PF4-heparin-IgG complexes activate monocytes and endothelium through NF-κB, switching on tissue factor and adhesion molecules that turn HIT into a relentlessly prothrombotic state.
- `connects-to` → **[Pulmonary Arterial Hypertension](../pulmonary-arterial-hypertension/README.md)** — Unresolved clots can stiffen the lung circulation: the pulmonary emboli thrown by HIT, if incompletely cleared, can organize into chronic thromboembolic pulmonary hypertension, a lasting rise in pulmonary artery pressure.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Large clots can buckle the right heart: a massive pulmonary embolism thrown by HIT acutely overloads the right ventricle into acute cor pulmonale, and HIT itself often arises after cardiac surgery in patients with limited cardiac reserve.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — It strikes the already critically ill: HIT typically develops in post-surgical and intensive-care patients who carry the anemia of chronic disease from their inflammatory state, compounding the hematologic complexity.
- `connects-to` → **[Polycythemia Vera](../polycythemia-vera/README.md)** — It joins the differential of thrombosis with an odd platelet count: when clotting coincides with abnormal platelets, myeloproliferative disorders like polycythemia vera are weighed alongside HIT as drivers of an acquired prothrombotic state.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Its clots kill tissue and leave wounds: HIT thrombosis causes heparin-injection-site skin necrosis and limb ischemia that can progress to gangrene and amputation, leaving major wounds to heal.
- `connects-to` → **[PTSD](../ptsd/README.md)** — A sudden limb-threatening crisis can scar the mind: HIT often strikes critically ill patients, and surviving its abrupt thrombosis, amputation or ICU course can leave post-traumatic stress.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Limb loss and prolonged illness weigh on mood: the disability from HIT-related amputation and the protracted critical illness it accompanies contribute to depression in survivors.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It can necrose the skin at injection sites: HIT classically causes skin lesions ranging from erythematous plaques to frank necrosis where heparin is injected, a recognised marker of the syndrome.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It can infarct both adrenal glands: thrombosis of the adrenal veins in HIT causes bilateral haemorrhagic adrenal infarction, precipitating acute adrenal insufficiency that is easily missed.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A sudden paradoxical clotting crisis breeds worry: the abrupt limb- and life-threatening thrombosis of HIT and the lifelong need to avoid heparin foster chronic health anxiety alongside the PTSD and depression it leaves.
- `connects-to` → **[Immune System](../immune-system/README.md)** — It is an immune drug reaction at heart: IgG antibodies against platelet factor 4-heparin complexes cross-link platelet FcγRIIa receptors, activating platelets and the clotting cascade despite a falling platelet count.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It often clots the lungs: pulmonary embolism is a frequent thrombotic outcome of HIT, and a rapid intravenous heparin bolus can trigger an acute anaphylactoid reaction with dyspnoea and collapse.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It thromboses unusual sites: HIT can clot the mesenteric and portal veins, causing bowel ischaemia and abdominal pain, and adrenal vein thrombosis can lead to haemorrhagic adrenal infarction.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It clots the brain's vessels: cerebral venous sinus thrombosis and arterial stroke are serious neurological thrombotic complications of HIT.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It clots the renal vessels: renal vein and renal artery thrombosis in HIT cause acute kidney injury.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It can cost a limb: arterial thrombosis in HIT causes acute limb ischaemia and gangrene that may require amputation, the 'white clot syndrome'.
- `connects-to` → **[Warfarin](../../../03-medicine/01-modern/09-hematology/warfarin/README.md)** — Warfarin is dangerous early in it: starting warfarin during acute HIT can precipitate venous limb gangrene by dropping protein C, so a non-heparin anticoagulant is used first.
- `connects-to` → **[aHUS](../ahus/README.md)** — A fellow antibody-driven thrombotic disorder: like atypical HUS, HIT is an antibody-mediated prothrombotic state, here from anti-PF4-heparin immune complexes that activate platelets.
- `connects-to` → **[Staphylococcus aureus](../../../02-pathogen/02-bacteria/staphylococcus-aureus/README.md)** — Infection can trigger anti-PF4 antibodies: 'spontaneous' or autoimmune HIT, occurring without heparin after infection or orthopaedic surgery, has been linked to bacterial triggers such as Staphylococcus aureus.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — White clots in the arteries: the platelet-activating PF4 antibodies of HIT seed platelet-rich 'white clot' thrombi not only in veins but in arteries, causing limb ischaemia, stroke and acute arterial occlusion.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Cardiac surgery is the danger zone: cardiopulmonary bypass exposes patients to massive heparin doses, making cardiac surgery the highest-incidence setting for HIT, where the antibodies can drive coronary thrombosis and myocardial infarction.
- `connects-to` → **[Essential Thrombocythemia](../essential-thrombocythemia/README.md)** — Opposite counts, shared thrombosis: HIT thromboses while platelets fall as they are consumed by activation, whereas essential thrombocythemia thromboses with a high platelet count — a paradox of platelet number versus platelet activation.
- `connects-to` → **[Hemophilia A](../hemophilia-a/README.md)** — Opposite poles of haemostasis: heparin-induced thrombocytopenia clots despite falling platelets, while haemophilia A bleeds from absent factor VIII—the thrombosis-versus-bleeding extremes of coagulation.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — Microthrombi reach the kidney: the intense prothrombotic state of HIT can seed microvascular thrombi that impair the renal glomeruli, adding acute kidney injury to its limb and organ thromboses.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — It clots the lungs: HIT's hypercoagulability drives venous thromboembolism and pulmonary embolism, lodging clots in the pulmonary vasculature feeding the alveoli—a leading cause of HIT death.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Splanchnic thrombosis: HIT can clot the portal and mesenteric veins, congesting the hepatic lobules and threatening bowel infarction—an under-recognised but dangerous site of HIT thrombosis.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — An unusual antibody response: HIT's anti-PF4/heparin IgG arises within days and is short-lived, reflecting a largely extrafollicular B-cell response that bypasses durable germinal-centre memory—why the antibodies wane within months.
- `connects-to` → **[Pancreatic Cancer](../pancreatic-cancer/README.md)** — Cancer, clots and heparin: highly thrombogenic cancers like pancreatic adenocarcinoma (Trousseau syndrome) demand heavy heparin anticoagulation, the very setting in which heparin-induced thrombocytopenia can dangerously compound the clotting.
- `connects-to` → **[Protein C](../../03-molecular/protein-c/README.md)** — Why warfarin is dangerous in HIT: starting warfarin during acute HIT depletes protein C faster than the procoagulant factors, tipping into venous limb gangrene—so warfarin is withheld until the platelet count recovers.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Limb-threatening ischaemia: HIT's arterial thromboses and venous limb gangrene starve the extremities, damaging peripheral nerves with ischaemic neuropathy and sometimes forcing amputation.
- `connects-to` → **[Myelofibrosis](../myelofibrosis/README.md)** — Thrombosis on thrombosis: myeloproliferative neoplasms like myelofibrosis are intrinsically prothrombotic and their patients receive heparin, a setting where HIT can stack a second, antibody-driven clotting risk on top.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — FcγR-triggered activation: cross-linking of platelet FcγRIIa by PF4-heparin immune complexes signals through PI3K-AKT to drive the explosive platelet activation behind HIT thrombosis.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Immunothrombosis: monocyte NLRP3-inflammasome activation contributes to the tissue-factor expression and immunothrombosis that make HIT so prothrombotic.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Inflammatory amplification: TNF-α in the inflammatory milieu of HIT upregulates endothelial and monocyte tissue factor, compounding the antibody-driven clotting.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — Platelet activation product: FcγRIIa crosslinking by PF4–heparin–IgG immune complexes triggers platelet α-granule release of PDGF, a marker of the intense platelet activation that drives thrombosis in HIT.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — Thrombus scaffold: plasma and platelet α-granule fibronectin is incorporated into the platelet-rich arterial and venous clots characteristic of HIT, stabilising the prothrombotic aggregates.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — Platelet chemokine: CXCL12 released from activated platelets reinforces the procoagulant, prothrombotic platelet phenotype amplified during HIT.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — FcγRIIa-activated platelets in HIT generate thromboxane A2, a prostanoid that recruits and aggregates further platelets, amplifying the prothrombotic cascade well beyond the initial PF4–heparin–IgG immune trigger.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — PF4–heparin immune complexes engage monocyte FcγRIIa alongside CCL2-driven recruitment, inducing the tissue-factor expression that fuels the intense thrombin generation underlying the paradoxical thrombosis of HIT.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — HIT antibodies activate endothelium and reduce its nitric-oxide output, removing a key antithrombotic brake and shifting the vessel wall toward the venous and arterial thrombosis that defines the dangerous form of the syndrome.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — Activated neutrophils releasing S100A8/A9 and extracellular traps (NETs) scaffold and amplify the immunothrombosis of HIT, adding an innate-immune amplifier to the platelet-driven clotting that makes the syndrome so prothrombotic.
- `connects-to` → **[BAFF](../../03-molecular/baff/README.md)** — BAFF-supported B cells generate the anti-PF4/heparin IgG that drives HIT, an unusually rapid and transient antibody response without lasting memory, explaining why the antibodies wane and re-exposure can sometimes be tolerated.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — PF4-heparin immune complexes engage innate receptors including TLR4 on monocytes, driving the tissue-factor expression and inflammatory state that couples the immune response to the thrombin generation behind HIT thrombosis.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — The limb- and organ-threatening arterial and venous thromboses of HIT cause tissue hypoxia that drives HIF-1α responses, the basis of the gangrene and infarction that make HIT thrombosis so dangerous.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — The systemic inflammatory milieu of HIT includes IL-6, which amplifies the hypercoagulable, platelet- and endothelial-activating state underlying its paradoxical thrombosis despite falling platelet counts.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — FcγRIIa-driven platelet activation in HIT triggers caspase-dependent procoagulant membrane changes and microparticle shedding, expanding the catalytic surface that accelerates thrombin generation.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — Clustering of platelet FcγRIIa by PF4-heparin immune complexes (PF4 and IgG mapped) triggers Src-family/Syk kinase signaling, the proximal step driving the platelet activation that causes HIT thrombosis.
- `connects-to` → **[Thrombopoietin](../../03-molecular/thrombopoietin/README.md)** — As activated platelets aggregate and clear in HIT, the falling platelet count drives a compensatory thrombopoietin response reflecting the accelerated turnover.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — Complement activation on PF4-heparin complexes (C3 and C5 mapped) acting through C5aR1 amplifies the procoagulant, prothrombotic response of HIT.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR-MyD88-NF-κB innate signaling (TLR4 and NF-κB already mapped) on monocytes amplifies the prothrombotic inflammatory response of heparin-induced thrombocytopenia.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — FcγRIIa engagement by PF4-heparin immune complexes signals through Src and ERK1/2 (Src kinase already mapped) to drive the platelet activation central to heparin-induced thrombocytopenia.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) downstream of FcγRIIa contributes to the platelet activation and aggregation of heparin-induced thrombocytopenia.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 promotes the neutrophil-extracellular-trap-driven thromboinflammation that amplifies the prothrombotic state of heparin-induced thrombocytopenia.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling transduces the inflammatory cytokine response of activated monocytes that contributes to the thrombosis of heparin-induced thrombocytopenia.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — DNA released within neutrophil extracellular traps engages cGAS-STING, linking NET-driven thromboinflammation to the prothrombotic milieu of heparin-induced thrombocytopenia.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK1/2 cytokine signaling (IL-6 already mapped) amplifies the inflammatory milieu accompanying the prothrombotic immune response of heparin-induced thrombocytopenia.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the immune activation underlying the anti-PF4/heparin antibody response in heparin-induced thrombocytopenia.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO downstream of PI3K-AKT signaling (AKT and PIK3CA already mapped) helps set the platelet and endothelial activation balance in heparin-induced thrombocytopenia.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β participates in the platelet-activation signaling downstream of FcγRIIa engagement in heparin-induced thrombocytopenia.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR signaling in activated platelets and immune cells participates in the prothrombotic immune activation of heparin-induced thrombocytopenia.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Endothelin-1 released by the activated endothelium contributes to the prothrombotic vascular tone of heparin-induced thrombocytopenia.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven monocyte recruitment contributes to the tissue-factor-bearing prothrombotic monocyte activation of heparin-induced thrombocytopenia.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the platelet and endothelial activation responses relevant to heparin-induced thrombocytopenia.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the platelet and immune-cell activation of heparin-induced thrombocytopenia.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the immune response generating anti-PF4/heparin antibodies in heparin-induced thrombocytopenia.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the prothrombotic inflammatory milieu of heparin-induced thrombocytopenia.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — CD20-expressing B cells produce the pathogenic anti-PF4/heparin antibodies of heparin-induced thrombocytopenia, a rationale for B-cell-depleting therapy in refractory cases.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the endothelial and immune activation relevant to heparin-induced thrombocytopenia.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the T-cell-mediated immune dysregulation of heparin-induced thrombocytopenia.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the T-cell help driving the anti-PF4/heparin antibody response of heparin-induced thrombocytopenia.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — T-cell help: the transient anti-PF4/heparin IgG response depends on MHC class II-restricted CD4 T-cell help (T-helper cells already mapped), so antigen presentation of the PF4-heparin complex is central to how HIT antibodies arise.
- `connects-to` → **[CTLA-4](../../03-molecular/ctla-4/README.md)** — Immune regulation: the characteristically self-limited, transient nature of the HIT antibody response reflects immune checkpoints such as CTLA-4 restraining the autoreactive T-cell help, unlike the persistent antibodies of chronic autoimmunity.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Alpha-granule release: massive FcgammaRIIa-driven platelet activation in HIT discharges alpha-granule contents including PF4 (already mapped) and VEGF, contributing to the endothelial activation and inflammatory milieu of the prothrombotic state.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Arterial thrombosis: HIT causes arterial as well as venous thrombosis, including myocardial infarction and limb ischaemia, and troponin elevation marks the cardiac injury of the arterial events that complicate this prothrombotic disorder.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell help: IL-2-driven T-cell help supports the rapid but transient B-cell response that generates the anti-PF4/heparin antibodies (IgG already mapped), the T-cell dependence underlying the characteristically self-limited HIT antibody response.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Th2 antibody axis: IL-4 and type-2 T-cell help drive the B-cell production of the pathogenic anti-PF4/heparin antibodies of HIT, part of the humoral response that immune checkpoints (CTLA-4 already mapped) normally restrain.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immune counter-regulation: IL-10 helps restrain the transient anti-PF4/heparin antibody response of HIT (IL-6 and TNF already mapped), part of the immunoregulation that limits this typically self-limited immune reaction.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 cytokine axis: IL-13, with IL-4 (already mapped), completes the type-2 cytokine support for the B-cell production of the pathogenic anti-PF4/heparin antibodies of HIT.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative thrombo-inflammation: reactive oxygen species, to which xanthine oxidase contributes, are generated in the activated platelets and endothelium (already mapped) of HIT, adding oxidative stress to the prothrombotic, inflammatory state.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Platelet purinergic signalling: the ADP released from the activated platelets (already mapped) amplifies aggregation, while adenosine provides counter-regulatory inhibition, part of the purinergic control of the platelet activation that drives HIT.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Basophil activation: the anti-PF4/heparin antibodies (immunoglobulin G already mapped) activate basophils as well as platelets, releasing histamine, the basis of the basophil-activation test used to help diagnose HIT.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Platelet zinc and coagulation: zinc released from the activated platelets (already mapped) promotes the contact pathway and fibrin formation (fibrinogen and thrombin already mapped), contributing to the prothrombotic state of HIT.
- `connects-to` → **[Regulatory T cell](../../04-cellular/regulatory-t-cell/README.md)** — Loss of tolerance: the regulatory T cells maintain tolerance to PF4 (already mapped), and the breakdown of this tolerance permits the transient anti-PF4/heparin antibody response that causes HIT.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Immune regulation: the PD-1 checkpoint and peripheral-tolerance mechanisms shape the self-limited nature of the anti-PF4 (already mapped) antibody response, which typically wanes over weeks in HIT.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate priming: the innate immune context (cGAS-STING already mapped), including type-I interferon, primes the rapid, T-cell-independent-like anti-PF4/heparin antibody response of HIT.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Immune-metabolic adipokine: leptin is the adipokine of the immune-metabolic milieu that modulates the immune-thrombotic response of heparin-induced thrombocytopenia.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic milieu of heparin-induced thrombocytopenia.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the immune-thrombotic milieu (IL-6 already mapped) of heparin-induced thrombocytopenia.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Innate immune modulation: the NK cells (perforin already mapped) contribute to the innate immune dysregulation of the immune-thrombotic response of heparin-induced thrombocytopenia.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 alloimmunity: the IFN-γ of the T cells is the type-II interferon arm (with the type-I interferon already mapped) of the immune response driving the anti-PF4/heparin IgG (immunoglobulin already mapped) of HIT.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the alloimmune response that generates the PF4 (already mapped) antibodies of heparin-induced thrombocytopenia.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the T-helper response generating the anti-PF4 antibodies of heparin-induced thrombocytopenia.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the alloimmune response of heparin-induced thrombocytopenia.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the alloimmune response of heparin-induced thrombocytopenia.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway activated on the PF4-heparin immune complexes (complement C3, C5 and C5aR1 already mapped) of heparin-induced thrombocytopenia.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Contact/kinin arm: the bradykinin-kinin system, activated alongside the coagulation (thrombin already mapped), contributes to the vascular and thromboinflammatory dimension of heparin-induced thrombocytopenia.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Adaptive arm: the cytotoxic T cells (perforin already mapped), alongside the T-helper (already mapped) support of the anti-PF4 B-cell response, are part of the transient alloimmune adaptive response of heparin-induced thrombocytopenia.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical/contact regulation: the C1-esterase inhibitor regulates the classical complement (C3, C5, C5aR1 and factor H already mapped) and the contact-kinin (bradykinin already mapped) systems co-activated in the thromboinflammation of heparin-induced thrombocytopenia.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Platelet thromboinflammation: osteopontin, released by the activated platelets (already mapped), is a matricellular mediator that amplifies the monocyte recruitment and the thromboinflammation of heparin-induced thrombocytopenia.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Consumptive iron: transferrin, the iron carrier, reflects the disordered iron handling accompanying the platelet consumption and the thrombotic microvascular injury of heparin-induced thrombocytopenia.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Thromboinflammatory alarmin: TSLP, released from endothelial cells (already mapped) and mast cells (already mapped) during the thromboinflammatory cascade, amplifies the type-2 immune polarisation at the platelet-thrombus interface of heparin-induced thrombocytopenia.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Platelet-EPO crosstalk: erythropoietin, secreted in response to the anaemia of the consumptive thrombocytopenia, also signals through EPOR on megakaryocytes to support the compensatory thrombopoiesis (thrombopoietin already mapped) in heparin-induced thrombocytopenia.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Vascular matricellular remodelling: periostin, induced by thromboinflammatory cytokines (IL-6 already mapped) in endothelial (already mapped) and smooth-muscle cells (already mapped), promotes vascular-wall fibrosis at thrombus sites in heparin-induced thrombocytopenia.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian platelet axis: melatonin, via MT1/MT2 receptors on platelets (already mapped), modulates platelet aggregation and the circadian oscillation of thrombotic risk, with overnight surges of coagulation (already mapped) activity amplifying HIT thrombosis.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Immune-endocrine coupling: prolactin, elevated during acute-phase inflammation (IL-6 already mapped) of HIT, potentiates B-cell (already mapped) autoantibody production (anti-PF4/heparin IgG) and may amplify the thromboinflammatory cascade.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Neuroimmune anti-thrombotic: oxytocin, via OXT receptors on platelets (already mapped) and endothelial cells (already mapped), modulates platelet activation and the thromboinflammatory signalling at the PF4-heparin antibody complex sites of HIT.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — HIT testosterone: testosterone suppresses NF-κB (already mapped) driven endothelial-cell (already mapped) activation in HIT; androgen receptor signalling also modulates platelet (already mapped) aggregation and thrombin (already mapped) generation in the HIT cascade.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — HIT vasopressin: vasopressin (ADH) potentiates platelet (already mapped) aggregation and thrombin (already mapped) generation via V1a receptor; vasopressin also amplifies the endothelial-cell (already mapped) prothrombotic NF-κB (already mapped) signalling in HIT.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — HIT selenium: selenoprotein antioxidants protect endothelial cells (already mapped) from the oxidative burst of platelet (already mapped) activation in HIT; selenium deficiency amplifies TNF-α (already mapped) driven NF-κB (already mapped) activation and the thrombotic cascade.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — HIT iodine: thyroid hormones (iodine-dependent) modulate platelet (already mapped) activation thresholds; iodine deficiency amplifies NF-κB (already mapped) endothelial cell (already mapped) prothrombotic activation and TNF-α (already mapped) thrombin (already mapped) cascade.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — HIT sodium: platelet (already mapped) ionic sodium modulates PF4 (already mapped) release and thrombin (already mapped) generation; sodium dysregulation amplifies NF-κB (already mapped) endothelial cell (already mapped) prothrombotic activation and IL-6 (already mapped) cascade.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — HIT magnesium: magnesium inhibits platelet (already mapped) activation and PF4 (already mapped) release; magnesium deficiency amplifies thrombin (already mapped) generation and NF-κB (already mapped) endothelial cell (already mapped) prothrombotic signalling in the HIT cascade.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — HIT copper: copper, via ceruloplasmin, modulates platelet (already mapped) activation and PF4 (already mapped) release; copper deficiency amplifies NF-κB (already mapped) endothelial cell (already mapped) prothrombotic signalling and thrombin (already mapped) cascade in HIT.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — HIT phosphorus: phosphate fuels platelet (already mapped) ATP and PF4 (already mapped) exocytosis; phosphorus deficiency amplifies thrombin (already mapped) generation and NF-κB (already mapped) endothelial cell (already mapped) prothrombotic cascade in HIT.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — HIT potassium: potassium regulates platelet (already mapped) and endothelial cell (already mapped) membrane potential; potassium dysregulation amplifies NF-κB (already mapped) and thrombin (already mapped) and PF4 (already mapped) prothrombotic cascade in HIT.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — HIT iron: iron, via ferritin in macrophages (already mapped) and platelet (already mapped) stores, modulates coagulation; iron dysregulation amplifies thrombin (already mapped) generation and NF-κB (already mapped) endothelial cell (already mapped) prothrombotic cascade in HIT.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — HIT chloride: chloride, as a key ionic regulator, maintains platelet (already mapped) and endothelial cell (already mapped) ion balance; chloride dysregulation amplifies NF-κB (already mapped) and thrombin (already mapped) and PF4 (already mapped) prothrombotic cascade in HIT.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — HIT carbon: carbon as backbone of PF4 (already mapped) and thrombin (already mapped) proteins anchors prothrombotic signalling; carbon-derived metabolites in platelets (already mapped) and endothelial cells (already mapped) amplify NF-κB (already mapped) cascade in HIT.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — HIT nitrogen: nitrogen as backbone of PF4 (already mapped) and thrombin (already mapped) sustains prothrombotic signalling; nitrogen-derived RNS from macrophages (already mapped) amplifies NF-κB (already mapped) and IL-6 (already mapped) endothelial damage in HIT.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — HIT sulfur: sulfur in disulfide bonds of PF4 (already mapped) and thrombin (already mapped) stabilises their prothrombotic conformations; sulfur-derived ROS in platelets (already mapped) amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade in HIT.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — HIT hydrogen: hydrogen via ROS from platelets (already mapped) and endothelial cells (already mapped) modulates prothrombotic oxidative stress; hydrogen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and PF4 (already mapped) prothrombotic cascade in HIT.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — HIT glp-1: GLP-1 from platelets (already mapped) and endothelial cells (already mapped) modulates thrombotic-metabolic tone; glp-1 dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) and PF4 (already mapped) and thrombin (already mapped) cascade in HIT.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — HIT angiotensin-ii: angiotensin-II from endothelial cells (already mapped) and platelets (already mapped) modulates vascular tone in HIT; angiotensin-ii dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and PF4 (already mapped) thrombotic cascade in HIT.
- `connects-to` → **[Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — HIT Wnt/β-catenin: Wnt/β-catenin in endothelium (already mapped) and platelets (already mapped) modulates HIT thrombotic vascular homeostasis; Wnt dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) thrombotic cascade of HIT.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — HIT RANKL: RANKL in macrophages (already mapped) and endothelium (already mapped) modulates HIT immune-thrombotic bone axis; RANKL excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) thrombotic cascade of heparin-induced thrombocytopenia.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — HIT SMAD4: SMAD4 in endothelium (already mapped) and macrophages (already mapped) modulates TGF-β-driven HIT vascular remodelling; SMAD4 loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) thrombotic cascade of HIT.

[^warkentin-2007-hit-review]: Warkentin TE, Greinacher A. Heparin-induced thrombocytopenia: recognition, treatment, and prevention. *Chest.* 2004;126(3 Suppl):311S-337S. [doi:10.1378/chest.126.3_suppl.311S](https://doi.org/10.1378/chest.126.3_suppl.311S) · [PubMed 15383477](https://pubmed.ncbi.nlm.nih.gov/15383477/)
[^greinacher-2021-vitt-nejm]: Greinacher A, Thiele T, Warkentin TE, et al. Thrombotic thrombocytopenia after ChAdOx1 nCov-19 vaccination. *N Engl J Med.* 2021;384(22):2092-2101. [doi:10.1056/NEJMoa2104840](https://doi.org/10.1056/NEJMoa2104840) · [PubMed 33835769](https://pubmed.ncbi.nlm.nih.gov/33835769/)
[^linkins-2012-hit-chest]: Linkins LA, Dans AL, Moores LK, et al. Treatment and prevention of heparin-induced thrombocytopenia: ACCP 9th ed. Guidelines. *Chest.* 2012;141(2 Suppl):e495S-e530S. [doi:10.1378/chest.11-2303](https://doi.org/10.1378/chest.11-2303) · [PubMed 22315270](https://pubmed.ncbi.nlm.nih.gov/22315270/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
