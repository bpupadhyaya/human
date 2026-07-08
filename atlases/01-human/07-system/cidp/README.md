---
schema: human-scale-entry/v1
id: cidp
name: CIDP
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "CIDP (chronic inflammatory demyelinating polyneuropathy) is immune-mediated PNS demyelination lasting >8 weeks; anti-NF155/CNTN1 IgG4 define subtypes; IVIG and corticosteroids first-line; efgartigimod (FcRn inhibitor; FDA Jun 2024) and inebilizumab (anti-CD19) are new options."
aliases: ["CIDP", "chronic inflammatory demyelinating polyneuropathy", "chronic inflammatory demyelinating polyradiculoneuropathy", "anti-NF155 neuropathy"]
sources:
  - id: vanlaar-2010-efns-cidp
    type: peer-reviewed
    cite: "European Federation of Neurological Societies/Peripheral Nerve Society Guideline on management of chronic inflammatory demyelinating polyradiculoneuropathy. J Peripher Nerv Syst. 2010;15(1):1-9."
    doi: "10.1111/j.1529-8027.2010.00238.x"
    pmid: "20433600"
  - id: merkies-2008-ivig-ice
    type: peer-reviewed
    cite: "Hughes RA, Donofrio P, Bril V, et al. Intravenous immune globulin (10% caprylate-chromatography purified) for the treatment of chronic inflammatory demyelinating polyradiculoneuropathy (ICE study). Lancet Neurol. 2008;7(2):136-144."
    doi: "10.1016/S1474-4422(07)70329-0"
    pmid: "18178525"
  - id: vandenberheijde-2023-efgartigimod-cidp
    type: peer-reviewed
    cite: "van den Bergh PYK, van Doorn PA, Hadden RDM, et al. Efgartigimod alfa and hyaluronidase-qvfc in CIDP (ADHERE). N Engl J Med. 2023;390(3):219-232."
    doi: "10.1056/NEJMoa2310819"
    pmid: "38197812"
  - id: van-den-bergh-2023-cidp-guidelines
    type: peer-reviewed
    cite: "Van den Bergh PYK, van Doorn PA, Hadden RDM, et al. European Academy of Neurology/Peripheral Nerve Society guideline on diagnosis and treatment of chronic inflammatory demyelinating polyradiculoneuropathy: 2023 update. Eur J Neurol. 2023;30(10):2976-3020."
    doi: "10.1111/ene.15927"
    pmid: "37382198"
