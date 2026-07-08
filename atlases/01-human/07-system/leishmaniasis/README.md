---
schema: human-scale-entry/v1
id: leishmaniasis
name: Leishmaniasis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Leishmaniasis (Leishmania spp.; sand fly vector) causes cutaneous (CL), mucocutaneous (MCL), and visceral (VL/kala-azar) disease; IL-12/IFN-γ/iNOS axis controls Leishmania in macrophages; liposomal amphotericin B (L-AmB) is first-line for VL; miltefosine is the only oral agent."
aliases: ["kala-azar", "visceral leishmaniasis", "cutaneous leishmaniasis", "mucocutaneous leishmaniasis", "VL", "CL", "MCL", "PKDL", "Leishmania", "black fever", "dumdum fever"]
sources:
  - id: scott-2016-leishmaniasis-immunity
    type: peer-reviewed
    cite: "Scott P, Novais FO. Cutaneous leishmaniasis: immune responses in protection and pathogenesis. Nat Rev Immunol. 2016;16(9):581-592."
    doi: "10.1038/nri.2016.72"
    pmid: "27424773"
    url: "https://doi.org/10.1038/nri.2016.72"
    accessed: "2026-06-08"
  - id: who-2022-leishmaniasis-guideline
    type: clinical-guideline
    cite: "World Health Organization. Leishmaniasis. WHO Fact Sheet. Geneva: WHO; 2023."
    url: "https://www.who.int/news-room/fact-sheets/detail/leishmaniasis"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "TLR4-MyD88 signalling on macrophages initiates anti-Leishmania innate response: LPG → TLR4 → NF-κB → TNF-α + IL-12; however, L. donovani subverts TLR2 to suppress IL-12 production and promote parasite survival; TLR4-deficient mice are more susceptible to visceral leishmaniasis."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "IL-12 is the pivotal cytokine determining resistance vs. susceptibility to Leishmania: Th1 response (IL-12 → IFN-γ → iNOS → NO) eliminates intracellular parasites; IL-12 deficiency (MSMD) → disseminated cutaneous Leishmania; IL-12 genetic polymorphisms influence disease severity."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "HIV-AIDS reactivates visceral leishmaniasis in co-endemic regions: CD4+ depletion → Leishmania escapes macrophage control → disseminated VL; HIV-VL co-infection is a leading opportunistic parasitosis in Mediterranean Europe, East Africa, and the Indian subcontinent."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: damages
    note: "Visceral leishmaniasis causes severe ACD: chronic Leishmania infection → IL-6 + IFN-γ + TNF-α → hepcidin elevation → profound hypoferraemia; VL anemia is compounded by direct parasite infiltration of bone marrow, hypersplenism, and haemolysis; L-AmB treatment resolves ACD."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "IFN-γ from Th1 T cells and NK cells is the key anti-Leishmania effector: IFN-γ → iNOS → nitric oxide → kills intracellular Leishmania in macrophages; IFNGR deficiency (MSMD) → VL; IFN-γ also upregulates MHC-II on macrophages for better T cell priming."
  - target: 02-pathogen/04-parasites/leishmania-donovani
    relation: connects-to
    note: "Leishmania donovani, delivered by sand-fly bite, causes visceral leishmaniasis: promastigotes become amastigotes that survive inside macrophage phagolysosomes using LPG and gp63 to dodge the oxidative burst; single-dose liposomal amphotericin B now cures >95% in South Asia."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "The macrophage is both Leishmania's hideout and its executioner: parasites enter via complement receptors without triggering the oxidative burst and suppress IL-12, but a Th1 IL-12→IFN-γ→iNOS response makes nitric oxide that kills the amastigotes."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "Visceral leishmaniasis floods the spleen with parasitized macrophages, producing the massive splenomegaly of kala-azar; hypersplenism plus marrow infiltration drives pancytopenia, and splenic aspirate is the most sensitive diagnostic test despite bleeding risk."
  - target: 01-human/07-system/malaria
    relation: connects-to
    note: "Both are vector-borne protozoa of the tropics: sand-fly-borne Leishmania parasitizes macrophages while mosquito-borne Plasmodium invades erythrocytes; both cause fever, massive splenomegaly and anemia in overlapping endemic regions, and HIV co-infection reactivates VL."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Cutaneous leishmaniasis is the skin form: sand-fly inoculation into the dermis → localized macrophage infection → chronic ulcer that scars; mucocutaneous L. braziliensis destroys nasal/oral mucosa; post-kala-azar dermal leishmaniasis follows visceral cure and sustains spread."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "The Th1/Th2 balance decides Leishmania outcome: Th1 (IL-12→IFN-γ→iNOS→NO) clears intracellular amastigotes and gives healing immunity, while Th2 (IL-4, IL-10) permits parasite persistence and progressive disease; the textbook model of CD4+ T-helper polarization."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Visceral leishmaniasis (kala-azar) is a reticuloendothelial disease with the liver a prime target: Leishmania-laden macrophages expand the liver and spleen, causing massive hepatosplenomegaly, while hypergammaglobulinemia and hypoalbuminemia reflect the parasite burden."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "The bone marrow is invaded in visceral leishmaniasis: amastigote-laden macrophages crowd the marrow, causing pancytopenia (anemia, leukopenia, thrombocytopenia), and a marrow or splenic aspirate showing amastigotes is a classic diagnostic test for kala-azar."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells determine whether leishmaniasis is controlled or progresses: by presenting Leishmania antigen and producing IL-12, they steer CD4 cells toward a protective Th1/IFN-γ response, so impaired DC function tips toward Th2 and disseminated disease."
  - target: 01-human/07-system/tuberculosis
    relation: connects-to
    note: "Leishmaniasis and tuberculosis are both chronic intracellular infections of the macrophage controlled by Th1 immunity: each hides inside the very cell meant to kill it, requiring IFN-γ-driven macrophage activation—so both flare in HIV."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Natural killer cells shape early defense against Leishmania: NK-derived IFN-γ helps polarize the protective Th1 response that activates infected macrophages to kill the parasite, so weak NK/Th1 immunity allows the visceral disease (kala-azar) to progress."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Regulatory T cells let Leishmania persist: by dampening the protective Th1 response, Tregs allow the parasite to survive inside macrophages, contributing to chronic and relapsing infection and to reactivation in immunosuppression."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Leishmaniasis outcome hinges on the immune response type: a Th1/IFN-gamma response controls the parasite, while a Th2/IL-10 shift lets it disseminate—so whether infection stays a self-healing skin sore or becomes lethal visceral disease depends on immune polarization."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Macrophages kill Leishmania with nitric oxide—or fail to: IFN-gamma-activated macrophages use inducible NO synthase to destroy the parasite, but Leishmania survives by suppressing NO production inside the very cell meant to kill it, the heart of its immune evasion."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils are Leishmania's Trojan horse: sandfly-injected parasites first enter neutrophils, then ride apoptotic neutrophils silently into macrophages—their true replicative niche—so the early innate response is subverted to establish infection."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Visceral leishmaniasis floods the blood with antibody: chronic infection drives polyclonal B-cell activation and hypergammaglobulinemia, yet this humoral response cannot clear the intracellular parasite—so control needs T cells, and the antibodies mainly aid diagnosis."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Visceral leishmaniasis crashes the blood counts: parasite-packed macrophages enlarge the spleen and crowd the marrow, so platelets, red cells, and white cells all fall—the pancytopenia and bleeding of kala-azar that makes advanced disease so dangerous."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Leishmaniasis is a disease of the reticuloendothelial system: the parasite colonizes macrophages in lymphatic tissue, spleen, liver, and marrow, causing lymphadenopathy and organomegaly—so visceral leishmaniasis spreads along the mononuclear-phagocyte network."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Leishmaniasis turns on whether immunity goes Th1 or Th2: IL-10 (with IL-4) suppresses the protective IFN-gamma/IL-12 response, letting parasites survive inside macrophages—so high IL-10 marks progressive visceral disease and is a target for immunotherapy."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Visceral leishmaniasis crashes the blood counts: parasite infiltration of marrow plus an enlarged spleen destroying cells causes anemia and pancytopenia, with low red cells (and platelets and white cells) a hallmark of kala-azar."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Leishmania fights macrophages over iron: the parasite scavenges host iron to grow inside macrophages, while the host tries to withhold it—so iron handling is a battleground that shapes infection and contributes to the anemia of visceral disease."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Visceral leishmaniasis floods the blood with IgG: chronic infection drives massive polyclonal hypergammaglobulinemia—largely non-protective antibody—so a high globulin level is a classic clue to kala-azar even as cellular immunity fails."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Leishmaniasis is decided by the Th1-Th2 balance, and IL-4 picks the losing side: an IL-4-driven Th2 response lets the parasite survive inside macrophages, whereas the IL-12/IFN-γ Th1 response clears it—the textbook model of this split."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "Visceral leishmaniasis swells the liver: the parasite infects macrophages throughout the liver and spleen, enlarging both organs (hepatosplenomegaly) and crowding the hepatocytes—the massive spleen and liver being hallmarks of kala-azar."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Visceral leishmaniasis can attack the kidneys: chronic infection deposits immune complexes in the glomeruli, causing protein-losing nephritis and acute kidney injury that worsen the outlook in severe kala-azar."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Macrophages try to kill Leishmania with oxygen: the respiratory burst forges reactive oxygen species to destroy the engulfed parasite, but the organism dampens this oxidative killing to survive inside the very cell meant to clear it."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "TNF-α arms macrophages against Leishmania but also wastes the body: it helps drive parasite killing, yet in chronic visceral disease its excess fuels the fever, wasting, and cachexia that make kala-azar so debilitating."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Leishmaniasis is found under the light microscope: Giemsa-stained smears reveal amastigotes packed inside macrophages, and small cutaneous lesions can be treated locally with heat or laser light."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Chronic visceral leishmaniasis scars the organs it invades: long-standing infection of the liver and spleen drives fibrosis, contributing to the portal hypertension and organ enlargement of advanced kala-azar."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Visceral leishmaniasis floods the blood with antibody: plasma cells pour out immunoglobulin in a massive polyclonal response, the hypergammaglobulinemia behind its classic non-specific protein tests."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reveals the parasite hiding inside our cells: Leishmania amastigotes pack the cytoplasm of macrophages as Donovan bodies, each with a nucleus and a bar-shaped kinetoplast — the rod of mitochondrial DNA that fingerprints the genus."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Visceral leishmaniasis quietly drops the sodium: an SIADH-like state of inappropriate water retention causes hyponatremia, a common laboratory clue in the chronic wasting illness of kala-azar."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "The lungs can be drawn in too: visceral leishmaniasis may cause an interstitial pneumonitis, and in HIV co-infection the parasite spreads to unusual sites including the airways, broadening its reach beyond spleen and marrow."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "The cure can stress the heart: the pentavalent antimonials long used against leishmaniasis prolong the QT interval and risk arrhythmia, so ECGs are watched during treatment of this otherwise-fatal infection."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "Antileishmanial drugs can inflame the pancreas: antimonials and pentamidine both cause chemical pancreatitis, and pentamidine can damage the islet cells enough to trigger hypoglycemia then diabetes."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Visceral leishmaniasis floods the blood with antibody: relentless B-cell stimulation produces a striking polyclonal hypergammaglobulinemia, and the anti-rK39 antibody test has become a rapid bedside diagnosis for kala-azar."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "The parasite turns complement into a Trojan horse: C3b coats the promastigote and, instead of killing it, ushers it through complement receptors into the macrophage where it safely multiplies — an elegant subversion of innate immunity."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Healing and destruction both scar: cutaneous lesions resolve through fibroblast-laid collagen into disfiguring marks, while mucocutaneous disease erodes the soft tissue and cartilage of the nose and mouth into devastating deformity."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "In the immunocompromised the gut joins in: HIV-associated visceral leishmaniasis can colonize the small-bowel mucosa, the amastigote-laden macrophages causing diarrhea and malabsorption as the parasite spreads beyond its usual organs."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "CD8 T cells cut both ways in leishmaniasis: their IFN-γ helps macrophages kill the parasite, but in chronic and post-kala-azar dermal disease their cytotoxic attack drives tissue damage, so they protect and injure depending on the setting."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Visceral leishmaniasis runs hot with IL-6: the cytokine surge fuels the polyclonal B-cell activation and hypergammaglobulinemia of kala-azar, and high IL-6 marks the systemic inflammation and poor outcome of severe disease."
  - target: 01-human/07-system/aplastic-anemia
    relation: connects-to
    note: "Kala-azar mimics marrow failure: fever with pancytopenia and a big spleen makes visceral leishmaniasis a key tropical differential of aplastic anemia, but here the marrow teems with parasitized macrophages rather than standing empty."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Most deaths come from other germs: visceral leishmaniasis cripples immunity and empties the blood counts, so patients succumb to secondary bacterial infections and sepsis — the proximate killer behind the parasite."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Inflammation locks away the iron: the chronic immune activation of kala-azar drives hepcidin up, trapping iron in macrophages and starving red-cell production — a key mechanism of the anemia that accompanies its huge spleen."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "The fight starts at the bite: mast cells in the skin at the sandfly bite shape the earliest immune response to Leishmania, influencing whether the parasite is contained as a local sore or disseminates to the organs."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "The parasite silences the macrophage's alarm: Leishmania actively blocks NF-κB activation in the very cell it lives in, shutting down the nitric-oxide and cytokine killing program so it can survive inside the phagosome."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "It flips the macrophage to a tolerant state through STAT3: by inducing IL-10, Leishmania drives STAT3 signaling that deactivates the macrophage, a key switch toward the non-healing, parasite-permissive response of visceral disease."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "An immunosuppressive cytokine helps it persist: Leishmania induces TGF-β that dampens protective Th1 immunity and promotes parasite survival, tilting the balance toward progressive, disseminated infection."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Both disease and drug strain the kidney: visceral leishmaniasis can deposit immune complexes in the glomeruli, and amphotericin B — its mainstay treatment — is nephrotoxic, together threatening chronic kidney injury."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: connects-to
    note: "It deepens immune collapse: visceral leishmaniasis, especially with HIV co-infection, profoundly suppresses cellular immunity, opening the door to opportunistic infections like Pneumocystis pneumonia."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Its old drugs are hard on the heart: pentavalent antimonials used for leishmaniasis cause QT prolongation and cardiotoxicity, and profound anemia of advanced visceral disease can drive high-output cardiac strain."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Its skin lesions ulcerate and scar: cutaneous leishmaniasis produces chronic non-healing ulcers, and the mucocutaneous form destroys nasal and oral tissue, leaving disfiguring scars that heal slowly."
  - target: 01-human/07-system/disseminated-intravascular-coagulation
    relation: connects-to
    note: "Advanced visceral disease can derange clotting: severe kala-azar with its hepatosplenic involvement, thrombocytopenia and secondary sepsis can tip into disseminated intravascular coagulation and bleeding."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A disfiguring, chronic disease weighs on the mind: the visible scarring of cutaneous and mucocutaneous leishmaniasis and the debilitating course of visceral disease carry stigma and contribute to depression."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Its commonest form is a skin disease: cutaneous leishmaniasis produces chronic ulcerating skin lesions that scar, and post-kala-azar dermal leishmaniasis seeds the skin with parasite-laden nodules."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Visceral disease swells the gut organs: kala-azar grossly enlarges the liver and spleen, while mucocutaneous leishmaniasis destroys the mucosa of the mouth, nose and pharynx."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Disfigurement and chronic illness breed worry: the visible facial scarring, social stigma and prolonged debilitating course of leishmaniasis foster chronic anxiety alongside depression."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It can devour the upper airway: mucocutaneous leishmaniasis (espundia) erodes the nose, pharynx and larynx months to years after the skin lesion, threatening the airway and disfiguring the face."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Visceral disease reaches the kidney: kala-azar can cause immune-complex glomerulonephritis and interstitial nephritis, and nephrotoxic amphotericin therapy further strains renal function."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its old drugs are hard on the heart: pentavalent antimonial treatment causes QT prolongation and arrhythmias requiring ECG monitoring, and severe visceral disease can be complicated by myocarditis."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Visceral disease fills the marrow: kala-azar infiltrates the bone marrow causing pancytopenia, and immune-complex arthritis can accompany the infection."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Chronic infection stunts growth and hormones: long-standing visceral leishmaniasis causes growth retardation and hypogonadism in affected children."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "It can pass to the unborn: visceral leishmaniasis can be transmitted congenitally and tends to worsen with the immune changes of pregnancy."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It can reach the nervous system: rare cases of leishmaniasis involve the central or peripheral nerves, and the antimonial and amphotericin drugs used against it carry neurological side-effects."
  - target: 02-pathogen/06-environmental/zoonosis
    relation: connects-to
    note: "It is a vector-borne zoonosis: Leishmania is transmitted by sandflies from animal reservoirs such as dogs and rodents, so its control links human and animal health."
  - target: 02-pathogen/02-bacteria/mycobacterium-tuberculosis
    relation: connects-to
    note: "It opens the door to TB: the profound immunosuppression of visceral leishmaniasis can reactivate latent tuberculosis, and the two infections are co-endemic in many regions."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "An oncology drug repurposed: miltefosine, the first oral drug for visceral leishmaniasis, began as an anticancer alkylphosphocholine, and conversely chemotherapy-induced immunosuppression can reactivate latent Leishmania."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "It drives massive antibody output: visceral leishmaniasis hyperactivates B cells in germinal centres, producing the striking polyclonal hypergammaglobulinaemia and reactive lymphoid hyperplasia that accompany the parasite burden."
  - target: 02-pathogen/04-parasites/trypanosoma-cruzi
    relation: connects-to
    note: "A related kinetoplastid parasite: Leishmania and Trypanosoma cruzi are both vector-borne kinetoplastid protozoa that survive inside host cells, sharing biology that makes both notoriously hard to drug."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "It parasitizes the liver's macrophages: visceral leishmaniasis fills the Kupffer cells of the hepatic lobule with amastigotes, driving the granulomatous response and massive hepatomegaly of kala-azar."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "It immune-complexes the kidney: chronic visceral leishmaniasis deposits immune complexes in the glomerulus, causing glomerulonephritis and proteinuria as part of its multi-organ disease."
  - target: 01-human/07-system/myelofibrosis
    relation: connects-to
    note: "A great mimic of blood cancer: visceral leishmaniasis causes massive splenomegaly, pancytopenia and marrow infiltration that mimic myelofibrosis and other haematological malignancies, delaying diagnosis in non-endemic areas."
  - target: 01-human/07-system/hodgkin-lymphoma
    relation: connects-to
    note: "A lymphoma mimic: visceral leishmaniasis causes fever, weight loss and massive splenomegaly that closely mimic Hodgkin lymphoma, and immunosuppression for lymphoma can in turn unmask latent infection."
  - target: 01-human/07-system/multiple-myeloma
    relation: connects-to
    note: "Polyclonal gammopathy, not myeloma: visceral leishmaniasis floods the blood with polyclonal IgG, a benign hypergammaglobulinaemia that must be distinguished from the monoclonal paraprotein spike of multiple myeloma."
  - target: 01-human/07-system/iga-nephropathy
    relation: connects-to
    note: "Immune-complex kidney injury: the enormous antibody load of visceral leishmaniasis deposits immune complexes in the glomeruli, causing a glomerulonephritis that can include mesangial IgA deposition."
  - target: 01-human/07-system/cytokine-storm
    relation: connects-to
    note: "A trigger of HLH: visceral leishmaniasis is a classic infectious cause of secondary haemophagocytic lymphohistiocytosis, a cytokine storm of activated macrophages devouring blood cells, with fever, cytopenias and organ failure."
  - target: 02-pathogen/04-parasites/trypanosoma-brucei
    relation: connects-to
    note: "Fellow kinetoplastid: like Leishmania and Trypanosoma cruzi, Trypanosoma brucei is a kinetoplastid protozoan causing a major neglected tropical disease (sleeping sickness), sharing antigenic-variation immune evasion."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Opportunism and disruption: the immunosuppression of severe COVID-19 and its treatments can unmask visceral leishmaniasis, while the pandemic disrupted control of this neglected disease in endemic regions."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "Macrophage killing switch: IFN-γ signals through STAT1 to arm macrophages with nitric oxide against intracellular Leishmania, the core of the protective Th1 response."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Double-edged inflammasome: NLRP3-inflammasome activation and IL-1β shape the macrophage response to Leishmania, contributing to both parasite control and immunopathology."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Detrimental interferon: type I interferon can impair host defence in visceral leishmaniasis, skewing macrophages away from effective parasite killing."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Monocyte recruitment: CCL2 draws inflammatory monocytes to sites of Leishmania infection, replenishing the macrophage pool the parasite exploits as its replicative niche while contributing to granuloma formation."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "Th17 balance: IL-17A from Th17 cells modulates outcome in leishmaniasis, contributing to neutrophil-driven protection in some settings and to lesion immunopathology in cutaneous disease."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Cytotoxic immunopathology: CD8 T-cell perforin-mediated cytotoxicity drives much of the tissue destruction in cutaneous leishmaniasis, damaging infected and bystander skin cells rather than clearing the parasite."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Antigen-presentation evasion: Leishmania amastigotes downregulate MHC class II on the infected macrophage and degrade loaded peptides, blunting CD4 T-cell recognition so the parasite survives within the very cell meant to present it."
  - target: 01-human/03-molecular/ferroportin
    relation: connects-to
    note: "Iron tug-of-war: Leishmania scavenges iron inside the macrophage, and host control via ferroportin and the NRAMP1 transporter that withholds iron from the phagosome is a key determinant of resistance to infection."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic sensing: parasite DNA reaching the cytosol activates cGAS-STING, an innate sensing pathway that shapes the type-I-interferon response which can paradoxically favour Leishmania persistence in visceral disease."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "PGE2 immune subversion: Leishmania induces macrophage prostaglandin E2 that suppresses microbicidal activity and biases the response toward a permissive Th2 state, an eicosanoid arm of the immune evasion that lets the parasite survive inside the macrophage."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Purinergic evasion: Leishmania surface ecto-nucleotidases hydrolyse host nucleotides to generate immunosuppressive adenosine, dampening macrophage and T-cell activation to create the tolerant niche the parasite needs to establish infection."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Cholesterol parasitism: Leishmania scavenges and depletes host-cell cholesterol, remodelling the macrophage membrane in ways that impair antigen presentation and microbicidal function, a lipid-metabolic dimension of its intracellular survival."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Th2 permissiveness: with the IL-4 already mapped, IL-13 drives the Th2 response that deactivates macrophage killing and permits Leishmania persistence, the immune polarisation that determines progression to visceral disease."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Host-cell subversion: Leishmania manipulates host macrophage PI3K-AKT signalling to suppress apoptosis and microbicidal function, securing the intracellular niche in which the amastigote survives and replicates."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Inflammasome double edge: inflammasome-driven IL-1β shapes the response to Leishmania with a context-dependent role in both parasite control and the immunopathology of the leishmaniases."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Protective innate signalling: TLR sensing of Leishmania (TLR4 mapped) through MyD88 to NF-κB (mapped) drives the IL-12/IFN-γ-dependent macrophage activation that controls the parasite; MyD88 deficiency causes susceptibility."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Immune subversion: Leishmania manipulates host MAPK-ERK signalling to dampen macrophage activation and IL-12 production, promoting its own intracellular survival."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Macrophage metabolism: mTOR-regulated macrophage metabolism and autophagy influence the balance between killing and harbouring intracellular Leishmania amastigotes."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Protective immunity against Leishmania depends on IFN-γ and IL-12 signalling through JAK-STAT (STAT1 mapped), the axis the parasite subverts to survive inside macrophages."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "The IL-23/IL-17 axis (IL-17A mapped) modulates the inflammatory response in cutaneous and mucocutaneous leishmaniasis, shaping lesion immunopathology."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α drives the glycolytic, antimicrobial macrophage program that constrains intracellular Leishmania, a metabolic determinant of parasite killing."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 recognises Leishmania surface glycoconjugates and modulates the macrophage inflammatory response that determines parasite control versus persistence."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β already mapped) drives the macrophage deactivation and immunosuppression that Leishmania exploits to survive intracellularly."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "Leishmania subverts macrophage PI3K-AKT signalling (AKT already mapped) to suppress the microbicidal program and promote its intracellular survival."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors regulate macrophage autophagy and antimicrobial gene programs that determine control versus persistence of intracellular Leishmania."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins released by recruited myeloid cells amplify the inflammation of cutaneous and visceral leishmaniasis lesions."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the macrophage inflammatory-versus-anti-inflammatory polarization that governs the intracellular survival of Leishmania."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling in infected macrophages modulates the phagosome and inflammatory response that Leishmania subverts."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Host autophagy participates in the intracellular control of Leishmania, a defense the parasite modulates to survive within macrophages."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK signaling, coupled to autophagy and metabolic reprogramming, shapes the macrophage's capacity to control intracellular Leishmania."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation and macrophage epigenetic reprogramming shape the host response to Leishmania."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven monocyte and macrophage recruitment shapes the granulomatous and cutaneous immune response to Leishmania."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the type-2 immune skewing that shapes susceptibility to Leishmania."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the leukocyte trafficking and granuloma organization of leishmaniasis."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "VEGF-driven angiogenesis and lymphangiogenesis participate in the lesion vascularization and remodeling of leishmaniasis."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Collagen deposition contributes to the tissue remodeling and scarring of cutaneous and mucocutaneous leishmaniasis."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the macrophage responses to leishmaniasis."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the T-cell activation of the immune response to leishmaniasis."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin participates in the macrophage activation and granulomatous response to leishmaniasis."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Visceral anaemia: visceral leishmaniasis (kala-azar) causes marked anaemia and pancytopenia from bone-marrow infiltration, haemolysis and splenic sequestration, and the falling haemoglobin is a hallmark of severe, untreated disease."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell expansion: IL-2-driven proliferation of Th1 cells sustains the interferon-gamma response (already mapped) that activates macrophages to kill Leishmania, and adequate T-cell immunity determines whether infection is controlled or progresses."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Intracellular survival: Leishmania modulates host macrophage calcium signalling to blunt microbicidal responses, and the parasite's own calcium-dependent processes are being explored as antileishmanial drug targets."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative burst: alongside nitric oxide (already mapped), macrophage-derived reactive oxygen species help kill intracellular Leishmania, and the parasite deploys antioxidant defences to survive this oxidative arm of the microbicidal response."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Nutritional immunity: the host restricts zinc and other metals to starve intracellular Leishmania, and adequate zinc also supports the Th1 response (IL-12 already mapped), so deficiency worsens susceptibility to the infection."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: connects-to
    note: "Immunosuppression and reactivation: corticosteroid therapy acting through the glucocorticoid receptor, like HIV (already mapped), suppresses the Th1 immunity that contains Leishmania, precipitating progression to or reactivation of visceral disease."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Malnutrition and susceptibility: undernutrition lowers leptin and impairs the Th1 immunity (IL-12 already mapped) that contains Leishmania, so malnourished children are far more likely to progress to visceral leishmaniasis, a link between nutrition and outcome."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Micronutrient immunity: selenium and its antioxidant selenoproteins support the macrophage (already mapped) killing and Th1 response against Leishmania (zinc already mapped), so micronutrient deficiency compounds susceptibility to the infection."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D and antimicrobial defence: vitamin D modulates the macrophage antimicrobial response and the Th1/Th2 balance (IL-4 already mapped), and its status influences the immunity that determines the outcome of Leishmania infection."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Copper nutritional immunity: the macrophage (already mapped) floods its phagosome with toxic copper to kill the intracellular Leishmania, part of the metal-poisoning host defence (zinc and selenium already mapped) against the parasite."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Antigen presentation and Th1 priming: dendritic cells take up Leishmania and present its antigen to prime the protective Th1 response (IL-12 and IFN-γ already mapped), a key early step in controlling the infection."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Early innate IFN-γ: natural killer cells provide an early source of IFN-γ (already mapped) in the innate response to Leishmania, helping activate the macrophages (already mapped) before the adaptive Th1 response matures."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 susceptibility: IL-5, with the Th2 cytokines (IL-4 and IL-13 already mapped), is part of the non-protective type-2 response that, when it dominates over the Th1 (IL-12 and IFN-γ already mapped), favours the non-healing susceptible phenotype of leishmaniasis."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Malnutrition and immunity: adiponectin, with leptin (already mapped), links the malnutrition common in endemic regions to the impaired immune response that worsens visceral leishmaniasis."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipokine milieu: resistin, with leptin and adiponectin (already mapped), is part of the adipokine milieu of the malnutrition-immunity axis that shapes the susceptibility to and severity of leishmaniasis."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Nutritional immunity zinc: the zinc nutrition shapes the immune response (the Th1 already-mapped function) to Leishmania; the zinc deficiency of malnutrition (leptin already mapped) worsens susceptibility, and topical zinc treats the cutaneous form."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Antioxidant selenium: the antioxidant selenoprotein status shapes the immune response and the oxidative (nitric oxide and xanthine oxidase already mapped) killing of Leishmania, the malnutrition deficiency worsening the outcome."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Sandfly-bite mast cells: the histamine from the mast cells recruited to the sandfly-bite inoculation site shapes the early inflammatory milieu that the Leishmania parasite exploits to establish infection."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Hypergammaglobulinaemia IgE: the polyclonal B-cell (already mapped) activation of the visceral leishmaniasis raises the IgE, part of the Th2 (IL-4, IL-5 and IL-13 already mapped) non-protective response."
  - target: 01-human/03-molecular/secretory-iga
    relation: connects-to
    note: "Mucosal IgA: the secretory IgA of the mucosal immunity is relevant to the mucocutaneous leishmaniasis and the mucosal barrier response to the parasite."
  - target: 01-human/03-molecular/il-36
    relation: connects-to
    note: "Epithelial IL-36: the IL-36 of the keratinocytes amplifies the skin inflammation of the cutaneous leishmaniasis lesion, part of the innate cutaneous response."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Iron acquisition: the intracellular Leishmania scavenges host iron via the transferrin-bound iron of the macrophage (already mapped), and this iron competition (hepcidin and ferroportin already mapped) shapes the parasite survival and the anaemia."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the C5 and its cleavage product C5a (with C3 already mapped) contribute to the opsonisation-mediated macrophage (already mapped) entry and the inflammatory response to Leishmania."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling modulates the macrophage (already mapped) response and the Th1/Th2 balance of the immune response to Leishmania."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement evasion: Leishmania recruits the host factor H to its surface to accelerate the decay of the C3 convertase (complement C3, C5 and C5aR1 already mapped), evading the complement lysis before the macrophage (already mapped) entry."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Cutaneous alarmin: TSLP, from the injured keratinocytes at the sandfly bite, contributes to the type-2 (IL-4 and IL-13 already mapped) skewing that favours the parasite persistence in cutaneous leishmaniasis."
  - target: 01-human/03-molecular/il-31
    relation: connects-to
    note: "Pruritus cytokine: IL-31, a type-2 (IL-4 and IL-13 already mapped) cytokine, is the pruritogenic effector of the itch of the cutaneous leishmaniasis lesions."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement regulation: the C1-esterase inhibitor regulates the classical and lectin complement pathways (C3, C5, C5aR1 and factor H already mapped) that opsonise Leishmania promastigotes, which the parasite exploits to enter its macrophage (already mapped) niche."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "Granuloma matrix: fibronectin, an extracellular-matrix glycoprotein, is part of the provisional matrix of the granuloma and the lesion of cutaneous leishmaniasis, and Leishmania exploits fibronectin-integrin binding for the macrophage entry."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Type-2 fibrosis: periostin, downstream of the type-2 (IL-4 and IL-13 already mapped) cytokines and TSLP (already mapped), is part of the fibrotic remodelling and scarring of the cutaneous leishmaniasis lesion."
