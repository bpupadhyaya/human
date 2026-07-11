---
schema: human-scale-entry/v1
id: sjogrens-syndrome
name: Sjögren's Syndrome
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Primary Sjögren's syndrome (pSS): systemic lymphocytic exocrinopathy; xerostomia, xerophthalmia, anti-Ro/SSA (80%); type I IFN signature; 40× elevated lymphoma risk; BAFF drives B-cell hyperactivation. Ianalumab (anti-BAFFR; TWINSS 2023) and rituximab are active biologics."
aliases: ["Sjögren's syndrome", "primary Sjögren's syndrome", "pSS", "Sjogrens", "sicca syndrome", "autoimmune exocrinopathy", "anti-Ro/SSA disease"]
sources:
  - id: shiboski-2017-sjogrens-criteria
    type: peer-reviewed
    cite: "Shiboski CH, Shiboski SC, Seror R, et al. 2016 American College of Rheumatology/European League Against Rheumatism classification criteria for primary Sjögren's syndrome. Arthritis Rheumatol. 2017;69(1):35-45."
    doi: "10.1002/art.39859"
    pmid: "27785888"
    url: "https://doi.org/10.1002/art.39859"
  - id: dorner-2023-ianalumab-twinss
    type: peer-reviewed
    cite: "Dörner T, Bowman SJ, Fox R, et al. Ianalumab (VAY736) in patients with primary Sjögren's syndrome: a multicentre, randomised, double-blind, placebo-controlled, phase 3 trial (TWINSS). Lancet. 2023;402(10400):477-489."
    doi: "10.1016/S0140-6736(23)00454-4"
    pmid: "37499657"
    url: "https://doi.org/10.1016/S0140-6736(23)00454-4"
  - id: seror-2019-eular-sjogrens
    type: peer-reviewed
    cite: "Seror R, Ravaud P, Mariette X, et al. EULAR Sjögren's Syndrome Disease Activity Index and Patient Reported Index. Ann Rheum Dis. 2019;78(11):1554-1560."
    doi: "10.1136/annrheumdis-2019-215024"
    pmid: "31462415"
    url: "https://doi.org/10.1136/annrheumdis-2019-215024"