cross_links:
  - target: 01-human/03-molecular/fcrn
    relation: connects-to
    note: "FcRn recycles pathogenic anti-paranodal IgG4 (anti-NF155, anti-CNTN1) and total IgG in CIDP; efgartigimod alfa SC (ADHERE: 67% vs 36% INCAT responders; FDA Jun 2024) accelerates IgG catabolism → reduces pathogenic antibody titers and IVIG dose requirements."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: modulated-by
    note: "IVIG (2 g/kg loading; 1 g/kg q4w maintenance) is first-line CIDP therapy via FcγR blockade and anti-idiotypic antibodies (ICE trial: Lancet Neurol 2008); pathogenic IgG4 anti-NF155 and anti-CNTN1 disrupt paranodal axo-glial junctions; efgartigimod reduces total IgG."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "CIDP demyelinates peripheral nerves via macrophage-mediated paranodal stripping; NCS shows slowed conduction velocity, prolonged DML, F wave prolongation, and conduction blocks; anti-NF155 IgG4 disrupts paranodal axo-glial junctions → nodal instability and conduction failure."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "CD4+ T cells (IL-2-dependent) drive macrophage recruitment and paranodal demyelination in CIDP; Treg dysfunction may predispose; low-dose IL-2 for Treg expansion is under investigation as adjunct therapy in refractory CIDP and other autoimmune neuropathies."
  - target: 01-human/05-tissue/guillain-barre
    relation: connects-to
    note: "CIDP and GBS share peripheral nerve demyelination but differ in course: CIDP is chronic (>8 weeks); GBS is acute monophasic triggered by Campylobacter or EBV; both respond to IVIG and PLEX acutely; CIDP requires chronic immunosuppression; early CIDP may be misdiagnosed as GBS."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages are primary effectors of myelin destruction in CIDP via paranodal myelin stripping and FcR-mediated phagocytosis; IVIG blocks macrophage FcγR; macrophage TNF-α drives oxidative myelin damage; endoneurial macrophage infiltration is the histological hallmark of CIDP."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "TNF-α elevated in CIDP endoneurium and serum; macrophage TNF-α drives oxidative myelin damage and Schwann cell apoptosis; anti-TNF agents (etanercept, infliximab) are CONTRAINDICATED in CIDP — they paradoxically worsen or trigger demyelinating neuropathy (FDA black box warning)."
  - target: 01-human/07-system/als
    relation: connects-to
    note: "CIDP and ALS both weaken muscles but are opposite kinds of disease: CIDP is an immune attack on peripheral-nerve myelin — chronic, demyelinating, and treatable with IVIG or FcRn inhibitors — while ALS is irreversible degeneration of the motor neuron itself."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "B cells drive the IgG4 subtypes of CIDP: clones producing anti-NF155 or anti-CNTN1 paranodal antibodies cause an aggressive, IVIG-resistant disease, which is why depleting them with rituximab (anti-CD20) or inebilizumab (anti-CD19) works where antibody-clearing therapies do less."
  - target: 01-human/07-system/multiple-sclerosis
    relation: connects-to
    note: "CIDP is sometimes called the peripheral counterpart of multiple sclerosis: both are immune-mediated demyelinating diseases, but MS attacks central myelin made by oligodendrocytes while CIDP attacks peripheral myelin made by Schwann cells — different cells and different drugs."
  - target: 01-human/07-system/myasthenia-gravis
    relation: connects-to
    note: "CIDP and myasthenia gravis are both antibody/immune-mediated, treatable autoimmune neuromuscular disorders at different sites: CIDP attacks peripheral-nerve myelin (areflexia, sensory loss), MG the postsynaptic junction (fatigable weakness); both improve with IVIG."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "CIDP and diabetes overlap and complicate each other: CIDP is over-represented in diabetes, and distinguishing demyelinating CIDP (which responds to immunotherapy) from common diabetic peripheral neuropathy is a key challenge, since conduction studies and response differ."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "CIDP often causes neuropathic pain alongside its hallmark weakness: demyelination and secondary axonal damage of sensory fibers produce burning, tingling and sensory ataxia, so beyond immunotherapy (IVIG, steroids) patients frequently need gabapentinoids or SNRIs for the pain."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Plasma cells underlie much of CIDP's autoimmunity: long-lived plasma cells secrete IgG antibodies that, with complement and macrophages, strip myelin from peripheral nerves—so IVIG, plasma exchange, and B-cell-targeting therapies are mainstays."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Regulatory T-cell failure permits CIDP: when Tregs cannot restrain autoreactive T and B cells, the immune system attacks peripheral-nerve myelin, so CIDP is treated by rebalancing immunity (steroids, IVIG)—immune dysregulation drives chronic demyelination."
  - target: 01-human/07-system/nmo
    relation: connects-to
    note: "CIDP and neuromyelitis optica are both antibody-mediated demyelinating diseases at different sites: CIDP attacks peripheral-nerve myelin (areflexia, sensorimotor loss), while NMO attacks CNS astrocytes/myelin via anti-AQP4—both IgG-driven and treated with immunotherapy."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "T helper cells help drive the autoimmune attack in CIDP: activated T cells breach the blood-nerve barrier and, with macrophages and antibodies, strip myelin from peripheral nerves—so immunosuppression, IVIG and plasma exchange restore conduction."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Complement amplifies nerve damage in CIDP: antibodies against myelin or nodal proteins fix complement on peripheral nerves, recruiting macrophages to demyelinate—so complement and the antibodies behind it are why IVIG and plasma exchange, which remove them, work."
  - target: 01-human/07-system/type-1-diabetes
    relation: connects-to
    note: "CIDP must be distinguished from diabetic neuropathy: diabetes both mimics and predisposes to CIDP, so a diabetic with disproportionate, treatable demyelinating weakness may have CIDP rather than ordinary diabetic polyneuropathy—a crucial, treatable distinction."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "CIDP attacks the insulation of peripheral neurons: immune-mediated stripping of myelin from motor and sensory nerve fibers slows or blocks conduction, causing the progressive weakness and numbness that, unlike Guillain-Barré, persist or relapse over months."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "CIDP is an autoimmune disease of peripheral nerves: antibodies, complement and T cells attack myelin, so it responds to immunotherapy (IVIG, steroids, plasma exchange)—the treatable, chronic counterpart of Guillain-Barré syndrome."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "CIDP is a chronic disorder of the peripheral nervous system: demyelination of nerve roots and trunks impairs the signals between cord and limbs, producing symmetric weakness and sensory loss that can be reversed if immunotherapy starts before axons are lost."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement helps strip myelin in CIDP: antibodies against nerve antigens fix complement (C3 and beyond), and macrophages then peel myelin off axons, so complement activation is part of the demyelinating attack that IVIg and plasma exchange interrupt."
  - target: 01-human/07-system/waldenstrom-macroglobulinemia
    relation: connects-to
    note: "A CIDP-like neuropathy can signal a paraprotein: anti-MAG IgM from Waldenström macroglobulinemia or MGUS attacks myelin, producing a demyelinating neuropathy that mimics CIDP—so an unexplained case warrants checking for a monoclonal protein."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "CIDP is driven partly by T cells: cytotoxic and helper T cells breach the blood-nerve barrier and, with macrophages, attack peripheral myelin, so the disease reflects a cellular as well as antibody-mediated assault on nerves."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "CIDP responds to corticosteroids—unlike its acute cousin: steroids that mimic cortisol calm the autoimmune attack on peripheral myelin and are first-line in CIDP, a key contrast with Guillain-Barré, where steroids fail and only IVIG or plasma exchange help."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "CIDP begins with dendritic cells presenting myelin: these antigen-presenting cells display peripheral-nerve proteins to T cells, breaking tolerance and launching the chronic immune attack that strips myelin from the nerves."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "Refractory CIDP can be treated by deleting B cells via CD20: rituximab targets this B-cell marker to shut down antibody production, especially effective in CIDP variants driven by antibodies against nodal proteins or MAG."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "CIDP cripples nerve conduction at the sodium channels: myelin loss disperses the sodium channels clustered at the nodes of Ranvier, so the saltatory jump of the impulse fails, producing the conduction block behind the weakness."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Demyelination in CIDP exposes potassium channels: stripped of myelin, the juxtaparanodal potassium channels normally hidden under it leak current and dampen the nerve impulse, worsening conduction failure—a target of channel-blocking drugs."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Macrophages strip myelin in CIDP under NF-kB's command: this inflammatory switch drives the cytokines and activation that send macrophages to peel myelin off peripheral nerves, the core attack that immunosuppression aims to halt."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "CIDP can travel with kidney disease: it sometimes co-occurs with membranous nephropathy, the two sharing autoantibodies against nodal proteins like neurofascin and contactin, linking the leaky kidney filter to the demyelinated nerve."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "In POEMS syndrome, VEGF drives a CIDP-like neuropathy: this rare plasma-cell disorder floods the blood with VEGF, producing a demyelinating polyneuropathy that mimics CIDP but needs entirely different, anti-plasma-cell treatment."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Chronic CIDP damage is sealed by calcium: when long demyelination finally lets axons degenerate, calcium pours into the bare fibers and executes their death, the irreversible loss behind lasting disability."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Imaging supports the CIDP diagnosis: MRI photons reveal the thickened, enhancing nerve roots and plexuses, and nerve ultrasound shows the enlarged nerves of this demyelinating disease."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Some CIDP is driven from the marrow: a monoclonal plasma-cell clone (an IgM MGUS, often anti-MAG) makes antibodies that attack peripheral myelin, a paraproteinemic neuropathy needing marrow-directed treatment."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Inflammatory cytokines sustain CIDP: IL-6 and its kin help drive the autoimmune attack on myelin, keeping the demyelination smoldering and offering a target for newer immunomodulatory therapies."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows CIDP's repeated injury: round after round of demyelination and repair leaves Schwann cells wrapped in concentric 'onion-bulb' whorls around the axon, the hallmark of a chronic, relapsing nerve attack."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Severe CIDP can reach the breathing muscles: when the demyelination involves the nerves driving the diaphragm, respiratory weakness develops, the rare but dangerous extension that can require ventilatory support."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Some CIDP variants strike the cranial nerves: involvement of the nerves controlling eye movement causes double vision and drooping, broadening the disease beyond the limbs in its atypical forms."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies both treat and define CIDP: intravenous immunoglobulin is a first-line therapy, and a subset is driven by autoantibodies against the nerve's nodes (anti-NF155, anti-contactin-1) that mark a distinct, treatment-resistant form."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: connects-to
    note: "CIDP demyelinates the peripheral, not central, nerves: it strips the Schwann-cell myelin of peripheral nerves while sparing the oligodendrocyte myelin of the brain and cord — the opposite territory to multiple sclerosis."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "The disability is muscular: as demyelination slows nerve conduction, CIDP brings progressive limb weakness, areflexia, and eventual muscle wasting, the motor loss that physiotherapy and immunotherapy aim to reverse."
  - target: 01-human/07-system/hiv
    relation: connects-to
    note: "HIV can trigger CIDP: a demyelinating polyneuropathy indistinguishable from idiopathic CIDP appears in HIV infection, often around seroconversion, so a new diagnosis warrants HIV testing because the underlying infection changes management."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "CIDP breaches the blood-nerve barrier: the tight endothelial cells lining endoneurial vessels normally wall the nerve off from the immune system, and their breakdown is what lets autoantibodies and T cells reach and strip the myelin."
  - target: 01-human/06-organ/thymus
    relation: connects-to
    note: "CIDP traces back to broken tolerance: the thymus that should delete self-reactive T cells fails to fully restrain those targeting peripheral myelin, the lapse in central tolerance underlying this T-cell-dependent autoimmune neuropathy."
  - target: 01-human/03-molecular/baff
    relation: connects-to
    note: "BAFF keeps the autoimmune B cells alive: this survival cytokine sustains the antibody-producing B cells that attack peripheral myelin, part of why B-cell-directed rituximab can help refractory CIDP."
  - target: 01-human/07-system/multiple-myeloma
    relation: connects-to
    note: "A rogue antibody can strip the nerves: monoclonal gammopathy and multiple myeloma (notably POEMS) produce paraproteins that attack myelin, causing a demyelinating neuropathy that mimics or overlaps CIDP — so a paraprotein screen is part of the workup."
  - target: 01-human/07-system/sjogrens-syndrome
    relation: connects-to
    note: "Systemic autoimmunity can carry CIDP with it: Sjögren's and other connective-tissue diseases are associated with chronic inflammatory demyelinating neuropathy, a secondary form pointing to a shared loss of tolerance."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "A Th17 arm helps strip the myelin: IL-17A from autoreactive helper T cells promotes the inflammatory attack on peripheral nerve in CIDP, part of the cytokine milieu that breaks immune tolerance to myelin."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Faltering NK regulation lets autoimmunity run: natural killer cells normally help restrain autoreactive T cells, and their reduced number and function in CIDP is one of the immune-regulatory failures behind the chronic demyelination."
  - target: 01-human/07-system/hepatitis-c
    relation: connects-to
    note: "Chronic infection can drive the neuropathy: hepatitis C is associated with demyelinating and cryoglobulinemic neuropathies that overlap CIDP, so viral serology is part of the workup because it changes treatment."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "Th17 autoimmunity funnels through STAT3: IL-6- and IL-17-driven STAT3 signaling supports the autoreactive T-helper response that attacks peripheral myelin in CIDP, a node downstream of the cytokines elevated in the disease."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Immobility and IVIG raise the clot risk: limb weakness limits mobility while intravenous immunoglobulin — a mainstay treatment — is itself prothrombotic, together increasing the risk of deep-vein thrombosis and pulmonary embolism."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Long-term immunosuppression opens a gap: the corticosteroids and immunosuppressants used to control CIDP, plus immobility-related aspiration and pressure sores in severe disease, predispose to serious infection and sepsis."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Chronic steroids and immobility thin the bone: the prolonged corticosteroids used to control CIDP, combined with reduced mobility from limb weakness, accelerate bone loss and raise fracture risk."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Its IVIG can injure the kidney: high-dose intravenous immunoglobulin, a mainstay of CIDP treatment, can cause an osmotic acute kidney injury, and repeated courses risk lasting renal impairment."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Chronic disabling weakness weighs on mood: the relapsing numbness, weakness and dependence of CIDP, plus the side effects of long-term immunotherapy, carry a substantial burden of depression."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Numb, weak limbs break down: the sensory loss and weakness of CIDP lead to unnoticed injuries and immobility, and steroid therapy slows the healing of the resulting wounds and ulcers."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Its immunotherapy opens the lung to mold: the corticosteroids and immunosuppressants used to control CIDP blunt immunity, occasionally permitting invasive aspergillosis."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Its IVIG can thicken the blood: the intravenous immunoglobulin used to treat CIDP raises blood viscosity and carries a recognized risk of thromboembolic events including stroke."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "Its immunosuppression reawakens shingles: the corticosteroids, rituximab and other immunosuppressants used long-term for CIDP deplete antiviral immunity, allowing herpes-zoster reactivation."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Long steroid courses disturb the glands: the prolonged corticosteroids used to control CIDP cause hyperglycaemia and adrenal suppression, and steroid diabetes is a common treatment complication."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A chronic, relapsing, disabling neuropathy breeds worry: the fluctuating weakness, dependence on repeated infusions and uncertain course of CIDP foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Severe disease can weaken breathing: although milder than Guillain-Barré, severe or acute-onset CIDP can involve the respiratory muscles and occasionally require ventilatory support."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Its immunoglobulin therapy can injure the kidney: intravenous immunoglobulin, a mainstay CIDP treatment, can cause acute kidney injury, particularly with older sucrose-stabilised preparations."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its treatments strain the circulation: IVIG carries thromboembolic and volume-overload risks, and long-term corticosteroids used in CIDP add hypertension and fluid retention."
  - target: 03-medicine/01-modern/02-respiratory/corticosteroids
    relation: connects-to
    note: "A first-line immunotherapy: unlike Guillain-Barré, CIDP responds to corticosteroids, used with IVIG and plasma exchange to suppress the autoimmune attack on myelin."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It travels with paraproteins: CIDP-like neuropathies arise with MGUS and lymphoplasmacytic disorders, and its treatment leans on immunoglobulin pooled from the lymphoid system."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Pregnancy can flare it: CIDP often worsens during pregnancy and the puerperium, and the immunosuppressants used to control it complicate reproductive planning."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Chemo both mimics and treats it: drugs like vincristine and bortezomib cause a peripheral neuropathy that enters CIDP's differential, while cyclophosphamide is used for refractory CIDP."
  - target: 02-pathogen/01-viruses/hiv-1
    relation: connects-to
    note: "A virus that triggers the same attack: HIV can cause an inflammatory demyelinating polyneuropathy resembling CIDP, especially around seroconversion, one of its many neurological complications."
  - target: 01-human/07-system/anca-vasculitis
    relation: connects-to
    note: "A vasculitic mimic to exclude: ANCA-associated and other vasculitides damage peripheral nerves as mononeuritis multiplex, a key differential of CIDP that demands different treatment."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "New targeted immunotherapies arrive: the anti-FcRn agent efgartigimod, which strips pathogenic IgG, is now approved for CIDP, and rituximab against B cells treats refractory and antibody-mediated nodopathy subtypes."
  - target: 01-human/05-tissue/axonal-transport
    relation: connects-to
    note: "Chronic demyelination starves the axon: repeated de- and remyelination in CIDP eventually causes secondary axonal degeneration with impaired axonal transport, the substrate of the permanent disability that immunotherapy cannot reverse."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "Systemic autoimmunity can drive it: SLE and other connective-tissue diseases occasionally produce a CIDP-like demyelinating polyneuropathy, part of the autoimmune company CIDP keeps alongside Sjögren's and vasculitis."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Where the autoantibodies form: CIDP's myelin- and nodal-protein-targeting antibodies arise from germinal-centre B-cell responses, the rationale for B-cell-depleting and FcRn-blocking therapy."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "A drug-induced trigger: anti-TNF therapy given for rheumatoid arthritis can paradoxically provoke a CIDP-like demyelinating neuropathy, an iatrogenic route into the disease."
  - target: 01-human/07-system/inflammatory-bowel-disease
    relation: connects-to
    note: "Shared autoimmune ground: CIDP is over-represented in inflammatory bowel disease, both through shared immune dysregulation and through the demyelination that TNF inhibitors used for IBD can provoke."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Immunotherapy-triggered neuropathy: checkpoint-inhibitor cancer therapy can precipitate a CIDP-like immune demyelinating neuropathy, an emerging iatrogenic cause needing prompt recognition."
  - target: 01-human/07-system/melanoma
    relation: connects-to
    note: "A cancer context for immune neuropathy: checkpoint-inhibitor treatment of cancers like melanoma is a growing trigger of CIDP-like neuropathy, the same immune activation that fights the tumour attacking nerves."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Post-viral demyelination: COVID-19, like other infections, can precipitate or worsen CIDP and Guillain-Barré-spectrum neuropathies through molecular mimicry and immune activation."
  - target: 01-human/03-molecular/ctla-4
    relation: connects-to
    note: "Checkpoint and tolerance: CTLA-4 restrains autoreactive T cells, and anti-CTLA-4 checkpoint-inhibitor cancer therapy can unleash a CIDP-like immune neuropathy by breaking peripheral tolerance."
  - target: 01-human/03-molecular/btk
    relation: connects-to
    note: "B-cell signalling target: Bruton tyrosine kinase relays B-cell receptor signals that sustain the autoantibody response, and BTK inhibitors are being trialled to dampen CIDP."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Cytokine signal relay: JAK1/JAK2 transduce the inflammatory cytokines (IL-6 and others) that drive CIDP nerve damage, positioning JAK inhibition as an investigational approach."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 demyelination: IFN-γ from autoreactive T-helper cells activates macrophages that strip myelin from peripheral nerves, a central driver of the demyelination in CIDP."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Macrophage inflammation: IL-1β released by the activated macrophages that invade CIDP nerves amplifies the inflammatory demyelination of the disease."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Innate amplification: NLRP3-inflammasome activation in macrophages matures the IL-1β that intensifies the autoimmune attack on peripheral myelin in CIDP."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Macrophage recruitment: CCL2 draws the macrophages that strip myelin from peripheral nerves in CIDP, the chemokine axis behind the macrophage-mediated demyelination that is its histological hallmark."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Antigen presentation: MHC class II presentation of peripheral-nerve myelin antigens to CD4 T cells initiates the autoimmune response that drives the demyelination of CIDP."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Regulatory failure: impaired TGF-beta-dependent regulatory T-cell function permits the sustained autoreactivity against peripheral myelin that distinguishes chronic CIDP from self-limited Guillain-Barré."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Innate macrophage activation: TLR4 signalling primes the macrophages that, directed by autoantibody and complement, strip myelin from peripheral nerves in CIDP, the innate arm of the demyelinating attack."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Blood-nerve trafficking: CXCL12 helps direct autoreactive leukocytes across the blood-nerve barrier into peripheral nerve in CIDP, a step in establishing the endoneurial inflammation that demyelinates."
  - target: 01-human/03-molecular/ntrk
    relation: connects-to
    note: "Neurotrophic repair: NGF and BDNF signalling through Trk receptors supports the Schwann-cell remyelination and axonal repair that determine functional recovery between the relapses of CIDP."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: connects-to
    note: "First-line therapy: corticosteroids acting through the glucocorticoid receptor are a first-line treatment for CIDP, broadly suppressing the autoreactive immune attack on peripheral myelin, used alongside IVIG and plasma exchange."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Plasma-cell persistence: long-lived plasma cells making the anti-nodal and anti-myelin antibodies of CIDP survive on BCL-2 and escape CD20-targeted depletion, the basis for relapse after rituximab in the autoimmune-nodopathy subset."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Cell-mediated demyelination: macrophages and cytotoxic T cells strip myelin from peripheral nerves in CIDP, with perforin-based cytotoxicity contributing to the segmental demyelination that slows nerve conduction."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 drives differentiation of Th1 cells and their IFN-γ output (IFN-γ already mapped), polarising the autoreactive T-cell response that attacks peripheral myelin in CIDP."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 maintenance: IL-23 sustains pathogenic Th17 cells and their IL-17A production (IL-17A already mapped), a second effector arm of the autoimmune demyelination of CIDP."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Regulatory restraint: IL-10 from regulatory T cells normally dampens these responses, and its relative insufficiency permits the sustained autoimmune nerve injury of CIDP, with recovery often accompanying remission."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Innate macrophage activation: TLR-MyD88-NF-κB innate signalling (TLR4 and NF-κB already mapped) in endoneurial macrophages drives the inflammatory demyelination of peripheral nerve in CIDP."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "Complement effector: complement activation generates C5a that engages C5aR1 to recruit and activate macrophages (C3 and C5 already mapped), effecting the complement-mediated myelin injury of CIDP."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Oxidative axonal injury: NRF2-regulated antioxidant defence counters the oxidative stress of chronic nerve inflammation, modulating the secondary axonal injury that determines lasting disability in CIDP."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "BAFF-driven PI3K-AKT signalling (BAFF mapped) sustains the autoreactive B cells producing the pathogenic antibodies of CIDP."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "The mTOR-regulated metabolic program supports the antibody-secreting plasmablast and effector-T-cell responses in CIDP."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Macrophage galectin-3 participates in the macrophage-mediated demyelination of peripheral nerves in CIDP."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the Th1/interferon component of the autoimmune attack on peripheral-nerve myelin in CIDP."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA released by nerve and Schwann-cell injury can engage cGAS-STING, amplifying the innate inflammation of CIDP."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling shapes the Schwann-cell remyelination responses that determine recovery in CIDP."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO regulates the autoreactive lymphocyte tolerance and Schwann-cell oxidative-stress responses relevant to the demyelination of CIDP."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signaling transduces the macrophage and Schwann-cell responses driving the demyelination of CIDP."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins from infiltrating macrophages amplify the inflammatory nerve injury of CIDP."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the T-cell and macrophage inflammatory signaling that drives the demyelination of chronic inflammatory demyelinating polyneuropathy."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) supports the survival and activation of the autoreactive T and B cells of chronic inflammatory demyelinating polyneuropathy."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α in the inflamed peripheral nerve contributes to the metabolic and inflammatory milieu of chronic inflammatory demyelinating polyneuropathy."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked immunometabolic signaling shapes the autoreactive T-cell and macrophage metabolism of chronic inflammatory demyelinating polyneuropathy."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the autoreactive-immune-cell and Schwann-cell responses of chronic inflammatory demyelinating polyneuropathy."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment into the peripheral nerve contributes to the demyelinating inflammation of chronic inflammatory demyelinating polyneuropathy."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the autoreactive immune response of chronic inflammatory demyelinating polyneuropathy."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the immune-cell and Schwann-cell signaling of chronic inflammatory demyelinating polyneuropathy."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the neuroinflammatory and immune responses of chronic inflammatory demyelinating polyneuropathy."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the autoreactive immune responses of chronic inflammatory demyelinating polyneuropathy."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the T-cell activation of chronic inflammatory demyelinating polyneuropathy."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine signaling participates in the immunomodulation and neuroinflammatory processes of chronic inflammatory demyelinating polyneuropathy."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "Nerve support and repair: BDNF and neurotrophic signalling support axonal survival and remyelination, and their adequacy shapes recovery from the demyelinating injury of chronic inflammatory demyelinating polyneuropathy."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Th2 help: IL-4-driven type-2 help supports the B-cell and autoantibody responses (immunoglobulin G already mapped) against nodal and myelin antigens in chronic inflammatory demyelinating polyneuropathy."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Immune checkpoint: PD-1 normally restrains autoreactive T cells, and checkpoint-inhibitor cancer therapy can trigger a CIDP-like neuropathy, revealing the role of this checkpoint in protecting peripheral nerve from autoimmunity."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 humoral help: IL-13, with the IL-4 (already mapped) type-2 response, supports the B-cell autoantibody production against nodal and myelin antigens that drives the demyelination of chronic inflammatory demyelinating polyneuropathy."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Nerve inflammatory injury: nitric oxide from activated macrophages (already mapped) in the inflamed nerve contributes to the demyelination and secondary axonal injury of CIDP, part of the effector damage beyond antibody and complement."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Endoneurial fibrosis: chronic and relapsing inflammation in CIDP leads to onion-bulb formation and endoneurial collagen deposition, the fibrotic scarring of repeated demyelination and remyelination that underlies fixed disability."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Inflammatory eicosanoids: prostaglandins from the macrophages (already mapped) and infiltrating cells of the inflamed nerve amplify the demyelinating inflammation (IL-6, TNF and IL-1 already mapped) of CIDP."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative nerve injury: the inflamed nerve generates oxidative stress, to which xanthine oxidase contributes, and the resulting reactive oxygen species (nitric oxide already mapped) add to the demyelination and secondary axonal injury of CIDP."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Myelin lipid: myelin is a cholesterol-rich membrane, and the repeated demyelination and remyelination of CIDP demand the cholesterol handling of the Schwann cells rebuilding the myelin sheath."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Neurotrophic remyelination: IGF-1 supports the Schwann-cell remyelination and axonal maintenance (BDNF already mapped), part of the reparative response to the repeated demyelination of CIDP."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Schwann-cell proliferation: PDGF drives the Schwann-cell proliferation of the onion-bulb remyelination that characterises the chronic, relapsing demyelination and repair of CIDP."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Copper-deficiency mimic: copper deficiency causes a myeloneuropathy with demyelination that can clinically mimic CIDP, an important metabolic differential in the chronic neuropathies."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate immune signalling: type-I interferon is part of the innate-immune signalling of the autoimmune demyelination of the peripheral nerve (already mapped) in CIDP."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Autoantibody source: the long-lived plasma cells secrete the anti-myelin and anti-nodal IgG (immunoglobulin already mapped) autoantibodies of CIDP, resisting the B-cell (CD20 already mapped) depletion, the rationale for the anti-plasma-cell approaches."
  - target: 01-human/07-system/nmo
    relation: connects-to
    note: "Antibody-mediated demyelination sibling: neuromyelitis optica and CIDP are antibody- and complement (already mapped)-mediated demyelinating diseases (CNS vs PNS), both responding to the B-cell (CD20 already mapped) and complement therapies."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Immune-metabolic adipokine: leptin is the adipokine of the immune-metabolic milieu and the steroid (cortisol already mapped)-related metabolic disturbance of CIDP."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the immune-metabolic milieu of CIDP."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the systemic inflammation (IL-6 already mapped) of CIDP."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Inflammatory infiltrate: the neutrophils and the neutrophil-lymphocyte ratio are part of the inflammatory infiltrate (CCL2 already mapped) of the demyelinating nerve lesions of CIDP."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension balancing the dominant Th1/Th17 (IFN-γ, IL-12 and IL-23 already mapped) drive of CIDP."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 IgE: the IgE (with IL-4 and IL-13 already mapped) reflects the type-2 immune dimension present in a subset of CIDP."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells in nerve: the mast cells infiltrate the inflamed peripheral nerve and contribute to the type-2 (IgE already mapped) and the vascular-permeability dimension of the demyelination of CIDP."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Immunomodulatory vitamin: the low vitamin D status is associated with the autoimmune neuropathies, and its immunomodulation of the T-helper (already mapped) response is studied in CIDP."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Antioxidant micronutrient: selenium, a selenoprotein cofactor, is part of the oxidative-stress and micronutrient dimension of the peripheral-nerve inflammation of CIDP."
