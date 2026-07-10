---
schema: human-scale-entry/v1
id: thrombotic-thrombocytopenic-purpura
name: Thrombotic Thrombocytopenic Purpura
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "TTP is a life-threatening TMA caused by ADAMTS13 deficiency (<10%); ULVWF-platelet microthrombi → MAHA + thrombocytopenia + end-organ ischemia. Caplacizumab (anti-VWF; FDA 2019) + plasma exchange + rituximab is current first-line; untreated mortality ~90%."
aliases: ["TTP", "thrombotic thrombocytopenic purpura", "iTTP", "immune TTP", "Upshaw-Schulman syndrome", "congenital TTP", "hereditary TTP", "thrombotic microangiopathy TTP", "MAHA TTP"]
sources:
  - id: scully-2019-caplacizumab-hercules
    type: peer-reviewed
    cite: "Scully M, Cataland SR, Peyvandi F, et al. Caplacizumab treatment for acquired thrombotic thrombocytopenic purpura. N Engl J Med. 2019;380(4):335-346."
    doi: "10.1056/NEJMoa1806311"
    pmid: "30625070"
    url: "https://doi.org/10.1056/NEJMoa1806311"
  - id: george-2010-ttp-review
    type: peer-reviewed
    cite: "George JN. Clinical practice. Thrombotic thrombocytopenic purpura. N Engl J Med. 2006;354(18):1927-1935."
    doi: "10.1056/NEJMcp053024"
    pmid: "16672704"
    url: "https://doi.org/10.1056/NEJMcp053024"
  - id: coppo-2019-rituximab-ttp
    type: peer-reviewed
    cite: "Coppo P, Busson M, Veyradier A, et al. HLA-DRB1*11: a strong risk factor for acquired severe ADAMTS13 deficiency-related thrombotic thrombocytopenic purpura in Caucasians. J Thromb Haemost. 2010;8(11):2466-2469."
    doi: "10.1111/j.1538-7836.2010.04028.x"
    pmid: "20735727"
    url: "https://doi.org/10.1111/j.1538-7836.2010.04028.x"
