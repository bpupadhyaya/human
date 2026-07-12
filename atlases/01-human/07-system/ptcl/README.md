---
schema: human-scale-entry/v1
id: ptcl
name: Peripheral T-cell Lymphoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "PTCLs are aggressive T/NK-cell lymphomas (~10-15% of NHL); major subtypes PTCL-NOS (~25%), AITL (~20%), ALK+ ALCL (~7%), ALK- ALCL (~8%); AITL driven by TET2+DNMT3A+RHOA G17V; brentuximab vedotin+CHP is standard for CD30+ PTCL (ECHELON-2); 5-year OS ~30-50%."
aliases: ["PTCL", "peripheral T-cell lymphoma", "AITL", "angioimmunoblastic T-cell lymphoma", "ALCL", "anaplastic large cell lymphoma", "ALK+ ALCL", "ALK- ALCL", "T-cell lymphoma", "PTCL-NOS"]
sources:
  - id: horwitz-2019-echelon2
    type: peer-reviewed
    cite: "Horwitz S, O'Connor OA, Pro B, et al. Brentuximab vedotin with chemotherapy for CD30-positive peripheral T-cell lymphoma (ECHELON-2): a global, double-blind, randomised, phase 3 trial. Lancet. 2019;393(10168):229-240."
    doi: "10.1016/S0140-6736(18)32984-2"
    pmid: "30522922"
    url: "https://doi.org/10.1016/S0140-6736(18)32984-2"
  - id: palomero-2014-ptcl-epigenetics
    type: peer-reviewed
    cite: "Palomero T, Couronné L, Khiabanian H, et al. Recurrent mutations in epigenetic regulators, RHOA and FYN kinase in peripheral T cell lymphomas. Nat Genet. 2014;46(2):166-170."
    doi: "10.1038/ng.2872"
    pmid: "24413734"
    url: "https://doi.org/10.1038/ng.2872"