cross_links:
  - target: 01-human/03-molecular/baff
    relation: connects-to
    note: "BAFF overexpressed in Sjögren's salivary glands → B-cell hyperactivation → anti-Ro/SSA production, ectopic GC formation, lymphoma risk; ianalumab (anti-BAFFR; TWINSS: ESSDAI –5.1 vs –2.7 at week 24; Lancet 2023) is the first Phase 3 positive biologic in pSS."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Type I IFN signature is present in ~75% of pSS patients and is highest in anti-Ro/SSA+ disease; pDCs in salivary glands produce IFN-α driven by TLR7 (ssRNA–anti-Ro complexes) and TLR9 (DNA–anti-La complexes); IFN signature correlates with disease activity and systemic features."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 is elevated in Sjögren's glands and serum; drives plasma cell differentiation → anti-Ro/SSA and RF production; supports ectopic GC formation; salivary gland epithelial cells produce IL-6 locally → autocrine B-cell hyperactivation and lymphoma risk."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "Rituximab (anti-CD20) depletes B cells in pSS; Phase 3 TEARS/TRACTISS had mixed results; used off-label for severe extraglandular pSS (vasculitis, cryoglobulinemia); CD20+ ectopic GC B cells are the key pathogenic and lymphoma-risk population in salivary glands."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "pSS B-cell hyperactivation (BAFF-driven) → anti-Ro/SSA, anti-La/SSB autoantibodies; ectopic germinal center formation in salivary glands; CD27+ memory B cells expanded; rituximab (anti-CD20) targets B cells in refractory pSS; 40× lymphoma risk from chronic B-cell stimulation."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Treg frequency and suppressive function reduced in pSS; Treg/Th17 imbalance drives salivary gland inflammation; impaired peripheral tolerance permits autoreactive B- and T-cell activation; low FoxP3+ Tregs in minor salivary gland biopsies correlate with disease activity scores."
  - target: 01-human/07-system/dlbcl
    relation: connects-to
    note: "pSS carries 15-40× population-level NHL risk; MALT lymphoma most common (parotid gland), progressing to DLBCL in ~10-15%; cryoglobulinemia, low C4, parotid swelling predict lymphoma transformation; R-CHOP for DLBCL; pSS-associated lymphoma has better prognosis than de novo DLBCL."
  - target: 01-human/07-system/systemic-sclerosis
    relation: connects-to
    note: "Sjögren's and systemic sclerosis are overlapping connective-tissue autoimmune diseases that often coexist and share a type-I-interferon signature, but Sjögren is a lymphocytic exocrine-gland disease causing sicca while SSc is a fibrosing vasculopathy — dryness versus scarring."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "The eye bears the brunt of Sjögren's: lymphocytic destruction of lacrimal glands causes aqueous-deficient dry eye (keratoconjunctivitis sicca) — gritty, burning eyes with corneal damage on Schirmer testing — which with dry mouth forms the sicca complex that defines the disease."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "Sjögren's and lupus are closely related autoimmune diseases sharing anti-Ro/SSA and anti-La/SSB antibodies and a type-I-interferon signature; secondary Sjögren commonly complicates lupus, and anti-Ro can cross the placenta to cause neonatal lupus and congenital heart block."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Sjögren's syndrome most often appears as secondary Sjögren's atop rheumatoid arthritis or lupus: shared autoimmune mechanisms extend inflammation to lacrimal and salivary glands, so any RA patient with dry eyes and mouth (sicca) is evaluated for the overlap."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Sjögren's syndrome is a B-cell/plasma-cell-driven disease: BAFF-fueled clonal B and plasma cells make anti-Ro/La autoantibodies and hypergammaglobulinemia, and persistent germinal-center activity in salivary glands is what drives the high MALT-lymphoma risk."
  - target: 01-human/07-system/follicular-lymphoma
    relation: connects-to
    note: "Sjögren's syndrome carries the highest lymphoma risk of any autoimmune disease: chronic salivary B-cell activation predisposes mainly to MALT marginal-zone lymphoma but also to follicular and other B-cell lymphomas—so persistent parotid swelling demands biopsy."
  - target: 01-human/07-system/mantle-cell-lymphoma
    relation: connects-to
    note: "Sjögren's lymphomas differ from mantle cell lymphoma in origin: Sjögren's drives antigen-stimulated marginal-zone lymphomas in inflamed glands, whereas MCL is a t(11;14) cyclin-D1 tumor of naive B cells—both B-NHL, but one inflammation-driven, one translocation-driven."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Sjögren's syndrome is a lymphoproliferative disease of exocrine glands: lymphocytes infiltrate and destroy salivary and lacrimal glands, and the chronic lymphoid activation causing dryness also drives its lymphoma risk—tying it to lymphatic-system biology."
  - target: 01-human/07-system/dermatomyositis
    relation: connects-to
    note: "Sjögren's syndrome overlaps with connective-tissue autoimmune diseases like dermatomyositis: both share sicca symptoms, autoantibodies and sometimes myositis, and secondary Sjögren's often accompanies inflammatory myopathy—so an overlap syndrome must be considered."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "T helper cells orchestrate the gland destruction of Sjögren's: infiltrating CD4 T cells and the cytokines they drive (with B cells and interferon) attack salivary and lacrimal glands, so the autoimmune assault that dries eyes and mouth is T-cell-coordinated."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "Sjögren's clusters with autoimmune thyroid disease: it frequently coexists with Hashimoto's thyroiditis, reflecting a shared tendency to organ-specific autoimmunity, so thyroid function is checked in Sjögren's patients who develop fatigue or weight change."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Sjögren's commonly damages peripheral nerves: lymphocytic infiltration and vasculitis cause sensory neuropathy and sometimes ganglionopathy, so numbness and pain are frequent extra-glandular features—occasionally the presenting sign before sicca symptoms."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Sjögren's affects the kidney as tubulointerstitial nephritis: lymphocytic infiltration of tubules causes distal renal tubular acidosis with hypokalemia and stones, a classic extra-glandular complication distinct from the glomerular disease of lupus."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Sjögren's involves the lung as interstitial lung disease: lymphocytic infiltration (NSIP, LIP) and airway dryness cause cough and dyspnea, a leading cause of morbidity that overlaps the pulmonary fibrosis of related connective-tissue diseases."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Beyond peripheral nerves, Sjögren's can strike the central nervous system: white-matter lesions may mimic multiple sclerosis and autonomic dysfunction worsens the dryness—so neurological disease ranges from brain to autonomic, not just sensory neuropathy."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "Sjögren's anti-Ro/SSA antibodies cross the placenta: they can cause neonatal lupus and congenital heart block in the fetus, so anti-Ro-positive pregnancies are monitored with fetal heart surveillance—an autoimmune disease reaching the next generation."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Plasmacytoid dendritic cells fuel Sjögren's interferon signature: they pour out type I interferon that drives the autoimmune attack on exocrine glands, linking the disease's hallmark IFN signature to a specific immune cell."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Sjögren's syndrome is HLA-associated: MHC class II HLA-DR/DQ variants shape presentation of the Ro and La autoantigens to T cells, the genetic basis for the anti-SSA/SSB antibodies that define the disease."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "Sjögren's dries glands by blocking acetylcholine: antibodies against the M3 muscarinic receptor stop acetylcholine from triggering saliva and tears, so beyond gland destruction the secretion machinery is jammed—why cholinergic drugs like pilocarpine help."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Falling complement warns of severe Sjögren's: low C3/C4 from immune-complex consumption marks aggressive disease and flags the patients at highest risk of progressing to lymphoma, making complement a prognostic blood test."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Sjögren's glands fill with immune cells including macrophages: lymphocytic foci and macrophages infiltrate and destroy the salivary and lacrimal glands, the histologic lesion seen on lip biopsy that confirms the diagnosis."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Sjogren's can drain potassium through the kidney: immune attack on the renal tubules causes distal renal tubular acidosis, which wastes potassium and can cause hypokalemic muscle paralysis—a striking renal manifestation of the disease."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Sjogren's reaches the nervous system, including the brain: it can cause CNS lesions, cognitive change and cranial neuropathies beyond the peripheral nerve damage, so neurologic symptoms are part of its systemic reach."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Cytotoxic T cells help destroy the Sjogren's glands: alongside the B cells that drive the autoantibodies, CD8 T cells infiltrate and kill the salivary and lacrimal gland cells, contributing to the dryness that defines the disease."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "Sjogren's acidifies the blood through the kidney: its attack on the renal tubules causes distal renal tubular acidosis—a failure to excrete hydrogen ions—so acid builds up despite normal lungs."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Sjogren's dries and inflames the skin: beyond dry eyes and mouth, it parches the skin and can cause a cutaneous small-vessel vasculitis with palpable purpura, part of its systemic reach."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Sjogren's builds germinal centers where they don't belong: its inflamed salivary glands grow ectopic germinal centers, chronic B-cell factories that explain the syndrome's notable risk of MALT lymphoma."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photons gauge Sjogren's dryness at its source: salivary gland ultrasound shows the patchy, pitted glands, and scintigraphy times how sluggishly they take up and release tracer — imaging that documents the failing secretory tissue behind the dry mouth."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "Sjogren's is a disease of all exocrine glands, the pancreas included: the same lymphocytic attack that dries the mouth and eyes can scar the pancreas, causing exocrine insufficiency and overlapping with autoimmune pancreatitis."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D runs low in Sjogren's and seems to matter: deficiency is common and tracks with the peripheral neuropathy and the lymphoma risk that mark more severe disease, hinting at the vitamin's role in restraining the autoimmunity."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Sjogren's is written in its autoantibodies: anti-Ro/SSA and anti-La/SSB are the serologic hallmarks used to diagnose it, and anti-Ro crossing the placenta can give the fetus congenital heart block — making the antibody a clinical signature in its own right."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Sjogren's keeps autoimmune company in the liver: it overlaps notably with primary biliary cholangitis and autoimmune hepatitis, so dry eyes and mouth may arrive alongside the anti-mitochondrial antibodies and cholestasis of liver autoimmunity."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "The autoimmunity spills into the blood counts: Sjogren's commonly brings anemia and other cytopenias, from the anemia of chronic inflammation to occasional autoimmune hemolysis that strips red cells from the circulation."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "The same immune dysregulation can drop the neutrophils: a mild autoimmune neutropenia is common in Sjogren's, part of the cytopenia picture alongside the anemia and low platelets that reflect the disease's reach into the blood."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "Dryness and autoimmunity reach the gut: lost saliva makes swallowing hard and unprotected, while Sjogren's overlaps with autoimmune atrophic gastritis, thinning the stomach lining and impairing acid and intrinsic-factor secretion."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Exocrine failure dries more than eyes and mouth: vaginal dryness and dyspareunia are common in Sjogren's, and the anti-Ro/La antibodies can cross the placenta to cause neonatal lupus and congenital heart block."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "An interferon signature defines Sjogren's: type-I interferon signals through JAK-STAT1 to switch on the gene program seen in the salivary glands and blood, a central driver of the autoimmunity and a target of JAK inhibitors under study."
  - target: 01-human/07-system/waldenstrom-macroglobulinemia
    relation: connects-to
    note: "Sustained B-cell drive courts lymphoma: Sjogren's carries one of the highest lymphoma risks of any autoimmune disease, the chronic B-cell stimulation favoring MALT and other low-grade lymphomas including lymphoplasmacytic Waldenström-type disease."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "Dry mouth and eyes come down to ion transport: saliva and tears form when acinar cells pump chloride to draw water across the gland, and the autoimmune attack that wrecks these cells shuts down that secretion."
  - target: 02-pathogen/03-fungi/candida-albicans
    relation: connects-to
    note: "The dried-out mouth invites a fungus: without protective saliva, Candida overgrows into oral thrush and angular cheilitis, a recurrent infection that is one of the most common day-to-day complications of Sjögren's xerostomia."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "An interferon signature runs the disease: type I interferon signals through the JAK-STAT pathway to sustain the autoimmune attack on the glands, making JAK inhibitors a logical therapy being tested against Sjögren's."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It reaches past the glands to the kidneys: lymphocytic infiltration of the renal tubules causes tubulointerstitial nephritis and distal renal tubular acidosis, so unexplained low potassium or acidosis can be the clue that points to Sjögren's."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 keeps the autoreactive B cells alive: downstream of IL-6 and IL-21 in the glandular germinal-center-like infiltrates, STAT3 activation supports the B-cell survival that drives Sjögren's toward lymphoma."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB fuels the glandular inflammation: BAFF and TNF signaling converge on NF-κB in the salivary-gland infiltrate, sustaining the chronic activation that destroys glandular tissue in Sjögren's."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Chronic autoimmune inflammation thickens the blood: Sjögren's carries a raised risk of deep-vein thrombosis and pulmonary embolism, part of the prothrombotic state shared across the systemic autoimmune diseases."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "It quietly attacks the kidney: Sjögren's classically causes tubulointerstitial nephritis and distal renal tubular acidosis, and the cumulative interstitial damage can progress to chronic kidney disease."
  - target: 01-human/07-system/fibromyalgia
    relation: connects-to
    note: "Fatigue and pain overlap heavily: fibromyalgia is a very common comorbidity in Sjögren's, and its widespread pain and exhaustion confound assessment of how much disability comes from the autoimmune disease itself."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Persistent inflammation dulls the marrow: the chronic immune activation and IL-6 of Sjögren's raise hepcidin and blunt erythropoiesis, contributing the anemia of chronic disease seen among its cytopenias."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "It attacks the small sensory nerves: Sjögren's is a leading autoimmune cause of small-fiber neuropathy and sensory ganglionopathy, producing burning neuropathic pain and numbness even when dryness is mild."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "As a connective-tissue disease it can pressurize the lungs: like lupus and scleroderma, Sjögren's is associated with pulmonary arterial hypertension through immune-mediated remodeling of the pulmonary vasculature."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Chronic dryness and fatigue wear on mood: the relentless ocular and oral dryness, profound fatigue and pain of Sjögren's substantially impair quality of life and carry elevated rates of depression."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Losing saliva harms the whole upper gut: the xerostomia of Sjögren's drives rampant dental caries and difficulty chewing and swallowing dry food, and oesophageal dysmotility and reflux are common."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "The exocrine attack dries and inflames the skin: Sjögren's causes xerosis from reduced secretions and can produce cutaneous small-vessel vasculitis with palpable purpura and annular erythema."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A chronic, dry, fatiguing disease breeds worry: the relentless symptoms, lymphoma-risk surveillance and unpredictable systemic flares of Sjögren's foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Dryness and inflammation reach the lungs: Sjögren's dries the trachea into a chronic cough and causes interstitial lung disease and bronchiectasis from lymphocytic airway infiltration."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It clusters with autoimmune thyroid disease: Sjögren's frequently coexists with Hashimoto's thyroiditis, sharing the autoimmune diathesis that attacks the body's glands."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "It is an autoimmune exocrinopathy: anti-Ro/SSA and anti-La/SSB autoantibodies and lymphocytic infiltration of the salivary and lacrimal glands drive Sjögren's, with a marked risk of B-cell lymphoma."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its antibodies can stop the fetal heart: anti-Ro/SSA antibodies cross the placenta and damage the fetal conduction system, causing congenital complete heart block in neonatal lupus."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It aches the joints and muscles: non-erosive arthritis and arthralgia are common in Sjögren's, and an overlap myositis can occur with its other autoimmune associations."
  - target: 02-pathogen/01-viruses/hepatitis-c-virus
    relation: connects-to
    note: "A virus can mimic it: chronic hepatitis C causes a sicca syndrome with lymphocytic sialadenitis that resembles and associates with Sjögren's, so HCV is excluded at diagnosis."
  - target: 03-medicine/01-modern/02-respiratory/corticosteroids
    relation: connects-to
    note: "Steroids treat its systemic flares: while dryness is managed with substitutes, corticosteroids and immunosuppressants control the extraglandular vasculitis, arthritis and organ involvement of Sjögren's."
  - target: 02-pathogen/01-viruses/epstein-barr-virus
    relation: connects-to
    note: "A virus implicated in its biology: EBV is found in Sjögren's salivary glands and is linked to the chronic B-cell activation that drives both the autoimmunity and its MALT-lymphoma risk."
  - target: 03-medicine/03-food/omega-3-fatty-acids
    relation: connects-to
    note: "Diet is tried for the dryness: omega-3 supplementation is studied for the dry-eye symptoms of Sjögren's, with modest and inconsistent benefit."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Its lymphomas need chemo: Sjögren's carries the highest lymphoma risk of any autoimmune disease, and the MALT and diffuse large B-cell lymphomas it spawns are treated with rituximab-based chemotherapy, while cyclophosphamide handles severe systemic disease."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "B-cell-directed biologics: because Sjögren is driven by BAFF-fuelled autoreactive B cells, anti-CD20 rituximab, anti-BAFF agents and JAK inhibitors are used or trialled for its systemic and glandular manifestations."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "It scars the lung: Sjögren's syndrome causes interstitial lung disease, usually a non-specific interstitial pneumonia pattern, where chronic lymphocytic inflammation lays down pulmonary fibrosis that stiffens the lungs and impairs gas exchange."
  - target: 01-human/07-system/nmo
    relation: connects-to
    note: "A neuro-autoimmune overlap: Sjögren's syndrome can co-occur with neuromyelitis optica, the two sharing anti-Ro/aquaporin autoantibody biology and a type-I-interferon signature, so dry eyes and mouth may accompany optic neuritis and myelitis."
  - target: 01-human/07-system/pemphigus-vulgaris
    relation: connects-to
    note: "A fellow autoantibody, B-cell disease: like pemphigus vulgaris, Sjögren's is driven by autoreactive B cells and autoantibodies and responds to rituximab, though Sjögren targets exocrine glands and pemphigus the skin's desmosomes."
  - target: 01-human/05-tissue/guillain-barre
    relation: connects-to
    note: "It strikes the peripheral nerves too: Sjögren's syndrome is a leading cause of sensory ataxic neuronopathy and small-fibre neuropathy—an autoimmune assault on peripheral nerves, distinct from but echoing Guillain-Barré."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Interstitial lung disease: Sjögren's lymphocytic infiltration reaches the lung, causing interstitial lung disease and cystic change around the alveoli, an underrecognised source of morbidity."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "Renal involvement: Sjögren's causes interstitial nephritis with distal renal tubular acidosis and, less often, a cryoglobulin-driven glomerulonephritis injuring the glomerulus."
  - target: 01-human/07-system/cidp
    relation: connects-to
    note: "Neurological Sjögren: beyond a sensory ganglionopathy, Sjögren's can produce a CIDP-like chronic demyelinating neuropathy, part of its peripheral and central nervous-system involvement."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Neonatal heart block: maternal anti-Ro/SSA antibodies in Sjögren's cross the placenta and attack the developing cardiac conduction system, causing congenital complete heart block in the fetus."
  - target: 01-human/07-system/ptcl
    relation: connects-to
    note: "Lymphoma's broad reach: Sjögren's carries the highest lymphoma risk of the autoimmune diseases—mostly MALT B-cell lymphoma but also T-cell lymphomas, and angioimmunoblastic T-cell lymphoma can itself mimic Sjögren's sicca and hypergammaglobulinaemia."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Interferon and immunosuppression: Sjögren's shares a type-I interferon signature with severe COVID-19, and the rituximab used to deplete B cells leaves treated patients vulnerable to severe infection and poor vaccine responses."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 glandular attack: alongside the type I interferon signature, IFN-γ-driven Th1 inflammation fuels the lymphocytic infiltration that destroys salivary and lacrimal glands in Sjögren's."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "Th17 contribution: the IL-17/Th17 axis participates in the glandular inflammation and ectopic lymphoid structures of Sjögren's syndrome."
  - target: 01-human/03-molecular/aquaporin-4
    relation: connects-to
    note: "Aquaporin overlap: anti-aquaporin-4 antibodies link Sjögren's to neuromyelitis optica, and aquaporin water channels in exocrine glands are central to the secretory failure causing sicca."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Glandular inflammation: TNF-α within the lymphocytic infiltrate of the salivary and lacrimal glands contributes to the inflammation and secretory destruction of Sjögren's syndrome."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Inflammatory amplification: IL-1β from activated macrophages in the inflamed exocrine glands amplifies the tissue damage of Sjögren's syndrome."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Inflammasome activation: NLRP3-inflammasome activation in the salivary glands matures the IL-1β that drives the chronic glandular inflammation of Sjögren's syndrome."
  - target: 01-human/03-molecular/btk
    relation: connects-to
    note: "B-cell signalling: BTK transduces the B-cell-receptor signals driving the autoreactive B-cell expansion of Sjögren's, the target of BTK inhibitors in trials and a node relevant to the elevated risk of MALT lymphoma."
  - target: 01-human/03-molecular/ctla-4
    relation: connects-to
    note: "T-cell costimulation: abatacept (CTLA-4-Ig) blocks the CD28 costimulation activating the glandular T cells of Sjögren's syndrome, a costimulation-blockade strategy tested to interrupt the autoimmune attack on exocrine tissue."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Glandular infiltration: CCL2 recruits monocytes into the inflamed salivary and lacrimal glands of Sjögren's, building the macrophage component of the lymphocytic infiltrate that destroys secretory tissue."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Ectopic lymphoid neogenesis: CXCL12 helps organise the tertiary lymphoid structures with germinal centres that form within Sjögren's salivary glands, the ectopic B-cell follicles that drive local autoantibody production and mark lymphoma-prone disease."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Lymphomagenesis: chronic BAFF-driven B-cell survival via anti-apoptotic BCL-2 underlies Sjögren's uniquely high risk of MALT lymphoma, the transformation of the persistently stimulated glandular B-cell clones into malignancy."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "Epithelial alarmin: IL-33 released from stressed salivary-gland epithelium is elevated in Sjögren's, acting as an alarmin that amplifies the innate and type-2 inflammation injuring the secretory tissue."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Glandular destruction: caspase-3-mediated apoptosis of salivary- and lacrimal-gland epithelial cells contributes to the loss of secretory tissue that produces the dry mouth and eyes of Sjögren's syndrome."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 amplification: IL-12-driven Th1 and IFN-γ polarisation reinforces the interferon signature already mapped here, sustaining the lymphocytic infiltration of the exocrine glands in Sjögren's."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Vasculitis and lymphoma risk: complement activation (with the C3 already mapped) drives the cryoglobulinaemic vasculitis of Sjögren's, and complement consumption marks the patients at highest risk of B-cell lymphoma."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "TLR-IFN drive: anti-Ro/La immune complexes engage endosomal TLR7/9, signalling through MyD88 to activate NF-κB (mapped) and the type-I interferon programme (mapped) that defines the Sjögren's IFN signature."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic nucleic-acid sensing: the cGAS-STING pathway senses self nucleic acids in the inflamed glands and feeds the type-I interferon signature (mapped) central to Sjögren's pathogenesis."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Lymphomagenesis: the chronic B-cell hyperactivation of Sjögren's (BAFF mapped) carries a marked risk of transformation to MALT/marginal-zone lymphoma, a MYC-associated event in the salivary glands."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 inflammation: IL-23 sustains the pathogenic Th17 response (IL-17A already mapped) that contributes to the glandular inflammation of Sjögren's syndrome."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Innate interferon trigger: TLR-driven innate sensing of viral and self-nucleic-acid signals (with MyD88 already mapped) helps trigger the type-I-interferon-driven autoimmunity of Sjögren's syndrome."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Glandular cytotoxicity: CD8 cytotoxic T cells deploy perforin to destroy the salivary and lacrimal glandular epithelium, a direct effector mechanism of the sicca symptoms of Sjögren's syndrome."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "BAFF-driven PI3K-AKT signalling (BAFF mapped) sustains the autoreactive B cells and ectopic germinal centres of Sjögren's syndrome."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "The mTOR-regulated metabolic program supports the B-cell and plasmablast expansion driving the autoantibody response of Sjögren's syndrome."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 is upregulated in the inflamed salivary glands of Sjögren's syndrome, contributing to glandular inflammation and dysfunction."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling governs the regulatory-T-cell balance and the glandular fibrosis of Sjögren's syndrome."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors modulate the survival of glandular epithelial cells and the autoreactive lymphocytes of Sjögren's syndrome."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signalling transduces the cytokine and B-cell-receptor stimuli that sustain the lymphocytic infiltration of Sjögren's syndrome."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the NF-κB-driven inflammatory and B-cell survival signaling of Sjögren's syndrome."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins amplify the innate inflammation of the salivary and lacrimal gland lesions of Sjögren's syndrome."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α in the hypoxic inflamed glandular tissue contributes to the metabolic and inflammatory adaptation of Sjögren's syndrome."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) supports the survival and activation of the autoreactive B and T cells of Sjögren's syndrome."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family (LYN) kinase signaling downstream of the B-cell receptor participates in the autoreactive B-cell activation of Sjögren's syndrome."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the salivary-gland epithelial and immune-cell responses of Sjögren's syndrome."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked immunometabolic signaling shapes the autoreactive T- and B-cell metabolism of Sjögren's syndrome."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment into the exocrine glands contributes to the lymphocytic infiltration of Sjögren's syndrome."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic dysregulation of the immune responses of Sjögren's syndrome."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the autoreactive T-cell activation of the salivary and lacrimal gland infiltrates of Sjögren's syndrome."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "IL-10-mediated immunoregulation participates in the dysregulated immune balance of Sjögren's syndrome."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine and purinergic signaling participate in the salivary-gland dysfunction and immunomodulation of Sjögren's syndrome."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Hypergammaglobulinaemia: polyclonal B-cell activation in Sjögren's produces marked IgG elevation and the diagnostic anti-Ro/SSA and anti-La/SSB autoantibodies, and this sustained IgG autoreactivity underlies the risk of transformation to MALT lymphoma."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Sex-hormone dimension: the striking female predominance and typical postmenopausal onset implicate declining estrogen in the glandular epithelial apoptosis and loss of immune tolerance that characterise Sjögren's syndrome."
  - target: 01-human/03-molecular/secretory-iga
    relation: connects-to
    note: "Mucosal secretory failure: lymphocytic destruction of exocrine glands reduces secretory IgA output into saliva and tears, weakening the mucosal immune barrier at the ocular and oral surfaces damaged by the sicca disease."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Anaemia and cytopenias: chronic inflammation and autoimmune cytopenias in Sjögren's syndrome lower haemoglobin, and anaemia with leukopenia is a common systemic feature alongside the hypergammaglobulinaemia (immunoglobulin G already mapped)."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Th2 B-cell help: IL-4 and type-2 T-cell help support the intense B-cell activation (BAFF already mapped) that produces the anti-Ro/La autoantibodies and drives the germinal-centre-like lymphoid organisation of the affected glands in Sjögren's."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Congenital heart block: anti-Ro/SSA antibodies from mothers with Sjögren's cross the placenta and damage the fetal cardiac conduction system, causing neonatal lupus with congenital complete heart block, a serious pregnancy complication."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 B-cell help: IL-13, with the IL-4 (already mapped) type-2 response, supports the intense B-cell activation (BAFF already mapped) that produces the anti-Ro/La autoantibodies and the glandular lymphoid organisation of Sjögren's."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell and Treg balance: IL-2 drives the T-cell responses in the lymphocytic sialadenitis of Sjögren's, and low-dose IL-2 to restore regulatory T cells (CTLA-4 already mapped) is being trialled to rebalance the autoimmunity."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative glandular injury: chronic lymphocytic inflammation of the exocrine glands generates oxidative stress, to which xanthine oxidase contributes, and the resulting reactive oxygen species add to the epithelial damage of Sjögren's."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Glandular inflammation: prostaglandins from the lymphocytic sialadenitis (IL-6, TNF and IL-1 already mapped) amplify the inflammation of the exocrine glands, part of the inflammatory injury behind the sicca of Sjögren's syndrome."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Anaemia of inflammation: the chronic autoimmune inflammation (IL-6 already mapped) of Sjögren's causes the anaemia of chronic disease (haemoglobin already mapped) through iron sequestration, part of its systemic haematological involvement."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Impaired secretion and vasculature: nitric oxide, disturbed in the inflamed exocrine glands, affects the secretory and vascular function (acetylcholine already mapped), part of the glandular dysfunction of Sjögren's syndrome."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin sequesters iron (already mapped) to produce the anaemia of chronic disease that is part of the systemic haematological involvement of Sjögren's syndrome."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Glandular angiogenesis: VEGF drives the angiogenesis and vascular changes of the chronically inflamed exocrine glands, part of the tissue remodelling of the salivary and lacrimal glands in Sjögren's syndrome."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "RTA and nephrocalcinosis: the distal renal tubular acidosis of the tubulointerstitial nephritis (kidney and potassium already mapped) of Sjögren's impairs urinary acidification, causing the nephrocalcinosis and calcium stones."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Immune-metabolic adipokine: leptin modulates the autoreactive response of Sjögren's syndrome, part of the immune-metabolic milieu of the autoimmune exocrinopathy."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the immune-metabolic milieu of Sjögren's syndrome."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the immune-metabolic milieu of Sjögren's syndrome."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Innate surveillance: the NK cells (perforin already mapped) infiltrate the salivary glands and contribute to the innate inflammation and the MALT-lymphoma surveillance of Sjögren's syndrome."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension balancing the Th1/Th17 (IFN-γ and IL-17 already mapped) drive of Sjögren's syndrome."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 IgE: the IgE (with IL-4 and IL-13 already mapped) reflects the type-2 immune dimension present in a subset of Sjögren's syndrome."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast-cell fibrosis: the mast cells infiltrate the salivary glands and contribute to the periductal fibrosis and the type-2 (IL-4 and IL-13 already mapped) dimension of Sjögren's syndrome."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Epithelial alarmin: the ductal-epithelial TSLP alarmin drives the type-2 (IL-4 and IL-13 already mapped) immunity of the damaged exocrine epithelium of Sjögren's syndrome."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Selenium immune status: the selenium selenoprotein antioxidant defence modulates the lymphocyte function and the autoimmune-thyroid overlap of Sjögren's syndrome."
  - target: 01-human/03-molecular/il-31
    relation: connects-to
    note: "Neuroimmune itch/dryness: IL-31, a type-2 (IL-4 and IL-13 already mapped) cytokine, links the type-2 immunity to the sensory-nerve dysfunction contributing to the dryness and discomfort of Sjögren's syndrome."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "Complement C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the glandular inflammation and, when consumed, the low complement marks the lymphoma risk of Sjögren's syndrome."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Type-2 glandular fibrosis: periostin, downstream of the type-2 (IL-4 and IL-13 already mapped) cytokines and the TSLP (already mapped), is part of the fibrotic remodelling of the exocrine glands of Sjögren's syndrome."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) whose consumption (the low complement) marks the disease activity and lymphoma risk of Sjögren's syndrome."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway activated by the anti-Ro/La immune complexes (immunoglobulin already mapped) in the glands of Sjögren's syndrome."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Chronic-disease iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the anaemia of the chronic systemic inflammation of Sjögren's syndrome."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Glandular kinin: bradykinin, generated by the tissue-kallikrein cascade in the inflamed salivary and lacrimal glands of Sjögren's syndrome, amplifies vascular permeability and the pain of the glandular infiltrates via B1/B2 receptors."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Autoimmune anaemia support: erythropoietin addresses the normocytic anaemia of chronic inflammation and autoimmune haemolysis in Sjögren's syndrome; EPOR expression on salivary ductal cells may also modulate local epithelial repair."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Glandular mast-cell mediator: histamine from the mast cells of the inflamed salivary and lacrimal glands promotes vascular permeability and lymphocytic infiltration, amplifying the sicca symptoms and glandular destruction of Sjögren's syndrome."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian immune modulator: melatonin is reduced in active Sjögren's syndrome; it down-regulates IFN-γ and IL-17A (already mapped) production by autoreactive lymphocytes and exerts cytoprotective effects on the glandular epithelium."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Neuroendocrine autoimmune amplifier: prolactin is elevated in a subset of Sjögren's patients and drives B-cell survival and anti-Ro/La autoantibody production (BAFF already mapped), paralleling its pathogenic role in other systemic autoimmune diseases."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Lacrimal-salivary neuromodulator: oxytocin receptors on acinar cells regulate lacrimal and salivary secretory function; oxytocin deficiency contributes to the sicca phenotype and the autonomic-nerve dysfunction of Sjögren's syndrome."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "SjS testosterone: testosterone exerts anti-inflammatory effects via androgen receptor on the salivary and lacrimal-gland-infiltrating lymphocytes; androgen deficiency in females underlies the sex predominance and exocrine-gland vulnerability of Sjögren's syndrome."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "SjS serotonin: serotonin drives neurogenic dysautonomia and glandular secretory dysfunction in Sjögren's syndrome via 5-HT2 receptor-mediated modulation of autonomic innervation; altered serotonin metabolism amplifies the fatigue, pain and depressive symptoms of the disease."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "SjS vasopressin: vasopressin (ADH) regulates aquaporin-4 (already mapped) water transport in salivary and lacrimal glands; in Sjögren's syndrome the inflammatory destruction of glandular parenchyma impairs this vasopressin-driven secretion, worsening the sicca phenotype."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "SjS iodine: iodine-dependent thyroid hormones modulate Th17/Treg (IL-17A already mapped) and BAFF (already mapped)-driven autoimmune B-cell activation in Sjögren syndrome; hypothyroidism amplifies exocrine-gland inflammation and the sicca phenotype."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "SjS sodium: sodium-driven osmotic Th17 polarisation amplifies the IL-17A (already mapped) and NF-κB (already mapped)-mediated salivary and lacrimal-gland inflammation of Sjögren syndrome; high-salt diet promotes Th17/Treg imbalance worsening sicca symptoms."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "SjS magnesium: magnesium deficiency amplifies the NF-κB (already mapped) and BAFF (already mapped)-driven B-cell survival and autoantibody production of Sjögren syndrome; magnesium is required for salivary-gland secretory enzyme activity and mucosal repair in the sicca phenotype."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "SjS copper: copper, as ceruloplasmin cofactor in macrophages (already mapped) and dendritic-cell (already mapped), modulates ROS and BAFF (already mapped) signalling; copper deficiency impairs T-cytotoxic-cell (already mapped) and B-cell (already mapped) regulation in SjS."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "SjS zinc: zinc deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) in macrophages (already mapped) and mast-cell (already mapped); zinc supports salivary-gland repair and BAFF (already mapped)-mediated B-cell (already mapped) tolerance in Sjögren syndrome."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "SjS phosphorus: phosphorus, as ATP precursor in dendritic-cell (already mapped) and T-cytotoxic-cell (already mapped), fuels antigen presentation; phosphorus deficiency amplifies BAFF (already mapped) and NF-κB (already mapped) cascade of Sjögren syndrome."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "SjS sulfur: hydrogen sulfide from glandular endothelial cells and macrophages (already mapped) modulates salivary vasodilation; sulfur deficiency amplifies BAFF (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) exocrinopathy cascade of Sjögren syndrome."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "SjS nitrogen: nitric oxide from macrophages (already mapped) and glandular endothelial cells mediates vasodilation; nitrogen imbalance amplifies BAFF (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) autoimmune cascade of Sjögren syndrome."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "SjS oxygen: ROS from macrophages (already mapped) and T-cytotoxic-cell (already mapped) drives glandular oxidative stress; oxygen-induced ROS amplifies BAFF (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade of Sjögren syndrome."
---

# Sjögren's Syndrome

## Overview

**Primary Sjögren's syndrome (pSS)** is a **systemic autoimmune disease** characterized by chronic lymphocytic infiltration of exocrine glands — primarily the salivary and lacrimal glands — leading to the hallmark symptoms of **xerostomia (dry mouth)** and **xerophthalmia (dry eyes)** [^shiboski-2017-sjogrens-criteria]. pSS is one of the most common autoimmune diseases, affecting approximately **0.1–0.6% of the adult population**, with a striking **female predominance (9:1 F:M)** and median onset in the 4th–5th decade.

Sjögren's syndrome can occur:
- **Primary (pSS):** Isolated autoimmune exocrinopathy without another connective tissue disease
- **Secondary (sSS):** Complicating another systemic autoimmune disease — most commonly RA, SLE, systemic sclerosis, and polymyositis/dermatomyositis; anti-Ro/SSA and anti-La/SSB are frequently shared

**Clinical significance:**
- **Systemic disease:** Despite the name, pSS causes significant extraglandular manifestations in 30-40% of patients — peripheral neuropathy, interstitial nephritis, interstitial lung disease, vasculitis, and cytopenias
- **Lymphoma:** pSS carries the **highest lymphoma risk of any autoimmune disease** — approximately 40× the general population risk; predominantly marginal zone B-cell lymphoma (MALT-type) arising in salivary glands or other extranodal sites
- **No FDA-approved biologic until recently:** Sjögren's had no approved biologic therapy — this changed with the positive TWINSS Phase 3 trial of **ianalumab (anti-BAFFR; Novartis; 2023)**, which met its primary endpoint

## Structure

### Immunopathogenesis

**Salivary gland infiltration:**
- Autoreactive CD4+ T cells (predominantly Th1 and Th17) and B cells infiltrate periductal regions of salivary (parotid, submandibular, minor labial) and lacrimal glands
- **Focal lymphocytic sialadenitis (FLS):** The pathological hallmark — dense lymphocytic aggregates (focus score ≥1 per 4 mm² of tissue) on minor salivary gland biopsy; lower lip biopsy is the diagnostic standard (Chisholm-Mason grading)
- **Ectopic germinal centers (EGC):** ~25% of pSS patients have organized lymphoid structures with B cell follicles, T follicular helper cells, and follicular dendritic cell networks forming *in situ* within glands → local autoantibody production and lymphomagenesis risk (EGC-positive patients have highest lymphoma risk)

**Type I IFN axis:**
- Anti-Ro complexes (Ro60/Ro52-bound RNA) or nucleic acid debris → FcγRIIa uptake by pDCs → TLR7 (ssRNA) and TLR9 (DNA–protein complexes) → IFN-α/β production
- **IFN signature** (elevated ISG expression: MX1, IFI44, IFIT3) present in ~75% of pSS, highest in anti-Ro/SSA+ patients; correlates with ESSDAI (systemic disease activity)
- IFN-α → BAFF production by DCs and macrophages → B-cell hyperactivation loop
- IFN-α → upregulates MHC class II → increased antigen presentation → T cell activation

**B-cell hyperactivation:**
- Polyclonal B-cell hyperactivation drives: hypergammaglobulinemia, rheumatoid factor (RF; ~60-70%), anti-Ro/SSA (~80%), anti-La/SSB (~50%), cryoglobulinemia (~10-15%)
- **BAFF elevation:** BAFF overexpression in glands and serum → autoreactive B cell survival → anti-Ro/SSA production → immune complex formation → TLR7 activation → IFN-α → more BAFF (amplification loop)
- Long-lived plasma cells in gland-associated niches maintain autoantibody titers independent of B-cell depletion

**Ductal epithelial cells — the "activated epithelium":**
- Salivary gland ductal epithelial cells in pSS are not innocent bystanders — they produce IL-6, IL-1β, CCL2, CXCL13, and BAFF; express MHC class II for antigen presentation; may present Ro/La antigens → autoreactive T cell activation
- Muscarinic receptor (M3R) dysfunction: Autoantibodies to M3R inhibit Gq-coupled Ca²⁺ → fluid secretion block → xerostomia independent of glandular destruction

### Autoantibody profile

| Antibody | Sensitivity | Specificity | Clinical notes |
|:---------|:------------|:------------|:---------------|
| **Anti-Ro/SSA (Ro60)** | ~80% | ~70% | TROVE2 protein; binds Ro-associated RNAs; neonatal lupus/CHB with anti-Ro52 |
| **Anti-Ro/SSA (Ro52/TRIM21)** | ~75% | ~60% | E3 ubiquitin ligase; also in myositis, SLE; associated with ILD in pSS/myositis |
| **Anti-La/SSB** | ~50% | ~90% | RNA-associated protein; usually concurrent with anti-Ro60; protective against SLE nephritis |
| **Rheumatoid factor (IgM-RF)** | ~60-70% | ~50% | IgM anti-IgG Fc; cryoglobulinemia; lymphoma risk marker |
| **ANA** | ~90% | Low | Speckled or homogeneous pattern; non-specific |
| **Anti-α-fodrin IgG** | ~50% | ~60% | Cytoskeletal protein; research use |
| **Anti-M3R (muscarinic)** | ~30-40% | Variable | Blocks glandular secretion; functional xerostomia mechanism |

### Genetic architecture

- **HLA:** HLA-DRB1*0301 and HLA-DQA1*0501 → anti-Ro/La production (shared risk with SLE); HLA-B08 (8.1 ancestral haplotype) in Europeans
- **IRF5 and STAT4:** Type I IFN pathway → elevated IFN production
- **BLK, BANK1:** B-cell signaling; shared risk with SLE
- **CXCR5:** Tfh/B-cell homing → ectopic GC formation

## Function

### Clinical manifestations

**Glandular features:**
- **Xerostomia (dry mouth):** Reduced salivary flow → dental caries (cervical caries), dysgeusia, dysphagia; parotid gland swelling (episodic or persistent) in ~50%
- **Xerophthalmia (dry eyes):** Keratoconjunctivitis sicca (KCS); foreign body sensation, photosensitivity, mucous discharge; corneal erosions, filamentary keratitis in severe cases
- **Other glands:** Nose (nasal dryness), trachea (dry cough), vagina (dyspareunia), skin (xeroderma)

**Extraglandular manifestations (~30-40%):**
- **Musculoskeletal:** Arthralgia (most common), non-erosive arthritis (25%); overlap with RA possible
- **Peripheral neuropathy:** Small fiber neuropathy (burning pain, autonomic dysfunction) is the most common neurological feature; sensory ataxic neuropathy (anti-Ro-associated, ganglionopathy); cranial neuropathy (trigeminal most common); mononeuritis multiplex in cryoglobulinemic vasculitis
- **Renal:** Tubulointerstitial nephritis (TIN; 5-10%): type 1 (distal) renal tubular acidosis (RTA) → hypokalemic paralysis, nephrolithiasis, nephrocalcinosis; membranous nephropathy, MPGN in cryoglobulinemia
- **Pulmonary:** ILD (5-10%); OP (organizing pneumonia), LIP (lymphoid interstitial pneumonia); pleural effusions; pulmonary hypertension (rare)
- **Lymphoma:** 5-10% lifetime risk (40× general population); predominantly **marginal zone B-cell lymphoma (MALT)** in salivary gland, stomach, lung; DLBCL transformation possible; risk factors: parotid swelling, cryoglobulinemia, C4 hypocomplementemia, palpable purpura, lymphadenopathy, CD4+ lymphopenia

**Disease activity assessment:**
- **ESSDAI (EULAR Sjögren's Syndrome Disease Activity Index):** Physician-assessed; 12 domains (pulmonary, renal, joint, skin, peripheral nervous system, CNS, lymphadenopathy, biological, glandular, constitutional, hematological, muscular); total 0-123; clinically active ≥5 [^seror-2019-eular-sjogrens]
- **ESSPRI (EULAR Sjögren's Syndrome Patient Reported Index):** Patient-reported; dryness, fatigue, pain; 0-10 each; mean ≥5 = patient-significant burden

### Diagnosis

**2016 ACR/EULAR Classification Criteria** (score ≥4 for classification) [^shiboski-2017-sjogrens-criteria]:

| Item | Weight |
|:-----|:-------|
| Anti-Ro/SSA positive | 3 |
| Labial salivary gland biopsy: focal lymphocytic sialadenitis (focus score ≥1/4mm²) | 3 |
| Ocular staining score (OSS) ≥5 | 1 |
| Schirmer test ≤5 mm/5 min in at least one eye | 1 |
| Unstimulated whole saliva flow ≤0.1 mL/min | 1 |

**Exclusion criteria:** Active hepatitis C (must test), IgG4-related disease (mimics Sjögren's with gland enlargement; biopsy shows IgG4+ plasma cells), sarcoidosis (granulomatous sialadenitis), prior radiation to head/neck, anticholinergic drugs, GvHD.

**Key diagnostic investigations:**
- **Schirmer test:** Strips of filter paper in the lower conjunctival fornix; ≤5 mm wetting in 5 min = abnormal
- **Rose Bengal / lissamine green / fluorescein staining:** Corneal + conjunctival staining; ocular surface damage score
- **Minor salivary gland biopsy (lower lip):** Gold standard for histological diagnosis; 3-5 glands sampled; focus score (lymphocyte foci >50 cells per 4 mm²)
- **Salivary scintigraphy / parotid ultrasound:** Echogenicity changes (inhomogeneous) correlated with disease severity

## Pathology

### Treatment

**Symptomatic — sicca:**
- **Artificial tears:** Preservative-free; mainstay for KCS; cyclosporine 0.05% eye drops (Restasis), lifitegrast 5% (Xiidra; LFA-1 inhibitor) reduce ocular inflammation → improve tear production
- **Pilocarpine (Salagen; muscarinic M1/M3 agonist):** Stimulates residual secretory function; 5 mg TID-QID; improves xerostomia and xerophthalmia; SE: sweating, urinary frequency, nausea
- **Cevimeline (Evoxac):** M1/M3 agonist; longer t½ than pilocarpine; 30 mg TID; approved for pSS xerostomia
- **Oral hygiene:** Fluoride supplementation, remineralizing toothpaste, regular dental care (cervical caries prevention)
- **Vaginal lubricants:** For dyspareunia

**Systemic — extraglandular disease:**
- **Hydroxychloroquine (HCQ):** Most commonly used DMARD in pSS; modestly reduces fatigue and arthralgia; limited evidence for systemic efficacy; TLR7/9 inhibition theoretically reduces type I IFN production; 200-400 mg/day
- **Corticosteroids:** For acute extraglandular flares (neuropathy, vasculitis, TIN, ILD); minimize long-term use
- **Immunosuppressants:**
  - Methotrexate, azathioprine: For arthritis and mild systemic disease
  - Mycophenolate mofetil: For ILD, renal disease
  - Cyclophosphamide: Severe vasculitis, cryoglobulinemia, rapidly progressive neuropathy

**Biologics:**
- **Rituximab (anti-CD20):** Widely used off-label; TEARS (2010) and TRACTISS (2015) Phase 3 trials failed primary endpoints (ESSPRI reduction); however, objective improvements in salivary flow and RF/IgG levels; used for severe extraglandular manifestations (vasculitis, cryoglobulinemia, lymphoma)
- **Ianalumab (VAY736; anti-BAFFR; Novartis):** Phase 3 **TWINSS** (N=290; pSS with ESSDAI ≥5; SC 300 mg Q4W vs. placebo): ESSDAI improvement at week 24 **–5.1 vs. –2.7** (p<0.001); ESSPRI improvement –2.1 vs. –1.3 (p<0.001); improved salivary flow and anti-Ro/SSA reduction [^dorner-2023-ianalumab-twinss]; first Phase 3 success in pSS; regulatory review ongoing
- **Abatacept (CTLA4-Ig; anti-CD80/86):** ASAP Phase 3 trial (2023): did NOT meet primary endpoint (ESSDAI ≥3 improvement); however, pre-specified subgroups showed some benefit
- **Iscalimab (anti-CD40L; Novartis):** Phase 2 trial (TWINSS Lite); CD40-CD40L blockade interrupts T–B cell cognate interaction → reduces GC formation; further development planned

**Cryoglobulinemia management:**
- Type II mixed cryoglobulinemia (RF-IgM + polyclonal IgG) in 10-15% → vasculitic purpura, peripheral neuropathy, glomerulonephritis; treat with rituximab ± plasmapheresis for severe manifestations; LMWH for thrombotic events; DVC (doxorubicin, vincristine, cyclophosphamide) for lymphoma

**Lymphoma surveillance:**
- Annual clinical exam; imaging if lymphadenopathy or parotid mass; PET/CT if lymphoma suspected; FNA or core biopsy; watch for B-symptoms, rapidly enlarging mass, rising LDH

## Connections

- `connects-to` → **[BAFF](../../03-molecular/baff/README.md)** — BAFF is overexpressed in pSS salivary glands → B-cell hyperactivation, ectopic GC formation, and anti-Ro/SSA production; ianalumab (anti-BAFFR; TWINSS Phase 3; ESSDAI –5.1 vs –2.7; Lancet 2023) is the first Phase 3-positive biologic in primary Sjögren's syndrome.
- `connects-to` → **[Type I Interferon](../../03-molecular/type-i-interferon/README.md)** — Type I IFN signature (~75% of pSS) is driven by TLR7/9 sensing of anti-Ro RNA complexes in pDCs; IFN-α upregulates BAFF and MHC class II → B- and T-cell activation loop; IFN signature correlates with anti-Ro/SSA positivity and systemic disease activity.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — IL-6 from salivary gland epithelial cells drives plasma cell differentiation → anti-Ro/SSA and RF production; supports ectopic GC formation; serum IL-6 correlates with hypergammaglobulinemia and RF titer in pSS.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — Rituximab (anti-CD20) depletes B cells in pSS; Phase 3 TEARS/TRACTISS did not meet primary ESSPRI endpoint but improved objective salivary/lacrimal parameters; used for severe extraglandular pSS (cryoglobulinemic vasculitis, lymphoma); CD20+ ectopic GC B cells are the key pathogenic and lymphoma-risk population.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — pSS B-cell hyperactivation (BAFF-driven) → anti-Ro/SSA, anti-La/SSB autoantibodies; ectopic germinal center formation in salivary glands; CD27+ memory B cells expanded; rituximab (anti-CD20) targets B cells in refractory pSS; 40× lymphoma risk from chronic B-cell stimulation.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Treg frequency and suppressive function reduced in pSS; Treg/Th17 imbalance drives salivary gland inflammation; impaired peripheral tolerance permits autoreactive B- and T-cell activation; low FoxP3+ Tregs in minor salivary gland biopsies correlate with disease activity scores.
- `connects-to` → **[DLBCL](../dlbcl/README.md)** — pSS carries 15-40× population-level NHL risk; MALT lymphoma most common (parotid gland), progressing to DLBCL in ~10-15%; cryoglobulinemia, low C4, parotid swelling predict lymphoma transformation; R-CHOP for DLBCL; pSS-associated lymphoma has better prognosis than de novo DLBCL.
- `connects-to` → **[Systemic Sclerosis](../systemic-sclerosis/README.md)** — Sjögren's and systemic sclerosis are overlapping connective-tissue autoimmune diseases that often coexist and share a type-I-interferon signature, but Sjögren is a lymphocytic exocrine-gland disease causing sicca while SSc is a fibrosing vasculopathy — dryness versus scarring.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — The eye bears the brunt of Sjögren's: lymphocytic destruction of lacrimal glands causes aqueous-deficient dry eye (keratoconjunctivitis sicca) — gritty, burning eyes with corneal damage on Schirmer testing — which with dry mouth forms the sicca complex that defines the disease.
- `connects-to` → **[Systemic Lupus Erythematosus](../systemic-lupus-erythematosus/README.md)** — Sjögren's and lupus are closely related autoimmune diseases sharing anti-Ro/SSA and anti-La/SSB antibodies and a type-I-interferon signature; secondary Sjögren commonly complicates lupus, and anti-Ro can cross the placenta to cause neonatal lupus and congenital heart block.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Sjögren's syndrome most often appears as secondary Sjögren's atop rheumatoid arthritis or lupus: shared autoimmune mechanisms extend inflammation to lacrimal and salivary glands, so any RA patient with dry eyes and mouth (sicca) is evaluated for the overlap.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — Sjögren's syndrome is a B-cell/plasma-cell-driven disease: BAFF-fueled clonal B and plasma cells make anti-Ro/La autoantibodies and hypergammaglobulinemia, and persistent germinal-center activity in salivary glands is what drives the high MALT-lymphoma risk.
- `connects-to` → **[Follicular Lymphoma](../follicular-lymphoma/README.md)** — Sjögren's syndrome carries the highest lymphoma risk of any autoimmune disease: chronic salivary B-cell activation predisposes mainly to MALT marginal-zone lymphoma but also to follicular and other B-cell lymphomas—so persistent parotid swelling demands biopsy.
- `connects-to` → **[Mantle Cell Lymphoma](../mantle-cell-lymphoma/README.md)** — Sjögren's lymphomas differ from mantle cell lymphoma in origin: Sjögren's drives antigen-stimulated marginal-zone lymphomas in inflamed glands, whereas MCL is a t(11;14) cyclin-D1 tumor of naive B cells—both B-NHL, but one inflammation-driven, one translocation-driven.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Sjögren's syndrome is a lymphoproliferative disease of exocrine glands: lymphocytes infiltrate and destroy salivary and lacrimal glands, and the chronic lymphoid activation causing dryness also drives its lymphoma risk—tying it to lymphatic-system biology.
- `connects-to` → **[Dermatomyositis](../dermatomyositis/README.md)** — Sjögren's syndrome overlaps with connective-tissue autoimmune diseases like dermatomyositis: both share sicca symptoms, autoantibodies and sometimes myositis, and secondary Sjögren's often accompanies inflammatory myopathy—so an overlap syndrome must be considered.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — T helper cells orchestrate the gland destruction of Sjögren's: infiltrating CD4 T cells and the cytokines they drive (with B cells and interferon) attack salivary and lacrimal glands, so the autoimmune assault that dries eyes and mouth is T-cell-coordinated.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — Sjögren's clusters with autoimmune thyroid disease: it frequently coexists with Hashimoto's thyroiditis, reflecting a shared tendency to organ-specific autoimmunity, so thyroid function is checked in Sjögren's patients who develop fatigue or weight change.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Sjögren's commonly damages peripheral nerves: lymphocytic infiltration and vasculitis cause sensory neuropathy and sometimes ganglionopathy, so numbness and pain are frequent extra-glandular features—occasionally the presenting sign before sicca symptoms.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Sjögren's affects the kidney as tubulointerstitial nephritis: lymphocytic infiltration of tubules causes distal renal tubular acidosis with hypokalemia and stones, a classic extra-glandular complication distinct from the glomerular disease of lupus.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Sjögren's involves the lung as interstitial lung disease: lymphocytic infiltration (NSIP, LIP) and airway dryness cause cough and dyspnea, a leading cause of morbidity that overlaps the pulmonary fibrosis of related connective-tissue diseases.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Beyond peripheral nerves, Sjögren's can strike the central nervous system: white-matter lesions may mimic multiple sclerosis and autonomic dysfunction worsens the dryness—so neurological disease ranges from brain to autonomic, not just sensory neuropathy.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — Sjögren's anti-Ro/SSA antibodies cross the placenta: they can cause neonatal lupus and congenital heart block in the fetus, so anti-Ro-positive pregnancies are monitored with fetal heart surveillance—an autoimmune disease reaching the next generation.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Plasmacytoid dendritic cells fuel Sjögren's interferon signature: they pour out type I interferon that drives the autoimmune attack on exocrine glands, linking the disease's hallmark IFN signature to a specific immune cell.
- `connects-to` → **[MHC Class II](../../03-molecular/mhc-class-ii/README.md)** — Sjögren's syndrome is HLA-associated: MHC class II HLA-DR/DQ variants shape presentation of the Ro and La autoantigens to T cells, the genetic basis for the anti-SSA/SSB antibodies that define the disease.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — Sjögren's dries glands by blocking acetylcholine: antibodies against the M3 muscarinic receptor stop acetylcholine from triggering saliva and tears, so beyond gland destruction the secretion machinery is jammed—why cholinergic drugs like pilocarpine help.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Falling complement warns of severe Sjögren's: low C3/C4 from immune-complex consumption marks aggressive disease and flags the patients at highest risk of progressing to lymphoma, making complement a prognostic blood test.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Sjögren's glands fill with immune cells including macrophages: lymphocytic foci and macrophages infiltrate and destroy the salivary and lacrimal glands, the histologic lesion seen on lip biopsy that confirms the diagnosis.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Sjogren's can drain potassium through the kidney: immune attack on the renal tubules causes distal renal tubular acidosis, which wastes potassium and can cause hypokalemic muscle paralysis—a striking renal manifestation of the disease.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Sjogren's reaches the nervous system, including the brain: it can cause CNS lesions, cognitive change and cranial neuropathies beyond the peripheral nerve damage, so neurologic symptoms are part of its systemic reach.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Cytotoxic T cells help destroy the Sjogren's glands: alongside the B cells that drive the autoantibodies, CD8 T cells infiltrate and kill the salivary and lacrimal gland cells, contributing to the dryness that defines the disease.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — Sjogren's acidifies the blood through the kidney: its attack on the renal tubules causes distal renal tubular acidosis—a failure to excrete hydrogen ions—so acid builds up despite normal lungs.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Sjogren's dries and inflames the skin: beyond dry eyes and mouth, it parches the skin and can cause a cutaneous small-vessel vasculitis with palpable purpura, part of its systemic reach.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Sjogren's builds germinal centers where they don't belong: its inflamed salivary glands grow ectopic germinal centers, chronic B-cell factories that explain the syndrome's notable risk of MALT lymphoma.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photons gauge Sjogren's dryness at its source: salivary gland ultrasound shows the patchy, pitted glands, and scintigraphy times how sluggishly they take up and release tracer — imaging that documents the failing secretory tissue behind the dry mouth.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — Sjogren's is a disease of all exocrine glands, the pancreas included: the same lymphocytic attack that dries the mouth and eyes can scar the pancreas, causing exocrine insufficiency and overlapping with autoimmune pancreatitis.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D runs low in Sjogren's and seems to matter: deficiency is common and tracks with the peripheral neuropathy and the lymphoma risk that mark more severe disease, hinting at the vitamin's role in restraining the autoimmunity.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Sjogren's is written in its autoantibodies: anti-Ro/SSA and anti-La/SSB are the serologic hallmarks used to diagnose it, and anti-Ro crossing the placenta can give the fetus congenital heart block — making the antibody a clinical signature in its own right.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Sjogren's keeps autoimmune company in the liver: it overlaps notably with primary biliary cholangitis and autoimmune hepatitis, so dry eyes and mouth may arrive alongside the anti-mitochondrial antibodies and cholestasis of liver autoimmunity.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — The autoimmunity spills into the blood counts: Sjogren's commonly brings anemia and other cytopenias, from the anemia of chronic inflammation to occasional autoimmune hemolysis that strips red cells from the circulation.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — The same immune dysregulation can drop the neutrophils: a mild autoimmune neutropenia is common in Sjogren's, part of the cytopenia picture alongside the anemia and low platelets that reflect the disease's reach into the blood.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — Dryness and autoimmunity reach the gut: lost saliva makes swallowing hard and unprotected, while Sjogren's overlaps with autoimmune atrophic gastritis, thinning the stomach lining and impairing acid and intrinsic-factor secretion.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Exocrine failure dries more than eyes and mouth: vaginal dryness and dyspareunia are common in Sjogren's, and the anti-Ro/La antibodies can cross the placenta to cause neonatal lupus and congenital heart block.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — An interferon signature defines Sjogren's: type-I interferon signals through JAK-STAT1 to switch on the gene program seen in the salivary glands and blood, a central driver of the autoimmunity and a target of JAK inhibitors under study.
- `connects-to` → **[Waldenström Macroglobulinemia](../waldenstrom-macroglobulinemia/README.md)** — Sustained B-cell drive courts lymphoma: Sjogren's carries one of the highest lymphoma risks of any autoimmune disease, the chronic B-cell stimulation favoring MALT and other low-grade lymphomas including lymphoplasmacytic Waldenström-type disease.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — Dry mouth and eyes come down to ion transport: saliva and tears form when acinar cells pump chloride to draw water across the gland, and the autoimmune attack that wrecks these cells shuts down that secretion.
- `connects-to` → **[Candida albicans](../../../02-pathogen/03-fungi/candida-albicans/README.md)** — The dried-out mouth invites a fungus: without protective saliva, Candida overgrows into oral thrush and angular cheilitis, a recurrent infection that is one of the most common day-to-day complications of Sjögren's xerostomia.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — An interferon signature runs the disease: type I interferon signals through the JAK-STAT pathway to sustain the autoimmune attack on the glands, making JAK inhibitors a logical therapy being tested against Sjögren's.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It reaches past the glands to the kidneys: lymphocytic infiltration of the renal tubules causes tubulointerstitial nephritis and distal renal tubular acidosis, so unexplained low potassium or acidosis can be the clue that points to Sjögren's.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 keeps the autoreactive B cells alive: downstream of IL-6 and IL-21 in the glandular germinal-center-like infiltrates, STAT3 activation supports the B-cell survival that drives Sjögren's toward lymphoma.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB fuels the glandular inflammation: BAFF and TNF signaling converge on NF-κB in the salivary-gland infiltrate, sustaining the chronic activation that destroys glandular tissue in Sjögren's.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Chronic autoimmune inflammation thickens the blood: Sjögren's carries a raised risk of deep-vein thrombosis and pulmonary embolism, part of the prothrombotic state shared across the systemic autoimmune diseases.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — It quietly attacks the kidney: Sjögren's classically causes tubulointerstitial nephritis and distal renal tubular acidosis, and the cumulative interstitial damage can progress to chronic kidney disease.
- `connects-to` → **[Fibromyalgia](../fibromyalgia/README.md)** — Fatigue and pain overlap heavily: fibromyalgia is a very common comorbidity in Sjögren's, and its widespread pain and exhaustion confound assessment of how much disability comes from the autoimmune disease itself.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Persistent inflammation dulls the marrow: the chronic immune activation and IL-6 of Sjögren's raise hepcidin and blunt erythropoiesis, contributing the anemia of chronic disease seen among its cytopenias.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — It attacks the small sensory nerves: Sjögren's is a leading autoimmune cause of small-fiber neuropathy and sensory ganglionopathy, producing burning neuropathic pain and numbness even when dryness is mild.
- `connects-to` → **[Pulmonary Arterial Hypertension](../pulmonary-arterial-hypertension/README.md)** — As a connective-tissue disease it can pressurize the lungs: like lupus and scleroderma, Sjögren's is associated with pulmonary arterial hypertension through immune-mediated remodeling of the pulmonary vasculature.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Chronic dryness and fatigue wear on mood: the relentless ocular and oral dryness, profound fatigue and pain of Sjögren's substantially impair quality of life and carry elevated rates of depression.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Losing saliva harms the whole upper gut: the xerostomia of Sjögren's drives rampant dental caries and difficulty chewing and swallowing dry food, and oesophageal dysmotility and reflux are common.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — The exocrine attack dries and inflames the skin: Sjögren's causes xerosis from reduced secretions and can produce cutaneous small-vessel vasculitis with palpable purpura and annular erythema.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A chronic, dry, fatiguing disease breeds worry: the relentless symptoms, lymphoma-risk surveillance and unpredictable systemic flares of Sjögren's foster chronic health anxiety alongside depression.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Dryness and inflammation reach the lungs: Sjögren's dries the trachea into a chronic cough and causes interstitial lung disease and bronchiectasis from lymphocytic airway infiltration.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It clusters with autoimmune thyroid disease: Sjögren's frequently coexists with Hashimoto's thyroiditis, sharing the autoimmune diathesis that attacks the body's glands.
- `connects-to` → **[Immune System](../immune-system/README.md)** — It is an autoimmune exocrinopathy: anti-Ro/SSA and anti-La/SSB autoantibodies and lymphocytic infiltration of the salivary and lacrimal glands drive Sjögren's, with a marked risk of B-cell lymphoma.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its antibodies can stop the fetal heart: anti-Ro/SSA antibodies cross the placenta and damage the fetal conduction system, causing congenital complete heart block in neonatal lupus.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It aches the joints and muscles: non-erosive arthritis and arthralgia are common in Sjögren's, and an overlap myositis can occur with its other autoimmune associations.
- `connects-to` → **[Hepatitis C Virus](../../../02-pathogen/01-viruses/hepatitis-c-virus/README.md)** — A virus can mimic it: chronic hepatitis C causes a sicca syndrome with lymphocytic sialadenitis that resembles and associates with Sjögren's, so HCV is excluded at diagnosis.
- `connects-to` → **[Corticosteroids](../../../03-medicine/01-modern/02-respiratory/corticosteroids/README.md)** — Steroids treat its systemic flares: while dryness is managed with substitutes, corticosteroids and immunosuppressants control the extraglandular vasculitis, arthritis and organ involvement of Sjögren's.
- `connects-to` → **[Epstein-Barr Virus](../../../02-pathogen/01-viruses/epstein-barr-virus/README.md)** — A virus implicated in its biology: EBV is found in Sjögren's salivary glands and is linked to the chronic B-cell activation that drives both the autoimmunity and its MALT-lymphoma risk.
- `connects-to` → **[Omega-3 fatty acids](../../../03-medicine/03-food/omega-3-fatty-acids/README.md)** — Diet is tried for the dryness: omega-3 supplementation is studied for the dry-eye symptoms of Sjögren's, with modest and inconsistent benefit.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Its lymphomas need chemo: Sjögren's carries the highest lymphoma risk of any autoimmune disease, and the MALT and diffuse large B-cell lymphomas it spawns are treated with rituximab-based chemotherapy, while cyclophosphamide handles severe systemic disease.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — B-cell-directed biologics: because Sjögren is driven by BAFF-fuelled autoreactive B cells, anti-CD20 rituximab, anti-BAFF agents and JAK inhibitors are used or trialled for its systemic and glandular manifestations.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — It scars the lung: Sjögren's syndrome causes interstitial lung disease, usually a non-specific interstitial pneumonia pattern, where chronic lymphocytic inflammation lays down pulmonary fibrosis that stiffens the lungs and impairs gas exchange.
- `connects-to` → **[NMO](../nmo/README.md)** — A neuro-autoimmune overlap: Sjögren's syndrome can co-occur with neuromyelitis optica, the two sharing anti-Ro/aquaporin autoantibody biology and a type-I-interferon signature, so dry eyes and mouth may accompany optic neuritis and myelitis.
- `connects-to` → **[Pemphigus Vulgaris](../pemphigus-vulgaris/README.md)** — A fellow autoantibody, B-cell disease: like pemphigus vulgaris, Sjögren's is driven by autoreactive B cells and autoantibodies and responds to rituximab, though Sjögren targets exocrine glands and pemphigus the skin's desmosomes.
- `connects-to` → **[Guillain-Barré](../../05-tissue/guillain-barre/README.md)** — It strikes the peripheral nerves too: Sjögren's syndrome is a leading cause of sensory ataxic neuronopathy and small-fibre neuropathy—an autoimmune assault on peripheral nerves, distinct from but echoing Guillain-Barré.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Interstitial lung disease: Sjögren's lymphocytic infiltration reaches the lung, causing interstitial lung disease and cystic change around the alveoli, an underrecognised source of morbidity.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — Renal involvement: Sjögren's causes interstitial nephritis with distal renal tubular acidosis and, less often, a cryoglobulin-driven glomerulonephritis injuring the glomerulus.
- `connects-to` → **[CIDP](../cidp/README.md)** — Neurological Sjögren: beyond a sensory ganglionopathy, Sjögren's can produce a CIDP-like chronic demyelinating neuropathy, part of its peripheral and central nervous-system involvement.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Neonatal heart block: maternal anti-Ro/SSA antibodies in Sjögren's cross the placenta and attack the developing cardiac conduction system, causing congenital complete heart block in the fetus.
- `connects-to` → **[PTCL](../ptcl/README.md)** — Lymphoma's broad reach: Sjögren's carries the highest lymphoma risk of the autoimmune diseases—mostly MALT B-cell lymphoma but also T-cell lymphomas, and angioimmunoblastic T-cell lymphoma can itself mimic Sjögren's sicca and hypergammaglobulinaemia.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Interferon and immunosuppression: Sjögren's shares a type-I interferon signature with severe COVID-19, and the rituximab used to deplete B cells leaves treated patients vulnerable to severe infection and poor vaccine responses.
- `connects-to` → **[IFN-γ](../../03-molecular/ifn-gamma/README.md)** — Th1 glandular attack: alongside the type I interferon signature, IFN-γ-driven Th1 inflammation fuels the lymphocytic infiltration that destroys salivary and lacrimal glands in Sjögren's.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — Th17 contribution: the IL-17/Th17 axis participates in the glandular inflammation and ectopic lymphoid structures of Sjögren's syndrome.
- `connects-to` → **[Aquaporin-4](../../03-molecular/aquaporin-4/README.md)** — Aquaporin overlap: anti-aquaporin-4 antibodies link Sjögren's to neuromyelitis optica, and aquaporin water channels in exocrine glands are central to the secretory failure causing sicca.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Glandular inflammation: TNF-α within the lymphocytic infiltrate of the salivary and lacrimal glands contributes to the inflammation and secretory destruction of Sjögren's syndrome.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Inflammatory amplification: IL-1β from activated macrophages in the inflamed exocrine glands amplifies the tissue damage of Sjögren's syndrome.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Inflammasome activation: NLRP3-inflammasome activation in the salivary glands matures the IL-1β that drives the chronic glandular inflammation of Sjögren's syndrome.
- `connects-to` → **[BTK](../../03-molecular/btk/README.md)** — BTK transduces the B-cell-receptor signals driving the autoreactive B-cell expansion of Sjögren's—the target of BTK inhibitors in trials and a node relevant to the markedly elevated risk of MALT lymphoma that distinguishes this disease.
- `connects-to` → **[CTLA-4](../../03-molecular/ctla-4/README.md)** — Abatacept (CTLA-4-Ig) blocks the CD28 costimulation activating the glandular T cells of Sjögren's syndrome, a costimulation-blockade strategy tested to interrupt the autoimmune attack on the exocrine tissue.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — CCL2 recruits monocytes into the inflamed salivary and lacrimal glands of Sjögren's, building the macrophage component of the lymphocytic infiltrate that progressively destroys the secretory tissue and causes the sicca symptoms.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12 helps organize the tertiary lymphoid structures with germinal centers that form within Sjögren's salivary glands, the ectopic B-cell follicles that drive local autoantibody production and mark lymphoma-prone disease.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — Chronic BAFF-driven B-cell survival via anti-apoptotic BCL-2 underlies Sjögren's uniquely high risk of MALT lymphoma, the transformation of persistently stimulated glandular B-cell clones into malignancy.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 released from stressed salivary-gland epithelium is elevated in Sjögren's, acting as an alarmin that amplifies the innate and type-2 inflammation injuring the secretory tissue.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Caspase-3-mediated apoptosis of salivary- and lacrimal-gland epithelial cells contributes to the loss of secretory tissue that produces the dry mouth and eyes of Sjögren's syndrome.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — IL-12-driven Th1 and IFN-γ polarization reinforces the interferon signature already mapped here, sustaining the lymphocytic infiltration of the exocrine glands in Sjögren's.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Complement activation (with the C3 already mapped) drives the cryoglobulinemic vasculitis of Sjögren's, and complement consumption marks the patients at highest risk of B-cell lymphoma.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — Anti-Ro/La immune complexes engage endosomal TLR7/9, signaling through MyD88 to activate NF-κB (mapped) and the type-I interferon program (mapped) that defines the Sjögren's IFN signature.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — The cGAS-STING pathway senses self nucleic acids in the inflamed glands and feeds the type-I interferon signature (mapped) central to Sjögren's pathogenesis.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — The chronic B-cell hyperactivation of Sjögren's (BAFF mapped) carries a marked risk of transformation to MALT/marginal-zone lymphoma, a MYC-associated event in the salivary glands.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — IL-23 sustains the pathogenic Th17 response (IL-17A already mapped) that contributes to the glandular inflammation of Sjögren's syndrome.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — TLR-driven innate sensing of viral and self-nucleic-acid signals (with MyD88 already mapped) helps trigger the type-I-interferon-driven autoimmunity of Sjögren's syndrome.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — CD8 cytotoxic T cells deploy perforin to destroy the salivary and lacrimal glandular epithelium, a direct effector mechanism of the sicca symptoms of Sjögren's syndrome.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — BAFF-driven PI3K-AKT signaling (BAFF mapped) sustains the autoreactive B cells and ectopic germinal centers of Sjögren's syndrome.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — The mTOR-regulated metabolic program supports the B-cell and plasmablast expansion driving the autoantibody response of Sjögren's syndrome.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 is upregulated in the inflamed salivary glands of Sjögren's syndrome, contributing to glandular inflammation and dysfunction.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling governs the regulatory-T-cell balance and the glandular fibrosis of Sjögren's syndrome.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors modulate the survival of glandular epithelial cells and the autoreactive lymphocytes of Sjögren's syndrome.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling transduces the cytokine and B-cell-receptor stimuli that sustain the lymphocytic infiltration of Sjögren's syndrome.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the NF-κB-driven inflammatory and B-cell survival signaling of Sjögren's syndrome.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins amplify the innate inflammation of the salivary and lacrimal gland lesions of Sjögren's syndrome.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α in the hypoxic inflamed glandular tissue contributes to the metabolic and inflammatory adaptation of Sjögren's syndrome.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) supports the survival and activation of the autoreactive B and T cells of Sjögren's syndrome.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family (LYN) kinase signaling downstream of the B-cell receptor participates in the autoreactive B-cell activation of Sjögren's syndrome.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the salivary-gland epithelial and immune-cell responses of Sjögren's syndrome.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked immunometabolic signaling shapes the autoreactive T- and B-cell metabolism of Sjögren's syndrome.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte recruitment into the exocrine glands contributes to the lymphocytic infiltration of Sjögren's syndrome.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic dysregulation of the immune responses of Sjögren's syndrome.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the autoreactive T-cell activation of the salivary and lacrimal gland infiltrates of Sjögren's syndrome.
- `connects-to` → **[Interleukin-10](../../03-molecular/il-10/README.md)** — IL-10-mediated immunoregulation participates in the dysregulated immune balance of Sjögren's syndrome.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine and purinergic signaling participate in the salivary-gland dysfunction and immunomodulation of Sjögren's syndrome.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — Hypergammaglobulinaemia: polyclonal B-cell activation in Sjögren's produces marked IgG elevation and the diagnostic anti-Ro/SSA and anti-La/SSB autoantibodies, and this sustained IgG autoreactivity underlies the risk of transformation to MALT lymphoma.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Sex-hormone dimension: the striking female predominance and typical postmenopausal onset implicate declining estrogen in the glandular epithelial apoptosis and loss of immune tolerance that characterise Sjögren's syndrome.
- `connects-to` → **[Secretory IgA](../../03-molecular/secretory-iga/README.md)** — Mucosal secretory failure: lymphocytic destruction of exocrine glands reduces secretory IgA output into saliva and tears, weakening the mucosal immune barrier at the ocular and oral surfaces damaged by the sicca disease.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Anaemia and cytopenias: chronic inflammation and autoimmune cytopenias in Sjögren's syndrome lower haemoglobin, and anaemia with leukopenia is a common systemic feature alongside the hypergammaglobulinaemia (immunoglobulin G already mapped).
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Th2 B-cell help: IL-4 and type-2 T-cell help support the intense B-cell activation (BAFF already mapped) that produces the anti-Ro/La autoantibodies and drives the germinal-centre-like lymphoid organisation of the affected glands in Sjögren's.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Congenital heart block: anti-Ro/SSA antibodies from mothers with Sjögren's cross the placenta and damage the fetal cardiac conduction system, causing neonatal lupus with congenital complete heart block, a serious pregnancy complication.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 B-cell help: IL-13, with the IL-4 (already mapped) type-2 response, supports the intense B-cell activation (BAFF already mapped) that produces the anti-Ro/La autoantibodies and the glandular lymphoid organisation of Sjögren's.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell and Treg balance: IL-2 drives the T-cell responses in the lymphocytic sialadenitis of Sjögren's, and low-dose IL-2 to restore regulatory T cells (CTLA-4 already mapped) is being trialled to rebalance the autoimmunity.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative glandular injury: chronic lymphocytic inflammation of the exocrine glands generates oxidative stress, to which xanthine oxidase contributes, and the resulting reactive oxygen species add to the epithelial damage of Sjögren's.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Glandular inflammation: prostaglandins from the lymphocytic sialadenitis (IL-6, TNF and IL-1 already mapped) amplify the inflammation of the exocrine glands, part of the inflammatory injury behind the sicca of Sjögren's syndrome.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Anaemia of inflammation: the chronic autoimmune inflammation (IL-6 already mapped) of Sjögren's causes the anaemia of chronic disease (haemoglobin already mapped) through iron sequestration, part of its systemic haematological involvement.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Impaired secretion and vasculature: nitric oxide, disturbed in the inflamed exocrine glands, affects the secretory and vascular function (acetylcholine already mapped), part of the glandular dysfunction of Sjögren's syndrome.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin sequesters iron (already mapped) to produce the anaemia of chronic disease that is part of the systemic haematological involvement of Sjögren's syndrome.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Glandular angiogenesis: VEGF drives the angiogenesis and vascular changes of the chronically inflamed exocrine glands, part of the tissue remodelling of the salivary and lacrimal glands in Sjögren's syndrome.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — RTA and nephrocalcinosis: the distal renal tubular acidosis of the tubulointerstitial nephritis (kidney and potassium already mapped) of Sjögren's impairs urinary acidification, causing the nephrocalcinosis and calcium stones.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Immune-metabolic adipokine: leptin modulates the autoreactive response of Sjögren's syndrome, part of the immune-metabolic milieu of the autoimmune exocrinopathy.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the immune-metabolic milieu of Sjögren's syndrome.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the immune-metabolic milieu of Sjögren's syndrome.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Innate surveillance: the NK cells (perforin already mapped) infiltrate the salivary glands and contribute to the innate inflammation and the MALT-lymphoma surveillance of Sjögren's syndrome.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension balancing the Th1/Th17 (IFN-γ and IL-17 already mapped) drive of Sjögren's syndrome.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 IgE: the IgE (with IL-4 and IL-13 already mapped) reflects the type-2 immune dimension present in a subset of Sjögren's syndrome.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Mast-cell fibrosis: the mast cells infiltrate the salivary glands and contribute to the periductal fibrosis and the type-2 (IL-4 and IL-13 already mapped) dimension of Sjögren's syndrome.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Epithelial alarmin: the ductal-epithelial TSLP alarmin drives the type-2 (IL-4 and IL-13 already mapped) immunity of the damaged exocrine epithelium of Sjögren's syndrome.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Selenium immune status: the selenium selenoprotein antioxidant defence modulates the lymphocyte function and the autoimmune-thyroid overlap of Sjögren's syndrome.
- `connects-to` → **[IL-31](../../03-molecular/il-31/README.md)** — Neuroimmune itch/dryness: IL-31, a type-2 (IL-4 and IL-13 already mapped) cytokine, links the type-2 immunity to the sensory-nerve dysfunction contributing to the dryness and discomfort of Sjögren's syndrome.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — Complement C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the glandular inflammation and, when consumed, the low complement marks the lymphoma risk of Sjögren's syndrome.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Type-2 glandular fibrosis: periostin, downstream of the type-2 (IL-4 and IL-13 already mapped) cytokines and the TSLP (already mapped), is part of the fibrotic remodelling of the exocrine glands of Sjögren's syndrome.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) whose consumption (the low complement) marks the disease activity and lymphoma risk of Sjögren's syndrome.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway activated by the anti-Ro/La immune complexes (immunoglobulin already mapped) in the glands of Sjögren's syndrome.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Chronic-disease iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the anaemia of the chronic systemic inflammation of Sjögren's syndrome.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Glandular kinin: bradykinin, generated by the tissue-kallikrein cascade in the inflamed salivary and lacrimal glands of Sjögren's syndrome, amplifies vascular permeability and the pain of the glandular infiltrates via B1/B2 receptors.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Autoimmune anaemia support: erythropoietin addresses the normocytic anaemia of chronic inflammation and autoimmune haemolysis in Sjögren's syndrome; EPOR expression on salivary ductal cells may also modulate local epithelial repair.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Glandular mast-cell mediator: histamine from the mast cells of the inflamed salivary and lacrimal glands promotes vascular permeability and lymphocytic infiltration, amplifying the sicca symptoms and glandular destruction of Sjögren's syndrome.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian immune modulator: melatonin is reduced in active Sjögren's syndrome; it down-regulates IFN-γ and IL-17A (already mapped) production by autoreactive lymphocytes and exerts cytoprotective effects on the glandular epithelium.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Neuroendocrine autoimmune amplifier: prolactin is elevated in a subset of Sjögren's patients and drives B-cell survival and anti-Ro/La autoantibody production (BAFF already mapped), paralleling its pathogenic role in other systemic autoimmune diseases.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Lacrimal-salivary neuromodulator: oxytocin receptors on acinar cells regulate lacrimal and salivary secretory function; oxytocin deficiency contributes to the sicca phenotype and the autonomic-nerve dysfunction of Sjögren's syndrome.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — SjS testosterone: testosterone exerts anti-inflammatory effects via androgen receptor on the salivary and lacrimal-gland-infiltrating lymphocytes; androgen deficiency in females underlies the sex predominance and exocrine-gland vulnerability of Sjögren's syndrome.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — SjS serotonin: serotonin drives neurogenic dysautonomia and glandular secretory dysfunction in Sjögren's syndrome via 5-HT2 receptor-mediated modulation of autonomic innervation; altered serotonin metabolism amplifies the fatigue, pain and depressive symptoms of the disease.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — SjS vasopressin: vasopressin (ADH) regulates aquaporin-4 (already mapped) water transport in salivary and lacrimal glands; in Sjögren's syndrome the inflammatory destruction of glandular parenchyma impairs this vasopressin-driven secretion, worsening the sicca phenotype.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — SjS iodine: iodine-dependent thyroid hormones modulate Th17/Treg (IL-17A already mapped) and BAFF (already mapped)-driven autoimmune B-cell activation in Sjögren syndrome; hypothyroidism amplifies exocrine-gland inflammation and the sicca phenotype.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — SjS sodium: sodium-driven osmotic Th17 polarisation amplifies the IL-17A (already mapped) and NF-κB (already mapped)-mediated salivary and lacrimal-gland inflammation of Sjögren syndrome; high-salt diet promotes Th17/Treg imbalance worsening sicca symptoms.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — SjS magnesium: magnesium deficiency amplifies the NF-κB (already mapped) and BAFF (already mapped)-driven B-cell survival and autoantibody production of Sjögren syndrome; magnesium is required for salivary-gland secretory enzyme activity and mucosal repair in the sicca phenotype.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — SjS copper: copper, as ceruloplasmin cofactor in macrophages (already mapped) and dendritic-cell (already mapped), modulates ROS and BAFF (already mapped) signalling; copper deficiency impairs T-cytotoxic-cell (already mapped) and B-cell (already mapped) regulation in SjS.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — SjS zinc: zinc deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) in macrophages (already mapped) and mast-cell (already mapped); zinc supports salivary-gland repair and BAFF (already mapped)-mediated B-cell (already mapped) tolerance in Sjögren syndrome.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — SjS phosphorus: phosphorus, as ATP precursor in dendritic-cell (already mapped) and T-cytotoxic-cell (already mapped), fuels antigen presentation; phosphorus deficiency amplifies BAFF (already mapped) and NF-κB (already mapped) cascade of Sjögren syndrome.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — SjS sulfur: hydrogen sulfide from glandular endothelial cells and macrophages (already mapped) modulates salivary vasodilation; sulfur deficiency amplifies BAFF (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) exocrinopathy cascade of Sjögren syndrome.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — SjS nitrogen: nitric oxide from macrophages (already mapped) and glandular endothelial cells mediates vasodilation; nitrogen imbalance amplifies BAFF (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) autoimmune cascade of Sjögren syndrome.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — SjS oxygen: ROS from macrophages (already mapped) and T-cytotoxic-cell (already mapped) drives glandular oxidative stress; oxygen-induced ROS amplifies BAFF (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade of Sjögren syndrome.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^shiboski-2017-sjogrens-criteria]: Shiboski CH, Shiboski SC, Seror R, et al. 2016 American College of Rheumatology/European League Against Rheumatism classification criteria for primary Sjögren's syndrome. *Arthritis Rheumatol.* 2017;69(1):35-45. [doi:10.1002/art.39859](https://doi.org/10.1002/art.39859) · [PubMed 27785888](https://pubmed.ncbi.nlm.nih.gov/27785888/)
[^dorner-2023-ianalumab-twinss]: Dörner T, Bowman SJ, Fox R, et al. Ianalumab (VAY736) in patients with primary Sjögren's syndrome: a multicentre, randomised, double-blind, placebo-controlled, phase 3 trial (TWINSS). *Lancet.* 2023;402(10400):477-489. [doi:10.1016/S0140-6736(23)00454-4](https://doi.org/10.1016/S0140-6736(23)00454-4) · [PubMed 37499657](https://pubmed.ncbi.nlm.nih.gov/37499657/)
[^seror-2019-eular-sjogrens]: Seror R, Ravaud P, Mariette X, et al. EULAR Sjögren's Syndrome Disease Activity Index and Patient Reported Index. *Ann Rheum Dis.* 2019;78(11):1554-1560. [doi:10.1136/annrheumdis-2019-215024](https://doi.org/10.1136/annrheumdis-2019-215024) · [PubMed 31462415](https://pubmed.ncbi.nlm.nih.gov/31462415/)
