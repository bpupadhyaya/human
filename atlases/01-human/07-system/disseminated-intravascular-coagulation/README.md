---
schema: human-scale-entry/v1
id: disseminated-intravascular-coagulation
name: Disseminated Intravascular Coagulation
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "DIC is a syndrome of microvascular thrombosis and consumption coagulopathy from systemic thrombin activation; sepsis, obstetric emergencies, and malignancy are top triggers. ISTH score ≥5 = overt DIC. Treatment targets underlying cause; FFP + cryoprecipitate for bleeding."
aliases: ["DIC", "disseminated intravascular coagulation", "consumptive coagulopathy", "defibrination syndrome", "DIC coagulopathy", "overt DIC", "non-overt DIC", "microangiopathic coagulation"]
sources:
  - id: levi-2009-dic-review
    type: peer-reviewed
    cite: "Levi M, Toh CH, Thachil J, Watson HG. Guidelines for the diagnosis and management of disseminated intravascular coagulation. British Committee for Standards in Haematology. Br J Haematol. 2009;145(1):24-33."
    doi: "10.1111/j.1365-2141.2009.07600.x"
    pmid: "19222477"
    url: "https://doi.org/10.1111/j.1365-2141.2009.07600.x"
  - id: levi-2018-dic-lancet
    type: peer-reviewed
    cite: "Levi M, Scully M. How I treat disseminated intravascular coagulation. Blood. 2018;131(8):845-854."
    doi: "10.1182/blood-2017-10-804096"
    pmid: "29255070"
    url: "https://doi.org/10.1182/blood-2017-10-804096"
  - id: taylor-2001-isth-dic-score
    type: peer-reviewed
    cite: "Taylor FB Jr, Toh CH, Hoots WK, et al. Towards definition, clinical and laboratory criteria, and a scoring system for disseminated intravascular coagulation. Thromb Haemost. 2001;86(5):1327-1330."
    doi: "10.1055/s-0037-1616068"
    pmid: "11816725"
    url: "https://doi.org/10.1055/s-0037-1616068"