---

# Leishmaniasis

## Overview

Leishmaniasis is a vector-borne protozoan disease caused by over 20 species of *Leishmania*, transmitted by the bite of female phlebotomine sand flies (*Phlebotomus* in Old World; *Lutzomyia* in New World). With 700,000–1,000,000 new cases annually and 26,000–65,000 deaths, leishmaniasis ranks second among fatal parasitic diseases after malaria. Disease manifests across a clinical spectrum — cutaneous (CL), mucocutaneous (MCL), and visceral (VL/kala-azar) — determined by *Leishmania* species, host immune genetics, and geographic setting. The IL-12/IFN-γ/iNOS Th1 axis is the critical host determinant of resistance versus progressive disease.

Leishmaniasis is a neglected tropical disease (NTD) affecting primarily impoverished populations in 88 countries. It is intimately linked to poverty, malnutrition, deforestation, and HIV co-infection. The WHO 2030 NTD Roadmap targets elimination of VL as a public health problem in South Asia and East Africa.

## Structure

### Parasite biology

*Leishmania* is a kinetoplastid protozoan with a two-stage lifecycle:

- **Promastigote** (extracellular, in sand fly): Motile, flagellated form; resides in sand fly midgut; inoculated into skin during blood meal
- **Amastigote** (intracellular, in mammalian host): Non-flagellated, oval; survives within acidic phagolysosomes (pH 4.5–5.5) of macrophages, dendritic cells, and neutrophils

