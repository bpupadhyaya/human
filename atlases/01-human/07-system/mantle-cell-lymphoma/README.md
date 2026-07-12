---
schema: human-scale-entry/v1
id: mantle-cell-lymphoma
name: Mantle Cell Lymphoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Mantle cell lymphoma is aggressive B-cell lymphoma with t(11;14) CCND1-IGH → cyclin D1 overexpression and CDK4/6 → S-phase entry; SOX11+, ATM deletion in ~40%, blastoid variant has TP53 mutations. Ibrutinib/zanubrutinib and venetoclax transformed R/R MCL; CAR-T is approved."
aliases: ["mantle cell lymphoma", "MCL", "t(11;14) lymphoma", "CCND1-IGH", "cyclin D1 lymphoma", "blastoid MCL", "leukemic non-nodal MCL"]
sources:
  - id: wang-2013-ibrutinib-mcl
    type: peer-reviewed
    cite: "Wang ML, Rule S, Martin P, et al. Targeting BTK with ibrutinib in relapsed or refractory mantle-cell lymphoma. N Engl J Med. 2013;369(6):507-516."
    doi: "10.1056/NEJMoa1306220"
    pmid: "23782157"
    url: "https://doi.org/10.1056/NEJMoa1306220"
  - id: wang-2020-brexu-zuma2
    type: peer-reviewed
    cite: "Wang M, Munoz J, Goy A, et al. KTE-X19 CAR T-cell therapy in relapsed or refractory mantle-cell lymphoma. N Engl J Med. 2020;382(14):1331-1342."
    doi: "10.1056/NEJMoa1914347"
    pmid: "32242358"
    url: "https://doi.org/10.1056/NEJMoa1914347"
