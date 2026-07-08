---
schema: human-scale-entry/v1
id: immune-system
name: Immune System
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-04
summary: "Two-layer defense: innate (fast, pattern recognition, complement, IFN) and adaptive (antigen-specific T/B lymphocytes, immunological memory). Peak adaptive response 7–14 days first exposure; memory recall 2–3 days. Organized around lymphoid organs."
aliases: ["immunity", "immune response", "lymphoid system", "humoral immunity", "cellular immunity"]
sources:
  - id: janeway-immunobiology-9e
    type: textbook
    cite: "Murphy K, Weaver C, Berg L. Janeway's Immunobiology. 9th ed. Garland Science; 2016."
    url: "https://www.garlandscience.com/product/isbn/9780815345053"
    accessed: "2026-06-04"
  - id: abbas-immunology-9e
    type: textbook
    cite: "Abbas AK, Lichtman AH, Pillai S. Cellular and Molecular Immunology. 9th ed. Elsevier; 2018."
    url: "https://www.elsevier.com/books/cellular-and-molecular-immunology/abbas/978-0-323-52323-3"
    accessed: "2026-06-04"
  - id: medzhitov-2007-innate
    type: peer-reviewed
    cite: "Medzhitov R. Recognition of microorganisms and activation of the immune response. Nature. 2007;449(7164):819-26."
    doi: "10.1038/nature06246"
    pmid: "17943118"
  - id: akbar-2016-immune-memory
    type: peer-reviewed
    cite: "Akbar AN, Gilroy DW. Aging immunity may exacerbate COVID-19. Science. 2020;369(6501):256-257."
    doi: "10.1126/science.abb0762"
    pmid: "32675364"
  - id: who-immunology-2012
    type: regulatory
    cite: "World Health Organization. Understanding the Immune System: How It Works. NIH Publication No. 03-5423. 2003."
    url: "https://www.niaid.nih.gov/sites/default/files/theimmunesystem.pdf"
    accessed: "2026-06-04"
  - id: iwasaki-medzhitov-2015
    type: peer-reviewed
    cite: "Iwasaki A, Medzhitov R. Control of adaptive immunity by the innate immune system. Nat Immunol. 2015;16(4):343-53."
    doi: "10.1038/ni.3123"
    pmid: "25789684"