cross_links:
  - target: 01-human/03-molecular/adamts13
    relation: connects-to
    note: "ADAMTS13 deficiency (<10% activity) is the defining pathophysiology of TTP; acquired iTTP: anti-ADAMTS13 IgG4 antibodies; hereditary Upshaw-Schulman syndrome: ADAMTS13 biallelic mutations; caplacizumab blocks VWF A1 domain → prevents ULVWF-platelet binding."
  - target: 01-human/03-molecular/von-willebrand-factor
    relation: connects-to
    note: "ULVWF from Weibel-Palade bodies accumulates in TTP (ADAMTS13 deficiency) → GPIb-mediated platelet aggregation → microthrombi; caplacizumab (anti-VWF A1 nanobody; FDA 2019) blocks ULVWF-platelet tethering → fastest reversal of acute microthrombus formation."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Anti-ADAMTS13 autoantibodies are predominantly IgG4 (inhibiting spacer domain) in iTTP; IgG1 non-inhibiting antibodies accelerate ADAMTS13 clearance; rituximab (anti-CD20) depletes antibody-producing B cells → ADAMTS13 recovery; anti-ADAMTS13 IgG titer guides therapy duration."
  - target: 01-human/07-system/ahus
    relation: connects-to
    note: "TTP (ADAMTS13 <10%) and aHUS (complement gene mutations; ADAMTS13 ≥10%) are the two most important complement/coagulation TMAs: both cause MAHA + thrombocytopenia + AKI; TTP is treated with PEX + caplacizumab + rituximab; aHUS with eculizumab — never interchange these therapies."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "ULVWF binds GPIbα on platelets → platelet-rich microthrombi in arterioles/capillaries → consumption; thrombocytopenia <30,000/μL is characteristic; caplacizumab blocks ULVWF-GPIbα → fastest microthrombus resolution; platelet count >150,000/μL × 2 days marks clinical remission."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "ULVWF-platelet microthrombi → ischemic endothelial injury → local C3 deposition; refractory iTTP shows elevated sC5b-9; TTP-aHUS overlap responds to eculizumab + PEX; C3d/sC5b-9 studied as TTP severity biomarkers; complement distinguishes refractory TTP from typical iTTP."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Endothelial Weibel-Palade bodies store ULVWF; endothelial activation → ULVWF secretion → ADAMTS13 normally cleaves; TTP: ADAMTS13 failure → ULVWF accumulates on endothelial surface → platelet tethering; endothelial injury from microthrombi → ULVWF release → amplification loop."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "The kidney is a TTP target organ: VWF-platelet microthrombi lodge in the renal microvasculature, causing acute kidney injury — usually milder than in aHUS, where renal failure dominates; this difference in renal severity helps separate the two thrombotic microangiopathies."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Neurologic involvement is TTP's most dangerous feature: cerebral microthrombi cause fluctuating confusion, headache, focal deficits, seizures, or coma — part of the classic pentad — that can come and go within hours, so suspected TTP needs urgent plasma exchange."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "TTP shears red cells: as erythrocytes squeeze through platelet-rich microthrombi they fragment into schistocytes, producing microangiopathic hemolytic anemia with high LDH, low haptoglobin, negative Coombs — schistocytes plus thrombocytopenia trigger ADAMTS13 testing."
  - target: 01-human/07-system/immune-thrombocytopenia
    relation: connects-to
    note: "TTP and immune thrombocytopenia both cause severe thrombocytopenia but differ: ITP is antibody-mediated platelet destruction without hemolysis, while TTP adds microangiopathic hemolysis and organ ischemia from ADAMTS13 deficiency—an emergency needing plasma exchange."
  - target: 01-human/07-system/disseminated-intravascular-coagulation
    relation: connects-to
    note: "TTP and DIC both produce thrombocytopenia and schistocytes but are distinguished by coagulation tests: DIC consumes clotting factors and prolongs PT/PTT with high D-dimer, while TTP leaves coagulation times normal—because its clots are platelet-VWF, not fibrin."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "Lupus can trigger or mimic TTP: SLE may produce acquired ADAMTS13 deficiency or a TTP-like thrombotic microangiopathy, and the two share features (hemolysis, low platelets, neuro/renal signs), so a lupus flare with schistocytes demands urgent ADAMTS13 testing."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "TTP can present as stroke: ADAMTS13 deficiency lets VWF-platelet microthrombi lodge in the cerebral microvasculature, causing fluctuating confusion and focal deficits—so an unexplained stroke with thrombocytopenia and hemolysis should trigger urgent TTP work-up."
  - target: 01-human/07-system/antiphospholipid-syndrome
    relation: connects-to
    note: "TTP and catastrophic antiphospholipid syndrome are both thrombotic microangiopathies occluding small vessels: TTP from ADAMTS13 deficiency, CAPS from antiphospholipid antibodies—overlapping clinically, so antibody testing helps separate these emergencies."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "HIV is a recognized cause of secondary TTP: the infection can trigger ADAMTS13 autoantibodies, producing thrombotic microangiopathy—so a new TTP diagnosis warrants HIV testing, and antiretroviral therapy plus plasma exchange treats the HIV-associated form."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Plasma cells make the anti-ADAMTS13 antibody behind acquired TTP: long-lived autoantibody-secreting cells block the enzyme that cleaves von Willebrand factor, so giant VWF multimers clump platelets—why plasma exchange (removing antibody) and rituximab treat TTP."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "The heart is a major, underrecognized TTP target: microthrombi in coronary microvasculature cause troponin rise, arrhythmia and sudden death, so cardiac involvement is a leading cause of TTP mortality—reason to start plasma exchange urgently on suspicion."
  - target: 01-human/03-molecular/thrombin
    relation: connects-to
    note: "TTP clots without activating thrombin: unlike DIC, the microthrombi are platelet-VWF aggregates formed without triggering the coagulation cascade, so thrombin generation and clotting times stay normal—distinguishing it from consumptive coagulopathy."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Acquired TTP is autoantibody-driven, so B cells are a treatment target: rituximab (anti-CD20) depletes the B cells making anti-ADAMTS13 antibodies, raising enzyme levels, preventing relapse, and increasingly used upfront alongside plasma exchange."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Most TTP is autoimmune: the immune system generates IgG autoantibodies against ADAMTS13, crippling the enzyme that cleaves von Willebrand factor—so unchecked VWF multimers trigger platelet microthrombi, distinguishing acquired TTP from the hereditary enzyme deficiency."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "The spleen links to TTP through antibody handling: its reticuloendothelial cells clear autoantibody-coated platelets and produce immunoglobulin, and historically splenectomy was used for refractory or relapsing immune TTP before rituximab became standard."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "Acquired TTP is treated by depleting B cells via CD20: rituximab, an anti-CD20 antibody, removes the B cells making anti-ADAMTS13 autoantibodies, reducing relapse alongside plasma exchange and the anti-vWF nanobody caplacizumab."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "Pregnancy can precipitate TTP: ADAMTS13 activity falls naturally in pregnancy, unmasking congenital deficiency or triggering acquired TTP, so it must be distinguished from preeclampsia and HELLP—a diagnostic challenge with very different treatments."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Acquired TTP is an autoimmune disease needing T-cell help: helper T cells recognizing ADAMTS13 drive B cells to make the inhibitory autoantibodies, so the disorder reflects a breakdown of tolerance to the body's own vWF-cleaving enzyme."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "TTP shreds red cells and spills hemoglobin: platelet-vWF microthrombi slice passing red cells (microangiopathic hemolysis), producing schistocytes, free hemoglobin, low haptoglobin and high LDH—the lab fingerprint that flags the emergency."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Treating TTP with plasma exchange drains calcium: the citrate anticoagulant in the apheresis circuit binds calcium, causing the tingling and cramps of hypocalcemia, so calcium is monitored and replaced during the daily exchanges that are lifesaving."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Acquired TTP is calmed with cortisol: corticosteroids suppress the autoantibody response against ADAMTS13 and are given alongside plasma exchange (with rituximab and caplacizumab) to bring the immune-driven disease under control."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "TTP starves organs of oxygen with platelet microthrombi: clumps of platelets plug small vessels throughout the body, cutting oxygen to brain, heart and kidney, so the ischemic organ damage—not bleeding—drives its danger."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells help start acquired TTP: by presenting ADAMTS13 fragments to T cells they break tolerance, licensing the autoantibodies that disable the enzyme—the autoimmune trigger upstream of the microthrombi."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "TTP can strike the gut with microvascular clots: ischemia of the bowel causes abdominal pain, nausea and even pancreatitis, so gastrointestinal symptoms are common and sometimes the presenting feature of the disease."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "TTP can spill potassium into the blood: brisk microangiopathic hemolysis releases potassium from shattered red cells, and the acute kidney injury compounds it, risking dangerous hyperkalemia."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "TTP can injure the pancreas: microthrombi in its small vessels cause ischemic damage that disturbs blood sugar and raises pancreatic enzymes, another organ the microangiopathy quietly strikes."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "The marrow races to refill what TTP destroys: as microangiopathy shears red cells and consumes platelets, the bone marrow ramps up production, though it cannot keep pace with the relentless destruction."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Light through a blood smear clinches TTP: the microscope reveals schistocytes — red cells sheared into helmet shapes by the microthrombi — the single most important clue, while brain MRI shows the strokes and reversible edema behind the neurologic signs."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows what clogs the vessels: hyaline microthrombi of platelets glued by ultralong von Willebrand multimers pack the arterioles and capillaries — the pathologic lesion TTP's missing ADAMTS13 enzyme fails to prevent."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver registers TTP's hemolysis: red cells shredded across the body spill lactate dehydrogenase and bilirubin that the liver processes, while microthrombi in its small vessels can derange liver enzymes during a crisis."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "TTP starves the brain's neurons in flickers: platelet microthrombi plug the cerebral microvessels, producing the fluctuating confusion, headache, seizures, and focal deficits that are the hallmark neurologic feature of a crisis."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "The heart muscle is a hidden victim: microthrombi clog the coronary microcirculation, injuring cardiomyocytes with troponin rise, arrhythmia, and sudden death — a leading cause of acute mortality in TTP that can be silent until severe."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "The 'purpura' shows on the skin: the profound thrombocytopenia of TTP lets blood leak into the skin as petechiae and bruises, often the first visible sign that sends a patient for the blood count that reveals the crisis."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Acquired TTP is an autoantibody disease: an inhibitor antibody against ADAMTS13 lets giant vWF multimers run wild, so rituximab clears the B cells making it and the anti-vWF nanobody caplacizumab blocks the platelet clumping while plasma exchange replaces the enzyme."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Pregnancy can ignite TTP: the physiologic fall in ADAMTS13 and rise in vWF make gestation a classic trigger, and the picture must be told apart from HELLP and preeclampsia, which it can dangerously mimic."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Microthrombi reach the eye: occlusion of retinal vessels causes hemorrhages, exudates, and serous detachments with sudden visual blurring, a window onto the same microangiopathy strangling the brain and kidney."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils help weave the clots: NETs — webs of DNA and enzymes the neutrophils cast out — provide a scaffold for the von Willebrand factor strings and platelets that occlude the microvessels in TTP, amplifying the thrombotic storm."
  - target: 01-human/07-system/gvhd
    relation: connects-to
    note: "A transplant can trigger a TTP-like illness: transplant-associated thrombotic microangiopathy, driven by endothelial injury from conditioning, calcineurin inhibitors and graft-versus-host disease, mimics TTP but stems from complement rather than ADAMTS13 loss."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Complement tells the microangiopathies apart: TTP comes from ADAMTS13 deficiency, while its look-alike aHUS is driven by uncontrolled complement at C5 — the distinction that decides between plasma exchange and the C5 blocker eculizumab."
  - target: 01-human/03-molecular/fcrn
    relation: connects-to
    note: "The disease lives on a recycled antibody: the anti-ADAMTS13 IgG that causes immune TTP is kept in circulation by FcRn, so FcRn blockers that speed IgG clearance are an emerging way to lower the autoantibody without broad immunosuppression."
  - target: 02-pathogen/02-bacteria/escherichia-coli
    relation: connects-to
    note: "A bacterial toxin makes the look-alike: Shiga-toxin E. coli causes typical hemolytic uremic syndrome, a thrombotic microangiopathy that mimics TTP's clotting and red-cell shredding but spares ADAMTS13 and centers on the kidney."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Severe infection can fracture the picture: sepsis triggers its own microangiopathy and consumptive coagulopathy that overlaps TTP's low platelets and organ damage, a key mimic that must be sorted out before committing to plasma exchange."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 keeps the autoantibody factory running: acquired TTP is driven by anti-ADAMTS13 IgG, and STAT3 signaling supports the survival of the plasma cells that secrete it — part of why B-cell-directed rituximab quiets relapsing disease."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB primes the endothelium that clots: inflammatory activation of endothelial cells through NF-κB promotes release of ultralarge von Willebrand factor multimers, the very strings that uncleaved ADAMTS13 fails to cut in TTP."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 rises with the acute storm: levels of this inflammatory cytokine climb during acute TTP episodes and track with severity, reflecting the systemic inflammation that accompanies the microvascular thrombosis."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Microthrombi scar the kidney over time: even when acute renal failure is milder than in HUS, the renal microvascular injury of repeated TTP episodes can leave residual chronic kidney disease in survivors."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "The heart is a hidden target: microvascular thrombi in the myocardium during acute TTP cause troponin rise, arrhythmia and cardiac dysfunction — a leading cause of death — that can leave lasting heart failure."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Survivors carry a lasting mental toll: even after ADAMTS13 recovers, TTP survivors have high rates of depression and cognitive impairment, a long-term neuropsychiatric sequela of the cerebral microvascular injury and traumatic illness."
  - target: 01-human/07-system/ptsd
    relation: connects-to
    note: "A sudden life-threatening, relapsing illness can scar the mind: surviving acute TTP and living under the threat of relapse leaves many patients with post-traumatic stress symptoms, a recognized psychological aftermath of the disease."
  - target: 02-pathogen/01-viruses/hepatitis-b-virus
    relation: connects-to
    note: "Its rituximab can reactivate dormant hepatitis B: the anti-CD20 antibody used to treat and prevent relapse in immune TTP depletes B cells, so screening and antiviral prophylaxis for hepatitis B precede therapy."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: connects-to
    note: "Rituximab and steroids blunt defense against Pneumocystis: the B-cell depletion and corticosteroids used in immune TTP suppress immunity enough that Pneumocystis pneumonia becomes a risk, sometimes prompting prophylaxis."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "Its rituximab reawakens shingles: the B-cell-depleting therapy used to treat and prevent relapse in immune TTP blunts antiviral immunity, allowing latent varicella-zoster to reactivate."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Microthrombi starve the gut: the platelet-rich microvascular clots of TTP can lodge in mesenteric and pancreatic vessels, causing abdominal pain, pancreatitis and bowel ischaemia."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A sudden, relapsing, life-threatening illness breeds worry: the abrupt onset, risk of relapse and need for ongoing monitoring in TTP foster chronic health anxiety alongside the PTSD and depression it can leave."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It clots the brain's small vessels: fluctuating confusion, headache, seizures, focal deficits and coma from cerebral microthrombi are defining features of TTP and a hallmark of its classic pentad."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Falling platelets bruise the skin: the severe thrombocytopenia of TTP causes widespread petechiae, purpura and mucosal bleeding, often the first visible clue to the diagnosis."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Microthrombi can injure the heart: cardiac involvement in TTP causes myocardial microinfarction, arrhythmias and sudden death, an under-recognised cause of its mortality."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Microthrombi reach the kidney: renal involvement is part of the TTP pentad, causing acute kidney injury, usually milder than the severe renal failure of haemolytic uraemic syndrome."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Its treatment can flood the lungs: plasma exchange, the mainstay therapy, carries a risk of transfusion-related acute lung injury, and microthrombi can rarely involve the pulmonary vasculature."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It can clot the glands: microvascular thrombi can injure the pancreas, causing pancreatitis, and the adrenal glands, causing microinfarction."
  - target: 03-medicine/01-modern/02-respiratory/corticosteroids
    relation: connects-to
    note: "Immunosuppression treats the autoimmune form: corticosteroids, with plasma exchange, rituximab and caplacizumab, suppress the autoantibody that destroys ADAMTS13 in immune TTP."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "B cells drive the autoimmune attack: the autoantibody against ADAMTS13 in immune TTP is produced by lymphoid B cells, which is why B-cell-depleting rituximab is now central to treatment."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Microvascular thrombosis reaches the muscles: the platelet-rich microthrombi of TTP lodge throughout the body, causing myalgia and ischaemic injury beyond the classic brain and kidney targets."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Targeted agents transformed it: caplacizumab, an anti-von Willebrand factor nanobody, blocks platelet-VWF binding to halt microthrombi acutely, while recombinant ADAMTS13 replaces the missing enzyme in congenital TTP."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Both rescue and cause: cytotoxic immunosuppressants like cyclophosphamide and vincristine salvage refractory immune TTP, yet certain chemotherapies such as gemcitabine and mitomycin can themselves trigger a drug-induced thrombotic microangiopathy."
  - target: 01-human/07-system/heparin-induced-thrombocytopenia
    relation: connects-to
    note: "Thrombocytopenia with thrombosis: like HIT, TTP is a syndrome where platelets fall yet clotting paradoxically increases — TTP from ADAMTS13 deficiency seeding VWF-platelet microthrombi, HIT from anti-PF4 antibodies activating platelets."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "Microthrombi clog the kidney's filters: the VWF-platelet microthrombi of TTP lodge in glomerular and arteriolar capillaries causing renal impairment, though kidney injury is typically milder than in its cousin aHUS."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Its clots stop the heart: microvascular thrombi in the myocardium during acute TTP cause troponin rise, arrhythmia and sudden cardiac death—a leading cause of mortality that justifies urgent plasma exchange."
  - target: 01-human/07-system/systemic-sclerosis
    relation: connects-to
    note: "Another thrombotic microangiopathy: scleroderma renal crisis causes microangiopathic haemolysis and thrombocytopenia resembling TTP but with normal ADAMTS13, so systemic sclerosis sits in the differential of an unexplained TMA."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "Disseminated arteriolar occlusion: TTP's platelet-VWF microthrombi lodge in terminal arterioles throughout the body—brain, heart, kidney—and this systemic small-vessel obstruction drives its multi-organ ischaemia."
  - target: 01-human/07-system/gastric-cancer
    relation: connects-to
    note: "Cancer-associated microangiopathy: widely metastatic adenocarcinomas—classically gastric cancer—can trigger a microangiopathic haemolytic anaemia mimicking TTP, but with normal ADAMTS13 and no response to plasma exchange."
  - target: 01-human/07-system/malaria
    relation: connects-to
    note: "A TMA mimic in the returning traveller: severe falciparum malaria sequesters parasitised red cells in the microvasculature, producing thrombocytopenia and haemolysis that can be mistaken for a thrombotic microangiopathy."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "An infectious trigger: COVID-19 can precipitate relapse of immune TTP and cause its own thrombotic microangiopathy through widespread endothelial injury, blurring the line between the two."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "Cancer-associated microangiopathy: mucin-producing adenocarcinomas such as pancreatic and gastric cancer cause a microangiopathic haemolytic anaemia that mimics TTP but has normal ADAMTS13 and needs treating the tumour."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Microthrombi in the heart: platelet-rich microthrombi lodge in the myocardium and its conduction system during TTP, causing arrhythmia and sudden cardiac death—a major and often overlooked cause of acute mortality."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Splenic clearance and autoimmunity: splenic macrophages clear antibody-coated cells and contribute to the autoimmune response against ADAMTS13, the rationale for splenectomy in refractory acquired TTP."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Endothelial inflammation: NLRP3-inflammasome activation in injured microvascular endothelium amplifies the inflammatory damage that accompanies the thrombotic microangiopathy of TTP."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Inflammatory amplification: IL-1β and related cytokines released during TTP's endothelial injury heighten the prothrombotic, inflammatory state of the acute episode."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Endothelial dysfunction: the microvascular endothelial injury of TTP cuts nitric oxide production, removing its vasodilator and antithrombotic brake and worsening microthrombosis."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Vasoconstrictor imbalance: injured endothelium in TTP releases endothelin-1, whose vasoconstriction aggravates the organ ischaemia of the thrombotic microangiopathy."
  - target: 01-human/03-molecular/fibrinogen
    relation: connects-to
    note: "Platelet-rich microthrombi: the VWF-driven platelet aggregates of TTP, with fibrinogen-mediated cross-linking, form the microthrombi that shear red cells and occlude small vessels."
  - target: 01-human/03-molecular/pf4
    relation: connects-to
    note: "Platelet activation: platelets caught in the VWF-rich microthrombi of TTP degranulate and release platelet factor 4, a marker of the platelet consumption that produces the profound thrombocytopenia of the disease."
  - target: 01-human/03-molecular/baff
    relation: connects-to
    note: "Autoantibody drive: in immune TTP, BAFF supports the autoreactive B cells that produce the anti-ADAMTS13 IgG autoantibodies, the rationale behind B-cell-directed therapy alongside rituximab."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Inflammatory trigger: infection-driven TLR4 signalling on endothelium promotes Weibel-Palade-body release of VWF, helping explain why infections and inflammation precipitate acute TTP episodes and relapses."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Genetic predisposition: the HLA-DRB1*11 allele predisposes to acquired TTP by favouring presentation of ADAMTS13 peptides to T cells, helping break tolerance and license the autoantibodies that inhibit the enzyme."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Refractory plasma cells: long-lived anti-ADAMTS13 plasma cells survive on BCL-2 and escape rituximab, the rationale for proteasome-inhibitor or anti-CD38 plasma-cell-directed therapy in relapsing or refractory acquired TTP."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "Neutrophil thrombo-inflammation: neutrophils releasing S100A8/A9 and extracellular traps (NETs) within the microvasculature amplify the platelet-VWF microthrombi of TTP, adding an innate-immune layer to the ADAMTS13-deficient thrombotic process."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Ischaemic organ damage: disseminated platelet-VWF microthrombi occlude the microvasculature of TTP, and the resulting tissue hypoxia drives HIF-1α responses in brain, kidney and heart — the basis of its neurological and cardiac end-organ injury."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Endothelial integrity: VEGF maintains endothelial and glomerular health, and its blockade causes drug-induced thrombotic microangiopathy that mimics TTP — distinguishing VEGF-disruption TMA from the ADAMTS13-deficient disease."
  - target: 01-human/03-molecular/btk
    relation: connects-to
    note: "Autoantibody production: in acquired TTP, Bruton's tyrosine kinase relays B-cell-receptor signals in the autoreactive B cells that make anti-ADAMTS13 antibodies, an axis (with the CD20 cells and BAFF already mapped) of interest for B-cell-directed therapy."
  - target: 01-human/03-molecular/ctla-4
    relation: connects-to
    note: "Tolerance breakdown: impaired CTLA-4-dependent regulatory T-cell control underlies the loss of self-tolerance that permits the anti-ADAMTS13 autoantibody response of acquired TTP."
  - target: 01-human/03-molecular/thrombopoietin
    relation: connects-to
    note: "Platelet consumption: the consumptive thrombocytopenia of TTP, as platelets are swept into microthrombi, drives a compensatory thrombopoietin response reflecting the high platelet turnover."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Endothelial activation: Ang-2 release from activated endothelium amplifies the endothelial dysfunction of the thrombotic microangiopathy, promoting the microvascular platelet thrombosis of TTP."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Inflammatory trigger: TLR-MyD88-NF-κB innate signalling (TLR4 and NF-κB already mapped) contributes to the endothelial activation and inflammatory milieu that can trigger and amplify TTP episodes."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Cytokine response: IL-6-JAK-STAT3 signalling (IL-6 and STAT3 already mapped) participates in the systemic inflammatory response accompanying acute TTP."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "Complement amplification: complement activation generating C5a engages C5aR1 (C3 and C5 already mapped) to amplify the endothelial and platelet activation of the thrombotic microangiopathy in TTP."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Endothelial and platelet PI3K-AKT signalling shapes the activated, procoagulant phenotype that propagates the microvascular thrombosis of TTP."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signalling in platelets and endothelium amplifies the cellular activation driving the von-Willebrand-factor-rich microthrombi of TTP."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 promotes the neutrophil-extracellular-trap-driven thromboinflammation that contributes to the microvascular injury of TTP."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA released from NETs and lysed cells engages cGAS-STING, amplifying the type-I-interferon thromboinflammation of TTP."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signaling propagates the interferon-driven endothelial activation that aggravates the microvascular injury of TTP."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA) signaling in platelets and endothelium reinforces the activated, procoagulant phenotype that sustains the microthrombi of TTP."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO downstream of PI3K-AKT signaling (AKT and PIK3CA already mapped) regulates the survival of the autoantibody-producing B and plasma cells driving acquired thrombotic thrombocytopenic purpura."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the platelet-activation and inflammatory signaling relevant to the microthrombosis of thrombotic thrombocytopenic purpura."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated cytotoxicity contributes to the endothelial injury that provokes the von-Willebrand-factor release of thrombotic thrombocytopenic purpura."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family (LYN) kinase signaling downstream of the B-cell receptor participates in the autoreactive anti-ADAMTS13 B-cell response of immune thrombotic thrombocytopenic purpura."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTOR signaling in the autoreactive B and plasma cells participates in the immune process of thrombotic thrombocytopenic purpura."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the endothelial and immune-cell responses relevant to thrombotic thrombocytopenic purpura."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked endothelial metabolic signaling modulates the vascular homeostasis relevant to thrombotic thrombocytopenic purpura."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment contributes to the autoantibody-driven inflammation of acquired thrombotic thrombocytopenic purpura."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the autoreactive immune response in acquired thrombotic thrombocytopenic purpura."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the platelet and endothelial interactions relevant to thrombotic thrombocytopenic purpura."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the endothelial and immune activation relevant to thrombotic thrombocytopenic purpura."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the immune dysregulation of immune-mediated thrombotic thrombocytopenic purpura."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Cardiac microthrombosis: myocardial capillary platelet microthrombi in TTP release cardiac troponin, and troponin elevation on presentation predicts mortality, tying the systemic microangiopathy to the frequently fatal cardiac injury."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Adhesion anchor: von Willebrand factor (already mapped) normally binds subendothelial collagen to tether platelets at injury sites, the physiological adhesion axis that becomes pathological when uncleaved ultra-large multimers bind platelets under shear in TTP."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Platelet amplification: platelets recruited into the TTP microthrombi release thromboxane, a prostaglandin that amplifies aggregation and vasoconstriction, reinforcing the growing platelet plugs that occlude the microcirculation."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Dense-granule vasoconstrictor: platelets consumed into the TTP microthrombi release their stored serotonin, which constricts vessels and further activates platelets, adding a vasoactive component to the microvascular occlusion."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Pregnancy and female predominance: TTP is more common in women and can be precipitated by pregnancy, when rising oestrogen and falling ADAMTS13 (already mapped) activity combine to trigger the thrombotic microangiopathy."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Immune tolerance: PD-1 helps restrain the autoreactive response, and checkpoint-inhibitor cancer therapy has been reported to trigger acquired TTP by breaking tolerance to ADAMTS13, revealing this checkpoint's role in the autoimmunity."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immune regulation: the anti-inflammatory IL-10 and regulatory T cells (CTLA-4 already mapped) normally restrain the autoreactive response, and the tolerance defect allowing anti-ADAMTS13 (already mapped) autoantibodies reflects a failure of this immunoregulation in acquired TTP."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Type-2 autoantibody help: IL-4 and the Th2 response support the B cells (already mapped) that produce the inhibitory anti-ADAMTS13 autoantibodies driving acquired thrombotic thrombocytopenic purpura."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Haemolysis and oxidative stress: the microangiopathic haemolysis of TTP releases lactate dehydrogenase and, with the endothelial injury, generates oxidative stress to which xanthine oxidase contributes, marking the intravascular cell destruction."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Haemolysis and iron: the microangiopathic haemolysis of TTP fragments red cells (haemoglobin already mapped) into schistocytes, releasing iron and haem, part of the intravascular red-cell destruction that marks the disease."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 autoantibody help: IL-13, with IL-4 (already mapped), supports the B cells (already mapped) producing the inhibitory anti-ADAMTS13 autoantibodies that drive acquired thrombotic thrombocytopenic purpura."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Iron handling in haemolysis: the haem released by the microangiopathic haemolysis and the inflammation (IL-6 already mapped) disturb hepcidin-regulated iron handling, part of the altered iron biology of the intravascular destruction in TTP."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Autoimmune dysregulation: type-I interferon signalling is implicated in the loss of tolerance that permits the anti-ADAMTS13 (already mapped) autoantibody production of acquired thrombotic thrombocytopenic purpura."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, a pro-inflammatory adipokine, rises with the systemic inflammation (IL-6 already mapped) and endothelial activation of acute thrombotic thrombocytopenic purpura, part of its inflammatory milieu."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Plasma-exchange citrate: the citrate anticoagulant of the therapeutic plasma exchange central to TTP treatment chelates magnesium as well as calcium (already mapped), needing electrolyte replacement."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Cardiac microthrombi: the myocardial microthrombi of TTP cause the troponin (already mapped) rise, the arrhythmias and the sudden cardiac death, a leading cause of acute TTP mortality affecting the heart."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Immune-metabolic adipokine: leptin, with resistin (already mapped), is part of the adipokine milieu of the systemic inflammation (IL-6 already mapped) of acute thrombotic thrombocytopenic purpura."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin and resistin (already mapped), completes the adipokine dimension of the immune-metabolic milieu of thrombotic thrombocytopenic purpura."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 autoimmunity: the IFN-γ of the T cells is the type-II interferon arm (with the type-I interferon already mapped) of the immune dysregulation driving the anti-ADAMTS13 (already mapped) autoimmunity of acquired thrombotic thrombocytopenic purpura."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the autoimmune response against ADAMTS13 (already mapped) in thrombotic thrombocytopenic purpura."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Innate immune modulation: the NK cells (perforin already mapped) contribute to the innate immune dysregulation of the acquired autoimmune thrombotic thrombocytopenic purpura."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation of the acquired autoimmune thrombotic thrombocytopenic purpura."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune dysregulation underlying the anti-ADAMTS13 (already mapped) autoimmunity of thrombotic thrombocytopenic purpura."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the autoimmune thrombotic thrombocytopenic purpura."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Adaptive autoimmunity: the cytotoxic T cells (perforin already mapped), alongside the T-helper (already mapped) support of the anti-ADAMTS13 (already mapped) B-cell response, are part of the adaptive autoimmunity of thrombotic thrombocytopenic purpura."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Antioxidant micronutrient: selenium, a selenoprotein antioxidant cofactor, is part of the micronutrient dimension of the immune dysregulation of the autoimmune thrombotic thrombocytopenic purpura."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Immunomodulatory vitamin: vitamin D modulates the T-cell (already mapped) autoimmunity, and its deficiency is part of the micronutrient dimension of the autoimmune thrombotic thrombocytopenic purpura."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) at the injured endothelium (already mapped), overlapping the complement-mediated microangiopathy that distinguishes TTP from atypical HUS."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement/contact regulation: the C1-esterase inhibitor regulates the classical complement and the contact-coagulation systems activated by the anti-ADAMTS13 (immunoglobulin already mapped) autoimmunity of thrombotic thrombocytopenic purpura."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Haemolytic iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the microangiopathic haemolysis of thrombotic thrombocytopenic purpura."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-driven autoimmunity: TSLP released from the injured platelet-rich endothelium (already mapped) of thrombotic thrombocytopenic purpura activates plasmacytoid dendritic cells and sustains the type-2 and anti-ADAMTS13 autoimmune response."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kallikrein-contact activation: bradykinin, generated by contact-pathway (C1-esterase inhibitor already mapped) activation on ULVWF-platelet thrombi, amplifies the vascular permeability and endothelial (already mapped) injury in thrombotic thrombocytopenic purpura."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Haemolytic anaemia support: erythropoietin corrects the microangiopathic haemolytic anaemia of thrombotic thrombocytopenic purpura refractory to plasma exchange, and EPO signalling may modulate the erythrocyte (already mapped) fragmentation kinetics."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell vascular permeability: histamine from mast cells activated in the inflamed TTP endothelium amplifies vascular permeability and contributes to the thrombocytopenic microangiopathy, complementing the bradykinin (already mapped) kinin axis."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Endothelial matrix remodelling: periostin is expressed in the vascular wall remodelled by ULVWF-mediated platelet aggregation in TTP, modulating integrin signalling on endothelial cells during the thrombotic microangiopathy."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Platelet circadian regulator: melatonin modulates platelet reactivity and platelet-endothelial interactions via melatonin receptors on platelets; reduced melatonin rhythmicity may amplify the platelet hyper-reactivity of TTP."
