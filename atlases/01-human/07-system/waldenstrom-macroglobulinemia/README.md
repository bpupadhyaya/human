---
schema: human-scale-entry/v1
id: waldenstrom-macroglobulinemia
name: Waldenström Macroglobulinemia
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Waldenström macroglobulinemia is lymphoplasmacytic lymphoma producing IgM monoclonal protein; MYD88 L265P in ~90% drives NF-κB and JAK-STAT3. Hyperviscosity, neuropathy, and cryoglobulinemia are hallmarks; ibrutinib and zanubrutinib are approved for MYD88 L265P WM."
aliases: ["Waldenström macroglobulinemia", "WM", "lymphoplasmacytic lymphoma", "LPL", "IgM monoclonal protein", "IgM paraprotein", "hyperviscosity syndrome", "MYD88 L265P WM"]
sources:
  - id: treon-2015-ibrutinib-wm
    type: peer-reviewed
    cite: "Treon SP, Tripsas CK, Meid K, et al. Ibrutinib in previously treated Waldenström's macroglobulinemia. N Engl J Med. 2015;373(18):1765-1774."
    doi: "10.1056/NEJMoa1501548"
    pmid: "26352686"
    url: "https://doi.org/10.1056/NEJMoa1501548"
  - id: tam-2020-aspen
    type: peer-reviewed
    cite: "Tam CS, Opat S, D'Sa S, et al. A randomized phase 3 trial of zanubrutinib vs ibrutinib in symptomatic Waldenström macroglobulinemia: the ASPEN study. Blood. 2020;136(18):2038-2050."
    doi: "10.1182/blood.2020006844"
    pmid: "32828187"
    url: "https://doi.org/10.1182/blood.2020006844"
