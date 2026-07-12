---
schema: human-scale-entry/v1
id: hemophilia-a
name: Hemophilia A
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Hemophilia A is X-linked FVIII deficiency (F8 gene; Xq28); severe <1 IU/dL → joint/muscle hemorrhage. Emicizumab (bispecific FIXa/FX mAb; HAVEN-3: ABR 0.3 vs 22.9; FDA 2017) replaced prophylactic FVIII as standard of care in inhibitor and non-inhibitor severe HA."
aliases: ["hemophilia A", "HA", "factor VIII deficiency", "FVIII deficiency", "hemophilia A with inhibitors", "haemophilia A", "congenital FVIII deficiency"]
sources:
  - id: oldenburg-2017-emicizumab-haven1
    type: peer-reviewed
    cite: "Oldenburg J, Mahlangu JN, Kim B, et al. Emicizumab prophylaxis in hemophilia A with inhibitors. N Engl J Med. 2017;377(9):809-818."
    doi: "10.1056/NEJMoa1703068"
    pmid: "28691557"
    url: "https://doi.org/10.1056/NEJMoa1703068"
  - id: mahlangu-2018-emicizumab-haven3
    type: peer-reviewed
    cite: "Mahlangu J, Oldenburg J, Paz-Priel I, et al. Emicizumab prophylaxis in patients who have hemophilia A without inhibitors. N Engl J Med. 2018;379(9):811-822."
    doi: "10.1056/NEJMoa1803550"
    pmid: "30157389"
    url: "https://doi.org/10.1056/NEJMoa1803550"
  - id: pipe-2023-fitusiran-atlas
    type: peer-reviewed
    cite: "Pipe SW, Leebeek FW, Recht M, et al. Once-monthly subcutaneous fitusiran versus on-demand bypassing agent for haemophilia A or B with inhibitors (ATLAS-INH): a multicentre, open-label, randomised phase 3 trial. Lancet. 2023;401(10386):1427-1439."
    doi: "10.1016/S0140-6736(23)00284-2"
    pmid: "37003297"
    url: "https://doi.org/10.1016/S0140-6736(23)00284-2"
