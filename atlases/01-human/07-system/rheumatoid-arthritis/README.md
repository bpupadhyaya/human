---
schema: human-scale-entry/v1
id: rheumatoid-arthritis
name: Rheumatoid Arthritis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Autoimmune synovitis from Th17/macrophage TNF-alpha and IL-6 activation; ACPA/anti-CCP antibodies are diagnostic. Methotrexate is first-line; TNF inhibitors (adalimumab), IL-6 blockade (tocilizumab), and JAK inhibitors (baricitinib) for refractory disease."
aliases: ["RA", "rheumatoid disease", "adult RA", "seropositive arthritis", "inflammatory arthritis"]
sources:
  - id: smolen-2016-ra-lancet
    type: peer-reviewed
    cite: "Smolen JS, Aletaha D, McInnes IB. Rheumatoid arthritis. Lancet. 2016;388(10055):2023-2038."
    doi: "10.1016/S0140-6736(16)30173-8"
    pmid: "27156434"
    url: "https://doi.org/10.1016/S0140-6736(16)30173-8"
  - id: firestein-2003-ra-pathogenesis
    type: peer-reviewed
    cite: "Firestein GS. Evolving concepts of rheumatoid arthritis. Nature. 2003;423(6937):356-361."
    doi: "10.1038/nature01661"
    pmid: "12748655"
    url: "https://doi.org/10.1038/nature01661"
  - id: genovese-2016-baricitinib
    type: peer-reviewed
    cite: "Genovese MC, Kremer J, Zamani O, et al. Baricitinib in Patients with Refractory Rheumatoid Arthritis. N Engl J Med. 2016;374(13):1243-1252."
    doi: "10.1056/NEJMoa1507247"
    pmid: "27028914"
    url: "https://doi.org/10.1056/NEJMoa1507247"
