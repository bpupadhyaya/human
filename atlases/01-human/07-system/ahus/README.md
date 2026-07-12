---
schema: human-scale-entry/v1
id: ahus
name: Atypical HUS
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Atypical hemolytic uremic syndrome (aHUS) is a complement-mediated thrombotic microangiopathy (MAHA + thrombocytopenia + AKI); Factor H mutations are most common (20-30%); uncontrolled alternative pathway at renal endothelium → microthrombi. Eculizumab is standard of care."
aliases: ["aHUS", "atypical HUS", "atypical hemolytic uremic syndrome", "complement-mediated TMA", "CFH-HUS", "HUS", "thrombotic microangiopathy complement"]
sources:
  - id: fakhouri-2017-ahus-lancet
    type: peer-reviewed
    cite: "Fakhouri F, Zuber J, Frémeaux-Bacchi V, Loirat C. Haemolytic uraemic syndrome. Lancet. 2017;390(10095):681-696."
    doi: "10.1016/S0140-6736(17)30062-4"
    pmid: "28242109"
    url: "https://doi.org/10.1016/S0140-6736(17)30062-4"
  - id: legendre-2013-eculizumab-ahus-nejm
    type: peer-reviewed
    cite: "Legendre CM, Licht C, Muus P, et al. Terminal complement inhibitor eculizumab in atypical hemolytic-uremic syndrome. N Engl J Med. 2013;368(23):2169-2181."
    doi: "10.1056/NEJMoa1208981"
    pmid: "23738544"
    url: "https://doi.org/10.1056/NEJMoa1208981"
  - id: goodship-2017-ahus-consensus
    type: clinical-guideline
    cite: "Goodship TH, Cook HT, Fakhouri F, et al. Atypical hemolytic uremic syndrome and C3 glomerulopathy: conclusions from a 'Kidney Disease: Improving Global Outcomes' (KDIGO) Controversies Conference. Kidney Int. 2017;91(3):539-551."
    doi: "10.1016/j.kint.2016.10.005"
    pmid: "28062089"
    url: "https://doi.org/10.1016/j.kint.2016.10.005"
