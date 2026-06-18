---
schema: human-scale-entry/v1
id: hiv
name: HIV
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "HIV (HIV-1; lentivirus; ~10 kb ssRNA) causes AIDS by depleting CD4+ T cells; CCR5/CXCR4 co-receptor tropism; reverse transcription → proviral integration → latency; ART (NRTI/NNRTI/PI/InSTI) controls but cannot cure; ~39 million people live with HIV globally."
aliases: ["HIV", "HIV-1", "HIV-2", "human immunodeficiency virus", "AIDS", "acquired immunodeficiency syndrome", "antiretroviral therapy", "ART", "HAART", "HIV reservoir", "HIV latency", "elite controller"]
sources:
  - id: barre-sinoussi-1983-hiv-isolation
    type: peer-reviewed
    cite: "Barré-Sinoussi F, Chermann JC, Rey F, et al. Isolation of a T-lymphotropic retrovirus from a patient at risk for acquired immune deficiency syndrome (AIDS). Science. 1983;220(4599):868-871."
    doi: "10.1126/science.6189183"
    pmid: "6189183"
    url: "https://doi.org/10.1126/science.6189183"
    accessed: "2026-06-08"
  - id: ho-1995-viral-dynamics
    type: peer-reviewed
    cite: "Ho DD, Neumann AU, Perelson AS, Chen W, Leonard JM, Markowitz M. Rapid turnover of plasma virions and CD4 lymphocytes in HIV-1 infection. Nature. 1995;373(6510):123-126."
    doi: "10.1038/373123a0"
    pmid: "7816094"
    url: "https://doi.org/10.1038/373123a0"
    accessed: "2026-06-08"
  - id: siliciano-2003-hiv-latency
    type: peer-reviewed
    cite: "Siliciano JD, Kajdas J, Finzi D, et al. Long-term follow-up studies confirm the stability of the latent reservoir for HIV-1 in resting CD4+ T cells. Nat Med. 2003;9(6):727-728."
    doi: "10.1038/nm880"
    pmid: "12754504"
    url: "https://doi.org/10.1038/nm880"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/hiv-gp120
    relation: connects-to
    note: "HIV gp120 is the receptor-binding subunit of the HIV Env trimer; gp120 CD4-binding + CCR5/CXCR4 coreceptor binding drives HIV tropism and entry; gp41 six-helix bundle executes membrane fusion; Env trimer is the primary target of broadly neutralizing antibodies for vaccine design."
  - target: 01-human/03-molecular/mavs
    relation: connects-to
    note: "HIV ssRNA/dsRNA replication intermediates activate RIG-I/MDA5 → MAVS → IRF3 → IFN-β; HIV Vif degrades APOBEC3G; HIV capsid-CPSF6 nuclear pore threading evades cytosolic sensing before MAVS activation; Vpx (HIV-2) degrades SAMHD1 to enable reverse transcription in macrophages."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic HIV DNA from reverse transcription activates cGAS → cGAMP → STING → IRF3/IFN-β; HIV capsid-CPSF6 nuclear import limits cytosolic DNA exposure; TREX1 exonuclease degrades cytosolic HIV DNA to dampen cGAS; SAMHD1 blocks RT by depleting dNTP pools upstream of cGAS sensing."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "IFN-α from pDCs (TLR7/9) restricts HIV via BST-2/tetherin (HIV Vpu counteracts), APOBEC3G (HIV Vif counteracts), and IFITM3; chronic type I IFN in HIV disease drives T cell exhaustion and immune activation; IFN-λ and IFN-α coordinate innate viral control at mucosal entry sites."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "HIV-1 LTR has two κB sites; NF-κB p65/p50 drives transcription from integrated provirus; T cell activation (TCR/CD28 → IKKβ → NF-κB) reactivates latent HIV; Tat cooperates with NF-κB at LTR → high-level virion production; NF-κB inhibition explored for latency reversal."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "HIV-infected macrophages and Tregs produce TGF-β1 → CD8+ T cell suppression and NK dysfunction; TGF-β maintains latent HIV in quiescent memory CD4+ T cells; TGF-β-driven lymph node fibrosis (collagen deposition) disrupts T cell zones → progressive CD4+ T cell depletion."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "HIV is, at its core, a disease of the CD4+ T helper cell: gp120 docks on CD4, the provirus integrates, and the cell is killed by viral budding or by pyroptosis of bystanders — while a pool of resting memory CD4 cells harbours the latent reservoir that makes HIV incurable."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages are a durable HIV reservoir and a route to the brain: long-lived and resistant to the cytopathic killing that destroys T cells, they support replication (HIV-2's Vpx degrades SAMHD1 to permit reverse transcription) and seed CNS infection and neurocognitive disorder."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "CD8+ cytotoxic T cells are the main brake on HIV: in elite controllers, HLA-B*57/B*27-restricted CD8 cells kill infected cells and force viral escape, but chronic antigen and type-I interferon exhaust them over time, and they cannot reach the latent reservoir."
  - target: 02-pathogen/01-viruses/hiv-1
    relation: connects-to
    note: "HIV-1 is the retrovirus causing this infection: gp120 binds CD4 and CCR5/CXCR4 to enter helper T cells, reverse transcriptase and integrase splice the provirus into the genome, and its mutation rate plus a latent reservoir defeat cure—antiretrovirals suppress but cannot clear it."
  - target: 01-human/07-system/tuberculosis
    relation: connects-to
    note: "Tuberculosis is the leading cause of death in people with HIV: CD4 depletion cripples the Th1/macrophage granuloma that contains Mycobacterium tuberculosis, so latent TB reactivates and progresses fast; co-treatment must juggle drug interactions and immune reconstitution (IRIS)."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Lymphoid tissue is HIV's main battleground and reservoir: the virus replicates in CD4 T cells of lymph nodes and gut-associated lymphoid tissue, destroying their architecture; latent provirus persists in resting memory cells there, the key barrier to cure on suppressive therapy."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "HIV the virus and HIV/AIDS the disease are two views of one process: untreated HIV destroys CD4 T cells until immunity collapses into AIDS with opportunistic infections and cancers—antiretroviral therapy halts this, making HIV a chronic infection, not a death sentence."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "HIV exploits dendritic cells to reach its target: mucosal dendritic cells capture the virus via DC-SIGN and ferry it to lymph nodes, handing it to CD4 T cells—so the very cells meant to launch immunity instead deliver HIV to the cells it destroys."
  - target: 01-human/07-system/hepatitis-c
    relation: connects-to
    note: "HIV and hepatitis C frequently coinfect through shared blood-borne transmission: HIV accelerates HCV liver fibrosis toward cirrhosis, so coinfected patients are prioritized for direct-acting antiviral cure, which clears HCV in most regardless of HIV status."
  - target: 01-human/07-system/hepatitis-b
    relation: connects-to
    note: "HIV and hepatitis B frequently coinfect through shared transmission, and each worsens the other: HIV accelerates HBV liver disease while some antiretrovirals (tenofovir, lamivudine) treat both viruses—so HIV care includes HBV screening and dual-active therapy."
  - target: 01-human/07-system/pcnsl
    relation: connects-to
    note: "Primary CNS lymphoma is an AIDS-defining cancer of advanced HIV: profound CD4 depletion lets EBV-driven B cells proliferate unchecked in the brain, so PCNSL was common before antiretrovirals—its incidence fell sharply with immune recovery."
  - target: 01-human/07-system/hodgkin-lymphoma
    relation: connects-to
    note: "HIV raises Hodgkin lymphoma risk and changes its biology: unlike AIDS-defining lymphomas, HIV-associated Hodgkin is almost always EBV-driven and did not fall with antiretroviral therapy—a reminder that not every HIV-related cancer is reversed by immune recovery."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5 is HIV's main entry coreceptor: the virus uses it with CD4 to infect T cells, the blocker maraviroc exploits this, and people with the CCR5-delta32 deletion are naturally resistant—the basis of the only cures achieved via stem-cell transplant."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "HIV is fundamentally a disease of the immune system: by destroying CD4 T cells it collapses coordinated immunity, so opportunistic infections and cancers define AIDS—and antiretroviral therapy works by preserving this immune architecture before it fails."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "HIV invades the nervous system early: it infects brain macrophages and microglia, and even on treatment can cause HIV-associated neurocognitive disorder, so the CNS is both a target organ and a viral reservoir that complicates cure."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "HIV both cripples and is chased by B cells: chronic infection causes B-cell exhaustion and poor vaccine responses, yet rare broadly neutralizing antibodies from some patients now guide vaccine and long-acting prevention research—central to the search for a cure."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "HIV is largely a sexually transmitted infection of the reproductive tract: it spreads through genital and rectal mucosa, crosses to infants in pregnancy and breast-feeding, and is blocked by PrEP and 'undetectable = untransmittable' viral suppression."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Natural killer cells are frontline against HIV: they kill infected cells and shape early control, and certain NK-receptor (KIR) and HLA combinations track with slower progression—so innate immunity helps explain why a few 'elite controllers' suppress HIV without drugs."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "HIV crosses the placenta without prevention: mother-to-child transmission in pregnancy, birth or breastfeeding once infected many infants, but maternal antiretroviral therapy now makes transmission rare—one of HIV medicine's great successes."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "HIV hides in the brain's microglia: these long-lived cells form a viral reservoir behind the blood-brain barrier, driving HIV-associated neurocognitive disorder and frustrating cure efforts even when blood virus is suppressed."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Treated HIV smolders with IL-6-driven inflammation: even with virus suppressed, chronic immune activation raises IL-6 and inflammatory markers, accelerating heart disease, frailty and other non-AIDS conditions—the 'inflammaging' of long-term HIV."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "HIV's first great battlefield is the gut: it destroys most CD4 cells in the intestine's lymphoid tissue early, and the leaky gut that follows lets microbes translocate, fueling the chronic immune activation that persists even on treatment."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "HIV invades the brain and hides there: infected macrophages carry it across the blood-brain barrier into a sanctuary the drugs reach poorly, causing HIV-associated neurocognitive disorder and a reservoir that blocks cure."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "HIV warps the regulatory T-cell balance: it expands these immune suppressors that can damp the antiviral attack while also serving as a viral hiding place, so Tregs both blunt control of the virus and help sustain its reservoir."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "HIV can attack the kidneys: HIV-associated nephropathy, a collapsing form of glomerular scarring, spills heavy protein and can rapidly fail the kidneys, especially before treatment and in those of African ancestry."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "HIV guts the immune system at the bowel lining: within weeks it wipes out the dense CD4 T cells of the gut's GALT and breaches the epithelium, letting microbes leak through to drive the chronic immune activation that fuels disease."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "HIV is worsened by low zinc: deficiency is common in infection and impairs the immune cells already under attack, so poor zinc status is linked to faster progression and worse outcomes."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Imaging guides HIV care indirectly: CT and PET photons stage the lymphomas and opportunistic infections that strike as immunity falls, and brain MRI maps HIV's central-nervous-system disease."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "HIV harms neurons without infecting them: infected microglia release toxins that injure neurons, causing the HIV-associated neurocognitive disorder that can persist even on suppressive treatment."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "HIV suppresses the bone marrow: direct infection and chronic inflammation blunt blood-cell production, causing the anemia, low platelets and leukopenia common in untreated infection."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy first revealed HIV's shape: spherical virions studded with envelope spikes bud from the infected cell, each carrying the cone-shaped capsid core that protects the viral RNA — the structure antiviral drugs target."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "HIV is written across the skin: from the violet plaques of Kaposi sarcoma to severe seborrheic dermatitis, shingles, and stubborn fungal rashes, cutaneous signs often herald the immune collapse beneath."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Selenium drains away as HIV advances: deficiency of this antioxidant trace element is common and independently linked to faster progression and higher mortality, making it a marker of the disease's toll on nutrition and immunity."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies both diagnose and may one day defeat HIV: the standard test detects anti-HIV antibody (with p24 antigen), yet the virus mutates past most antibodies — driving the search for the broadly neutralizing antibodies that a vaccine would need to elicit."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "The treatment reshapes the body's fat: older antiretrovirals, the protease inhibitors and stavudine especially, cause lipodystrophy — fat lost from limbs and face while it piles on the trunk — alongside insulin resistance and high lipids."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "HIV and the liver are entangled: hepatitis B and C coinfection is common through shared transmission, and the lifelong antiretrovirals add their own risk of drug-induced liver injury that must be monitored."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "HIV breaches the gut to fuel itself: it destroys the intestinal CD4 cells early, and the leaky, dysbiotic gut lets microbial products translocate into the blood, driving the chronic immune activation that persists even on treatment."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "The white cells run low too: HIV and several of its drugs suppress the marrow into neutropenia, compounding the immune deficit and raising bacterial-infection risk beyond the loss of CD4 T cells."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "The adrenal is the gland HIV most often hits: CMV adrenalitis and the infection itself can blunt cortisol output, making adrenal insufficiency the commonest endocrine complication of advanced HIV."
  - target: 01-human/06-organ/thymus
    relation: connects-to
    note: "HIV cripples the organ that makes T cells: it depletes the thymus and its output of naive CD4 cells, so the gland's failing reserve limits immune reconstitution even once antiretrovirals suppress the virus."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Treated HIV ages the arteries early: chronic immune activation plus the dyslipidemia of some antiretrovirals accelerate atherosclerosis, so heart attack and stroke have become leading causes of death in the ART era."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "B-cell help fails even as antibody floods in: HIV drives a chaotic polyclonal plasma-cell activation and hypergammaglobulinemia, yet the specific, protective antibody response decays — dysregulation, not just deficiency."
  - target: 01-human/07-system/cervical-cancer
    relation: connects-to
    note: "Lost immunity lets HPV run to cancer: with CD4 surveillance gone, human papillomavirus persists and progresses, making invasive cervical cancer an AIDS-defining malignancy and a major cause of cancer death in women with HIV."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "The virus scars the kidney: HIV-associated nephropathy, a collapsing glomerulopathy driven by viral genes in kidney cells, drives chronic kidney disease, especially before treatment and in those of African ancestry with APOL1 risk variants."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Even controlled HIV ages the arteries: chronic immune activation on top of antiretroviral metabolic effects accelerates atherosclerosis, so cardiovascular disease is now a leading cause of death in the treated, aging HIV population."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: connects-to
    note: "It hands the lungs to an opportunist: as CD4 counts fall below 200, Pneumocystis jirovecii pneumonia becomes the classic AIDS-defining infection, the reason prophylaxis is started at that threshold."
  - target: 02-pathogen/04-parasites/toxoplasma-gondii
    relation: connects-to
    note: "A latent parasite reawakens in the brain: with advanced immunosuppression, Toxoplasma gondii reactivates into the ring-enhancing brain abscesses of cerebral toxoplasmosis, a leading cause of AIDS-related focal neurological disease."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "The virus exploits host signaling: HIV manipulates STAT3 and JAK-STAT pathways in infected cells to favor its persistence and the chronic immune activation that smolders even under treatment."
  - target: 02-pathogen/03-fungi/candida-albicans
    relation: connects-to
    note: "A telltale early opportunist: oral and esophageal candidiasis is one of the commonest infections as HIV erodes CD4 T-cells, often the first clinical clue to underlying immunodeficiency."
  - target: 02-pathogen/01-viruses/epstein-barr-virus
    relation: connects-to
    note: "Loss of T-cell control lets EBV drive cancer: with HIV immunosuppression, unchecked Epstein-Barr virus fuels B-cell lymphomas including primary CNS lymphoma and Burkitt and Hodgkin lymphoma."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "It burdens the mind directly and indirectly: HIV causes depression through neuroinflammation and direct CNS effects as well as the stigma, chronic illness and isolation of living with the infection."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "It inflames and ages the arteries: chronic HIV drives accelerated atherosclerosis and an HIV-associated vasculopathy, and with antiretroviral metabolic effects raises the risk of ischemic stroke."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "The virus and its drugs thin the bones: chronic HIV inflammation plus tenofovir-based antiretroviral therapy lower bone mineral density, giving people with HIV markedly higher rates of osteoporosis and fracture."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "It attacks the peripheral nerves: HIV causes a distal sensory polyneuropathy directly, and older antiretrovirals added their own neurotoxicity, producing chronic burning neuropathic pain in the feet."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "The skin flags the infection: HIV brings Kaposi sarcoma, severe seborrhoeic dermatitis, extensive herpes and zoster, eosinophilic folliculitis and antiretroviral drug rashes, often the first visible clues."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It wastes and infects the gut: HIV enteropathy and opportunistic infections cause chronic diarrhoea and wasting, with oral and oesophageal candidiasis and antiretroviral GI side effects."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A chronic, stigmatised, lifelong infection breeds worry: the diagnosis, disclosure fears, adherence demands and stigma of HIV foster chronic health anxiety alongside its well-recognised depression."