cross_links:
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "TNF-alpha is the master cytokine in RA synovitis; synovial macrophages and fibroblasts produce TNF → NF-kB → MMP secretion and bone erosion; TNF inhibitors (etanercept, adalimumab, certolizumab) are the backbone of biologic DMARD therapy in RA."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 drives systemic RA inflammation (acute-phase response, anemia, fatigue) and Th17/Tfh polarization → ACPA production; tocilizumab and sarilumab (anti-IL-6R) improve ACR50 vs methotrexate alone; IL-6 is the dominant cytokine driving RA fever and CRP elevation."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Th17 cells produce IL-17A/F → recruit neutrophils and activate synovial fibroblasts; Tfh cells drive ACPA-producing B cells; Th1 drives macrophage activation; abatacept (CTLA-4-Ig) blocks CD28 co-stimulation, suppressing both T cell subsets in RA synovium."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-kB activated in RA synovial fibroblasts by TNF-alpha and IL-1beta → MMP secretion → cartilage degradation; NF-kB also induces RANKL → osteoclast activation → bone erosion; glucocorticoids and DMARDs (methotrexate, bDMARDs) suppress NF-kB as a shared mechanism."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A is present in RA synovium but secondary to TNF-alpha and IL-6; IL-17A promotes osteoclastogenesis via RANKL induction; IL-17A inhibitors (secukinumab) failed pivotal RA trials; bimekizumab (anti-IL-17A/F) showed marginal RA benefit vs established TNF/IL-6 blockade."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5+ macrophages and Th1 cells are abundant in RA synovium; CCR5 ligands (CCL3/CCL4/CCL5) are elevated in RA synovial fluid and correlate with disease activity; maraviroc (CCR5 antagonist) has been explored in RA with modest benefit in small trials."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "CCL2 is the dominant synovial chemokine in RA: synoviocytes and FLS secrete CCL2 → CCR2+ monocyte/macrophage recruitment → pannus formation; synovial fluid CCL2 >5 ng/mL correlates with radiographic damage; macrophage-derived RANKL and MMPs drive joint destruction."
  - target: 03-medicine/01-modern/12-anti-inflammatory/ibuprofen
    relation: treated-by
    note: "NSAIDs including ibuprofen reduce COX-2-driven synovial PGE₂ → less joint pain, swelling, and stiffness; adjuncts to DMARDs; reduce RA symptoms but not radiographic progression; long-term use requires GI prophylaxis (PPI)."
  - target: 03-medicine/01-modern/02-respiratory/corticosteroids
    relation: treated-by
    note: "Corticosteroids (prednisolone 5–10 mg/day) are bridge therapy in RA while DMARDs take effect; reduce radiographic progression in early RA (COBRA, BeSt trials); long-term use requires osteoporosis prophylaxis (bisphosphonate + calcium/vitamin D)."
  - target: 03-medicine/01-modern/11-biologics/adalimumab
    relation: treated-by
    note: "Adalimumab (anti-TNFα) is first-line biologic for MTX-inadequate RA; ARMADA trial: ACR50 59% vs 24% at 24 weeks; inhibits radiographic progression; mTNFα reverse signaling induces IL-10; TB screening mandatory before initiation (3-25× TB reactivation risk)."
  - target: 01-human/07-system/psoriatic-arthritis
    relation: connects-to
    note: "Rheumatoid and psoriatic arthritis are the two major inflammatory arthritides but contrast: RA is a symmetric, RF/anti-CCP-positive synovitis sparing the DIP joints, while PsA is a seronegative spondyloarthropathy with enthesitis, dactylitis, DIP disease, and psoriasis."
  - target: 01-human/07-system/sjogrens-syndrome
    relation: connects-to
    note: "Rheumatoid arthritis is the commonest disease complicated by secondary Sjögren's syndrome: chronic autoimmune inflammation extends to lacrimal and salivary glands, causing dry eyes and mouth (sicca), so RA patients are screened for the overlap."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Synovial fibroblasts are active drivers, not bystanders, of rheumatoid arthritis: activated fibroblast-like synoviocytes form the invasive pannus and secrete proteases and cytokines that erode cartilage and bone, behaving almost tumor-like—a therapeutic target."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "Rheumatoid arthritis and lupus are archetypal systemic autoimmune diseases: RA's anti-CCP/RF antibodies drive symmetric synovitis, while lupus's antinuclear antibodies form immune complexes injuring skin, kidney and other organs—overlapping yet distinct."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Rheumatoid arthritis accelerates osteoporosis through several routes: chronic inflammatory cytokines (TNF, IL-6) activate osteoclasts, immobility reduces loading, and glucocorticoid treatment thins bone—so RA patients fracture more and need bone protection."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "B cells are central to rheumatoid arthritis despite its joint focus: they make rheumatoid factor and anti-CCP autoantibodies, which is why the B-cell-depleting antibody rituximab controls RA—linking the autoantibody-making cell to the disease and its therapy."
  - target: 01-human/04-cellular/osteoclast
    relation: connects-to
    note: "Osteoclasts carve the bone erosions of rheumatoid arthritis: RANKL and TNF from inflamed synovium overactivate osteoclasts at the joint margin, eroding bone and cartilage—so the joint destruction on X-ray is osteoclast-mediated, a target of anti-TNF therapy."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Rheumatoid arthritis attacks the lung as well as joints: it causes interstitial lung disease, pleuritis and nodules, and RA-ILD is a major cause of death—so chronic cough or dyspnea in RA warrants pulmonary imaging, a key extra-articular manifestation."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Rheumatoid arthritis is a cardiovascular disease too: chronic systemic inflammation accelerates atherosclerosis, so RA patients die more of heart attacks and strokes than of joint disease—and controlling inflammation lowers that excess cardiovascular risk."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK inhibitors are a major oral therapy for rheumatoid arthritis: the cytokines that inflame the joint (IL-6, interferons, GM-CSF) signal through JAK, so tofacitinib and baricitinib match biologic efficacy in pill form when methotrexate fails."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages are central effectors in the rheumatoid joint: synovial macrophages pour out TNF and IL-1 that drive inflammation and erode cartilage and bone, and their numbers track disease activity—so TNF blockade quiets this macrophage-driven cascade."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Rheumatoid arthritis is the archetypal autoimmune disease of the musculoskeletal system: immune attack on the synovium forms an invasive pannus that destroys cartilage and bone, deforming joints—so autoimmunity strikes the skeleton's moving parts."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Rheumatoid arthritis's strongest genetic risk is the HLA 'shared epitope': MHC class II HLA-DRB1 variants present citrullinated self-peptides to T cells, explaining why anti-CCP antibodies form and why these alleles predispose to seropositive RA."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "The microbiome may help ignite rheumatoid arthritis: gum and gut bacteria such as Porphyromonas gingivalis citrullinate proteins, and dysbiosis is linked to disease onset—part of why periodontitis and RA travel together."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Rheumatoid arthritis reflects failed regulatory T-cell control: Tregs that should restrain autoreactive responses are reduced or dysfunctional, tipping the balance toward the Th17/inflammatory attack on the joints—a target for tolerance-restoring therapies."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "RA erodes bone through RANKL: inflamed synovial cells and T cells release RANKL that activates osteoclasts to chew through joint bone, producing the erosions on X-ray—so RANKL blockade (denosumab) can protect the joints."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "RA's immune attack targets joint collagen: type II collagen in cartilage is both an autoantigen and the tissue destroyed as the pannus invades, so the breakdown of collagen is what ultimately deforms the rheumatoid joint."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "RA may start when dendritic cells present citrullinated peptides: these antigen-presenters display modified self-proteins on HLA-DR to T cells, breaking tolerance and launching the anti-CCP autoimmunity that defines the disease."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Rheumatoid arthritis commonly causes anemia: chronic inflammation raises hepcidin that locks away iron, so the anemia of chronic disease tracks with disease activity and improves when the inflammation is controlled."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Rheumatoid arthritis's biggest killer is the heart: chronic systemic inflammation accelerates atherosclerosis, so cardiovascular disease—not joint damage—is the leading cause of death, and controlling RA lowers that risk."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils flood the rheumatoid joint and arm the autoimmunity: they pack the synovial fluid and release enzymes and NETs that citrullinate proteins, feeding the anti-CCP response and the cartilage destruction of the disease."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Rheumatoid arthritis inflames the eyes: it causes scleritis, episcleritis, and dry-eye keratoconjunctivitis, so red or gritty painful eyes in RA signal the autoimmunity reaching beyond the joints."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Rheumatoid arthritis scars the lungs: chronic inflammation drives interstitial lung fibrosis and forms fibrous rheumatoid nodules, a serious extra-articular complication that shortens life."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Rheumatoid arthritis drains calcium from bone: inflammation and steroids tip remodeling toward loss, eroding bone at joints and thinning the whole skeleton into osteoporosis."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photons chart rheumatoid joint destruction: X-rays catch the juxta-articular erosions and narrowed joint spaces that grade damage, while MRI and ultrasound reveal the active synovitis and early erosions before plain films can, guiding treatment."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "An enlarged spleen names a rare rheumatoid variant: Felty syndrome is the triad of longstanding RA, splenomegaly, and neutropenia, where the swollen spleen consumes white cells and leaves the patient prone to serious infection."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Rheumatoid immune complexes burn through complement: rheumatoid factor and anti-CCP antibodies bind into clusters that fix and consume complement, so low C3 in joint fluid and blood marks the active, sometimes vasculitic, disease."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Treating RA keeps watch on the liver: methotrexate and leflunomide, mainstays of disease-modifying therapy, can raise transaminases and rarely scar the liver, so enzymes are checked regularly and alcohol limited."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Plasma cells are RA's antibody foundries: differentiated from the autoreactive B cells, they secrete the rheumatoid factor and anti-CCP antibodies that drive the disease — the upstream B-lineage that rituximab depletes to quiet it."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Chronic inflammation starves the red cells: RA's high IL-6 drives hepcidin, locking iron away from the marrow to cause the anemia of chronic disease — the commonest extra-articular finding, tracking with how active the arthritis is."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Two antibodies define and forecast RA: rheumatoid factor and anti-CCP (ACPA) mark seropositive disease, predict a more erosive course, and can appear in the blood years before the first joint ever swells."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "RA pinches and inflames the nerves: synovial swelling at the wrist compresses the median nerve into carpal tunnel syndrome, while rheumatoid vasculitis can starve nerves into a mononeuritis multiplex of sudden focal weakness."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "The kidney is hit from several sides: decades of inflammation can deposit AA amyloid, the NSAIDs and disease-modifying drugs carry their own nephrotoxicity, and rarely a rheumatoid vasculitis inflames the glomeruli."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Inflammation hardens the arteries: chronic RA accelerates atherosclerosis, so heart attack and stroke — not the joints — are the leading cause of death, and controlling disease activity is itself cardiovascular prevention."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells crowd the inflamed joint: abundant in rheumatoid synovium, they release TNF, histamine and proteases that amplify inflammation and angiogenesis, an innate-immune contributor to the pannus that erodes cartilage and bone."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1 beta helps drive the joint destruction: secreted by synovial macrophages, it spurs cartilage breakdown and osteoclast bone erosion, the rationale for the IL-1 blocker anakinra in disease resistant to other biologics."
  - target: 01-human/03-molecular/ctla-4
    relation: connects-to
    note: "A brake on T-cell activation became a drug: abatacept is a CTLA-4-Ig fusion that blocks the co-stimulation T cells need, cooling the autoimmune attack on the joints — a treatment built directly from how this checkpoint normally restrains immunity."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "The inflamed joint grows new vessels: endothelial cells proliferate to vascularize the invading pannus, feeding the synovial overgrowth with oxygen and ferrying in the immune cells that sustain the destruction."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Chronic inflammation starves the marrow of iron: RA's high IL-6 drives hepcidin that locks iron away from red-cell production, producing the anemia of chronic disease that commonly shadows active rheumatoid arthritis."
  - target: 02-pathogen/01-viruses/epstein-barr-virus
    relation: connects-to
    note: "EBV is woven into RA's biology: the virus is implicated in triggering the autoimmunity, and reactivation underlies many of the methotrexate-associated lymphoproliferations that can complicate long-term RA treatment."
  - target: 01-human/07-system/dlbcl
    relation: connects-to
    note: "Chronic immune activation raises lymphoma risk: RA — especially highly active disease and immunosuppressive therapy — increases the risk of diffuse large B-cell lymphoma, sometimes EBV-driven and regressing when methotrexate is stopped."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "The inflammasome amplifies the synovitis: NLRP3 in synovial macrophages releases IL-1β that drives cartilage breakdown and osteoclast bone erosion, an innate-immune engine alongside the autoantibody response."
  - target: 01-human/07-system/tuberculosis
    relation: connects-to
    note: "Its biologics can wake latent TB: TNF-α inhibitors disable the granuloma that walls off Mycobacterium tuberculosis, so RA patients are screened and treated for latent infection before starting therapy to prevent reactivation."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: connects-to
    note: "Combination immunosuppression opens the lung to it: methotrexate plus steroids or biologics in RA can drop T-cell defenses enough for Pneumocystis pneumonia, sometimes warranting prophylaxis in high-intensity regimens."
  - target: 02-pathogen/01-viruses/hepatitis-b-virus
    relation: connects-to
    note: "Immunosuppression can reactivate it: rituximab and TNF inhibitors used in RA can reawaken occult hepatitis B, so serologic screening and antiviral prophylaxis precede these therapies to avert a flare."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Combined immunosuppression opens the lung to mold: corticosteroids stacked on biologics or JAK inhibitors for RA deeply blunt immunity, occasionally letting inhaled Aspergillus invade as pulmonary aspergillosis."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Chronic pain and disability press on mood: the relentless joint pain, fatigue and functional loss of RA, amplified by its inflammatory cytokines acting on the brain, give it markedly elevated rates of depression."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Inflammation and its JAK inhibitors raise the clot risk: active RA is a hypercoagulable, prothrombotic state, and the JAK inhibitors used to treat it carry a recognized signal for venous thromboembolism."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "Its JAK inhibitors notably reawaken shingles: tofacitinib and other JAK inhibitors used for RA, along with biologics and steroids, markedly raise the risk of herpes-zoster reactivation."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Chronic inflammation and its drugs scar the kidney: long-standing RA can deposit AA amyloid in the kidneys, and years of NSAID use add analgesic nephropathy, together driving chronic kidney disease."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "An unpredictable, painful disease breeds worry: the flares, disability and lifelong immunosuppressive treatment of RA foster chronic health anxiety alongside its well-documented depression."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It scars and nodules the lungs: rheumatoid arthritis causes interstitial lung disease, pulmonary nodules, pleuritis and bronchiectasis, and methotrexate adds a risk of hypersensitivity pneumonitis."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It can compress and inflame nerves: cervical atlantoaxial subluxation in RA threatens the spinal cord, and entrapment neuropathies and vasculitic mononeuritis multiplex injure peripheral nerves."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "It is an archetypal autoimmune disease: rheumatoid arthritis is driven by anti-citrullinated-protein and rheumatoid-factor autoantibodies and T-cell-driven synovial inflammation, the target of its immune therapies."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It shows on the skin: rheumatoid nodules form over pressure points, and rheumatoid vasculitis causes skin ulcers and nail-fold infarcts in severe seropositive disease."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It can swell the spleen and raise lymphoma risk: Felty's syndrome combines rheumatoid arthritis with splenomegaly and neutropenia, and chronic immune activation modestly increases lymphoma risk."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Inflammation and its drugs reach the kidney: sustained inflammation deposits secondary AA amyloid causing proteinuria, and NSAIDs and some disease-modifying drugs are nephrotoxic."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Its drugs burden the gut and liver: NSAIDs cause peptic ulcers, methotrexate is hepatotoxic, and Felty syndrome adds splenomegaly with neutropenia."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Pregnancy shifts its course: rheumatoid arthritis often eases in pregnancy and flares afterward, while methotrexate's teratogenicity demands contraception and planning."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Treatment and autoimmunity touch the glands: long-term corticosteroids suppress the adrenal axis and disturb glucose, and RA coexists with autoimmune thyroid disease."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Methotrexate anchors treatment: weekly low-dose methotrexate, a chemotherapy antimetabolite, is the first-line DMARD for rheumatoid arthritis, controlling synovitis and serving as the backbone for combination with biologics."
  - target: 01-human/07-system/ankylosing-spondylitis
    relation: connects-to
    note: "Seropositive versus seronegative: RA is a symmetric, anti-CCP/RF-positive small-joint synovitis, whereas ankylosing spondylitis is an HLA-B27 axial spondyloarthropathy with sacroiliitis and enthesitis — the two poles of inflammatory arthritis."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "It erodes bone at the joint: RANKL-driven osteoclasts in the rheumatoid pannus carve marginal bone erosions and periarticular osteopenia, while chronic inflammation and steroids add systemic bone loss."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "It builds lymphoid follicles in the joint: rheumatoid synovium forms ectopic germinal centres where autoreactive B cells produce anti-citrullinated-protein antibodies, which is why B-cell depletion with rituximab controls the disease."
  - target: 01-human/07-system/multiple-sclerosis
    relation: connects-to
    note: "A caution for its TNF blockers: the anti-TNF biologics central to rheumatoid arthritis can unmask or worsen demyelination, so multiple sclerosis contraindicates them—one cytokine blockade helping joints yet harming nerves."
  - target: 01-human/07-system/immune-thrombocytopenia
    relation: connects-to
    note: "Felty and beyond: rheumatoid arthritis can drive secondary immune cytopenias—Felty syndrome pairs RA with splenomegaly and neutropenia, and immune thrombocytopenia also complicates it as the same autoimmunity turns on blood cells."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "Accelerated atherosclerosis: RA's chronic systemic inflammation accelerates atherosclerosis of the arterial wall, making cardiovascular disease the leading cause of death and shortening lifespan beyond the joint disease itself."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "RA-associated interstitial lung disease: rheumatoid arthritis causes interstitial lung disease and fibrosis around the alveoli—a major extra-articular cause of death—alongside rheumatoid nodules and pleuritis."
  - target: 01-human/07-system/iga-nephropathy
    relation: connects-to
    note: "When inflammation reaches the kidney: long-standing RA can drive secondary IgA nephropathy and AA amyloidosis, the acute-phase response depositing in the glomerulus—a systemic joint disease turning renal."
  - target: 01-human/07-system/ptcl
    relation: connects-to
    note: "Clonal T-cells in chronic autoimmunity: rheumatoid arthritis is classically associated with T-cell large granular lymphocytic leukaemia (Felty-like neutropenia) and a raised risk of T-cell lymphomas alongside the more familiar B-cell ones."
  - target: 01-human/07-system/gout
    relation: connects-to
    note: "Two inflammatory arthritides: gout and rheumatoid arthritis can mimic and even coexist, both causing acute swollen joints and erosions, distinguished by urate crystals versus autoantibodies and pannus."
  - target: 01-human/07-system/psoriasis
    relation: connects-to
    note: "Paradoxical psoriasis: the anti-TNF biologics that treat rheumatoid arthritis can paradoxically trigger psoriasiform skin eruptions, an unexpected adverse effect of blocking a cytokine central to both diseases."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Pannus angiogenesis: VEGF-driven new vessel growth feeds the invasive synovial pannus of rheumatoid arthritis, sustaining the inflamed tissue that erodes joints."
  - target: 01-human/03-molecular/baff
    relation: connects-to
    note: "Autoantibody support: BAFF sustains the autoreactive B cells that produce rheumatoid factor and anti-citrullinated-protein antibodies central to rheumatoid arthritis."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 inflammation: the IL-23/Th17 axis drives the IL-17-mediated synovial inflammation of rheumatoid arthritis, complementing TNF and IL-6 signalling."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 contribution: IFN-γ from Th1 cells participates in the mixed cytokine milieu of the rheumatoid synovium, activating macrophages that drive joint destruction."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Pannus hypoxia: the hyperplastic, poorly perfused rheumatoid synovium becomes hypoxic, stabilising HIF-1α to drive the VEGF angiogenesis that feeds the invasive pannus."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Synovial proliferation: PDGF drives the proliferation of the synovial fibroblasts that form the destructive pannus invading cartilage and bone in rheumatoid arthritis."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "B-cell depletion: rituximab depletes CD20+ B cells in rheumatoid arthritis, cutting autoantibody production and antigen presentation — proof that B cells, not just T cells and cytokines, drive the disease."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "Alarmin biomarker: calprotectin (S100A8/A9) released by activated synovial neutrophils and monocytes amplifies joint inflammation through TLR4 and serves as a sensitive serum marker of rheumatoid disease activity."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "Citrullinated autoantigen: citrullinated fibronectin in the rheumatoid synovium is a target of anti-citrullinated-protein antibodies, and fibronectin fragments stimulate the matrix-degrading enzymes that erode cartilage."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Symptomatic eicosanoid axis: COX-2-derived prostaglandins generated in the inflamed rheumatoid synovium produce much of the pain, swelling and warmth, the target of the NSAIDs that relieve symptoms without altering the underlying disease course."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "Synovial alarmin: IL-33 released from damaged rheumatoid synoviocytes acts as an alarmin on mast cells and innate lymphoid cells, amplifying the cytokine cascade and helping translate joint injury into self-perpetuating synovial inflammation."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Th17 polarisation and fibrosis: TGF-β together with IL-6 drives naive T cells toward the pathogenic Th17 lineage central to RA, while also activating synovial fibroblasts that build the invasive pannus."
  - target: 01-human/03-molecular/fibrinogen
    relation: connects-to
    note: "Citrullinated autoantigen: citrullinated fibrinogen is a principal target of the anti-citrullinated-protein antibodies (anti-CCP) of rheumatoid arthritis, and immune complexes formed with it deposit in the joint to drive synovial inflammation."
  - target: 01-human/03-molecular/btk
    relation: connects-to
    note: "B-cell and Fc signalling: Bruton's tyrosine kinase relays B-cell-receptor and Fc-receptor signals in the autoreactive B cells and myeloid effectors of rheumatoid arthritis, an axis (with the CD20 B cells and BAFF already mapped) targeted by BTK inhibitors under study."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Complement amplification: the immune complexes of rheumatoid arthritis activate complement in the synovium, and C5/C5a amplify the inflammatory cell recruitment and joint damage, extending the C3 arm already mapped."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-JAK-STAT effector: IL-6 signalling through JAK (both mapped) activates STAT3, the transcription factor driving synovial inflammation and Th17 differentiation, central to the JAK-inhibitor and anti-IL-6 mechanisms in RA."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Innate hub: IL-1 receptor and TLR signalling converge on MyD88 to activate NF-κB (mapped), amplifying the innate-immune drive of rheumatoid synovitis."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Regulatory deficit: a relative shortfall of anti-inflammatory IL-10 against the dominant TNF, IL-6 and IL-17 (all mapped) contributes to the failure of resolution in rheumatoid synovitis."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Innate perpetuation: TLR4 sensing of damage-associated and citrullinated self-molecules (with MyD88 already mapped) helps initiate and perpetuate the synovial inflammation of rheumatoid arthritis."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Synovial immunometabolism: mTOR-driven metabolic reprogramming of synovial fibroblasts and Th17 cells sustains the aggressive, invasive pannus of rheumatoid arthritis."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Fibroblast survival: PI3K-AKT signalling promotes the survival, proliferation and apoptosis-resistance of the rheumatoid synovial fibroblasts that drive joint destruction."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signalling drives the aggressive fibroblast-like synoviocyte proliferation that builds the invasive pannus of rheumatoid arthritis."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 is highly expressed by rheumatoid synovial fibroblasts, amplifying joint inflammation and serving as a biomarker of disease activity."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-γ-STAT1 signalling (IFN-γ mapped) drives the Th1 and macrophage activation contributing to rheumatoid synovitis."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "DNA within the neutrophil extracellular traps that source citrullinated autoantigens engages cGAS-STING, amplifying the autoimmune inflammation of rheumatoid arthritis."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling governs the regulatory-T-cell balance and the synovial fibrosis of rheumatoid arthritis."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated CD8 cytotoxicity contributes to the synovial tissue injury of rheumatoid arthritis."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors regulate the survival and activation of the T cells and synovial fibroblasts driving rheumatoid arthritis, their dysregulation contributing to synovial hyperplasia."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the NF-κB-driven inflammatory cytokine production of the rheumatoid synovium."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling in synovial fibroblasts and osteoclasts contributes to the invasive pannus and bone erosion of rheumatoid arthritis."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) supports the survival and activation of the fibroblast-like synoviocytes and immune cells of rheumatoid arthritis."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked immunometabolic signaling shapes the T-cell activation and synoviocyte metabolism of rheumatoid arthritis."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the citrullination, osteoclastogenesis, and synoviocyte survival relevant to rheumatoid arthritis."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of the synovial fibroblasts and immune cells of rheumatoid arthritis."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling, a target of immunosuppressive therapy, participates in the autoreactive T-cell activation of rheumatoid arthritis."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the leukocyte and fibroblast recruitment into the inflamed synovium of rheumatoid arthritis."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine signaling, the mechanism of methotrexate's anti-inflammatory action, participates in the immunomodulation of rheumatoid arthritis."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Type I interferon signaling participates in the interferon signature and immune dysregulation of rheumatoid arthritis."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin participates in the synovial inflammation and bone/cartilage destruction of rheumatoid arthritis."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Rheumatoid factor: RF is an autoantibody directed against the Fc portion of IgG, one of the two classic RA serologies alongside anti-CCP, and the resulting immune complexes fix complement (C3/C5 already mapped) to drive synovial inflammation."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Cardiovascular mortality: chronic systemic inflammation in rheumatoid arthritis impairs endothelial nitric-oxide function, driving the accelerated atherosclerosis that is the leading cause of the excess cardiovascular death seen in RA."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Pannus angiogenesis: the invasive rheumatoid pannus depends on new blood vessels driven by angiopoietin-Tie2 and VEGF (VEGF already mapped) to feed the hyperplastic, hypoxic synovium that erodes cartilage and bone."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Anaemia of chronic disease: the sustained IL-6-driven inflammation of rheumatoid arthritis (hepcidin pathway) suppresses erythropoiesis, and the resulting anaemia lowering haemoglobin is the commonest extra-articular manifestation."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Cardiovascular mortality: accelerated atherosclerosis from chronic inflammation (nitric oxide already mapped) raises the risk of myocardial infarction in rheumatoid arthritis, and troponin marks the cardiac injury of the events that drive its excess death."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Sex and hormonal modulation: rheumatoid arthritis is about three times more common in women, and estrogen influences the disease, which often improves in pregnancy and can flare postpartum and around the menopause."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Lipid paradox and cardiovascular risk: rheumatoid arthritis alters cholesterol handling, and despite the lipid paradox of low levels in active disease, the inflammation accelerates atherosclerosis (nitric oxide already mapped) and cardiovascular risk."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative synovitis: reactive oxygen species generated in the inflamed synovium, to which xanthine oxidase contributes, damage cartilage and amplify inflammation, and the associated hyperuricaemia links rheumatoid arthritis to coexisting gout."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Adipokine inflammation: adiponectin and other adipokines from articular and systemic fat modulate the synovial inflammation of rheumatoid arthritis, part of the metabolic-immune crosstalk shaping disease activity and its cardiovascular comorbidity."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Anaemia of inflammation: the IL-6 surge (already mapped) of rheumatoid arthritis raises hepcidin, sequestering iron to produce the anaemia of chronic disease (haemoglobin already mapped) common in active disease."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Pro-inflammatory adipokine: leptin, with adiponectin (already mapped), links the articular and systemic fat to the synovial inflammation of rheumatoid arthritis, part of the adipokine-immune crosstalk shaping disease activity."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Insulin resistance: the systemic inflammation (TNF and IL-6 already mapped) and the glucocorticoids used to treat rheumatoid arthritis cause insulin resistance, contributing to the metabolic and cardiovascular comorbidity of the disease."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Synovial adipokine: resistin, a pro-inflammatory adipokine (leptin and adiponectin already mapped), is elevated in the synovial fluid and serum of rheumatoid arthritis and correlates with the disease activity."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Th2 counter-regulation: IL-4 and the Th2/M2 arm (IL-10 already mapped) oppose the Th17 and Th1 (IL-17, IL-23 and IFN-γ already mapped) drive of the synovitis, the anti-inflammatory balance in rheumatoid arthritis."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 arm: IL-13, with IL-4 (already mapped), is part of the type-2 cytokine response whose balance against the pro-inflammatory signals shapes the joint inflammation of rheumatoid arthritis."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "MMP and inflammation: the disturbed zinc homeostasis (low serum zinc) of the active rheumatoid inflammation, and the zinc-dependent matrix metalloproteinases that degrade the joint cartilage (collagen already mapped)."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Antioxidant defence: selenium supports the antioxidant selenoprotein defence, and low selenium is associated with rheumatoid arthritis and its oxidative (xanthine oxidase already mapped) joint damage."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Synovial mast cells: the synovial mast cells release histamine that contributes to the vascular permeability and the inflammation of the rheumatoid synovitis."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm complementing the dominant Th17 (IL-17 already mapped) axis of rheumatoid arthritis."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 counter-arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 arm balancing the Th17/Th1 drive of rheumatoid arthritis."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Synovial NK cells: the NK cells (perforin already mapped) infiltrate the rheumatoid synovium and modulate the innate inflammation of rheumatoid arthritis."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Synovial CD8 cells: the cytotoxic (CD8) T cells (perforin already mapped) infiltrate the rheumatoid synovium and contribute to the local tissue damage of rheumatoid arthritis."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the type-2 immune dimension balancing the dominant Th17/Th1 drive of rheumatoid arthritis."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Immunomodulatory vitamin: vitamin D modulates the T-cell (already mapped) autoimmunity, and its deficiency is associated with the higher disease activity of rheumatoid arthritis."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the neutrophil (already mapped) recruitment into the inflamed synovium of rheumatoid arthritis."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Stromal alarmin: TSLP, from the synovial fibroblasts (already mapped) and stroma, conditions the dendritic cells (already mapped) and contributes to the pro-inflammatory milieu of the rheumatoid synovium."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Synovial matricellular: periostin, secreted by the synovial fibroblasts (already mapped), is part of the matricellular remodelling of the pannus and the bone erosion (RANKL already mapped) of rheumatoid arthritis."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) whose dysregulation on the immune complexes drives the synovial complement activation of rheumatoid arthritis."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway activated by the ACPA and rheumatoid-factor (immunoglobulin already mapped) immune complexes in the rheumatoid synovium."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Chronic-disease iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the anaemia of chronic disease of rheumatoid arthritis."