cross_links:
  - target: 01-human/03-molecular/fibrinogen
    relation: connects-to
    note: "Fibrinogen is consumed in DIC by uncontrolled thrombin generation (sepsis, obstetric catastrophe, malignancy); fibrinogen <1.5 g/L in DIC is both diagnostic and a trigger for cryoprecipitate replacement; D-dimer from fibrin cross-links confirms active fibrinolysis in DIC."
  - target: 01-human/03-molecular/thrombin
    relation: connects-to
    note: "Systemic TF/thrombin activation is the central mechanism of DIC: infection → cytokines → TF upregulation on monocytes/endothelium → FVIIa/TF → FX → thrombin → fibrin microthrombi; thrombin also exhausts natural anticoagulants (protein C/S, antithrombin) → feedback amplification."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Sepsis-induced DIC: endotoxin/DAMPs → NLRP3 inflammasome → IL-1β + IL-18 → endothelial TF expression → thrombin generation → fibrin; IL-1β amplifies NF-κB → PAI-1 upregulation → hypofibrinolysis → fibrin microthrombus persistence in septic DIC."
  - target: 01-human/03-molecular/antithrombin
    relation: connects-to
    note: "AT is consumed in DIC by ongoing thrombin generation; AT levels <60% correlate with DIC severity (ISTH DIC score); AT concentrate studied in sepsis-DIC (KyberSept trial: no mortality benefit); low AT + prolonged PT + thrombocytopenia = DIC triad."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "DIC causes platelet consumption → thrombocytopenia; platelet count is a key ISTH DIC score parameter (score 1 if <100K, score 2 if <50K); platelet transfusion if <50K + active bleeding, or <10K; platelet activation by thrombin amplifies DIC microthrombus formation."
  - target: 01-human/03-molecular/protein-c
    relation: connects-to
    note: "Protein C is consumed in DIC → loss of anticoagulant brake; PC deficiency → purpura fulminans (limb gangrene in septic DIC); protein C concentrate explored in severe sepsis-DIC; drotrecogin alfa (APC) withdrawn after PROWESS-SHOCK failed to show mortality benefit in sepsis-DIC."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Gram-negative sepsis is the most common DIC trigger: LPS → TLR4 → NF-κB → TF on monocytes/endothelium → systemic thrombin → fibrin microthrombi; 25-50% of severe sepsis develops overt DIC; sepsis-DIC mortality ~40-60%; antibiotics + source control are the primary treatment."
  - target: 01-human/07-system/essential-thrombocythemia
    relation: connects-to
    note: "DIC and essential thrombocythemia are mirror images: DIC consumes platelets and clotting factors in runaway thrombin activation (thrombocytopenia, bleeding), while ET clonally overproduces platelets causing thrombosis — yet both can bleed via acquired von Willebrand deficiency."
  - target: 01-human/07-system/cytokine-storm
    relation: connects-to
    note: "Cytokine storm is a major driver of DIC: TNF-α, IL-1β, and IL-6 induce tissue factor on monocytes and endothelium while suppressing anticoagulants and fibrinolysis, turning inflammation into systemic microthrombosis — the coagulopathy of sepsis, severe COVID, and CAR-T toxicity."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver makes nearly every coagulation factor consumed in DIC — fibrinogen, prothrombin, protein C, antithrombin — so acute liver failure produces a DIC-like consumptive coagulopathy that is the main diagnostic mimic; factor VIII stays normal in liver disease but falls in DIC."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Endothelium is the stage for DIC: inflammatory injury makes it express tissue factor and lose its anticoagulant thrombomodulin/protein-C surface, so widespread microvascular thrombi form and consume platelets and clotting factors—turning the vessel lining procoagulant systemwide."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "Acute promyelocytic leukemia (APL, AML-M3) is the classic malignant cause of DIC: the leukemic promyelocytes release tissue factor and profibrinolytic activity, so fatal hemorrhage at diagnosis is a hallmark—ATRA-based treatment plus blood-product support is started urgently."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "Obstetric catastrophes are a major DIC trigger via the placenta: abruption, amniotic-fluid embolism, retained dead fetus and pre-eclampsia release tissue factor into the maternal circulation, igniting consumptive coagulopathy—so delivery and source control are central."
  - target: 01-human/07-system/thrombotic-thrombocytopenic-purpura
    relation: connects-to
    note: "DIC and TTP both cause thrombocytopenia with microthrombi but differ in coagulation: DIC consumes clotting factors and prolongs PT/PTT, while TTP from ADAMTS13 deficiency leaves clotting times normal—normal coagulation amid a microangiopathy points to TTP."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "Pancreatic and other mucinous adenocarcinomas are a classic chronic cause of DIC: tumor mucin and tissue factor continuously activate coagulation (Trousseau syndrome), producing migratory thrombophlebitis and consumptive coagulopathy—often the first clue to an occult cancer."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "DIC shears red cells passing through fibrin-laden microvasculature: the strands fragment erythrocytes into schistocytes, producing a microangiopathic hemolytic anemia on the film—a clue, alongside low platelets and prolonged clotting, to consumptive coagulopathy."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "The kidney is an early DIC casualty: widespread microthrombi clog glomerular capillaries while consumption of clotting factors causes bleeding, so acute kidney injury is a common, prognostically important feature of disseminated intravascular coagulation."
  - target: 01-human/03-molecular/von-willebrand-factor
    relation: connects-to
    note: "DIC must be separated from VWF/ADAMTS13 disorders like TTP: both consume platelets and shear red cells, but DIC also consumes clotting factors (low fibrinogen, high D-dimer) whereas TTP spares them—the coagulation profile, not the smear alone, distinguishes them."
  - target: 01-human/07-system/immune-thrombocytopenia
    relation: connects-to
    note: "DIC and immune thrombocytopenia both lower platelets by different mechanisms: DIC consumes platelets in widespread clotting (with abnormal coagulation tests), while ITP destroys them via autoantibodies with normal clotting—so coagulation studies separate them."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils help ignite DIC through immunothrombosis: in sepsis they release neutrophil extracellular traps that activate clotting on the vessel wall, fusing the inflammatory and coagulation cascades that drive disseminated microthrombi and consumption of clotting factors."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "The lung is a frequent casualty of DIC: widespread microthrombi clog the pulmonary microvasculature while consumed clotting factors cause alveolar hemorrhage, so DIC contributes to the ARDS and respiratory failure of severe sepsis."
  - target: 01-human/07-system/malaria
    relation: connects-to
    note: "Severe falciparum malaria is a classic infectious trigger of DIC: parasitized red cells and inflammation activate coagulation and damage endothelium, so the bleeding and microthrombi of DIC complicate the deadliest form of malaria."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement and coagulation amplify each other in DIC: activated complement (C3 and beyond) promotes tissue factor and platelet activation while clotting enzymes cleave complement, so this crosstalk intensifies the runaway clotting of severe sepsis."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages help ignite DIC: in sepsis and cancer, monocytes and macrophages express tissue factor that triggers systemic coagulation, so these immune cells link inflammation to the widespread microthrombi that consume clotting factors."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "DIC threatens the brain at both extremes: microthrombi cause small strokes while consumed clotting factors invite intracranial hemorrhage, so altered mental status in a critically ill patient can signal cerebral involvement of this clotting-bleeding paradox."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Clotting in DIC runs on calcium—factor IV: calcium ions are an essential cofactor at multiple steps of the cascade, and the massive transfusions used to treat severe DIC can bind calcium and drop its level, worsening bleeding."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "DIC can destroy the adrenal glands (Waterhouse-Friderichsen): in meningococcal sepsis, widespread clotting causes bilateral adrenal hemorrhage, triggering sudden adrenal failure and shock on top of the coagulopathy."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "DIC shreds red cells and spills hemoglobin: fibrin strands strung across small vessels slice passing red cells (microangiopathic hemolysis), producing schistocytes and free hemoglobin that can itself injure the kidneys."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "TNF-alpha lights the fuse of sepsis-driven DIC: it induces tissue factor on monocytes and endothelium, igniting the clotting cascade throughout the circulation, the inflammation-to-coagulation link that turns infection into widespread microthrombosis."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "DIC can choke the heart's small vessels: microthrombi scattered through the coronary microcirculation, plus the bleeding and shock of the syndrome, strain the heart and add cardiac injury to its multi-organ damage."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "DIC starves organs of oxygen with countless tiny clots: fibrin microthrombi plug small vessels, cutting oxygen delivery to kidney, lung and brain, so tissue hypoxia and organ failure—not just bleeding—drive its high mortality."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "DIC drives the blood acidic: as microthrombi choke off perfusion and shock sets in, starved tissues pour out lactic acid, so a falling pH marks the metabolic acidosis of advancing multi-organ failure."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "DIC ravages the skin: widespread microthrombi and consumed clotting factors cause purpura fulminans—dark patches of hemorrhagic skin necrosis—alongside bruising, a dramatic visible sign of the coagulation chaos."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "DIC is a consumptive state the marrow races to refill: as clotting devours platelets and cells, the bone marrow ramps up production, but it cannot keep pace, leaving the low counts that fuel bleeding."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "DIC is a lab diagnosis, but imaging finds its cause and toll: CT photons reveal the sepsis source, cancer or placental catastrophe driving it, and the organ infarcts from its microthrombi."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "DIC clogs the kidney's filters: microthrombi lodge in the glomeruli while consumption and schistocytes mount, causing the acute kidney injury that often accompanies the coagulation chaos."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Complement fuels DIC's storm: C5a from the activated cascade inflames the endothelium and drives tissue factor, the crosstalk between complement and coagulation that worsens the clotting."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows DIC shredding the blood: fibrin strands strung across small vessels slice passing red cells into the helmet-shaped schistocytes of microangiopathic hemolysis, while platelet-fibrin microthrombi plug the capillaries."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "DIC's microthrombi can starve the gut: clots seeded throughout the mesenteric microvasculature cut off the bowel's blood supply, causing ischemia and bleeding amid the body-wide clotting-and-hemorrhage paradox."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "The spleen takes its share of DIC's clots: microinfarcts pepper it as the widespread microthrombosis lodges in its small vessels, one of the many organs silently injured during the consumptive coagulopathy."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "DIC strikes the brain both ways: microthrombi infarct it while the consumed clotting factors let it bleed, so altered consciousness, focal deficits, and intracranial hemorrhage all complicate the coagulopathy."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Obstetric catastrophes are classic triggers: placental abruption, amniotic fluid embolism, retained dead fetus, and HELLP all flood the blood with tissue factor, igniting DIC in pregnancy and childbirth."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "The eye bleeds and clots in miniature: DIC produces retinal and subconjunctival hemorrhages and microvascular occlusions, a window onto the simultaneous bleeding and thrombosis playing out body-wide."
  - target: 01-human/07-system/prostate-cancer
    relation: connects-to
    note: "Metastatic prostate cancer drives a bleeding-type DIC: the tumor releases plasminogen activators that ignite excess fibrinolysis, so unlike most clot-heavy DIC it presents with oozing and bruising — a hyperfibrinolytic state needing its own tailored treatment."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "Severe acute pancreatitis can set off DIC: leaking pancreatic enzymes and the systemic inflammation they unleash activate the clotting cascade body-wide, one of the noninfectious triggers of the consumptive coagulopathy."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "DIC strikes the brain both ways: showers of microthrombi cause scattered ischemic strokes while the consumed clotting factors invite intracerebral hemorrhage, the combination behind the confusion and focal deficits of severe cases."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Inflammation flips on the clotting switch: NF-κB activation in sepsis drives tissue-factor expression on monocytes and endothelium, the molecular trigger that launches the runaway coagulation of DIC."
  - target: 01-human/07-system/all
    relation: connects-to
    note: "Acute leukemia bleeds as it clots: leukemic cells — most dramatically in acute promyelocytic leukemia, and at presentation or induction in ALL — release procoagulants that set off DIC, a hematologic emergency at diagnosis."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "Microthrombi can starve the bowel: DIC clogs the small-vessel circulation of the gut, causing the ischemia and bleeding that add an abdominal catastrophe to its multi-organ failure."
  - target: 02-pathogen/02-bacteria/neisseria-meningitidis
    relation: connects-to
    note: "Meningococcus triggers the most vivid DIC: Neisseria meningitidis endotoxin sets off purpura fulminans with skin necrosis and Waterhouse-Friderichsen adrenal hemorrhage, a fulminant DIC that can kill within hours."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Contact activation links clotting to shock: the same surface activation that feeds DIC's coagulation also generates bradykinin, whose vasodilation and capillary leak deepen the hypotension of the underlying sepsis."
  - target: 01-human/07-system/dengue-fever
    relation: connects-to
    note: "Severe dengue clots and bleeds at once: the viral hemorrhagic fever activates coagulation while consuming platelets and factors, so DIC underlies the bleeding and shock of its critical phase."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Microthrombi shut down the kidney: fibrin clots clogging the glomerular capillaries cause acute kidney injury and, in severe cases, renal cortical necrosis that can leave lasting chronic kidney disease."
  - target: 01-human/06-organ/ards
    relation: connects-to
    note: "The lungs fill with microclots and fluid: pulmonary microthrombi and the shared sepsis inflammation make DIC a frequent companion of acute respiratory distress syndrome, each worsening the other."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Beyond the microclots, large veins can clot too: the systemic hypercoagulable drive of DIC raises the risk of macrovascular venous thromboembolism even as consumption of factors paradoxically causes bleeding."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Microthrombi and shock stun the heart: the myocardial microvascular clotting and profound hypotension of DIC's underlying critical illness impair cardiac function, contributing to acute heart failure."
  - target: 01-human/07-system/pnh
    relation: connects-to
    note: "A hemolytic disorder that can tip into it: the complement-driven hemolysis and intense thrombotic state of paroxysmal nocturnal hemoglobinuria can precipitate or overlap with DIC during severe crises."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Surviving the catastrophe leaves a mark: patients who survive the multiorgan failure and ICU course in which DIC arises carry the depression and cognitive sequelae of the post-intensive-care syndrome."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Microthrombi kill tissue and leave wounds: DIC's small-vessel clotting causes purpura fulminans and limb gangrene, sometimes requiring amputation, leaving major wounds that heal poorly amid critical illness."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Ischemic limb loss leaves lasting pain: the digital and limb gangrene of severe DIC can require amputation, producing chronic stump and phantom-limb neuropathic pain in survivors."
  - target: 01-human/07-system/ptsd
    relation: connects-to
    note: "A life-threatening ICU crisis can scar the mind: surviving the catastrophic bleeding, clotting and intensive care in which DIC occurs frequently leaves post-traumatic stress."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It is dramatically written on the skin: DIC causes widespread petechiae, ecchymoses and oozing from puncture sites, and in its severe form purpura fulminans with skin necrosis and digital gangrene."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Microthrombi and bleeding hit the lungs: DIC contributes to acute respiratory distress syndrome through diffuse microvascular thrombosis and can cause pulmonary haemorrhage."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It bleeds and starves the gut: DIC causes gastrointestinal haemorrhage from consumed clotting factors and platelets, while microthrombi cause bowel ischaemia and hepatic dysfunction."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Microthrombi clog the kidney: DIC deposits fibrin in the renal microvasculature, causing acute kidney injury and, in severe cases, bilateral renal cortical necrosis."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It both clots and bleeds the brain: cerebral microthrombi and intracranial haemorrhage from consumed platelets and clotting factors cause encephalopathy, stroke and bleeding."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It can destroy the adrenals: bilateral adrenal haemorrhage — Waterhouse-Friderichsen syndrome — complicates meningococcal DIC, causing acute adrenal failure."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "It clots and bleeds in the vessels at once: DIC scatters microthrombi that occlude small vessels while consuming clotting factors, causing both ischaemia and haemorrhage with circulatory collapse."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "It is driven by inflammation: sepsis and cytokine release trigger DIC through tissue factor and immunothrombosis, tying coagulation tightly to the innate immune response."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It bleeds into soft tissue: consumption of platelets and clotting factors causes spontaneous bleeding into muscles and, with purpura fulminans, ischaemic limb necrosis."
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: connects-to
    note: "Sepsis and toxic shock ignite it: Staphylococcus aureus bacteraemia and toxic-shock syndrome are major triggers of DIC, the bacterial sepsis driving uncontrolled coagulation."
  - target: 01-human/07-system/ahus
    relation: connects-to
    note: "A thrombotic-microangiopathy to distinguish: DIC must be told apart from aHUS and TTP, which also consume platelets and shear red cells but spare the clotting factors that DIC depletes."
  - target: 01-human/07-system/heparin-induced-thrombocytopenia
    relation: connects-to
    note: "A paradoxical clotting comparator: like DIC, heparin-induced thrombocytopenia combines a falling platelet count with thrombosis, but through antibody-mediated platelet activation rather than consumption."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Acute leukaemia both causes and cures it: acute promyelocytic leukaemia classically triggers life-threatening DIC, and treating it with ATRA and chemotherapy rapidly resolves the coagulopathy — while tumour lysis and other chemo can also provoke DIC."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "The liver makes and loses the factors: DIC microthrombi injure the hepatic lobule, and because the liver synthesises clotting factors, hepatic failure both worsens and mimics the coagulopathy of DIC."
  - target: 01-human/07-system/antiphospholipid-syndrome
    relation: connects-to
    note: "Catastrophic APS mimics it: catastrophic antiphospholipid syndrome causes widespread small-vessel thrombosis with consumption resembling DIC, a key differential demanding anticoagulation rather than factor replacement."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Pulmonary microthrombi: fibrin microthrombi clog the alveolar capillaries in DIC, worsening the hypoxaemia and ARDS of severe sepsis and amniotic-fluid embolism."
  - target: 01-human/07-system/gastric-cancer
    relation: connects-to
    note: "Chronic compensated DIC (Trousseau): mucin-secreting adenocarcinomas like gastric and pancreatic cancer activate coagulation, causing chronic DIC and migratory thrombophlebitis."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Microthrombi injure the heart: widespread microvascular thrombosis and shock in DIC starve the myocardium, contributing to the cardiac dysfunction of multi-organ failure."
  - target: 02-pathogen/02-bacteria/neisseria-meningitidis
    relation: connects-to
    note: "Purpura fulminans: meningococcal sepsis triggers fulminant DIC with skin necrosis and bilateral adrenal haemorrhage (Waterhouse-Friderichsen), a classic and rapidly fatal infectious cause."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "Endothelium drives the consumption: DIC begins when an injured or activated endothelium of the arterial wall and capillaries exposes tissue factor, igniting the runaway clotting that consumes platelets and factors."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "COVID coagulopathy: severe COVID-19 causes a distinctive coagulopathy with very high D-dimer and microthrombi that overlaps DIC, though usually with thrombosis rather than the consumptive bleeding."
  - target: 02-pathogen/01-viruses/ebola-virus
    relation: connects-to
    note: "Viral haemorrhagic coagulopathy: Ebola virus triggers severe DIC with consumptive coagulopathy and bleeding, a hallmark of the haemorrhagic fever it causes."
  - target: 02-pathogen/02-bacteria/streptococcus-pyogenes
    relation: connects-to
    note: "Toxic shock and purpura: invasive group A streptococcal infection and toxic shock syndrome drive DIC and purpura fulminans through overwhelming systemic inflammation."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Inflammation-coagulation crosstalk: IL-6 induces tissue factor and fibrinogen and amplifies the cytokine response that ignites DIC in sepsis, linking inflammation to clotting."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Tissue-factor induction: IL-1β from activated monocytes upregulates endothelial and monocyte tissue factor, a key inflammatory trigger of the systemic coagulation in DIC."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Endothelial collapse: the widespread endothelial injury of DIC cuts protective nitric oxide, removing its antithrombotic brake and worsening microvascular thrombosis."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Microvascular constriction: injured endothelium in DIC releases endothelin-1, whose vasoconstriction compounds the microthrombi to drive the ischaemic organ failure of the syndrome."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "Immunothrombosis: S100A8/A9-rich neutrophil extracellular traps provide a scaffold and trigger for the widespread microthrombi of DIC, linking the innate immune response of sepsis to its consumptive coagulopathy."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Endotoxin trigger: TLR4 sensing of bacterial LPS in sepsis induces tissue factor on monocytes and endothelium, the initiating signal that unleashes the systemic coagulation of DIC."
  - target: 01-human/03-molecular/pf4
    relation: connects-to
    note: "Platelet consumption: PF4 released from the platelets massively activated and consumed in DIC marks the platelet activation that, with coagulation-factor depletion, produces the bleeding-thrombosis paradox."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Monocyte tissue factor: CCL2 recruits and activates the monocytes whose tissue-factor expression is the principal initiator of the systemic coagulation activation that drives sepsis-induced DIC."
  - target: 01-human/03-molecular/rage
    relation: connects-to
    note: "HMGB1 thromboinflammation: HMGB1 signalling through RAGE sustains the thromboinflammation of DIC, a late DAMP mediator that perpetuates the coagulation activation beyond the initial sepsis or trauma."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Mitochondrial-DNA trigger: mitochondrial DNA released in sepsis and trauma activates cGAS-STING, contributing the innate-immune signalling that feeds the immunothrombosis underlying DIC."
  - target: 01-human/03-molecular/adamts13
    relation: connects-to
    note: "VWF-cleaving deficiency: the inflammatory consumption of ADAMTS13 in sepsis leaves uncleaved ultra-large von Willebrand factor multimers that capture platelets, adding a microvascular thrombotic mechanism to the tissue-factor-driven coagulopathy of DIC."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Endothelial apoptosis: inflammatory injury drives caspase-3-mediated apoptosis of endothelial cells, exposing the procoagulant tissue factor and basement membrane that ignite and sustain the disseminated clotting of DIC."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative endothelial injury: xanthine-oxidase-derived reactive oxygen species damage the endothelium in the systemic inflammation that triggers DIC, shifting the vessel wall to a procoagulant state that feeds the microvascular thrombosis."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Endothelial destabilisation: Ang-2 released from activated, injured endothelium in sepsis-associated DIC destabilises the vasculature, amplifying the endothelial dysfunction that triggers and sustains the coagulopathy."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "Complement-coagulation crosstalk: C5a acting through C5aR1 (complement C5 already mapped) induces tissue-factor expression and amplifies the thromboinflammation that drives the microvascular clotting of DIC."
  - target: 01-human/03-molecular/thrombopoietin
    relation: connects-to
    note: "Platelet consumption: the consumptive thrombocytopenia central to DIC drives a compensatory thrombopoietin response, reflecting the accelerated platelet turnover as clots form throughout the microvasculature."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Sepsis trigger: in sepsis-induced DIC — its commonest cause — TLR-MyD88-NF-κB signalling (TLR4 and NF-κB already mapped) couples infection to the tissue-factor expression and inflammation that ignite systemic coagulation."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Thromboinflammatory amplification: IL-6 signalling through JAK-STAT (IL-6 already mapped) amplifies the cytokine response and drives the hepatic acute-phase and procoagulant changes of DIC."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Endothelial dysfunction: VEGF-mediated endothelial activation and permeability, alongside the angiopoietin-Tie2 axis (already mapped), contributes to the endothelial injury underlying the microvascular thrombosis of DIC."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "C5a acting on C5aR (C5aR1 mapped) and platelet agonists engage ERK-MAPK, amplifying the cellular activation that propagates DIC."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Endothelial and platelet PI3K-AKT signalling shapes the procoagulant, activated phenotype that drives the widespread microthrombosis of DIC."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 promotes the neutrophil-extracellular-trap-driven thromboinflammation that fuels disseminated intravascular coagulation."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling transduces the inflammatory cytokine response that drives the tissue-factor expression and procoagulant state of disseminated intravascular coagulation."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K-AKT signalling (AKT already mapped) in platelets and endothelium supports the activated, procoagulant phenotype of disseminated intravascular coagulation."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the interferon component of the systemic inflammation (often sepsis-driven) underlying disseminated intravascular coagulation."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO downstream of PI3K-AKT signaling (AKT and PIK3CA already mapped) regulates the endothelial activation balance disrupted in the thromboinflammation of disseminated intravascular coagulation."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α in the hypoxic, microthrombosed tissues amplifies the endothelial dysfunction of disseminated intravascular coagulation."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signaling drives the organ fibrosis that can follow the microvascular ischemic injury of disseminated intravascular coagulation."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the platelet-activation and inflammatory signaling that drive the systemic coagulation activation of disseminated intravascular coagulation."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTOR signaling in activated endothelium and immune cells participates in the immunothrombosis underlying disseminated intravascular coagulation."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-bearing cytotoxic lymphocytes contribute to the endothelial injury that triggers the coagulation cascade in sepsis-associated disseminated intravascular coagulation."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the platelet activation and endothelial responses of disseminated intravascular coagulation."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked endothelial metabolic signaling modulates the vascular homeostasis disrupted in disseminated intravascular coagulation."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment contributes to the thrombo-inflammation of disseminated intravascular coagulation."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the endothelial and immune-cell responses relevant to the thrombo-inflammation of disseminated intravascular coagulation."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic modulation of the coagulation and endothelial gene expression relevant to disseminated intravascular coagulation."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the endothelial and leukocyte interactions of the thrombo-inflammation of disseminated intravascular coagulation."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the endothelial activation and thromboinflammation of disseminated intravascular coagulation."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the thromboinflammation of disseminated intravascular coagulation."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the endothelial and inflammatory gene programs of disseminated intravascular coagulation."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Lactic acidosis: the microvascular thrombosis and shock of severe DIC starve tissues of oxygen (already mapped), forcing anaerobic metabolism that generates protons and lactate, so a worsening metabolic acidosis tracks the severity of the coagulopathy."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Multi-organ injury: the widespread microthrombi of DIC injure organs including the heart, and troponin elevation marks the myocardial damage that is part of the multi-organ failure driving its high mortality."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Tissue hypoxia: fibrin microthrombi occlude the microcirculation in DIC, cutting off oxygen delivery and causing the ischaemic organ dysfunction, from kidneys (already mapped) to skin, that defines its thrombotic phase."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Cytokine balance: the anti-inflammatory cytokine IL-10 counters the TNF, IL-1 and IL-6 (already mapped) that ignite the coagulation of sepsis-induced DIC, and the balance between them shapes the severity of the coagulopathy."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Inflammatory iron handling: the IL-6 surge (already mapped) of the sepsis that commonly triggers DIC raises hepcidin, sequestering iron and contributing to the anaemia (haemoglobin already mapped) of the critical illness."
  - target: 01-human/03-molecular/adrenomedullin
    relation: connects-to
    note: "Endothelial vasodilation: adrenomedullin rises with the endothelial activation (already mapped) of the sepsis and DIC, contributing to the vasodilation and vascular leak of shock, and is studied as a biomarker and therapeutic target."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Thromboxane and inflammation: the prostaglandin/thromboxane balance on the activated platelets (already mapped) and endothelium shifts toward the prothrombotic thromboxane, part of the platelet activation and inflammation of DIC."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Platelet serotonin: serotonin released from the activated, consumed platelets (PF4 already mapped) causes vasoconstriction and amplifies platelet aggregation in the widespread microthrombi of DIC."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Haemolysis and iron: the microangiopathic haemolysis of DIC fragments red cells (haemoglobin already mapped) releasing iron, while the inflammatory hepcidin (already mapped) sequesters it, part of the anaemia of the critical illness."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Contact-pathway zinc: zinc released from the activated, consumed platelets (PF4 already mapped) promotes the contact pathway and fibrin (fibrinogen already mapped) formation, adding to the coagulation activation of DIC."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Sepsis-severity adipokine: resistin, a pro-inflammatory adipokine, rises markedly in the sepsis (already mapped) that commonly triggers DIC, a marker of the severity of the inflammatory drive behind the consumptive coagulopathy."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Vascular permeability: histamine from the activated mast cells and basophils adds to the vascular permeability (bradykinin already mapped) and the vasodilatory shock of the severe conditions that trigger DIC."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Inflammatory adipokine: leptin, with resistin (already mapped), rises in the acute inflammation (IL-6 already mapped) of the sepsis (already mapped) and severe conditions that trigger the consumptive coagulopathy of DIC."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Adipokine axis: adiponectin, with leptin and resistin (already mapped), completes the adipokine axis of the systemic inflammation driving the disseminated intravascular coagulation."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate immunothrombosis: type-I interferon is part of the innate-immune signalling of the viral and inflammatory (IL-6 already mapped) triggers of DIC, contributing to the immunothrombotic host response."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Immunothrombosis NETs: the neutrophils release the NETs (S100A8/9 already mapped) that scaffold the microthrombi, the immunothrombosis driving the disseminated intravascular coagulation."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "APL emergency: the acute promyelocytic leukaemia (a subtype of AML) classically presents with the severe DIC (the procoagulant granules), a haematological emergency."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Microthrombotic AKI: the fibrin microthrombi (thrombin already mapped) lodge in the kidney, causing the acute kidney injury and the organ dysfunction of DIC."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 inflammation: the IFN-γ of the T cells is the type-II interferon arm of the inflammatory drive (IL-6 and TNF already mapped) that, via the immunothrombosis, activates the coagulation of DIC."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the systemic inflammation underlying DIC."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Type-2 counter-arm: IL-4 is the type-2 cytokine arm counter-balancing the pro-inflammatory (IL-6 and TNF already mapped) drive of the coagulopathy of DIC."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 arm: IL-13, with IL-4 (already mapped), completes the type-2 immune arm counter-balancing the pro-inflammatory drive of the systemic coagulopathy of DIC."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune milieu of the systemic inflammation underlying DIC."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the systemic inflammation (IL-6 and TNF already mapped) that drives the immunothrombosis of DIC."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) whose consumption and dysregulation amplify the complement–coagulation crosstalk of DIC."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Contact/complement regulation: the C1-esterase inhibitor regulates both the classical complement and the contact (intrinsic-coagulation, bradykinin already mapped) pathways, a key brake at the complement–coagulation interface consumed in DIC."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Haemolytic iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the microangiopathic haemolysis and the inflammation of DIC."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Thromboinflammation: osteopontin, released by the activated platelets (already mapped), is a matricellular mediator linking the inflammation to the microthrombosis of DIC."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Vascular mast cells: the mast cells contribute to the vascular permeability and, through tissue-factor and heparin release, to the coagulation-anticoagulation imbalance of DIC."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Adaptive immunothrombosis: the CD4 T-helper cells contribute to the inflammatory drive of the immunothrombosis that underlies the sepsis-associated DIC."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-DIC axis: TSLP, from the septic or inflammatory epithelium, primes dendritic cells and mast cells (already mapped) and amplifies the cytokine storm (already mapped) and the systemic inflammatory response that triggers disseminated intravascular coagulation."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "EPO-DIC axis: erythropoietin, upregulated by the HIF-1α (already mapped) hypoxia of DIC-related multi-organ injury, mobilises erythroid progenitors and modulates macrophage (already mapped) polarisation, linking the anaemia of DIC to the inflammatory coagulopathy."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Remodelling axis: periostin, released from the injured endothelium (already mapped) and fibroblasts during the DIC-related vascular injury, contributes to the tissue remodelling and repair after the consumptive coagulopathy."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian-coagulopathy axis: melatonin, via MT1/MT2 receptors and its antioxidant activity, modulates the oxidative stress of the systemic inflammatory response (cytokine-storm already mapped) and the endothelial injury that triggers DIC."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Sex-hormone coagulation axis: testosterone, via androgen receptors on endothelium (already mapped) and platelets (already mapped), modulates the coagulation cascade and the sex-differential thrombotic risk of the consumptive coagulopathy of DIC."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Immunostimulatory prolactin axis: prolactin, via PRL receptors on T cells (already mapped) and macrophages (already mapped), amplifies the cytokine production and the systemic inflammatory activation that can trigger the consumptive coagulopathy of DIC."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "DIC oxytocin: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates the systemic inflammatory cascade; oxytocin deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) coagulopathic cascade of DIC."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "DIC vasopressin: vasopressin, via V2R on endothelium (already mapped) and macrophages (already mapped), modulates vascular tone and haemostasis; vasopressin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) consumptive coagulopathy of DIC."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "DIC selenium: selenium, via selenoprotein antioxidant activity in macrophages (already mapped) and neutrophils (already mapped), suppresses the oxidative amplification of the NF-κB (already mapped) and TNF-α (already mapped) systemic inflammatory cascade of DIC."