Key surface virulence factors:
- **Lipophosphoglycan (LPG)**: Abundant promastigote surface glycolipid; inhibits phagosome maturation via PI3K blockade; TLR4 and TLR2 ligand
- **gp63 (leishmanolysin)**: Zinc metalloprotease; cleaves complement C3b → C3bi → CR3-mediated phagocytosis without oxidative burst activation; cleaves host proteins that trigger innate alarms
- **A2 protein**: Visceral-tropic survival factor; promotes amastigote tolerance of acidic lysosomes; absent in dermatotropic species

### Clinical forms

| Form | Species | Vector | Distribution |
|------|---------|--------|--------------|
| Cutaneous (CL) | *L. major*, *L. tropica*, *L. aethiopica* | *Phlebotomus* | Middle East, Central Asia, Africa |
| New World CL | *L. mexicana*, *L. braziliensis* | *Lutzomyia* | Latin America |
| Mucocutaneous (MCL) | *L. braziliensis* | *Lutzomyia* | South America |
| Visceral (VL/kala-azar) | *L. donovani*, *L. infantum* | *Phlebotomus* | South Asia, East Africa, Mediterranean |

## Function

### Macrophage subversion

*Leishmania* exploits macrophages as its primary intracellular niche:

1. **Entry**: Promastigotes bind CR3, FcγR, and mannose receptor → phagocytosis without activation of the oxidative burst (gp63 suppresses PKC signaling)
2. **Phagosome arrest**: LPG inserts into phagosome membrane → inhibits PI3K and Ca²⁺ signaling → delays phagolysosome fusion; amastigotes later adapt to and require the acidic environment for survival
3. **IL-12 suppression**: *L. donovani* triggers TLR2 ligation → MAPK/ERK activation → IL-12 p70 suppression; simultaneously activates STAT3 → IL-10 upregulation → regulatory/Th2 skew
4. **Antigen presentation sabotage**: Downregulation of MHC-II and CD80/CD86 on macrophages → impaired CD4+ T cell priming