---

# Thrombotic Thrombocytopenic Purpura

## Overview

**Thrombotic thrombocytopenic purpura (TTP)** is a **life-threatening thrombotic microangiopathy (TMA)** caused by severe **ADAMTS13 deficiency (<10% of normal activity)**, leading to accumulation of ultra-large von Willebrand factor (ULVWF) multimers → platelet-rich microthrombi in arterioles and capillaries → ischemic end-organ injury [^george-2010-ttp-review].

TTP is defined by the **TMA pentad** (though all five features are present in <10% of cases at diagnosis):
1. **Microangiopathic hemolytic anemia (MAHA)** — schistocytes on peripheral blood smear; Coombs-negative; LDH elevated
2. **Thrombocytopenia** — typically <30,000/μL (often <20,000/μL)
3. **Neurological symptoms** — headache, confusion, focal deficits, seizures, coma (cerebral arteriolar microthrombi)
4. **Renal dysfunction** — mild AKI (creatinine elevation); cf. HUS which has severe renal failure
5. **Fever** — present in ~25%; no longer required for diagnosis

**In practice:** The combination of MAHA + thrombocytopenia in a patient without DIC or other obvious TMA cause should prompt **empiric treatment (plasma exchange) before ADAMTS13 results return** — the diagnosis is a clinical emergency.