---

# Disseminated Intravascular Coagulation

## Overview

**Disseminated intravascular coagulation (DIC)** is an **acquired syndrome** of simultaneous, uncontrolled activation of the coagulation and fibrinolytic systems throughout the vascular tree, resulting in:
1. **Microvascular thrombosis** — fibrin deposition in small vessels → end-organ ischemia (kidney, lung, brain, liver, adrenal glands)
2. **Consumption coagulopathy** — platelets, fibrinogen, and clotting factors depleted by the ongoing clotting process → paradoxical bleeding (hemorrhagic DIC)
3. **Microangiopathic hemolytic anemia (MAHA)** — RBCs mechanically fragmented by fibrin strands → schistocytes

DIC is always **secondary** — it does not occur in isolation but as a consequence of an underlying systemic trigger. DIC is not a diagnosis; it is a laboratory-clinical syndrome accompanying a primary disease. The most important therapeutic intervention is treating the underlying cause [^levi-2018-dic-lancet].

**Epidemiology:**
- Occurs in ~25-50% of patients with severe sepsis; ~20% of obstetric emergencies; ~10% of acute leukemia (especially AML-M3/APL)
- In-hospital mortality: varies by cause — sepsis-DIC ~40-60%; obstetric DIC ~1-2% (if treated promptly); AML-M3/APL DIC 5-10% with ATRA + arsenic trioxide

