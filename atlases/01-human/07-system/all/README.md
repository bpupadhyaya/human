---
schema: human-scale-entry/v1
id: all
name: Acute Lymphoblastic Leukemia
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "ALL is a lymphoid progenitor malignancy; B-ALL ~85% (ETV6-RUNX1 t(12;21) ~25% pediatric; BCR-ABL1 Ph+ ~25% adult; Ph-like ~15%); T-ALL ~15% (NOTCH1 ~60%); overall pediatric 5-year OS >90%; adult OS ~40-50%."
aliases: ["ALL", "acute lymphoblastic leukemia", "acute lymphocytic leukemia", "B-ALL", "T-ALL", "Ph+ ALL", "Ph-like ALL", "pediatric leukemia", "ETV6-RUNX1 ALL", "BCR-ABL1 ALL"]
sources:
  - id: pui-2018-all-cure
    type: peer-reviewed
    cite: "Pui CH, Yang JJ, Bhakta N, et al. Global efforts toward the cure of childhood acute lymphoblastic leukemia. Lancet Child Adolesc Health. 2018;2(6):440-454."
    doi: "10.1016/S2352-4642(18)30066-X"
    pmid: "29976322"
    url: "https://doi.org/10.1016/S2352-4642(18)30066-X"
  - id: maude-2018-tisagenlecleucel
    type: peer-reviewed
    cite: "Maude SL, Laetsch TW, Buechner J, et al. Tisagenlecleucel in children and young adults with B-cell lymphoblastic leukemia. N Engl J Med. 2018;378(5):439-448."
    doi: "10.1056/NEJMoa1709866"
    pmid: "29385370"
    url: "https://doi.org/10.1056/NEJMoa1709866"