cross_links:
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "CFH mutations (SCR19-20) are the most common cause of aHUS (~20-30%); Factor H regulates alternative C3 convertase on renal endothelial surfaces; anti-CFH autoantibodies (CFHR1-CFHR3 deletion) cause aHUS in ~6-10%; eculizumab/ravulizumab target downstream C5."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Uncontrolled alternative C3 convertase (C3bBb) from CFH/CFI/CD46 defects → persistent C3 consumption → hypocomplementemia; serum C3 is low-normal in many aHUS cases; C3 nephritic factor (C3NeF) stabilizes C3bBb → C3 glomerulopathy (related complement-mediated nephropathy)."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Uncontrolled alternative complement (from CFH/CFI mutations) generates C5 convertase → C5a (neutrophil priming, endothelial injury) + C5b-9 (MAC → TMA); eculizumab (anti-C5 mAb) and ravulizumab block C5 → normalize platelets and renal function in >80% of aHUS patients."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "aHUS causes progressive CKD from repeated TMA episodes; ~50% of untreated patients reach ESRD within 1 year; eculizumab/ravulizumab prevent and partially reverse renal injury; renal transplant in aHUS requires continued C5 inhibition to prevent TMA recurrence in the allograft."
  - target: 01-human/03-molecular/adamts13
    relation: connects-to
    note: "ADAMTS13 activity is the first test to exclude TTP from the aHUS differential; in TMA workup, ADAMTS13 <10% = TTP → plasma exchange + caplacizumab, NOT eculizumab; ADAMTS13 ≥10% + complement workup → aHUS; the distinction is critical since treatments are non-interchangeable."
  - target: 01-human/07-system/thrombotic-thrombocytopenic-purpura
    relation: connects-to
    note: "TTP (ADAMTS13 <10%) is the primary differential diagnosis of aHUS; both cause TMA (MAHA + thrombocytopenia + AKI) but TTP is treated with plasma exchange + caplacizumab and aHUS with eculizumab; TTP tends to spare the kidneys more; aHUS tends to dominate with AKI over neuro."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "The kidney is aHUS's main target: uncontrolled alternative complement strikes the glomerular endothelium, seeding microthrombi that occlude capillaries → acute kidney injury and, over repeated episodes, CKD and ESRD; aHUS recurs in transplants unless C5 inhibition continues."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "aHUS is a disease of the glomerular endothelial cell: because mutant Factor H cannot be recruited to the cell surface, the alternative pathway runs unchecked there → MAC sublytically injures the endothelium → VWF release and platelet adhesion → the microthrombi of TMA."
  - target: 02-pathogen/02-bacteria/escherichia-coli
    relation: connects-to
    note: "aHUS must be separated from typical HUS caused by Shiga-toxin-producing E. coli: STEC-HUS follows bloody diarrhoea, hits young children, is usually self-limited, and does not respond to eculizumab — whereas complement-driven aHUS does, making the stool toxin test a key fork."
  - target: 01-human/07-system/gvhd
    relation: connects-to
    note: "aHUS and transplant-associated TMA (TA-TMA) in GVHD overlap: both injure endothelium and activate complement to drive microvascular thrombosis with schistocytes, thrombocytopenia and kidney injury; complement variants predispose to TA-TMA, and C5 inhibition can treat both."
  - target: 01-human/07-system/pnh
    relation: connects-to
    note: "aHUS and PNH are the archetypal complement-mediated diseases treated by C5 blockade: PNH lacks GPI-anchored complement regulators causing hemolysis and thrombosis, while aHUS has uncontrolled alternative-pathway activation on endothelium causing TMA; eculizumab transformed both."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "aHUS is a thrombotic microangiopathy that consumes platelets: complement-injured endothelium triggers platelet adhesion and microthrombi in the renal microvasculature, dropping the count while sparing large vessels; consumed platelets and schistocytes are diagnostic clues."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "aHUS shreds red cells like all thrombotic microangiopathies: erythrocytes passing through complement-damaged, microthrombus-laden glomerular capillaries fragment into schistocytes, producing the hemolytic anemia that, with thrombocytopenia and AKI, defines the TMA triad."
  - target: 01-human/07-system/disseminated-intravascular-coagulation
    relation: connects-to
    note: "aHUS and DIC both cause thrombocytopenia with microthrombi but differ in coagulation: DIC consumes clotting factors with prolonged PT/PTT, while aHUS is complement-driven with normal clotting times—so normal coagulation amid a microangiopathy points to aHUS."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "Lupus can trigger a secondary thrombotic microangiopathy resembling aHUS: complement activation and antiphospholipid antibodies in SLE injure endothelium and cause a TMA, so distinguishing aHUS from lupus or TTP guides eculizumab vs immunosuppression vs plasma exchange."
  - target: 01-human/07-system/heparin-induced-thrombocytopenia
    relation: connects-to
    note: "aHUS and HIT both cause thrombocytopenia with thrombosis but by different mechanisms: aHUS is uncontrolled complement attacking endothelium, while HIT is PF4-heparin antibodies activating platelets—both consume platelets while clotting, needing different treatment."
  - target: 01-human/07-system/immune-thrombocytopenia
    relation: connects-to
    note: "aHUS and immune thrombocytopenia both lower platelets but differ fundamentally: aHUS consumes platelets in complement-driven microthrombi, while ITP is isolated antibody-mediated platelet destruction—the smear and renal function separate them."
  - target: 01-human/07-system/malaria
    relation: connects-to
    note: "aHUS and severe malaria can both present as thrombotic microangiopathy: malaria's infected red cells and inflammation damage the microvasculature much as complement does in aHUS—so in endemic areas falciparum infection enters the differential of TMA."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "aHUS strikes the glomerulus hardest: uncontrolled complement injures glomerular endothelium, triggering the thrombotic microangiopathy that shears red cells and clogs capillaries—so renal failure with microangiopathic hemolysis is the disease's hallmark."
  - target: 01-human/03-molecular/von-willebrand-factor
    relation: connects-to
    note: "aHUS shares thrombotic-microangiopathy machinery with TTP via von Willebrand factor: complement-injured endothelium releases ultralarge VWF multimers that snare platelets into microthrombi—the same VWF that ADAMTS13 deficiency unleashes in TTP."
  - target: 01-human/04-cellular/podocyte
    relation: connects-to
    note: "aHUS injures the glomerular filter including its podocytes: complement-driven endothelial damage and microthrombi disrupt the filtration barrier, contributing to the proteinuria, hematuria and progressive renal failure that mark the disease."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "Pregnancy can trigger atypical HUS: the complement stress of pregnancy and especially the postpartum period unmasks aHUS in women with regulatory mutations, so a thrombotic microangiopathy around delivery must be distinguished from pre-eclampsia and HELLP."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "Severe hypertension and aHUS form a vicious circle: complement-driven microvascular injury in the kidney drives malignant hypertension, and the high pressure further shears endothelium—so accelerated hypertension can both trigger and result from the microangiopathy."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "aHUS is not confined to the kidney—it can strike the brain: complement-mediated microthrombi in cerebral vessels cause seizures, confusion, and stroke, so neurological signs in a thrombotic microangiopathy mark severe, extrarenal aHUS needing urgent complement blockade."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "aHUS is driven by runaway complement reaching C5a: uncontrolled activation cleaves C5 to C5a, which through its receptor C5aR1 inflames and injures endothelium—why C5-blocking eculizumab transformed this once-lethal disease."
  - target: 01-human/03-molecular/thrombin
    relation: connects-to
    note: "aHUS is a thrombotic microangiopathy fueled by thrombin: complement-injured endothelium becomes prothrombotic, generating thrombin and platelet-fibrin microthrombi that shred red cells and clog the kidney's small vessels."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Complement's C5a recruits neutrophils that worsen aHUS: drawn to the activated endothelium, neutrophils release enzymes and oxidants that amplify the microvascular injury, linking the complement defect to the destructive inflammation in the kidney."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "aHUS is the 'H' of hemolytic-uremic: uncontrolled complement injures small-vessel endothelium, and the fibrin and platelet strands shear passing red cells (microangiopathic hemolysis), spilling hemoglobin and producing schistocytes."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "aHUS damages the kidney enough to raise potassium: complement-driven microthrombi block glomerular capillaries, causing the acute kidney injury that—with hemolysis releasing potassium—drives dangerous hyperkalemia needing urgent care."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages clean up aHUS's destroyed red cells: as complement shears erythrocytes, splenic and hepatic macrophages clear the damaged cells and free hemoglobin, the reticuloendothelial cleanup behind the hemolytic anemia of the disease."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "aHUS can strike the heart: the same complement-driven microthrombi that clog the kidney lodge in cardiac vessels, causing ischemia and cardiomyopathy, one of the extrarenal manifestations that mark severe disease."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "aHUS chokes off oxygen across organs: widespread microvascular clots block blood flow while the hemolytic anemia leaves less to carry oxygen, so tissues throughout the body are starved during an acute episode."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "aHUS can injure the pancreas: microthrombi in its small vessels cause ischemic pancreatitis and can disturb blood sugar, another extrarenal site of the thrombotic microangiopathy that defines the disease."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "aHUS is confirmed on the kidney biopsy under the microscope: thrombotic microangiopathy—fibrin clots and swollen endothelium in the glomeruli, read in light—distinguishes it from other causes of failing kidneys."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Recurrent aHUS scars the kidney: repeated thrombotic injury heals with glomerular and interstitial fibrosis, driving the chronic kidney disease that can follow even after attacks are controlled."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "aHUS can injure the gut: mesenteric microthrombi cause abdominal pain and ischemic colitis, part of the multi-organ thrombotic reach that sets it apart from a purely renal disease."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reveals aHUS's lesion in the kidney's filters: the glomerular endothelium swells and lifts off, widening the subendothelial space and trapping platelet-fibrin microthrombi — the thrombotic microangiopathy unchecked complement drives."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "The complement storm can reach the lungs: aHUS occasionally causes pulmonary thrombotic microangiopathy with hemorrhage and respiratory failure, evidence its endothelial injury is systemic, not confined to the kidney."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "aHUS can blur the eye: microthrombi and the malignant hypertension it provokes injure the retinal vessels, producing a Purtscher-like retinopathy of cotton-wool spots and hemorrhages that can threaten vision."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "aHUS reaches the brain through its tiniest vessels: microthrombi in the cerebral microcirculation injure neurons, causing the seizures, confusion, and stroke that complicate severe disease in up to half of patients."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Some aHUS is antibody-made: a subset is driven by autoantibodies against complement factor H (often with CFHR deletions), and the disease's mainstay treatment, eculizumab, is itself a monoclonal antibody that blocks C5."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The microangiopathy can scar more than the kidney: aHUS is a systemic TMA, and clots in the hepatic and mesenteric microvessels can derange the liver and bowel as part of its multi-organ reach."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Pregnancy is a classic trigger: complement-mediated aHUS often erupts in the peripartum period, especially postpartum, and must be told apart from HELLP and preeclampsia, which it can closely mimic in a sick mother."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "The damage remodels the small arteries: aHUS injures arterioles into the concentric 'onion-skin' thickening of smooth-muscle and matrix layers, the chronic vascular lesion of thrombotic microangiopathy seen on biopsy."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Microthrombi reach the brain: aHUS is not confined to the kidney — clots in the cerebral microvessels cause seizures, encephalopathy, and stroke, the CNS face of its systemic thrombotic microangiopathy."
  - target: 02-pathogen/02-bacteria/streptococcus-pneumoniae
    relation: connects-to
    note: "Pneumococcus can ignite its own HUS: the bacterium's neuraminidase strips sialic acid to expose the hidden T antigen on red cells and endothelium, triggering a thrombotic microangiopathy distinct from the usual E. coli kind."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Glomerular vessels live on VEGF: podocyte VEGF keeps the filtration endothelium healthy, so cancer drugs that block it can unleash a complement-amplified thrombotic microangiopathy that mirrors aHUS."
  - target: 01-human/07-system/systemic-sclerosis
    relation: connects-to
    note: "Scleroderma renal crisis is a TMA twin: it injures the same small renal vessels with malignant hypertension and microangiopathic hemolysis, a key differential to separate from complement-driven aHUS at the bedside."
  - target: 01-human/07-system/antiphospholipid-syndrome
    relation: connects-to
    note: "Catastrophic APS mimics it: antiphospholipid antibodies can trigger a widespread thrombotic microangiopathy with renal failure resembling aHUS, another autoimmune cause that must be excluded before settling on complement-driven disease."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It is not only a kidney disease: complement-driven microthrombi strike the brain too, causing seizures, confusion and stroke in a large share of patients — a leading extrarenal manifestation of aHUS."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Inflammation amplifies the endothelial injury: IL-6 and other cytokines released as complement attacks the vessel lining feed forward into more endothelial activation and microthrombosis, worsening the microangiopathy."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Complement switches the endothelium to attack mode through NF-κB: C5a-driven NF-κB activation makes the vessel lining procoagulant and inflamed, amplifying the microthrombosis that defines the complement-mediated microangiopathy."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "It can clot the heart's small vessels too: complement-driven microthrombi in the coronary microcirculation injure cardiomyocytes, causing the cardiomyopathy and heart attacks that are a recognized extrarenal manifestation of aHUS."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Blocking complement raises the infection stakes: the anti-C5 therapy eculizumab that controls aHUS disables the membrane attack complex, sharply increasing meningococcal infection and sepsis risk and mandating vaccination."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "It is a thrombotic state beyond the microcirculation: the complement-driven endothelial activation and platelet consumption of aHUS create a prothrombotic milieu that can throw large-vessel venous thrombi as well as the defining microthrombi."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Beyond the hemolysis, the failing kidney starves the marrow: as aHUS damages the kidney, lost erythropoietin production and chronic inflammation add a renal anemia-of-chronic-disease component on top of the microangiopathic hemolysis."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A relapsing, life-threatening disease weighs on the mind: the unpredictability of aHUS flares, dialysis dependence and lifelong complement-blocking infusions impose a heavy psychological burden and depression."
  - target: 02-pathogen/02-bacteria/neisseria-meningitidis
    relation: connects-to
    note: "Its complement-blocking cure invites meningococcus: eculizumab and ravulizumab, the mainstays of aHUS therapy, cut off the terminal complement that kills Neisseria, mandating meningococcal vaccination and prophylaxis."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Its microangiopathy reaches the heart: aHUS thrombotic microangiopathy and severe hypertension can injure the myocardium and coronary microvasculature, an extra-renal manifestation that can precipitate heart failure."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "Microvascular thrombi can pressurize the lungs: the systemic endothelial injury and thrombotic microangiopathy of aHUS can involve the pulmonary vasculature, contributing to pulmonary hypertension."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Its microthrombi injure the gut: aHUS thrombotic microangiopathy can involve the GI tract, causing pancreatitis, hepatic dysfunction, colitis and bowel ischaemia as extra-renal manifestations."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Severe microvascular thrombosis reaches the skin: extensive aHUS can cause cutaneous microvascular ischaemia with digital and skin necrosis when the thrombotic microangiopathy is widespread."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A sudden, relapsing, complement-driven disease breeds worry: the abrupt kidney-and-blood crisis, relapse risk and indefinite complement-blocking therapy of aHUS foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "It is a disease of uncontrolled complement: mutations in alternative-pathway regulators or anti-factor-H antibodies let complement attack the endothelium, which is why complement-blocking eculizumab is the treatment."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its microthrombi strike the heart: the thrombotic microangiopathy of aHUS can occlude cardiac microvessels, causing ischaemia, arrhythmia and cardiomyopathy beyond the hypertension it drives."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It can injure the pancreatic islets: thrombotic microangiopathy of the pancreatic microvasculature can impair insulin-producing islets, causing transient hyperglycaemia during an aHUS crisis."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "The kidney is its prime target: aHUS is fundamentally a renal thrombotic microangiopathy causing acute kidney injury that often progresses to end-stage failure without complement-blocking therapy."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Severe disease can flood the lungs: diffuse alveolar haemorrhage and pulmonary thrombotic microangiopathy occur in severe systemic aHUS."
  - target: 02-pathogen/02-bacteria/neisseria-meningitidis
    relation: connects-to
    note: "Its life-saving drug invites meningococcus: eculizumab blocks the terminal complement that defends against Neisseria meningitidis, so vaccination is mandatory before treating aHUS."
  - target: 02-pathogen/01-viruses/influenza-a
    relation: connects-to
    note: "Infection can flip the switch: influenza A, especially H1N1, is a recognised trigger that unmasks complement-mediated aHUS in genetically predisposed people, precipitating thrombotic microangiopathy."
  - target: 02-pathogen/01-viruses/hiv-1
    relation: connects-to
    note: "A virus that injures the endothelium: untreated HIV can cause a thrombotic microangiopathy resembling aHUS, through direct endothelial damage and complement activation."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Some chemotherapy mimics it: drugs such as gemcitabine and mitomycin C cause a drug-induced thrombotic microangiopathy that overlaps clinically with complement-mediated aHUS."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Complement blockade transformed it: the anti-C5 monoclonals eculizumab and ravulizumab halt the uncontrolled alternative-complement activation of aHUS, preventing the microthrombi and rescuing the kidney where plasma exchange once failed."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "It thickens small arteries: the thrombotic microangiopathy of aHUS injures arteriolar and capillary walls, producing the onion-skin intimal swelling and luminal narrowing of renal arterioles characteristic of TMA."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Microthrombi reach the heart: aHUS is not kidney-limited — complement-driven microthrombi in the myocardial microvasculature cause cardiac ischaemia and dysfunction in a notable minority, contributing to its mortality."
  - target: 01-human/07-system/inherited-thrombophilia
    relation: connects-to
    note: "Complement versus coagulation thrombosis: atypical haemolytic uraemic syndrome thromboses the microvasculature through uncontrolled complement, contrasting with the coagulation-factor defects of inherited thrombophilia—two genetic routes to clotting."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "A virus that can trigger it: severe COVID-19 activates complement and injures the endothelium, precipitating a thrombotic microangiopathy resembling aHUS in susceptible patients."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "It is not only renal: although aHUS is a renal-predominant thrombotic microangiopathy, uncontrolled complement can also injure the pulmonary alveolar-capillary bed, causing extrarenal lung involvement in severe disease."
  - target: 01-human/07-system/myasthenia-gravis
    relation: connects-to
    note: "A complement-therapy bridge: the anti-C5 drugs (eculizumab, ravulizumab) that control aHUS also treat complement-mediated diseases like myasthenia gravis, the same terminal pathway behind very different illnesses."
  - target: 01-human/07-system/iga-nephropathy
    relation: connects-to
    note: "Complement in the glomerulus: aHUS and IgA nephropathy both involve alternative-complement dysregulation injuring the glomerulus, and C5- and factor-B-targeted inhibitors are now used or trialled in both."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Systemic, not only renal: as a complement-driven thrombotic microangiopathy, aHUS can also injure the skin and gut with the same microthrombi, causing digital ischaemia and extrarenal organ damage in severe disease."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "The STEC-HUS differential: typical HUS follows Shiga-toxin E. coli colitis that damages the intestinal epithelium with bloody diarrhoea, the key diagnosis to distinguish from complement-driven, often diarrhoea-negative aHUS."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "Cancer-associated TMA: mucin-producing adenocarcinomas like pancreatic cancer and chemotherapies such as gemcitabine and mitomycin cause a secondary thrombotic microangiopathy that mimics aHUS but needs treating the cause."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Microthrombi in the heart: the complement-driven microangiopathy of aHUS lodges platelet-rich thrombi in the myocardium and its conduction system, causing arrhythmia and cardiac injury as extrarenal complications."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Endothelial dysfunction: complement injury to the endothelium in aHUS cuts nitric oxide production, removing the vessel's vasodilator and antithrombotic brake and worsening the microangiopathy."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Vasoconstrictor surge: injured endothelium in aHUS releases endothelin-1, whose vasoconstriction aggravates the renal ischaemia and severe hypertension of the thrombotic microangiopathy."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "Malignant hypertension: renal microangiopathy in aHUS activates the renin-angiotensin system, and the resulting angiotensin-II-driven hypertension can itself drive a self-perpetuating TMA."
  - target: 01-human/03-molecular/pf4
    relation: connects-to
    note: "Platelet microthrombi: complement attack on the aHUS endothelium activates platelets to release PF4 and form the platelet-rich microthrombi that consume platelets and occlude the renal microvasculature."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "Neutrophil thromboinflammation: S100A8/A9 and neutrophil extracellular traps released in aHUS further activate complement and the endothelium, amplifying the thrombotic microangiopathy."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Heme danger signal: free heme from the intravascular haemolysis of aHUS acts as a TLR4 agonist, driving endothelial inflammation that compounds the complement-mediated microvascular injury."
  - target: 01-human/03-molecular/protein-c
    relation: connects-to
    note: "Thrombomodulin axis: THBD (thrombomodulin) mutations cause a subset of aHUS by impairing the thrombomodulin-protein C anticoagulant pathway and complement regulation, tipping the renal microvasculature toward thrombosis."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Endothelial destabilisation: complement injury to the aHUS endothelium raises the angiopoietin-2/angiopoietin-1 ratio, destabilising the Tie2-regulated barrier and promoting the vascular leak and thrombosis of the microangiopathy."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Renal inflammation: CCL2 released by the injured glomerular endothelium recruits monocytes that amplify the inflammatory damage of the thrombotic microangiopathy in the aHUS kidney."
  - target: 01-human/03-molecular/rage
    relation: connects-to
    note: "Free-heme amplification: the microangiopathic haemolysis of aHUS releases free haem that, as a DAMP signalling through RAGE, further activates complement and endothelium — a vicious cycle in which haemolysis feeds the complement-driven injury that caused it."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Microangiopathic anaemia: mechanical fragmentation of red cells across the complement-damaged glomerular microvasculature produces the Coombs-negative haemolytic anaemia of aHUS, outpacing the erythropoietin-driven marrow response."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Endothelial apoptosis: sublytic membrane-attack-complex deposition on glomerular endothelium triggers caspase-3-mediated apoptosis as well as activation, the endothelial cell death that exposes prothrombotic surfaces and seeds the renal microthrombi of aHUS."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Ischaemic kidney injury: the glomerular microthrombi of aHUS produce renal ischaemia that drives HIF-mediated hypoxic responses, the basis of the acute kidney injury that dominates its presentation."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Endothelial trigger: TNF-α-driven endothelial activation, often from an infectious trigger, tips the complement-vulnerable aHUS endothelium into the thrombotic microangiopathy of an acute episode."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Inflammatory amplifier: complement C5a (already mapped) and endothelial injury activate the NLRP3 inflammasome, adding an inflammatory dimension to the complement-driven microangiopathy of aHUS."
  - target: 01-human/03-molecular/thrombopoietin
    relation: connects-to
    note: "Platelet consumption: as platelets are consumed into microthrombi in the thrombotic microangiopathy of aHUS, the falling count drives a compensatory thrombopoietin response."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Platelet amplification: serotonin released from activated platelet dense granules promotes further aggregation and vasoconstriction, propagating the microvascular thrombosis of aHUS."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Thromboinflammation: endothelial DAMPs engage TLR4 (mapped) and MyD88 to NF-κB (mapped), amplifying the inflammatory injury that compounds the complement-driven microangiopathy of aHUS."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Sublytic complement attack on the renal endothelium triggers PI3K-AKT survival and activation signalling, shaping the endothelial response that determines microangiopathic injury in aHUS."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "C5a acting on C5aR (C5aR1 mapped) engages ERK-MAPK in endothelium and leukocytes, amplifying the complement-driven thromboinflammation of aHUS."
  - target: 01-human/03-molecular/fibrinogen
    relation: connects-to
    note: "Fibrinogen conversion to fibrin underlies the platelet-fibrin microthrombi that occlude the microvasculature in the thrombotic microangiopathy of aHUS (thrombin and vWF mapped)."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 promotes the neutrophil-extracellular-trap-driven thromboinflammation and endothelial activation that amplify the thrombotic microangiopathy of aHUS."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "DNA within complement-triggered neutrophil extracellular traps engages cGAS-STING, linking NET-driven inflammation to the microvascular thrombosis of aHUS."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling transduces the inflammatory cytokine response that accompanies the endothelial injury of aHUS."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK1/2-STAT cytokine signaling (IL-6 already mapped) amplifies the endothelial inflammatory response in the complement-driven thrombotic microangiopathy of aHUS."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signaling shapes the endothelial activation that contributes to the microvascular injury of aHUS."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO downstream of PI3K-AKT signaling (AKT already mapped) regulates the endothelial quiescence and oxidative-stress balance disrupted in aHUS."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the platelet-activation and endothelial signaling relevant to the thrombotic microangiopathy of atypical hemolytic uremic syndrome."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTOR signaling in activated endothelium participates in the complement-driven vascular injury of atypical hemolytic uremic syndrome."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) shapes the endothelial activation and survival during the complement-mediated injury of atypical hemolytic uremic syndrome."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of platelet and endothelial receptors participates in the platelet activation and endothelial injury of atypical hemolytic uremic syndrome."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked endothelial metabolic signaling modulates the microvascular homeostasis relevant to atypical hemolytic uremic syndrome."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated cytotoxic activity contributes to the endothelial injury of the thrombotic microangiopathy in atypical hemolytic uremic syndrome."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the endothelial-cell homeostasis relevant to the thrombotic microangiopathy of atypical hemolytic uremic syndrome."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment participates in the endothelial inflammation and renal injury of atypical hemolytic uremic syndrome."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic modulation of the complement and endothelial gene expression relevant to atypical hemolytic uremic syndrome."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the endothelial and leukocyte interactions of the thrombotic microangiopathy of atypical hemolytic uremic syndrome."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the endothelial injury and thromboinflammation of atypical hemolytic uremic syndrome."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the endothelial activation of atypical hemolytic uremic syndrome."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Anti-factor-H autoantibodies: a subset of atypical HUS is caused by IgG autoantibodies against factor H (already mapped), usually with CFHR gene deletions, an acquired form managed with immunosuppression and plasma exchange rather than lifelong complement blockade alone."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Extrarenal microangiopathy: the thrombotic microangiopathy of atypical HUS is not confined to the kidney, and cardiac involvement with myocardial microthrombi raising troponin reflects the systemic endothelial injury that also affects the brain."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Platelet activation: sublytic complement C5b-9 deposited on platelets and endothelium triggers calcium-dependent activation and procoagulant microvesicle release, driving the microthrombi that consume platelets in the thrombotic microangiopathy."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Pregnancy trigger: pregnancy and the postpartum period are major triggers of atypical HUS in genetically predisposed women, the estrogen-associated haemostatic and complement changes unmasking the underlying complement dysregulation."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Complement-kinin crosstalk: complement activation intersects with the kinin system, and bradykinin-driven vascular permeability contributes to the endothelial injury (already mapped) and oedema of the thrombotic microangiopathy in atypical HUS."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative haemolysis: mechanical fragmentation of red cells in the microthrombi releases haem and drives oxidative stress, to which xanthine-oxidase-derived reactive oxygen species contribute, compounding the microangiopathic haemolysis (haemoglobin already mapped)."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immune counter-regulation: IL-10 opposes the inflammatory cytokines (IL-6, TNF and IL-1 already mapped) amplified by the complement activation of atypical HUS, part of the immune balance in the thrombotic microangiopathy."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "Renal RAAS activation: the renal injury and hypertension of atypical HUS activate the renin-angiotensin system (angiotensin II already mapped), and the resulting aldosterone drives sodium retention and further vascular and renal damage."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Haemolytic iron load: the chronic microangiopathic haemolysis (haemoglobin already mapped) and repeated transfusions of atypical HUS load the body with iron, adding an iron-overload burden to the disease and its management."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Thromboxane and platelets: the activated platelets (PF4 and serotonin already mapped) of atypical HUS generate thromboxane to amplify aggregation, part of the eicosanoid contribution to the microthrombosis of the thrombotic microangiopathy."
  - target: 01-human/03-molecular/renin
    relation: connects-to
    note: "Renal renin activation: the renal injury and hypertension of atypical HUS activate renin, driving the angiotensin II and aldosterone (already mapped) that worsen the vascular and renal damage."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Platelet zinc and coagulation: zinc released from the activated platelets (already mapped) promotes the contact pathway and fibrin formation (fibrinogen and thrombin already mapped), adding to the prothrombotic state of atypical HUS."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Haemolytic iron handling: the intravascular microangiopathic haemolysis (haemoglobin already mapped) and the inflammation (IL-6 already mapped) disturb the hepcidin-regulated iron handling of atypical HUS."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron loss and release: the intravascular haemolysis of atypical HUS releases iron and causes urinary iron loss, disturbing the iron balance (hepcidin already mapped) alongside the anaemia (haemoglobin already mapped)."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Electrolyte derangement: the renal impairment of atypical HUS, and the citrate of any plasma exchange, disturb the magnesium (with calcium already mapped) balance, needing replacement."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Immune-metabolic adipokine: leptin is the adipokine of the immune-metabolic milieu that modulates the endothelial (already mapped) and complement inflammation of atypical HUS."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic-inflammatory milieu of atypical HUS."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the inflammatory (IL-6 and TNF already mapped) milieu of atypical HUS."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate immune crosstalk: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, is part of the innate-immune dimension that crosstalks with the complement (C3 already mapped) dysregulation of atypical HUS."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 arm: the IFN-γ of the T cells is the type-II interferon arm of the inflammatory dimension (IL-6 and TNF already mapped) accompanying the complement-mediated endothelial (already mapped) injury of atypical HUS."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension of atypical HUS."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Type-2 arm: IL-4 is the prototypical type-2 cytokine of the immune milieu that balances the Th1 (IFN-γ already mapped) inflammation accompanying the complement-mediated injury of atypical HUS."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 arm: IL-13, with IL-4 (already mapped), completes the type-2/Th2 dimension of the immune milieu accompanying the complement-mediated endothelial (already mapped) injury of atypical HUS."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Eosinophil arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune milieu accompanying atypical HUS."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement regulation: the C1-esterase inhibitor regulates the classical and lectin complement pathways, complementing the factor H (already mapped) control of the alternative pathway (complement C3, C5 and C5aR1 already mapped) dysregulated in atypical HUS."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2 (IFN-γ and IL-4 already mapped) cytokines of the immune milieu accompanying the complement-mediated endothelial (already mapped) injury of atypical HUS."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the type-2 immune dimension of the immune milieu accompanying atypical HUS."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Thromboinflammation: osteopontin, released by the activated platelets (already mapped), is a matricellular mediator linking the complement-driven endothelial (already mapped) injury to the microthrombosis of atypical HUS."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Haemolytic iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the microangiopathic haemolysis of atypical HUS."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Adaptive milieu: the cytotoxic T cells (perforin already mapped), with the T-helper (already mapped) arm, are part of the adaptive-immune milieu accompanying the complement-mediated endothelial injury of atypical HUS."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-endothelial axis: TSLP, released from injured renal (already mapped) endothelium under complement (C3, C5, C5aR1 and factor H already mapped) stress, activates mast cells (already mapped) and dendritic cells, amplifying the thromboinflammatory cascade of atypical HUS."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell vasodilator: histamine, released from activated mast cells (already mapped) in the complement-driven vascular inflammation of atypical HUS, augments endothelial permeability and amplifies the microvascular thromboinflammation alongside nitric-oxide depletion."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Fibrotic matricellular: periostin, a matricellular mediator upregulated in the renal (already mapped) tubulointerstitium under complement-driven injury in aHUS, promotes fibroblast (already mapped) activation and the progressive renal fibrosis of atypical HUS."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian complement modulation: melatonin, via MT1/MT2 receptors on endothelial cells (already mapped) and macrophages (already mapped), scavenges ROS (already mapped) and attenuates the nocturnal complement activation surge driving TMA episodes in atypical HUS."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Immune-endocrine haematopoietic axis: prolactin, acting via PRLR on haematopoietic progenitors (already mapped) and T-helper cells (already mapped), modulates the immune activation and the complement-driven thromboinflammatory microangiopathy of atypical HUS."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Neuroimmune endothelial protection: oxytocin, via oxytocin receptors on endothelial cells (already mapped) and macrophages (already mapped), suppresses the NF-κB-driven (already mapped) pro-inflammatory cytokine cascade and limits endothelial injury in atypical HUS."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "aHUS testosterone: testosterone, via androgen receptors on endothelial cells (already mapped), suppresses complement-C5 (already mapped); androgen deficiency amplifies TMA severity, glomerulus (already mapped) microangiopathy, and the haemolytic cascade in aHUS."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "aHUS selenium: selenium, via glutathione peroxidase (GPx), shields endothelial cells (already mapped) from complement-C5 (already mapped)-driven oxidative injury; selenium deficiency amplifies haemolytic microangiopathic stress and platelet (already mapped) activation of aHUS."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "aHUS vasopressin: vasopressin, via V2 receptors on renal tubular cells, promotes fluid retention and hypertension (already mapped) in aHUS; vasopressin also amplifies endothelial cell (already mapped) oxidative stress and kidney (already mapped) microangiopathic injury."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "aHUS iodine: iodine-dependent thyroid hormones modulate endothelial-cell (already mapped) function and platelet (already mapped) reactivity; iodine deficiency amplifies the complement-C5 (already mapped) and NF-κB (already mapped) microangiopathic cascade of aHUS."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "aHUS sodium: sodium dysregulation amplifies hypertension (already mapped) and endothelial-cell (already mapped) injury in aHUS; hypernatraemia-driven osmotic stress activates the NF-κB (already mapped) and complement-C5 (already mapped) microangiopathic cascade of aHUS."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "aHUS copper: copper, as cofactor of superoxide dismutase in endothelial cells (already mapped) and kidney (already mapped) tubular cells, scavenges complement-C5 (already mapped)-driven ROS; copper deficiency amplifies the microangiopathic and haemolytic cascade of aHUS."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "aHUS phosphorus: phosphorus fuels endothelial-cell (already mapped) and platelet (already mapped) ATP; phosphorus deficiency impairs complement-C5 (already mapped) regulation and amplifies NF-κB (already mapped) and IL-6 (already mapped) microangiopathic cascade of aHUS."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "aHUS nitrogen: nitric oxide (NO, nitrogen-derived) in endothelial cells (already mapped) regulates vasodilation and platelet (already mapped) inhibition; NO deficiency amplifies complement-C5 (already mapped) and NF-κB (already mapped) microangiopathic cascade of aHUS."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "aHUS chloride: chloride channels on endothelial cells (already mapped) and kidney (already mapped) tubular cells maintain ionic homeostasis; chloride dysregulation amplifies complement-C5 (already mapped) and NF-κB (already mapped) and thrombin (already mapped) cascade of aHUS."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "aHUS sulfur: sulfur-containing glutathione in endothelial cells (already mapped) and macrophages (already mapped) quenches complement-C5 (already mapped)-driven ROS; sulfur deficiency amplifies NF-κB (already mapped) and thrombin (already mapped) microangiopathic cascade of aHUS."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "carbon, via bicarbonate in endothelial cells (already mapped) and kidney (already mapped) tubular cells, maintains pH homeostasis; pH dysregulation amplifies complement-C5 (already mapped) and NF-κB (already mapped) and thrombin (already mapped) microangiopathic cascade of aHUS."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "hydrogen, via H2O2 and ROS balance in endothelial cells (already mapped) and macrophages (already mapped), sets redox tone; hydrogen excess amplifies complement-C5 (already mapped) and NF-κB (already mapped) and thrombin (already mapped) microangiopathic cascade of aHUS."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β from macrophages (already mapped) and endothelial cells (already mapped) promotes fibrotic remodelling of glomerulus (already mapped) in aHUS; TGF-β amplifies NF-κB (already mapped) and complement-C5 (already mapped) mesangial expansion and microangiopathic progression."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "aHUS PD-1: PD-1 on T-cytotoxic-cell (already mapped) and t-helper-cell (already mapped) modulates thromboinflammatory homeostasis; PD-1 dysregulation amplifies complement-C5 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) microangiopathic cascade of aHUS."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "aHUS GLP-1: GLP-1 signalling in endothelial cells (already mapped) and podocytes (already mapped) modulates renal metabolic homeostasis; GLP-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and complement-C5 (already mapped) cascade of aHUS."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "aHUS WNT/β-catenin: WNT/β-catenin in endothelial cells (already mapped) and podocytes (already mapped) drives glomerular repair; WNT dysregulation amplifies NF-κB (already mapped) and TGF-β (already mapped) fibrotic remodelling and complement-C5 (already mapped) cascade of aHUS."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "aHUS RANKL: RANKL signalling in endothelial cells (already mapped) and macrophages (already mapped) modulates renal bone-immune axis; RANKL excess amplifies NF-κB (already mapped) and complement-C5 (already mapped) and IL-6 (already mapped) cascade of aHUS."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "aHUS SMAD4: SMAD4 in endothelial cells (already mapped) and podocytes (already mapped) mediates TGF-β-driven renal fibrosis; SMAD4 dysregulation amplifies NF-κB (already mapped) and complement-C5 (already mapped) and IL-6 (already mapped) cascade of aHUS."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "aHUS IL-2: IL-2 signalling in T-cells (already mapped) and macrophages (already mapped) modulates complement-driven immune tolerance; IL-2 deficiency amplifies NF-κB (already mapped) and complement-C5 (already mapped) and IL-6 (already mapped) cascade of aHUS."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "aHUS fibronectin: fibronectin in glomerular endothelium (already mapped) and podocytes (already mapped) modulates microvascular integrity; fibronectin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of aHUS."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "aHUS Notch: Notch signalling in glomerular endothelium (already mapped) and mesangial cells (already mapped) modulates vascular remodelling; Notch dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of aHUS."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "aHUS IGF-1: IGF-1 signalling in podocytes (already mapped) and mesangial cells (already mapped) sustains glomerular repair; IGF-1 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of aHUS."