cross_links:
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "MYD88 L265P → constitutive NF-κB via IRAK4-TRAF6-IKK → BCL-2, MYC, CXCR4 transcription; ibrutinib (BTK inhibitor) blocks BTK-dependent NF-κB in MYD88 L265P WM (ORR >90%); CXCR4 mutation (~35%) confers ibrutinib resistance (ORR ~60%)."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "MYD88 L265P drives JAK1-STAT3 → BCL-XL survival in WM independent of cytokine receptor signaling; ruxolitinib (JAK1/2 inhibitor) shows activity in MYD88 L265P WM; combined BTK+JAK inhibition studied in ibrutinib-resistant WM; JAK2 V617F absent in WM (unlike MPN)."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "BCL-2 overexpression is driven by MYD88/NF-κB → IRF4 in WM; venetoclax (BCL-2 inhibitor) shows activity in R/R WM; combined ibrutinib+venetoclax achieves deep responses in R/R WM; BCL-2 is an anti-apoptotic target complementary to BTK inhibition in WM."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "Rituximab ± bendamustine or cyclophosphamide is first-line for WM; rituximab monotherapy causes IgM flare (~40%) before response; ofatumumab and obinutuzumab are alternatives for rituximab-refractory WM; CD20 is uniformly expressed (CD19+/CD20+/sIgM+)."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCR4 gain-of-function mutations (WHIM-type S338X, C1013G) in 30-40% of WM → impaired receptor desensitization → enhanced CXCL12/CXCR4 bone marrow retention and resistance to BTK inhibitor ibrutinib; CXCR4 mutation status predicts ibrutinib response and PFS in WM."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Waldenström macroglobulinemia is a lymphoplasmacytic lymphoma — a clonal B-cell neoplasm frozen midway between a memory B cell and an IgM-secreting plasma cell; this dual identity gives it both surface CD20 and cytoplasmic IgM and shapes its B-cell-directed therapy."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "MYD88 L265P, present in ~90% of WM, is the defining and diagnostic mutation: it assembles a constitutive myddosome that fires NF-κB, JAK-STAT3, and BTK to keep the tumor alive, and its presence predicts response to BTK inhibitors — while MYD88-wildtype WM responds poorly."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "About half of WM patients with neuropathy have IgM anti-MAG antibodies that attack peripheral-nerve myelin, producing a distal, symmetric, sensory-predominant demyelinating neuropathy; lowering IgM with rituximab improves it in some, and titer tracks severity."
  - target: 01-human/07-system/multiple-myeloma
    relation: connects-to
    note: "Waldenström macroglobulinemia and myeloma are B-cell dyscrasias secreting a monoclonal paraprotein but differ: WM is a lymphoplasmacytic lymphoma making IgM (hyperviscosity, neuropathy) with MYD88 L265P, while myeloma is a marrow plasma-cell tumor making IgG/IgA with lytic bone."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "WM's malignant clone is lymphoplasmacytic—a spectrum from small B cells to plasma cells—so it secretes monoclonal IgM like a plasma-cell tumor while keeping B-cell markers (CD20); this dual differentiation explains why both rituximab and plasma-cell-directed agents work."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "WM characteristically infiltrates the bone marrow with lymphoplasmacytic cells, often paratrabecular and with increased mast cells; this marrow involvement causes anemia (the commonest symptom) and underlies the cytopenias, with diagnosis confirmed by marrow biopsy."
  - target: 01-human/07-system/follicular-lymphoma
    relation: connects-to
    note: "Waldenström macroglobulinemia and follicular lymphoma are both indolent B-cell non-Hodgkin lymphomas but molecularly distinct: WM is a lymphoplasmacytic lymphoma defined by MYD88 L265P and an IgM paraprotein, while follicular lymphoma is BCL2-translocated."
  - target: 01-human/07-system/dlbcl
    relation: connects-to
    note: "Waldenström macroglobulinemia can transform into aggressive diffuse large B-cell lymphoma: like other indolent lymphomas, the low-grade clone can acquire further lesions and evolve into DLBCL, a Richter-like transformation with rapid deterioration and worse prognosis."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Hyperviscosity from WM's IgM paraprotein can mimic or cause stroke: large pentameric IgM thickens blood, causing headache, visual blurring, and neurological deficits, so a stroke-like presentation with a very high protein points to WM, treated by plasmapheresis."
  - target: 01-human/07-system/mantle-cell-lymphoma
    relation: connects-to
    note: "Waldenström macroglobulinemia and mantle cell lymphoma are both B-cell non-Hodgkin lymphomas but distinct: WM is a lymphoplasmacytic lymphoma secreting IgM (MYD88 L265P) causing hyperviscosity, while MCL is a t(11;14) cyclin-D1 nodal tumor."
  - target: 01-human/07-system/cll
    relation: connects-to
    note: "Waldenström macroglobulinemia and CLL are indolent mature B-cell neoplasms: both involve small B cells and respond to BTK inhibitors, but WM's cells secrete monoclonal IgM while CLL circulates as a leukemia—immunophenotype and MYD88 separate them."
  - target: 01-human/07-system/hepatitis-c
    relation: connects-to
    note: "Hepatitis C links to Waldenström macroglobulinemia: chronic HCV-driven B-cell stimulation can progress to lymphoplasmacytic lymphoma, so HCV is screened for in IgM-secreting lymphomas—and antiviral cure can sometimes treat the lymphoproliferation."
  - target: 01-human/03-molecular/btk
    relation: connects-to
    note: "WM is exquisitely BTK-dependent: its hallmark MYD88 mutation signals through Bruton tyrosine kinase to drive malignant B-cell survival, so BTK inhibitors like ibrutinib are highly effective—response even predicted by MYD88 and CXCR4 genotype."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "WM's monoclonal IgM attacks red cells: it can act as a cold agglutinin that clumps and lyses erythrocytes, and marrow infiltration suppresses production, so anemia—often the presenting feature—comes from both hemolysis and crowded-out red-cell formation."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "WM is a classic cause of hyperviscosity retinopathy: the thick, IgM-laden blood engorges and tortuoses retinal veins ('sausage-link' veins) and can cause hemorrhages and blurred vision—an ophthalmoscopic clue that prompts urgent plasmapheresis."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Waldenström's IgM impairs platelets and bleeding: the huge monoclonal IgM coats platelets and clotting factors and thickens blood, so patients bruise and bleed—nosebleeds and mucosal bleeding—even as hyperviscosity paradoxically also risks clots and stroke."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "Waldenström's infiltrates the spleen and lymph nodes: the malignant lymphoplasmacytic cells expand beyond the marrow into the spleen and nodes, causing splenomegaly and lymphadenopathy that mark it as a lymphoma, not just a plasma-cell disorder."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Anemia is Waldenström's most common problem: marrow crowding by tumor cells plus chronic-disease and dilutional effects of the expanded plasma volume lower hemoglobin, so fatigue from anemia—not hyperviscosity—is usually what brings patients in."
  - target: 01-human/07-system/pcnsl
    relation: connects-to
    note: "Waldenstrom and primary CNS lymphoma share the MYD88 L265P mutation: when WM invades the brain it is called Bing-Neel syndrome, and the shared mutation makes both B-cell cancers responsive to BTK inhibitors that cross into the CNS."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Waldenstrom's IgM can turn on complement against red cells: as cold agglutinins or cryoglobulins, the paraprotein binds erythrocytes and fixes complement (C3), causing hemolysis—an extra anemia beyond marrow crowding."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Waldenstrom's marrow is studded with mast cells: increased mast cells are a characteristic histologic feature that support the lymphoplasmacytic clone through CD40-ligand and cytokines, part of the tumor's marrow microenvironment."
  - target: 01-human/03-molecular/albumin
    relation: connects-to
    note: "Waldenström's hallmark is hyperviscosity from monoclonal protein: the malignant clone floods blood with IgM that thickens it, inverting the normal albumin-to-globulin ratio and causing the bleeding, visual, and neurologic symptoms relieved by plasmapheresis."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Waldenström's cells survive on autophagy downstream of MYD88: constant MYD88/NF-κB signaling and heavy antibody output make the clone lean on autophagy to manage stress, a vulnerability alongside the BTK pathway that drugs target."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Waldenström evades immunity through regulatory T cells: the marrow accumulates Tregs and exhausted T cells that dampen the antitumor response, helping the slow-growing lymphoplasmacytic clone persist and limiting immunotherapy."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Waldenström can invade the brain: in rare Bing-Neel syndrome the lymphoplasmacytic cells seed the central nervous system, causing headaches, confusion, and neurological deficits that require treatments able to cross into the brain."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Waldenström blunts the body's iron use: marrow packed with the clone and chronic inflammation choke off red-cell production and lock away iron, so anemia—often the presenting complaint—dominates the disease."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Waldenström's thick IgM batters the endothelium: the sludgy, hyperviscous blood engorges and damages the vessel-lining cells, swelling retinal veins and causing the headaches, bleeding, and vision loss of hyperviscosity syndrome."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Waldenström's hyperviscosity shows in the eye: fundoscopy in visible light reveals dilated, sausage-segmented retinal veins, while CT photons map the lymph-node and spleen enlargement of the clone."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Waldenström spreads through the lymphatic organs: hepatomegaly and lymphadenopathy join the splenomegaly as the lymphoplasmacytic clone seeds beyond the bone marrow."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Waldenström's high IgM fools the lab: the excess protein displaces water in the blood sample, producing a spurious low sodium—pseudohyponatremia—that must not be wrongly corrected."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy captures Waldenström's hybrid cell: a lymphoplasmacytic cell caught between lymphocyte and plasma cell, its cytoplasm swollen with rough endoplasmic reticulum churning out IgM, sometimes with antibody packed into Dutcher bodies."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "The flood of IgM can injure the kidney: the antibody and its light chains deposit as casts, amyloid, or in the glomerulus, while hyperviscosity slows renal blood flow — routes by which Waldenström threatens kidney function."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Waldenström can surface on the skin: IgM deposits raise flesh-colored papules of macroglobulinemia cutis, and cryoglobulins precipitating in the cold inflame small vessels into the purpura of cryoglobulinemic vasculitis."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Waldenström is a disease of one antibody overmade: its clone pumps out monoclonal IgM that thickens the blood, and when that IgM happens to target myelin (anti-MAG), clump in the cold (cryoglobulin, cold agglutinin), it drives the syndrome's protean complications."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "The rogue IgM frays the nerves: anti-MAG antibodies strip myelin from peripheral neurons into a slowly progressive demyelinating neuropathy, and rarely the lymphoma itself invades the brain as Bing-Neel syndrome."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Thickened blood overworks the heart: the high IgM raises plasma viscosity and volume, and with the accompanying anemia the heart must pump harder, tipping toward high-output strain in hyperviscosity syndrome."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It is a lymphoma at heart: the lymphoplasmacytic clone of Waldenström infiltrates lymph nodes and spleen, so lymphadenopathy and splenomegaly accompany the marrow disease, marking its place among the indolent B-cell lymphomas."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "The clone can seed the gut: infiltration of the bowel wall by lymphoplasmacytic cells, and IgM deposition, cause malabsorption, diarrhea, and bleeding — an uncommon but recognized extramedullary face of the disease."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Marrow and treatment both lower the counts: the lymphoplasmacytic infiltrate crowds out normal blood production, and the chemo and BTK-inhibitor therapy add their own myelosuppression, dropping neutrophils and raising infection risk."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "The IgM can attack the nerves: in many patients it binds myelin-associated glycoprotein, stripping the peripheral nerves into a slow demyelinating neuropathy with numb, tingling, unsteady feet — sometimes the first sign of the disease."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 fuels the IgM factory: the cytokine pushes the malignant B cells toward plasma-cell differentiation and antibody output, helping sustain the monoclonal IgM that defines and harms in Waldenström's."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Rituximab leans on natural killer cells: the anti-CD20 antibody tags the tumor B cells for NK-mediated killing (ADCC), so the strength of the NK response shapes how well this mainstay therapy works."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "The MYD88 mutation feeds an autocrine loop: constitutive NF-κB signaling drives the tumor cells to secrete IL-10 and IL-6 that loop back to sustain their own growth, a survival circuit downstream of the defining mutation."
  - target: 01-human/07-system/immune-thrombocytopenia
    relation: connects-to
    note: "The monoclonal IgM turns on the body: it can act as an autoantibody, driving immune thrombocytopenia, cold agglutinin hemolysis and neuropathy — paraneoplastic phenomena that can dominate the picture more than the tumor bulk."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "The marrow niche nurtures the clone: supportive macrophages and mast cells in the bone marrow supply CD40L and APRIL signals that help the lymphoplasmacytic cells survive, part of the microenvironment targeted alongside the tumor."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "The driver mutation lights two fuses: MYD88 L265P fires not only NF-κB but also JAK-STAT3 signaling, a parallel survival pathway that sustains the Waldenström clone and is explored as a therapeutic target."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It reaches the nervous system in several ways: anti-MAG IgM causes peripheral neuropathy, hyperviscosity impairs the brain, and rarely the clone infiltrates the CNS directly as Bing-Neel syndrome."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Low normal antibodies leave a defense gap: the suppressed normal immunoglobulins of Waldenström, compounded by rituximab and BTK-inhibitor therapy, predispose to serious infection and sepsis."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Thick IgM-laden blood clots and bleeds: the hyperviscosity of Waldenström both impairs flow and, with its cancer-associated hypercoagulability, raises venous thromboembolism risk even as paraprotein can paradoxically cause bleeding."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "The IgM paraprotein can injure the kidney: deposition of monoclonal IgM and cryoglobulins in the glomeruli, plus hyperviscosity, can damage renal function and progress toward chronic kidney disease."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: connects-to
    note: "B-cell-directed therapy opens the lung: rituximab and BTK inhibitors used in Waldenström deplete immune defenses enough to risk Pneumocystis pneumonia, sometimes warranting prophylaxis during treatment."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Its BTK-inhibitor therapy admits invasive mold: ibrutinib, a mainstay for Waldenström, impairs macrophage and neutrophil antifungal defense, with a recognized risk of invasive aspergillosis."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Ibrutinib and hyperviscosity stress the heart: the BTK inhibitor central to Waldenström causes atrial fibrillation and cardiotoxicity, and the IgM-driven hyperviscosity raises high-output cardiac strain toward heart failure."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A chronic, incurable lymphoma weighs on mood: the indolent but relapsing course, lifelong monitoring and treatment burden of Waldenström contribute to depression and reduced quality of life."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "Its B-cell-targeted therapy reawakens shingles: rituximab and the BTK inhibitors used for Waldenström deplete B-cell and antiviral immunity, allowing latent varicella-zoster to reactivate."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Its abnormal IgM shows on the skin: Waldenström's monoclonal IgM can act as a cryoglobulin causing cold-induced purpura and acrocyanosis, and rarely deposits in the skin as IgM storm papules."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A chronic, relapsing, incurable lymphoma breeds worry: the indolent-but-watchful course, hyperviscosity scares and lifelong monitoring of Waldenström foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "It is a clonal antibody-making disease: lymphoplasmacytic cells secrete monoclonal IgM and suppress normal immunoglobulins, so Waldenström causes immunoparesis with infections alongside cryoglobulinaemia and cold agglutinin disease."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It can deposit in the gut: IgM and amyloid deposition in the bowel wall cause malabsorption and diarrhoea, and the disease commonly enlarges the liver and spleen."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It fills the marrow but spares the bones: Waldenström infiltrates the bone marrow with lymphoplasmacytic cells causing cytopenias, yet characteristically lacks the lytic bone lesions of multiple myeloma."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Thick blood and drugs strain the heart: IgM hyperviscosity raises cardiac workload toward high-output failure, ibrutinib causes atrial fibrillation, and AL amyloid can infiltrate the myocardium."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It can infiltrate the lungs: IgM and amyloid deposition can involve the lung parenchyma and pleura, and hyperviscosity causes breathlessness, alongside infection risk from immunoparesis."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Its IgM injures the kidney: monoclonal IgM, light chains and amyloid deposit in the glomeruli, and cryoglobulinaemia causes a membranoproliferative glomerulonephritis."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Precision drugs define modern care: BTK inhibitors (ibrutinib, zanubrutinib) exploit the MYD88 L265P mutation, and BCL-2 inhibitors add to them, transforming treatment of Waldenström macroglobulinaemia."
  - target: 02-pathogen/01-viruses/hepatitis-c-virus
    relation: connects-to
    note: "A virus that can seed the clone: chronic hepatitis C drives B-cell lymphoproliferation and cryoglobulinaemia, and is an associated antigenic trigger in a subset of IgM-secreting lymphomas like WM."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Chemoimmunotherapy remains a backbone: bendamustine combined with rituximab is a standard frontline regimen for symptomatic Waldenström macroglobulinaemia, alongside the newer targeted agents."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Born of the germinal-centre reaction: Waldenström cells are post-germinal-centre memory B cells carrying somatic hypermutation and the MYD88 L265P mutation, frozen midway between B cell and plasma cell as they secrete monoclonal IgM."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "Monoclonal IgM injures the kidney: type I cryoglobulinaemia and IgM deposition from Waldenström's can cause a membranoproliferative glomerulonephritis, and rarely IgM casts, spilling protein and blood into the urine."
  - target: 01-human/07-system/sjogrens-syndrome
    relation: connects-to
    note: "Autoimmunity can seed it: chronic B-cell stimulation in Sjögren's syndrome raises the risk of lymphoplasmacytic and marginal-zone lymphomas, the same indolent B-cell malignancies that include Waldenström's macroglobulinaemia."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "Its antibody thickens the blood: the monoclonal IgM of Waldenström raises serum viscosity, sludging flow through small vessels and the arterial wall to cause the visual, neurological and bleeding features of hyperviscosity syndrome."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "It can deposit amyloid in the heart: the monoclonal IgM or its light chains in Waldenström can form AL amyloid that infiltrates the myocardium, causing a restrictive cardiomyopathy and heart failure."
  - target: 01-human/07-system/hemophilia-a
    relation: connects-to
    note: "It causes an acquired bleeding disorder: the IgM of Waldenström can bind and clear von Willebrand factor, producing an acquired von Willebrand syndrome—a bleeding tendency reached by a different route than inherited haemophilia A."
  - target: 01-human/07-system/cidp
    relation: connects-to
    note: "An IgM demyelinating neuropathy: anti-MAG IgM in Waldenström causes a distal demyelinating sensory neuropathy that resembles CIDP, a characteristic paraproteinaemic complication often preceding diagnosis."
  - target: 01-human/07-system/hereditary-angioedema
    relation: connects-to
    note: "Acquired angioedema: lymphoplasmacytic clones in Waldenström can consume C1-inhibitor or generate autoantibodies against it, producing a bradykinin-mediated acquired angioedema mimicking the hereditary disease."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Organ infiltration: Waldenström's lymphoplasmacytic cells infiltrate the liver and spleen, enlarging the hepatic lobules and splenic pulp as the disease burden advances."
  - target: 01-human/03-molecular/von-willebrand-factor
    relation: connects-to
    note: "Acquired von Willebrand syndrome: the high IgM paraprotein of Waldenström binds and clears von Willebrand factor, causing acquired bleeding that, with hyperviscosity, makes mucosal haemorrhage a hallmark."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "BTK inhibitors and atrial fibrillation: ibrutinib, a mainstay of Waldenström therapy, off-targets cardiac kinases to cause atrial fibrillation and conduction disturbance, compounding the strain of IgM hyperviscosity on the heart."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Profound immunoparesis: Waldenström suppresses normal antibody production, and anti-CD20 and BTK-inhibitor therapy deepen the deficit, leaving patients with severe, prolonged COVID-19 and poor vaccine responses."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Marrow angiogenesis: VEGF is elevated in Waldenström and drives the increased bone-marrow microvessel density that supports the lymphoplasmacytic clone."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Inflammatory niche: TNF-α within the bone-marrow microenvironment helps sustain the malignant B-cell clone and contributes to the cytopenias and constitutional symptoms of Waldenström."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Hypoxic marrow: HIF-1α stabilised in the crowded, hypoxic Waldenström marrow promotes the VEGF-driven angiogenesis and survival signalling of the tumour niche."
  - target: 01-human/03-molecular/baff
    relation: connects-to
    note: "B-cell survival factor: BAFF from the marrow microenvironment supports the survival and expansion of the malignant lymphoplasmacytic clone in Waldenström, sustaining IgM-secreting cells."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "PI3K-mTOR survival: mTOR signalling downstream of MYD88 and the B-cell receptor drives Waldenström cell growth, and the mTOR inhibitor everolimus has clinical activity in the disease."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Complement-mediated hemolysis: monoclonal IgM with cold-agglutinin or cryoglobulin activity fixes complement, so terminal C5-driven haemolysis contributes to the anaemia of some Waldenström patients."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Hijacked TLR adaptor: MYD88 is the signalling adaptor for TLR4 and related receptors, so the MYD88 L265P mutation of Waldenström drives constitutive NF-κB as if the cell were chronically TLR-stimulated."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K survival arm: PI3K signalling downstream of MYD88 and the B-cell receptor sustains the Waldenström clone in parallel with BTK, contributing to resistance when BTK alone is inhibited."
  - target: 01-human/03-molecular/kit
    relation: connects-to
    note: "Mast-cell support: Waldenström marrow is characteristically infiltrated by KIT-expressing mast cells that nurture the lymphoplasmacytic clone through CD40L and APRIL, a distinctive feature of the disease's microenvironment."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Therapy apoptosis: bendamustine-rituximab and BTK inhibitors ultimately kill Waldenström cells through caspase-3 apoptosis, and the anti-apoptotic BCL-2 these cells express both limits responses and motivates adding venetoclax."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Anaemia at presentation: marrow infiltration by the lymphoplasmacytic clone and IL-6-driven hepcidin blunt erythropoietin-driven red-cell production, making anaemia the commonest presenting feature and the usual trigger to start treatment."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Macrophage microenvironment: CCL2 recruits monocytes and macrophages into the Waldenström marrow, part of the supportive niche that — alongside the mast cells — feeds the lymphoplasmacytic clone with survival signals."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K survival arm: MYD88 L265P signalling (already mapped) activates not only BTK-NF-κB but the PI3K-AKT pathway (PIK3CA and mTOR already mapped), a survival axis and route of resistance in Waldenström macroglobulinemia."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "MAPK proliferation: MYD88-driven signalling also engages the MAPK-ERK1/2 cascade, contributing to the proliferation of the lymphoplasmacytic clone and to incomplete responses to BTK inhibition."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Transformation: MYC activation cooperates with the MYD88 driver in the progression and high-grade transformation of Waldenström macroglobulinemia to diffuse large B-cell lymphoma."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "BCR proximal signalling: Src-family (LYN) kinases relay B-cell-receptor signals upstream of BTK (mapped), feeding the BTK-MYD88-NF-κB axis that drives Waldenström cell survival."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "Adverse genetics: TP53 mutation is an adverse-prognostic lesion in Waldenström macroglobulinemia, associated with treatment resistance and risk of high-grade transformation."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Proliferative output: the cyclin-D-CDK4/6 axis releases E2F1 to drive proliferation of the lymphoplasmacytic clone (MYC mapped) in Waldenström macroglobulinemia."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "Loss of PTEN-restrained PI3K-AKT-mTOR signalling (AKT, PIK3CA and mTOR mapped) reinforces the survival of the MYD88-driven lymphoplasmacytic clone in Waldenström macroglobulinemia."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "CDKN2A (p16) loss releases CDK4/6-cyclin-D control of the cell cycle, contributing to clonal progression in Waldenström macroglobulinemia."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "TERT-mediated telomere maintenance supports the replicative longevity of the malignant lymphoplasmacytic clone in Waldenström macroglobulinemia."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 supports the survival and bone-marrow-niche adhesion of the lymphoplasmacytic clone in Waldenström macroglobulinemia."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "EZH2-mediated polycomb repression contributes to the epigenetic dysregulation of the malignant clone in Waldenström macroglobulinemia."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the immune microenvironment of the bone marrow infiltrated by Waldenström macroglobulinemia."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "BTK and PI3K-AKT signaling (BTK, AKT, and PIK3CA already mapped) inactivates FOXO, supporting survival of the malignant lymphoplasmacytic clone in Waldenström macroglobulinemia."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6 acting on the cyclin-D-RB axis (E2F1 and CDKN2A already mapped) drives the cell-cycle progression of Waldenström macroglobulinemia cells."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signaling shapes the bone-marrow microenvironment and immune tone that support Waldenström macroglobulinemia."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the survival and Wnt/NF-κB signaling of the lymphoplasmacytic cells of Waldenström macroglobulinemia."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in Waldenström macroglobulinemia."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated cytotoxic immunosurveillance is a component of the immune response to Waldenström macroglobulinemia."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of Waldenström macroglobulinemia."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of the lymphoplasmacytic cells of Waldenström macroglobulinemia."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the inflammatory bone-marrow microenvironment of Waldenström macroglobulinemia."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-family chemokine signaling participates in the bone-marrow niche interactions of Waldenström macroglobulinemia."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of Waldenström macroglobulinemia."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the bone-marrow microenvironment of Waldenström macroglobulinemia."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune bone-marrow microenvironment of Waldenström macroglobulinemia."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory bone-marrow microenvironment of Waldenström macroglobulinemia."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the B-cell-receptor and downstream survival signaling of Waldenström macroglobulinemia."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Anaemia: anaemia from marrow infiltration and IgM-mediated cold-agglutinin haemolysis is the most common presenting feature of Waldenström macroglobulinaemia and a primary indication to begin treatment."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Anaemia of inflammation: IL-6-driven hepcidin (IL-6 already mapped) restricts iron availability in Waldenström macroglobulinaemia, compounding the marrow-infiltration anaemia with a functional iron-restricted component."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Antigen presentation: the lymphoplasmacytic clone of Waldenström may be antigen-driven, and MHC class II shapes the T-cell microenvironment and antigen presentation that support its survival alongside the MYD88-driven signalling already mapped."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Immunoparesis: the monoclonal IgM of Waldenström is accompanied by suppression of normal immunoglobulins including IgG, the immunoparesis that raises infection risk, while the paraprotein itself can cause hyperviscosity and cryoglobulinaemia."
  - target: 01-human/03-molecular/thrombin
    relation: connects-to
    note: "Coagulopathy: the monoclonal IgM interferes with fibrin polymerisation and platelet function and drives an acquired von Willebrand syndrome (vWF already mapped), and hyperviscosity disturbs the thrombin-driven coagulation balance, causing bleeding."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell microenvironment: IL-2-driven T cells in the marrow microenvironment support the survival of the lymphoplasmacytic clone (MHC class II already mapped), part of the immune niche sustaining Waldenström macroglobulinaemia."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Th2 clone support: IL-4 and type-2 T-cell help sustain the IgM-secreting B-cell clone (BAFF and IL-2 already mapped) of Waldenström macroglobulinaemia, part of the cytokine support of the lymphoplasmacytic proliferation."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Hyperviscosity vasculature: the high IgM raises serum viscosity and disturbs microvascular flow, and nitric-oxide-mediated vascular regulation is stressed in the hyperviscosity syndrome that causes the visual and neurological symptoms of Waldenström macroglobulinaemia."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Tumour lysis and oxidation: treating the lymphoplasmacytic clone releases purines that xanthine oxidase converts to uric acid, and the reactive oxygen species it generates add oxidative and tumour-lysis burden to therapy for Waldenström macroglobulinaemia."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Marrow-adipocyte crosstalk: the marrow adipocytes and their adipokine adiponectin engage in metabolic crosstalk with the lymphoplasmacytic clone, the marrow adipose tissue shaping the niche that supports Waldenström macroglobulinaemia."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Adipokine marrow signalling: leptin, with adiponectin (already mapped), from the marrow adipose tissue signals to the clonal and stromal cells, part of the metabolic microenvironment of the infiltrated marrow in Waldenström macroglobulinaemia."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipokine milieu: resistin, with leptin and adiponectin (already mapped), completes the adipokine signalling of the marrow adipose niche that shapes the microenvironment of the lymphoplasmacytic infiltrate in Waldenström macroglobulinaemia."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "M2 marrow milieu: IL-13, with IL-4 (already mapped), supports the M2 macrophage (already mapped) and type-2 milieu of the marrow microenvironment of Waldenström macroglobulinaemia."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "T-cell checkpoint: the PD-1 checkpoint on the T cells of the Waldenström tumour microenvironment contributes to the immune evasion of the lymphoplasmacytic clone."
  - target: 01-human/03-molecular/ctla-4
    relation: connects-to
    note: "Checkpoint co-inhibition: CTLA-4, with PD-1 (already mapped), forms the immune-checkpoint brake on the T cells of the Waldenström tumour microenvironment, part of its immune evasion."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate B-cell signalling: type-I interferon, downstream of the TLR/MYD88 (already mapped) innate signalling of the Waldenström B cells, and the historical interferon therapy of the lymphoma."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Marrow macrophages: the marrow macrophages and tumour-associated macrophages (CCL2 already mapped) support the lymphoplasmacytic clone and the immune microenvironment of Waldenström macroglobulinaemia."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Hepatomegaly: the lymphoplasmacytic infiltration causes the hepatomegaly (with the splenomegaly already mapped) and the organomegaly of Waldenström macroglobulinaemia."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the immune microenvironment of Waldenström macroglobulinaemia."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of the lymphoplasmacytic lymphoma of Waldenström macroglobulinaemia."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of Waldenström macroglobulinaemia."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune microenvironment of the lymphoplasmacytic lymphoma of Waldenström macroglobulinaemia."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the microenvironment (distinct from the monoclonal IgM already mapped) of Waldenström macroglobulinaemia."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "CD8 antitumour arm: the cytotoxic T cells (perforin already mapped) of the immune microenvironment provide the antitumour surveillance of the clonal B cells (already mapped) of Waldenström macroglobulinaemia."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the cytokines (IL-6 already mapped) of the lymphoplasmacytic microenvironment supporting the clonal B cells (already mapped) of Waldenström macroglobulinaemia."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) contributes to the complement dimension of the IgM-mediated (immunoglobulin already mapped) immune-complex and cold-agglutinin phenomena of Waldenström macroglobulinaemia."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Antigen presentation: the dendritic cells present antigen to the T cells (already mapped) shaping the immune microenvironment of Waldenström macroglobulinaemia."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) engaged by the IgM (immunoglobulin already mapped) immune complexes and cold agglutinins of Waldenström macroglobulinaemia."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway activated by the IgM cold agglutinins (immunoglobulin already mapped) that mediate the complement-dependent haemolysis of Waldenström macroglobulinaemia."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Anaemia iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the anaemia of the marrow infiltration and chronic disease of Waldenström macroglobulinaemia."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-marrow axis: TSLP, secreted by bone-marrow (already mapped) stromal cells, activates mast cells (already mapped) and B cells (already mapped), amplifying the MYD88 (already mapped)-driven plasmacytic differentiation of Waldenström macroglobulinaemia."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-hyperviscosity axis: bradykinin, generated by the kallikrein-kinin system in the hyperviscous IgM (immunoglobulin already mapped) plasma environment, augments vascular permeability and contributes to the vascular complications of Waldenström macroglobulinaemia."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell mediator: histamine, released from the activated mast cells (already mapped) recruited to the marrow niche of Waldenström macroglobulinaemia, promotes B-cell (already mapped) and plasmacytic survival via H2 receptor signalling in the disease microenvironment."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Marrow ECM scaffold: periostin, expressed by stromal fibroblasts and bone marrow mesenchymal cells (already mapped) in the Waldenström niche, promotes the fibrotic extracellular matrix remodelling that supports the MYD88-mutant B-cell/plasmacytic infiltration of the disease."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian haematopoietic protection: melatonin, via MT1/MT2 receptors on haematopoietic progenitors (already mapped) and NK cells (already mapped), suppresses the pro-tumour cytokine milieu and B-cell trafficking (CXCL13 already mapped) of Waldenström macroglobulinaemia."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Immune-endocrine B-cell axis: prolactin, acting via PRLR on B cells (already mapped) and plasmacytic cells, promotes immunoglobulin production (IgM already mapped) and the survival of the malignant clone in the marrow niche of Waldenström macroglobulinaemia."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "WM testosterone: testosterone, via androgen receptors on B cells (already mapped) and plasma cells (already mapped), modulates the MYD88 (already mapped)/NF-κB (already mapped) signalling; androgen deficiency amplifies WM clone expansion in the bone-marrow (already mapped) niche."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "WM serotonin: mast-cell (already mapped) serotonin promotes the hyperviscosity and vascular complications of WM; 5-HT2 signalling on platelet (already mapped) and erythrocyte (already mapped) surfaces amplifies the NF-κB (already mapped) inflammatory niche of Waldenström."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "WM oxytocin: oxytocin, via OXTR on bone-marrow (already mapped) stromal cells and regulatory T cells (already mapped), attenuates the MYD88 (already mapped)/NF-κB (already mapped) pro-tumour microenvironment and the B-cell (already mapped) clone survival of Waldenström."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "WM vasopressin: vasopressin, via V1B receptors on plasma cells (already mapped) and B cells (already mapped), modulates the bone-marrow (already mapped) microenvironment and amplifies NF-κB (already mapped)/MYD88 (already mapped) clone-survival signalling in Waldenström."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "WM selenium: selenium-dependent GPx suppresses the ROS amplifying NF-κB (already mapped)/MYD88 (already mapped) tumour microenvironment in the bone-marrow (already mapped); selenium deficiency promotes oxidative vascular injury and IgM (already mapped) hyperviscosity of WM."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "WM iodine: iodine-dependent thyroid hormones modulate B-cell (already mapped) differentiation and haematopoietic cycling in the bone-marrow (already mapped); hypothyroidism amplifies the pro-tumour macrophage (already mapped) and NF-κB (already mapped) signalling niche of WM."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "WM zinc: zinc cofactors macrophage (already mapped) anti-tumour function and B-cell (already mapped) homeostasis; zinc deficiency amplifies NF-κB (already mapped) and MYD88 (already mapped) and IL-6 (already mapped) B-cell (already mapped) clonal expansion in WM."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "WM magnesium: magnesium supports macrophage (already mapped) anti-inflammatory resolution and B-cell (already mapped) regulation; magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) tumour-promoting cascade in WM."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "WM copper: copper-dependent SOD in macrophages (already mapped) and B-cell (already mapped) quenches ROS; copper deficiency amplifies MYD88 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) tumour-promoting cascade of Waldenström."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "WM potassium: potassium efflux from macrophages (already mapped) and B-cell (already mapped) modulates NLRP3-IL-1β; potassium dysregulation amplifies NF-κB (already mapped) and MYD88 (already mapped) and IL-6 (already mapped) clonal survival cascade of Waldenström."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "WM calcium: calcium signalling in B-cell (already mapped) and plasma-cell (already mapped) drives MYD88 (already mapped)/NF-κB (already mapped) clonal activation; calcium dysregulation amplifies IL-6 (already mapped) and IgM (already mapped) hyperviscosity cascade of WM."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "WM carbon: carbon, as metabolic backbone of IgM (already mapped) and MYD88 (already mapped) in B-cell (already mapped) and plasma-cell (already mapped), drives clonal expansion; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of WM."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "WM chloride: chloride channels in B-cell (already mapped) and macrophages (already mapped) modulate clonal B-cell survival; chloride dysregulation amplifies NF-κB (already mapped) and MYD88 (already mapped) and IL-6 (already mapped) hyperviscosity cascade of WM."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "WM hydrogen: hydrogen, via redox homeostasis in B-cell (already mapped) and macrophages (already mapped), quenches NF-κB-driven ROS; hydrogen dysregulation amplifies MYD88 (already mapped) and IL-6 (already mapped) and IgM (already mapped) clonal cascade of WM."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "WM nitrogen: nitric oxide from B-cell (already mapped) and macrophages (already mapped) modulates clonal B-cell survival; nitrogen imbalance amplifies NF-κB (already mapped) and MYD88 (already mapped) and IL-6 (already mapped) hyperviscosity cascade of WM."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "WM sulfur: hydrogen sulfide from B-cell (already mapped) and macrophages (already mapped) modulates redox homeostasis; sulfur deficiency amplifies NF-κB (already mapped) and MYD88 (already mapped) and IL-6 (already mapped) clonal cascade of waldenstrom macroglobulinemia."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "WM oxygen: mitochondrial oxygen in B-cell (already mapped) and macrophages (already mapped) drives ATP for clonal proliferation; hypoxia amplifies NF-κB (already mapped) and MYD88 (already mapped) and IL-6 (already mapped) hyperviscosity cascade of WM."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "WM GLP-1: GLP-1 from gut L-cells (already mapped) and macrophages (already mapped) modulates lymphoma metabolic homeostasis; GLP-1 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of Waldenström macroglobulinemia."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "WM angiotensin-II: Angiotensin-II in B-cells (already mapped) and macrophages (already mapped) promotes lymphoma stroma activation; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of Waldenström macroglobulinemia."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "WM Wnt/β-catenin: Wnt/β-catenin in B-cells (already mapped) and macrophages (already mapped) drives lymphoma clonal expansion; Wnt dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of Waldenström macroglobulinemia."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "WM rankl: RANKL in macrophages (already mapped) and B-cells (already mapped) modulates WM bone-immune axis; RANKL excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of Waldenström macroglobulinemia."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "WM fibronectin: Fibronectin in B-cells (already mapped) and macrophages (already mapped) scaffolds lymphoma ECM; fibronectin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of Waldenström macroglobulinemia."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "WM notch: NOTCH on B-cells (already mapped) and macrophages (already mapped) regulates WM clonal immune tone; NOTCH dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of Waldenström macroglobulinemia."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "WM igf-1: IGF-1 from macrophages (already mapped) and B-cells (already mapped) promotes WM clonal B-cell growth; igf-1 excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of Waldenström macroglobulinemia."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "WM activin-a: activin-A from macrophages (already mapped) and B-cells (already mapped) regulates WM immune-fibrotic balance; activin-a excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of Waldenström macroglobulinemia."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "WM tgf-beta: TGF-β from macrophages (already mapped) and B-cells (already mapped) drives WM stromal fibrosis; tgf-beta excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of Waldenström macroglobulinemia."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "WM cgrp: CGRP from macrophages (already mapped) and B-cells (already mapped) modulates WM vascular-immune tone; cgrp dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of Waldenström macroglobulinemia."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "WM calcitonin: calcitonin from macrophages (already mapped) and B-cells (already mapped) modulates WM calcium balance; calcitonin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of Waldenström macroglobulinemia."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "WM substance-p: substance P from macrophages (already mapped) and B-cells (already mapped) modulates WM neuroimmune tone; substance-p excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of Waldenström macroglobulinemia."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "WM insulin-receptor: insulin receptor on macrophages (already mapped) and B-cells (already mapped) drives WM metabolic tone; insulin-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of Waldenström macroglobulinemia."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "WM aldosterone: aldosterone from macrophages (already mapped) and B-cells (already mapped) modulates WM ion balance; aldosterone excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of Waldenström macroglobulinemia."
  - target: 01-human/03-molecular/androgen-receptor
    relation: connects-to
    note: "WM androgen-receptor: androgen receptor on macrophages (already mapped) and B-cells (already mapped) modulates WM hormonal tone; androgen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of Waldenström macroglobulinemia."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "WM norepinephrine: norepinephrine from macrophages (already mapped) and B-cells (already mapped) modulates WM adrenergic tone; norepinephrine excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of Waldenström macroglobulinemia."
  - target: 01-human/03-molecular/adrenomedullin
    relation: connects-to
    note: "WM adrenomedullin: adrenomedullin from macrophages (already mapped) and B-cells (already mapped) modulates WM vascular tone; adrenomedullin loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of Waldenström macroglobulinemia."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "WM bdnf: BDNF from macrophages (already mapped) and B-cells (already mapped) modulates WM neuroimmune tone; bdnf loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of Waldenström macroglobulinemia."