---

# Rheumatoid Arthritis

## Overview

**Rheumatoid arthritis (RA)** is a **chronic, systemic autoimmune disease** characterized by persistent synovial inflammation, progressive joint destruction, and extra-articular manifestations. It affects approximately **1% of the global population** (~18 million people), with a female:male ratio of ~3:1, and peak incidence between 40-60 years of age. RA is the most common inflammatory arthritis and a leading cause of disability worldwide [^smolen-2016-ra-lancet].

RA is defined by **synovitis** — inflammation of the synovial membrane lining the joint — driven by an aberrant adaptive immune response against self-antigens, particularly **citrullinated proteins** (resulting from post-translational deimination of arginine to citrulline by PAD enzymes). The resulting **ACPA (anti-citrullinated protein antibodies) / anti-CCP** response is pathognomonic: detected in ~70% of RA patients and present years before clinical disease.

**Classification criteria (ACR/EULAR 2010):** Score ≥6/10 defines RA; includes joint involvement (0-5), serology (RF/ACPA, 0-3), acute-phase reactants (0-1), and duration (0-1).

**Clinical heterogeneity:**
- **Seropositive RA** (~70-80%): RF and/or ACPA positive; more destructive disease; higher risk of erosions and extra-articular manifestations
- **Seronegative RA** (~20-30%): No RF/ACPA; diagnosis by clinical criteria; may represent heterogeneous group including early seronegative psoriatic arthritis, reactive arthritis
- **Very early RA (VERA):** Undifferentiated arthritis evolving to RA; window of opportunity for remission induction before structural damage

