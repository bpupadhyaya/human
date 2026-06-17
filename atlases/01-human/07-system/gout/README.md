---
schema: human-scale-entry/v1
id: gout
name: Gout
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Inflammatory arthritis from monosodium urate (MSU) crystal deposition; hyperuricemia → crystals → NLRP3 inflammasome → IL-1beta → neutrophil-driven acute flares. Colchicine, NSAIDs, and IL-1 inhibitors treat flares; allopurinol and febuxostat reduce urate."
aliases: ["gouty arthritis", "hyperuricemia", "tophaceous gout", "MSU crystallopathy", "podagra"]
sources:
  - id: dalbeth-2019-gout-primer
    type: peer-reviewed
    cite: "Dalbeth N, Choi HK, Joosten LAB, et al. Gout. Nat Rev Dis Primers. 2019;5(1):69."
    doi: "10.1038/s41572-019-0115-y"
    pmid: "31558729"
    url: "https://doi.org/10.1038/s41572-019-0115-y"
  - id: martinon-2006-nlrp3-gout
    type: peer-reviewed
    cite: "Martinon F, Pétrilli V, Mayor A, Tardivel A, Tschopp J. Gout-associated uric acid crystals activate the NALP3 inflammasome. Nature. 2006;440(7081):237-241."
    doi: "10.1038/nature04516"
    pmid: "16407889"
    url: "https://doi.org/10.1038/nature04516"
  - id: fitzgerald-2020-acr-gout
    type: peer-reviewed
    cite: "FitzGerald JD, Dalbeth N, Mikuls T, et al. 2020 American College of Rheumatology Guideline for the Management of Gout. Arthritis Care Res (Hoboken). 2020;72(6):744-760."
    doi: "10.1002/acr.24180"
    pmid: "32391934"
    url: "https://doi.org/10.1002/acr.24180"
