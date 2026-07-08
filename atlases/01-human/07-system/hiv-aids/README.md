---
schema: human-scale-entry/v1
id: hiv-aids
name: HIV/AIDS
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "HIV/AIDS (HIV-1; retrovirus; CCR5/CXCR4 co-receptor) systematically depletes CD4+ T cells → immunodeficiency → AIDS-defining illnesses; ART (antiretrovirals, 6+ classes) suppresses viral load to undetectable; U=U (Undetectable = Untransmittable) prevents sexual transmission."
aliases: ["HIV", "human immunodeficiency virus", "AIDS", "acquired immunodeficiency syndrome", "HIV-1", "HIV-2", "PLHIV", "ART", "antiretroviral therapy", "HAART"]
sources:
  - id: barre-sinoussi-1983-hiv
    type: peer-reviewed
    cite: "Barré-Sinoussi F, Chermann JC, Rey F, et al. Isolation of a T-lymphotropic retrovirus from a patient at risk for acquired immune deficiency syndrome (AIDS). Science. 1983;220(4599):868-871."
    doi: "10.1126/science.6189183"
    pmid: "6189183"
    url: "https://doi.org/10.1126/science.6189183"
    accessed: "2026-06-08"
  - id: dhhs-2024-hiv-guidelines
    type: clinical-guideline
    cite: "Panel on Antiretroviral Guidelines for Adults and Adolescents. Guidelines for the Use of Antiretroviral Agents in Adults and Adolescents with HIV. US Department of Health and Human Services. 2024."
    url: "https://clinicalinfo.hiv.gov/en/guidelines"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "HIV-1 entry requires CD4 + CCR5 (R5-tropic, early infection) or CXCR4 (X4-tropic, late/AIDS stage); CCR5-Δ32 homozygosity → complete HIV-1 resistance; maraviroc (CCR5 antagonist) requires prior tropism testing (Trofile assay) to exclude X4-tropic virus."
  - target: 01-human/07-system/tuberculosis
    relation: connects-to
    note: "HIV-TB co-infection is the most lethal pathogen combination: HIV depletes CD4+ Th1 cells → granuloma dissolution → TB reactivation; TB is the leading cause of AIDS death; concurrent ART + HRZE reduces mortality; IRIS complicates early ART in TB-HIV co-infection."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "HIV-1 depletes CD4+ T cells (gp120 → CD4/CCR5 → fusion → reverse transcription → integration → viral DNA); AIDS defined as CD4 <200/μL or AIDS-defining illness; chronic immune activation drives T cell exhaustion and monocyte dysregulation even with ART."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "HIV drives ACD via sustained immune activation → IL-6 + IFN-γ → hepcidin elevation → functional iron deficiency; AZT-induced bone marrow suppression adds an aplastic component; severity correlates with viral load and CD4 count; ART reduces ACD severity."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "IL-12/IFN-γ axis is severely impaired in HIV-AIDS: HIV depletes CD4+ Th1 cells → ↓IFN-γ → ↓macrophage activation; DCs in AIDS produce less IL-12; IL-12 deficiency → susceptibility to TB, NTM, Leishmania, and dimorphic fungi; ART partially restores IL-12 responsiveness."
  - target: 01-human/07-system/leishmaniasis
    relation: connects-to
    note: "HIV-VL co-infection: CD4+ Th1 cell depletion → loss of IFN-γ → Leishmania escapes macrophage control → disseminated VL; Mediterranean Europe, East Africa, and Indian subcontinent are co-endemic zones; ART partially restores anti-Leishmania Th1 immunity; L-AmB prophylaxis needed."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "AIDS is defined by the loss of CD4+ T helper cells: as HIV drives their count below 200/μL, cell-mediated immunity collapses, opening the door to the opportunistic infections and cancers that define the syndrome; ART restores ~100-150 cells/μL per year."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: connects-to
    note: "Pneumocystis jirovecii pneumonia (PCP) is the classic AIDS-defining infection, striking once CD4 falls below 200/μL: this fungus causes a diffuse interstitial pneumonia, treated and prevented with trimethoprim-sulfamethoxazole — prophylaxis started at that CD4 threshold."
  - target: 01-human/07-system/pcnsl
    relation: connects-to
    note: "Primary CNS lymphoma is an AIDS-defining malignancy of profound immunosuppression (CD4 <50/μL): unchecked Epstein-Barr virus drives a brain B-cell lymphoma, and restoring immunity with ART is central to treatment alongside methotrexate or radiation."
  - target: 02-pathogen/01-viruses/hiv-1
    relation: connects-to
    note: "AIDS is the late stage of HIV-1 infection: years of unchecked viral replication deplete CD4 T cells below ~200/µL, collapsing cell-mediated immunity and opening the door to opportunistic infections and cancers; antiretroviral therapy suppressing HIV-1 prevents and can reverse it."
  - target: 01-human/07-system/cervical-cancer
    relation: connects-to
    note: "Cervical cancer is an AIDS-defining illness: HIV-driven immunosuppression lets oncogenic HPV persist and progress faster to invasive cancer, so women with HIV face markedly higher risk; antiretroviral therapy and HPV vaccination plus screening are key preventive measures."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "AIDS reflects the collapse of T-cell immunity: as CD4 helper cells fall, CD8+ cytotoxic T cells lose the help they need and become exhausted, so cell-mediated control of viruses, intracellular bacteria and tumors fails—explaining the opportunistic infections that define AIDS."
  - target: 01-human/07-system/hiv
    relation: connects-to
    note: "HIV/AIDS is the disease end of HIV infection: as the retrovirus depletes CD4 T cells, defenses collapse and AIDS-defining opportunistic infections and cancers appear—so the pathogen and the syndrome name one continuum, now arrested early by antiretroviral therapy."
  - target: 01-human/07-system/burkitt-lymphoma
    relation: connects-to
    note: "Burkitt lymphoma is an AIDS-defining cancer: HIV-driven immune dysregulation and chronic B-cell activation, often with EBV co-infection, raise Burkitt risk even at preserved CD4 counts—so a fast-growing lymphoma in an HIV patient is Burkitt until proven otherwise."
  - target: 01-human/07-system/hepatitis-b
    relation: connects-to
    note: "HIV and hepatitis B frequently coinfect via shared blood and sexual routes: HIV accelerates HBV liver fibrosis, and several antiretrovirals (tenofovir, lamivudine) suppress both viruses—so HIV regimens are chosen to cover HBV and avoid flares if stopped."
  - target: 01-human/07-system/hodgkin-lymphoma
    relation: connects-to
    note: "Hodgkin lymphoma is more common in HIV/AIDS though not AIDS-defining: even on antiretrovirals, HIV patients have several-fold higher Hodgkin risk, usually EBV-driven—a malignancy whose rate, unlike AIDS-defining lymphomas, did not fall with treatment."
  - target: 01-human/07-system/dlbcl
    relation: connects-to
    note: "Diffuse large B-cell lymphoma is the commonest AIDS-defining lymphoma: profound immunosuppression and EBV co-infection let B cells proliferate unchecked, so DLBCL marks advanced HIV—rates dropped sharply with antiretroviral immune restoration."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages are a key HIV reservoir and disease driver: unlike CD4 T cells, infected macrophages resist HIV's cytopathic effect and survive, seeding tissues (including the brain) with virus that persists despite antiretrovirals—a major obstacle to cure."
  - target: 02-pathogen/03-fungi/candida-albicans
    relation: connects-to
    note: "Oral and esophageal candidiasis is a hallmark of advancing HIV/AIDS: as CD4 counts fall, Candida albicans overgrows mucosa it normally cannot, so thrush and esophagitis are clinical clues to immunosuppression and an AIDS-defining illness when esophageal."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "HIV/AIDS frequently strikes the nervous system: beyond direct HIV brain infection causing dementia, falling CD4 counts open the door to CNS opportunists—toxoplasmosis, cryptococcal meningitis and CNS lymphoma—making neurologic disease a major source of AIDS morbidity."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "HIV/AIDS plays out largely in the lymphatic system: lymphoid tissue is where the virus replicates and where CD4 T cells are depleted, generalized lymphadenopathy is an early sign, and the resulting immune collapse drives the lymphomas that complicate AIDS."
  - target: 02-pathogen/03-fungi/cryptococcus-neoformans
    relation: connects-to
    note: "Cryptococcus is a leading AIDS killer: when CD4 counts fall, this environmental yeast causes cryptococcal meningitis, a major cause of death in advanced HIV worldwide—so a positive serum cryptococcal antigen prompts urgent antifungal treatment."
  - target: 02-pathogen/04-parasites/toxoplasma-gondii
    relation: connects-to
    note: "Toxoplasma reactivates in AIDS as brain abscesses: latent cysts flare when CD4 counts drop, producing ring-enhancing lesions and toxoplasmic encephalitis—so seropositive patients take prophylaxis, the same drugs treating Pneumocystis."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "AIDS turns the brain into a battleground: falling immunity invites toxoplasmosis, cryptococcal meningitis, PCNSL, and PML, while HIV itself causes dementia—so new neurological signs in advanced HIV demand urgent imaging and workup."
  - target: 02-pathogen/01-viruses/epstein-barr-virus
    relation: connects-to
    note: "AIDS unleashes Epstein-Barr-driven lymphomas: with CD4 cells gone, EBV escapes immune control to cause primary CNS lymphoma, Burkitt, Hodgkin and DLBCL—the EBV-linked cancers that define advanced HIV."
  - target: 02-pathogen/01-viruses/hpv-16
    relation: connects-to
    note: "HIV lets oncogenic HPV run wild: immunosuppression reactivates HPV-16, driving the cervical and anal cancers that are AIDS-defining—so HPV vaccination and cancer screening are essential in HIV care."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "HIV exploits dendritic cells to spread: these antigen-presenting cells capture the virus at mucosal surfaces and ferry it to lymph nodes, handing it to the CD4 T cells it destroys—turning a sentinel of immunity into a vehicle for infection."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "The lung is the classic stage for AIDS: as CD4 cells vanish, Pneumocystis pneumonia and other lung infections take hold, so a previously rare fungal pneumonia became the alarm that first announced the AIDS epidemic."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "AIDS often shows itself in the gut: with immunity gone, infections like cryptosporidium and CMV inflame the intestine, causing the relentless diarrhea and wasting—'slim disease'—that mark advanced untreated infection."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "AIDS cripples B cells even as it spares them from direct infection: lost CD4 help leaves antibody responses disorganized, raising risk of bacterial infections, while chronic stimulation drives the B-cell lymphomas that define late disease."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "AIDS suffocates through Pneumocystis: as immunity collapses, this fungal pneumonia (PCP) fills the lungs and starves the blood of oxygen, the AIDS-defining infection whose silent, worsening hypoxia is a classic warning sign."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "AIDS can blind through the eye: when CD4 counts crash, cytomegalovirus attacks the retina (CMV retinitis), an AIDS-defining infection that destroys sight unless immunity is restored."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "AIDS turns endothelial cells cancerous: the herpesvirus KSHV infects these vessel-lining cells and, with immunity gone, transforms them into Kaposi sarcoma, the purple vascular tumor that became the face of the epidemic."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Imaging is central to AIDS care: chest X-ray photons reveal the diffuse infiltrates of PCP pneumonia, and brain CT or MRI distinguishes the ring-enhancing lesions of toxoplasmosis from CNS lymphoma."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "In AIDS the bone marrow becomes a battleground: disseminated infections like MAC and histoplasmosis invade it while HIV and drugs suppress it, deepening the cytopenias of advanced disease."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "AIDS often shows first on the skin: severe shingles, stubborn fungal and seborrheic rashes, and oral thrush are common early warnings that immunity is failing."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy names AIDS's opportunists: the foamy cysts of Pneumocystis, the owl-eye inclusions of CMV, and viral particles in tumors come into focus, letting the diagnostic beam catch the infections that exploit a collapsed immune system."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "AIDS scars the kidney directly: HIV-associated nephropathy, a collapsing form of focal glomerulosclerosis, drives heavy protein loss and rapid renal failure, especially before antiretroviral therapy takes hold."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Advanced AIDS weakens the heart: chronic infection and direct viral injury can dilate it into an HIV cardiomyopathy, and pericardial effusions from opportunistic infections add to the cardiac toll."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "AIDS is diagnosed by antibody yet defined by immune failure: the anti-HIV antibody test identifies infection, but as CD4 cells vanish the body's whole antibody response falters, leaving even vaccines and routine defenses ineffective."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "AIDS reaches deep into the brain: the virus and its opportunistic invaders — toxoplasma, JC virus's PML, CMV — injure neurons into HIV-associated dementia, the cognitive decline that marks advanced disease."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "HIV thins the platelets: an immune thrombocytopenia is common and can be an early sign, as antibodies and direct marrow infection drop the platelet count, sometimes improving once antiretroviral therapy begins."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "The nerves ache in advanced HIV: a distal sensory polyneuropathy from the virus itself and from older antiretrovirals brings burning, numb feet, one of the most common and disabling neurological complications."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "The epidemic turns on reproduction and prevention: HIV spreads sexually and from mother to child, but treatment-as-prevention (undetectable = untransmittable) and PrEP now block both routes, reshaping its spread."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "Adrenal failure stalks advanced disease: CMV adrenalitis and other opportunistic invaders, plus the virus itself, impair cortisol production, making adrenal insufficiency a treatable cause of the wasting and collapse of late AIDS."
  - target: 02-pathogen/02-bacteria/mycobacterium-tuberculosis
    relation: connects-to
    note: "Tuberculosis is the great killer of AIDS: the failing CD4 defense lets Mycobacterium tuberculosis reactivate and spread, making TB the leading cause of death in people with HIV worldwide."
  - target: 01-human/07-system/malaria
    relation: connects-to
    note: "HIV and malaria amplify each other: the immune deficit makes malaria more frequent and severe, especially in pregnancy, while acute malaria transiently raises HIV viral load across their co-endemic regions."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Innate defense falters too: natural killer cells fall in number and function in advanced HIV, weakening the early control of viruses and tumors that lets opportunistic infections and AIDS cancers take hold."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "The gut is ground zero: HIV depletes the mucosal CD4 and Th17 cells early, breaching the gut barrier so microbial products leak into the blood — a microbial translocation that drives the chronic immune activation behind AIDS progression."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "The virus and its drugs strain the kidney: HIV-associated nephropathy plus the toxicity of some antiretrovirals make chronic kidney disease a common comorbidity, especially in untreated or African-ancestry patients."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Survival exposes a new killer: with opportunistic infections controlled, the chronic inflammation of treated HIV accelerates atherosclerosis, making cardiovascular disease a leading cause of death in the aging AIDS-era population."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "The virus wires itself to the host's master switch: HIV's LTR carries NF-κB binding sites, so the very pathway that activates T cells also drives proviral transcription — a link that ties immune activation to viral reactivation from latency."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "It hijacks JAK-STAT to persist: HIV manipulates STAT3 signaling in infected cells, contributing to the chronic immune activation and reservoir maintenance that smolder even under effective therapy."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Collapsed immunity ends in overwhelming infection: in advanced AIDS, opportunistic and bacterial infections readily disseminate into sepsis, a common terminal event when CD4 counts fall and defenses fail."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Profound immune loss opens the lung to mold: in advanced AIDS, especially with neutropenia or steroids, invasive pulmonary aspergillosis joins the opportunistic infections that exploit the collapsed defenses."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "The virus inflames the arteries: HIV drives an accelerated atherosclerosis and a direct vasculopathy, and with chronic immune activation even treated patients carry a raised long-term risk of ischemic stroke."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Virus and therapy both thin the bone: chronic HIV inflammation plus antiretrovirals — tenofovir disoproxil especially — accelerate bone loss, giving people with HIV high rates of osteoporosis and fracture."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "It attacks the peripheral nerves: advanced HIV causes a distal sensory polyneuropathy, and older antiretrovirals compounded it, producing the chronic burning foot pain common in long-standing infection."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "The virus can weaken the heart muscle: HIV-associated cardiomyopathy from direct viral effects, chronic inflammation and opportunistic infection remains a cause of heart failure even in the antiretroviral era."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "It burdens the mind directly and through stigma: HIV causes depression via neuroinflammation and CNS infection, compounded by the chronic illness, isolation and stigma of living with the disease."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "AIDS wastes and infects the gut: advanced HIV brings the wasting syndrome and opportunistic GI infections — CMV colitis, cryptosporidiosis and oesophageal candidiasis — causing intractable diarrhoea and malnutrition."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "The skin reveals advancing immunodeficiency: AIDS brings Kaposi sarcoma, disseminated herpes and zoster, severe seborrhoeic dermatitis and eosinophilic folliculitis, often the visible markers of progression."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "An advanced, stigmatised illness breeds worry: the opportunistic-infection risk, disclosure fears and uncertainty of AIDS foster chronic health anxiety alongside its well-recognised depression."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "The lungs define many AIDS illnesses: Pneumocystis pneumonia, tuberculosis and pulmonary Kaposi sarcoma are AIDS-defining lung diseases that emerge as CD4 counts fall."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It wastes and weakens the frame: HIV myopathy, profound AIDS wasting and avascular necrosis of bone erode the musculoskeletal system in advanced disease."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Advanced infection derails hormones: AIDS wasting syndrome, adrenal insufficiency from disseminated CMV or mycobacterial infection, and hypogonadism reflect endocrine collapse in late disease."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "HIV attacks the kidney directly: HIV-associated nephropathy, a collapsing FSGS, plus tenofovir tubular toxicity and immune-complex disease drive chronic kidney failure."
  - target: 02-pathogen/01-viruses/herpesvirus
    relation: connects-to
    note: "AIDS reactivates the herpes family: CMV causes sight-threatening retinitis and colitis, HHV-8 drives Kaposi sarcoma, and severe mucocutaneous herpes-simplex marks deep immunodeficiency."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "Shingles flags failing immunity: multidermatomal or recurrent herpes-zoster is an early marker of HIV-related immune decline and can disseminate in advanced AIDS."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "The virus injures the brain through them: HIV-infected microglia and macrophages release neurotoxins driving HIV encephalitis and the cognitive decline of HIV-associated neurocognitive disorder."
  - target: 03-medicine/03-food/zinc-dietary
    relation: connects-to
    note: "Wasting depletes key nutrients: zinc deficiency is common in advanced HIV and contributes to immune dysfunction, with supplementation studied to support immunity in the malnourished."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Smouldering inflammation persists despite treatment: chronically raised IL-6 from residual immune activation drives the cardiovascular disease, frailty and other comorbidities seen in treated HIV."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "AIDS-defining cancers need chemo: Kaposi sarcoma and the aggressive non-Hodgkin lymphomas that define AIDS are treated with chemotherapy alongside antiretrovirals, with immune reconstitution itself improving tumour control."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Immunotherapy enters HIV oncology: checkpoint inhibitors treat HIV-associated lung cancer and Kaposi sarcoma, and by reversing T-cell exhaustion are studied as part of cure strategies to flush the latent reservoir."
  - target: 01-human/05-tissue/axonal-transport
    relation: connects-to
    note: "It degenerates the long nerves: HIV and some antiretrovirals cause a distal sensory polyneuropathy, a dying-back axonopathy of impaired axonal transport producing painful, length-dependent neuropathy."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "It dismantles the lymph node: HIV destroys the follicular dendritic networks and germinal centres where antibody responses mature, so humoral immunity decays even as the virus hides in this reservoir."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "HIV-associated nephropathy: HIV injures glomerular cells to cause a collapsing focal segmental glomerulosclerosis, classically in people of African ancestry, a leading cause of kidney failure in untreated AIDS."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Treated HIV still inflames arteries: persistent immune activation and antiretroviral metabolic effects accelerate atherosclerosis, making cardiovascular disease a leading cause of death in the ART era."
  - target: 01-human/07-system/hepatitis-c
    relation: connects-to
    note: "Shared routes, dual infection: HIV and hepatitis C share blood-borne and sexual transmission, and HIV accelerates HCV liver fibrosis, so co-infection is common and worsens both diseases."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Immunodeficiency meets a pandemic: advanced, untreated HIV raises the risk of severe COVID-19 and prolonged viral shedding, while blunting the antibody response to vaccination."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "HIV and the heart muscle: chronic immune activation in HIV/AIDS causes a dilated cardiomyopathy of the myocardium and accelerates heart failure, persisting as a cardiovascular burden despite ART."
  - target: 01-human/07-system/cytokine-storm
    relation: connects-to
    note: "Immune reconstitution storm: starting ART in advanced AIDS can unleash IRIS, a paradoxical inflammatory surge against unmasked opportunistic infections as the recovering immune system overreacts."
  - target: 01-human/07-system/immune-thrombocytopenia
    relation: connects-to
    note: "HIV-associated low platelets: HIV is a classic secondary cause of immune thrombocytopenia, driving antibody-mediated platelet destruction that often improves once ART controls the virus."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Pneumocystis fills the lung: PJP, the AIDS-defining pneumonia, packs the alveoli with foamy exudate and causes the hypoxic respiratory failure that long defined advanced HIV."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Failing cytotoxicity: CD8 cytotoxic T cells kill HIV-infected cells with perforin, but as the disease advances toward AIDS this response becomes exhausted and the virus escapes control."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Chronic interferon: persistent type-I interferon signalling in untreated HIV paradoxically drives immune exhaustion and activation rather than clearing the virus, contributing to progression to AIDS."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Wasting and activation: TNF-α from the chronic immune activation of advanced HIV drives the cachexia, fever and systemic inflammation that mark the AIDS-defining state."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Collapse of Th1 defence: loss of CD4 T helper cells cripples IFN-γ-dependent macrophage activation, removing the control of intracellular pathogens and opening the door to the opportunistic infections that define AIDS."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Pyroptotic depletion: abortive HIV infection of resting CD4 cells triggers inflammasome-driven caspase-1 pyroptosis, the dominant mechanism of CD4 T-cell loss driving progression to AIDS."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "DNA sensing of the virus: cGAS-STING detection of HIV reverse-transcription intermediates fuels the chronic type-I-interferon response and immune activation that accelerate immune exhaustion in AIDS."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "X4 tropism in late disease: emergence of CXCR4-using (X4) HIV, whose ligand is CXCL12, marks advanced infection and accelerates the CD4 collapse that ushers in the AIDS-defining stage."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Terminal exhaustion: profound PD-1-marked T-cell exhaustion in AIDS leaves the few remaining T cells unable to control HIV or opportunistic pathogens, the functional endpoint of the immune collapse."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Helper-cell collapse: the destruction of CD4 T cells in AIDS dismantles MHC-class-II-restricted T-helper responses, removing the help that B cells and CD8 cells need and explaining the broad immunodeficiency."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "CD4 cell death: HIV destroys CD4 T cells both by caspase-3 apoptosis of infected cells and by abortive-infection-triggered inflammatory death of bystander cells, the depletion that drives the progression to AIDS-defining immunodeficiency."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Homeostasis collapse: loss of CD4 T cells in AIDS removes a major source of IL-2 needed to sustain T-cell proliferation and survival, deepening the lymphopenia in a self-reinforcing failure of the adaptive immune compartment."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive milieu: the IL-10-skewed, exhausted immune state of advanced AIDS suppresses the residual cellular immunity, helping explain the susceptibility to the opportunistic infections that define the syndrome."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Microbial translocation: leakage of microbial products across the damaged gut epithelium in AIDS engages TLR4, driving the chronic immune activation that accelerates CD4 decline and progression."
  - target: 01-human/03-molecular/mavs
    relation: connects-to
    note: "Innate evasion: HIV antagonises RIG-I/MAVS antiviral signalling, contributing to the impaired innate control of the virus that permits progression to AIDS."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Lymphoid fibrosis: TGF-β drives the collagen deposition and lymphoid-tissue fibrosis of chronic HIV that impairs immune reconstitution even on effective antiretroviral therapy."
  - target: 01-human/03-molecular/hiv-gp120
    relation: connects-to
    note: "Viral entry and cytopathicity: HIV gp120 binds CD4 and the CCR5 co-receptor (already mapped) to mediate entry, and its engagement of bystander cells drives the syncytia formation and CD4 depletion that define progression to AIDS."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Chronic immune activation: interferon and inflammatory-cytokine signalling through JAK-STAT (type-I IFN and STAT3 already mapped) sustains the persistent immune activation that drives AIDS progression and is a JAK-inhibitor target under study."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "T-cell apoptosis: HIV dysregulates the Bcl-2 family to tip infected and bystander CD4+ T cells toward apoptosis, a major mechanism of the progressive lymphocyte depletion of AIDS."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "HIV exploits PI3K-AKT signalling to promote infected-cell survival and viral persistence as immunity collapses in AIDS."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTOR-regulated T-cell metabolism shapes both HIV replication and the exhausted, dysfunctional immune state of AIDS."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "TLR-MyD88 signalling driven by gut microbial translocation sustains the chronic immune activation that accelerates progression to AIDS."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 promotes HIV-1 budding and amplifies the chronic immune activation that drives progression to AIDS."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling (type-I interferon already mapped) drives the antiviral and chronic interferon response that shapes immune exhaustion in AIDS."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signalling is engaged during HIV replication and contributes to the activation state of infected and bystander immune cells in AIDS."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "HIV-driven PI3K-AKT-FOXO modulation (AKT already mapped) shapes the T-cell survival-versus-depletion balance underlying progression to AIDS."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α supports viral replication and the metabolic dysregulation of immune cells in advanced HIV/AIDS."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins reflect the chronic myeloid inflammatory activation and immune exhaustion of HIV/AIDS."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the T-cell survival and inflammatory signaling relevant to the immune exhaustion and reservoir persistence of HIV/AIDS."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "HIV subverts host autophagy in CD4 T cells and macrophages, contributing to the immune-cell depletion and viral persistence of HIV/AIDS."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) governs the T-cell survival pathways dysregulated in the profound immunodeficiency of HIV/AIDS."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family (LCK) kinase signaling downstream of the T-cell receptor participates in the T-cell activation and immune dysfunction of HIV/AIDS."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked immunometabolic signaling shapes the T-cell metabolism and exhaustion of HIV/AIDS."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the proviral latency and T-cell-exhaustion epigenetics of HIV/AIDS."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the mucosal and immune dysregulation of HIV/AIDS."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling and the loss of Th17 cells participate in the mucosal barrier dysfunction and opportunistic-infection susceptibility of HIV/AIDS."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the innate immune responses and immune-complex processes of HIV/AIDS."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammasome activation participates in the chronic immune activation of AIDS."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "CCL2 (MCP-1) chemokine signaling participates in the monocyte trafficking and HIV-associated neurocognitive and tissue inflammation of AIDS."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine signaling (the CD73/CD39 pathway) participates in the immunosuppression and immune exhaustion of AIDS."
  - target: 01-human/03-molecular/lmp1
    relation: connects-to
    note: "EBV malignancies: profound immunosuppression in AIDS permits Epstein-Barr-virus-driven lymphomas including primary CNS lymphoma (already mapped), where the viral oncoprotein LMP1 drives B-cell transformation unchecked by the lost T-cell surveillance."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Wasting and lipodystrophy: AIDS wasting syndrome and antiretroviral lipodystrophy involve dysregulated leptin and adipose signalling, driving the loss of lean mass and the metabolic complications that persist even with treatment."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Advanced anaemia: anaemia deepens as HIV progresses to AIDS through marrow suppression, opportunistic infection and drug toxicity, and a low haemoglobin is a strong independent predictor of mortality."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Polyclonal hypergammaglobulinaemia: AIDS produces high but poorly targeted IgG from dysregulated B cells (BAFF-driven), an ineffective antibody excess that coexists with failing specific immunity and raises the risk of B-cell lymphomas."
  - target: 01-human/03-molecular/secretory-iga
    relation: connects-to
    note: "Mucosal immunity loss: destruction of gut-associated lymphoid tissue in AIDS impairs secretory IgA at mucosal surfaces, weakening the barrier and contributing to the enteric opportunistic infections and HIV enteropathy that drive wasting."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Th1-to-Th2 shift: progression to AIDS is accompanied by a shift away from the protective Th1 response (IL-12/IFN-gamma already mapped) toward IL-4-driven type-2 immunity, a cytokine reorientation that tracks with immune collapse."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Anaemia of AIDS: the chronic inflammation of advanced HIV raises hepcidin to sequester iron, and with marrow suppression, opportunistic infection and drug toxicity this produces the multifactorial anaemia (haemoglobin already mapped) common in AIDS."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Metabolic paradox: advanced AIDS causes wasting, yet antiretroviral therapy and chronic immune activation disturb cholesterol handling toward an atherogenic profile, part of the metabolic and cardiovascular burden that persists on treatment."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative immune activation: the persistent immune activation of AIDS generates oxidative stress, to which xanthine oxidase contributes, and the resulting reactive oxygen species add to the tissue injury and accelerated ageing of the disease."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Selenium and mortality: selenium deficiency is common in AIDS and strongly predicts mortality, its antioxidant selenoproteins countering the oxidative immune activation (xanthine oxidase already mapped) of advanced disease."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc and progression: zinc deficiency is common in AIDS and associated with faster progression and more opportunistic infections, reflecting zinc's role in the immune function depleted by the disease."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Immune-activation eicosanoids: prostaglandins from the chronic immune activation and inflammation (IL-6, TNF and IL-1 already mapped) of AIDS modulate the immune response and contribute to the persistent tissue injury of the disease."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Multifactorial anaemia: the anaemia of chronic infection (hepcidin and haemoglobin already mapped) combines with the marrow suppression, drugs and opportunistic infections to cause the multifactorial iron-disturbed anaemia common in AIDS."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Th2 immune shift: IL-13, with IL-4 (already mapped), reflects the Th2 shift of the immune dysregulation of AIDS, part of the loss of the Th1 (IFN-γ and IL-12 already mapped) control that permits the opportunistic infections."
  - target: 01-human/03-molecular/baff
    relation: connects-to
    note: "B-cell hyperactivation: the raised BAFF of AIDS drives the B-cell hyperactivation and the hypergammaglobulinaemia (immunoglobulin already mapped), contributing to the B-cell lymphomas (LMP1 already mapped) of the disease."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Lipodystrophy adipokine: adiponectin, with leptin (already mapped), is disturbed by the HIV lipodystrophy and the ART-associated metabolic syndrome (insulin already mapped) of AIDS."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipokine of the HIV lipodystrophy and the metabolic-inflammatory (IL-6 already mapped) milieu of AIDS."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Kaposi angiogenesis: the Kaposi sarcoma (an AIDS-defining, HHV-8-driven malignancy) is highly angiogenic (VEGF), the vascular tumour of the profound immunosuppression of AIDS."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Immune dysregulation: the regulatory T cells are disproportionately altered relative to the depleted CD4 T-helper cells (already mapped), contributing to the immune dysregulation and the loss of tolerance of AIDS."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Th2 shift: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the Th2 shift of the progressive immunodeficiency of AIDS."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Elevated IgE: the polyclonal B-cell (BAFF already mapped) activation of AIDS raises the IgE (with IL-4 and IL-13 already mapped), part of the dysregulated type-2 immunity."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 gut depletion: IL-23 sustains the Th17 (IL-17 already mapped) cells whose preferential gut-mucosal depletion contributes to the microbial translocation and immune activation of AIDS."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Hypergammaglobulinaemia: the plasma cells, from the polyclonal B-cell (BAFF already mapped) activation, secrete the excess immunoglobulin (already mapped) and the elevated IgE (already mapped) of AIDS."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Type-2 dysregulation: the mast cells, armed by the elevated IgE (already mapped), reflect the type-2 immune dysregulation and the allergic manifestations of the immunodeficiency of AIDS."