cross_links:
  - target: 01-human/03-molecular/von-willebrand-factor
    relation: connects-to
    note: "VWF binds and protects FVIII in plasma → t½ ~12 h (VWF-bound) vs. ~2 h (free); VWF deficiency in VWD type 3 → secondary FVIII <10 IU/dL (resembles mild hemophilia A); VWD type 2N: FVIII-binding domain mutations → FVIII deficiency with normal VWF antigen levels."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Anti-FVIII inhibitor antibodies are predominantly IgG4 (non-complement-fixing); IgG4 neutralizes FVIII infused as replacement therapy; inhibitor titer (Bethesda units) determines immune tolerance induction strategy; emicizumab bypasses FVIII → effective despite IgG4 inhibitors."
  - target: 01-human/03-molecular/thrombin
    relation: connects-to
    note: "Thrombin cleaves FVIII at Arg372/Arg740/Arg1689 → generates FVIIIa cofactor for intrinsic tenase; APC (thrombomodulin-thrombin product) cleaves FVIIIa at Arg336/Arg562 → inactivation; in HA, extrinsic-pathway thrombin is intact but amplification (intrinsic tenase) fails."
  - target: 01-human/03-molecular/protein-c
    relation: connects-to
    note: "APC inactivates FVIIIa by cleavage at Arg336 and Arg562; APC + protein S → efficient FVIIIa proteolysis → limits thrombin amplification; FV Leiden co-inheritance with mild HA creates a clinical paradox — APC resistance partially counteracts the hemophilic bleeding tendency."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Severe HA (FVIII <1%) confers significant VTE protection; historical VTE rate in HA ~0.5/1000 PY vs. ~1.5-3/1000 general population; emicizumab reconstitutes intrinsic tenase; avoid high-dose APCC with emicizumab → TMA; gene therapy raising FVIII >150% increases VTE risk."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "Gene therapy for hemophilia A delivers an AAV-packaged F8 transgene to hepatocytes, which then secrete factor VIII; valoctocogene roxaparvovec raised FVIII toward normal, but expression wanes ~50%/year as episomal AAV DNA dilutes with hepatocyte turnover."
  - target: 01-human/03-molecular/antithrombin
    relation: connects-to
    note: "Fitusiran flips hemophilia A treatment around: instead of replacing factor VIII, this siRNA lowers antithrombin to rebalance hemostasis and restore clotting in FVIII- or FIX-deficient patients, including those with inhibitors; overcorrection risks thrombosis."
  - target: 01-human/07-system/inherited-thrombophilia
    relation: connects-to
    note: "Hemophilia A and inherited thrombophilia are mirror images — too little clotting versus too much; strikingly, co-inheriting factor V Leiden can soften a hemophiliac's bleeding because APC resistance keeps FVa active longer, compensating for the missing factor VIII amplification."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Recurrent hemarthrosis is the defining morbidity of hemophilia A: bleeding into knees, ankles and elbows triggers synovitis, cartilage loss and destructive 'hemophilic arthropathy' → chronic pain and disability; prophylaxis and emicizumab aim to prevent these joint bleeds."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Factor VIII is synthesized largely by liver sinusoidal endothelial cells and circulates protected by endothelial von Willebrand factor; injury exposing the subendothelial matrix starts hemostasis—context for FVIII deficiency, and a target for hemophilia gene therapy."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Hemophilia A spares primary hemostasis—platelets still form the plug—but lacks the FVIIIa/FIXa 'tenase' complex that assembles on the activated platelet surface to burst-generate thrombin; without it the plug is unstable and rebleeds, hence delayed deep-tissue and joint bleeding."
  - target: 01-human/07-system/disseminated-intravascular-coagulation
    relation: connects-to
    note: "Hemophilia A and DIC cause bleeding by opposite mechanisms: hemophilia is isolated factor VIII deficiency (long aPTT, normal PT and platelets) bleeding into joints, while DIC consumes all factors and platelets at once—the lab pattern tells inherited from acquired."
  - target: 01-human/07-system/immune-thrombocytopenia
    relation: connects-to
    note: "Hemophilia A and immune thrombocytopenia bleed by different mechanisms: hemophilia is a factor VIII deficit causing deep joint and muscle bleeds, while ITP is platelet destruction causing mucocutaneous petechiae—the pattern hints which arm of hemostasis failed."
  - target: 01-human/07-system/thrombotic-thrombocytopenic-purpura
    relation: connects-to
    note: "Hemophilia A and TTP sit at opposite poles of hemostasis: hemophilia fails to clot from factor VIII deficiency and bleeds, while TTP clots pathologically from ADAMTS13 deficiency, consuming platelets in microthrombi—both too little and too much clotting cause disease."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver is central to hemophilia A: hepatocytes make clotting factors, and liver-directed gene therapy now delivers a working factor VIII gene to hepatocytes, enabling them to produce the missing factor—turning the factor-making organ into the cure."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Intracranial hemorrhage is the most feared bleed in hemophilia A: deficient factor VIII can't stabilize clots, so brain bleeding is a leading cause of death—hemorrhagic stroke here is the mirror image of the ischemic stroke that clotting disorders cause."
  - target: 01-human/07-system/antiphospholipid-syndrome
    relation: connects-to
    note: "Hemophilia A and antiphospholipid syndrome are mirror-image coagulation disorders—bleeding versus clotting: hemophilia lacks factor VIII, while APS has thrombosis-driving antiphospholipid antibodies; an acquired factor VIII inhibitor rarely bridges them."
  - target: 01-human/03-molecular/fibrinogen
    relation: connects-to
    note: "Hemophilia A spares fibrinogen but fails to reach it: factor VIII deficiency cripples the intrinsic pathway's thrombin burst, so although fibrinogen is normal, too little thrombin forms to convert it to a stable fibrin clot—hence delayed, recurrent bleeding."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Intracranial hemorrhage is the most feared hemophilia A complication: minor head trauma can cause life-threatening brain bleeding because clot formation is delayed, so prophylactic factor replacement and urgent dosing after head injury are central to care."
  - target: 01-human/07-system/hepatitis-c
    relation: connects-to
    note: "Hemophilia A is historically tied to hepatitis C and HIV: before viral screening, pooled factor concentrates infected most treated patients with HCV and HIV—a tragedy that drove recombinant factor development, so older hemophiliacs carry a heavy chronic-viral burden."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Hemophilia A is X-linked: the factor VIII gene sits on the X chromosome, so it overwhelmingly affects males while carrier mothers pass it on—making family history, carrier testing, and genetic counseling central to the reproductive side of the disease."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "The immune system is hemophilia A's biggest treatment hurdle: some patients form neutralizing antibodies (inhibitors) against infused factor VIII, making replacement fail—so immune tolerance regimens and inhibitor-bypassing agents like emicizumab are needed."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Bleeding in hemophilia A drains red cells: recurrent joint and muscle bleeds, plus dangerous internal hemorrhage, cause iron-deficiency or acute anemia, so falling hemoglobin and the need for transfusion track the severity of uncontrolled bleeding."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium is the silent partner of the clotting cascade hemophilia disrupts: as coagulation Factor IV, calcium ions are needed to assemble the tenase and prothrombinase complexes—so clotting depends on calcium, and citrate that binds it blocks coagulation in stored blood."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "The feared complication of hemophilia A is inhibitors, driven by T-helper cells: in some patients, helper T cells license B cells to make anti-Factor-VIII antibodies that neutralize replacement therapy, forcing bypassing agents or immune tolerance induction."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Repeated joint bleeds in hemophilia damage joints through macrophages: blood in the joint loads synovial macrophages with iron, driving inflammatory synovitis that erodes cartilage—the hemophilic arthropathy that prophylactic factor aims to prevent."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Hemophilia A forms the collagen-triggered platelet plug but can't stabilize it: exposed collagen still recruits platelets into an initial plug, but without factor VIII the secondary fibrin clot never reinforces it, so bleeding restarts hours later."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Hemophilia A's worst complication is immune, needing regulatory T cells: about a third of severe patients make anti-factor-VIII antibodies (inhibitors), and immune tolerance induction works to restore the Tregs that should accept the infused factor."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Hemophilia A's inhibitors come from B cells: in patients who make anti-factor-VIII antibodies, B cells produce the neutralizing IgG that defeats replacement therapy—so B-cell-depleting rituximab is used to help eradicate stubborn inhibitors."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Hemophilia's joint bleeds leave iron behind: blood pooling in a joint deposits iron as hemosiderin that inflames the synovium and erodes cartilage, driving the crippling hemophilic arthropathy—and repeated bleeds also cause iron-loss anemia."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Hemophilia often bleeds into the urinary tract: painless hematuria is common, and clots can obstruct the ureter, so kidney and bladder bleeding is a recognized, usually self-limited feature managed cautiously to avoid clot retention."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Hemophilia can bleed dangerously into the gut: gastrointestinal hemorrhage, sometimes massive, is a serious complication, so dark or bloody stools in a hemophiliac demand urgent factor replacement and evaluation."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Imaging tracks hemophilia's joint damage: X-ray and MRI photons reveal the arthropathy from repeated bleeds, and radiosynovectomy uses radiation to quiet a chronically bleeding joint."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Hemophilia shows on the skin: easy bruising and large, deep hematomas are often the first sign in a toddler learning to walk, hinting at the clotting defect beneath the surface."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Chronic bleeding taxes the marrow: ongoing blood and iron loss in hemophilia push the bone marrow to ramp up red-cell production to keep pace, and anemia results when the losses outstrip it."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "Hemophilia carries a tragic medical legacy: before viral screening and recombinant factor, the pooled plasma concentrates that treated it infected a large share of patients with HIV and hepatitis C, a catastrophe that reshaped blood-product safety."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows why hemophilia's clots fail: lacking factor VIII to drive thrombin, the fibrin mesh forms with fewer, thinner, loosely woven fibers, a fragile structure that cannot hold against ongoing bleeding."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Bleeding into the eye threatens sight in hemophilia: spontaneous or traumatic intraocular and retinal hemorrhages, like bleeds into other closed spaces, can raise pressure and damage vision if not promptly treated with factor replacement."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Hemophilia's bleeds can crush nerves: a deep muscle bleed — the classic iliopsoas hematoma — compresses the femoral nerve into palsy, while an intracranial hemorrhage destroys neurons directly, the most feared complication."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "Hemophilia quietly weakens the skeleton: recurrent joint bleeds destroy cartilage and bone, and reduced activity plus chronic inflammation tip the osteoblast-osteoclast balance toward the low bone density common in these patients."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "Why hemophilia bleeds late, not instantly: the first response to injury — reflex constriction of the vessel's smooth muscle and the platelet plug — is intact, so small cuts seal, but the missing factor VIII fails the later step, letting deep bleeds well up hours afterward."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies are hemophilia's nemesis and its newest cure: inhibitor alloantibodies against infused factor VIII are the dreaded complication that neutralizes treatment, while emicizumab, a bispecific antibody bridging factors IXa and X, now prevents bleeds without it."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "A deep bleed can crush a nerve: a tense hematoma in the iliopsoas or forearm compresses the peripheral nerve running through it, causing a compartment syndrome with numbness, weakness, and palsy that needs urgent factor replacement."
  - target: 01-human/07-system/hepatitis-b
    relation: connects-to
    note: "The old treatment carried hidden viruses: before viral inactivation, plasma-derived factor VIII concentrates transmitted hepatitis B and C and HIV to a generation of patients, a tragedy that drove the shift to recombinant factor and vaccination."
  - target: 01-human/04-cellular/osteoclast
    relation: connects-to
    note: "Bleeding into joints destroys them: recurrent hemarthrosis dumps iron and inflammation into the joint, driving osteoclasts to erode bone and cartilage into the crippling hemophilic arthropathy that defines untreated disease."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Hemophilia thins the skeleton: the pain and arthropathy that limit weight-bearing exercise, plus the disease itself, leave people with hemophilia with reduced bone density and a higher fracture risk than the general population."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "The immune system can reject the treatment: in some patients dendritic cells present infused factor VIII as foreign, priming the neutralizing antibodies (inhibitors) that are the most challenging complication of replacement therapy."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Repeated joint bleeds wreck the joint: blood in the synovium drives a fibroblast-led hypertrophy and fibrosis that, with iron-laden inflammation, destroys cartilage into the crippling hemophilic arthropathy that defines the disease's burden."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Gene therapy meets the immune system: the AAV vector delivering a working factor VIII gene to liver cells can draw cytotoxic T cells that attack the transduced hepatocytes, an immune response that can erode the durability of the one-time cure."
  - target: 01-human/07-system/iron-deficiency-anemia
    relation: connects-to
    note: "Chronic blood loss drains iron: beyond dramatic joint and muscle bleeds, mucosal and gastrointestinal bleeding in hemophilia steadily depletes iron stores, leaving many patients with a superimposed iron deficiency anemia."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Blood in the joint turns on inflammation: iron and breakdown products from recurrent hemarthroses activate NF-κB in synovial cells, switching on the inflammatory and angiogenic genes that drive the chronic synovitis of hemophilic arthropathy."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Beyond blood loss, inflammation suppresses the marrow: the chronic synovitis of hemophilic arthropathy raises inflammatory cytokines that blunt erythropoiesis, an anemia of chronic disease distinct from the iron loss of bleeding."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "The lines used to infuse factor can seed infection: many patients, especially children, rely on indwelling central venous ports for clotting-factor delivery, and these catheters are a recurring source of bloodstream infection and sepsis."
  - target: 01-human/07-system/opioid-use-disorder
    relation: connects-to
    note: "Crippled joints drive long-term opioid use: the recurrent hemarthroses of hemophilia destroy joints into a painful arthropathy, and the chronic pain often leads to sustained opioid use with its risk of dependence."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A lifelong disease with a heavy history weighs on mood: chronic pain, disability, and for older patients the trauma of transfusion-acquired HIV and hepatitis C give hemophilia A a high burden of depression."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Aging hemophiliacs now meet heart disease: with near-normal lifespans, older patients develop coronary disease and heart failure, whose antithrombotic management is a delicate balance against their underlying bleeding tendency."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Bleeds compress nerves and wreck joints: hematomas pressing on peripheral nerves and the chronic hemophilic arthropathy from recurrent hemarthrosis generate persistent neuropathic and nociceptive pain in hemophilia A."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "The kidneys both bleed and decline: recurrent hematuria is common in hemophilia, and aging patients — many with prior HIV or hepatitis C from old factor concentrates — face rising rates of hypertension and chronic kidney disease."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "Blood pressure runs high in this population: hemophilia A patients show a higher prevalence of hypertension than the general population, compounding the bleeding risk of any intracranial event."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Without clotting, wounds bleed instead of healing: deficient factor VIII leaves the clot unstable, so any surgery or injury in hemophilia A re-bleeds, and procedures demand factor replacement to allow healing."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It bleeds into the gut: gastrointestinal haemorrhage is a recognised bleeding site in hemophilia A, where even a minor mucosal lesion or ulcer can cause prolonged, dangerous blood loss."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Living one bleed away from danger breeds worry: the lifelong unpredictability of spontaneous bleeds, joint damage and the vigilance hemophilia A demands foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Its most lethal bleeds are in the brain: intracranial and intraspinal haemorrhage are the leading causes of death in hemophilia A, while deep haematomas can compress peripheral nerves."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It bleeds into the urinary tract: spontaneous haematuria is common in hemophilia A, usually self-limiting but distressing, and clot colic or retention can follow heavy bleeding."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It shows beneath the skin: easy bruising, large spreading ecchymoses and soft-tissue haematomas after minor trauma are among the earliest visible signs of hemophilia A."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Bleeding can block the airway: retropharyngeal and neck haematomas in hemophilia A can obstruct the airway — a bleeding emergency — and haemothorax can occur with chest trauma."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Longer life brings a treatment dilemma: as patients with hemophilia A now age into coronary disease and atrial fibrillation, the antiplatelet and anticoagulant therapy they need is hazardous given their bleeding tendency."
  - target: 03-medicine/01-modern/12-anti-inflammatory/ibuprofen
    relation: connects-to
    note: "A common painkiller is off-limits: NSAIDs like ibuprofen are avoided in hemophilia because they impair platelet function and irritate the gut, compounding the bleeding risk."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "New drugs bypass the missing factor: the bispecific antibody emicizumab mimics factor VIII, and gene therapy delivering an FVIII gene now offers durable correction in haemophilia A."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "A tragic legacy in the lymphoid system: before viral inactivation, pooled factor concentrates transmitted HIV and hepatitis C to many haemophilia patients, with downstream AIDS-related lymphomas."
  - target: 02-pathogen/05-prions/prion-protein
    relation: connects-to
    note: "A feared transfusion legacy: plasma-derived clotting products carried a theoretical variant-CJD prion risk in the UK, prompting recipient notification and a shift to recombinant factor VIII."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Bleeding wrecks joints and bone: recurrent haemarthroses drive hemophilic arthropathy with cartilage and subchondral-bone destruction, and reduced mobility plus chronic disease leave many patients with low bone density and fractures."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "The liver makes its missing factor: factor VIII is produced largely by liver sinusoidal endothelial cells, which is why AAV gene therapy for hemophilia A delivers a working FVIII gene to the hepatocytes of the lobule for durable endogenous production."
  - target: 01-human/07-system/sickle-cell-disease
    relation: connects-to
    note: "A contrasting inherited blood disorder: hemophilia A is an X-linked clotting-factor deficiency causing bleeding, while sickle cell is a recessive haemoglobinopathy causing vaso-occlusion — both inherited and both now targets of gene therapy."
  - target: 01-human/07-system/heparin-induced-thrombocytopenia
    relation: connects-to
    note: "Opposite poles of haemostasis: haemophilia A bleeds from absent factor VIII, while heparin-induced thrombocytopenia paradoxically clots despite falling platelets—two disorders that frame the balance between bleeding and thrombosis."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Acquired haemophilia is autoimmune: autoantibodies against factor VIII can arise in autoimmune disease such as rheumatoid arthritis (and postpartum), causing sudden bleeding distinct from the inherited X-linked deficiency."
  - target: 01-human/07-system/dlbcl
    relation: connects-to
    note: "New bleeding can flag a hidden cancer: acquired haemophilia A from anti-factor-VIII autoantibodies is often paraneoplastic, classically with lymphoproliferative disorders like diffuse large B-cell lymphoma, so unexplained bleeding in an older adult warrants a malignancy search."
  - target: 01-human/07-system/hcc
    relation: connects-to
    note: "The transfusion-era legacy: hepatitis C from contaminated clotting-factor concentrates gave a generation of haemophilia patients chronic liver disease, cirrhosis and hepatocellular carcinoma, still a leading cause of death."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Where inhibitors are born: the anti-factor-VIII alloantibodies that defeat replacement therapy are class-switched and affinity-matured by B cells in germinal centres, the central immunological problem of haemophilia care."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "A paradoxical protection: the lifelong hypocoagulable state of haemophilia lowers the risk of arterial thrombosis, so atherosclerotic plaques in the arterial wall less often trigger heart attacks and ischaemic strokes."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "Acquired haemophilia: autoantibodies against Factor VIII can arise paraneoplastically with solid tumours like breast cancer (and with lymphoma or postpartum), causing sudden severe bleeding in a previously normal person."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "Renal bleeding: spontaneous haematuria is common in haemophilia, blood passing from the kidney through the glomerulus and urinary tract, where antifibrinolytics are avoided lest clots obstruct the ureter."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "An anticoagulation paradox: COVID-19's prothrombotic state complicates haemophilia management, balancing thromboprophylaxis against the underlying bleeding tendency, while the pandemic disrupted factor-replacement care."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "Joint destruction: recurrent haemarthrosis in haemophilia drives RANKL-mediated bone and cartilage resorption, the basis of the crippling hemophilic arthropathy."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Iron-driven synovitis: blood and iron deposited in joints by repeated bleeds trigger TNF-α-rich synovial inflammation that perpetuates hemophilic joint damage."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Synovial neovascularisation: VEGF-driven new-vessel growth in the iron-laden hemophilic synovium creates fragile vessels that rebleed, perpetuating the cycle of joint destruction."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Cartilage breakdown: IL-1β released after recurrent hemarthrosis drives chondrocyte matrix-metalloproteinase production, degrading articular cartilage in hemophilic arthropathy independent of the synovial inflammation."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Synovial hyperplasia: PDGF from activated platelets and macrophages after joint bleeds stimulates fibroblast and synoviocyte proliferation, thickening the hemophilic synovium toward chronic destructive disease."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Joint fibrosis: TGF-beta drives the fibrotic remodelling and contracture of chronically bled hemophilic joints, converting recurrent hemarthrosis into fixed deformity and stiffness."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Synovitis recruitment: CCL2 released after hemarthrosis draws monocytes and macrophages into the hemophilic synovium, building the inflammatory infiltrate that perpetuates the proliferative synovitis of target joints."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Synovial angiogenesis: the hypertrophic, iron-laden hemophilic synovium becomes hypoxic, stabilising HIF-1α to drive the fragile neovascularisation that predisposes the target joint to repeated rebleeding."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Heme-driven inflammation: heme and iron from repeated joint bleeds act as DAMPs on TLR4, igniting the innate inflammatory cascade that converts hemarthrosis into the chronic synovitis of hemophilic arthropathy."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Synovial neoangiogenesis: repeated hemarthrosis drives angiopoietin- and VEGF-dependent growth of fragile, leaky new vessels in the hemophilic synovium, which rebleed easily and lock the joint into a self-perpetuating cycle of bleeding and arthropathy."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Cartilage destruction: direct exposure of cartilage to blood triggers caspase-3-mediated chondrocyte apoptosis, a key mechanism by which recurrent joint bleeds degrade articular cartilage and produce the irreversible hemophilic arthropathy."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Synovitis amplification: IL-6 generated in the iron-laden hemophilic synovium amplifies the chronic inflammatory synovitis that follows recurrent bleeds, contributing to the proliferative pannus that erodes the joint."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "FVIII tolerance: regulatory IL-10 and regulatory T cells (already mapped) mediate immune tolerance to factor VIII, and their failure permits the neutralising-antibody inhibitors that are the major complication of hemophilia A therapy."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Iron-driven synovitis: repeated joint bleeds deposit iron (already mapped) that activates the NLRP3 inflammasome and IL-1β in the synovium, driving the chronic synovitis and progressive hemophilic arthropathy."
  - target: 01-human/03-molecular/ferroportin
    relation: connects-to
    note: "Joint iron overload: recurrent hemarthroses overwhelm macrophage iron export through ferroportin, leaving hemosiderin deposits in the synovium that perpetuate the inflammatory and oxidative damage of hemophilic arthropathy."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "Synovitis amplifier: blood in the joint drives synovial macrophages to release S100A8/A9 (calprotectin), amplifying the inflammatory synovitis that destroys cartilage in hemophilic arthropathy."
  - target: 01-human/03-molecular/fcrn
    relation: connects-to
    note: "Half-life and inhibitors: the neonatal Fc receptor extends the half-life of Fc-fused factor VIII concentrates (efmoroctocog) and recycles IgG, including the inhibitor antibodies (anti-FVIII) that complicate hemophilia A therapy."
  - target: 01-human/03-molecular/ctla-4
    relation: connects-to
    note: "Inhibitor tolerance: development of anti-FVIII inhibitor antibodies reflects loss of immune tolerance, and CTLA-4-dependent regulatory mechanisms underlie the immune-tolerance-induction protocols used to eradicate them."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Hemarthrosis synovitis: iron and blood-breakdown products in the hemophilic joint activate TLR-MyD88-NF-κB signalling (TLR4 and NF-κB already mapped), driving the chronic synovitis of recurrent hemarthrosis."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Inflammatory arthropathy: IL-6-JAK-STAT signalling (IL-6 already mapped) sustains the inflammatory synovitis that progresses to destructive hemophilic arthropathy."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Synovial proliferation: ERK-MAPK signalling drives the synovial proliferation and neoangiogenesis (VEGF already mapped) of the hypertrophic synovium in hemophilic arthropathy."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 amplifies the iron-driven synovial inflammation that drives the chronic synovitis of hemophilic arthropathy after recurrent haemarthrosis."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β already mapped) drives the joint fibrosis and cartilage degradation of the hemophilic arthropathy that follows repeated bleeds."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling transduces the inflammatory cytokine milieu of the hypertrophic synovium in hemophilic arthropathy."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO regulates the chondrocyte and synovial oxidative-stress response to the iron-driven joint degeneration of hemophilic arthropathy."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signaling shapes the T-helper response that governs anti-factor-VIII inhibitor antibody development in hemophilia A."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Hemarthrosis-derived cytosolic and mitochondrial DNA engages cGAS-STING, contributing to the chronic synovial inflammation of hemophilic arthropathy."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT signaling in synovial and endothelial cells participates in the blood-induced synovitis and neoangiogenesis of hemophilic arthropathy."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the inflammatory and iron-driven signaling of the recurrent hemarthrosis and synovial damage of hemophilia A."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-bearing cytotoxic lymphocytes participate in the immune response to factor-VIII replacement that can drive inhibitor development in hemophilia A."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) participates in the synovial and inflammatory responses of the hemophilic arthropathy of hemophilia A."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTOR signaling in the iron-laden synovium participates in the joint inflammation of hemophilic arthropathy in hemophilia A."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the synovitis and osteoclast-driven bone erosion of hemophilic arthropathy in hemophilia A."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment participates in the anti-factor-VIII immune response and hemophilic-arthropathy synovitis of hemophilia A."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the immune response to factor VIII in hemophilia A."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the synovial angiogenesis and leukocyte recruitment of hemophilic arthropathy in hemophilia A."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the immune response contributing to the anti-FVIII inhibitor formation of hemophilia A."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the immune activation influencing the anti-FVIII inhibitor response of hemophilia A."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the T-cell help driving the anti-FVIII inhibitor formation (a target of immune-tolerance induction) of hemophilia A."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Gene-therapy barrier: AAV gene therapy delivering a factor VIII transgene to the liver triggers innate type I interferon and adaptive responses against the capsid, the immune hurdle that limits durable expression and drives the corticosteroid prophylaxis used with these vectors."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Blood-loss anaemia: recurrent and sometimes occult bleeding in hemophilia A causes chronic blood loss that lowers haemoglobin, producing an iron-deficiency anaemia that compounds the disability and can require transfusion in severe bleeds."
  - target: 01-human/03-molecular/mu-opioid-receptor
    relation: connects-to
    note: "Chronic pain: the progressive hemophilic arthropathy from repeated joint bleeds causes chronic pain frequently managed with opioids acting on the mu-opioid receptor, a persistent burden and dependence risk in the aging hemophilia population."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Inhibitor immunology: development of neutralising anti-factor-VIII antibodies (inhibitors; IgG already mapped) depends on MHC class II presentation of factor VIII peptides to helper T cells, and HLA type influences the risk of this major treatment complication."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Tolerance and gene therapy: IL-2-driven T-cell responses shape both the immune-tolerance induction used to eradicate inhibitors and the immune reaction to the AAV vector and transgene in the liver-directed gene therapy (liver already mapped)."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Th2 antibody help: IL-4 and type-2 T-cell help drive the B-cell production of anti-factor-VIII inhibitors (immunoglobulin G already mapped), so the Th2 axis contributes to the alloimmune response that complicates factor replacement."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Haemophilic synovitis: prostaglandins from the inflamed synovium of recurrent haemarthrosis drive the pain and inflammation of haemophilic arthropathy, though NSAIDs are used cautiously given the bleeding risk."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Iron-catalysed joint oxidation: the iron deposited in the joint from repeated bleeds (ferroportin already mapped) catalyses reactive oxygen species, to which xanthine oxidase contributes, driving the synovial proliferation and cartilage damage of haemophilic arthropathy."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 cytokine axis: IL-13, with IL-4 (already mapped), completes the type-2 cytokine support for the B-cell inhibitor response, part of the alloimmune reaction against replacement factor VIII."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Coagulation factor IV: calcium is factor IV, an essential cofactor that anchors the clotting factors to membranes at the tenase and prothrombinase complexes (thrombin already mapped) where the missing factor VIII normally accelerates fibrin formation in haemophilia A."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "Th17 inhibitor immunity: the IL-17-producing helper T cells, with the type-2 IL-4 and IL-13 (already mapped), support the B-cell (already mapped) alloantibody response that produces the factor VIII inhibitors of haemophilia A."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Vascular and joint microenvironment: nitric oxide regulates the vascular tone and, in the iron-laden (already mapped) haemophilic joint, contributes to the synovial vascular changes and inflammation of the arthropathy."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Immune tolerance: the PD-1 checkpoint and the peripheral tolerance mechanisms are relevant to the immune-tolerance induction used to eradicate the factor VIII inhibitors (immunoglobulin already mapped) of haemophilia A."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Tolerance induction: the regulatory T cells are central to the immune-tolerance induction that re-establishes tolerance to factor VIII and eradicates the alloantibody inhibitors of haemophilia A."
  - target: 01-human/03-molecular/baff
    relation: connects-to
    note: "Inhibitor B-cell survival: BAFF supports the survival of the alloreactive B cells (already mapped) that produce the factor VIII inhibitors, part of the humoral response that complicates haemophilia A replacement therapy."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Bleeding iron balance: the recurrent bleeding and the anaemia (haemoglobin already mapped) of haemophilia A interact with the iron-regulatory hepcidin and the ferroportin (already mapped) iron export."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Metabolic-arthropathy adipokine: leptin is the adipokine of the marrow and synovial adipose signalling in the arthropathy and the immune-metabolic milieu of haemophilia A."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic milieu of haemophilia A."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the synovial and metabolic milieu of the haemophilic arthropathy."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 inhibitor immunity: the IFN-γ of the T-helper cells (already mapped) is the type-II interferon arm of the anti-FVIII alloantibody (immunoglobulin already mapped) inhibitor response of haemophilia A."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune response that drives the FVIII-inhibitor formation in haemophilia A."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the T-helper (already mapped) response to the infused FVIII in haemophilia A."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune response to the FVIII in haemophilia A."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2/anaphylaxis arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), can develop against the infused factor and underlies the rare anaphylactic reactions in haemophilia A."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Inhibitor source: the plasma cells, downstream of the B cells (already mapped), secrete the anti-FVIII inhibitor antibodies (immunoglobulin already mapped) that neutralise the infused factor in haemophilia A."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Anaphylaxis effector: the mast cells, armed with the anti-factor IgE (already mapped), are the effectors of the rare anaphylactic reactions to the infused FVIII in haemophilia A."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Gene-therapy complement: the complement C5 and its activation (with C3 already mapped) are part of the innate response to the AAV vector of the FVIII gene therapy of haemophilia A."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) links the complement to the innate inflammatory response to the AAV vector of the FVIII gene therapy of haemophilia A."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the innate response to the AAV vector of the FVIII gene therapy of haemophilia A."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Bleeding iron loss: transferrin, the iron carrier, reflects the disordered iron handling (ferroportin and hepcidin already mapped) of the iron-deficiency anaemia from the recurrent bleeding of haemophilia A."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Haemostatic barrier alarmin: TSLP, released from the vascular endothelium (already mapped) and connective tissue at trauma sites, modulates mast-cell (already mapped) and dendritic-cell (already mapped) immune responses at the bleeding sites of haemophilia A."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Contact-kinin amplifier: bradykinin, generated by the contact activation pathway, amplifies vascular permeability and the pain response at the haemarthrosis and soft-tissue haematoma sites of haemophilia A."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Anaemia axis: erythropoietin, secreted by the kidney (already mapped) in response to the recurrent bleeding-associated iron-deficiency anaemia (already mapped) of haemophilia A, drives the compensatory erythropoiesis of the disease."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Contact-kinin regulation: the C1-esterase inhibitor limits the classical complement and contact-kinin (bradykinin already mapped) cascades activated by recurrent haemarthrosis and soft-tissue haematoma, moderating the inflammatory joint damage of haemophilia A."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell haemarthrosis mediator: histamine, released by mast cells (already mapped) at haemarthrosis sites in haemophilia A, amplifies the local vascular permeability and inflammatory cytokine signalling (IL-1 and TNF already mapped) of the haemophilic joint."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Synovial ECM remodelling: periostin, induced by TGF-β (already mapped) in the synovial fibroblasts (already mapped) after recurrent haemarthrosis, contributes to the cartilage destruction and the chronic haemophilic arthropathy of haemophilia A."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "HA melatonin: melatonin suppresses TNF-α (already mapped) and IL-6 (already mapped) driven synovial inflammation in haemophilic arthropathy; melatonin also reduces macrophage (already mapped) activation and attenuates the cortical-bone (already mapped) erosion cascade."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "HA testosterone: androgen receptor signalling modulates platelet (already mapped) and thrombin (already mapped) activity in haemophilia A; testosterone also drives macrophage (already mapped) and B-cell (already mapped) activity in the inhibitor-development cascade."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "HA serotonin: platelet (already mapped) serotonin release modulates thrombin (already mapped) generation in haemophilia A; 5-HT2A on endothelial cells (already mapped) amplifies the TNF-α (already mapped) and IL-6 (already mapped) joint inflammatory cascade."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "HA oxytocin: oxytocin promotes VWF (already mapped) release and platelet (already mapped) aggregation via endothelial cell (already mapped) V1 receptors; oxytocin-driven NF-κB (already mapped) attenuation reduces macrophage (already mapped) synovial inflammation in arthropathy."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "HA vasopressin: DDAVP (synthetic AVP) triggers VWF (already mapped) and factor VIII release from endothelial cells (already mapped); V2 receptor signalling mobilises platelet (already mapped) cofactors and modulates NF-κB (already mapped) haemostatic inflammation."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "HA prolactin: prolactin signalling on B-cells (already mapped) amplifies anti-FVIII inhibitor development; prolactin-driven NF-κB (already mapped) activation promotes macrophage (already mapped) synovial inflammation and thrombin (already mapped) dysregulation in arthropathy."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "HA zinc: zinc cofactors hepatocyte (already mapped) coagulation-protein synthesis and macrophage (already mapped) function; zinc deficiency amplifies NF-κB (already mapped) inhibitor development and impairs thrombin (already mapped) and platelet (already mapped) haemostasis."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "HA selenium: selenium, via GPx in endothelial cells (already mapped), scavenges haemostatic ROS; selenium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) inflammation and impairs VWF (already mapped) and thrombin (already mapped) generation in HA."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "HA iodine: iodine-dependent thyroid hormones modulate hepatocyte (already mapped) coagulation-protein synthesis; iodine deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and impairs thrombin (already mapped) and VWF (already mapped) generation in HA."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "HA sodium: high dietary sodium promotes endothelial cell (already mapped) activation and macrophage (already mapped) inflammation; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) amplifies haemostatic impairment and thrombin (already mapped) dysfunction in HA."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "HA magnesium: magnesium cofactors hepatocyte (already mapped) coagulation-protein synthesis and endothelial cell (already mapped) function; magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and impairs thrombin (already mapped) generation in HA."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "HA chloride: chloride channels regulate hepatocyte (already mapped) and endothelial cell (already mapped) volume and ion homeostasis; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and impairs thrombin (already mapped) generation in HA."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "HA nitrogen: nitrogen as backbone of coagulation proteins and cytokines (already mapped) sustains haemostatic signalling; nitrogen-derived RNS from macrophages (already mapped) amplifies NF-κB (already mapped) and IL-6 (already mapped) inflammatory bleeding cascade in HA."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "HA phosphorus: phosphorus as ATP in hepatocytes (already mapped) and endothelial cells (already mapped) fuels coagulation-protein synthesis; phosphorus dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and impairs thrombin (already mapped) in HA."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "HA carbon: carbon in nucleotides of hepatocytes (already mapped) and endothelial cells (already mapped) fuels coagulation-factor biosynthesis; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and impairs thrombin (already mapped) generation in HA."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "HA copper: copper cofactors ceruloplasmin and lysyl oxidase in hepatocytes (already mapped) and endothelial cells (already mapped) support coagulation matrix; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and impairs thrombin (already mapped) in HA."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "HA hydrogen: hydrogen via ROS from macrophages (already mapped) and endothelial cells (already mapped) modulates haemostatic redox homeostasis; hydrogen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and impairs thrombin (already mapped) generation in HA."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "HA GLP-1: GLP-1 from gut L-cells (already mapped) and macrophages (already mapped) modulates haemophilia metabolic homeostasis; GLP-1 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) inflammatory cascade of haemophilia A."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "HA angiotensin-II: Angiotensin-II in endothelium (already mapped) and macrophages (already mapped) promotes vascular remodelling in haemophilia A; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) haemophilic cascade."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "HA Wnt/β-catenin: Wnt/β-catenin in synoviocytes (already mapped) and macrophages (already mapped) drives haemophilic arthropathy; Wnt dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) haemophilic arthropathy cascade."