cross_links:
  - target: 01-human/08-whole-body/human-body
    relation: part-of
    note: "The immune system is one of the major functional systems of the human body, spanning lymphoid organs, circulating cells, and soluble mediators throughout all tissues."
  - target: 01-human/04-cellular/dendritic-cell
    relation: contains
    note: "Dendritic cells are the professional antigen-presenting cells of the immune system, bridging innate detection and adaptive T cell priming."
  - target: 01-human/04-cellular/t-helper-cell
    relation: contains
    note: "CD4+ T helper cells are the master coordinators of adaptive immune responses, directing both cellular and humoral immunity."
  - target: 01-human/04-cellular/b-cell
    relation: contains
    note: "B lymphocytes are the antibody-producing arm of adaptive immunity, generating humoral protection via germinal center reactions."
  - target: 01-human/04-cellular/plasma-cell
    relation: contains
    note: "Plasma cells are the terminal antibody-secreting effectors of B cell differentiation; long-lived plasma cells in bone marrow maintain durable serum IgG titers."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: contains
    note: "IgG is the most abundant circulating antibody and the primary soluble effector molecule of humoral adaptive immunity."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: contains
    note: "MHC class II molecules are expressed on professional APCs of the immune system and are the molecular platform for CD4+ T cell activation and adaptive immune priming."
  - target: 02-pathogen/01-viruses/sars-cov-2
    relation: damaged-by
    note: "SARS-CoV-2 evades and damages the immune system via multiple mechanisms: suppression of type I IFN production, dysregulation of innate sensing, lymphopenia (CD4+/CD8+ T cell depletion), and cytokine storm (IL-6, IL-1β, TNF) that causes immunopathology."
  - target: 02-pathogen/01-viruses/influenza-a
    relation: damaged-by
    note: "Influenza A NS1 protein blocks IFN-β induction; neuraminidase cleaves surface antibodies and sialic acids that aid innate immunity; annual antigenic drift requires continuous immune adaptation."
  - target: 02-pathogen/02-bacteria/mycobacterium-tuberculosis
    relation: damaged-by
    note: "M. tuberculosis blocks phagosome acidification and fusion with lysosomes (via ESAT-6, coronin-1A), evades macrophage killing, establishes latent intracellular infection, and can reactivate when cell-mediated immunity is suppressed."
  - target: 03-medicine/01-modern/04-cardio/aspirin
    relation: treated-by
    note: "Aspirin inhibits COX-1 and COX-2, reducing prostaglandin E2 (PGE2) production; PGE2 is an immunomodulatory lipid mediator that normally suppresses T cell activation and NK cell cytotoxicity, so aspirin has net immunostimulatory effects in some inflammatory contexts."
  - target: 02-pathogen/01-viruses/hiv-1
    relation: damaged-by
    note: "HIV-1 systematically destroys the immune system by depleting CD4+ T helper cells (hallmark of AIDS), impairing DC antigen presentation via Nef, exhausting CTL responses, and driving chronic immune activation; AIDS is defined as CD4 <200/μL or an AIDS-defining illness."
  - target: 02-pathogen/02-bacteria/streptococcus-pneumoniae
    relation: infected-by
    note: "S. pneumoniae evades innate immunity via polysaccharide capsule (anti-phagocytic), pneumolysin (disrupts complement and oxidative burst), PspA (inhibits complement deposition), and CbpA (impairs IgA-mediated clearance in mucosa)."
  - target: 01-human/03-molecular/il-6
    relation: expresses
    note: "The immune system is the dominant source of IL-6 in infection and inflammation: macrophages, DCs, T cells, and B cells all produce IL-6 in response to PAMPs, DAMPs, and pro-inflammatory cytokines."
  - target: 01-human/03-molecular/il-6
    relation: modulates
    note: "IL-6 shapes adaptive immunity by driving Th17 differentiation, suppressing Treg development, promoting B cell to plasma cell differentiation, and activating effector T cells; IL-6/IL-6R signaling is a key checkpoint in the immune-inflammatory response."
  - target: 01-human/03-molecular/il-6
    relation: modulated-by
    note: "Immune activation (infection, injury, cytokine storm) dramatically upregulates IL-6 production; conversely, IL-10, glucocorticoids, and anti-IL-6R therapy (tocilizumab) suppress IL-6 levels."
  - target: 01-human/03-molecular/cortisol
    relation: modulated-by
    note: "Cortisol suppresses the immune system via NF-κB inhibition, lymphocyte apoptosis induction, and downregulation of pro-inflammatory cytokines, COX-2, and adhesion molecules; therapeutic glucocorticoids exploit this pathway."
  - target: 01-human/03-molecular/tnf-alpha
    relation: expresses
    note: "Macrophages and monocytes of the immune system are the primary source of TNF-α; released within minutes of innate receptor (TLR) activation, TNF-α is the proximal alarm cytokine of systemic inflammation."
  - target: 02-pathogen/01-viruses/dengue-virus
    relation: damaged-by
    note: "Dengue NS5 degrades STAT2 (blocking IFN-α/β signaling); secondary heterotypic infection triggers ADE and cross-reactive T-cell responses, amplifying viral burden in monocytes and driving the cytokine storm that causes vascular leak in dengue hemorrhagic fever."
  - target: 02-pathogen/04-parasites/plasmodium-falciparum
    relation: damaged-by
    note: "P. falciparum evades adaptive immunity via extensive var-gene antigenic variation (PfEMP1 switching); GPI-mediated TLR activation drives systemic inflammation; repeated infections cause progressive immune exhaustion and impaired T-cell and antibody responses."
  - target: 01-human/04-cellular/macrophage
    relation: contains
    evidence: janeway-immunobiology-9e
    note: "Macrophages are resident and recruited innate immune cells present in every tissue; they are core effectors of the immune system's first-line and inflammatory responses."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: contains
    evidence: janeway-immunobiology-9e
    note: "NK cells are innate lymphoid cells that are core constituents of the immune system, providing rapid cytotoxic surveillance against infected and malignant cells."
  - target: 01-human/05-tissue/bone-marrow
    relation: contains
    evidence: janeway-immunobiology-9e
    note: "Bone marrow is the primary haematopoietic organ generating all immune cells: HSCs → CLPs → T, B, NK cells; GMPs → granulocytes, monocytes, macrophages."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: modulated-by
    evidence: janeway-immunobiology-9e
    note: "Intestinal epithelium shapes systemic immunity via GALT and microbiome interactions, secreting cytokines and antimicrobial peptides that calibrate mucosal and systemic immune tone."
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: infected-by
    evidence: janeway-immunobiology-9e
    note: "S. aureus evades immune surveillance via Protein A (IgG Fc binding), leukotoxins killing neutrophils and macrophages, and biofilm formation resistant to phagocytosis."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: infected-by
    evidence: janeway-immunobiology-9e
    note: "A. fumigatus infects the immune system's phagocytes by evading killing through gliotoxin-mediated immune evasion and ROS scavenging via catalase/SOD."
  - target: 02-pathogen/03-fungi/candida-albicans
    relation: damaged-by
    evidence: janeway-immunobiology-9e
    note: "Systemic candidiasis overwhelms immune surveillance; Candida suppresses DC and T cell responses via Crk1-regulated immune evasion mechanisms."
  - target: 02-pathogen/06-microbiome/lactobacillus-rhamnosus
    relation: modulated-by
    evidence: janeway-immunobiology-9e
    note: "L. rhamnosus GG enhances immune system function by stimulating mucosal IgA, NK cell activity, and Treg development, reducing pathogen susceptibility."
  - target: 03-medicine/02-traditional/ashwagandha
    relation: treated-by
    evidence: janeway-immunobiology-9e
    note: "Ashwagandha withanolides enhance NK cell cytotoxicity, lymphocyte proliferation, and immunoglobulin levels in clinical trials of immune function."
  - target: 01-human/03-molecular/stat3
    relation: modulated-by
    note: "STAT3 downstream of IL-6 and IL-10 shapes innate and adaptive immunity; constitutive STAT3 in tumour-associated immune cells suppresses antitumour responses; STAT3 in Tregs maintains immune homeostasis."
  - target: 01-human/06-organ/thymus
    relation: contains
    note: "The thymus is the primary lymphoid organ responsible for generating the entire peripheral T cell repertoire via positive and negative selection; loss of thymic function (DiGeorge syndrome) causes profound T cell immunodeficiency."
  - target: 01-human/06-organ/spleen
    relation: modulated-by
    note: "The spleen orchestrates adaptive immune responses to blood-borne antigens via marginal zone B cells, follicular T/B GC reactions, and macrophage-T cell crosstalk; splenectomy increases susceptibility to encapsulated bacteria."
  - target: 02-pathogen/01-viruses/hepatitis-c-virus
    relation: damaged-by
    note: "HCV drives T cell exhaustion via PD-1/TIM-3 upregulation; chronic antigen stimulation depletes HCV-specific CD8⁺ T cells; NS3/4A cleaves MAVS and TRIF to suppress innate immune sensing, enabling viral persistence."
  - target: 02-pathogen/01-viruses/hpv-16
    relation: damaged-by
    note: "HPV E6/E7 suppress innate immune sensing by impairing IFN-β production; E7 degrades IRF3 and inhibits TLR9; this immune evasion enables persistent infection, failure of immune clearance, and oncogenic transformation."
  - target: 02-pathogen/01-viruses/hpv-16
    relation: prevented-by
    note: "Gardasil-9 generates neutralising IgG against HPV-16 L1 VLPs, preventing viral entry into mucosal keratinocytes; 90%+ efficacy against CIN2/3 and cervical cancer in seronegative individuals at time of vaccination."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: modulated-by
    note: "GR activation by glucocorticoids broadly suppresses the immune system via transrepression of NF-κB and AP-1, reducing production of pro-inflammatory cytokines (TNF-α, IL-6, IL-1β, IL-12) across innate and adaptive compartments."
  - target: 01-human/03-molecular/complement-c3
    relation: modulated-by
    note: "Modulated by Complement C3."
  - target: 01-human/03-molecular/histamine
    relation: modulated-by
    note: "Modulated by Histamine."
  - target: 01-human/03-molecular/prostaglandins
    relation: modulated-by
    note: "Modulated by Prostaglandins (Eicosanoids)."
  - target: 01-human/03-molecular/leptin
    relation: modulated-by
    note: "Modulated by Leptin."
  - target: 01-human/02-atomic/selenium
    relation: modulated-by
    note: "Modulated by Selenium."
  - target: 01-human/02-atomic/iron
    relation: modulated-by
    note: "Modulated by Iron."
  - target: 01-human/02-atomic/zinc
    relation: modulated-by
    note: "Modulated by Zinc."
  - target: 01-human/07-system/reproductive-system
    relation: modulated-by
    note: "Modulated by Reproductive System."
  - target: 01-human/07-system/lymphatic-system
    relation: modulated-by
    note: "Modulated by Lymphatic System."
  - target: 01-human/07-system/musculoskeletal-system
    relation: modulated-by
    note: "Modulated by Musculoskeletal System."
  - target: 01-human/07-system/endocrine-system
    relation: modulated-by
    note: "Modulated by Endocrine System."
  - target: 01-human/07-system/integumentary-system
    relation: modulated-by
    note: "Modulated by Integumentary System."
  - target: 01-human/04-cellular/neutrophil
    relation: composed-of
    note: "Composed Of by Neutrophil."
  - target: 01-human/04-cellular/adipocyte
    relation: modulated-by
    note: "Modulated by Adipocyte."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: composed-of
    note: "Composed Of by Cytotoxic T Cell."
  - target: 01-human/04-cellular/osteoblast
    relation: modulated-by
    note: "Modulated by Osteoblast."
  - target: 01-human/04-cellular/osteoclast
    relation: modulated-by
    note: "Modulated by Osteoclast."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: modulated-by
    note: "Modulated by Regulatory T Cell."
  - target: 01-human/04-cellular/fibroblast
    relation: modulated-by
    note: "Modulated by Fibroblast."
  - target: 01-human/04-cellular/endothelial-cell
    relation: modulated-by
    note: "Modulated by Endothelial Cell."
  - target: 01-human/04-cellular/mast-cell
    relation: composed-of
    note: "Composed Of by Mast Cell."
  - target: 01-human/06-organ/large-intestine
    relation: modulated-by
    note: "Modulated by Large Intestine."
  - target: 01-human/06-organ/adrenal-gland
    relation: modulated-by
    note: "Modulated by Adrenal Gland."
  - target: 02-pathogen/01-viruses/norovirus
    relation: damaged-by
    note: "Damaged by Norovirus."
  - target: 02-pathogen/01-viruses/ebola-virus
    relation: damaged-by
    note: "Damaged by Ebola Virus (EBOV)."
  - target: 02-pathogen/01-viruses/zika-virus
    relation: damaged-by
    note: "Damaged by Zika Virus (ZIKV)."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: damaged-by
    note: "Damaged by Varicella-Zoster Virus."
  - target: 02-pathogen/01-viruses/epstein-barr-virus
    relation: damaged-by
    note: "Damaged by Epstein-Barr Virus."
  - target: 02-pathogen/01-viruses/respiratory-syncytial-virus
    relation: damaged-by
    note: "Damaged by Respiratory Syncytial Virus."
  - target: 02-pathogen/01-viruses/measles-virus
    relation: damaged-by
    note: "Damaged by Measles Virus."
  - target: 02-pathogen/06-microbiome/bacteroides-fragilis
    relation: modulated-by
    note: "Modulated by Bacteroides fragilis."
  - target: 02-pathogen/06-microbiome/akkermansia-muciniphila
    relation: modulated-by
    note: "Modulated by Akkermansia muciniphila."
  - target: 02-pathogen/06-microbiome/faecalibacterium-prausnitzii
    relation: modulated-by
    note: "Modulated by Faecalibacterium prausnitzii."
  - target: 02-pathogen/06-microbiome/bifidobacterium-longum
    relation: modulated-by
    note: "Modulated by Bifidobacterium longum."
  - target: 02-pathogen/03-fungi/cryptococcus-neoformans
    relation: damaged-by
    note: "Damaged by Cryptococcus neoformans."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: damaged-by
    note: "Damaged by Pneumocystis jirovecii (formerly carinii)."
  - target: 02-pathogen/04-parasites/trypanosoma-brucei
    relation: damaged-by
    note: "Damaged by Trypanosoma brucei."
  - target: 02-pathogen/04-parasites/toxoplasma-gondii
    relation: damaged-by
    note: "Damaged by Toxoplasma gondii."
  - target: 02-pathogen/04-parasites/giardia-lamblia
    relation: damaged-by
    note: "Damaged by Giardia lamblia (G. intestinalis / G. duodenalis)."
  - target: 02-pathogen/04-parasites/leishmania-donovani
    relation: damaged-by
    note: "Damaged by Leishmania donovani."
  - target: 02-pathogen/02-bacteria/streptococcus-pyogenes
    relation: damaged-by
    note: "Damaged by Streptococcus pyogenes."
  - target: 02-pathogen/02-bacteria/clostridioides-difficile
    relation: damaged-by
    note: "Damaged by Clostridioides difficile."
  - target: 02-pathogen/02-bacteria/neisseria-meningitidis
    relation: damaged-by
    note: "Damaged by Neisseria meningitidis."
  - target: 03-medicine/03-food/vitamin-d
    relation: modulated-by
    note: "Modulated by Vitamin D (Calciferol)."
  - target: 03-medicine/03-food/sulforaphane
    relation: modulated-by
    note: "Modulated by Sulforaphane."
  - target: 03-medicine/03-food/zinc-dietary
    relation: modulated-by
    note: "Modulated by Dietary Zinc."
  - target: 03-medicine/03-food/dietary-fiber
    relation: modulated-by
    note: "Modulated by Dietary Fiber and Butyrate."
  - target: 03-medicine/03-food/quercetin
    relation: modulated-by
    note: "Modulated by Quercetin."
  - target: 03-medicine/02-traditional/milk-thistle
    relation: modulated-by
    note: "Modulated by Milk Thistle / Silymarin (Silybum marianum)."
  - target: 03-medicine/02-traditional/panax-ginseng
    relation: modulated-by
    note: "Modulated by Panax ginseng (Korean Red Ginseng)."
  - target: 01-human/03-molecular/complement-c5
    relation: contains
    note: "C5a (C5aR1/C5aR2) → neutrophil/monocyte chemotaxis + NLRP3 inflammasome priming + Th1/Th17 polarization; C5b-9 MAC → cell lysis; dysregulated terminal complement → autoimmune injury in gMG (NMJ), NMOSD (astrocytes), aHUS (glomerular endothelium)."
  - target: 01-human/03-molecular/il-12
    relation: contains
    note: "IL-12 (p35+p40 heterodimer) is the principal Th1-polarizing cytokine: DC → IL-12 → NK/T STAT4 → T-bet → IFN-γ; IL12B/IL12RB1 loss → MSMD (recurrent BCG, NTM, Salmonella); ustekinumab blocks IL-12 and IL-23 (shared p40 subunit) → TB screening required."
  - target: 01-human/07-system/tuberculosis
    relation: damaged-by
    note: "MTB is the paradigmatic intracellular pathogen evading innate immunity; granuloma (Th1/CD4+ T cells + macrophages) is the defining immune structure in TB; AIDS-related CD4+ depletion → TB reactivation; anti-TNF and anti-IL-12 therapy → highest TB reactivation risk."
  - target: 01-human/07-system/hiv-aids
    relation: damaged-by
    note: "HIV-1 is the paradigmatic cause of acquired immunodeficiency: preferentially destroys CD4+ Th1 cells (gp120/CCR5 or CXCR4 entry) → AIDS-defining opportunistic infections; ART achieves undetectable viral load (U=U) but residual immune activation and CD4 dysfunction persist."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "IL-10 is the prototypical anti-inflammatory cytokine produced by Tregs, M2 macrophages, Bregs, and Th2 cells; IL-10/STAT3 → ↑IκBα → NF-κB suppression in macrophages → ↓pro-inflammatory cytokines; IL-10 deficiency → colitis, autoimmunity; IL-10 excess → tumor immunosuppression."
  - target: 01-human/03-molecular/secretory-iga
    relation: connects-to
    note: "SIgA is the effector arm of mucosal immunity: pIgR transcytoses dimeric IgA across epithelium; 3-5 g/day secreted into gut lumen; immune exclusion is the primary mucosal defense before systemic IgG; selective IgA deficiency → recurrent respiratory and GI infections."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "C1-INH is a central innate immunity regulator: inhibits classical C1r/C1s (preventing C3 convertase formation) and contact FXII/kallikrein (preventing bradykinin-driven inflammation); C1-INH maintains homeostasis between complement activation and vascular integrity."
  - target: 02-pathogen/05-prions/prion-protein
    relation: damaged-by
    note: "PrPSc is identical in sequence to PrPC (self-protein); no innate or adaptive immune recognition occurs; lymphoid FDCs paradoxically amplify prions before neuroinvasion; silent propagation enables years-to-decades of subclinical disease without immune clearance."
  - target: 02-pathogen/06-environmental/aedes-aegypti
    relation: damaged-by
    note: "Ae. aegypti salivary proteins suppress DC activation and NK function at bite sites; apyrase blocks platelet aggregation enabling bloodmeal; immunomodulation at the inoculation site enables early DENV/ZIKV replication before innate immune sensing."
  - target: 01-human/03-molecular/mv-h-protein
    relation: connects-to
    note: "MV-H SLAM/CD150 tropism infects CD150+ T cells, B cells, and DCs → loss of pre-existing pathogen-specific memory (measles immune amnesia, 2–3 years); MMR vaccination prevents this memory deletion and the consequent 2-3 year elevation in all-cause child mortality."
  - target: 01-human/07-system/measles
    relation: connects-to
    note: "Measles immune amnesia (Mina 2019): MV SLAM/CD150 tropism infects SLAM-high memory B cells → erases 20-70% of pre-existing antibody diversity; naive B cells cannot reconstitute pathogen-specific memory → 2-3 years re-susceptibility to other infections post-measles."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Cell-mediated immunity: IFN-γ is the signature cytokine of Th1 and cytotoxic responses, activating macrophages and orchestrating the cell-mediated arm of the immune system against intracellular pathogens."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Antiviral innate arm: the type-I interferons are the rapid innate antiviral response, inducing an antiviral state in infected and neighbouring cells and bridging to the adaptive immune system."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Tolerance and checkpoint: the inhibitory receptor PD-1 enforces peripheral tolerance and limits immunopathology, the brake on T-cell responses that checkpoint-blockade immunotherapy releases against cancer."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Master inflammatory switch: NF-κB is the central transcription factor of immune activation, converting signals from pattern-recognition and cytokine receptors into the inflammatory gene programme."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Pattern recognition: Toll-like receptors such as TLR4 are the innate sensors that detect microbial molecular patterns and initiate the first-line immune response."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Inflammasome sensing: the NLRP3 inflammasome senses danger signals and activates caspase-1 to release IL-1β, a central effector arm of innate inflammation."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK-STAT signalling transduces the cytokine receptors that coordinate immune-cell differentiation and effector function across the immune system."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "The TLR adaptor MyD88 transduces innate pattern-recognition into NF-κB-driven inflammation (NF-κB mapped), a foundational mechanism of innate immunity."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated cytotoxicity is the core killing mechanism by which cytotoxic T cells and NK cells eliminate infected and transformed cells."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling (IFN-γ and type-I interferon already mapped) is the central transducer of the interferon responses that program antiviral and antitumour immunity."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "cGAS-STING is the core cytosolic-DNA sensor of the innate immune system, triggering the type-I-interferon response to pathogens and damaged self."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 is a broadly immunomodulatory lectin shaping macrophage activation, T-cell regulation and the resolution of inflammation across the immune system."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors regulate lymphocyte homeostasis, tolerance, and the memory-versus-effector balance across the immune system."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signaling governs the regulatory-T-cell induction and peripheral immune tolerance central to the immune system."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signaling downstream of antigen and cytokine receptors transduces the activation and differentiation of immune cells."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "Class I PI3K (PIK3CA)-AKT signaling downstream of immune receptors drives the activation and expansion of lymphocytes across the immune system."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTOR integrates nutrient and immune signals to program the differentiation and effector function of T cells and other immune cells of the immune system."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "CCL2 and the chemokine network orchestrate the trafficking of monocytes and other leukocytes throughout the immune system."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked immunometabolic signaling shapes the differentiation and effector metabolism of the immune cells of the immune system."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy participates in the antigen presentation, lymphocyte homeostasis, and innate immune responses of the immune system."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of antigen and Fc receptors participates in the activation of the lymphocytes and myeloid cells of the immune system."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven chemokine signaling directs the leukocyte trafficking and immune-cell recruitment of the immune system."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling directs the lymphocyte homing and hematopoietic-niche interactions of the immune system."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the immune-cell differentiation and identity of the immune system."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β signaling participates in the innate-immune inflammatory responses of the immune system."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the Th17-mediated adaptive immune responses of the immune system."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the type-2 innate and adaptive immune responses of the immune system."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell clonal expansion: IL-2 is the central growth factor driving the proliferation of antigen-activated T cells, the reaction that turns a few specific lymphocytes into the army of the adaptive immune response, and the basis of IL-2-based immunotherapies."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Type-2 and humoral immunity: IL-4 directs the Th2 arm of the immune system, driving B-cell antibody class-switching and the response to parasites and allergens, balancing the Th1/interferon-gamma (already mapped) axis."
  - target: 01-human/03-molecular/ctla-4
    relation: connects-to
    note: "Peripheral tolerance: CTLA-4 is a key inhibitory checkpoint that restrains T-cell activation and enforces self-tolerance (alongside PD-1 already mapped), preventing autoimmunity and serving as a target that immunotherapy releases against tumours."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Affinity maturation: within lymphoid germinal centres, B cells (already mapped) undergo somatic hypermutation and class-switching under T-follicular-helper guidance, the reaction that refines antibody affinity and generates memory in the adaptive immune system."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Immunoregulation: TGF-beta is a central immunoregulatory cytokine driving regulatory T-cell differentiation and IgA class-switching, restraining the immune system alongside IL-10 (already mapped) to prevent excess inflammation and autoimmunity."
  - target: 01-human/03-molecular/baff
    relation: connects-to
    note: "B-cell survival: BAFF is the key survival cytokine for B cells (already mapped), setting the size of the mature B-cell pool, and its excess drives the autoantibody production targeted in autoimmune disease."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Cytotoxic effectors: CD8 cytotoxic T cells kill virus-infected and tumour cells through perforin and granzyme (perforin already mapped), the cell-killing arm of adaptive immunity restrained by checkpoints (PD-1 already mapped)."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Peripheral tolerance: regulatory T cells suppress other immune cells through IL-10 and TGF-beta (already mapped), enforcing the peripheral tolerance whose failure causes the autoimmunity the immune system must avoid."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Antibody maturation: germinal centres are where B cells undergo somatic hypermutation and class-switching (immunoglobulin G already mapped) to produce high-affinity antibody, the engine of the humoral immune response."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "CNS immune arm: the microglia are the resident macrophages of the central nervous system, the brain's own arm of the immune system that surveils, prunes and defends the neural tissue behind the blood-brain barrier."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "Gut-associated lymphoid tissue: the small intestine holds the largest concentration of immune cells in the body — the Peyer's patches and lamina propria (secretory IgA already mapped) — the mucosal front line of the immune system."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "Microbiome education: the commensal gut microbiota educate and regulate the immune system, the host-microbe symbiosis shaping the tolerance and reactivity (regulatory T cells already mapped) of immunity throughout life."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immunity: IL-13, with IL-4 (already mapped), is a type-2 cytokine of the anti-parasite and allergic arm of the immune system, driving the mucus and barrier response."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Eosinophil arm: IL-5 is the type-2 cytokine that expands and recruits the eosinophils of the anti-helminth and allergic response of the immune system."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 arm: IL-23 sustains the Th17 (IL-17 already mapped) cells of the mucosal and antifungal defence of the immune system."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Barrier immunity: the skin is the first physical and immunological barrier of the immune system, with the Langerhans/dendritic (already mapped) cells and the antimicrobial peptides."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Hepatic immunity: the liver synthesises the complement (C3 and C5 already mapped) and the acute-phase proteins, houses the Kupffer macrophages (already mapped) and filters the portal antigens of the immune system."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Respiratory mucosal immunity: the lung's mucosal immune system (the alveolar macrophages already mapped, the BALT and the secretory-IgA already mapped) defends the vast air-tissue interface of the immune system."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (C3 and C5 already mapped), protecting the host tissue from the complement self-attack, a core self/non-self control of the immune system."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2/allergic arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped) and the mast cells (already mapped), is the antibody arm of the anti-parasite and allergic immunity of the immune system."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Immune-adherence clearance: the erythrocytes bind the complement (C3 already mapped)-opsonised immune complexes via the CR1 receptor and ferry them for hepatic (already mapped) clearance, a role of the immune system."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Epithelial alarmin: TSLP, with IL-33 (already mapped), is the epithelial-barrier alarmin that initiates the type-2 (IL-4, IL-5 and IL-13 already mapped) immune response of the immune system."
  - target: 01-human/03-molecular/il-31
    relation: connects-to
    note: "Itch cytokine: IL-31, a type-2 (IL-4 and IL-13 already mapped) cytokine, is the pruritogenic effector linking the immune system to the sensory nervous system in the itch response."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Thromboinflammation: the platelets, beyond haemostasis, act as innate immune cells that release chemokines (PF4) and interact with the neutrophils (already mapped) in the thromboinflammation of the immune system."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "Anaphylatoxin receptor: the C5aR1 is the receptor for the C5a anaphylatoxin, transducing the complement (C3, C5, factor H and C1-esterase inhibitor already mapped) signal into the myeloid chemotaxis and inflammation of the immune system."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Type-2 matricellular: periostin, downstream of the type-2 (IL-13 already mapped) cytokines, is a matricellular effector of the tissue remodelling and eosinophilic inflammation of the immune system."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Immunomodulatory matricellular: osteopontin is a matricellular cytokine that promotes the Th1 and macrophage responses and the leukocyte migration of the immune system."