**Epidemiology:**
- Incidence: ~3-10 per million per year; F>M (~2:1); median age 40 years
- HLA-DRB1*11 is the strongest genetic risk factor for acquired iTTP in European populations
- Triggers: infections (most common), pregnancy (obstetric TTP; first trimester → think congenital; second/third → acquired iTTP), autoimmune disease (SLE, inflammatory bowel disease), HIV, medications (ticlopidine, clopidogrel, quinine — "drug-induced TMA"; ADAMTS13 may or may not be <10%)

## Structure

### Classification of TTP

**Acquired iTTP (immune-mediated; ~95% of TTP cases):**
- Anti-ADAMTS13 IgG autoantibodies inhibit ADAMTS13 activity or accelerate clearance → ADAMTS13 <10%
- Predominantly IgG4 subclass targeting the ADAMTS13 spacer domain (inhibiting); also IgG1 non-inhibiting clearance antibodies
- Episodic: acute event → remission (ADAMTS13 recovers to >50% off therapy) → potential relapse (anti-ADAMTS13 IgG returns)
- Relapse rate: ~30-40% at 5 years without rituximab; <10% with rituximab-based immunosuppression

**Congenital TTP (Upshaw-Schulman syndrome; cTTP; ~5%):**
- Biallelic *ADAMTS13* mutations → absent or severely reduced constitutive ADAMTS13 activity
- Onset: neonatal (unexplained neonatal jaundice + thrombocytopenia) or childhood
- Triggers: pregnancy (ULVWF release from placental endothelium), infections, surgeries
- Treatment: FFP infusion every 2-3 weeks (prophylactic ADAMTS13 replacement); recombinant ADAMTS13 (rADAMTS13; Tasigna; FDA 2023) now available

**TMA differential diagnosis — not TTP:**

| Condition | ADAMTS13 | Key distinguishing features |
|:---------|:---------|:---------------------------|
| TTP | <10% | Neurological dominant; platelet count very low; renal mild |
| HUS (Shiga toxin) | Normal | Shiga toxin + (STEC O157:H7 → bloody diarrhea); severe AKI; complement activation |
| aHUS | Normal | Complement dysregulation (CFH/CFI/C3/MCP mutations); severe AKI; eculizumab treatment |
| DIC | Variable | Elevated PT, D-dimer, fibrinogen consumption; underlying trigger (sepsis, malignancy) |
| Malignant hypertension | Normal | DBP >120 mmHg; hypertensive crisis |
| Drug-induced TMA | Variable | Drug exposure (quinine, gemcitabine, VEGF inhibitors); some ADAMTS13-dependent |
| Pregnancy (HELLP) | Normal (or mildly low) | Preeclampsia features; elevated LFTs; 3rd trimester; resolves with delivery |

### PLASMIC score for iTTP probability

The PLASMIC score guides empiric treatment decisions when ADAMTS13 result is pending:

| Variable | Points |
|:---------|:-------|
| Platelet count <30 × 10⁹/L | 1 |
| Combined hemolysis (reticulocyte >2.5% or haptoglobin undetectable or indirect bilirubin >2 mg/dL) | 1 |
| Absence of active cancer | 1 |
| Absence of stem cell/solid organ transplant | 1 |
| MCV <90 fL | 1 |
| INR <1.5 | 1 |
| Creatinine <2 mg/dL | 1 |
| **Score 6-7 (high probability):** | ADAMTS13 <10% in ~90%; treat empirically with PEX |

## Function

### Normal ADAMTS13 physiology

In healthy individuals, ADAMTS13 (~190 kDa plasma glycoprotein; hepatic synthesis) maintains VWF multimer size by cleaving ULVWF at Tyr1605-Met1606 in the VWF A2 domain under shear stress — preventing spontaneous platelet aggregation in the microcirculation. Normal plasma ADAMTS13 activity: 50-150%; physiological reserve means TTP only manifests when activity falls below ~10%.

## Pathology

### Clinical manifestations

**Neurological (~75% of iTTP):**
- Headache, confusion, aphasia, visual changes → cerebral arteriolar microthrombi
- Fluctuating: relapsing-remitting over hours as microthrombi form and lyse
- Seizures (typically during severe thrombocytopenia/anemia)
- Stroke (hemorrhagic or ischemic; thrombocytopenia + anticoagulation risk)
- **Key teaching:** Neurological symptoms often precede MAHA recognition → TTP must be in the differential for any unexplained acute neurological syndrome + thrombocytopenia