cross_links:
  - target: 01-human/03-molecular/tet2
    relation: connects-to
    note: "TET2 loss-of-function is the most common mutation in AITL (~60-80%) and a major driver in PTCL-NOS (~20%); TET2+DNMT3A+RHOA G17V is the canonical AITL triplet; TET2 mutations arise in a pre-malignant TFH HSC clone and precede RHOA G17V acquisition."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A R882H/C mutations occur in ~20-30% of AITL and ~15% PTCL-NOS, co-mutating with TET2 in the pre-malignant TFH clone; DNMT3A+TET2 co-loss → genome-wide hypermethylation; therapy-related T-cell lymphomas from DNMT3A CHIP clones have been reported."
  - target: 01-human/03-molecular/alk
    relation: connects-to
    note: "NPM1-ALK t(2;5)(p23;q35) defines ALK+ ALCL (~7% of PTCL); ALK fusion drives JAK-STAT3 constitutive activation; crizotinib, alectinib, brigatinib active in ALK+ ALCL; ALK+ ALCL is the most favorable PTCL subtype (5-year OS ~70-80% with A+CHP)."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "PD-1 is a TFH cell surface marker expressed in AITL tumor cells; anti-PD-1 (pembrolizumab, nivolumab) has activity in relapsed PTCL (ORR ~15-30%) but risk of paradoxical lymphoma acceleration in AITL; PD-L1 overexpressed on ALK- ALCL via DUSP22/IRF4 rearrangements."
  - target: 01-human/03-molecular/idh2
    relation: connects-to
    note: "IDH2 R172K (distinct from MDS R140Q) occurs in ~20-30% of AITL/nTFHL; IDH2 → 2-HG → TET2 + KDM competitive inhibition → epigenetic reprogramming; enasidenib (IDH2 inhibitor, approved AML) explored in IDH2-mutant AITL; IDH2+TET2 co-mutation drives extreme hypermethylation."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "Constitutive STAT3 activation in ALK+ ALCL (NPM1-ALK → JAK3 → STAT3), ALK- ALCL (STAT3 activating mutations ~15%), and HSTCL (STAT3/STAT5b mutations); STAT3 drives CD30, BCL-2, MCL-1, and VEGF → lymphoma survival; ruxolitinib (JAK1/2→STAT3) has activity in PTCL trials."
  - target: 01-human/03-molecular/cd30
    relation: connects-to
    note: "CD30 (TNFRSF8) is the primary PTCL therapeutic target; brentuximab vedotin (anti-CD30 ADC) FDA-approved for ALCL and CD30+ PTCL; ECHELON-2: BV+CHP vs CHOP → PFS HR 0.71; CD30 in ALCL (~100%), PTCL-NOS (~30-50%); CD30 signals via TRAF1/2/3 → NF-κB → lymphoma survival."
  - target: 01-human/07-system/pcnsl
    relation: connects-to
    note: "Peripheral T-cell lymphoma and primary CNS lymphoma are aggressive non-Hodgkin lymphomas of opposite lineage: PTCL is a heterogeneous T-cell group (TET2/RHOA/STAT3-driven), PCNSL a CNS-confined B-cell (DLBCL) tumor driven by MYD88 — lineage and site reshape lymphoma biology."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Angioimmunoblastic T-cell lymphoma, a major PTCL subtype, arises from the follicular helper T cell (TFH): tumor cells keep TFH markers (PD-1, CXCL13, ICOS, BCL6) and recruit a reactive B-cell/EBV background, while TET2/DNMT3A/RHOA-G17V mutations drive the malignancy."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "The skin is a defining PTCL site: primary cutaneous CD30+ T-cell lymphomas (cutaneous ALCL, lymphomatoid papulosis) and the mycosis fungoides/Sézary spectrum home to skin, often indolent — contrasting with the aggressive nodal PTCLs like AITL and systemic ALCL."
  - target: 01-human/07-system/dlbcl
    relation: connects-to
    note: "Peripheral T-cell and diffuse large B-cell lymphoma are the aggressive non-Hodgkin lymphomas of the two lineages: PTCL arises from mature T cells, is rarer, and has a worse prognosis than DLBCL, which is CD20+ and responds to rituximab-based R-CHOP that PTCL cannot use."
  - target: 01-human/07-system/hodgkin-lymphoma
    relation: connects-to
    note: "PTCL and Hodgkin lymphoma intersect at CD30: anaplastic large cell lymphoma, a PTCL subtype, strongly expresses CD30 like Hodgkin's Reed-Sternberg cells, so the anti-CD30 drug brentuximab vedotin treats both—and the two can be hard to distinguish histologically."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Some peripheral T-cell lymphomas derive from regulatory or follicular-helper T cells: adult T-cell leukemia often has a Treg-like FOXP3+ phenotype and angioimmunoblastic PTCL arises from follicular-helper T cells—so the normal T-cell subset shapes the lymphoma."
  - target: 02-pathogen/01-viruses/epstein-barr-virus
    relation: connects-to
    note: "Several peripheral T-cell lymphomas are EBV-driven: extranodal NK/T-cell lymphoma is defined by EBV infection, and angioimmunoblastic T-cell lymphoma harbors EBV-positive B-immunoblasts—so the virus shapes diagnosis and biology across this T-cell lymphoma group."
  - target: 01-human/07-system/mantle-cell-lymphoma
    relation: connects-to
    note: "PTCL and mantle cell lymphoma are both aggressive non-Hodgkin lymphomas but of opposite lineage: PTCL arises from mature T cells, while MCL is a B-cell tumor with t(11;14) cyclin D1—immunophenotyping the T- versus B-cell origin guides therapy."
  - target: 01-human/07-system/follicular-lymphoma
    relation: connects-to
    note: "PTCL and follicular lymphoma sit at opposite ends of lineage and tempo: follicular lymphoma is an indolent germinal-center B-cell tumor, while most PTCLs are aggressive mature T-cell cancers—the T-versus-B distinction fundamentally separates their biology and treatment."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "PTCL includes NK/T-cell lymphomas: peripheral T-cell lymphomas span many entities, and the related extranodal NK/T-cell lymphoma is an aggressive, EBV-driven, often nasal tumor—so the T/NK lineage spawns a heterogeneous, generally poor-prognosis lymphoma group."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "PTCL is a lymphoma of the lymphatic system's T cells: unlike the common B-cell lymphomas, it arises from mature T cells in lymph nodes and spreads through the lymphatic network, often with systemic B symptoms and a worse outcome than B-cell lymphomas."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Bone marrow involvement is common and ominous in PTCL: these aggressive T-cell lymphomas frequently infiltrate the marrow, causing cytopenias and upstaging disease—so marrow biopsy is part of staging and marrow disease worsens an already poor prognosis."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "PTCL spans many T-cell subsets, including cytotoxic-T-cell-derived types: extranodal NK/T-cell and hepatosplenic lymphomas arise from cytotoxic lineage cells, so unlike B-cell lymphomas, PTCL's diversity reflects the many normal T-cell populations it can mimic."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "Some PTCLs home to the spleen and liver: hepatosplenic T-cell lymphoma infiltrates these organs (often in immunosuppressed patients) causing cytopenias without nodal masses, so an aggressive T-cell lymphoma can present as hepatosplenomegaly rather than lymphadenopathy."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "PTCL both arises from and dysregulates the immune system: angioimmunoblastic T-cell lymphoma in particular causes autoimmune features and immunodeficiency as the malignant helper T cells distort immune regulation—so infection and autoimmunity complicate the disease."
  - target: 01-human/06-organ/thymus
    relation: connects-to
    note: "T-cell lymphomas trace back to the thymus-educated T lineage: PTCLs are malignancies of mature post-thymic T cells, so unlike T-ALL they arise after thymic development—their subtype reflecting which mature T-cell type (helper, cytotoxic, NK-like) transformed."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Angioimmunoblastic PTCL springs from germinal-center helper cells: it arises from T-follicular-helper cells that normally aid B cells in germinal centers, which is why this subtype shows expanded follicular dendritic networks and reactive B-cell proliferation."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Angioimmunoblastic T-cell lymphoma expands follicular dendritic cells: a hallmark is a proliferating meshwork of follicular dendritic cells and high endothelial venules around the tumor T cells, giving the node its distinctive polymorphous, vascular appearance."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Angioimmunoblastic PTCL builds a forest of new vessels via VEGF: this T-cell lymphoma drives prominent arborizing blood vessels that are a diagnostic hallmark, fed by VEGF from the tumor and its inflammatory backdrop."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "PTCL hides malignant T cells in a crowd of macrophages: especially in AITL, a polymorphous infiltrate of macrophages, eosinophils, and plasma cells can outnumber the cancer cells, making the diagnosis easy to miss."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "PTCL's systemic symptoms run on IL-6: tumor and bystander cells pour out IL-6 and other cytokines that cause the fevers, weight loss, rash, and high antibody levels typical of angioimmunoblastic lymphoma."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Some T-cell lymphomas raise blood calcium dangerously: adult T-cell leukemia/lymphoma from HTLV-1 secretes factors like PTHrP that pull calcium from bone, so hypercalcemia is a hallmark emergency of this PTCL subtype."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "T-cell lymphoma can arise in the gut itself: enteropathy-associated T-cell lymphoma grows in the intestine, often on a background of celiac disease, so unexplained bowel symptoms or perforation in celiac patients raise the alarm."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "PTCL survives on constitutive NF-kB signaling: the malignant T cells keep this survival switch active downstream of T-cell-receptor and cytokine inputs, sustaining proliferation and making the pathway a target in these aggressive lymphomas."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Peripheral T-cell lymphoma drains iron and blood: marrow involvement and chronic inflammation suppress red-cell production and lock iron away, so anemia commonly accompanies these aggressive lymphomas."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Some T-cell lymphomas home to the liver: hepatosplenic T-cell lymphoma infiltrates the liver and spleen rather than forming nodal masses, enlarging both organs in this rare, aggressive subtype."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Angioimmunoblastic PTCL sprouts blood vessels: it is marked by a striking proliferation of arborizing high-endothelial venules, so its endothelial cells multiply alongside the malignant T cells."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photons stage and track PTCL: these lymphomas are avid for FDG, so PET-CT lights up nodal and extranodal disease for staging and gauges whether the aggressive tumor is melting away under chemotherapy."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "One PTCL is born in the gut: enteropathy-associated T-cell lymphoma arises from the intraepithelial T cells of the small intestine in long-standing celiac disease, presenting with bowel perforation or obstruction in a malnourished patient."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Angioimmunoblastic PTCL turns the immune system on its own red cells: the dysregulated helper-T-cell tumor drives autoantibodies that coat erythrocytes, producing a Coombs-positive hemolytic anemia alongside the lymphoma."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "AITL floods the blood with antibody: its malignant follicular-helper T cells whip up a polyclonal plasma-cell response, producing the hypergammaglobulinemia and autoantibodies that give angioimmunoblastic lymphoma its autoimmune-like face."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "A T-cell cancer that breeds rogue B cells: the helper-T tumor of AITL fosters EBV-driven B-cell blasts in its inflamed milieu, expansions that can themselves transform into a secondary diffuse large B-cell lymphoma."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "The CHOP backbone bites the nerves: vincristine, part of the standard PTCL chemotherapy, poisons the microtubule transport of peripheral neurons, leaving a dose-limiting numbness, tingling, and weakness."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies name and target PTCL: a CD3, CD30, and ALK stain panel sorts the subtypes on biopsy, and the CD30-positive ones — anaplastic large-cell lymphoma especially — are hit by the anti-CD30 antibody-drug conjugate brentuximab vedotin."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "The CHOEP regimen empties the marrow: the cyclophosphamide, etoposide, and anthracycline given for PTCL are heavily myelosuppressive, so neutrophil counts crater between cycles and growth-factor support and infection vigilance are routine."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Bulky, fast PTCL threatens the kidney: starting chemotherapy can burst the tumor into tumor lysis syndrome, flooding the blood with potassium, phosphate, and urate that crystallize in and injure the kidney unless hydration and rasburicase pre-empt it."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "The CHOP backbone strains the heart: the doxorubicin in standard PTCL chemotherapy is cumulatively cardiotoxic to cardiomyocytes, so cardiac function is checked before and during the anthracycline-based regimens these aggressive lymphomas require."
  - target: 01-human/03-molecular/jak2
    relation: connects-to
    note: "Many PTCLs run on JAK-STAT: recurrent activation of the JAK2-STAT3 pathway drives several subtypes, especially the NK/T-cell and ALK-negative anaplastic forms, making JAK inhibition an actively studied targeted approach."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Cure can cost fertility: the multi-agent and high-dose chemotherapy, sometimes with transplant, used against these aggressive lymphomas damages the gonads, so fertility preservation is discussed before treating younger patients."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "One subtype is born in the damaged gut: enteropathy-associated T-cell lymphoma arises from the intraepithelial T cells of the small-bowel lining injured by celiac disease, turning chronic mucosal inflammation into an aggressive intestinal lymphoma."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Survival signaling runs through a familiar hub: PI3K-AKT-mTOR activation supports the malignant T cells across PTCL subtypes, so mTOR inhibitors are tested in a group of lymphomas that respond poorly to standard chemotherapy."
  - target: 01-human/07-system/mds
    relation: connects-to
    note: "The cure can sow a second cancer: the intensive chemotherapy and autologous transplant used against PTCL damage the marrow, raising the risk of therapy-related myelodysplastic syndromes years later."
  - target: 01-human/07-system/cytokine-storm
    relation: connects-to
    note: "Aggressive T-cell lymphoma can ignite the immune system: PTCL is a leading driver of secondary hemophagocytic lymphohistiocytosis, a cytokine storm of runaway macrophage activation that can be the lethal presenting picture."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Disease and treatment both gut immunity: the T-cell malignancy itself plus intensive chemotherapy leave PTCL patients profoundly immunosuppressed and prone to opportunistic infection and sepsis."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Inflammasome activation feeds the cytokine flood: NLRP3-driven IL-1β release contributes to the hyperinflammatory, HLH-like state that can complicate aggressive peripheral T-cell lymphomas."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "An aggressive lymphoma is a prothrombotic state: bulky nodal disease, the inflammatory cytokine milieu and indwelling catheters during therapy combine to raise venous thromboembolism risk in PTCL patients."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: connects-to
    note: "T-cell loss is exactly its opening: PTCL depletes the CD4 T-cells that hold Pneumocystis in check, and the intensive chemotherapy compounds it, so PJP prophylaxis is standard during treatment."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Marrow involvement and cytokines starve the red cells: PTCL infiltrating the bone marrow alongside its high IL-6 drive raises hepcidin and suppresses erythropoiesis, contributing an anemia-of-chronic-disease component to the cytopenias."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Its intensive chemo and T-cell defect open the lung to mold: CHOP-based therapy plus the profound T-cell immunodeficiency of PTCL cause deep neutropenia, letting inhaled Aspergillus invade as pulmonary aspergillosis."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Its anthracycline backbone can weaken the heart: doxorubicin in the CHOP/CHOEP regimens for PTCL is dose-dependently cardiotoxic, risking a cardiomyopathy and heart failure during and after treatment."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "An aggressive lymphoma with poor odds weighs on mood: PTCL's rapid course, relapsing pattern and grueling therapy impose a heavy psychological burden that contributes to depression and anxiety."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "Chemotherapy reawakens shingles: the CHOP/CHOEP and salvage regimens for PTCL deplete T-cell immunity, allowing latent varicella-zoster to reactivate, so antiviral prophylaxis is standard."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Bulky disease and chemo strain the kidneys: rapid tumour lysis from treating a high-burden PTCL, plus nephrotoxic agents, can cause acute kidney injury that may settle into chronic impairment."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "An aggressive, relapsing lymphoma breeds worry: the poor prognosis, high relapse rate and intensive therapy of PTCL foster chronic health anxiety alongside the depression it brings."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "One subtype erupts in the bowel: enteropathy-associated T-cell lymphoma arises in the small intestine of coeliac disease, causing pain, obstruction, bleeding and a high risk of perforation."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "T-cell lymphomas often involve the skin: PTCL subtypes infiltrate the skin with plaques, nodules and ulcers, and angioimmunoblastic disease causes a widespread paraneoplastic rash."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It reaches the nervous system: PTCL can involve the central nervous system and meninges, and its chemotherapy adds peripheral neuropathy, complicating its aggressive course."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "One subtype floods the blood with calcium: adult T-cell leukaemia/lymphoma, an HTLV-1-driven PTCL, classically causes severe paraneoplastic hypercalcaemia from osteoclast-activating signals."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It crowds and exposes the chest: mediastinal and pulmonary involvement and pleural effusions occur, and the profound immunosuppression invites opportunistic pneumonia."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its chemotherapy can scar the heart: the anthracycline in CHOP-based regimens for PTCL carries a dose-dependent cardiotoxicity risk."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It can dissolve bone: adult T-cell leukaemia/lymphoma classically causes severe hypercalcaemia with lytic bone lesions, and marrow involvement causes cytopenias."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Treatment and metabolism reach the kidney: tumour lysis syndrome at the start of therapy and ATLL hypercalcaemia threaten acute kidney injury."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Targeted antibodies refine its treatment: brentuximab vedotin against CD30 and HDAC inhibitors supplement CHOP-based chemotherapy in peripheral T-cell lymphoma."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "CHOEP then transplant: peripheral T-cell lymphoma is treated with anthracycline regimens like CHOEP followed by autologous stem-cell transplant, yet responds far worse than B-cell lymphomas with frequent early relapse."
  - target: 01-human/07-system/burkitt-lymphoma
    relation: connects-to
    note: "A B-lineage aggressive counterpart: Burkitt and PTCL are both aggressive non-Hodgkin lymphomas, but Burkitt is a MYC-driven B-cell tumour cured by intensive chemo, whereas PTCL is a chemo-resistant T-cell malignancy — lineage dictates prognosis."
  - target: 03-medicine/01-modern/13-cancer/car-t
    relation: connects-to
    note: "Fratricide blocks T-cell CAR-T: the CAR-T therapy that transformed B-cell lymphoma is hard to apply to PTCL because engineered T-cells share target antigens with the tumour and kill each other, driving gene-edited and NK-cell designs."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "Shared epigenetic mutations: angioimmunoblastic T-cell lymphoma carries TET2, DNMT3A and IDH2 mutations like acute myeloid leukaemia and clonal haematopoiesis, sometimes arising from the same mutant haematopoietic precursor."
  - target: 01-human/07-system/nsclc
    relation: connects-to
    note: "A shared ALK fusion: ALK-positive anaplastic large-cell lymphoma and ALK-rearranged non-small-cell lung cancer both depend on a constitutively active ALK kinase, so ALK inhibitors like crizotinib treat both across blood and lung."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Immunotherapy with a caveat: some peripheral T-cell lymphomas (especially EBV-driven or PD-L1-high subtypes) respond to PD-1 inhibitors, but checkpoint blockade can paradoxically accelerate certain T-cell lymphomas, so it is used cautiously."
  - target: 01-human/07-system/cmml
    relation: connects-to
    note: "Shared clonal-haematopoiesis mutations: angioimmunoblastic T-cell lymphoma shares TET2 and DNMT3A mutations with CMML and other myeloid neoplasms, a common clonal-haematopoiesis origin—patients can develop both."
  - target: 01-human/07-system/idh-mutant-glioma
    relation: connects-to
    note: "A shared IDH2 oncometabolite: angioimmunoblastic PTCL carries IDH2 mutations like those of IDH-mutant glioma and AML, producing 2-hydroxyglutarate—an unexpected metabolic link to a brain tumour."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Hepatosplenic infiltration: PTCL, especially the hepatosplenic subtype, infiltrates the sinusoids of the hepatic lobule and the spleen, causing cytopenias and hepatosplenomegaly."
  - target: 01-human/07-system/sjogrens-syndrome
    relation: connects-to
    note: "An autoimmune masquerade: angioimmunoblastic T-cell lymphoma presents with rash, polyclonal hypergammaglobulinaemia, autoimmune cytopenias and sicca that mimic Sjogren's, while chronic autoimmunity itself raises lymphoma risk."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Immunosuppression and T-cell clones: rheumatoid arthritis and its therapies raise lymphoma risk, and RA is classically associated with T-cell large granular lymphocytic leukaemia, a clonal T-cell disorder on the PTCL spectrum."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "Immunodeficiency-driven lymphoma: HIV-associated immune dysregulation and EBV reactivation raise the risk of aggressive non-Hodgkin lymphomas, including peripheral T-cell lymphomas alongside the more common B-cell types."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Epigenetic dysregulation: EZH2 and the broader epigenetic machinery (with TET2, DNMT3A and IDH2) are deranged in angioimmunoblastic and other peripheral T-cell lymphomas, a rationale for epigenetic therapy."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Inflammatory microenvironment: an IFN-γ-rich, cytotoxic-skewed microenvironment characterises many peripheral T-cell lymphomas, driving the B symptoms and immune dysregulation of the disease."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell growth axis: IL-2 and its receptor subunit CD25 drive the proliferation of malignant T cells in peripheral T-cell lymphoma, and CD25 is exploited by targeted antibody-drug conjugates."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Inflammatory milieu: TNF-α within the peripheral T-cell lymphoma microenvironment drives the B symptoms and supports the malignant T-cell clone."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Cell-cycle drive: cyclin D-CDK4/6 activity propels malignant T cells through the G1 checkpoint in peripheral T-cell lymphoma, fuelling its proliferation."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Tumour hypoxia: HIF-1α stabilised in the hypoxic nodal microenvironment supports the metabolism and angiogenesis of peripheral T-cell lymphoma."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK-STAT activation: recurrent JAK1/JAK2 and STAT3 mutations drive constitutive JAK-STAT signalling in several PTCL subtypes, the rationale for testing ruxolitinib and other JAK inhibitors in this hard-to-treat lymphoma."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Immunosuppressive milieu: TGF-β in the PTCL microenvironment dampens cytotoxic responses and shapes the reactive infiltrate, especially in angioimmunoblastic T-cell lymphoma where the tumour cells are a minority among bystander cells."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Reactive infiltrate: CCL2 secreted within PTCL nodes recruits monocytes and macrophages into the prominent inflammatory background that characterises angioimmunoblastic and other peripheral T-cell lymphomas."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K dependence: peripheral T-cell lymphomas frequently depend on PI3K signalling, the rationale for the dual PI3K-δ/γ inhibitor duvelisib, which targets both the malignant T cells and the supportive tumour-microenvironment cells."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Apoptotic resistance: anti-apoptotic BCL-2-family proteins help PTCL cells evade the death programme, underlying the chemoresistance of these aggressive lymphomas and motivating BH3-mimetic combinations under study."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Cytotoxic cell of origin: a subset of peripheral T-cell lymphomas derive from cytotoxic T or NK cells and express perforin and granzyme, the cytotoxic-molecule phenotype that defines extranodal NK/T-cell and hepatosplenic lymphomas with their aggressive course."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Transformation driver: MYC deregulation drives the aggressive behaviour and large-cell transformation of peripheral T-cell lymphomas, cooperating with the epigenetic TET2/DNMT3A/IDH2 lesions already mapped to accelerate disease."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Angioimmunoblastic vasculature: AITL, the commonest Tfh-derived PTCL, shows prominent arborizing high-endothelial venules, and PDGF angiogenic signalling helps build this vascular, follicular-dendritic-cell-rich microenvironment alongside the VEGF already mapped."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immune dysregulation: the Tfh tumour and microenvironment of angioimmunoblastic T-cell lymphoma secrete immunosuppressive IL-10, contributing to the autoimmunity, hypergammaglobulinaemia and infection susceptibility characteristic of the disease."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ALK-MAPK: the NPM-ALK fusion of ALK-positive anaplastic large cell lymphoma (ALK mapped) signals through the MAPK-ERK cascade to drive proliferation of this PTCL subtype."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "ALK-PI3K survival: ALK also engages PI3K-AKT (PIK3CA and mTOR already mapped), a survival pathway downstream of the fusion kinase in anaplastic large cell lymphoma."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Cell-cycle output: cyclin-D1 (mapped) and CDK4/6 release E2F1 to drive the cell-cycle progression of peripheral T-cell lymphoma."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Checkpoint loss: dysregulation of the RB1-E2F checkpoint (cyclin-D1 and E2F1 already mapped) contributes to the proliferation of peripheral T-cell lymphoma."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "RAS proliferation: RAS-ERK signalling (ERK1/2 already mapped) downstream of T-cell-receptor and cytokine inputs provides a proliferative drive in peripheral T-cell lymphoma."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "NF-κB activation: TLR-MyD88-NF-κB signalling (NF-κB already mapped) contributes to the constitutive NF-κB activation characteristic of several peripheral T-cell lymphoma subtypes."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 modulates T-cell-lymphoma survival and the immune microenvironment of peripheral T-cell lymphoma."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β mapped) shapes the immunosuppressive microenvironment, prominent in the Tfh-derived angioimmunoblastic subtype of peripheral T-cell lymphoma."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "Loss of PTEN restraint on PI3K-AKT-mTOR signalling (AKT, PIK3CA and mTOR mapped) supports proliferation and survival in peripheral T-cell lymphoma."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the antitumour immune response and the interferon-associated subtypes of peripheral T-cell lymphoma."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING modulates the inflammatory microenvironment of peripheral T-cell lymphoma."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6-cyclin-D activity (cyclin-D1 and RB1 already mapped) drives the cell-cycle progression of peripheral T-cell lymphoma."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "PI3K-AKT signaling (AKT already mapped) inactivates FOXO, supporting the survival of the malignant T cells of peripheral T-cell lymphoma."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the survival and Wnt/NF-κB signaling of peripheral T-cell lymphoma."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation restrains apoptosis in peripheral T-cell lymphoma."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family (LCK/FYN) kinase signaling downstream of the T-cell receptor supports the survival of the malignant T cells of peripheral T-cell lymphoma."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the inflammatory microenvironment of peripheral T-cell lymphoma."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival and chemoresistance of peripheral T-cell lymphoma cells."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of peripheral T-cell lymphoma."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-family chemokine signaling participates in the trafficking and microenvironment of peripheral T-cell lymphoma."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic dysregulation (alongside TET2/DNMT3A/IDH2 mutations) of peripheral T-cell lymphoma."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the tumor-microenvironment and lymphoid interactions of peripheral T-cell lymphoma."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment of peripheral T-cell lymphoma."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of peripheral T-cell lymphoma."
  - target: 01-human/03-molecular/lmp1
    relation: connects-to
    note: "EBV-driven subtypes: extranodal NK/T-cell lymphoma and EBV-positive nodal T-cell lymphomas depend on Epstein-Barr virus, whose oncoprotein LMP1 mimics CD40 to activate NF-kB (already mapped), and EBV+ B-blasts also populate angioimmunoblastic PTCL."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "TFH biology: angioimmunoblastic PTCL arises from follicular helper T cells whose physiological role is MHC class II-restricted help to B cells, and this retained programme drives the polyclonal B-cell expansion and hypergammaglobulinaemia typical of the disease."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Chemotherapy execution: CHOP-based anthracycline chemotherapy, the standard PTCL regimen, kills lymphoma cells through caspase-3-mediated apoptosis, and resistance to this executioner pathway contributes to the poor outcomes that characterise most peripheral T-cell lymphomas."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Hypergammaglobulinaemia: angioimmunoblastic PTCL, arising from follicular helper T cells (MHC class II already mapped), drives a polyclonal B-cell expansion that produces hypergammaglobulinaemia and the autoantibodies behind its autoimmune features."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Autoimmune cytopenias: angioimmunoblastic PTCL commonly causes autoimmune haemolytic anaemia and other cytopenias through its dysregulated B-cell help (immunoglobulin G already mapped), lowering haemoglobin at presentation."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Tumour lysis: the bulky, aggressive peripheral T-cell lymphomas can develop tumour-lysis syndrome on treatment, releasing purines that xanthine oxidase converts to uric acid, managed with allopurinol or rasburicase."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Anthracycline cardiotoxicity: the CHOP/CHOEP chemotherapy for peripheral T-cell lymphoma includes cardiotoxic doxorubicin, and troponin elevation helps detect the myocardial injury that limits the cumulative anthracycline dose."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Tumour-lysis acidosis: the rapid lysis of bulky peripheral T-cell lymphoma by chemotherapy releases acids that, with lactate, produce the metabolic acidosis of tumour-lysis syndrome (urate already mapped), part of its acute metabolic risk."
  - target: 01-human/03-molecular/secretory-iga
    relation: connects-to
    note: "Immune dysregulation: angioimmunoblastic and other peripheral T-cell lymphomas dysregulate humoral immunity, and hypogammaglobulinaemia depleting secretory IgA (immunoglobulin G already mapped) impairs mucosal defence, contributing to the infections that complicate them."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune dysregulation: IL-13 reflects the type-2 cytokine skewing of angioimmunoblastic T-cell lymphoma, the follicular-helper-T-cell (already mapped) programme driving the polyclonal immune dysregulation and rash of this peripheral T-cell lymphoma."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Th2 cytokine milieu: IL-4, with IL-13 (already mapped), drives the type-2 immune dysregulation and eosinophilia of angioimmunoblastic and other peripheral T-cell lymphomas, part of their characteristic reactive immune microenvironment."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Tumour vasculature: nitric oxide with VEGF (already mapped) regulates the prominent vascular proliferation of angioimmunoblastic T-cell lymphoma, part of the rich high-endothelial-venule vasculature of this peripheral T-cell lymphoma."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Eosinophilia: IL-5, with the Th2 skewing (IL-4 and IL-13 already mapped), drives the blood and tissue eosinophilia that characterises angioimmunoblastic and other peripheral T-cell lymphomas."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 dysregulation: the Th2-driven (IL-4 and IL-13 already mapped) polyclonal hypergammaglobulinaemia and raised IgE reflect the immune dysregulation of angioimmunoblastic T-cell lymphoma."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Tumour-lysis hyperkalaemia: the bulky, aggressive peripheral T-cell lymphoma treated with chemotherapy can release potassium in tumour-lysis syndrome (xanthine oxidase and calcium already mapped), a metabolic emergency."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Metabolic microenvironment: leptin from the marrow and stromal adipose tissue signals within the metabolic microenvironment of peripheral T-cell lymphoma."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Adipokine microenvironment: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic microenvironment of peripheral T-cell lymphoma."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the metabolic microenvironment of peripheral T-cell lymphoma."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate antitumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment relevant to the immunotherapy of peripheral T-cell lymphoma."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of peripheral T-cell lymphoma."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 arm of the inflammatory microenvironment of peripheral T-cell lymphoma."
  - target: 01-human/03-molecular/il-31
    relation: connects-to
    note: "Pruritus cytokine: IL-31, produced by the malignant T cells, mediates the severe pruritus that is a characteristic paraneoplastic symptom of peripheral (and cutaneous) T-cell lymphoma."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Eosinophil/mast infiltrate: histamine, from the mast cells and the eosinophil-rich (IL-5 already mapped) polymorphous infiltrate, is part of the reactive microenvironment of peripheral T-cell lymphoma (especially AITL)."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast-cell infiltrate: the mast cells (the histamine already mapped source) populate the polymorphous reactive infiltrate of peripheral T-cell lymphoma."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Type-2 alarmin: TSLP, an epithelial/stromal alarmin, contributes to the type-2 (IL-4, IL-5, IL-13 and IL-31 already mapped) skewing of the polymorphous reactive microenvironment of peripheral T-cell lymphoma (especially AITL)."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Type-2 remodelling: periostin, downstream of the type-2 (IL-4 and IL-13 already mapped) cytokines, is part of the type-2 stromal-remodelling dimension of the reactive microenvironment of peripheral T-cell lymphoma."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a provide the innate chemotactic arm within the polymorphous reactive infiltrate of peripheral T-cell lymphoma."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Central complement: the complement C3, upstream of the C5 (already mapped), is the pivot of the complement activation within the polymorphous reactive infiltrate of peripheral T-cell lymphoma."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) links the complement to the myeloid inflammation of the peripheral-T-cell-lymphoma microenvironment."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement evasion: the peripheral-T-cell-lymphoma cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), tempering the complement attack in the reactive microenvironment."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Lymphomagenesis kinin: bradykinin, released from the kallikrein–kinin system activated by the protease-rich PTCL microenvironment, amplifies tumour vasodilation and the vascular permeability that characterises the reactive angioedema variants of this lymphoma."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical complement brake: C1-esterase inhibitor modulates the classical complement pathway (C3, C5 and C5aR1 already mapped) activated on the polymorphous reactive infiltrate and tumour surface of peripheral T-cell lymphoma."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Chemotherapy anaemia: erythropoietin corrects the cytopenias of CHOP-based chemotherapy used in peripheral T-cell lymphoma, and its receptor on lymphoma T cells raises the question of a potential direct tumour-trophic effect."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian immune surveillance: melatonin modulates NK cell (already mapped) and CD8 T-cell activity, with circadian disruption—common in lymphoma patients—impairing immune control of the peripheral T-cell lymphoma clone."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Lymphocyte activation: prolactin, via JAK2 (already mapped) signalling, promotes T-cell and B-cell proliferation within the reactive infiltrate of peripheral T-cell lymphoma; hyperprolactinaemia has been associated with lymphoma risk in autoimmune contexts."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Neuroendocrine immune modulation: oxytocin modulates the NK cell (already mapped) and T-cell activity restraining the peripheral T-cell lymphoma clone, with psychosocial stress—which suppresses oxytocin—being an immunosuppressive co-factor."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "PTCL androgen axis: testosterone via androgen receptor on T cells (already mapped) modulates Th1/Th17 (already mapped) differentiation and cytotoxic T-cell function, with androgen-driven immunosuppression contributing to the immune evasion of peripheral T-cell lymphoma."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "PTCL serotonin: serotonin via 5-HT receptors on T cells (already mapped) and NK cells (already mapped) modulates the cytotoxic immune response against the PTCL clone, with platelet (already mapped)-derived serotonin shaping the tumour microenvironment."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "PTCL vasopressin: vasopressin via V1aR on T cells (already mapped) and endothelial cells (nitric oxide already mapped) modulates lymphocyte trafficking, vascular tone and the haemophagocytic syndrome (HLH) complicating aggressive peripheral T-cell lymphoma."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "PTCL selenium: selenium-dependent glutathione peroxidase (GPX) quenches reactive-oxygen-species driving NF-κB (already mapped)-mediated genomic instability and survival signalling in the malignant T cells of peripheral T-cell lymphoma."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "PTCL iodine: iodine-dependent thyroid hormones modulate T-cell (already mapped) differentiation and NK-cell (already mapped) cytotoxic activity within the PTCL tumour microenvironment, with hypothyroidism blunting anti-tumour immune surveillance of peripheral T-cell lymphoma."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "PTCL sodium: sodium-driven Th17 polarisation via osmotic sodium sensing in T cells (already mapped) amplifies the inflammatory cytokine (NF-κB already mapped) milieu of peripheral T-cell lymphoma, with high-salt microenvironments promoting tumour-promoting T-helper skewing."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "PTCL magnesium: magnesium, as mTOR (already mapped) kinase cofactor in malignant T cells and macrophages (already mapped), restrains tumour proliferation; magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of peripheral T-cell lymphoma."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "PTCL copper: copper, as lysyl oxidase cofactor in endothelial cells (already mapped) and macrophages (already mapped), drives tumour angiogenesis; copper deficiency amplifies NF-κB (already mapped) and VEGF (already mapped) angiogenic cascade of peripheral T-cell lymphoma."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "PTCL zinc: zinc, as co-factor of immune-regulatory metalloproteinases in macrophages (already mapped) and NK cells (already mapped), supports anti-tumour cytotoxicity; zinc deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of PTCL."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "PTCL phosphorus: phosphorus-dependent ATP in macrophages (already mapped) and NK cells (already mapped) sustains anti-tumour immune surveillance; phosphorus deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of peripheral T-cell lymphoma."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "PTCL chloride: chloride channels in macrophages (already mapped) and endothelial cells (already mapped) regulate tumour-stromal homeostasis; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) angiogenic cascade in PTCL."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "PTCL sulfur: sulfur-containing glutathione in macrophages (already mapped) and NK cells (already mapped) limits oxidative stress in the tumour microenvironment; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of peripheral T-cell lymphoma."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "PTCL carbon: carbon as backbone of NF-κB (already mapped) and BCL-2 proteins in T-lymphoma cells and macrophages (already mapped) sustains tumour survival; carbon depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of peripheral T-cell lymphoma."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "PTCL hydrogen: hydrogen, via redox homeostasis in macrophages (already mapped) and NK cells (already mapped), supports anti-tumour effector function; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) oxidative cascade of PTCL."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "PTCL nitrogen: nitrogen in amino-acid scaffold of TCR signalling proteins and NF-κB (already mapped) in T-lymphoma cells sustains oncogenic signalling; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of peripheral T-cell lymphoma."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "PTCL oxygen: oxygen, via mitochondrial respiration in T-lymphoma cells and macrophages (already mapped), sustains tumour-cell survival; oxygen depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) angiogenic cascade of peripheral T-cell lymphoma."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "PTCL GLP-1: GLP-1 receptor signalling in T-lymphoma cells and macrophages (already mapped) modulates metabolic and inflammatory tumour risk; GLP-1 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of PTCL."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "PTCL angiotensin-II: angiotensin-II signalling in macrophages (already mapped) and endothelial cells (already mapped) promotes tumour angiogenesis; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of peripheral T-cell lymphoma."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "PTCL wnt-beta-catenin: WNT/β-catenin on T-lymphoma cells (already mapped) and macrophages (already mapped) drives tumour invasion; wnt-beta-catenin dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of PTCL."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "PTCL rankl: RANKL from macrophages (already mapped) and T-lymphoma cells (already mapped) promotes tumour immune evasion; rankl excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of PTCL."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "PTCL fibronectin: fibronectin in fibroblasts (already mapped) and macrophages (already mapped) scaffolds T-lymphoma tumour ECM; fibronectin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of PTCL."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "PTCL notch: Notch signalling on T-lymphoma cells (already mapped) and macrophages (already mapped) regulates T-lymphoma cell fate; notch dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of PTCL."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "PTCL igf-1: IGF-1 from T-lymphoma cells (already mapped) and macrophages (already mapped) promotes T-lymphoma cell survival; igf-1 dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of PTCL."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "PTCL activin-a: activin-A from T-lymphoma cells (already mapped) and macrophages (already mapped) drives T-lymphoma fibrosis; activin-a excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of PTCL."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "PTCL cgrp: CGRP from T-lymphoma cells (already mapped) and macrophages (already mapped) modulates T-lymphoma neuroimmune tone; cgrp excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of PTCL."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "PTCL calcitonin: calcitonin from T-lymphoma cells (already mapped) and macrophages (already mapped) modulates calcium balance in T-cell lymphoma; calcitonin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of PTCL."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "PTCL substance-p: substance P from T-lymphoma cells (already mapped) and macrophages (already mapped) modulates T-lymphoma neuroimmune signalling; substance-p excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of PTCL."