cross_links:
  - target: 01-human/03-molecular/runx1
    relation: connects-to
    note: "ETV6-RUNX1 t(12;21) is the most common translocation in childhood ALL (~25%); RUNX1-RUNX1T1 t(8;21) defines CBF-AML; germline RUNX1 mutations (FPD) confer ~35-40% AML risk; RUNX1 controls lymphoid/myeloid lineage fate decisions."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "NOTCH1 activating mutations occur in ~60% of T-ALL; NOTCH1 drives T-cell progenitor proliferation and blocks differentiation; gamma-secretase inhibitors suppress NOTCH1 in T-ALL preclinically; ETP-ALL has low NOTCH1 mutation frequency."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "BCL-2 overexpression contributes to chemotherapy resistance in B-ALL; venetoclax (BCL-2 inhibitor) shows activity in relapsed/refractory B-ALL in early trials; Ph+ ALL and Ph-like ALL show BCL-2 dependence amenable to venetoclax combinations."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "PD-1/PD-L1 expression is upregulated in relapsed ALL and post-CAR-T failure; pembrolizumab studied for ALL after blinatumomab failure; checkpoint inhibition is investigated to prevent CAR-T exhaustion and enhance blinatumomab activity."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "B-ALL arises from arrested B-cell lymphoid progenitors; CD19+/CD10+/TdT+ immunophenotype defines most B-ALL; CD19 is exploited by tisagenlecleucel (CAR-T; 81% remission in ELIANA) and blinatumomab (CD19×CD3 BiTE); B-cell lineage markers determine eligibility for immunotherapy."
  - target: 01-human/03-molecular/abl1
    relation: connects-to
    note: "BCR-ABL1 t(9;22) → p190 BCR-ABL1 in ~25% adult ALL and ~3-5% pediatric ALL; Ph+ ALL requires TKI (dasatinib or ponatinib) from Day 1; blinatumomab+dasatinib is emerging as a chemotherapy-free regimen; allo-SCT deferred if MRD-negative on TKI."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "T-ALL arises from T-cell progenitor arrest at DN-DP transition; CD7+/cytoplasmic CD3+/TdT+ immunophenotype; NOTCH1 governs T-cell lineage commitment and is mutated in ~60% of T-ALL; nelarabine (T-cell-specific purine analog) is active in T-ALL relapse."
  - target: 01-human/07-system/aplastic-anemia
    relation: connects-to
    note: "ALL and aplastic anemia both present with pancytopenia and a failing marrow but are opposites in mechanism: AA an empty marrow from T-cell destruction of stem cells, ALL a marrow packed with lymphoblasts — so the marrow biopsy (hypocellular vs blast-replaced) distinguishes them."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "ALL arises in the bone marrow from a transformed lymphoid progenitor whose blasts crowd out normal hematopoiesis, causing the anemia, thrombocytopenia, and neutropenia at presentation; marrow with ≥20% lymphoblasts is diagnostic, and marrow MRD after induction guides prognosis."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "ALL and AML are the two acute leukemias — both blast-crisis marrow failure, but ALL from lymphoid and AML from myeloid progenitors; flow cytometry (TdT, CD19/CD10 vs MPO, CD33) separates them, and the distinction dictates entirely different chemotherapy backbones."
  - target: 01-human/07-system/cml
    relation: connects-to
    note: "ALL and CML intersect at the Philadelphia chromosome: BCR-ABL1 defines CML and ~25% of adult B-ALL (Ph+ ALL), the highest-risk subtype, so both use ABL tyrosine-kinase inhibitors (imatinib, dasatinib, ponatinib); a CML blast crisis can present as acute lymphoblastic leukemia."
  - target: 01-human/07-system/burkitt-lymphoma
    relation: connects-to
    note: "Mature B-cell ALL is biologically Burkitt leukemia: it shares the MYC t(8;14), starry-sky morphology and explosive growth of Burkitt lymphoma, presenting as a leukemic phase rather than a mass, and both are cured by short, intensive, CNS-directed chemo not standard ALL regimens."
  - target: 01-human/06-organ/thymus
    relation: connects-to
    note: "T-cell ALL arises in the thymus: malignant transformation of developing thymocytes (often via NOTCH1) produces a mediastinal thymic mass with airway/SVC compression at presentation, distinguishing it from marrow-based B-ALL and reflecting the thymus's role in T-cell development."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Acute lymphoblastic leukemia is the paradigm cancer for cytotoxic T-cell therapy: CD19-directed CAR-T cells reprogram cytotoxic T cells to kill the leukemic B lymphoblasts, achieving deep remissions in relapsed B-ALL—the first CAR-T approval (tisagenlecleucel)."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Radiation has a defined role in acute lymphoblastic leukemia: cranial irradiation once prevented CNS relapse (now mostly replaced by intrathecal chemo to spare neurocognition), and total-body irradiation conditions the marrow before allogeneic transplant in high-risk disease."
  - target: 01-human/07-system/dlbcl
    relation: connects-to
    note: "Acute lymphoblastic leukemia and diffuse large B-cell lymphoma are aggressive B-cell cancers at opposite ends of maturation: ALL is a precursor-lymphoblast malignancy of children on prolonged multi-agent chemo, while DLBCL is a mature B-cell tumor of adults cured by R-CHOP."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Acute lymphoblastic leukemia crowds out platelet production: leukemic blasts fill the marrow and suppress megakaryocytes, so thrombocytopenia causes bruising and bleeding—one of the cytopenias, with anemia and neutropenia, that signals marrow takeover at diagnosis."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "The brain is a sanctuary site in acute lymphoblastic leukemia: blasts hide in the CNS where systemic chemo penetrates poorly, so untreated patients relapse in the meninges—why ALL therapy routinely includes intrathecal chemotherapy and sometimes cranial radiation."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "Acute lymphoblastic leukemia infiltrates the spleen and liver: circulating blasts lodge in these organs causing hepatosplenomegaly, a common presenting sign along with lymphadenopathy—reflecting how a marrow cancer spills into the lymphoid filtering organs."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "CD20 is a target in B-lineage ALL: adding the anti-CD20 antibody rituximab to chemotherapy improves outcomes in CD20-positive B-ALL, complementing the CD19- and CD22-directed immunotherapies (blinatumomab, CAR-T) that have transformed treatment."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "ALL crowds out normal blood production: leukemic blasts pack the marrow and suppress red-cell, neutrophil and platelet formation, so anemia, infection and bleeding—not the leukemia itself—are how acute lymphoblastic leukemia usually first presents."
  - target: 01-human/07-system/pcnsl
    relation: connects-to
    note: "ALL has a special tropism for the central nervous system: leukemic cells seed the meninges as a sanctuary site beyond most chemotherapy, so CNS-directed prophylaxis (intrathecal drugs) is essential—unlike PCNSL, a distinct lymphoma confined to the brain."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "ALL endangers patients through the neutrophil: leukemic blasts crowd the marrow and chemotherapy wipes out neutrophils, so profound neutropenia leaves children and adults dangerously prone to life-threatening infection during treatment."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "ALL can be the first sign of a cancer-predisposition syndrome: germline TP53 mutations (Li-Fraumeni) and other inherited defects raise leukemia risk, so ALL in a child with a strong family cancer history prompts genetic evaluation."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "ALL has been transformed by harnessing the immune system: CD19 CAR-T cells and the bispecific blinatumomab redirect the patient's T cells to kill B-lymphoblasts, rescuing relapsed B-ALL—among the first triumphs of cellular immunotherapy."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Treating ALL can crash the kidneys via tumor lysis: rapid leukemic-cell breakdown floods the blood with potassium, phosphate and urate that precipitate in the kidney, so hydration and rasburicase guard against this acute kidney injury."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "The testis is a sanctuary where ALL hides: the blood-testis barrier shields leukemic cells from chemotherapy, so the testis (like the CNS) is a site of relapse that requires dedicated treatment and monitoring in boys."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Natural killer cells help control ALL after transplant: donor NK cells mount a graft-versus-leukemia effect against residual blasts, and NK-based and CAR therapies are being developed to harness this innate killing."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: connects-to
    note: "Steroids are a cornerstone of ALL treatment through the glucocorticoid receptor: when activated, it triggers apoptosis in lymphoblasts, so every regimen leans on it—and resistance to this signal predicts a worse outcome."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "ALL can crash blood calcium through tumor lysis: as chemotherapy bursts huge numbers of blasts, released phosphate binds calcium and potassium and uric acid surge, a metabolic emergency that threatens the heart and kidneys."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "ALL and its therapy both burden the liver: leukemic cells infiltrate it to cause hepatomegaly, while drugs like asparaginase and methotrexate are hepatotoxic, so liver function is watched throughout the long treatment course."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "ALL treatment can scar the heart: the anthracycline chemotherapy central to cure is cardiotoxic, weakening the heart muscle, so cardiac function is watched for years—an important late effect in children cured of leukemia."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "ALL hides behind regulatory T cells: the leukemia expands these immune suppressors that blunt the antileukemic response, a barrier that immunotherapies like CAR-T and bispecific antibodies must overcome."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "ALL's tumor lysis floods the blood with potassium: when chemotherapy bursts masses of blasts, potassium pours out of the dying cells, and the resulting hyperkalemia can stop the heart if not urgently managed."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "ALL's tumor lysis spills phosphate too: dying blasts release phosphorus that binds calcium and crashes it, while precipitating in the kidneys, part of the metabolic emergency of starting chemotherapy."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "ALL hides in the eye: like the brain, the eye is a sanctuary the bloodstream's chemotherapy reaches poorly, so leukemic infiltration there can seed relapse and is checked in high-risk disease."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "A MYC translocation defines the most aggressive B-ALL: mature B-cell (Burkitt-type) leukemia is driven by MYC switched on next to an antibody gene, demanding intensive, lymphoma-style treatment."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy distinguishes ALL's blast: a lymphoblast with a high nucleus-to-cytoplasm ratio, condensed chromatin, and scant organelles — and, crucially, none of the Auer rods that mark the myeloid leukemias."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Leukemia can settle in the skin: ALL blasts infiltrate it as leukemia cutis, firm violet nodules or plaques, an uncommon but telling sign that the disease has spilled beyond the blood and marrow."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Treating ALL convulses the body's chemistry: as chemotherapy bursts the huge mass of blasts in tumor lysis syndrome, magnesium and other electrolytes swing wildly, demanding close monitoring and correction to protect the heart and kidneys."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "ALL hides in and harms the nervous system: leukemic cells seed the CNS as a sanctuary, demanding intrathecal chemotherapy, while vincristine in the regimen poisons peripheral neurons into a dose-limiting neuropathy."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Engineered antibodies transformed ALL: blinatumomab, a bispecific that yokes T cells to CD19, and the CD22 drug-conjugate inotuzumab now clear relapsed disease that chemotherapy alone could not."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "A signature ALL drug inflames the pancreas: asparaginase, key to pediatric regimens, can trigger acute pancreatitis and disturb blood sugar, a toxicity watched for throughout treatment."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "ALL often announces itself in the bones: marrow packed with blasts causes the bone and joint pain that can mimic arthritis in a child, while the high-dose steroids of treatment later bring avascular necrosis and myopathy."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "The long chemotherapy is hard on the liver: methotrexate, 6-mercaptopurine, and asparaginase all injure hepatocytes, so transaminases and bilirubin are tracked across the months-to-years of ALL maintenance therapy."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "Steroids are core to the cure and suppress the adrenal: the prolonged high-dose glucocorticoids central to ALL regimens shut down the adrenal axis, so withdrawal must be gradual and stress dosing considered during illness."
  - target: 01-human/07-system/gvhd
    relation: connects-to
    note: "Transplant trades one risk for another: high-risk ALL is cured by allogeneic stem-cell transplant, whose graft-versus-leukemia effect helps clear the disease but brings graft-versus-host disease as its dangerous price."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Growth signaling fuels the leukemic cell: the PI3K-AKT-mTOR pathway is often hyperactive in ALL, driving proliferation and survival, so mTOR inhibitors are studied to resensitize resistant disease."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "The marrow's macrophages shelter the leukemia: tumor-associated macrophages in the niche support blast survival and resistance, and they also mediate the cytokine release that complicates CAR-T and blinatumomab therapy."