---

# Immune System

## Overview

The immune system is the body's multilayered defense against pathogens, malignant cells, and foreign substances — and simultaneously the regulatory network that maintains tolerance to self [^janeway-immunobiology-9e]. It is not a single organ but a distributed system spanning every tissue in the body: cells circulate in blood and lymph, patrol tissues as resident populations, and communicate through soluble mediators (cytokines, chemokines, antibodies, complement proteins).

Two functionally distinct but deeply interconnected arms cooperate [^iwasaki-medzhitov-2015]:

1. **Innate immunity** — rapid (minutes to hours), broad-specificity, non-adaptive detection of molecular patterns associated with pathogens (PAMPs — pathogen-associated molecular patterns) or tissue damage (DAMPs — damage-associated molecular patterns). Effectors: phagocytes (neutrophils, macrophages), NK cells, innate lymphoid cells, dendritic cells, complement, type I interferons.

2. **Adaptive immunity** — slow first response (7–14 days), exquisitely antigen-specific, capable of immunological memory. Effectors: T lymphocytes (CD4+ helper, CD8+ cytotoxic, regulatory), B lymphocytes, antibodies. On second encounter with the same antigen, memory recall response peaks in 2–3 days with higher magnitude and affinity.

This two-layer architecture is why vaccination works: a vaccine primes the adaptive immune system at low cost (no disease), establishing memory cells and long-lived plasma cells that enable rapid, protective responses on subsequent natural exposure.