---

# CIDP

## Overview

Chronic inflammatory demyelinating polyneuropathy (CIDP) is the most common chronic immune-mediated neuropathy, affecting 2–9 per 100,000 adults, with a mean age of onset of 50–55 years [^vanlaar-2010-efns-cidp]. It is characterized by progressive or relapsing-remitting **symmetric proximal and distal limb weakness** and **sensory deficits**, evolving over more than 8 weeks, caused by immune-mediated attack on the peripheral nerve myelin and paranodal structures.

CIDP represents a spectrum of disorders, with the classical phenotype accounting for ~50% of cases and several electrophysiologically and immunologically distinct variants comprising the rest. The identification of **anti-paranodal IgG4 autoantibodies** (anti-NF155, anti-CNTN1, anti-CASPR1, anti-pan-neurofascin) has transformed understanding of CIDP as a molecularly heterogeneous disease — these subsets have distinct clinical features, respond differently to IVIG, and are amenable to targeted B cell depletion therapy.

The approval of **efgartigimod alfa SC** (ADHERE trial, FDA June 2024) marked the first new mechanism of action approved for CIDP in decades, establishing FcRn inhibition as an effective approach to CIDP alongside the long-established IVIG, corticosteroids, and plasma exchange [^vandenberheijde-2023-efgartigimod-cidp].