---

# Acute Lymphoblastic Leukemia

## Overview

**Acute lymphoblastic leukemia (ALL)** is a malignancy of lymphoid progenitor cells arrested at early stages of B-cell or T-cell differentiation, characterized by clonal expansion of lymphoblasts in bone marrow, peripheral blood, and extramedullary sites (CNS, testes, lymph nodes). ALL is the most common cancer in children (peak age 2-5 years) and a biologically distinct disease in adults. **B-ALL comprises ~85%** of cases; **T-ALL comprises ~15%**. Pediatric ALL represents one of oncology's major success stories: overall 5-year OS exceeds **90%** in high-income countries for children [^pui-2018-all-cure]. Adult ALL carries substantially worse prognosis (5-year OS ~40-50%) due to adverse cytogenetics, higher BCR-ABL1 frequency (~25%), and reduced treatment tolerance. Modern ALL management integrates **cytogenetic/molecular risk stratification**, **MRD (minimal residual disease) monitoring**, and immunotherapies including **blinatumomab** (CD19×CD3 BiTE) and **tisagenlecleucel** (CD19 CAR-T) for relapsed/refractory disease [^maude-2018-tisagenlecleucel].

**Epidemiology:**
- Incidence: ~6,500 ALL cases/year in USA; ~3,500 in children (<20 years)
- B-ALL: bimodal age distribution (peak 2-5 years; second peak >50 years)
- T-ALL: median age ~15 years (adolescent/young adult predominance); M:F ~3:1
- Down syndrome: ~10-20× elevated ALL risk (often ETV6-RUNX1 or hyperdiploidy)
- Race: higher incidence in Hispanic children; worse outcomes historically; now largely equalized with risk-adapted therapy