---

# Hemophilia A

## Overview

**Hemophilia A (HA)** is an **X-linked recessive bleeding disorder** caused by deficiency or dysfunction of **coagulation factor VIII (FVIII)**, encoded by the *F8* gene on chromosome Xq28 [^oldenburg-2017-emicizumab-haven1]. FVIII is the essential cofactor for factor IXa (FIXa) in the **intrinsic tenase complex** (FIXa + FVIIIa + Ca²⁺ + phospholipid → activates factor X → thrombin generation → fibrin clot); without adequate FVIII, the coagulation cascade is severely impaired.

Hemophilia A is the **most common severe hereditary bleeding disorder**, affecting ~1 in 5,000-10,000 male births. Females are typically carriers (heterozygous; may have mild bleeding due to lyonization) or rarely have clinically significant disease (compound heterozygous; Turner syndrome).

**Severity classification:**

| Severity | FVIII level | Clinical phenotype |
|:---------|:-----------|:-------------------|
| Severe | <1 IU/dL (<1% normal) | Spontaneous joint/muscle hemorrhage; hemarthroses without provocation; life-threatening bleeds |
| Moderate | 1-5 IU/dL | Bleeds with minor trauma; rare spontaneous bleeds; occasional hemarthrosis |
| Mild | 5-40 IU/dL | Bleeds only with significant trauma/surgery; often undiagnosed until adult life |