---

# Atypical HUS

## Overview

**Atypical hemolytic uremic syndrome (aHUS)** is a **thrombotic microangiopathy (TMA)** caused by **uncontrolled activation of the complement alternative pathway**, primarily at the glomerular endothelium. It presents with the classic TMA triad:
1. **Microangiopathic hemolytic anemia (MAHA):** Schistocytes, elevated LDH, low/absent haptoglobin, Coombs-negative
2. **Thrombocytopenia:** Platelet consumption in microthrombi
3. **Acute kidney injury (AKI):** From glomerular microvascular occlusion

aHUS is distinguished from **STEC-HUS** (Shiga-toxin–producing *E. coli* HUS; more common, especially in children, self-limited) and **TTP** (ADAMTS13 deficiency; predominantly neurological) — all three are TMAs but have distinct mechanisms, prognosis, and treatment [^fakhouri-2017-ahus-lancet].

**Epidemiology:**
- Incidence: ~1-2 per million/year; affects all ages (children and adults; bimodal distribution)
- ~40-60% have identifiable complement gene mutations; ~6-10% have anti-CFH antibodies; ~30-40% have no identified mutation ("unknown/idiopathic")
- Without treatment: ~50% reach ESRD within 1 year; ~25% die in the acute phase
- With eculizumab: >80% achieve hematologic normalization and renal recovery [^legendre-2013-eculizumab-ahus-nejm]