## Structure

### B-ALL cytogenetic/molecular subtypes

**Favorable-risk:**
- **ETV6-RUNX1 (t(12;21)(p13;q22), ~25% pediatric B-ALL):** Cryptic translocation (not visible on karyotype); requires FISH or RT-PCR; pre-B immunophenotype (CD19+, CD10+, TdT+); 5-year EFS ~90-95%; sensitive to L-asparaginase; late relapses from persisting pre-leukemic clone possible (years after therapy cessation); the ETV6-RUNX1 fusion is the initiating hit in utero but requires additional mutations for overt leukemia
- **High hyperdiploidy (>50 chromosomes, ~25% pediatric B-ALL):** Extra chromosomes 4, 10, 17, 21 (X4+10+17 = very favorable); 5-year EFS ~85-90%; excellent response to antimetabolites (methotrexate, 6-MP); hyperdiploid DNA index correlates with outcome
- **iAMP21 (intrachromosomal amplification chromosome 21, ~2%):** Multiple extra copies of RUNX1; intermediate-risk; treated on high-risk protocols

**Intermediate/High-risk:**
- **BCR-ABL1 (Ph+ ALL, t(9;22)(q34;q11), ~3-5% pediatric, ~25% adult B-ALL):** p190 BCR-ABL1 in most (vs. p210 in CML); treated with TKI (dasatinib, ponatinib) + chemotherapy; allo-SCT deferred if MRD-negative with TKI; 5-year OS ~60-70% (children), ~40-50% (adults); blinatumomab+dasatinib emerging as chemotherapy-free regimen
- **BCR-ABL1-like (Ph-like, ~15% pediatric, ~20-25% adult B-ALL):** Gene expression profile resembling Ph+ ALL but lacking BCR-ABL1 fusion; harbors CRLF2 rearrangements (~50%), JAK2 rearrangements (~10%), EPOR rearrangements, PDGFRB fusions (~10%), ABL-class fusions (~10%); ruxolitinib (CRLF2/JAK2), dasatinib (ABL-class) added to backbone; adverse prognosis without targeted therapy
- **KMT2A rearrangements (MLL, 11q23, ~5% overall; ~75% infant ALL):** t(4;11) most common in adults; t(9;11) in infants; infant ALL: 5-year OS ~25-40%; sensitive to venetoclax+chemotherapy; MENIN inhibitors (revumenib) emerging for KMT2A-r AML/ALL
- **Hypodiploidy (<44 chromosomes, ~2%):** Near-haploid (24-31) or low-hypodiploid (32-39); TP53 germline mutations in ~50% low-hypodiploid; 5-year OS ~25-30%; allo-SCT in CR1
- **DUX4 rearrangements (~5%):** Favorable prognosis; CD2+ atypical immunophenotype; ERG overexpression

### T-ALL molecular subtypes

**NOTCH1/FBXW7:**
- NOTCH1 activating mutations: ~60% T-ALL (heterodimerization domain or PEST domain)
- FBXW7 inactivating mutations: ~15% T-ALL → impairs NOTCH1 degradation → prolonged NOTCH1 signaling
- NOTCH1+FBXW7 co-mutation: ~70-75% T-ALL combined; independently favorable within T-ALL

**Early T-cell Precursor ALL (ETP-ALL, ~15% T-ALL):**
- Immature immunophenotype: CD1a−, CD8−, CD5 dim, CD34+, CD117+, myeloid markers+
- Molecular overlap with AML: FLT3, RAS, IDH1/IDH2 mutations
- High-risk T-ALL; historically poor outcomes; responds to nelarabine-containing regimens

**Other T-ALL molecular features:**
- CDKN2A/2B deletion: ~70% T-ALL
- TAL1 rearrangements: ~20%; HOXA deregulation: ~25%; TLX1/3 overexpression: ~10-25%
- PTEN deletions: ~15%; JAK mutations (JAKSTAT): ~10-15%

### Immunophenotype

| Marker | B-ALL | T-ALL |
|--------|-------|-------|
| CD19 | + (nearly all) | − |
| CD10 (CALLA) | + (most pre-B) | − |
| TdT | + | + |
| CD3 (cytoplasmic) | − | + |
| CD7 | − | + (all) |
| CD34 | Variable | Variable (ETP+) |
| MPO | − | − |

## Function

### Normal lymphoid progenitor biology