## Structure

### Synovial pathology [^firestein-2003-ra-pathogenesis]

Normal synovium: 1-2 cell layers of synoviocytes (type A macrophage-like, type B fibroblast-like) on a thin, vascularized stroma.

**RA pannus formation:**
- **Synovial hyperplasia:** Inflammatory cytokines (TNF-alpha, IL-6, IL-1beta) → synoviocyte proliferation → synovium thickens to 6-10 cell layers
- **Angiogenesis:** VEGF and TNF-alpha → neovascularization → sustains inflammatory infiltrate
- **Cellular infiltrate:** CD4+ T cells (predominantly Th1, Th17) and B cells (follicle-like structures in ~25%) + macrophages + plasma cells (produce RF and ACPA locally)
- **Pannus:** Invasive synovial tissue → invades and destroys cartilage and bone at the cartilage-pannus junction
- **Fibroblast-like synoviocytes (FLS):** Central pathological effector; produce: MMP-1/3/13 → cartilage collagen degradation; RANKL → osteoclast differentiation; IL-6, IL-8, VEGF; also migrate and spread disease to other joints (metastasis-like)

### Pathogenic sequence

**1. Initiating events (years before clinical disease):**
- Genetic susceptibility: **HLA-DRB1 shared epitope** (SE alleles: *0101, *0401, *0404) — SE presents citrullinated peptides to CD4+ T cells; OR 3-5× for seropositive RA
- Environmental triggers: Smoking (most reproducible; promotes citrullination in lungs → anti-CCP production → systemic spread); periodontal disease (P. gingivalis, a citrullinating bacterium); microbiome dysbiosis
- Citrullination: PAD2/4 enzymes citrullinate proteins (vimentin, fibrinogen, alpha-enolase, type II collagen) → neoepitopes presented by SE HLA-DR → ACPA production

**2. Pre-clinical phase:**
- ACPA (IgG, IgM, IgA) and RF in serum; no joint inflammation
- Systemic inflammatory biomarkers: elevated IL-6, TNF-alpha, sRANKL in blood
- First-degree relatives with ACPA: 1-2%/year rate of progression to RA

**3. Clinical synovitis:**
- ACPA-immune complex formation in synovium → activates complement → C3a/C5a → mast cell degranulation and macrophage activation
- **Macrophages:** Master orchestrators; produce TNF-alpha, IL-1beta, IL-6, IL-12/23 → amplify all downstream pathways
- **Th17 cells:** IL-17A/F → IL-17R on FLS and osteoblasts → IL-6, IL-8, CXCL1 (neutrophil recruitment), RANKL (osteoclast activation)
- **B cell involvement:** ACPA and RF production by plasma cells; B cells also present antigens to T cells and produce cytokines; B cell depletion (rituximab) effective

## Function

### Clinical presentation [^smolen-2016-ra-lancet]

**Articular:**
- **Symmetrical polyarthritis:** MCPs, PIPs, wrists, MTPs most commonly; DIP joints typically spared (vs psoriatic arthritis)
- **Morning stiffness:** >1 hour of joint stiffness/pain on waking → correlates with synovitis activity; a key diagnostic criterion
- **Synovitis on exam:** Warm, swollen, tender joints; synovial thickening (boggy texture); reduced grip strength
- **Joint deformities (chronic/untreated RA):**
  - Ulnar deviation of MCPs
  - Swan-neck deformity (MCP flexion, PIP hyperextension, DIP flexion)
  - Boutonnière deformity (PIP flexion, DIP hyperextension)
  - Z-thumb deformity
  - Hammer toes
- **Cervical spine:** C1-C2 atlantoaxial subluxation (cricoarytenoid involvement → hoarseness); screen pre-surgery

**Extra-articular manifestations (~40% of RA):**
- **Rheumatoid nodules:** Fibrinoid necrosis surrounded by palisading macrophages; elbows, fingers, bursae; associated with RF+/seropositive disease and MTX use (accelerated nodulosis)
- **Cardiovascular disease:** Major cause of excess RA mortality; systemic inflammation accelerates atherosclerosis; doubled risk of MI; treat CV risk aggressively; anti-TNF therapy reduces CV events
- **Interstitial lung disease (ILD):** UIP or NSIP pattern; ~10%; anti-CCP+ and male sex are risk factors; smoking cessation critical
- **Felty's syndrome:** RA + splenomegaly + neutropenia → recurrent infections
- **Scleritis, episcleritis**
- **Peripheral neuropathy, mononeuritis multiplex (vasculitis)**

**Disease activity measures:**
- **DAS28:** 28-joint disease activity score; ESR and CRP-based; remission <2.6, low activity 2.6-3.2
- **CDAI/SDAI:** Clinical/simplified disease activity index
- **Treat-to-target (T2T) strategy:** Target DAS28 remission or low disease activity; monthly adjustment until target achieved