---

# Peripheral T-cell Lymphoma

## Overview

**Peripheral T-cell lymphomas (PTCL)** are a heterogeneous group of mature (post-thymic) T-cell and NK-cell neoplasms arising from peripheral T/NK lymphocytes at various differentiation stages. PTCLs collectively account for **~10-15% of all non-Hodgkin lymphomas** (NHL) and are notably more aggressive and chemotherapy-resistant than B-cell lymphomas. The landmark discovery of recurrent **TET2, DNMT3A, RHOA G17V**, and **IDH2 R172K** mutations in AITL established epigenetic dysregulation as a central oncogenic mechanism in nodal T-cell lymphomas [^palomero-2014-ptcl-epigenetics]. The ECHELON-2 trial established **brentuximab vedotin + CHP** (BV+CHP) as standard first-line therapy for CD30-positive PTCL, replacing CHOP [^horwitz-2019-echelon2]. Overall prognosis remains poor for most PTCL subtypes: 5-year OS ~30-50% with current standard therapy.

**PTCL epidemiology:**
- Incidence: ~9,000 cases/year in USA; global variation (higher in Asia: ENKTL, ATLL)
- Median age at diagnosis: ~60 years; male predominance (M:F ~1.5-2:1)
- Geographic variation: ALK+ ALCL more common in young patients; ATLL endemic in HTLV-1 areas (Japan, Caribbean, West Africa); ENKTL prevalent in Asia and Latin America