cross_links:
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "MSU crystals are a canonical NLRP3 activator: lysosomal destabilization → cathepsin B release → NLRP3-ASC-caspase-1 activation → IL-1beta and IL-18 secretion; IL-1 blockade (anakinra, canakinumab) rapidly resolves refractory gouty flares."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Synovial macrophages phagocytose MSU crystals → NLRP3 → IL-1beta; surface-activated macrophages produce IL-6, TNF-alpha, CXCL1 → neutrophil recruitment; colchicine blocks macrophage microtubule-dependent NLRP3 assembly and inflammasome activation."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils are the primary effectors of acute gout: IL-8/CXCL1 → neutrophil influx → MSU crystal phagocytosis → ROS and proteases → tissue damage; colchicine inhibits neutrophil migration and crystal phagocytosis via microtubule disruption."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "MSU crystals activate NF-kB in macrophages and synoviocytes via TLR4 and NLRP3 → IL-6, IL-8, TNF-alpha, COX-2 → synovial inflammation; NF-kB drives both acute flare cytokines and chronic tophus-associated synovial tissue remodeling."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Xanthine oxidase converts xanthine → uric acid; serum urate >6.8 mg/dL exceeds solubility threshold → MSU crystal nucleation in joints and soft tissue → phagocytosis by neutrophils and macrophages → NLRP3 activation → acute gouty flare; allopurinol/febuxostat target XOR."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β is the central acute gout mediator: MSU crystals → NLRP3 → caspase-1 → IL-1β → neutrophil influx and arthritis; anakinra (off-label) and canakinumab (EMA approved 2013 for gout flares) target IL-1β in refractory flares unresponsive to colchicine/NSAIDs."
  - target: 03-medicine/01-modern/12-anti-inflammatory/ibuprofen
    relation: treated-by
    note: "NSAIDs including ibuprofen are first-line for acute gout (ACR 2020 guidelines): COX-2-driven PGE₂ amplifies NLRP3-IL-1β neutrophil recruitment to MSU crystals; 600–800 mg TDS × 7–10 days effective; contraindicated in eGFR <30."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "Gout and hypertension are tightly linked: hyperuricemia independently raises blood pressure (urate impairs endothelial NO and activates the RAAS), while thiazide/loop diuretics for HTN raise serum urate and trigger gout flares — a two-way interaction that complicates treatment."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "The kidney is central to gout: it excretes ~two-thirds of uric acid, so reduced urate clearance (URAT1/GLUT9 variants, CKD, diuretics) is the main cause of hyperuricemia; conversely MSU crystals damage the kidney (urate nephropathy, stones), so gout and CKD reinforce each other."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Gout is the most common inflammatory arthritis: MSU crystals deposit in cooler peripheral joints — classically the first metatarsophalangeal joint (podagra) — igniting excruciating attacks, and over years form tophi that erode bone and cartilage if urate isn't lowered."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Gout and chronic kidney disease feed each other: reduced renal urate excretion raises serum urate to cause gout, while urate crystals and inflammation injure the kidney; CKD also limits NSAID and colchicine use, so urate-lowering with allopurinol must be dose-adjusted."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Gout is a core feature of metabolic syndrome anchored by obesity: adiposity and insulin resistance raise serum urate by cutting renal excretion and boosting purine turnover, so weight loss lowers urate and flares; gout clusters with type 2 diabetes, hypertension and fatty liver."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Hyperuricemia and gout independently raise cardiovascular risk: urate crystals and NLRP3-driven inflammation promote endothelial dysfunction and atherosclerosis, and gout patients have excess MI and stroke—part of why gout is seen as a vascular as well as joint disease."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Gout is literally a sodium disease: when uric acid exceeds its solubility it crystallizes as monosodium urate, and these needle-shaped MSU crystals deposited in joints and tophi trigger the NLRP3-driven inflammation—dissolving them by lowering urate is the cure."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Gout and rheumatoid arthritis are both inflammatory arthritides but distinct: gout is a crystal-driven (MSU) innate attack with acute monoarticular flares, while RA is an autoantibody-driven symmetric polyarthritis—aspiration versus serology separates them."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Gout clusters with type 2 diabetes in the metabolic syndrome: insulin resistance reduces renal uric-acid excretion, raising urate, while obesity and high-purine, fructose-rich diets drive both—gout often flags an underlying cardiometabolic disorder."
  - target: 01-human/07-system/alcohol-use-disorder
    relation: connects-to
    note: "Alcohol is a classic gout trigger: beer (rich in purines) and spirits raise uric acid by boosting production and blocking renal excretion, so binges precipitate acute attacks—making alcohol moderation a core part of gout prevention."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Gout signals and worsens heart disease: hyperuricemia and urate-crystal inflammation track with hypertension, coronary disease and higher cardiovascular mortality, so a gout diagnosis flags cardiovascular risk—and shared drivers like obesity link the two."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Gout has a calcium-crystal mimic, pseudogout: where gout deposits monosodium urate crystals, pseudogout (CPPD) deposits calcium pyrophosphate, causing similar acute joint inflammation—so polarized-light crystal analysis distinguishes the two arthritides."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Gout is strongly tied to cardiovascular disease: hyperuricemia and the chronic inflammation of gout independently raise the risk of hypertension, coronary disease and stroke, so gout flags cardiovascular risk beyond its joint and kidney damage."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "The renal system both causes and suffers from gout: under-excretion of urate by the kidney is the main reason uric acid rises, and deposited crystals form kidney stones and urate nephropathy—so gout and kidney disease drive each other in a vicious cycle."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Tophi are the chronic granulomas of gout: persistent urate crystals provoke macrophages and fibroblasts to wall them off in firm, fibrous nodular deposits in joints and soft tissue, so fibroblast-rich tophi mark long-standing, undertreated disease."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "Gout is a disease of nitrogen waste: uric acid is the nitrogen-rich end-product of purine breakdown that humans, lacking uricase, cannot degrade further, so this evolutionary loss leaves urate to crystallize in joints when it builds up."
  - target: 01-human/07-system/myeloproliferative-neoplasms
    relation: connects-to
    note: "Myeloproliferative neoplasms cause secondary gout: massive cell turnover in polycythemia vera and related disorders floods the blood with purines and urate, so gout flares can be the first clue to an underlying blood-cell overproduction."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Chronic gout deposits in the skin as tophi: long-standing high urate forms chalky subcutaneous nodules over joints and ears that can ulcerate and discharge crystals, so visible tophi mark years of untreated disease."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Gout flares can be quelled with cortisol: when NSAIDs and colchicine are unsafe—as in kidney disease—corticosteroids (oral or injected into the joint) calm the crystal-driven inflammation, a key fallback for treating an acute attack."
  - target: 01-human/04-cellular/osteoclast
    relation: connects-to
    note: "Chronic tophaceous gout erodes bone via osteoclasts: long-standing urate deposits activate bone-resorbing osteoclasts, carving the 'punched-out' periarticular erosions seen on X-ray that distinguish advanced gout from other arthritis."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Gout traces back to purine metabolism through adenosine: breaking down adenosine and other purines yields uric acid, so a high turnover of these nucleotides—from diet or cell breakdown—feeds the hyperuricemia that precipitates urate crystals."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "The gut shares the job of clearing urate with the kidney: about a third of uric acid is excreted into the intestine, so gut transporters and microbes that break down urate influence blood levels—and impaired gut excretion can worsen gout."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 helps inflame the gouty joint: alongside IL-1beta, urate crystals trigger IL-6 release that amplifies the fever, pain and swelling of an acute attack, part of the cytokine cascade targeted to calm flares."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells help ignite the gout flare: they take up monosodium urate crystals and, with macrophages, activate the inflammasome and prime the inflammatory response that turns crystal deposition into a sudden painful attack."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "Acid urine turns gout into kidney stones: uric acid dissolves poorly when urine is acidic, so a low urinary pH lets it crystallize into stones, which is why alkalinizing the urine helps prevent them."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Chronic gout lays down fibrosis: long-standing tophi become fibrous nodules that erode joints, and persistent urate in the kidney drives interstitial scarring, the lasting damage beyond the acute flare."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells help fire the first hours of a gout attack: urate crystals trigger them to release histamine and mediators that dilate vessels and recruit neutrophils, kicking off the sudden inflammation."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Gout is confirmed by light: polarized-light microscopy of joint fluid reveals the negatively birefringent urate needles, and dual-energy CT photons map urate deposits without a tap."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Gout can spring from the marrow: myeloproliferative diseases and their rapid cell turnover flood the blood with purines that become uric acid, a secondary cause of the disease."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Gout can deposit in the eye: urate tophi form on the eyelids and conjunctiva and rarely inflame the sclera, an unusual but recognized site of crystal deposition."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron and polarized-light microscopy clinch the gout diagnosis: aspirated joint fluid shows needle-shaped monosodium urate crystals, negatively birefringent and packed into the tophi that the inflammasome attacks."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver makes the uric acid that crystallizes in gout: it is the main site where xanthine oxidase breaks purines down to urate, so the liver's metabolism — fueled by fructose and alcohol — sets the blood level."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Low magnesium tracks with gout: deficiency is common in the metabolic syndrome that accompanies it and is linked to higher uric acid, so magnesium status is part of the metabolic picture behind the crystals."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "Treating the flare punishes the gut: colchicine causes diarrhea and the NSAIDs used for acute gout inflame the stomach into gastritis and ulcers, so the drugs that quell the joint must be balanced against the bowel."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "Body fat fuels hyperuricemia: adipose tissue's inflammation and the insulin resistance of obesity cut the kidney's excretion of urate, which is why weight gain raises uric acid and weight loss helps lower it."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "Gout rides with insulin resistance: the hyperinsulinemia of metabolic syndrome makes the kidney retain urate, tying the pancreatic insulin axis to the crystals — and gout flags a higher risk of type 2 diabetes."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Estrogen shields women from gout: the hormone is uricosuric, helping the kidney dump urate, so gout is uncommon before menopause and its incidence in women climbs once that protection is lost."
  - target: 01-human/07-system/psoriasis
    relation: connects-to
    note: "Rapid skin turnover feeds the urate pool: psoriasis's accelerated proliferation breaks down purines into extra uric acid, so gout is more common in psoriasis — and the two arthritides can be hard to tell apart in an inflamed joint."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Crystals also rouse the complement system: monosodium urate activates complement on its surface, generating C5a that pulls neutrophils into the joint — an arm of the acute flare working alongside the NLRP3-IL-1 pathway."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "TNF amplifies the crystal storm: released by activated macrophages alongside IL-1β, it deepens the recruitment and activation of neutrophils that make the gout flare so exquisitely painful."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Urate injures the vessel lining: high uric acid impairs endothelial nitric-oxide and promotes inflammation, a mechanism tying gout to the hypertension and cardiovascular disease that shadow it."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "The gut is gout's second drain: about a third of uric acid is excreted through the intestine via the ABCG2 transporter, so impaired gut elimination — not just the kidney — can raise urate into gout."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Insulin resistance fuels hyperuricemia: high insulin tells the kidney to retain urate, so the hyperinsulinemia of metabolic syndrome raises uric acid into gout — one reason gout clusters with obesity and type 2 diabetes."
  - target: 01-human/07-system/polycythemia-vera
    relation: connects-to
    note: "High cell turnover overproduces urate: the expanded marrow of polycythemia vera and other myeloproliferative disease floods the blood with purines, causing a secondary gout that can be the presenting clue to the hematologic disorder."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Hyperuricemia is an independent vascular risk: beyond its joint disease, elevated urate promotes endothelial dysfunction and is associated with a raised risk of stroke, part of gout's broader cardiovascular shadow."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Urate and the failing heart feed each other: hyperuricemia independently predicts heart failure and worsens its outcomes, while the disease and its diuretics raise urate — a bidirectional link in gout's cardiovascular burden."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "A hot joint forces a critical question: acute gout closely mimics septic arthritis, which must be excluded by joint aspiration because a missed joint infection can seed sepsis, and tophi themselves can become infected."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Gouty inflammation tips toward clotting: the systemic inflammation of gout and hyperuricemia is associated with a higher risk of venous thromboembolism, adding a venous dimension to its vascular complications."
  - target: 01-human/07-system/nash
    relation: connects-to
    note: "Hyperuricemia and fatty liver cluster: gout sits squarely in the metabolic syndrome, and its insulin resistance and fructose metabolism strongly associate it with non-alcoholic steatohepatitis."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Recurrent disabling pain weighs on mood: the unpredictable, intensely painful flares and chronic joint damage of tophaceous gout reduce quality of life and carry an elevated rate of depression."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Chronic inflammation and renal disease lower the count: longstanding tophaceous gout's persistent inflammation, compounded by the chronic kidney disease that so often accompanies it, can produce an anemia of chronic disease."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Tophi erode through the skin: large chronic tophi can ulcerate and discharge chalky urate, leaving open wounds over joints that are slow to heal and prone to infection."
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: connects-to
    note: "Ulcerated tophi invite Staph: when a tophus breaks through the skin, Staphylococcus aureus readily colonizes and infects it, risking cellulitis, septic arthritis and bloodstream infection."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Chronic inflammation and immobility cost bone: longstanding gout's persistent inflammation, joint damage and reduced mobility are associated with lower bone density and a raised fracture risk."