**Key dichotomy:**
- **Bleeding-predominant DIC:** Obstetric catastrophe (abruptio placentae, amniotic fluid embolism), AML-M3/APL, transfusion reactions → rapid consumption → severe coagulopathy + hemorrhage
- **Thrombosis-predominant DIC (chronic/compensated):** Malignancy (especially mucin-secreting adenocarcinoma), sepsis (early phase) → Trousseau syndrome (migratory thrombophlebitis in cancer-associated DIC)

## Structure

### Pathophysiological framework

**Central mechanism: TF-driven thrombin storm**

1. **Underlying trigger** (infection, tissue injury, cancer, immune complex) → systemic **tissue factor (TF)** expression on monocytes and endothelial cells
2. TF + FVIIa → extrinsic pathway → **FX → FXa → prothrombinase → massive thrombin generation**
3. Thrombin → fibrin deposits throughout microcirculation + platelet activation + feedback amplification (activates FV, FVIII, FXIII)
4. **Natural anticoagulant exhaustion:** Thrombin consumes protein C, protein S, antithrombin → loss of anti-thrombotic brakes → runaway amplification
5. **Fibrinolysis activation:** Plasmin generated → degrades fibrin → FDPs/D-dimer → FDPs inhibit further fibrin polymerization and platelet function (prothrombotic → hemorrhagic shift)
6. **Consumption:** Platelets, fibrinogen, factors V/VIII/X consumed faster than replaced → coagulopathy → hemorrhage

### Triggers of DIC

**Infections (most common cause):**
- Gram-negative sepsis: LPS → TLR4 → NF-κB → TF, TNF-α, IL-1β → monocyte/endothelial TF expression
- Gram-positive: TSST-1, PVL toxins → cytokine storm → TF
- Viremia (COVID-19, dengue, viral hemorrhagic fevers): endothelial injury + cytokine storm → TF + complement activation
- Malaria (Plasmodium falciparum): RBC parasitization → adhesion to endothelium → local TF + hemolysis

**Obstetric emergencies:**
- **Abruptio placentae** (most common): Placental TF → maternal DIC; hemorrhagic; very rapid onset
- **Amniotic fluid embolism:** Amniotic fluid (rich in TF, fetal squames) → systemic TF → DIC + anaphylactoid reaction
- **Preeclampsia/HELLP syndrome:** Endothelial dysfunction → TF + complement + platelet consumption (microangiopathic)
- **Placenta previa, uterine rupture, retained fetal demise**

**Malignancy:**
- AML-M3 (APL, acute promyelocytic leukemia): Promyelocyte granules release TF + cancer procoagulant (cysteine protease) + t-PA → hemorrhagic DIC (most dangerous subtype); **ATRA (all-trans retinoic acid) differentiation therapy → TF downregulation → DIC resolves**
- Solid tumors (pancreas, prostate, lung adenocarcinoma): Trousseau syndrome — chronic low-grade DIC with migratory thrombophlebitis; mucin activates coagulation; warfarin poorly effective → LMWH preferred

**Trauma/tissue destruction:**
- Polytrauma: traumatic brain injury → massive TF release from brain parenchyma; crush injury → myoglobin + TF; Trauma-Induced Coagulopathy (TIC) has overlapping features with DIC
- Burns, fat embolism, major surgery

**Immune-mediated:**
- Transfusion reactions (ABO incompatibility → hemolysis → TF)
- Severe autoimmune disease; vasculitis
- Snake venom (specifically: Echis, Agkistrodon species produce thrombin-like enzymes → fibrinogen depletion)

## Function

### ISTH DIC scoring system [^taylor-2001-isth-dic-score]

**Overt DIC (International Society on Thrombosis and Haemostasis) score:**