---

# HIV

## Overview

**HIV (Human Immunodeficiency Virus)** is a **lentivirus** (retrovirus family; genus *Lentivirus*) that causes progressive immune deficiency by depleting **CD4+ T cells**, ultimately resulting in **AIDS (Acquired Immune Deficiency Syndrome)** — the clinical syndrome of severe immune suppression leaving the host vulnerable to opportunistic infections and malignancies. Two major types exist: **HIV-1** (global pandemic strain; higher replication rate) and **HIV-2** (primarily West Africa; slower progression; naturally resistant to NNRTIs). HIV-1 is further divided into **groups M/N/O/P**, with group M containing the pandemic subtypes (clades A through K); subtype B predominates in North America and Europe, subtype C predominates globally (accounts for ~50% of infections).

HIV was first isolated in 1983 by Françoise Barré-Sinoussi and Luc Montagnier (Nobel Prize 2008) from a patient with AIDS-related lymphadenopathy [^barre-sinoussi-1983-hiv-isolation]. Since then, HIV has caused one of history's largest pandemics: **~84 million infections total; ~40 million AIDS-related deaths; ~39 million people currently living with HIV** (UNAIDS 2023). Sub-Saharan Africa carries ~70% of the global burden.

**The defining paradox of HIV:** HIV replicates at extraordinary rates (~10^9 new virions per day in untreated infection) but integrates into long-lived quiescent CD4+ T cells — creating a **latent reservoir** with a 44-year half-life that persists lifelong despite suppressive ART, explaining why current therapy cannot cure HIV [^siliciano-2003-hiv-latency].