## Structure

### Clinical Phenotypes

| Phenotype | Approximate frequency | Key features |
|:---------|:---------------------|:-------------|
| Typical/Classical CIDP | ~50% | Symmetric proximal + distal; motor + sensory; responds to IVIG |
| Pure sensory CIDP | ~10% | Sensory ataxia; large-fiber; normal strength |
| Pure motor CIDP | ~10% | Motor predominant; distinguish from MMN |
| Multifocal CIDP (MADSAM) | ~5% | Multifocal asymmetric; Lewis-Sumner syndrome |
| Distal CIDP (DADS) | ~5% | Distal predominant; anti-MAG antibodies in some |
| Anti-NF155 CIDP | ~5–10% | Prominent tremor; sensory ataxia; young onset; poor IVIG response |
| Anti-CNTN1 CIDP | ~3–5% | Aggressive; nephropathy; poor IVIG response; responds to rituximab |

### Diagnostic Criteria (EAN/PNS 2023 Update)

**Clinical criteria** (mandatory):
- Symptom duration >8 weeks (distinguishes from GBS)
- Symmetric proximal + distal weakness in arms and legs (or equivalent for variants)
- Sensory signs (reduced vibration, position sense, pinprick)
- Absent or reduced deep tendon reflexes

**Electrodiagnostic criteria** (nerve conduction studies):
The diagnosis requires ≥1 of (in ≥2 nerves):
- **Prolonged DML** (distal motor latency)
- **Reduced motor conduction velocity**
- **Prolonged F-wave latency** or absent F-waves
- **Conduction block** (≥50% CMAP amplitude reduction across a nerve segment)
- **Temporal dispersion** (>30% CMAP duration increase)

**Supportive criteria**:
- CSF: elevated protein (>45 mg/dL) with normal white cell count (<5/mm³) — albuminocytological dissociation
- MRI: gadolinium enhancement or hypertrophy of nerve roots, plexus, proximal nerve trunks
- Anti-paranodal antibodies: anti-NF155 IgG4, anti-CNTN1 IgG4, anti-CASPR1 IgG4
- Response to IVIG or corticosteroids (therapeutic trial as diagnostic criterion)
- Nerve biopsy: onion bulb formations (repeated demyelination/remyelination), macrophage-mediated demyelination

## Function

CIDP impairs peripheral nerve function through:

1. **Demyelination** — slowed or blocked conduction velocity → weakness and sensory dysfunction; proximal nerve and root involvement explains the unusual combination of proximal + distal deficits (contrasting with length-dependent peripheral neuropathies)

2. **Paranodal disruption** — anti-NF155 and anti-CNTN1 IgG4 disrupt the axo-glial paranodal junction (NF155-CNTN1-CASPR1 complex) → nodal Na⁺ channel instability → conduction failure independent of myelin destruction; explains the poor IVIG response in these subtypes (IVIG primarily targets macrophage FcγR and complement; IgG4 does not fix complement)

3. **Secondary axonal degeneration** — in severe or long-standing CIDP, axonal loss occurs secondary to chronic demyelination → poor recovery even after immunotherapy; explains why early treatment prevents long-term disability

Disease activity is quantified with:
- **INCAT disability scale** (0–10; inflammatory neuropathy cause and treatment)
- **ONLS** (overall neuropathy limitations scale)
- **I-RODS** (Inflammatory-RODS; Rasch-based measure)
- **MRC sum score** (muscle strength)
- **R-ODS** (Rasch-built overall disability scale)

## Pathology

### Immunopathogenesis

CIDP involves both **humoral** and **cellular** immune mechanisms [^van-den-bergh-2023-cidp-guidelines]:

**Humoral arm:**
- Complement-activating IgG1/IgG3 antibodies target compact myelin and Schwann cell surface antigens → classical complement activation → MAC deposition → Schwann cell lysis
- Non-complement-activating IgG4 antibodies target paranodal junctions (NF155, CNTN1, CASPR1) → functional disruption without complement activation; these are resistant to IVIG and plasma exchange but respond to B cell depletion (rituximab)
- Total IgG recycled by FcRn → FcRn inhibitors (efgartigimod) reduce all IgG including pathogenic subtypes