### Th1 vs. Th2 immunity paradigm

The murine model (*L. major* in BALB/c vs. C57BL/6 mice) established the Th1/Th2 paradigm for infection immunity:

- **Th1 (resistance)**: IL-12 from DCs/macrophages → IFN-γ from NK cells and CD4+ T cells → iNOS induction → nitric oxide (NO) → kills intracellular amastigotes; IFN-γ also activates macrophage oxidative burst
- **Th2 (susceptibility)**: IL-4/IL-13 → alternative macrophage activation (arginase-1 upregulation vs. iNOS) → permissive intracellular environment; IL-10 suppresses IL-12 and IFN-γ (key driver of VL chronicity)
- **Regulatory axis**: Foxp3+ Tregs and IL-10-producing CD4+ T cells maintain parasite tolerance and PKDL

## Pathology

### Visceral leishmaniasis (kala-azar)

*L. donovani* and *L. infantum* disseminate from skin to liver, spleen, and bone marrow:

- **Hepatosplenomegaly**: Massive splenomegaly from reticuloendothelial hyperplasia and immune cell infiltration; spleen may reach the pelvis; Dunbar's sign (spleen extending to right iliac fossa) in severe cases
- **Pancytopenia**: Bone marrow infiltration by parasitized macrophages + hypersplenism → normocytic normochromic anemia, leukopenia, thrombocytopenia
- **Anemia of chronic disease**: IL-6 + TNF-α + IFN-γ → hepcidin induction → iron sequestration from erythroid precursors; compounded by haemolysis, BM suppression, and hypersplenism
- **Hypoalbuminaemia and edema**: Hepatic synthetic failure + severe protein-energy malnutrition → anasarca in terminal cases
- **Hypergammaglobulinaemia**: Polyclonal B cell activation → high IgG (may reach 50–60 g/L); non-protective antibodies (parasite survives despite high antibody titres); total protein elevated, albumin:globulin ratio inverted
- **PKDL**: Post-kala-azar dermal leishmaniasis — macular or nodular rash appearing 6 months to 3 years after VL treatment; dermal parasites serve as an anthroponotic reservoir; 5–50% of treated VL in South Asia; treated with miltefosine 12 weeks