## Structure

### Genetic causes and complement proteins

**Frequency of complement gene mutations in aHUS:**

| Gene | Protein | Mechanism | Frequency | Notes |
|:-----|:--------|:----------|:----------|:------|
| **CFH** | Factor H | Loss-of-function (SCR19-20 hotspot) → impaired surface C3b regulation | ~20-30% | Most common; SCR19-20 mutations disrupt surface-specific regulation |
| **CD46 (MCP)** | Membrane Cofactor Protein | Loss-of-function → reduced Factor I cofactor on cell surface | ~5-15% | Good prognosis with eculizumab; high recurrence post-transplant without it |
| **CFI** | Factor I | Loss-of-function → loss of C3b inactivation (iC3b generation impaired) | ~5-10% | Phenotypically indistinguishable from CFH-aHUS |
| **C3** | Complement C3 | Gain-of-function → C3b resistant to Factor H/I regulation | ~5% | Associated with C3 glomerulopathy overlap |
| **CFB** | Factor B | Gain-of-function → hyperactive C3 convertase (C3bBb more stable) | ~2% | Rare; often severe infantile presentation |
| **THBD** | Thrombomodulin | Loss-of-function → reduced complement regulation on endothelium | ~3-5% | Triggers TMA at endothelial level |
| **Anti-CFH antibodies** | — | Autoimmune blockade of Factor H surface binding | ~6-10% | Predominantly children; CFHR1-CFHR3 homozygous deletion predisposes |

**Key insight:** Most mutations impair the ability of host cells to **recruit Factor H to their surface** (not fluid-phase regulation) — this explains why complement levels (C3, C4) can be normal or mildly reduced in aHUS, unlike C3 deficiency states.

### Pathophysiological cascade

```
CFH/CFI/CD46 mutation (or anti-CFH antibody)
        ↓
Impaired surface C3b regulation on glomerular endothelium
        ↓
C3b amplification → C3bBb (alternative C3 convertase) not inactivated
        ↓
C3bBbC3b (alternative C5 convertase) → C5 cleavage
        ↓
C5a: neutrophil priming → TF expression → pro-thrombotic state
C5b-9 (MAC): sublytic endothelial injury → VWF release → platelet adhesion
        ↓
Intravascular microthrombi (platelets + fibrin) in glomerular capillaries
        ↓
Glomerular occlusion → AKI  +  RBC fragmentation → MAHA  +  Platelet consumption → thrombocytopenia
        ↓
Repeated TMA episodes → glomerular fibrosis → CKD → ESRD
```

**Common triggers for aHUS episodes:**
- Infections (upper respiratory, GI — especially in children; infection activates complement independently)
- Pregnancy (especially peripartum; pregnancy + complement mutation → severe TMA)
- Combined oral contraceptives (OCP → complement activation + endothelial stress)
- Vaccination (rare)
- Malignancy
- Solid organ transplantation (donor organ → ischemia-reperfusion → complement activation)

## Function

### Diagnosis

**The diagnostic challenge:** aHUS is a diagnosis of exclusion — TTP and STEC-HUS must be ruled out first.

**Step-by-step diagnostic workup:**

1. **Confirm TMA:** CBC (low platelets, anemia), blood smear (schistocytes ≥1% → MAHA), LDH (elevated), haptoglobin (undetectable), Coombs test (negative), creatinine (elevated)

2. **Exclude TTP (priority):**
   - **ADAMTS13 activity:** <10% → TTP; ≥10% → not TTP; send URGENTLY (treatment differs fundamentally — TTP needs PEX, not eculizumab)
   - Anti-ADAMTS13 antibodies (in immune TTP)

3. **Exclude STEC-HUS:**
   - Stool cultures and O157:H7 Shiga toxin PCR
   - STEC-HUS: usually age <5 years, prodromal bloody diarrhea, seasonal (summer), no family history, self-limited without eculizumab

4. **Complement workup (once TTP excluded):**