**Hematological:**
- Microangiopathic hemolytic anemia: schistocytes ≥1% on peripheral blood smear (helmet cells, fragmented RBCs from mechanical destruction in narrowed vessels)
- LDH markedly elevated (hemolysis + ischemic tissue damage); haptoglobin undetectable
- Coombs-negative hemolysis (non-immune; cf. Evans syndrome or AIHA)
- Platelet count typically <30,000/μL; often <10,000/μL

**Cardiac:**
- TTP-related cardiac events in ~10-20% (troponin elevation, arrhythmias, sudden death)
- Coronary arteriolar microthrombi → demand ischemia; complement amplification → myocardial injury
- Risk of cardiac death increases if platelet count <20,000 with persistent hemolysis

**Renal:**
- Mild AKI (creatinine typically <3 mg/dL) in iTTP — distinguishes from HUS where severe renal failure is the norm
- Proteinuria and mild hematuria
- Glomerular microthrombi (endothelial-platelet plugs) without significant fibrin deposition (unlike DIC)

### Diagnosis

**Essential workup:**
- Peripheral blood smear: schistocytes (≥1-2% of RBCs) — pathognomonic of TMA; report absolute count
- CBC: thrombocytopenia + anemia
- LDH, haptoglobin, indirect bilirubin, reticulocyte count: hemolysis markers
- Coagulation studies: PT, aPTT, fibrinogen, D-dimer — typically **normal** in TTP (distinguishes from DIC)
- Creatinine, urinalysis: mild renal involvement
- Coombs (direct antiglobulin test): negative in TTP (hemolysis is mechanical, not immune)
- **ADAMTS13 activity assay** (send stat; FRETS-VWF73 or CBA): <10% confirms iTTP; results within 4-24 hours at specialized centers
- **Anti-ADAMTS13 IgG ELISA:** Confirms immune-mediated TTP; titer correlates with disease severity
- STEC/Shiga toxin stool testing: exclude HUS if diarrheal prodrome; complement genetics: exclude aHUS if ADAMTS13 normal
- HIV, ANA, pregnancy test: assess for secondary triggers

### Treatment

**Acute iTTP — first-line (triple therapy):**

1. **Therapeutic plasma exchange (PEX; plasmapheresis):**
   - Mechanism: Removes anti-ADAMTS13 antibodies + replenishes ADAMTS13 (FFP source)
   - Volume: 1.5× plasma volume daily until platelet count >150,000/μL × 2 days
   - Historical mortality reduction: 90% (untreated) → 20% (PEX alone) → <6% (PEX + caplacizumab)
   - Timing: Start within 4-8 hours of diagnosis; do not wait for ADAMTS13 results if PLASMIC score ≥6

2. **Caplacizumab (Cablivi; Sanofi; FDA Feb 2019):**
   - Mechanism: Bivalent anti-VWF A1 domain nanobody → blocks VWF-GPIbα → prevents platelet microthrombus formation; does NOT restore ADAMTS13
   - Dosing: 11 mg IV bolus before first PEX → 11 mg SC OD during PEX and ≥30 days after; extend if ADAMTS13 still <10%
   - **HERCULES trial (NEJM 2019):** PEX + caplacizumab vs. PEX + placebo; platelet normalization 2.69 vs. 2.88 days; composite endpoint (TTP death + recurrence + major thromboembolism) 12% vs. 38% (p<0.001); 12% relapse on caplacizumab after stopping if ADAMTS13 not replenished → mandates immunosuppression [^scully-2019-caplacizumab-hercules]
   - Bleeding risk: Mild-moderate; von Willebrand-like bleeding (epistaxis, GI bleeding); hold before invasive procedures

3. **Corticosteroids:**
   - Methylprednisolone 1 mg/kg/day IV (or oral prednisone 1 mg/kg/day) during acute phase
   - Mechanism: Reduce autoantibody production and inflammatory endothelial activation
   - Taper once ADAMTS13 recovers to >50%

**Rituximab (anti-CD20; off-label but now standard):**
- Indication: All acquired iTTP (acute phase: prevents relapse; or relapsing iTTP)
- Mechanism: Depletes B cells → eliminates ADAMTS13-antibody-producing clones → durable ADAMTS13 recovery
- Dosing: 375 mg/m² IV weekly × 4 (standard lymphoma dose); or 1000 mg IV × 2 doses 2 weeks apart
- Outcome: 5-year relapse-free survival ~85-90% with rituximab vs. ~60% without [^coppo-2019-rituximab-ttp]
- Response: ADAMTS13 recovery within 2-4 months post-rituximab; repeat dosing if anti-ADAMTS13 IgG rises during follow-up

**Refractory/relapsed iTTP:**
- Cyclosporin A or cyclophosphamide: second-line immunosuppression
- Bortezomib (proteasome inhibitor): targets plasma cells producing anti-ADAMTS13 IgG; case series support
- Splenectomy: Historical (pre-rituximab era); rarely needed now
- rADAMTS13 (recombinant ADAMTS13): Under investigation for cTTP and refractory iTTP

**Congenital TTP (Upshaw-Schulman syndrome):**
- FFP infusions (10-15 mL/kg) every 2-3 weeks (prophylactic) or on demand for triggers
- **Recombinant ADAMTS13 (BAX930/rADAMTS13; Takeda):** FDA approved 2023 for cTTP; 40 IU/kg IV Q2W → normalizes ADAMTS13 activity; preferred over FFP (defined dose, no volume overload, no infection risk)
- Pregnancy: Increase PEX/rADAMTS13 frequency; close platelet and ADAMTS13 monitoring throughout

**Monitoring and relapse prevention:**
- ADAMTS13 activity every 4-8 weeks for 2 years post-remission; anti-ADAMTS13 IgG concurrently
- **ADAMTS13 <20% in remission:** High relapse risk; consider preemptive rituximab even if platelets normal
- **Platelet count monitoring:** Sudden thrombocytopenia in a TTP survivor = presumptive relapse → restart PEX ± caplacizumab emergently

## Connections