---

# Waldenström Macroglobulinemia

## Overview

**Waldenström macroglobulinemia (WM)** is a rare indolent B-cell malignancy defined by **lymphoplasmacytic lymphoma (LPL)** — a neoplasm of small lymphocytes, plasmacytoid lymphocytes, and plasma cells — with serum **IgM monoclonal protein** (IgM paraprotein). WM accounts for ~2% of hematologic malignancies (~2,000 new cases/year in the US); it follows a characteristically indolent natural history (median OS >10 years) but produces organ dysfunction via IgM-mediated complications: hyperviscosity syndrome, peripheral neuropathy (antimyelin antibodies), cold agglutinin hemolytic anemia, cryoglobulinemia, and systemic amyloidosis (AL). The molecular landscape of WM is dominated by **MYD88 L265P** (~90%), the landmark somatic mutation identifying constitutive NF-κB/JAK-STAT activation as the oncogenic driver, and **CXCR4 WHIM mutations** (~35%) that confer BTK inhibitor resistance. Ibrutinib (FDA approved 2015) and zanubrutinib (ASPEN trial, FDA approved 2021) transformed WM management [^treon-2015-ibrutinib-wm].

**Epidemiology:**
- ~2,000 new cases/year in the US; predominantly older patients (median age ~70); M:F ~2:1
- Mostly Caucasian; familial clustering in ~20% of WM (highest familial risk of any lymphoma)
- Incurable with current therapy; median OS >10 years for treated symptomatic WM
- MGUS-IgM (IgM monoclonal gammopathy of undetermined significance) → WM progression rate ~1.5%/year
- 5-year OS: ~87% (modern BTK inhibitor era); favorable prognosis for most patients