---

# Gout

## Overview

**Gout** is the most common inflammatory arthritis in adults, affecting ~4% of adults in Western countries (>41 million affected globally). It is caused by **monosodium urate (MSU) crystal deposition** in joints and periarticular tissues, driven by chronic **hyperuricemia** (serum urate >6.8 mg/dL, the saturation threshold for MSU crystallization at physiological pH and temperature) [^dalbeth-2019-gout-primer].

**The gout spectrum:**
- **Asymptomatic hyperuricemia:** Elevated serum urate without crystals or gout; not routinely treated but associated with incident gout, CKD, hypertension, and cardiovascular events over time
- **Acute gouty arthritis (flare):** Sudden-onset, severely painful joint inflammation; typically monoarticular initially (classically first metatarsophalangeal joint = podagra ~50%); self-limiting (3-10 days without treatment)
- **Intercritical gout:** Asymptomatic period between flares; MSU crystals persist in joints; progressive joint damage accumulates with recurrent flares
- **Chronic tophaceous gout:** Tophi (MSU crystal deposits in periarticular soft tissue, subcutaneous tissue, olecranon bursa, auricles, tendons) → joint destruction, deformity, functional impairment; urate-lowering therapy (ULT) can dissolve tophi over months-years

**Hyperuricemia mechanisms:**
- **Underexcretion (~90% of gout):** Impaired renal urate excretion; major genetic contributors: ABCG2 (urate transporter, gout risk alleles), SLC22A12 (URAT1, urate reabsorber in proximal tubule — target of benzbromarone, probenecid), SLC2A9 (GLUT9); risk factors: CKD, diuretics (thiazide, loop → compete with urate for renal tubular secretion), cyclosporine, low-dose aspirin
- **Overproduction (~10% of gout):** Purine overproduction from rapid cell turnover (myeloproliferative disease, tumor lysis syndrome), HPRT1 deficiency (Lesch-Nyhan syndrome), PRPP synthetase superactivity; dietary purines (meat, seafood, organ meats, fructose-sweetened beverages — fructose → rapid ATP consumption → AMP → uric acid)
- **Alcohol:** Ethanol → lactate → blocks urate renal excretion; beer contains purines; wine less strongly associated
- **Comorbidities:** CKD, hypertension, metabolic syndrome, obesity, type 2 diabetes — all associated with hyperuricemia; gout disproportionately affects men (estrogen promotes uricosuria → lower serum urate in premenopausal women) and postmenopausal women

