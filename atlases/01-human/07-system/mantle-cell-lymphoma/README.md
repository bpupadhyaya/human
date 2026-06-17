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

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^wang-2013-ibrutinib-mcl]: Wang ML, Rule S, Martin P, et al. Targeting BTK with ibrutinib in relapsed or refractory mantle-cell lymphoma. *N Engl J Med.* 2013;369(6):507-516. [doi:10.1056/NEJMoa1306220](https://doi.org/10.1056/NEJMoa1306220) · [PubMed 23782157](https://pubmed.ncbi.nlm.nih.gov/23782157/)
[^wang-2020-brexu-zuma2]: Wang M, Munoz J, Goy A, et al. KTE-X19 CAR T-cell therapy in relapsed or refractory mantle-cell lymphoma. *N Engl J Med.* 2020;382(14):1331-1342. [doi:10.1056/NEJMoa1914347](https://doi.org/10.1056/NEJMoa1914347) · [PubMed 32242358](https://pubmed.ncbi.nlm.nih.gov/32242358/)