## Structure

### WHO 2022 classification of mature T/NK-cell neoplasms

**Nodal PTCLs (lymph node-derived):**
- **PTCL-NOS (not otherwise specified):** Largest subtype (~25%); heterogeneous; aggressive; lacks defining genetic alterations of other subtypes; molecular subgroups: TBX21+ (Th1-like, worse prognosis) and GATA3+ (Th2-like, worse prognosis), CD30+
- **AITL / Nodal T-follicular helper lymphoma (nTFHL-AI, ~20%):** TFH immunophenotype; TET2+DNMT3A+RHOA G17V; follicular dendritic cell meshwork; EBER-negative (EBV in bystander B cells); hypergammaglobulinemia; autoimmune features
- **Nodal PTCL with TFH phenotype (nTFHL-other, ~5%):** TFH markers but AITL-like histology without full AITL criteria
- **Follicular T-cell lymphoma (FTCL, ~2%):** TFH phenotype with follicular growth pattern; RHOA G17V, TET2

**Systemic PTCLs:**
- **ALK+ ALCL (~7%):** NPM1-ALK t(2;5)(p23;q35) or variant ALK fusions; strong CD30+; TIA-1+; 5-year OS ~70-80%; best prognosis among PTCL
- **ALK- ALCL (~8%):** CD30+ without ALK rearrangement; DUSP22/IRF4 rearrangements (favorable, ~30%), TP63 rearrangements (adverse, ~8%), JAK1 mutations (~15%); 5-year OS ~40-50%
- **Breast implant-associated ALCL (BIA-ALCL):** CD30+; ALK-; in peri-implant fluid; excellent prognosis with implant removal; rare progression to systemic ALCL
- **PTCL with GATA3/TBX21:** Emerging molecular subtypes within PTCL-NOS

**Extranodal PTCLs:**
- **Extranodal NK/T-cell lymphoma (ENKTL, ~10%):** EBV-driven; nasal type; KIR3DL2+; DDX3X, KMT2D, ARID1A, TP53 mutations; SMILE protocol or l-asparaginase-based regimens; PD-L1 overexpressed via EBV LMP1; pembrolizumab activity in R/R
- **Hepatosplenic T-cell lymphoma (HSTCL, ~1%):** γδ TCR; STAT3/STAT5b mutations; isochromosome 7q; young males; iatrogenic immunosuppression (IBD on biologics); aggressive; median OS <2 years
- **Subcutaneous panniculitis-like T-cell lymphoma (SPTCL):** αβ TCR; indolent when HLH-absent
- **Mycosis fungoides/Sézary syndrome:** Cutaneous PTCL; CTCL; separate clinical considerations

**Adult T-cell leukemia/lymphoma (ATLL):**
- HTLV-1 driven; endemic Japan, Caribbean, West Africa; acute/lymphomatous/chronic/smoldering
- Tax protein → NF-κB constitutive activation; CCR4+; FOXP3+
- Mogamulizumab (anti-CCR4, FDA 2018 for CTCL; activity in ATLL); lenalidomide; allogeneic SCT

### AITL molecular architecture

AITL arises from TFH (T-follicular helper) cell progenitors through sequential mutational acquisition:

**Stage 1 — Pre-malignant HSC clone:**
TET2 and/or DNMT3A mutations in HSCs → clonal expansion; TET2-mutant HSCs differentiate toward both myeloid and lymphoid lineages → pre-malignant TFH cells carry TET2/DNMT3A mutations alongside normal cells; this stage is detectable in peripheral blood (non-T cells also carry mutations).

**Stage 2 — TFH progenitor expansion:**
RHOA G17V acquired in TFH progenitor → impairs RhoA GTPase activity (dominant-negative) → altered VAV1 signaling, PI3K activation → TFH clonal expansion; RHOA G17V is lymphoid-specific (not in myeloid compartment of same patient).

**Stage 3 — AITL:**
IDH2 R172K (not R140Q) acquired in ~20-30% → 2-HG → TET2 further inhibited → hypermethylation accelerated; FYN kinase mutations (~3%); additional co-mutations accumulate → overt lymphoma with TFH phenotype, follicular dendritic cell meshwork, abundant reactive cells (B cells, plasma cells, eosinophils, macrophages).

**AITL immunophenotype:**
CD3+, CD4+, CD10+, BCL6+, CXCR5+, ICOS+, PD-1+, CD279+ (TFH markers); CD30 variable; EBV+ bystander B cells (EBER+); follicular dendritic cell meshwork (CD21+, CD23+).

### ALK+ ALCL molecular biology

**NPM1-ALK fusion (t(2;5)):**
NPM1 N-terminus provides oligomerization → constitutive cytoplasmic ALK dimerization → trans-autophosphorylation → JAK3/STAT3, PI3K/AKT, RAS/ERK activation; ALK+ALCL: strong uniform CD30 staining; cytoplasmic ALK by IHC; hallmark "doughnut cells" (horseshoe/kidney-shaped nuclei); pediatric peak (15-30 years).

**Variant ALK fusions:**
TPM3-ALK (cytoplasmic, granular), CLTC-ALK (cytoplasmic, granular), EML4-ALK (cytoplasmic) → same downstream signaling; IHC pattern differs from NPM1-ALK (nuclear+cytoplasmic).

## Function

### Normal T-cell biology context