## Structure

### NLRP3 inflammasome activation by MSU crystals [^martinon-2006-nlrp3-gout]

The central mechanism linking MSU crystals to acute gouty arthritis is **NLRP3 inflammasome activation** — first definitively demonstrated in macrophages by Martinon and Tschopp in 2006 [^martinon-2006-nlrp3-gout].

**Mechanism:**
1. MSU crystals phagocytosed by synovial macrophages → crystals rupture phagolysosomes → **lysosomal destabilization** → cytosolic cathepsin B release → NLRP3 oligomerization
2. Crystal surface-mediated ROS generation (NADPH oxidase-dependent) + cholesterol crystal co-stimulation → additional NLRP3 priming
3. Potassium efflux (crystals insert into plasma membrane → K⁺ channels) → NLRP3 conformational change → ASC pyroptosome assembly → caspase-1 autoactivation
4. Active caspase-1 → IL-1beta (pro-IL-1beta → mature IL-1beta) + IL-18 + gasdermin D (pore formation → pyroptosis in some macrophages)
5. **IL-1beta** is the central acute gout mediator: binds synovial fibroblast and endothelial IL-1R1 → NF-kB → IL-6, IL-8 (CXCL8), ICAM-1 → massive neutrophil influx

**Two-signal model for maximal inflammasome activation:**
- **Signal 1 (priming):** TLR4/TLR2 ligands (MSU crystal surface, urate at lower concentrations, LPS co-stimulation) → NF-kB → pro-IL-1beta, NLRP3, and ASC transcription
- **Signal 2 (activation):** MSU crystal phagocytosis → lysosomal rupture → NLRP3 activation

**Resolution of acute gout (spontaneous within 7-10 days):**
- Neutrophils undergo NET formation and apoptosis → efferocytosis by macrophages → anti-inflammatory macrophage polarization → IL-10, TGF-beta → resolution
- Lipid mediators: transition from pro-inflammatory prostaglandins and leukotrienes → pro-resolving lipoxins and resolvins → self-limited flare

### Crystal properties

- MSU crystals: needle-shaped (monosodium urate monohydrate), negatively birefringent under polarized light (gold/yellow parallel to polarizer) — diagnostic by synovial fluid microscopy; length 2-20 μm
- CPPD crystals (calcium pyrophosphate, pseudogout): rhomboid-shaped, weakly positively birefringent — distinct from gout; associated with OA, hemochromatosis, hyperparathyroidism

## Function

### Clinical presentation