**Cellular arm:**
- CD4+ Th17 cells and CD8+ T cells infiltrate endoneurium → macrophage activation → paranodal myelin stripping
- Aberrant macrophage activation → TNF-α, IL-1β, ROS → oxidative myelin damage
- Defective Treg suppression allows autoreactive T cells to escape peripheral tolerance

### Paranodal Biology — NF155 and Contactin System

The **node of Ranvier** paranodal junction is maintained by a tripartite adhesion complex:
- **Neurofascin-155** (NF155, encoded by *NFASC*): glial side (paranodal loops)
- **Contactin-1** (CNTN1): axonal side
- **Contactin-associated protein 1** (CASPR1): axonal; links CNTN1 to cytoskeleton

IgG4 anti-NF155 or anti-CNTN1 disrupts this complex → paranodal loop detachment → Na⁺/K⁺ channel redistribution → electrical instability. Unlike compact myelin antibodies, these do not activate complement (IgG4 does not fix C1q efficiently) — the reason these patients do not respond to IVIG and respond poorly to plasma exchange. **Rituximab** (anti-CD20) achieves better responses in anti-NF155+ and anti-CNTN1+ CIDP by depleting the B cell clone producing these antibodies.

### Distinction from GBS (Guillain-Barré Syndrome)

| Feature | GBS | CIDP |
|:--------|:----|:-----|
| Course | Acute; monophasic | Chronic (>8 weeks); relapsing or progressive |
| Nadir | <4 weeks | Evolves >8 weeks |
| CSF protein | Elevated | Elevated |
| Electrodiagnostic | Acute demyelination | Chronic demyelination (onion bulbs) |
| Preceding infection | Common (Campylobacter, EBV, CMV) | Less common |
| Treatment | IVIG or PLEX (acute) | IVIG, corticosteroids, FcRn inhibitors (chronic) |

## Treatment

### First-line

**IVIG (Intravenous immunoglobulin):**
- 2 g/kg loading over 2–5 days → sustained therapy 1 g/kg q4w or 2 g/kg q12w
- The **ICE trial** (N=117, randomized, double-blind) demonstrated improvement in INCAT score in 54% vs 21% placebo at 24 weeks [^merkies-2008-ivig-ice]; FDA-approved for CIDP
- Mechanism: FcγR saturation → reduces macrophage phagocytosis of myelin; anti-idiotypic antibodies; complement neutralization; possibly accelerates pathogenic IgG catabolism by saturation of FcRn
- Subcutaneous IVIG (SCIG): equivalent efficacy to IVIG with home administration; Hyqvia (IVIG + recombinant hyaluronidase) and Hizentra approved for CIDP maintenance

**Corticosteroids:**
- Pulsed dexamethasone 40 mg/d × 4 days q4w × 6 cycles: DexDROP trial showed non-inferiority to daily prednisolone in short term
- Oral prednisolone 60 mg/d tapering: long-term immunosuppression; cumulative toxicity (osteoporosis, diabetes, cataract)
- Intravenous methylprednisolone 500–1000 mg/d × 3–5 days: used for relapses

**Plasma Exchange (PLEX):**
- 2–3× weekly × 6 sessions then tapering → removes circulating antibodies
- Benefit is typically short-lived (2–4 weeks); maintenance PLEX 1–2× weekly in some patients
- Less practical than IVIG/corticosteroids; mainly for acute relapses or IVIG-intolerant patients

### Second-line

**Rituximab** (anti-CD20; 375 mg/m² × 4 doses or 1000 mg × 2):
- Preferred for **anti-NF155** and **anti-CNTN1 IgG4-positive** CIDP — depletes the B cell clone producing paranodal antibodies; achieve complete/near-complete responses in ~50-70% of anti-NF155+ patients
- Rituximab does not deplete long-lived plasma cells → antibody titers fall gradually over months

**Azathioprine, mycophenolate mofetil, cyclosporine:**
- Steroid-sparing agents for long-term maintenance; limited controlled trial evidence but widely used

**Cyclophosphamide:** Reserved for severely refractory cases; risk of secondary malignancy

### Newer Approved and Investigational Agents

**FcRn inhibitors:**
- **Efgartigimod alfa and hyaluronidase-qvfc SC** (Vyvgart Hytrulo; argenx): The **ADHERE trial** (N=322, Phase 3, randomized, double-blind) showed **67.0% vs 36.0%** INCAT responders at cycle 3 vs placebo (p<0.0001); FDA approved **June 2024** for CIDP [^vandenberheijde-2023-efgartigimod-cidp]. Weekly SC injection. Reduces all IgG (~50-70%) including anti-paranodal IgG4 → decreases both macrophage-mediated demyelination and paranodal disruption.
- **Rozanolixizumab** (UCB): Phase 3 in CIDP (MOBILITY trial) ongoing; already FDA-approved for MG.
- **Nipocalimab** (Janssen): Anti-FcRn; Phase 3 in CIDP (RALI trial) ongoing.
- **Batoclimab** (Immunovant): Phase 3 in CIDP ongoing.

**Anti-CD19 mAb:**
- **Inebilizumab** (Uplizna; Amgen): FDA-approved for NMO; Phase 3 CIDP-IgG trial ongoing; anti-CD19 depletes a broader B cell compartment than anti-CD20 (includes plasmablasts and some plasma cells)

## Connections

