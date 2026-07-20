---
schema: human-scale-entry/v1
id: anca-vasculitis
name: ANCA Vasculitis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "ANCA vasculitis (GPA, MPA, EGPA): small-vessel necrotizing vasculitis; anti-PR3 or anti-MPO IgG primes neutrophils via C5a/C5aR1 → NET formation → endothelial injury. Cyclophosphamide/rituximab induction; avacopan (steroid-sparing; FDA Oct 2021) and rituximab maintenance."
aliases: ["ANCA vasculitis", "AAV", "GPA", "MPA", "EGPA", "granulomatosis with polyangiitis", "microscopic polyangiitis", "eosinophilic granulomatosis", "Wegener's granulomatosis", "Churg-Strauss syndrome", "pauci-immune vasculitis", "anti-PR3 vasculitis", "anti-MPO vasculitis"]
sources:
  - id: jayne-2021-avacopan-advocate
    type: peer-reviewed
    cite: "Jayne DRW, Merkel PA, Schall TJ, Bekker P. Avacopan for the Treatment of ANCA-Associated Vasculitis. N Engl J Med. 2021;384(7):599-609."
    doi: "10.1056/NEJMoa2021349"
    pmid: "33596356"
    url: "https://doi.org/10.1056/NEJMoa2021349"
  - id: stone-2010-rituximab-gpa-rave
    type: peer-reviewed
    cite: "Stone JH, Merkel PA, Spiera R, et al. Rituximab versus cyclophosphamide for ANCA-associated vasculitis. N Engl J Med. 2010;363(3):221-232."
    doi: "10.1056/NEJMoa0909905"
    pmid: "20647199"
    url: "https://doi.org/10.1056/NEJMoa0909905"
  - id: specks-2013-rituximab-anca-maintenance
    type: peer-reviewed
    cite: "Charles P, Terrier B, Perrodeau É, et al. Comparison of individually tailored versus fixed-schedule rituximab regimen to maintain ANCA-associated vasculitis remission. Ann Rheum Dis. 2018;77(8):1143-1149."
    doi: "10.1136/annrheumdis-2017-212862"
    pmid: "29549154"
    url: "https://doi.org/10.1136/annrheumdis-2017-212862"
  - id: yates-2022-anca-review
    type: peer-reviewed
    cite: "Yates M, Watts RA, Bajema IM, et al. EULAR/ERA-EDTA recommendations for the management of ANCA-associated vasculitis. Ann Rheum Dis. 2016;75(9):1583-1594."
    doi: "10.1136/annrheumdis-2016-209133"
    pmid: "27338776"
    url: "https://doi.org/10.1136/annrheumdis-2016-209133"