**Inhibitor development:** The most serious complication of hemophilia A treatment; anti-FVIII IgG4 antibodies develop in ~25-30% of severe HA patients after FVIII exposure (typically within the first 50 exposure days). Inhibitors neutralize replacement FVIII, making standard therapy ineffective. Inhibitor titer is measured in Bethesda units (BU): high-titer inhibitors >5 BU require bypassing agents or immune tolerance induction (ITI).

**Revolutionary shift — emicizumab era:** Since the HAVEN-1 and HAVEN-3 trials (2017-2018), **emicizumab** (Hemlibra; Roche/Genentech) — a bispecific antibody bridging FIXa and FX — has replaced prophylactic FVIII infusions as the standard of care for most patients with severe HA (with or without inhibitors), reducing the treatment burden from frequent IV infusions to weekly/biweekly/monthly SC injections.

## Structure

### F8 gene and FVIII protein

| Feature | Detail |
|:--------|:-------|
| Gene | *F8*, chromosome Xq28; 186 kb, 26 exons — one of the largest genes in the human genome |
| mRNA | 9 kb; alternative splicing of exon 16 generates B-domain variants |
| FVIII protein | 2332 aa; domain structure: A1-A2-B-A3-C1-C2 (6 domains) |
| A domains (A1, A2, A3) | Copper-binding TRP domains; thrombin cleavage sites (Arg372, Arg740, Arg1689); FIXa binding (A2) and FX binding (A2, A3) |
| B domain | Heavily glycosylated (~100 kDa); no known cofactor function; removed during FVIII activation; absent in recombinant B-domain-deleted FVIII (rFVIIIBDD) products |
| C1-C2 domains (light chain) | Phospholipid membrane binding (C2: GRP48/phosphatidylserine); VWF binding (C1, C2) |
| Active form (FVIIIa) | Thrombin cleaves FVIII at Arg372/Arg740/Arg1689 → releases B domain → A1/A2/A3-C1-C2 trimer → FVIIIa cofactor; FVIIIa is unstable → rapid inactivation by APC/protein S or spontaneous A2 domain dissociation |

### Common F8 mutations

| Mutation type | Frequency | Severity |
|:-------------|:---------|:---------|
| Intron 22 inversion (inv22) | ~40-50% of severe HA | Severe |
| Intron 1 inversion (inv1) | ~5% of severe HA | Severe |
| Large deletions | ~5-10% | Severe; high inhibitor risk |
| Nonsense mutations | ~15% | Severe |
| Missense mutations | ~40% (all severities) | Mild to severe depending on domain |
| Splice site mutations | ~10% | Variable |

**Inhibitor risk:** Inversely related to residual FVIII epitope sharing with infused product. Patients with inv22 or large deletions have no FVIII protein → highest inhibitor risk (~35-40%). Missense mutations in mild-moderate HA: low inhibitor risk (shared epitopes with normal FVIII).

## Function

### FVIII in coagulation

FVIII is a critical **amplifier** of the coagulation cascade at the junction between the intrinsic pathway initiation and the common pathway:

1. **FVIII in plasma:** Circulates as an inactive procofactor bound to VWF (protects FVIII from LRP1-mediated clearance and APC cleavage); plasma concentration ~0.1-0.2 µg/mL (~1 nM)

2. **Activation:** At sites of vascular injury, thrombin (generated by the extrinsic pathway via TF-VIIa) cleaves VWF-bound FVIII → releases FVIIIa; alternatively, FXa cleaves FVIII less efficiently

3. **Intrinsic tenase complex:** FVIIIa binds FIXa on the phospholipid surface of activated platelets (PS exposed) → FIXa/FVIIIa complex = "intrinsic tenase" → activates FX → FXa → prothrombinase → thrombin generation increases by ~10⁵-fold vs. FIXa alone (this amplification = "coagulation burst")

4. **Inactivation:** APC (activated protein C) + protein S cleave FVIIIa at Arg336 and Arg562 (A1 domain); FVIIIa also spontaneously inactivates by A2 domain dissociation; thrombomodulin-thrombin generates APC

**Without FVIII:** TF-VIIa initiates thrombin generation but the amplification loop (intrinsic tenase) is absent → clot forms slowly or not at all → hemarthrosis, intramuscular hematoma, potentially life-threatening CNS or retroperitoneal hemorrhage in severe HA.

## Pathology

### Clinical manifestations

**Hemarthrosis (joint bleeding; ~75% of hemorrhagic events in severe HA):**
- Knees, ankles, elbows most commonly affected
- Acute: pain, swelling, warmth, limited range of motion
- Chronic: synovitis → iron deposition → reactive synovial proliferation → cartilage destruction → **hemophilic arthropathy** (radiographic changes, chronic pain, contracture)
- **Target joint:** A joint with ≥3 bleeds in 6 months; most at risk for chronic damage; primary target for prophylaxis monitoring
- MRI scoring (IPSG MRI score) or ultrasound (Haemophilia Early Arthropathy Detection; HEAD-US) monitors joint damage

