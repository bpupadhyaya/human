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
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "The CNS is a leukemic sanctuary: ALL blasts hide in the meninges where chemotherapy penetrates poorly, so every patient gets intrathecal therapy and sometimes cranial radiation to prevent and treat CNS relapse."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: connects-to
    note: "Treatment opens the door to Pneumocystis: the prolonged steroids and chemotherapy of ALL deplete T cells, so PCP pneumonia is a real threat — which is why co-trimoxazole prophylaxis runs through the entire treatment course."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB keeps the blast alive: constitutive NF-κB signaling in ALL cells drives survival and anti-apoptotic gene expression and underlies resistance to glucocorticoids, making the pathway a therapeutic target."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "A subset runs on JAK-STAT: Ph-like ALL carries JAK2 and cytokine-receptor rearrangements that activate STAT signaling including STAT3, a driver that makes these high-risk cases candidates for JAK inhibition."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Empty marrow invites overwhelming infection: leukemic replacement and intensive chemotherapy leave ALL patients profoundly neutropenic, so febrile neutropenia and sepsis are the leading cause of treatment-related death."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Its signature drug clots the blood: L-asparaginase depletes antithrombin and other clotting regulators, so venous thromboembolism — including cerebral venous sinus thrombosis — is a characteristic complication of ALL therapy."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Prolonged neutropenia opens the lung to mold: the deep neutropenia of ALL induction lets inhaled Aspergillus invade as angioinvasive pulmonary aspergillosis, a leading infectious cause of treatment-related death."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Its steroids attack the bone: the high-dose corticosteroids central to ALL therapy cause osteopenia and avascular necrosis, a characteristic skeletal toxicity that can cripple joints in survivors, especially adolescents."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Its anthracyclines scar the heart: the daunorubicin and doxorubicin used to cure ALL are dose-dependently cardiotoxic, leaving some survivors with a cardiomyopathy and heart failure years later."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Vincristine leaves the nerves raw: the vinca alkaloid central to ALL therapy causes a dose-limiting peripheral neuropathy with numbness, weakness and neuropathic pain that can persist after treatment."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Tumor lysis and nephrotoxic drugs batter the kidneys: the massive cell turnover at ALL induction triggers tumor lysis syndrome, and methotrexate and antifungals add nephrotoxicity, together threatening kidney injury."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A long, intensive treatment weighs on mood: ALL's prolonged multi-year therapy, repeated hospitalizations and, in survivors, the cognitive effects of CNS-directed treatment contribute to depression."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Its therapy disturbs many glands: the high-dose steroids of ALL cause hyperglycaemia and osteonecrosis, asparaginase can inflame the pancreas, and cranial irradiation damages the pituitary and growth in children."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Its drugs injure the gut and liver: asparaginase causes acute pancreatitis and hepatotoxicity, and chemotherapy brings mucositis and the dangerous neutropenic colitis (typhlitis)."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "Profound immune suppression reawakens shingles: the prolonged chemotherapy and stem-cell transplant for ALL deplete T-cell immunity, allowing latent or primary varicella-zoster to cause severe disease."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It arises in and fills the lymphoid organs: ALL infiltrates lymph nodes, spleen and thymus, with T-cell ALL classically forming an anterior mediastinal mass alongside hepatosplenomegaly."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Treatment can flood and block the kidney: tumour lysis syndrome releases urate and potassium causing acute kidney injury, and leukemic cells can directly infiltrate the kidneys."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It marks the skin: thrombocytopenia causes petechiae and bruising, and leukemic infiltration produces leukemia cutis and, occasionally, chloromas."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its chemotherapy bruises the heart: anthracyclines like daunorubicin used in ALL induction can cause cardiomyopathy, a late effect that follows childhood survivors for life."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It can fill the chest: T-cell ALL classically presents with a mediastinal mass compressing the airway and SVC, while immunosuppression invites pneumonia and fungal lung infection."
  - target: 02-pathogen/01-viruses/herpesvirus
    relation: connects-to
    note: "Chemotherapy reawakens latent virus: under the deep immunosuppression of ALL treatment, cytomegalovirus reactivation and severe herpes-simplex infection are major threats, prompting surveillance and antiviral prophylaxis."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "The backbone of cure: intensive multi-agent chemotherapy over two to three years, with intrathecal therapy for the CNS, cures most childhood acute lymphoblastic leukaemia."
  - target: 03-medicine/01-modern/13-cancer/car-t
    relation: connects-to
    note: "Engineered cells rescue relapse: CD19-directed CAR-T therapy (tisagenlecleucel) induces remission in relapsed or refractory B-cell ALL, a landmark of cellular immunotherapy."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Philadelphia-positive disease needs a TKI: BCR-ABL1 tyrosine-kinase inhibitors such as imatinib and dasatinib, added to chemotherapy, transformed the once-dismal Ph+ subtype of ALL."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "It hurts and weakens bone: leukaemic marrow infiltration causes the bone pain of ALL, while prolonged corticosteroids and methotrexate leave survivors with osteonecrosis and osteoporosis as major late effects."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "The CNS is a sanctuary site: leukaemic cells hide in the meninges, so ALL needs intrathecal chemotherapy and once cranial irradiation — treatments that injure the hippocampus and cause neurocognitive late effects in survivors."
  - target: 01-human/07-system/cll
    relation: connects-to
    note: "Acute versus chronic lymphoid leukaemia: ALL is an aggressive proliferation of immature lymphoblasts needing immediate intensive therapy, whereas CLL is an indolent accumulation of mature B-lymphocytes — opposite ends of lymphoid malignancy."
  - target: 01-human/07-system/mds
    relation: connects-to
    note: "From dysplasia to acute leukaemia: myelodysplastic syndromes are clonal marrow-failure states that can transform into acute leukaemia, and intensive ALL therapy can itself later cause therapy-related myeloid neoplasms."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "Neutropenic enterocolitis: chemotherapy for ALL denudes the gut epithelium and, combined with profound neutropenia, causes typhlitis—a life-threatening infection of the bowel wall."
  - target: 01-human/07-system/hodgkin-lymphoma
    relation: connects-to
    note: "Two cancers of the lymphoid system: ALL is a malignancy of lymphoid precursors in the marrow while Hodgkin lymphoma arises from mature B cells in lymph nodes—distinct lymphoid cancers that both strike the young."
  - target: 03-medicine/01-modern/13-cancer/car-t
    relation: connects-to
    note: "The CAR-T breakthrough: B-cell ALL was the first cancer cured by CD19 CAR-T cells (tisagenlecleucel), engineered T cells now standard for relapsed and refractory disease."
  - target: 01-human/07-system/cytokine-storm
    relation: connects-to
    note: "Immunotherapy's storm: CD19 CAR-T cells and the bispecific blinatumomab used for ALL trigger cytokine release syndrome, a systemic cytokine storm needing tocilizumab and intensive care."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "Tumour-lysis nephropathy: the rapid blast turnover of ALL at induction floods the blood with urate and phosphate that precipitate in the glomerulus and tubules, causing acute kidney injury."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "p53 and relapse: TP53 alterations—seen in hypodiploid and relapsed ALL and as germline Li-Fraumeni mutations—drive chemoresistance and a poor prognosis."
  - target: 02-pathogen/01-viruses/epstein-barr-virus
    relation: connects-to
    note: "Post-transplant lymphoproliferation: after allogeneic stem-cell transplant for high-risk ALL, EBV can drive post-transplant lymphoproliferative disorder under immunosuppression."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Immunosuppressed COVID: leukaemia and its chemotherapy or CAR-T immunosuppression cause severe, prolonged COVID-19 with blunted vaccine responses and reactivation risk."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Ph-like ALL: a high-risk subtype of B-ALL carries kinase fusions that activate JAK-STAT signalling, making JAK inhibitors a targeted strategy in this aggressive disease."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "Cell-cycle target: cyclin D-CDK4/6 drives the proliferation of lymphoblasts, and CDK4/6 inhibitors are being explored to restore cell-cycle control in acute lymphoblastic leukaemia."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Epigenetic dependency: EZH2 and the PRC2 complex enforce the repressive chromatin state of leukaemic blasts, an epigenetic vulnerability particularly in T-cell ALL."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "Lost cell-cycle brake: deletion of the CDKN2A tumour suppressor is among the most frequent lesions in ALL, removing the p16-mediated restraint on CDK4/6 and unleashing lymphoblast proliferation."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Marrow-niche refuge: CXCL12 from bone-marrow stroma signals through CXCR4 to home and shelter leukaemic blasts in the protective niche, a mechanism of chemoresistance and minimal residual disease in ALL."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Survival signalling: PI3K-AKT activation, often via PTEN loss in T-cell ALL, drives the growth and survival of lymphoblasts and contributes to glucocorticoid resistance."
  - target: 01-human/03-molecular/men1
    relation: connects-to
    note: "Menin-MLL dependency: KMT2A (MLL)-rearranged ALL, common in infants, depends on the menin-MLL interaction to maintain leukaemic HOX transcription, the target of menin inhibitors (revumenib) entering ALL therapy."
  - target: 01-human/03-molecular/flt3
    relation: connects-to
    note: "Targetable kinase: FLT3 is overexpressed or activated in KMT2A-rearranged and hyperdiploid ALL, a receptor tyrosine kinase under investigation as a therapeutic target in these subtypes."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Glucocorticoid apoptosis: glucocorticoids and chemotherapy kill lymphoblasts by triggering caspase-3-mediated apoptosis, and the early apoptotic response to steroids is one of the strongest prognostic markers in ALL."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Immunotherapy killing: the CD19-CD3 bispecific blinatumomab and CD19 CAR-T cells redirect cytotoxic T cells to destroy B-ALL blasts through perforin and granzyme, the immune effector mechanism that has transformed relapsed and refractory disease."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Growth dependency: lymphoblasts depend on IGF-1R signalling for proliferation and survival, a growth-factor axis that supports leukaemic growth and is being explored as a therapeutic target in ALL."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "Stem-cell quiescence: FOXO transcription factors maintain quiescent leukaemia-initiating cells that survive chemotherapy in the marrow niche, a reservoir that seeds the relapse which remains the main cause of treatment failure in ALL."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K survival: PI3K-AKT-mTOR signalling (AKT and mTOR already mapped) is activated in acute lymphoblastic leukemia, especially T-ALL downstream of NOTCH and PTEN loss, supporting blast survival."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "RAS-MAPK proliferation: RAS-MAPK-ERK activation, common in B-cell ALL and the Ph-like subtype, drives blast proliferation and is a target of MEK inhibition in resistant disease."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Cell-cycle drive: deregulated RB-E2F1 transcription (with the CDK4/6 and CDKN2A lesions already mapped) powers the unchecked proliferation of acute lymphoblastic leukemia blasts."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PI3K tumour suppression: PTEN loss unleashes the PI3K-AKT-mTOR axis (AKT and mTOR already mapped), a frequent driver of T-cell ALL that promotes leukemic-cell growth and survival."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "RAS proliferation: activating RAS-pathway mutations (KRAS/NRAS) are among the most common lesions in B-cell ALL, driving the ERK-MAPK proliferative signalling (ERK1/2 already mapped) of the leukemic clone."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Leukemic stemness: Wnt/β-catenin signalling sustains the leukemia-initiating cells of ALL, contributing to the self-renewal and chemoresistance of the leukemic stem-cell compartment."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β within the bone-marrow niche regulates leukemic-cell quiescence and chemoresistance in acute lymphoblastic leukemia."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Stromal and leukemic galectin-3 promotes the marrow-niche survival signalling and chemoresistance of acute lymphoblastic leukemia blasts."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α in the hypoxic bone-marrow niche supports the survival and metabolic adaptation of acute lymphoblastic leukemia cells."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the antileukemic immune response and immune-evasion balance of acute lymphoblastic leukemia, relevant to its immunotherapy."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING modulates the inflammatory and immune microenvironment of the bone marrow infiltrated by acute lymphoblastic leukemia."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling in the bone-marrow niche contributes to the immunosuppression and chemoprotection of acute lymphoblastic leukemia cells."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β supports leukemic stem-cell self-renewal and survival, a targetable dependency in acute lymphoblastic leukemia."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins from the leukemic bone-marrow myeloid compartment shape the inflammatory niche of acute lymphoblastic leukemia."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis and is a therapeutic target in acute lymphoblastic leukemia."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family (LYN/LCK) kinase signaling downstream of the pre-B-cell receptor and BCR-ABL supports the survival of acute lymphoblastic leukemia blasts."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of acute lymphoblastic leukemia."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival and chemoresistance of acute lymphoblastic leukemia blasts, a candidate therapeutic vulnerability."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of acute lymphoblastic leukemia, a candidate metabolic-therapy target."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-family chemokine signaling (CXCL12/CXCR4 already mapped) participates in the bone-marrow homing and CNS infiltration of acute lymphoblastic leukemia."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic dysregulation of acute lymphoblastic leukemia."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation in the bone-marrow niche contributes to the leukemic-cell maintenance of acute lymphoblastic leukemia."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the inflammatory bone-marrow microenvironment of acute lymphoblastic leukemia."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6-STAT3 signaling (STAT3 already mapped) participates in the bone-marrow microenvironment and survival signaling of acute lymphoblastic leukemia."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory bone-marrow microenvironment of acute lymphoblastic leukemia."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory bone-marrow microenvironment of acute lymphoblastic leukemia."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the antigen-receptor (pre-B-cell-receptor/T-cell-receptor) and survival signaling of acute lymphoblastic leukemia."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Tumour lysis syndrome: the rapid cell turnover of acute lymphoblastic leukaemia, especially on starting treatment, releases purines that xanthine oxidase converts to uric acid, causing the hyperuricaemia and urate nephropathy prevented by rasburicase and allopurinol."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immunotherapy: antigen presentation shapes the T-cell response harnessed by the CD19-directed CAR-T cells and bispecific antibodies (perforin already mapped) that have transformed relapsed acute lymphoblastic leukaemia."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell expansion: IL-2 drives the proliferation of the engineered and endogenous T cells used against acute lymphoblastic leukaemia, and its release contributes to the cytokine-release syndrome seen with CAR-T therapy."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Marrow-failure anaemia: replacement of the marrow (already mapped) by lymphoblasts crowds out red-cell production, and the resulting anaemia with falling haemoglobin, alongside thrombocytopenia, presents acute lymphoblastic leukaemia."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Anthracycline cardiotoxicity: the anthracycline chemotherapy central to ALL regimens is cardiotoxic, and troponin elevation helps detect the cumulative myocardial injury that threatens the long-term survivors of this highly curable leukaemia."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Tumour-lysis acidosis: the high blast burden of ALL, lysed by induction chemotherapy, releases acids that, with lactate from the metabolic stress, produce the metabolic acidosis of tumour-lysis syndrome (potassium and urate already mapped)."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive marrow: IL-10 in the leukaemic marrow microenvironment dampens the anti-leukaemia T-cell response (MHC class II already mapped), part of the immune evasion that the CAR-T and bispecific immunotherapies of ALL aim to overcome."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Transfusional iron overload: the chronic red-cell transfusion support during intensive ALL therapy (haemoglobin already mapped) loads the body with iron, an overload burden that can require monitoring and chelation in the long-term survivor."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Marrow angiogenesis: increased bone-marrow (already mapped) microvascular density supported by VEGF is part of the altered leukaemic microenvironment that sustains the lymphoblastic clone in acute lymphoblastic leukaemia."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage niche: IL-4 polarises the marrow macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the leukaemic bone-marrow (already mapped) microenvironment that shelters the lymphoblasts of acute lymphoblastic leukaemia."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Marrow-adipocyte crosstalk: the marrow adipocytes and their adipokine adiponectin engage in metabolic crosstalk with the lymphoblasts, the marrow adipose tissue shaping the niche that sustains the clone in acute lymphoblastic leukaemia."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Adipokine marrow signalling: leptin, with adiponectin (already mapped), from the marrow adipose tissue signals to the leukaemic cells, part of the metabolic microenvironment and the chemoresistance of acute lymphoblastic leukaemia."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Tumour-lysis hypocalcaemia: the hyperphosphataemia of the tumour lysis syndrome at ALL induction binds calcium, causing the hypocalcaemia that accompanies the hyperkalaemia (already mapped) and needs monitoring."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "M2 marrow niche: IL-13, with IL-4 (already mapped), sustains the M2 marrow macrophages of the immunosuppressive niche that shelters the lymphoblasts of acute lymphoblastic leukaemia."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Marrow-adipocyte adipokine: resistin, with leptin and adiponectin (already mapped), is part of the marrow-adipocyte adipokine crosstalk that shapes the leukaemic niche and the chemoresistance of acute lymphoblastic leukaemia."
  - target: 01-human/07-system/cml
    relation: connects-to
    note: "Ph+ overlap: the Ph+ (BCR-ABL — ABL1 already mapped) ALL and the CML (lymphoid blast crisis) share the BCR-ABL fusion and the TKI (imatinib) therapy."
  - target: 01-human/07-system/burkitt-lymphoma
    relation: connects-to
    note: "Mature-B malignancy: the Burkitt lymphoma/leukaemia (MYC already mapped, the L3/mature-B ALL) is a related aggressive B-cell malignancy of the ALL spectrum."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Transfusion iron: the transfusion-dependent anaemia (haemoglobin already mapped) of the ALL and its chemotherapy loads the body with iron."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antileukaemic arm: the IFN-γ of the T and NK cells (perforin already mapped) is the type-II interferon arm of the anti-leukaemic immunity, relevant to the blinatumomab and CAR-T (T-cell already mapped) immunotherapy of ALL."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-leukaemic response of the ALL immune microenvironment."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate antileukaemic interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment relevant to the immunotherapy of ALL."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of the ALL marrow."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory bone-marrow (already mapped) microenvironment of ALL."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the ALL marrow microenvironment."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Antigen presentation: the dendritic cells present the leukaemia antigen (MHC already mapped) to the T cells (already mapped), shaping the immune microenvironment and the antileukaemic response of ALL."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "B-cell aplasia: the normal plasma cells and their antibody (already mapped) output are lost with the CD19 (CD20 already mapped) CAR-T and blinatumomab therapy, causing the B-cell aplasia and hypogammaglobulinaemia of treated ALL."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "Complement C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) contributes to the myeloid inflammation and the cytokine-release-syndrome complement activation of the CAR-T therapy of ALL."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) are effectors of the antibody-mediated cytotoxicity and the cytokine-release-syndrome complement activation of the immunotherapy of ALL."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement evasion: the ALL blasts recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), tempering the complement attack within the marrow (already mapped) microenvironment."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Anaemia/iron overload: transferrin, the iron carrier, reflects the disordered iron handling of the marrow-failure anaemia and the transfusional iron overload of ALL."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-leukaemia axis: TSLP, from marrow stroma (already mapped) and thymic epithelium, drives CRLF2-rearranged ALL blasts and primes the marrow (already mapped) microenvironment for leukaemia-promoting Th2 skewing."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-marrow axis: bradykinin, via B1/B2 receptors on marrow endothelium (already mapped) and leukaemia blasts, amplifies the vascular permeability and the inflammatory cytokine milieu of the leukaemia marrow of ALL."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Erythropoietic failure: erythropoietin signalling is impaired by the marrow infiltration of the ALL blasts (already mapped), contributing to the hypoproliferative anaemia and the transfusion dependence of ALL."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell marrow niche: mast cells (already mapped) in the bone marrow (already mapped) niche of ALL release histamine that amplifies the vascular permeability and the inflammatory cytokine milieu that sustains the leukaemia-promoting microenvironment of ALL."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Oncostatic chronobiology: melatonin has pro-apoptotic and anti-proliferative effects on leukaemic cells; disrupted melatonin rhythm (common in paediatric cancer) amplifies the immune dysregulation (T-cell already mapped) and the oxidative stress of ALL."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement-contact regulation: C1-esterase inhibitor regulates the classical complement (C3, C5 and factor H already mapped) pathway exploited by ALL blasts for complement evasion and the leukaemia-promoting marrow-niche inflammatory activation."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "ALL testosterone: testosterone, via androgen receptors on bone-marrow (already mapped) stromal cells and leukaemic blasts, modulates marrow haematopoiesis; androgen-deprivation therapy amplifies the immunosuppressive (regulatory T cell already mapped) niche of ALL."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "ALL serotonin: serotonin, via 5-HT receptors on bone-marrow (already mapped) stromal cells and leukaemic blasts, modulates the immune microenvironment; serotonin dysregulation amplifies the IL-6 (already mapped) and IL-1β (already mapped) leukaemia-niche activation of ALL."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "ALL prolactin: prolactin, via PRLR on bone-marrow (already mapped) stromal cells and leukaemic blasts, promotes leukaemic cell survival; hyperprolactinaemia amplifies the IL-6 (already mapped) and NF-κB (already mapped) leukaemia-niche activation of ALL."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "ALL oxytocin: oxytocin, via OXTR on bone-marrow (already mapped) stromal cells and regulatory T cells (already mapped), modulates leukaemic-niche immune suppression; oxytocin deficiency amplifies the IL-6 (already mapped) and NF-κB (already mapped) activation of ALL."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "ALL vasopressin: vasopressin, via V1aR on bone-marrow (already mapped) stromal cells and megakaryocyte progenitors (platelet already mapped), modulates haematopoiesis; vasopressin dysregulation amplifies the IL-6 (already mapped) and NF-κB (already mapped) leukaemia-niche of ALL."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "ALL selenium: selenium, as GPx in bone-marrow (already mapped) stromal cells and leukaemic blasts, scavenges ROS driving leukaemic proliferation; selenium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) leukaemia-niche inflammatory cascade of ALL."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "ALL sodium: sodium dysregulation in bone-marrow (already mapped) stroma and B-cell (already mapped) precursors amplifies ionic stress; osmotic changes worsen NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) leukaemic blast proliferation in ALL."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "ALL zinc: zinc cofactors macrophage (already mapped) anti-tumour function and B-cell (already mapped) homeostasis; zinc deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) leukaemic blast expansion in ALL."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "ALL copper: copper, via ceruloplasmin and SOD in macrophages (already mapped) and bone-marrow (already mapped) stroma, scavenges ROS; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) leukaemic proliferation in ALL."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "thyroid hormones (iodine-dependent) in B-cell (already mapped) precursors and macrophages (already mapped) modulate proliferative signalling; iodine deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) leukaemic blast expansion in ALL."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "chloride channels on B-cell (already mapped) precursors and bone-marrow (already mapped) stroma maintain ionic homeostasis; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) leukaemic blast proliferation in ALL."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "H2S from sulfur-amino acids in macrophages (already mapped) and bone-marrow (already mapped) stroma scavenges ROS promoting leukaemic blast apoptosis; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) blast expansion in ALL."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "ALL carbon: carbon, as metabolic backbone of purines and nucleotides in B-cell (already mapped) precursors and bone-marrow (already mapped) stroma, drives leukaemic blast expansion; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) in ALL."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "ALL hydrogen: hydrogen, via redox homeostasis in B-cell (already mapped) precursors and macrophages (already mapped), quenches leukaemic ROS; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) blast proliferation in ALL."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "ALL nitrogen: nitric oxide from iNOS in macrophages (already mapped) and bone-marrow (already mapped) stroma modulates niche homeostasis; nitrogen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) leukaemic cascade in ALL."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "ALL oxygen: mitochondrial oxygen in B-cell (already mapped) precursors and macrophages (already mapped) sustains ATP for leukaemic blast proliferation; hypoxia amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) cascade in ALL."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "ALL GLP-1: GLP-1 receptor signalling in macrophages (already mapped) and B-cell (already mapped) precursors modulates metabolic immune homeostasis; GLP-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) leukaemic cascade in ALL."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "ALL angiotensin-II: angiotensin-II signalling in macrophages (already mapped) and bone-marrow (already mapped) stroma promotes niche inflammation; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) cascade of ALL."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "ALL RANKL: RANKL in bone-marrow (already mapped) stromal cells and macrophages (already mapped) modulates the leukaemic niche bone-immune axis; RANKL excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of ALL."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "ALL fibronectin: fibronectin in bone-marrow (already mapped) extracellular matrix and macrophages (already mapped) modulates leukaemic blast adhesion; fibronectin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of ALL."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "ALL activin-A: activin-A from bone-marrow (already mapped) stromal cells and macrophages (already mapped) modulates haematopoietic differentiation; activin-A excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of ALL."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "ALL cgrp: CGRP from macrophages (already mapped) and bone-marrow stromal cells (already mapped) modulates leukaemic neuroimmune tone; cgrp excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of ALL."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "ALL calcitonin: calcitonin from macrophages (already mapped) and bone-marrow stromal cells (already mapped) modulates leukaemic calcium balance; calcitonin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of ALL."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "ALL substance-p: substance-P from macrophages (already mapped) and bone-marrow stromal cells (already mapped) modulates leukaemic nociceptive signalling; substance-P excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of ALL."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "ALL insulin-receptor: insulin receptor on macrophages (already mapped) and bone-marrow stromal cells (already mapped) modulates leukaemic metabolic axis; insulin-receptor excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of ALL."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "ALL aldosterone: aldosterone from macrophages (already mapped) and bone-marrow stromal cells (already mapped) modulates leukaemic fluid balance; aldosterone excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of ALL."
  - target: 01-human/03-molecular/androgen-receptor
    relation: connects-to
    note: "ALL androgen-receptor: androgen receptor on macrophages (already mapped) and bone-marrow stromal cells (already mapped) modulates leukaemic sex tone; androgen-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of ALL."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "ALL norepinephrine: norepinephrine from macrophages (already mapped) and bone-marrow stromal cells (already mapped) modulates leukaemic adrenergic tone; norepinephrine excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of ALL."
  - target: 01-human/03-molecular/adrenomedullin
    relation: connects-to
    note: "ALL adrenomedullin: adrenomedullin from macrophages (already mapped) and bone-marrow stromal cells (already mapped) modulates leukaemic vascular tone; adrenomedullin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of ALL."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "ALL bdnf: BDNF from macrophages (already mapped) and bone-marrow stromal cells (already mapped) sustains leukaemic neural-immune niche; BDNF deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of ALL."
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
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — The CNS is a leukemic sanctuary: ALL blasts hide in the meninges where chemotherapy penetrates poorly, so every patient gets intrathecal therapy and sometimes cranial radiation to prevent and treat CNS relapse.
- `connects-to` → **[Pneumocystis jirovecii](../../../02-pathogen/03-fungi/pneumocystis-jirovecii/README.md)** — Treatment opens the door to Pneumocystis: the prolonged steroids and chemotherapy of ALL deplete T cells, so PCP pneumonia is a real threat — which is why co-trimoxazole prophylaxis runs through the entire treatment course.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB keeps the blast alive: constitutive NF-κB signaling in ALL cells drives survival and anti-apoptotic gene expression and underlies resistance to glucocorticoids, making the pathway a therapeutic target.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — A subset runs on JAK-STAT: Ph-like ALL carries JAK2 and cytokine-receptor rearrangements that activate STAT signaling including STAT3, a driver that makes these high-risk cases candidates for JAK inhibition.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Empty marrow invites overwhelming infection: leukemic replacement and intensive chemotherapy leave ALL patients profoundly neutropenic, so febrile neutropenia and sepsis are the leading cause of treatment-related death.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Its signature drug clots the blood: L-asparaginase depletes antithrombin and other clotting regulators, so venous thromboembolism — including cerebral venous sinus thrombosis — is a characteristic complication of ALL therapy.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Prolonged neutropenia opens the lung to mold: the deep neutropenia of ALL induction lets inhaled Aspergillus invade as angioinvasive pulmonary aspergillosis, a leading infectious cause of treatment-related death.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Its steroids attack the bone: the high-dose corticosteroids central to ALL therapy cause osteopenia and avascular necrosis, a characteristic skeletal toxicity that can cripple joints in survivors, especially adolescents.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Its anthracyclines scar the heart: the daunorubicin and doxorubicin used to cure ALL are dose-dependently cardiotoxic, leaving some survivors with a cardiomyopathy and heart failure years later.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Vincristine leaves the nerves raw: the vinca alkaloid central to ALL therapy causes a dose-limiting peripheral neuropathy with numbness, weakness and neuropathic pain that can persist after treatment.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Tumor lysis and nephrotoxic drugs batter the kidneys: the massive cell turnover at ALL induction triggers tumor lysis syndrome, and methotrexate and antifungals add nephrotoxicity, together threatening kidney injury.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A long, intensive treatment weighs on mood: ALL's prolonged multi-year therapy, repeated hospitalizations and, in survivors, the cognitive effects of CNS-directed treatment contribute to depression.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Its therapy disturbs many glands: the high-dose steroids of ALL cause hyperglycaemia and osteonecrosis, asparaginase can inflame the pancreas, and cranial irradiation damages the pituitary and growth in children.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Its drugs injure the gut and liver: asparaginase causes acute pancreatitis and hepatotoxicity, and chemotherapy brings mucositis and the dangerous neutropenic colitis (typhlitis).
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — Profound immune suppression reawakens shingles: the prolonged chemotherapy and stem-cell transplant for ALL deplete T-cell immunity, allowing latent or primary varicella-zoster to cause severe disease.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It arises in and fills the lymphoid organs: ALL infiltrates lymph nodes, spleen and thymus, with T-cell ALL classically forming an anterior mediastinal mass alongside hepatosplenomegaly.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Treatment can flood and block the kidney: tumour lysis syndrome releases urate and potassium causing acute kidney injury, and leukemic cells can directly infiltrate the kidneys.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It marks the skin: thrombocytopenia causes petechiae and bruising, and leukemic infiltration produces leukemia cutis and, occasionally, chloromas.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its chemotherapy bruises the heart: anthracyclines like daunorubicin used in ALL induction can cause cardiomyopathy, a late effect that follows childhood survivors for life.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It can fill the chest: T-cell ALL classically presents with a mediastinal mass compressing the airway and SVC, while immunosuppression invites pneumonia and fungal lung infection.
- `connects-to` → **[Herpesvirus](../../../02-pathogen/01-viruses/herpesvirus/README.md)** — Chemotherapy reawakens latent virus: under the deep immunosuppression of ALL treatment, cytomegalovirus reactivation and severe herpes-simplex infection are major threats, prompting surveillance and antiviral prophylaxis.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — The backbone of cure: intensive multi-agent chemotherapy over two to three years, with intrathecal therapy for the CNS, cures most childhood acute lymphoblastic leukaemia.
- `connects-to` → **[CAR-T](../../../03-medicine/01-modern/13-cancer/car-t/README.md)** — Engineered cells rescue relapse: CD19-directed CAR-T therapy (tisagenlecleucel) induces remission in relapsed or refractory B-cell ALL, a landmark of cellular immunotherapy.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Philadelphia-positive disease needs a TKI: BCR-ABL1 tyrosine-kinase inhibitors such as imatinib and dasatinib, added to chemotherapy, transformed the once-dismal Ph+ subtype of ALL.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — It hurts and weakens bone: leukaemic marrow infiltration causes the bone pain of ALL, while prolonged corticosteroids and methotrexate leave survivors with osteonecrosis and osteoporosis as major late effects.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — The CNS is a sanctuary site: leukaemic cells hide in the meninges, so ALL needs intrathecal chemotherapy and once cranial irradiation — treatments that injure the hippocampus and cause neurocognitive late effects in survivors.
- `connects-to` → **[CLL](../cll/README.md)** — Acute versus chronic lymphoid leukaemia: ALL is an aggressive proliferation of immature lymphoblasts needing immediate intensive therapy, whereas CLL is an indolent accumulation of mature B-lymphocytes — opposite ends of lymphoid malignancy.
- `connects-to` → **[MDS](../mds/README.md)** — From dysplasia to acute leukaemia: myelodysplastic syndromes are clonal marrow-failure states that can transform into acute leukaemia, and intensive ALL therapy can itself later cause therapy-related myeloid neoplasms.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — Neutropenic enterocolitis: chemotherapy for ALL denudes the gut epithelium and, combined with profound neutropenia, causes typhlitis—a life-threatening infection of the bowel wall.
- `connects-to` → **[Hodgkin Lymphoma](../hodgkin-lymphoma/README.md)** — Two cancers of the lymphoid system: ALL is a malignancy of lymphoid precursors in the marrow while Hodgkin lymphoma arises from mature B cells in lymph nodes—distinct lymphoid cancers that both strike the young.
- `connects-to` → **[CAR-T](../../../03-medicine/01-modern/13-cancer/car-t/README.md)** — The CAR-T breakthrough: B-cell ALL was the first cancer cured by CD19 CAR-T cells (tisagenlecleucel), engineered T cells now standard for relapsed and refractory disease.
- `connects-to` → **[Cytokine Storm](../cytokine-storm/README.md)** — Immunotherapy's storm: CD19 CAR-T cells and the bispecific blinatumomab used for ALL trigger cytokine release syndrome, a systemic cytokine storm needing tocilizumab and intensive care.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — Tumour-lysis nephropathy: the rapid blast turnover of ALL at induction floods the blood with urate and phosphate that precipitate in the glomerulus and tubules, causing acute kidney injury.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — p53 and relapse: TP53 alterations—seen in hypodiploid and relapsed ALL and as germline Li-Fraumeni mutations—drive chemoresistance and a poor prognosis.
- `connects-to` → **[Epstein-Barr Virus](../../../02-pathogen/01-viruses/epstein-barr-virus/README.md)** — Post-transplant lymphoproliferation: after allogeneic stem-cell transplant for high-risk ALL, EBV can drive post-transplant lymphoproliferative disorder under immunosuppression.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Immunosuppressed COVID: leukaemia and its chemotherapy or CAR-T immunosuppression cause severe, prolonged COVID-19 with blunted vaccine responses and reactivation risk.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Ph-like ALL: a high-risk subtype of B-ALL carries kinase fusions that activate JAK-STAT signalling, making JAK inhibitors a targeted strategy in this aggressive disease.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — Cell-cycle target: cyclin D-CDK4/6 drives the proliferation of lymphoblasts, and CDK4/6 inhibitors are being explored to restore cell-cycle control in acute lymphoblastic leukaemia.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Epigenetic dependency: EZH2 and the PRC2 complex enforce the repressive chromatin state of leukaemic blasts, an epigenetic vulnerability particularly in T-cell ALL.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — Lost cell-cycle brake: deletion of the CDKN2A tumour suppressor is among the most frequent lesions in ALL, removing the p16-mediated restraint on CDK4/6 and unleashing lymphoblast proliferation.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — Marrow-niche refuge: CXCL12 from bone-marrow stroma signals through CXCR4 to home and shelter leukaemic blasts in the protective niche, a mechanism of chemoresistance and minimal residual disease in ALL.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Survival signalling: PI3K-AKT activation, often via PTEN loss in T-cell ALL, drives the growth and survival of lymphoblasts and contributes to glucocorticoid resistance.
- `connects-to` → **[Menin (MEN1)](../../03-molecular/men1/README.md)** — KMT2A (MLL)-rearranged ALL, common and aggressive in infants, depends on the menin-MLL interaction to maintain leukemic HOX transcription—the target of menin inhibitors (revumenib) now entering ALL therapy.
- `connects-to` → **[FLT3](../../03-molecular/flt3/README.md)** — FLT3 is overexpressed or activated in KMT2A-rearranged and hyperdiploid ALL, a receptor tyrosine kinase under investigation as a therapeutic target in these high-risk and infant subtypes.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Glucocorticoids and chemotherapy kill lymphoblasts by triggering caspase-3-mediated apoptosis, and the speed of the early apoptotic response to prednisone is one of the strongest prognostic markers in childhood ALL.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — The CD19-CD3 bispecific blinatumomab and CD19 CAR-T cells redirect cytotoxic T cells to destroy B-ALL blasts through perforin and granzyme, the immune effector mechanism that has transformed relapsed and refractory disease.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — Lymphoblasts depend on IGF-1R signaling for proliferation and survival, a growth-factor axis that supports leukemic growth and is being explored as a therapeutic target in ALL.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors maintain quiescent leukemia-initiating cells that survive chemotherapy in the marrow niche, a reservoir that seeds the relapse which remains the main cause of treatment failure in ALL.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K-AKT-mTOR signaling (AKT and mTOR already mapped) is activated in acute lymphoblastic leukemia, especially T-ALL downstream of NOTCH and PTEN loss, supporting blast survival.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — RAS-MAPK-ERK activation, common in B-cell ALL and the Ph-like subtype, drives blast proliferation and is a target of MEK inhibition in resistant disease.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — Deregulated RB-E2F1 transcription (with the CDK4/6 and CDKN2A lesions already mapped) powers the unchecked proliferation of acute lymphoblastic leukemia blasts.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN loss unleashes the PI3K-AKT-mTOR axis (AKT and mTOR already mapped), a frequent driver of T-cell ALL that promotes leukemic-cell growth and survival.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — Activating RAS-pathway mutations (KRAS/NRAS) are among the most common lesions in B-cell ALL, driving the ERK-MAPK proliferative signaling (ERK1/2 already mapped) of the leukemic clone.
- `connects-to` → **[Wnt/beta-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Wnt/β-catenin signaling sustains the leukemia-initiating cells of ALL, contributing to the self-renewal and chemoresistance of the leukemic stem-cell compartment.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-β within the bone-marrow niche regulates leukemic-cell quiescence and chemoresistance in acute lymphoblastic leukemia.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Stromal and leukemic galectin-3 promotes the marrow-niche survival signaling and chemoresistance of acute lymphoblastic leukemia blasts.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α in the hypoxic bone-marrow niche supports the survival and metabolic adaptation of acute lymphoblastic leukemia cells.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the antileukemic immune response and immune-evasion balance of acute lymphoblastic leukemia, relevant to its immunotherapy.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING modulates the inflammatory and immune microenvironment of the bone marrow infiltrated by acute lymphoblastic leukemia.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling in the bone-marrow niche contributes to the immunosuppression and chemoprotection of acute lymphoblastic leukemia cells.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β supports leukemic stem-cell self-renewal and survival, a targetable dependency in acute lymphoblastic leukemia.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins from the leukemic bone-marrow myeloid compartment shape the inflammatory niche of acute lymphoblastic leukemia.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis and is a therapeutic target in acute lymphoblastic leukemia.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family (LYN/LCK) kinase signaling downstream of the pre-B-cell receptor and BCR-ABL supports the survival of acute lymphoblastic leukemia blasts.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of acute lymphoblastic leukemia.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival and chemoresistance of acute lymphoblastic leukemia blasts, a candidate therapeutic vulnerability.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of acute lymphoblastic leukemia, a candidate metabolic-therapy target.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-family chemokine signaling (CXCL12/CXCR4 already mapped) participates in the bone-marrow homing and CNS infiltration of acute lymphoblastic leukemia.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic dysregulation of acute lymphoblastic leukemia.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation in the bone-marrow niche contributes to the leukemic-cell maintenance of acute lymphoblastic leukemia.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the inflammatory bone-marrow microenvironment of acute lymphoblastic leukemia.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) participates in the bone-marrow microenvironment and survival signaling of acute lymphoblastic leukemia.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory bone-marrow microenvironment of acute lymphoblastic leukemia.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory bone-marrow microenvironment of acute lymphoblastic leukemia.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the antigen-receptor (pre-B-cell-receptor/T-cell-receptor) and survival signaling of acute lymphoblastic leukemia.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Tumour lysis syndrome: the rapid cell turnover of acute lymphoblastic leukaemia, especially on starting treatment, releases purines that xanthine oxidase converts to uric acid, causing the hyperuricaemia and urate nephropathy prevented by rasburicase and allopurinol.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Immunotherapy: antigen presentation shapes the T-cell response harnessed by the CD19-directed CAR-T cells and bispecific antibodies (perforin already mapped) that have transformed relapsed acute lymphoblastic leukaemia.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell expansion: IL-2 drives the proliferation of the engineered and endogenous T cells used against acute lymphoblastic leukaemia, and its release contributes to the cytokine-release syndrome seen with CAR-T therapy.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Marrow-failure anaemia: replacement of the marrow (already mapped) by lymphoblasts crowds out red-cell production, and the resulting anaemia with falling haemoglobin, alongside thrombocytopenia, presents acute lymphoblastic leukaemia.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Anthracycline cardiotoxicity: the anthracycline chemotherapy central to ALL regimens is cardiotoxic, and troponin elevation helps detect the cumulative myocardial injury that threatens the long-term survivors of this highly curable leukaemia.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Tumour-lysis acidosis: the high blast burden of ALL, lysed by induction chemotherapy, releases acids that, with lactate from the metabolic stress, produce the metabolic acidosis of tumour-lysis syndrome (potassium and urate already mapped).
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive marrow: IL-10 in the leukaemic marrow microenvironment dampens the anti-leukaemia T-cell response (MHC class II already mapped), part of the immune evasion that the CAR-T and bispecific immunotherapies of ALL aim to overcome.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Transfusional iron overload: the chronic red-cell transfusion support during intensive ALL therapy (haemoglobin already mapped) loads the body with iron, an overload burden that can require monitoring and chelation in the long-term survivor.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Marrow angiogenesis: increased bone-marrow (already mapped) microvascular density supported by VEGF is part of the altered leukaemic microenvironment that sustains the lymphoblastic clone in acute lymphoblastic leukaemia.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage niche: IL-4 polarises the marrow macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the leukaemic bone-marrow (already mapped) microenvironment that shelters the lymphoblasts of acute lymphoblastic leukaemia.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Marrow-adipocyte crosstalk: the marrow adipocytes and their adipokine adiponectin engage in metabolic crosstalk with the lymphoblasts, the marrow adipose tissue shaping the niche that sustains the clone in acute lymphoblastic leukaemia.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Adipokine marrow signalling: leptin, with adiponectin (already mapped), from the marrow adipose tissue signals to the leukaemic cells, part of the metabolic microenvironment and the chemoresistance of acute lymphoblastic leukaemia.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Tumour-lysis hypocalcaemia: the hyperphosphataemia of the tumour lysis syndrome at ALL induction binds calcium, causing the hypocalcaemia that accompanies the hyperkalaemia (already mapped) and needs monitoring.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — M2 marrow niche: IL-13, with IL-4 (already mapped), sustains the M2 marrow macrophages of the immunosuppressive niche that shelters the lymphoblasts of acute lymphoblastic leukaemia.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Marrow-adipocyte adipokine: resistin, with leptin and adiponectin (already mapped), is part of the marrow-adipocyte adipokine crosstalk that shapes the leukaemic niche and the chemoresistance of acute lymphoblastic leukaemia.
- `connects-to` → **[CML](../cml/README.md)** — Ph+ overlap: the Ph+ (BCR-ABL — ABL1 already mapped) ALL and the CML (lymphoid blast crisis) share the BCR-ABL fusion and the TKI (imatinib) therapy.
- `connects-to` → **[Burkitt lymphoma](../burkitt-lymphoma/README.md)** — Mature-B malignancy: the Burkitt lymphoma/leukaemia (MYC already mapped, the L3/mature-B ALL) is a related aggressive B-cell malignancy of the ALL spectrum.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Transfusion iron: the transfusion-dependent anaemia (haemoglobin already mapped) of the ALL and its chemotherapy loads the body with iron.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antileukaemic arm: the IFN-γ of the T and NK cells (perforin already mapped) is the type-II interferon arm of the anti-leukaemic immunity, relevant to the blinatumomab and CAR-T (T-cell already mapped) immunotherapy of ALL.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-leukaemic response of the ALL immune microenvironment.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate antileukaemic interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment relevant to the immunotherapy of ALL.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of the ALL marrow.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory bone-marrow (already mapped) microenvironment of ALL.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the ALL marrow microenvironment.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Antigen presentation: the dendritic cells present the leukaemia antigen (MHC already mapped) to the T cells (already mapped), shaping the immune microenvironment and the antileukaemic response of ALL.
- `connects-to` → **[Plasma cell](../../04-cellular/plasma-cell/README.md)** — B-cell aplasia: the normal plasma cells and their antibody (already mapped) output are lost with the CD19 (CD20 already mapped) CAR-T and blinatumomab therapy, causing the B-cell aplasia and hypogammaglobulinaemia of treated ALL.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — Complement C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) contributes to the myeloid inflammation and the cytokine-release-syndrome complement activation of the CAR-T therapy of ALL.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) are effectors of the antibody-mediated cytotoxicity and the cytokine-release-syndrome complement activation of the immunotherapy of ALL.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement evasion: the ALL blasts recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), tempering the complement attack within the marrow (already mapped) microenvironment.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Anaemia/iron overload: transferrin, the iron carrier, reflects the disordered iron handling of the marrow-failure anaemia and the transfusional iron overload of ALL.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-leukaemia axis: TSLP, from marrow stroma (already mapped) and thymic epithelium, drives CRLF2-rearranged ALL blasts and primes the marrow (already mapped) microenvironment for leukaemia-promoting Th2 skewing.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-marrow axis: bradykinin, via B1/B2 receptors on marrow endothelium (already mapped) and leukaemia blasts, amplifies the vascular permeability and the inflammatory cytokine milieu of the leukaemia marrow of ALL.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Erythropoietic failure: erythropoietin signalling is impaired by the marrow infiltration of the ALL blasts (already mapped), contributing to the hypoproliferative anaemia and the transfusion dependence of ALL.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell marrow niche: mast cells (already mapped) in the bone marrow (already mapped) niche of ALL release histamine that amplifies the vascular permeability and the inflammatory cytokine milieu that sustains the leukaemia-promoting microenvironment of ALL.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Oncostatic chronobiology: melatonin has pro-apoptotic and anti-proliferative effects on leukaemic cells; disrupted melatonin rhythm (common in paediatric cancer) amplifies the immune dysregulation (T-cell already mapped) and the oxidative stress of ALL.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement-contact regulation: C1-esterase inhibitor regulates the classical complement (C3, C5 and factor H already mapped) pathway exploited by ALL blasts for complement evasion and the leukaemia-promoting marrow-niche inflammatory activation.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — ALL testosterone: testosterone, via androgen receptors on bone-marrow (already mapped) stromal cells and leukaemic blasts, modulates marrow haematopoiesis; androgen-deprivation therapy amplifies the immunosuppressive (regulatory T cell already mapped) niche of ALL.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — ALL serotonin: serotonin, via 5-HT receptors on bone-marrow (already mapped) stromal cells and leukaemic blasts, modulates the immune microenvironment; serotonin dysregulation amplifies the IL-6 (already mapped) and IL-1β (already mapped) leukaemia-niche activation of ALL.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — ALL prolactin: prolactin, via PRLR on bone-marrow (already mapped) stromal cells and leukaemic blasts, promotes leukaemic cell survival; hyperprolactinaemia amplifies the IL-6 (already mapped) and NF-κB (already mapped) leukaemia-niche activation of ALL.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Leukaemia-niche immunomodulator: oxytocin, via OXTR on bone-marrow (already mapped) stromal cells and regulatory T cells (already mapped), modulates leukaemic-niche immune suppression; oxytocin deficiency amplifies the IL-6 (already mapped) and NF-κB (already mapped) activation of ALL.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Haematopoietic niche regulator: vasopressin, via V1aR on bone-marrow (already mapped) stromal cells and megakaryocyte progenitors (platelet already mapped), modulates haematopoiesis; vasopressin dysregulation amplifies the IL-6 (already mapped) and NF-κB (already mapped) leukaemia-niche of ALL.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Leukaemic ROS scavenger: selenium, as GPx in bone-marrow (already mapped) stromal cells and leukaemic blasts, scavenges ROS driving leukaemic proliferation; selenium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) leukaemia-niche inflammatory cascade of ALL.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — ALL sodium: sodium dysregulation in bone-marrow (already mapped) stroma and B-cell (already mapped) precursors amplifies ionic stress; osmotic changes worsen NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) leukaemic blast proliferation in ALL.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — ALL zinc: zinc cofactors macrophage (already mapped) anti-tumour function and B-cell (already mapped) homeostasis; zinc deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) leukaemic blast expansion in ALL.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — ALL copper: copper, via ceruloplasmin and SOD in macrophages (already mapped) and bone-marrow (already mapped) stroma, scavenges ROS; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) leukaemic proliferation in ALL.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — thyroid hormones (iodine-dependent) in B-cell (already mapped) precursors and macrophages (already mapped) modulate proliferative signalling; iodine deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) leukaemic blast expansion in ALL.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — chloride channels on B-cell (already mapped) precursors and bone-marrow (already mapped) stroma maintain ionic homeostasis; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) leukaemic blast proliferation in ALL.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — H2S from sulfur-amino acids in macrophages (already mapped) and bone-marrow (already mapped) stroma scavenges ROS promoting leukaemic blast apoptosis; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) blast expansion in ALL.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — ALL carbon: carbon, as metabolic backbone of purines and nucleotides in B-cell (already mapped) precursors and bone-marrow (already mapped) stroma, drives leukaemic blast expansion; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) in ALL.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — ALL hydrogen: hydrogen, via redox homeostasis in B-cell (already mapped) precursors and macrophages (already mapped), quenches leukaemic ROS; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) blast proliferation in ALL.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — ALL nitrogen: nitric oxide from iNOS in macrophages (already mapped) and bone-marrow (already mapped) stroma modulates niche homeostasis; nitrogen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) leukaemic cascade in ALL.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — ALL oxygen: mitochondrial oxygen in B-cell (already mapped) precursors and macrophages (already mapped) sustains ATP for leukaemic blast proliferation; hypoxia amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) cascade in ALL.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — ALL GLP-1: GLP-1 receptor signalling in macrophages (already mapped) and B-cell (already mapped) precursors modulates metabolic immune homeostasis; GLP-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) leukaemic cascade in ALL.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — ALL angiotensin-II: angiotensin-II signalling in macrophages (already mapped) and bone-marrow (already mapped) stroma promotes niche inflammation; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) cascade of ALL.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — ALL RANKL: RANKL in bone-marrow (already mapped) stromal cells and macrophages (already mapped) modulates the leukaemic niche bone-immune axis; RANKL excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of ALL.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — ALL fibronectin: fibronectin in bone-marrow (already mapped) extracellular matrix and macrophages (already mapped) modulates leukaemic blast adhesion; fibronectin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of ALL.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — ALL activin-A: activin-A from bone-marrow (already mapped) stromal cells and macrophages (already mapped) modulates haematopoietic differentiation; activin-A excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of ALL.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — ALL cgrp: CGRP from macrophages (already mapped) and bone-marrow stromal cells (already mapped) modulates leukaemic neuroimmune tone; cgrp excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of ALL.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — ALL calcitonin: calcitonin from macrophages (already mapped) and bone-marrow stromal cells (already mapped) modulates leukaemic calcium balance; calcitonin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of ALL.
- `connects-to` → **[Substance-P](../../03-molecular/substance-p/README.md)** — ALL substance-p: substance-P from macrophages (already mapped) and bone-marrow stromal cells (already mapped) modulates leukaemic nociceptive signalling; substance-P excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of ALL.
- `connects-to` → **[Insulin Receptor](../../03-molecular/insulin-receptor/README.md)** — ALL insulin-receptor: insulin receptor on macrophages (already mapped) and bone-marrow stromal cells (already mapped) modulates leukaemic metabolic axis; insulin-receptor excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of ALL.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — ALL aldosterone: aldosterone from macrophages (already mapped) and bone-marrow stromal cells (already mapped) modulates leukaemic fluid balance; aldosterone excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of ALL.
- `connects-to` → **[Androgen Receptor](../../03-molecular/androgen-receptor/README.md)** — ALL androgen-receptor: androgen receptor on macrophages (already mapped) and bone-marrow stromal cells (already mapped) modulates leukaemic sex tone; androgen-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of ALL.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — ALL norepinephrine: norepinephrine from macrophages (already mapped) and bone-marrow stromal cells (already mapped) modulates leukaemic adrenergic tone; norepinephrine excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of ALL.
- `connects-to` → **[Adrenomedullin](../../03-molecular/adrenomedullin/README.md)** — ALL adrenomedullin: adrenomedullin from macrophages (already mapped) and bone-marrow stromal cells (already mapped) modulates leukaemic vascular tone; adrenomedullin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of ALL.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — ALL bdnf: BDNF from macrophages (already mapped) and bone-marrow stromal cells (already mapped) sustains leukaemic neural-immune niche; BDNF deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of ALL.

[^pui-2018-all-cure]: Pui CH, Yang JJ, Bhakta N, et al. Global efforts toward the cure of childhood acute lymphoblastic leukemia. *Lancet Child Adolesc Health.* 2018;2(6):440-454. [doi:10.1016/S2352-4642(18)30066-X](https://doi.org/10.1016/S2352-4642(18)30066-X) · [PubMed 29976322](https://pubmed.ncbi.nlm.nih.gov/29976322/)
[^maude-2018-tisagenlecleucel]: Maude SL, Laetsch TW, Buechner J, et al. Tisagenlecleucel in children and young adults with B-cell lymphoblastic leukemia. *N Engl J Med.* 2018;378(5):439-448. [doi:10.1056/NEJMoa1709866](https://doi.org/10.1056/NEJMoa1709866) · [PubMed 29385370](https://pubmed.ncbi.nlm.nih.gov/29385370/)

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