cross_links:
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "t(11;14)(q13;q32) CCND1-IGH translocation in >95% of MCL → cyclin D1 constitutive overexpression → CDK4/6-RB phosphorylation → cell cycle entry; cyclin D1 IHC positivity distinguishes MCL from CLL, FL, MZL; CDK4/6 inhibitors (palbociclib) + ibrutinib studied in R/R MCL."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "BCL-2 overexpression in MCL cells → apoptosis resistance; venetoclax (BCL-2 inhibitor) ORR ~75% in R/R MCL (AIM trial: ibrutinib+venetoclax); combined ibrutinib+venetoclax achieves complete MRD negativity in ~50% of R/R MCL; BCL-2 inhibition + BTK inhibition is synergistic."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 mutation in blastoid/pleomorphic MCL → most aggressive MCL subtype (TP53 mutations ~80%); TP53-mutant MCL → ibrutinib resistance and dismal prognosis; strategies include venetoclax+BTK, CAR-T, allo-SCT; TP53 del(17p) is the highest-risk molecular feature in MCL."
  - target: 01-human/03-molecular/atm
    relation: connects-to
    note: "ATM deletion/mutation in ~40-50% of MCL (del(11q22.3)) → impaired DNA double-strand break repair → genomic instability; ATM-deficient MCL is more aggressive and shows ibrutinib resistance; PARP inhibitors + BTK inhibitors studied in ATM-mutant MCL; biallelic ATM loss in ~15%."
  - target: 01-human/03-molecular/btk
    relation: connects-to
    note: "BCR-BTK-NF-κB axis is constitutively active in MCL; ibrutinib (FDA 2013 R/R MCL: ORR 68%), zanubrutinib (FDA 2019: ORR 83%), acalabrutinib (FDA 2017: ORR 81%) are approved; BTK C481S (acquired ibrutinib resistance) → pirtobrutinib (non-covalent BTK inhibitor, FDA 2023: ORR 57%)."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB constitutively active in MCL via BCR-BTK → BCL-2, cyclin D1, XIAP → apoptosis resistance and proliferation; bortezomib (↑IκB → ↓NF-κB) active in MCL; BTK inhibitors block NF-κB upstream; NF-κB target MALT1 (CBM complex) active in MCL and under therapeutic investigation."
  - target: 01-human/07-system/cll
    relation: connects-to
    note: "MCL and CLL are both CD5+ B-cell lymphomas with frequent BM/blood involvement; key distinctions: MCL (cyclin D1+, SOX11+, CD23−, t(11;14)) vs CLL (CD23+, ZAP70+, no cyclin D1); both respond to BTK inhibitors; MCL prognosis worse; different IGHV mutation significance or histology."
  - target: 01-human/07-system/follicular-lymphoma
    relation: connects-to
    note: "Mantle cell and follicular lymphoma are both translocation-defined B-cell NHLs but opposites: MCL (t(11;14), cyclin D1) is proliferation-driven and aggressive, FL (t(14;18), BCL-2) indolent and apoptosis-resistant — cyclin D1 vs BCL-2 IHC and SOX11 distinguish them."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Mantle cell lymphoma arises from a CD5+ naive B cell of the follicular mantle zone (pre-germinal-center): t(11;14) drives cyclin D1, pushing these cells through the cell cycle; unlike FL, most MCL cells are IGHV-unmutated, reflecting their pre-germinal-center origin."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "Mantle cell lymphoma has a distinctive tropism for the GI tract: multiple lymphomatous polyposis studs the small and large bowel with MCL nodules, and occult involvement is so common that many patients have microscopic gut disease even when staging looks limited."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Mantle cell lymphoma spreads widely through the lymphatic system and beyond: it produces generalized lymphadenopathy and characteristically lymphomatous polyposis of the gut, with frequent leukemic blood and marrow involvement, so most patients present at stage IV."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "The spleen is often heavily involved in mantle cell lymphoma, and a leukemic, splenomegalic, SOX11-negative variant exists that mimics chronic lymphocytic leukemia and behaves indolently; splenic and blood involvement reflect MCL's tendency to circulate as a disseminated disease."
  - target: 01-human/07-system/dlbcl
    relation: connects-to
    note: "Mantle cell lymphoma and DLBCL are both aggressive B-cell lymphomas but distinct: MCL carries cyclin D1/t(11;14) and is incurable-relapsing, while DLBCL is potentially cured by R-CHOP; blastoid MCL can mimic DLBCL morphologically, so cyclin D1/SOX11 staining is decisive."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Mantle cell lymphoma is defined by its pre-germinal-center origin: it arises from naive mantle-zone B cells that have not transited the germinal center, so it usually lacks somatic hypermutation—its hallmark is instead t(11;14) cyclin D1 overexpression."
  - target: 01-human/07-system/multiple-myeloma
    relation: connects-to
    note: "Mantle cell lymphoma and multiple myeloma are both incurable B-lineage cancers treated with proteasome inhibitors: bortezomib works in both, though MCL is a cyclin-D1-driven nodal lymphoma while myeloma is a marrow plasma-cell tumor secreting monoclonal protein."
  - target: 01-human/07-system/hodgkin-lymphoma
    relation: connects-to
    note: "Mantle cell and Hodgkin lymphoma sit at opposite ends of B-cell lymphoma outcomes: Hodgkin's Reed-Sternberg-cell disease is usually curable, while MCL is an aggressive yet incurable t(11;14)-driven lymphoma—molecular drivers, not just lineage, set prognosis."
  - target: 01-human/07-system/burkitt-lymphoma
    relation: connects-to
    note: "Mantle cell and Burkitt lymphoma are both aggressive translocation-driven B-cell cancers: MCL's t(11;14) drives cyclin D1, Burkitt's t(8;14) drives MYC—but Burkitt is curable while mantle cell, despite responding initially, relapses and is generally incurable."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Mantle cell lymphoma frequently involves the bone marrow and blood: unlike many lymphomas it is often leukemic at diagnosis, spreading through marrow and the GI tract—so staging includes marrow biopsy, and the widespread disease shapes its aggressive, relapsing course."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Mantle cell lymphoma runs on the cyclin D1-CDK4-RB axis: overexpressed cyclin D1 inactivates RB to force the cell cycle forward, which is why CDK4/6 inhibitors are being tested—targeting the very pathway that the defining t(11;14) translocation unleashes."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "Mantle cell lymphoma is treated by targeting CD20: this B-cell marker is the target of rituximab, a backbone of MCL therapy alongside BTK inhibitors and BCL-2 blockade—reflecting MCL's identity as a CD5+ mature B-cell lymphoma."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Mantle cell lymphoma has a striking affinity for the gut: it commonly seeds the GI tract as multiple lymphomatous polyposis—numerous lymphoma polyps from stomach to colon—so endoscopic involvement is frequent even when not obviously symptomatic."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Mantle cell lymphoma both exploits and depletes the immune system: it is an aggressive mature B-cell cancer, and its therapies (anti-CD20, BTK inhibitors, chemo) cause profound immunosuppression—so infection is a major cause of morbidity during treatment."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Mantle cell lymphoma is driven through mTOR: cyclin D1 overexpression and PI3K-AKT signaling converge on mTOR to push proliferation, which is why the mTOR inhibitor temsirolimus is an approved therapy for relapsed disease."
  - target: 01-human/07-system/waldenstrom-macroglobulinemia
    relation: connects-to
    note: "Mantle cell lymphoma and Waldenstrom macroglobulinemia are both BTK-dependent B-cell cancers: ibrutinib works in each by blocking B-cell receptor signaling, though they differ in cell of origin and the IgM paraprotein that defines Waldenstrom."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Mantle cell lymphoma is now a CAR-T target: brexucabtagene engineers a patient's cytotoxic T cells to recognize CD19 and kill the lymphoma, achieving durable remissions in disease that has relapsed after chemo and BTK inhibitors."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "Mantle cell lymphoma's overexpressed cyclin D1 partners with CDK4/6: the t(11;14) translocation floods the cell with cyclin D1, which activates CDK4/6 to push past the cell-cycle checkpoint—making CDK4/6 inhibitors like palbociclib a rational target."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Mantle cell lymphoma loves the gut as lymphomatous polyposis: it studs the colon and small bowel with countless lymphoid polyps, so multiple GI polyps that turn out to be lymphoma rather than adenomas are a classic MCL presentation."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Rituximab clears mantle cell lymphoma partly via NK cells: the anti-CD20 antibody tags the malignant B cells for natural killer cells to destroy by antibody-dependent killing, a backbone mechanism of MCL immunochemotherapy."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Mantle cell lymphoma survives on B-cell-receptor calcium signaling: tonic receptor firing drives a BTK-dependent calcium flux that keeps the malignant cells alive, the very pathway ibrutinib interrupts to treat the disease."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Mantle cell lymphoma can invade the brain: especially the aggressive blastoid variant spreads to the central nervous system, a grim relapse site that drives CNS-directed prophylaxis and treatment in high-risk patients."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages support the mantle cell lymphoma niche: tumor-associated macrophages in the nodes and marrow feed the malignant B cells and dampen immunity, and a macrophage-rich tumor tends to carry a worse prognosis."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Mantle cell lymphoma bleeds iron from the gut: its lymphomatous polyposis studs the bowel with tumor nodules that ooze blood, so iron-deficiency anemia is a common sign of GI involvement."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Mantle cell lymphoma infiltrates the liver: as the widespread disease advances, it seeds the liver and spleen, enlarging them as part of the bulky, disseminated stage at diagnosis."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Mantle cell lymphoma leans on regulatory T cells: Tregs in the node and marrow microenvironment dampen the antitumor response, helping the malignant B cells persist and resist immune clearance."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "MCL is staged by imaging and scope: PET/CT photons map the widespread nodal and splenic disease, and endoscopy finds the 'lymphomatous polyposis' studding the bowel."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Aggressive MCL can lyse fast on treatment: dying cells spill phosphate and potassium in tumor lysis, a risk with bulky or blastoid disease starting chemotherapy."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "MCL studs the whole gut: 'multiple lymphomatous polyposis' carpets the stomach and intestines with polyps, a classic presentation found on endoscopy."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows MCL's irregular cell: a small-to-medium lymphocyte with a deeply notched, cleaved nucleus, its overexpressed cyclin D1 — from the t(11;14) translocation — driving relentless division."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "MCL can settle around the eye: ocular adnexal and orbital involvement form a painless mass in the conjunctiva or orbit, one of the extranodal sites this widely-spreading lymphoma reaches."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Aggressive MCL risks tumor lysis: the bulky, fast-dividing blastoid variant, burst by chemotherapy, spills potassium and phosphate into the blood, an electrolyte emergency that can stop the heart."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies both name and treat MCL: nuclear cyclin D1 shown by immunohistochemistry clinches the diagnosis, while the CD20 on the cell surface is the bullseye for rituximab and other anti-CD20 antibody drugs that anchor every regimen."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Marrow and spleen takeover shows in the red cells: as MCL packs the bone marrow and swells the spleen, it crowds out and pools erythrocytes into the anemia that, with the leukemic blood spread common in MCL, marks advanced disease."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "The same takeover drops the platelets: marrow infiltration and splenic sequestration cause thrombocytopenia, and the BTK-inhibitor drugs central to MCL therapy add their own bleeding risk by blunting platelet function."
  - target: 01-human/07-system/hepatitis-b
    relation: connects-to
    note: "Anti-CD20 therapy can reactivate hepatitis B: rituximab strips out the B cells that help hold the virus in check, so MCL patients are screened and given antiviral prophylaxis before treatment to prevent a dangerous viral flare."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "Its intensive regimens strain the heart: the anthracycline in R-CHOP and the high-dose cytarabine of induction carry cardiotoxic risk, so cardiac function is checked before the aggressive chemotherapy MCL often demands."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "MCL leans on PI3K-AKT beyond BTK: chronic B-cell-receptor signaling feeds the AKT-mTOR axis, a survival route that drives resistance to BTK inhibitors and is targeted by PI3K and mTOR inhibitors in relapsed disease."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "The bowel is a classic hideout: MCL frequently studs the gastrointestinal lining with lymphomatous polyposis, so even apparently localized disease is often found seeded through the gut epithelium when biopsied, shaping staging and follow-up."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "The lymph-node stroma is a protective niche: fibroblastic reticular and other stromal cells supply survival signals that shelter MCL cells, and part of how BTK inhibitors work is by evicting the lymphoma from this supportive microenvironment into the blood."
  - target: 01-human/07-system/mds
    relation: connects-to
    note: "Treatment leaves a later shadow: the intensive chemo and stem-cell transplants used against MCL can damage the marrow, raising the risk of therapy-related myelodysplastic syndromes years afterward — a long-term cost of aggressive cure attempts."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 backs up the survival signal: alongside constitutive NF-κB, JAK-STAT3 activation sustains mantle cell lymphoma and contributes to its resistance to BTK inhibitors, marking another targetable node."
  - target: 01-human/07-system/cytokine-storm
    relation: connects-to
    note: "CAR-T cure can spark a storm: brexucabtagene autoleucel for relapsed mantle cell lymphoma routinely triggers cytokine release syndrome as the engineered cells engage, managed with the IL-6 blocker tocilizumab."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Lymphoma and its therapy clot the veins: bulky mantle cell lymphoma and its chemotherapy raise venous thromboembolism risk, a complication watched for through the disease's aggressive treatment course."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Deep immunosuppression invites infection: the intensive chemoimmunotherapy, BTK inhibitors and CAR-T used against mantle cell lymphoma cause profound neutropenia and B-cell depletion, making febrile neutropenia and sepsis a leading danger."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: connects-to
    note: "B-cell-directed therapy opens the lung to an opportunist: rituximab and BTK-inhibitor treatment of mantle cell lymphoma suppress immunity enough that Pneumocystis pneumonia becomes a risk, prompting prophylaxis."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Marrow infiltration and inflammation lower the count: mantle cell lymphoma commonly involves the bone marrow and raises inflammatory cytokines, producing an anemia of chronic disease on top of any marrow crowding."
  - target: 02-pathogen/01-viruses/hepatitis-b-virus
    relation: connects-to
    note: "Anti-CD20 therapy can reactivate it: the rituximab central to mantle cell lymphoma treatment depletes B cells and can reawaken latent hepatitis B, so screening and antiviral prophylaxis precede therapy."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Its BTK inhibitors invite mold: ibrutinib and related agents used in mantle cell lymphoma are associated with invasive aspergillosis and other fungal infections, a recognized hazard of this targeted therapy."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Its drugs can strain the heart: ibrutinib causes atrial fibrillation and cardiac events, while the anthracyclines and cardiotoxic agents in MCL induction regimens add to the risk of heart failure."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Its chemotherapy injures the nerves: the bortezomib and vincristine used in mantle cell lymphoma regimens cause a dose-limiting peripheral neuropathy with neuropathic pain."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "Its BTK-inhibitor therapy reawakens shingles: ibrutinib and other agents for mantle cell lymphoma suppress immunity and characteristically reactivate latent varicella-zoster as herpes zoster."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "An aggressive, relapsing lymphoma weighs on mood: the poor prognosis, intensive therapy and recurrent relapses of mantle cell lymphoma contribute to a substantial burden of depression."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its BTK inhibitors strain the heart: ibrutinib used for mantle cell lymphoma causes atrial fibrillation, hypertension and bleeding, the main cardiovascular toxicities of BTK-inhibitor therapy."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "CAR-T and CNS spread reach the brain: mantle cell lymphoma can involve the central nervous system, and the CAR-T cell therapy used for relapsed disease causes immune-effector neurotoxicity (ICANS)."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "An aggressive, incurable, relapsing lymphoma breeds worry: the poor prognosis, intensive therapy and inevitable relapse of mantle cell lymphoma foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It fills the marrow at diagnosis: mantle cell lymphoma almost always involves the bone marrow, causing cytopenias, and the ibrutinib used to treat it commonly causes arthralgia."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Its high tumour burden floods the kidney: the bulky disease of mantle cell lymphoma risks tumour lysis syndrome with acute kidney injury when treatment begins."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It crowds and exposes the chest: mediastinal and pulmonary nodal disease can cause effusions, and the BTK-inhibitor therapy raises the risk of pneumonia and fungal infection."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It can mark the skin: mantle cell lymphoma occasionally infiltrates the skin, and its BTK-inhibitor and chemotherapy treatments cause rashes, bruising and alopecia."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Treatment threatens fertility and sanctuary sites: chemotherapy for mantle cell lymphoma can impair fertility, and the testis can act as a sanctuary site for residual disease."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It can infiltrate endocrine glands: aggressive mantle cell lymphoma occasionally involves the thyroid or adrenal glands, and steroid-containing regimens disturb glucose control."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "BTK inhibition transformed it: BTK inhibitors (ibrutinib, acalabrutinib), the BCL-2 inhibitor venetoclax and CDK4/6 inhibitors against its cyclin-D1 driver are central to modern mantle cell lymphoma care."
  - target: 03-medicine/01-modern/13-cancer/car-t
    relation: connects-to
    note: "Engineered cells for relapse: brexucabtagene autoleucel, a CD19 CAR-T therapy, achieves durable remissions in mantle cell lymphoma that has relapsed after chemotherapy and BTK inhibitors."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Intensive chemoimmunotherapy upfront: high-dose cytarabine-containing regimens with rituximab, often with autologous transplant, are the chemotherapy backbone for younger patients."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Its targeted drug provokes arrhythmia: the BTK inhibitors that treat mantle cell lymphoma—ibrutinib above all—commonly cause atrial fibrillation through off-target effects on cardiac signalling, so the conduction system is a key toxicity site of MCL therapy."
  - target: 01-human/07-system/all
    relation: connects-to
    note: "When it turns acute-leukaemia-like: the blastoid and pleomorphic variants of mantle cell lymphoma behave aggressively with a leukaemic phase and CNS spread, resembling acute lymphoblastic leukaemia and demanding similarly intensive, transplant-based treatment."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Largely checkpoint-resistant: unlike Hodgkin lymphoma, mantle cell lymphoma responds poorly to PD-1 inhibitors as monotherapy, so its immunotherapy centres on CD19 CAR-T and bispecific antibodies rather than checkpoint blockade."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "BTK-inhibitor cardiotoxicity: ibrutinib, a mainstay of mantle-cell lymphoma, causes atrial fibrillation, ventricular arrhythmia and cardiomyopathy, so cardiac monitoring accompanies treatment."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Hepatic and splenic infiltration: mantle-cell lymphoma spreads widely, infiltrating the liver's portal tracts and the hepatic lobule along with marrow, spleen and gut."
  - target: 01-human/07-system/ptcl
    relation: connects-to
    note: "Aggressive lymphomas, opposite lineages: mantle-cell lymphoma is an aggressive B-cell lymphoma while peripheral T-cell lymphoma is its T-cell counterpart, both hard to cure and often relapsing."
  - target: 01-human/07-system/immune-thrombocytopenia
    relation: connects-to
    note: "Secondary autoimmune cytopenia: like other low-grade B-cell malignancies, mantle-cell lymphoma can drive antibody-mediated platelet destruction, so a new immune thrombocytopenia in an older adult warrants screening for an underlying lymphoma."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Defenceless against infection: anti-CD20 antibodies and BTK inhibitors used for mantle-cell lymphoma deplete B cells profoundly, causing severe, prolonged COVID-19 and poor vaccine responses in these patients."
  - target: 01-human/07-system/gout
    relation: connects-to
    note: "Tumour-lysis fallout: bulky or blastoid mantle-cell lymphoma releases a flood of urate when treated, driving acute hyperuricaemia and crystal disease that overlaps with gout and threatens the kidney unless rasburicase is given."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Recurrent driver: NOTCH1 and NOTCH2 mutations recur in mantle cell lymphoma and mark a more aggressive clinical course, a candidate therapeutic target."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Blastoid transformation: MYC amplification or translocation drives the aggressive blastoid and pleomorphic variants of mantle cell lymphoma, worsening prognosis."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Epigenetic dependence: EZH2 overexpression contributes to mantle cell lymphoma proliferation, an emerging epigenetic vulnerability beyond the defining cyclin D1 lesion."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K dependence: chronic B-cell-receptor signalling activates PI3K in mantle cell lymphoma, sustaining survival and underlying resistance to BTK inhibitors."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Metabolic adaptation: HIF-1α supports the glycolytic metabolism of proliferating mantle cell lymphoma cells in the hypoxic lymph-node and marrow niches."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Nodal angiogenesis: VEGF drives the angiogenesis of involved lymph nodes in mantle cell lymphoma, supporting tumour growth and dissemination."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Niche homing: CXCL12-CXCR4 signalling anchors mantle cell lymphoma cells in the protective marrow and nodal niche, and BTK inhibitors mobilise them out of it, causing the transient treatment-related lymphocytosis."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Telomerase immortalisation: TERT activation maintains telomeres in mantle cell lymphoma cells, granting the replicative capacity that complements the cyclin D1 overexpression driving the disease."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Macrophage microenvironment: CCL2 recruits tumour-associated macrophages into the mantle cell lymphoma niche, supporting the malignant B cells and shaping response to therapy."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "BCR-proximal kinase: Src-family kinases such as LYN transduce the chronic-active B-cell-receptor signal upstream of BTK that drives mantle cell lymphoma, the proximal node of the pathway BTK inhibitors block downstream."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Apoptosis blockade: BCL-2 dependency lets mantle cell lymphoma evade caspase-3-mediated apoptosis, the basis for the dramatic activity of the BCL-2 inhibitor venetoclax that restores the cell-death program."
  - target: 01-human/03-molecular/rad51
    relation: connects-to
    note: "ATM-loss instability: frequent ATM loss in mantle cell lymphoma impairs the DNA-damage response and leaves RAD51-dependent repair under strain, driving the genomic instability that fuels its aggressive course."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Cellular immunotherapy: CD19 CAR-T (brexucabtagene) and CD20-CD3 bispecific antibodies redirect cytotoxic T cells to kill mantle-cell lymphoma through perforin and granzyme, achieving durable remissions after chemotherapy and BTK inhibitors fail."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement-dependent killing: anti-CD20 antibodies (rituximab, obinutuzumab), a backbone of mantle-cell therapy, kill cells partly through complement-dependent cytotoxicity, fixing C3 and the membrane-attack complex on the lymphoma cells."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Translocation and BCR: the defining t(11;14) places cyclin D1 under the immunoglobulin heavy-chain enhancer, driving its overexpression, while tonic B-cell-receptor signalling sustains the cell — the dependence that BTK inhibitors exploit."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Proliferative output: overexpressed cyclin D1 (mapped) drives CDK4/6 (mapped) to phosphorylate RB (mapped) and release E2F1, the cell-cycle engine central to mantle cell lymphoma."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "Aggressive variant: CDKN2A/p16 deletion removes the brake on the cyclin-D1-CDK4/6 axis and marks the blastoid, high-proliferation form of mantle cell lymphoma."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PI3K survival and resistance: PTEN loss activates PI3K-AKT (PIK3CA, AKT and mTOR already mapped), a survival pathway and a mechanism of resistance to BTK inhibitors in mantle cell lymphoma."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "STAT3 survival: JAK-STAT3 signalling (STAT3 already mapped) contributes to the survival and microenvironmental support of mantle cell lymphoma."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Nodal microenvironment: IL-6 from the tumour microenvironment signals through STAT3 (already mapped) to support the survival of mantle-cell-lymphoma cells, particularly in their protective nodal niches."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "p53 inactivation: MDM2 overexpression provides an alternative route to p53 inactivation (p53 already mapped), cooperating with cyclin-D1 overexpression and ATM loss in mantle cell lymphoma."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "B-cell-receptor signalling through ERK-MAPK provides a proliferative input in mantle cell lymphoma, downstream of the BTK-dependent BCR pathway already mapped."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 supports mantle-cell-lymphoma survival and its interactions with the nodal microenvironment."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β within the lymph-node microenvironment modulates immune evasion and the stromal niche of mantle cell lymphoma."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the antitumour immune response of mantle cell lymphoma."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β already mapped) normally restrains B-cell proliferation, a brake overridden by the cyclin-D1 translocation of mantle cell lymphoma."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors, restrained by BCR-PI3K-AKT signalling, modulate the survival of the cyclin-D1-driven cells of mantle cell lymphoma."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the cyclin-D1 stability and survival signaling of mantle cell lymphoma."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the inflammatory tumor microenvironment of mantle cell lymphoma."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING modulates the inflammatory and immune microenvironment of mantle cell lymphoma."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of mantle cell lymphoma."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival and drug resistance of mantle cell lymphoma cells, particularly under BTK-inhibitor therapy."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling is recurrently mutated in mantle cell lymphoma, dysregulating its transcriptional program."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of mantle cell lymphoma."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-family chemokine signaling (CXCL12/CXCR4 already mapped) participates in the microenvironment homing of mantle cell lymphoma."
  - target: 01-human/03-molecular/baff
    relation: connects-to
    note: "BAFF-driven B-cell survival signaling participates in the microenvironment-dependent survival of mantle cell lymphoma."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment of mantle cell lymphoma."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of mantle cell lymphoma."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory microenvironment of mantle cell lymphoma."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling downstream of the B-cell receptor participates in the survival signaling of mantle cell lymphoma."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine (CD39/CD73-adenosine) signaling participates in the immunosuppressive tumor microenvironment of mantle cell lymphoma."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin participates in the microenvironment and stromal interactions of mantle cell lymphoma."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immunotherapy: MHC class II antigen presentation shapes the T-cell response to mantle cell lymphoma, relevant to the CD19 CAR-T and bispecific-antibody therapies that have transformed treatment of relapsed disease."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "CD19 CAR-T: IL-2-driven T-cell expansion powers the brexucabtagene autoleucel CD19 CAR-T therapy (perforin already mapped) that produces durable remissions in relapsed, BTK-inhibitor-exposed mantle cell lymphoma."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Tumour lysis: the aggressive, high-burden blastoid variant of mantle cell lymphoma is prone to tumour-lysis syndrome on treatment, releasing purines that xanthine oxidase converts to uric acid, managed with allopurinol or rasburicase."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "BTK-inhibitor cardiotoxicity: the BTK inhibitors central to mantle cell lymphoma therapy (BTK already mapped) cause atrial fibrillation and, rarely, ventricular arrhythmia, and troponin elevation marks the myocardial injury of this major class toxicity."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Marrow involvement: bone-marrow infiltration (already mapped) by mantle cell lymphoma and its intensive chemoimmunotherapy lower haemoglobin, the anaemia with other cytopenias marking advanced disease and treatment toxicity."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Tumour-lysis acidosis: the rapid lysis of the high-burden blastoid mantle cell lymphoma by chemotherapy releases acids that, with lactate, produce the metabolic acidosis of tumour-lysis syndrome (urate already mapped)."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive microenvironment: IL-10 in the tumour microenvironment dampens the anti-tumour T-cell response, part of the immune evasion of mantle cell lymphoma that the CD19 CAR-T and bispecific therapies aim to overcome."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Nurse-like stromal support: IL-4 polarises the tumour-associated macrophages toward an M2 phenotype (IL-10 already mapped), the nurse-like cells of the microenvironment that support the survival of the mantle cell lymphoma clone."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Tumour vasculature: nitric oxide with VEGF (already mapped) regulates the vascular tone and angiogenesis of mantle cell lymphoma, part of the supportive stroma of this aggressive lymphoma."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "Splenomegaly: mantle cell lymphoma commonly presents with marked splenomegaly, the spleen and lymph nodes infiltrated by the cyclin-D1-positive (already mapped) clone, and splenic involvement can dominate the leukaemic-variant disease."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "CAR-T immunotherapy: the cytotoxic T cells — engineered as CD19 CAR-T (brexucabtagene; perforin already mapped) — achieve deep remissions in relapsed mantle cell lymphoma that has failed BTK inhibition."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Tumour-lysis hypocalcaemia: the bulky, proliferative mantle cell lymphoma treated with intensive therapy can trigger tumour-lysis syndrome (xanthine oxidase already mapped), the hyperphosphataemia complexing calcium to cause hypocalcaemia."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "M2 stromal arm: IL-13, with IL-4 (already mapped), drives the M2 macrophage arm of the immunosuppressive microenvironment of mantle cell lymphoma."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Marrow-adipocyte adipokine: leptin from the marrow adipose tissue of the bone-marrow (already mapped) microenvironment signals to the mantle cell lymphoma cells, part of its metabolic niche crosstalk."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Adipokine microenvironment: adiponectin, with leptin (already mapped), from the marrow adipose tissue signals within the metabolic microenvironment of mantle cell lymphoma."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipokine microenvironment: resistin, with leptin and adiponectin (already mapped), completes the marrow-adipocyte adipokine signalling of the microenvironment of mantle cell lymphoma."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "ADCC effectors: the NK cells mediate the antibody-dependent cellular cytotoxicity of the anti-CD20 (already mapped) rituximab against the mantle cell lymphoma B cells (already mapped)."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate antitumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment relevant to the immunotherapy of mantle cell lymphoma."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the T and NK (already mapped) cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity, relevant to the CD19 CAR-T immunotherapy of mantle cell lymphoma."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of mantle cell lymphoma."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of mantle cell lymphoma."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the mantle-cell-lymphoma microenvironment."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the mantle-cell-lymphoma microenvironment."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of mantle cell lymphoma."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Rituximab CDC: the complement C5 (with C3 already mapped) is the effector of the complement-dependent cytotoxicity by which the anti-CD20 (already mapped) rituximab kills the mantle-cell-lymphoma B cells (already mapped)."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling links the complement (C3 and C5 already mapped) to the myeloid inflammation of the mantle-cell-lymphoma microenvironment."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement evasion: the mantle-cell-lymphoma cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), a resistance mechanism to the anti-CD20 complement-dependent killing."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Lymph node stroma alarmin: TSLP from lymph-node stromal cells activates the dendritic cells and B cells of the mantle zone, promoting the BCR survival signalling and NF-kB-mediated apoptosis resistance that drive the aggressive expansion of mantle-cell lymphoma."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Chemoimmunotherapy anaemia: erythropoietin counters the myelosuppression induced by the RCHOP and bendamustine-rituximab regimens used in MCL; EPO-stimulating agents are a standard supportive measure to maintain haemoglobin and treatment tolerance in mantle-cell lymphoma."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Lymphoma dissemination: bradykinin promotes vascular permeability and transendothelial migration of MCL cells, facilitating the aggressive dissemination into peripheral blood, marrow, and extranodal sites that characterise the blastoid variant of mantle-cell lymphoma."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "C1-INH complement regulation: C1-INH modulates the classical pathway (C3, C5 and C5aR1 already mapped) activated by anti-CD20 (CD20 already mapped) therapies in MCL, balancing rituximab complement-dependent cytotoxicity and minimising complement-mediated adverse effects."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell mediator in MCL stroma: histamine from mast cells (already mapped) in the MCL stroma promotes VEGF-driven (already mapped) angiogenesis and immunosuppression, while H2-receptor signalling on MCL B cells (already mapped) reduces cAMP-mediated apoptosis."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Lymphoma-niche periostin: periostin, secreted by cancer-associated fibroblasts (already mapped) in the MCL stroma under TGF-β (already mapped) stimulation, reinforces the lymphoma niche and promotes the B-cell (already mapped) proliferative advantage in mantle-cell lymphoma."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian lymphoma regulation: melatonin, via MT1/MT2 receptors on MCL B cells and tumour-associated macrophages (already mapped), suppresses cyclin D1-driven (already mapped) cell-cycle progression and NF-κB (already mapped) anti-apoptotic signalling in mantle-cell lymphoma."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Androgen-B-cell axis: testosterone, via androgen receptor on MCL B cells (already mapped), suppresses anti-tumour immune surveillance and modulates the NF-κB (already mapped) and cyclin D1-overexpressing (already mapped) proliferative programme of mantle-cell lymphoma."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Tumour-microenvironment 5-HT: serotonin released from activated platelets (already mapped) in the MCL vasculature binds 5-HT2 receptors on MCL B cells and macrophages (already mapped), modulating pro-tumour NF-κB (already mapped) inflammation in mantle-cell lymphoma."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "MCL prolactin B-cell: prolactin, via PRLR on MCL B cells (already mapped) and tumour-associated macrophages (already mapped), upregulates NF-κB (already mapped) and IL-6 (already mapped) pro-survival signalling, promoting the immunosuppressive TME of mantle-cell lymphoma."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "MCL oxytocin anti-tumour: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped) in the MCL stroma, attenuates the NF-κB (already mapped) and IL-6 (already mapped) pro-tumour immune cascade in mantle-cell lymphoma."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "MCL vasopressin vascular: vasopressin, via V1aR on macrophages (already mapped) and mast cells (already mapped) in the MCL stroma, modulates the vascular niche; dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) pro-tumour signalling in mantle-cell lymphoma."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "MCL selenium: selenium, as GPx in macrophages (already mapped) and T-cytotoxic cells (already mapped), scavenges ROS; selenium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) oxidative B-cell (already mapped) tumour cascade of mantle-cell lymphoma."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "MCL iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) polarisation and T-cytotoxic (already mapped) immune activation; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of mantle-cell lymphoma."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "MCL sodium: high dietary sodium promotes macrophage (already mapped) and mast-cell (already mapped) activation; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) skewing amplifies the B-cell (already mapped) tumour cascade of mantle-cell lymphoma."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "MCL magnesium: magnesium cofactors kinase signalling in macrophages (already mapped) and B-cells (already mapped); magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and mast-cell (already mapped) tumour cascade of mantle-cell lymphoma."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "MCL copper: copper, via SOD1 in macrophages (already mapped) and T-cytotoxic cells (already mapped), scavenges ROS; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and B-cell (already mapped) tumour cascade of mantle-cell lymphoma."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "MCL zinc: zinc, as cofactor of antioxidant enzymes in macrophages (already mapped) and T-cytotoxic cells (already mapped), attenuates oxidative stress; zinc deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and B-cell (already mapped) cascade of MCL."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "MCL carbon: carbon as backbone of cyclin-D1 (already mapped) and BTK protein scaffold sustains B-cell (already mapped) mantle-zone proliferation; carbon depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCL-2 (already mapped) lymphoma cascade of MCL."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "MCL chloride: chloride regulates B-cell (already mapped) and macrophage (already mapped) ion homeostasis; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCL-2 (already mapped) protumorigenic microenvironment of mantle-cell lymphoma."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "MCL nitrogen: nitrogen in amino-acid scaffold of cyclin-D1 (already mapped) and BTK proteins sustains B-cell (already mapped) proliferation; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of mantle-cell lymphoma."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "MCL hydrogen: hydrogen in redox chemistry of B-cells (already mapped) and macrophages (already mapped) modulates cyclin-D1 (already mapped) stability; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCL-2 (already mapped) cascade of MCL."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "MCL oxygen: oxygen supports aerobic metabolism in B-cells (already mapped) and macrophages (already mapped) for cyclin-D1 (already mapped) signalling; oxygen deficit amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCL-2 (already mapped) cascade of MCL."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "MCL sulfur: sulfur in cysteine residues of BTK and NF-κB (already mapped) proteins sustains B-cell (already mapped) signalling; sulfur dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCL-2 (already mapped) cascade of mantle-cell lymphoma."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "MCL pd-1: PD-1 on T-cytotoxic cells (already mapped) and macrophages (already mapped) modulates lymphoma immune evasion; pd-1 dysregulation amplifies smad4 (already mapped) and vegf (already mapped) and il-2 (already mapped) B-cell lymphoma cascade of MCL."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "MCL glp-1: GLP-1 from macrophages (already mapped) and natural killer cells (already mapped) modulates metabolic-inflammatory tone; glp-1 dysfunction amplifies smad4 (already mapped) and vegf (already mapped) and il-2 (already mapped) cascade of mantle cell lymphoma."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "MCL angiotensin-ii: angiotensin-II from macrophages (already mapped) and fibroblasts (already mapped) drives tumour vascular remodelling; angiotensin-ii excess amplifies smad4 (already mapped) and vegf (already mapped) and il-2 (already mapped) cascade of MCL."