cross_links:
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a primes neutrophils via C5aR1 → surface PR3/MPO → ANCA IgG crosslinking → NETosis + ROS → endothelial injury; avacopan (C5aR1 antagonist; ADVOCATE trial: 65.7% vs 54.9% sustained remission; FDA Oct 2021) blocks neutrophil priming."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Complement activation generates C5a in ANCA vasculitis; C5a–C5aR1 primes neutrophils for ANCA-triggered NETosis; C5b-9 MAC contributes to endothelial injury; avacopan (C5aR1) allows glucocorticoid sparing without inhibiting C5b-9-mediated pathogen defense."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "Rituximab (anti-CD20) is non-inferior to cyclophosphamide for ANCA vasculitis induction (RAVE trial: 64% vs 53% complete remission; FDA Apr 2011 for GPA/MPA) and is preferred for maintenance; rituximab reduces ANCA-producing B cells and PR3/MPO autoantibody titers."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "ANCA (anti-neutrophil cytoplasmic antibodies) are IgG autoantibodies (IgG3 > IgG1) against PR3 (cANCA; GPA) or MPO (pANCA; MPA/EGPA); ANCA IgG Fc engages FcγRIIa on neutrophils → full effector activation; ANCA titers correlate with disease activity and relapse risk."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils are the primary effector cells in ANCA vasculitis; ANCA IgG (anti-PR3 or anti-MPO) crosslinks surface PR3/MPO on C5a-primed neutrophils → FcγRIIa → exuberant NETosis + respiratory burst → fibrinoid necrosis of small vessel walls and pauci-immune crescentic GN."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Crescentic pauci-immune GN in GPA/MPA → rapidly progressive kidney failure; untreated AAV → ESRD within weeks-months; avacopan (ADVOCATE) preserves eGFR significantly better than prednisone at 52 weeks; ANCA GN is a leading cause of vasculitis-related dialysis."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "AAV renal involvement progresses to CKD in up to 40% at 5 years; ESRD in 20-25% over 10 years; creatinine at diagnosis and % crescents on biopsy predict CKD trajectory; avacopan eGFR advantage at 52 weeks may translate to reduced long-term CKD progression."
  - target: 01-human/07-system/giant-cell-arteritis
    relation: connects-to
    note: "ANCA vasculitis and giant cell arteritis sit at opposite ends of the vessel spectrum: AAV attacks small vessels with pauci-immune necrotizing inflammation, GCA the large arteries with granulomatous giant cells — contrasting poles classified by vessel caliber and histology."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "B cells are the source of ANCA: they become plasma cells secreting IgG against PR3 or MPO, which is why anti-CD20 rituximab (RAVE trial) — depleting B cells and lowering autoantibody titers — is non-inferior to cyclophosphamide for induction and preferred for maintenance."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "AAV is a pulmonary-renal syndrome: small-vessel inflammation in the alveolar capillaries causes diffuse alveolar hemorrhage (hemoptysis, hypoxemia) alongside crescentic glomerulonephritis, and GPA additionally produces necrotizing granulomas of the upper and lower airways."
  - target: 01-human/07-system/asthma
    relation: connects-to
    note: "Asthma defines one ANCA-vasculitis subtype: eosinophilic granulomatosis with polyangiitis (EGPA, Churg-Strauss) arises in patients with adult-onset asthma and eosinophilia who then develop vasculitis; only ~40% are ANCA-positive, and anti-IL-5 (mepolizumab) treats it."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "The skin is a common, accessible window on ANCA-vasculitis: small-vessel inflammation produces palpable purpura, livedo, nodules and ulcers, and a skin biopsy showing leukocytoclastic vasculitis helps confirm the diagnosis while sparing the patient an organ biopsy."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages build the granulomas of ANCA-vasculitis: in granulomatosis with polyangiitis, neutrophil activation and necrosis recruit macrophages that organize into the necrotizing granulomas of lung and sinuses, distinguishing GPA from non-granulomatous microscopic polyangiitis."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "ANCA vasculitis is not purely antibody-driven—T-helper cells orchestrate it: autoreactive Th1 and Th17 cells help B cells make ANCA and form GPA granulomas, so T-cell- and B-cell-directed therapies both work, and relapse tracks T-cell inflammation."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Plasma cells make the pathogenic ANCA antibodies (anti-PR3, anti-MPO): these autoantibodies activate primed neutrophils to injure small vessels, and because long-lived plasma cells resist rituximab, persistent autoantibody helps explain relapse and refractory disease."
  - target: 01-human/07-system/hepatitis-b
    relation: connects-to
    note: "ANCA vasculitis must be distinguished from hepatitis-B-associated vasculitis: HBV classically causes polyarteritis nodosa—an immune-complex, ANCA-negative medium-vessel vasculitis—so vasculitis workup checks viral serologies, since antivirals treat HBV disease."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Endothelial cells are the battlefield of ANCA vasculitis: ANCA-activated neutrophils adhere to and destroy vessel endothelium, causing necrotizing inflammation that infarcts glomeruli, lung capillaries and skin—so endothelial injury underlies the multi-organ damage."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "ANCA vasculitis and lupus both attack the kidney but by opposite mechanisms: ANCA causes pauci-immune glomerulonephritis with little immune-complex deposition, while lupus nephritis is driven by immune-complex deposits—a key distinction on renal biopsy."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "ANCA vasculitis is a breakdown of immune tolerance: the immune system makes antibodies against its own neutrophil enzymes (PR3 or MPO), which turn neutrophils into agents of vascular destruction—so B-cell-depleting therapy that removes the autoantibody source works."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "ANCA vasculitis attacks the glomerulus ferociously: ANCA-activated neutrophils damage glomerular capillaries, producing the pauci-immune crescentic glomerulonephritis that causes rapidly progressive kidney failure—a medical emergency needing urgent immunosuppression."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "ANCA vasculitis often strikes peripheral nerves: inflammation of the small vessels feeding nerves causes ischemic mononeuritis multiplex—sudden foot- or wrist-drop—so a vasculitic neuropathy can be an early, diagnostic clue to systemic ANCA disease."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "ANCA vasculitis is a classic pulmonary-renal syndrome: it inflames the airways and alveolar capillaries, causing sinusitis, lung nodules and life-threatening alveolar hemorrhage alongside the kidney disease—so respiratory and renal involvement often present together."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "ANCA vasculitis often inflames the eye: granulomatosis with polyangiitis causes scleritis, episcleritis, and orbital masses that can threaten vision, so red, painful eyes can be an early clue—part of its classic ear-nose-eye-lung-kidney pattern."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "ANCA vasculitis damages peripheral nerves as mononeuritis multiplex: inflammation of the small vessels feeding nerves causes patchy, asymmetric foot- or wrist-drop, a hallmark vasculitic neuropathy that signals active, organ-threatening disease."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Eosinophilic GPA (Churg-Strauss), an ANCA-associated vasculitis, is IL-5-driven: this cytokine expands the eosinophils that infiltrate lungs, nerves, and heart, so the anti-IL-5 antibody mepolizumab is an approved targeted treatment for it."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "ANCA vasculitis runs on the alternative complement pathway: ANCA-activated neutrophils generate C3 and C5a that recruit and prime more neutrophils in a self-amplifying loop—so complement blockade (avacopan) spares steroids."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "ANCA vasculitis scars what it inflames: crescentic glomerulonephritis fibroses into kidney failure, and MPO-ANCA disease can cause progressive pulmonary fibrosis—so early immunosuppression aims to halt inflammation before irreversible fibrosis sets in."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "ANCA vasculitis reflects failed regulatory T-cell control: defective Tregs let autoreactive B and T cells drive anti-MPO/PR3 autoimmunity, so restoring immune tolerance is a goal beyond the B-cell depletion that current therapy relies on."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "ANCA vasculitis can strike the heart, especially in EGPA: eosinophilic myocarditis and coronary inflammation damage the muscle, making cardiac involvement the leading cause of death in the eosinophilic form of the disease."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Primed neutrophils drive ANCA vasculitis partly via the NLRP3 inflammasome: it amplifies inflammatory signaling and NET release when ANCA antibodies activate the cells, fueling the vessel-wall damage at the disease's core."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells help break tolerance in ANCA vasculitis: by presenting MPO and PR3 fragments to T cells, they license the autoimmune response that drives B cells to make the ANCA antibodies, a step upstream of current B-cell therapy."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "ANCA vasculitis can starve the lungs of oxygen: inflamed alveolar capillaries bleed into the air sacs (diffuse alveolar hemorrhage), so gas exchange fails—a pulmonary-renal emergency that can need a ventilator."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "ANCA vasculitis can strangle the gut: inflammation of the bowel's small vessels causes mesenteric ischemia, abdominal pain, and GI bleeding, a serious extrarenal manifestation of severe disease."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "ANCA vasculitis can reach the brain: inflammation of cerebral vessels and the dura causes strokes, seizures, and pachymeningitis, extending the small-vessel attack into the central nervous system."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Imaging maps ANCA vasculitis: chest CT photons reveal the lung nodules, cavities and alveolar hemorrhage of granulomatosis, and sinus scans show the destructive upper-airway disease."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "ANCA vasculitis can flood the alveoli: capillaritis in the lung's gas-exchange units causes diffuse alveolar hemorrhage, a life-threatening bleed that fills the air sacs and drops the blood count."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Alveolar hemorrhage in ANCA vasculitis leaves an iron trail: blood in the air sacs is engulfed by iron-laden macrophages, and the falling hemoglobin marks the severity of the lung bleeding."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows what ANCA vasculitis lacks: its inflamed vessels are 'pauci-immune,' nearly free of the immune-complex deposits that fill other vasculitides, because ANCA-activated neutrophils attack the wall directly with their toxic granules and NETs."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "The vasculitis can ulcerate the gut: inflammation of the mesenteric and gastric vessels causes abdominal pain, bleeding, and even bowel perforation, a dangerous abdominal manifestation of systemic disease."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "ANCA vasculitis can infarct the spleen: inflamed, clotting small arteries cut off blood to wedges of splenic tissue, one of the silent organ infarctions that mark widespread vascular involvement."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "The disease is named for its antibody: ANCA against proteinase-3 (c-ANCA) or myeloperoxidase (p-ANCA) both diagnose it and activate neutrophils to attack vessels, and the anti-CD20 antibody rituximab is a frontline treatment."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Inflamed vessels starve the nerves: occlusion of the small arteries feeding peripheral nerves produces mononeuritis multiplex — patchy, painful weakness and numbness that is a classic presenting feature, especially in EGPA."
  - target: 01-human/07-system/bladder-cancer
    relation: connects-to
    note: "The old workhorse drug scars the bladder: cyclophosphamide, long used to induce remission, releases acrolein that inflames the bladder into hemorrhagic cystitis and, over years, raises the risk of bladder cancer — so mesna and dose limits guard against it."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Glucocorticoids anchor induction: high-dose steroids rapidly quench the vasculitis alongside rituximab or cyclophosphamide, but their infection, bone, and metabolic toll drives the modern push to taper them fast."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Active vasculitis is sharply prothrombotic: ANCA disease carries a markedly raised risk of deep-vein thrombosis and pulmonary embolism during flares, the inflamed endothelium tipping the blood toward clotting."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "The inflammation eats the vessel wall: neutrophil-driven necrotizing inflammation destroys the smooth-muscle media of small arteries, weakening them into the microaneurysms and ruptures that bleed into lung and kidney."
  - target: 01-human/04-cellular/podocyte
    relation: connects-to
    note: "The kidney's filter is wrecked from above: pauci-immune necrotizing glomerulonephritis ruptures the capillary tuft and forms crescents that crush the podocytes, producing the hematuria and rapidly rising creatinine that make renal ANCA disease an emergency."
  - target: 01-human/03-molecular/baff
    relation: connects-to
    note: "BAFF keeps the ANCA factories alive: the cytokine sustains the autoreactive B cells that make anti-MPO and anti-PR3 antibodies, the rationale behind rituximab and the B-cell-targeted control of the disease."
  - target: 01-human/07-system/inflammatory-bowel-disease
    relation: connects-to
    note: "ANCA blurs into bowel disease: an atypical perinuclear ANCA is a hallmark antibody of ulcerative colitis, one of the overlaps where the same autoantibody family marks both vasculitis and inflammatory bowel disease."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "A Th17 arm drives the autoimmunity: IL-17A from autoreactive helper T cells promotes neutrophil recruitment and the granulomatous inflammation of GPA, running higher in active ANCA vasculitis."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Autoantibodies are schooled in lymphoid tissue: ectopic germinal centers, including those in inflamed nasal mucosa in GPA, generate the B cells that make anti-PR3 and anti-MPO — which is why germinal-center-directed B-cell depletion works."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "The heart is a hidden target: ANCA vasculitis—especially eosinophilic GPA—can inflame the myocardium and coronary vessels, and the resulting cardiomyopathy is a leading cause of death, so cardiac screening matters even when symptoms are quiet."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "ANCA-primed neutrophils run on NF-κB: cytokine priming activates NF-κB in neutrophils, which then degranulate when ANCA binds their surface PR3 and MPO, driving the explosive small-vessel inflammation of the disease."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Treatment trades vasculitis for infection: the cyclophosphamide, rituximab and high-dose steroids that induce remission leave patients severely immunosuppressed, so infection and sepsis are a leading cause of death — and a mimic of relapse."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "It can inflame the brain's vessels: ANCA vasculitis occasionally involves the cerebral circulation, causing ischemic or hemorrhagic stroke as part of its central nervous system disease."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: connects-to
    note: "Its induction therapy opens the lung: the cyclophosphamide, rituximab and high-dose steroids used to control ANCA vasculitis deplete T-cell defenses, so Pneumocystis prophylaxis is standard during remission induction."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Inflammation and renal disease blunt the marrow: the systemic inflammation of active ANCA vasculitis raises hepcidin while its glomerulonephritis cuts erythropoietin, together producing an anemia of chronic disease."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A relapsing multisystem disease weighs on mood: the chronic, unpredictable course, organ damage and toxic immunosuppression of ANCA vasculitis carry a substantial burden of depression."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Its heavy immunosuppression opens the lung to mold: cyclophosphamide, rituximab and high-dose steroids used to induce remission in ANCA vasculitis deeply blunt immunity, permitting invasive aspergillosis."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "Lung capillaritis and fibrosis can pressurize the arteries: the alveolar hemorrhage and interstitial scarring of ANCA vasculitis damage the pulmonary vasculature, contributing to pulmonary hypertension."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Prolonged steroids erode the skeleton: the months of high-dose corticosteroids needed to control ANCA vasculitis accelerate bone loss and raise fracture risk, a common treatment complication."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Small-vessel inflammation erupts on the skin: ANCA vasculitis causes palpable purpura, cutaneous nodules and ulcers, and granulomatosis with polyangiitis classically destroys the nasal cartilage into a saddle-nose."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It can inflame the gut's vessels: mesenteric vasculitis in ANCA disease causes abdominal pain, bowel ischaemia and GI bleeding, a serious extra-renal manifestation."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "Its heavy immunosuppression reawakens shingles: the cyclophosphamide, rituximab and steroids used to induce remission in ANCA vasculitis deplete immunity, allowing herpes-zoster reactivation."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "The kidney is its classic target: ANCA vasculitis causes pauci-immune crescentic rapidly progressive glomerulonephritis, a renal emergency demanding prompt immunosuppression to prevent permanent failure."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Eosinophilic GPA strikes the heart: myocarditis and cardiomyopathy are a leading cause of death in EGPA, and coronary arteritis can occur, so cardiac assessment is essential."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Granulomatous disease can hit the pituitary: GPA occasionally involves the pituitary gland, causing hypophysitis and diabetes insipidus among its protean manifestations."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It aches in joints and muscles: migratory arthralgia, frank arthritis and myalgia are common features of ANCA-associated vasculitis, especially at disease onset."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Its cyclophosphamide threatens fertility: the alkylating agent long used to induce remission causes ovarian failure and impaired spermatogenesis, prompting fertility preservation before treatment."
  - target: 03-medicine/01-modern/02-respiratory/corticosteroids
    relation: connects-to
    note: "Remission starts with steroids: high-dose glucocorticoids, with rituximab or cyclophosphamide, induce remission in ANCA-associated vasculitis, though their toxicity drives steroid-sparing strategies."
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: connects-to
    note: "A trigger living in the nose: chronic nasal carriage of Staphylococcus aureus is linked to relapse of granulomatosis with polyangiitis, and decolonisation can reduce flares."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Autoimmunity can overlap: rheumatoid arthritis and ANCA vasculitis sometimes coexist, and rheumatoid vasculitis is a feared small-vessel complication of long-standing severe RA."
  - target: 02-pathogen/02-bacteria/mycobacterium-tuberculosis
    relation: connects-to
    note: "A granulomatous mimic to exclude: the lung nodules and cavities of granulomatosis with polyangiitis resemble tuberculosis, which must be excluded before the heavy immunosuppression that would let TB run rampant."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Biologics reshaped its treatment: rituximab against CD20 induces and maintains remission, avacopan blocks the C5a receptor to spare steroids, and mepolizumab against IL-5 treats eosinophilic GPA — targeted therapies for ANCA vasculitis."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Cyclophosphamide induces, at a cost: cyclophosphamide remains a mainstay for organ-threatening ANCA vasculitis, but its bladder toxicity and later bladder-cancer risk push earlier use of rituximab where possible."
  - target: 01-human/07-system/iga-nephropathy
    relation: connects-to
    note: "Two faces of glomerulonephritis: ANCA vasculitis causes a pauci-immune crescentic glomerulonephritis with scant deposits, whereas IgA nephropathy is an immune-complex disease with mesangial IgA — contrasting mechanisms of the same renal emergency."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "Small-vessel vasculitis: ANCA-activated neutrophils degranulate on the walls of small arteries, capillaries and venules, causing the fibrinoid necrosis and vessel destruction that define the disease."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "Gut vasculitis: mesenteric small-vessel involvement, especially in granulomatosis with polyangiitis and EGPA, causes bowel ischaemia, ulceration and, rarely, perforation."
  - target: 01-human/07-system/stimulant-use-disorder
    relation: connects-to
    note: "Drug-induced ANCA vasculitis: levamisole, a common cocaine adulterant, triggers an ANCA-positive vasculitis with skin necrosis and neutropenia—a drug-induced mimic to recognise in stimulant users."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Eosinophilic heart disease: EGPA (Churg-Strauss) infiltrates the myocardium with eosinophils, causing a cardiomyopathy and myocarditis that are a leading cause of death in this ANCA-associated vasculitis."
  - target: 01-human/07-system/hepatitis-c
    relation: connects-to
    note: "An infectious mimic: hepatitis C causes a cryoglobulinaemic small-vessel vasculitis that overlaps clinically with ANCA-associated disease, a key infection to exclude before immunosuppression."
  - target: 01-human/07-system/dlbcl
    relation: connects-to
    note: "Rituximab and lymphoma: the anti-CD20 antibody rituximab is now first-line for ANCA-associated vasculitis—the same drug treating B-cell lymphomas like DLBCL—while chronic immunosuppression slightly raises lymphoma risk."
  - target: 01-human/07-system/systemic-sclerosis
    relation: connects-to
    note: "Scleroderma overlap: a subset of systemic sclerosis patients are MPO-ANCA positive and develop an overlapping ANCA vasculitis with glomerulonephritis, distinct from scleroderma renal crisis."
  - target: 01-human/07-system/sjogrens-syndrome
    relation: connects-to
    note: "Autoimmune co-occurrence: Sjögren's syndrome can coexist with ANCA-associated vasculitis, the two systemic autoimmune diseases sharing B-cell-driven mechanisms and overlapping organ involvement."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6-driven inflammation: interleukin-6 fuels the systemic inflammation, acute-phase response and B-cell help in ANCA vasculitis, making IL-6 blockade a candidate steroid-sparing therapy."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Neutrophil priming: TNF-α primes neutrophils to surface their ANCA antigens, the key first step that lets ANCA antibodies trigger the destructive neutrophil activation of the vasculitis."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Granuloma formation: IFN-γ from Th1 cells drives the granulomatous inflammation characteristic of GPA, shaping the necrotising lesions of ANCA-associated vasculitis."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Inflammasome amplification: NLRP3-driven IL-1β release from activated neutrophils and monocytes adds to the inflammatory tissue injury of ANCA-associated vasculitis."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "NETosis driver: ANCA-activated neutrophils release extracellular traps rich in S100A8/A9 that expose PR3 and MPO autoantigens and directly injure vessel walls, a central mechanism of ANCA-associated vasculitis."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Monocyte recruitment: CCL2 draws monocytes into vasculitic lesions, where they become the macrophages of the granulomatous and necrotising inflammation of ANCA-associated vasculitis."
  - target: 01-human/03-molecular/fibrinogen
    relation: connects-to
    note: "Fibrinoid necrosis: vessel-wall injury in ANCA-associated vasculitis exposes tissue factor and converts fibrinogen to the fibrin of fibrinoid necrosis and the crescents of pauci-immune glomerulonephritis."
  - target: 01-human/03-molecular/btk
    relation: connects-to
    note: "B-cell and neutrophil signalling: BTK transduces B-cell-receptor and Fc-receptor signals in the autoreactive B cells and ANCA-activated neutrophils of the disease, making BTK inhibitors a candidate therapy in AAV."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Infection-primed flares: TLR-mediated priming of neutrophils (as during infection) is required for ANCA to trigger the respiratory burst and NETosis, helping explain why infections precipitate flares of ANCA-associated vasculitis."
  - target: 01-human/03-molecular/thrombin
    relation: connects-to
    note: "Hypercoagulability: active ANCA-associated vasculitis markedly raises venous-thromboembolism risk, with NET- and tissue-factor-driven thrombin generation underlying the thrombotic tendency during disease flares."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: connects-to
    note: "Induction therapy: high-dose glucocorticoids acting through the glucocorticoid receptor are the backbone of remission induction in ANCA vasculitis, rapidly suppressing the neutrophil-driven inflammation, with the C5aR antagonist avacopan now allowing steroid sparing."
  - target: 01-human/03-molecular/fcrn
    relation: connects-to
    note: "Pathogenic-IgG removal: because ANCA are pathogenic IgG autoantibodies, plasma exchange and FcRn-blocking agents that accelerate IgG clearance are used to lower autoantibody levels in severe ANCA vasculitis with rapidly progressive kidney or lung disease."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Genetic predisposition: distinct HLA class II alleles predispose to anti-PR3 (HLA-DP) versus anti-MPO disease, favouring presentation of the neutrophil-autoantigen peptides to T cells that license ANCA production."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Crescentic fibrosis: TGF-β drives the fibrotic crescent formation and glomerulosclerosis that determine renal outcome in ANCA-associated glomerulonephritis."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Alternative-complement priming: the alternative complement pathway, normally restrained by factor H, is primed by ANCA-activated neutrophils to generate the C5a (already mapped) that amplifies vasculitic injury."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Autoantigen exposure: dysregulated neutrophil apoptosis and impaired clearance of apoptotic neutrophils expose the MPO and PR3 autoantigens that drive ANCA production."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Neutrophil priming: TLR-MyD88-NF-κB innate signalling (TLR4 and NF-κB already mapped) primes neutrophils, lowering the threshold for ANCA-induced respiratory burst and degranulation that injures the vessel wall."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Cytokine amplification: IL-6 and IFN-γ signalling through JAK-STAT (both already mapped) sustains the inflammatory milieu and T-cell responses of ANCA-associated vasculitis."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 maintenance: IL-23 sustains the pathogenic Th17 cells (IL-17A already mapped) implicated in the granulomatous inflammation of ANCA-associated vasculitis."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ANCA binding to primed neutrophils triggers ERK-MAPK signalling that drives the respiratory burst, degranulation and NET formation injuring small vessels."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT signalling mediates neutrophil priming and the B-cell survival that sustain the autoantibody response of ANCA vasculitis."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 amplifies the NET-driven thromboinflammation and endothelial injury of ANCA-associated vasculitis."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "DNA within the neutrophil extracellular traps central to ANCA-associated vasculitis engages cGAS-STING, amplifying the autoimmune inflammation."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling transduces the inflammatory cytokine milieu and Th17 response driving ANCA-associated vasculitis."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the interferon-driven component of the immune response in ANCA-associated vasculitis."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO regulates the neutrophil and lymphocyte survival and oxidative-stress balance relevant to the autoreactivity and NET formation of ANCA-associated vasculitis."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α in the inflamed, hypoxic vessel wall shapes the granulomatous and necrotizing inflammation of ANCA-associated vasculitis."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated cytotoxic T- and NK-cell activity contributes to the endothelial and tissue injury of ANCA-associated vasculitis."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the neutrophil activation and inflammatory signaling that drive the necrotizing vasculitis of ANCA-associated vasculitis."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) participates in the ANCA-triggered neutrophil respiratory burst and degranulation of ANCA-associated vasculitis."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of Fcγ-receptor engagement by ANCA drives the neutrophil activation central to ANCA-associated vasculitis."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked immunometabolic signaling shapes the neutrophil and autoreactive-lymphocyte metabolism of ANCA-associated vasculitis."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy participates in the neutrophil NETosis and autoreactive-immune-cell responses of ANCA-associated vasculitis."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment contributes to the vascular and glomerular inflammation of ANCA-associated vasculitis."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the autoreactive immune response and PR3/MPO gene expression of ANCA-associated vasculitis."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the neutrophil and leukocyte trafficking of ANCA-associated vasculitis."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the immune dysregulation and eosinophilic (EGPA) responses of ANCA-associated vasculitis."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the autoreactive immune responses (and PR3/MPO gene regulation) of ANCA-associated vasculitis."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the T-cell activation of ANCA-associated vasculitis."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Type I interferon signaling participates in the immune dysregulation of ANCA-associated vasculitis."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "EGPA allergic axis: eosinophilic granulomatosis with polyangiitis, the asthma-associated subtype (asthma already mapped), features elevated IgE and an allergic, eosinophil-driven inflammation distinct from the PR3/MPO autoimmunity of the other AAV subtypes."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Th2 eosinophilia: IL-4 and the type-2 response (IL-5 already mapped) drive the eosinophil expansion and tissue infiltration of eosinophilic granulomatosis with polyangiitis, targeted by anti-IL-5 and emerging anti-IL-4/13 therapy."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Endothelial injury: impaired endothelial nitric-oxide function accompanies the small-vessel inflammation of ANCA-associated vasculitis, contributing to the vascular damage that underlies its ischaemic organ manifestations."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Alveolar-haemorrhage anaemia: diffuse alveolar haemorrhage in the lung (already mapped) and the anaemia of chronic inflammation lower haemoglobin in ANCA-associated vasculitis, a fall in haemoglobin that can signal active pulmonary bleeding."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Th2 axis in EGPA: IL-13 with IL-4 and IL-5 (already mapped) drives the type-2 eosinophilic inflammation of eosinophilic granulomatosis with polyangiitis, the subset increasingly treated with anti-type-2 biologics."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative burst injury: ANCA-activated neutrophils (already mapped) release reactive oxygen species, including from xanthine oxidase, that damage the small-vessel endothelium, part of the oxidative injury of the vasculitic lesion."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Regulatory balance: IL-10 from regulatory T and B cells restrains the autoreactive response, and deficient IL-10-mediated regulation contributes to the unchecked autoimmunity that produces the ANCA and the vasculitis."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Inflammatory eicosanoids: prostaglandins from the neutrophil (already mapped) and infiltrating cells amplify the inflammation of the vasculitic lesion (IL-6, TNF and IL-1 already mapped), part of the eicosanoid dimension of the small-vessel injury."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Eosinophilic type-2 inflammation: mast cells, with eosinophils and the type-2 cytokines (IL-5, IL-4 and IL-13 already mapped), drive the allergic inflammation of eosinophilic granulomatosis with polyangiitis (EGPA), the type-2 subset of ANCA vasculitis."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Anaemia of inflammation: the chronic IL-6 (already mapped) inflammation of active ANCA vasculitis raises hepcidin, sequestering iron to produce the anaemia of chronic disease (haemoglobin already mapped) seen in active disease."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Vascular injury and repair: VEGF drives the endothelial injury and the angiogenesis of the granulomatous and healing vasculitic lesions, part of the vascular biology of the small-vessel injury in ANCA vasculitis."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Endothelial activation: the angiopoietin-Tie2 axis reflects the endothelial activation of the small-vessel injury of ANCA vasculitis (VEGF already mapped), part of the endotheliopathy of the vasculitic lesion."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Checkpoint-triggered vasculitis: the PD-1 checkpoint whose blockade by cancer immunotherapy can trigger an ANCA-associated vasculitis, and whose peripheral-tolerance mechanisms are disturbed in the autoimmunity of the disease."
  - target: 01-human/03-molecular/ctla-4
    relation: connects-to
    note: "Co-inhibitory checkpoint: CTLA-4, with PD-1 (already mapped), regulates the autoreactive T cells that help the B cells (CD20 and BAFF already mapped) produce the ANCA (immunoglobulin already mapped), and its blockade can precipitate vasculitis."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Regulatory T-cell tolerance: IL-2 signalling in the regulatory T cells maintains the tolerance whose failure permits the autoreactive response of ANCA vasculitis, and low-dose IL-2 is studied to restore it."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Immune-metabolic adipokine: leptin is the adipokine of the immune-metabolic milieu and the steroid (cortisol already mapped)-related metabolic disturbance of ANCA vasculitis."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the immune-metabolic milieu of ANCA vasculitis."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the systemic inflammation (IL-6 already mapped) of ANCA vasculitis."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Innate cytotoxicity: the NK cells (perforin already mapped) are part of the innate immune dysregulation of the small-vessel autoimmunity of ANCA vasculitis."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Cytotoxic effectors: the cytotoxic T cells (perforin already mapped) contribute to the endothelial and tissue injury of the ANCA vasculitis, alongside the ANCA-activated neutrophils (already mapped)."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm, which with the Th17 (IL-17 and IL-23 already mapped) drives the granulomatous inflammation of ANCA vasculitis."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Type-2 alarmin: TSLP, with IL-33 (already mapped), is the epithelial alarmin driving the eosinophilic type-2 (IL-4, IL-5 and IL-13 already mapped) inflammation of the EGPA subtype of ANCA vasculitis."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Eosinophil biomarker: periostin, downstream of the type-2 (IL-13 already mapped) cytokines, marks the eosinophilic tissue inflammation of the EGPA subtype of ANCA vasculitis."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell/eosinophil effector: the histamine of the mast cells (already mapped) and eosinophils contributes to the type-2 vascular and tissue inflammation of the EGPA subtype of ANCA vasculitis."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement/contact regulation: the C1-esterase inhibitor regulates the classical complement and the contact pathways, complementing the factor H (already mapped) control of the alternative pathway (C5aR1 already mapped, the avacopan target) of ANCA vasculitis."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Antioxidant micronutrient: selenium, a selenoprotein cofactor, is part of the oxidative-stress and micronutrient dimension of the autoimmune vascular inflammation of ANCA vasculitis."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Nutritional immunity: transferrin, the iron carrier, reflects the disordered iron handling of the anaemia of the chronic inflammation of ANCA vasculitis."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Vascular matricellular: osteopontin, released by the activated neutrophils (already mapped) and myeloid cells, is a matricellular mediator amplifying the vascular inflammation of ANCA vasculitis."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Crescent/granuloma fibrosis: the fibroblasts drive the fibrotic remodelling of the pauci-immune crescentic glomerulonephritis and the granulomatous inflammation of ANCA vasculitis."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Vessel-wall matrix: collagen, the vascular extracellular-matrix scaffold, is degraded and remodelled during the necrotising vascular injury and the fibrosis of ANCA vasculitis."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-vasculitis axis: bradykinin, via B1/B2 receptors on vascular endothelium (already mapped) and neutrophils (already mapped), amplifies the vascular permeability and the necrotising inflammation of ANCA vasculitis."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Anaemia of inflammation: erythropoietin response is blunted by the chronic inflammation (IL-6, TNF already mapped) of ANCA vasculitis, contributing to the normocytic anaemia of the active disease."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian immunomodulation: melatonin, via its anti-inflammatory and antioxidant effects, modulates the neutrophil (already mapped) activation and the oxidative injury of the systemic autoimmune inflammation of ANCA vasculitis."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Sex-hormone vasculitis: testosterone exerts anti-inflammatory effects on neutrophil (already mapped) and T-cell (already mapped) autoimmunity; the male sex predisposition to GPA and the female-to-MPA ratio implicate androgen-mediated immune modulation in ANCA vasculitis."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Platelet-serotonin vascular injury: serotonin, released by platelets (already mapped) upon the endothelial (already mapped) injury of necrotising vasculitis, amplifies the vasoconstriction and the thrombotic occlusion of the ANCA-damaged vessel wall."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Immune neuroendocrine: prolactin modulates T-cell (already mapped) and B-cell (already mapped) autoimmune activation; its elevation in active systemic autoimmune disease contributes to the sex-immune-neuroendocrine dimension of ANCA vasculitis."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "ANCA oxytocin: oxytocin, via OXTR on neutrophils (already mapped) and regulatory T cells (already mapped), attenuates autoimmune vascular inflammation; oxytocin deficiency amplifies the IL-6 (already mapped) and NLRP3 (already mapped) vasculitic cascade of ANCA vasculitis."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "ANCA vasopressin: vasopressin, via V1aR on endothelial cells (already mapped) and smooth-muscle cells (already mapped), modulates vascular tone; vasopressin dysregulation amplifies the nitric-oxide (already mapped) and complement C3 (already mapped) cascade of ANCA vasculitis."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "ANCA iodine: iodine-dependent thyroid hormones modulate neutrophil (already mapped) and T-cell (already mapped) autoimmune activation; iodine deficiency impairs the cortisol (already mapped) and IL-6 (already mapped) regulatory axis of the autoimmune cascade of ANCA vasculitis."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "ANCA sodium: high dietary sodium promotes Th17 (T-helper cell already mapped) polarisation and neutrophil (already mapped) activation; sodium-induced IL-17 (already mapped) and NF-κB (already mapped) dysregulation amplifies the autoimmune vascular inflammation of ANCA vasculitis."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "ANCA magnesium: magnesium, as cofactor of immune enzymes in T-helper cells (already mapped) and neutrophils (already mapped), restrains NLRP3 (already mapped) and NF-κB (already mapped); magnesium deficiency amplifies the autoimmune vascular inflammation of ANCA vasculitis."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "ANCA copper: copper, as SOD cofactor, scavenges ROS in endothelial cells (already mapped) and neutrophils (already mapped) driving vascular injury; copper deficiency amplifies the NLRP3 (already mapped) and NF-κB (already mapped) complement-driven inflammation of ANCA vasculitis."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "ANCA potassium: potassium efflux from neutrophils (already mapped) and macrophages (already mapped) activates NLRP3 (already mapped); potassium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and complement-C3 (already mapped) vasculitic cascade in ANCA."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "ANCA calcium: calcium activates neutrophil (already mapped) degranulation and endothelial-cell (already mapped) injury; calcium dysregulation amplifies NLRP3 (already mapped) and NF-κB (already mapped) and complement-C5 (already mapped) and IL-6 (already mapped) cascade in ANCA."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "ANCA zinc: zinc cofactors macrophage (already mapped) anti-inflammatory function and neutrophil (already mapped) regulation; zinc deficiency amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) and complement-C3 (already mapped) cascade in ANCA."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "phosphorus-driven ATP in neutrophils (already mapped) and macrophages (already mapped) sustains vasculitic immune activation; phosphorus deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and complement-C3 (already mapped) vasculitic cascade in ANCA."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "nitric oxide from iNOS in neutrophils (already mapped) and macrophages (already mapped) modulates endothelial-cell (already mapped) vasodilation; nitrogen excess amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) vasculitic cascade in ANCA."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "chloride channels on neutrophils (already mapped) and endothelial cells (already mapped) regulate intracellular pH; chloride dysregulation amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) vasculitic cascade in ANCA."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "ANCA carbon: carbon backbone of cytokines in neutrophils (already mapped) and macrophages (already mapped) drives vasculitic inflammation; carbon dysregulation amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) vasculitic cascade in ANCA."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "ANCA hydrogen: hydrogen, via redox homeostasis in neutrophils (already mapped) and endothelial cells (already mapped), quenches vasculitic ROS; hydrogen dysregulation amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade in ANCA."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "ANCA sulfur: H2S from sulfur-amino acids in neutrophils (already mapped) and endothelial cells (already mapped) modulates vascular tone; sulfur deficiency amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) vasculitic cascade in ANCA."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "ANCA GLP-1: GLP-1 receptor signalling in macrophages (already mapped) and endothelial cells (already mapped) modulates vascular homeostasis; GLP-1 dysregulation amplifies NF-κB (already mapped) and NLRP3 (already mapped) and IL-6 (already mapped) cascade of ANCA vasculitis."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "ANCA angiotensin-II: angiotensin-II in endothelial cells (already mapped) and macrophages (already mapped) promotes vascular inflammation; angiotensin-II excess amplifies NF-κB (already mapped) and NLRP3 (already mapped) and IL-6 (already mapped) vasculitic cascade of ANCA."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "ANCA WNT/β-catenin: WNT/β-catenin in endothelial cells (already mapped) and macrophages (already mapped) supports vascular repair; WNT dysregulation amplifies NF-κB (already mapped) and NLRP3 (already mapped) and IL-6 (already mapped) vasculitic cascade of ANCA vasculitis."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "ANCA RANKL: RANKL in macrophages (already mapped) and vascular endothelium (already mapped) modulates the vascular bone-immune axis; RANKL excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) vasculitic cascade of ANCA vasculitis."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "ANCA SMAD4: SMAD4 in vascular endothelium (already mapped) and macrophages (already mapped) modulates vascular remodelling; SMAD4 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) vasculitic cascade of ANCA vasculitis."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "ANCA fibronectin: fibronectin in vessel walls (already mapped) and macrophages (already mapped) modulates vascular matrix integrity; fibronectin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of ANCA vasculitis."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "ANCA notch: NOTCH on endothelial cells (already mapped) and macrophages (already mapped) regulates vascular repair; NOTCH dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of ANCA vasculitis."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "ANCA igf-1: IGF-1 from endothelial cells (already mapped) and macrophages (already mapped) promotes vascular repair; IGF-1 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of ANCA vasculitis."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "ANCA activin-a: activin-A from macrophages (already mapped) and endothelial cells (already mapped) regulates vascular immune-fibrotic balance; activin-a excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of ANCA vasculitis."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "ANCA cgrp: CGRP from macrophages (already mapped) and endothelial cells (already mapped) modulates ANCA vascular tone; cgrp dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of ANCA vasculitis."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "ANCA calcitonin: calcitonin from macrophages (already mapped) and endothelial cells (already mapped) modulates ANCA calcium balance; calcitonin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of ANCA vasculitis."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "ANCA substance-p: substance P from macrophages (already mapped) and endothelial cells (already mapped) modulates ANCA neuroimmune tone; substance-p excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of ANCA vasculitis."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "ANCA insulin-receptor: insulin receptor on macrophages (already mapped) and endothelial cells (already mapped) drives vascular tone; insulin-receptor dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of ANCA vasculitis."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "ANCA aldosterone: aldosterone from macrophages (already mapped) and endothelial cells (already mapped) modulates vascular ion balance; aldosterone excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of ANCA vasculitis."
  - target: 01-human/03-molecular/androgen-receptor
    relation: connects-to
    note: "ANCA androgen-receptor: androgen receptor on macrophages (already mapped) and endothelial cells (already mapped) modulates hormonal tone; androgen-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of ANCA vasculitis."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "ANCA norepinephrine: norepinephrine from macrophages (already mapped) and endothelial cells (already mapped) modulates vascular adrenergic tone; norepinephrine excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of ANCA vasculitis."
  - target: 01-human/03-molecular/adrenomedullin
    relation: connects-to
    note: "ANCA adrenomedullin: adrenomedullin from macrophages (already mapped) and endothelial cells (already mapped) modulates vessel tone; adrenomedullin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of ANCA vasculitis."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "ANCA bdnf: BDNF from macrophages (already mapped) and endothelial cells (already mapped) modulates vascular neuroimmune repair; BDNF deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of ANCA vasculitis."