---

# HIV/AIDS

## Overview

Human Immunodeficiency Virus (HIV-1) is a **lentivirus** (genus *Lentivirus*, family *Retroviridae*) first isolated by Barré-Sinoussi and colleagues in 1983 [^barre-sinoussi-1983-hiv]. HIV-1 and the related HIV-2 (less virulent, West Africa) cause **acquired immunodeficiency syndrome (AIDS)** by progressively depleting CD4⁺ T helper cells until cell-mediated immunity collapses, leaving the host vulnerable to AIDS-defining opportunistic infections and malignancies.

**Global burden (2023):**
- ~39 million people living with HIV (PLHIV) globally
- ~1.3 million new infections per year
- ~630,000 AIDS-related deaths per year (down from 2M/year peak in 2004)
- Sub-Saharan Africa carries ~65% of global HIV burden
- ~29.8 million PLHIV on antiretroviral therapy (ART)

**Transformative paradigm: U=U (Undetectable = Untransmittable)**

HIV-positive individuals with sustained undetectable viral load on ART pose **zero risk** of sexual HIV transmission to HIV-negative partners (PARTNER, Opposites Attract, HPTN 052 studies). This scientific finding has transformed HIV prevention and destigmatisation.

**Epidemiology:**
- Transmission: sexual (most common globally: vaginal and anal intercourse); mother-to-child (pregnancy, delivery, breastfeeding); blood (injecting drug use, transfusion, needlestick)
- Anal sex carries ~18× higher per-act transmission risk than vaginal sex
- Primary risk co-factors: other STIs (especially HSV-2, ulcerative STIs disrupt mucosal barrier), high viral load in the source partner, acute/early HIV infection (peak viremia), lack of male circumcision