---

# Mantle Cell Lymphoma

## Overview

**Mantle cell lymphoma (MCL)** is a mature B-cell non-Hodgkin lymphoma arising from naïve B-cells of the inner mantle zone of secondary lymphoid follicles. MCL accounts for ~5-7% of NHL (~4,000-5,000 cases/year in the US) and is historically aggressive with median OS of ~4-5 years in the pre-BTK inhibitor era. The molecular hallmark is **t(11;14)(q13;q32) CCND1-IGH** — present in >95% of cases — which places cyclin D1 (CCND1) under the IgH enhancer, driving constitutive cyclin D1 overexpression → CDK4/6 phosphorylation of RB → S-phase entry in cells that would otherwise be quiescent. BTK inhibitors (ibrutinib, zanubrutinib, acalabrutinib) transformed the R/R landscape with ~65-70% ORR [^wang-2013-ibrutinib-mcl], and brexucabtagene autoleucel (KTE-X19, ZUMA-2) became the first CAR-T approved for MCL in 2020 [^wang-2020-brexu-zuma2].

**Epidemiology:**
- ~4,000-5,000 new cases/year in the US; median age ~67; M:F ~3-4:1 (strong male predominance)
- Stage III-IV in ~70% at diagnosis; BM and peripheral blood involvement common
- Highly variable natural history: Indolent subset (~10%) vs. aggressive majority; blastoid variant: worst prognosis
- Median OS: ~5-7 years with chemoimmunotherapy; improving with BTK inhibitors (PFS 15-20 months in R/R); 5-year OS ~60%