- `connects-to` → **[ADAMTS13](../../03-molecular/adamts13/README.md)** — ADAMTS13 deficiency (<10% activity) is the defining pathophysiology of TTP; acquired iTTP is driven by anti-ADAMTS13 IgG4 antibodies; hereditary Upshaw-Schulman syndrome involves biallelic ADAMTS13 mutations; caplacizumab blocks VWF A1 domain → prevents ULVWF-platelet binding.
- `connects-to` → **[Von Willebrand Factor](../../03-molecular/von-willebrand-factor/README.md)** — ULVWF from Weibel-Palade bodies accumulates in TTP (ADAMTS13 deficiency) → GPIb-mediated platelet aggregation → microthrombi; caplacizumab (anti-VWF A1 nanobody; FDA 2019) blocks ULVWF-platelet tethering → fastest reversal of acute microthrombus formation in iTTP.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — Anti-ADAMTS13 autoantibodies are predominantly IgG4 (inhibiting spacer domain) in iTTP; IgG1 non-inhibiting antibodies accelerate ADAMTS13 clearance; rituximab (anti-CD20) depletes antibody-producing B cells → ADAMTS13 recovery; anti-ADAMTS13 IgG titer guides therapy duration.
- `connects-to` → **[Atypical HUS](../ahus/README.md)** — TTP (ADAMTS13 <10%) and aHUS (complement gene mutations; ADAMTS13 ≥10%) are the two most important complement/coagulation TMAs: both cause MAHA + thrombocytopenia + AKI; TTP is treated with PEX + caplacizumab + rituximab; aHUS with eculizumab — never interchange these therapies.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — ULVWF binds GPIbα on platelets → platelet-rich microthrombi in arterioles/capillaries → consumption; thrombocytopenia <30,000/μL is characteristic; caplacizumab blocks ULVWF-GPIbα → fastest microthrombus resolution; platelet count >150,000/μL × 2 days marks clinical remission.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — ULVWF-platelet microthrombi → ischemic endothelial injury → local C3 deposition; refractory iTTP shows elevated sC5b-9; TTP-aHUS overlap responds to eculizumab + PEX; C3d/sC5b-9 studied as TTP severity biomarkers; complement distinguishes refractory TTP from typical iTTP.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Endothelial Weibel-Palade bodies store ULVWF; endothelial activation → ULVWF secretion → ADAMTS13 normally cleaves; TTP: ADAMTS13 failure → ULVWF accumulates on endothelial surface → platelet tethering; endothelial injury from microthrombi → ULVWF release → amplification loop.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — The kidney is a TTP target organ: VWF-platelet microthrombi lodge in the renal microvasculature, causing acute kidney injury — usually milder than in aHUS, where renal failure dominates; this difference in renal severity helps separate the two thrombotic microangiopathies.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Neurologic involvement is TTP's most dangerous feature: cerebral microthrombi cause fluctuating confusion, headache, focal deficits, seizures, or coma — part of the classic pentad — that can come and go within hours, so suspected TTP needs urgent plasma exchange.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — TTP shears red cells: as erythrocytes squeeze through platelet-rich microthrombi they fragment into schistocytes, producing microangiopathic hemolytic anemia with high LDH, low haptoglobin, negative Coombs — schistocytes plus thrombocytopenia trigger ADAMTS13 testing.
- `connects-to` → **[Immune Thrombocytopenia](../immune-thrombocytopenia/README.md)** — TTP and immune thrombocytopenia both cause severe thrombocytopenia but differ: ITP is antibody-mediated platelet destruction without hemolysis, while TTP adds microangiopathic hemolysis and organ ischemia from ADAMTS13 deficiency—an emergency needing plasma exchange.
- `connects-to` → **[Disseminated Intravascular Coagulation](../disseminated-intravascular-coagulation/README.md)** — TTP and DIC both produce thrombocytopenia and schistocytes but are distinguished by coagulation tests: DIC consumes clotting factors and prolongs PT/PTT with high D-dimer, while TTP leaves coagulation times normal—because its clots are platelet-VWF, not fibrin.
- `connects-to` → **[Systemic Lupus Erythematosus](../systemic-lupus-erythematosus/README.md)** — Lupus can trigger or mimic TTP: SLE may produce acquired ADAMTS13 deficiency or a TTP-like thrombotic microangiopathy, and the two share features (hemolysis, low platelets, neuro/renal signs), so a lupus flare with schistocytes demands urgent ADAMTS13 testing.
- `connects-to` → **[Stroke](../stroke/README.md)** — TTP can present as stroke: ADAMTS13 deficiency lets VWF-platelet microthrombi lodge in the cerebral microvasculature, causing fluctuating confusion and focal deficits—so an unexplained stroke with thrombocytopenia and hemolysis should trigger urgent TTP work-up.
- `connects-to` → **[Antiphospholipid Syndrome](../antiphospholipid-syndrome/README.md)** — TTP and catastrophic antiphospholipid syndrome are both thrombotic microangiopathies occluding small vessels: TTP from ADAMTS13 deficiency, CAPS from antiphospholipid antibodies—overlapping clinically, so antibody testing helps separate these emergencies.
- `connects-to` → **[HIV/AIDS](../hiv-aids/README.md)** — HIV is a recognized cause of secondary TTP: the infection can trigger ADAMTS13 autoantibodies, producing thrombotic microangiopathy—so a new TTP diagnosis warrants HIV testing, and antiretroviral therapy plus plasma exchange treats the HIV-associated form.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — Plasma cells make the anti-ADAMTS13 antibody behind acquired TTP: long-lived autoantibody-secreting cells block the enzyme that cleaves von Willebrand factor, so giant VWF multimers clump platelets—why plasma exchange (removing antibody) and rituximab treat TTP.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — The heart is a major, underrecognized TTP target: microthrombi in coronary microvasculature cause troponin rise, arrhythmia and sudden death, so cardiac involvement is a leading cause of TTP mortality—reason to start plasma exchange urgently on suspicion.
- `connects-to` → **[Thrombin](../../03-molecular/thrombin/README.md)** — TTP clots without activating thrombin: unlike DIC, the microthrombi are platelet-VWF aggregates formed without triggering the coagulation cascade, so thrombin generation and clotting times stay normal—distinguishing it from consumptive coagulopathy.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — Acquired TTP is autoantibody-driven, so B cells are a treatment target: rituximab (anti-CD20) depletes the B cells making anti-ADAMTS13 antibodies, raising enzyme levels, preventing relapse, and increasingly used upfront alongside plasma exchange.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Most TTP is autoimmune: the immune system generates IgG autoantibodies against ADAMTS13, crippling the enzyme that cleaves von Willebrand factor—so unchecked VWF multimers trigger platelet microthrombi, distinguishing acquired TTP from the hereditary enzyme deficiency.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — The spleen links to TTP through antibody handling: its reticuloendothelial cells clear autoantibody-coated platelets and produce immunoglobulin, and historically splenectomy was used for refractory or relapsing immune TTP before rituximab became standard.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — Acquired TTP is treated by depleting B cells via CD20: rituximab, an anti-CD20 antibody, removes the B cells making anti-ADAMTS13 autoantibodies, reducing relapse alongside plasma exchange and the anti-vWF nanobody caplacizumab.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — Pregnancy can precipitate TTP: ADAMTS13 activity falls naturally in pregnancy, unmasking congenital deficiency or triggering acquired TTP, so it must be distinguished from preeclampsia and HELLP—a diagnostic challenge with very different treatments.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Acquired TTP is an autoimmune disease needing T-cell help: helper T cells recognizing ADAMTS13 drive B cells to make the inhibitory autoantibodies, so the disorder reflects a breakdown of tolerance to the body's own vWF-cleaving enzyme.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — TTP shreds red cells and spills hemoglobin: platelet-vWF microthrombi slice passing red cells (microangiopathic hemolysis), producing schistocytes, free hemoglobin, low haptoglobin and high LDH—the lab fingerprint that flags the emergency.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Treating TTP with plasma exchange drains calcium: the citrate anticoagulant in the apheresis circuit binds calcium, causing the tingling and cramps of hypocalcemia, so calcium is monitored and replaced during the daily exchanges that are lifesaving.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Acquired TTP is calmed with cortisol: corticosteroids suppress the autoantibody response against ADAMTS13 and are given alongside plasma exchange (with rituximab and caplacizumab) to bring the immune-driven disease under control.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — TTP starves organs of oxygen with platelet microthrombi: clumps of platelets plug small vessels throughout the body, cutting oxygen to brain, heart and kidney, so the ischemic organ damage—not bleeding—drives its danger.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells help start acquired TTP: by presenting ADAMTS13 fragments to T cells they break tolerance, licensing the autoantibodies that disable the enzyme—the autoimmune trigger upstream of the microthrombi.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — TTP can strike the gut with microvascular clots: ischemia of the bowel causes abdominal pain, nausea and even pancreatitis, so gastrointestinal symptoms are common and sometimes the presenting feature of the disease.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — TTP can spill potassium into the blood: brisk microangiopathic hemolysis releases potassium from shattered red cells, and the acute kidney injury compounds it, risking dangerous hyperkalemia.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — TTP can injure the pancreas: microthrombi in its small vessels cause ischemic damage that disturbs blood sugar and raises pancreatic enzymes, another organ the microangiopathy quietly strikes.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — The marrow races to refill what TTP destroys: as microangiopathy shears red cells and consumes platelets, the bone marrow ramps up production, though it cannot keep pace with the relentless destruction.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Light through a blood smear clinches TTP: the microscope reveals schistocytes — red cells sheared into helmet shapes by the microthrombi — the single most important clue, while brain MRI shows the strokes and reversible edema behind the neurologic signs.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows what clogs the vessels: hyaline microthrombi of platelets glued by ultralong von Willebrand multimers pack the arterioles and capillaries — the pathologic lesion TTP's missing ADAMTS13 enzyme fails to prevent.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver registers TTP's hemolysis: red cells shredded across the body spill lactate dehydrogenase and bilirubin that the liver processes, while microthrombi in its small vessels can derange liver enzymes during a crisis.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — TTP starves the brain's neurons in flickers: platelet microthrombi plug the cerebral microvessels, producing the fluctuating confusion, headache, seizures, and focal deficits that are the hallmark neurologic feature of a crisis.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — The heart muscle is a hidden victim: microthrombi clog the coronary microcirculation, injuring cardiomyocytes with troponin rise, arrhythmia, and sudden death — a leading cause of acute mortality in TTP that can be silent until severe.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — The 'purpura' shows on the skin: the profound thrombocytopenia of TTP lets blood leak into the skin as petechiae and bruises, often the first visible sign that sends a patient for the blood count that reveals the crisis.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Acquired TTP is an autoantibody disease: an inhibitor antibody against ADAMTS13 lets giant vWF multimers run wild, so rituximab clears the B cells making it and the anti-vWF nanobody caplacizumab blocks the platelet clumping while plasma exchange replaces the enzyme.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Pregnancy can ignite TTP: the physiologic fall in ADAMTS13 and rise in vWF make gestation a classic trigger, and the picture must be told apart from HELLP and preeclampsia, which it can dangerously mimic.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Microthrombi reach the eye: occlusion of retinal vessels causes hemorrhages, exudates, and serous detachments with sudden visual blurring, a window onto the same microangiopathy strangling the brain and kidney.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Neutrophils help weave the clots: NETs — webs of DNA and enzymes the neutrophils cast out — provide a scaffold for the von Willebrand factor strings and platelets that occlude the microvessels in TTP, amplifying the thrombotic storm.
- `connects-to` → **[Graft-Versus-Host Disease](../gvhd/README.md)** — A transplant can trigger a TTP-like illness: transplant-associated thrombotic microangiopathy, driven by endothelial injury from conditioning, calcineurin inhibitors and graft-versus-host disease, mimics TTP but stems from complement rather than ADAMTS13 loss.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Complement tells the microangiopathies apart: TTP comes from ADAMTS13 deficiency, while its look-alike aHUS is driven by uncontrolled complement at C5 — the distinction that decides between plasma exchange and the C5 blocker eculizumab.
- `connects-to` → **[FcRn](../../03-molecular/fcrn/README.md)** — The disease lives on a recycled antibody: the anti-ADAMTS13 IgG that causes immune TTP is kept in circulation by FcRn, so FcRn blockers that speed IgG clearance are an emerging way to lower the autoantibody without broad immunosuppression.
- `connects-to` → **[Escherichia coli](../../../02-pathogen/02-bacteria/escherichia-coli/README.md)** — A bacterial toxin makes the look-alike: Shiga-toxin E. coli causes typical hemolytic uremic syndrome, a thrombotic microangiopathy that mimics TTP's clotting and red-cell shredding but spares ADAMTS13 and centers on the kidney.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Severe infection can fracture the picture: sepsis triggers its own microangiopathy and consumptive coagulopathy that overlaps TTP's low platelets and organ damage, a key mimic that must be sorted out before committing to plasma exchange.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 keeps the autoantibody factory running: acquired TTP is driven by anti-ADAMTS13 IgG, and STAT3 signaling supports the survival of the plasma cells that secrete it — part of why B-cell-directed rituximab quiets relapsing disease.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB primes the endothelium that clots: inflammatory activation of endothelial cells through NF-κB promotes release of ultralarge von Willebrand factor multimers, the very strings that uncleaved ADAMTS13 fails to cut in TTP.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6 rises with the acute storm: levels of this inflammatory cytokine climb during acute TTP episodes and track with severity, reflecting the systemic inflammation that accompanies the microvascular thrombosis.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Microthrombi scar the kidney over time: even when acute renal failure is milder than in HUS, the renal microvascular injury of repeated TTP episodes can leave residual chronic kidney disease in survivors.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — The heart is a hidden target: microvascular thrombi in the myocardium during acute TTP cause troponin rise, arrhythmia and cardiac dysfunction — a leading cause of death — that can leave lasting heart failure.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Survivors carry a lasting mental toll: even after ADAMTS13 recovers, TTP survivors have high rates of depression and cognitive impairment, a long-term neuropsychiatric sequela of the cerebral microvascular injury and traumatic illness.
- `connects-to` → **[PTSD](../ptsd/README.md)** — A sudden life-threatening, relapsing illness can scar the mind: surviving acute TTP and living under the threat of relapse leaves many patients with post-traumatic stress symptoms, a recognized psychological aftermath of the disease.
- `connects-to` → **[Hepatitis B virus](../../../02-pathogen/01-viruses/hepatitis-b-virus/README.md)** — Its rituximab can reactivate dormant hepatitis B: the anti-CD20 antibody used to treat and prevent relapse in immune TTP depletes B cells, so screening and antiviral prophylaxis for hepatitis B precede therapy.
- `connects-to` → **[Pneumocystis jirovecii](../../../02-pathogen/03-fungi/pneumocystis-jirovecii/README.md)** — Rituximab and steroids blunt defense against Pneumocystis: the B-cell depletion and corticosteroids used in immune TTP suppress immunity enough that Pneumocystis pneumonia becomes a risk, sometimes prompting prophylaxis.
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — Its rituximab reawakens shingles: the B-cell-depleting therapy used to treat and prevent relapse in immune TTP blunts antiviral immunity, allowing latent varicella-zoster to reactivate.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Microthrombi starve the gut: the platelet-rich microvascular clots of TTP can lodge in mesenteric and pancreatic vessels, causing abdominal pain, pancreatitis and bowel ischaemia.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A sudden, relapsing, life-threatening illness breeds worry: the abrupt onset, risk of relapse and need for ongoing monitoring in TTP foster chronic health anxiety alongside the PTSD and depression it can leave.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It clots the brain's small vessels: fluctuating confusion, headache, seizures, focal deficits and coma from cerebral microthrombi are defining features of TTP and a hallmark of its classic pentad.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Falling platelets bruise the skin: the severe thrombocytopenia of TTP causes widespread petechiae, purpura and mucosal bleeding, often the first visible clue to the diagnosis.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Microthrombi can injure the heart: cardiac involvement in TTP causes myocardial microinfarction, arrhythmias and sudden death, an under-recognised cause of its mortality.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Microthrombi reach the kidney: renal involvement is part of the TTP pentad, causing acute kidney injury, usually milder than the severe renal failure of haemolytic uraemic syndrome.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Its treatment can flood the lungs: plasma exchange, the mainstay therapy, carries a risk of transfusion-related acute lung injury, and microthrombi can rarely involve the pulmonary vasculature.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It can clot the glands: microvascular thrombi can injure the pancreas, causing pancreatitis, and the adrenal glands, causing microinfarction.
- `connects-to` → **[Corticosteroids](../../../03-medicine/01-modern/02-respiratory/corticosteroids/README.md)** — Immunosuppression treats the autoimmune form: corticosteroids, with plasma exchange, rituximab and caplacizumab, suppress the autoantibody that destroys ADAMTS13 in immune TTP.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — B cells drive the autoimmune attack: the autoantibody against ADAMTS13 in immune TTP is produced by lymphoid B cells, which is why B-cell-depleting rituximab is now central to treatment.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Microvascular thrombosis reaches the muscles: the platelet-rich microthrombi of TTP lodge throughout the body, causing myalgia and ischaemic injury beyond the classic brain and kidney targets.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Targeted agents transformed it: caplacizumab, an anti-von Willebrand factor nanobody, blocks platelet-VWF binding to halt microthrombi acutely, while recombinant ADAMTS13 replaces the missing enzyme in congenital TTP.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Both rescue and cause: cytotoxic immunosuppressants like cyclophosphamide and vincristine salvage refractory immune TTP, yet certain chemotherapies such as gemcitabine and mitomycin can themselves trigger a drug-induced thrombotic microangiopathy.
- `connects-to` → **[Heparin-induced Thrombocytopenia](../heparin-induced-thrombocytopenia/README.md)** — Thrombocytopenia with thrombosis: like HIT, TTP is a syndrome where platelets fall yet clotting paradoxically increases — TTP from ADAMTS13 deficiency seeding VWF-platelet microthrombi, HIT from anti-PF4 antibodies activating platelets.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — Microthrombi clog the kidney's filters: the VWF-platelet microthrombi of TTP lodge in glomerular and arteriolar capillaries causing renal impairment, though kidney injury is typically milder than in its cousin aHUS.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Its clots stop the heart: microvascular thrombi in the myocardium during acute TTP cause troponin rise, arrhythmia and sudden cardiac death—a leading cause of mortality that justifies urgent plasma exchange.
- `connects-to` → **[Systemic Sclerosis](../systemic-sclerosis/README.md)** — Another thrombotic microangiopathy: scleroderma renal crisis causes microangiopathic haemolysis and thrombocytopenia resembling TTP but with normal ADAMTS13, so systemic sclerosis sits in the differential of an unexplained TMA.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — Disseminated arteriolar occlusion: TTP's platelet-VWF microthrombi lodge in terminal arterioles throughout the body—brain, heart, kidney—and this systemic small-vessel obstruction drives its multi-organ ischaemia.
- `connects-to` → **[Gastric Cancer](../gastric-cancer/README.md)** — Cancer-associated microangiopathy: widely metastatic adenocarcinomas—classically gastric cancer—can trigger a microangiopathic haemolytic anaemia mimicking TTP, but with normal ADAMTS13 and no response to plasma exchange.
- `connects-to` → **[Malaria](../malaria/README.md)** — A TMA mimic in the returning traveller: severe falciparum malaria sequesters parasitised red cells in the microvasculature, producing thrombocytopenia and haemolysis that can be mistaken for a thrombotic microangiopathy.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — An infectious trigger: COVID-19 can precipitate relapse of immune TTP and cause its own thrombotic microangiopathy through widespread endothelial injury, blurring the line between the two.
- `connects-to` → **[Pancreatic Cancer](../pancreatic-cancer/README.md)** — Cancer-associated microangiopathy: mucin-producing adenocarcinomas such as pancreatic and gastric cancer cause a microangiopathic haemolytic anaemia that mimics TTP but has normal ADAMTS13 and needs treating the tumour.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Microthrombi in the heart: platelet-rich microthrombi lodge in the myocardium and its conduction system during TTP, causing arrhythmia and sudden cardiac death—a major and often overlooked cause of acute mortality.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Splenic clearance and autoimmunity: splenic macrophages clear antibody-coated cells and contribute to the autoimmune response against ADAMTS13, the rationale for splenectomy in refractory acquired TTP.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Endothelial inflammation: NLRP3-inflammasome activation in injured microvascular endothelium amplifies the inflammatory damage that accompanies the thrombotic microangiopathy of TTP.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Inflammatory amplification: IL-1β and related cytokines released during TTP's endothelial injury heighten the prothrombotic, inflammatory state of the acute episode.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — Endothelial dysfunction: the microvascular endothelial injury of TTP cuts nitric oxide production, removing its vasodilator and antithrombotic brake and worsening microthrombosis.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Vasoconstrictor imbalance: injured endothelium in TTP releases endothelin-1, whose vasoconstriction aggravates the organ ischaemia of the thrombotic microangiopathy.
- `connects-to` → **[Fibrinogen](../../03-molecular/fibrinogen/README.md)** — Platelet-rich microthrombi: the VWF-driven platelet aggregates of TTP, with fibrinogen-mediated cross-linking, form the microthrombi that shear red cells and occlude small vessels.
- `connects-to` → **[PF4](../../03-molecular/pf4/README.md)** — Platelets caught in the VWF-rich microthrombi of TTP degranulate and release platelet factor 4, a marker of the platelet consumption that produces the profound thrombocytopenia central to the diagnosis.
- `connects-to` → **[BAFF](../../03-molecular/baff/README.md)** — In immune TTP, BAFF supports the autoreactive B cells that produce the anti-ADAMTS13 IgG autoantibodies—the autoimmune mechanism underlying the acquired form and the rationale for B-cell-directed therapy alongside rituximab.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — Infection-driven TLR4 signaling on endothelium promotes Weibel-Palade-body release of ultra-large VWF multimers, helping explain why infections and inflammation so often precipitate acute TTP episodes and relapses in susceptible patients.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — The HLA-DRB1*11 allele predisposes to acquired TTP by favoring presentation of ADAMTS13 peptides to T cells, helping break tolerance and license the autoantibodies that inhibit the enzyme.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — Long-lived anti-ADAMTS13 plasma cells survive on BCL-2 and escape rituximab, the rationale for proteasome-inhibitor or anti-CD38 plasma-cell-directed therapy in relapsing or refractory acquired TTP.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — Neutrophils releasing S100A8/A9 and extracellular traps (NETs) within the microvasculature amplify the platelet-VWF microthrombi of TTP, adding an innate-immune layer to the ADAMTS13-deficient thrombotic process.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — Disseminated platelet-VWF microthrombi occlude the microvasculature of TTP, and the resulting tissue hypoxia drives HIF-1α responses in brain, kidney and heart—the basis of its neurological and cardiac end-organ injury.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — VEGF maintains endothelial and glomerular health, and its blockade causes drug-induced thrombotic microangiopathy that mimics TTP—distinguishing VEGF-disruption TMA from the ADAMTS13-deficient disease.
- `connects-to` → **[BTK](../../03-molecular/btk/README.md)** — In acquired TTP, Bruton's tyrosine kinase relays B-cell-receptor signals in the autoreactive B cells that make anti-ADAMTS13 antibodies, an axis (with the CD20 cells and BAFF already mapped) of interest for B-cell-directed therapy.
- `connects-to` → **[CTLA-4](../../03-molecular/ctla-4/README.md)** — Impaired CTLA-4-dependent regulatory T-cell control underlies the loss of self-tolerance that permits the anti-ADAMTS13 autoantibody response of acquired TTP.
- `connects-to` → **[Thrombopoietin](../../03-molecular/thrombopoietin/README.md)** — The consumptive thrombocytopenia of TTP, as platelets are swept into microthrombi, drives a compensatory thrombopoietin response reflecting the high platelet turnover.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — Ang-2 release from activated endothelium amplifies the endothelial dysfunction of the thrombotic microangiopathy, promoting the microvascular platelet thrombosis of TTP.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR-MyD88-NF-κB innate signaling (TLR4 and NF-κB already mapped) contributes to the endothelial activation and inflammatory milieu that can trigger and amplify TTP episodes.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — IL-6-JAK-STAT3 signaling (IL-6 and STAT3 already mapped) participates in the systemic inflammatory response accompanying acute TTP.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — Complement activation generating C5a engages C5aR1 (C3 and C5 already mapped) to amplify the endothelial and platelet activation of the thrombotic microangiopathy in TTP.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Endothelial and platelet PI3K-AKT signaling shapes the activated, procoagulant phenotype that propagates the microvascular thrombosis of TTP.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling in platelets and endothelium amplifies the cellular activation driving the von-Willebrand-factor-rich microthrombi of TTP.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 promotes the neutrophil-extracellular-trap-driven thromboinflammation that contributes to the microvascular injury of TTP.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA released from NETs and lysed cells engages cGAS-STING, amplifying the type-I-interferon thromboinflammation of TTP.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling propagates the interferon-driven endothelial activation that aggravates the microvascular injury of TTP.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA) signaling in platelets and endothelium reinforces the activated, procoagulant phenotype that sustains the microthrombi of TTP.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO downstream of PI3K-AKT signaling (AKT and PIK3CA already mapped) regulates the survival of the autoantibody-producing B and plasma cells driving acquired thrombotic thrombocytopenic purpura.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the platelet-activation and inflammatory signaling relevant to the microthrombosis of thrombotic thrombocytopenic purpura.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated cytotoxicity contributes to the endothelial injury that provokes the von-Willebrand-factor release of thrombotic thrombocytopenic purpura.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family (LYN) kinase signaling downstream of the B-cell receptor participates in the autoreactive anti-ADAMTS13 B-cell response of immune thrombotic thrombocytopenic purpura.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR signaling in the autoreactive B and plasma cells participates in the immune process of thrombotic thrombocytopenic purpura.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the endothelial and immune-cell responses relevant to thrombotic thrombocytopenic purpura.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked endothelial metabolic signaling modulates the vascular homeostasis relevant to thrombotic thrombocytopenic purpura.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte recruitment contributes to the autoantibody-driven inflammation of acquired thrombotic thrombocytopenic purpura.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the autoreactive immune response in acquired thrombotic thrombocytopenic purpura.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the platelet and endothelial interactions relevant to thrombotic thrombocytopenic purpura.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the endothelial and immune activation relevant to thrombotic thrombocytopenic purpura.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the immune dysregulation of immune-mediated thrombotic thrombocytopenic purpura.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Cardiac microthrombosis: myocardial capillary platelet microthrombi in TTP release cardiac troponin, and troponin elevation on presentation predicts mortality, tying the systemic microangiopathy to the frequently fatal cardiac injury.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Adhesion anchor: von Willebrand factor (already mapped) normally binds subendothelial collagen to tether platelets at injury sites, the physiological adhesion axis that becomes pathological when uncleaved ultra-large multimers bind platelets under shear in TTP.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Platelet amplification: platelets recruited into the TTP microthrombi release thromboxane, a prostaglandin that amplifies aggregation and vasoconstriction, reinforcing the growing platelet plugs that occlude the microcirculation.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Dense-granule vasoconstrictor: platelets consumed into the TTP microthrombi release their stored serotonin, which constricts vessels and further activates platelets, adding a vasoactive component to the microvascular occlusion.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Pregnancy and female predominance: TTP is more common in women and can be precipitated by pregnancy, when rising oestrogen and falling ADAMTS13 (already mapped) activity combine to trigger the thrombotic microangiopathy.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Immune tolerance: PD-1 helps restrain the autoreactive response, and checkpoint-inhibitor cancer therapy has been reported to trigger acquired TTP by breaking tolerance to ADAMTS13, revealing this checkpoint's role in the autoimmunity.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immune regulation: the anti-inflammatory IL-10 and regulatory T cells (CTLA-4 already mapped) normally restrain the autoreactive response, and the tolerance defect allowing anti-ADAMTS13 (already mapped) autoantibodies reflects a failure of this immunoregulation in acquired TTP.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Type-2 autoantibody help: IL-4 and the Th2 response support the B cells (already mapped) that produce the inhibitory anti-ADAMTS13 autoantibodies driving acquired thrombotic thrombocytopenic purpura.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Haemolysis and oxidative stress: the microangiopathic haemolysis of TTP releases lactate dehydrogenase and, with the endothelial injury, generates oxidative stress to which xanthine oxidase contributes, marking the intravascular cell destruction.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Haemolysis and iron: the microangiopathic haemolysis of TTP fragments red cells (haemoglobin already mapped) into schistocytes, releasing iron and haem, part of the intravascular red-cell destruction that marks the disease.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 autoantibody help: IL-13, with IL-4 (already mapped), supports the B cells (already mapped) producing the inhibitory anti-ADAMTS13 autoantibodies that drive acquired thrombotic thrombocytopenic purpura.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Iron handling in haemolysis: the haem released by the microangiopathic haemolysis and the inflammation (IL-6 already mapped) disturb hepcidin-regulated iron handling, part of the altered iron biology of the intravascular destruction in TTP.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Autoimmune dysregulation: type-I interferon signalling is implicated in the loss of tolerance that permits the anti-ADAMTS13 (already mapped) autoantibody production of acquired thrombotic thrombocytopenic purpura.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, a pro-inflammatory adipokine, rises with the systemic inflammation (IL-6 already mapped) and endothelial activation of acute thrombotic thrombocytopenic purpura, part of its inflammatory milieu.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Plasma-exchange citrate: the citrate anticoagulant of the therapeutic plasma exchange central to TTP treatment chelates magnesium as well as calcium (already mapped), needing electrolyte replacement.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Cardiac microthrombi: the myocardial microthrombi of TTP cause the troponin (already mapped) rise, the arrhythmias and the sudden cardiac death, a leading cause of acute TTP mortality affecting the heart.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Immune-metabolic adipokine: leptin, with resistin (already mapped), is part of the adipokine milieu of the systemic inflammation (IL-6 already mapped) of acute thrombotic thrombocytopenic purpura.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin and resistin (already mapped), completes the adipokine dimension of the immune-metabolic milieu of thrombotic thrombocytopenic purpura.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 autoimmunity: the IFN-γ of the T cells is the type-II interferon arm (with the type-I interferon already mapped) of the immune dysregulation driving the anti-ADAMTS13 (already mapped) autoimmunity of acquired thrombotic thrombocytopenic purpura.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the autoimmune response against ADAMTS13 (already mapped) in thrombotic thrombocytopenic purpura.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Innate immune modulation: the NK cells (perforin already mapped) contribute to the innate immune dysregulation of the acquired autoimmune thrombotic thrombocytopenic purpura.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation of the acquired autoimmune thrombotic thrombocytopenic purpura.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune dysregulation underlying the anti-ADAMTS13 (already mapped) autoimmunity of thrombotic thrombocytopenic purpura.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the autoimmune thrombotic thrombocytopenic purpura.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Adaptive autoimmunity: the cytotoxic T cells (perforin already mapped), alongside the T-helper (already mapped) support of the anti-ADAMTS13 (already mapped) B-cell response, are part of the adaptive autoimmunity of thrombotic thrombocytopenic purpura.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Antioxidant micronutrient: selenium, a selenoprotein antioxidant cofactor, is part of the micronutrient dimension of the immune dysregulation of the autoimmune thrombotic thrombocytopenic purpura.
- `connects-to` → **[Vitamin D](../../../03-medicine/03-food/vitamin-d/README.md)** — Immunomodulatory vitamin: vitamin D modulates the T-cell (already mapped) autoimmunity, and its deficiency is part of the micronutrient dimension of the autoimmune thrombotic thrombocytopenic purpura.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) at the injured endothelium (already mapped), overlapping the complement-mediated microangiopathy that distinguishes TTP from atypical HUS.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement/contact regulation: the C1-esterase inhibitor regulates the classical complement and the contact-coagulation systems activated by the anti-ADAMTS13 (immunoglobulin already mapped) autoimmunity of thrombotic thrombocytopenic purpura.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Haemolytic iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the microangiopathic haemolysis of thrombotic thrombocytopenic purpura.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-driven autoimmunity: TSLP released from the injured platelet-rich endothelium (already mapped) of thrombotic thrombocytopenic purpura activates plasmacytoid dendritic cells and sustains the type-2 and anti-ADAMTS13 autoimmune response.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kallikrein-contact activation: bradykinin, generated by contact-pathway (C1-esterase inhibitor already mapped) activation on ULVWF-platelet thrombi, amplifies the vascular permeability and endothelial (already mapped) injury in thrombotic thrombocytopenic purpura.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Haemolytic anaemia support: erythropoietin corrects the microangiopathic haemolytic anaemia of thrombotic thrombocytopenic purpura refractory to plasma exchange, and EPO signalling may modulate the erythrocyte (already mapped) fragmentation kinetics.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell vascular permeability: histamine from mast cells activated in the inflamed TTP endothelium amplifies vascular permeability and contributes to the thrombocytopenic microangiopathy, complementing the bradykinin (already mapped) kinin axis.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Endothelial matrix remodelling: periostin is expressed in the vascular wall remodelled by ULVWF-mediated platelet aggregation in TTP, modulating integrin signalling on endothelial cells during the thrombotic microangiopathy.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Platelet circadian regulator: melatonin modulates platelet reactivity and platelet-endothelial interactions via melatonin receptors on platelets; reduced melatonin rhythmicity may amplify the platelet hyper-reactivity of TTP.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^george-2010-ttp-review]: George JN. Clinical practice. Thrombotic thrombocytopenic purpura. *N Engl J Med.* 2006;354(18):1927-1935. [doi:10.1056/NEJMcp053024](https://doi.org/10.1056/NEJMcp053024) · [PubMed 16672704](https://pubmed.ncbi.nlm.nih.gov/16672704/)
[^scully-2019-caplacizumab-hercules]: Scully M, Cataland SR, Peyvandi F, et al. Caplacizumab treatment for acquired thrombotic thrombocytopenic purpura. *N Engl J Med.* 2019;380(4):335-346. [doi:10.1056/NEJMoa1806311](https://doi.org/10.1056/NEJMoa1806311) · [PubMed 30625070](https://pubmed.ncbi.nlm.nih.gov/30625070/)
[^coppo-2019-rituximab-ttp]: Coppo P, Busson M, Veyradier A, et al. HLA-DRB1*11: a strong risk factor for acquired severe ADAMTS13 deficiency-related thrombotic thrombocytopenic purpura in Caucasians. *J Thromb Haemost.* 2010;8(11):2466-2469. [doi:10.1111/j.1538-7836.2010.04028.x](https://doi.org/10.1111/j.1538-7836.2010.04028.x) · [PubMed 20735727](https://pubmed.ncbi.nlm.nih.gov/20735727/)