### Extra-articular: CV and cancer risk

RA patients have:
- **2× increased cardiovascular mortality** (atherosclerosis acceleration via systemic inflammation; endothelial dysfunction; dyslipidemia from steroids)
- **~2× increased lymphoma risk** (particularly diffuse large B-cell; correlates with disease activity, not treatment)
- **Reduced solid tumor risk** (colorectal) relative to general population

## Pathology

### Diagnosis

**Laboratory:**
- **RF (IgM anti-IgG Fc):** Sensitivity 70%, specificity ~80%; also positive in Sjögren's (>75%), hepatitis C (40-70%), healthy elderly (~5%)
- **ACPA (anti-CCP, Ig class mixture):** Sensitivity 70%, specificity **>95%** — best serological marker for RA diagnosis; detectable 10+ years before symptom onset
- **CRP, ESR:** Correlate with disease activity; CRP more sensitive than ESR for monitoring
- **CBC:** Anemia of chronic disease (normocytic, normochromic); thrombocytosis during active disease
- **Complete metabolic panel:** Monitor for treatment-related hepatotoxicity (MTX) and renal disease

**Imaging:**
- **X-ray:** Periarticular osteopenia (early) → joint space narrowing → marginal erosions (late, irreversible); modified Sharp-van der Heijde score to track progression
- **Ultrasound:** Synovitis (grey-scale) and active vascularity (power Doppler) in real-time; detects subclinical synovitis and guides joint aspiration
- **MRI:** Most sensitive for bone marrow edema (pre-erosive) and synovitis; RAMRIS (RA MRI scoring) in clinical trials

### Treatment [^genovese-2016-baricitinib]

**Treat-to-target strategy:** Aggressive early therapy, monthly monitoring until remission, then taper.

**Conventional synthetic DMARDs (csDMARDs):**
- **Methotrexate (MTX):** First-line; weekly oral/subcutaneous; folate antagonist → adenosine-mediated anti-inflammatory; 15-25 mg/week; folic acid co-administration; monitor LFTs, CBC; teratogenic; combinations with bDMARDs superior to MTX monotherapy
- **Hydroxychloroquine (HCQ):** Mild-moderate RA; antimalarial → inhibits TLR9 and lysosomal acidification → reduces cytokine production; retinal toxicity (annual ophthalmology screening after 5 years)
- **Sulfasalazine:** Combined with MTX+HCQ in "triple therapy"; effective for seronegative RA
- **Leflunomide:** Inhibits DHODH → reduces de novo pyrimidine synthesis → anti-proliferative; alternative to MTX (comparable efficacy)

**Biologic DMARDs (bDMARDs) — for MTX-inadequate responders:**

*Anti-TNF (first-line biologic):*
- Etanercept (TNF receptor-Fc fusion), adalimumab, infliximab (anti-TNF-alpha mAbs), certolizumab (PEGylated anti-TNF Fab, safe in pregnancy), golimumab
- ~30-40% ACR50 at 6 months added to MTX; reduce radiographic progression
- Screen for TB (reactivation risk); do not use with active serious infection; contraindicated in advanced heart failure (Class III-IV)

*Anti-IL-6 receptor:*
- **Tocilizumab (anti-IL-6R, Actemra):** IV or SC; monotherapy effective (unlike TNF inhibitors) for MTX-intolerant patients; MONARCH trial: superior to adalimumab in monotherapy on DAS28 remission; reduces acute-phase reactants → normalizes CRP/ESR (caution: CRP may not reflect infection when on tocilizumab)
- **Sarilumab (anti-IL-6R):** SC injection; SARIL-RA MONARCH: superior to adalimumab monotherapy

*Anti-CD20 (B-cell depletion):*
- **Rituximab:** IV infusion (2× 1000 mg, 2 weeks apart); reserve for RF+/ACPA+ patients (B-cell-driven); effective in TNF-refractory RA; risk of hypogammaglobulinemia with repeated courses; hepatitis B reactivation screening required

*T-cell co-stimulation blockade:*
- **Abatacept (CTLA-4-Ig):** Binds B7 (CD80/86) on APCs → blocks CD28 co-stimulation → prevents T-cell activation; particularly effective in ACPA+ patients (seropositive RA); safer infection profile than anti-TNF; IV or SC

**Targeted synthetic DMARDs (tsDMARDs) — JAK inhibitors:**

*JAK1/2 inhibitors:*
- **Baricitinib (Olumiant):** JAK1/2 inhibitor → blocks IL-6, IFN-gamma, EPO, and growth factor signaling; RA-BEACON: 55% ACR20 vs 27% placebo in TNF-inadequate responders [^genovese-2016-baricitinib]; COVID-19 hospitalized patients benefit (non-RA indication via ACTT-2)
- **Upadacitinib (Rinvoq):** Selective JAK1 inhibitor; SELECT-COMPARE: superior to adalimumab on ACR50 at 12 weeks; also approved for psoriatic arthritis, AS, atopic dermatitis

*JAK1 inhibitors:*
- **Tofacitinib (Xeljanz):** First JAK inhibitor in RA; JAK1/3; FDA approved 2012; boxed warning for thrombosis risk (more prominent in ORAL Surveillance post-marketing study)

**Safety considerations for JAK inhibitors:** Boxed warnings for serious infection, malignancy, thromboembolism, cardiovascular events (MACE); preferred in patients failing TNF inhibitors; not preferred as first-line biologic in high-CV-risk patients per 2022 FDA/EMA guidance

**Glucocorticoids:**
- Prednisone (oral) or methylprednisolone (IV pulse) for bridging during DMARD initiation or flare management
- Intra-articular triamcinolone for monoarthritis flares
- Minimize long-term use: osteoporosis (bisphosphonate prophylaxis if >3 months at ≥7.5 mg/day), adrenal suppression, infection risk

## Connections