**MCL clinical heterogeneity:**
- **Conventional MCL (SOX11+, nodal, GI tract):** Most common; aggressive; requires treatment at diagnosis
- **Leukemic non-nodal MCL (nnMCL, SOX11−, BM/blood, IGHV mutated):** Indolent subset; watch-and-wait approach acceptable; lower TP53 mutation rate; better prognosis
- **Blastoid variant:** Blastoid or pleomorphic morphology; high Ki-67 (>40-50%); TP53 mutations frequent; aggressive; poor prognosis even with current therapies

## Structure

### Molecular landscape

**t(11;14)(q13;q32) — the founding translocation:**
BCR VDJ recombination error → CCND1 (chromosome 11q13) fused to IgH locus (14q32) → cyclin D1 placed under IGH super-enhancer → constitutive cyclin D1 protein overexpression in mantle zone B-cells → CDK4-cyclin D1 complex → RB phosphorylation → E2F → S-phase entry → cell cycle entry without mitogenic signals. Normal naive B-cells of the inner mantle zone express cyclin D1 transiently; MCL cells maintain constitutive cyclin D1 → clonal expansion.

**Cyclin D1-negative MCL (~5%):**
Rare cases lack t(11;14); alternative translocations: t(11;14) with CCND2 or CCND3 → cyclin D2/D3 overexpression; gene expression profiling (SOX11, MCL signatures) helps diagnose cyclin D1-negative MCL.

**Secondary alterations:**
- **IGHV mutation status:** Unmutated (≥98% germline) → more aggressive; mutated (nnMCL, SOX11−) → more indolent
- **SOX11:** Transcription factor expressed in >85% of conventional MCL; absent in nnMCL; SOX11 IHC distinguishes MCL from CLL (SOX11−), FL (SOX11−), and MZL (SOX11−)
- **ATM deletion/mutation (~40-50%):** del(11q22.3); impairedDNA DSB repair; cooperates with cyclin D1 in MCL pathogenesis; MCL is closely related to ATM-expressing mantle zone B-cells
- **TP53 mutation/deletion:** ~20-30% overall; ~80% in blastoid MCL → ibrutinib resistance; del(17p) → highest-risk MCL
- **CDKN2A deletion (p16/ARF):** ~30%; co-deleted with ATM in some cases; accelerates progression
- **BCL-2 overexpression:** ~90%; driven by NF-κB and signal transduction; not by t(14;18) (which is absent in MCL); cooperates with cyclin D1
- **MYC rearrangement:** ~10-15% of blastoid/refractory MCL; very aggressive; triple-hit variant (MYC+BCL-2 rearrangement)

**Ki-67 proliferation index:**
Ki-67 >30%: High-risk MCL; >50%: Blastoid morphology regardless of classification. MIPI-combined (MIPI-c) includes Ki-67 → best prognostic stratification for treatment decisions.

**BTK pathway alterations:**
Constitutive BCR-BTK-NF-κB signaling in MCL; BTK C481S acquired resistance in ~30% of ibrutinib-resistant MCL; PLCγ2 gain-of-function mutations in ~5% of ibrutinib-resistant MCL.

### Immunophenotype

CD5+, CD19+, CD20+ (bright), CD23− (distinguishes from CLL, which is CD23+), FMC7+, CD43+ (distinguishes from FL), cyclin D1+ (nuclear, by IHC), SOX11+ (nuclear, by IHC); surface IgM+ typically; CD10− (distinguishes from FL); CD25−. Flow cytometry: CD5+/CD23− is virtually diagnostic of MCL or CLL; cyclin D1 IHC or t(11;14) FISH confirms MCL.

## Function

### Mantle zone B-cell biology

**Normal mantle zone B-cells:**
Naïve B-cells that surround the germinal center (GC) in secondary lymphoid follicles; express surface IgM and IgD; not hypermutated; express BCR signaling machinery. MCL arises from these cells (or from B-cells transitioning through the mantle zone) — explaining the characteristic indolent leukemic variant (nnMCL) vs. aggressive nodal/GI variant.