## Structure

### Virion architecture

HIV virions are roughly **spherical, ~120 nm** diameter with a distinctive **conical (fullerene) capsid** made of CA (p24/capsid protein):

- **Envelope**: Lipid bilayer derived from host cell plasma membrane; **14 trimeric Env spikes** (gp120/gp41 trimers) embedded; also carries host proteins (MHC-II, ICAM-1) that aid transmission
- **Matrix (MA/p17)**: Underlies the envelope; involved in nuclear targeting; interacts with Env cytoplasmic tail
- **Conical capsid (CA/p24)**: Contains ~1,500 CA hexamers + 12 CA pentamers forming the fullerene cone; encloses the genome and enzymes; stabilized by CPSF6-NUP153 interaction during nuclear import; p24 antigen is the primary virological test marker
- **Nucleocapsid (NC/p7)**: Coats the two copies of ssRNA genome; zinc-finger motifs; facilitates reverse transcription
- **Genome**: Two copies of ~10 kb positive-sense ssRNA; structured as 5′LTR-gag-pol-env-vif-vpr-tat-rev-vpu-nef-3′LTR
- **Enzymes in capsid**: Reverse transcriptase (RT; p66/p51 heterodimer), integrase (IN/p32), protease (PR/p11 homodimer)

### Genome organization