**Acute gouty flare:**
- Sudden, severe pain (often awakening at night), swelling, erythema, warmth → maximal intensity within 12-24 hours
- First MTP joint (podagra) most common; also ankle, midfoot, knee; wrist, finger (less common initially; more frequent in patients on diuretics, transplant recipients)
- **Fever** (low-grade) and leukocytosis may be present → mimics septic arthritis (always aspirate if uncertain; gout and septic arthritis can co-exist)
- Precipitating triggers: alcohol (especially beer), dietary purine load, dehydration, illness/surgery (acute serum urate change), starting or stopping ULT (crystal mobilization)

**Tophi:**
- Whitish chalk-like deposits in periarticular tissue, extensor surfaces, olecranon bursa, ear cartilage (helix), tendons (Achilles, finger tendons)
- MSU crystal aggregates surrounded by chronic granulomatous inflammation; may ulcerate and drain chalky material; can destroy cartilage and bone
- **DECT (dual-energy CT):** Differentiates MSU (green coding) from calcium crystals → non-invasive tophus detection and monitoring; superior to ultrasound and plain X-ray for tophus burden

**Radiographic findings (late disease):**
- Punched-out erosions with sclerotic margins and overhanging edges (Martel sign) — pathognomonic for tophaceous gout; first MTP most common
- Tophaceous deposits as soft-tissue opacities; cartilage and joint space often preserved until late (unlike OA/RA)

## Pathology

### Diagnosis

**Gold standard:** Synovial fluid or tophus aspiration → polarized light microscopy demonstrating needle-shaped, negatively birefringent MSU crystals within or adjacent to neutrophils during acute flare.

**2015 ACR/EULAR Gout Classification Criteria:** Score-based (score ≥8/23 = gout); domains: clinical (joint involvement, synovitis characteristics), laboratory (serum urate, leukocytes in synovial fluid), imaging (ultrasound double contour sign, DECT urate deposits, X-ray erosions). Crystal demonstration = definitive classification regardless of score.

**Serum urate:** Cannot rule out gout during acute flare (urate may be normal or low during acute flare due to acute phase response → uricosuria); repeat when patient has recovered.

**Ultrasonography:** Double contour sign (urate coating on cartilage) and snowstorm appearance (hyperechoic foci in synovial fluid) — sensitive and specific for MSU deposits.

### Treatment [^fitzgerald-2020-acr-gout]

**Acute flare treatment:**
- **Colchicine (low-dose, 1.2 mg then 0.6 mg 1 hour later):** First-line; tubulin polymerization inhibitor → inhibits neutrophil chemotaxis, NLRP3 inflammasome assembly (microtubule-dependent), and inflammasome-mediated IL-1beta secretion; must be initiated within 36 hours of flare onset for maximal effect; avoid in severe renal/hepatic impairment; CYP3A4/P-gp substrate
- **NSAIDs (indomethacin, naproxen, celecoxib):** First-line alternative; COX inhibition → reduced prostaglandin-mediated vasodilation and pain; avoid in CKD, heart failure, GI ulcer history
- **Corticosteroids (prednisone 30-40 mg/day × 5-7 days):** Preferred when colchicine and NSAIDs are contraindicated (e.g., severe CKD, anticoagulated patients); intra-articular triamcinolone effective for monoarthritis
- **IL-1 inhibitors:** Anakinra (anti-IL-1R), canakinumab (anti-IL-1beta) → highly effective in recurrent refractory gout; canakinumab (Novartis) approved in EU for gout flares; anakinra used off-label; especially valuable in transplant patients (colchicine and NSAIDs contraindicated due to immunosuppressants and renal function)

**Urate-lowering therapy (ULT) — for recurrent or tophaceous gout:**
- **Indications (2020 ACR):** ≥2 flares/year, 1+ tophi, radiographic evidence of joint damage from gout, serum urate >9 mg/dL, or uric acid nephrolithiasis
- **Target serum urate:** <6 mg/dL (<5 mg/dL in tophaceous gout) for crystal dissolution
- **Allopurinol (xanthine oxidase inhibitor):** First-line; blocks urate synthesis; start low (100 mg/day) → titrate monthly to target; HLA-B*5801 screening required before use in Asian patients (SJS/TENS risk: 1-2% in HLA-B*5801 carriers); dose adjust for eGFR; drug interactions: azathioprine (XO inactivation → azathioprine toxicity → reduce azathioprine dose 75% if co-prescribed)
- **Febuxostat (Uloric):** Non-purine XO inhibitor; more potent than allopurinol at equivalent doses; CARES trial: non-inferior to allopurinol for gout endpoints but possible increased CV mortality signal → now boxed warning; reserved for allopurinol-intolerant patients
- **Uricosurics:** Probenecid (URAT1 inhibitor), benzbromarone (uricosuric, not available in US) — increase renal urate excretion; less effective in CKD; avoided with nephrolithiasis history
- **Pegloticase (Krystexxa):** Pegylated recombinant uricase; converts urate → allantoin (soluble) → dramatic serum urate lowering; IV Q2W; for refractory/tophaceous gout; anti-drug antibodies → loss of efficacy and infusion reactions in ~40%; co-administration with methotrexate reduces immunogenicity and improves durability (MIRROR trial); G6PD testing required (hemolysis risk)
- **Flare prophylaxis during ULT initiation (mandatory for ≥3-6 months):** Low-dose colchicine (0.6 mg QD-BID) or NSAID; urate mobilization from established deposits during ULT initiation triggers flares; this prophylaxis sharply reduces flare incidence during the critical ULT initiation period