## Structure

### HIV-1 Virion and Genome

The **HIV-1 virion** (~120 nm spherical particle) is enveloped and architecturally complex:

| Component | Structure | Function |
|:----------|:----------|:---------|
| **Envelope (Env)** | gp120/gp41 trimeric spikes (~72 per virion); gp120 = surface; gp41 = transmembrane | CD4 binding (gp120); membrane fusion (gp41 heptad repeats) |
| **Matrix (MA/p17)** | Beneath lipid bilayer | Structural integrity; mediates nuclear import of PIC |
| **Capsid (CA/p24)** | Fullerene cone; ~1,200 CA monomers | Protects viral RNA; interacts with host restriction factors (TRIM5α, cyclophilin A) |
| **Nucleocapsid (NC/p7)** | Zinc-finger protein, coats viral RNA | RNA packaging, reverse transcription chaperone |
| **Genome** | Two copies of (+)ssRNA; 9.8 kb; 9 genes | Genetic blueprint; dimerises via dimerisation initiation site (DIS) |
| **Enzymes** | Reverse transcriptase (RT), integrase (IN), protease (PR) | Replication, integration, polyprotein processing |

**HIV-1 genome organisation:**
- **Structural genes:** *gag* (MA/CA/NC/p6), *pol* (PR/RT/IN), *env* (gp120/gp41)
- **Regulatory:** *tat* (transcriptional transactivator, HIV-LTR → 100× transcription boost), *rev* (nuclear export of unspliced mRNAs via RRE)
- **Accessory:** *vif* (degrades APOBEC3G restriction), *vpr* (G2 arrest, nuclear import), *vpu* (CD4 degradation, BST-2/tetherin antagonism), *nef* (CD4/MHC-I downregulation, virion infectivity)