| Parameter | 0 | 1 | 2 | 3 |
|:---------|:-|:-|:-|:-|
| Platelet count (×10⁹/L) | ≥100 | <100 | <50 | — |
| PT prolongation (seconds above ULN) | <3 | 3-6 | >6 | — |
| D-dimer / fibrin-related marker | No increase | Moderate increase | Strong increase | — |
| Fibrinogen (g/L) | ≥1 | <1 | — | — |

- **Score ≥5 = overt DIC**: Compatible with DIC; treat aggressively
- **Score <5 = non-overt/suspected DIC**: Repeat daily; treat underlying cause

**Note:** DIC scoring requires an underlying predisposing condition as entry criterion. A score ≥5 has >90% specificity for DIC in appropriate clinical context.

## Pathology

### Diagnosis

**Laboratory findings in overt DIC:**
- **Thrombocytopenia:** Platelet consumption (<100,000/μL in overt DIC; declining serial counts important even before threshold)
- **Prolonged PT/aPTT:** Factor consumption (FV, FVIII, FX, prothrombin); aPTT prolonged; may be only mildly elevated in compensated DIC
- **Hypofibrinogenemia:** Fibrinogen <1.5 g/L (very specific for DIC when combined with other findings); note fibrinogen is an acute-phase reactant and may remain "normal" (2-4 g/L) even with significant consumption in sepsis — a declining fibrinogen trend is key
- **Elevated D-dimer:** Most sensitive marker (>95% sensitivity) but non-specific (elevated in PE, MI, surgery, liver disease, pregnancy)
- **Schistocytes on peripheral blood smear:** MAHA from fibrin strand-mediated RBC fragmentation; Coombs-negative
- **Low antithrombin, protein C, protein S:** Consumed by ongoing thrombin activation
- **Thrombin-antithrombin (TAT) complex:** Most specific marker of thrombin generation; elevated early in DIC; research test

**Distinguishing DIC from TTP/HUS:**
| Feature | DIC | TTP | aHUS |
|:--------|:----|:----|:-----|
| ADAMTS13 | Normal | <10% | Normal |
| PT/aPTT | Prolonged | Normal | Normal |
| Fibrinogen | Low | Normal | Normal |
| D-dimer | High | Mildly elevated | Mildly elevated |
| Schistocytes | Present | Prominent | Prominent |

### Treatment [^levi-2018-dic-lancet]

**1. Treat the underlying cause — the most important intervention:**
- Sepsis: Antibiotics, source control (drainage, surgery)
- APL: ATRA ± arsenic trioxide → differentiation therapy → TF downregulation → DIC resolves within days
- Obstetric: Delivery, oxytocin, uterine massage, surgical repair; transfuse aggressively

**2. Blood product replacement (bleeding DIC):**
- **Fresh frozen plasma (FFP):** Replaces all clotting factors (FV, FVIII, fibrinogen, protein C/S, antithrombin); 10-20 mL/kg; use if PT >1.5× normal + active bleeding or invasive procedure planned
- **Cryoprecipitate:** Concentrated fibrinogen (10× FFP per unit) + FVIII + VWF + FXIII; give if fibrinogen <1.5 g/L; 10 units → fibrinogen +0.5-1 g/L; target fibrinogen ≥1.5-2 g/L
- **Platelet transfusion:** Give if platelets <50,000/μL + active bleeding, or <10,000/μL prophylactically
- **Avoid aggressive factor replacement in thrombotic DIC** (Trousseau, early compensated sepsis DIC) — may worsen microthrombosis

**3. Anticoagulation (thrombosis-predominant DIC):**
- Therapeutic LMWH or UFH in Trousseau syndrome (cancer-associated DIC with thrombosis)
- Heparin in purpura fulminans (protein C deficiency + DIC with limb gangrene)
- **Protein C concentrate or recombinant APC:** Considered in severe sepsis-DIC with purpura fulminans; restores depleted anticoagulant protein C → breaks thrombin amplification loop; high-dose recombinant APC (drotrecogin alfa) was withdrawn due to survival benefit not confirmed in large trial (PROWESS-SHOCK)

**4. Antifibrinolytic therapy — use with extreme caution:**
- **Tranexamic acid:** Inhibits plasminogen → fibrin protection; use only if fibrinolysis-predominant DIC with life-threatening bleeding (APL-DIC before ATRA starts, obstetric DIC); CONTRAINDICATED in thrombotic DIC (will worsen microthrombosis)
- The CRASH-2 trial showed benefit of tranexamic acid within 3 hours of trauma injury — this is trauma-TIC context, not classic DIC

**5. Antithrombin concentrate (AT-III):**
- AT is consumed in DIC; replacement improves outcomes in some studies (sepsis-DIC with AT <70%)
- Not universally recommended; may be considered in severe DIC with AT <70% and ongoing thrombosis despite heparin

**Special situations:**
- **APL/AML-M3-DIC:** ATRA + arsenic trioxide → primary treatment; aggressive cryoprecipitate/FFP/platelet transfusion during induction; avoid heparin (increases bleeding risk); DIC typically resolves within 5-10 days of ATRA
- **Obstetric DIC:** Rapid delivery is the definitive treatment; concurrent 1:1:1 (RBC:FFP:platelet) massive transfusion protocol; fibrinogen concentrate (3-4 g IV) preferred over FFP for targeted fibrinogen correction in obstetric hemorrhage
- **Purpura fulminans:** Protein C-depleted DIC → gangrene of extremities; protein C concentrate + anticoagulation; may require limb amputation if already gangrenous

## Connections