**Intramuscular hematoma:**
- Iliopsoas hematoma: mimics appendicitis; femoral nerve compression → hip flexion deformity; requires urgent FVIII
- Compartment syndrome: forearm, calf bleeds → treat aggressively before compartment compromise

**Life-threatening bleeds:**
- CNS hemorrhage (3-10% lifetime risk in severe HA): intracranial, subdural, subarachnoid; any head trauma → immediate FVIII prophylaxis + urgent CT
- Retroperitoneal hematoma
- Upper airway compromise (neck/pharyngeal hematoma)
- GI bleeding

### Diagnosis

**Laboratory:**
- **aPTT prolonged**; PT/INR normal (FVIII is intrinsic pathway only); fibrinogen normal; platelets normal
- **FVIII activity assay (1-stage aPTT-based or 2-stage chromogenic):** Quantifies FVIII function; chronic discrepancy between 1-stage and 2-stage (2-stage higher) suggests mild hemophilia A with specific F8 mutations (e.g., Arg531His)
- **FVIII antigen (FVIII:Ag):** Normal in mild HA with dysfunctional FVIII (missense mutations)
- **VWF:Ag and VWF:RCo:** Exclude VWD type 2N (FVIII-binding domain mutation — presents like mild HA but VWF antigen normal, FVIII reduced)
- **Inhibitor screen (Bethesda assay / Nijmegen modification):** Heat-inactivated patient plasma mixed with normal plasma at 50:50 → incubate 2 hours at 37°C → measure residual FVIII; ≥0.6 BU/mL = positive inhibitor

### Treatment

**Prophylaxis — standard of care (severe and moderate HA):**

**Emicizumab (Hemlibra; Roche/Genentech; bispecific FIXa/FX mAb):**
- Mechanism: Binds FIXa (via one arm) and FX (via other arm) → mimics FVIIIa cofactor function → reconstitutes intrinsic tenase activity independent of FVIII
- Structure: Asymmetric bispecific antibody (two different Fab arms); IgG4 Fc with half-life extension modifications → t½ ~4 weeks; SC injection
- **HAVEN-1 (inhibitor HA):** Emicizumab SC QW vs. BPA prophylaxis (APCC; FEIBA): ABR 2.9 vs. 23.3 (p<0.001); 63% zero bleeds [^oldenburg-2017-emicizumab-haven1]; FDA approved November 2017 for inhibitor HA
- **HAVEN-3 (non-inhibitor severe HA):** Emicizumab SC QW vs. no prophylaxis: ABR 1.5 vs. 38.2 (87% reduction); vs. prior FVIII prophylaxis (within-arm cross-over): ABR 1.5 vs. 4.8 (68% reduction) [^mahlangu-2018-emicizumab-haven3]; FDA approved October 2018 for non-inhibitor severe HA; extended to all HA regardless of inhibitor status
- Dosing: 3 mg/kg SC Q1W × 4 (loading) → 1.5 mg/kg Q1W or 3 mg/kg Q2W or 6 mg/kg Q4W (all equivalent maintenance)
- **Key limitation:** DOES NOT replace FVIII for breakthrough bleeds or surgery → still need FVIII (or bypassing agents in inhibitor patients) for acute hemostasis; **AVOID high-dose APCC (>100 IU/kg/day × 24h) with emicizumab** → thrombotic microangiopathy risk (HAVEN-1 signal)

**FVIII replacement (non-inhibitor HA; surgical prophylaxis; breakthrough bleeds):**
- Standard half-life (SHL) rFVIII: Advate, Kogenate, Helixate — t½ ~8-12 h; dosing Q8-12h for continuous prophylaxis
- Extended half-life (EHL) rFVIII: Efanesoctocog alfa (Altuviiio; Sanofi; FDA Apr 2023) — rFVIII fused to XTEN + VWF D'D3 domain → t½ ~96 h; Q1W dosing; XTEND-1 trial: ABR 0.71 (prophylaxis) → first once-weekly FVIII approved; Damoctocog alfa pegol (Jivi) — PEGylated EHL rFVIII; Q2W dosing
- Factor VIII dose formula: FVIII increment (%) = dose (IU) / body weight (kg) × 2; target levels: minor bleeds 30-50%; major bleeds 80-100%; surgery 100% perioperative → 50-80% for 7-14 days

**Inhibitor management:**
- **Immune tolerance induction (ITI):** High-dose FVIII (100-200 IU/kg/day IV) given daily until inhibitor eradicated (<0.6 BU/mL); success rate ~60-70% in high-titer inhibitors; 12-33 months median; now often preceded by rituximab to deplete B cells and shorten ITI duration
- **Bypassing agents (acute bleeding in inhibitor HA with breakthrough bleeds):**
  - APCC (anti-inhibitor coagulant complex; FEIBA; Shire): Activated prothrombin complex concentrate; 50-100 IU/kg Q12h; avoid with emicizumab (TMA risk)
  - Recombinant FVIIa (NovoSeven; Novo Nordisk): 90-270 µg/kg IV bolus Q2-3h; activates TF-FVIIa pathway to generate thrombin despite absent FVIII
- **Fitusiran (anti-antithrombin siRNA; ATLAS-INH trial):** Monthly SC injection; reduces antithrombin (AT) → lowers threshold for thrombin generation → bypasses FVIII; ATLAS-INH: ABR 0 vs. 17.8 vs. BPA on-demand (p<0.001) [^pipe-2023-fitusiran-atlas]; FDA approved 2024 for HA and HB with inhibitors

**Gene therapy:**
- **Valoctocogene roxaparvovec (BMGene-001; BioMarin; FDA Aug 2023):** AAV5-F8-SQ; single IV infusion → hepatocyte FVIII expression; FVIII levels 40-150 IU/dL at 2 years in ~60% of patients; GENEr8-1 trial: ABR reduced from 4.1 to 0.8; durability concern: FVIII levels decline ~50%/year (AAV episomal DNA diluted with hepatocyte proliferation); approved for adults with severe HA without pre-existing AAV5 neutralizing antibodies

## Connections