### Mucocutaneous leishmaniasis

*L. braziliensis*: Metastatic spread from primary CL to nasopharyngeal mucosa (months to years later) → destructive granulomatous inflammation driven by paradoxically hyperactive Th1 response (high IFN-γ + TNF-α); disfiguring destruction of nose (tapir nose), lips, and palate; treated with pentavalent antimonials + liposomal AmB; miltefosine

### Diagnosis

- **rK39 rapid immunochromatographic test (ICT)**: Field-deployable serological test for VL; sensitivity ~97%, specificity ~97% in South Asia; less reliable in East Africa and HIV co-infection
- **Splenic aspirate culture**: Gold standard for VL diagnosis (sensitivity ~98%) but carries bleeding risk; bone marrow aspirate safer alternative (sensitivity ~70%)
- **PCR**: High sensitivity on peripheral blood (VL) and tissue biopsies (CL); useful in HIV co-infection where serology is unreliable
- **Skin slit smear or punch biopsy**: CL/PKDL diagnosis; Giemsa stain reveals amastigotes within macrophages; Leishman-Donovan bodies

### Treatment

| Disease | First-line | Alternative |
|---------|-----------|-------------|
| Visceral (South Asia) | Liposomal amphotericin B (L-AmB) single 10 mg/kg dose | Miltefosine 28 days (oral) |
| Visceral (East Africa) | L-AmB + miltefosine combination | SSG + paromomycin IM |
| Cutaneous | Meglumine antimoniate or SSG (intralesional/IM) | Miltefosine, fluconazole |
| Mucocutaneous | Pentavalent antimonials IM ± L-AmB | Miltefosine |
| PKDL | Miltefosine 12 weeks | SSG prolonged |

**Liposomal amphotericin B (L-AmB)**: Acts by binding ergosterol in *Leishmania* cell membrane → ion channel formation → osmotic lysis; single-dose 10 mg/kg IV achieves >95% cure in India; dramatically reduces treatment burden vs. 28-day regimens

**Miltefosine** (hexadecylphosphocholine): The only approved oral antileishmanial agent; mechanism involves disruption of *Leishmania* phospholipid metabolism and mitochondrial function; 28-day oral course; teratogenic (contraindicated in pregnancy, requires contraception); resistance emerging in South Asia due to uptake transporter mutations

**Pentavalent antimonials** (sodium stibogluconate/SSG, meglumine antimoniate): Prodrug activated to Sb(III) by *Leishmania* → inhibits trypanothione reductase; widespread SSG resistance in Bihar, India (>60% primary failure) has shifted first-line therapy to L-AmB in that region

### HIV co-infection

HIV-VL co-infection: CD4+ depletion → loss of IFN-γ production → *Leishmania* escapes macrophage control → disseminated VL with atypical organ involvement (GI tract, pleura, lungs). High relapse rates (>50%) post-treatment. ART partially restores Th1 immunity but rarely cures. Secondary prophylaxis with L-AmB monthly recommended while CD4 count <200 cells/μL.

## Connections

**→ [TLR4](../../../03-molecular/tlr4/)**: TLR4-MyD88 signalling on macrophages initiates anti-Leishmania innate response: LPG → TLR4 → NF-κB → TNF-α + IL-12; however, L. donovani subverts TLR2 to suppress IL-12 production and promote parasite survival; TLR4-deficient mice are more susceptible to visceral leishmaniasis.

**→ [IL-12](../../../03-molecular/il-12/)**: IL-12 is the pivotal cytokine determining resistance vs. susceptibility to Leishmania: Th1 response (IL-12 → IFN-γ → iNOS → NO) eliminates intracellular parasites; IL-12 deficiency (MSMD) → disseminated cutaneous Leishmania; IL-12 genetic polymorphisms influence disease severity.

**→ [HIV/AIDS](../hiv-aids/)**: HIV-AIDS reactivates visceral leishmaniasis in co-endemic regions: CD4+ depletion → Leishmania escapes macrophage control → disseminated VL; HIV-VL co-infection is a leading opportunistic parasitosis in Mediterranean Europe, East Africa, and the Indian subcontinent.

**→ [Anemia of Chronic Disease](../anemia-of-chronic-disease/)**: Visceral leishmaniasis causes severe ACD: chronic Leishmania infection → IL-6 + IFN-γ + TNF-α → hepcidin elevation → profound hypoferraemia; VL anemia is compounded by direct parasite infiltration of bone marrow, hypersplenism, and haemolysis; L-AmB treatment resolves ACD.

**→ [IFN-γ](../../../03-molecular/ifn-gamma/)**: IFN-γ from Th1 T cells and NK cells is the key anti-Leishmania effector: IFN-γ → iNOS → nitric oxide → kills intracellular Leishmania in macrophages; IFNGR deficiency (MSMD) → VL; IFN-γ also upregulates MHC-II on macrophages for better T cell priming.