- `connects-to` → **[Fibrinogen](../../03-molecular/fibrinogen/README.md)** — Fibrinogen is consumed in DIC by uncontrolled thrombin generation (sepsis, obstetric catastrophe, malignancy); fibrinogen <1.5 g/L in DIC is both diagnostic and a trigger for cryoprecipitate replacement; D-dimer from fibrin cross-links confirms active fibrinolysis in DIC.
- `connects-to` → **[Thrombin](../../03-molecular/thrombin/README.md)** — Systemic TF/thrombin activation is the central mechanism of DIC: infection → cytokines → TF upregulation → FVIIa/TF → FX → thrombin → fibrin microthrombi; thrombin also exhausts natural anticoagulants (protein C/S, antithrombin) → feedback amplification of coagulopathy.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Sepsis-induced DIC: endotoxin/DAMPs → NLRP3 inflammasome → IL-1β + IL-18 → endothelial TF expression → thrombin generation → fibrin; IL-1β amplifies NF-κB → PAI-1 upregulation → hypofibrinolysis → fibrin microthrombus persistence in septic DIC.
- `connects-to` → **[Antithrombin](../../03-molecular/antithrombin/README.md)** — AT is consumed in DIC by ongoing thrombin generation; AT levels <60% correlate with DIC severity (ISTH DIC score); AT concentrate studied in sepsis-DIC (KyberSept trial: no mortality benefit); low AT + prolonged PT + thrombocytopenia = DIC triad.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — DIC causes platelet consumption → thrombocytopenia; platelet count is a key ISTH DIC score parameter (score 1 if <100K, score 2 if <50K); platelet transfusion if <50K + active bleeding, or <10K; platelet activation by thrombin amplifies DIC microthrombus formation.
- `connects-to` → **[Protein C](../../03-molecular/protein-c/README.md)** — Protein C is consumed in DIC → loss of anticoagulant brake; PC deficiency → purpura fulminans (limb gangrene in septic DIC); protein C concentrate explored in severe sepsis-DIC; drotrecogin alfa (APC) withdrawn after PROWESS-SHOCK failed to show mortality benefit in sepsis-DIC.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Gram-negative sepsis is the most common DIC trigger: LPS → TLR4 → NF-κB → TF on monocytes/endothelium → systemic thrombin → fibrin microthrombi; 25-50% of severe sepsis develops overt DIC; sepsis-DIC mortality ~40-60%; antibiotics + source control are the primary treatment.
- `connects-to` → **[Essential Thrombocythemia](../essential-thrombocythemia/README.md)** — DIC and essential thrombocythemia are mirror images: DIC consumes platelets and clotting factors in runaway thrombin activation (thrombocytopenia, bleeding), while ET clonally overproduces platelets causing thrombosis — yet both can bleed via acquired von Willebrand deficiency.
- `connects-to` → **[Cytokine Storm](../cytokine-storm/README.md)** — Cytokine storm is a major driver of DIC: TNF-α, IL-1β, and IL-6 induce tissue factor on monocytes and endothelium while suppressing anticoagulants and fibrinolysis, turning inflammation into systemic microthrombosis — the coagulopathy of sepsis, severe COVID, and CAR-T toxicity.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver makes nearly every coagulation factor consumed in DIC — fibrinogen, prothrombin, protein C, antithrombin — so acute liver failure produces a DIC-like consumptive coagulopathy that is the main diagnostic mimic; factor VIII stays normal in liver disease but falls in DIC.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Endothelium is the stage for DIC: inflammatory injury makes it express tissue factor and lose its anticoagulant thrombomodulin/protein-C surface, so widespread microvascular thrombi form and consume platelets and clotting factors—turning the vessel lining procoagulant systemwide.
- `connects-to` → **[AML](../aml/README.md)** — Acute promyelocytic leukemia (APL, AML-M3) is the classic malignant cause of DIC: the leukemic promyelocytes release tissue factor and profibrinolytic activity, so fatal hemorrhage at diagnosis is a hallmark—ATRA-based treatment plus blood-product support is started urgently.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — Obstetric catastrophes are a major DIC trigger via the placenta: abruption, amniotic-fluid embolism, retained dead fetus and pre-eclampsia release tissue factor into the maternal circulation, igniting consumptive coagulopathy—so delivery and source control are central.
- `connects-to` → **[Thrombotic thrombocytopenic purpura](../thrombotic-thrombocytopenic-purpura/README.md)** — DIC and TTP both cause thrombocytopenia with microthrombi but differ in coagulation: DIC consumes clotting factors and prolongs PT/PTT, while TTP from ADAMTS13 deficiency leaves clotting times normal—normal coagulation amid a microangiopathy points to TTP.
- `connects-to` → **[Pancreatic cancer](../pancreatic-cancer/README.md)** — Pancreatic and other mucinous adenocarcinomas are a classic chronic cause of DIC: tumor mucin and tissue factor continuously activate coagulation (Trousseau syndrome), producing migratory thrombophlebitis and consumptive coagulopathy—often the first clue to an occult cancer.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — DIC shears red cells passing through fibrin-laden microvasculature: the strands fragment erythrocytes into schistocytes, producing a microangiopathic hemolytic anemia on the film—a clue, alongside low platelets and prolonged clotting, to consumptive coagulopathy.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — The kidney is an early DIC casualty: widespread microthrombi clog glomerular capillaries while consumption of clotting factors causes bleeding, so acute kidney injury is a common, prognostically important feature of disseminated intravascular coagulation.
- `connects-to` → **[Von Willebrand Factor](../../03-molecular/von-willebrand-factor/README.md)** — DIC must be separated from VWF/ADAMTS13 disorders like TTP: both consume platelets and shear red cells, but DIC also consumes clotting factors (low fibrinogen, high D-dimer) whereas TTP spares them—the coagulation profile, not the smear alone, distinguishes them.
- `connects-to` → **[Immune Thrombocytopenia](../immune-thrombocytopenia/README.md)** — DIC and immune thrombocytopenia both lower platelets by different mechanisms: DIC consumes platelets in widespread clotting (with abnormal coagulation tests), while ITP destroys them via autoantibodies with normal clotting—so coagulation studies separate them.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Neutrophils help ignite DIC through immunothrombosis: in sepsis they release neutrophil extracellular traps that activate clotting on the vessel wall, fusing the inflammatory and coagulation cascades that drive disseminated microthrombi and consumption of clotting factors.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — The lung is a frequent casualty of DIC: widespread microthrombi clog the pulmonary microvasculature while consumed clotting factors cause alveolar hemorrhage, so DIC contributes to the ARDS and respiratory failure of severe sepsis.
- `connects-to` → **[Malaria](../malaria/README.md)** — Severe falciparum malaria is a classic infectious trigger of DIC: parasitized red cells and inflammation activate coagulation and damage endothelium, so the bleeding and microthrombi of DIC complicate the deadliest form of malaria.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement and coagulation amplify each other in DIC: activated complement (C3 and beyond) promotes tissue factor and platelet activation while clotting enzymes cleave complement, so this crosstalk intensifies the runaway clotting of severe sepsis.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages help ignite DIC: in sepsis and cancer, monocytes and macrophages express tissue factor that triggers systemic coagulation, so these immune cells link inflammation to the widespread microthrombi that consume clotting factors.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — DIC threatens the brain at both extremes: microthrombi cause small strokes while consumed clotting factors invite intracranial hemorrhage, so altered mental status in a critically ill patient can signal cerebral involvement of this clotting-bleeding paradox.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Clotting in DIC runs on calcium—factor IV: calcium ions are an essential cofactor at multiple steps of the cascade, and the massive transfusions used to treat severe DIC can bind calcium and drop its level, worsening bleeding.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — DIC can destroy the adrenal glands (Waterhouse-Friderichsen): in meningococcal sepsis, widespread clotting causes bilateral adrenal hemorrhage, triggering sudden adrenal failure and shock on top of the coagulopathy.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — DIC shreds red cells and spills hemoglobin: fibrin strands strung across small vessels slice passing red cells (microangiopathic hemolysis), producing schistocytes and free hemoglobin that can itself injure the kidneys.
- `connects-to` → **[TNF-α (Tumor Necrosis Factor-alpha)](../../03-molecular/tnf-alpha/README.md)** — TNF-alpha lights the fuse of sepsis-driven DIC: it induces tissue factor on monocytes and endothelium, igniting the clotting cascade throughout the circulation, the inflammation-to-coagulation link that turns infection into widespread microthrombosis.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — DIC can choke the heart's small vessels: microthrombi scattered through the coronary microcirculation, plus the bleeding and shock of the syndrome, strain the heart and add cardiac injury to its multi-organ damage.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — DIC starves organs of oxygen with countless tiny clots: fibrin microthrombi plug small vessels, cutting oxygen delivery to kidney, lung and brain, so tissue hypoxia and organ failure—not just bleeding—drive its high mortality.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — DIC drives the blood acidic: as microthrombi choke off perfusion and shock sets in, starved tissues pour out lactic acid, so a falling pH marks the metabolic acidosis of advancing multi-organ failure.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — DIC ravages the skin: widespread microthrombi and consumed clotting factors cause purpura fulminans—dark patches of hemorrhagic skin necrosis—alongside bruising, a dramatic visible sign of the coagulation chaos.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — DIC is a consumptive state the marrow races to refill: as clotting devours platelets and cells, the bone marrow ramps up production, but it cannot keep pace, leaving the low counts that fuel bleeding.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — DIC is a lab diagnosis, but imaging finds its cause and toll: CT photons reveal the sepsis source, cancer or placental catastrophe driving it, and the organ infarcts from its microthrombi.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — DIC clogs the kidney's filters: microthrombi lodge in the glomeruli while consumption and schistocytes mount, causing the acute kidney injury that often accompanies the coagulation chaos.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Complement fuels DIC's storm: C5a from the activated cascade inflames the endothelium and drives tissue factor, the crosstalk between complement and coagulation that worsens the clotting.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows DIC shredding the blood: fibrin strands strung across small vessels slice passing red cells into the helmet-shaped schistocytes of microangiopathic hemolysis, while platelet-fibrin microthrombi plug the capillaries.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — DIC's microthrombi can starve the gut: clots seeded throughout the mesenteric microvasculature cut off the bowel's blood supply, causing ischemia and bleeding amid the body-wide clotting-and-hemorrhage paradox.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — The spleen takes its share of DIC's clots: microinfarcts pepper it as the widespread microthrombosis lodges in its small vessels, one of the many organs silently injured during the consumptive coagulopathy.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — DIC strikes the brain both ways: microthrombi infarct it while the consumed clotting factors let it bleed, so altered consciousness, focal deficits, and intracranial hemorrhage all complicate the coagulopathy.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Obstetric catastrophes are classic triggers: placental abruption, amniotic fluid embolism, retained dead fetus, and HELLP all flood the blood with tissue factor, igniting DIC in pregnancy and childbirth.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — The eye bleeds and clots in miniature: DIC produces retinal and subconjunctival hemorrhages and microvascular occlusions, a window onto the simultaneous bleeding and thrombosis playing out body-wide.
- `connects-to` → **[Prostate Cancer](../prostate-cancer/README.md)** — Metastatic prostate cancer drives a bleeding-type DIC: the tumor releases plasminogen activators that ignite excess fibrinolysis, so unlike most clot-heavy DIC it presents with oozing and bruising — a hyperfibrinolytic state needing its own tailored treatment.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — Severe acute pancreatitis can set off DIC: leaking pancreatic enzymes and the systemic inflammation they unleash activate the clotting cascade body-wide, one of the noninfectious triggers of the consumptive coagulopathy.
- `connects-to` → **[Stroke](../stroke/README.md)** — DIC strikes the brain both ways: showers of microthrombi cause scattered ischemic strokes while the consumed clotting factors invite intracerebral hemorrhage, the combination behind the confusion and focal deficits of severe cases.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Inflammation flips on the clotting switch: NF-κB activation in sepsis drives tissue-factor expression on monocytes and endothelium, the molecular trigger that launches the runaway coagulation of DIC.
- `connects-to` → **[Acute Lymphoblastic Leukemia](../all/README.md)** — Acute leukemia bleeds as it clots: leukemic cells — most dramatically in acute promyelocytic leukemia, and at presentation or induction in ALL — release procoagulants that set off DIC, a hematologic emergency at diagnosis.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — Microthrombi can starve the bowel: DIC clogs the small-vessel circulation of the gut, causing the ischemia and bleeding that add an abdominal catastrophe to its multi-organ failure.
- `connects-to` → **[Neisseria meningitidis](../../../02-pathogen/02-bacteria/neisseria-meningitidis/README.md)** — Meningococcus triggers the most vivid DIC: Neisseria meningitidis endotoxin sets off purpura fulminans with skin necrosis and Waterhouse-Friderichsen adrenal hemorrhage, a fulminant DIC that can kill within hours.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Contact activation links clotting to shock: the same surface activation that feeds DIC's coagulation also generates bradykinin, whose vasodilation and capillary leak deepen the hypotension of the underlying sepsis.
- `connects-to` → **[Dengue Fever](../dengue-fever/README.md)** — Severe dengue clots and bleeds at once: the viral hemorrhagic fever activates coagulation while consuming platelets and factors, so DIC underlies the bleeding and shock of its critical phase.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Microthrombi shut down the kidney: fibrin clots clogging the glomerular capillaries cause acute kidney injury and, in severe cases, renal cortical necrosis that can leave lasting chronic kidney disease.
- `connects-to` → **[Acute Respiratory Distress Syndrome](../../06-organ/ards/README.md)** — The lungs fill with microclots and fluid: pulmonary microthrombi and the shared sepsis inflammation make DIC a frequent companion of acute respiratory distress syndrome, each worsening the other.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Beyond the microclots, large veins can clot too: the systemic hypercoagulable drive of DIC raises the risk of macrovascular venous thromboembolism even as consumption of factors paradoxically causes bleeding.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Microthrombi and shock stun the heart: the myocardial microvascular clotting and profound hypotension of DIC's underlying critical illness impair cardiac function, contributing to acute heart failure.
- `connects-to` → **[Paroxysmal Nocturnal Hemoglobinuria](../pnh/README.md)** — A hemolytic disorder that can tip into it: the complement-driven hemolysis and intense thrombotic state of paroxysmal nocturnal hemoglobinuria can precipitate or overlap with DIC during severe crises.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Surviving the catastrophe leaves a mark: patients who survive the multiorgan failure and ICU course in which DIC arises carry the depression and cognitive sequelae of the post-intensive-care syndrome.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Microthrombi kill tissue and leave wounds: DIC's small-vessel clotting causes purpura fulminans and limb gangrene, sometimes requiring amputation, leaving major wounds that heal poorly amid critical illness.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Ischemic limb loss leaves lasting pain: the digital and limb gangrene of severe DIC can require amputation, producing chronic stump and phantom-limb neuropathic pain in survivors.
- `connects-to` → **[PTSD](../ptsd/README.md)** — A life-threatening ICU crisis can scar the mind: surviving the catastrophic bleeding, clotting and intensive care in which DIC occurs frequently leaves post-traumatic stress.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It is dramatically written on the skin: DIC causes widespread petechiae, ecchymoses and oozing from puncture sites, and in its severe form purpura fulminans with skin necrosis and digital gangrene.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Microthrombi and bleeding hit the lungs: DIC contributes to acute respiratory distress syndrome through diffuse microvascular thrombosis and can cause pulmonary haemorrhage.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It bleeds and starves the gut: DIC causes gastrointestinal haemorrhage from consumed clotting factors and platelets, while microthrombi cause bowel ischaemia and hepatic dysfunction.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Microthrombi clog the kidney: DIC deposits fibrin in the renal microvasculature, causing acute kidney injury and, in severe cases, bilateral renal cortical necrosis.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It both clots and bleeds the brain: cerebral microthrombi and intracranial haemorrhage from consumed platelets and clotting factors cause encephalopathy, stroke and bleeding.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It can destroy the adrenals: bilateral adrenal haemorrhage — Waterhouse-Friderichsen syndrome — complicates meningococcal DIC, causing acute adrenal failure.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — It clots and bleeds in the vessels at once: DIC scatters microthrombi that occlude small vessels while consuming clotting factors, causing both ischaemia and haemorrhage with circulatory collapse.
- `connects-to` → **[Immune System](../immune-system/README.md)** — It is driven by inflammation: sepsis and cytokine release trigger DIC through tissue factor and immunothrombosis, tying coagulation tightly to the innate immune response.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It bleeds into soft tissue: consumption of platelets and clotting factors causes spontaneous bleeding into muscles and, with purpura fulminans, ischaemic limb necrosis.
- `connects-to` → **[Staphylococcus aureus](../../../02-pathogen/02-bacteria/staphylococcus-aureus/README.md)** — Sepsis and toxic shock ignite it: Staphylococcus aureus bacteraemia and toxic-shock syndrome are major triggers of DIC, the bacterial sepsis driving uncontrolled coagulation.
- `connects-to` → **[aHUS](../ahus/README.md)** — A thrombotic-microangiopathy to distinguish: DIC must be told apart from aHUS and TTP, which also consume platelets and shear red cells but spare the clotting factors that DIC depletes.
- `connects-to` → **[Heparin-Induced Thrombocytopenia](../heparin-induced-thrombocytopenia/README.md)** — A paradoxical clotting comparator: like DIC, heparin-induced thrombocytopenia combines a falling platelet count with thrombosis, but through antibody-mediated platelet activation rather than consumption.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Acute leukaemia both causes and cures it: acute promyelocytic leukaemia classically triggers life-threatening DIC, and treating it with ATRA and chemotherapy rapidly resolves the coagulopathy — while tumour lysis and other chemo can also provoke DIC.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — The liver makes and loses the factors: DIC microthrombi injure the hepatic lobule, and because the liver synthesises clotting factors, hepatic failure both worsens and mimics the coagulopathy of DIC.
- `connects-to` → **[Antiphospholipid Syndrome](../antiphospholipid-syndrome/README.md)** — Catastrophic APS mimics it: catastrophic antiphospholipid syndrome causes widespread small-vessel thrombosis with consumption resembling DIC, a key differential demanding anticoagulation rather than factor replacement.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Pulmonary microthrombi: fibrin microthrombi clog the alveolar capillaries in DIC, worsening the hypoxaemia and ARDS of severe sepsis and amniotic-fluid embolism.
- `connects-to` → **[Gastric Cancer](../gastric-cancer/README.md)** — Chronic compensated DIC (Trousseau): mucin-secreting adenocarcinomas like gastric and pancreatic cancer activate coagulation, causing chronic DIC and migratory thrombophlebitis.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Microthrombi injure the heart: widespread microvascular thrombosis and shock in DIC starve the myocardium, contributing to the cardiac dysfunction of multi-organ failure.
- `connects-to` → **[Neisseria meningitidis](../../../02-pathogen/02-bacteria/neisseria-meningitidis/README.md)** — Purpura fulminans: meningococcal sepsis triggers fulminant DIC with skin necrosis and bilateral adrenal haemorrhage (Waterhouse-Friderichsen), a classic and rapidly fatal infectious cause.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — Endothelium drives the consumption: DIC begins when an injured or activated endothelium of the arterial wall and capillaries exposes tissue factor, igniting the runaway clotting that consumes platelets and factors.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — COVID coagulopathy: severe COVID-19 causes a distinctive coagulopathy with very high D-dimer and microthrombi that overlaps DIC, though usually with thrombosis rather than the consumptive bleeding.
- `connects-to` → **[Ebola Virus](../../../02-pathogen/01-viruses/ebola-virus/README.md)** — Viral haemorrhagic coagulopathy: Ebola virus triggers severe DIC with consumptive coagulopathy and bleeding, a hallmark of the haemorrhagic fever it causes.
- `connects-to` → **[Streptococcus pyogenes](../../../02-pathogen/02-bacteria/streptococcus-pyogenes/README.md)** — Toxic shock and purpura: invasive group A streptococcal infection and toxic shock syndrome drive DIC and purpura fulminans through overwhelming systemic inflammation.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — Inflammation-coagulation crosstalk: IL-6 induces tissue factor and fibrinogen and amplifies the cytokine response that ignites DIC in sepsis, linking inflammation to clotting.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Tissue-factor induction: IL-1β from activated monocytes upregulates endothelial and monocyte tissue factor, a key inflammatory trigger of the systemic coagulation in DIC.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — Endothelial collapse: the widespread endothelial injury of DIC cuts protective nitric oxide, removing its antithrombotic brake and worsening microvascular thrombosis.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Microvascular constriction: injured endothelium in DIC releases endothelin-1, whose vasoconstriction compounds the microthrombi to drive the ischaemic organ failure of the syndrome.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — Immunothrombosis: S100A8/A9-rich neutrophil extracellular traps provide a scaffold and trigger for the widespread microthrombi of DIC, linking the innate immune response of sepsis to its consumptive coagulopathy.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — Endotoxin trigger: TLR4 sensing of bacterial LPS in sepsis induces tissue factor on monocytes and endothelium, the initiating signal that unleashes the systemic coagulation of DIC.
- `connects-to` → **[PF4](../../03-molecular/pf4/README.md)** — Platelet consumption: PF4 released from the platelets massively activated and consumed in DIC marks the platelet activation that, with coagulation-factor depletion, produces the bleeding-thrombosis paradox.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — CCL2 recruits and activates the monocytes whose tissue-factor expression is the principal initiator of the systemic coagulation activation that drives sepsis-induced DIC—linking the chemokine response to the coagulopathy.
- `connects-to` → **[RAGE](../../03-molecular/rage/README.md)** — HMGB1 signaling through RAGE sustains the thromboinflammation of DIC, a late DAMP mediator that perpetuates the coagulation activation beyond the initial sepsis, trauma, or obstetric trigger.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Mitochondrial DNA released in sepsis and trauma activates cGAS-STING, contributing the innate-immune signaling that feeds the immunothrombosis underlying the microvascular clotting of DIC.
- `connects-to` → **[ADAMTS13](../../03-molecular/adamts13/README.md)** — The inflammatory consumption of ADAMTS13 in sepsis leaves uncleaved ultra-large von Willebrand factor multimers that capture platelets, adding a microvascular thrombotic mechanism to the tissue-factor-driven coagulopathy of DIC.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Inflammatory injury drives caspase-3-mediated apoptosis of endothelial cells, exposing the procoagulant tissue factor and basement membrane that ignite and sustain the disseminated clotting of DIC.
- `connects-to` → **[Xanthine Oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Xanthine-oxidase-derived reactive oxygen species damage the endothelium in the systemic inflammation that triggers DIC, shifting the vessel wall to a procoagulant state that feeds the microvascular thrombosis.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — Ang-2 released from activated, injured endothelium in sepsis-associated DIC destabilizes the vasculature, amplifying the endothelial dysfunction that triggers and sustains the coagulopathy.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a acting through C5aR1 (complement C5 already mapped) induces tissue-factor expression and amplifies the thromboinflammation that drives the microvascular clotting of DIC.
- `connects-to` → **[Thrombopoietin](../../03-molecular/thrombopoietin/README.md)** — The consumptive thrombocytopenia central to DIC drives a compensatory thrombopoietin response, reflecting the accelerated platelet turnover as clots form throughout the microvasculature.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — In sepsis-induced DIC — its commonest cause — TLR-MyD88-NF-κB signaling (TLR4 and NF-κB already mapped) couples infection to the tissue-factor expression and inflammation that ignite systemic coagulation.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — IL-6 signaling through JAK-STAT (IL-6 already mapped) amplifies the cytokine response and drives the hepatic acute-phase and procoagulant changes of DIC.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — VEGF-mediated endothelial activation and permeability, alongside the angiopoietin-Tie2 axis (already mapped), contributes to the endothelial injury underlying the microvascular thrombosis of DIC.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — C5a acting on C5aR (C5aR1 mapped) and platelet agonists engage ERK-MAPK, amplifying the cellular activation that propagates DIC.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Endothelial and platelet PI3K-AKT signaling shapes the procoagulant, activated phenotype that drives the widespread microthrombosis of DIC.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 promotes the neutrophil-extracellular-trap-driven thromboinflammation that fuels disseminated intravascular coagulation.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling transduces the inflammatory cytokine response that drives the tissue-factor expression and procoagulant state of disseminated intravascular coagulation.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K-AKT signaling (AKT already mapped) in platelets and endothelium supports the activated, procoagulant phenotype of disseminated intravascular coagulation.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the interferon component of the systemic inflammation (often sepsis-driven) underlying disseminated intravascular coagulation.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO downstream of PI3K-AKT signaling (AKT and PIK3CA already mapped) regulates the endothelial activation balance disrupted in the thromboinflammation of disseminated intravascular coagulation.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α in the hypoxic, microthrombosed tissues amplifies the endothelial dysfunction of disseminated intravascular coagulation.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling drives the organ fibrosis that can follow the microvascular ischemic injury of disseminated intravascular coagulation.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the platelet-activation and inflammatory signaling that drive the systemic coagulation activation of disseminated intravascular coagulation.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR signaling in activated endothelium and immune cells participates in the immunothrombosis underlying disseminated intravascular coagulation.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-bearing cytotoxic lymphocytes contribute to the endothelial injury that triggers the coagulation cascade in sepsis-associated disseminated intravascular coagulation.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the platelet activation and endothelial responses of disseminated intravascular coagulation.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked endothelial metabolic signaling modulates the vascular homeostasis disrupted in disseminated intravascular coagulation.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte recruitment contributes to the thrombo-inflammation of disseminated intravascular coagulation.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the endothelial and immune-cell responses relevant to the thrombo-inflammation of disseminated intravascular coagulation.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic modulation of the coagulation and endothelial gene expression relevant to disseminated intravascular coagulation.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the endothelial and leukocyte interactions of the thrombo-inflammation of disseminated intravascular coagulation.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the endothelial activation and thromboinflammation of disseminated intravascular coagulation.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the thromboinflammation of disseminated intravascular coagulation.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the endothelial and inflammatory gene programs of disseminated intravascular coagulation.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Lactic acidosis: the microvascular thrombosis and shock of severe DIC starve tissues of oxygen (already mapped), forcing anaerobic metabolism that generates protons and lactate, so a worsening metabolic acidosis tracks the severity of the coagulopathy.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Multi-organ injury: the widespread microthrombi of DIC injure organs including the heart, and troponin elevation marks the myocardial damage that is part of the multi-organ failure driving its high mortality.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Tissue hypoxia: fibrin microthrombi occlude the microcirculation in DIC, cutting off oxygen delivery and causing the ischaemic organ dysfunction, from kidneys (already mapped) to skin, that defines its thrombotic phase.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Cytokine balance: the anti-inflammatory cytokine IL-10 counters the TNF, IL-1 and IL-6 (already mapped) that ignite the coagulation of sepsis-induced DIC, and the balance between them shapes the severity of the coagulopathy.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Inflammatory iron handling: the IL-6 surge (already mapped) of the sepsis that commonly triggers DIC raises hepcidin, sequestering iron and contributing to the anaemia (haemoglobin already mapped) of the critical illness.
- `connects-to` → **[Adrenomedullin](../../03-molecular/adrenomedullin/README.md)** — Endothelial vasodilation: adrenomedullin rises with the endothelial activation (already mapped) of the sepsis and DIC, contributing to the vasodilation and vascular leak of shock, and is studied as a biomarker and therapeutic target.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Thromboxane and inflammation: the prostaglandin/thromboxane balance on the activated platelets (already mapped) and endothelium shifts toward the prothrombotic thromboxane, part of the platelet activation and inflammation of DIC.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Platelet serotonin: serotonin released from the activated, consumed platelets (PF4 already mapped) causes vasoconstriction and amplifies platelet aggregation in the widespread microthrombi of DIC.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Haemolysis and iron: the microangiopathic haemolysis of DIC fragments red cells (haemoglobin already mapped) releasing iron, while the inflammatory hepcidin (already mapped) sequesters it, part of the anaemia of the critical illness.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Contact-pathway zinc: zinc released from the activated, consumed platelets (PF4 already mapped) promotes the contact pathway and fibrin (fibrinogen already mapped) formation, adding to the coagulation activation of DIC.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Sepsis-severity adipokine: resistin, a pro-inflammatory adipokine, rises markedly in the sepsis (already mapped) that commonly triggers DIC, a marker of the severity of the inflammatory drive behind the consumptive coagulopathy.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Vascular permeability: histamine from the activated mast cells and basophils adds to the vascular permeability (bradykinin already mapped) and the vasodilatory shock of the severe conditions that trigger DIC.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Inflammatory adipokine: leptin, with resistin (already mapped), rises in the acute inflammation (IL-6 already mapped) of the sepsis (already mapped) and severe conditions that trigger the consumptive coagulopathy of DIC.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Adipokine axis: adiponectin, with leptin and resistin (already mapped), completes the adipokine axis of the systemic inflammation driving the disseminated intravascular coagulation.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate immunothrombosis: type-I interferon is part of the innate-immune signalling of the viral and inflammatory (IL-6 already mapped) triggers of DIC, contributing to the immunothrombotic host response.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Immunothrombosis NETs: the neutrophils release the NETs (S100A8/9 already mapped) that scaffold the microthrombi, the immunothrombosis driving the disseminated intravascular coagulation.
- `connects-to` → **[AML](../aml/README.md)** — APL emergency: the acute promyelocytic leukaemia (a subtype of AML) classically presents with the severe DIC (the procoagulant granules), a haematological emergency.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Microthrombotic AKI: the fibrin microthrombi (thrombin already mapped) lodge in the kidney, causing the acute kidney injury and the organ dysfunction of DIC.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 inflammation: the IFN-γ of the T cells is the type-II interferon arm of the inflammatory drive (IL-6 and TNF already mapped) that, via the immunothrombosis, activates the coagulation of DIC.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the systemic inflammation underlying DIC.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Type-2 counter-arm: IL-4 is the type-2 cytokine arm counter-balancing the pro-inflammatory (IL-6 and TNF already mapped) drive of the coagulopathy of DIC.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 arm: IL-13, with IL-4 (already mapped), completes the type-2 immune arm counter-balancing the pro-inflammatory drive of the systemic coagulopathy of DIC.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune milieu of the systemic inflammation underlying DIC.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the systemic inflammation (IL-6 and TNF already mapped) that drives the immunothrombosis of DIC.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) whose consumption and dysregulation amplify the complement–coagulation crosstalk of DIC.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Contact/complement regulation: the C1-esterase inhibitor regulates both the classical complement and the contact (intrinsic-coagulation, bradykinin already mapped) pathways, a key brake at the complement–coagulation interface consumed in DIC.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Haemolytic iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the microangiopathic haemolysis and the inflammation of DIC.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Thromboinflammation: osteopontin, released by the activated platelets (already mapped), is a matricellular mediator linking the inflammation to the microthrombosis of DIC.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Vascular mast cells: the mast cells contribute to the vascular permeability and, through tissue-factor and heparin release, to the coagulation-anticoagulation imbalance of DIC.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — Adaptive immunothrombosis: the CD4 T-helper cells contribute to the inflammatory drive of the immunothrombosis that underlies the sepsis-associated DIC.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-DIC axis: TSLP, from the septic or inflammatory epithelium, primes dendritic cells and mast cells (already mapped) and amplifies the cytokine storm (already mapped) and the systemic inflammatory response that triggers disseminated intravascular coagulation.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — EPO-DIC axis: erythropoietin, upregulated by the HIF-1α (already mapped) hypoxia of DIC-related multi-organ injury, mobilises erythroid progenitors and modulates macrophage (already mapped) polarisation, linking the anaemia of DIC to the inflammatory coagulopathy.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Remodelling axis: periostin, released from the injured endothelium (already mapped) and fibroblasts during the DIC-related vascular injury, contributes to the tissue remodelling and repair after the consumptive coagulopathy.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian-coagulopathy axis: melatonin, via MT1/MT2 receptors and its antioxidant activity, modulates the oxidative stress of the systemic inflammatory response (cytokine-storm already mapped) and the endothelial injury that triggers DIC.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Sex-hormone coagulation axis: testosterone, via androgen receptors on endothelium (already mapped) and platelets (already mapped), modulates the coagulation cascade and the sex-differential thrombotic risk of the consumptive coagulopathy of DIC.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Immunostimulatory prolactin axis: prolactin, via PRL receptors on T cells (already mapped) and macrophages (already mapped), amplifies the cytokine production and the systemic inflammatory activation that can trigger the consumptive coagulopathy of DIC.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — DIC oxytocin: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates the systemic inflammatory cascade; oxytocin deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) coagulopathic cascade of DIC.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — DIC vasopressin: vasopressin, via V2R on endothelium (already mapped) and macrophages (already mapped), modulates vascular tone and haemostasis; vasopressin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) consumptive coagulopathy of DIC.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — DIC selenium: selenium, via selenoprotein antioxidant activity in macrophages (already mapped) and neutrophils (already mapped), suppresses the oxidative amplification of the NF-κB (already mapped) and TNF-α (already mapped) systemic inflammatory cascade of DIC.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^levi-2009-dic-review]: Levi M, Toh CH, Thachil J, Watson HG. Guidelines for the diagnosis and management of disseminated intravascular coagulation. *Br J Haematol.* 2009;145(1):24-33. [doi:10.1111/j.1365-2141.2009.07600.x](https://doi.org/10.1111/j.1365-2141.2009.07600.x) · [PubMed 19222477](https://pubmed.ncbi.nlm.nih.gov/19222477/)
[^levi-2018-dic-lancet]: Levi M, Scully M. How I treat disseminated intravascular coagulation. *Blood.* 2018;131(8):845-854. [doi:10.1182/blood-2017-10-804096](https://doi.org/10.1182/blood-2017-10-804096) · [PubMed 29255070](https://pubmed.ncbi.nlm.nih.gov/29255070/)
[^taylor-2001-isth-dic-score]: Taylor FB Jr, Toh CH, Hoots WK, et al. Towards definition, clinical and laboratory criteria, and a scoring system for disseminated intravascular coagulation. *Thromb Haemost.* 2001;86(5):1327-1330. [doi:10.1055/s-0037-1616068](https://doi.org/10.1055/s-0037-1616068) · [PubMed 11816725](https://pubmed.ncbi.nlm.nih.gov/11816725/)