| Gene | Product | Function |
|:---|:---|:---|
| **gag** | Pr55Gag (MA, CA, NC, SP1, SP2, p6) | Structural proteins; capsid assembly; budding |
| **pol** | PR, RT, IN | Protease (Gag/Gag-Pol processing); reverse transcriptase (RNA→DNA); integrase (provirus integration) |
| **env** | gp160 → gp120/gp41 | Receptor binding (gp120) and fusion (gp41); trimeric Env spike |
| **vif** | Vif | Degrades APOBEC3G/3F → prevents hypermutation |
| **vpr** | Vpr | Nuclear import of pre-integration complex; G2/M arrest; DCAF1/VprBP ubiquitin ligase hijacking |
| **tat** | Tat | Transactivator; binds TAR RNA loop at LTR 5′ end → recruits P-TEFb (CDK9/CycT1) → RNA Pol II pause release → viral transcription elongation |
| **rev** | Rev | Shuttles unspliced/singly-spliced viral RNA from nucleus via CRM1/exportin; essential for structural protein expression |
| **vpu** | Vpu | Degrades CD4 and BST-2/tetherin (the IFN-induced restriction factor) via BTRC/β-TrCP E3 ligase |
| **nef** | Nef | Downregulates CD4 and MHC-I; activates PAK2; enhances virion infectivity; critical for pathogenesis |

### HIV-1 vs HIV-2

| Feature | HIV-1 | HIV-2 |
|:---|:---|:---|
| Geographic distribution | Global | West Africa primarily |
| Progression to AIDS | 7-11 years (untreated) | >20 years (slower) |
| Plasma viral load | Higher | Lower |
| NNRTI susceptibility | Yes | Intrinsically resistant |
| Vpx gene | Absent | Present (degrades SAMHD1) |
| Transmission risk | Higher | 5-10× lower |

## Function

### Viral lifecycle

**Step 1 — Attachment**: gp120 binds CD4 (T cells, macrophages, DCs) → conformational change exposes co-receptor binding site → binds CCR5 (M-tropic strain; initial transmission) or CXCR4 (X4-tropic; late disease)

**Step 2 — Fusion**: gp41 hairpin formation (HR1/HR2 six-helix bundle) → viral/host membrane fusion → capsid enters cytoplasm

**Step 3 — Reverse transcription**: RT synthesizes dsDNA from ssRNA template in the cytoplasm within the reverse transcription complex (RTC); error-prone (~10^-5 per base per replication cycle) → high mutation rate → drug resistance and immune escape

**Step 4 — Nuclear import**: The pre-integration complex (PIC; intact capsid cone with dsDNA) transits through the nuclear pore via CPSF6 and NUP153; capsid disassembly occurs at the nuclear pore (uncoating coupled to nuclear entry)

**Step 5 — Integration**: Integrase catalyzes 3′-processing and strand transfer → HIV dsDNA integrates into the host genome (provirus); prefers **H3K36me3 transcriptionally active chromatin** near gene bodies; LEDGF/p75 acts as integrase cofactor for chromatin targeting

**Step 6 — Latency**: In quiescent resting memory CD4+ T cells, the provirus is transcriptionally silenced by: **chromatin compaction** (HDAC1/2 on LTR nucleosomes nuc-0 and nuc-1); **PRC2-mediated H3K27me3** at the LTR; **insufficient Tat and NF-κB**; **lack of P-TEFb** (CDK9/CycT1) → **latent reservoir**

**Step 7 — Reactivation**: T cell activation (antigen, cytokines) → NF-κB → κB sites in LTR → nascent Tat transcribed → Tat binds TAR RNA → recruits P-TEFb → CDK9 phosphorylates RNA Pol II C-terminal domain Ser2 → pause release → full-length viral transcription