**TFH biology (AITL origin):**
TFH cells are CD4+ T cells that home to germinal centers via CXCR5 (follicle-homing receptor); interact with B cells via ICOS-ICOSL, CD40L-CD40, IL-21; promote B-cell somatic hypermutation and affinity maturation; BCL6 is the master TFH transcription factor; PD-1 expressed on TFH prevents premature T-cell activation. AITL neoplastic cells retain full TFH identity: CXCR5+, BCL6+, ICOS+, PD-1+, IL-21-producing.

**TCR signaling in T-cell lymphoma:**
T-cell receptor (TCR) signaling amplified in PTCL: LCK/ZAP70 → LAT → PLC-γ → DAG+IP₃ → PKC-θ+NFAT → T-cell activation; RHOA G17V interferes with VAV1-CDC42/RAC1 axis → promotes aberrant cytoskeletal organization and PI3K activation without requiring TCR stimulation; FYN mutations (gain-of-function) → hyperactive Src-family kinase → enhanced TCR-proximal signaling.

## Pathology

### Clinical presentation

**AITL:**
Generalized lymphadenopathy (>90%); B symptoms (fever, night sweats, weight loss) ~75%; hepatosplenomegaly ~70%; skin rash (maculopapular, ~50%); pleural effusion, ascites (~30%); autoimmune hemolytic anemia (Coombs+), cold agglutinins, thrombocytopenia; hypergammaglobulinemia (polyclonal IgG elevation); elevated LDH, β2-microglobulin; often misdiagnosed as autoimmune disease before biopsy.

**ALK+ ALCL:**
Young patients (median ~25 years); advanced stage (~70%); systemic symptoms; excellent prognosis; B symptoms common; extranodal involvement (bone, skin, liver, lung); mediastinal disease less common than Hodgkin lymphoma.

**PTCL-NOS:**
Aggressive presentation; generalized lymphadenopathy; extranodal involvement (~60%); advanced stage (~70%); elevated LDH; poor prognosis (5-year OS ~30-40%).

### Diagnosis and workup

**Biopsy essential:** Excisional lymph node biopsy preferred (core needle biopsy may be insufficient for architecture assessment).

**Immunophenotyping:**
- TCR flow cytometry and IHC: αβ vs γδ; pan-T markers (CD2, CD3, CD5, CD7) often aberrantly lost
- CD4/CD8 ratio; TFH markers for AITL (PD-1, CXCR5, CD10, BCL6, ICOS)
- CD30 IHC (ALCL, some PTCL-NOS): scored quantitatively for brentuximab eligibility
- ALK IHC (ALCL): nuclear+cytoplasmic = NPM1-ALK; cytoplasmic = variant fusions
- EBER ISH (EBV in bystander B cells = AITL feature; if tumor cells EBV+ = ENKTL or EBV+ DLBCL)

**Molecular:**
- TCR gene clonality (PCR/NGS): confirms clonal T-cell expansion; not subtype-specific
- NGS panel: TET2, DNMT3A, RHOA G17V, IDH2, SRSF2 (AITL pattern); TP53, SETD2, KMT2D (PTCL-NOS); STAT3/5B (HSTCL)
- ALK FISH for t(2;5) and variant fusions
- Cytogenetics: isochromosome 7q (HSTCL); DUSP22/IRF4 FISH (ALK- ALCL)

### Prognostic scoring

**PTCL-specific IPI (PIT — Prognostic Index for PTCL):** Age >60, PS ≥2, elevated LDH, bone marrow involvement → 4 adverse factors; Low (0), Low-Int (1), High-Int (2), High (3-4) risk groups; 5-year OS: 62%, 53%, 33%, 18%.

**AITL-specific:** No validated molecular prognostic score; TET2 biallelic → worse; IDH2 co-mutation → may predict enasidenib sensitivity.

### Treatment

**First-line (non-ALK+ ALCL):**
- **CHOP (cyclophosphamide, doxorubicin, vincristine, prednisone):** Historical standard; ORR ~60-75%; CR ~50%; 5-year OS ~30-40%; inadequate for most PTCL
- **CHOEP (CHOP + etoposide):** Benefit in young (<60 years) patients in Nordic retrospective data; no Phase 3 RCT confirmation; etoposide toxicity limits use in elderly
- **BV+CHP (brentuximab vedotin + cyclophosphamide, doxorubicin, prednisone) for CD30+ PTCL:**
  ECHELON-2 (Phase 3 RCT, N=452): BV+CHP vs CHOP for CD30+ PTCL; primary endpoint PFS: 48.2 vs 20.8 months (HR 0.71, p=0.011); 5-year OS: 70.1% vs 61.0% (HR 0.72); FDA approved 2018 for CD30+ PTCL; neuropathy (Grade ≥3 ~17%) main toxicity [^horwitz-2019-echelon2]
- **AITL epigenetic approach:** Azacitidine ± CHOP in clinical trials (NCT02795832); romidepsin+CHOP (ROMIDEPSIN trial)

**ALK+ ALCL:**
- BV+CHP: primary frontline regimen for CD30+ PTCL including ALK+ ALCL
- CHOP → excellent outcomes (5-year OS ~75%); BV+CHP improves upon CHOP in ECHELON-2 subgroup
- ALK inhibitors (crizotinib, alectinib): active in relapsed/refractory ALK+ ALCL; ORR ~75-85%

**Relapsed/Refractory:**
- **Brentuximab vedotin** (CD30+, single-agent R/R): ORR ~86% ALK+ ALCL, ~57% ALK- ALCL; FDA 2011 accelerated (R/R ALCL); FDA 2018 (PCNS+ PTCL)
- **Romidepsin** (HDAC inhibitor, IV): ORR ~25-38% in PTCL; FDA 2011; preferred for PTCL-NOS/AITL
- **Belinostat** (HDAC inhibitor, IV): ORR ~26% PTCL; FDA 2014 (Belingen-1 trial)
- **Pralatrexate** (antifolate, Folotyn): ORR ~29% PTCL; FDA 2009; mucositis dose-limiting
- **Mogamulizumab** (anti-CCR4): ORR ~35% in CCR4+ PTCL (ATLL, AITL); FDA approved CTCL, investigational PTCL
- **Duvelisib** (PI3K-δ/γ inhibitor): ORR ~32% R/R PTCL (PRIMO trial); FDA approved for FL
- **Pembrolizumab/nivolumab:** ORR ~15-33% in selected PTCL; **caution in AITL** (paradoxical progression reported — checkpoint inhibition may promote AITL TFH expansion)

**Consolidation allo-SCT:**
- Recommended in responding high-risk patients in first remission (CR1/PR1)
- 3-year OS post-allo-SCT ~45-60% (registry data)
- Particularly beneficial: PTCL-NOS, AITL, ALK- ALCL (especially TP63-rearranged)
- Myeloablative vs RIC depending on age/comorbidities

**ENKTL-specific:**
- L-asparaginase-containing regimens (SMILE: dexamethasone, methotrexate, ifosfamide, l-asparaginase, etoposide; AspaMetDex)
- Concurrent/sequential radiotherapy for localized nasal ENKTL
- Pembrolizumab: ORR ~46% in R/R ENKTL (EBV-driven PD-L1 upregulation)

## Connections