- `connects-to` → **[Von Willebrand Factor](../../03-molecular/von-willebrand-factor/README.md)** — VWF binds and protects FVIII in plasma → t½ ~12 h (VWF-bound) vs. ~2 h (free); VWF deficiency in VWD type 3 → secondary FVIII <10 IU/dL (resembles mild hemophilia A); VWD type 2N: FVIII-binding domain mutations → FVIII deficiency with normal VWF antigen levels.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — Anti-FVIII inhibitor antibodies are predominantly IgG4 (non-complement-fixing); IgG4 neutralizes FVIII infused as replacement therapy; inhibitor titer (Bethesda units) determines ITI strategy; emicizumab bypasses FVIII → effective despite IgG4 inhibitors.
- `connects-to` → **[Thrombin](../../03-molecular/thrombin/README.md)** — Thrombin cleaves FVIII at Arg372/Arg740/Arg1689 → generates FVIIIa cofactor for intrinsic tenase; APC (thrombomodulin-thrombin product) cleaves FVIIIa at Arg336/Arg562 → inactivation; in HA, extrinsic-pathway thrombin is intact but amplification (intrinsic tenase) fails.
- `connects-to` → **[Protein C](../../03-molecular/protein-c/README.md)** — APC inactivates FVIIIa by cleavage at Arg336 and Arg562; APC + protein S → efficient FVIIIa proteolysis → limits thrombin amplification; FV Leiden co-inheritance with mild HA creates a clinical paradox — APC resistance partially counteracts the hemophilic bleeding tendency.
- `connects-to` → **[Venous Thromboembolism](../../07-system/venous-thromboembolism/README.md)** — Severe HA (FVIII <1%) confers significant VTE protection; historical VTE rate in HA ~0.5/1000 PY vs. ~1.5-3/1000 general population; emicizumab reconstitutes intrinsic tenase; avoid high-dose APCC with emicizumab → TMA; gene therapy raising FVIII >150% increases VTE risk.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — Gene therapy for hemophilia A delivers an AAV-packaged F8 transgene to hepatocytes, which then secrete factor VIII; valoctocogene roxaparvovec raised FVIII toward normal, but expression wanes ~50%/year as episomal AAV DNA dilutes with hepatocyte turnover.
- `connects-to` → **[Antithrombin](../../03-molecular/antithrombin/README.md)** — Fitusiran flips hemophilia A treatment around: instead of replacing factor VIII, this siRNA lowers antithrombin to rebalance hemostasis and restore clotting in FVIII- or FIX-deficient patients, including those with inhibitors; overcorrection risks thrombosis.
- `connects-to` → **[Inherited Thrombophilia](../inherited-thrombophilia/README.md)** — Hemophilia A and inherited thrombophilia are mirror images — too little clotting versus too much; strikingly, co-inheriting factor V Leiden can soften a hemophiliac's bleeding because APC resistance keeps FVa active longer, compensating for the missing factor VIII amplification.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Recurrent hemarthrosis is the defining morbidity of hemophilia A: bleeding into knees, ankles and elbows triggers synovitis, cartilage loss and destructive 'hemophilic arthropathy' → chronic pain and disability; prophylaxis and emicizumab aim to prevent these joint bleeds.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Factor VIII is synthesized largely by liver sinusoidal endothelial cells and circulates protected by endothelial von Willebrand factor; injury exposing the subendothelial matrix starts hemostasis—context for FVIII deficiency, and a target for hemophilia gene therapy.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Hemophilia A spares primary hemostasis—platelets still form the plug—but lacks the FVIIIa/FIXa 'tenase' complex that assembles on the activated platelet surface to burst-generate thrombin; without it the plug is unstable and rebleeds, hence delayed deep-tissue and joint bleeding.
- `connects-to` → **[Disseminated Intravascular Coagulation](../disseminated-intravascular-coagulation/README.md)** — Hemophilia A and DIC cause bleeding by opposite mechanisms: hemophilia is isolated factor VIII deficiency (long aPTT, normal PT and platelets) bleeding into joints, while DIC consumes all factors and platelets at once—the lab pattern tells inherited from acquired.
- `connects-to` → **[Immune Thrombocytopenia](../immune-thrombocytopenia/README.md)** — Hemophilia A and immune thrombocytopenia bleed by different mechanisms: hemophilia is a factor VIII deficit causing deep joint and muscle bleeds, while ITP is platelet destruction causing mucocutaneous petechiae—the pattern hints which arm of hemostasis failed.
- `connects-to` → **[Thrombotic Thrombocytopenic Purpura](../thrombotic-thrombocytopenic-purpura/README.md)** — Hemophilia A and TTP sit at opposite poles of hemostasis: hemophilia fails to clot from factor VIII deficiency and bleeds, while TTP clots pathologically from ADAMTS13 deficiency, consuming platelets in microthrombi—both too little and too much clotting cause disease.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver is central to hemophilia A: hepatocytes make clotting factors, and liver-directed gene therapy now delivers a working factor VIII gene to hepatocytes, enabling them to produce the missing factor—turning the factor-making organ into the cure.
- `connects-to` → **[Stroke](../stroke/README.md)** — Intracranial hemorrhage is the most feared bleed in hemophilia A: deficient factor VIII can't stabilize clots, so brain bleeding is a leading cause of death—hemorrhagic stroke here is the mirror image of the ischemic stroke that clotting disorders cause.
- `connects-to` → **[Antiphospholipid Syndrome](../antiphospholipid-syndrome/README.md)** — Hemophilia A and antiphospholipid syndrome are mirror-image coagulation disorders—bleeding versus clotting: hemophilia lacks factor VIII, while APS has thrombosis-driving antiphospholipid antibodies; an acquired factor VIII inhibitor rarely bridges them.
- `connects-to` → **[Fibrinogen](../../03-molecular/fibrinogen/README.md)** — Hemophilia A spares fibrinogen but fails to reach it: factor VIII deficiency cripples the intrinsic pathway's thrombin burst, so although fibrinogen is normal, too little thrombin forms to convert it to a stable fibrin clot—hence delayed, recurrent bleeding.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Intracranial hemorrhage is the most feared hemophilia A complication: minor head trauma can cause life-threatening brain bleeding because clot formation is delayed, so prophylactic factor replacement and urgent dosing after head injury are central to care.
- `connects-to` → **[Hepatitis C](../hepatitis-c/README.md)** — Hemophilia A is historically tied to hepatitis C and HIV: before viral screening, pooled factor concentrates infected most treated patients with HCV and HIV—a tragedy that drove recombinant factor development, so older hemophiliacs carry a heavy chronic-viral burden.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Hemophilia A is X-linked: the factor VIII gene sits on the X chromosome, so it overwhelmingly affects males while carrier mothers pass it on—making family history, carrier testing, and genetic counseling central to the reproductive side of the disease.
- `connects-to` → **[Immune System](../immune-system/README.md)** — The immune system is hemophilia A's biggest treatment hurdle: some patients form neutralizing antibodies (inhibitors) against infused factor VIII, making replacement fail—so immune tolerance regimens and inhibitor-bypassing agents like emicizumab are needed.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Bleeding in hemophilia A drains red cells: recurrent joint and muscle bleeds, plus dangerous internal hemorrhage, cause iron-deficiency or acute anemia, so falling hemoglobin and the need for transfusion track the severity of uncontrolled bleeding.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium is the silent partner of the clotting cascade hemophilia disrupts: as coagulation Factor IV, calcium ions are needed to assemble the tenase and prothrombinase complexes—so clotting depends on calcium, and citrate that binds it blocks coagulation in stored blood.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — The feared complication of hemophilia A is inhibitors, driven by T-helper cells: in some patients, helper T cells license B cells to make anti-Factor-VIII antibodies that neutralize replacement therapy, forcing bypassing agents or immune tolerance induction.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Repeated joint bleeds in hemophilia damage joints through macrophages: blood in the joint loads synovial macrophages with iron, driving inflammatory synovitis that erodes cartilage—the hemophilic arthropathy that prophylactic factor aims to prevent.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Hemophilia A forms the collagen-triggered platelet plug but can't stabilize it: exposed collagen still recruits platelets into an initial plug, but without factor VIII the secondary fibrin clot never reinforces it, so bleeding restarts hours later.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Hemophilia A's worst complication is immune, needing regulatory T cells: about a third of severe patients make anti-factor-VIII antibodies (inhibitors), and immune tolerance induction works to restore the Tregs that should accept the infused factor.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — Hemophilia A's inhibitors come from B cells: in patients who make anti-factor-VIII antibodies, B cells produce the neutralizing IgG that defeats replacement therapy—so B-cell-depleting rituximab is used to help eradicate stubborn inhibitors.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Hemophilia's joint bleeds leave iron behind: blood pooling in a joint deposits iron as hemosiderin that inflames the synovium and erodes cartilage, driving the crippling hemophilic arthropathy—and repeated bleeds also cause iron-loss anemia.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Hemophilia often bleeds into the urinary tract: painless hematuria is common, and clots can obstruct the ureter, so kidney and bladder bleeding is a recognized, usually self-limited feature managed cautiously to avoid clot retention.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Hemophilia can bleed dangerously into the gut: gastrointestinal hemorrhage, sometimes massive, is a serious complication, so dark or bloody stools in a hemophiliac demand urgent factor replacement and evaluation.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Imaging tracks hemophilia's joint damage: X-ray and MRI photons reveal the arthropathy from repeated bleeds, and radiosynovectomy uses radiation to quiet a chronically bleeding joint.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Hemophilia shows on the skin: easy bruising and large, deep hematomas are often the first sign in a toddler learning to walk, hinting at the clotting defect beneath the surface.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Chronic bleeding taxes the marrow: ongoing blood and iron loss in hemophilia push the bone marrow to ramp up red-cell production to keep pace, and anemia results when the losses outstrip it.
- `connects-to` → **[HIV/AIDS](../hiv-aids/README.md)** — Hemophilia carries a tragic medical legacy: before viral screening and recombinant factor, the pooled plasma concentrates that treated it infected a large share of patients with HIV and hepatitis C, a catastrophe that reshaped blood-product safety.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows why hemophilia's clots fail: lacking factor VIII to drive thrombin, the fibrin mesh forms with fewer, thinner, loosely woven fibers, a fragile structure that cannot hold against ongoing bleeding.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Bleeding into the eye threatens sight in hemophilia: spontaneous or traumatic intraocular and retinal hemorrhages, like bleeds into other closed spaces, can raise pressure and damage vision if not promptly treated with factor replacement.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Hemophilia's bleeds can crush nerves: a deep muscle bleed — the classic iliopsoas hematoma — compresses the femoral nerve into palsy, while an intracranial hemorrhage destroys neurons directly, the most feared complication.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — Hemophilia quietly weakens the skeleton: recurrent joint bleeds destroy cartilage and bone, and reduced activity plus chronic inflammation tip the osteoblast-osteoclast balance toward the low bone density common in these patients.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — Why hemophilia bleeds late, not instantly: the first response to injury — reflex constriction of the vessel's smooth muscle and the platelet plug — is intact, so small cuts seal, but the missing factor VIII fails the later step, letting deep bleeds well up hours afterward.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies are hemophilia's nemesis and its newest cure: inhibitor alloantibodies against infused factor VIII are the dreaded complication that neutralizes treatment, while emicizumab, a bispecific antibody bridging factors IXa and X, now prevents bleeds without it.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — A deep bleed can crush a nerve: a tense hematoma in the iliopsoas or forearm compresses the peripheral nerve running through it, causing a compartment syndrome with numbness, weakness, and palsy that needs urgent factor replacement.
- `connects-to` → **[Hepatitis B](../hepatitis-b/README.md)** — The old treatment carried hidden viruses: before viral inactivation, plasma-derived factor VIII concentrates transmitted hepatitis B and C and HIV to a generation of patients, a tragedy that drove the shift to recombinant factor and vaccination.
- `connects-to` → **[Osteoclast](../../04-cellular/osteoclast/README.md)** — Bleeding into joints destroys them: recurrent hemarthrosis dumps iron and inflammation into the joint, driving osteoclasts to erode bone and cartilage into the crippling hemophilic arthropathy that defines untreated disease.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Hemophilia thins the skeleton: the pain and arthropathy that limit weight-bearing exercise, plus the disease itself, leave people with hemophilia with reduced bone density and a higher fracture risk than the general population.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — The immune system can reject the treatment: in some patients dendritic cells present infused factor VIII as foreign, priming the neutralizing antibodies (inhibitors) that are the most challenging complication of replacement therapy.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Repeated joint bleeds wreck the joint: blood in the synovium drives a fibroblast-led hypertrophy and fibrosis that, with iron-laden inflammation, destroys cartilage into the crippling hemophilic arthropathy that defines the disease's burden.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Gene therapy meets the immune system: the AAV vector delivering a working factor VIII gene to liver cells can draw cytotoxic T cells that attack the transduced hepatocytes, an immune response that can erode the durability of the one-time cure.
- `connects-to` → **[Iron Deficiency Anemia](../iron-deficiency-anemia/README.md)** — Chronic blood loss drains iron: beyond dramatic joint and muscle bleeds, mucosal and gastrointestinal bleeding in hemophilia steadily depletes iron stores, leaving many patients with a superimposed iron deficiency anemia.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Blood in the joint turns on inflammation: iron and breakdown products from recurrent hemarthroses activate NF-κB in synovial cells, switching on the inflammatory and angiogenic genes that drive the chronic synovitis of hemophilic arthropathy.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Beyond blood loss, inflammation suppresses the marrow: the chronic synovitis of hemophilic arthropathy raises inflammatory cytokines that blunt erythropoiesis, an anemia of chronic disease distinct from the iron loss of bleeding.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — The lines used to infuse factor can seed infection: many patients, especially children, rely on indwelling central venous ports for clotting-factor delivery, and these catheters are a recurring source of bloodstream infection and sepsis.
- `connects-to` → **[Opioid Use Disorder](../opioid-use-disorder/README.md)** — Crippled joints drive long-term opioid use: the recurrent hemarthroses of hemophilia destroy joints into a painful arthropathy, and the chronic pain often leads to sustained opioid use with its risk of dependence.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A lifelong disease with a heavy history weighs on mood: chronic pain, disability, and for older patients the trauma of transfusion-acquired HIV and hepatitis C give hemophilia A a high burden of depression.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Aging hemophiliacs now meet heart disease: with near-normal lifespans, older patients develop coronary disease and heart failure, whose antithrombotic management is a delicate balance against their underlying bleeding tendency.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Bleeds compress nerves and wreck joints: hematomas pressing on peripheral nerves and the chronic hemophilic arthropathy from recurrent hemarthrosis generate persistent neuropathic and nociceptive pain in hemophilia A.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — The kidneys both bleed and decline: recurrent hematuria is common in hemophilia, and aging patients — many with prior HIV or hepatitis C from old factor concentrates — face rising rates of hypertension and chronic kidney disease.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — Blood pressure runs high in this population: hemophilia A patients show a higher prevalence of hypertension than the general population, compounding the bleeding risk of any intracranial event.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Without clotting, wounds bleed instead of healing: deficient factor VIII leaves the clot unstable, so any surgery or injury in hemophilia A re-bleeds, and procedures demand factor replacement to allow healing.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It bleeds into the gut: gastrointestinal haemorrhage is a recognised bleeding site in hemophilia A, where even a minor mucosal lesion or ulcer can cause prolonged, dangerous blood loss.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Living one bleed away from danger breeds worry: the lifelong unpredictability of spontaneous bleeds, joint damage and the vigilance hemophilia A demands foster chronic health anxiety alongside depression.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Its most lethal bleeds are in the brain: intracranial and intraspinal haemorrhage are the leading causes of death in hemophilia A, while deep haematomas can compress peripheral nerves.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It bleeds into the urinary tract: spontaneous haematuria is common in hemophilia A, usually self-limiting but distressing, and clot colic or retention can follow heavy bleeding.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It shows beneath the skin: easy bruising, large spreading ecchymoses and soft-tissue haematomas after minor trauma are among the earliest visible signs of hemophilia A.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Bleeding can block the airway: retropharyngeal and neck haematomas in hemophilia A can obstruct the airway — a bleeding emergency — and haemothorax can occur with chest trauma.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Longer life brings a treatment dilemma: as patients with hemophilia A now age into coronary disease and atrial fibrillation, the antiplatelet and anticoagulant therapy they need is hazardous given their bleeding tendency.
- `connects-to` → **[Ibuprofen](../../../03-medicine/01-modern/12-anti-inflammatory/ibuprofen/README.md)** — A common painkiller is off-limits: NSAIDs like ibuprofen are avoided in hemophilia because they impair platelet function and irritate the gut, compounding the bleeding risk.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — New drugs bypass the missing factor: the bispecific antibody emicizumab mimics factor VIII, and gene therapy delivering an FVIII gene now offers durable correction in haemophilia A.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — A tragic legacy in the lymphoid system: before viral inactivation, pooled factor concentrates transmitted HIV and hepatitis C to many haemophilia patients, with downstream AIDS-related lymphomas.
- `connects-to` → **[Prion Protein](../../../02-pathogen/05-prions/prion-protein/README.md)** — A feared transfusion legacy: plasma-derived clotting products carried a theoretical variant-CJD prion risk in the UK, prompting recipient notification and a shift to recombinant factor VIII.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Bleeding wrecks joints and bone: recurrent haemarthroses drive hemophilic arthropathy with cartilage and subchondral-bone destruction, and reduced mobility plus chronic disease leave many patients with low bone density and fractures.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — The liver makes its missing factor: factor VIII is produced largely by liver sinusoidal endothelial cells, which is why AAV gene therapy for hemophilia A delivers a working FVIII gene to the hepatocytes of the lobule for durable endogenous production.
- `connects-to` → **[Sickle Cell Disease](../sickle-cell-disease/README.md)** — A contrasting inherited blood disorder: hemophilia A is an X-linked clotting-factor deficiency causing bleeding, while sickle cell is a recessive haemoglobinopathy causing vaso-occlusion — both inherited and both now targets of gene therapy.
- `connects-to` → **[Heparin-Induced Thrombocytopenia](../heparin-induced-thrombocytopenia/README.md)** — Opposite poles of haemostasis: haemophilia A bleeds from absent factor VIII, while heparin-induced thrombocytopenia paradoxically clots despite falling platelets—two disorders that frame the balance between bleeding and thrombosis.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Acquired haemophilia is autoimmune: autoantibodies against factor VIII can arise in autoimmune disease such as rheumatoid arthritis (and postpartum), causing sudden bleeding distinct from the inherited X-linked deficiency.
- `connects-to` → **[DLBCL](../dlbcl/README.md)** — New bleeding can flag a hidden cancer: acquired haemophilia A from anti-factor-VIII autoantibodies is often paraneoplastic, classically with lymphoproliferative disorders like diffuse large B-cell lymphoma, so unexplained bleeding in an older adult warrants a malignancy search.
- `connects-to` → **[HCC](../hcc/README.md)** — The transfusion-era legacy: hepatitis C from contaminated clotting-factor concentrates gave a generation of haemophilia patients chronic liver disease, cirrhosis and hepatocellular carcinoma, still a leading cause of death.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Where inhibitors are born: the anti-factor-VIII alloantibodies that defeat replacement therapy are class-switched and affinity-matured by B cells in germinal centres, the central immunological problem of haemophilia care.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — A paradoxical protection: the lifelong hypocoagulable state of haemophilia lowers the risk of arterial thrombosis, so atherosclerotic plaques in the arterial wall less often trigger heart attacks and ischaemic strokes.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — Acquired haemophilia: autoantibodies against Factor VIII can arise paraneoplastically with solid tumours like breast cancer (and with lymphoma or postpartum), causing sudden severe bleeding in a previously normal person.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — Renal bleeding: spontaneous haematuria is common in haemophilia, blood passing from the kidney through the glomerulus and urinary tract, where antifibrinolytics are avoided lest clots obstruct the ureter.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — An anticoagulation paradox: COVID-19's prothrombotic state complicates haemophilia management, balancing thromboprophylaxis against the underlying bleeding tendency, while the pandemic disrupted factor-replacement care.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — Joint destruction: recurrent haemarthrosis in haemophilia drives RANKL-mediated bone and cartilage resorption, the basis of the crippling hemophilic arthropathy.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Iron-driven synovitis: blood and iron deposited in joints by repeated bleeds trigger TNF-α-rich synovial inflammation that perpetuates hemophilic joint damage.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Synovial neovascularisation: VEGF-driven new-vessel growth in the iron-laden hemophilic synovium creates fragile vessels that rebleed, perpetuating the cycle of joint destruction.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Cartilage breakdown: IL-1β released after recurrent hemarthrosis drives chondrocyte matrix-metalloproteinase production, degrading articular cartilage in hemophilic arthropathy independent of the synovial inflammation.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — Synovial hyperplasia: PDGF from activated platelets and macrophages after joint bleeds stimulates fibroblast and synoviocyte proliferation, thickening the hemophilic synovium toward chronic destructive disease.
- `connects-to` → **[TGF-beta](../../03-molecular/tgf-beta/README.md)** — Joint fibrosis: TGF-beta drives the fibrotic remodelling and contracture of chronically bled hemophilic joints, converting recurrent hemarthrosis into fixed deformity and stiffness.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — CCL2 released after hemarthrosis draws monocytes and macrophages into the hemophilic synovium, building the inflammatory infiltrate that perpetuates the proliferative synovitis of target joints between bleeds.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — The hypertrophic, iron-laden hemophilic synovium becomes hypoxic, stabilizing HIF-1α to drive the fragile neovascularization that predisposes the target joint to the repeated rebleeding that perpetuates the arthropathy.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — Heme and iron from repeated joint bleeds act as DAMPs on TLR4, igniting the innate inflammatory cascade that converts an acute hemarthrosis into the self-sustaining chronic synovitis of hemophilic arthropathy.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — Repeated hemarthrosis drives angiopoietin- and VEGF-dependent growth of fragile, leaky new vessels in the hemophilic synovium, which rebleed easily and lock the joint into a self-perpetuating cycle of bleeding and arthropathy.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Direct exposure of cartilage to blood triggers caspase-3-mediated chondrocyte apoptosis, a key mechanism by which recurrent joint bleeds degrade articular cartilage and produce the irreversible hemophilic arthropathy.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — IL-6 generated in the iron-laden hemophilic synovium amplifies the chronic inflammatory synovitis that follows recurrent bleeds, contributing to the proliferative pannus that erodes the joint.
- `connects-to` → **[Interleukin-10](../../03-molecular/il-10/README.md)** — Regulatory IL-10 and regulatory T cells (already mapped) mediate immune tolerance to factor VIII, and their failure permits the neutralizing-antibody inhibitors that are the major complication of hemophilia A therapy.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Repeated joint bleeds deposit iron (already mapped) that activates the NLRP3 inflammasome and IL-1β in the synovium, driving the chronic synovitis and progressive hemophilic arthropathy.
- `connects-to` → **[Ferroportin](../../03-molecular/ferroportin/README.md)** — Recurrent hemarthroses overwhelm macrophage iron export through ferroportin, leaving hemosiderin deposits in the synovium that perpetuate the inflammatory and oxidative damage of hemophilic arthropathy.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — Blood in the joint drives synovial macrophages to release S100A8/A9 (calprotectin), amplifying the inflammatory synovitis that destroys cartilage in hemophilic arthropathy.
- `connects-to` → **[FcRn](../../03-molecular/fcrn/README.md)** — The neonatal Fc receptor extends the half-life of Fc-fused factor VIII concentrates (efmoroctocog) and recycles IgG, including the inhibitor antibodies (anti-FVIII) that complicate hemophilia A therapy.
- `connects-to` → **[CTLA-4](../../03-molecular/ctla-4/README.md)** — Development of anti-FVIII inhibitor antibodies reflects loss of immune tolerance, and CTLA-4-dependent regulatory mechanisms underlie the immune-tolerance-induction protocols used to eradicate them.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — Iron and blood-breakdown products in the hemophilic joint activate TLR-MyD88-NF-κB signaling (TLR4 and NF-κB already mapped), driving the chronic synovitis of recurrent hemarthrosis.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — IL-6-JAK-STAT signaling (IL-6 already mapped) sustains the inflammatory synovitis that progresses to destructive hemophilic arthropathy.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling drives the synovial proliferation and neoangiogenesis (VEGF already mapped) of the hypertrophic synovium in hemophilic arthropathy.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 amplifies the iron-driven synovial inflammation that drives the chronic synovitis of hemophilic arthropathy after recurrent hemarthrosis.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β already mapped) drives the joint fibrosis and cartilage degradation of the hemophilic arthropathy that follows repeated bleeds.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling transduces the inflammatory cytokine milieu of the hypertrophic synovium in hemophilic arthropathy.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO regulates the chondrocyte and synovial oxidative-stress response to the iron-driven joint degeneration of hemophilic arthropathy.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the T-helper response that governs anti-factor-VIII inhibitor antibody development in hemophilia A.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Hemarthrosis-derived cytosolic and mitochondrial DNA engages cGAS-STING, contributing to the chronic synovial inflammation of hemophilic arthropathy.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT signaling in synovial and endothelial cells participates in the blood-induced synovitis and neoangiogenesis of hemophilic arthropathy.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the inflammatory and iron-driven signaling of the recurrent hemarthrosis and synovial damage of hemophilia A.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-bearing cytotoxic lymphocytes participate in the immune response to factor-VIII replacement that can drive inhibitor development in hemophilia A.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) participates in the synovial and inflammatory responses of the hemophilic arthropathy of hemophilia A.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR signaling in the iron-laden synovium participates in the joint inflammation of hemophilic arthropathy in hemophilia A.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the synovitis and osteoclast-driven bone erosion of hemophilic arthropathy in hemophilia A.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte recruitment participates in the anti-factor-VIII immune response and hemophilic-arthropathy synovitis of hemophilia A.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the immune response to factor VIII in hemophilia A.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the synovial angiogenesis and leukocyte recruitment of hemophilic arthropathy in hemophilia A.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the immune response contributing to the anti-FVIII inhibitor formation of hemophilia A.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the immune activation influencing the anti-FVIII inhibitor response of hemophilia A.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the T-cell help driving the anti-FVIII inhibitor formation (a target of immune-tolerance induction) of hemophilia A.
- `connects-to` → **[Type I Interferon](../../03-molecular/type-i-interferon/README.md)** — Gene-therapy barrier: AAV gene therapy delivering a factor VIII transgene to the liver triggers innate type I interferon and adaptive responses against the capsid, the immune hurdle that limits durable expression and drives the corticosteroid prophylaxis used with these vectors.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Blood-loss anaemia: recurrent and sometimes occult bleeding in hemophilia A causes chronic blood loss that lowers haemoglobin, producing an iron-deficiency anaemia that compounds the disability and can require transfusion in severe bleeds.
- `connects-to` → **[Mu-opioid receptor](../../03-molecular/mu-opioid-receptor/README.md)** — Chronic pain: the progressive hemophilic arthropathy from repeated joint bleeds causes chronic pain frequently managed with opioids acting on the mu-opioid receptor, a persistent burden and dependence risk in the aging hemophilia population.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Inhibitor immunology: development of neutralising anti-factor-VIII antibodies (inhibitors; IgG already mapped) depends on MHC class II presentation of factor VIII peptides to helper T cells, and HLA type influences the risk of this major treatment complication.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Tolerance and gene therapy: IL-2-driven T-cell responses shape both the immune-tolerance induction used to eradicate inhibitors and the immune reaction to the AAV vector and transgene in the liver-directed gene therapy (liver already mapped).
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Th2 antibody help: IL-4 and type-2 T-cell help drive the B-cell production of anti-factor-VIII inhibitors (immunoglobulin G already mapped), so the Th2 axis contributes to the alloimmune response that complicates factor replacement.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Haemophilic synovitis: prostaglandins from the inflamed synovium of recurrent haemarthrosis drive the pain and inflammation of haemophilic arthropathy, though NSAIDs are used cautiously given the bleeding risk.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Iron-catalysed joint oxidation: the iron deposited in the joint from repeated bleeds (ferroportin already mapped) catalyses reactive oxygen species, to which xanthine oxidase contributes, driving the synovial proliferation and cartilage damage of haemophilic arthropathy.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 cytokine axis: IL-13, with IL-4 (already mapped), completes the type-2 cytokine support for the B-cell inhibitor response, part of the alloimmune reaction against replacement factor VIII.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Coagulation factor IV: calcium is factor IV, an essential cofactor that anchors the clotting factors to membranes at the tenase and prothrombinase complexes (thrombin already mapped) where the missing factor VIII normally accelerates fibrin formation in haemophilia A.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — Th17 inhibitor immunity: the IL-17-producing helper T cells, with the type-2 IL-4 and IL-13 (already mapped), support the B-cell (already mapped) alloantibody response that produces the factor VIII inhibitors of haemophilia A.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Vascular and joint microenvironment: nitric oxide regulates the vascular tone and, in the iron-laden (already mapped) haemophilic joint, contributes to the synovial vascular changes and inflammation of the arthropathy.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Immune tolerance: the PD-1 checkpoint and the peripheral tolerance mechanisms are relevant to the immune-tolerance induction used to eradicate the factor VIII inhibitors (immunoglobulin already mapped) of haemophilia A.
- `connects-to` → **[Regulatory T cell](../../04-cellular/regulatory-t-cell/README.md)** — Tolerance induction: the regulatory T cells are central to the immune-tolerance induction that re-establishes tolerance to factor VIII and eradicates the alloantibody inhibitors of haemophilia A.
- `connects-to` → **[BAFF](../../03-molecular/baff/README.md)** — Inhibitor B-cell survival: BAFF supports the survival of the alloreactive B cells (already mapped) that produce the factor VIII inhibitors, part of the humoral response that complicates haemophilia A replacement therapy.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Bleeding iron balance: the recurrent bleeding and the anaemia (haemoglobin already mapped) of haemophilia A interact with the iron-regulatory hepcidin and the ferroportin (already mapped) iron export.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Metabolic-arthropathy adipokine: leptin is the adipokine of the marrow and synovial adipose signalling in the arthropathy and the immune-metabolic milieu of haemophilia A.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic milieu of haemophilia A.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the synovial and metabolic milieu of the haemophilic arthropathy.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 inhibitor immunity: the IFN-γ of the T-helper cells (already mapped) is the type-II interferon arm of the anti-FVIII alloantibody (immunoglobulin already mapped) inhibitor response of haemophilia A.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune response that drives the FVIII-inhibitor formation in haemophilia A.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the T-helper (already mapped) response to the infused FVIII in haemophilia A.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune response to the FVIII in haemophilia A.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2/anaphylaxis arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), can develop against the infused factor and underlies the rare anaphylactic reactions in haemophilia A.
- `connects-to` → **[Plasma cell](../../04-cellular/plasma-cell/README.md)** — Inhibitor source: the plasma cells, downstream of the B cells (already mapped), secrete the anti-FVIII inhibitor antibodies (immunoglobulin already mapped) that neutralise the infused factor in haemophilia A.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Anaphylaxis effector: the mast cells, armed with the anti-factor IgE (already mapped), are the effectors of the rare anaphylactic reactions to the infused FVIII in haemophilia A.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Gene-therapy complement: the complement C5 and its activation (with C3 already mapped) are part of the innate response to the AAV vector of the FVIII gene therapy of haemophilia A.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) links the complement to the innate inflammatory response to the AAV vector of the FVIII gene therapy of haemophilia A.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the innate response to the AAV vector of the FVIII gene therapy of haemophilia A.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Bleeding iron loss: transferrin, the iron carrier, reflects the disordered iron handling (ferroportin and hepcidin already mapped) of the iron-deficiency anaemia from the recurrent bleeding of haemophilia A.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Haemostatic barrier alarmin: TSLP, released from the vascular endothelium (already mapped) and connective tissue at trauma sites, modulates mast-cell (already mapped) and dendritic-cell (already mapped) immune responses at the bleeding sites of haemophilia A.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Contact-kinin amplifier: bradykinin, generated by the contact activation pathway, amplifies vascular permeability and the pain response at the haemarthrosis and soft-tissue haematoma sites of haemophilia A.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Anaemia axis: erythropoietin, secreted by the kidney (already mapped) in response to the recurrent bleeding-associated iron-deficiency anaemia (already mapped) of haemophilia A, drives the compensatory erythropoiesis of the disease.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Contact-kinin regulation: the C1-esterase inhibitor limits the classical complement and contact-kinin (bradykinin already mapped) cascades activated by recurrent haemarthrosis and soft-tissue haematoma, moderating the inflammatory joint damage of haemophilia A.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell haemarthrosis mediator: histamine, released by mast cells (already mapped) at haemarthrosis sites in haemophilia A, amplifies the local vascular permeability and inflammatory cytokine signalling (IL-1 and TNF already mapped) of the haemophilic joint.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Synovial ECM remodelling: periostin, induced by TGF-β (already mapped) in the synovial fibroblasts (already mapped) after recurrent haemarthrosis, contributes to the cartilage destruction and the chronic haemophilic arthropathy of haemophilia A.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — HA melatonin: melatonin suppresses TNF-α (already mapped) and IL-6 (already mapped) driven synovial inflammation in haemophilic arthropathy; melatonin also reduces macrophage (already mapped) activation and attenuates the cortical-bone (already mapped) erosion cascade.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — HA testosterone: androgen receptor signalling modulates platelet (already mapped) and thrombin (already mapped) activity in haemophilia A; testosterone also drives macrophage (already mapped) and B-cell (already mapped) activity in the inhibitor-development cascade.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — HA serotonin: platelet (already mapped) serotonin release modulates thrombin (already mapped) generation in haemophilia A; 5-HT2A on endothelial cells (already mapped) amplifies the TNF-α (already mapped) and IL-6 (already mapped) joint inflammatory cascade.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — HA oxytocin: oxytocin promotes VWF (already mapped) release and platelet (already mapped) aggregation via endothelial cell (already mapped) V1 receptors; oxytocin-driven NF-κB (already mapped) attenuation reduces macrophage (already mapped) synovial inflammation in arthropathy.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — HA vasopressin: DDAVP (synthetic AVP) triggers VWF (already mapped) and factor VIII release from endothelial cells (already mapped); V2 receptor signalling mobilises platelet (already mapped) cofactors and modulates NF-κB (already mapped) haemostatic inflammation.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — HA prolactin: prolactin signalling on B-cells (already mapped) amplifies anti-FVIII inhibitor development; prolactin-driven NF-κB (already mapped) activation promotes macrophage (already mapped) synovial inflammation and thrombin (already mapped) dysregulation in arthropathy.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — HA zinc: zinc cofactors hepatocyte (already mapped) coagulation-protein synthesis and macrophage (already mapped) function; zinc deficiency amplifies NF-κB (already mapped) inhibitor development and impairs thrombin (already mapped) and platelet (already mapped) haemostasis.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — HA selenium: selenium, via GPx in endothelial cells (already mapped), scavenges haemostatic ROS; selenium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) inflammation and impairs VWF (already mapped) and thrombin (already mapped) generation in HA.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — HA iodine: iodine-dependent thyroid hormones modulate hepatocyte (already mapped) coagulation-protein synthesis; iodine deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and impairs thrombin (already mapped) and VWF (already mapped) generation in HA.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — HA sodium: high dietary sodium promotes endothelial cell (already mapped) activation and macrophage (already mapped) inflammation; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) amplifies haemostatic impairment and thrombin (already mapped) dysfunction in HA.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — HA magnesium: magnesium cofactors hepatocyte (already mapped) coagulation-protein synthesis and endothelial cell (already mapped) function; magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and impairs thrombin (already mapped) generation in HA.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — HA chloride: chloride channels regulate hepatocyte (already mapped) and endothelial cell (already mapped) volume and ion homeostasis; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and impairs thrombin (already mapped) generation in HA.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — HA nitrogen: nitrogen as backbone of coagulation proteins and cytokines (already mapped) sustains haemostatic signalling; nitrogen-derived RNS from macrophages (already mapped) amplifies NF-κB (already mapped) and IL-6 (already mapped) inflammatory bleeding cascade in HA.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — HA phosphorus: phosphorus as ATP in hepatocytes (already mapped) and endothelial cells (already mapped) fuels coagulation-protein synthesis; phosphorus dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and impairs thrombin (already mapped) in HA.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — HA carbon: carbon in nucleotides of hepatocytes (already mapped) and endothelial cells (already mapped) fuels coagulation-factor biosynthesis; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and impairs thrombin (already mapped) generation in HA.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — HA copper: copper cofactors ceruloplasmin and lysyl oxidase in hepatocytes (already mapped) and endothelial cells (already mapped) support coagulation matrix; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and impairs thrombin (already mapped) in HA.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — HA hydrogen: hydrogen via ROS from macrophages (already mapped) and endothelial cells (already mapped) modulates haemostatic redox homeostasis; hydrogen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and impairs thrombin (already mapped) generation in HA.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — HA GLP-1: GLP-1 from gut L-cells (already mapped) and macrophages (already mapped) modulates haemophilia metabolic homeostasis; GLP-1 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) inflammatory cascade of haemophilia A.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — HA angiotensin-II: Angiotensin-II in endothelium (already mapped) and macrophages (already mapped) promotes vascular remodelling in haemophilia A; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) haemophilic cascade.
- `connects-to` → **[Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — HA Wnt/β-catenin: Wnt/β-catenin in synoviocytes (already mapped) and macrophages (already mapped) drives haemophilic arthropathy; Wnt dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) haemophilic arthropathy cascade.