## Structure

### Molecular landscape

**MYD88 L265P (Leu265Pro, TIR domain):**
Present in ~90% of WM/LPL; diagnostic and predictive biomarker; constitutive myddosome assembly → IRAK4-IRAK1 → TRAF6 → NF-κB → BCL-2, CXCR4, IRF4; also activates BTK (non-canonical) and JAK1-STAT3 (via IRAK1). MYD88 WT WM (~10%): inferior outcomes with BTK inhibitors; consider clinical trial or rituximab-based regimen.

**CXCR4 WHIM mutations (exon 2, C-terminal truncations):**
Found in ~35% of WM; gain-of-function truncations that impair CXCR4 internalization → prolonged CXCL12 signaling → PI3K-AKT-ERK → reduced BTK inhibitor efficacy. CXCR4 mutations occur on MYD88 L265P background (virtually never alone); allele burden correlates with depth of ibrutinib response failure.

**Additional co-mutations:**
- ARID1A: ~17%; chromatin remodeling; SWI/SNF subunit
- CD79B: ~5-10% in LPL (more common in ABC-DLBCL); BCR co-receptor; BTK dependency
- TP53: ~5%; rare in WM (unlike aggressive lymphoma); poor prognosis
- 6q deletion: ~40%; most common cytogenetic abnormality; not targetable but prognostic
- Trisomy 4: Less common; prognostic value under study

**Immunophenotype:**
CD19+, CD20+ (often dim), CD22+, CD25+, CD27+ (memory B marker), sIgM+; CD5−, CD10−, CD23−, CD103−; plasma cell component: cytoplasmic IgM+, CD38+, CD138+; PAS-positive intranuclear inclusions (Dutcher bodies) in some cases; mast cells prominent in BM background (CD117+, MYD88 L265P positive — WM microenvironment feature).

### IgM monoclonal protein biology

**IgM structure and overproduction:**
WM plasma cells secrete IgM (pentameric, MW ~900 kDa) as monoclonal paraprotein; elevated serum IgM (often >3 g/dL) → several complications driven by IgM physicochemical properties:

**Hyperviscosity syndrome:**
IgM pentamers are large and do not circulate freely at high concentrations → blood viscosity increases at IgM >4-5 g/dL → retinal hemorrhage (funduscopic "sausage-link" veins), visual disturbance, headache, mental status change, heart failure; treat with urgent plasmapheresis to remove IgM → immediate viscosity reduction before chemotherapy (rituximab can cause transient IgM spike → plasmapheresis before rituximab if symptomatic hyperviscosity).

**Peripheral neuropathy:**
IgM anti-MAG (myelin-associated glycoprotein) antibodies in ~50% of WM neuropathy → predominantly sensory demyelinating neuropathy (distal, symmetric, predominantly sensory, gait disturbance); anti-MAG antibody titer correlates with neuropathy severity; anti-GD1b, anti-GM1 antibodies: motor neuropathy variants; rituximab reduces IgM burden → neuropathy improvement in some.

**Cold agglutinin hemolytic anemia:**
IgM anti-I antibodies bind erythrocytes at cold temperatures → complement activation → hemolysis; common cold agglutinin disease in WM (1°C-10°C: IgM binds/dissociates); sutimlimab (anti-C1s) approved for cold agglutinin disease.

**Cryoglobulinemia:**
IgM (often with IgG) precipitates in cold → mixed cryoglobulinemia (type II) → vasculitis, purpura, arthralgias, membranoproliferative glomerulonephritis; treatment: plasmapheresis + rituximab + immunosuppression for severe manifestations.

## Function

### Normal B-cell to plasma cell differentiation

Mature naive B-cells → antigen stimulation + T-cell help → GC formation → affinity maturation → class switch recombination (in GCB cells) OR terminal differentiation to plasma cells or memory B-cells. IgM-secreting plasma cells are the immediate product of T-independent B-cell activation (without class switching); in WM, this differentiation program is arrested at the lymphoplasmacytic stage — partially differentiated toward plasma cell secreting IgM but retaining B-cell surface markers (CD20).