**B-cell development:**
Common lymphoid progenitor (CLP) → Pro-B (D-J rearrangement, RAG1/2) → Pre-B (V-DJ rearrangement, μ heavy chain, IL-7 signaling via JAK1/JAK3) → Immature B (light chain rearrangement, BCR expression) → Mature naive B. B-ALL is arrested at Pro-B (early precursor B-ALL) or Pre-B stage. ETV6-RUNX1 blocks pro-B to pre-B transition; BCR-ABL1 blocks pre-B to immature B. Key transcription factors: PAX5 (B-cell commitment), EBF1, IKZF1 (Ikaros).

**T-cell development:**
CLP → ETP (early T-cell precursor) → DN (double negative, CD4−CD8−) → DP (double positive, CD4+CD8+) → CD4 or CD8 SP (single positive). T-ALL arises from DN to DP transition. NOTCH1 governs T-cell lineage commitment; gamma-secretase cleaves NOTCH1 intracellular domain → nuclear → HES1, MYC target activation → T-cell progenitor proliferation. ETP-ALL arrested at DN1-2 stage.

## Pathology

### Clinical presentation and diagnosis

**Symptoms:** Bone marrow failure (anemia, thrombocytopenia, neutropenia); bone pain (periosteal infiltration); lymphadenopathy, hepatosplenomegaly; mediastinal mass (T-ALL — superior vena cava syndrome); CNS (headache, cranial nerve palsy); testicular ALL (painless enlargement).

**Diagnosis:**
- Bone marrow aspiration: ≥20% lymphoblasts by WHO 2022 criteria (≥25% older criteria)
- Morphology: L1 (small uniform) or L2 (large pleomorphic) by FAB; less used now
- Immunophenotyping (flow cytometry): lineage assignment; minimal residual disease (MRD) monitoring
- Cytogenetics (karyotype + FISH): t(12;21), t(9;22), t(4;11), hyperdiploidy, hypodiploidy
- Molecular: RT-PCR for BCR-ABL1; NGS for IKZF1, CRLF2, JAK2, NOTCH1, FLT3, RAS
- CSF analysis: CNS1 (no blasts), CNS2 (<5 WBC + blasts), CNS3 (≥5 WBC + blasts or cranial nerve palsy)

### Risk stratification (NCI/COG system)

**NCI standard risk (SR):** Age 1-9.99 years AND WBC <50×10⁹/L at diagnosis (B-ALL only)
**NCI high risk (HR):** Age ≥10 years OR WBC ≥50×10⁹/L (B-ALL); all T-ALL

**Molecular risk modifiers:**
- ETV6-RUNX1, high hyperdiploidy → very favorable (de-intensification eligible)
- IKZF1 deletion ("Ikarus deletion") → adverse (independent of other features)
- BCR-ABL1 → TKI required; allo-SCT if MRD+
- Ph-like → TKI addition investigational
- Hypodiploidy, KMT2A-r → very high risk → allo-SCT in CR1
- MRD Day 29: negative (<0.01%) → favorable; positive → high-risk intensification

### Treatment

**Induction (4-6 weeks):** Vincristine + dexamethasone + L-asparaginase ± anthracycline (daunorubicin); CR rate ~95-99% in children; ~80-85% in adults; TKI added from Day 1 for Ph+ ALL.

**CNS prophylaxis/treatment:** Intrathecal methotrexate (IT-MTX) at diagnosis and throughout; high-dose systemic MTX (HDMTX); CNS radiation reserved for CNS3 or high-risk CNS disease only (risk of neurocognitive sequelae).

**Consolidation/maintenance:** HDMTX consolidation cycles; 6-mercaptopurine (daily); MTX (weekly); L-asparaginase (PEG-asparaginase); pulses of vincristine+steroids; total duration ~2-3 years (males) or ~2 years (females).

**Targeted therapy:**
- **Dasatinib or ponatinib** for Ph+ ALL (TKI + chemotherapy or TKI + blinatumomab)
- **Ruxolitinib** (JAK1/2) for CRLF2/JAK2-rearranged Ph-like ALL
- **Nelarabine** (T-ALL specific purine nucleoside analog; neurotoxicity dose-limiting)
- **Venetoclax** combinations: emerging for KMT2A-r, Ph-like, relapsed B-ALL

**Relapsed/Refractory:**
- **Blinatumomab (Blincyto):** CD19×CD3 bispecific T-cell engager; continuous IV infusion; TOWER trial (adults): CR 39% vs 13%, OS 7.7 vs 4.0 months (FDA 2017 adult R/R B-ALL); pediatric R/R B-ALL: CR ~39%; MRD-negative CR ~76% in MRD+ setting; cytokine release syndrome (CRS), neurologic toxicity
- **Tisagenlecleucel (Kymriah):** Autologous CD19 CAR-T; ELIANA trial: remission rate 81%, 12-month EFS 50%, 12-month OS 76% (FDA 2017 pediatric/young adult R/R B-ALL) [^maude-2018-tisagenlecleucel]; CRS + immune effector cell-associated neurotoxicity syndrome (ICANS)
- **Inotuzumab ozogamicin (Besylomab):** Anti-CD22 ADC (calicheamicin); INO-VATION trial: CR/CRi 80.7% vs 29.4%; sinusoidal obstruction syndrome (VOD) post-SCT risk
- **Allo-SCT:** High-risk ALL (hypodiploidy, KMT2A-r, Ph+ MRD+, persistent MRD after intensification); myeloablative conditioning; related/unrelated/haplo/CBT