| Test | Interpretation |
|:-----|:--------------|
| Serum C3 | Low-normal in ~40-50% of aHUS (not always abnormal) |
| Serum C4 | Normal (alternative pathway activation; C4 not consumed) |
| Factor H antigen | Low → type I CFH mutation or anti-CFH antibodies; normal → type II (SCR19-20 functional mutation) |
| Factor H functional activity | Low → loss-of-function mutation |
| Factor I antigen + activity | Low → CFI mutation |
| CD46 (MCP) on neutrophils (flow) | Reduced → CD46 mutation |
| Anti-CFH antibodies | Present → autoimmune aHUS (CFHR1-CFHR3 deletion) |
| Complement genetic panel (CFH, CFI, CD46, C3, CFB, THBD, CFHRs) | Gold standard; guides long-term therapy and recurrence risk |

5. **Renal biopsy (when diagnosis uncertain):**
   - Characteristic: TMA histology — fibrin/platelet thrombi in glomerular capillaries; endothelial swelling; ischemic glomerular collapse
   - No immune deposits (distinguishes from immune complex GN)
   - May show MPGN pattern if C3 glomerulopathy overlap

**Differential diagnosis of TMA:**

| Feature | aHUS | TTP | STEC-HUS | HELLP/obstetric TMA |
|:--------|:-----|:----|:---------|:--------------------|
| Mechanism | Complement | ADAMTS13 deficiency | Shiga toxin | Placental/hormonal |
| Age | All | Adults (F > M) | <5 years | Pregnant/peripartum |
| Diarrhea | No | No | Yes (bloody) | No |
| Neurological sx | Mild | Dominant | Minimal | Variable |
| Renal sx | Dominant | Mild | Dominant | Variable |
| ADAMTS13 activity | ≥10% | <10% | ≥10% | ≥10% |
| C3 | Low-normal | Normal | Normal | Normal |
| Stool Shiga toxin | Negative | Negative | Positive | Negative |
| Family history | Often positive | No | No | No |
| Treatment | Eculizumab | PEX + immunosuppression | Supportive | Delivery |

## Pathology

### Acute treatment [^legendre-2013-eculizumab-ahus-nejm]

**Eculizumab (Soliris) — standard of care:**
- **Dose:** 900 mg IV weekly × 4, then 1200 mg IV every 2 weeks (adults); weight-based dosing in pediatrics
- **Mechanism:** Anti-C5 monoclonal antibody (humanized IgG2/4κ); blocks C5 cleavage → prevents C5a and C5b-9 generation
- **Efficacy (NEJM 2013):** Platelet normalization in 80-88% within 1 week; eGFR improvement in 65-80%; complete TMA response in 75%
- **Meningococcal prophylaxis MANDATORY:** Eculizumab blocks terminal complement → prevents lysis of encapsulated bacteria → *N. meningitidis* risk ×1000-2000×; **vaccinate with MenACWY + MenB ≥2 weeks before first dose; if urgent: prophylactic antibiotics (penicillin/ciprofloxacin) from day 1**
- **Duration:** Typically lifelong for high-risk mutations (CFH, CFI); trial discontinuation possible for CFH-antibody aHUS after titer suppression and in some CD46 patients with close monitoring

**Ravulizumab (Ultomiris) — long-acting C5 inhibitor:**
- Same efficacy as eculizumab; half-life extended by FcRn recycling modification (Met428Leu, Asn434Ser in Fc)
- **Dose:** Weight-based IV loading, then maintenance Q8W (adults); reduces infusion burden significantly
- FDA approved for aHUS 2019; now preferred for many patients

**Before eculizumab — Plasma Exchange (PEX):**
- PEX (or FFP infusion) replenishes Factor H in plasma → may temporarily stabilize complement
- Still used: (1) diagnostic uncertainty (covers TTP while ADAMTS13 returns); (2) anti-CFH antibody aHUS (removes antibody)
- Do NOT delay eculizumab for PEX if diagnosis of aHUS is clear

**Anti-CFH antibody aHUS — additional treatment:**
- Plasma exchange (removes antibody + replenishes CFH) + immunosuppression (rituximab, mycophenolate) → reduce antibody titer
- Eculizumab continues to block downstream C5 while antibody is cleared
- Goal: antibody-negative remission → consider weaning eculizumab

### Renal transplantation