### BM microenvironment in WM

The WM BM contains characteristic mast cells (CD117+, tryptase+, MYD88 L265P+) that support WM cell survival via CD40L-CD40 interaction → NF-κB; CXCL12/CXCR4 axis retains WM cells in the BM niche; IL-6, BAFF (B-cell activating factor), APRIL from stromal cells → plasma cell differentiation signals. IgM paraprotein in BM interstitium contributes to hyperviscosity and neuropathy independently of blood IgM levels.

## Pathology

### Diagnostic criteria (WHO 2022)

1. IgM monoclonal gammopathy of any concentration
2. BM infiltration by lymphoplasmacytic lymphoma (≥10% of BM cellularity by clonal lymphoplasmacytic cells)
3. Pathological pattern: Small lymphocytes + plasmacytoid lymphocytes + plasma cells; paratrabecular or diffuse BM involvement; PAS+ Dutcher bodies (intranuclear pseudo-inclusions of IgM); mast cells in background; CD20+/CD138+ dual staining shows lymphocytic + plasmacytic spectrum

**Note:** Symptomatic WM = LPL + IgM + any WM-related organ damage (anemia, hyperviscosity, neuropathy, cryoglobulinemia, amyloidosis, hepatosplenomegaly). Asymptomatic (smoldering) WM = LPL + IgM but no organ damage.

**IPSSWM (International Prognostic Scoring System for WM):**
5 adverse factors: Age >65, Hgb ≤11.5 g/dL, platelets ≤100 × 10⁹/L, β2M >3 mg/L, serum IgM >7 g/dL
- Low risk (0-1 factors, not age): Median OS >10 years
- Intermediate (2 factors or age alone): Median OS 8-10 years
- High risk (≥3 factors): Median OS 3-5 years

**Staging workup:**
- CBC, comprehensive metabolic panel, serum protein electrophoresis + IFE (confirm IgM monoclonal), quantitative immunoglobulins, serum free light chains, β2M, LDH, uric acid
- CT chest/abdomen/pelvis: Lymphadenopathy, splenomegaly, extramedullary disease
- BM biopsy + aspirate: Diagnostic; morphology, immunohistochemistry (CD20, CD138, CD56, κ/λ), flow cytometry
- MYD88 L265P mutation testing (AS-PCR or NGS on BM/blood); CXCR4 mutation testing (BM/blood NGS)
- Viscosity measurement: Serum viscosity if IgM >4 g/dL or symptoms
- Anti-MAG antibodies: If neuropathy present; nerve conduction studies
- Echocardiogram/fat pad biopsy: If amyloidosis suspected (AL amyloid deposition in WM)

### Treatment

**Watch and wait (asymptomatic WM):**
~25-30% of newly diagnosed WM is asymptomatic; ECOG 9902 study: No benefit to early treatment in asymptomatic WM; initiate therapy when: symptomatic anemia (Hgb <10 g/dL), symptomatic hyperviscosity, progressive neuropathy, cryoglobulinemia, amyloidosis, bulky lymphadenopathy, thrombocytopenia (<100 × 10⁹/L), or IgM >4 g/dL with symptoms.

**Plasmapheresis (emergent):**
For symptomatic hyperviscosity → removes IgM immediately; does not treat underlying WM; used before rituximab (avoids IgM flare-mediated hyperviscosity exacerbation); requires 2-4 sessions to lower IgM before chemoimmunotherapy.

**First-line systemic therapy:**

**BTK inhibitors (preferred for MYD88 L265P WM):**
- **Ibrutinib 420 mg daily:** [^treon-2015-ibrutinib-wm] Phase 2, R/R WM; ORR 90.5% (VGPR 12%); median PFS 69 months in MYD88 L265P/CXCR4 WT; FDA approved 2015; ECOG-ACRIN 1603 (1st-line): ibrutinib+rituximab superior to PO-rituximab+dexamethasone; toxicities: AFib (~10-15%), bleeding, hypertension, arthralgias
- **Zanubrutinib 160 mg BID (ASPEN trial):** [^tam-2020-aspen] Randomized vs. ibrutinib; VGPR or better: 28% vs. 19% at 19 months; similar OS; AFib rate ~2% vs. ~15%; FDA approved 2021; preferred for cardiac-risk patients or post-ibrutinib intolerance

**Chemoimmunotherapy (BTK inhibitor-ineligible or MYD88 WT WM):**
- **Rituximab + bendamustine (BR):** ORR ~93%; deep responses; peripheral neuropathy risk with bendamustine is lower than bortezomib regimens
- **Rituximab + cyclophosphamide + dexamethasone (RCD) / Rituximab + cyclophosphamide + dexamethasone + bortezomib (BDR):** Less preferred; neuropathy with bortezomib + existing WM neuropathy is problematic

**Relapsed/refractory WM:**
- **Zanubrutinib (after ibrutinib):** Active in ibrutinib-intolerant patients (cardiac/bleeding issues)
- **Pirtobrutinib (non-covalent BTK inhibitor):** Active after covalent BTK inhibitor progression; C481S resistance overcome by non-covalent BTK inhibition; BRUIN trial includes WM; ORR ~70% in BTK-refractory WM
- **Venetoclax:** Active in R/R WM; ibrutinib+venetoclax combination (VCAP trial): deep responses
- **Rituximab + cyclophosphamide (or bendamustine):** Re-challenge if prior response
- **Proteasome inhibitors (bortezomib/carfilzomib + rituximab):** Active in WM; bortezomib toxicity limited by neuropathy
- **Auto-SCT:** Selected high-risk patients in second remission

**WM neuropathy specific:**
- Rituximab-based regimens to reduce IgM burden → neuropathy improvement in ~30-40%; IgM level correlates with neuropathy severity; goal: IgM <1 g/dL for maximal neuropathy benefit
- Intravenous immunoglobulin (IVIg): Symptomatic relief for anti-MAG neuropathy; not disease-modifying
- Sutimlimab (anti-C1s): For cold agglutinin-mediated hemolysis

## Connections

- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — MYD88 L265P → constitutive NF-κB via IRAK4-TRAF6-IKK → BCL-2, MYC, CXCR4 transcription; ibrutinib (BTK inhibitor) blocks BTK-dependent NF-κB in MYD88 L265P WM (ORR >90%); CXCR4 mutation (~35%) confers ibrutinib resistance (ORR ~60%).
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — MYD88 L265P drives JAK1-STAT3 → BCL-XL survival in WM independent of cytokine receptor signaling; ruxolitinib (JAK1/2 inhibitor) shows activity in MYD88 L265P WM; combined BTK+JAK inhibition studied in ibrutinib-resistant WM; JAK2 V617F absent in WM (unlike MPN).
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — BCL-2 overexpression is driven by MYD88/NF-κB → IRF4 in WM; venetoclax (BCL-2 inhibitor) shows activity in R/R WM; combined ibrutinib+venetoclax achieves deep responses in R/R WM; BCL-2 is an anti-apoptotic target complementary to BTK inhibition in WM.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — Rituximab ± bendamustine or cyclophosphamide is first-line for WM; rituximab monotherapy causes IgM flare (~40%) before response; ofatumumab and obinutuzumab are alternatives for rituximab-refractory WM; CD20 is uniformly expressed (CD19+/CD20+/sIgM+).
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — Waldenström macroglobulinemia is a lymphoplasmacytic lymphoma — a clonal B-cell neoplasm frozen midway between a memory B cell and an IgM-secreting plasma cell; this dual identity gives it both surface CD20 and cytoplasmic IgM and shapes its B-cell-directed therapy.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — MYD88 L265P, present in ~90% of WM, is the defining and diagnostic mutation: it assembles a constitutive myddosome that fires NF-κB, JAK-STAT3, and BTK to keep the tumor alive, and its presence predicts response to BTK inhibitors — while MYD88-wildtype WM responds poorly.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — About half of WM patients with neuropathy have IgM anti-MAG antibodies that attack peripheral-nerve myelin, producing a distal, symmetric, sensory-predominant demyelinating neuropathy; lowering IgM with rituximab improves it in some, and titer tracks severity.
- `connects-to` → **[Multiple Myeloma](../multiple-myeloma/README.md)** — Waldenström macroglobulinemia and myeloma are B-cell dyscrasias secreting a monoclonal paraprotein but differ: WM is a lymphoplasmacytic lymphoma making IgM (hyperviscosity, neuropathy) with MYD88 L265P, while myeloma is a marrow plasma-cell tumor making IgG/IgA with lytic bone.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — WM's malignant clone is lymphoplasmacytic—a spectrum from small B cells to plasma cells—so it secretes monoclonal IgM like a plasma-cell tumor while keeping B-cell markers (CD20); this dual differentiation explains why both rituximab and plasma-cell-directed agents work.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — WM characteristically infiltrates the bone marrow with lymphoplasmacytic cells, often paratrabecular and with increased mast cells; this marrow involvement causes anemia (the commonest symptom) and underlies the cytopenias, with diagnosis confirmed by marrow biopsy.
- `connects-to` → **[Follicular Lymphoma](../follicular-lymphoma/README.md)** — Waldenström macroglobulinemia and follicular lymphoma are both indolent B-cell non-Hodgkin lymphomas but molecularly distinct: WM is a lymphoplasmacytic lymphoma defined by MYD88 L265P and an IgM paraprotein, while follicular lymphoma is BCL2-translocated.
- `connects-to` → **[Diffuse Large B-Cell Lymphoma](../dlbcl/README.md)** — Waldenström macroglobulinemia can transform into aggressive diffuse large B-cell lymphoma: like other indolent lymphomas, the low-grade clone can acquire further lesions and evolve into DLBCL, a Richter-like transformation with rapid deterioration and worse prognosis.
- `connects-to` → **[Stroke](../stroke/README.md)** — Hyperviscosity from WM's IgM paraprotein can mimic or cause stroke: large pentameric IgM thickens blood, causing headache, visual blurring, and neurological deficits, so a stroke-like presentation with a very high protein points to WM, treated by plasmapheresis.
- `connects-to` → **[Mantle Cell Lymphoma](../mantle-cell-lymphoma/README.md)** — Waldenström macroglobulinemia and mantle cell lymphoma are both B-cell non-Hodgkin lymphomas but distinct: WM is a lymphoplasmacytic lymphoma secreting IgM (MYD88 L265P) causing hyperviscosity, while MCL is a t(11;14) cyclin-D1 nodal tumor.
- `connects-to` → **[CLL](../cll/README.md)** — Waldenström macroglobulinemia and CLL are indolent mature B-cell neoplasms: both involve small B cells and respond to BTK inhibitors, but WM's cells secrete monoclonal IgM while CLL circulates as a leukemia—immunophenotype and MYD88 separate them.
- `connects-to` → **[Hepatitis C](../hepatitis-c/README.md)** — Hepatitis C links to Waldenström macroglobulinemia: chronic HCV-driven B-cell stimulation can progress to lymphoplasmacytic lymphoma, so HCV is screened for in IgM-secreting lymphomas—and antiviral cure can sometimes treat the lymphoproliferation.
- `connects-to` → **[BTK](../../03-molecular/btk/README.md)** — WM is exquisitely BTK-dependent: its hallmark MYD88 mutation signals through Bruton tyrosine kinase to drive malignant B-cell survival, so BTK inhibitors like ibrutinib are highly effective—response even predicted by MYD88 and CXCR4 genotype.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — WM's monoclonal IgM attacks red cells: it can act as a cold agglutinin that clumps and lyses erythrocytes, and marrow infiltration suppresses production, so anemia—often the presenting feature—comes from both hemolysis and crowded-out red-cell formation.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — WM is a classic cause of hyperviscosity retinopathy: the thick, IgM-laden blood engorges and tortuoses retinal veins ('sausage-link' veins) and can cause hemorrhages and blurred vision—an ophthalmoscopic clue that prompts urgent plasmapheresis.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Waldenström's IgM impairs platelets and bleeding: the huge monoclonal IgM coats platelets and clotting factors and thickens blood, so patients bruise and bleed—nosebleeds and mucosal bleeding—even as hyperviscosity paradoxically also risks clots and stroke.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — Waldenström's infiltrates the spleen and lymph nodes: the malignant lymphoplasmacytic cells expand beyond the marrow into the spleen and nodes, causing splenomegaly and lymphadenopathy that mark it as a lymphoma, not just a plasma-cell disorder.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Anemia is Waldenström's most common problem: marrow crowding by tumor cells plus chronic-disease and dilutional effects of the expanded plasma volume lower hemoglobin, so fatigue from anemia—not hyperviscosity—is usually what brings patients in.
- `connects-to` → **[Primary CNS Lymphoma](../pcnsl/README.md)** — Waldenstrom and primary CNS lymphoma share the MYD88 L265P mutation: when WM invades the brain it is called Bing-Neel syndrome, and the shared mutation makes both B-cell cancers responsive to BTK inhibitors that cross into the CNS.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Waldenstrom's IgM can turn on complement against red cells: as cold agglutinins or cryoglobulins, the paraprotein binds erythrocytes and fixes complement (C3), causing hemolysis—an extra anemia beyond marrow crowding.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Waldenstrom's marrow is studded with mast cells: increased mast cells are a characteristic histologic feature that support the lymphoplasmacytic clone through CD40-ligand and cytokines, part of the tumor's marrow microenvironment.
- `connects-to` → **[Albumin](../../03-molecular/albumin/README.md)** — Waldenström's hallmark is hyperviscosity from monoclonal protein: the malignant clone floods blood with IgM that thickens it, inverting the normal albumin-to-globulin ratio and causing the bleeding, visual, and neurologic symptoms relieved by plasmapheresis.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Waldenström's cells survive on autophagy downstream of MYD88: constant MYD88/NF-κB signaling and heavy antibody output make the clone lean on autophagy to manage stress, a vulnerability alongside the BTK pathway that drugs target.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Waldenström evades immunity through regulatory T cells: the marrow accumulates Tregs and exhausted T cells that dampen the antitumor response, helping the slow-growing lymphoplasmacytic clone persist and limiting immunotherapy.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Waldenström can invade the brain: in rare Bing-Neel syndrome the lymphoplasmacytic cells seed the central nervous system, causing headaches, confusion, and neurological deficits that require treatments able to cross into the brain.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Waldenström blunts the body's iron use: marrow packed with the clone and chronic inflammation choke off red-cell production and lock away iron, so anemia—often the presenting complaint—dominates the disease.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Waldenström's thick IgM batters the endothelium: the sludgy, hyperviscous blood engorges and damages the vessel-lining cells, swelling retinal veins and causing the headaches, bleeding, and vision loss of hyperviscosity syndrome.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Waldenström's hyperviscosity shows in the eye: fundoscopy in visible light reveals dilated, sausage-segmented retinal veins, while CT photons map the lymph-node and spleen enlargement of the clone.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Waldenström spreads through the lymphatic organs: hepatomegaly and lymphadenopathy join the splenomegaly as the lymphoplasmacytic clone seeds beyond the bone marrow.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Waldenström's high IgM fools the lab: the excess protein displaces water in the blood sample, producing a spurious low sodium—pseudohyponatremia—that must not be wrongly corrected.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy captures Waldenström's hybrid cell: a lymphoplasmacytic cell caught between lymphocyte and plasma cell, its cytoplasm swollen with rough endoplasmic reticulum churning out IgM, sometimes with antibody packed into Dutcher bodies.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — The flood of IgM can injure the kidney: the antibody and its light chains deposit as casts, amyloid, or in the glomerulus, while hyperviscosity slows renal blood flow — routes by which Waldenström threatens kidney function.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Waldenström can surface on the skin: IgM deposits raise flesh-colored papules of macroglobulinemia cutis, and cryoglobulins precipitating in the cold inflame small vessels into the purpura of cryoglobulinemic vasculitis.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Waldenström is a disease of one antibody overmade: its clone pumps out monoclonal IgM that thickens the blood, and when that IgM happens to target myelin (anti-MAG), clump in the cold (cryoglobulin, cold agglutinin), it drives the syndrome's protean complications.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — The rogue IgM frays the nerves: anti-MAG antibodies strip myelin from peripheral neurons into a slowly progressive demyelinating neuropathy, and rarely the lymphoma itself invades the brain as Bing-Neel syndrome.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Thickened blood overworks the heart: the high IgM raises plasma viscosity and volume, and with the accompanying anemia the heart must pump harder, tipping toward high-output strain in hyperviscosity syndrome.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It is a lymphoma at heart: the lymphoplasmacytic clone of Waldenström infiltrates lymph nodes and spleen, so lymphadenopathy and splenomegaly accompany the marrow disease, marking its place among the indolent B-cell lymphomas.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — The clone can seed the gut: infiltration of the bowel wall by lymphoplasmacytic cells, and IgM deposition, cause malabsorption, diarrhea, and bleeding — an uncommon but recognized extramedullary face of the disease.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Marrow and treatment both lower the counts: the lymphoplasmacytic infiltrate crowds out normal blood production, and the chemo and BTK-inhibitor therapy add their own myelosuppression, dropping neutrophils and raising infection risk.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — The IgM can attack the nerves: in many patients it binds myelin-associated glycoprotein, stripping the peripheral nerves into a slow demyelinating neuropathy with numb, tingling, unsteady feet — sometimes the first sign of the disease.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6 fuels the IgM factory: the cytokine pushes the malignant B cells toward plasma-cell differentiation and antibody output, helping sustain the monoclonal IgM that defines and harms in Waldenström's.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Rituximab leans on natural killer cells: the anti-CD20 antibody tags the tumor B cells for NK-mediated killing (ADCC), so the strength of the NK response shapes how well this mainstay therapy works.
- `connects-to` → **[Interleukin-10](../../03-molecular/il-10/README.md)** — The MYD88 mutation feeds an autocrine loop: constitutive NF-κB signaling drives the tumor cells to secrete IL-10 and IL-6 that loop back to sustain their own growth, a survival circuit downstream of the defining mutation.
- `connects-to` → **[Immune Thrombocytopenia](../immune-thrombocytopenia/README.md)** — The monoclonal IgM turns on the body: it can act as an autoantibody, driving immune thrombocytopenia, cold agglutinin hemolysis and neuropathy — paraneoplastic phenomena that can dominate the picture more than the tumor bulk.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — The marrow niche nurtures the clone: supportive macrophages and mast cells in the bone marrow supply CD40L and APRIL signals that help the lymphoplasmacytic cells survive, part of the microenvironment targeted alongside the tumor.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — The driver mutation lights two fuses: MYD88 L265P fires not only NF-κB but also JAK-STAT3 signaling, a parallel survival pathway that sustains the Waldenström clone and is explored as a therapeutic target.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It reaches the nervous system in several ways: anti-MAG IgM causes peripheral neuropathy, hyperviscosity impairs the brain, and rarely the clone infiltrates the CNS directly as Bing-Neel syndrome.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Low normal antibodies leave a defense gap: the suppressed normal immunoglobulins of Waldenström, compounded by rituximab and BTK-inhibitor therapy, predispose to serious infection and sepsis.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Thick IgM-laden blood clots and bleeds: the hyperviscosity of Waldenström both impairs flow and, with its cancer-associated hypercoagulability, raises venous thromboembolism risk even as paraprotein can paradoxically cause bleeding.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — The IgM paraprotein can injure the kidney: deposition of monoclonal IgM and cryoglobulins in the glomeruli, plus hyperviscosity, can damage renal function and progress toward chronic kidney disease.
- `connects-to` → **[Pneumocystis jirovecii](../../../02-pathogen/03-fungi/pneumocystis-jirovecii/README.md)** — B-cell-directed therapy opens the lung: rituximab and BTK inhibitors used in Waldenström deplete immune defenses enough to risk Pneumocystis pneumonia, sometimes warranting prophylaxis during treatment.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Its BTK-inhibitor therapy admits invasive mold: ibrutinib, a mainstay for Waldenström, impairs macrophage and neutrophil antifungal defense, with a recognized risk of invasive aspergillosis.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Ibrutinib and hyperviscosity stress the heart: the BTK inhibitor central to Waldenström causes atrial fibrillation and cardiotoxicity, and the IgM-driven hyperviscosity raises high-output cardiac strain toward heart failure.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A chronic, incurable lymphoma weighs on mood: the indolent but relapsing course, lifelong monitoring and treatment burden of Waldenström contribute to depression and reduced quality of life.
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — Its B-cell-targeted therapy reawakens shingles: rituximab and the BTK inhibitors used for Waldenström deplete B-cell and antiviral immunity, allowing latent varicella-zoster to reactivate.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Its abnormal IgM shows on the skin: Waldenström's monoclonal IgM can act as a cryoglobulin causing cold-induced purpura and acrocyanosis, and rarely deposits in the skin as IgM storm papules.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A chronic, relapsing, incurable lymphoma breeds worry: the indolent-but-watchful course, hyperviscosity scares and lifelong monitoring of Waldenström foster chronic health anxiety alongside depression.
- `connects-to` → **[Immune System](../immune-system/README.md)** — It is a clonal antibody-making disease: lymphoplasmacytic cells secrete monoclonal IgM and suppress normal immunoglobulins, so Waldenström causes immunoparesis with infections alongside cryoglobulinaemia and cold agglutinin disease.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It can deposit in the gut: IgM and amyloid deposition in the bowel wall cause malabsorption and diarrhoea, and the disease commonly enlarges the liver and spleen.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It fills the marrow but spares the bones: Waldenström infiltrates the bone marrow with lymphoplasmacytic cells causing cytopenias, yet characteristically lacks the lytic bone lesions of multiple myeloma.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Thick blood and drugs strain the heart: IgM hyperviscosity raises cardiac workload toward high-output failure, ibrutinib causes atrial fibrillation, and AL amyloid can infiltrate the myocardium.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It can infiltrate the lungs: IgM and amyloid deposition can involve the lung parenchyma and pleura, and hyperviscosity causes breathlessness, alongside infection risk from immunoparesis.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Its IgM injures the kidney: monoclonal IgM, light chains and amyloid deposit in the glomeruli, and cryoglobulinaemia causes a membranoproliferative glomerulonephritis.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Precision drugs define modern care: BTK inhibitors (ibrutinib, zanubrutinib) exploit the MYD88 L265P mutation, and BCL-2 inhibitors add to them, transforming treatment of Waldenström macroglobulinaemia.
- `connects-to` → **[Hepatitis C Virus](../../../02-pathogen/01-viruses/hepatitis-c-virus/README.md)** — A virus that can seed the clone: chronic hepatitis C drives B-cell lymphoproliferation and cryoglobulinaemia, and is an associated antigenic trigger in a subset of IgM-secreting lymphomas like WM.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Chemoimmunotherapy remains a backbone: bendamustine combined with rituximab is a standard frontline regimen for symptomatic Waldenström macroglobulinaemia, alongside the newer targeted agents.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Born of the germinal-centre reaction: Waldenström cells are post-germinal-centre memory B cells carrying somatic hypermutation and the MYD88 L265P mutation, frozen midway between B cell and plasma cell as they secrete monoclonal IgM.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — Monoclonal IgM injures the kidney: type I cryoglobulinaemia and IgM deposition from Waldenström's can cause a membranoproliferative glomerulonephritis, and rarely IgM casts, spilling protein and blood into the urine.
- `connects-to` → **[Sjögren's Syndrome](../sjogrens-syndrome/README.md)** — Autoimmunity can seed it: chronic B-cell stimulation in Sjögren's syndrome raises the risk of lymphoplasmacytic and marginal-zone lymphomas, the same indolent B-cell malignancies that include Waldenström's macroglobulinaemia.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — Its antibody thickens the blood: the monoclonal IgM of Waldenström raises serum viscosity, sludging flow through small vessels and the arterial wall to cause the visual, neurological and bleeding features of hyperviscosity syndrome.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — It can deposit amyloid in the heart: the monoclonal IgM or its light chains in Waldenström can form AL amyloid that infiltrates the myocardium, causing a restrictive cardiomyopathy and heart failure.
- `connects-to` → **[Hemophilia A](../hemophilia-a/README.md)** — It causes an acquired bleeding disorder: the IgM of Waldenström can bind and clear von Willebrand factor, producing an acquired von Willebrand syndrome—a bleeding tendency reached by a different route than inherited haemophilia A.
- `connects-to` → **[CIDP](../cidp/README.md)** — An IgM demyelinating neuropathy: anti-MAG IgM in Waldenström causes a distal demyelinating sensory neuropathy that resembles CIDP, a characteristic paraproteinaemic complication often preceding diagnosis.
- `connects-to` → **[Hereditary Angioedema](../hereditary-angioedema/README.md)** — Acquired angioedema: lymphoplasmacytic clones in Waldenström can consume C1-inhibitor or generate autoantibodies against it, producing a bradykinin-mediated acquired angioedema mimicking the hereditary disease.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Organ infiltration: Waldenström's lymphoplasmacytic cells infiltrate the liver and spleen, enlarging the hepatic lobules and splenic pulp as the disease burden advances.
- `connects-to` → **[Von Willebrand Factor](../../03-molecular/von-willebrand-factor/README.md)** — Acquired von Willebrand syndrome: the high IgM paraprotein of Waldenström binds and clears von Willebrand factor, causing acquired bleeding that, with hyperviscosity, makes mucosal haemorrhage a hallmark.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — BTK inhibitors and atrial fibrillation: ibrutinib, a mainstay of Waldenström therapy, off-targets cardiac kinases to cause atrial fibrillation and conduction disturbance, compounding the strain of IgM hyperviscosity on the heart.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Profound immunoparesis: Waldenström suppresses normal antibody production, and anti-CD20 and BTK-inhibitor therapy deepen the deficit, leaving patients with severe, prolonged COVID-19 and poor vaccine responses.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Marrow angiogenesis: VEGF is elevated in Waldenström and drives the increased bone-marrow microvessel density that supports the lymphoplasmacytic clone.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Inflammatory niche: TNF-α within the bone-marrow microenvironment helps sustain the malignant B-cell clone and contributes to the cytopenias and constitutional symptoms of Waldenström.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Hypoxic marrow: HIF-1α stabilised in the crowded, hypoxic Waldenström marrow promotes the VEGF-driven angiogenesis and survival signalling of the tumour niche.
- `connects-to` → **[BAFF](../../03-molecular/baff/README.md)** — B-cell survival factor: BAFF from the marrow microenvironment supports the survival and expansion of the malignant lymphoplasmacytic clone in Waldenström, sustaining IgM-secreting cells.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — PI3K-mTOR survival: mTOR signalling downstream of MYD88 and the B-cell receptor drives Waldenström cell growth, and the mTOR inhibitor everolimus has clinical activity in the disease.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Complement-mediated hemolysis: monoclonal IgM with cold-agglutinin or cryoglobulin activity fixes complement, so terminal C5-driven haemolysis contributes to the anaemia of some Waldenström patients.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — MYD88 is the signaling adaptor for TLR4 and related innate receptors, so the MYD88 L265P mutation that defines Waldenström drives constitutive NF-κB as if the cell were chronically TLR-stimulated—the mechanistic basis for BTK-inhibitor sensitivity.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K signaling downstream of MYD88 and the B-cell receptor sustains the Waldenström clone in parallel with BTK, contributing to the resistance that emerges when BTK is inhibited alone and supporting combination approaches.
- `connects-to` → **[KIT](../../03-molecular/kit/README.md)** — Waldenström marrow is characteristically infiltrated by KIT-expressing mast cells that nurture the lymphoplasmacytic clone through CD40L and APRIL—a distinctive microenvironmental feature distinguishing it from other indolent lymphomas.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Bendamustine-rituximab and BTK inhibitors ultimately kill Waldenström cells through caspase-3 apoptosis, and the anti-apoptotic BCL-2 these cells express both limits responses and motivates adding venetoclax.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Marrow infiltration by the lymphoplasmacytic clone and IL-6-driven hepcidin blunt erythropoietin-driven red-cell production, making anemia the commonest presenting feature and the usual trigger to start treatment.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — CCL2 recruits monocytes and macrophages into the Waldenström marrow, part of the supportive niche that—alongside the mast cells—feeds the lymphoplasmacytic clone with survival signals.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — MYD88 L265P signaling (already mapped) activates not only BTK-NF-κB but the PI3K-AKT pathway (PIK3CA and mTOR already mapped), a survival axis and route of resistance in Waldenström macroglobulinemia.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — MYD88-driven signaling also engages the MAPK-ERK1/2 cascade, contributing to the proliferation of the lymphoplasmacytic clone and to incomplete responses to BTK inhibition.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — MYC activation cooperates with the MYD88 driver in the progression and high-grade transformation of Waldenström macroglobulinemia to diffuse large B-cell lymphoma.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — Src-family (LYN) kinases relay B-cell-receptor signals upstream of BTK (mapped), feeding the BTK-MYD88-NF-κB axis that drives Waldenström cell survival.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 mutation is an adverse-prognostic lesion in Waldenström macroglobulinemia, associated with treatment resistance and risk of high-grade transformation.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — The cyclin-D-CDK4/6 axis releases E2F1 to drive proliferation of the lymphoplasmacytic clone (MYC mapped) in Waldenström macroglobulinemia.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — Loss of PTEN-restrained PI3K-AKT-mTOR signaling (AKT, PIK3CA and mTOR mapped) reinforces the survival of the MYD88-driven lymphoplasmacytic clone in Waldenström macroglobulinemia.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A (p16) loss releases CDK4/6-cyclin-D control of the cell cycle, contributing to clonal progression in Waldenström macroglobulinemia.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — TERT-mediated telomere maintenance supports the replicative longevity of the malignant lymphoplasmacytic clone in Waldenström macroglobulinemia.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 supports the survival and bone-marrow-niche adhesion of the lymphoplasmacytic clone in Waldenström macroglobulinemia.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — EZH2-mediated polycomb repression contributes to the epigenetic dysregulation of the malignant clone in Waldenström macroglobulinemia.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the immune microenvironment of the bone marrow infiltrated by Waldenström macroglobulinemia.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — BTK and PI3K-AKT signaling (BTK, AKT, and PIK3CA already mapped) inactivates FOXO, supporting survival of the malignant lymphoplasmacytic clone in Waldenström macroglobulinemia.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6 acting on the cyclin-D-RB axis (E2F1 and CDKN2A already mapped) drives the cell-cycle progression of Waldenström macroglobulinemia cells.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling shapes the bone-marrow microenvironment and immune tone that support Waldenström macroglobulinemia.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the survival and Wnt/NF-κB signaling of the lymphoplasmacytic cells of Waldenström macroglobulinemia.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in Waldenström macroglobulinemia.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated cytotoxic immunosurveillance is a component of the immune response to Waldenström macroglobulinemia.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of Waldenström macroglobulinemia.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of the lymphoplasmacytic cells of Waldenström macroglobulinemia.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the inflammatory bone-marrow microenvironment of Waldenström macroglobulinemia.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-family chemokine signaling participates in the bone-marrow niche interactions of Waldenström macroglobulinemia.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of Waldenström macroglobulinemia.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the bone-marrow microenvironment of Waldenström macroglobulinemia.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune bone-marrow microenvironment of Waldenström macroglobulinemia.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory bone-marrow microenvironment of Waldenström macroglobulinemia.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the B-cell-receptor and downstream survival signaling of Waldenström macroglobulinemia.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Anaemia: anaemia from marrow infiltration and IgM-mediated cold-agglutinin haemolysis is the most common presenting feature of Waldenström macroglobulinaemia and a primary indication to begin treatment.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Anaemia of inflammation: IL-6-driven hepcidin (IL-6 already mapped) restricts iron availability in Waldenström macroglobulinaemia, compounding the marrow-infiltration anaemia with a functional iron-restricted component.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Antigen presentation: the lymphoplasmacytic clone of Waldenström may be antigen-driven, and MHC class II shapes the T-cell microenvironment and antigen presentation that support its survival alongside the MYD88-driven signalling already mapped.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — Immunoparesis: the monoclonal IgM of Waldenström is accompanied by suppression of normal immunoglobulins including IgG, the immunoparesis that raises infection risk, while the paraprotein itself can cause hyperviscosity and cryoglobulinaemia.
- `connects-to` → **[Thrombin](../../03-molecular/thrombin/README.md)** — Coagulopathy: the monoclonal IgM interferes with fibrin polymerisation and platelet function and drives an acquired von Willebrand syndrome (vWF already mapped), and hyperviscosity disturbs the thrombin-driven coagulation balance, causing bleeding.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell microenvironment: IL-2-driven T cells in the marrow microenvironment support the survival of the lymphoplasmacytic clone (MHC class II already mapped), part of the immune niche sustaining Waldenström macroglobulinaemia.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Th2 clone support: IL-4 and type-2 T-cell help sustain the IgM-secreting B-cell clone (BAFF and IL-2 already mapped) of Waldenström macroglobulinaemia, part of the cytokine support of the lymphoplasmacytic proliferation.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Hyperviscosity vasculature: the high IgM raises serum viscosity and disturbs microvascular flow, and nitric-oxide-mediated vascular regulation is stressed in the hyperviscosity syndrome that causes the visual and neurological symptoms of Waldenström macroglobulinaemia.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Tumour lysis and oxidation: treating the lymphoplasmacytic clone releases purines that xanthine oxidase converts to uric acid, and the reactive oxygen species it generates add oxidative and tumour-lysis burden to therapy for Waldenström macroglobulinaemia.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Marrow-adipocyte crosstalk: the marrow adipocytes and their adipokine adiponectin engage in metabolic crosstalk with the lymphoplasmacytic clone, the marrow adipose tissue shaping the niche that supports Waldenström macroglobulinaemia.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Adipokine marrow signalling: leptin, with adiponectin (already mapped), from the marrow adipose tissue signals to the clonal and stromal cells, part of the metabolic microenvironment of the infiltrated marrow in Waldenström macroglobulinaemia.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipokine milieu: resistin, with leptin and adiponectin (already mapped), completes the adipokine signalling of the marrow adipose niche that shapes the microenvironment of the lymphoplasmacytic infiltrate in Waldenström macroglobulinaemia.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — M2 marrow milieu: IL-13, with IL-4 (already mapped), supports the M2 macrophage (already mapped) and type-2 milieu of the marrow microenvironment of Waldenström macroglobulinaemia.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — T-cell checkpoint: the PD-1 checkpoint on the T cells of the Waldenström tumour microenvironment contributes to the immune evasion of the lymphoplasmacytic clone.
- `connects-to` → **[CTLA-4](../../03-molecular/ctla-4/README.md)** — Checkpoint co-inhibition: CTLA-4, with PD-1 (already mapped), forms the immune-checkpoint brake on the T cells of the Waldenström tumour microenvironment, part of its immune evasion.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate B-cell signalling: type-I interferon, downstream of the TLR/MYD88 (already mapped) innate signalling of the Waldenström B cells, and the historical interferon therapy of the lymphoma.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Marrow macrophages: the marrow macrophages and tumour-associated macrophages (CCL2 already mapped) support the lymphoplasmacytic clone and the immune microenvironment of Waldenström macroglobulinaemia.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Hepatomegaly: the lymphoplasmacytic infiltration causes the hepatomegaly (with the splenomegaly already mapped) and the organomegaly of Waldenström macroglobulinaemia.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the immune microenvironment of Waldenström macroglobulinaemia.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of the lymphoplasmacytic lymphoma of Waldenström macroglobulinaemia.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of Waldenström macroglobulinaemia.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune microenvironment of the lymphoplasmacytic lymphoma of Waldenström macroglobulinaemia.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the microenvironment (distinct from the monoclonal IgM already mapped) of Waldenström macroglobulinaemia.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — CD8 antitumour arm: the cytotoxic T cells (perforin already mapped) of the immune microenvironment provide the antitumour surveillance of the clonal B cells (already mapped) of Waldenström macroglobulinaemia.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the cytokines (IL-6 already mapped) of the lymphoplasmacytic microenvironment supporting the clonal B cells (already mapped) of Waldenström macroglobulinaemia.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) contributes to the complement dimension of the IgM-mediated (immunoglobulin already mapped) immune-complex and cold-agglutinin phenomena of Waldenström macroglobulinaemia.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Antigen presentation: the dendritic cells present antigen to the T cells (already mapped) shaping the immune microenvironment of Waldenström macroglobulinaemia.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) engaged by the IgM (immunoglobulin already mapped) immune complexes and cold agglutinins of Waldenström macroglobulinaemia.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway activated by the IgM cold agglutinins (immunoglobulin already mapped) that mediate the complement-dependent haemolysis of Waldenström macroglobulinaemia.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Anaemia iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the anaemia of the marrow infiltration and chronic disease of Waldenström macroglobulinaemia.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-marrow axis: TSLP, secreted by bone-marrow (already mapped) stromal cells, activates mast cells (already mapped) and B cells (already mapped), amplifying the MYD88 (already mapped)-driven plasmacytic differentiation of Waldenström macroglobulinaemia.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-hyperviscosity axis: bradykinin, generated by the kallikrein-kinin system in the hyperviscous IgM (immunoglobulin already mapped) plasma environment, augments vascular permeability and contributes to the vascular complications of Waldenström macroglobulinaemia.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell mediator: histamine, released from the activated mast cells (already mapped) recruited to the marrow niche of Waldenström macroglobulinaemia, promotes B-cell (already mapped) and plasmacytic survival via H2 receptor signalling in the disease microenvironment.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Marrow ECM scaffold: periostin, expressed by stromal fibroblasts and bone marrow mesenchymal cells (already mapped) in the Waldenström niche, promotes the fibrotic extracellular matrix remodelling that supports the MYD88-mutant B-cell/plasmacytic infiltration of the disease.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian haematopoietic protection: melatonin, via MT1/MT2 receptors on haematopoietic progenitors (already mapped) and NK cells (already mapped), suppresses the pro-tumour cytokine milieu and the CXCL13-driven (already mapped) B-cell trafficking of Waldenström macroglobulinaemia.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Immune-endocrine B-cell axis: prolactin, acting via PRLR on B cells (already mapped) and plasmacytic cells, promotes immunoglobulin production (IgM already mapped) and the survival of the malignant clone in the marrow niche of Waldenström macroglobulinaemia.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — WM testosterone: testosterone, via androgen receptors on B cells (already mapped) and plasma cells (already mapped), modulates the MYD88 (already mapped)/NF-κB (already mapped) signalling; androgen deficiency amplifies WM clone expansion in the bone-marrow (already mapped) niche.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — WM serotonin: mast-cell (already mapped) serotonin promotes the hyperviscosity and vascular complications of WM; 5-HT2 signalling on platelet (already mapped) and erythrocyte (already mapped) surfaces amplifies the NF-κB (already mapped) inflammatory niche of Waldenström.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — WM oxytocin: oxytocin, via OXTR on bone-marrow (already mapped) stromal cells and regulatory T cells (already mapped), attenuates the MYD88 (already mapped)/NF-κB (already mapped) pro-tumour microenvironment and the B-cell (already mapped) clone survival of Waldenström.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — WM vasopressin: vasopressin, via V1B receptors on plasma cells (already mapped) and B cells (already mapped), modulates the bone-marrow (already mapped) microenvironment and amplifies NF-κB (already mapped)/MYD88 (already mapped) clone-survival signalling in Waldenström.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — WM selenium: selenium-dependent GPx suppresses the ROS amplifying NF-κB (already mapped)/MYD88 (already mapped) tumour microenvironment in the bone-marrow (already mapped); selenium deficiency promotes oxidative vascular injury and IgM (already mapped) hyperviscosity of WM.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — WM iodine: iodine-dependent thyroid hormones modulate B-cell (already mapped) differentiation and haematopoietic cycling in the bone-marrow (already mapped); hypothyroidism amplifies the pro-tumour macrophage (already mapped) and NF-κB (already mapped) signalling niche of WM.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — WM zinc: zinc cofactors macrophage (already mapped) anti-tumour function and B-cell (already mapped) homeostasis; zinc deficiency amplifies NF-κB (already mapped) and MYD88 (already mapped) and IL-6 (already mapped) B-cell (already mapped) clonal expansion in WM.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — WM magnesium: magnesium supports macrophage (already mapped) anti-inflammatory resolution and B-cell (already mapped) regulation; magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) tumour-promoting cascade in WM.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — WM copper: copper-dependent SOD in macrophages (already mapped) and B-cell (already mapped) quenches ROS; copper deficiency amplifies MYD88 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) tumour-promoting cascade of Waldenström.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — WM potassium: potassium efflux from macrophages (already mapped) and B-cell (already mapped) modulates NLRP3-IL-1β; potassium dysregulation amplifies NF-κB (already mapped) and MYD88 (already mapped) and IL-6 (already mapped) clonal survival cascade of Waldenström.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — WM calcium: calcium signalling in B-cell (already mapped) and plasma-cell (already mapped) drives MYD88 (already mapped)/NF-κB (already mapped) clonal activation; calcium dysregulation amplifies IL-6 (already mapped) and IgM (already mapped) hyperviscosity cascade of WM.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — WM carbon: carbon, as metabolic backbone of IgM (already mapped) and MYD88 (already mapped) in B-cell (already mapped) and plasma-cell (already mapped), drives clonal expansion; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of WM.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — WM chloride: chloride channels in B-cell (already mapped) and macrophages (already mapped) modulate clonal B-cell survival; chloride dysregulation amplifies NF-κB (already mapped) and MYD88 (already mapped) and IL-6 (already mapped) hyperviscosity cascade of WM.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — WM hydrogen: hydrogen, via redox homeostasis in B-cell (already mapped) and macrophages (already mapped), quenches NF-κB-driven ROS; hydrogen dysregulation amplifies MYD88 (already mapped) and IL-6 (already mapped) and IgM (already mapped) clonal cascade of WM.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — WM nitrogen: nitric oxide from B-cell (already mapped) and macrophages (already mapped) modulates clonal B-cell survival; nitrogen imbalance amplifies NF-κB (already mapped) and MYD88 (already mapped) and IL-6 (already mapped) hyperviscosity cascade of WM.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — WM sulfur: hydrogen sulfide from B-cell (already mapped) and macrophages (already mapped) modulates redox homeostasis; sulfur deficiency amplifies NF-κB (already mapped) and MYD88 (already mapped) and IL-6 (already mapped) clonal cascade of waldenstrom macroglobulinemia.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — WM oxygen: mitochondrial oxygen in B-cell (already mapped) and macrophages (already mapped) drives ATP for clonal proliferation; hypoxia amplifies NF-κB (already mapped) and MYD88 (already mapped) and IL-6 (already mapped) hyperviscosity cascade of WM.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — WM GLP-1: GLP-1 from gut L-cells (already mapped) and macrophages (already mapped) modulates lymphoma metabolic homeostasis; GLP-1 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of Waldenström macroglobulinemia.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — WM angiotensin-II: Angiotensin-II in B-cells (already mapped) and macrophages (already mapped) promotes lymphoma stroma activation; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of Waldenström macroglobulinemia.
- `connects-to` → **[Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — WM Wnt/β-catenin: Wnt/β-catenin in B-cells (already mapped) and macrophages (already mapped) drives lymphoma clonal expansion; Wnt dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of Waldenström macroglobulinemia.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — WM rankl: RANKL in macrophages (already mapped) and B-cells (already mapped) modulates WM bone-immune axis; RANKL excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of Waldenström macroglobulinemia.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — WM fibronectin: Fibronectin in B-cells (already mapped) and macrophages (already mapped) scaffolds lymphoma ECM; fibronectin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of Waldenström macroglobulinemia.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — WM notch: NOTCH on B-cells (already mapped) and macrophages (already mapped) regulates WM clonal immune tone; NOTCH dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of Waldenström macroglobulinemia.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — WM igf-1: IGF-1 from macrophages (already mapped) and B-cells (already mapped) promotes WM clonal B-cell growth; igf-1 excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of Waldenström macroglobulinemia.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — WM activin-a: activin-A from macrophages (already mapped) and B-cells (already mapped) regulates WM immune-fibrotic balance; activin-a excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of Waldenström macroglobulinemia.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — WM tgf-beta: TGF-β from macrophages (already mapped) and B-cells (already mapped) drives WM stromal fibrosis; tgf-beta excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of Waldenström macroglobulinemia.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — WM cgrp: CGRP from macrophages (already mapped) and B-cells (already mapped) modulates WM vascular-immune tone; cgrp dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of Waldenström macroglobulinemia.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — WM calcitonin: calcitonin from macrophages (already mapped) and B-cells (already mapped) modulates WM calcium balance; calcitonin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of Waldenström macroglobulinemia.
- `connects-to` → **[Substance P](../../03-molecular/substance-p/README.md)** — WM substance-p: substance P from macrophages (already mapped) and B-cells (already mapped) modulates WM neuroimmune tone; substance-p excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of Waldenström macroglobulinemia.
- `connects-to` → **[Insulin Receptor](../../03-molecular/insulin-receptor/README.md)** — WM insulin-receptor: insulin receptor on macrophages (already mapped) and B-cells (already mapped) drives WM metabolic tone; insulin-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of Waldenström macroglobulinemia.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — WM aldosterone: aldosterone from macrophages (already mapped) and B-cells (already mapped) modulates WM ion balance; aldosterone excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of Waldenström macroglobulinemia.
- `connects-to` → **[Androgen Receptor](../../03-molecular/androgen-receptor/README.md)** — WM androgen-receptor: androgen receptor on macrophages (already mapped) and B-cells (already mapped) modulates WM hormonal tone; androgen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of Waldenström macroglobulinemia.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — WM norepinephrine: norepinephrine from macrophages (already mapped) and B-cells (already mapped) modulates WM adrenergic tone; norepinephrine excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of Waldenström macroglobulinemia.
- `connects-to` → **[Adrenomedullin](../../03-molecular/adrenomedullin/README.md)** — WM adrenomedullin: adrenomedullin from macrophages (already mapped) and B-cells (already mapped) modulates WM vascular tone; adrenomedullin loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of Waldenström macroglobulinemia.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — WM bdnf: BDNF from macrophages (already mapped) and B-cells (already mapped) modulates WM neuroimmune tone; bdnf loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of Waldenström macroglobulinemia.

[^treon-2015-ibrutinib-wm]: Treon SP, Tripsas CK, Meid K, et al. Ibrutinib in previously treated Waldenström's macroglobulinemia. *N Engl J Med.* 2015;373(18):1765-1774. [doi:10.1056/NEJMoa1501548](https://doi.org/10.1056/NEJMoa1501548) · [PubMed 26352686](https://pubmed.ncbi.nlm.nih.gov/26352686/)
[^tam-2020-aspen]: Tam CS, Opat S, D'Sa S, et al. A randomized phase 3 trial of zanubrutinib vs ibrutinib in symptomatic Waldenström macroglobulinemia: the ASPEN study. *Blood.* 2020;136(18):2038-2050. [doi:10.1182/blood.2020006844](https://doi.org/10.1182/blood.2020006844) · [PubMed 32828187](https://pubmed.ncbi.nlm.nih.gov/32828187/)