- `connects-to` → **[TET2](../../03-molecular/tet2/README.md)** — TET2 loss-of-function is the most common mutation in AITL (~60-80%) and a major driver in PTCL-NOS (~20%); TET2+DNMT3A+RHOA G17V is the canonical AITL triplet; TET2 mutations arise in a pre-malignant TFH HSC clone and precede RHOA G17V acquisition.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A R882H/C mutations occur in ~20-30% of AITL and ~15% PTCL-NOS, co-mutating with TET2 in the pre-malignant TFH clone; DNMT3A+TET2 co-loss → genome-wide hypermethylation; therapy-related T-cell lymphomas from DNMT3A CHIP clones have been reported.
- `connects-to` → **[ALK](../../03-molecular/alk/README.md)** — NPM1-ALK t(2;5)(p23;q35) defines ALK+ ALCL (~7% of PTCL); ALK fusion drives JAK-STAT3 constitutive activation; crizotinib, alectinib, brigatinib active in ALK+ ALCL; ALK+ ALCL is the most favorable PTCL subtype (5-year OS ~70-80% with A+CHP).
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — PD-1 is a TFH cell surface marker expressed in AITL tumor cells; anti-PD-1 (pembrolizumab, nivolumab) has activity in relapsed PTCL (ORR ~15-30%) but risk of paradoxical lymphoma acceleration in AITL; PD-L1 overexpressed on ALK- ALCL via DUSP22/IRF4 rearrangements.
- `connects-to` → **[IDH2](../../03-molecular/idh2/README.md)** — IDH2 R172K (distinct from MDS R140Q) occurs in ~20-30% of AITL/nTFHL; IDH2 → 2-HG → TET2 + KDM competitive inhibition → epigenetic reprogramming; enasidenib (IDH2 inhibitor, approved AML) explored in IDH2-mutant AITL; IDH2+TET2 co-mutation drives extreme hypermethylation.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — constitutive STAT3 activation in ALK+ ALCL (NPM1-ALK → JAK3 → STAT3), ALK- ALCL (STAT3 activating mutations ~15%), and HSTCL (STAT3/STAT5b mutations); STAT3 drives CD30, BCL-2, MCL-1, and VEGF → lymphoma survival; ruxolitinib (JAK1/2→STAT3) has activity in PTCL trials.
- `connects-to` → **[CD30](../../03-molecular/cd30/README.md)** — CD30 (TNFRSF8) is the primary PTCL therapeutic target; brentuximab vedotin (anti-CD30 ADC) FDA-approved for ALCL and CD30+ PTCL; ECHELON-2: BV+CHP vs CHOP → PFS HR 0.71; CD30 in ALCL (~100%), PTCL-NOS (~30-50%); CD30 signals via TRAF1/2/3 → NF-κB → lymphoma survival.
- `connects-to` → **[Primary CNS Lymphoma](../pcnsl/README.md)** — Peripheral T-cell lymphoma and primary CNS lymphoma are aggressive non-Hodgkin lymphomas of opposite lineage: PTCL is a heterogeneous T-cell group (TET2/RHOA/STAT3-driven), PCNSL a CNS-confined B-cell (DLBCL) tumor driven by MYD88 — lineage and site reshape lymphoma biology.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Angioimmunoblastic T-cell lymphoma, a major PTCL subtype, arises from the follicular helper T cell (TFH): tumor cells keep TFH markers (PD-1, CXCL13, ICOS, BCL6) and recruit a reactive B-cell/EBV background, while TET2/DNMT3A/RHOA-G17V mutations drive the malignancy.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — The skin is a defining PTCL site: primary cutaneous CD30+ T-cell lymphomas (cutaneous ALCL, lymphomatoid papulosis) and the mycosis fungoides/Sézary spectrum home to skin, often indolent — contrasting with the aggressive nodal PTCLs like AITL and systemic ALCL.
- `connects-to` → **[Diffuse Large B-Cell Lymphoma](../dlbcl/README.md)** — Peripheral T-cell and diffuse large B-cell lymphoma are the aggressive non-Hodgkin lymphomas of the two lineages: PTCL arises from mature T cells, is rarer, and has a worse prognosis than DLBCL, which is CD20+ and responds to rituximab-based R-CHOP that PTCL cannot use.
- `connects-to` → **[Hodgkin Lymphoma](../hodgkin-lymphoma/README.md)** — PTCL and Hodgkin lymphoma intersect at CD30: anaplastic large cell lymphoma, a PTCL subtype, strongly expresses CD30 like Hodgkin's Reed-Sternberg cells, so the anti-CD30 drug brentuximab vedotin treats both—and the two can be hard to distinguish histologically.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Some peripheral T-cell lymphomas derive from regulatory or follicular-helper T cells: adult T-cell leukemia often has a Treg-like FOXP3+ phenotype and angioimmunoblastic PTCL arises from follicular-helper T cells—so the normal T-cell subset shapes the lymphoma.
- `connects-to` → **[Epstein-Barr Virus](../../../02-pathogen/01-viruses/epstein-barr-virus/README.md)** — Several peripheral T-cell lymphomas are EBV-driven: extranodal NK/T-cell lymphoma is defined by EBV infection, and angioimmunoblastic T-cell lymphoma harbors EBV-positive B-immunoblasts—so the virus shapes diagnosis and biology across this T-cell lymphoma group.
- `connects-to` → **[Mantle Cell Lymphoma](../mantle-cell-lymphoma/README.md)** — PTCL and mantle cell lymphoma are both aggressive non-Hodgkin lymphomas but of opposite lineage: PTCL arises from mature T cells, while MCL is a B-cell tumor with t(11;14) cyclin D1—immunophenotyping the T- versus B-cell origin guides therapy.
- `connects-to` → **[Follicular Lymphoma](../follicular-lymphoma/README.md)** — PTCL and follicular lymphoma sit at opposite ends of lineage and tempo: follicular lymphoma is an indolent germinal-center B-cell tumor, while most PTCLs are aggressive mature T-cell cancers—the T-versus-B distinction fundamentally separates their biology and treatment.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — PTCL includes NK/T-cell lymphomas: peripheral T-cell lymphomas span many entities, and the related extranodal NK/T-cell lymphoma is an aggressive, EBV-driven, often nasal tumor—so the T/NK lineage spawns a heterogeneous, generally poor-prognosis lymphoma group.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — PTCL is a lymphoma of the lymphatic system's T cells: unlike the common B-cell lymphomas, it arises from mature T cells in lymph nodes and spreads through the lymphatic network, often with systemic B symptoms and a worse outcome than B-cell lymphomas.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Bone marrow involvement is common and ominous in PTCL: these aggressive T-cell lymphomas frequently infiltrate the marrow, causing cytopenias and upstaging disease—so marrow biopsy is part of staging and marrow disease worsens an already poor prognosis.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — PTCL spans many T-cell subsets, including cytotoxic-T-cell-derived types: extranodal NK/T-cell and hepatosplenic lymphomas arise from cytotoxic lineage cells, so unlike B-cell lymphomas, PTCL's diversity reflects the many normal T-cell populations it can mimic.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — Some PTCLs home to the spleen and liver: hepatosplenic T-cell lymphoma infiltrates these organs (often in immunosuppressed patients) causing cytopenias without nodal masses, so an aggressive T-cell lymphoma can present as hepatosplenomegaly rather than lymphadenopathy.
- `connects-to` → **[Immune System](../immune-system/README.md)** — PTCL both arises from and dysregulates the immune system: angioimmunoblastic T-cell lymphoma in particular causes autoimmune features and immunodeficiency as the malignant helper T cells distort immune regulation—so infection and autoimmunity complicate the disease.
- `connects-to` → **[Thymus](../../06-organ/thymus/README.md)** — T-cell lymphomas trace back to the thymus-educated T lineage: PTCLs are malignancies of mature post-thymic T cells, so unlike T-ALL they arise after thymic development—their subtype reflecting which mature T-cell type (helper, cytotoxic, NK-like) transformed.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Angioimmunoblastic PTCL springs from germinal-center helper cells: it arises from T-follicular-helper cells that normally aid B cells in germinal centers, which is why this subtype shows expanded follicular dendritic networks and reactive B-cell proliferation.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Angioimmunoblastic T-cell lymphoma expands follicular dendritic cells: a hallmark is a proliferating meshwork of follicular dendritic cells and high endothelial venules around the tumor T cells, giving the node its distinctive polymorphous, vascular appearance.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Angioimmunoblastic PTCL builds a forest of new vessels via VEGF: this T-cell lymphoma drives prominent arborizing blood vessels that are a diagnostic hallmark, fed by VEGF from the tumor and its inflammatory backdrop.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — PTCL hides malignant T cells in a crowd of macrophages: especially in AITL, a polymorphous infiltrate of macrophages, eosinophils, and plasma cells can outnumber the cancer cells, making the diagnosis easy to miss.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — PTCL's systemic symptoms run on IL-6: tumor and bystander cells pour out IL-6 and other cytokines that cause the fevers, weight loss, rash, and high antibody levels typical of angioimmunoblastic lymphoma.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Some T-cell lymphomas raise blood calcium dangerously: adult T-cell leukemia/lymphoma from HTLV-1 secretes factors like PTHrP that pull calcium from bone, so hypercalcemia is a hallmark emergency of this PTCL subtype.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — T-cell lymphoma can arise in the gut itself: enteropathy-associated T-cell lymphoma grows in the intestine, often on a background of celiac disease, so unexplained bowel symptoms or perforation in celiac patients raise the alarm.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — PTCL survives on constitutive NF-kB signaling: the malignant T cells keep this survival switch active downstream of T-cell-receptor and cytokine inputs, sustaining proliferation and making the pathway a target in these aggressive lymphomas.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Peripheral T-cell lymphoma drains iron and blood: marrow involvement and chronic inflammation suppress red-cell production and lock iron away, so anemia commonly accompanies these aggressive lymphomas.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Some T-cell lymphomas home to the liver: hepatosplenic T-cell lymphoma infiltrates the liver and spleen rather than forming nodal masses, enlarging both organs in this rare, aggressive subtype.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Angioimmunoblastic PTCL sprouts blood vessels: it is marked by a striking proliferation of arborizing high-endothelial venules, so its endothelial cells multiply alongside the malignant T cells.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photons stage and track PTCL: these lymphomas are avid for FDG, so PET-CT lights up nodal and extranodal disease for staging and gauges whether the aggressive tumor is melting away under chemotherapy.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — One PTCL is born in the gut: enteropathy-associated T-cell lymphoma arises from the intraepithelial T cells of the small intestine in long-standing celiac disease, presenting with bowel perforation or obstruction in a malnourished patient.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Angioimmunoblastic PTCL turns the immune system on its own red cells: the dysregulated helper-T-cell tumor drives autoantibodies that coat erythrocytes, producing a Coombs-positive hemolytic anemia alongside the lymphoma.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — AITL floods the blood with antibody: its malignant follicular-helper T cells whip up a polyclonal plasma-cell response, producing the hypergammaglobulinemia and autoantibodies that give angioimmunoblastic lymphoma its autoimmune-like face.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — A T-cell cancer that breeds rogue B cells: the helper-T tumor of AITL fosters EBV-driven B-cell blasts in its inflamed milieu, expansions that can themselves transform into a secondary diffuse large B-cell lymphoma.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — The CHOP backbone bites the nerves: vincristine, part of the standard PTCL chemotherapy, poisons the microtubule transport of peripheral neurons, leaving a dose-limiting numbness, tingling, and weakness.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies name and target PTCL: a CD3, CD30, and ALK stain panel sorts the subtypes on biopsy, and the CD30-positive ones — anaplastic large-cell lymphoma especially — are hit by the anti-CD30 antibody-drug conjugate brentuximab vedotin.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — The CHOEP regimen empties the marrow: the cyclophosphamide, etoposide, and anthracycline given for PTCL are heavily myelosuppressive, so neutrophil counts crater between cycles and growth-factor support and infection vigilance are routine.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Bulky, fast PTCL threatens the kidney: starting chemotherapy can burst the tumor into tumor lysis syndrome, flooding the blood with potassium, phosphate, and urate that crystallize in and injure the kidney unless hydration and rasburicase pre-empt it.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — The CHOP backbone strains the heart: the doxorubicin in standard PTCL chemotherapy is cumulatively cardiotoxic to cardiomyocytes, so cardiac function is checked before and during the anthracycline-based regimens these aggressive lymphomas require.
- `connects-to` → **[JAK2](../../03-molecular/jak2/README.md)** — Many PTCLs run on JAK-STAT: recurrent activation of the JAK2-STAT3 pathway drives several subtypes, especially the NK/T-cell and ALK-negative anaplastic forms, making JAK inhibition an actively studied targeted approach.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Cure can cost fertility: the multi-agent and high-dose chemotherapy, sometimes with transplant, used against these aggressive lymphomas damages the gonads, so fertility preservation is discussed before treating younger patients.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — One subtype is born in the damaged gut: enteropathy-associated T-cell lymphoma arises from the intraepithelial T cells of the small-bowel lining injured by celiac disease, turning chronic mucosal inflammation into an aggressive intestinal lymphoma.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Survival signaling runs through a familiar hub: PI3K-AKT-mTOR activation supports the malignant T cells across PTCL subtypes, so mTOR inhibitors are tested in a group of lymphomas that respond poorly to standard chemotherapy.
- `connects-to` → **[Myelodysplastic Syndromes](../mds/README.md)** — The cure can sow a second cancer: the intensive chemotherapy and autologous transplant used against PTCL damage the marrow, raising the risk of therapy-related myelodysplastic syndromes years later.
- `connects-to` → **[Cytokine Storm](../cytokine-storm/README.md)** — Aggressive T-cell lymphoma can ignite the immune system: PTCL is a leading driver of secondary hemophagocytic lymphohistiocytosis, a cytokine storm of runaway macrophage activation that can be the lethal presenting picture.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Disease and treatment both gut immunity: the T-cell malignancy itself plus intensive chemotherapy leave PTCL patients profoundly immunosuppressed and prone to opportunistic infection and sepsis.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Inflammasome activation feeds the cytokine flood: NLRP3-driven IL-1β release contributes to the hyperinflammatory, HLH-like state that can complicate aggressive peripheral T-cell lymphomas.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — An aggressive lymphoma is a prothrombotic state: bulky nodal disease, the inflammatory cytokine milieu and indwelling catheters during therapy combine to raise venous thromboembolism risk in PTCL patients.
- `connects-to` → **[Pneumocystis jirovecii](../../../02-pathogen/03-fungi/pneumocystis-jirovecii/README.md)** — T-cell loss is exactly its opening: PTCL depletes the CD4 T-cells that hold Pneumocystis in check, and the intensive chemotherapy compounds it, so PJP prophylaxis is standard during treatment.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Marrow involvement and cytokines starve the red cells: PTCL infiltrating the bone marrow alongside its high IL-6 drive raises hepcidin and suppresses erythropoiesis, contributing an anemia-of-chronic-disease component to the cytopenias.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Its intensive chemo and T-cell defect open the lung to mold: CHOP-based therapy plus the profound T-cell immunodeficiency of PTCL cause deep neutropenia, letting inhaled Aspergillus invade as pulmonary aspergillosis.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Its anthracycline backbone can weaken the heart: doxorubicin in the CHOP/CHOEP regimens for PTCL is dose-dependently cardiotoxic, risking a cardiomyopathy and heart failure during and after treatment.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — An aggressive lymphoma with poor odds weighs on mood: PTCL's rapid course, relapsing pattern and grueling therapy impose a heavy psychological burden that contributes to depression and anxiety.
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — Chemotherapy reawakens shingles: the CHOP/CHOEP and salvage regimens for PTCL deplete T-cell immunity, allowing latent varicella-zoster to reactivate, so antiviral prophylaxis is standard.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Bulky disease and chemo strain the kidneys: rapid tumour lysis from treating a high-burden PTCL, plus nephrotoxic agents, can cause acute kidney injury that may settle into chronic impairment.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — An aggressive, relapsing lymphoma breeds worry: the poor prognosis, high relapse rate and intensive therapy of PTCL foster chronic health anxiety alongside the depression it brings.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — One subtype erupts in the bowel: enteropathy-associated T-cell lymphoma arises in the small intestine of coeliac disease, causing pain, obstruction, bleeding and a high risk of perforation.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — T-cell lymphomas often involve the skin: PTCL subtypes infiltrate the skin with plaques, nodules and ulcers, and angioimmunoblastic disease causes a widespread paraneoplastic rash.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It reaches the nervous system: PTCL can involve the central nervous system and meninges, and its chemotherapy adds peripheral neuropathy, complicating its aggressive course.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — One subtype floods the blood with calcium: adult T-cell leukaemia/lymphoma, an HTLV-1-driven PTCL, classically causes severe paraneoplastic hypercalcaemia from osteoclast-activating signals.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It crowds and exposes the chest: mediastinal and pulmonary involvement and pleural effusions occur, and the profound immunosuppression invites opportunistic pneumonia.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its chemotherapy can scar the heart: the anthracycline in CHOP-based regimens for PTCL carries a dose-dependent cardiotoxicity risk.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It can dissolve bone: adult T-cell leukaemia/lymphoma classically causes severe hypercalcaemia with lytic bone lesions, and marrow involvement causes cytopenias.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Treatment and metabolism reach the kidney: tumour lysis syndrome at the start of therapy and ATLL hypercalcaemia threaten acute kidney injury.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Targeted antibodies refine its treatment: brentuximab vedotin against CD30 and HDAC inhibitors supplement CHOP-based chemotherapy in peripheral T-cell lymphoma.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — CHOEP then transplant: peripheral T-cell lymphoma is treated with anthracycline regimens like CHOEP followed by autologous stem-cell transplant, yet responds far worse than B-cell lymphomas with frequent early relapse.
- `connects-to` → **[Burkitt Lymphoma](../burkitt-lymphoma/README.md)** — A B-lineage aggressive counterpart: Burkitt and PTCL are both aggressive non-Hodgkin lymphomas, but Burkitt is a MYC-driven B-cell tumour cured by intensive chemo, whereas PTCL is a chemo-resistant T-cell malignancy — lineage dictates prognosis.
- `connects-to` → **[CAR-T](../../../03-medicine/01-modern/13-cancer/car-t/README.md)** — Fratricide blocks T-cell CAR-T: the CAR-T therapy that transformed B-cell lymphoma is hard to apply to PTCL because engineered T-cells share target antigens with the tumour and kill each other, driving gene-edited and NK-cell designs.
- `connects-to` → **[AML](../aml/README.md)** — Shared epigenetic mutations: angioimmunoblastic T-cell lymphoma carries TET2, DNMT3A and IDH2 mutations like acute myeloid leukaemia and clonal haematopoiesis, sometimes arising from the same mutant haematopoietic precursor.
- `connects-to` → **[NSCLC](../nsclc/README.md)** — A shared ALK fusion: ALK-positive anaplastic large-cell lymphoma and ALK-rearranged non-small-cell lung cancer both depend on a constitutively active ALK kinase, so ALK inhibitors like crizotinib treat both across blood and lung.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Immunotherapy with a caveat: some peripheral T-cell lymphomas (especially EBV-driven or PD-L1-high subtypes) respond to PD-1 inhibitors, but checkpoint blockade can paradoxically accelerate certain T-cell lymphomas, so it is used cautiously.
- `connects-to` → **[CMML](../cmml/README.md)** — Shared clonal-haematopoiesis mutations: angioimmunoblastic T-cell lymphoma shares TET2 and DNMT3A mutations with CMML and other myeloid neoplasms, a common clonal-haematopoiesis origin—patients can develop both.
- `connects-to` → **[IDH-mutant Glioma](../idh-mutant-glioma/README.md)** — A shared IDH2 oncometabolite: angioimmunoblastic PTCL carries IDH2 mutations like those of IDH-mutant glioma and AML, producing 2-hydroxyglutarate—an unexpected metabolic link to a brain tumour.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Hepatosplenic infiltration: PTCL, especially the hepatosplenic subtype, infiltrates the sinusoids of the hepatic lobule and the spleen, causing cytopenias and hepatosplenomegaly.
- `connects-to` → **[Sjögren's Syndrome](../sjogrens-syndrome/README.md)** — An autoimmune masquerade: angioimmunoblastic T-cell lymphoma presents with rash, polyclonal hypergammaglobulinaemia, autoimmune cytopenias and sicca that mimic Sjogren's, while chronic autoimmunity itself raises lymphoma risk.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Immunosuppression and T-cell clones: rheumatoid arthritis and its therapies raise lymphoma risk, and RA is classically associated with T-cell large granular lymphocytic leukaemia, a clonal T-cell disorder on the PTCL spectrum.
- `connects-to` → **[HIV/AIDS](../hiv-aids/README.md)** — Immunodeficiency-driven lymphoma: HIV-associated immune dysregulation and EBV reactivation raise the risk of aggressive non-Hodgkin lymphomas, including peripheral T-cell lymphomas alongside the more common B-cell types.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Epigenetic dysregulation: EZH2 and the broader epigenetic machinery (with TET2, DNMT3A and IDH2) are deranged in angioimmunoblastic and other peripheral T-cell lymphomas, a rationale for epigenetic therapy.
- `connects-to` → **[IFN-γ](../../03-molecular/ifn-gamma/README.md)** — Inflammatory microenvironment: an IFN-γ-rich, cytotoxic-skewed microenvironment characterises many peripheral T-cell lymphomas, driving the B symptoms and immune dysregulation of the disease.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell growth axis: IL-2 and its receptor subunit CD25 drive the proliferation of malignant T cells in peripheral T-cell lymphoma, and CD25 is exploited by targeted antibody-drug conjugates.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Inflammatory milieu: TNF-α within the peripheral T-cell lymphoma microenvironment drives the B symptoms and supports the malignant T-cell clone.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Cell-cycle drive: cyclin D-CDK4/6 activity propels malignant T cells through the G1 checkpoint in peripheral T-cell lymphoma, fuelling its proliferation.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Tumour hypoxia: HIF-1α stabilised in the hypoxic nodal microenvironment supports the metabolism and angiogenesis of peripheral T-cell lymphoma.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Recurrent JAK1/JAK2 and STAT3 mutations drive constitutive JAK-STAT signaling in several PTCL subtypes, the rationale for testing ruxolitinib and other JAK inhibitors in this lymphoma where conventional chemotherapy often fails.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — TGF-β in the PTCL microenvironment dampens cytotoxic responses and shapes the reactive infiltrate—especially in angioimmunoblastic T-cell lymphoma, where the malignant TFH cells are a minority among an inflamed bystander background.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — CCL2 secreted within PTCL nodes recruits monocytes and macrophages into the prominent inflammatory background that characterizes angioimmunoblastic and other peripheral T-cell lymphomas, where reactive cells outnumber tumor cells.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — Peripheral T-cell lymphomas frequently depend on PI3K signaling, the rationale for the dual PI3K-δ/γ inhibitor duvelisib, which targets both the malignant T cells and the supportive tumor-microenvironment cells.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — Anti-apoptotic BCL-2-family proteins help PTCL cells evade the death program, underlying the chemoresistance of these aggressive lymphomas and motivating BH3-mimetic combinations under study.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — A subset of peripheral T-cell lymphomas derive from cytotoxic T or NK cells and express perforin and granzyme, the cytotoxic-molecule phenotype that defines extranodal NK/T-cell and hepatosplenic lymphomas with their aggressive course.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — MYC deregulation drives the aggressive behavior and large-cell transformation of peripheral T-cell lymphomas, cooperating with the epigenetic TET2/DNMT3A/IDH2 lesions already mapped to accelerate disease.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — AITL, the commonest Tfh-derived PTCL, shows prominent arborizing high-endothelial venules, and PDGF angiogenic signaling helps build this vascular, follicular-dendritic-cell-rich microenvironment alongside the VEGF already mapped.
- `connects-to` → **[Interleukin-10](../../03-molecular/il-10/README.md)** — The Tfh tumor and microenvironment of angioimmunoblastic T-cell lymphoma secrete immunosuppressive IL-10, contributing to the autoimmunity, hypergammaglobulinemia and infection susceptibility characteristic of the disease.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — The NPM-ALK fusion of ALK-positive anaplastic large cell lymphoma (ALK mapped) signals through the MAPK-ERK cascade to drive proliferation of this PTCL subtype.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — ALK also engages PI3K-AKT (PIK3CA and mTOR already mapped), a survival pathway downstream of the fusion kinase in anaplastic large cell lymphoma.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — Cyclin-D1 (mapped) and CDK4/6 release E2F1 to drive the cell-cycle progression of peripheral T-cell lymphoma.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — Dysregulation of the RB1-E2F checkpoint (cyclin-D1 and E2F1 already mapped) contributes to the proliferation of peripheral T-cell lymphoma.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — RAS-ERK signaling (ERK1/2 already mapped) downstream of T-cell-receptor and cytokine inputs provides a proliferative drive in peripheral T-cell lymphoma.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR-MyD88-NF-κB signaling (NF-κB already mapped) contributes to the constitutive NF-κB activation characteristic of several peripheral T-cell lymphoma subtypes.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 modulates T-cell-lymphoma survival and the immune microenvironment of peripheral T-cell lymphoma.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β mapped) shapes the immunosuppressive microenvironment, prominent in the Tfh-derived angioimmunoblastic subtype of peripheral T-cell lymphoma.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — Loss of PTEN restraint on PI3K-AKT-mTOR signaling (AKT, PIK3CA and mTOR mapped) supports proliferation and survival in peripheral T-cell lymphoma.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the antitumor immune response and the interferon-associated subtypes of peripheral T-cell lymphoma.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING modulates the inflammatory microenvironment of peripheral T-cell lymphoma.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6-cyclin-D activity (cyclin-D1 and RB1 already mapped) drives the cell-cycle progression of peripheral T-cell lymphoma.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — PI3K-AKT signaling (AKT already mapped) inactivates FOXO, supporting the survival of the malignant T cells of peripheral T-cell lymphoma.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the survival and Wnt/NF-κB signaling of peripheral T-cell lymphoma.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation restrains apoptosis in peripheral T-cell lymphoma.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family (LCK/FYN) kinase signaling downstream of the T-cell receptor supports the survival of the malignant T cells of peripheral T-cell lymphoma.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the inflammatory microenvironment of peripheral T-cell lymphoma.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival and chemoresistance of peripheral T-cell lymphoma cells.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of peripheral T-cell lymphoma.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-family chemokine signaling participates in the trafficking and microenvironment of peripheral T-cell lymphoma.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic dysregulation (alongside TET2/DNMT3A/IDH2 mutations) of peripheral T-cell lymphoma.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the tumor-microenvironment and lymphoid interactions of peripheral T-cell lymphoma.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment of peripheral T-cell lymphoma.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of peripheral T-cell lymphoma.
- `connects-to` → **[LMP1](../../03-molecular/lmp1/README.md)** — EBV-driven subtypes: extranodal NK/T-cell lymphoma and EBV-positive nodal T-cell lymphomas depend on Epstein-Barr virus, whose oncoprotein LMP1 mimics CD40 to activate NF-kB (already mapped), and EBV+ B-blasts also populate angioimmunoblastic PTCL.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — TFH biology: angioimmunoblastic PTCL arises from follicular helper T cells whose physiological role is MHC class II-restricted help to B cells, and this retained programme drives the polyclonal B-cell expansion and hypergammaglobulinaemia typical of the disease.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Chemotherapy execution: CHOP-based anthracycline chemotherapy, the standard PTCL regimen, kills lymphoma cells through caspase-3-mediated apoptosis, and resistance to this executioner pathway contributes to the poor outcomes that characterise most peripheral T-cell lymphomas.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — Hypergammaglobulinaemia: angioimmunoblastic PTCL, arising from follicular helper T cells (MHC class II already mapped), drives a polyclonal B-cell expansion that produces hypergammaglobulinaemia and the autoantibodies behind its autoimmune features.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Autoimmune cytopenias: angioimmunoblastic PTCL commonly causes autoimmune haemolytic anaemia and other cytopenias through its dysregulated B-cell help (immunoglobulin G already mapped), lowering haemoglobin at presentation.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Tumour lysis: the bulky, aggressive peripheral T-cell lymphomas can develop tumour-lysis syndrome on treatment, releasing purines that xanthine oxidase converts to uric acid, managed with allopurinol or rasburicase.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Anthracycline cardiotoxicity: the CHOP/CHOEP chemotherapy for peripheral T-cell lymphoma includes cardiotoxic doxorubicin, and troponin elevation helps detect the myocardial injury that limits the cumulative anthracycline dose.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Tumour-lysis acidosis: the rapid lysis of bulky peripheral T-cell lymphoma by chemotherapy releases acids that, with lactate, produce the metabolic acidosis of tumour-lysis syndrome (urate already mapped), part of its acute metabolic risk.
- `connects-to` → **[Secretory IgA](../../03-molecular/secretory-iga/README.md)** — Immune dysregulation: angioimmunoblastic and other peripheral T-cell lymphomas dysregulate humoral immunity, and hypogammaglobulinaemia depleting secretory IgA (immunoglobulin G already mapped) impairs mucosal defence, contributing to the infections that complicate them.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune dysregulation: IL-13 reflects the type-2 cytokine skewing of angioimmunoblastic T-cell lymphoma, the follicular-helper-T-cell (already mapped) programme driving the polyclonal immune dysregulation and rash of this peripheral T-cell lymphoma.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Th2 cytokine milieu: IL-4, with IL-13 (already mapped), drives the type-2 immune dysregulation and eosinophilia of angioimmunoblastic and other peripheral T-cell lymphomas, part of their characteristic reactive immune microenvironment.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Tumour vasculature: nitric oxide with VEGF (already mapped) regulates the prominent vascular proliferation of angioimmunoblastic T-cell lymphoma, part of the rich high-endothelial-venule vasculature of this peripheral T-cell lymphoma.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Eosinophilia: IL-5, with the Th2 skewing (IL-4 and IL-13 already mapped), drives the blood and tissue eosinophilia that characterises angioimmunoblastic and other peripheral T-cell lymphomas.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 dysregulation: the Th2-driven (IL-4 and IL-13 already mapped) polyclonal hypergammaglobulinaemia and raised IgE reflect the immune dysregulation of angioimmunoblastic T-cell lymphoma.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Tumour-lysis hyperkalaemia: the bulky, aggressive peripheral T-cell lymphoma treated with chemotherapy can release potassium in tumour-lysis syndrome (xanthine oxidase and calcium already mapped), a metabolic emergency.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Metabolic microenvironment: leptin from the marrow and stromal adipose tissue signals within the metabolic microenvironment of peripheral T-cell lymphoma.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Adipokine microenvironment: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic microenvironment of peripheral T-cell lymphoma.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the metabolic microenvironment of peripheral T-cell lymphoma.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate antitumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment relevant to the immunotherapy of peripheral T-cell lymphoma.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of peripheral T-cell lymphoma.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 arm of the inflammatory microenvironment of peripheral T-cell lymphoma.
- `connects-to` → **[IL-31](../../03-molecular/il-31/README.md)** — Pruritus cytokine: IL-31, produced by the malignant T cells, mediates the severe pruritus that is a characteristic paraneoplastic symptom of peripheral (and cutaneous) T-cell lymphoma.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Eosinophil/mast infiltrate: histamine, from the mast cells and the eosinophil-rich (IL-5 already mapped) polymorphous infiltrate, is part of the reactive microenvironment of peripheral T-cell lymphoma (especially AITL).
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Mast-cell infiltrate: the mast cells (the histamine already mapped source) populate the polymorphous reactive infiltrate of peripheral T-cell lymphoma.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Type-2 alarmin: TSLP, an epithelial/stromal alarmin, contributes to the type-2 (IL-4, IL-5, IL-13 and IL-31 already mapped) skewing of the polymorphous reactive microenvironment of peripheral T-cell lymphoma (especially AITL).
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Type-2 remodelling: periostin, downstream of the type-2 (IL-4 and IL-13 already mapped) cytokines, is part of the type-2 stromal-remodelling dimension of the reactive microenvironment of peripheral T-cell lymphoma.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a provide the innate chemotactic arm within the polymorphous reactive infiltrate of peripheral T-cell lymphoma.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Central complement: the complement C3, upstream of the C5 (already mapped), is the pivot of the complement activation within the polymorphous reactive infiltrate of peripheral T-cell lymphoma.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) links the complement to the myeloid inflammation of the peripheral-T-cell-lymphoma microenvironment.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement evasion: the peripheral-T-cell-lymphoma cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), tempering the complement attack in the reactive microenvironment.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Lymphomagenesis kinin: bradykinin, released from the kallikrein–kinin system activated by the protease-rich PTCL microenvironment, amplifies tumour vasodilation and the vascular permeability that characterises the reactive angioedema variants of this lymphoma.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical complement brake: C1-esterase inhibitor modulates the classical complement pathway (C3, C5 and C5aR1 already mapped) activated on the polymorphous reactive infiltrate and tumour surface of peripheral T-cell lymphoma.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Chemotherapy anaemia: erythropoietin corrects the cytopenias of CHOP-based chemotherapy used in peripheral T-cell lymphoma, and its receptor on lymphoma T cells raises the question of a potential direct tumour-trophic effect.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian immune surveillance: melatonin modulates NK cell (already mapped) and CD8 T-cell activity, with circadian disruption—common in lymphoma patients—impairing immune control of the peripheral T-cell lymphoma clone.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Lymphocyte activation: prolactin, via JAK2 (already mapped) signalling, promotes T-cell and B-cell proliferation within the reactive infiltrate of peripheral T-cell lymphoma; hyperprolactinaemia has been associated with lymphoma risk in autoimmune contexts.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Neuroendocrine immune modulation: oxytocin modulates the NK cell (already mapped) and T-cell activity restraining the peripheral T-cell lymphoma clone, with psychosocial stress—which suppresses oxytocin—being an immunosuppressive co-factor.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — PTCL androgen axis: testosterone via androgen receptor on T cells (already mapped) modulates Th1/Th17 (already mapped) differentiation and cytotoxic T-cell function, with androgen-driven immunosuppression contributing to the immune evasion of peripheral T-cell lymphoma.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — PTCL serotonin: serotonin via 5-HT receptors on T cells (already mapped) and NK cells (already mapped) modulates the cytotoxic immune response against the PTCL clone, with platelet (already mapped)-derived serotonin shaping the tumour microenvironment.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — PTCL vasopressin: vasopressin via V1aR on T cells (already mapped) and endothelial cells (nitric oxide already mapped) modulates lymphocyte trafficking, vascular tone and the haemophagocytic syndrome (HLH) complicating aggressive peripheral T-cell lymphoma.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — PTCL selenium: selenium-dependent glutathione peroxidase (GPX) quenches reactive-oxygen-species driving NF-κB (already mapped)-mediated genomic instability and survival signalling in the malignant T cells of peripheral T-cell lymphoma.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — PTCL iodine: iodine-dependent thyroid hormones modulate T-cell (already mapped) differentiation and NK-cell (already mapped) cytotoxic activity within the PTCL tumour microenvironment, with hypothyroidism blunting anti-tumour immune surveillance of peripheral T-cell lymphoma.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — PTCL sodium: sodium-driven Th17 polarisation via osmotic sodium sensing in T cells (already mapped) amplifies the inflammatory cytokine (NF-κB already mapped) milieu of peripheral T-cell lymphoma, with high-salt microenvironments promoting tumour-promoting T-helper skewing.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — PTCL magnesium: magnesium, as mTOR (already mapped) kinase cofactor in malignant T cells and macrophages (already mapped), restrains tumour proliferation; magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of peripheral T-cell lymphoma.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — PTCL copper: copper, as lysyl oxidase cofactor in endothelial cells (already mapped) and macrophages (already mapped), drives tumour angiogenesis; copper deficiency amplifies NF-κB (already mapped) and VEGF (already mapped) angiogenic cascade of peripheral T-cell lymphoma.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — PTCL zinc: zinc, as co-factor of immune-regulatory metalloproteinases in macrophages (already mapped) and NK cells (already mapped), supports anti-tumour cytotoxicity; zinc deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of PTCL.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — PTCL phosphorus: phosphorus-dependent ATP in macrophages (already mapped) and NK cells (already mapped) sustains anti-tumour immune surveillance; phosphorus deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of peripheral T-cell lymphoma.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — PTCL chloride: chloride channels in macrophages (already mapped) and endothelial cells (already mapped) regulate tumour-stromal homeostasis; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) angiogenic cascade in PTCL.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — PTCL sulfur: sulfur-containing glutathione in macrophages (already mapped) and NK cells (already mapped) limits oxidative stress in the tumour microenvironment; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of peripheral T-cell lymphoma.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — PTCL carbon: carbon as backbone of NF-κB (already mapped) and BCL-2 proteins in T-lymphoma cells and macrophages (already mapped) sustains tumour survival; carbon depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of peripheral T-cell lymphoma.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — PTCL hydrogen: hydrogen, via redox homeostasis in macrophages (already mapped) and NK cells (already mapped), supports anti-tumour effector function; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) oxidative cascade of PTCL.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — PTCL nitrogen: nitrogen in amino-acid scaffold of TCR signalling proteins and NF-κB (already mapped) in T-lymphoma cells sustains oncogenic signalling; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of peripheral T-cell lymphoma.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — PTCL oxygen: oxygen, via mitochondrial respiration in T-lymphoma cells and macrophages (already mapped), sustains tumour-cell survival; oxygen depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) angiogenic cascade of peripheral T-cell lymphoma.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — PTCL GLP-1: GLP-1 receptor signalling in T-lymphoma cells and macrophages (already mapped) modulates metabolic and inflammatory tumour risk; GLP-1 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of PTCL.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — PTCL angiotensin-II: angiotensin-II signalling in macrophages (already mapped) and endothelial cells (already mapped) promotes tumour angiogenesis; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of peripheral T-cell lymphoma.
- `connects-to` → **[WNT/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — PTCL wnt-beta-catenin: WNT/β-catenin on T-lymphoma cells (already mapped) and macrophages (already mapped) drives tumour invasion; wnt-beta-catenin dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of PTCL.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — PTCL rankl: RANKL from macrophages (already mapped) and T-lymphoma cells (already mapped) promotes tumour immune evasion; rankl excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of PTCL.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — PTCL fibronectin: fibronectin in fibroblasts (already mapped) and macrophages (already mapped) scaffolds T-lymphoma tumour ECM; fibronectin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of PTCL.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — PTCL notch: Notch signalling on T-lymphoma cells (already mapped) and macrophages (already mapped) regulates T-lymphoma cell fate; notch dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of PTCL.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — PTCL igf-1: IGF-1 from T-lymphoma cells (already mapped) and macrophages (already mapped) promotes T-lymphoma cell survival; igf-1 dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of PTCL.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — PTCL activin-a: activin-A from T-lymphoma cells (already mapped) and macrophages (already mapped) drives T-lymphoma fibrosis; activin-a excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of PTCL.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — PTCL cgrp: CGRP from T-lymphoma cells (already mapped) and macrophages (already mapped) modulates T-lymphoma neuroimmune tone; cgrp excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of PTCL.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — PTCL calcitonin: calcitonin from T-lymphoma cells (already mapped) and macrophages (already mapped) modulates calcium balance in T-cell lymphoma; calcitonin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of PTCL.
- `connects-to` → **[Substance P](../../03-molecular/substance-p/README.md)** — PTCL substance-p: substance P from T-lymphoma cells (already mapped) and macrophages (already mapped) modulates T-lymphoma neuroimmune signalling; substance-p excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of PTCL.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^horwitz-2019-echelon2]: Horwitz S, O'Connor OA, Pro B, et al. Brentuximab vedotin with chemotherapy for CD30-positive peripheral T-cell lymphoma (ECHELON-2): a global, double-blind, randomised, phase 3 trial. *Lancet.* 2019;393(10168):229-240. [doi:10.1016/S0140-6736(18)32984-2](https://doi.org/10.1016/S0140-6736(18)32984-2) · [PubMed 30522922](https://pubmed.ncbi.nlm.nih.gov/30522922/)
[^palomero-2014-ptcl-epigenetics]: Palomero T, Couronné L, Khiabanian H, et al. Recurrent mutations in epigenetic regulators, RHOA and FYN kinase in peripheral T cell lymphomas. *Nat Genet.* 2014;46(2):166-170. [doi:10.1038/ng.2872](https://doi.org/10.1038/ng.2872) · [PubMed 24413734](https://pubmed.ncbi.nlm.nih.gov/24413734/)