**aHUS recurs in transplant kidneys** (the genetic defect persists → same endothelial vulnerability in allograft):
- **CFH mutations:** ~75-90% recurrence without C5 inhibition → prohibitive without eculizumab coverage
- **CD46 mutations:** <15% recurrence (donor kidney has normal CD46; patient's circulating complement is sufficient with normal CD46)
- **CFI mutations:** ~50-70% recurrence
- **Anti-CFH antibody aHUS:** Continue immunosuppression + eculizumab perioperatively → antibody-negative remission required before transplant
- **Standard:** Eculizumab prophylaxis on day of transplant + continued maintenance for high-risk genotypes; may allow discontinuation in low-risk mutations after 6-12 months

**Liver transplantation for CFH aHUS:**
- CFH is synthesized primarily in the liver → liver transplant (or combined liver-kidney for ESRD) could theoretically cure CFH-aHUS
- High surgical risk; pursued rarely in children refractory to eculizumab; eculizumab bridge perioperatively essential

### Long-term monitoring

- Monthly: CBC, creatinine, LDH, haptoglobin, urinalysis while on eculizumab
- Complement C3, C4, factor H levels: periodically (especially after eculizumab discontinuation trial)
- Renal function: eGFR every 3-6 months
- Screen first-degree relatives with complement genetic panel (autosomal dominant CFH/CFI/C3/CFB mutations; ~50% penetrance)

## Connections

- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — CFH mutations (SCR19-20) are the most common cause of aHUS (~20-30%); Factor H regulates alternative C3 convertase on renal endothelial surfaces; anti-CFH autoantibodies (CFHR1-CFHR3 deletion) cause aHUS in ~6-10%; eculizumab/ravulizumab target downstream C5.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Uncontrolled alternative C3 convertase (C3bBb) from CFH/CFI/CD46 defects → persistent C3 consumption → hypocomplementemia; serum C3 is low-normal in many aHUS cases; C3 nephritic factor (C3NeF) stabilizes C3bBb → C3 glomerulopathy (related complement-mediated nephropathy).
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Uncontrolled alternative complement (from CFH/CFI mutations) generates C5 convertase → C5a (neutrophil priming, endothelial injury) + C5b-9 (MAC → TMA); eculizumab (anti-C5 mAb) and ravulizumab block C5 → normalize platelets and renal function in >80% of aHUS patients.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — aHUS causes progressive CKD from repeated TMA episodes; ~50% of untreated patients reach ESRD within 1 year; eculizumab/ravulizumab prevent and partially reverse renal injury; renal transplant in aHUS requires continued C5 inhibition to prevent TMA recurrence in the allograft.
- `connects-to` → **[ADAMTS13](../../03-molecular/adamts13/README.md)** — ADAMTS13 activity is the first test to exclude TTP from the aHUS differential; in TMA workup, ADAMTS13 <10% = TTP → plasma exchange + caplacizumab, NOT eculizumab; ADAMTS13 ≥10% + complement workup → aHUS; the distinction is critical since treatments are non-interchangeable.
- `connects-to` → **[Thrombotic Thrombocytopenic Purpura](../thrombotic-thrombocytopenic-purpura/README.md)** — TTP (ADAMTS13 <10%) is the primary differential diagnosis of aHUS; both cause TMA (MAHA + thrombocytopenia + AKI) but TTP is treated with plasma exchange + caplacizumab and aHUS with eculizumab; TTP tends to spare the kidneys more; aHUS tends to dominate with AKI over neuro.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — The kidney is aHUS's main target: uncontrolled alternative complement strikes the glomerular endothelium, seeding microthrombi that occlude capillaries → acute kidney injury and, over repeated episodes, CKD and ESRD; aHUS recurs in transplants unless C5 inhibition continues.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — aHUS is a disease of the glomerular endothelial cell: because mutant Factor H cannot be recruited to the cell surface, the alternative pathway runs unchecked there → MAC sublytically injures the endothelium → VWF release and platelet adhesion → the microthrombi of TMA.
- `connects-to` → **[Escherichia coli](../../../02-pathogen/02-bacteria/escherichia-coli/README.md)** — aHUS must be separated from typical HUS caused by Shiga-toxin-producing E. coli: STEC-HUS follows bloody diarrhoea, hits young children, is usually self-limited, and does not respond to eculizumab — whereas complement-driven aHUS does, making the stool toxin test a key fork.
- `connects-to` → **[Graft-Versus-Host Disease](../gvhd/README.md)** — aHUS and transplant-associated TMA (TA-TMA) in GVHD overlap: both injure endothelium and activate complement to drive microvascular thrombosis with schistocytes, thrombocytopenia and kidney injury; complement variants predispose to TA-TMA, and C5 inhibition can treat both.
- `connects-to` → **[Paroxysmal Nocturnal Hemoglobinuria](../pnh/README.md)** — aHUS and PNH are the archetypal complement-mediated diseases treated by C5 blockade: PNH lacks GPI-anchored complement regulators causing hemolysis and thrombosis, while aHUS has uncontrolled alternative-pathway activation on endothelium causing TMA; eculizumab transformed both.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — aHUS is a thrombotic microangiopathy that consumes platelets: complement-injured endothelium triggers platelet adhesion and microthrombi in the renal microvasculature, dropping the count while sparing large vessels; consumed platelets and schistocytes are diagnostic clues.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — aHUS shreds red cells like all thrombotic microangiopathies: erythrocytes passing through complement-damaged, microthrombus-laden glomerular capillaries fragment into schistocytes, producing the hemolytic anemia that, with thrombocytopenia and AKI, defines the TMA triad.
- `connects-to` → **[Disseminated Intravascular Coagulation](../disseminated-intravascular-coagulation/README.md)** — aHUS and DIC both cause thrombocytopenia with microthrombi but differ in coagulation: DIC consumes clotting factors with prolonged PT/PTT, while aHUS is complement-driven with normal clotting times—so normal coagulation amid a microangiopathy points to aHUS.
- `connects-to` → **[Systemic Lupus Erythematosus](../systemic-lupus-erythematosus/README.md)** — Lupus can trigger a secondary thrombotic microangiopathy resembling aHUS: complement activation and antiphospholipid antibodies in SLE injure endothelium and cause a TMA, so distinguishing aHUS from lupus or TTP guides eculizumab vs immunosuppression vs plasma exchange.
- `connects-to` → **[Heparin-Induced Thrombocytopenia](../heparin-induced-thrombocytopenia/README.md)** — aHUS and HIT both cause thrombocytopenia with thrombosis but by different mechanisms: aHUS is uncontrolled complement attacking endothelium, while HIT is PF4-heparin antibodies activating platelets—both consume platelets while clotting, needing different treatment.
- `connects-to` → **[Immune Thrombocytopenia](../immune-thrombocytopenia/README.md)** — aHUS and immune thrombocytopenia both lower platelets but differ fundamentally: aHUS consumes platelets in complement-driven microthrombi, while ITP is isolated antibody-mediated platelet destruction—the smear and renal function separate them.
- `connects-to` → **[Malaria](../malaria/README.md)** — aHUS and severe malaria can both present as thrombotic microangiopathy: malaria's infected red cells and inflammation damage the microvasculature much as complement does in aHUS—so in endemic areas falciparum infection enters the differential of TMA.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — aHUS strikes the glomerulus hardest: uncontrolled complement injures glomerular endothelium, triggering the thrombotic microangiopathy that shears red cells and clogs capillaries—so renal failure with microangiopathic hemolysis is the disease's hallmark.
- `connects-to` → **[Von Willebrand Factor](../../03-molecular/von-willebrand-factor/README.md)** — aHUS shares thrombotic-microangiopathy machinery with TTP via von Willebrand factor: complement-injured endothelium releases ultralarge VWF multimers that snare platelets into microthrombi—the same VWF that ADAMTS13 deficiency unleashes in TTP.
- `connects-to` → **[Podocyte](../../04-cellular/podocyte/README.md)** — aHUS injures the glomerular filter including its podocytes: complement-driven endothelial damage and microthrombi disrupt the filtration barrier, contributing to the proteinuria, hematuria and progressive renal failure that mark the disease.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — Pregnancy can trigger atypical HUS: the complement stress of pregnancy and especially the postpartum period unmasks aHUS in women with regulatory mutations, so a thrombotic microangiopathy around delivery must be distinguished from pre-eclampsia and HELLP.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — Severe hypertension and aHUS form a vicious circle: complement-driven microvascular injury in the kidney drives malignant hypertension, and the high pressure further shears endothelium—so accelerated hypertension can both trigger and result from the microangiopathy.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — aHUS is not confined to the kidney—it can strike the brain: complement-mediated microthrombi in cerebral vessels cause seizures, confusion, and stroke, so neurological signs in a thrombotic microangiopathy mark severe, extrarenal aHUS needing urgent complement blockade.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — aHUS is driven by runaway complement reaching C5a: uncontrolled activation cleaves C5 to C5a, which through its receptor C5aR1 inflames and injures endothelium—why C5-blocking eculizumab transformed this once-lethal disease.
- `connects-to` → **[Thrombin](../../03-molecular/thrombin/README.md)** — aHUS is a thrombotic microangiopathy fueled by thrombin: complement-injured endothelium becomes prothrombotic, generating thrombin and platelet-fibrin microthrombi that shred red cells and clog the kidney's small vessels.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Complement's C5a recruits neutrophils that worsen aHUS: drawn to the activated endothelium, neutrophils release enzymes and oxidants that amplify the microvascular injury, linking the complement defect to the destructive inflammation in the kidney.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — aHUS is the 'H' of hemolytic-uremic: uncontrolled complement injures small-vessel endothelium, and the fibrin and platelet strands shear passing red cells (microangiopathic hemolysis), spilling hemoglobin and producing schistocytes.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — aHUS damages the kidney enough to raise potassium: complement-driven microthrombi block glomerular capillaries, causing the acute kidney injury that—with hemolysis releasing potassium—drives dangerous hyperkalemia needing urgent care.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages clean up aHUS's destroyed red cells: as complement shears erythrocytes, splenic and hepatic macrophages clear the damaged cells and free hemoglobin, the reticuloendothelial cleanup behind the hemolytic anemia of the disease.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — aHUS can strike the heart: the same complement-driven microthrombi that clog the kidney lodge in cardiac vessels, causing ischemia and cardiomyopathy, one of the extrarenal manifestations that mark severe disease.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — aHUS chokes off oxygen across organs: widespread microvascular clots block blood flow while the hemolytic anemia leaves less to carry oxygen, so tissues throughout the body are starved during an acute episode.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — aHUS can injure the pancreas: microthrombi in its small vessels cause ischemic pancreatitis and can disturb blood sugar, another extrarenal site of the thrombotic microangiopathy that defines the disease.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — aHUS is confirmed on the kidney biopsy under the microscope: thrombotic microangiopathy—fibrin clots and swollen endothelium in the glomeruli, read in light—distinguishes it from other causes of failing kidneys.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Recurrent aHUS scars the kidney: repeated thrombotic injury heals with glomerular and interstitial fibrosis, driving the chronic kidney disease that can follow even after attacks are controlled.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — aHUS can injure the gut: mesenteric microthrombi cause abdominal pain and ischemic colitis, part of the multi-organ thrombotic reach that sets it apart from a purely renal disease.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reveals aHUS's lesion in the kidney's filters: the glomerular endothelium swells and lifts off, widening the subendothelial space and trapping platelet-fibrin microthrombi — the thrombotic microangiopathy unchecked complement drives.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — The complement storm can reach the lungs: aHUS occasionally causes pulmonary thrombotic microangiopathy with hemorrhage and respiratory failure, evidence its endothelial injury is systemic, not confined to the kidney.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — aHUS can blur the eye: microthrombi and the malignant hypertension it provokes injure the retinal vessels, producing a Purtscher-like retinopathy of cotton-wool spots and hemorrhages that can threaten vision.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — aHUS reaches the brain through its tiniest vessels: microthrombi in the cerebral microcirculation injure neurons, causing the seizures, confusion, and stroke that complicate severe disease in up to half of patients.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Some aHUS is antibody-made: a subset is driven by autoantibodies against complement factor H (often with CFHR deletions), and the disease's mainstay treatment, eculizumab, is itself a monoclonal antibody that blocks C5.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The microangiopathy can scar more than the kidney: aHUS is a systemic TMA, and clots in the hepatic and mesenteric microvessels can derange the liver and bowel as part of its multi-organ reach.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Pregnancy is a classic trigger: complement-mediated aHUS often erupts in the peripartum period, especially postpartum, and must be told apart from HELLP and preeclampsia, which it can closely mimic in a sick mother.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — The damage remodels the small arteries: aHUS injures arterioles into the concentric 'onion-skin' thickening of smooth-muscle and matrix layers, the chronic vascular lesion of thrombotic microangiopathy seen on biopsy.
- `connects-to` → **[Stroke](../stroke/README.md)** — Microthrombi reach the brain: aHUS is not confined to the kidney — clots in the cerebral microvessels cause seizures, encephalopathy, and stroke, the CNS face of its systemic thrombotic microangiopathy.
- `connects-to` → **[Streptococcus pneumoniae](../../../02-pathogen/02-bacteria/streptococcus-pneumoniae/README.md)** — Pneumococcus can ignite its own HUS: the bacterium's neuraminidase strips sialic acid to expose the hidden T antigen on red cells and endothelium, triggering a thrombotic microangiopathy distinct from the usual E. coli kind.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Glomerular vessels live on VEGF: podocyte VEGF keeps the filtration endothelium healthy, so cancer drugs that block it can unleash a complement-amplified thrombotic microangiopathy that mirrors aHUS.
- `connects-to` → **[Systemic Sclerosis](../systemic-sclerosis/README.md)** — Scleroderma renal crisis is a TMA twin: it injures the same small renal vessels with malignant hypertension and microangiopathic hemolysis, a key differential to separate from complement-driven aHUS at the bedside.
- `connects-to` → **[Antiphospholipid Syndrome](../antiphospholipid-syndrome/README.md)** — Catastrophic APS mimics it: antiphospholipid antibodies can trigger a widespread thrombotic microangiopathy with renal failure resembling aHUS, another autoimmune cause that must be excluded before settling on complement-driven disease.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It is not only a kidney disease: complement-driven microthrombi strike the brain too, causing seizures, confusion and stroke in a large share of patients — a leading extrarenal manifestation of aHUS.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — Inflammation amplifies the endothelial injury: IL-6 and other cytokines released as complement attacks the vessel lining feed forward into more endothelial activation and microthrombosis, worsening the microangiopathy.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Complement switches the endothelium to attack mode through NF-κB: C5a-driven NF-κB activation makes the vessel lining procoagulant and inflamed, amplifying the microthrombosis that defines the complement-mediated microangiopathy.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — It can clot the heart's small vessels too: complement-driven microthrombi in the coronary microcirculation injure cardiomyocytes, causing the cardiomyopathy and heart attacks that are a recognized extrarenal manifestation of aHUS.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Blocking complement raises the infection stakes: the anti-C5 therapy eculizumab that controls aHUS disables the membrane attack complex, sharply increasing meningococcal infection and sepsis risk and mandating vaccination.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — It is a thrombotic state beyond the microcirculation: the complement-driven endothelial activation and platelet consumption of aHUS create a prothrombotic milieu that can throw large-vessel venous thrombi as well as the defining microthrombi.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Beyond the hemolysis, the failing kidney starves the marrow: as aHUS damages the kidney, lost erythropoietin production and chronic inflammation add a renal anemia-of-chronic-disease component on top of the microangiopathic hemolysis.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A relapsing, life-threatening disease weighs on the mind: the unpredictability of aHUS flares, dialysis dependence and lifelong complement-blocking infusions impose a heavy psychological burden and depression.
- `connects-to` → **[Neisseria meningitidis](../../../02-pathogen/02-bacteria/neisseria-meningitidis/README.md)** — Its complement-blocking cure invites meningococcus: eculizumab and ravulizumab, the mainstays of aHUS therapy, cut off the terminal complement that kills Neisseria, mandating meningococcal vaccination and prophylaxis.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Its microangiopathy reaches the heart: aHUS thrombotic microangiopathy and severe hypertension can injure the myocardium and coronary microvasculature, an extra-renal manifestation that can precipitate heart failure.
- `connects-to` → **[Pulmonary Arterial Hypertension](../pulmonary-arterial-hypertension/README.md)** — Microvascular thrombi can pressurize the lungs: the systemic endothelial injury and thrombotic microangiopathy of aHUS can involve the pulmonary vasculature, contributing to pulmonary hypertension.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Its microthrombi injure the gut: aHUS thrombotic microangiopathy can involve the GI tract, causing pancreatitis, hepatic dysfunction, colitis and bowel ischaemia as extra-renal manifestations.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Severe microvascular thrombosis reaches the skin: extensive aHUS can cause cutaneous microvascular ischaemia with digital and skin necrosis when the thrombotic microangiopathy is widespread.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A sudden, relapsing, complement-driven disease breeds worry: the abrupt kidney-and-blood crisis, relapse risk and indefinite complement-blocking therapy of aHUS foster chronic health anxiety alongside depression.
- `connects-to` → **[Immune System](../immune-system/README.md)** — It is a disease of uncontrolled complement: mutations in alternative-pathway regulators or anti-factor-H antibodies let complement attack the endothelium, which is why complement-blocking eculizumab is the treatment.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its microthrombi strike the heart: the thrombotic microangiopathy of aHUS can occlude cardiac microvessels, causing ischaemia, arrhythmia and cardiomyopathy beyond the hypertension it drives.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It can injure the pancreatic islets: thrombotic microangiopathy of the pancreatic microvasculature can impair insulin-producing islets, causing transient hyperglycaemia during an aHUS crisis.
- `connects-to` → **[Renal System](../renal-system/README.md)** — The kidney is its prime target: aHUS is fundamentally a renal thrombotic microangiopathy causing acute kidney injury that often progresses to end-stage failure without complement-blocking therapy.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Severe disease can flood the lungs: diffuse alveolar haemorrhage and pulmonary thrombotic microangiopathy occur in severe systemic aHUS.
- `connects-to` → **[Neisseria meningitidis](../../../02-pathogen/02-bacteria/neisseria-meningitidis/README.md)** — Its life-saving drug invites meningococcus: eculizumab blocks the terminal complement that defends against Neisseria meningitidis, so vaccination is mandatory before treating aHUS.
- `connects-to` → **[Influenza A](../../../02-pathogen/01-viruses/influenza-a/README.md)** — Infection can flip the switch: influenza A, especially H1N1, is a recognised trigger that unmasks complement-mediated aHUS in genetically predisposed people, precipitating thrombotic microangiopathy.
- `connects-to` → **[HIV-1](../../../02-pathogen/01-viruses/hiv-1/README.md)** — A virus that injures the endothelium: untreated HIV can cause a thrombotic microangiopathy resembling aHUS, through direct endothelial damage and complement activation.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Some chemotherapy mimics it: drugs such as gemcitabine and mitomycin C cause a drug-induced thrombotic microangiopathy that overlaps clinically with complement-mediated aHUS.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Complement blockade transformed it: the anti-C5 monoclonals eculizumab and ravulizumab halt the uncontrolled alternative-complement activation of aHUS, preventing the microthrombi and rescuing the kidney where plasma exchange once failed.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — It thickens small arteries: the thrombotic microangiopathy of aHUS injures arteriolar and capillary walls, producing the onion-skin intimal swelling and luminal narrowing of renal arterioles characteristic of TMA.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Microthrombi reach the heart: aHUS is not kidney-limited — complement-driven microthrombi in the myocardial microvasculature cause cardiac ischaemia and dysfunction in a notable minority, contributing to its mortality.
- `connects-to` → **[Inherited Thrombophilia](../inherited-thrombophilia/README.md)** — Complement versus coagulation thrombosis: atypical haemolytic uraemic syndrome thromboses the microvasculature through uncontrolled complement, contrasting with the coagulation-factor defects of inherited thrombophilia—two genetic routes to clotting.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — A virus that can trigger it: severe COVID-19 activates complement and injures the endothelium, precipitating a thrombotic microangiopathy resembling aHUS in susceptible patients.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — It is not only renal: although aHUS is a renal-predominant thrombotic microangiopathy, uncontrolled complement can also injure the pulmonary alveolar-capillary bed, causing extrarenal lung involvement in severe disease.
- `connects-to` → **[Myasthenia Gravis](../myasthenia-gravis/README.md)** — A complement-therapy bridge: the anti-C5 drugs (eculizumab, ravulizumab) that control aHUS also treat complement-mediated diseases like myasthenia gravis, the same terminal pathway behind very different illnesses.
- `connects-to` → **[IgA Nephropathy](../iga-nephropathy/README.md)** — Complement in the glomerulus: aHUS and IgA nephropathy both involve alternative-complement dysregulation injuring the glomerulus, and C5- and factor-B-targeted inhibitors are now used or trialled in both.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Systemic, not only renal: as a complement-driven thrombotic microangiopathy, aHUS can also injure the skin and gut with the same microthrombi, causing digital ischaemia and extrarenal organ damage in severe disease.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — The STEC-HUS differential: typical HUS follows Shiga-toxin E. coli colitis that damages the intestinal epithelium with bloody diarrhoea, the key diagnosis to distinguish from complement-driven, often diarrhoea-negative aHUS.
- `connects-to` → **[Pancreatic Cancer](../pancreatic-cancer/README.md)** — Cancer-associated TMA: mucin-producing adenocarcinomas like pancreatic cancer and chemotherapies such as gemcitabine and mitomycin cause a secondary thrombotic microangiopathy that mimics aHUS but needs treating the cause.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Microthrombi in the heart: the complement-driven microangiopathy of aHUS lodges platelet-rich thrombi in the myocardium and its conduction system, causing arrhythmia and cardiac injury as extrarenal complications.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — Endothelial dysfunction: complement injury to the endothelium in aHUS cuts nitric oxide production, removing the vessel's vasodilator and antithrombotic brake and worsening the microangiopathy.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Vasoconstrictor surge: injured endothelium in aHUS releases endothelin-1, whose vasoconstriction aggravates the renal ischaemia and severe hypertension of the thrombotic microangiopathy.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — Malignant hypertension: renal microangiopathy in aHUS activates the renin-angiotensin system, and the resulting angiotensin-II-driven hypertension can itself drive a self-perpetuating TMA.
- `connects-to` → **[PF4](../../03-molecular/pf4/README.md)** — Platelet microthrombi: complement attack on the aHUS endothelium activates platelets to release PF4 and form the platelet-rich microthrombi that consume platelets and occlude the renal microvasculature.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — Neutrophil thromboinflammation: S100A8/A9 and neutrophil extracellular traps released in aHUS further activate complement and the endothelium, amplifying the thrombotic microangiopathy.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — Heme danger signal: free heme from the intravascular haemolysis of aHUS acts as a TLR4 agonist, driving endothelial inflammation that compounds the complement-mediated microvascular injury.
- `connects-to` → **[Protein C](../../03-molecular/protein-c/README.md)** — THBD (thrombomodulin) mutations cause a subset of aHUS by impairing the thrombomodulin-protein C anticoagulant pathway and its complement regulation, tipping the renal microvasculature toward the thrombosis that defines the disease.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — Complement injury to the aHUS endothelium raises the angiopoietin-2/angiopoietin-1 ratio, destabilizing the Tie2-regulated vascular barrier and promoting the leak and thrombosis of the thrombotic microangiopathy.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — CCL2 released by the injured glomerular endothelium recruits monocytes that amplify the inflammatory damage of the thrombotic microangiopathy in the aHUS kidney, compounding the complement-driven injury.
- `connects-to` → **[RAGE](../../03-molecular/rage/README.md)** — The microangiopathic hemolysis of aHUS releases free heme that, as a DAMP signaling through RAGE, further activates complement and endothelium—a vicious cycle in which hemolysis feeds the complement-driven injury that caused it.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Mechanical fragmentation of red cells across the complement-damaged glomerular microvasculature produces the Coombs-negative hemolytic anemia of aHUS, outpacing the erythropoietin-driven marrow response.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Sublytic membrane-attack-complex deposition on glomerular endothelium triggers caspase-3-mediated apoptosis as well as activation, the endothelial cell death that exposes prothrombotic surfaces and seeds the renal microthrombi of aHUS.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — The glomerular microthrombi of aHUS produce renal ischemia that drives HIF-mediated hypoxic responses, the basis of the acute kidney injury that dominates its presentation.
- `connects-to` → **[TNF-α (Tumor Necrosis Factor-alpha)](../../03-molecular/tnf-alpha/README.md)** — TNF-α-driven endothelial activation, often from an infectious trigger, tips the complement-vulnerable aHUS endothelium into the thrombotic microangiopathy of an acute episode.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Complement C5a (already mapped) and endothelial injury activate the NLRP3 inflammasome, adding an inflammatory dimension to the complement-driven microangiopathy of aHUS.
- `connects-to` → **[Thrombopoietin](../../03-molecular/thrombopoietin/README.md)** — As platelets are consumed into microthrombi in the thrombotic microangiopathy of aHUS, the falling count drives a compensatory thrombopoietin response.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Serotonin released from activated platelet dense granules promotes further aggregation and vasoconstriction, propagating the microvascular thrombosis of aHUS.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — Endothelial DAMPs engage TLR4 (mapped) and MyD88 to NF-κB (mapped), amplifying the inflammatory injury that compounds the complement-driven microangiopathy of aHUS.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Sublytic complement attack on the renal endothelium triggers PI3K-AKT survival and activation signaling, shaping the endothelial response that determines microangiopathic injury in aHUS.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — C5a acting on C5aR (C5aR1 mapped) engages ERK-MAPK in endothelium and leukocytes, amplifying the complement-driven thromboinflammation of aHUS.
- `connects-to` → **[Fibrinogen](../../03-molecular/fibrinogen/README.md)** — Fibrinogen conversion to fibrin underlies the platelet-fibrin microthrombi that occlude the microvasculature in the thrombotic microangiopathy of aHUS (thrombin and vWF mapped).
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 promotes the neutrophil-extracellular-trap-driven thromboinflammation and endothelial activation that amplify the thrombotic microangiopathy of aHUS.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — DNA within complement-triggered neutrophil extracellular traps engages cGAS-STING, linking NET-driven inflammation to the microvascular thrombosis of aHUS.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling transduces the inflammatory cytokine response that accompanies the endothelial injury of aHUS.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK1/2-STAT cytokine signaling (IL-6 already mapped) amplifies the endothelial inflammatory response in the complement-driven thrombotic microangiopathy of aHUS.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the endothelial activation that contributes to the microvascular injury of aHUS.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO downstream of PI3K-AKT signaling (AKT already mapped) regulates the endothelial quiescence and oxidative-stress balance disrupted in aHUS.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the platelet-activation and endothelial signaling relevant to the thrombotic microangiopathy of atypical hemolytic uremic syndrome.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR signaling in activated endothelium participates in the complement-driven vascular injury of atypical hemolytic uremic syndrome.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) shapes the endothelial activation and survival during the complement-mediated injury of atypical hemolytic uremic syndrome.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of platelet and endothelial receptors participates in the platelet activation and endothelial injury of atypical hemolytic uremic syndrome.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked endothelial metabolic signaling modulates the microvascular homeostasis relevant to atypical hemolytic uremic syndrome.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated cytotoxic activity contributes to the endothelial injury of the thrombotic microangiopathy in atypical hemolytic uremic syndrome.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the endothelial-cell homeostasis relevant to the thrombotic microangiopathy of atypical hemolytic uremic syndrome.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte recruitment participates in the endothelial inflammation and renal injury of atypical hemolytic uremic syndrome.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic modulation of the complement and endothelial gene expression relevant to atypical hemolytic uremic syndrome.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the endothelial and leukocyte interactions of the thrombotic microangiopathy of atypical hemolytic uremic syndrome.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the endothelial injury and thromboinflammation of atypical hemolytic uremic syndrome.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the endothelial activation of atypical hemolytic uremic syndrome.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — Anti-factor-H autoantibodies: a subset of atypical HUS is caused by IgG autoantibodies against factor H (already mapped), usually with CFHR gene deletions, an acquired form managed with immunosuppression and plasma exchange rather than lifelong complement blockade alone.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Extrarenal microangiopathy: the thrombotic microangiopathy of atypical HUS is not confined to the kidney, and cardiac involvement with myocardial microthrombi raising troponin reflects the systemic endothelial injury that also affects the brain.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Platelet activation: sublytic complement C5b-9 deposited on platelets and endothelium triggers calcium-dependent activation and procoagulant microvesicle release, driving the microthrombi that consume platelets in the thrombotic microangiopathy.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Pregnancy trigger: pregnancy and the postpartum period are major triggers of atypical HUS in genetically predisposed women, the estrogen-associated haemostatic and complement changes unmasking the underlying complement dysregulation.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Complement-kinin crosstalk: complement activation intersects with the kinin system, and bradykinin-driven vascular permeability contributes to the endothelial injury (already mapped) and oedema of the thrombotic microangiopathy in atypical HUS.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative haemolysis: mechanical fragmentation of red cells in the microthrombi releases haem and drives oxidative stress, to which xanthine-oxidase-derived reactive oxygen species contribute, compounding the microangiopathic haemolysis (haemoglobin already mapped).
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immune counter-regulation: IL-10 opposes the inflammatory cytokines (IL-6, TNF and IL-1 already mapped) amplified by the complement activation of atypical HUS, part of the immune balance in the thrombotic microangiopathy.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — Renal RAAS activation: the renal injury and hypertension of atypical HUS activate the renin-angiotensin system (angiotensin II already mapped), and the resulting aldosterone drives sodium retention and further vascular and renal damage.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Haemolytic iron load: the chronic microangiopathic haemolysis (haemoglobin already mapped) and repeated transfusions of atypical HUS load the body with iron, adding an iron-overload burden to the disease and its management.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Thromboxane and platelets: the activated platelets (PF4 and serotonin already mapped) of atypical HUS generate thromboxane to amplify aggregation, part of the eicosanoid contribution to the microthrombosis of the thrombotic microangiopathy.
- `connects-to` → **[Renin](../../03-molecular/renin/README.md)** — Renal renin activation: the renal injury and hypertension of atypical HUS activate renin, driving the angiotensin II and aldosterone (already mapped) that worsen the vascular and renal damage.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Platelet zinc and coagulation: zinc released from the activated platelets (already mapped) promotes the contact pathway and fibrin formation (fibrinogen and thrombin already mapped), adding to the prothrombotic state of atypical HUS.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Haemolytic iron handling: the intravascular microangiopathic haemolysis (haemoglobin already mapped) and the inflammation (IL-6 already mapped) disturb the hepcidin-regulated iron handling of atypical HUS.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron loss and release: the intravascular haemolysis of atypical HUS releases iron and causes urinary iron loss, disturbing the iron balance (hepcidin already mapped) alongside the anaemia (haemoglobin already mapped).
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Electrolyte derangement: the renal impairment of atypical HUS, and the citrate of any plasma exchange, disturb the magnesium (with calcium already mapped) balance, needing replacement.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Immune-metabolic adipokine: leptin is the adipokine of the immune-metabolic milieu that modulates the endothelial (already mapped) and complement inflammation of atypical HUS.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic-inflammatory milieu of atypical HUS.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the inflammatory (IL-6 and TNF already mapped) milieu of atypical HUS.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate immune crosstalk: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, is part of the innate-immune dimension that crosstalks with the complement (C3 already mapped) dysregulation of atypical HUS.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 arm: the IFN-γ of the T cells is the type-II interferon arm of the inflammatory dimension (IL-6 and TNF already mapped) accompanying the complement-mediated endothelial (already mapped) injury of atypical HUS.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension of atypical HUS.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Type-2 arm: IL-4 is the prototypical type-2 cytokine of the immune milieu that balances the Th1 (IFN-γ already mapped) inflammation accompanying the complement-mediated injury of atypical HUS.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 arm: IL-13, with IL-4 (already mapped), completes the type-2/Th2 dimension of the immune milieu accompanying the complement-mediated endothelial (already mapped) injury of atypical HUS.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Eosinophil arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune milieu accompanying atypical HUS.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement regulation: the C1-esterase inhibitor regulates the classical and lectin complement pathways, complementing the factor H (already mapped) control of the alternative pathway (complement C3, C5 and C5aR1 already mapped) dysregulated in atypical HUS.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2 (IFN-γ and IL-4 already mapped) cytokines of the immune milieu accompanying the complement-mediated endothelial (already mapped) injury of atypical HUS.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the type-2 immune dimension of the immune milieu accompanying atypical HUS.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Thromboinflammation: osteopontin, released by the activated platelets (already mapped), is a matricellular mediator linking the complement-driven endothelial (already mapped) injury to the microthrombosis of atypical HUS.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Haemolytic iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the microangiopathic haemolysis of atypical HUS.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Adaptive milieu: the cytotoxic T cells (perforin already mapped), with the T-helper (already mapped) arm, are part of the adaptive-immune milieu accompanying the complement-mediated endothelial injury of atypical HUS.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-endothelial axis: TSLP, released from injured renal (already mapped) endothelium under complement (C3, C5, C5aR1 and factor H already mapped) stress, activates mast cells (already mapped) and dendritic cells, amplifying the thromboinflammatory cascade of atypical HUS.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell vasodilator: histamine, released from activated mast cells (already mapped) in the complement-driven vascular inflammation of atypical HUS, augments endothelial permeability and amplifies the microvascular thromboinflammation alongside nitric-oxide depletion.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Fibrotic matricellular: periostin, a matricellular mediator upregulated in the renal (already mapped) tubulointerstitium under complement-driven injury in aHUS, promotes fibroblast (already mapped) activation and the progressive renal fibrosis of atypical HUS.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian complement modulation: melatonin, via MT1/MT2 receptors on endothelial cells (already mapped) and macrophages (already mapped), scavenges ROS (already mapped) and attenuates the nocturnal complement activation surge driving TMA episodes in atypical HUS.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Immune-endocrine haematopoietic axis: prolactin, acting via PRLR on haematopoietic progenitors (already mapped) and T-helper cells (already mapped), modulates the immune activation and the complement-driven thromboinflammatory microangiopathy of atypical HUS.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Neuroimmune endothelial protection: oxytocin, via oxytocin receptors on endothelial cells (already mapped) and macrophages (already mapped), suppresses the NF-κB-driven (already mapped) pro-inflammatory cytokine cascade and limits endothelial injury in atypical HUS.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Androgen complement suppression: testosterone, via androgen receptors on endothelial cells (already mapped), suppresses complement-C5 (already mapped); androgen deficiency amplifies TMA severity, glomerulus (already mapped) microangiopathy, and the haemolytic cascade in aHUS.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Antioxidant endothelial defence: selenium, via glutathione peroxidase (GPx), shields endothelial cells (already mapped) from complement-C5 (already mapped)-driven oxidative injury; selenium deficiency amplifies haemolytic microangiopathic stress and platelet (already mapped) activation of aHUS.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Renal tubular stress: vasopressin, via V2 receptors on renal tubular cells, promotes fluid retention and hypertension (already mapped) in aHUS; vasopressin also amplifies endothelial cell (already mapped) oxidative stress and kidney (already mapped) microangiopathic injury.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Thyroid-endothelial axis: iodine-dependent thyroid hormones modulate endothelial-cell (already mapped) function and platelet (already mapped) reactivity; iodine deficiency amplifies the complement-C5 (already mapped) and NF-κB (already mapped) microangiopathic cascade of aHUS.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Osmotic microangiopathic amplifier: sodium dysregulation amplifies hypertension (already mapped) and endothelial-cell (already mapped) injury in aHUS; hypernatraemia-driven osmotic stress activates the NF-κB (already mapped) and complement-C5 (already mapped) microangiopathic cascade of aHUS.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Superoxide dismutase cofactor: copper, as cofactor of superoxide dismutase in endothelial cells (already mapped) and kidney (already mapped) tubular cells, scavenges complement-C5 (already mapped)-driven ROS; copper deficiency amplifies the microangiopathic and haemolytic cascade of aHUS.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — aHUS phosphorus: phosphorus fuels endothelial-cell (already mapped) and platelet (already mapped) ATP; phosphorus deficiency impairs complement-C5 (already mapped) regulation and amplifies NF-κB (already mapped) and IL-6 (already mapped) microangiopathic cascade of aHUS.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — aHUS nitrogen: nitric oxide (NO, nitrogen-derived) in endothelial cells (already mapped) regulates vasodilation and platelet (already mapped) inhibition; NO deficiency amplifies complement-C5 (already mapped) and NF-κB (already mapped) microangiopathic cascade of aHUS.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — aHUS chloride: chloride channels on endothelial cells (already mapped) and kidney (already mapped) tubular cells maintain ionic homeostasis; chloride dysregulation amplifies complement-C5 (already mapped) and NF-κB (already mapped) and thrombin (already mapped) cascade of aHUS.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — aHUS sulfur: sulfur-containing glutathione in endothelial cells (already mapped) and macrophages (already mapped) quenches complement-C5 (already mapped)-driven ROS; sulfur deficiency amplifies NF-κB (already mapped) and thrombin (already mapped) microangiopathic cascade of aHUS.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — carbon, via bicarbonate in endothelial cells (already mapped) and kidney (already mapped) tubular cells, maintains pH homeostasis; pH dysregulation amplifies complement-C5 (already mapped) and NF-κB (already mapped) and thrombin (already mapped) microangiopathic cascade of aHUS.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — hydrogen, via H2O2 and ROS balance in endothelial cells (already mapped) and macrophages (already mapped), sets redox tone; hydrogen excess amplifies complement-C5 (already mapped) and NF-κB (already mapped) and thrombin (already mapped) microangiopathic cascade of aHUS.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — TGF-β from macrophages (already mapped) and endothelial cells (already mapped) promotes fibrotic remodelling of glomerulus (already mapped) in aHUS; TGF-β amplifies NF-κB (already mapped) and complement-C5 (already mapped) mesangial expansion and microangiopathic progression.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — aHUS PD-1: PD-1 on T-cytotoxic-cell (already mapped) and t-helper-cell (already mapped) modulates thromboinflammatory homeostasis; PD-1 dysregulation amplifies complement-C5 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) microangiopathic cascade of aHUS.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — aHUS GLP-1: GLP-1 signalling in endothelial cells (already mapped) and podocytes (already mapped) modulates renal metabolic homeostasis; GLP-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and complement-C5 (already mapped) cascade of aHUS.
- `connects-to` → **[WNT/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — aHUS WNT/β-catenin: WNT/β-catenin in endothelial cells (already mapped) and podocytes (already mapped) drives glomerular repair; WNT dysregulation amplifies NF-κB (already mapped) and TGF-β (already mapped) fibrotic remodelling and complement-C5 (already mapped) cascade of aHUS.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — aHUS RANKL: RANKL signalling in endothelial cells (already mapped) and macrophages (already mapped) modulates renal bone-immune axis; RANKL excess amplifies NF-κB (already mapped) and complement-C5 (already mapped) and IL-6 (already mapped) cascade of aHUS.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — aHUS SMAD4: SMAD4 in endothelial cells (already mapped) and podocytes (already mapped) mediates TGF-β-driven renal fibrosis; SMAD4 dysregulation amplifies NF-κB (already mapped) and complement-C5 (already mapped) and IL-6 (already mapped) cascade of aHUS.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — aHUS IL-2: IL-2 signalling in T-cells (already mapped) and macrophages (already mapped) modulates complement-driven immune tolerance; IL-2 deficiency amplifies NF-κB (already mapped) and complement-C5 (already mapped) and IL-6 (already mapped) cascade of aHUS.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — aHUS fibronectin: fibronectin in glomerular endothelium (already mapped) and podocytes (already mapped) modulates microvascular integrity; fibronectin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of aHUS.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — aHUS Notch: Notch signalling in glomerular endothelium (already mapped) and mesangial cells (already mapped) modulates vascular remodelling; Notch dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of aHUS.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — aHUS IGF-1: IGF-1 signalling in podocytes (already mapped) and mesangial cells (already mapped) sustains glomerular repair; IGF-1 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of aHUS.

[^fakhouri-2017-ahus-lancet]: Fakhouri F, Zuber J, Frémeaux-Bacchi V, Loirat C. Haemolytic uraemic syndrome. *Lancet.* 2017;390(10095):681-696. [doi:10.1016/S0140-6736(17)30062-4](https://doi.org/10.1016/S0140-6736(17)30062-4) · [PubMed 28242109](https://pubmed.ncbi.nlm.nih.gov/28242109/)
[^legendre-2013-eculizumab-ahus-nejm]: Legendre CM, Licht C, Muus P, et al. Terminal complement inhibitor eculizumab in atypical hemolytic-uremic syndrome. *N Engl J Med.* 2013;368(23):2169-2181. [doi:10.1056/NEJMoa1208981](https://doi.org/10.1056/NEJMoa1208981) · [PubMed 23738544](https://pubmed.ncbi.nlm.nih.gov/23738544/)
[^goodship-2017-ahus-consensus]: Goodship TH, Cook HT, Fakhouri F, et al. Atypical hemolytic uremic syndrome and C3 glomerulopathy: conclusions from a KDIGO Controversies Conference. *Kidney Int.* 2017;91(3):539-551. [doi:10.1016/j.kint.2016.10.005](https://doi.org/10.1016/j.kint.2016.10.005) · [PubMed 28062089](https://pubmed.ncbi.nlm.nih.gov/28062089/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