The immune system surveils approximately **37 trillion cells** in the human body via constitutive MHC-I self-presentation — any cell that fails to display normal MHC-I with normal self-peptides is detected as abnormal by NK cells and cytotoxic T cells. This surveillance is the primary defense against intracellular pathogens and cancer.

## Structure

### Primary lymphoid organs

Primary lymphoid organs are the sites of immune cell development and education:

| Organ | Function |
|:---|:---|
| **Bone marrow** | Origin of all immune cells (hematopoietic stem cells); site of B cell development, maturation, and central tolerance; long-lived plasma cell niche |
| **Thymus** | Site of T cell development: TCR rearrangement, positive selection (MHC restriction), negative selection (central tolerance/clonal deletion), Treg generation |

### Secondary lymphoid organs

Secondary lymphoid organs are where adaptive immune responses are initiated — where circulating naïve lymphocytes encounter antigen presented by dendritic cells:

| Organ | Specialization |
|:---|:---|
| **Lymph nodes** | Filter lymph draining tissues; T cell zones (paracortex) + B cell follicles (cortex); site of DC–T cell priming and germinal center reactions |
| **Spleen** | Filters blood; marginal zone (innate, T-independent B responses) + white pulp (T and B cell zones, GC reactions); red pulp (erythrophagocytosis) |
| **MALT (mucosa-associated lymphoid tissue)** | Tonsils, Peyer's patches (gut), bronchus-associated lymphoid tissue (BALT); front-line mucosal immunity; IgA production |