### HIV-1 Clades

HIV-1 is divided into four groups (M, N, O, P), with Group M comprising >90% of global infections. Group M subtype B (Europe, Americas, Australia) is the most studied in clinical research; subtype C (sub-Saharan Africa, India) accounts for ~50% of global infections.

## Function

### HIV-1 Replication Cycle

1. **Attachment and entry:** gp120 binds CD4 (Kd ~4 nM) → conformational change exposes V3 loop → V3 + bridging sheet contact CCR5 (or CXCR4) → gp41 hairpin refolding → six-helix bundle → membrane fusion → capsid released into cytoplasm
2. **Reverse transcription:** RT converts (+)ssRNA → dsDNA (via RNA:DNA hybrid intermediate); RNA strand degraded by RT RNase H domain → ss(-) DNA → complementary (+) strand synthesis → blunt-ended linear dsDNA (10.0 kb)
3. **Nuclear import:** Pre-integration complex (PIC: dsDNA + MA + IN + LEDGF/p75) enters nucleus via nuclear pore; LEDGF/p75 tethers PIC to chromatin
4. **Integration:** IN catalyses strand transfer → HIV-1 proviral DNA inserted into host genome (preferentially in active transcription units); INSTI drugs (raltegravir, elvitegravir, dolutegravir, bictegravir) block integration
5. **Transcription:** HIV-LTR → Pol II → early spliced mRNAs (*tat*, *rev*, *nef*); Tat → P-TEFb (CDK9/cyclinT1) → phosphorylates RNA Pol II → full-length genomic RNA; Rev → nuclear export of unspliced gRNA and partially spliced mRNAs
6. **Assembly:** Gag and GagPol polyproteins bud at plasma membrane; MA targets Env (gp41) into budding sites
7. **Budding:** ESCRT pathway (TSG101, ALIX) mediates membrane scission → immature virion released
8. **Maturation:** PR cleaves Gag/GagPol polyproteins → capsid condensation → infectious virion; PI drugs block PR

### CD4⁺ T Cell Depletion