- `connects-to` → **[Leishmania donovani](../../../02-pathogen/04-parasites/leishmania-donovani/README.md)** — Leishmania donovani, delivered by sand-fly bite, causes visceral leishmaniasis: promastigotes become amastigotes that survive inside macrophage phagolysosomes using LPG and gp63 to dodge the oxidative burst; single-dose liposomal amphotericin B now cures >95% in South Asia.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — The macrophage is both Leishmania's hideout and its executioner: parasites enter via complement receptors without triggering the oxidative burst and suppress IL-12, but a Th1 IL-12→IFN-γ→iNOS response makes nitric oxide that kills the amastigotes.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — Visceral leishmaniasis floods the spleen with parasitized macrophages, producing the massive splenomegaly of kala-azar; hypersplenism plus marrow infiltration drives pancytopenia, and splenic aspirate is the most sensitive diagnostic test despite bleeding risk.
- `connects-to` → **[Malaria](../malaria/README.md)** — Both are vector-borne protozoa of the tropics: sand-fly-borne Leishmania parasitizes macrophages while mosquito-borne Plasmodium invades erythrocytes; both cause fever, massive splenomegaly and anemia in overlapping endemic regions, and HIV co-infection reactivates VL.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Cutaneous leishmaniasis is the skin form: sand-fly inoculation into the dermis → localized macrophage infection → chronic ulcer that scars; mucocutaneous L. braziliensis destroys nasal/oral mucosa; post-kala-azar dermal leishmaniasis follows visceral cure and sustains spread.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — The Th1/Th2 balance decides Leishmania outcome: Th1 (IL-12→IFN-γ→iNOS→NO) clears intracellular amastigotes and gives healing immunity, while Th2 (IL-4, IL-10) permits parasite persistence and progressive disease; the textbook model of CD4+ T-helper polarization.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Visceral leishmaniasis (kala-azar) is a reticuloendothelial disease with the liver a prime target: Leishmania-laden macrophages expand the liver and spleen, causing massive hepatosplenomegaly, while hypergammaglobulinemia and hypoalbuminemia reflect the parasite burden.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — The bone marrow is invaded in visceral leishmaniasis: amastigote-laden macrophages crowd the marrow, causing pancytopenia (anemia, leukopenia, thrombocytopenia), and a marrow or splenic aspirate showing amastigotes is a classic diagnostic test for kala-azar.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells determine whether leishmaniasis is controlled or progresses: by presenting Leishmania antigen and producing IL-12, they steer CD4 cells toward a protective Th1/IFN-γ response, so impaired DC function tips toward Th2 and disseminated disease.
- `connects-to` → **[Tuberculosis](../tuberculosis/README.md)** — Leishmaniasis and tuberculosis are both chronic intracellular infections of the macrophage controlled by Th1 immunity: each hides inside the very cell meant to kill it, requiring IFN-γ-driven macrophage activation—so both flare in HIV.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Natural killer cells shape early defense against Leishmania: NK-derived IFN-γ helps polarize the protective Th1 response that activates infected macrophages to kill the parasite, so weak NK/Th1 immunity allows the visceral disease (kala-azar) to progress.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Regulatory T cells let Leishmania persist: by dampening the protective Th1 response, Tregs allow the parasite to survive inside macrophages, contributing to chronic and relapsing infection and to reactivation in immunosuppression.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Leishmaniasis outcome hinges on the immune response type: a Th1/IFN-gamma response controls the parasite, while a Th2/IL-10 shift lets it disseminate—so whether infection stays a self-healing skin sore or becomes lethal visceral disease depends on immune polarization.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — Macrophages kill Leishmania with nitric oxide—or fail to: IFN-gamma-activated macrophages use inducible NO synthase to destroy the parasite, but Leishmania survives by suppressing NO production inside the very cell meant to kill it, the heart of its immune evasion.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Neutrophils are Leishmania's Trojan horse: sandfly-injected parasites first enter neutrophils, then ride apoptotic neutrophils silently into macrophages—their true replicative niche—so the early innate response is subverted to establish infection.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — Visceral leishmaniasis floods the blood with antibody: chronic infection drives polyclonal B-cell activation and hypergammaglobulinemia, yet this humoral response cannot clear the intracellular parasite—so control needs T cells, and the antibodies mainly aid diagnosis.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Visceral leishmaniasis crashes the blood counts: parasite-packed macrophages enlarge the spleen and crowd the marrow, so platelets, red cells, and white cells all fall—the pancytopenia and bleeding of kala-azar that makes advanced disease so dangerous.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Leishmaniasis is a disease of the reticuloendothelial system: the parasite colonizes macrophages in lymphatic tissue, spleen, liver, and marrow, causing lymphadenopathy and organomegaly—so visceral leishmaniasis spreads along the mononuclear-phagocyte network.
- `connects-to` → **[Interleukin-10](../../03-molecular/il-10/README.md)** — Leishmaniasis turns on whether immunity goes Th1 or Th2: IL-10 (with IL-4) suppresses the protective IFN-gamma/IL-12 response, letting parasites survive inside macrophages—so high IL-10 marks progressive visceral disease and is a target for immunotherapy.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Visceral leishmaniasis crashes the blood counts: parasite infiltration of marrow plus an enlarged spleen destroying cells causes anemia and pancytopenia, with low red cells (and platelets and white cells) a hallmark of kala-azar.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Leishmania fights macrophages over iron: the parasite scavenges host iron to grow inside macrophages, while the host tries to withhold it—so iron handling is a battleground that shapes infection and contributes to the anemia of visceral disease.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — Visceral leishmaniasis floods the blood with IgG: chronic infection drives massive polyclonal hypergammaglobulinemia—largely non-protective antibody—so a high globulin level is a classic clue to kala-azar even as cellular immunity fails.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Leishmaniasis is decided by the Th1-Th2 balance, and IL-4 picks the losing side: an IL-4-driven Th2 response lets the parasite survive inside macrophages, whereas the IL-12/IFN-γ Th1 response clears it—the textbook model of this split.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — Visceral leishmaniasis swells the liver: the parasite infects macrophages throughout the liver and spleen, enlarging both organs (hepatosplenomegaly) and crowding the hepatocytes—the massive spleen and liver being hallmarks of kala-azar.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Visceral leishmaniasis can attack the kidneys: chronic infection deposits immune complexes in the glomeruli, causing protein-losing nephritis and acute kidney injury that worsen the outlook in severe kala-azar.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Macrophages try to kill Leishmania with oxygen: the respiratory burst forges reactive oxygen species to destroy the engulfed parasite, but the organism dampens this oxidative killing to survive inside the very cell meant to clear it.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — TNF-α arms macrophages against Leishmania but also wastes the body: it helps drive parasite killing, yet in chronic visceral disease its excess fuels the fever, wasting, and cachexia that make kala-azar so debilitating.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Leishmaniasis is found under the light microscope: Giemsa-stained smears reveal amastigotes packed inside macrophages, and small cutaneous lesions can be treated locally with heat or laser light.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Chronic visceral leishmaniasis scars the organs it invades: long-standing infection of the liver and spleen drives fibrosis, contributing to the portal hypertension and organ enlargement of advanced kala-azar.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — Visceral leishmaniasis floods the blood with antibody: plasma cells pour out immunoglobulin in a massive polyclonal response, the hypergammaglobulinemia behind its classic non-specific protein tests.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reveals the parasite hiding inside our cells: Leishmania amastigotes pack the cytoplasm of macrophages as Donovan bodies, each with a nucleus and a bar-shaped kinetoplast — the rod of mitochondrial DNA that fingerprints the genus.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Visceral leishmaniasis quietly drops the sodium: an SIADH-like state of inappropriate water retention causes hyponatremia, a common laboratory clue in the chronic wasting illness of kala-azar.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — The lungs can be drawn in too: visceral leishmaniasis may cause an interstitial pneumonitis, and in HIV co-infection the parasite spreads to unusual sites including the airways, broadening its reach beyond spleen and marrow.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — The cure can stress the heart: the pentavalent antimonials long used against leishmaniasis prolong the QT interval and risk arrhythmia, so ECGs are watched during treatment of this otherwise-fatal infection.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — Antileishmanial drugs can inflame the pancreas: antimonials and pentamidine both cause chemical pancreatitis, and pentamidine can damage the islet cells enough to trigger hypoglycemia then diabetes.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Visceral leishmaniasis floods the blood with antibody: relentless B-cell stimulation produces a striking polyclonal hypergammaglobulinemia, and the anti-rK39 antibody test has become a rapid bedside diagnosis for kala-azar.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — The parasite turns complement into a Trojan horse: C3b coats the promastigote and, instead of killing it, ushers it through complement receptors into the macrophage where it safely multiplies — an elegant subversion of innate immunity.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Healing and destruction both scar: cutaneous lesions resolve through fibroblast-laid collagen into disfiguring marks, while mucocutaneous disease erodes the soft tissue and cartilage of the nose and mouth into devastating deformity.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — In the immunocompromised the gut joins in: HIV-associated visceral leishmaniasis can colonize the small-bowel mucosa, the amastigote-laden macrophages causing diarrhea and malabsorption as the parasite spreads beyond its usual organs.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — CD8 T cells cut both ways in leishmaniasis: their IFN-γ helps macrophages kill the parasite, but in chronic and post-kala-azar dermal disease their cytotoxic attack drives tissue damage, so they protect and injure depending on the setting.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — Visceral leishmaniasis runs hot with IL-6: the cytokine surge fuels the polyclonal B-cell activation and hypergammaglobulinemia of kala-azar, and high IL-6 marks the systemic inflammation and poor outcome of severe disease.
- `connects-to` → **[Aplastic Anemia](../aplastic-anemia/README.md)** — Kala-azar mimics marrow failure: fever with pancytopenia and a big spleen makes visceral leishmaniasis a key tropical differential of aplastic anemia, but here the marrow teems with parasitized macrophages rather than standing empty.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Most deaths come from other germs: visceral leishmaniasis cripples immunity and empties the blood counts, so patients succumb to secondary bacterial infections and sepsis — the proximate killer behind the parasite.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Inflammation locks away the iron: the chronic immune activation of kala-azar drives hepcidin up, trapping iron in macrophages and starving red-cell production — a key mechanism of the anemia that accompanies its huge spleen.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — The fight starts at the bite: mast cells in the skin at the sandfly bite shape the earliest immune response to Leishmania, influencing whether the parasite is contained as a local sore or disseminates to the organs.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — The parasite silences the macrophage's alarm: Leishmania actively blocks NF-κB activation in the very cell it lives in, shutting down the nitric-oxide and cytokine killing program so it can survive inside the phagosome.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — It flips the macrophage to a tolerant state through STAT3: by inducing IL-10, Leishmania drives STAT3 signaling that deactivates the macrophage, a key switch toward the non-healing, parasite-permissive response of visceral disease.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — An immunosuppressive cytokine helps it persist: Leishmania induces TGF-β that dampens protective Th1 immunity and promotes parasite survival, tilting the balance toward progressive, disseminated infection.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Both disease and drug strain the kidney: visceral leishmaniasis can deposit immune complexes in the glomeruli, and amphotericin B — its mainstay treatment — is nephrotoxic, together threatening chronic kidney injury.
- `connects-to` → **[Pneumocystis jirovecii](../../../02-pathogen/03-fungi/pneumocystis-jirovecii/README.md)** — It deepens immune collapse: visceral leishmaniasis, especially with HIV co-infection, profoundly suppresses cellular immunity, opening the door to opportunistic infections like Pneumocystis pneumonia.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Its old drugs are hard on the heart: pentavalent antimonials used for leishmaniasis cause QT prolongation and cardiotoxicity, and profound anemia of advanced visceral disease can drive high-output cardiac strain.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Its skin lesions ulcerate and scar: cutaneous leishmaniasis produces chronic non-healing ulcers, and the mucocutaneous form destroys nasal and oral tissue, leaving disfiguring scars that heal slowly.
- `connects-to` → **[Disseminated Intravascular Coagulation](../disseminated-intravascular-coagulation/README.md)** — Advanced visceral disease can derange clotting: severe kala-azar with its hepatosplenic involvement, thrombocytopenia and secondary sepsis can tip into disseminated intravascular coagulation and bleeding.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A disfiguring, chronic disease weighs on the mind: the visible scarring of cutaneous and mucocutaneous leishmaniasis and the debilitating course of visceral disease carry stigma and contribute to depression.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Its commonest form is a skin disease: cutaneous leishmaniasis produces chronic ulcerating skin lesions that scar, and post-kala-azar dermal leishmaniasis seeds the skin with parasite-laden nodules.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Visceral disease swells the gut organs: kala-azar grossly enlarges the liver and spleen, while mucocutaneous leishmaniasis destroys the mucosa of the mouth, nose and pharynx.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Disfigurement and chronic illness breed worry: the visible facial scarring, social stigma and prolonged debilitating course of leishmaniasis foster chronic anxiety alongside depression.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It can devour the upper airway: mucocutaneous leishmaniasis (espundia) erodes the nose, pharynx and larynx months to years after the skin lesion, threatening the airway and disfiguring the face.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Visceral disease reaches the kidney: kala-azar can cause immune-complex glomerulonephritis and interstitial nephritis, and nephrotoxic amphotericin therapy further strains renal function.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its old drugs are hard on the heart: pentavalent antimonial treatment causes QT prolongation and arrhythmias requiring ECG monitoring, and severe visceral disease can be complicated by myocarditis.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Visceral disease fills the marrow: kala-azar infiltrates the bone marrow causing pancytopenia, and immune-complex arthritis can accompany the infection.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Chronic infection stunts growth and hormones: long-standing visceral leishmaniasis causes growth retardation and hypogonadism in affected children.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — It can pass to the unborn: visceral leishmaniasis can be transmitted congenitally and tends to worsen with the immune changes of pregnancy.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It can reach the nervous system: rare cases of leishmaniasis involve the central or peripheral nerves, and the antimonial and amphotericin drugs used against it carry neurological side-effects.
- `connects-to` → **[Zoonosis](../../../02-pathogen/06-environmental/zoonosis/README.md)** — It is a vector-borne zoonosis: Leishmania is transmitted by sandflies from animal reservoirs such as dogs and rodents, so its control links human and animal health.
- `connects-to` → **[Mycobacterium tuberculosis](../../../02-pathogen/02-bacteria/mycobacterium-tuberculosis/README.md)** — It opens the door to TB: the profound immunosuppression of visceral leishmaniasis can reactivate latent tuberculosis, and the two infections are co-endemic in many regions.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — An oncology drug repurposed: miltefosine, the first oral drug for visceral leishmaniasis, began as an anticancer alkylphosphocholine, and conversely chemotherapy-induced immunosuppression can reactivate latent Leishmania.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — It drives massive antibody output: visceral leishmaniasis hyperactivates B cells in germinal centres, producing the striking polyclonal hypergammaglobulinaemia and reactive lymphoid hyperplasia that accompany the parasite burden.
- `connects-to` → **[Trypanosoma cruzi](../../../02-pathogen/04-parasites/trypanosoma-cruzi/README.md)** — A related kinetoplastid parasite: Leishmania and Trypanosoma cruzi are both vector-borne kinetoplastid protozoa that survive inside host cells, sharing biology that makes both notoriously hard to drug.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — It parasitizes the liver's macrophages: visceral leishmaniasis fills the Kupffer cells of the hepatic lobule with amastigotes, driving the granulomatous response and massive hepatomegaly of kala-azar.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — It immune-complexes the kidney: chronic visceral leishmaniasis deposits immune complexes in the glomerulus, causing glomerulonephritis and proteinuria as part of its multi-organ disease.
- `connects-to` → **[Myelofibrosis](../myelofibrosis/README.md)** — A great mimic of blood cancer: visceral leishmaniasis causes massive splenomegaly, pancytopenia and marrow infiltration that mimic myelofibrosis and other haematological malignancies, delaying diagnosis in non-endemic areas.
- `connects-to` → **[Hodgkin Lymphoma](../hodgkin-lymphoma/README.md)** — A lymphoma mimic: visceral leishmaniasis causes fever, weight loss and massive splenomegaly that closely mimic Hodgkin lymphoma, and immunosuppression for lymphoma can in turn unmask latent infection.
- `connects-to` → **[Multiple Myeloma](../multiple-myeloma/README.md)** — Polyclonal gammopathy, not myeloma: visceral leishmaniasis floods the blood with polyclonal IgG, a benign hypergammaglobulinaemia that must be distinguished from the monoclonal paraprotein spike of multiple myeloma.
- `connects-to` → **[IgA Nephropathy](../iga-nephropathy/README.md)** — Immune-complex kidney injury: the enormous antibody load of visceral leishmaniasis deposits immune complexes in the glomeruli, causing a glomerulonephritis that can include mesangial IgA deposition.
- `connects-to` → **[Cytokine Storm](../cytokine-storm/README.md)** — A trigger of HLH: visceral leishmaniasis is a classic infectious cause of secondary haemophagocytic lymphohistiocytosis, a cytokine storm of activated macrophages devouring blood cells, with fever, cytopenias and organ failure.
- `connects-to` → **[Trypanosoma brucei](../../../02-pathogen/04-parasites/trypanosoma-brucei/README.md)** — Fellow kinetoplastid: like Leishmania and Trypanosoma cruzi, Trypanosoma brucei is a kinetoplastid protozoan causing a major neglected tropical disease (sleeping sickness), sharing antigenic-variation immune evasion.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Opportunism and disruption: the immunosuppression of severe COVID-19 and its treatments can unmask visceral leishmaniasis, while the pandemic disrupted control of this neglected disease in endemic regions.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — Macrophage killing switch: IFN-γ signals through STAT1 to arm macrophages with nitric oxide against intracellular Leishmania, the core of the protective Th1 response.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Double-edged inflammasome: NLRP3-inflammasome activation and IL-1β shape the macrophage response to Leishmania, contributing to both parasite control and immunopathology.
- `connects-to` → **[Type I Interferon](../../03-molecular/type-i-interferon/README.md)** — Detrimental interferon: type I interferon can impair host defence in visceral leishmaniasis, skewing macrophages away from effective parasite killing.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Monocyte recruitment: CCL2 draws inflammatory monocytes to sites of Leishmania infection, replenishing the macrophage pool the parasite exploits as its replicative niche while contributing to granuloma formation.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — Th17 balance: IL-17A from Th17 cells modulates outcome in leishmaniasis, contributing to neutrophil-driven protection in some settings and to lesion immunopathology in cutaneous disease.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Cytotoxic immunopathology: CD8 T-cell perforin-mediated cytotoxicity drives much of the tissue destruction in cutaneous leishmaniasis, damaging infected and bystander skin cells rather than clearing the parasite.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Leishmania amastigotes downregulate MHC class II on the infected macrophage and degrade loaded peptides, blunting CD4 T-cell recognition so the parasite survives within the very cell meant to present its antigens.
- `connects-to` → **[Ferroportin](../../03-molecular/ferroportin/README.md)** — Leishmania scavenges iron inside the macrophage, and host control via ferroportin and the NRAMP1 (SLC11A1) transporter that withholds iron from the phagosome is a key genetic determinant of resistance to infection.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Parasite DNA reaching the cytosol activates cGAS-STING, an innate sensing pathway that shapes the type-I-interferon response which can paradoxically favor Leishmania persistence in visceral disease rather than clearing it.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Leishmania induces macrophage prostaglandin E2 that suppresses microbicidal activity and biases the response toward a permissive Th2 state, an eicosanoid arm of the immune evasion that lets the parasite survive inside the macrophage.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Leishmania surface ecto-nucleotidases hydrolyze host nucleotides to generate immunosuppressive adenosine, dampening macrophage and T-cell activation to create the tolerant niche the parasite needs to establish infection.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Leishmania scavenges and depletes host-cell cholesterol, remodeling the macrophage membrane in ways that impair antigen presentation and microbicidal function, a lipid-metabolic dimension of its intracellular survival.
- `connects-to` → **[Interleukin-13](../../03-molecular/il-13/README.md)** — With the IL-4 already mapped, IL-13 drives the Th2 response that deactivates macrophage killing and permits Leishmania persistence, the immune polarization that determines progression to visceral disease.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Leishmania manipulates host macrophage PI3K-AKT signaling to suppress apoptosis and microbicidal function, securing the intracellular niche in which the amastigote survives and replicates.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Inflammasome-driven IL-1β shapes the response to Leishmania with a context-dependent role in both parasite control and the immunopathology of the leishmaniases.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR sensing of Leishmania (TLR4 mapped) through MyD88 to NF-κB (mapped) drives the IL-12/IFN-γ-dependent macrophage activation that controls the parasite; MyD88 deficiency causes susceptibility.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — Leishmania manipulates host MAPK-ERK signaling to dampen macrophage activation and IL-12 production, promoting its own intracellular survival.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR-regulated macrophage metabolism and autophagy influence the balance between killing and harboring intracellular Leishmania amastigotes.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Protective immunity against Leishmania depends on IFN-γ and IL-12 signaling through JAK-STAT (STAT1 mapped), the axis the parasite subverts to survive inside macrophages.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — The IL-23/IL-17 axis (IL-17A mapped) modulates the inflammatory response in cutaneous and mucocutaneous leishmaniasis, shaping lesion immunopathology.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α drives the glycolytic, antimicrobial macrophage program that constrains intracellular Leishmania, a metabolic determinant of parasite killing.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 recognizes Leishmania surface glycoconjugates and modulates the macrophage inflammatory response that determines parasite control versus persistence.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β already mapped) drives the macrophage deactivation and immunosuppression that Leishmania exploits to survive intracellularly.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — Leishmania subverts macrophage PI3K-AKT signaling (AKT already mapped) to suppress the microbicidal program and promote its intracellular survival.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors regulate macrophage autophagy and antimicrobial gene programs that determine control versus persistence of intracellular Leishmania.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins released by recruited myeloid cells amplify the inflammation of cutaneous and visceral leishmaniasis lesions.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the macrophage inflammatory-versus-anti-inflammatory polarization that governs the intracellular survival of Leishmania.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling in infected macrophages modulates the phagosome and inflammatory response that Leishmania subverts.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Host autophagy participates in the intracellular control of Leishmania, a defense the parasite modulates to survive within macrophages.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK signaling, coupled to autophagy and metabolic reprogramming, shapes the macrophage's capacity to control intracellular Leishmania.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation and macrophage epigenetic reprogramming shape the host response to Leishmania.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven monocyte and macrophage recruitment shapes the granulomatous and cutaneous immune response to Leishmania.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the type-2 immune skewing that shapes susceptibility to Leishmania.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the leukocyte trafficking and granuloma organization of leishmaniasis.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — VEGF-driven angiogenesis and lymphangiogenesis participate in the lesion vascularization and remodeling of leishmaniasis.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Collagen deposition contributes to the tissue remodeling and scarring of cutaneous and mucocutaneous leishmaniasis.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the macrophage responses to leishmaniasis.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the T-cell activation of the immune response to leishmaniasis.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin participates in the macrophage activation and granulomatous response to leishmaniasis.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Visceral anaemia: visceral leishmaniasis (kala-azar) causes marked anaemia and pancytopenia from bone-marrow infiltration, haemolysis and splenic sequestration, and the falling haemoglobin is a hallmark of severe, untreated disease.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell expansion: IL-2-driven proliferation of Th1 cells sustains the interferon-gamma response (already mapped) that activates macrophages to kill Leishmania, and adequate T-cell immunity determines whether infection is controlled or progresses.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Intracellular survival: Leishmania modulates host macrophage calcium signalling to blunt microbicidal responses, and the parasite's own calcium-dependent processes are being explored as antileishmanial drug targets.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative burst: alongside nitric oxide (already mapped), macrophage-derived reactive oxygen species help kill intracellular Leishmania, and the parasite deploys antioxidant defences to survive this oxidative arm of the microbicidal response.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Nutritional immunity: the host restricts zinc and other metals to starve intracellular Leishmania, and adequate zinc also supports the Th1 response (IL-12 already mapped), so deficiency worsens susceptibility to the infection.
- `connects-to` → **[Glucocorticoid receptor](../../03-molecular/glucocorticoid-receptor/README.md)** — Immunosuppression and reactivation: corticosteroid therapy acting through the glucocorticoid receptor, like HIV (already mapped), suppresses the Th1 immunity that contains Leishmania, precipitating progression to or reactivation of visceral disease.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Malnutrition and susceptibility: undernutrition lowers leptin and impairs the Th1 immunity (IL-12 already mapped) that contains Leishmania, so malnourished children are far more likely to progress to visceral leishmaniasis, a link between nutrition and outcome.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Micronutrient immunity: selenium and its antioxidant selenoproteins support the macrophage (already mapped) killing and Th1 response against Leishmania (zinc already mapped), so micronutrient deficiency compounds susceptibility to the infection.
- `connects-to` → **[Vitamin D](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D and antimicrobial defence: vitamin D modulates the macrophage antimicrobial response and the Th1/Th2 balance (IL-4 already mapped), and its status influences the immunity that determines the outcome of Leishmania infection.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Copper nutritional immunity: the macrophage (already mapped) floods its phagosome with toxic copper to kill the intracellular Leishmania, part of the metal-poisoning host defence (zinc and selenium already mapped) against the parasite.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Antigen presentation and Th1 priming: dendritic cells take up Leishmania and present its antigen to prime the protective Th1 response (IL-12 and IFN-γ already mapped), a key early step in controlling the infection.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Early innate IFN-γ: natural killer cells provide an early source of IFN-γ (already mapped) in the innate response to Leishmania, helping activate the macrophages (already mapped) before the adaptive Th1 response matures.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 susceptibility: IL-5, with the Th2 cytokines (IL-4 and IL-13 already mapped), is part of the non-protective type-2 response that, when it dominates over the Th1 (IL-12 and IFN-γ already mapped), favours the non-healing susceptible phenotype of leishmaniasis.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Malnutrition and immunity: adiponectin, with leptin (already mapped), links the malnutrition common in endemic regions to the impaired immune response that worsens visceral leishmaniasis.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipokine milieu: resistin, with leptin and adiponectin (already mapped), is part of the adipokine milieu of the malnutrition-immunity axis that shapes the susceptibility to and severity of leishmaniasis.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Nutritional immunity zinc: the zinc nutrition shapes the immune response (the Th1 already-mapped function) to Leishmania; the zinc deficiency of malnutrition (leptin already mapped) worsens susceptibility, and topical zinc treats the cutaneous form.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Antioxidant selenium: the antioxidant selenoprotein status shapes the immune response and the oxidative (nitric oxide and xanthine oxidase already mapped) killing of Leishmania, the malnutrition deficiency worsening the outcome.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Sandfly-bite mast cells: the histamine from the mast cells recruited to the sandfly-bite inoculation site shapes the early inflammatory milieu that the Leishmania parasite exploits to establish infection.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Hypergammaglobulinaemia IgE: the polyclonal B-cell (already mapped) activation of the visceral leishmaniasis raises the IgE, part of the Th2 (IL-4, IL-5 and IL-13 already mapped) non-protective response.
- `connects-to` → **[Secretory IgA](../../03-molecular/secretory-iga/README.md)** — Mucosal IgA: the secretory IgA of the mucosal immunity is relevant to the mucocutaneous leishmaniasis and the mucosal barrier response to the parasite.
- `connects-to` → **[IL-36](../../03-molecular/il-36/README.md)** — Epithelial IL-36: the IL-36 of the keratinocytes amplifies the skin inflammation of the cutaneous leishmaniasis lesion, part of the innate cutaneous response.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Iron acquisition: the intracellular Leishmania scavenges host iron via the transferrin-bound iron of the macrophage (already mapped), and this iron competition (hepcidin and ferroportin already mapped) shapes the parasite survival and the anaemia.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the C5 and its cleavage product C5a (with C3 already mapped) contribute to the opsonisation-mediated macrophage (already mapped) entry and the inflammatory response to Leishmania.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling modulates the macrophage (already mapped) response and the Th1/Th2 balance of the immune response to Leishmania.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement evasion: Leishmania recruits the host factor H to its surface to accelerate the decay of the C3 convertase (complement C3, C5 and C5aR1 already mapped), evading the complement lysis before the macrophage (already mapped) entry.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Cutaneous alarmin: TSLP, from the injured keratinocytes at the sandfly bite, contributes to the type-2 (IL-4 and IL-13 already mapped) skewing that favours the parasite persistence in cutaneous leishmaniasis.
- `connects-to` → **[IL-31](../../03-molecular/il-31/README.md)** — Pruritus cytokine: IL-31, a type-2 (IL-4 and IL-13 already mapped) cytokine, is the pruritogenic effector of the itch of the cutaneous leishmaniasis lesions.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement regulation: the C1-esterase inhibitor regulates the classical and lectin complement pathways (C3, C5, C5aR1 and factor H already mapped) that opsonise Leishmania promastigotes, which the parasite exploits to enter its macrophage (already mapped) niche.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — Granuloma matrix: fibronectin, an extracellular-matrix glycoprotein, is part of the provisional matrix of the granuloma and the lesion of cutaneous leishmaniasis, and Leishmania exploits fibronectin-integrin binding for the macrophage entry.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Type-2 fibrosis: periostin, downstream of the type-2 (IL-4 and IL-13 already mapped) cytokines and TSLP (already mapped), is part of the fibrotic remodelling and scarring of the cutaneous leishmaniasis lesion.