### Circulating cells

| Cell type | Approximate blood count | Primary function |
|:---|:---|:---|
| Neutrophils | 1.8–7.7 × 10⁹/L | First phagocytic responders; bacteria/fungi; NET formation |
| Monocytes | 0.2–1.0 × 10⁹/L | Phagocytosis; cytokine production; DC precursors |
| NK cells | 0.07–0.5 × 10⁹/L | Kill MHC-I-low cells; produce IFN-γ |
| CD4+ T cells | 0.4–1.1 × 10⁹/L | Coordinate adaptive response |
| CD8+ T cells | 0.2–0.9 × 10⁹/L | Kill infected/malignant cells |
| B cells | 0.05–0.4 × 10⁹/L | Produce antibodies; APCs |
| Eosinophils | 0.02–0.5 × 10⁹/L | Anti-parasite; allergy |
| Basophils/mast cells | <0.1 × 10⁹/L blood | IgE-mediated degranulation; allergy |

### Soluble mediators

- **Complement system** — 30+ plasma proteins; three activation pathways (classical, lectin, alternative) converging on C3 cleavage → C3b opsonization + MAC lysis + C5a anaphylatoxin
- **Cytokines** — soluble signaling proteins: interleukins (IL-1 through IL-38+), interferons (type I: IFN-α/β; type II: IFN-γ; type III: IFN-λ), TNF, TGF-β, colony-stimulating factors
- **Chemokines** — ~50 small cytokines guiding cell migration via concentration gradients (CXCL8/IL-8 for neutrophils; CCL19/21 for DC/T cell homing; CXCL13 for B cell follicle formation)
- **Antibodies (immunoglobulins)** — IgM (first response, complement activation), IgG (most abundant, long half-life, placental transfer), IgA (mucosal secretory), IgE (allergy, anti-parasite), IgD (B cell surface co-receptor)

## Function

### Innate immune response (Phase 1: minutes–hours)

When a pathogen breaches barriers (skin, mucosa), innate immune cells respond within minutes [^medzhitov-2007-innate]:

1. **Pattern recognition** — tissue macrophages and DCs recognize PAMPs via TLRs (TLR4: LPS; TLR3: dsRNA; TLR9: CpG DNA), NLRs (NOD2: bacterial muramyl dipeptide; NLRP3 inflammasome), RIG-I/MDA5 (cytosolic RNA), cGAS/STING (cytosolic DNA)
2. **Immediate effector response** — vasodilation, increased permeability (histamine from mast cells, bradykinin from plasma contact system); neutrophil recruitment via CXCL8; phagocytosis; complement activation
3. **Type I IFN induction** — TLR7/9 in pDCs or RIG-I/STING in infected cells triggers IRF3/7 → massive IFN-α/β secretion → IFNAR signaling on all neighboring cells → antiviral state (ISGs: OAS, MX1, PKR, IFIT)
4. **Cytokine storm risk** — excessive innate activation (especially IL-6, IL-1β, TNF, IL-18) can cause systemic inflammatory response syndrome (SIRS); this is the basis of the cytokine storm in severe COVID-19 and influenza

### Adaptive immune response (Phase 2: days 3–14)

4. **DC maturation and migration** (Days 1–3) — PAMPs trigger DC maturation; mature DCs upregulate MHC-II, CD80/86, CCR7; migrate to draining lymph nodes
5. **T cell priming** (Days 3–5) — DC–T cell pMHC-II–TCR interaction in lymph node paracortex; naïve CD4+ T cell activation + CD8+ T cell priming; Signals 1+2+3 trigger clonal expansion
6. **B cell activation and germinal center** (Days 5–14) — antigen-specific B cells activated at follicle border by cognate antigen + Tfh help; germinal centers form; affinity maturation, class switching, plasmablast and memory B cell generation
7. **Effector deployment** — cytotoxic CD8+ T cells kill infected cells; IgM then IgG antibodies neutralize pathogen; opsonization, ADCC, complement enhance clearance