## Connections

- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — MSU crystals are a canonical NLRP3 activator: lysosomal destabilization → cathepsin B → NLRP3-ASC-caspase-1 → IL-1beta secretion; IL-1 blockade (anakinra, canakinumab) rapidly resolves refractory gouty flares.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Synovial macrophages phagocytose MSU crystals → NLRP3 → IL-1beta; surface-activated macrophages produce IL-6, TNF-alpha, CXCL1 → neutrophil recruitment; colchicine blocks macrophage microtubule-dependent NLRP3 assembly.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Neutrophils are the primary effectors of acute gout: IL-8/CXCL1 → neutrophil influx → MSU crystal phagocytosis → ROS and proteases → tissue damage; colchicine inhibits neutrophil migration and crystal phagocytosis via microtubule disruption.
- `connects-to` → **[NF-kB](../../03-molecular/nf-kb/README.md)** — MSU crystals activate NF-kB in macrophages and synoviocytes via TLR4 → IL-6, IL-8, TNF-alpha, COX-2 → synovial inflammation; NF-kB drives both acute flare cytokines and chronic tophus-associated tissue remodeling.
- `connects-to` → **[Xanthine Oxidase](../../03-molecular/xanthine-oxidase/README.md)** — xanthine oxidase converts xanthine → uric acid; serum urate >6.8 mg/dL exceeds solubility threshold → MSU crystal nucleation in joints and soft tissue → phagocytosis by neutrophils and macrophages → NLRP3 activation → acute gouty flare; allopurinol/febuxostat target XOR.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β is the central acute gout mediator: MSU crystals → NLRP3 → caspase-1 → IL-1β → neutrophil influx and arthritis; anakinra (off-label) and canakinumab (EMA approved 2013 for gout flares) target IL-1β in refractory flares unresponsive to colchicine/NSAIDs.
- `treated-by` → **[Ibuprofen](../../../03-medicine/01-modern/12-anti-inflammatory/ibuprofen/README.md)** — NSAIDs including ibuprofen are first-line for acute gout (ACR 2020 guidelines): COX-2-driven PGE₂ amplifies NLRP3-IL-1β neutrophil recruitment to MSU crystals; 600–800 mg TDS × 7–10 days effective; contraindicated in eGFR <30.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — Gout and hypertension are tightly linked: hyperuricemia independently raises blood pressure (urate impairs endothelial NO and activates the RAAS), while thiazide/loop diuretics for HTN raise serum urate and trigger gout flares — a two-way interaction that complicates treatment.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — The kidney is central to gout: it excretes ~two-thirds of uric acid, so reduced urate clearance (URAT1/GLUT9 variants, CKD, diuretics) is the main cause of hyperuricemia; conversely MSU crystals damage the kidney (urate nephropathy, stones), so gout and CKD reinforce each other.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Gout is the most common inflammatory arthritis: MSU crystals deposit in cooler peripheral joints — classically the first metatarsophalangeal joint (podagra) — igniting excruciating attacks, and over years form tophi that erode bone and cartilage if urate isn't lowered.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Gout and chronic kidney disease feed each other: reduced renal urate excretion raises serum urate to cause gout, while urate crystals and inflammation injure the kidney; CKD also limits NSAID and colchicine use, so urate-lowering with allopurinol must be dose-adjusted.
- `connects-to` → **[Obesity](../obesity/README.md)** — Gout is a core feature of metabolic syndrome anchored by obesity: adiposity and insulin resistance raise serum urate by cutting renal excretion and boosting purine turnover, so weight loss lowers urate and flares; gout clusters with type 2 diabetes, hypertension and fatty liver.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Hyperuricemia and gout independently raise cardiovascular risk: urate crystals and NLRP3-driven inflammation promote endothelial dysfunction and atherosclerosis, and gout patients have excess MI and stroke—part of why gout is seen as a vascular as well as joint disease.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Gout is literally a sodium disease: when uric acid exceeds its solubility it crystallizes as monosodium urate, and these needle-shaped MSU crystals deposited in joints and tophi trigger the NLRP3-driven inflammation—dissolving them by lowering urate is the cure.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Gout and rheumatoid arthritis are both inflammatory arthritides but distinct: gout is a crystal-driven (MSU) innate attack with acute monoarticular flares, while RA is an autoantibody-driven symmetric polyarthritis—aspiration versus serology separates them.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Gout clusters with type 2 diabetes in the metabolic syndrome: insulin resistance reduces renal uric-acid excretion, raising urate, while obesity and high-purine, fructose-rich diets drive both—gout often flags an underlying cardiometabolic disorder.
- `connects-to` → **[Alcohol Use Disorder](../alcohol-use-disorder/README.md)** — Alcohol is a classic gout trigger: beer (rich in purines) and spirits raise uric acid by boosting production and blocking renal excretion, so binges precipitate acute attacks—making alcohol moderation a core part of gout prevention.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Gout signals and worsens heart disease: hyperuricemia and urate-crystal inflammation track with hypertension, coronary disease and higher cardiovascular mortality, so a gout diagnosis flags cardiovascular risk—and shared drivers like obesity link the two.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Gout has a calcium-crystal mimic, pseudogout: where gout deposits monosodium urate crystals, pseudogout (CPPD) deposits calcium pyrophosphate, causing similar acute joint inflammation—so polarized-light crystal analysis distinguishes the two arthritides.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — Gout is strongly tied to cardiovascular disease: hyperuricemia and the chronic inflammation of gout independently raise the risk of hypertension, coronary disease and stroke, so gout flags cardiovascular risk beyond its joint and kidney damage.
- `connects-to` → **[Renal System](../renal-system/README.md)** — The renal system both causes and suffers from gout: under-excretion of urate by the kidney is the main reason uric acid rises, and deposited crystals form kidney stones and urate nephropathy—so gout and kidney disease drive each other in a vicious cycle.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Tophi are the chronic granulomas of gout: persistent urate crystals provoke macrophages and fibroblasts to wall them off in firm, fibrous nodular deposits in joints and soft tissue, so fibroblast-rich tophi mark long-standing, undertreated disease.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — Gout is a disease of nitrogen waste: uric acid is the nitrogen-rich end-product of purine breakdown that humans, lacking uricase, cannot degrade further, so this evolutionary loss leaves urate to crystallize in joints when it builds up.
- `connects-to` → **[Myeloproliferative Neoplasms](../myeloproliferative-neoplasms/README.md)** — Myeloproliferative neoplasms cause secondary gout: massive cell turnover in polycythemia vera and related disorders floods the blood with purines and urate, so gout flares can be the first clue to an underlying blood-cell overproduction.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Chronic gout deposits in the skin as tophi: long-standing high urate forms chalky subcutaneous nodules over joints and ears that can ulcerate and discharge crystals, so visible tophi mark years of untreated disease.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Gout flares can be quelled with cortisol: when NSAIDs and colchicine are unsafe—as in kidney disease—corticosteroids (oral or injected into the joint) calm the crystal-driven inflammation, a key fallback for treating an acute attack.
- `connects-to` → **[Osteoclast](../../04-cellular/osteoclast/README.md)** — Chronic tophaceous gout erodes bone via osteoclasts: long-standing urate deposits activate bone-resorbing osteoclasts, carving the 'punched-out' periarticular erosions seen on X-ray that distinguish advanced gout from other arthritis.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Gout traces back to purine metabolism through adenosine: breaking down adenosine and other purines yields uric acid, so a high turnover of these nucleotides—from diet or cell breakdown—feeds the hyperuricemia that precipitates urate crystals.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — The gut shares the job of clearing urate with the kidney: about a third of uric acid is excreted into the intestine, so gut transporters and microbes that break down urate influence blood levels—and impaired gut excretion can worsen gout.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6 helps inflame the gouty joint: alongside IL-1beta, urate crystals trigger IL-6 release that amplifies the fever, pain and swelling of an acute attack, part of the cytokine cascade targeted to calm flares.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells help ignite the gout flare: they take up monosodium urate crystals and, with macrophages, activate the inflammasome and prime the inflammatory response that turns crystal deposition into a sudden painful attack.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — Acid urine turns gout into kidney stones: uric acid dissolves poorly when urine is acidic, so a low urinary pH lets it crystallize into stones, which is why alkalinizing the urine helps prevent them.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Chronic gout lays down fibrosis: long-standing tophi become fibrous nodules that erode joints, and persistent urate in the kidney drives interstitial scarring, the lasting damage beyond the acute flare.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells help fire the first hours of a gout attack: urate crystals trigger them to release histamine and mediators that dilate vessels and recruit neutrophils, kicking off the sudden inflammation.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Gout is confirmed by light: polarized-light microscopy of joint fluid reveals the negatively birefringent urate needles, and dual-energy CT photons map urate deposits without a tap.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Gout can spring from the marrow: myeloproliferative diseases and their rapid cell turnover flood the blood with purines that become uric acid, a secondary cause of the disease.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Gout can deposit in the eye: urate tophi form on the eyelids and conjunctiva and rarely inflame the sclera, an unusual but recognized site of crystal deposition.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron and polarized-light microscopy clinch the gout diagnosis: aspirated joint fluid shows needle-shaped monosodium urate crystals, negatively birefringent and packed into the tophi that the inflammasome attacks.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver makes the uric acid that crystallizes in gout: it is the main site where xanthine oxidase breaks purines down to urate, so the liver's metabolism — fueled by fructose and alcohol — sets the blood level.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Low magnesium tracks with gout: deficiency is common in the metabolic syndrome that accompanies it and is linked to higher uric acid, so magnesium status is part of the metabolic picture behind the crystals.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — Treating the flare punishes the gut: colchicine causes diarrhea and the NSAIDs used for acute gout inflame the stomach into gastritis and ulcers, so the drugs that quell the joint must be balanced against the bowel.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — Body fat fuels hyperuricemia: adipose tissue's inflammation and the insulin resistance of obesity cut the kidney's excretion of urate, which is why weight gain raises uric acid and weight loss helps lower it.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — Gout rides with insulin resistance: the hyperinsulinemia of metabolic syndrome makes the kidney retain urate, tying the pancreatic insulin axis to the crystals — and gout flags a higher risk of type 2 diabetes.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Estrogen shields women from gout: the hormone is uricosuric, helping the kidney dump urate, so gout is uncommon before menopause and its incidence in women climbs once that protection is lost.
- `connects-to` → **[Psoriasis](../psoriasis/README.md)** — Rapid skin turnover feeds the urate pool: psoriasis's accelerated proliferation breaks down purines into extra uric acid, so gout is more common in psoriasis — and the two arthritides can be hard to tell apart in an inflamed joint.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Crystals also rouse the complement system: monosodium urate activates complement on its surface, generating C5a that pulls neutrophils into the joint — an arm of the acute flare working alongside the NLRP3-IL-1 pathway.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — TNF amplifies the crystal storm: released by activated macrophages alongside IL-1β, it deepens the recruitment and activation of neutrophils that make the gout flare so exquisitely painful.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Urate injures the vessel lining: high uric acid impairs endothelial nitric-oxide and promotes inflammation, a mechanism tying gout to the hypertension and cardiovascular disease that shadow it.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — The gut is gout's second drain: about a third of uric acid is excreted through the intestine via the ABCG2 transporter, so impaired gut elimination — not just the kidney — can raise urate into gout.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Insulin resistance fuels hyperuricemia: high insulin tells the kidney to retain urate, so the hyperinsulinemia of metabolic syndrome raises uric acid into gout — one reason gout clusters with obesity and type 2 diabetes.
- `connects-to` → **[Polycythemia Vera](../polycythemia-vera/README.md)** — High cell turnover overproduces urate: the expanded marrow of polycythemia vera and other myeloproliferative disease floods the blood with purines, causing a secondary gout that can be the presenting clue to the hematologic disorder.
- `connects-to` → **[Stroke](../stroke/README.md)** — Hyperuricemia is an independent vascular risk: beyond its joint disease, elevated urate promotes endothelial dysfunction and is associated with a raised risk of stroke, part of gout's broader cardiovascular shadow.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Urate and the failing heart feed each other: hyperuricemia independently predicts heart failure and worsens its outcomes, while the disease and its diuretics raise urate — a bidirectional link in gout's cardiovascular burden.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — A hot joint forces a critical question: acute gout closely mimics septic arthritis, which must be excluded by joint aspiration because a missed joint infection can seed sepsis, and tophi themselves can become infected.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Gouty inflammation tips toward clotting: the systemic inflammation of gout and hyperuricemia is associated with a higher risk of venous thromboembolism, adding a venous dimension to its vascular complications.
- `connects-to` → **[NASH](../nash/README.md)** — Hyperuricemia and fatty liver cluster: gout sits squarely in the metabolic syndrome, and its insulin resistance and fructose metabolism strongly associate it with non-alcoholic steatohepatitis.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Recurrent disabling pain weighs on mood: the unpredictable, intensely painful flares and chronic joint damage of tophaceous gout reduce quality of life and carry an elevated rate of depression.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Chronic inflammation and renal disease lower the count: longstanding tophaceous gout's persistent inflammation, compounded by the chronic kidney disease that so often accompanies it, can produce an anemia of chronic disease.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Tophi erode through the skin: large chronic tophi can ulcerate and discharge chalky urate, leaving open wounds over joints that are slow to heal and prone to infection.
- `connects-to` → **[Staphylococcus aureus](../../../02-pathogen/02-bacteria/staphylococcus-aureus/README.md)** — Ulcerated tophi invite Staph: when a tophus breaks through the skin, Staphylococcus aureus readily colonizes and infects it, risking cellulitis, septic arthritis and bloodstream infection.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Chronic inflammation and immobility cost bone: longstanding gout's persistent inflammation, joint damage and reduced mobility are associated with lower bone density and a raised fracture risk.

[^dalbeth-2019-gout-primer]: Dalbeth N, Choi HK, Joosten LAB, et al. Gout. *Nat Rev Dis Primers.* 2019;5(1):69. [doi:10.1038/s41572-019-0115-y](https://doi.org/10.1038/s41572-019-0115-y) · [PubMed 31558729](https://pubmed.ncbi.nlm.nih.gov/31558729/)
[^martinon-2006-nlrp3-gout]: Martinon F, Pétrilli V, Mayor A, Tardivel A, Tschopp J. Gout-associated uric acid crystals activate the NALP3 inflammasome. *Nature.* 2006;440(7081):237-241. [doi:10.1038/nature04516](https://doi.org/10.1038/nature04516) · [PubMed 16407889](https://pubmed.ncbi.nlm.nih.gov/16407889/)
[^fitzgerald-2020-acr-gout]: FitzGerald JD, Dalbeth N, Mikuls T, et al. 2020 American College of Rheumatology Guideline for the Management of Gout. *Arthritis Care Res (Hoboken).* 2020;72(6):744-760. [doi:10.1002/acr.24180](https://doi.org/10.1002/acr.24180) · [PubMed 32391934](https://pubmed.ncbi.nlm.nih.gov/32391934/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