**Step 8 — Assembly and budding**: Gag polyprotein traffics to plasma membrane; gp120/gp41 Env trimer incorporated via Gag-MA interaction with Env cytoplasmic tail; budding requires ESCRT machinery (TSG101, ALIX, VPS4); ~10^4 virions per cell per day in activated infected T cells

**Step 9 — Maturation**: HIV protease (activated by dimerization) cleaves Gag polyprotein (MA/CA/SP1/NC/SP2/p6) → condensed conical capsid forms; RT and IN also released and repackaged; maturation inhibitors (lenacapavir) block this step

### CD4+ T cell depletion

Three mechanisms explain progressive CD4+ T cell loss:
1. **Productive infection**: Virus production kills infected cells via caspase/apoptosis and necrosis; ~10^9 CD4+ T cells killed and replaced per day → sustainability collapses when production cannot replace loss
2. **Pyroptosis (abortive infection)**: Bystander CD4+ T cells take up incomplete HIV reverse transcripts (incomplete RT products) → cytosolic DNA → cGAS → caspase-1 → pyroptosis (inflammatory programmed death); accounts for the majority of CD4+ cell loss
3. **Immunological killing**: HIV-specific CD8+ T cells recognize infected cells; antibody-dependent cellular cytotoxicity (ADCC) by NK cells; complement-mediated lysis

### Elite controllers

Fewer than 1% of HIV-infected individuals maintain viral loads below detection (<50 copies/mL) without ART — termed **elite controllers** or **long-term non-progressors**. Mechanisms:
- **HLA-B*57:01 and HLA-B*27:05**: Present immunodominant HIV epitopes with high avidity → CD8+ T cells with broad, cross-reactive coverage → rapid viral evolution pressure
- **CD8+ T cell polyfunctionality**: Elite controllers' CD8+ T cells produce IFN-γ, TNF-α, IL-2, perforin simultaneously
- **CCR5Δ32 homozygosity**: ~1% of northern Europeans; CCR5 protein not expressed → resistant to CCR5-tropic HIV; basis for the Berlin/London patient CCR5Δ32 bone marrow transplant cure

### Latent reservoir and cure challenge

The **latent reservoir** — HIV integrated into quiescent resting memory CD4+ T cells — is established within **3 days of infection** and persists with a 44-year half-life [^siliciano-2003-hiv-latency]. Current approaches:
- **"Shock and kill"**: Latency-reversing agents (LRAs; PKC agonists, HDAC inhibitors) reactivate latent provirus → immune clearance; limited by immune exhaustion and incomplete reactivation
- **"Block and lock"**: Epigenetic silencing agents (didehydro-cortistatin A; SMYD2 inhibitors) permanently lock the latent provirus → prevent reactivation without clearing reservoir; "functional cure" concept
- **CCR5Δ32 cell therapy**: Infusion of CCR5Δ32 homozygous donor cells (Berlin and London patients cured); requires myeloablative conditioning; not scalable
- **LRA + bNAb combination**: Reactivate reservoir → clear with broadly neutralizing antibody (bNAb); clinical trials ongoing

## Pathology

### AIDS progression

| Stage | CD4+ count | Characteristics |
|:---|:---|:---|
| **Acute HIV infection** | Transient drop → recovery | Flu-like illness (2-4 wk); viremia peak ~10^7 copies/mL; CD4+ nadir; some become antibody-negative initially |
| **Chronic infection (latency)** | 350-1000/μL | Clinically silent; slow CD4+ decline ~50-100 cells/μL/year; low-level viral replication; viral set point established |
| **Symptomatic HIV** | 200-350/μL | Constitutional symptoms; oral candidiasis; herpes zoster; minor OIs; hepatosplenomegaly |
| **AIDS** | <200/μL | AIDS-defining OIs and malignancies |

### AIDS-defining conditions (selected)

- **Pneumocystis jirovecii pneumonia (PCP)**: Most common AIDS OI in ART-naive; CD4+ <200/μL; trimethoprim-sulfamethoxazole prophylaxis and treatment; high LDH, bilateral ground-glass on CT
- **CNS toxoplasmosis**: CD4+ <100/μL; ring-enhancing lesions; *Toxoplasma gondii* reactivation; sulfadiazine + pyrimethamine
- **CMV retinitis**: CD4+ <50/μL; risk of blindness; ganciclovir/valganciclovir
- **Cryptococcal meningitis**: CD4+ <100/μL; India ink-positive CSF; liposomal amphotericin B + flucytosine → fluconazole
- **Mycobacterium avium complex (MAC)**: Disseminated; CD4+ <50/μL; azithromycin prophylaxis
- **Primary CNS lymphoma (PCNSL)**: EBV-driven B cell lymphoma; CD4+ <50/μL; T1 ring enhancement; WBRT + ART
- **Kaposi sarcoma**: HHV-8 (KSHV) driven; cutaneous/visceral; purple skin lesions; responds to ART; liposomal doxorubicin for systemic disease
- **Wasting syndrome**: >10% body weight loss + chronic diarrhea or fever; multifactorial

### ART — antiretroviral therapy

| Class | Mechanism | Examples |
|:---|:---|:---|
| **NRTI** | Nucleoside RT inhibitor; chain terminators | Tenofovir (TDF/TAF), emtricitabine (FTC), abacavir, lamivudine |
| **NNRTI** | Non-nucleoside RT inhibitor; allosteric RT block | Efavirenz, rilpivirine, doravirine |
| **PI** | Protease inhibitor; prevent Gag cleavage/maturation | Darunavir/r, atazanavir/r |
| **InSTI** | Integrase strand transfer inhibitor | Dolutegravir, bictegravir, cabotegravir, raltegravir |
| **Entry inhibitor** | Blocks gp120-CD4 or CCR5 | Maraviroc (CCR5 antagonist), ibalizumab (anti-CD4) |
| **Capsid inhibitor** | Blocks capsid uncoating/assembly | Lenacapavir (LA injection every 26 weeks) |