---

# ANCA Vasculitis

## Overview

**ANCA-associated vasculitis (AAV)** is a group of systemic autoimmune small-vessel vasculitides characterized by **anti-neutrophil cytoplasmic antibody (ANCA)** production and **pauci-immune necrotizing vasculitis** — vascular inflammation without immune complex deposition, distinguishing it from lupus nephritis or IgA nephropathy [^yates-2022-anca-review]. AAV encompasses three clinically distinct entities unified by ANCA serology and shared pathomechanism:

| Entity | Former name | ANCA specificity | Primary targets | Key features |
|:-------|:-----------|:----------------|:----------------|:------------|
| **GPA** | Wegener's | Anti-PR3 (cANCA, ~80%) | Upper/lower airways, kidneys | Granulomatous ENT disease, saddle nose, cavitating lung nodules |
| **MPA** | — | Anti-MPO (pANCA, ~60%) | Kidneys, lungs | Rapidly progressive GN; diffuse alveolar hemorrhage |
| **EGPA** | Churg-Strauss | Anti-MPO (pANCA, ~40%) | Lungs, heart, PNS, skin | Eosinophilia (>10%); asthma; cardiac involvement |

**Epidemiology:**
- Combined AAV prevalence: ~150–200/million; incidence ~20/million/year
- GPA most common in northern Europe; MPA more prevalent in Asia
- Age of onset: 50–70 years; slight male predominance
- 5-year survival before modern immunosuppression: <30%; with current treatment: ~80%