### Memory and recall

After primary response contraction, long-lived memory cells persist:
- **Memory CD4+ and CD8+ T cells** — distributed in lymphoid and non-lymphoid tissues (including tissue-resident memory T cells, T_RM); respond within hours
- **Memory B cells** — circulate; respond within 1–3 days on re-encounter
- **Long-lived plasma cells (LLPCs)** — in bone marrow; continuously secrete IgG for years, maintaining serum antibody titers that provide immediate neutralization on re-exposure

## Connections

- **Part of:** [human-body](../../08-whole-body/human-body/README.md)
- **Contains:** [dendritic-cell](../../04-cellular/dendritic-cell/README.md), [t-helper-cell](../../04-cellular/t-helper-cell/README.md), [b-cell](../../04-cellular/b-cell/README.md), [plasma-cell](../../04-cellular/plasma-cell/README.md), [immunoglobulin-g](../../03-molecular/immunoglobulin-g/README.md)
- **Damaged by:** [sars-cov-2](../../../../02-pathogen/01-viruses/sars-cov-2/README.md), [influenza-a](../../../../02-pathogen/01-viruses/influenza-a/README.md), [mycobacterium-tuberculosis](../../../../02-pathogen/02-bacteria/mycobacterium-tuberculosis/README.md)
- **Treated by:** [aspirin](../../../../03-medicine/01-modern/04-cardio/aspirin/README.md) (immunomodulatory via COX inhibition → reduced PGE2)
- `contains` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — C5a (C5aR1/C5aR2) → neutrophil/monocyte chemotaxis + NLRP3 inflammasome priming + Th1/Th17 polarization; C5b-9 MAC → cell lysis; dysregulated terminal complement → autoimmune injury in gMG (NMJ), NMOSD (astrocytes), aHUS (glomerular endothelium).
- `contains` → **[IL-12](../../03-molecular/il-12/README.md)** — IL-12 (p35+p40 heterodimer) is the master Th1-polarizing cytokine produced by dendritic cells and macrophages; drives IFN-γ from NK cells and T cells via JAK2/TYK2/STAT4/T-bet; IL12B/IL12RB1 loss → MSMD with recurrent BCG/NTM disease; ustekinumab (anti-p40) blocks both IL-12 and IL-23, carrying TB reactivation risk comparable to anti-TNF agents.
- `damaged-by` → **[Tuberculosis](../tuberculosis/README.md)** — MTB is the archetypal intracellular pathogen: evades innate immunity via phagosome arrest, ESAT-6 cytosolic escape, MHC-II inhibition, and Treg induction; granuloma formation requires an intact Th1/IL-12/IFN-γ/TNF-α axis; CD4⁺ T cell depletion (HIV/AIDS) → TB reactivation is the defining CD4-dependent opportunistic infection.
- `damaged-by` → **[HIV/AIDS](../hiv-aids/README.md)** — HIV-1 is the paradigmatic cause of acquired immunodeficiency: selectively depletes CD4⁺ T helper cells via gp120/CD4/CCR5 entry → AIDS-defining opportunistic infections; residual immune dysregulation (T cell exhaustion, monocyte activation, chronic inflammation) persists even with fully suppressive ART.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — IL-10 is the prototypical anti-inflammatory cytokine produced by Tregs, M2 macrophages, and Bregs; IL-10/STAT3 → NF-κB suppression in macrophages → ↓pro-inflammatory cytokines; IL-10 deficiency → colitis and autoimmunity; IL-10 excess → tumor immunosuppression.
- `connects-to` → **[Secretory IgA](../../03-molecular/secretory-iga/README.md)** — SIgA is the effector arm of mucosal immunity: pIgR transcytoses dimeric IgA across epithelium; 3-5 g/day secreted into gut lumen; immune exclusion is the primary mucosal defense before systemic IgG; selective IgA deficiency → recurrent respiratory and GI infections.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — C1-INH is a central innate immunity regulator: inhibits classical C1r/C1s (preventing C3 convertase formation) and contact FXII/kallikrein (preventing bradykinin-driven inflammation); C1-INH maintains homeostasis between complement activation and vascular integrity.
- `connects-to` → **[PCV13 (Prevnar 13)](../../../../04-vaccine/08-conjugate/pcv13/README.md)** — PCV13 activates T-cell-dependent immunity via CRM197 conjugation: germinal center reaction, affinity maturation, IgG class-switch (IgG2/IgG1); generates long-lived plasma cells and memory B cells; enables infant immunization from 6 weeks; herd protection via carriage reduction.
- `connects-to` → **[MMR Vaccine](../../../../04-vaccine/05-live-attenuated/mmr-vaccine/README.md)** — MMR live-attenuated replication in local lymphoid tissue drives Th1-biased cellular immunity (CD8+ CTL, CD4+ Th1) and robust germinal center reactions; generates durable IgG via long-lived plasma cells; natural-infection mimic is more immunogenic than inactivated vaccines.
- `damaged-by` → **[Prion Protein (PrP)](../../../02-pathogen/05-prions/prion-protein/README.md)** — PrPSc is a self-protein; the immune system mounts no antibody or T-cell response; lymphoid follicular dendritic cells amplify prions peripherally before neuroinvasion; silent propagation enables disease progression without immune clearance.
- `damaged-by` → **[Aedes aegypti](../../../02-pathogen/06-environmental/aedes-aegypti/README.md)** — salivary proteins suppress DC activation and NK function at bite sites; salivary apyrase blocks platelet aggregation enabling bloodmeal; immunomodulation at the inoculation site enables early DENV/ZIKV replication before innate immune sensing.
- `connects-to` → **[OPV (Oral Polio Vaccine)](../../../../04-vaccine/05-live-attenuated/oral-polio-vaccine/README.md)** — OPV gut replication activates mucosal immunity (GALT → sIgA) and systemic immunity (mesenteric lymph nodes → serum IgG + T cells); dual response enables paralysis prevention and transmission interruption — the mechanism underlying polio eradication.
- `damaged-by` → **[Herpesviridae](../../../02-pathogen/01-viruses/herpesvirus/README.md)** — all nine human herpesviruses encode dedicated immune evasion genes: HSV ICP47/CMV US6 block MHC-I via TAP inhibition; CMV UL16-21 downregulate NKG2D ligands; all subfamilies antagonize IFN signaling; latency renders infected cells invisible to CTLs indefinitely.
- `connects-to` → **[MV-H Protein](../../03-molecular/mv-h-protein/README.md)** — MV-H SLAM/CD150 tropism infects CD150+ T cells, B cells, and DCs → loss of pre-existing pathogen-specific memory (measles immune amnesia, 2–3 years); MMR vaccination prevents this memory deletion and the consequent elevated all-cause child mortality risk.
- `connects-to` → **[Measles](../../07-system/measles/README.md)** — Measles immune amnesia (Mina 2019): MV SLAM/CD150 tropism infects memory B cells → erases 20-70% of pre-existing antibody diversity; naive B cells cannot reconstitute pathogen-specific memory → 2-3 years re-susceptibility to other infections post-measles.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — IFN-γ is the signature cytokine of Th1 and cytotoxic responses, activating macrophages and orchestrating the cell-mediated arm of the immune system against intracellular pathogens.
- `connects-to` → **[Type I Interferon](../../03-molecular/type-i-interferon/README.md)** — The type-I interferons are the rapid innate antiviral response, inducing an antiviral state in infected and neighboring cells and bridging to the adaptive immune system.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — The inhibitory receptor PD-1 enforces peripheral tolerance and limits immunopathology, the brake on T-cell responses that checkpoint-blockade immunotherapy releases against cancer.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB is the central transcription factor of immune activation, converting signals from pattern-recognition and cytokine receptors into the inflammatory gene program.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — Toll-like receptors such as TLR4 are the innate sensors that detect microbial molecular patterns and initiate the first-line immune response.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — The NLRP3 inflammasome senses danger signals and activates caspase-1 to release IL-1β, a central effector arm of innate inflammation.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK-STAT signaling transduces the cytokine receptors that coordinate immune-cell differentiation and effector function across the immune system.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — The TLR adaptor MyD88 transduces innate pattern-recognition into NF-κB-driven inflammation (NF-κB mapped), a foundational mechanism of innate immunity.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated cytotoxicity is the core killing mechanism by which cytotoxic T cells and NK cells eliminate infected and transformed cells.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling (IFN-γ and type-I interferon already mapped) is the central transducer of the interferon responses that program antiviral and antitumor immunity.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — cGAS-STING is the core cytosolic-DNA sensor of the innate immune system, triggering the type-I-interferon response to pathogens and damaged self.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 is a broadly immunomodulatory lectin shaping macrophage activation, T-cell regulation and the resolution of inflammation across the immune system.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors regulate lymphocyte homeostasis, tolerance, and the memory-versus-effector balance across the immune system.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling governs the regulatory-T-cell induction and peripheral immune tolerance central to the immune system.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling downstream of antigen and cytokine receptors transduces the activation and differentiation of immune cells.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — Class I PI3K (PIK3CA)-AKT signaling downstream of immune receptors drives the activation and expansion of lymphocytes across the immune system.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR integrates nutrient and immune signals to program the differentiation and effector function of T cells and other immune cells of the immune system.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — CCL2 and the chemokine network orchestrate the trafficking of monocytes and other leukocytes throughout the immune system.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked immunometabolic signaling shapes the differentiation and effector metabolism of the immune cells of the immune system.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy participates in the antigen presentation, lymphocyte homeostasis, and innate immune responses of the immune system.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of antigen and Fc receptors participates in the activation of the lymphocytes and myeloid cells of the immune system.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven chemokine signaling directs the leukocyte trafficking and immune-cell recruitment of the immune system.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling directs the lymphocyte homing and hematopoietic-niche interactions of the immune system.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the immune-cell differentiation and identity of the immune system.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β signaling participates in the innate-immune inflammatory responses of the immune system.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the Th17-mediated adaptive immune responses of the immune system.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the type-2 innate and adaptive immune responses of the immune system.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell clonal expansion: IL-2 is the central growth factor driving the proliferation of antigen-activated T cells, the reaction that turns a few specific lymphocytes into the army of the adaptive immune response, and the basis of IL-2-based immunotherapies.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Type-2 and humoral immunity: IL-4 directs the Th2 arm of the immune system, driving B-cell antibody class-switching and the response to parasites and allergens, balancing the Th1/interferon-gamma (already mapped) axis.
- `connects-to` → **[CTLA-4](../../03-molecular/ctla-4/README.md)** — Peripheral tolerance: CTLA-4 is a key inhibitory checkpoint that restrains T-cell activation and enforces self-tolerance (alongside PD-1 already mapped), preventing autoimmunity and serving as a target that immunotherapy releases against tumours.
- `connects-to` → **[Germinal center](../../05-tissue/germinal-center/README.md)** — Affinity maturation: within lymphoid germinal centres, B cells (already mapped) undergo somatic hypermutation and class-switching under T-follicular-helper guidance, the reaction that refines antibody affinity and generates memory in the adaptive immune system.
- `connects-to` → **[TGF-beta](../../03-molecular/tgf-beta/README.md)** — Immunoregulation: TGF-beta is a central immunoregulatory cytokine driving regulatory T-cell differentiation and IgA class-switching, restraining the immune system alongside IL-10 (already mapped) to prevent excess inflammation and autoimmunity.
- `connects-to` → **[BAFF](../../03-molecular/baff/README.md)** — B-cell survival: BAFF is the key survival cytokine for B cells (already mapped), setting the size of the mature B-cell pool, and its excess drives the autoantibody production targeted in autoimmune disease.
- `connects-to` → **[T-cytotoxic cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Cytotoxic effectors: CD8 cytotoxic T cells kill virus-infected and tumour cells through perforin and granzyme (perforin already mapped), the cell-killing arm of adaptive immunity restrained by checkpoints (PD-1 already mapped).
- `connects-to` → **[Regulatory T cell](../../04-cellular/regulatory-t-cell/README.md)** — Peripheral tolerance: regulatory T cells suppress other immune cells through IL-10 and TGF-beta (already mapped), enforcing the peripheral tolerance whose failure causes the autoimmunity the immune system must avoid.
- `connects-to` → **[Germinal center](../../05-tissue/germinal-center/README.md)** — Antibody maturation: germinal centres are where B cells undergo somatic hypermutation and class-switching (immunoglobulin G already mapped) to produce high-affinity antibody, the engine of the humoral immune response.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — CNS immune arm: the microglia are the resident macrophages of the central nervous system, the brain's own arm of the immune system that surveils, prunes and defends the neural tissue behind the blood-brain barrier.
- `connects-to` → **[Small intestine](../../06-organ/small-intestine/README.md)** — Gut-associated lymphoid tissue: the small intestine holds the largest concentration of immune cells in the body — the Peyer's patches and lamina propria (secretory IgA already mapped) — the mucosal front line of the immune system.
- `connects-to` → **[Gut microbiome](../gut-microbiome/README.md)** — Microbiome education: the commensal gut microbiota educate and regulate the immune system, the host-microbe symbiosis shaping the tolerance and reactivity (regulatory T cells already mapped) of immunity throughout life.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immunity: IL-13, with IL-4 (already mapped), is a type-2 cytokine of the anti-parasite and allergic arm of the immune system, driving the mucus and barrier response.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Eosinophil arm: IL-5 is the type-2 cytokine that expands and recruits the eosinophils of the anti-helminth and allergic response of the immune system.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 arm: IL-23 sustains the Th17 (IL-17 already mapped) cells of the mucosal and antifungal defence of the immune system.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Barrier immunity: the skin is the first physical and immunological barrier of the immune system, with the Langerhans/dendritic (already mapped) cells and the antimicrobial peptides.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Hepatic immunity: the liver synthesises the complement (C3 and C5 already mapped) and the acute-phase proteins, houses the Kupffer macrophages (already mapped) and filters the portal antigens of the immune system.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Respiratory mucosal immunity: the lung's mucosal immune system (the alveolar macrophages already mapped, the BALT and the secretory-IgA already mapped) defends the vast air-tissue interface of the immune system.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (C3 and C5 already mapped), protecting the host tissue from the complement self-attack, a core self/non-self control of the immune system.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2/allergic arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped) and the mast cells (already mapped), is the antibody arm of the anti-parasite and allergic immunity of the immune system.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Immune-adherence clearance: the erythrocytes bind the complement (C3 already mapped)-opsonised immune complexes via the CR1 receptor and ferry them for hepatic (already mapped) clearance, a role of the immune system.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Epithelial alarmin: TSLP, with IL-33 (already mapped), is the epithelial-barrier alarmin that initiates the type-2 (IL-4, IL-5 and IL-13 already mapped) immune response of the immune system.
- `connects-to` → **[IL-31](../../03-molecular/il-31/README.md)** — Itch cytokine: IL-31, a type-2 (IL-4 and IL-13 already mapped) cytokine, is the pruritogenic effector linking the immune system to the sensory nervous system in the itch response.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Thromboinflammation: the platelets, beyond haemostasis, act as innate immune cells that release chemokines (PF4) and interact with the neutrophils (already mapped) in the thromboinflammation of the immune system.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — Anaphylatoxin receptor: the C5aR1 is the receptor for the C5a anaphylatoxin, transducing the complement (C3, C5, factor H and C1-esterase inhibitor already mapped) signal into the myeloid chemotaxis and inflammation of the immune system.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Type-2 matricellular: periostin, downstream of the type-2 (IL-13 already mapped) cytokines, is a matricellular effector of the tissue remodelling and eosinophilic inflammation of the immune system.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Immunomodulatory matricellular: osteopontin is a matricellular cytokine that promotes the Th1 and macrophage responses and the leukocyte migration of the immune system.

## Pathology

### Immunodeficiency

**Primary immunodeficiencies** are monogenic disorders of immune development or function:
- **Severe Combined Immunodeficiency (SCID)** — absence of both T and B cell function; ADA-SCID (adenosine deaminase deficiency), X-SCID (IL-2Rγ chain mutation), RAG1/2 mutations. Untreated, invariably fatal in infancy. Curable by hematopoietic stem cell transplantation or gene therapy (ADA-SCID is the first human gene therapy success, 1990).
- **X-linked agammaglobulinemia (XLA)** — BTK mutation; B cell development arrest at pro-B stage; absent serum immunoglobulins; treated with IV immunoglobulin (IVIG)
- **DiGeorge syndrome** — thymic aplasia (22q11.2 deletion); absent T cell development; severe susceptibility to viral and fungal infections

**Secondary immunodeficiencies** (acquired):
- **HIV-1/AIDS** — retrovirus selectively infecting and depleting CD4+ T cells (via CCR5/CXCR4 co-receptors); CD4+ count <200 cells/µL defines AIDS; opportunistic infections (PCP, CMV retinitis, cryptococcal meningitis, MAI) are the proximate causes of death. ART (antiretroviral therapy) can fully reconstitute CD4+ counts and prevent progression.
- **Iatrogenic** — immunosuppressive drugs (corticosteroids, cyclophosphamide, tacrolimus, biologics like rituximab, anti-TNF) used in autoimmunity, transplantation, and cancer cause secondary immunodeficiency

### Autoimmunity

When central and peripheral tolerance fail, self-reactive T and B cells escape deletion and attack host tissues:
- **Systemic lupus erythematosus (SLE)** — loss of tolerance to nuclear antigens (dsDNA, histones, Sm); anti-dsDNA antibodies form immune complexes; complement-mediated damage in kidneys (lupus nephritis), skin, joints, brain. HLA-DR2/DR3 strongly associated. Type I IFN signature is pathognomonic.
- **Rheumatoid arthritis (RA)** — anti-citrullinated protein antibodies (ACPA/anti-CCP) + rheumatoid factor (RF) attack synovial joint membranes; Th17-driven neutrophilic/macrophage synovitis → cartilage and bone destruction. HLA-DRB1 shared epitope is the major genetic risk factor.
- **Type 1 diabetes (T1D)** — autoreactive CD8+ T cells destroy insulin-secreting pancreatic β-cells; Th1-dominant; HLA-DQ8/DR4 strongly associated
- **Multiple sclerosis (MS)** — autoreactive T cells (Th17 prominent) and B cells damage CNS myelin; HLA-DRB1\*15:01 is the strongest genetic risk factor

### Hypersensitivity (Gell-Coombs classification)

| Type | Mechanism | Examples |
|:---|:---|:---|
| I (immediate) | IgE-mediated mast cell/basophil degranulation | Anaphylaxis, atopy, asthma |
| II (cytotoxic) | IgG/IgM against cell-surface antigens → complement + ADCC | Autoimmune hemolytic anemia, Goodpasture |
| III (immune complex) | IgG immune complex deposition → complement → tissue inflammation | SLE nephritis, serum sickness |
| IV (delayed-type) | Th1-mediated macrophage activation / Tc-mediated cytotoxicity | Contact dermatitis, tuberculin reaction, T1D |

**Anaphylaxis** is the most immediately life-threatening: systemic mast cell degranulation (IgE crosslinking by allergen → FcεRI → histamine, tryptase, LTC4) causes airway edema, bronchospasm, and circulatory collapse. Treatment: epinephrine (reverses bronchospasm and vasoconstriction).

### Immune evasion by pathogens

- **SARS-CoV-2** — NSP1 blocks mRNA translation of innate immune genes; ORF3b and ORF6 suppress IFN-β; N protein prevents TRIM25-mediated RIG-I ubiquitination; spike downregulates MHC-I on infected cells. Severe disease associated with defective early IFN response and subsequent hyperinflammation.
- **Influenza A** — NS1 binds TRIM25, blocking RIG-I signaling and IFN-β production; PB1-F2 promotes mitochondrial apoptosis in immune cells; neuraminidase cleaves sialic acids that normally facilitate IgA binding; antigenic drift in HA/NA evades existing antibody responses annually.
- **M. tuberculosis** — ESAT-6 perforates phagosomal membrane; LipoArabinomannan (LAM) from the mycobacterial cell wall blocks phagosome maturation (blocks Rab7, preventing lysosome fusion); coronin-1A retains functional mitochondria near the phagosome; the bacterium can persist for decades in granulomas. Reactivation risk is highest when cell-mediated immunity is suppressed (HIV co-infection, anti-TNF therapy, malnutrition).

[^janeway-immunobiology-9e]: Murphy K, Weaver C, Berg L. *Janeway's Immunobiology.* 9th ed. Garland Science; 2016.
[^abbas-immunology-9e]: Abbas AK, Lichtman AH, Pillai S. *Cellular and Molecular Immunology.* 9th ed. Elsevier; 2018.
[^medzhitov-2007-innate]: Medzhitov R. Recognition of microorganisms and activation of the immune response. *Nature.* 2007;449(7164):819-26. [doi:10.1038/nature06246](https://doi.org/10.1038/nature06246) · [PubMed 17943118](https://pubmed.ncbi.nlm.nih.gov/17943118/)
[^iwasaki-medzhitov-2015]: Iwasaki A, Medzhitov R. Control of adaptive immunity by the innate immune system. *Nat Immunol.* 2015;16(4):343-53. [doi:10.1038/ni.3123](https://doi.org/10.1038/ni.3123) · [PubMed 25789684](https://pubmed.ncbi.nlm.nih.gov/25789684/)
[^akbar-2016-immune-memory]: Akbar AN, Gilroy DW. Aging immunity may exacerbate COVID-19. *Science.* 2020;369(6501):256-257. [doi:10.1126/science.abb0762](https://doi.org/10.1126/science.abb0762) · [PubMed 32675364](https://pubmed.ncbi.nlm.nih.gov/32675364/)
[^who-immunology-2012]: World Health Organization / NIH. Understanding the Immune System: How It Works. NIH Publication No. 03-5423. [Read online →](https://www.niaid.nih.gov/sites/default/files/theimmunesystem.pdf)

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