**Cyclin D1 and cell cycle entry:**
Cyclin D1 overexpression → CDK4/cyclin D1 complex → RB phosphorylation at Ser780/Ser795 → RB releases E2F1/2/3 → E2F target genes (CDC25A, thymidine kinase, DHFR, dihydrofolate reductase) → DNA synthesis initiation. Cells in G0 are forced into G1 → S → proliferating. Sole cyclin D1 overexpression is insufficient for malignancy (requires ATM/TP53 loss or BCR-BTK amplification as co-events).

### BCR-BTK signaling in MCL

MCL cells maintain constitutive tonic BCR signaling (independent of antigen) and enhanced BTK activity → NF-κB → BCL-2, cyclin D1, XIAP → survival and proliferation. BTK inhibition (ibrutinib) blocks this survival signal → redistribution of MCL cells from nodes to blood → response (similar to CLL). MCL cells in proliferation centers of lymph nodes (high cyclin D1, high Ki-67) are more BTK-dependent than circulating MCL cells.

## Pathology

### Staging and workup

**Ann Arbor staging (Lugano classification):**
Most MCL presents at Stage III-IV; staging rarely changes management (treatment indicated if symptomatic at any stage).

**MIPI (MCL International Prognostic Index):**
4 factors: Age, ECOG PS, LDH, WBC → low/intermediate/high risk; median OS: low ~not reached; intermediate ~51 months; high ~29 months.
- MIPI-combined (MIPI-c): MIPI + Ki-67; best predictor; Ki-67 ≥30% = high risk.

**Staging workup:**
- CT chest/abdomen/pelvis with contrast + PET-CT: Baseline (PET not routinely standard but recommended for staging)
- BM biopsy + aspirate: Standard; MCL often involves BM at diagnosis (~50-70%)
- Complete blood count: Circulating MCL cells (lymphocytosis) in leukemic variant
- Morphology review: Classic (small-medium lymphocytes with irregular nuclei), blastoid, pleomorphic
- IHC: Cyclin D1, SOX11, Ki-67; FISH: t(11;14) if cyclin D1-negative
- Molecular: TP53 mutation/del(17p) by FISH or NGS; IGHV mutation status; ATM deletion
- IGHV sequencing: To identify nnMCL (mutated IGHV = indolent subset); SOX11 IHC
- Lumbar puncture: For blastoid MCL or neurological symptoms (CNS MCL prophylaxis)
- Upper/lower endoscopy: If GI symptoms; MCL has high GI involvement (multiple lymphomatous polyposis)

### Treatment

**Watch and wait (nnMCL only):**
For SOX11−, mutated IGHV, non-bulky, asymptomatic nnMCL: Observation is safe; initiate treatment when symptomatic. Intensive chemotherapy not indicated in asymptomatic nnMCL.

**First-line (conventional MCL, eligible for intensive therapy):**

**Intensive (young, fit patients <65-70):**
- **R-CHOP alternating with R-DHAP → autologous SCT consolidation (MCL Younger protocol):** MCL0306 trial; MCL Nordic protocol; 6-year OS ~60%; standard for transplant-eligible MCL
- **BR (rituximab-bendamustine):** Alternative for less-fit patients; PFS ~35-40 months; less neurotoxicity than hyper-CVAD
- **Hyper-CVAD + rituximab (alternating with methotrexate-cytarabine):** MDACC regimen; ORR 97%; high CR; toxic (neurotoxicity, cytopenias); used in blastoid/aggressive variants
- **Rituximab maintenance:** Post-induction or post-auto-SCT; improves PFS (MCL Elderly trial); 4 years rituximab q2 months

**Non-intensive (elderly/less-fit patients):**
- **BR (rituximab-bendamustine) × 6 cycles → rituximab maintenance:** PFS ~35-40 months; standard for elderly MCL
- **Ibrutinib + rituximab (WINDOW-1 trial):** Emerging first-line option; deep responses; ongoing evaluation
- **VR-CAP (bortezomib + rituximab + cyclophosphamide + doxorubicin + prednisone):** Improved PFS vs. R-CHOP; option for first-line
- **Acalabrutinib monotherapy:** Under investigation first-line for older/unfit

**Relapsed/refractory MCL:**

**BTK inhibitors:**
- **Ibrutinib 560 mg daily:** [^wang-2013-ibrutinib-mcl] ORR 68%; CR 21%; median DOR 17.5 months; FDA approved 2013 for R/R MCL
- **Zanubrutinib 160 mg BID (SEQUOIA/BGB-3111-206):** ORR 83%; preferred for cardiac-risk patients; FDA approved 2019 for R/R MCL
- **Acalabrutinib (ACE-LY-004):** ORR 81%; FDA approved 2017 for R/R MCL after ≥1 prior therapy
- **Pirtobrutinib (LOXO-305, BRUIN trial):** ORR ~57% in covalent BTK-inhibitor-pretreated MCL; FDA approved 2023 for R/R MCL after ≥2 prior lines including BTK inhibitor

**Venetoclax:**
- Venetoclax (BCL-2 inhibitor) ORR ~75% in R/R MCL monotherapy; combined ibrutinib+venetoclax (AIM trial): CR 62%; deep MRD negativity; time-limited therapy studied

**CAR-T therapy:**
- **Brexucabtagene autoleucel (KTE-X19, ZUMA-2 trial):** [^wang-2020-brexu-zuma2] ORR 93%; CR 67%; 12-month PFS 61%; FDA approved 2020 for R/R MCL (after ≥2 prior lines including BTK inhibitor); most active option for BTK-refractory MCL; toxicities: CRS grade ≥3 (~15%), ICANS grade ≥3 (~31%)
- Lisocabtagene maraleucel (liso-cel, TRANSCEND-NHL-001): ORR 84%; CR 67% in R/R MCL; FDA approved 2024

**Blastoid/TP53-mutant MCL:**
- Conventional chemotherapy largely ineffective; ibrutinib may have limited activity; consider venetoclax combination, CAR-T as early as possible, allo-SCT for eligible patients; clinical trials prioritized

## Connections

- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — t(11;14)(q13;q32) CCND1-IGH translocation in >95% of MCL → cyclin D1 constitutive overexpression → CDK4/6-RB phosphorylation → cell cycle entry; cyclin D1 IHC positivity distinguishes MCL from CLL, FL, MZL; CDK4/6 inhibitors (palbociclib) + ibrutinib studied in R/R MCL.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — BCL-2 overexpression in MCL cells → apoptosis resistance; venetoclax (BCL-2 inhibitor) ORR ~75% in R/R MCL (AIM trial: ibrutinib+venetoclax); combined ibrutinib+venetoclax achieves complete MRD negativity in ~50% of R/R MCL; BCL-2 inhibition + BTK inhibition is synergistic.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 mutation in blastoid/pleomorphic MCL → most aggressive MCL subtype (TP53 mutations ~80%); TP53-mutant MCL → ibrutinib resistance and dismal prognosis; strategies include venetoclax+BTK, CAR-T, allo-SCT; TP53 del(17p) is the highest-risk molecular feature in MCL.
- `connects-to` → **[ATM](../../03-molecular/atm/README.md)** — ATM deletion/mutation in ~40-50% of MCL (del(11q22.3)) → impaired DNA double-strand break repair → genomic instability; ATM-deficient MCL is more aggressive and shows ibrutinib resistance; PARP inhibitors + BTK inhibitors studied in ATM-mutant MCL; biallelic ATM loss in ~15%.
- `connects-to` → **[BTK](../../03-molecular/btk/README.md)** — BCR-BTK-NF-κB axis is constitutively active in MCL; ibrutinib (FDA 2013 R/R MCL: ORR 68%), zanubrutinib (FDA 2019: ORR 83%), acalabrutinib (FDA 2017: ORR 81%) are approved; BTK C481S (acquired ibrutinib resistance) → pirtobrutinib (non-covalent BTK inhibitor, FDA 2023: ORR 57%).
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB constitutively active in MCL via BCR-BTK → BCL-2, cyclin D1, XIAP → apoptosis resistance and proliferation; bortezomib (↑IκB → ↓NF-κB) active in MCL; BTK inhibitors block NF-κB upstream; NF-κB target MALT1 (CBM complex) active in MCL and under therapeutic investigation.
- `connects-to` → **[CLL](../cll/README.md)** — MCL and CLL are both CD5+ B-cell lymphomas with frequent BM/blood involvement; key distinctions: MCL (cyclin D1+, SOX11+, CD23−, t(11;14)) vs CLL (CD23+, ZAP70+, no cyclin D1); both respond to BTK inhibitors; MCL prognosis worse; different IGHV mutation significance or histology.
- `connects-to` → **[Follicular Lymphoma](../follicular-lymphoma/README.md)** — Mantle cell and follicular lymphoma are both translocation-defined B-cell NHLs but opposites: MCL (t(11;14), cyclin D1) is proliferation-driven and aggressive, FL (t(14;18), BCL-2) indolent and apoptosis-resistant — cyclin D1 vs BCL-2 IHC and SOX11 distinguish them.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — Mantle cell lymphoma arises from a CD5+ naive B cell of the follicular mantle zone (pre-germinal-center): t(11;14) drives cyclin D1, pushing these cells through the cell cycle; unlike FL, most MCL cells are IGHV-unmutated, reflecting their pre-germinal-center origin.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — Mantle cell lymphoma has a distinctive tropism for the GI tract: multiple lymphomatous polyposis studs the small and large bowel with MCL nodules, and occult involvement is so common that many patients have microscopic gut disease even when staging looks limited.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Mantle cell lymphoma spreads widely through the lymphatic system and beyond: it produces generalized lymphadenopathy and characteristically lymphomatous polyposis of the gut, with frequent leukemic blood and marrow involvement, so most patients present at stage IV.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — The spleen is often heavily involved in mantle cell lymphoma, and a leukemic, splenomegalic, SOX11-negative variant exists that mimics chronic lymphocytic leukemia and behaves indolently; splenic and blood involvement reflect MCL's tendency to circulate as a disseminated disease.
- `connects-to` → **[Diffuse Large B-Cell Lymphoma](../dlbcl/README.md)** — Mantle cell lymphoma and DLBCL are both aggressive B-cell lymphomas but distinct: MCL carries cyclin D1/t(11;14) and is incurable-relapsing, while DLBCL is potentially cured by R-CHOP; blastoid MCL can mimic DLBCL morphologically, so cyclin D1/SOX11 staining is decisive.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Mantle cell lymphoma is defined by its pre-germinal-center origin: it arises from naive mantle-zone B cells that have not transited the germinal center, so it usually lacks somatic hypermutation—its hallmark is instead t(11;14) cyclin D1 overexpression.
- `connects-to` → **[Multiple Myeloma](../multiple-myeloma/README.md)** — Mantle cell lymphoma and multiple myeloma are both incurable B-lineage cancers treated with proteasome inhibitors: bortezomib works in both, though MCL is a cyclin-D1-driven nodal lymphoma while myeloma is a marrow plasma-cell tumor secreting monoclonal protein.
- `connects-to` → **[Hodgkin Lymphoma](../hodgkin-lymphoma/README.md)** — Mantle cell and Hodgkin lymphoma sit at opposite ends of B-cell lymphoma outcomes: Hodgkin's Reed-Sternberg-cell disease is usually curable, while MCL is an aggressive yet incurable t(11;14)-driven lymphoma—molecular drivers, not just lineage, set prognosis.
- `connects-to` → **[Burkitt Lymphoma](../burkitt-lymphoma/README.md)** — Mantle cell and Burkitt lymphoma are both aggressive translocation-driven B-cell cancers: MCL's t(11;14) drives cyclin D1, Burkitt's t(8;14) drives MYC—but Burkitt is curable while mantle cell, despite responding initially, relapses and is generally incurable.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Mantle cell lymphoma frequently involves the bone marrow and blood: unlike many lymphomas it is often leukemic at diagnosis, spreading through marrow and the GI tract—so staging includes marrow biopsy, and the widespread disease shapes its aggressive, relapsing course.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — Mantle cell lymphoma runs on the cyclin D1-CDK4-RB axis: overexpressed cyclin D1 inactivates RB to force the cell cycle forward, which is why CDK4/6 inhibitors are being tested—targeting the very pathway that the defining t(11;14) translocation unleashes.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — Mantle cell lymphoma is treated by targeting CD20: this B-cell marker is the target of rituximab, a backbone of MCL therapy alongside BTK inhibitors and BCL-2 blockade—reflecting MCL's identity as a CD5+ mature B-cell lymphoma.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Mantle cell lymphoma has a striking affinity for the gut: it commonly seeds the GI tract as multiple lymphomatous polyposis—numerous lymphoma polyps from stomach to colon—so endoscopic involvement is frequent even when not obviously symptomatic.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Mantle cell lymphoma both exploits and depletes the immune system: it is an aggressive mature B-cell cancer, and its therapies (anti-CD20, BTK inhibitors, chemo) cause profound immunosuppression—so infection is a major cause of morbidity during treatment.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Mantle cell lymphoma is driven through mTOR: cyclin D1 overexpression and PI3K-AKT signaling converge on mTOR to push proliferation, which is why the mTOR inhibitor temsirolimus is an approved therapy for relapsed disease.
- `connects-to` → **[Waldenström Macroglobulinemia](../waldenstrom-macroglobulinemia/README.md)** — Mantle cell lymphoma and Waldenstrom macroglobulinemia are both BTK-dependent B-cell cancers: ibrutinib works in each by blocking B-cell receptor signaling, though they differ in cell of origin and the IgM paraprotein that defines Waldenstrom.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Mantle cell lymphoma is now a CAR-T target: brexucabtagene engineers a patient's cytotoxic T cells to recognize CD19 and kill the lymphoma, achieving durable remissions in disease that has relapsed after chemo and BTK inhibitors.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — Mantle cell lymphoma's overexpressed cyclin D1 partners with CDK4/6: the t(11;14) translocation floods the cell with cyclin D1, which activates CDK4/6 to push past the cell-cycle checkpoint—making CDK4/6 inhibitors like palbociclib a rational target.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Mantle cell lymphoma loves the gut as lymphomatous polyposis: it studs the colon and small bowel with countless lymphoid polyps, so multiple GI polyps that turn out to be lymphoma rather than adenomas are a classic MCL presentation.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Rituximab clears mantle cell lymphoma partly via NK cells: the anti-CD20 antibody tags the malignant B cells for natural killer cells to destroy by antibody-dependent killing, a backbone mechanism of MCL immunochemotherapy.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Mantle cell lymphoma survives on B-cell-receptor calcium signaling: tonic receptor firing drives a BTK-dependent calcium flux that keeps the malignant cells alive, the very pathway ibrutinib interrupts to treat the disease.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Mantle cell lymphoma can invade the brain: especially the aggressive blastoid variant spreads to the central nervous system, a grim relapse site that drives CNS-directed prophylaxis and treatment in high-risk patients.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages support the mantle cell lymphoma niche: tumor-associated macrophages in the nodes and marrow feed the malignant B cells and dampen immunity, and a macrophage-rich tumor tends to carry a worse prognosis.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Mantle cell lymphoma bleeds iron from the gut: its lymphomatous polyposis studs the bowel with tumor nodules that ooze blood, so iron-deficiency anemia is a common sign of GI involvement.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Mantle cell lymphoma infiltrates the liver: as the widespread disease advances, it seeds the liver and spleen, enlarging them as part of the bulky, disseminated stage at diagnosis.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Mantle cell lymphoma leans on regulatory T cells: Tregs in the node and marrow microenvironment dampen the antitumor response, helping the malignant B cells persist and resist immune clearance.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — MCL is staged by imaging and scope: PET/CT photons map the widespread nodal and splenic disease, and endoscopy finds the 'lymphomatous polyposis' studding the bowel.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Aggressive MCL can lyse fast on treatment: dying cells spill phosphate and potassium in tumor lysis, a risk with bulky or blastoid disease starting chemotherapy.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — MCL studs the whole gut: 'multiple lymphomatous polyposis' carpets the stomach and intestines with polyps, a classic presentation found on endoscopy.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows MCL's irregular cell: a small-to-medium lymphocyte with a deeply notched, cleaved nucleus, its overexpressed cyclin D1 — from the t(11;14) translocation — driving relentless division.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — MCL can settle around the eye: ocular adnexal and orbital involvement form a painless mass in the conjunctiva or orbit, one of the extranodal sites this widely-spreading lymphoma reaches.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Aggressive MCL risks tumor lysis: the bulky, fast-dividing blastoid variant, burst by chemotherapy, spills potassium and phosphate into the blood, an electrolyte emergency that can stop the heart.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies both name and treat MCL: nuclear cyclin D1 shown by immunohistochemistry clinches the diagnosis, while the CD20 on the cell surface is the bullseye for rituximab and other anti-CD20 antibody drugs that anchor every regimen.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Marrow and spleen takeover shows in the red cells: as MCL packs the bone marrow and swells the spleen, it crowds out and pools erythrocytes into the anemia that, with the leukemic blood spread common in MCL, marks advanced disease.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — The same takeover drops the platelets: marrow infiltration and splenic sequestration cause thrombocytopenia, and the BTK-inhibitor drugs central to MCL therapy add their own bleeding risk by blunting platelet function.
- `connects-to` → **[Hepatitis B](../hepatitis-b/README.md)** — Anti-CD20 therapy can reactivate hepatitis B: rituximab strips out the B cells that help hold the virus in check, so MCL patients are screened and given antiviral prophylaxis before treatment to prevent a dangerous viral flare.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — Its intensive regimens strain the heart: the anthracycline in R-CHOP and the high-dose cytarabine of induction carry cardiotoxic risk, so cardiac function is checked before the aggressive chemotherapy MCL often demands.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — MCL leans on PI3K-AKT beyond BTK: chronic B-cell-receptor signaling feeds the AKT-mTOR axis, a survival route that drives resistance to BTK inhibitors and is targeted by PI3K and mTOR inhibitors in relapsed disease.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — The bowel is a classic hideout: MCL frequently studs the gastrointestinal lining with lymphomatous polyposis, so even apparently localized disease is often found seeded through the gut epithelium when biopsied, shaping staging and follow-up.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — The lymph-node stroma is a protective niche: fibroblastic reticular and other stromal cells supply survival signals that shelter MCL cells, and part of how BTK inhibitors work is by evicting the lymphoma from this supportive microenvironment into the blood.
- `connects-to` → **[Myelodysplastic Syndromes](../mds/README.md)** — Treatment leaves a later shadow: the intensive chemo and stem-cell transplants used against MCL can damage the marrow, raising the risk of therapy-related myelodysplastic syndromes years afterward — a long-term cost of aggressive cure attempts.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 backs up the survival signal: alongside constitutive NF-κB, JAK-STAT3 activation sustains mantle cell lymphoma and contributes to its resistance to BTK inhibitors, marking another targetable node.
- `connects-to` → **[Cytokine Storm](../cytokine-storm/README.md)** — CAR-T cure can spark a storm: brexucabtagene autoleucel for relapsed mantle cell lymphoma routinely triggers cytokine release syndrome as the engineered cells engage, managed with the IL-6 blocker tocilizumab.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Lymphoma and its therapy clot the veins: bulky mantle cell lymphoma and its chemotherapy raise venous thromboembolism risk, a complication watched for through the disease's aggressive treatment course.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Deep immunosuppression invites infection: the intensive chemoimmunotherapy, BTK inhibitors and CAR-T used against mantle cell lymphoma cause profound neutropenia and B-cell depletion, making febrile neutropenia and sepsis a leading danger.
- `connects-to` → **[Pneumocystis jirovecii](../../../02-pathogen/03-fungi/pneumocystis-jirovecii/README.md)** — B-cell-directed therapy opens the lung to an opportunist: rituximab and BTK-inhibitor treatment of mantle cell lymphoma suppress immunity enough that Pneumocystis pneumonia becomes a risk, prompting prophylaxis.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Marrow infiltration and inflammation lower the count: mantle cell lymphoma commonly involves the bone marrow and raises inflammatory cytokines, producing an anemia of chronic disease on top of any marrow crowding.
- `connects-to` → **[Hepatitis B Virus](../../../02-pathogen/01-viruses/hepatitis-b-virus/README.md)** — Anti-CD20 therapy can reactivate it: the rituximab central to mantle cell lymphoma treatment depletes B cells and can reawaken latent hepatitis B, so screening and antiviral prophylaxis precede therapy.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Its BTK inhibitors invite mold: ibrutinib and related agents used in mantle cell lymphoma are associated with invasive aspergillosis and other fungal infections, a recognized hazard of this targeted therapy.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Its drugs can strain the heart: ibrutinib causes atrial fibrillation and cardiac events, while the anthracyclines and cardiotoxic agents in MCL induction regimens add to the risk of heart failure.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Its chemotherapy injures the nerves: the bortezomib and vincristine used in mantle cell lymphoma regimens cause a dose-limiting peripheral neuropathy with neuropathic pain.
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — Its BTK-inhibitor therapy reawakens shingles: ibrutinib and other agents for mantle cell lymphoma suppress immunity and characteristically reactivate latent varicella-zoster as herpes zoster.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — An aggressive, relapsing lymphoma weighs on mood: the poor prognosis, intensive therapy and recurrent relapses of mantle cell lymphoma contribute to a substantial burden of depression.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its BTK inhibitors strain the heart: ibrutinib used for mantle cell lymphoma causes atrial fibrillation, hypertension and bleeding, the main cardiovascular toxicities of BTK-inhibitor therapy.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — CAR-T and CNS spread reach the brain: mantle cell lymphoma can involve the central nervous system, and the CAR-T cell therapy used for relapsed disease causes immune-effector neurotoxicity (ICANS).
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — An aggressive, incurable, relapsing lymphoma breeds worry: the poor prognosis, intensive therapy and inevitable relapse of mantle cell lymphoma foster chronic health anxiety alongside depression.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It fills the marrow at diagnosis: mantle cell lymphoma almost always involves the bone marrow, causing cytopenias, and the ibrutinib used to treat it commonly causes arthralgia.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Its high tumour burden floods the kidney: the bulky disease of mantle cell lymphoma risks tumour lysis syndrome with acute kidney injury when treatment begins.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It crowds and exposes the chest: mediastinal and pulmonary nodal disease can cause effusions, and the BTK-inhibitor therapy raises the risk of pneumonia and fungal infection.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It can mark the skin: mantle cell lymphoma occasionally infiltrates the skin, and its BTK-inhibitor and chemotherapy treatments cause rashes, bruising and alopecia.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Treatment threatens fertility and sanctuary sites: chemotherapy for mantle cell lymphoma can impair fertility, and the testis can act as a sanctuary site for residual disease.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It can infiltrate endocrine glands: aggressive mantle cell lymphoma occasionally involves the thyroid or adrenal glands, and steroid-containing regimens disturb glucose control.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — BTK inhibition transformed it: BTK inhibitors (ibrutinib, acalabrutinib), the BCL-2 inhibitor venetoclax and CDK4/6 inhibitors against its cyclin-D1 driver are central to modern mantle cell lymphoma care.
- `connects-to` → **[CAR-T](../../../03-medicine/01-modern/13-cancer/car-t/README.md)** — Engineered cells for relapse: brexucabtagene autoleucel, a CD19 CAR-T therapy, achieves durable remissions in mantle cell lymphoma that has relapsed after chemotherapy and BTK inhibitors.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Intensive chemoimmunotherapy upfront: high-dose cytarabine-containing regimens with rituximab, often with autologous transplant, are the chemotherapy backbone for younger patients.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Its targeted drug provokes arrhythmia: the BTK inhibitors that treat mantle cell lymphoma—ibrutinib above all—commonly cause atrial fibrillation through off-target effects on cardiac signalling, so the conduction system is a key toxicity site of MCL therapy.
- `connects-to` → **[ALL](../all/README.md)** — When it turns acute-leukaemia-like: the blastoid and pleomorphic variants of mantle cell lymphoma behave aggressively with a leukaemic phase and CNS spread, resembling acute lymphoblastic leukaemia and demanding similarly intensive, transplant-based treatment.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Largely checkpoint-resistant: unlike Hodgkin lymphoma, mantle cell lymphoma responds poorly to PD-1 inhibitors as monotherapy, so its immunotherapy centres on CD19 CAR-T and bispecific antibodies rather than checkpoint blockade.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — BTK-inhibitor cardiotoxicity: ibrutinib, a mainstay of mantle-cell lymphoma, causes atrial fibrillation, ventricular arrhythmia and cardiomyopathy, so cardiac monitoring accompanies treatment.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Hepatic and splenic infiltration: mantle-cell lymphoma spreads widely, infiltrating the liver's portal tracts and the hepatic lobule along with marrow, spleen and gut.
- `connects-to` → **[PTCL](../ptcl/README.md)** — Aggressive lymphomas, opposite lineages: mantle-cell lymphoma is an aggressive B-cell lymphoma while peripheral T-cell lymphoma is its T-cell counterpart, both hard to cure and often relapsing.
- `connects-to` → **[Immune Thrombocytopenia](../immune-thrombocytopenia/README.md)** — Secondary autoimmune cytopenia: like other low-grade B-cell malignancies, mantle-cell lymphoma can drive antibody-mediated platelet destruction, so a new immune thrombocytopenia in an older adult warrants screening for an underlying lymphoma.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Defenceless against infection: anti-CD20 antibodies and BTK inhibitors used for mantle-cell lymphoma deplete B cells profoundly, causing severe, prolonged COVID-19 and poor vaccine responses in these patients.
- `connects-to` → **[Gout](../gout/README.md)** — Tumour-lysis fallout: bulky or blastoid mantle-cell lymphoma releases a flood of urate when treated, driving acute hyperuricaemia and crystal disease that overlaps with gout and threatens the kidney unless rasburicase is given.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — Recurrent driver: NOTCH1 and NOTCH2 mutations recur in mantle cell lymphoma and mark a more aggressive clinical course, a candidate therapeutic target.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Blastoid transformation: MYC amplification or translocation drives the aggressive blastoid and pleomorphic variants of mantle cell lymphoma, worsening prognosis.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Epigenetic dependence: EZH2 overexpression contributes to mantle cell lymphoma proliferation, an emerging epigenetic vulnerability beyond the defining cyclin D1 lesion.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K dependence: chronic B-cell-receptor signalling activates PI3K in mantle cell lymphoma, sustaining survival and underlying resistance to BTK inhibitors.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Metabolic adaptation: HIF-1α supports the glycolytic metabolism of proliferating mantle cell lymphoma cells in the hypoxic lymph-node and marrow niches.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Nodal angiogenesis: VEGF drives the angiogenesis of involved lymph nodes in mantle cell lymphoma, supporting tumour growth and dissemination.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — Niche homing: CXCL12-CXCR4 signalling anchors mantle cell lymphoma cells in the protective marrow and nodal niche, and BTK inhibitors mobilise them out of it, causing the transient treatment-related lymphocytosis.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — Telomerase immortalisation: TERT activation maintains telomeres in mantle cell lymphoma cells, granting the replicative capacity that complements the cyclin D1 overexpression driving the disease.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Macrophage microenvironment: CCL2 recruits tumour-associated macrophages into the mantle cell lymphoma niche, supporting the malignant B cells and shaping response to therapy.
- `connects-to` → **[Src kinase](../../03-molecular/src-kinase/README.md)** — Src-family kinases such as LYN transduce the chronic-active B-cell-receptor signal upstream of BTK that drives mantle cell lymphoma, the proximal signaling node of the very pathway that BTK inhibitors block further downstream.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — BCL-2 dependency lets mantle cell lymphoma evade caspase-3-mediated apoptosis, the basis for the dramatic activity of the BCL-2 inhibitor venetoclax that restores the cell-death program in this otherwise relapse-prone lymphoma.
- `connects-to` → **[RAD51](../../03-molecular/rad51/README.md)** — Frequent ATM loss in mantle cell lymphoma impairs the DNA-damage response and leaves RAD51-dependent repair under strain, driving the genomic instability that fuels its aggressive, treatment-resistant course.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — CD19 CAR-T (brexucabtagene) and CD20-CD3 bispecific antibodies redirect cytotoxic T cells to kill mantle-cell lymphoma through perforin and granzyme, achieving durable remissions after chemotherapy and BTK inhibitors fail.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Anti-CD20 antibodies (rituximab, obinutuzumab), a backbone of mantle-cell therapy, kill cells partly through complement-dependent cytotoxicity, fixing C3 and the membrane-attack complex on the lymphoma cells.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — The defining t(11;14) places cyclin D1 under the immunoglobulin heavy-chain enhancer, driving its overexpression, while tonic B-cell-receptor signaling sustains the cell—the dependence that BTK inhibitors exploit.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — Overexpressed cyclin D1 (mapped) drives CDK4/6 (mapped) to phosphorylate RB (mapped) and release E2F1, the cell-cycle engine central to mantle cell lymphoma.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A/p16 deletion removes the brake on the cyclin-D1-CDK4/6 axis and marks the blastoid, high-proliferation form of mantle cell lymphoma.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN loss activates PI3K-AKT (PIK3CA, AKT and mTOR already mapped), a survival pathway and a mechanism of resistance to BTK inhibitors in mantle cell lymphoma.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK-STAT3 signaling (STAT3 already mapped) contributes to the survival and microenvironmental support of mantle cell lymphoma.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6 from the tumor microenvironment signals through STAT3 (already mapped) to support the survival of mantle-cell-lymphoma cells, particularly in their protective nodal niches.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2 overexpression provides an alternative route to p53 inactivation (p53 already mapped), cooperating with cyclin-D1 overexpression and ATM loss in mantle cell lymphoma.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — B-cell-receptor signaling through ERK-MAPK provides a proliferative input in mantle cell lymphoma, downstream of the BTK-dependent BCR pathway already mapped.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 supports mantle-cell-lymphoma survival and its interactions with the nodal microenvironment.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-β within the lymph-node microenvironment modulates immune evasion and the stromal niche of mantle cell lymphoma.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the antitumor immune response of mantle cell lymphoma.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β already mapped) normally restrains B-cell proliferation, a brake overridden by the cyclin-D1 translocation of mantle cell lymphoma.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors, restrained by BCR-PI3K-AKT signaling, modulate the survival of the cyclin-D1-driven cells of mantle cell lymphoma.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the cyclin-D1 stability and survival signaling of mantle cell lymphoma.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the inflammatory tumor microenvironment of mantle cell lymphoma.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING modulates the inflammatory and immune microenvironment of mantle cell lymphoma.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of mantle cell lymphoma.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival and drug resistance of mantle cell lymphoma cells, particularly under BTK-inhibitor therapy.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling is recurrently mutated in mantle cell lymphoma, dysregulating its transcriptional program.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of mantle cell lymphoma.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-family chemokine signaling (CXCL12/CXCR4 already mapped) participates in the microenvironment homing of mantle cell lymphoma.
- `connects-to` → **[BAFF](../../03-molecular/baff/README.md)** — BAFF-driven B-cell survival signaling participates in the microenvironment-dependent survival of mantle cell lymphoma.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment of mantle cell lymphoma.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of mantle cell lymphoma.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory microenvironment of mantle cell lymphoma.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling downstream of the B-cell receptor participates in the survival signaling of mantle cell lymphoma.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine (CD39/CD73-adenosine) signaling participates in the immunosuppressive tumor microenvironment of mantle cell lymphoma.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin participates in the microenvironment and stromal interactions of mantle cell lymphoma.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Immunotherapy: MHC class II antigen presentation shapes the T-cell response to mantle cell lymphoma, relevant to the CD19 CAR-T and bispecific-antibody therapies that have transformed treatment of relapsed disease.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — CD19 CAR-T: IL-2-driven T-cell expansion powers the brexucabtagene autoleucel CD19 CAR-T therapy (perforin already mapped) that produces durable remissions in relapsed, BTK-inhibitor-exposed mantle cell lymphoma.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Tumour lysis: the aggressive, high-burden blastoid variant of mantle cell lymphoma is prone to tumour-lysis syndrome on treatment, releasing purines that xanthine oxidase converts to uric acid, managed with allopurinol or rasburicase.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — BTK-inhibitor cardiotoxicity: the BTK inhibitors central to mantle cell lymphoma therapy (BTK already mapped) cause atrial fibrillation and, rarely, ventricular arrhythmia, and troponin elevation marks the myocardial injury of this major class toxicity.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Marrow involvement: bone-marrow infiltration (already mapped) by mantle cell lymphoma and its intensive chemoimmunotherapy lower haemoglobin, the anaemia with other cytopenias marking advanced disease and treatment toxicity.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Tumour-lysis acidosis: the rapid lysis of the high-burden blastoid mantle cell lymphoma by chemotherapy releases acids that, with lactate, produce the metabolic acidosis of tumour-lysis syndrome (urate already mapped).
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive microenvironment: IL-10 in the tumour microenvironment dampens the anti-tumour T-cell response, part of the immune evasion of mantle cell lymphoma that the CD19 CAR-T and bispecific therapies aim to overcome.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Nurse-like stromal support: IL-4 polarises the tumour-associated macrophages toward an M2 phenotype (IL-10 already mapped), the nurse-like cells of the microenvironment that support the survival of the mantle cell lymphoma clone.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Tumour vasculature: nitric oxide with VEGF (already mapped) regulates the vascular tone and angiogenesis of mantle cell lymphoma, part of the supportive stroma of this aggressive lymphoma.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — Splenomegaly: mantle cell lymphoma commonly presents with marked splenomegaly, the spleen and lymph nodes infiltrated by the cyclin-D1-positive (already mapped) clone, and splenic involvement can dominate the leukaemic-variant disease.
- `connects-to` → **[T-cytotoxic cell](../../04-cellular/t-cytotoxic-cell/README.md)** — CAR-T immunotherapy: the cytotoxic T cells — engineered as CD19 CAR-T (brexucabtagene; perforin already mapped) — achieve deep remissions in relapsed mantle cell lymphoma that has failed BTK inhibition.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Tumour-lysis hypocalcaemia: the bulky, proliferative mantle cell lymphoma treated with intensive therapy can trigger tumour-lysis syndrome (xanthine oxidase already mapped), the hyperphosphataemia complexing calcium to cause hypocalcaemia.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — M2 stromal arm: IL-13, with IL-4 (already mapped), drives the M2 macrophage arm of the immunosuppressive microenvironment of mantle cell lymphoma.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Marrow-adipocyte adipokine: leptin from the marrow adipose tissue of the bone-marrow (already mapped) microenvironment signals to the mantle cell lymphoma cells, part of its metabolic niche crosstalk.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Adipokine microenvironment: adiponectin, with leptin (already mapped), from the marrow adipose tissue signals within the metabolic microenvironment of mantle cell lymphoma.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipokine microenvironment: resistin, with leptin and adiponectin (already mapped), completes the marrow-adipocyte adipokine signalling of the microenvironment of mantle cell lymphoma.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — ADCC effectors: the NK cells mediate the antibody-dependent cellular cytotoxicity of the anti-CD20 (already mapped) rituximab against the mantle cell lymphoma B cells (already mapped).
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate antitumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment relevant to the immunotherapy of mantle cell lymphoma.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the T and NK (already mapped) cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity, relevant to the CD19 CAR-T immunotherapy of mantle cell lymphoma.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of mantle cell lymphoma.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of mantle cell lymphoma.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the mantle-cell-lymphoma microenvironment.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the mantle-cell-lymphoma microenvironment.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of mantle cell lymphoma.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Rituximab CDC: the complement C5 (with C3 already mapped) is the effector of the complement-dependent cytotoxicity by which the anti-CD20 (already mapped) rituximab kills the mantle-cell-lymphoma B cells (already mapped).
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling links the complement (C3 and C5 already mapped) to the myeloid inflammation of the mantle-cell-lymphoma microenvironment.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement evasion: the mantle-cell-lymphoma cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), a resistance mechanism to the anti-CD20 complement-dependent killing.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Lymph node stroma alarmin: TSLP from lymph-node stromal cells activates the dendritic cells and B cells of the mantle zone, promoting the BCR survival signalling and NF-kB-mediated apoptosis resistance that drive the aggressive expansion of mantle-cell lymphoma.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Chemoimmunotherapy anaemia: erythropoietin counters the myelosuppression induced by the RCHOP and bendamustine-rituximab regimens used in MCL; EPO-stimulating agents are a standard supportive measure to maintain haemoglobin and treatment tolerance in mantle-cell lymphoma.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Lymphoma dissemination: bradykinin promotes vascular permeability and transendothelial migration of MCL cells, facilitating the aggressive dissemination into peripheral blood, marrow, and extranodal sites that characterise the blastoid variant of mantle-cell lymphoma.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — C1-INH complement regulation: C1-INH modulates the classical pathway (C3, C5 and C5aR1 already mapped) activated by anti-CD20 (CD20 already mapped) therapies in MCL, balancing rituximab complement-dependent cytotoxicity and minimising complement-mediated adverse effects.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell mediator in MCL stroma: histamine from mast cells (already mapped) in the MCL stroma promotes VEGF-driven (already mapped) angiogenesis and immunosuppression, while H2-receptor signalling on MCL B cells (already mapped) reduces cAMP-mediated apoptosis.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Lymphoma-niche periostin: periostin, secreted by cancer-associated fibroblasts (already mapped) in the MCL stroma under TGF-β (already mapped) stimulation, reinforces the lymphoma niche and promotes the B-cell (already mapped) proliferative advantage in mantle-cell lymphoma.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian lymphoma regulation: melatonin, via MT1/MT2 receptors on MCL B cells and tumour-associated macrophages (already mapped), suppresses cyclin D1-driven (already mapped) cell-cycle progression and NF-κB (already mapped) anti-apoptotic signalling in mantle-cell lymphoma.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Androgen-B-cell axis: testosterone, via androgen receptor on MCL B cells (already mapped), suppresses anti-tumour immune surveillance and modulates the NF-κB (already mapped) and cyclin D1-overexpressing (already mapped) proliferative programme of mantle-cell lymphoma.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Tumour-microenvironment 5-HT: serotonin released from activated platelets (already mapped) in the MCL vasculature binds 5-HT2 receptors on MCL B cells and macrophages (already mapped), modulating pro-tumour NF-κB (already mapped) inflammation in mantle-cell lymphoma.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — MCL prolactin B-cell: prolactin, via PRLR on MCL B cells (already mapped) and tumour-associated macrophages (already mapped), upregulates NF-κB (already mapped) and IL-6 (already mapped) pro-survival signalling, promoting the immunosuppressive TME of mantle-cell lymphoma.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — MCL oxytocin anti-tumour: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped) in the MCL stroma, attenuates the NF-κB (already mapped) and IL-6 (already mapped) pro-tumour immune cascade in mantle-cell lymphoma.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — MCL vasopressin vascular: vasopressin, via V1aR on macrophages (already mapped) and mast cells (already mapped) in the MCL stroma, modulates the vascular niche; dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) pro-tumour signalling in mantle-cell lymphoma.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — MCL selenium: selenium, as GPx in macrophages (already mapped) and T-cytotoxic cells (already mapped), scavenges ROS; selenium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) oxidative B-cell (already mapped) tumour cascade of mantle-cell lymphoma.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — MCL iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) polarisation and T-cytotoxic (already mapped) immune activation; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of mantle-cell lymphoma.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — MCL sodium: high dietary sodium promotes macrophage (already mapped) and mast-cell (already mapped) activation; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) skewing amplifies the B-cell (already mapped) tumour cascade of mantle-cell lymphoma.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — MCL magnesium: magnesium cofactors kinase signalling in macrophages (already mapped) and B-cells (already mapped); magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and mast-cell (already mapped) tumour cascade of mantle-cell lymphoma.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — MCL copper: copper, via SOD1 in macrophages (already mapped) and T-cytotoxic cells (already mapped), scavenges ROS; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and B-cell (already mapped) tumour cascade of mantle-cell lymphoma.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — MCL zinc: zinc, as cofactor of antioxidant enzymes in macrophages (already mapped) and T-cytotoxic cells (already mapped), attenuates oxidative stress; zinc deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and B-cell (already mapped) cascade of MCL.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — MCL carbon: carbon as backbone of cyclin-D1 (already mapped) and BTK protein scaffold sustains B-cell (already mapped) mantle-zone proliferation; carbon depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCL-2 (already mapped) lymphoma cascade of MCL.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — MCL chloride: chloride regulates B-cell (already mapped) and macrophage (already mapped) ion homeostasis; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCL-2 (already mapped) protumorigenic microenvironment of mantle-cell lymphoma.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — MCL nitrogen: nitrogen in amino-acid scaffold of cyclin-D1 (already mapped) and BTK proteins sustains B-cell (already mapped) proliferation; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of mantle-cell lymphoma.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — MCL hydrogen: hydrogen in redox chemistry of B-cells (already mapped) and macrophages (already mapped) modulates cyclin-D1 (already mapped) stability; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCL-2 (already mapped) cascade of MCL.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — MCL oxygen: oxygen supports aerobic metabolism in B-cells (already mapped) and macrophages (already mapped) for cyclin-D1 (already mapped) signalling; oxygen deficit amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCL-2 (already mapped) cascade of MCL.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — MCL sulfur: sulfur in cysteine residues of BTK and NF-κB (already mapped) proteins sustains B-cell (already mapped) signalling; sulfur dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCL-2 (already mapped) cascade of mantle-cell lymphoma.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — MCL pd-1: PD-1 on T-cytotoxic cells (already mapped) and macrophages (already mapped) modulates lymphoma immune evasion; pd-1 dysregulation amplifies smad4 (already mapped) and vegf (already mapped) and il-2 (already mapped) B-cell lymphoma cascade of MCL.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — MCL glp-1: GLP-1 from macrophages (already mapped) and natural killer cells (already mapped) modulates metabolic-inflammatory tone; glp-1 dysfunction amplifies smad4 (already mapped) and vegf (already mapped) and il-2 (already mapped) cascade of mantle cell lymphoma.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — MCL angiotensin-ii: angiotensin-II from macrophages (already mapped) and fibroblasts (already mapped) drives tumour vascular remodelling; angiotensin-ii excess amplifies smad4 (already mapped) and vegf (already mapped) and il-2 (already mapped) cascade of MCL.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^wang-2013-ibrutinib-mcl]: Wang ML, Rule S, Martin P, et al. Targeting BTK with ibrutinib in relapsed or refractory mantle-cell lymphoma. *N Engl J Med.* 2013;369(6):507-516. [doi:10.1056/NEJMoa1306220](https://doi.org/10.1056/NEJMoa1306220) · [PubMed 23782157](https://pubmed.ncbi.nlm.nih.gov/23782157/)
[^wang-2020-brexu-zuma2]: Wang M, Munoz J, Goy A, et al. KTE-X19 CAR T-cell therapy in relapsed or refractory mantle-cell lymphoma. *N Engl J Med.* 2020;382(14):1331-1342. [doi:10.1056/NEJMoa1914347](https://doi.org/10.1056/NEJMoa1914347) · [PubMed 32242358](https://pubmed.ncbi.nlm.nih.gov/32242358/)