[^oldenburg-2017-emicizumab-haven1]: Oldenburg J, Mahlangu JN, Kim B, et al. Emicizumab prophylaxis in hemophilia A with inhibitors. *N Engl J Med.* 2017;377(9):809-818. [doi:10.1056/NEJMoa1703068](https://doi.org/10.1056/NEJMoa1703068) · [PubMed 28691557](https://pubmed.ncbi.nlm.nih.gov/28691557/)
[^mahlangu-2018-emicizumab-haven3]: Mahlangu J, Oldenburg J, Paz-Priel I, et al. Emicizumab prophylaxis in patients who have hemophilia A without inhibitors. *N Engl J Med.* 2018;379(9):811-822. [doi:10.1056/NEJMoa1803550](https://doi.org/10.1056/NEJMoa1803550) · [PubMed 30157389](https://pubmed.ncbi.nlm.nih.gov/30157389/)
[^pipe-2023-fitusiran-atlas]: Pipe SW, Leebeek FW, Recht M, et al. Once-monthly subcutaneous fitusiran versus on-demand bypassing agent for haemophilia A or B with inhibitors (ATLAS-INH). *Lancet.* 2023;401(10386):1427-1439. [doi:10.1016/S0140-6736(23)00284-2](https://doi.org/10.1016/S0140-6736(23)00284-2) · [PubMed 37003297](https://pubmed.ncbi.nlm.nih.gov/37003297/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