- `connects-to` → **[FcRn](../../03-molecular/fcrn/README.md)** — FcRn recycles anti-paranodal IgG4 (anti-NF155, anti-CNTN1) sustaining pathogenic titers in CIDP; efgartigimod alfa SC (ADHERE: 67% vs 36% INCAT response; FDA Jun 2024) accelerates IgG catabolism and reduces IVIG requirements.
- `modulated-by` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — IVIG (2 g/kg; ICE trial Lancet Neurol 2008) is first-line CIDP therapy; pathogenic IgG4 anti-NF155 and anti-CNTN1 disrupt paranodal junctions; efgartigimod reduces total IgG catabolism.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — CIDP demyelinates peripheral nerves via macrophage-mediated paranodal stripping and anti-paranodal IgG4; NCS shows slowed conduction velocity, conduction blocks, and F-wave prolongation; axonal loss occurs secondary to chronic demyelination.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — CD4+ T cells (IL-2-dependent) drive macrophage recruitment and paranodal demyelination in CIDP; Treg dysfunction may predispose; low-dose IL-2 Treg expansion under investigation as adjunct therapy.
- `connects-to` → **[Guillain-Barré](../../05-tissue/guillain-barre/README.md)** — CIDP and GBS share peripheral nerve demyelination but differ in course: CIDP is chronic (>8 weeks); GBS is acute monophasic triggered by Campylobacter or EBV; both respond to IVIG and PLEX acutely; CIDP requires chronic immunosuppression; early CIDP may be misdiagnosed as GBS.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages are primary effectors of myelin destruction in CIDP via paranodal myelin stripping and FcR-mediated phagocytosis; IVIG blocks macrophage FcγR; macrophage TNF-α drives oxidative myelin damage; endoneurial macrophage infiltration is the histological hallmark of CIDP.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — TNF-α elevated in CIDP endoneurium and serum; macrophage TNF-α drives oxidative myelin damage and Schwann cell apoptosis; anti-TNF agents (etanercept, infliximab) are CONTRAINDICATED in CIDP — they paradoxically worsen or trigger demyelinating neuropathy (FDA black box warning).
- `connects-to` → **[ALS](../als/README.md)** — CIDP and ALS both weaken muscles but are opposite kinds of disease: CIDP is an immune attack on peripheral-nerve myelin — chronic, demyelinating, and treatable with IVIG or FcRn inhibitors — while ALS is irreversible degeneration of the motor neuron itself.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — B cells drive the IgG4 subtypes of CIDP: clones producing anti-NF155 or anti-CNTN1 paranodal antibodies cause an aggressive, IVIG-resistant disease, which is why depleting them with rituximab (anti-CD20) or inebilizumab (anti-CD19) works where antibody-clearing therapies do less.
- `connects-to` → **[Multiple Sclerosis](../multiple-sclerosis/README.md)** — CIDP is sometimes called the peripheral counterpart of multiple sclerosis: both are immune-mediated demyelinating diseases, but MS attacks central myelin made by oligodendrocytes while CIDP attacks peripheral myelin made by Schwann cells — different cells and different drugs.
- `connects-to` → **[Myasthenia Gravis](../myasthenia-gravis/README.md)** — CIDP and myasthenia gravis are both antibody/immune-mediated, treatable autoimmune neuromuscular disorders at different sites: CIDP attacks peripheral-nerve myelin (areflexia, sensory loss), MG the postsynaptic junction (fatigable weakness); both improve with IVIG.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — CIDP and diabetes overlap and complicate each other: CIDP is over-represented in diabetes, and distinguishing demyelinating CIDP (which responds to immunotherapy) from common diabetic peripheral neuropathy is a key challenge, since conduction studies and response differ.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — CIDP often causes neuropathic pain alongside its hallmark weakness: demyelination and secondary axonal damage of sensory fibers produce burning, tingling and sensory ataxia, so beyond immunotherapy (IVIG, steroids) patients frequently need gabapentinoids or SNRIs for the pain.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — Plasma cells underlie much of CIDP's autoimmunity: long-lived plasma cells secrete IgG antibodies that, with complement and macrophages, strip myelin from peripheral nerves—so IVIG, plasma exchange, and B-cell-targeting therapies are mainstays.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Regulatory T-cell failure permits CIDP: when Tregs cannot restrain autoreactive T and B cells, the immune system attacks peripheral-nerve myelin, so CIDP is treated by rebalancing immunity (steroids, IVIG)—immune dysregulation drives chronic demyelination.
- `connects-to` → **[NMOSD](../nmo/README.md)** — CIDP and neuromyelitis optica are both antibody-mediated demyelinating diseases at different sites: CIDP attacks peripheral-nerve myelin (areflexia, sensorimotor loss), while NMO attacks CNS astrocytes/myelin via anti-AQP4—both IgG-driven and treated with immunotherapy.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — T helper cells help drive the autoimmune attack in CIDP: activated T cells breach the blood-nerve barrier and, with macrophages and antibodies, strip myelin from peripheral nerves—so immunosuppression, IVIG and plasma exchange restore conduction.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Complement amplifies nerve damage in CIDP: antibodies against myelin or nodal proteins fix complement on peripheral nerves, recruiting macrophages to demyelinate—so complement and the antibodies behind it are why IVIG and plasma exchange, which remove them, work.
- `connects-to` → **[Type 1 Diabetes](../type-1-diabetes/README.md)** — CIDP must be distinguished from diabetic neuropathy: diabetes both mimics and predisposes to CIDP, so a diabetic with disproportionate, treatable demyelinating weakness may have CIDP rather than ordinary diabetic polyneuropathy—a crucial, treatable distinction.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — CIDP attacks the insulation of peripheral neurons: immune-mediated stripping of myelin from motor and sensory nerve fibers slows or blocks conduction, causing the progressive weakness and numbness that, unlike Guillain-Barré, persist or relapse over months.
- `connects-to` → **[Immune System](../immune-system/README.md)** — CIDP is an autoimmune disease of peripheral nerves: antibodies, complement and T cells attack myelin, so it responds to immunotherapy (IVIG, steroids, plasma exchange)—the treatable, chronic counterpart of Guillain-Barré syndrome.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — CIDP is a chronic disorder of the peripheral nervous system: demyelination of nerve roots and trunks impairs the signals between cord and limbs, producing symmetric weakness and sensory loss that can be reversed if immunotherapy starts before axons are lost.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement helps strip myelin in CIDP: antibodies against nerve antigens fix complement (C3 and beyond), and macrophages then peel myelin off axons, so complement activation is part of the demyelinating attack that IVIg and plasma exchange interrupt.
- `connects-to` → **[Waldenström Macroglobulinemia](../waldenstrom-macroglobulinemia/README.md)** — A CIDP-like neuropathy can signal a paraprotein: anti-MAG IgM from Waldenström macroglobulinemia or MGUS attacks myelin, producing a demyelinating neuropathy that mimics CIDP—so an unexplained case warrants checking for a monoclonal protein.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — CIDP is driven partly by T cells: cytotoxic and helper T cells breach the blood-nerve barrier and, with macrophages, attack peripheral myelin, so the disease reflects a cellular as well as antibody-mediated assault on nerves.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — CIDP responds to corticosteroids—unlike its acute cousin: steroids that mimic cortisol calm the autoimmune attack on peripheral myelin and are first-line in CIDP, a key contrast with Guillain-Barré, where steroids fail and only IVIG or plasma exchange help.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — CIDP begins with dendritic cells presenting myelin: these antigen-presenting cells display peripheral-nerve proteins to T cells, breaking tolerance and launching the chronic immune attack that strips myelin from the nerves.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — Refractory CIDP can be treated by deleting B cells via CD20: rituximab targets this B-cell marker to shut down antibody production, especially effective in CIDP variants driven by antibodies against nodal proteins or MAG.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — CIDP cripples nerve conduction at the sodium channels: myelin loss disperses the sodium channels clustered at the nodes of Ranvier, so the saltatory jump of the impulse fails, producing the conduction block behind the weakness.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Demyelination in CIDP exposes potassium channels: stripped of myelin, the juxtaparanodal potassium channels normally hidden under it leak current and dampen the nerve impulse, worsening conduction failure—a target of channel-blocking drugs.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Macrophages strip myelin in CIDP under NF-kB's command: this inflammatory switch drives the cytokines and activation that send macrophages to peel myelin off peripheral nerves, the core attack that immunosuppression aims to halt.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — CIDP can travel with kidney disease: it sometimes co-occurs with membranous nephropathy, the two sharing autoantibodies against nodal proteins like neurofascin and contactin, linking the leaky kidney filter to the demyelinated nerve.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — In POEMS syndrome, VEGF drives a CIDP-like neuropathy: this rare plasma-cell disorder floods the blood with VEGF, producing a demyelinating polyneuropathy that mimics CIDP but needs entirely different, anti-plasma-cell treatment.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Chronic CIDP damage is sealed by calcium: when long demyelination finally lets axons degenerate, calcium pours into the bare fibers and executes their death, the irreversible loss behind lasting disability.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Imaging supports the CIDP diagnosis: MRI photons reveal the thickened, enhancing nerve roots and plexuses, and nerve ultrasound shows the enlarged nerves of this demyelinating disease.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Some CIDP is driven from the marrow: a monoclonal plasma-cell clone (an IgM MGUS, often anti-MAG) makes antibodies that attack peripheral myelin, a paraproteinemic neuropathy needing marrow-directed treatment.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — Inflammatory cytokines sustain CIDP: IL-6 and its kin help drive the autoimmune attack on myelin, keeping the demyelination smoldering and offering a target for newer immunomodulatory therapies.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows CIDP's repeated injury: round after round of demyelination and repair leaves Schwann cells wrapped in concentric 'onion-bulb' whorls around the axon, the hallmark of a chronic, relapsing nerve attack.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Severe CIDP can reach the breathing muscles: when the demyelination involves the nerves driving the diaphragm, respiratory weakness develops, the rare but dangerous extension that can require ventilatory support.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Some CIDP variants strike the cranial nerves: involvement of the nerves controlling eye movement causes double vision and drooping, broadening the disease beyond the limbs in its atypical forms.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies both treat and define CIDP: intravenous immunoglobulin is a first-line therapy, and a subset is driven by autoantibodies against the nerve's nodes (anti-NF155, anti-contactin-1) that mark a distinct, treatment-resistant form.
- `connects-to` → **[Oligodendrocyte](../../04-cellular/oligodendrocyte/README.md)** — CIDP demyelinates the peripheral, not central, nerves: it strips the Schwann-cell myelin of peripheral nerves while sparing the oligodendrocyte myelin of the brain and cord — the opposite territory to multiple sclerosis.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — The disability is muscular: as demyelination slows nerve conduction, CIDP brings progressive limb weakness, areflexia, and eventual muscle wasting, the motor loss that physiotherapy and immunotherapy aim to reverse.
- `connects-to` → **[HIV](../hiv/README.md)** — HIV can trigger CIDP: a demyelinating polyneuropathy indistinguishable from idiopathic CIDP appears in HIV infection, often around seroconversion, so a new diagnosis warrants HIV testing because the underlying infection changes management.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — CIDP breaches the blood-nerve barrier: the tight endothelial cells lining endoneurial vessels normally wall the nerve off from the immune system, and their breakdown is what lets autoantibodies and T cells reach and strip the myelin.
- `connects-to` → **[Thymus](../../06-organ/thymus/README.md)** — CIDP traces back to broken tolerance: the thymus that should delete self-reactive T cells fails to fully restrain those targeting peripheral myelin, the lapse in central tolerance underlying this T-cell-dependent autoimmune neuropathy.
- `connects-to` → **[BAFF](../../03-molecular/baff/README.md)** — BAFF keeps the autoimmune B cells alive: this survival cytokine sustains the antibody-producing B cells that attack peripheral myelin, part of why B-cell-directed rituximab can help refractory CIDP.
- `connects-to` → **[Multiple Myeloma](../multiple-myeloma/README.md)** — A rogue antibody can strip the nerves: monoclonal gammopathy and multiple myeloma (notably POEMS) produce paraproteins that attack myelin, causing a demyelinating neuropathy that mimics or overlaps CIDP — so a paraprotein screen is part of the workup.
- `connects-to` → **[Sjögren's Syndrome](../sjogrens-syndrome/README.md)** — Systemic autoimmunity can carry CIDP with it: Sjögren's and other connective-tissue diseases are associated with chronic inflammatory demyelinating neuropathy, a secondary form pointing to a shared loss of tolerance.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — A Th17 arm helps strip the myelin: IL-17A from autoreactive helper T cells promotes the inflammatory attack on peripheral nerve in CIDP, part of the cytokine milieu that breaks immune tolerance to myelin.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Faltering NK regulation lets autoimmunity run: natural killer cells normally help restrain autoreactive T cells, and their reduced number and function in CIDP is one of the immune-regulatory failures behind the chronic demyelination.
- `connects-to` → **[Hepatitis C](../hepatitis-c/README.md)** — Chronic infection can drive the neuropathy: hepatitis C is associated with demyelinating and cryoglobulinemic neuropathies that overlap CIDP, so viral serology is part of the workup because it changes treatment.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — Th17 autoimmunity funnels through STAT3: IL-6- and IL-17-driven STAT3 signaling supports the autoreactive T-helper response that attacks peripheral myelin in CIDP, a node downstream of the cytokines elevated in the disease.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Immobility and IVIG raise the clot risk: limb weakness limits mobility while intravenous immunoglobulin — a mainstay treatment — is itself prothrombotic, together increasing the risk of deep-vein thrombosis and pulmonary embolism.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Long-term immunosuppression opens a gap: the corticosteroids and immunosuppressants used to control CIDP, plus immobility-related aspiration and pressure sores in severe disease, predispose to serious infection and sepsis.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Chronic steroids and immobility thin the bone: the prolonged corticosteroids used to control CIDP, combined with reduced mobility from limb weakness, accelerate bone loss and raise fracture risk.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Its IVIG can injure the kidney: high-dose intravenous immunoglobulin, a mainstay of CIDP treatment, can cause an osmotic acute kidney injury, and repeated courses risk lasting renal impairment.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Chronic disabling weakness weighs on mood: the relapsing numbness, weakness and dependence of CIDP, plus the side effects of long-term immunotherapy, carry a substantial burden of depression.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Numb, weak limbs break down: the sensory loss and weakness of CIDP lead to unnoticed injuries and immobility, and steroid therapy slows the healing of the resulting wounds and ulcers.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Its immunotherapy opens the lung to mold: the corticosteroids and immunosuppressants used to control CIDP blunt immunity, occasionally permitting invasive aspergillosis.
- `connects-to` → **[Stroke](../stroke/README.md)** — Its IVIG can thicken the blood: the intravenous immunoglobulin used to treat CIDP raises blood viscosity and carries a recognized risk of thromboembolic events including stroke.
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — Its immunosuppression reawakens shingles: the corticosteroids, rituximab and other immunosuppressants used long-term for CIDP deplete antiviral immunity, allowing herpes-zoster reactivation.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Long steroid courses disturb the glands: the prolonged corticosteroids used to control CIDP cause hyperglycaemia and adrenal suppression, and steroid diabetes is a common treatment complication.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A chronic, relapsing, disabling neuropathy breeds worry: the fluctuating weakness, dependence on repeated infusions and uncertain course of CIDP foster chronic health anxiety alongside depression.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Severe disease can weaken breathing: although milder than Guillain-Barré, severe or acute-onset CIDP can involve the respiratory muscles and occasionally require ventilatory support.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Its immunoglobulin therapy can injure the kidney: intravenous immunoglobulin, a mainstay CIDP treatment, can cause acute kidney injury, particularly with older sucrose-stabilised preparations.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its treatments strain the circulation: IVIG carries thromboembolic and volume-overload risks, and long-term corticosteroids used in CIDP add hypertension and fluid retention.
- `connects-to` → **[Corticosteroids](../../../03-medicine/01-modern/02-respiratory/corticosteroids/README.md)** — A first-line immunotherapy: unlike Guillain-Barré, CIDP responds to corticosteroids, used with IVIG and plasma exchange to suppress the autoimmune attack on myelin.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It travels with paraproteins: CIDP-like neuropathies arise with MGUS and lymphoplasmacytic disorders, and its treatment leans on immunoglobulin pooled from the lymphoid system.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Pregnancy can flare it: CIDP often worsens during pregnancy and the puerperium, and the immunosuppressants used to control it complicate reproductive planning.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Chemo both mimics and treats it: drugs like vincristine and bortezomib cause a peripheral neuropathy that enters CIDP's differential, while cyclophosphamide is used for refractory CIDP.
- `connects-to` → **[HIV-1](../../../02-pathogen/01-viruses/hiv-1/README.md)** — A virus that triggers the same attack: HIV can cause an inflammatory demyelinating polyneuropathy resembling CIDP, especially around seroconversion, one of its many neurological complications.
- `connects-to` → **[ANCA Vasculitis](../anca-vasculitis/README.md)** — A vasculitic mimic to exclude: ANCA-associated and other vasculitides damage peripheral nerves as mononeuritis multiplex, a key differential of CIDP that demands different treatment.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — New targeted immunotherapies arrive: the anti-FcRn agent efgartigimod, which strips pathogenic IgG, is now approved for CIDP, and rituximab against B cells treats refractory and antibody-mediated nodopathy subtypes.
- `connects-to` → **[Axonal Transport](../../05-tissue/axonal-transport/README.md)** — Chronic demyelination starves the axon: repeated de- and remyelination in CIDP eventually causes secondary axonal degeneration with impaired axonal transport, the substrate of the permanent disability that immunotherapy cannot reverse.
- `connects-to` → **[Systemic Lupus Erythematosus](../systemic-lupus-erythematosus/README.md)** — Systemic autoimmunity can drive it: SLE and other connective-tissue diseases occasionally produce a CIDP-like demyelinating polyneuropathy, part of the autoimmune company CIDP keeps alongside Sjögren's and vasculitis.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Where the autoantibodies form: CIDP's myelin- and nodal-protein-targeting antibodies arise from germinal-centre B-cell responses, the rationale for B-cell-depleting and FcRn-blocking therapy.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — A drug-induced trigger: anti-TNF therapy given for rheumatoid arthritis can paradoxically provoke a CIDP-like demyelinating neuropathy, an iatrogenic route into the disease.
- `connects-to` → **[Inflammatory Bowel Disease](../inflammatory-bowel-disease/README.md)** — Shared autoimmune ground: CIDP is over-represented in inflammatory bowel disease, both through shared immune dysregulation and through the demyelination that TNF inhibitors used for IBD can provoke.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Immunotherapy-triggered neuropathy: checkpoint-inhibitor cancer therapy can precipitate a CIDP-like immune demyelinating neuropathy, an emerging iatrogenic cause needing prompt recognition.
- `connects-to` → **[Melanoma](../melanoma/README.md)** — A cancer context for immune neuropathy: checkpoint-inhibitor treatment of cancers like melanoma is a growing trigger of CIDP-like neuropathy, the same immune activation that fights the tumour attacking nerves.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Post-viral demyelination: COVID-19, like other infections, can precipitate or worsen CIDP and Guillain-Barré-spectrum neuropathies through molecular mimicry and immune activation.
- `connects-to` → **[CTLA-4](../../03-molecular/ctla-4/README.md)** — Checkpoint and tolerance: CTLA-4 restrains autoreactive T cells, and anti-CTLA-4 checkpoint-inhibitor cancer therapy can unleash a CIDP-like immune neuropathy by breaking peripheral tolerance.
- `connects-to` → **[BTK](../../03-molecular/btk/README.md)** — B-cell signalling target: Bruton tyrosine kinase relays B-cell receptor signals that sustain the autoantibody response, and BTK inhibitors are being trialled to dampen CIDP.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Cytokine signal relay: JAK1/JAK2 transduce the inflammatory cytokines (IL-6 and others) that drive CIDP nerve damage, positioning JAK inhibition as an investigational approach.
- `connects-to` → **[IFN-γ](../../03-molecular/ifn-gamma/README.md)** — Th1 demyelination: IFN-γ from autoreactive T-helper cells activates macrophages that strip myelin from peripheral nerves, a central driver of the demyelination in CIDP.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Macrophage inflammation: IL-1β released by the activated macrophages that invade CIDP nerves amplifies the inflammatory demyelination of the disease.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Innate amplification: NLRP3-inflammasome activation in macrophages matures the IL-1β that intensifies the autoimmune attack on peripheral myelin in CIDP.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Macrophage recruitment: CCL2 draws the macrophages that strip myelin from peripheral nerves in CIDP, the chemokine axis behind the macrophage-mediated demyelination that is its histological hallmark.
- `connects-to` → **[MHC Class II](../../03-molecular/mhc-class-ii/README.md)** — Antigen presentation: MHC class II presentation of peripheral-nerve myelin antigens to CD4 T cells initiates the autoimmune response that drives the demyelination of CIDP.
- `connects-to` → **[TGF-beta](../../03-molecular/tgf-beta/README.md)** — Regulatory failure: impaired TGF-beta-dependent regulatory T-cell function permits the sustained autoreactivity against peripheral myelin that distinguishes chronic CIDP from self-limited Guillain-Barré.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — TLR4 signaling primes the macrophages that, directed by autoantibody and complement deposition, strip myelin from peripheral nerves in CIDP—the innate arm of the demyelinating attack alongside the adaptive response.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12 helps direct autoreactive leukocytes across the blood-nerve barrier into peripheral nerve in CIDP, a trafficking step in establishing the endoneurial inflammation that drives demyelination.
- `connects-to` → **[NTRK / TrkB](../../03-molecular/ntrk/README.md)** — NGF and BDNF signaling through Trk receptors supports the Schwann-cell remyelination and axonal repair that determine the functional recovery achieved between relapses of CIDP, and whose failure leads to fixed disability.
- `connects-to` → **[Glucocorticoid receptor](../../03-molecular/glucocorticoid-receptor/README.md)** — Corticosteroids acting through the glucocorticoid receptor are a first-line treatment for CIDP, broadly suppressing the autoreactive immune attack on peripheral myelin, used alongside IVIG and plasma exchange.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — Long-lived plasma cells making the anti-nodal and anti-myelin antibodies of CIDP survive on BCL-2 and escape CD20-targeted depletion, the basis for relapse after rituximab in the autoimmune-nodopathy subset.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Macrophages and cytotoxic T cells strip myelin from peripheral nerves in CIDP, with perforin-based cytotoxicity contributing to the segmental demyelination that slows nerve conduction.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — IL-12 drives differentiation of Th1 cells and their IFN-γ output (IFN-γ already mapped), polarizing the autoreactive T-cell response that attacks peripheral myelin in CIDP.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — IL-23 sustains pathogenic Th17 cells and their IL-17A production (IL-17A already mapped), a second effector arm of the autoimmune demyelination of CIDP.
- `connects-to` → **[Interleukin-10](../../03-molecular/il-10/README.md)** — IL-10 from regulatory T cells normally dampens these responses, and its relative insufficiency permits the sustained autoimmune nerve injury of CIDP, with recovery often accompanying remission.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR-MyD88-NF-κB innate signaling (TLR4 and NF-κB already mapped) in endoneurial macrophages drives the inflammatory demyelination of peripheral nerve in CIDP.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — Complement activation generates C5a that engages C5aR1 to recruit and activate macrophages (C3 and C5 already mapped), effecting the complement-mediated myelin injury of CIDP.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — NRF2-regulated antioxidant defense counters the oxidative stress of chronic nerve inflammation, modulating the secondary axonal injury that determines lasting disability in CIDP.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — BAFF-driven PI3K-AKT signaling (BAFF mapped) sustains the autoreactive B cells producing the pathogenic antibodies of CIDP.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — The mTOR-regulated metabolic program supports the antibody-secreting plasmablast and effector-T-cell responses in CIDP.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Macrophage galectin-3 participates in the macrophage-mediated demyelination of peripheral nerves in CIDP.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the Th1/interferon component of the autoimmune attack on peripheral-nerve myelin in CIDP.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA released by nerve and Schwann-cell injury can engage cGAS-STING, amplifying the innate inflammation of CIDP.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling shapes the Schwann-cell remyelination responses that determine recovery in CIDP.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO regulates the autoreactive lymphocyte tolerance and Schwann-cell oxidative-stress responses relevant to the demyelination of CIDP.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling transduces the macrophage and Schwann-cell responses driving the demyelination of CIDP.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins from infiltrating macrophages amplify the inflammatory nerve injury of CIDP.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the T-cell and macrophage inflammatory signaling that drives the demyelination of chronic inflammatory demyelinating polyneuropathy.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) supports the survival and activation of the autoreactive T and B cells of chronic inflammatory demyelinating polyneuropathy.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α in the inflamed peripheral nerve contributes to the metabolic and inflammatory milieu of chronic inflammatory demyelinating polyneuropathy.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked immunometabolic signaling shapes the autoreactive T-cell and macrophage metabolism of chronic inflammatory demyelinating polyneuropathy.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the autoreactive-immune-cell and Schwann-cell responses of chronic inflammatory demyelinating polyneuropathy.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte recruitment into the peripheral nerve contributes to the demyelinating inflammation of chronic inflammatory demyelinating polyneuropathy.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the autoreactive immune response of chronic inflammatory demyelinating polyneuropathy.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the immune-cell and Schwann-cell signaling of chronic inflammatory demyelinating polyneuropathy.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the neuroinflammatory and immune responses of chronic inflammatory demyelinating polyneuropathy.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the autoreactive immune responses of chronic inflammatory demyelinating polyneuropathy.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the T-cell activation of chronic inflammatory demyelinating polyneuropathy.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine signaling participates in the immunomodulation and neuroinflammatory processes of chronic inflammatory demyelinating polyneuropathy.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — Nerve support and repair: BDNF and neurotrophic signalling support axonal survival and remyelination, and their adequacy shapes recovery from the demyelinating injury of chronic inflammatory demyelinating polyneuropathy.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Th2 help: IL-4-driven type-2 help supports the B-cell and autoantibody responses (immunoglobulin G already mapped) against nodal and myelin antigens in chronic inflammatory demyelinating polyneuropathy.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Immune checkpoint: PD-1 normally restrains autoreactive T cells, and checkpoint-inhibitor cancer therapy can trigger a CIDP-like neuropathy, revealing the role of this checkpoint in protecting peripheral nerve from autoimmunity.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 humoral help: IL-13, with the IL-4 (already mapped) type-2 response, supports the B-cell autoantibody production against nodal and myelin antigens that drives the demyelination of chronic inflammatory demyelinating polyneuropathy.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Nerve inflammatory injury: nitric oxide from activated macrophages (already mapped) in the inflamed nerve contributes to the demyelination and secondary axonal injury of CIDP, part of the effector damage beyond antibody and complement.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Endoneurial fibrosis: chronic and relapsing inflammation in CIDP leads to onion-bulb formation and endoneurial collagen deposition, the fibrotic scarring of repeated demyelination and remyelination that underlies fixed disability.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Inflammatory eicosanoids: prostaglandins from the macrophages (already mapped) and infiltrating cells of the inflamed nerve amplify the demyelinating inflammation (IL-6, TNF and IL-1 already mapped) of CIDP.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative nerve injury: the inflamed nerve generates oxidative stress, to which xanthine oxidase contributes, and the resulting reactive oxygen species (nitric oxide already mapped) add to the demyelination and secondary axonal injury of CIDP.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Myelin lipid: myelin is a cholesterol-rich membrane, and the repeated demyelination and remyelination of CIDP demand the cholesterol handling of the Schwann cells rebuilding the myelin sheath.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — Neurotrophic remyelination: IGF-1 supports the Schwann-cell remyelination and axonal maintenance (BDNF already mapped), part of the reparative response to the repeated demyelination of CIDP.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — Schwann-cell proliferation: PDGF drives the Schwann-cell proliferation of the onion-bulb remyelination that characterises the chronic, relapsing demyelination and repair of CIDP.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Copper-deficiency mimic: copper deficiency causes a myeloneuropathy with demyelination that can clinically mimic CIDP, an important metabolic differential in the chronic neuropathies.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate immune signalling: type-I interferon is part of the innate-immune signalling of the autoimmune demyelination of the peripheral nerve (already mapped) in CIDP.
- `connects-to` → **[Plasma cell](../../04-cellular/plasma-cell/README.md)** — Autoantibody source: the long-lived plasma cells secrete the anti-myelin and anti-nodal IgG (immunoglobulin already mapped) autoantibodies of CIDP, resisting the B-cell (CD20 already mapped) depletion, the rationale for the anti-plasma-cell approaches.
- `connects-to` → **[NMO](../nmo/README.md)** — Antibody-mediated demyelination sibling: neuromyelitis optica and CIDP are antibody- and complement (already mapped)-mediated demyelinating diseases (CNS vs PNS), both responding to the B-cell (CD20 already mapped) and complement therapies.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Immune-metabolic adipokine: leptin is the adipokine of the immune-metabolic milieu and the steroid (cortisol already mapped)-related metabolic disturbance of CIDP.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the immune-metabolic milieu of CIDP.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the systemic inflammation (IL-6 already mapped) of CIDP.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Inflammatory infiltrate: the neutrophils and the neutrophil-lymphocyte ratio are part of the inflammatory infiltrate (CCL2 already mapped) of the demyelinating nerve lesions of CIDP.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension balancing the dominant Th1/Th17 (IFN-γ, IL-12 and IL-23 already mapped) drive of CIDP.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 IgE: the IgE (with IL-4 and IL-13 already mapped) reflects the type-2 immune dimension present in a subset of CIDP.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Mast cells in nerve: the mast cells infiltrate the inflamed peripheral nerve and contribute to the type-2 (IgE already mapped) and the vascular-permeability dimension of the demyelination of CIDP.
- `connects-to` → **[Vitamin D](../../../03-medicine/03-food/vitamin-d/README.md)** — Immunomodulatory vitamin: the low vitamin D status is associated with the autoimmune neuropathies, and its immunomodulation of the T-helper (already mapped) response is studied in CIDP.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Antioxidant micronutrient: selenium, a selenoprotein cofactor, is part of the oxidative-stress and micronutrient dimension of the peripheral-nerve inflammation of CIDP.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^vanlaar-2010-efns-cidp]: European Federation of Neurological Societies/Peripheral Nerve Society. Guideline on management of CIDP. *J Peripher Nerv Syst.* 2010;15(1):1-9. [doi:10.1111/j.1529-8027.2010.00238.x](https://doi.org/10.1111/j.1529-8027.2010.00238.x) · [PubMed 20433600](https://pubmed.ncbi.nlm.nih.gov/20433600/)
[^merkies-2008-ivig-ice]: Hughes RA, et al. Intravenous immune globulin for CIDP (ICE study). *Lancet Neurol.* 2008;7(2):136-144. [doi:10.1016/S1474-4422(07)70329-0](https://doi.org/10.1016/S1474-4422(07)70329-0) · [PubMed 18178525](https://pubmed.ncbi.nlm.nih.gov/18178525/)
[^vandenberheijde-2023-efgartigimod-cidp]: van den Bergh PYK, et al. Efgartigimod alfa and hyaluronidase-qvfc in CIDP (ADHERE). *N Engl J Med.* 2023;390(3):219-232. [doi:10.1056/NEJMoa2310819](https://doi.org/10.1056/NEJMoa2310819) · [PubMed 38197812](https://pubmed.ncbi.nlm.nih.gov/38197812/)
[^van-den-bergh-2023-cidp-guidelines]: Van den Bergh PYK, et al. EAN/PNS guideline on CIDP: 2023 update. *Eur J Neurol.* 2023;30(10):2976-3020. [doi:10.1111/ene.15927](https://doi.org/10.1111/ene.15927) · [PubMed 37382198](https://pubmed.ncbi.nlm.nih.gov/37382198/)