**Standard first-line ART**: Bictegravir/tenofovir alafenamide/emtricitabine (Biktarvy) — single daily pill; >95% viral suppression at 48 weeks. With proper adherence, life expectancy approaches that of HIV-negative individuals.

**PrEP**: Tenofovir disoproxil fumarate + emtricitabine (Truvada/Descovy) → daily oral, >99% protection; cabotegravir long-acting injection every 8 weeks (HPTN 083/084 trials; superior to TDF/FTC PrEP).

## Connections

**→ [HIV gp120](../../../03-molecular/hiv-gp120/)**: HIV gp120 is the receptor-binding subunit of the HIV Env trimer; gp120 CD4-binding site + CCR5/CXCR4 co-receptor binding drives HIV tropism and entry; gp41 six-helix bundle executes membrane fusion; Env trimer is the primary target of broadly neutralizing antibodies for HIV vaccine design.

**→ [MAVS](../../../03-molecular/mavs/)**: HIV ssRNA/dsRNA replication intermediates activate RIG-I/MDA5 → MAVS → IRF3 → IFN-β; HIV Vif degrades APOBEC3G; HIV capsid-CPSF6 nuclear pore threading evades cytosolic sensing before MAVS activation; Vpx (HIV-2) degrades SAMHD1 to enable reverse transcription in macrophages.

**→ [cGAS-STING](../../../03-molecular/cgas-sting/)**: Cytosolic HIV DNA from reverse transcription activates cGAS → cGAMP → STING → IRF3/IFN-β; HIV capsid-CPSF6 nuclear import limits cytosolic DNA exposure; TREX1 exonuclease degrades cytosolic HIV DNA to dampen cGAS; SAMHD1 blocks RT by depleting dNTP pools upstream of cGAS sensing.

**→ [Type I Interferon](../../../03-molecular/type-i-interferon/)**: IFN-α from pDCs (TLR7/9) restricts HIV via BST-2/tetherin (HIV Vpu counteracts), APOBEC3G (HIV Vif counteracts), and IFITM3; chronic type I IFN in HIV disease drives T cell exhaustion and immune activation; IFN-λ and IFN-α coordinate innate viral control at mucosal entry sites.

**→ [NF-κB](../../../03-molecular/nf-kb/)**: HIV-1 LTR has two κB sites; NF-κB p65/p50 drives transcription from integrated provirus; T cell activation (TCR/CD28 → IKKβ → NF-κB) reactivates latent HIV; Tat cooperates with NF-κB at LTR → high-level virion production; NF-κB inhibition explored for latency reversal.

**→ [TGF-β](../../../03-molecular/tgf-beta/)**: HIV-infected macrophages and Tregs produce TGF-β1 → CD8+ T cell suppression and NK dysfunction; TGF-β maintains latent HIV in quiescent memory CD4+ T cells; TGF-β-driven lymph node fibrosis (collagen deposition) disrupts T cell zones → progressive CD4+ T cell depletion.

- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — HIV is, at its core, a disease of the CD4+ T helper cell: gp120 docks on CD4, the provirus integrates, and the cell is killed by viral budding or by pyroptosis of bystanders — while a pool of resting memory CD4 cells harbours the latent reservoir that makes HIV incurable.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages are a durable HIV reservoir and a route to the brain: long-lived and resistant to the cytopathic killing that destroys T cells, they support replication (HIV-2's Vpx degrades SAMHD1 to permit reverse transcription) and seed CNS infection and neurocognitive disorder.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — CD8+ cytotoxic T cells are the main brake on HIV: in elite controllers, HLA-B*57/B*27-restricted CD8 cells kill infected cells and force viral escape, but chronic antigen and type-I interferon exhaust them over time, and they cannot reach the latent reservoir.
- `connects-to` → **[Human Immunodeficiency Virus type 1](../../../02-pathogen/01-viruses/hiv-1/README.md)** — HIV-1 is the retrovirus causing this infection: gp120 binds CD4 and CCR5/CXCR4 to enter helper T cells, reverse transcriptase and integrase splice the provirus into the genome, and its mutation rate plus a latent reservoir defeat cure—antiretrovirals suppress but cannot clear it.
- `connects-to` → **[Tuberculosis](../tuberculosis/README.md)** — Tuberculosis is the leading cause of death in people with HIV: CD4 depletion cripples the Th1/macrophage granuloma that contains Mycobacterium tuberculosis, so latent TB reactivates and progresses fast; co-treatment must juggle drug interactions and immune reconstitution (IRIS).
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Lymphoid tissue is HIV's main battleground and reservoir: the virus replicates in CD4 T cells of lymph nodes and gut-associated lymphoid tissue, destroying their architecture; latent provirus persists in resting memory cells there, the key barrier to cure on suppressive therapy.
- `connects-to` → **[HIV/AIDS](../hiv-aids/README.md)** — HIV the virus and HIV/AIDS the disease are two views of one process: untreated HIV destroys CD4 T cells until immunity collapses into AIDS with opportunistic infections and cancers—antiretroviral therapy halts this, making HIV a chronic infection, not a death sentence.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — HIV exploits dendritic cells to reach its target: mucosal dendritic cells capture the virus via DC-SIGN and ferry it to lymph nodes, handing it to CD4 T cells—so the very cells meant to launch immunity instead deliver HIV to the cells it destroys.
- `connects-to` → **[Hepatitis C](../hepatitis-c/README.md)** — HIV and hepatitis C frequently coinfect through shared blood-borne transmission: HIV accelerates HCV liver fibrosis toward cirrhosis, so coinfected patients are prioritized for direct-acting antiviral cure, which clears HCV in most regardless of HIV status.
- `connects-to` → **[Hepatitis B](../hepatitis-b/README.md)** — HIV and hepatitis B frequently coinfect through shared transmission, and each worsens the other: HIV accelerates HBV liver disease while some antiretrovirals (tenofovir, lamivudine) treat both viruses—so HIV care includes HBV screening and dual-active therapy.
- `connects-to` → **[Primary CNS Lymphoma](../pcnsl/README.md)** — Primary CNS lymphoma is an AIDS-defining cancer of advanced HIV: profound CD4 depletion lets EBV-driven B cells proliferate unchecked in the brain, so PCNSL was common before antiretrovirals—its incidence fell sharply with immune recovery.
- `connects-to` → **[Hodgkin Lymphoma](../hodgkin-lymphoma/README.md)** — HIV raises Hodgkin lymphoma risk and changes its biology: unlike AIDS-defining lymphomas, HIV-associated Hodgkin is almost always EBV-driven and did not fall with antiretroviral therapy—a reminder that not every HIV-related cancer is reversed by immune recovery.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5 is HIV's main entry coreceptor: the virus uses it with CD4 to infect T cells, the blocker maraviroc exploits this, and people with the CCR5-delta32 deletion are naturally resistant—the basis of the only cures achieved via stem-cell transplant.
- `connects-to` → **[Immune System](../immune-system/README.md)** — HIV is fundamentally a disease of the immune system: by destroying CD4 T cells it collapses coordinated immunity, so opportunistic infections and cancers define AIDS—and antiretroviral therapy works by preserving this immune architecture before it fails.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — HIV invades the nervous system early: it infects brain macrophages and microglia, and even on treatment can cause HIV-associated neurocognitive disorder, so the CNS is both a target organ and a viral reservoir that complicates cure.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — HIV both cripples and is chased by B cells: chronic infection causes B-cell exhaustion and poor vaccine responses, yet rare broadly neutralizing antibodies from some patients now guide vaccine and long-acting prevention research—central to the search for a cure.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — HIV is largely a sexually transmitted infection of the reproductive tract: it spreads through genital and rectal mucosa, crosses to infants in pregnancy and breast-feeding, and is blocked by PrEP and 'undetectable = untransmittable' viral suppression.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Natural killer cells are frontline against HIV: they kill infected cells and shape early control, and certain NK-receptor (KIR) and HLA combinations track with slower progression—so innate immunity helps explain why a few 'elite controllers' suppress HIV without drugs.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — HIV crosses the placenta without prevention: mother-to-child transmission in pregnancy, birth or breastfeeding once infected many infants, but maternal antiretroviral therapy now makes transmission rare—one of HIV medicine's great successes.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — HIV hides in the brain's microglia: these long-lived cells form a viral reservoir behind the blood-brain barrier, driving HIV-associated neurocognitive disorder and frustrating cure efforts even when blood virus is suppressed.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — Treated HIV smolders with IL-6-driven inflammation: even with virus suppressed, chronic immune activation raises IL-6 and inflammatory markers, accelerating heart disease, frailty and other non-AIDS conditions—the 'inflammaging' of long-term HIV.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — HIV's first great battlefield is the gut: it destroys most CD4 cells in the intestine's lymphoid tissue early, and the leaky gut that follows lets microbes translocate, fueling the chronic immune activation that persists even on treatment.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — HIV invades the brain and hides there: infected macrophages carry it across the blood-brain barrier into a sanctuary the drugs reach poorly, causing HIV-associated neurocognitive disorder and a reservoir that blocks cure.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — HIV warps the regulatory T-cell balance: it expands these immune suppressors that can damp the antiviral attack while also serving as a viral hiding place, so Tregs both blunt control of the virus and help sustain its reservoir.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — HIV can attack the kidneys: HIV-associated nephropathy, a collapsing form of glomerular scarring, spills heavy protein and can rapidly fail the kidneys, especially before treatment and in those of African ancestry.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — HIV guts the immune system at the bowel lining: within weeks it wipes out the dense CD4 T cells of the gut's GALT and breaches the epithelium, letting microbes leak through to drive the chronic immune activation that fuels disease.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — HIV is worsened by low zinc: deficiency is common in infection and impairs the immune cells already under attack, so poor zinc status is linked to faster progression and worse outcomes.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Imaging guides HIV care indirectly: CT and PET photons stage the lymphomas and opportunistic infections that strike as immunity falls, and brain MRI maps HIV's central-nervous-system disease.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — HIV harms neurons without infecting them: infected microglia release toxins that injure neurons, causing the HIV-associated neurocognitive disorder that can persist even on suppressive treatment.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — HIV suppresses the bone marrow: direct infection and chronic inflammation blunt blood-cell production, causing the anemia, low platelets and leukopenia common in untreated infection.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy first revealed HIV's shape: spherical virions studded with envelope spikes bud from the infected cell, each carrying the cone-shaped capsid core that protects the viral RNA — the structure antiviral drugs target.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — HIV is written across the skin: from the violet plaques of Kaposi sarcoma to severe seborrheic dermatitis, shingles, and stubborn fungal rashes, cutaneous signs often herald the immune collapse beneath.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Selenium drains away as HIV advances: deficiency of this antioxidant trace element is common and independently linked to faster progression and higher mortality, making it a marker of the disease's toll on nutrition and immunity.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies both diagnose and may one day defeat HIV: the standard test detects anti-HIV antibody (with p24 antigen), yet the virus mutates past most antibodies — driving the search for the broadly neutralizing antibodies that a vaccine would need to elicit.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — The treatment reshapes the body's fat: older antiretrovirals, the protease inhibitors and stavudine especially, cause lipodystrophy — fat lost from limbs and face while it piles on the trunk — alongside insulin resistance and high lipids.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — HIV and the liver are entangled: hepatitis B and C coinfection is common through shared transmission, and the lifelong antiretrovirals add their own risk of drug-induced liver injury that must be monitored.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — HIV breaches the gut to fuel itself: it destroys the intestinal CD4 cells early, and the leaky, dysbiotic gut lets microbial products translocate into the blood, driving the chronic immune activation that persists even on treatment.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — The white cells run low too: HIV and several of its drugs suppress the marrow into neutropenia, compounding the immune deficit and raising bacterial-infection risk beyond the loss of CD4 T cells.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — The adrenal is the gland HIV most often hits: CMV adrenalitis and the infection itself can blunt cortisol output, making adrenal insufficiency the commonest endocrine complication of advanced HIV.
- `connects-to` → **[Thymus](../../06-organ/thymus/README.md)** — HIV cripples the organ that makes T cells: it depletes the thymus and its output of naive CD4 cells, so the gland's failing reserve limits immune reconstitution even once antiretrovirals suppress the virus.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Treated HIV ages the arteries early: chronic immune activation plus the dyslipidemia of some antiretrovirals accelerate atherosclerosis, so heart attack and stroke have become leading causes of death in the ART era.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — B-cell help fails even as antibody floods in: HIV drives a chaotic polyclonal plasma-cell activation and hypergammaglobulinemia, yet the specific, protective antibody response decays — dysregulation, not just deficiency.
- `connects-to` → **[Cervical Cancer](../cervical-cancer/README.md)** — Lost immunity lets HPV run to cancer: with CD4 surveillance gone, human papillomavirus persists and progresses, making invasive cervical cancer an AIDS-defining malignancy and a major cause of cancer death in women with HIV.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — The virus scars the kidney: HIV-associated nephropathy, a collapsing glomerulopathy driven by viral genes in kidney cells, drives chronic kidney disease, especially before treatment and in those of African ancestry with APOL1 risk variants.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — Even controlled HIV ages the arteries: chronic immune activation on top of antiretroviral metabolic effects accelerates atherosclerosis, so cardiovascular disease is now a leading cause of death in the treated, aging HIV population.
- `connects-to` → **[Pneumocystis jirovecii](../../../02-pathogen/03-fungi/pneumocystis-jirovecii/README.md)** — It hands the lungs to an opportunist: as CD4 counts fall below 200, Pneumocystis jirovecii pneumonia becomes the classic AIDS-defining infection, the reason prophylaxis is started at that threshold.
- `connects-to` → **[Toxoplasma gondii](../../../02-pathogen/04-parasites/toxoplasma-gondii/README.md)** — A latent parasite reawakens in the brain: with advanced immunosuppression, Toxoplasma gondii reactivates into the ring-enhancing brain abscesses of cerebral toxoplasmosis, a leading cause of AIDS-related focal neurological disease.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — The virus exploits host signaling: HIV manipulates STAT3 and JAK-STAT pathways in infected cells to favor its persistence and the chronic immune activation that smolders even under treatment.
- `connects-to` → **[Candida albicans](../../../02-pathogen/03-fungi/candida-albicans/README.md)** — A telltale early opportunist: oral and esophageal candidiasis is one of the commonest infections as HIV erodes CD4 T-cells, often the first clinical clue to underlying immunodeficiency.
- `connects-to` → **[Epstein-Barr Virus](../../../02-pathogen/01-viruses/epstein-barr-virus/README.md)** — Loss of T-cell control lets EBV drive cancer: with HIV immunosuppression, unchecked Epstein-Barr virus fuels B-cell lymphomas including primary CNS lymphoma and Burkitt and Hodgkin lymphoma.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — It burdens the mind directly and indirectly: HIV causes depression through neuroinflammation and direct CNS effects as well as the stigma, chronic illness and isolation of living with the infection.
- `connects-to` → **[Stroke](../stroke/README.md)** — It inflames and ages the arteries: chronic HIV drives accelerated atherosclerosis and an HIV-associated vasculopathy, and with antiretroviral metabolic effects raises the risk of ischemic stroke.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — The virus and its drugs thin the bones: chronic HIV inflammation plus tenofovir-based antiretroviral therapy lower bone mineral density, giving people with HIV markedly higher rates of osteoporosis and fracture.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — It attacks the peripheral nerves: HIV causes a distal sensory polyneuropathy directly, and older antiretrovirals added their own neurotoxicity, producing chronic burning neuropathic pain in the feet.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — The skin flags the infection: HIV brings Kaposi sarcoma, severe seborrhoeic dermatitis, extensive herpes and zoster, eosinophilic folliculitis and antiretroviral drug rashes, often the first visible clues.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It wastes and infects the gut: HIV enteropathy and opportunistic infections cause chronic diarrhoea and wasting, with oral and oesophageal candidiasis and antiretroviral GI side effects.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A chronic, stigmatised, lifelong infection breeds worry: the diagnosis, disclosure fears, adherence demands and stigma of HIV foster chronic health anxiety alongside its well-recognised depression.

[^barre-sinoussi-1983-hiv-isolation]: Barré-Sinoussi F, Chermann JC, Rey F, et al. Isolation of a T-lymphotropic retrovirus from a patient at risk for acquired immune deficiency syndrome (AIDS). *Science.* 1983;220(4599):868-871. [doi:10.1126/science.6189183](https://doi.org/10.1126/science.6189183) · [PubMed 6189183](https://pubmed.ncbi.nlm.nih.gov/6189183/)
[^ho-1995-viral-dynamics]: Ho DD, Neumann AU, Perelson AS, et al. Rapid turnover of plasma virions and CD4 lymphocytes in HIV-1 infection. *Nature.* 1995;373(6510):123-126. [doi:10.1038/373123a0](https://doi.org/10.1038/373123a0) · [PubMed 7816094](https://pubmed.ncbi.nlm.nih.gov/7816094/)
[^siliciano-2003-hiv-latency]: Siliciano JD, Kajdas J, Finzi D, et al. Long-term follow-up studies confirm the stability of the latent reservoir for HIV-1 in resting CD4+ T cells. *Nat Med.* 2003;9(6):727-728. [doi:10.1038/nm880](https://doi.org/10.1038/nm880) · [PubMed 12754504](https://pubmed.ncbi.nlm.nih.gov/12754504/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