HIV-1 pathogenesis is primarily driven by CD4⁺ T cell loss:
- **Direct killing:** Viral cytopathic effect (accumulation of unintegrated viral DNA; apoptosis via Env/CD4 signalling)
- **Bystander killing:** HIV-infected macrophages and DCs kill uninfected CD4⁺ T cells via pyroptosis (cGAS-STING sensing of abortive viral DNA → IL-1β → CD4 T cell death — the dominant mechanism in lymph nodes)
- **Immune activation:** Translocated gut microbial products (LPS) drive chronic immune activation → T cell exhaustion → functional CD4 depletion exceeding absolute depletion

**CD4 count and clinical correlates:**
| CD4 Count | Immune Status | Risks |
|:----------|:-------------|:------|
| >500/μL | Normal range | HIV replication; mild immune impairment |
| 200–500/μL | Mild-moderate | Recurrent bacterial infections; oral thrush; herpes zoster |
| <200/μL | AIDS | *Pneumocystis jirovecii* pneumonia (PCP), CMV retinitis, toxoplasmosis |
| <100/μL | Severe AIDS | Cryptococcal meningitis, MAC (Mycobacterium avium complex) |
| <50/μL | Profound AIDS | CMV colitis, progressive multifocal leukoencephalopathy (PML) |

## Pathology

### Antiretroviral Therapy (ART)

**Six classes of approved antiretroviral drugs** [^dhhs-2024-hiv-guidelines]:

| Class | Mechanism | Key Drugs | Resistance Pathway |
|:------|:----------|:---------|:-------------------|
| **NRTI** (nucleoside RT inhibitors) | Compete with natural dNTPs → chain termination | Tenofovir (TDF/TAF), emtricitabine (FTC), abacavir (ABC), lamivudine (3TC), zidovudine (AZT) | M184V (3TC/FTC resistance); K65R (TDF); TAMs (thymidine analogue mutations) |
| **NNRTI** (non-nucleoside RT inhibitors) | Allosteric RT inhibition (palm subdomain) | Efavirenz, rilpivirine, doravirine, etravirine | K103N (efavirenz); E138K (rilpivirine) |
| **PI** (protease inhibitors) | Block GagPol polyprotein cleavage | Darunavir/r (boosted), atazanavir/r | Complex patterns; boosting with RTV/COBI prevents resistance |
| **INSTI** (integrase strand transfer inhibitors) | Block HIV-1 integrase strand transfer step | Dolutegravir (DTG), bictegravir (BIC), raltegravir, elvitegravir/c | N155H, Q148H (RAL/EVG); DTG/BIC has higher barrier to resistance |
| **Fusion inhibitor** | Block gp41-mediated membrane fusion | Enfuvirtide (T-20) | gp41 HR1 mutations; injectable only; rarely used |
| **CCR5 antagonist** | Block gp120/CCR5 co-receptor binding | Maraviroc | Tropism switch to X4; requires pre-treatment tropism assay |
| **CD4-attachment inhibitor** | Block gp120/CD4 primary receptor | Fostemsavir (prodrug of temsavir) | gp120 BMS pocket mutations |
| **Capsid inhibitor** | Block capsid-mediated nuclear import + assembly | Lenacapavir | Capsid mutations; injectable every 6 months |

**Preferred initial regimens (DHHS 2024):**
- **BIC/TAF/FTC** (Biktarvy): Single-pill once-daily; high barrier to resistance; most prescribed globally
- **DTG/ABC/3TC** (Triumeq): HLA-B*5701 test required before ABC (hypersensitivity)
- **DTG + TAF/FTC** (separate): Alternative

**Goal:** Viral load <20–50 copies/mL within 24 weeks; CD4 count recovery (~100–150 cells/μL per year).

### HIV Prevention

- **PrEP (Pre-Exposure Prophylaxis):** Daily TDF/FTC (Truvada) or TAF/FTC (Descovy) reduces HIV acquisition by >99% in adherent MSM (iPrEX trial); daily oral PrEP widely recommended; **cabotegravir LA** (Apretude; long-acting injectable cabotegravir every 8 weeks) demonstrated superiority to daily oral TDF/FTC (HPTN 083/084)
- **PEP (Post-Exposure Prophylaxis):** Within 72 hours of exposure; 28-day course TDF/FTC + DTG; ~80% effective
- **Male circumcision:** 60% reduction in female-to-male HIV transmission (VMMC — voluntary medical male circumcision)
- **PMTCT (Prevention of Mother-to-Child Transmission):** ART during pregnancy + intrapartum + infant NVP → <1% MTCT rate (from ~45% without intervention)

### HIV Cure Strategies

- **Functional cure:** Durable viral suppression without ART (achieved in >10 individuals after HSCT from CCR5-Δ32 donors — "Berlin/London/Düsseldorf/City of Hope/Geneva/New York patients")
- **Shock-and-kill (latency reversal):** LRAs (latency-reversing agents: IL-15, HDAC inhibitors, TLR7 agonists) to reactivate latent reservoir → ART + immune clearance → clinical trials ongoing; limited efficacy to date
- **Gene editing:** CCR5 knockout of CD4⁺ T cells and HSCs (ZFN, CRISPR-Cas9) — Phase I/II trials (SB-728, Excision BioTherapeutics); not yet approved

## Connections

- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — HIV-1 gp120 binds CD4 then CCR5 (R5-tropic) or CXCR4 (X4-tropic) as co-receptor for membrane fusion; CCR5-Δ32 homozygosity confers near-complete HIV-1 resistance; maraviroc blocks CCR5; HSCT from Δ32 donors has achieved functional HIV cure.
- `connects-to` → **[Tuberculosis](../tuberculosis/README.md)** — TB is the leading AIDS-defining cause of death; HIV depletes CD4⁺ Th1 cells → granuloma destabilisation → TB reactivation; HIV-TB co-infection requires simultaneous ART + HRZE; IRIS (immune reconstitution inflammatory syndrome) complicates early ART in TB-HIV; WHO recommends ART regardless of CD4 count in TB-HIV co-infection.
- `connects-to` → **[Immune System](../immune-system/README.md)** — HIV-1 systematically destroys CD4⁺ T helper cells (primary reservoir) and impairs DC antigen presentation, NK cytotoxicity, and B cell memory; AIDS is defined by CD4 <200 cells/μL or AIDS-defining illness; chronic immune activation persists despite ART (residual inflammation, T cell exhaustion, monocyte dysregulation).
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — HIV drives ACD through sustained immune activation → IL-6 + IFN-γ → hepcidin elevation; AZT-related bone marrow suppression adds a direct aplastic component; anemia severity tracks viral load and CD4 count; ART suppression improves ACD within months.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — IL-12/IFN-γ axis is profoundly impaired in HIV-AIDS: CD4⁺ Th1 depletion → ↓IFN-γ; HIV-infected DCs produce less IL-12; the resulting Th1 deficiency explains susceptibility to TB, NTM, Leishmania, and dimorphic fungi; ART partially restores IL-12 pathway function.
- `connects-to` → **[Leishmaniasis](../leishmaniasis/README.md)** — HIV-VL co-infection: CD4+ Th1 cell depletion → loss of IFN-γ → Leishmania escapes macrophage control → disseminated VL; Mediterranean Europe, East Africa, and Indian subcontinent are co-endemic zones; ART partially restores anti-Leishmania Th1 immunity; L-AmB prophylaxis needed.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — AIDS is defined by the loss of CD4+ T helper cells: as HIV drives their count below 200/μL, cell-mediated immunity collapses, opening the door to the opportunistic infections and cancers that define the syndrome; ART restores ~100-150 cells/μL per year.
- `connects-to` → **[Pneumocystis jirovecii](../../../02-pathogen/03-fungi/pneumocystis-jirovecii/README.md)** — Pneumocystis jirovecii pneumonia (PCP) is the classic AIDS-defining infection, striking once CD4 falls below 200/μL: this fungus causes a diffuse interstitial pneumonia, treated and prevented with trimethoprim-sulfamethoxazole — prophylaxis started at that CD4 threshold.
- `connects-to` → **[Primary CNS Lymphoma](../pcnsl/README.md)** — Primary CNS lymphoma is an AIDS-defining malignancy of profound immunosuppression (CD4 <50/μL): unchecked Epstein-Barr virus drives a brain B-cell lymphoma, and restoring immunity with ART is central to treatment alongside methotrexate or radiation.
- `connects-to` → **[Human Immunodeficiency Virus type 1](../../../02-pathogen/01-viruses/hiv-1/README.md)** — AIDS is the late stage of HIV-1 infection: years of unchecked viral replication deplete CD4 T cells below ~200/µL, collapsing cell-mediated immunity and opening the door to opportunistic infections and cancers; antiretroviral therapy suppressing HIV-1 prevents and can reverse it.
- `connects-to` → **[Cervical Cancer](../cervical-cancer/README.md)** — Cervical cancer is an AIDS-defining illness: HIV-driven immunosuppression lets oncogenic HPV persist and progress faster to invasive cancer, so women with HIV face markedly higher risk; antiretroviral therapy and HPV vaccination plus screening are key preventive measures.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — AIDS reflects the collapse of T-cell immunity: as CD4 helper cells fall, CD8+ cytotoxic T cells lose the help they need and become exhausted, so cell-mediated control of viruses, intracellular bacteria and tumors fails—explaining the opportunistic infections that define AIDS.
- `connects-to` → **[HIV](../hiv/README.md)** — HIV/AIDS is the disease end of HIV infection: as the retrovirus depletes CD4 T cells, defenses collapse and AIDS-defining opportunistic infections and cancers appear—so the pathogen and the syndrome name one continuum, now arrested early by antiretroviral therapy.
- `connects-to` → **[Burkitt Lymphoma](../burkitt-lymphoma/README.md)** — Burkitt lymphoma is an AIDS-defining cancer: HIV-driven immune dysregulation and chronic B-cell activation, often with EBV co-infection, raise Burkitt risk even at preserved CD4 counts—so a fast-growing lymphoma in an HIV patient is Burkitt until proven otherwise.
- `connects-to` → **[Hepatitis B](../hepatitis-b/README.md)** — HIV and hepatitis B frequently coinfect via shared blood and sexual routes: HIV accelerates HBV liver fibrosis, and several antiretrovirals (tenofovir, lamivudine) suppress both viruses—so HIV regimens are chosen to cover HBV and avoid flares if stopped.
- `connects-to` → **[Hodgkin Lymphoma](../hodgkin-lymphoma/README.md)** — Hodgkin lymphoma is more common in HIV/AIDS though not AIDS-defining: even on antiretrovirals, HIV patients have several-fold higher Hodgkin risk, usually EBV-driven—a malignancy whose rate, unlike AIDS-defining lymphomas, did not fall with treatment.
- `connects-to` → **[Diffuse Large B-Cell Lymphoma](../dlbcl/README.md)** — Diffuse large B-cell lymphoma is the commonest AIDS-defining lymphoma: profound immunosuppression and EBV co-infection let B cells proliferate unchecked, so DLBCL marks advanced HIV—rates dropped sharply with antiretroviral immune restoration.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages are a key HIV reservoir and disease driver: unlike CD4 T cells, infected macrophages resist HIV's cytopathic effect and survive, seeding tissues (including the brain) with virus that persists despite antiretrovirals—a major obstacle to cure.
- `connects-to` → **[Candida albicans](../../../02-pathogen/03-fungi/candida-albicans/README.md)** — Oral and esophageal candidiasis is a hallmark of advancing HIV/AIDS: as CD4 counts fall, Candida albicans overgrows mucosa it normally cannot, so thrush and esophagitis are clinical clues to immunosuppression and an AIDS-defining illness when esophageal.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — HIV/AIDS frequently strikes the nervous system: beyond direct HIV brain infection causing dementia, falling CD4 counts open the door to CNS opportunists—toxoplasmosis, cryptococcal meningitis and CNS lymphoma—making neurologic disease a major source of AIDS morbidity.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — HIV/AIDS plays out largely in the lymphatic system: lymphoid tissue is where the virus replicates and where CD4 T cells are depleted, generalized lymphadenopathy is an early sign, and the resulting immune collapse drives the lymphomas that complicate AIDS.
- `connects-to` → **[Cryptococcus neoformans](../../../02-pathogen/03-fungi/cryptococcus-neoformans/README.md)** — Cryptococcus is a leading AIDS killer: when CD4 counts fall, this environmental yeast causes cryptococcal meningitis, a major cause of death in advanced HIV worldwide—so a positive serum cryptococcal antigen prompts urgent antifungal treatment.
- `connects-to` → **[Toxoplasma gondii](../../../02-pathogen/04-parasites/toxoplasma-gondii/README.md)** — Toxoplasma reactivates in AIDS as brain abscesses: latent cysts flare when CD4 counts drop, producing ring-enhancing lesions and toxoplasmic encephalitis—so seropositive patients take prophylaxis, the same drugs treating Pneumocystis.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — AIDS turns the brain into a battleground: falling immunity invites toxoplasmosis, cryptococcal meningitis, PCNSL, and PML, while HIV itself causes dementia—so new neurological signs in advanced HIV demand urgent imaging and workup.
- `connects-to` → **[Epstein-Barr Virus](../../../02-pathogen/01-viruses/epstein-barr-virus/README.md)** — AIDS unleashes Epstein-Barr-driven lymphomas: with CD4 cells gone, EBV escapes immune control to cause primary CNS lymphoma, Burkitt, Hodgkin and DLBCL—the EBV-linked cancers that define advanced HIV.
- `connects-to` → **[HPV-16](../../../02-pathogen/01-viruses/hpv-16/README.md)** — HIV lets oncogenic HPV run wild: immunosuppression reactivates HPV-16, driving the cervical and anal cancers that are AIDS-defining—so HPV vaccination and cancer screening are essential in HIV care.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — HIV exploits dendritic cells to spread: these antigen-presenting cells capture the virus at mucosal surfaces and ferry it to lymph nodes, handing it to the CD4 T cells it destroys—turning a sentinel of immunity into a vehicle for infection.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — The lung is the classic stage for AIDS: as CD4 cells vanish, Pneumocystis pneumonia and other lung infections take hold, so a previously rare fungal pneumonia became the alarm that first announced the AIDS epidemic.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — AIDS often shows itself in the gut: with immunity gone, infections like cryptosporidium and CMV inflame the intestine, causing the relentless diarrhea and wasting—'slim disease'—that mark advanced untreated infection.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — AIDS cripples B cells even as it spares them from direct infection: lost CD4 help leaves antibody responses disorganized, raising risk of bacterial infections, while chronic stimulation drives the B-cell lymphomas that define late disease.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — AIDS suffocates through Pneumocystis: as immunity collapses, this fungal pneumonia (PCP) fills the lungs and starves the blood of oxygen, the AIDS-defining infection whose silent, worsening hypoxia is a classic warning sign.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — AIDS can blind through the eye: when CD4 counts crash, cytomegalovirus attacks the retina (CMV retinitis), an AIDS-defining infection that destroys sight unless immunity is restored.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — AIDS turns endothelial cells cancerous: the herpesvirus KSHV infects these vessel-lining cells and, with immunity gone, transforms them into Kaposi sarcoma, the purple vascular tumor that became the face of the epidemic.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Imaging is central to AIDS care: chest X-ray photons reveal the diffuse infiltrates of PCP pneumonia, and brain CT or MRI distinguishes the ring-enhancing lesions of toxoplasmosis from CNS lymphoma.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — In AIDS the bone marrow becomes a battleground: disseminated infections like MAC and histoplasmosis invade it while HIV and drugs suppress it, deepening the cytopenias of advanced disease.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — AIDS often shows first on the skin: severe shingles, stubborn fungal and seborrheic rashes, and oral thrush are common early warnings that immunity is failing.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy names AIDS's opportunists: the foamy cysts of Pneumocystis, the owl-eye inclusions of CMV, and viral particles in tumors come into focus, letting the diagnostic beam catch the infections that exploit a collapsed immune system.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — AIDS scars the kidney directly: HIV-associated nephropathy, a collapsing form of focal glomerulosclerosis, drives heavy protein loss and rapid renal failure, especially before antiretroviral therapy takes hold.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Advanced AIDS weakens the heart: chronic infection and direct viral injury can dilate it into an HIV cardiomyopathy, and pericardial effusions from opportunistic infections add to the cardiac toll.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — AIDS is diagnosed by antibody yet defined by immune failure: the anti-HIV antibody test identifies infection, but as CD4 cells vanish the body's whole antibody response falters, leaving even vaccines and routine defenses ineffective.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — AIDS reaches deep into the brain: the virus and its opportunistic invaders — toxoplasma, JC virus's PML, CMV — injure neurons into HIV-associated dementia, the cognitive decline that marks advanced disease.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — HIV thins the platelets: an immune thrombocytopenia is common and can be an early sign, as antibodies and direct marrow infection drop the platelet count, sometimes improving once antiretroviral therapy begins.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — The nerves ache in advanced HIV: a distal sensory polyneuropathy from the virus itself and from older antiretrovirals brings burning, numb feet, one of the most common and disabling neurological complications.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — The epidemic turns on reproduction and prevention: HIV spreads sexually and from mother to child, but treatment-as-prevention (undetectable = untransmittable) and PrEP now block both routes, reshaping its spread.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — Adrenal failure stalks advanced disease: CMV adrenalitis and other opportunistic invaders, plus the virus itself, impair cortisol production, making adrenal insufficiency a treatable cause of the wasting and collapse of late AIDS.
- `connects-to` → **[Mycobacterium tuberculosis](../../../02-pathogen/02-bacteria/mycobacterium-tuberculosis/README.md)** — Tuberculosis is the great killer of AIDS: the failing CD4 defense lets Mycobacterium tuberculosis reactivate and spread, making TB the leading cause of death in people with HIV worldwide.
- `connects-to` → **[Malaria](../malaria/README.md)** — HIV and malaria amplify each other: the immune deficit makes malaria more frequent and severe, especially in pregnancy, while acute malaria transiently raises HIV viral load across their co-endemic regions.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Innate defense falters too: natural killer cells fall in number and function in advanced HIV, weakening the early control of viruses and tumors that lets opportunistic infections and AIDS cancers take hold.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — The gut is ground zero: HIV depletes the mucosal CD4 and Th17 cells early, breaching the gut barrier so microbial products leak into the blood — a microbial translocation that drives the chronic immune activation behind AIDS progression.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — The virus and its drugs strain the kidney: HIV-associated nephropathy plus the toxicity of some antiretrovirals make chronic kidney disease a common comorbidity, especially in untreated or African-ancestry patients.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — Survival exposes a new killer: with opportunistic infections controlled, the chronic inflammation of treated HIV accelerates atherosclerosis, making cardiovascular disease a leading cause of death in the aging AIDS-era population.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — The virus wires itself to the host's master switch: HIV's LTR carries NF-κB binding sites, so the very pathway that activates T cells also drives proviral transcription — a link that ties immune activation to viral reactivation from latency.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — It hijacks JAK-STAT to persist: HIV manipulates STAT3 signaling in infected cells, contributing to the chronic immune activation and reservoir maintenance that smolder even under effective therapy.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Collapsed immunity ends in overwhelming infection: in advanced AIDS, opportunistic and bacterial infections readily disseminate into sepsis, a common terminal event when CD4 counts fall and defenses fail.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Profound immune loss opens the lung to mold: in advanced AIDS, especially with neutropenia or steroids, invasive pulmonary aspergillosis joins the opportunistic infections that exploit the collapsed defenses.
- `connects-to` → **[Stroke](../stroke/README.md)** — The virus inflames the arteries: HIV drives an accelerated atherosclerosis and a direct vasculopathy, and with chronic immune activation even treated patients carry a raised long-term risk of ischemic stroke.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Virus and therapy both thin the bone: chronic HIV inflammation plus antiretrovirals — tenofovir disoproxil especially — accelerate bone loss, giving people with HIV high rates of osteoporosis and fracture.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — It attacks the peripheral nerves: advanced HIV causes a distal sensory polyneuropathy, and older antiretrovirals compounded it, producing the chronic burning foot pain common in long-standing infection.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — The virus can weaken the heart muscle: HIV-associated cardiomyopathy from direct viral effects, chronic inflammation and opportunistic infection remains a cause of heart failure even in the antiretroviral era.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — It burdens the mind directly and through stigma: HIV causes depression via neuroinflammation and CNS infection, compounded by the chronic illness, isolation and stigma of living with the disease.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — AIDS wastes and infects the gut: advanced HIV brings the wasting syndrome and opportunistic GI infections — CMV colitis, cryptosporidiosis and oesophageal candidiasis — causing intractable diarrhoea and malnutrition.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — The skin reveals advancing immunodeficiency: AIDS brings Kaposi sarcoma, disseminated herpes and zoster, severe seborrhoeic dermatitis and eosinophilic folliculitis, often the visible markers of progression.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — An advanced, stigmatised illness breeds worry: the opportunistic-infection risk, disclosure fears and uncertainty of AIDS foster chronic health anxiety alongside its well-recognised depression.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — The lungs define many AIDS illnesses: Pneumocystis pneumonia, tuberculosis and pulmonary Kaposi sarcoma are AIDS-defining lung diseases that emerge as CD4 counts fall.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It wastes and weakens the frame: HIV myopathy, profound AIDS wasting and avascular necrosis of bone erode the musculoskeletal system in advanced disease.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Advanced infection derails hormones: AIDS wasting syndrome, adrenal insufficiency from disseminated CMV or mycobacterial infection, and hypogonadism reflect endocrine collapse in late disease.
- `connects-to` → **[Renal System](../renal-system/README.md)** — HIV attacks the kidney directly: HIV-associated nephropathy, a collapsing FSGS, plus tenofovir tubular toxicity and immune-complex disease drive chronic kidney failure.
- `connects-to` → **[Herpesvirus](../../../02-pathogen/01-viruses/herpesvirus/README.md)** — AIDS reactivates the herpes family: CMV causes sight-threatening retinitis and colitis, HHV-8 drives Kaposi sarcoma, and severe mucocutaneous herpes-simplex marks deep immunodeficiency.
- `connects-to` → **[Varicella-zoster virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — Shingles flags failing immunity: multidermatomal or recurrent herpes-zoster is an early marker of HIV-related immune decline and can disseminate in advanced AIDS.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — The virus injures the brain through them: HIV-infected microglia and macrophages release neurotoxins driving HIV encephalitis and the cognitive decline of HIV-associated neurocognitive disorder.
- `connects-to` → **[Dietary Zinc](../../../03-medicine/03-food/zinc-dietary/README.md)** — Wasting depletes key nutrients: zinc deficiency is common in advanced HIV and contributes to immune dysfunction, with supplementation studied to support immunity in the malnourished.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — Smouldering inflammation persists despite treatment: chronically raised IL-6 from residual immune activation drives the cardiovascular disease, frailty and other comorbidities seen in treated HIV.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — AIDS-defining cancers need chemo: Kaposi sarcoma and the aggressive non-Hodgkin lymphomas that define AIDS are treated with chemotherapy alongside antiretrovirals, with immune reconstitution itself improving tumour control.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Immunotherapy enters HIV oncology: checkpoint inhibitors treat HIV-associated lung cancer and Kaposi sarcoma, and by reversing T-cell exhaustion are studied as part of cure strategies to flush the latent reservoir.
- `connects-to` → **[Axonal Transport](../../05-tissue/axonal-transport/README.md)** — It degenerates the long nerves: HIV and some antiretrovirals cause a distal sensory polyneuropathy, a dying-back axonopathy of impaired axonal transport producing painful, length-dependent neuropathy.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — It dismantles the lymph node: HIV destroys the follicular dendritic networks and germinal centres where antibody responses mature, so humoral immunity decays even as the virus hides in this reservoir.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — HIV-associated nephropathy: HIV injures glomerular cells to cause a collapsing focal segmental glomerulosclerosis, classically in people of African ancestry, a leading cause of kidney failure in untreated AIDS.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Treated HIV still inflames arteries: persistent immune activation and antiretroviral metabolic effects accelerate atherosclerosis, making cardiovascular disease a leading cause of death in the ART era.
- `connects-to` → **[Hepatitis C](../hepatitis-c/README.md)** — Shared routes, dual infection: HIV and hepatitis C share blood-borne and sexual transmission, and HIV accelerates HCV liver fibrosis, so co-infection is common and worsens both diseases.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Immunodeficiency meets a pandemic: advanced, untreated HIV raises the risk of severe COVID-19 and prolonged viral shedding, while blunting the antibody response to vaccination.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — HIV and the heart muscle: chronic immune activation in HIV/AIDS causes a dilated cardiomyopathy of the myocardium and accelerates heart failure, persisting as a cardiovascular burden despite ART.
- `connects-to` → **[Cytokine Storm](../cytokine-storm/README.md)** — Immune reconstitution storm: starting ART in advanced AIDS can unleash IRIS, a paradoxical inflammatory surge against unmasked opportunistic infections as the recovering immune system overreacts.
- `connects-to` → **[Immune Thrombocytopenia](../immune-thrombocytopenia/README.md)** — HIV-associated low platelets: HIV is a classic secondary cause of immune thrombocytopenia, driving antibody-mediated platelet destruction that often improves once ART controls the virus.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Pneumocystis fills the lung: PJP, the AIDS-defining pneumonia, packs the alveoli with foamy exudate and causes the hypoxic respiratory failure that long defined advanced HIV.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Failing cytotoxicity: CD8 cytotoxic T cells kill HIV-infected cells with perforin, but as the disease advances toward AIDS this response becomes exhausted and the virus escapes control.
- `connects-to` → **[Type I Interferon](../../03-molecular/type-i-interferon/README.md)** — Chronic interferon: persistent type-I interferon signalling in untreated HIV paradoxically drives immune exhaustion and activation rather than clearing the virus, contributing to progression to AIDS.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Wasting and activation: TNF-α from the chronic immune activation of advanced HIV drives the cachexia, fever and systemic inflammation that mark the AIDS-defining state.
- `connects-to` → **[IFN-γ](../../03-molecular/ifn-gamma/README.md)** — Collapse of Th1 defence: loss of CD4 T helper cells cripples IFN-γ-dependent macrophage activation, removing the control of intracellular pathogens and opening the door to the opportunistic infections that define AIDS.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Pyroptotic depletion: abortive HIV infection of resting CD4 cells triggers inflammasome-driven caspase-1 pyroptosis, the dominant mechanism of CD4 T-cell loss driving progression to AIDS.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — DNA sensing of the virus: cGAS-STING detection of HIV reverse-transcription intermediates fuels the chronic type-I-interferon response and immune activation that accelerate immune exhaustion in AIDS.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — Emergence of CXCR4-using (X4) HIV, whose ligand is CXCL12, marks advanced infection and accelerates the CD4 collapse that ushers in the AIDS-defining stage with its opportunistic infections.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Profound PD-1-marked T-cell exhaustion in AIDS leaves the few remaining T cells unable to control HIV or opportunistic pathogens, the functional endpoint of the immune collapse that defines the syndrome.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — The destruction of CD4 T cells in AIDS dismantles MHC-class-II-restricted T-helper responses, removing the help that B cells and CD8 cells require—the immunological core of the broad immunodeficiency.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — HIV destroys CD4 T cells both by caspase-3 apoptosis of infected cells and by abortive-infection-triggered inflammatory death of bystander cells, the depletion that drives the progression to AIDS-defining immunodeficiency.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Loss of CD4 T cells in AIDS removes a major source of IL-2 needed to sustain T-cell proliferation and survival, deepening the lymphopenia in a self-reinforcing failure of the adaptive immune compartment.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — The IL-10-skewed, exhausted immune state of advanced AIDS suppresses the residual cellular immunity, helping explain the susceptibility to the opportunistic infections that define the syndrome.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — Leakage of microbial products across the damaged gut epithelium in AIDS engages TLR4, driving the chronic immune activation that accelerates CD4 decline and progression.
- `connects-to` → **[MAVS](../../03-molecular/mavs/README.md)** — HIV antagonizes RIG-I/MAVS antiviral signaling, contributing to the impaired innate control of the virus that permits progression to AIDS.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-β drives the collagen deposition and lymphoid-tissue fibrosis of chronic HIV that impairs immune reconstitution even on effective antiretroviral therapy.
- `connects-to` → **[HIV gp120](../../03-molecular/hiv-gp120/README.md)** — HIV gp120 binds CD4 and the CCR5 co-receptor (already mapped) to mediate entry, and its engagement of bystander cells drives the syncytia formation and CD4 depletion that define progression to AIDS.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Interferon and inflammatory-cytokine signaling through JAK-STAT (type-I IFN and STAT3 already mapped) sustains the persistent immune activation that drives AIDS progression and is a JAK-inhibitor target under study.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — HIV dysregulates the Bcl-2 family to tip infected and bystander CD4+ T cells toward apoptosis, a major mechanism of the progressive lymphocyte depletion of AIDS.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — HIV exploits PI3K-AKT signaling to promote infected-cell survival and viral persistence as immunity collapses in AIDS.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR-regulated T-cell metabolism shapes both HIV replication and the exhausted, dysfunctional immune state of AIDS.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR-MyD88 signaling driven by gut microbial translocation sustains the chronic immune activation that accelerates progression to AIDS.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 promotes HIV-1 budding and amplifies the chronic immune activation that drives progression to AIDS.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling (type-I interferon already mapped) drives the antiviral and chronic interferon response that shapes immune exhaustion in AIDS.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling is engaged during HIV replication and contributes to the activation state of infected and bystander immune cells in AIDS.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — HIV-driven PI3K-AKT-FOXO modulation (AKT already mapped) shapes the T-cell survival-versus-depletion balance underlying progression to AIDS.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α supports viral replication and the metabolic dysregulation of immune cells in advanced HIV/AIDS.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins reflect the chronic myeloid inflammatory activation and immune exhaustion of HIV/AIDS.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the T-cell survival and inflammatory signaling relevant to the immune exhaustion and reservoir persistence of HIV/AIDS.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — HIV subverts host autophagy in CD4 T cells and macrophages, contributing to the immune-cell depletion and viral persistence of HIV/AIDS.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) governs the T-cell survival pathways dysregulated in the profound immunodeficiency of HIV/AIDS.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family (LCK) kinase signaling downstream of the T-cell receptor participates in the T-cell activation and immune dysfunction of HIV/AIDS.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked immunometabolic signaling shapes the T-cell metabolism and exhaustion of HIV/AIDS.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the proviral latency and T-cell-exhaustion epigenetics of HIV/AIDS.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the mucosal and immune dysregulation of HIV/AIDS.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling and the loss of Th17 cells participate in the mucosal barrier dysfunction and opportunistic-infection susceptibility of HIV/AIDS.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the innate immune responses and immune-complex processes of HIV/AIDS.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammasome activation participates in the chronic immune activation of AIDS.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — CCL2 (MCP-1) chemokine signaling participates in the monocyte trafficking and HIV-associated neurocognitive and tissue inflammation of AIDS.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine signaling (the CD73/CD39 pathway) participates in the immunosuppression and immune exhaustion of AIDS.
- `connects-to` → **[LMP1](../../03-molecular/lmp1/README.md)** — EBV malignancies: profound immunosuppression in AIDS permits Epstein-Barr-virus-driven lymphomas including primary CNS lymphoma (already mapped), where the viral oncoprotein LMP1 drives B-cell transformation unchecked by the lost T-cell surveillance.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Wasting and lipodystrophy: AIDS wasting syndrome and antiretroviral lipodystrophy involve dysregulated leptin and adipose signalling, driving the loss of lean mass and the metabolic complications that persist even with treatment.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Advanced anaemia: anaemia deepens as HIV progresses to AIDS through marrow suppression, opportunistic infection and drug toxicity, and a low haemoglobin is a strong independent predictor of mortality.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — Polyclonal hypergammaglobulinaemia: AIDS produces high but poorly targeted IgG from dysregulated B cells (BAFF-driven), an ineffective antibody excess that coexists with failing specific immunity and raises the risk of B-cell lymphomas.
- `connects-to` → **[Secretory IgA](../../03-molecular/secretory-iga/README.md)** — Mucosal immunity loss: destruction of gut-associated lymphoid tissue in AIDS impairs secretory IgA at mucosal surfaces, weakening the barrier and contributing to the enteric opportunistic infections and HIV enteropathy that drive wasting.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Th1-to-Th2 shift: progression to AIDS is accompanied by a shift away from the protective Th1 response (IL-12/IFN-gamma already mapped) toward IL-4-driven type-2 immunity, a cytokine reorientation that tracks with immune collapse.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Anaemia of AIDS: the chronic inflammation of advanced HIV raises hepcidin to sequester iron, and with marrow suppression, opportunistic infection and drug toxicity this produces the multifactorial anaemia (haemoglobin already mapped) common in AIDS.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Metabolic paradox: advanced AIDS causes wasting, yet antiretroviral therapy and chronic immune activation disturb cholesterol handling toward an atherogenic profile, part of the metabolic and cardiovascular burden that persists on treatment.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative immune activation: the persistent immune activation of AIDS generates oxidative stress, to which xanthine oxidase contributes, and the resulting reactive oxygen species add to the tissue injury and accelerated ageing of the disease.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Selenium and mortality: selenium deficiency is common in AIDS and strongly predicts mortality, its antioxidant selenoproteins countering the oxidative immune activation (xanthine oxidase already mapped) of advanced disease.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc and progression: zinc deficiency is common in AIDS and associated with faster progression and more opportunistic infections, reflecting zinc's role in the immune function depleted by the disease.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Immune-activation eicosanoids: prostaglandins from the chronic immune activation and inflammation (IL-6, TNF and IL-1 already mapped) of AIDS modulate the immune response and contribute to the persistent tissue injury of the disease.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Multifactorial anaemia: the anaemia of chronic infection (hepcidin and haemoglobin already mapped) combines with the marrow suppression, drugs and opportunistic infections to cause the multifactorial iron-disturbed anaemia common in AIDS.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Th2 immune shift: IL-13, with IL-4 (already mapped), reflects the Th2 shift of the immune dysregulation of AIDS, part of the loss of the Th1 (IFN-γ and IL-12 already mapped) control that permits the opportunistic infections.
- `connects-to` → **[BAFF](../../03-molecular/baff/README.md)** — B-cell hyperactivation: the raised BAFF of AIDS drives the B-cell hyperactivation and the hypergammaglobulinaemia (immunoglobulin already mapped), contributing to the B-cell lymphomas (LMP1 already mapped) of the disease.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Lipodystrophy adipokine: adiponectin, with leptin (already mapped), is disturbed by the HIV lipodystrophy and the ART-associated metabolic syndrome (insulin already mapped) of AIDS.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipokine of the HIV lipodystrophy and the metabolic-inflammatory (IL-6 already mapped) milieu of AIDS.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Kaposi angiogenesis: the Kaposi sarcoma (an AIDS-defining, HHV-8-driven malignancy) is highly angiogenic (VEGF), the vascular tumour of the profound immunosuppression of AIDS.
- `connects-to` → **[Regulatory T cell](../../04-cellular/regulatory-t-cell/README.md)** — Immune dysregulation: the regulatory T cells are disproportionately altered relative to the depleted CD4 T-helper cells (already mapped), contributing to the immune dysregulation and the loss of tolerance of AIDS.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Th2 shift: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the Th2 shift of the progressive immunodeficiency of AIDS.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Elevated IgE: the polyclonal B-cell (BAFF already mapped) activation of AIDS raises the IgE (with IL-4 and IL-13 already mapped), part of the dysregulated type-2 immunity.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 gut depletion: IL-23 sustains the Th17 (IL-17 already mapped) cells whose preferential gut-mucosal depletion contributes to the microbial translocation and immune activation of AIDS.
- `connects-to` → **[Plasma cell](../../04-cellular/plasma-cell/README.md)** — Hypergammaglobulinaemia: the plasma cells, from the polyclonal B-cell (BAFF already mapped) activation, secrete the excess immunoglobulin (already mapped) and the elevated IgE (already mapped) of AIDS.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Type-2 dysregulation: the mast cells, armed by the elevated IgE (already mapped), reflect the type-2 immune dysregulation and the allergic manifestations of the immunodeficiency of AIDS.

## See Also

- [^barre-sinoussi-1983-hiv] Barré-Sinoussi F et al. Isolation of a T-lymphotropic retrovirus from a patient at risk for AIDS. *Science.* 1983;220(4599):868-871. [doi:10.1126/science.6189183](https://doi.org/10.1126/science.6189183) · [PubMed 6189183](https://pubmed.ncbi.nlm.nih.gov/6189183/)
- [^dhhs-2024-hiv-guidelines] Panel on Antiretroviral Guidelines for Adults and Adolescents. *Guidelines for the Use of Antiretroviral Agents in Adults and Adolescents with HIV.* US DHHS. 2024. [clinicalinfo.hiv.gov](https://clinicalinfo.hiv.gov/en/guidelines)
- Related entries: [ccr5](../../03-molecular/ccr5/README.md), [tuberculosis](../tuberculosis/README.md), [immune-system](../immune-system/README.md), [il-12](../../03-molecular/il-12/README.md)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