**ANCA biology:**
- **cANCA (cytoplasmic pattern):** Anti-PR3 (proteinase 3; encoded by *PRTN3*, chromosome 19p13.3); granular cytoplasmic staining by IIF; associated with GPA
- **pANCA (perinuclear pattern):** Anti-MPO (myeloperoxidase; encoded by *MPO*, chromosome 17q21-q23); perinuclear IIF pattern; associated with MPA and EGPA
- ANCA are IgG autoantibodies (predominantly IgG3) that bind neutrophil granule proteins translocated to the cell surface after cytokine priming

## Structure

### Disease phenotypes

**Granulomatosis with Polyangiitis (GPA):**
- **ENT involvement (>90%):** Chronic sinusitis, epistaxis, nasal septal perforation, saddle-nose deformity (cartilage destruction), subglottic stenosis (tracheal narrowing — life-threatening), otitis media/sensorineural hearing loss
- **Lung:** Pulmonary nodules (often cavitary; may be misdiagnosed as malignancy or infection), diffuse alveolar hemorrhage, pleuritis
- **Kidney:** Pauci-immune crescentic glomerulonephritis (rapidly progressive GN; proteinuria, hematuria, rising creatinine; no immune deposits on IF — pauci-immune)
- **Eye:** Scleritis, orbital pseudotumor (proptosis), episcleritis, retinal vasculitis
- **Skin:** Palpable purpura, ulcers (leukocytoclastic vasculitis)

**Microscopic Polyangiitis (MPA):**
- No granulomas; no upper airway disease
- Rapidly progressive GN (most common cause of dialysis in AAV)
- Pulmonary capillaritis → diffuse alveolar hemorrhage (hemoptysis, hypoxemia)
- Mononeuritis multiplex (vasculitic neuropathy)

**EGPA:**
- **Phase 1 (prodromal):** Allergic rhinitis, asthma (often severe, adult-onset)
- **Phase 2 (eosinophilic):** Peripheral eosinophilia (>10%, >1.5×10⁹/L), eosinophilic pneumonia, eosinophilic gastroenteritis
- **Phase 3 (vasculitic):** Mononeuritis multiplex, purpura, cardiac (eosinophilic myocarditis — major cause of mortality, ~50% of AAV deaths in EGPA)

### ANCA testing

**Indirect immunofluorescence (IIF):**
- cANCA: cytoplasmic granular pattern → send anti-PR3 ELISA
- pANCA: perinuclear pattern → send anti-MPO ELISA

**ELISA:** Anti-PR3 and anti-MPO; quantitative; correlates with disease activity; rising titer predicts relapse (but not reliably in all patients)

**Birmingham Vasculitis Activity Score (BVAS):** Validated composite disease activity score; guides treatment decisions

## Function

ANCA vasculitis causes injury through three parallel mechanisms:

1. **Neutrophil-mediated vascular necrosis** — ANCA IgG binds surface PR3/MPO on C5a-primed neutrophils → Fc receptor (FcγRIIa) crosslinking → exuberant respiratory burst + NETosis → endothelial damage → fibrinoid necrosis, thrombosis

2. **Granuloma formation (GPA)** — PR3 on macrophages activates CD4+ Th1 cells → IFN-γ → macrophage activation → granuloma assembly (epithelioid macrophages, giant cells, lymphocytes); granulomas destroy cartilage, bone, and tissue at ENT, orbital, and pulmonary sites

3. **Crescentic glomerulonephritis** — Glomerular capillary necrosis → fibrin + proliferating parietal epithelial cells form crescents; loss of glomerular filtration units → rapid GFR decline; without treatment → ESRD within weeks to months

## Pathology

### Two-hit pathomechanism (C5a + ANCA)

The prevailing model requires **two sequential stimuli**:

**Hit 1 — Complement-mediated neutrophil priming:**
- Low-level complement activation (from infection, DAMPs, or alternative pathway background) → C5a
- C5a binds **C5aR1** on neutrophils → Gαi → PI3K/ERK/p38 → cytoskeletal reorganization, surface PR3/MPO upregulation, adhesion molecule expression, primed respiratory burst

**Hit 2 — ANCA-mediated full activation:**
- ANCA IgG binds surface PR3 or MPO → FcγRIIa crosslinking + concomitant C5aR1 → synergistic activation → massive NETosis + respiratory burst
- NETs provide a template: citrullinated histones + PR3/MPO on NETs → amplify ANCA production (autoantigen spread) + activate endothelium (thrombosis)

**Complement evidence in human disease:**
- C3a and C5a elevated in urine and serum during active AAV
- Complement deposition identified in renal biopsies despite "pauci-immune" pattern (immunocomplex deposition absent, but terminal complement detectable)
- Avacopan (C5aR1 blocker) achieves remission comparable to prednisone — proving C5a/C5aR1 is the key inflammatory signal driving AAV [^jayne-2021-avacopan-advocate]

### EGPA — IL-5/IL-4 and eosinophil axis

EGPA is mechanistically distinct — eosinophils, not neutrophils, mediate tissue damage:
- IL-5 drives eosinophilopoiesis and survival; **mepolizumab** (anti-IL-5; MIRRA trial: relapse-free survival; FDA Sep 2017) is approved for EGPA
- Th2 cytokines (IL-4, IL-13) drive IgE production, airway remodeling, and eosinophil trafficking
- ANCA (anti-MPO) present in ~40% of EGPA (vasculitic phase) but absent in eosinophilic phase
- **Benralizumab** (anti-IL-5Rα): Phase 3 MANDARA trial (vs. mepolizumab) — showed similar efficacy; potential for deeper eosinophil depletion

## Treatment

### Remission induction

**Rituximab + glucocorticoids (preferred for severe GPA/MPA):**
- **RAVE trial** [^stone-2010-rituximab-gpa-rave]: Rituximab 375 mg/m² × 4 doses + glucocorticoids vs. cyclophosphamide + glucocorticoids; **64% complete remission (rituximab) vs. 53% (CYC)** at 6 months; non-inferior overall; superior in relapsing disease
- FDA approved rituximab for GPA and MPA: **April 2011**
- Mechanism: depletes PR3-specific and MPO-specific B cell clones + B cell precursors → reduces ANCA production; does NOT deplete plasma cells (ANCA titers fall slowly over months)

**Cyclophosphamide + glucocorticoids (alternative):**
- IV pulse CYC (15 mg/kg q3w × 3–6 pulses) preferred over oral CYC to reduce bladder toxicity
- Oral CYC 2 mg/kg/d for severe/refractory; cystitis, malignancy risk (mesna co-administration required for bladder protection)
- Largely replaced by rituximab in GPA; still used for severe MPA with renal involvement and for EGPA

**Avacopan + standard of care (glucocorticoid sparing):**
- **ADVOCATE trial** (N=331) [^jayne-2021-avacopan-advocate]: Avacopan (30 mg BID) vs. prednisone taper (60 mg/d tapered to 0 over 20 weeks) — both added to rituximab or CYC:
  - **Remission at week 26:** 72.3% (avacopan) vs. 70.1% (prednisone) — avacopan **non-inferior**
  - **Sustained remission at week 52:** **65.7% (avacopan) vs. 54.9% (prednisone)** — avacopan **superior** (p<0.05)
  - eGFR preservation at 52 weeks significantly better with avacopan
  - FDA approved for GPA and MPA: **October 2021**

**Plasma exchange (PLEX):** Previously used for rapidly progressive GN (serum creatinine >500 μmol/L or dialysis dependence); the PEXIVAS trial (2020) showed PLEX did NOT reduce ESRD or mortality → no longer routine standard of care

### Remission maintenance

**Rituximab maintenance (preferred):**
- Fixed schedule: 500 mg q6m × 2 years; or tailored to ANCA titer/B cell reconstitution
- **MAINRITSAN trial** showed rituximab superior to azathioprine for maintaining remission (5% vs 29% major relapse at 28 months)

**Azathioprine 2 mg/kg/d:** Alternative for patients who cannot receive rituximab; less effective than rituximab in PR3-ANCA patients

**Mycophenolate mofetil 3 g/d:** Second-line alternative

**EGPA-specific:** Mepolizumab (anti-IL-5; FDA Sep 2017) for relapsing/refractory EGPA; reduces oral glucocorticoid dependence

### Special considerations

- **Prophylaxis:** TMP-SMX for Pneumocystis jirovecii pneumonia during immunosuppression; osteoporosis prophylaxis during glucocorticoid therapy; bisphosphonate + calcium/vitamin D
- **Monitoring:** ANCA titers (imperfect; rising PR3-ANCA more predictive of relapse than rising MPO-ANCA); eGFR; urinalysis; BVAS
- **Relapse:** More common in GPA (50% at 5 years) than MPA; re-treat with rituximab preferred; escalate glucocorticoids acutely

## Connections

- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a primes neutrophils via C5aR1 → surface PR3/MPO translocation → ANCA IgG crosslinking → NETosis + ROS → endothelial injury; avacopan (C5aR1 antagonist; ADVOCATE: 65.7% vs 54.9% sustained remission; FDA Oct 2021) blocks neutrophil priming.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Complement activation generates C5a in AAV; C5a–C5aR1 primes neutrophils for ANCA-triggered NETosis; C5b-9 MAC contributes to endothelial injury; avacopan allows glucocorticoid sparing without inhibiting C5b-9-mediated pathogen defense.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — Rituximab (anti-CD20) is non-inferior to cyclophosphamide for AAV induction (RAVE trial: 64% vs 53% remission; FDA Apr 2011 for GPA/MPA) and is preferred for maintenance; rituximab depletes ANCA-producing B cells and reduces PR3/MPO autoantibody titers.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — ANCA are IgG autoantibodies (IgG3 > IgG1) against PR3 (cANCA; GPA) or MPO (pANCA; MPA/EGPA); ANCA IgG Fc engages FcγRIIa on neutrophils → full effector activation; ANCA titers correlate with disease activity and relapse risk.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — neutrophils are the primary effector cells in ANCA vasculitis; ANCA IgG crosslinks surface PR3/MPO on C5a-primed neutrophils → FcγRIIa → NETosis + respiratory burst → fibrinoid necrosis of small vessel walls and pauci-immune crescentic GN.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — crescentic pauci-immune GN in GPA/MPA causes rapidly progressive kidney failure; untreated AAV → ESRD within weeks-months; avacopan (ADVOCATE) preserves eGFR significantly better than prednisone at 52 weeks; ANCA GN is a leading cause of vasculitis-related dialysis.
- `connects-to` → **[CKD](../../07-system/ckd/README.md)** — AAV renal involvement progresses to CKD in up to 40% at 5 years; ESRD in 20-25% over 10 years; creatinine at diagnosis and percentage crescents on biopsy predict CKD trajectory; avacopan eGFR advantage at 52 weeks may translate to reduced long-term CKD progression.
- `connects-to` → **[Giant Cell Arteritis](../giant-cell-arteritis/README.md)** — ANCA vasculitis and giant cell arteritis sit at opposite ends of the vessel spectrum: AAV attacks small vessels with pauci-immune necrotizing inflammation, GCA the large arteries with granulomatous giant cells — contrasting poles classified by vessel caliber and histology.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — B cells are the source of ANCA: they become plasma cells secreting IgG against PR3 or MPO, which is why anti-CD20 rituximab (RAVE trial) — depleting B cells and lowering autoantibody titers — is non-inferior to cyclophosphamide for induction and preferred for maintenance.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — AAV is a pulmonary-renal syndrome: small-vessel inflammation in the alveolar capillaries causes diffuse alveolar hemorrhage (hemoptysis, hypoxemia) alongside crescentic glomerulonephritis, and GPA additionally produces necrotizing granulomas of the upper and lower airways.
- `connects-to` → **[Asthma](../asthma/README.md)** — Asthma defines one ANCA-vasculitis subtype: eosinophilic granulomatosis with polyangiitis (EGPA, Churg-Strauss) arises in patients with adult-onset asthma and eosinophilia who then develop vasculitis; only ~40% are ANCA-positive, and anti-IL-5 (mepolizumab) treats it.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — The skin is a common, accessible window on ANCA-vasculitis: small-vessel inflammation produces palpable purpura, livedo, nodules and ulcers, and a skin biopsy showing leukocytoclastic vasculitis helps confirm the diagnosis while sparing the patient an organ biopsy.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages build the granulomas of ANCA-vasculitis: in granulomatosis with polyangiitis, neutrophil activation and necrosis recruit macrophages that organize into the necrotizing granulomas of lung and sinuses, distinguishing GPA from non-granulomatous microscopic polyangiitis.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — ANCA vasculitis is not purely antibody-driven—T-helper cells orchestrate it: autoreactive Th1 and Th17 cells help B cells make ANCA and form GPA granulomas, so T-cell- and B-cell-directed therapies both work, and relapse tracks T-cell inflammation.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — Plasma cells make the pathogenic ANCA antibodies (anti-PR3, anti-MPO): these autoantibodies activate primed neutrophils to injure small vessels, and because long-lived plasma cells resist rituximab, persistent autoantibody helps explain relapse and refractory disease.
- `connects-to` → **[Hepatitis B](../hepatitis-b/README.md)** — ANCA vasculitis must be distinguished from hepatitis-B-associated vasculitis: HBV classically causes polyarteritis nodosa—an immune-complex, ANCA-negative medium-vessel vasculitis—so vasculitis workup checks viral serologies, since antivirals treat HBV disease.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Endothelial cells are the battlefield of ANCA vasculitis: ANCA-activated neutrophils adhere to and destroy vessel endothelium, causing necrotizing inflammation that infarcts glomeruli, lung capillaries and skin—so endothelial injury underlies the multi-organ damage.
- `connects-to` → **[Systemic Lupus Erythematosus](../systemic-lupus-erythematosus/README.md)** — ANCA vasculitis and lupus both attack the kidney but by opposite mechanisms: ANCA causes pauci-immune glomerulonephritis with little immune-complex deposition, while lupus nephritis is driven by immune-complex deposits—a key distinction on renal biopsy.
- `connects-to` → **[Immune System](../immune-system/README.md)** — ANCA vasculitis is a breakdown of immune tolerance: the immune system makes antibodies against its own neutrophil enzymes (PR3 or MPO), which turn neutrophils into agents of vascular destruction—so B-cell-depleting therapy that removes the autoantibody source works.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — ANCA vasculitis attacks the glomerulus ferociously: ANCA-activated neutrophils damage glomerular capillaries, producing the pauci-immune crescentic glomerulonephritis that causes rapidly progressive kidney failure—a medical emergency needing urgent immunosuppression.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — ANCA vasculitis often strikes peripheral nerves: inflammation of the small vessels feeding nerves causes ischemic mononeuritis multiplex—sudden foot- or wrist-drop—so a vasculitic neuropathy can be an early, diagnostic clue to systemic ANCA disease.
- `connects-to` → **[Respiratory system](../respiratory-system/README.md)** — ANCA vasculitis is a classic pulmonary-renal syndrome: it inflames the airways and alveolar capillaries, causing sinusitis, lung nodules and life-threatening alveolar hemorrhage alongside the kidney disease—so respiratory and renal involvement often present together.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — ANCA vasculitis often inflames the eye: granulomatosis with polyangiitis causes scleritis, episcleritis, and orbital masses that can threaten vision, so red, painful eyes can be an early clue—part of its classic ear-nose-eye-lung-kidney pattern.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — ANCA vasculitis damages peripheral nerves as mononeuritis multiplex: inflammation of the small vessels feeding nerves causes patchy, asymmetric foot- or wrist-drop, a hallmark vasculitic neuropathy that signals active, organ-threatening disease.
- `connects-to` → **[Interleukin-5](../../03-molecular/il-5/README.md)** — Eosinophilic GPA (Churg-Strauss), an ANCA-associated vasculitis, is IL-5-driven: this cytokine expands the eosinophils that infiltrate lungs, nerves, and heart, so the anti-IL-5 antibody mepolizumab is an approved targeted treatment for it.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — ANCA vasculitis runs on the alternative complement pathway: ANCA-activated neutrophils generate C3 and C5a that recruit and prime more neutrophils in a self-amplifying loop—so complement blockade (avacopan) spares steroids.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — ANCA vasculitis scars what it inflames: crescentic glomerulonephritis fibroses into kidney failure, and MPO-ANCA disease can cause progressive pulmonary fibrosis—so early immunosuppression aims to halt inflammation before irreversible fibrosis sets in.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — ANCA vasculitis reflects failed regulatory T-cell control: defective Tregs let autoreactive B and T cells drive anti-MPO/PR3 autoimmunity, so restoring immune tolerance is a goal beyond the B-cell depletion that current therapy relies on.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — ANCA vasculitis can strike the heart, especially in EGPA: eosinophilic myocarditis and coronary inflammation damage the muscle, making cardiac involvement the leading cause of death in the eosinophilic form of the disease.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Primed neutrophils drive ANCA vasculitis partly via the NLRP3 inflammasome: it amplifies inflammatory signaling and NET release when ANCA antibodies activate the cells, fueling the vessel-wall damage at the disease's core.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells help break tolerance in ANCA vasculitis: by presenting MPO and PR3 fragments to T cells, they license the autoimmune response that drives B cells to make the ANCA antibodies, a step upstream of current B-cell therapy.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — ANCA vasculitis can starve the lungs of oxygen: inflamed alveolar capillaries bleed into the air sacs (diffuse alveolar hemorrhage), so gas exchange fails—a pulmonary-renal emergency that can need a ventilator.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — ANCA vasculitis can strangle the gut: inflammation of the bowel's small vessels causes mesenteric ischemia, abdominal pain, and GI bleeding, a serious extrarenal manifestation of severe disease.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — ANCA vasculitis can reach the brain: inflammation of cerebral vessels and the dura causes strokes, seizures, and pachymeningitis, extending the small-vessel attack into the central nervous system.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Imaging maps ANCA vasculitis: chest CT photons reveal the lung nodules, cavities and alveolar hemorrhage of granulomatosis, and sinus scans show the destructive upper-airway disease.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — ANCA vasculitis can flood the alveoli: capillaritis in the lung's gas-exchange units causes diffuse alveolar hemorrhage, a life-threatening bleed that fills the air sacs and drops the blood count.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Alveolar hemorrhage in ANCA vasculitis leaves an iron trail: blood in the air sacs is engulfed by iron-laden macrophages, and the falling hemoglobin marks the severity of the lung bleeding.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows what ANCA vasculitis lacks: its inflamed vessels are 'pauci-immune,' nearly free of the immune-complex deposits that fill other vasculitides, because ANCA-activated neutrophils attack the wall directly with their toxic granules and NETs.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — The vasculitis can ulcerate the gut: inflammation of the mesenteric and gastric vessels causes abdominal pain, bleeding, and even bowel perforation, a dangerous abdominal manifestation of systemic disease.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — ANCA vasculitis can infarct the spleen: inflamed, clotting small arteries cut off blood to wedges of splenic tissue, one of the silent organ infarctions that mark widespread vascular involvement.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — The disease is named for its antibody: ANCA against proteinase-3 (c-ANCA) or myeloperoxidase (p-ANCA) both diagnose it and activate neutrophils to attack vessels, and the anti-CD20 antibody rituximab is a frontline treatment.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Inflamed vessels starve the nerves: occlusion of the small arteries feeding peripheral nerves produces mononeuritis multiplex — patchy, painful weakness and numbness that is a classic presenting feature, especially in EGPA.
- `connects-to` → **[Bladder Cancer](../bladder-cancer/README.md)** — The old workhorse drug scars the bladder: cyclophosphamide, long used to induce remission, releases acrolein that inflames the bladder into hemorrhagic cystitis and, over years, raises the risk of bladder cancer — so mesna and dose limits guard against it.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Glucocorticoids anchor induction: high-dose steroids rapidly quench the vasculitis alongside rituximab or cyclophosphamide, but their infection, bone, and metabolic toll drives the modern push to taper them fast.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Active vasculitis is sharply prothrombotic: ANCA disease carries a markedly raised risk of deep-vein thrombosis and pulmonary embolism during flares, the inflamed endothelium tipping the blood toward clotting.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — The inflammation eats the vessel wall: neutrophil-driven necrotizing inflammation destroys the smooth-muscle media of small arteries, weakening them into the microaneurysms and ruptures that bleed into lung and kidney.
- `connects-to` → **[Podocyte](../../04-cellular/podocyte/README.md)** — The kidney's filter is wrecked from above: pauci-immune necrotizing glomerulonephritis ruptures the capillary tuft and forms crescents that crush the podocytes, producing the hematuria and rapidly rising creatinine that make renal ANCA disease an emergency.
- `connects-to` → **[BAFF](../../03-molecular/baff/README.md)** — BAFF keeps the ANCA factories alive: the cytokine sustains the autoreactive B cells that make anti-MPO and anti-PR3 antibodies, the rationale behind rituximab and the B-cell-targeted control of the disease.
- `connects-to` → **[Inflammatory Bowel Disease](../inflammatory-bowel-disease/README.md)** — ANCA blurs into bowel disease: an atypical perinuclear ANCA is a hallmark antibody of ulcerative colitis, one of the overlaps where the same autoantibody family marks both vasculitis and inflammatory bowel disease.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — A Th17 arm drives the autoimmunity: IL-17A from autoreactive helper T cells promotes neutrophil recruitment and the granulomatous inflammation of GPA, running higher in active ANCA vasculitis.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Autoantibodies are schooled in lymphoid tissue: ectopic germinal centers, including those in inflamed nasal mucosa in GPA, generate the B cells that make anti-PR3 and anti-MPO — which is why germinal-center-directed B-cell depletion works.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — The heart is a hidden target: ANCA vasculitis—especially eosinophilic GPA—can inflame the myocardium and coronary vessels, and the resulting cardiomyopathy is a leading cause of death, so cardiac screening matters even when symptoms are quiet.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — ANCA-primed neutrophils run on NF-κB: cytokine priming activates NF-κB in neutrophils, which then degranulate when ANCA binds their surface PR3 and MPO, driving the explosive small-vessel inflammation of the disease.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Treatment trades vasculitis for infection: the cyclophosphamide, rituximab and high-dose steroids that induce remission leave patients severely immunosuppressed, so infection and sepsis are a leading cause of death — and a mimic of relapse.
- `connects-to` → **[Stroke](../stroke/README.md)** — It can inflame the brain's vessels: ANCA vasculitis occasionally involves the cerebral circulation, causing ischemic or hemorrhagic stroke as part of its central nervous system disease.
- `connects-to` → **[Pneumocystis jirovecii](../../../02-pathogen/03-fungi/pneumocystis-jirovecii/README.md)** — Its induction therapy opens the lung: the cyclophosphamide, rituximab and high-dose steroids used to control ANCA vasculitis deplete T-cell defenses, so Pneumocystis prophylaxis is standard during remission induction.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Inflammation and renal disease blunt the marrow: the systemic inflammation of active ANCA vasculitis raises hepcidin while its glomerulonephritis cuts erythropoietin, together producing an anemia of chronic disease.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A relapsing multisystem disease weighs on mood: the chronic, unpredictable course, organ damage and toxic immunosuppression of ANCA vasculitis carry a substantial burden of depression.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Its heavy immunosuppression opens the lung to mold: cyclophosphamide, rituximab and high-dose steroids used to induce remission in ANCA vasculitis deeply blunt immunity, permitting invasive aspergillosis.
- `connects-to` → **[Pulmonary Arterial Hypertension](../pulmonary-arterial-hypertension/README.md)** — Lung capillaritis and fibrosis can pressurize the arteries: the alveolar hemorrhage and interstitial scarring of ANCA vasculitis damage the pulmonary vasculature, contributing to pulmonary hypertension.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Prolonged steroids erode the skeleton: the months of high-dose corticosteroids needed to control ANCA vasculitis accelerate bone loss and raise fracture risk, a common treatment complication.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Small-vessel inflammation erupts on the skin: ANCA vasculitis causes palpable purpura, cutaneous nodules and ulcers, and granulomatosis with polyangiitis classically destroys the nasal cartilage into a saddle-nose.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It can inflame the gut's vessels: mesenteric vasculitis in ANCA disease causes abdominal pain, bowel ischaemia and GI bleeding, a serious extra-renal manifestation.
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — Its heavy immunosuppression reawakens shingles: the cyclophosphamide, rituximab and steroids used to induce remission in ANCA vasculitis deplete immunity, allowing herpes-zoster reactivation.
- `connects-to` → **[Renal System](../renal-system/README.md)** — The kidney is its classic target: ANCA vasculitis causes pauci-immune crescentic rapidly progressive glomerulonephritis, a renal emergency demanding prompt immunosuppression to prevent permanent failure.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Eosinophilic GPA strikes the heart: myocarditis and cardiomyopathy are a leading cause of death in EGPA, and coronary arteritis can occur, so cardiac assessment is essential.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Granulomatous disease can hit the pituitary: GPA occasionally involves the pituitary gland, causing hypophysitis and diabetes insipidus among its protean manifestations.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It aches in joints and muscles: migratory arthralgia, frank arthritis and myalgia are common features of ANCA-associated vasculitis, especially at disease onset.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Its cyclophosphamide threatens fertility: the alkylating agent long used to induce remission causes ovarian failure and impaired spermatogenesis, prompting fertility preservation before treatment.
- `connects-to` → **[Corticosteroids](../../../03-medicine/01-modern/02-respiratory/corticosteroids/README.md)** — Remission starts with steroids: high-dose glucocorticoids, with rituximab or cyclophosphamide, induce remission in ANCA-associated vasculitis, though their toxicity drives steroid-sparing strategies.
- `connects-to` → **[Staphylococcus aureus](../../../02-pathogen/02-bacteria/staphylococcus-aureus/README.md)** — A trigger living in the nose: chronic nasal carriage of Staphylococcus aureus is linked to relapse of granulomatosis with polyangiitis, and decolonisation can reduce flares.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Autoimmunity can overlap: rheumatoid arthritis and ANCA vasculitis sometimes coexist, and rheumatoid vasculitis is a feared small-vessel complication of long-standing severe RA.
- `connects-to` → **[Mycobacterium tuberculosis](../../../02-pathogen/02-bacteria/mycobacterium-tuberculosis/README.md)** — A granulomatous mimic to exclude: the lung nodules and cavities of granulomatosis with polyangiitis resemble tuberculosis, which must be excluded before the heavy immunosuppression that would let TB run rampant.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Biologics reshaped its treatment: rituximab against CD20 induces and maintains remission, avacopan blocks the C5a receptor to spare steroids, and mepolizumab against IL-5 treats eosinophilic GPA — targeted therapies for ANCA vasculitis.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Cyclophosphamide induces, at a cost: cyclophosphamide remains a mainstay for organ-threatening ANCA vasculitis, but its bladder toxicity and later bladder-cancer risk push earlier use of rituximab where possible.
- `connects-to` → **[IgA Nephropathy](../iga-nephropathy/README.md)** — Two faces of glomerulonephritis: ANCA vasculitis causes a pauci-immune crescentic glomerulonephritis with scant deposits, whereas IgA nephropathy is an immune-complex disease with mesangial IgA — contrasting mechanisms of the same renal emergency.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — Small-vessel vasculitis: ANCA-activated neutrophils degranulate on the walls of small arteries, capillaries and venules, causing the fibrinoid necrosis and vessel destruction that define the disease.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — Gut vasculitis: mesenteric small-vessel involvement, especially in granulomatosis with polyangiitis and EGPA, causes bowel ischaemia, ulceration and, rarely, perforation.
- `connects-to` → **[Stimulant Use Disorder](../stimulant-use-disorder/README.md)** — Drug-induced ANCA vasculitis: levamisole, a common cocaine adulterant, triggers an ANCA-positive vasculitis with skin necrosis and neutropenia—a drug-induced mimic to recognise in stimulant users.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Eosinophilic heart disease: EGPA (Churg-Strauss) infiltrates the myocardium with eosinophils, causing a cardiomyopathy and myocarditis that are a leading cause of death in this ANCA-associated vasculitis.
- `connects-to` → **[Hepatitis C](../hepatitis-c/README.md)** — An infectious mimic: hepatitis C causes a cryoglobulinaemic small-vessel vasculitis that overlaps clinically with ANCA-associated disease, a key infection to exclude before immunosuppression.
- `connects-to` → **[DLBCL](../dlbcl/README.md)** — Rituximab and lymphoma: the anti-CD20 antibody rituximab is now first-line for ANCA-associated vasculitis—the same drug treating B-cell lymphomas like DLBCL—while chronic immunosuppression slightly raises lymphoma risk.
- `connects-to` → **[Systemic Sclerosis](../systemic-sclerosis/README.md)** — Scleroderma overlap: a subset of systemic sclerosis patients are MPO-ANCA positive and develop an overlapping ANCA vasculitis with glomerulonephritis, distinct from scleroderma renal crisis.
- `connects-to` → **[Sjögren's Syndrome](../sjogrens-syndrome/README.md)** — Autoimmune co-occurrence: Sjögren's syndrome can coexist with ANCA-associated vasculitis, the two systemic autoimmune diseases sharing B-cell-driven mechanisms and overlapping organ involvement.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — IL-6-driven inflammation: interleukin-6 fuels the systemic inflammation, acute-phase response and B-cell help in ANCA vasculitis, making IL-6 blockade a candidate steroid-sparing therapy.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Neutrophil priming: TNF-α primes neutrophils to surface their ANCA antigens, the key first step that lets ANCA antibodies trigger the destructive neutrophil activation of the vasculitis.
- `connects-to` → **[IFN-γ](../../03-molecular/ifn-gamma/README.md)** — Granuloma formation: IFN-γ from Th1 cells drives the granulomatous inflammation characteristic of GPA, shaping the necrotising lesions of ANCA-associated vasculitis.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Inflammasome amplification: NLRP3-driven IL-1β release from activated neutrophils and monocytes adds to the inflammatory tissue injury of ANCA-associated vasculitis.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — NETosis driver: ANCA-activated neutrophils release extracellular traps rich in S100A8/A9 that expose PR3 and MPO autoantigens and directly injure vessel walls, a central mechanism of ANCA-associated vasculitis.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Monocyte recruitment: CCL2 draws monocytes into vasculitic lesions, where they become the macrophages of the granulomatous and necrotising inflammation of ANCA-associated vasculitis.
- `connects-to` → **[Fibrinogen](../../03-molecular/fibrinogen/README.md)** — Fibrinoid necrosis: vessel-wall injury in ANCA-associated vasculitis exposes tissue factor and converts fibrinogen to the fibrin of fibrinoid necrosis and the crescents of pauci-immune glomerulonephritis.
- `connects-to` → **[BTK](../../03-molecular/btk/README.md)** — BTK transduces B-cell-receptor and Fc-receptor signals in the autoreactive B cells and ANCA-activated neutrophils of the disease, making BTK inhibitors a candidate therapy complementing the established B-cell depletion of rituximab.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — TLR-mediated priming of neutrophils (as during infection) is required for ANCA to trigger the respiratory burst and NETosis, helping explain why infections precipitate flares of ANCA-associated vasculitis.
- `connects-to` → **[Thrombin](../../03-molecular/thrombin/README.md)** — Active ANCA-associated vasculitis markedly raises venous-thromboembolism risk, with NET- and tissue-factor-driven thrombin generation underlying the thrombotic tendency that accompanies disease flares.
- `connects-to` → **[Glucocorticoid receptor](../../03-molecular/glucocorticoid-receptor/README.md)** — High-dose glucocorticoids acting through the glucocorticoid receptor are the backbone of remission induction in ANCA vasculitis, rapidly suppressing the neutrophil-driven inflammation, with the C5aR antagonist avacopan now allowing steroid sparing.
- `connects-to` → **[FcRn](../../03-molecular/fcrn/README.md)** — Because ANCA are pathogenic IgG autoantibodies, plasma exchange and FcRn-blocking agents that accelerate IgG clearance are used to lower autoantibody levels in severe ANCA vasculitis with rapidly progressive kidney or lung disease.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Distinct HLA class II alleles predispose to anti-PR3 (HLA-DP) versus anti-MPO disease, favoring presentation of the neutrophil-autoantigen peptides to T cells that license ANCA production.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-β drives the fibrotic crescent formation and glomerulosclerosis that determine renal outcome in ANCA-associated glomerulonephritis.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — The alternative complement pathway, normally restrained by factor H, is primed by ANCA-activated neutrophils to generate the C5a (already mapped) that amplifies vasculitic injury.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Dysregulated neutrophil apoptosis and impaired clearance of apoptotic neutrophils expose the MPO and PR3 autoantigens that drive ANCA production.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR-MyD88-NF-κB innate signaling (TLR4 and NF-κB already mapped) primes neutrophils, lowering the threshold for ANCA-induced respiratory burst and degranulation that injures the vessel wall.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — IL-6 and IFN-γ signaling through JAK-STAT (both already mapped) sustains the inflammatory milieu and T-cell responses of ANCA-associated vasculitis.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — IL-23 sustains the pathogenic Th17 cells (IL-17A already mapped) implicated in the granulomatous inflammation of ANCA-associated vasculitis.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ANCA binding to primed neutrophils triggers ERK-MAPK signaling that drives the respiratory burst, degranulation and NET formation injuring small vessels.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT signaling mediates neutrophil priming and the B-cell survival that sustain the autoantibody response of ANCA vasculitis.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 amplifies the NET-driven thromboinflammation and endothelial injury of ANCA-associated vasculitis.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — DNA within the neutrophil extracellular traps central to ANCA-associated vasculitis engages cGAS-STING, amplifying the autoimmune inflammation.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling transduces the inflammatory cytokine milieu and Th17 response driving ANCA-associated vasculitis.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the interferon-driven component of the immune response in ANCA-associated vasculitis.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO regulates the neutrophil and lymphocyte survival and oxidative-stress balance relevant to the autoreactivity and NET formation of ANCA-associated vasculitis.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α in the inflamed, hypoxic vessel wall shapes the granulomatous and necrotizing inflammation of ANCA-associated vasculitis.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated cytotoxic T- and NK-cell activity contributes to the endothelial and tissue injury of ANCA-associated vasculitis.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the neutrophil activation and inflammatory signaling that drive the necrotizing vasculitis of ANCA-associated vasculitis.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) participates in the ANCA-triggered neutrophil respiratory burst and degranulation of ANCA-associated vasculitis.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of Fcγ-receptor engagement by ANCA drives the neutrophil activation central to ANCA-associated vasculitis.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked immunometabolic signaling shapes the neutrophil and autoreactive-lymphocyte metabolism of ANCA-associated vasculitis.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy participates in the neutrophil NETosis and autoreactive-immune-cell responses of ANCA-associated vasculitis.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte recruitment contributes to the vascular and glomerular inflammation of ANCA-associated vasculitis.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the autoreactive immune response and PR3/MPO gene expression of ANCA-associated vasculitis.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the neutrophil and leukocyte trafficking of ANCA-associated vasculitis.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the immune dysregulation and eosinophilic (EGPA) responses of ANCA-associated vasculitis.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the autoreactive immune responses (and PR3/MPO gene regulation) of ANCA-associated vasculitis.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the T-cell activation of ANCA-associated vasculitis.
- `connects-to` → **[Type I Interferon](../../03-molecular/type-i-interferon/README.md)** — Type I interferon signaling participates in the immune dysregulation of ANCA-associated vasculitis.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — EGPA allergic axis: eosinophilic granulomatosis with polyangiitis, the asthma-associated subtype (asthma already mapped), features elevated IgE and an allergic, eosinophil-driven inflammation distinct from the PR3/MPO autoimmunity of the other AAV subtypes.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Th2 eosinophilia: IL-4 and the type-2 response (IL-5 already mapped) drive the eosinophil expansion and tissue infiltration of eosinophilic granulomatosis with polyangiitis, targeted by anti-IL-5 and emerging anti-IL-4/13 therapy.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Endothelial injury: impaired endothelial nitric-oxide function accompanies the small-vessel inflammation of ANCA-associated vasculitis, contributing to the vascular damage that underlies its ischaemic organ manifestations.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Alveolar-haemorrhage anaemia: diffuse alveolar haemorrhage in the lung (already mapped) and the anaemia of chronic inflammation lower haemoglobin in ANCA-associated vasculitis, a fall in haemoglobin that can signal active pulmonary bleeding.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Th2 axis in EGPA: IL-13 with IL-4 and IL-5 (already mapped) drives the type-2 eosinophilic inflammation of eosinophilic granulomatosis with polyangiitis, the subset increasingly treated with anti-type-2 biologics.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative burst injury: ANCA-activated neutrophils (already mapped) release reactive oxygen species, including from xanthine oxidase, that damage the small-vessel endothelium, part of the oxidative injury of the vasculitic lesion.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Regulatory balance: IL-10 from regulatory T and B cells restrains the autoreactive response, and deficient IL-10-mediated regulation contributes to the unchecked autoimmunity that produces the ANCA and the vasculitis.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Inflammatory eicosanoids: prostaglandins from the neutrophil (already mapped) and infiltrating cells amplify the inflammation of the vasculitic lesion (IL-6, TNF and IL-1 already mapped), part of the eicosanoid dimension of the small-vessel injury.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Eosinophilic type-2 inflammation: mast cells, with eosinophils and the type-2 cytokines (IL-5, IL-4 and IL-13 already mapped), drive the allergic inflammation of eosinophilic granulomatosis with polyangiitis (EGPA), the type-2 subset of ANCA vasculitis.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Anaemia of inflammation: the chronic IL-6 (already mapped) inflammation of active ANCA vasculitis raises hepcidin, sequestering iron to produce the anaemia of chronic disease (haemoglobin already mapped) seen in active disease.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Vascular injury and repair: VEGF drives the endothelial injury and the angiogenesis of the granulomatous and healing vasculitic lesions, part of the vascular biology of the small-vessel injury in ANCA vasculitis.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — Endothelial activation: the angiopoietin-Tie2 axis reflects the endothelial activation of the small-vessel injury of ANCA vasculitis (VEGF already mapped), part of the endotheliopathy of the vasculitic lesion.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Checkpoint-triggered vasculitis: the PD-1 checkpoint whose blockade by cancer immunotherapy can trigger an ANCA-associated vasculitis, and whose peripheral-tolerance mechanisms are disturbed in the autoimmunity of the disease.
- `connects-to` → **[CTLA-4](../../03-molecular/ctla-4/README.md)** — Co-inhibitory checkpoint: CTLA-4, with PD-1 (already mapped), regulates the autoreactive T cells that help the B cells (CD20 and BAFF already mapped) produce the ANCA (immunoglobulin already mapped), and its blockade can precipitate vasculitis.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Regulatory T-cell tolerance: IL-2 signalling in the regulatory T cells maintains the tolerance whose failure permits the autoreactive response of ANCA vasculitis, and low-dose IL-2 is studied to restore it.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Immune-metabolic adipokine: leptin is the adipokine of the immune-metabolic milieu and the steroid (cortisol already mapped)-related metabolic disturbance of ANCA vasculitis.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the immune-metabolic milieu of ANCA vasculitis.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the systemic inflammation (IL-6 already mapped) of ANCA vasculitis.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Innate cytotoxicity: the NK cells (perforin already mapped) are part of the innate immune dysregulation of the small-vessel autoimmunity of ANCA vasculitis.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Cytotoxic effectors: the cytotoxic T cells (perforin already mapped) contribute to the endothelial and tissue injury of the ANCA vasculitis, alongside the ANCA-activated neutrophils (already mapped).
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm, which with the Th17 (IL-17 and IL-23 already mapped) drives the granulomatous inflammation of ANCA vasculitis.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Type-2 alarmin: TSLP, with IL-33 (already mapped), is the epithelial alarmin driving the eosinophilic type-2 (IL-4, IL-5 and IL-13 already mapped) inflammation of the EGPA subtype of ANCA vasculitis.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Eosinophil biomarker: periostin, downstream of the type-2 (IL-13 already mapped) cytokines, marks the eosinophilic tissue inflammation of the EGPA subtype of ANCA vasculitis.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell/eosinophil effector: the histamine of the mast cells (already mapped) and eosinophils contributes to the type-2 vascular and tissue inflammation of the EGPA subtype of ANCA vasculitis.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement/contact regulation: the C1-esterase inhibitor regulates the classical complement and the contact pathways, complementing the factor H (already mapped) control of the alternative pathway (C5aR1 already mapped, the avacopan target) of ANCA vasculitis.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Antioxidant micronutrient: selenium, a selenoprotein cofactor, is part of the oxidative-stress and micronutrient dimension of the autoimmune vascular inflammation of ANCA vasculitis.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Nutritional immunity: transferrin, the iron carrier, reflects the disordered iron handling of the anaemia of the chronic inflammation of ANCA vasculitis.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Vascular matricellular: osteopontin, released by the activated neutrophils (already mapped) and myeloid cells, is a matricellular mediator amplifying the vascular inflammation of ANCA vasculitis.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Crescent/granuloma fibrosis: the fibroblasts drive the fibrotic remodelling of the pauci-immune crescentic glomerulonephritis and the granulomatous inflammation of ANCA vasculitis.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Vessel-wall matrix: collagen, the vascular extracellular-matrix scaffold, is degraded and remodelled during the necrotising vascular injury and the fibrosis of ANCA vasculitis.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-vasculitis axis: bradykinin, via B1/B2 receptors on vascular endothelium (already mapped) and neutrophils (already mapped), amplifies the vascular permeability and the necrotising inflammation of ANCA vasculitis.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Anaemia of inflammation: erythropoietin response is blunted by the chronic inflammation (IL-6, TNF already mapped) of ANCA vasculitis, contributing to the normocytic anaemia of the active disease.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian immunomodulation: melatonin, via its anti-inflammatory and antioxidant effects, modulates the neutrophil (already mapped) activation and the oxidative injury of the systemic autoimmune inflammation of ANCA vasculitis.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Sex-hormone vasculitis: testosterone exerts anti-inflammatory effects on neutrophil (already mapped) and T-cell (already mapped) autoimmunity; the male sex predisposition to GPA and the female-to-MPA ratio implicate androgen-mediated immune modulation in ANCA vasculitis.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Platelet-serotonin vascular injury: serotonin, released by platelets (already mapped) upon the endothelial (already mapped) injury of necrotising vasculitis, amplifies the vasoconstriction and the thrombotic occlusion of the ANCA-damaged vessel wall.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Immune neuroendocrine: prolactin modulates T-cell (already mapped) and B-cell (already mapped) autoimmune activation; its elevation in active systemic autoimmune disease contributes to the sex-immune-neuroendocrine dimension of ANCA vasculitis.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — ANCA oxytocin: oxytocin, via OXTR on neutrophils (already mapped) and regulatory T cells (already mapped), attenuates autoimmune vascular inflammation; oxytocin deficiency amplifies the IL-6 (already mapped) and NLRP3 (already mapped) vasculitic cascade of ANCA vasculitis.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — ANCA vasopressin: vasopressin, via V1aR on endothelial cells (already mapped) and smooth-muscle cells (already mapped), modulates vascular tone; vasopressin dysregulation amplifies the nitric-oxide (already mapped) and complement C3 (already mapped) cascade of ANCA vasculitis.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — ANCA iodine: iodine-dependent thyroid hormones modulate neutrophil (already mapped) and T-cell (already mapped) autoimmune activation; iodine deficiency impairs the cortisol (already mapped) and IL-6 (already mapped) regulatory axis of the autoimmune cascade of ANCA vasculitis.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Th17 amplifier: high dietary sodium promotes Th17 (T-helper cell already mapped) polarisation and neutrophil (already mapped) activation; sodium-induced IL-17 (already mapped) and NF-κB (already mapped) dysregulation amplifies the autoimmune vascular inflammation of ANCA vasculitis.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Immune-enzyme cofactor: magnesium, as cofactor of immune enzymes in T-helper cells (already mapped) and neutrophils (already mapped), restrains NLRP3 (already mapped) and NF-κB (already mapped); magnesium deficiency amplifies the autoimmune vascular inflammation of ANCA vasculitis.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Vascular antioxidant: copper, as SOD cofactor, scavenges ROS in endothelial cells (already mapped) and neutrophils (already mapped) driving vascular injury; copper deficiency amplifies the NLRP3 (already mapped) and NF-κB (already mapped) complement-driven inflammation of ANCA vasculitis.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — ANCA potassium: potassium efflux from neutrophils (already mapped) and macrophages (already mapped) activates NLRP3 (already mapped); potassium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and complement-C3 (already mapped) vasculitic cascade in ANCA.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — ANCA calcium: calcium activates neutrophil (already mapped) degranulation and endothelial-cell (already mapped) injury; calcium dysregulation amplifies NLRP3 (already mapped) and NF-κB (already mapped) and complement-C5 (already mapped) and IL-6 (already mapped) cascade in ANCA.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — ANCA zinc: zinc cofactors macrophage (already mapped) anti-inflammatory function and neutrophil (already mapped) regulation; zinc deficiency amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) and complement-C3 (already mapped) cascade in ANCA.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — phosphorus-driven ATP in neutrophils (already mapped) and macrophages (already mapped) sustains vasculitic immune activation; phosphorus deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and complement-C3 (already mapped) vasculitic cascade in ANCA.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — nitric oxide from iNOS in neutrophils (already mapped) and macrophages (already mapped) modulates endothelial-cell (already mapped) vasodilation; nitrogen excess amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) vasculitic cascade in ANCA.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — chloride channels on neutrophils (already mapped) and endothelial cells (already mapped) regulate intracellular pH; chloride dysregulation amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) vasculitic cascade in ANCA.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — ANCA carbon: carbon backbone of cytokines in neutrophils (already mapped) and macrophages (already mapped) drives vasculitic inflammation; carbon dysregulation amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) vasculitic cascade in ANCA.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — ANCA hydrogen: hydrogen, via redox homeostasis in neutrophils (already mapped) and endothelial cells (already mapped), quenches vasculitic ROS; hydrogen dysregulation amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade in ANCA.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — ANCA sulfur: H2S from sulfur-amino acids in neutrophils (already mapped) and endothelial cells (already mapped) modulates vascular tone; sulfur deficiency amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) vasculitic cascade in ANCA.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — ANCA GLP-1: GLP-1 receptor signalling in macrophages (already mapped) and endothelial cells (already mapped) modulates vascular homeostasis; GLP-1 dysregulation amplifies NF-κB (already mapped) and NLRP3 (already mapped) and IL-6 (already mapped) cascade of ANCA vasculitis.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — ANCA angiotensin-II: angiotensin-II in endothelial cells (already mapped) and macrophages (already mapped) promotes vascular inflammation; angiotensin-II excess amplifies NF-κB (already mapped) and NLRP3 (already mapped) and IL-6 (already mapped) vasculitic cascade of ANCA.
- `connects-to` → **[WNT/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — ANCA WNT/β-catenin: WNT/β-catenin in endothelial cells (already mapped) and macrophages (already mapped) supports vascular repair; WNT dysregulation amplifies NF-κB (already mapped) and NLRP3 (already mapped) and IL-6 (already mapped) vasculitic cascade of ANCA vasculitis.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — ANCA RANKL: RANKL in macrophages (already mapped) and vascular endothelium (already mapped) modulates the vascular bone-immune axis; RANKL excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) vasculitic cascade of ANCA vasculitis.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — ANCA SMAD4: SMAD4 in vascular endothelium (already mapped) and macrophages (already mapped) modulates vascular remodelling; SMAD4 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) vasculitic cascade of ANCA vasculitis.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — ANCA fibronectin: fibronectin in vessel walls (already mapped) and macrophages (already mapped) modulates vascular matrix integrity; fibronectin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of ANCA vasculitis.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — ANCA notch: NOTCH on endothelial cells (already mapped) and macrophages (already mapped) regulates vascular repair; NOTCH dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of ANCA vasculitis.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — ANCA igf-1: IGF-1 from endothelial cells (already mapped) and macrophages (already mapped) promotes vascular repair; IGF-1 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of ANCA vasculitis.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — ANCA activin-a: activin-A from macrophages (already mapped) and endothelial cells (already mapped) regulates vascular immune-fibrotic balance; activin-a excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of ANCA vasculitis.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — ANCA cgrp: CGRP from macrophages (already mapped) and endothelial cells (already mapped) modulates ANCA vascular tone; cgrp dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of ANCA vasculitis.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — ANCA calcitonin: calcitonin from macrophages (already mapped) and endothelial cells (already mapped) modulates ANCA calcium balance; calcitonin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of ANCA vasculitis.
- `connects-to` → **[Substance P](../../03-molecular/substance-p/README.md)** — ANCA substance-p: substance P from macrophages (already mapped) and endothelial cells (already mapped) modulates ANCA neuroimmune tone; substance-p excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of ANCA vasculitis.
- `connects-to` → **[Insulin Receptor](../../03-molecular/insulin-receptor/README.md)** — ANCA insulin-receptor: insulin receptor on macrophages (already mapped) and endothelial cells (already mapped) drives vascular tone; insulin-receptor dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of ANCA vasculitis.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — ANCA aldosterone: aldosterone from macrophages (already mapped) and endothelial cells (already mapped) modulates vascular ion balance; aldosterone excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of ANCA vasculitis.
- `connects-to` → **[Androgen Receptor](../../03-molecular/androgen-receptor/README.md)** — ANCA androgen-receptor: androgen receptor on macrophages (already mapped) and endothelial cells (already mapped) modulates hormonal tone; androgen-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of ANCA vasculitis.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — ANCA norepinephrine: norepinephrine from macrophages (already mapped) and endothelial cells (already mapped) modulates vascular adrenergic tone; norepinephrine excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of ANCA vasculitis.
- `connects-to` → **[Adrenomedullin](../../03-molecular/adrenomedullin/README.md)** — ANCA adrenomedullin: adrenomedullin from macrophages (already mapped) and endothelial cells (already mapped) modulates vessel tone; adrenomedullin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of ANCA vasculitis.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — ANCA bdnf: BDNF from macrophages (already mapped) and endothelial cells (already mapped) modulates vascular neuroimmune repair; BDNF deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of ANCA vasculitis.