**Infant ALL (KMT2A-r):**
- Age <12 months + KMT2A rearrangement = very high risk (5-year OS ~25-40%)
- Infant leukemia protocols (Interfant-06); bortezomib and FLT3 inhibitors in trials
- Allo-SCT in CR1 for MRD+ disease

### Outcomes by subtype

| Subtype | 5-year EFS (pediatric) |
|---------|----------------------|
| ETV6-RUNX1 | ~90-95% |
| High hyperdiploidy | ~85-90% |
| BCR-ABL1 (Ph+) | ~60-70% (TKI era) |
| Ph-like | ~50-60% |
| T-ALL (NOTCH1-mutant) | ~70-75% |
| ETP-ALL | ~55-65% |
| Hypodiploidy | ~25-30% |
| Infant KMT2A-r | ~25-40% |

### Long-term effects

Childhood ALL survivors (now majority of patients): neurocognitive impairment (MTX, cranial RT); growth retardation (steroids, RT); avascular necrosis (dexamethasone); secondary malignancies (therapy-related AML; radiation-associated tumors); infertility; cardiomyopathy (anthracyclines). Modern protocols minimize cranial RT and anthracycline exposure in standard-risk patients.

## Connections

- `connects-to` → **[RUNX1](../../03-molecular/runx1/README.md)** — ETV6-RUNX1 t(12;21) is the most common translocation in childhood ALL (~25%); RUNX1-RUNX1T1 t(8;21) defines CBF-AML; germline RUNX1 mutations (FPD) confer ~35-40% AML risk; RUNX1 controls lymphoid/myeloid lineage fate decisions.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — NOTCH1 activating mutations occur in ~60% of T-ALL; NOTCH1 drives T-cell progenitor proliferation and blocks differentiation; gamma-secretase inhibitors suppress NOTCH1 in T-ALL preclinically; ETP-ALL has low NOTCH1 mutation frequency.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — BCL-2 overexpression contributes to chemotherapy resistance in B-ALL; venetoclax (BCL-2 inhibitor) shows activity in relapsed/refractory B-ALL in early trials; Ph+ ALL and Ph-like ALL show BCL-2 dependence amenable to venetoclax combinations.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — PD-1/PD-L1 expression is upregulated in relapsed ALL and post-CAR-T failure; pembrolizumab studied for ALL after blinatumomab failure; checkpoint inhibition is investigated to prevent CAR-T exhaustion and enhance blinatumomab activity.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — B-ALL arises from arrested B-cell lymphoid progenitors; CD19+/CD10+/TdT+ immunophenotype defines most B-ALL; CD19 is exploited by tisagenlecleucel (CAR-T; 81% remission in ELIANA) and blinatumomab (CD19×CD3 BiTE); B-cell lineage markers determine eligibility for immunotherapy.
- `connects-to` → **[ABL1](../../03-molecular/abl1/README.md)** — BCR-ABL1 t(9;22) produces p190 BCR-ABL1 in ~25% adult ALL and ~3-5% pediatric ALL; Ph+ ALL requires TKI (dasatinib or ponatinib) from Day 1; blinatumomab+dasatinib is emerging as a chemotherapy-free regimen; allo-SCT deferred if MRD-negative on TKI.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — T-ALL arises from T-cell progenitor arrest at DN-DP transition; CD7+/cytoplasmic CD3+/TdT+ immunophenotype; NOTCH1 governs T-cell lineage commitment and is mutated in ~60% of T-ALL; nelarabine (T-cell-specific purine analog) is active in T-ALL relapse.
- `connects-to` → **[Aplastic Anemia](../aplastic-anemia/README.md)** — ALL and aplastic anemia both present with pancytopenia and a failing marrow but are opposites in mechanism: AA an empty marrow from T-cell destruction of stem cells, ALL a marrow packed with lymphoblasts — so the marrow biopsy (hypocellular vs blast-replaced) distinguishes them.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — ALL arises in the bone marrow from a transformed lymphoid progenitor whose blasts crowd out normal hematopoiesis, causing the anemia, thrombocytopenia, and neutropenia at presentation; marrow with ≥20% lymphoblasts is diagnostic, and marrow MRD after induction guides prognosis.
- `connects-to` → **[AML](../aml/README.md)** — ALL and AML are the two acute leukemias — both blast-crisis marrow failure, but ALL from lymphoid and AML from myeloid progenitors; flow cytometry (TdT, CD19/CD10 vs MPO, CD33) separates them, and the distinction dictates entirely different chemotherapy backbones.
- `connects-to` → **[Chronic Myeloid Leukemia](../cml/README.md)** — ALL and CML intersect at the Philadelphia chromosome: BCR-ABL1 defines CML and ~25% of adult B-ALL (Ph+ ALL), the highest-risk subtype, so both use ABL tyrosine-kinase inhibitors (imatinib, dasatinib, ponatinib); a CML blast crisis can present as acute lymphoblastic leukemia.
- `connects-to` → **[Burkitt Lymphoma](../burkitt-lymphoma/README.md)** — Mature B-cell ALL is biologically Burkitt leukemia: it shares the MYC t(8;14), starry-sky morphology and explosive growth of Burkitt lymphoma, presenting as a leukemic phase rather than a mass, and both are cured by short, intensive, CNS-directed chemo not standard ALL regimens.
- `connects-to` → **[Thymus](../../06-organ/thymus/README.md)** — T-cell ALL arises in the thymus: malignant transformation of developing thymocytes (often via NOTCH1) produces a mediastinal thymic mass with airway/SVC compression at presentation, distinguishing it from marrow-based B-ALL and reflecting the thymus's role in T-cell development.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Acute lymphoblastic leukemia is the paradigm cancer for cytotoxic T-cell therapy: CD19-directed CAR-T cells reprogram cytotoxic T cells to kill the leukemic B lymphoblasts, achieving deep remissions in relapsed B-ALL—the first CAR-T approval (tisagenlecleucel).
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Radiation has a defined role in acute lymphoblastic leukemia: cranial irradiation once prevented CNS relapse (now mostly replaced by intrathecal chemo to spare neurocognition), and total-body irradiation conditions the marrow before allogeneic transplant in high-risk disease.
- `connects-to` → **[Diffuse Large B-Cell Lymphoma](../dlbcl/README.md)** — Acute lymphoblastic leukemia and diffuse large B-cell lymphoma are aggressive B-cell cancers at opposite ends of maturation: ALL is a precursor-lymphoblast malignancy of children on prolonged multi-agent chemo, while DLBCL is a mature B-cell tumor of adults cured by R-CHOP.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Acute lymphoblastic leukemia crowds out platelet production: leukemic blasts fill the marrow and suppress megakaryocytes, so thrombocytopenia causes bruising and bleeding—one of the cytopenias, with anemia and neutropenia, that signals marrow takeover at diagnosis.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — The brain is a sanctuary site in acute lymphoblastic leukemia: blasts hide in the CNS where systemic chemo penetrates poorly, so untreated patients relapse in the meninges—why ALL therapy routinely includes intrathecal chemotherapy and sometimes cranial radiation.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — Acute lymphoblastic leukemia infiltrates the spleen and liver: circulating blasts lodge in these organs causing hepatosplenomegaly, a common presenting sign along with lymphadenopathy—reflecting how a marrow cancer spills into the lymphoid filtering organs.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — CD20 is a target in B-lineage ALL: adding the anti-CD20 antibody rituximab to chemotherapy improves outcomes in CD20-positive B-ALL, complementing the CD19- and CD22-directed immunotherapies (blinatumomab, CAR-T) that have transformed treatment.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — ALL crowds out normal blood production: leukemic blasts pack the marrow and suppress red-cell, neutrophil and platelet formation, so anemia, infection and bleeding—not the leukemia itself—are how acute lymphoblastic leukemia usually first presents.
- `connects-to` → **[Primary CNS Lymphoma](../pcnsl/README.md)** — ALL has a special tropism for the central nervous system: leukemic cells seed the meninges as a sanctuary site beyond most chemotherapy, so CNS-directed prophylaxis (intrathecal drugs) is essential—unlike PCNSL, a distinct lymphoma confined to the brain.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — ALL endangers patients through the neutrophil: leukemic blasts crowd the marrow and chemotherapy wipes out neutrophils, so profound neutropenia leaves children and adults dangerously prone to life-threatening infection during treatment.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — ALL can be the first sign of a cancer-predisposition syndrome: germline TP53 mutations (Li-Fraumeni) and other inherited defects raise leukemia risk, so ALL in a child with a strong family cancer history prompts genetic evaluation.
- `connects-to` → **[Immune System](../immune-system/README.md)** — ALL has been transformed by harnessing the immune system: CD19 CAR-T cells and the bispecific blinatumomab redirect the patient's T cells to kill B-lymphoblasts, rescuing relapsed B-ALL—among the first triumphs of cellular immunotherapy.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Treating ALL can crash the kidneys via tumor lysis: rapid leukemic-cell breakdown floods the blood with potassium, phosphate and urate that precipitate in the kidney, so hydration and rasburicase guard against this acute kidney injury.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — The testis is a sanctuary where ALL hides: the blood-testis barrier shields leukemic cells from chemotherapy, so the testis (like the CNS) is a site of relapse that requires dedicated treatment and monitoring in boys.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Natural killer cells help control ALL after transplant: donor NK cells mount a graft-versus-leukemia effect against residual blasts, and NK-based and CAR therapies are being developed to harness this innate killing.
- `connects-to` → **[Glucocorticoid Receptor](../../03-molecular/glucocorticoid-receptor/README.md)** — Steroids are a cornerstone of ALL treatment through the glucocorticoid receptor: when activated, it triggers apoptosis in lymphoblasts, so every regimen leans on it—and resistance to this signal predicts a worse outcome.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — ALL can crash blood calcium through tumor lysis: as chemotherapy bursts huge numbers of blasts, released phosphate binds calcium and potassium and uric acid surge, a metabolic emergency that threatens the heart and kidneys.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — ALL and its therapy both burden the liver: leukemic cells infiltrate it to cause hepatomegaly, while drugs like asparaginase and methotrexate are hepatotoxic, so liver function is watched throughout the long treatment course.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — ALL treatment can scar the heart: the anthracycline chemotherapy central to cure is cardiotoxic, weakening the heart muscle, so cardiac function is watched for years—an important late effect in children cured of leukemia.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — ALL hides behind regulatory T cells: the leukemia expands these immune suppressors that blunt the antileukemic response, a barrier that immunotherapies like CAR-T and bispecific antibodies must overcome.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — ALL's tumor lysis floods the blood with potassium: when chemotherapy bursts masses of blasts, potassium pours out of the dying cells, and the resulting hyperkalemia can stop the heart if not urgently managed.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — ALL's tumor lysis spills phosphate too: dying blasts release phosphorus that binds calcium and crashes it, while precipitating in the kidneys, part of the metabolic emergency of starting chemotherapy.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — ALL hides in the eye: like the brain, the eye is a sanctuary the bloodstream's chemotherapy reaches poorly, so leukemic infiltration there can seed relapse and is checked in high-risk disease.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — A MYC translocation defines the most aggressive B-ALL: mature B-cell (Burkitt-type) leukemia is driven by MYC switched on next to an antibody gene, demanding intensive, lymphoma-style treatment.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy distinguishes ALL's blast: a lymphoblast with a high nucleus-to-cytoplasm ratio, condensed chromatin, and scant organelles — and, crucially, none of the Auer rods that mark the myeloid leukemias.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Leukemia can settle in the skin: ALL blasts infiltrate it as leukemia cutis, firm violet nodules or plaques, an uncommon but telling sign that the disease has spilled beyond the blood and marrow.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Treating ALL convulses the body's chemistry: as chemotherapy bursts the huge mass of blasts in tumor lysis syndrome, magnesium and other electrolytes swing wildly, demanding close monitoring and correction to protect the heart and kidneys.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — ALL hides in and harms the nervous system: leukemic cells seed the CNS as a sanctuary, demanding intrathecal chemotherapy, while vincristine in the regimen poisons peripheral neurons into a dose-limiting neuropathy.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Engineered antibodies transformed ALL: blinatumomab, a bispecific that yokes T cells to CD19, and the CD22 drug-conjugate inotuzumab now clear relapsed disease that chemotherapy alone could not.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — A signature ALL drug inflames the pancreas: asparaginase, key to pediatric regimens, can trigger acute pancreatitis and disturb blood sugar, a toxicity watched for throughout treatment.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — ALL often announces itself in the bones: marrow packed with blasts causes the bone and joint pain that can mimic arthritis in a child, while the high-dose steroids of treatment later bring avascular necrosis and myopathy.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — The long chemotherapy is hard on the liver: methotrexate, 6-mercaptopurine, and asparaginase all injure hepatocytes, so transaminases and bilirubin are tracked across the months-to-years of ALL maintenance therapy.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — Steroids are core to the cure and suppress the adrenal: the prolonged high-dose glucocorticoids central to ALL regimens shut down the adrenal axis, so withdrawal must be gradual and stress dosing considered during illness.
- `connects-to` → **[Graft-Versus-Host Disease](../gvhd/README.md)** — Transplant trades one risk for another: high-risk ALL is cured by allogeneic stem-cell transplant, whose graft-versus-leukemia effect helps clear the disease but brings graft-versus-host disease as its dangerous price.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Growth signaling fuels the leukemic cell: the PI3K-AKT-mTOR pathway is often hyperactive in ALL, driving proliferation and survival, so mTOR inhibitors are studied to resensitize resistant disease.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — The marrow's macrophages shelter the leukemia: tumor-associated macrophages in the niche support blast survival and resistance, and they also mediate the cytokine release that complicates CAR-T and blinatumomab therapy.

[^pui-2018-all-cure]: Pui CH, Yang JJ, Bhakta N, et al. Global efforts toward the cure of childhood acute lymphoblastic leukemia. *Lancet Child Adolesc Health.* 2018;2(6):440-454. [doi:10.1016/S2352-4642(18)30066-X](https://doi.org/10.1016/S2352-4642(18)30066-X) · [PubMed 29976322](https://pubmed.ncbi.nlm.nih.gov/29976322/)
[^maude-2018-tisagenlecleucel]: Maude SL, Laetsch TW, Buechner J, et al. Tisagenlecleucel in children and young adults with B-cell lymphoblastic leukemia. *N Engl J Med.* 2018;378(5):439-448. [doi:10.1056/NEJMoa1709866](https://doi.org/10.1056/NEJMoa1709866) · [PubMed 29385370](https://pubmed.ncbi.nlm.nih.gov/29385370/)

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