- `connects-to` → **[TNF-alpha](../../03-molecular/tnf-alpha/README.md)** — TNF-alpha is the master cytokine in RA synovitis; produced by synovial macrophages and FLS → drives NF-kB, MMP secretion, and RANKL-mediated bone erosion; anti-TNF biologics (adalimumab, etanercept, certolizumab) are the backbone of biologic DMARD therapy.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — IL-6 drives systemic RA inflammation (acute-phase response, anemia of chronic disease, fatigue) and Th17/Tfh polarization promoting ACPA production; tocilizumab and sarilumab (anti-IL-6R) are effective monotherapy or MTX-combination biologics for RA.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Th17 cells produce IL-17A/F driving neutrophil recruitment and FLS activation; Tfh cells sustain ACPA-producing plasma cell differentiation; abatacept (CTLA-4-Ig) blocks CD28 co-stimulation, suppressing pathogenic T-cell activation in RA synovium.
- `connects-to` → **[NF-kB](../../03-molecular/nf-kb/README.md)** — NF-kB activated in RA synovial fibroblasts and macrophages by TNF-alpha and IL-1beta → MMP secretion, RANKL induction, and osteoclast-driven bone erosion; glucocorticoids and multiple bDMARDs converge on NF-kB suppression as a shared downstream mechanism.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A is present in RA synovium but secondary to TNF-alpha and IL-6; IL-17A promotes osteoclastogenesis via RANKL induction; IL-17A inhibitors (secukinumab) failed pivotal RA trials; bimekizumab (anti-IL-17A/F) showed marginal RA benefit vs established TNF/IL-6 blockade.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5⁺ macrophages and Th1 cells are the dominant leukocyte populations in RA pannus; CCL3/CCL4/CCL5 (CCR5 ligands) are elevated in RA synovial fluid and correlate with disease activity; maraviroc (CCR5 antagonist) showed modest benefit in small RA trials, suggesting CCR5-mediated leukocyte recruitment contributes to synovitis.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — CCL2 is the dominant synovial chemokine in RA: synoviocytes and FLS secrete CCL2 → CCR2+ monocyte/macrophage recruitment → pannus formation; synovial fluid CCL2 >5 ng/mL correlates with radiographic damage; macrophage-derived RANKL and MMPs drive joint destruction.
- `treated-by` → **[Ibuprofen](../../../03-medicine/01-modern/12-anti-inflammatory/ibuprofen/README.md)** — NSAIDs including ibuprofen reduce COX-2-driven synovial PGE₂ → less joint pain, swelling, and stiffness; adjuncts to DMARDs; reduce RA symptoms but not radiographic progression; long-term use requires GI prophylaxis (PPI).
- `treated-by` → **[Corticosteroids](../../../03-medicine/01-modern/02-respiratory/corticosteroids/README.md)** — Prednisolone bridge therapy (5–10 mg/day) while DMARDs take effect (8–12 weeks latency); reduces radiographic progression in early RA (COBRA, BeSt trials); long-term use requires osteoporosis prophylaxis (bisphosphonate + calcium/vitamin D).
- `treated-by` → **[Adalimumab](../../../03-medicine/01-modern/11-biologics/adalimumab/README.md)** — fully human anti-TNFα IgG1 biologic; first-line for MTX-inadequate RA; ARMADA trial: ACR50 59% vs 24% at 24 weeks; halts radiographic progression; TB screening mandatory before initiation; concomitant MTX reduces immunogenicity.
- `connects-to` → **[Psoriatic Arthritis](../psoriatic-arthritis/README.md)** — Rheumatoid and psoriatic arthritis are the two major inflammatory arthritides but contrast: RA is a symmetric, RF/anti-CCP-positive synovitis sparing the DIP joints, while PsA is a seronegative spondyloarthropathy with enthesitis, dactylitis, DIP disease, and psoriasis.
- `connects-to` → **[Sjögren's Syndrome](../sjogrens-syndrome/README.md)** — Rheumatoid arthritis is the commonest disease complicated by secondary Sjögren's syndrome: chronic autoimmune inflammation extends to lacrimal and salivary glands, causing dry eyes and mouth (sicca), so RA patients are screened for the overlap.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Synovial fibroblasts are active drivers, not bystanders, of rheumatoid arthritis: activated fibroblast-like synoviocytes form the invasive pannus and secrete proteases and cytokines that erode cartilage and bone, behaving almost tumor-like—a therapeutic target.
- `connects-to` → **[Systemic Lupus Erythematosus](../systemic-lupus-erythematosus/README.md)** — Rheumatoid arthritis and lupus are archetypal systemic autoimmune diseases: RA's anti-CCP/RF antibodies drive symmetric synovitis, while lupus's antinuclear antibodies form immune complexes injuring skin, kidney and other organs—overlapping yet distinct.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Rheumatoid arthritis accelerates osteoporosis through several routes: chronic inflammatory cytokines (TNF, IL-6) activate osteoclasts, immobility reduces loading, and glucocorticoid treatment thins bone—so RA patients fracture more and need bone protection.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — B cells are central to rheumatoid arthritis despite its joint focus: they make rheumatoid factor and anti-CCP autoantibodies, which is why the B-cell-depleting antibody rituximab controls RA—linking the autoantibody-making cell to the disease and its therapy.
- `connects-to` → **[Osteoclast](../../04-cellular/osteoclast/README.md)** — Osteoclasts carve the bone erosions of rheumatoid arthritis: RANKL and TNF from inflamed synovium overactivate osteoclasts at the joint margin, eroding bone and cartilage—so the joint destruction on X-ray is osteoclast-mediated, a target of anti-TNF therapy.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Rheumatoid arthritis attacks the lung as well as joints: it causes interstitial lung disease, pleuritis and nodules, and RA-ILD is a major cause of death—so chronic cough or dyspnea in RA warrants pulmonary imaging, a key extra-articular manifestation.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — Rheumatoid arthritis is a cardiovascular disease too: chronic systemic inflammation accelerates atherosclerosis, so RA patients die more of heart attacks and strokes than of joint disease—and controlling inflammation lowers that excess cardiovascular risk.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK inhibitors are a major oral therapy for rheumatoid arthritis: the cytokines that inflame the joint (IL-6, interferons, GM-CSF) signal through JAK, so tofacitinib and baricitinib match biologic efficacy in pill form when methotrexate fails.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages are central effectors in the rheumatoid joint: synovial macrophages pour out TNF and IL-1 that drive inflammation and erode cartilage and bone, and their numbers track disease activity—so TNF blockade quiets this macrophage-driven cascade.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Rheumatoid arthritis is the archetypal autoimmune disease of the musculoskeletal system: immune attack on the synovium forms an invasive pannus that destroys cartilage and bone, deforming joints—so autoimmunity strikes the skeleton's moving parts.
- `connects-to` → **[MHC Class II](../../03-molecular/mhc-class-ii/README.md)** — Rheumatoid arthritis's strongest genetic risk is the HLA 'shared epitope': MHC class II HLA-DRB1 variants present citrullinated self-peptides to T cells, explaining why anti-CCP antibodies form and why these alleles predispose to seropositive RA.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — The microbiome may help ignite rheumatoid arthritis: gum and gut bacteria such as Porphyromonas gingivalis citrullinate proteins, and dysbiosis is linked to disease onset—part of why periodontitis and RA travel together.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Rheumatoid arthritis reflects failed regulatory T-cell control: Tregs that should restrain autoreactive responses are reduced or dysfunctional, tipping the balance toward the Th17/inflammatory attack on the joints—a target for tolerance-restoring therapies.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — RA erodes bone through RANKL: inflamed synovial cells and T cells release RANKL that activates osteoclasts to chew through joint bone, producing the erosions on X-ray—so RANKL blockade (denosumab) can protect the joints.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — RA's immune attack targets joint collagen: type II collagen in cartilage is both an autoantigen and the tissue destroyed as the pannus invades, so the breakdown of collagen is what ultimately deforms the rheumatoid joint.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — RA may start when dendritic cells present citrullinated peptides: these antigen-presenters display modified self-proteins on HLA-DR to T cells, breaking tolerance and launching the anti-CCP autoimmunity that defines the disease.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Rheumatoid arthritis commonly causes anemia: chronic inflammation raises hepcidin that locks away iron, so the anemia of chronic disease tracks with disease activity and improves when the inflammation is controlled.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Rheumatoid arthritis's biggest killer is the heart: chronic systemic inflammation accelerates atherosclerosis, so cardiovascular disease—not joint damage—is the leading cause of death, and controlling RA lowers that risk.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Neutrophils flood the rheumatoid joint and arm the autoimmunity: they pack the synovial fluid and release enzymes and NETs that citrullinate proteins, feeding the anti-CCP response and the cartilage destruction of the disease.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Rheumatoid arthritis inflames the eyes: it causes scleritis, episcleritis, and dry-eye keratoconjunctivitis, so red or gritty painful eyes in RA signal the autoimmunity reaching beyond the joints.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Rheumatoid arthritis scars the lungs: chronic inflammation drives interstitial lung fibrosis and forms fibrous rheumatoid nodules, a serious extra-articular complication that shortens life.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Rheumatoid arthritis drains calcium from bone: inflammation and steroids tip remodeling toward loss, eroding bone at joints and thinning the whole skeleton into osteoporosis.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photons chart rheumatoid joint destruction: X-rays catch the juxta-articular erosions and narrowed joint spaces that grade damage, while MRI and ultrasound reveal the active synovitis and early erosions before plain films can, guiding treatment.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — An enlarged spleen names a rare rheumatoid variant: Felty syndrome is the triad of longstanding RA, splenomegaly, and neutropenia, where the swollen spleen consumes white cells and leaves the patient prone to serious infection.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Rheumatoid immune complexes burn through complement: rheumatoid factor and anti-CCP antibodies bind into clusters that fix and consume complement, so low C3 in joint fluid and blood marks the active, sometimes vasculitic, disease.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Treating RA keeps watch on the liver: methotrexate and leflunomide, mainstays of disease-modifying therapy, can raise transaminases and rarely scar the liver, so enzymes are checked regularly and alcohol limited.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — Plasma cells are RA's antibody foundries: differentiated from the autoreactive B cells, they secrete the rheumatoid factor and anti-CCP antibodies that drive the disease — the upstream B-lineage that rituximab depletes to quiet it.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Chronic inflammation starves the red cells: RA's high IL-6 drives hepcidin, locking iron away from the marrow to cause the anemia of chronic disease — the commonest extra-articular finding, tracking with how active the arthritis is.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Two antibodies define and forecast RA: rheumatoid factor and anti-CCP (ACPA) mark seropositive disease, predict a more erosive course, and can appear in the blood years before the first joint ever swells.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — RA pinches and inflames the nerves: synovial swelling at the wrist compresses the median nerve into carpal tunnel syndrome, while rheumatoid vasculitis can starve nerves into a mononeuritis multiplex of sudden focal weakness.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — The kidney is hit from several sides: decades of inflammation can deposit AA amyloid, the NSAIDs and disease-modifying drugs carry their own nephrotoxicity, and rarely a rheumatoid vasculitis inflames the glomeruli.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Inflammation hardens the arteries: chronic RA accelerates atherosclerosis, so heart attack and stroke — not the joints — are the leading cause of death, and controlling disease activity is itself cardiovascular prevention.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells crowd the inflamed joint: abundant in rheumatoid synovium, they release TNF, histamine and proteases that amplify inflammation and angiogenesis, an innate-immune contributor to the pannus that erodes cartilage and bone.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1 beta helps drive the joint destruction: secreted by synovial macrophages, it spurs cartilage breakdown and osteoclast bone erosion, the rationale for the IL-1 blocker anakinra in disease resistant to other biologics.
- `connects-to` → **[CTLA-4](../../03-molecular/ctla-4/README.md)** — A brake on T-cell activation became a drug: abatacept is a CTLA-4-Ig fusion that blocks the co-stimulation T cells need, cooling the autoimmune attack on the joints — a treatment built directly from how this checkpoint normally restrains immunity.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — The inflamed joint grows new vessels: endothelial cells proliferate to vascularize the invading pannus, feeding the synovial overgrowth with oxygen and ferrying in the immune cells that sustain the destruction.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Chronic inflammation starves the marrow of iron: RA's high IL-6 drives hepcidin that locks iron away from red-cell production, producing the anemia of chronic disease that commonly shadows active rheumatoid arthritis.
- `connects-to` → **[Epstein-Barr Virus](../../../02-pathogen/01-viruses/epstein-barr-virus/README.md)** — EBV is woven into RA's biology: the virus is implicated in triggering the autoimmunity, and reactivation underlies many of the methotrexate-associated lymphoproliferations that can complicate long-term RA treatment.
- `connects-to` → **[Diffuse Large B-Cell Lymphoma](../dlbcl/README.md)** — Chronic immune activation raises lymphoma risk: RA — especially highly active disease and immunosuppressive therapy — increases the risk of diffuse large B-cell lymphoma, sometimes EBV-driven and regressing when methotrexate is stopped.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — The inflammasome amplifies the synovitis: NLRP3 in synovial macrophages releases IL-1β that drives cartilage breakdown and osteoclast bone erosion, an innate-immune engine alongside the autoantibody response.
- `connects-to` → **[Tuberculosis](../tuberculosis/README.md)** — Its biologics can wake latent TB: TNF-α inhibitors disable the granuloma that walls off Mycobacterium tuberculosis, so RA patients are screened and treated for latent infection before starting therapy to prevent reactivation.
- `connects-to` → **[Pneumocystis jirovecii](../../../02-pathogen/03-fungi/pneumocystis-jirovecii/README.md)** — Combination immunosuppression opens the lung to it: methotrexate plus steroids or biologics in RA can drop T-cell defenses enough for Pneumocystis pneumonia, sometimes warranting prophylaxis in high-intensity regimens.
- `connects-to` → **[Hepatitis B Virus](../../../02-pathogen/01-viruses/hepatitis-b-virus/README.md)** — Immunosuppression can reactivate it: rituximab and TNF inhibitors used in RA can reawaken occult hepatitis B, so serologic screening and antiviral prophylaxis precede these therapies to avert a flare.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Combined immunosuppression opens the lung to mold: corticosteroids stacked on biologics or JAK inhibitors for RA deeply blunt immunity, occasionally letting inhaled Aspergillus invade as pulmonary aspergillosis.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Chronic pain and disability press on mood: the relentless joint pain, fatigue and functional loss of RA, amplified by its inflammatory cytokines acting on the brain, give it markedly elevated rates of depression.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Inflammation and its JAK inhibitors raise the clot risk: active RA is a hypercoagulable, prothrombotic state, and the JAK inhibitors used to treat it carry a recognized signal for venous thromboembolism.
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — Its JAK inhibitors notably reawaken shingles: tofacitinib and other JAK inhibitors used for RA, along with biologics and steroids, markedly raise the risk of herpes-zoster reactivation.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Chronic inflammation and its drugs scar the kidney: long-standing RA can deposit AA amyloid in the kidneys, and years of NSAID use add analgesic nephropathy, together driving chronic kidney disease.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — An unpredictable, painful disease breeds worry: the flares, disability and lifelong immunosuppressive treatment of RA foster chronic health anxiety alongside its well-documented depression.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It scars and nodules the lungs: rheumatoid arthritis causes interstitial lung disease, pulmonary nodules, pleuritis and bronchiectasis, and methotrexate adds a risk of hypersensitivity pneumonitis.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It can compress and inflame nerves: cervical atlantoaxial subluxation in RA threatens the spinal cord, and entrapment neuropathies and vasculitic mononeuritis multiplex injure peripheral nerves.
- `connects-to` → **[Immune System](../immune-system/README.md)** — It is an archetypal autoimmune disease: rheumatoid arthritis is driven by anti-citrullinated-protein and rheumatoid-factor autoantibodies and T-cell-driven synovial inflammation, the target of its immune therapies.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It shows on the skin: rheumatoid nodules form over pressure points, and rheumatoid vasculitis causes skin ulcers and nail-fold infarcts in severe seropositive disease.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It can swell the spleen and raise lymphoma risk: Felty's syndrome combines rheumatoid arthritis with splenomegaly and neutropenia, and chronic immune activation modestly increases lymphoma risk.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Inflammation and its drugs reach the kidney: sustained inflammation deposits secondary AA amyloid causing proteinuria, and NSAIDs and some disease-modifying drugs are nephrotoxic.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Its drugs burden the gut and liver: NSAIDs cause peptic ulcers, methotrexate is hepatotoxic, and Felty syndrome adds splenomegaly with neutropenia.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Pregnancy shifts its course: rheumatoid arthritis often eases in pregnancy and flares afterward, while methotrexate's teratogenicity demands contraception and planning.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Treatment and autoimmunity touch the glands: long-term corticosteroids suppress the adrenal axis and disturb glucose, and RA coexists with autoimmune thyroid disease.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Methotrexate anchors treatment: weekly low-dose methotrexate, a chemotherapy antimetabolite, is the first-line DMARD for rheumatoid arthritis, controlling synovitis and serving as the backbone for combination with biologics.
- `connects-to` → **[Ankylosing Spondylitis](../ankylosing-spondylitis/README.md)** — Seropositive versus seronegative: RA is a symmetric, anti-CCP/RF-positive small-joint synovitis, whereas ankylosing spondylitis is an HLA-B27 axial spondyloarthropathy with sacroiliitis and enthesitis — the two poles of inflammatory arthritis.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — It erodes bone at the joint: RANKL-driven osteoclasts in the rheumatoid pannus carve marginal bone erosions and periarticular osteopenia, while chronic inflammation and steroids add systemic bone loss.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — It builds lymphoid follicles in the joint: rheumatoid synovium forms ectopic germinal centres where autoreactive B cells produce anti-citrullinated-protein antibodies, which is why B-cell depletion with rituximab controls the disease.
- `connects-to` → **[Multiple Sclerosis](../multiple-sclerosis/README.md)** — A caution for its TNF blockers: the anti-TNF biologics central to rheumatoid arthritis can unmask or worsen demyelination, so multiple sclerosis contraindicates them—one cytokine blockade helping joints yet harming nerves.
- `connects-to` → **[Immune Thrombocytopenia](../immune-thrombocytopenia/README.md)** — Felty and beyond: rheumatoid arthritis can drive secondary immune cytopenias—Felty syndrome pairs RA with splenomegaly and neutropenia, and immune thrombocytopenia also complicates it as the same autoimmunity turns on blood cells.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — Accelerated atherosclerosis: RA's chronic systemic inflammation accelerates atherosclerosis of the arterial wall, making cardiovascular disease the leading cause of death and shortening lifespan beyond the joint disease itself.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — RA-associated interstitial lung disease: rheumatoid arthritis causes interstitial lung disease and fibrosis around the alveoli—a major extra-articular cause of death—alongside rheumatoid nodules and pleuritis.
- `connects-to` → **[IgA Nephropathy](../iga-nephropathy/README.md)** — When inflammation reaches the kidney: long-standing RA can drive secondary IgA nephropathy and AA amyloidosis, the acute-phase response depositing in the glomerulus—a systemic joint disease turning renal.
- `connects-to` → **[PTCL](../ptcl/README.md)** — Clonal T-cells in chronic autoimmunity: rheumatoid arthritis is classically associated with T-cell large granular lymphocytic leukaemia (Felty-like neutropenia) and a raised risk of T-cell lymphomas alongside the more familiar B-cell ones.
- `connects-to` → **[Gout](../gout/README.md)** — Two inflammatory arthritides: gout and rheumatoid arthritis can mimic and even coexist, both causing acute swollen joints and erosions, distinguished by urate crystals versus autoantibodies and pannus.
- `connects-to` → **[Psoriasis](../psoriasis/README.md)** — Paradoxical psoriasis: the anti-TNF biologics that treat rheumatoid arthritis can paradoxically trigger psoriasiform skin eruptions, an unexpected adverse effect of blocking a cytokine central to both diseases.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Pannus angiogenesis: VEGF-driven new vessel growth feeds the invasive synovial pannus of rheumatoid arthritis, sustaining the inflamed tissue that erodes joints.
- `connects-to` → **[BAFF](../../03-molecular/baff/README.md)** — Autoantibody support: BAFF sustains the autoreactive B cells that produce rheumatoid factor and anti-citrullinated-protein antibodies central to rheumatoid arthritis.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 inflammation: the IL-23/Th17 axis drives the IL-17-mediated synovial inflammation of rheumatoid arthritis, complementing TNF and IL-6 signalling.
- `connects-to` → **[IFN-γ](../../03-molecular/ifn-gamma/README.md)** — Th1 contribution: IFN-γ from Th1 cells participates in the mixed cytokine milieu of the rheumatoid synovium, activating macrophages that drive joint destruction.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Pannus hypoxia: the hyperplastic, poorly perfused rheumatoid synovium becomes hypoxic, stabilising HIF-1α to drive the VEGF angiogenesis that feeds the invasive pannus.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — Synovial proliferation: PDGF drives the proliferation of the synovial fibroblasts that form the destructive pannus invading cartilage and bone in rheumatoid arthritis.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — Rituximab depletes CD20+ B cells in rheumatoid arthritis, cutting autoantibody production and antigen presentation—clinical proof that B cells, not just T cells and cytokines, are central drivers of the disease.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — Calprotectin (S100A8/A9) released by activated synovial neutrophils and monocytes amplifies joint inflammation through TLR4 and serves as a sensitive serum marker of rheumatoid disease activity that tracks subclinical synovitis.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — Citrullinated fibronectin in the rheumatoid synovium is a target of anti-citrullinated-protein antibodies (ACPA), and fibronectin fragments stimulate the matrix-degrading enzymes that erode cartilage—linking autoimmunity to joint destruction.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — COX-2-derived prostaglandins generated in the inflamed rheumatoid synovium produce much of the pain, swelling and warmth, the target of the NSAIDs that relieve symptoms without altering the underlying disease course.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 released from damaged rheumatoid synoviocytes acts as an alarmin on mast cells and innate lymphoid cells, amplifying the cytokine cascade and helping translate joint injury into self-perpetuating synovial inflammation.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — TGF-β together with IL-6 drives naive T cells toward the pathogenic Th17 lineage central to RA, while also activating synovial fibroblasts that build the invasive pannus.
- `connects-to` → **[Fibrinogen](../../03-molecular/fibrinogen/README.md)** — Citrullinated fibrinogen is a principal target of the anti-citrullinated-protein antibodies (anti-CCP) of rheumatoid arthritis, and immune complexes formed with it deposit in the joint to drive synovial inflammation.
- `connects-to` → **[BTK](../../03-molecular/btk/README.md)** — Bruton's tyrosine kinase relays B-cell-receptor and Fc-receptor signals in the autoreactive B cells and myeloid effectors of rheumatoid arthritis, an axis (with the CD20 B cells and BAFF already mapped) targeted by BTK inhibitors under study.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — The immune complexes of rheumatoid arthritis activate complement in the synovium, and C5/C5a amplify the inflammatory cell recruitment and joint damage, extending the C3 arm already mapped.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6 signaling through JAK (both mapped) activates STAT3, the transcription factor driving synovial inflammation and Th17 differentiation, central to the JAK-inhibitor and anti-IL-6 mechanisms in RA.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — IL-1 receptor and TLR signaling converge on MyD88 to activate NF-κB (mapped), amplifying the innate-immune drive of rheumatoid synovitis.
- `connects-to` → **[Interleukin-10](../../03-molecular/il-10/README.md)** — A relative shortfall of anti-inflammatory IL-10 against the dominant TNF, IL-6 and IL-17 (all mapped) contributes to the failure of resolution in rheumatoid synovitis.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — TLR4 sensing of damage-associated and citrullinated self-molecules (with MyD88 already mapped) helps initiate and perpetuate the synovial inflammation of rheumatoid arthritis.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR-driven metabolic reprogramming of synovial fibroblasts and Th17 cells sustains the aggressive, invasive pannus of rheumatoid arthritis.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT signaling promotes the survival, proliferation and apoptosis-resistance of the rheumatoid synovial fibroblasts that drive joint destruction.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling drives the aggressive fibroblast-like synoviocyte proliferation that builds the invasive pannus of rheumatoid arthritis.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 is highly expressed by rheumatoid synovial fibroblasts, amplifying joint inflammation and serving as a biomarker of disease activity.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-γ-STAT1 signaling (IFN-γ mapped) drives the Th1 and macrophage activation contributing to rheumatoid synovitis.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — DNA within the neutrophil extracellular traps that source citrullinated autoantigens engages cGAS-STING, amplifying the autoimmune inflammation of rheumatoid arthritis.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling governs the regulatory-T-cell balance and the synovial fibrosis of rheumatoid arthritis.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated CD8 cytotoxicity contributes to the synovial tissue injury of rheumatoid arthritis.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors regulate the survival and activation of the T cells and synovial fibroblasts driving rheumatoid arthritis, their dysregulation contributing to synovial hyperplasia.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the NF-κB-driven inflammatory cytokine production of the rheumatoid synovium.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling in synovial fibroblasts and osteoclasts contributes to the invasive pannus and bone erosion of rheumatoid arthritis.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) supports the survival and activation of the fibroblast-like synoviocytes and immune cells of rheumatoid arthritis.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked immunometabolic signaling shapes the T-cell activation and synoviocyte metabolism of rheumatoid arthritis.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the citrullination, osteoclastogenesis, and synoviocyte survival relevant to rheumatoid arthritis.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of the synovial fibroblasts and immune cells of rheumatoid arthritis.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling, a target of immunosuppressive therapy, participates in the autoreactive T-cell activation of rheumatoid arthritis.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the leukocyte and fibroblast recruitment into the inflamed synovium of rheumatoid arthritis.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine signaling, the mechanism of methotrexate's anti-inflammatory action, participates in the immunomodulation of rheumatoid arthritis.
- `connects-to` → **[Type I Interferon](../../03-molecular/type-i-interferon/README.md)** — Type I interferon signaling participates in the interferon signature and immune dysregulation of rheumatoid arthritis.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin participates in the synovial inflammation and bone/cartilage destruction of rheumatoid arthritis.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — Rheumatoid factor: RF is an autoantibody directed against the Fc portion of IgG, one of the two classic RA serologies alongside anti-CCP, and the resulting immune complexes fix complement (C3/C5 already mapped) to drive synovial inflammation.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Cardiovascular mortality: chronic systemic inflammation in rheumatoid arthritis impairs endothelial nitric-oxide function, driving the accelerated atherosclerosis that is the leading cause of the excess cardiovascular death seen in RA.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — Pannus angiogenesis: the invasive rheumatoid pannus depends on new blood vessels driven by angiopoietin-Tie2 and VEGF (VEGF already mapped) to feed the hyperplastic, hypoxic synovium that erodes cartilage and bone.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Anaemia of chronic disease: the sustained IL-6-driven inflammation of rheumatoid arthritis (hepcidin pathway) suppresses erythropoiesis, and the resulting anaemia lowering haemoglobin is the commonest extra-articular manifestation.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Cardiovascular mortality: accelerated atherosclerosis from chronic inflammation (nitric oxide already mapped) raises the risk of myocardial infarction in rheumatoid arthritis, and troponin marks the cardiac injury of the events that drive its excess death.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Sex and hormonal modulation: rheumatoid arthritis is about three times more common in women, and estrogen influences the disease, which often improves in pregnancy and can flare postpartum and around the menopause.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Lipid paradox and cardiovascular risk: rheumatoid arthritis alters cholesterol handling, and despite the lipid paradox of low levels in active disease, the inflammation accelerates atherosclerosis (nitric oxide already mapped) and cardiovascular risk.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative synovitis: reactive oxygen species generated in the inflamed synovium, to which xanthine oxidase contributes, damage cartilage and amplify inflammation, and the associated hyperuricaemia links rheumatoid arthritis to coexisting gout.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Adipokine inflammation: adiponectin and other adipokines from articular and systemic fat modulate the synovial inflammation of rheumatoid arthritis, part of the metabolic-immune crosstalk shaping disease activity and its cardiovascular comorbidity.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Anaemia of inflammation: the IL-6 surge (already mapped) of rheumatoid arthritis raises hepcidin, sequestering iron to produce the anaemia of chronic disease (haemoglobin already mapped) common in active disease.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Pro-inflammatory adipokine: leptin, with adiponectin (already mapped), links the articular and systemic fat to the synovial inflammation of rheumatoid arthritis, part of the adipokine-immune crosstalk shaping disease activity.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Insulin resistance: the systemic inflammation (TNF and IL-6 already mapped) and the glucocorticoids used to treat rheumatoid arthritis cause insulin resistance, contributing to the metabolic and cardiovascular comorbidity of the disease.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Synovial adipokine: resistin, a pro-inflammatory adipokine (leptin and adiponectin already mapped), is elevated in the synovial fluid and serum of rheumatoid arthritis and correlates with the disease activity.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Th2 counter-regulation: IL-4 and the Th2/M2 arm (IL-10 already mapped) oppose the Th17 and Th1 (IL-17, IL-23 and IFN-γ already mapped) drive of the synovitis, the anti-inflammatory balance in rheumatoid arthritis.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 arm: IL-13, with IL-4 (already mapped), is part of the type-2 cytokine response whose balance against the pro-inflammatory signals shapes the joint inflammation of rheumatoid arthritis.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — MMP and inflammation: the disturbed zinc homeostasis (low serum zinc) of the active rheumatoid inflammation, and the zinc-dependent matrix metalloproteinases that degrade the joint cartilage (collagen already mapped).
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Antioxidant defence: selenium supports the antioxidant selenoprotein defence, and low selenium is associated with rheumatoid arthritis and its oxidative (xanthine oxidase already mapped) joint damage.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Synovial mast cells: the synovial mast cells release histamine that contributes to the vascular permeability and the inflammation of the rheumatoid synovitis.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm complementing the dominant Th17 (IL-17 already mapped) axis of rheumatoid arthritis.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 counter-arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 arm balancing the Th17/Th1 drive of rheumatoid arthritis.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Synovial NK cells: the NK cells (perforin already mapped) infiltrate the rheumatoid synovium and modulate the innate inflammation of rheumatoid arthritis.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Synovial CD8 cells: the cytotoxic (CD8) T cells (perforin already mapped) infiltrate the rheumatoid synovium and contribute to the local tissue damage of rheumatoid arthritis.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the type-2 immune dimension balancing the dominant Th17/Th1 drive of rheumatoid arthritis.
- `connects-to` → **[Vitamin D](../../../03-medicine/03-food/vitamin-d/README.md)** — Immunomodulatory vitamin: vitamin D modulates the T-cell (already mapped) autoimmunity, and its deficiency is associated with the higher disease activity of rheumatoid arthritis.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the neutrophil (already mapped) recruitment into the inflamed synovium of rheumatoid arthritis.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Stromal alarmin: TSLP, from the synovial fibroblasts (already mapped) and stroma, conditions the dendritic cells (already mapped) and contributes to the pro-inflammatory milieu of the rheumatoid synovium.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Synovial matricellular: periostin, secreted by the synovial fibroblasts (already mapped), is part of the matricellular remodelling of the pannus and the bone erosion (RANKL already mapped) of rheumatoid arthritis.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) whose dysregulation on the immune complexes drives the synovial complement activation of rheumatoid arthritis.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway activated by the ACPA and rheumatoid-factor (immunoglobulin already mapped) immune complexes in the rheumatoid synovium.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Chronic-disease iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the anaemia of chronic disease of rheumatoid arthritis.

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^smolen-2016-ra-lancet]: Smolen JS, Aletaha D, McInnes IB. Rheumatoid arthritis. *Lancet.* 2016;388(10055):2023-2038. [doi:10.1016/S0140-6736(16)30173-8](https://doi.org/10.1016/S0140-6736(16)30173-8) · [PubMed 27156434](https://pubmed.ncbi.nlm.nih.gov/27156434/)
[^firestein-2003-ra-pathogenesis]: Firestein GS. Evolving concepts of rheumatoid arthritis. *Nature.* 2003;423(6937):356-361. [doi:10.1038/nature01661](https://doi.org/10.1038/nature01661) · [PubMed 12748655](https://pubmed.ncbi.nlm.nih.gov/12748655/)
[^genovese-2016-baricitinib]: Genovese MC, Kremer J, Zamani O, et al. Baricitinib in Patients with Refractory Rheumatoid Arthritis. *N Engl J Med.* 2016;374(13):1243-1252. [doi:10.1056/NEJMoa1507247](https://doi.org/10.1056/NEJMoa1507247) · [PubMed 27028914](https://pubmed.ncbi.nlm.nih.gov/27028914/)