[^yates-2022-anca-review]: Yates M, Watts RA, Bajema IM, et al. EULAR/ERA-EDTA recommendations for the management of ANCA-associated vasculitis. *Ann Rheum Dis.* 2016;75(9):1583-1594. [doi:10.1136/annrheumdis-2016-209133](https://doi.org/10.1136/annrheumdis-2016-209133) · [PubMed 27338776](https://pubmed.ncbi.nlm.nih.gov/27338776/)
[^stone-2010-rituximab-gpa-rave]: Stone JH, Merkel PA, Spiera R, et al. Rituximab versus cyclophosphamide for ANCA-associated vasculitis. *N Engl J Med.* 2010;363(3):221-232. [doi:10.1056/NEJMoa0909905](https://doi.org/10.1056/NEJMoa0909905) · [PubMed 20647199](https://pubmed.ncbi.nlm.nih.gov/20647199/)
[^jayne-2021-avacopan-advocate]: Jayne DRW, Merkel PA, Schall TJ, Bekker P. Avacopan for the Treatment of ANCA-Associated Vasculitis. *N Engl J Med.* 2021;384(7):599-609. [doi:10.1056/NEJMoa2021349](https://doi.org/10.1056/NEJMoa2021349) · [PubMed 33596356](https://pubmed.ncbi.nlm.nih.gov/33596356/)
[^specks-2013-rituximab-anca-maintenance]: Charles P, Terrier B, Perrodeau É, et al. Comparison of individually tailored versus fixed-schedule rituximab regimen to maintain ANCA-associated vasculitis remission. *Ann Rheum Dis.* 2018;77(8):1143-1149. [doi:10.1136/annrheumdis-2017-212862](https://doi.org/10.1136/annrheumdis-2017-212862) · [PubMed 29549154](https://pubmed.ncbi.nlm.nih.gov/29549154/)

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
