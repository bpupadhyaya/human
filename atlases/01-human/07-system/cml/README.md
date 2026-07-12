---
schema: human-scale-entry/v1
id: cml
name: Chronic Myeloid Leukemia
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Clonal myeloid leukemia driven by t(9;22)/BCR-ABL (Philadelphia chromosome); imatinib (IRIS trial) transformed CML from fatal to chronic; 5-year OS >85%. TKI-refractory T315I → ponatinib or asciminib; treatment-free remission achievable in ~50% of deep molecular responders."
aliases: ["CML", "chronic myelogenous leukemia", "Philadelphia chromosome leukemia", "BCR-ABL leukemia"]
sources:
  - id: druker-2006-iris-5year
    type: peer-reviewed
    cite: "Druker BJ, Guilhot F, O'Brien SG, et al. Five-year follow-up of patients receiving imatinib for chronic myeloid leukemia. N Engl J Med. 2006;355(23):2408-2417."
    doi: "10.1056/NEJMoa062867"
    pmid: "17151364"
    url: "https://doi.org/10.1056/NEJMoa062867"
  - id: hochhaus-2019-dasatinib
    type: peer-reviewed
    cite: "Hochhaus A, Saglio G, Hughes TP, et al. Long-term benefits and risks of frontline nilotinib vs imatinib for chronic myeloid leukemia in chronic phase: 5-year update of the randomized ENESTnd trial. Leukemia. 2016;30(5):1044-1054."
    doi: "10.1038/leu.2016.5"
    pmid: "26816503"
    url: "https://doi.org/10.1038/leu.2016.5"
cross_links:
  - target: 01-human/03-molecular/abl1
    relation: connects-to
    note: "CML is caused by BCR-ABL fusion (t(9;22)); ABL1 kinase domain is the drug target; imatinib/dasatinib/nilotinib/bosutinib inhibit ABL1; T315I gatekeeper → ponatinib or asciminib (STAMP); MR4.5 molecular response enables treatment-free remission attempts."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "BCR-ABL constitutively phosphorylates STAT5 (and STAT3) → transcription of BCL-XL, MYC, and cyclin D1 → blast survival and proliferation; STAT5 activation is a dominant signaling output of BCR-ABL; TKI response correlates with STAT5 dephosphorylation."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "BCR-ABL → PI3K-AKT → mTORC1 → S6K and 4EBP1 → protein synthesis and survival; mTOR pathway activation mediates imatinib resistance in some CML clones; dual PI3K-mTOR inhibitors studied as combination with TKIs in BCR-ABL-positive blast crisis."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "BCR-ABL activates SRC-family kinases (LYN, HCK, FGR) in CML; SRC kinases promote blast crisis transformation and TKI resistance; dasatinib and bosutinib inhibit both ABL and SRC-family kinases — dual ABL/SRC inhibition relevant in lymphoid blast crisis."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "BCR-ABL → PI3K → AKT → mTOR → S6K/4EBP1 → protein synthesis and cell survival; AKT phosphorylates BAD → prevents apoptosis in CML cells; imatinib resistance associated with PI3K/AKT activation independent of BCR-ABL; AKT inhibition synergizes with TKIs in blast crisis CML."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "BCR-ABL → STAT5/NF-κB → MYC transcription → G1/S acceleration; MYC amplification is common in blast crisis transformation; MYC overexpression promotes self-renewal of CML LSCs; BRD4 inhibitors (JQ1) reduce MYC expression and overcome TKI resistance in CML blast crisis models."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "RB1 inactivated in CML blast crisis via CDK4/6 hyperactivation; E2F release drives myeloid or lymphoid blast transformation; BCR-ABL accelerates CDK2-mediated RB1 inactivation; palbociclib (CDK4/6 inhibitor) re-engages RB1 and sensitizes TKI-resistant blast crisis to apoptosis."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "CML is defined by uncontrolled expansion of the neutrophil lineage: BCR-ABL drives massive leukocytosis with granulocytes at all maturation stages and hallmark basophilia; unlike normal neutrophils they retain function early, so infection is not the initial problem."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "The CML marrow is markedly hypercellular with a high myeloid:erythroid ratio and 'dwarf' megakaryocytes; the Philadelphia chromosome t(9;22) is detected here, and marrow blast percentage defines chronic phase (<10%), accelerated (10-19%), and blast crisis (≥20%)."
  - target: 01-human/07-system/cll
    relation: connects-to
    note: "CLL and CML are the two chronic adult leukemias from opposite lineages: CLL is a B-lymphoid accumulation of mature CD5+ cells driven by BCR/BTK signaling, while CML is a myeloid proliferation driven by the BCR-ABL fusion kinase — different cells, drivers, and targeted drugs."
  - target: 01-human/07-system/myeloproliferative-neoplasms
    relation: connects-to
    note: "CML is the BCR-ABL1-positive classic myeloproliferative neoplasm: like PV, ET and myelofibrosis it is a clonal stem-cell overproduction of mature myeloid cells, but its Philadelphia chromosome and exquisite TKI sensitivity set it apart from the JAK2/CALR-driven MPNs."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "CML's natural history is progression to acute leukemia: untreated, the chronic phase accelerates into a blast crisis that behaves like acute leukemia—myeloid (AML-like) in ~70%, lymphoid in the rest—so TKI therapy aims to prevent this transformation, which remains hard to treat."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "Splenomegaly is a hallmark of CML: massive extramedullary myeloid proliferation enlarges the spleen, causing early satiety and left-upper-quadrant pain at presentation; spleen size featured in old prognostic scores and shrinks rapidly once tyrosine-kinase inhibitors control it."
  - target: 01-human/07-system/all
    relation: connects-to
    note: "CML and Philadelphia-positive ALL are united by the BCR-ABL fusion: the same t(9;22) drives chronic myeloid leukemia and a subset of acute lymphoblastic leukemia, so BCR-ABL tyrosine kinase inhibitors treat both—though Ph+ ALL is far more aggressive."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "CML often presents with a high platelet count alongside leukocytosis: the BCR-ABL clone expands the megakaryocyte lineage too, so thrombocytosis and basophilia accompany the neutrophilia—distinguishing CML from reactive leukocytosis and sometimes causing thrombosis."
  - target: 01-human/07-system/mds
    relation: connects-to
    note: "CML and MDS sit at opposite poles of clonal myeloid disease: CML is a proliferative BCR-ABL-driven overproduction of mature myeloid cells, while MDS is a dysplastic, cytopenia-causing marrow failure—but both are clonal stem-cell disorders that can progress to AML."
  - target: 01-human/03-molecular/jak2
    relation: connects-to
    note: "CML and JAK2-driven neoplasms are mirror-image myeloproliferative diseases: CML is defined by the BCR-ABL fusion kinase, while polycythemia vera and kin are driven by JAK2 mutations—both activate growth signaling, so testing distinguishes them and guides therapy."
  - target: 01-human/07-system/polycythemia-vera
    relation: connects-to
    note: "CML and polycythemia vera are both myeloproliferative neoplasms but molecularly distinct: CML is BCR-ABL-positive and treated with TKIs, while PV is JAK2-mutant with red-cell overproduction—yet both feature splenomegaly and a risk of transforming to acute leukemia."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "CML enlarges the liver and spleen via extramedullary hematopoiesis: massive granulocyte overproduction and organ infiltration cause hepatosplenomegaly, often with early satiety from a huge spleen—signs that regress dramatically once TKI therapy controls the clone."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "CML disturbs red-cell production amid the myeloid overgrowth: marrow packed with granulocyte precursors crowds erythropoiesis, so anemia is common at diagnosis even as white cells soar—part of the imbalance the BCR-ABL clone imposes on blood formation."
  - target: 01-human/07-system/gout
    relation: connects-to
    note: "CML can trigger gout through high cell turnover: the massive proliferation and breakdown of leukemic cells floods the blood with uric acid, which crystallizes in joints, so hyperuricemia and gout—or urate kidney stones—accompany the disease and its treatment."
  - target: 01-human/07-system/essential-thrombocythemia
    relation: connects-to
    note: "CML and essential thrombocythemia are both myeloproliferative neoplasms but driven by different lesions: CML by BCR-ABL, ET usually by JAK2/CALR/MPL, so the Philadelphia chromosome distinguishes CML from the BCR-ABL-negative MPNs in the differential."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "CML pioneered treatment-free remission through the immune system: after deep response to TKIs, some patients stop the drug and stay in remission, because immune surveillance appears to hold residual leukemic stem cells in check."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Cytotoxic T and NK cells help control CML: immune effectors recognize leukemia-associated antigens, contributing to deep responses and the durability of treatment-free remission—so immunity complements the TKIs that block BCR-ABL."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Ionizing radiation can cause CML: survivors of the atomic bombs had sharply higher CML rates, evidence that X-ray and gamma photons damaging blood stem cells can create the BCR-ABL translocation that drives the disease."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "CML's stem cells survive TKIs by autophagy: leukemic stem cells recycle their contents to weather imatinib, so they persist despite a controlled blood count—why combining TKIs with autophagy blockers is studied to enable treatment-free remission."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "NK cells help control CML and predict cure: robust natural killer activity is linked to keeping leukemia in check, and patients with strong NK responses are likelier to stay in remission after stopping their TKI."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "CML's huge white-cell counts can fake high potassium: massive numbers of leukocytes and platelets leak potassium after blood is drawn, producing pseudohyperkalemia—a lab artifact to recognize before treating a number that isn't real in the body."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Wnt/beta-catenin keeps CML's stem cells alive: this pathway sustains the leukemic stem cells that survive BCR-ABL inhibitors, so it helps explain why the disease persists on therapy and can progress to blast crisis."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "CML can poison the kidneys through tumor lysis: the huge white-cell mass releases uric acid that, especially as treatment kills cells, crystallizes in the kidney and causes urate nephropathy, linking the leukemia to gout and renal injury."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells can spring from the CML clone itself: because the leukemia is a stem cell disease, even antigen-presenting cells carry BCR-ABL, and harnessing dendritic cells is explored to boost immune control after drug therapy."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Extreme CML counts can starve tissues of oxygen: when white cells soar, the sludgy blood (leukostasis) clogs small vessels, so organs are starved of oxygen—an emergency needing urgent cytoreduction."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "CML leukostasis can strike the brain: a sky-high white-cell mass sludges cerebral vessels, causing headaches, confusion, strokes, and visual loss, the neurologic face of hyperleukocytosis."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "CML's clone reaches into the macrophage lineage: because BCR-ABL arises in a myeloid stem cell, the expanded output includes monocytes and macrophages, part of the broad granulocytic overgrowth that defines the disease."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "CML's high cell turnover spills purines and phosphate: hyperuricemia causes the gout it is known for, and tumor lysis at blast crisis or on treatment releases phosphate and potassium."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "CML's huge white-cell mass clogs the eye's vessels: leukostasis causes retinal hemorrhages and engorged veins, visible on fundoscopy as a warning sign of dangerous hyperleukocytosis."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "CML can scar its marrow: reticulin and collagen fibrosis increase as the disease progresses and predict a worse response, blurring the line toward myelofibrosis."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows CML's overflowing granulocyte line: the marrow and blood teem with neutrophils at every stage of maturation plus a telltale rise in basophils, the expanded myeloid spectrum that the BCR-ABL kinase drives."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "A sky-high white count can clog the lungs: in CML's accelerated phase, leukostasis from the sheer mass of circulating cells sludges the pulmonary vessels, causing breathlessness and respiratory distress."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "CML can surface on the skin: leukemia cutis deposits tumor cells in the skin, and the neutrophilic Sweet syndrome can erupt with fever and tender plaques, sometimes heralding transformation to blast crisis."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "The targeted drugs that tamed CML can wound the vessels: the newer TKIs — nilotinib and especially ponatinib — drive arterial thrombosis, hypertension, and cardiac events, a vascular toll weighed against their potency."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Lifelong TKI therapy collides with childbearing: imatinib and its successors are teratogenic, so conception must be planned around treatment interruptions, a central concern now that CML is a chronic, survivable disease."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "The pills upset the gut: diarrhea is among the commonest TKI side effects — pronounced with bosutinib — and managing it is part of keeping patients on the daily therapy that controls the leukemia."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Some TKIs injure the vessel lining: nilotinib and ponatinib damage endothelial cells and accelerate atherosclerosis, raising the risk of arterial occlusion, peripheral artery disease and heart attack — the vascular toxicity that shapes which drug a CML patient receives."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-beta hides CML from cure: it keeps the leukemic stem cells quiescent through FOXO signaling, and these dormant cells survive even deep BCR-ABL inhibition — why most patients must keep taking TKIs and why stem-cell-targeting strategies are sought."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Long-term imatinib reshapes bone mineral handling: by blocking PDGFR and KIT on bone cells it lowers bone turnover and can disturb calcium and phosphate balance, an under-recognized metabolic effect of years on TKI therapy."
  - target: 01-human/07-system/gvhd
    relation: connects-to
    note: "Transplant was CML's first cure: before TKIs, allogeneic stem-cell transplant offered the only cure through its graft-versus-leukemia effect, at the cost of graft-versus-host disease — still the fallback for TKI-resistant or blast-crisis disease."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "The immune system can help hold CML down: regulatory T cells that blunt anti-leukemia immunity rise with disease, and their balance shapes the immune control that lets some patients stop TKIs and stay in remission."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Inflammation feeds the leukemic niche: BCR-ABL drives IL-6 release that remodels the marrow microenvironment to favor the leukemic stem cells over normal hematopoiesis."
  - target: 01-human/07-system/myelofibrosis
    relation: connects-to
    note: "CML can scar the marrow it fills: marrow fibrosis develops with advanced or accelerated disease and, like primary myelofibrosis, reflects the megakaryocyte-driven, cytokine-rich stroma of a myeloproliferative neoplasm."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Blast crisis leans on anti-apoptosis: BCR-ABL props up BCL-2-family survival signals, and adding the BCL-2 inhibitor venetoclax to a TKI is a strategy to kill the resistant blasts of advanced-phase CML."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Extreme white counts can clog the brain's vessels: the massive leukocytosis of CML can cause leukostasis, a hyperviscosity emergency that sludges cerebral flow and can present as stroke before the diagnosis is even known."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "BCR-ABL routes survival through NF-κB: the fusion kinase activates NF-κB among its downstream pathways, supporting leukemic-cell survival and contributing to the resistance that emerges in advanced-phase disease."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Some of its drugs damage vessels: the later-generation TKIs nilotinib and especially ponatinib cause arterial and venous vascular events, so thrombosis is a recognized hazard of long-term CML therapy."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Advanced disease strips the defenses: blast crisis and its intensive chemotherapy cause the neutropenia and immune failure that make febrile neutropenia and sepsis a danger in progressive CML."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "One of its drugs scars the lung vessels: dasatinib, a second-generation TKI for CML, causes pleural effusions and a reversible pulmonary arterial hypertension, a distinctive class toxicity needing monitoring."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Later TKIs strain the heart: nilotinib and ponatinib used in CML carry cardiovascular toxicity — arterial events, hypertension and cardiac dysfunction — that can contribute to heart failure over long-term therapy."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Lifelong treatment weighs on mood: the open-ended daily TKI therapy, its chronic side effects and the psychological weight of living with leukemia contribute to depression and reduced quality of life in CML."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Some of its TKIs harden the arteries: nilotinib and ponatinib used for CML accelerate atherosclerosis and cause arterial occlusive events, a major vascular toxicity of these later-line drugs."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Marrow crowding and TKIs lower the count: the expanded myeloid clone and the myelosuppression of tyrosine-kinase inhibitor therapy can produce an anemia with a chronic-disease component."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Blast crisis and its chemo open the lung to mold: progression of CML to blast crisis requires intensive chemotherapy that causes deep neutropenia, allowing inhaled Aspergillus to invade."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Its TKIs and big spleen upset the gut: tyrosine-kinase inhibitors cause nausea, diarrhoea and hepatotoxicity, and the massive splenomegaly of CML presses on the stomach causing early satiety."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Its targeted drugs mark the skin: imatinib and other TKIs commonly cause rashes and periorbital oedema, and they can characteristically lighten skin pigmentation through KIT inhibition."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Lifelong therapy and PCR monitoring breed worry: the indefinite tyrosine-kinase-inhibitor treatment and the scrutiny of molecular-response blood tests in CML foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It massively swells the spleen: overproduction of myeloid cells enlarges the spleen, often dramatically, causing early satiety and left-upper-quadrant pain with risk of splenic infarction."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "One of its drugs floods the chest: the tyrosine-kinase inhibitor dasatinib characteristically causes pleural effusions, sometimes large and recurrent, requiring dose change or drainage."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Its inhibitors disturb metabolism: nilotinib can raise blood glucose and cause hyperglycaemia, and tyrosine-kinase inhibitors affect thyroid function and growth in children."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its newer drugs clog arteries: TKIs like nilotinib and ponatinib raise the risk of arterial occlusive events — peripheral arterial disease, heart attack and stroke — needing cardiovascular monitoring."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Treatment aches in muscle and bone: imatinib commonly causes muscle cramps and bone-aching, and the expanding marrow of untreated CML brings bone pain."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Rapid cell turnover and drugs reach the kidney: tumour lysis at the start of therapy and the nephrotoxicity of some TKIs can impair kidney function."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "The archetype of targeted therapy: BCR-ABL1 tyrosine-kinase inhibitors (imatinib and successors) turned CML from fatal into a chronic, often treatment-free-remission disease, the founding success of precision oncology."
  - target: 01-human/07-system/gist
    relation: connects-to
    note: "A shared imatinib target: gastrointestinal stromal tumour, driven by KIT, responds to imatinib just as BCR-ABL-driven CML does, the same drug treating two unrelated cancers."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Before and beyond the TKIs: hydroxyurea, busulfan and interferon controlled CML before imatinib, and intensive chemotherapy is still needed if it transforms to blast crisis."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "Its drugs harm the arteries: the TKIs that control CML, especially nilotinib and ponatinib, accelerate atherosclerosis and cause arterial occlusive events — peripheral, coronary and cerebral — a key long-term toxicity to monitor."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Marrow overgrowth aches the bones: the massive myeloid hyperplasia of CML expands the marrow and can cause bone pain, while high cell turnover and infiltration stress the skeleton."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "TKIs can stress the heart: beyond arterial events, CML tyrosine-kinase inhibitors cause fluid retention, QT prolongation and, with ponatinib, heart failure, so cardiac function is monitored during long-term therapy."
  - target: 01-human/07-system/cmml
    relation: connects-to
    note: "Ph-negative myeloproliferation: CMML is a myelodysplastic/myeloproliferative overlap that lacks the BCR-ABL fusion of CML, the key distinction in a patient with leukocytosis, monocytosis and splenomegaly."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Extramedullary disease in the liver: in advanced or blast-phase CML, leukaemic cells and extramedullary haematopoiesis infiltrate the hepatic lobule, contributing to hepatomegaly."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "A price of long-term TKIs: the BCR-ABL inhibitor nilotinib raises blood glucose and worsens insulin resistance, so diabetes and arterial disease are monitored during the chronic therapy that now makes CML survivable."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "TKI cardiac effects: BCR-ABL inhibitors like nilotinib prolong the QT interval and (with ponatinib) provoke vascular events, disturbing the cardiac conduction system during long-term therapy."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Dasatinib's pleural effusions: the second-generation TKI dasatinib commonly causes pleural effusions, fluid collecting around the lung's alveolar surface—a class-specific toxicity needing dose adjustment."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "An unexpected antiviral angle: BCR-ABL TKIs like imatinib were studied as COVID-19 therapeutics for their effects on viral entry and inflammation, and CML patients on TKIs largely tolerated infection well."
  - target: 01-human/03-molecular/kit
    relation: connects-to
    note: "Off-target reach: imatinib and nilotinib also inhibit KIT, which is why these BCR-ABL drugs are effective in GIST and mast-cell disease—the same kinase explains some of their side effects."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "Survival signal switched off: BCR-ABL drives PI3K-AKT signalling that inactivates FOXO transcription factors, suppressing apoptosis and quiescence and helping leukaemic stem cells persist under therapy."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Protective hypoxic niche: HIF-1α-driven adaptation in the hypoxic bone-marrow niche shelters CML stem cells from TKIs, contributing to disease persistence and relapse on stopping treatment."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Blast-crisis epigenetics: EZH2 and PRC2 enforce a repressive chromatin state that contributes to the progression of CML from chronic phase to aggressive blast crisis."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Cell-cycle drive: BCR-ABL signalling upregulates cyclin D and the cell-cycle machinery, pushing myeloid progenitors into the expanded proliferation of chronic myeloid leukaemia."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Marrow angiogenesis: BCR-ABL raises VEGF, increasing bone-marrow microvessel density to support the expanded leukaemic population of CML."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "RAS-ERK signalling: BCR-ABL constitutively activates the RAS-RAF-ERK cascade, a key proliferative output of the fusion kinase driving the myeloid expansion of chronic myeloid leukaemia."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Stem-cell niche: CXCL12-CXCR4 signalling anchors leukaemic stem cells in the protective marrow niche, a sanctuary that shelters quiescent CML cells from tyrosine-kinase inhibitors."
  - target: 01-human/03-molecular/runx1
    relation: connects-to
    note: "Blast-crisis transformation: acquired RUNX1 alterations contribute to the progression of chronic-phase CML to the aggressive, treatment-resistant blast crisis."
  - target: 01-human/03-molecular/smo
    relation: connects-to
    note: "Stem-cell maintenance: Hedgehog signalling through Smoothened sustains the leukaemic stem cells that persist beneath TKI therapy in CML, the reservoir responsible for relapse after treatment discontinuation."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "TKI-induced apoptosis: imatinib and later BCR-ABL inhibitors kill CML cells by relieving the fusion kinase's block on caspase-3-mediated apoptosis, restoring the cell-death programme the oncoprotein suppresses."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Telomere shortening: progressive telomere attrition and telomerase changes accompany the evolution of chronic-phase CML toward blast crisis, reflecting the genomic instability of disease progression."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Graft-versus-leukaemia: CML was the disease in which donor T- and NK-cell perforin-mediated killing of leukaemic cells — graft-versus-leukaemia, the basis of donor lymphocyte infusion — was first proven curative, the paradigm of cellular immunotherapy."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "Clonal evolution: additional mutations such as DNMT3A acquired on the BCR-ABL background drive the progression of chronic-phase CML to accelerated phase and blast crisis, the transformation that TKIs do not by themselves prevent."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "Blast-crisis p53: TP53 inactivation, often through MDM2 overexpression, accompanies the transformation of CML to blast crisis, removing the apoptotic brake and conferring the resistance that makes advanced-phase disease so hard to treat."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "RAS-MAPK output: BCR-ABL1 activates RAS, driving the MAPK-ERK cascade (ERK1/2 already mapped) that is a core proliferative output of the Philadelphia-chromosome fusion kinase."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "Survival arm: BCR-ABL1 engages PI3K, initiating the AKT-mTOR signalling (both already mapped) that provides the survival limb cooperating with proliferative RAS-MAPK and JAK-STAT signalling in CML."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Cell-cycle drive: BCR-ABL1 signalling pushes the cyclin-D1-RB axis (cyclin-D1 and RB1 already mapped) to release E2F1, and CDKN2A loss in lymphoid blast crisis further unleashes this proliferative transcription."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "Blast-crisis transformation: TP53 inactivation drives the transformation from chronic phase to the aggressive, treatment-resistant blast crisis of CML."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "Lymphoid blast crisis: CDKN2A/p16 deletion is a recurrent lesion in the progression of CML to lymphoid blast crisis, removing a cell-cycle brake on the proliferating clone."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "TKI resistance: NRF2 antioxidant signalling protects CML cells — including leukemic stem cells — from oxidative stress and contributes to resistance against tyrosine-kinase inhibitors."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 in the bone-marrow niche promotes leukemic-stem-cell survival and tyrosine-kinase-inhibitor resistance in chronic myeloid leukemia."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN restraint of PI3K-AKT-mTOR signalling (AKT, PIK3CA and mTOR mapped) downstream of BCR-ABL shapes CML-cell proliferation and survival."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β and FOXO mapped) maintains the quiescent leukemic stem cells that resist BCR-ABL-targeted therapy in CML."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling underlies the antileukemic effect of interferon-α, a historic and adjunctive therapy in chronic myeloid leukemia."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING modulates the inflammatory bone-marrow microenvironment of chronic myeloid leukemia."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6-cyclin-D activity (cyclin-D1 and RB1 already mapped) drives the cell-cycle progression downstream of BCR-ABL in chronic myeloid leukemia."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β misregulation in CML blast crisis impairs myeloid differentiation and supports leukemic stem-cell self-renewal."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the inflammatory bone-marrow niche of chronic myeloid leukemia."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK1/2-STAT5 signaling (JAK2 and STAT3 already mapped) is co-opted by BCR-ABL to sustain leukemic survival in chronic myeloid leukemia."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation and quiescence of the leukemic stem cells of chronic myeloid leukemia."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "CCL2-driven monocyte and macrophage recruitment contributes to the inflammatory bone-marrow niche of chronic myeloid leukemia."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "NOTCH signaling participates in the maintenance of the leukemic stem cells of chronic myeloid leukemia."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-family chemokine signaling (CXCL12/CXCR4 already mapped) participates in the bone-marrow homing and microenvironment of chronic myeloid leukemia."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic dysregulation of chronic myeloid leukemia."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β signaling in the bone-marrow niche contributes to the leukemic stem-cell maintenance and inflammatory microenvironment of chronic myeloid leukemia."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the inflammatory bone-marrow microenvironment of chronic myeloid leukemia."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory bone-marrow microenvironment of chronic myeloid leukemia."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory microenvironment of chronic myeloid leukemia."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the leukemic-stem-cell and immune signaling of chronic myeloid leukemia."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine signaling participates in the immunosuppressive bone-marrow microenvironment of chronic myeloid leukemia."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin participates in the leukemic-stem-cell-niche and bone-marrow-microenvironment interactions of chronic myeloid leukemia."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immune control and remission: CML is the model for treatment-free remission, where MHC-restricted T-cell and NK responses against the BCR-ABL-driven clone help maintain remission after stopping tyrosine-kinase inhibitors."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Hyperuricaemia: the high cell turnover of chronic myeloid leukaemia releases purines that xanthine oxidase converts to uric acid, causing the hyperuricaemia and gout risk managed with allopurinol at diagnosis and during cytoreduction."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Immune surveillance: IL-2 drives the expansion of the T and NK cells that provide the immunological control believed to sustain treatment-free remission in chronic myeloid leukaemia after tyrosine-kinase-inhibitor withdrawal."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Anaemia: marrow crowding by the leukaemic clone and, later, transformation lower haemoglobin, and the anaemia adds to the fatigue of chronic myeloid leukaemia, usually improving as tyrosine-kinase inhibition restores normal haematopoiesis."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "TKI vascular toxicity: nilotinib and ponatinib cause arterial-occlusive and cardiac events, and troponin elevation marks the myocardial injury of the vascular toxicity that shapes tyrosine-kinase-inhibitor selection in CML."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Nilotinib hyperglycaemia: nilotinib impairs glucose handling and raises the risk of hyperglycaemia and diabetes through effects on insulin signalling, a metabolic toxicity that factors into tyrosine-kinase-inhibitor choice in CML."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "TKI endothelial toxicity: ponatinib and nilotinib impair endothelial nitric oxide and function, promoting the arterial-occlusive and cardiovascular events (troponin already mapped) that are a defining toxicity shaping tyrosine-kinase-inhibitor selection in CML."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Nilotinib dyslipidaemia: nilotinib raises cholesterol and drives an atherogenic dyslipidaemia that, with its glucose effects (insulin already mapped), contributes to the vascular risk of the second-generation tyrosine-kinase inhibitors in CML."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Anaemia and transfusion: the marrow disruption of CML and its tyrosine-kinase-inhibitor therapy causes anaemia (haemoglobin already mapped) that can require transfusion, whose repeated support can load the body with iron."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage niche: IL-4 polarises the marrow macrophages toward an M2 phenotype that helps shelter the leukaemic stem cells in the bone-marrow (already mapped) microenvironment of CML."
  - target: 01-human/03-molecular/pf4
    relation: connects-to
    note: "Thrombocytosis and platelets: CML commonly raises the platelet count, and platelet factor 4 from the expanded, sometimes dysfunctional platelets reflects the thrombo-haemorrhagic dimension of the myeloproliferation."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Marrow adipose crosstalk: the marrow adipocytes and their adipokine leptin signal to the leukaemic stem cells, part of the bone-marrow (already mapped) microenvironment that influences the persistence of the CML clone."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Marrow-adipocyte adipokine: adiponectin, with leptin (already mapped), from the marrow adipose tissue signals to the leukaemic stem cells of the bone-marrow (already mapped) microenvironment of CML."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipokine milieu: resistin, with leptin and adiponectin (already mapped), completes the marrow-adipocyte adipokine signalling of the microenvironment influencing the CML clone."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Anaemia and transfusion iron: the anaemia (haemoglobin already mapped) of CML and the iron overload of the transfusion support during the blast-phase treatment reflect the disturbed iron handling of the leukaemia."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Thrombocytosis: CML often causes the thrombocytosis (the megakaryocytic proliferation; PF4 already mapped), part of the myeloproliferation of the leukaemia."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "Myeloid blast crisis: CML can transform to the acute myeloid leukaemia (the myeloid blast crisis; RUNX1 already mapped), a terminal accelerated phase."
  - target: 01-human/07-system/all
    relation: connects-to
    note: "Lymphoid blast crisis: CML can also transform to a lymphoid (Ph+ ALL-like) blast crisis (ABL1 already mapped), treated as the Ph+ ALL."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "IFN-α therapy/immune control: the type-I interferon (IFN-α) was the pre-TKI standard therapy of CML and, downstream of cGAS-STING (already mapped), underlies the immune surveillance relevant to the treatment-free remission."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 anti-leukaemic arm: the IFN-γ of the T and NK cells (perforin already mapped) is the type-II interferon arm of the anti-leukaemic immunity relevant to the immune control of CML."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of chronic myeloid leukaemia."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of chronic myeloid leukaemia (and the eosinophilia of some myeloproliferative overlaps)."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 arm: IL-13, with IL-4 (already mapped), completes the type-2 immune arm of the immune microenvironment of chronic myeloid leukaemia."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory bone-marrow (already mapped) microenvironment of chronic myeloid leukaemia."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) links the complement to the myeloid inflammation of the chronic-myeloid-leukaemia bone-marrow (already mapped) microenvironment."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Basophil/mast lineage: the mast cells, sharing the myeloid basophil lineage that is expanded (the basophilia) in chronic myeloid leukaemia, are part of the leukaemic myeloid output."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Immune surveillance: the CD4 T-helper cells contribute to the antileukaemic immunity that supports the treatment-free remission after the tyrosine-kinase-inhibitor therapy of chronic myeloid leukaemia."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) are part of the myeloid inflammatory dimension of the chronic-myeloid-leukaemia marrow microenvironment."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the inflammatory marrow niche of chronic myeloid leukaemia."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Leukaemia iron: transferrin, the iron carrier, reflects the disordered iron handling of the anaemia and the high cell turnover of chronic myeloid leukaemia."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-marrow axis: TSLP, from marrow stromal cells and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2/Treg imbalance of the inflammatory leukaemia marrow microenvironment of CML."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-marrow axis: bradykinin, via B1/B2 receptors on marrow endothelium (already mapped) and BCR-ABL-driven stromal cells, amplifies the vascular permeability and the cytokine milieu of the CML marrow microenvironment."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Erythropoietic failure: the BCR-ABL-driven CML leukaemia marrow (already mapped) displaces the normal erythropoiesis, and erythropoietin supports the management of the anaemia of CML."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell CML marrow axis: histamine, from the expanded mast-cell pool (already mapped) in the CML marrow niche, amplifies the BCR-ABL-driven (already mapped) angiogenesis (already mapped) and the inflammatory cytokine milieu of the CML stroma."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian-BCR-ABL axis: melatonin, via MT1/MT2 receptors on CML haematopoietic progenitors (already mapped), modulates the oxidative stress of the BCR-ABL-driven (already mapped) clonal expansion and the inflammatory marrow niche of CML."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical complement regulation: the C1-esterase inhibitor regulates the classical complement pathway (C5 and C5aR1 already mapped) whose activation contributes to the inflammatory leukaemia marrow microenvironment of chronic myeloid leukaemia."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "CML testosterone: testosterone, via androgen receptors on macrophages (already mapped) and T-cytotoxic cells (already mapped), modulates the CML TME; testosterone deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) BCR-ABL survival cascade of CML."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "CML serotonin: serotonin, via 5-HT receptors on macrophages (already mapped) and mast cells (already mapped), modulates the CML TME; serotonin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) BCR-ABL cascade of CML."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "CML prolactin: prolactin, via PRLR on macrophages (already mapped) and mast cells (already mapped), promotes CML immune escape; hyperprolactinaemia amplifies the NF-κB (already mapped) and IL-6 (already mapped) leukaemic survival cascade of CML."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "CML oxytocin: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates the BCR-ABL (already mapped)-driven TME inflammation; oxytocin deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) leukaemic survival cascade of CML."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "CML vasopressin: vasopressin, via V1aR on macrophages (already mapped) and mast cells (already mapped), modulates the CML marrow vascular milieu; vasopressin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) BCR-ABL cascade of CML."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "CML selenium: selenium, as GPx in macrophages (already mapped) and T-cytotoxic cells (already mapped), scavenges BCR-ABL-driven ROS; selenium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) oxidative leukaemia cascade of CML."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "CML iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) polarisation and T-cytotoxic (already mapped) surveillance; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) BCR-ABL leukaemia cascade of CML."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "CML sodium: sodium dysregulation in macrophages (already mapped) and leukaemic stem cells (already mapped) amplifies ionic stress; osmotic changes worsen NF-κB (already mapped) and IL-6 (already mapped) and BCR-ABL tumour-promoting cascade of CML."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "CML magnesium: magnesium cofactors kinase signalling in macrophages (already mapped) and T-cytotoxic cells (already mapped); magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCR-ABL leukaemic signalling cascade of CML."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "copper, via SOD in macrophage (already mapped) and T-cytotoxic cell (already mapped), counters BCR-ABL-driven ROS; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCR-ABL leukaemic cascade of CML."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "zinc cofactors kinase signalling in macrophage (already mapped) and T-cytotoxic cell (already mapped); zinc deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCR-ABL leukaemic survival cascade of CML."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "chloride channels on macrophage (already mapped) and leukaemic stem cell (already mapped) regulate membrane potential; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCR-ABL cascade of CML."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "CML carbon: carbon backbone of nucleotides in macrophages (already mapped) and leukaemic stem cells (already mapped) fuels tumour proliferation; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCR-ABL leukaemic cascade of CML."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "CML hydrogen: hydrogen via ROS from macrophages (already mapped) and leukaemic stem cells (already mapped) modulates redox homeostasis; hydrogen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCR-ABL leukaemic cascade of CML."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "CML nitrogen: nitrogen in DNA bases of macrophages (already mapped) and leukaemic stem cells (already mapped) sustains tumour growth; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCR-ABL leukaemic cascade of CML."
---

# Chronic Myeloid Leukemia

## Overview

**Chronic myeloid leukemia (CML)** is a clonal myeloproliferative neoplasm defined by the **Philadelphia chromosome** — the translocation t(9;22)(q34;q11.2) — which fuses the *BCR* gene on chromosome 22 with the *ABL1* gene on chromosome 9, creating the **BCR-ABL1 fusion oncoprotein**. The Philadelphia chromosome is present in >95% of CML and is both the defining molecular event and the therapeutic target [^druker-2006-iris-5year].

**Epidemiology:**
- Incidence: ~2/100,000 per year; ~9,000 new cases/year in the United States
- Median age at diagnosis: ~55-60 years; can occur at any age
- Accounts for ~15% of all adult leukemias

**Natural history (without treatment):**
- **Chronic phase (CP):** Most patients present here (~90%); WBC markedly elevated with left-shifted myeloid maturation; splenomegaly; blasts <10% in blood/marrow; relatively indolent, median duration 3-5 years without effective treatment
- **Accelerated phase (AP):** Blasts 10-19% in blood/marrow, basophilia >20%, thrombocytopenia unrelated to therapy, clonal evolution; intermediate
- **Blast crisis (BC):** Blasts ≥20% in blood/marrow; myeloid BC (~70%) or lymphoid BC (~30%); resembles acute leukemia; historically median survival <6 months without allogenic SCT

**Treatment-free remission (TFR):**
Following the imatinib revolution, the current frontier is achieving **deep molecular response (DMR)**: MR4 (BCR-ABL1/ABL1 ≤0.01% IS) or MR4.5 (≤0.0032% IS). Approximately 50% of patients who discontinue imatinib after sustained DMR maintain molecular remission — true functional cure without continued TKI. Second-generation TKIs (nilotinib, dasatinib) achieve DMR faster → higher TFR rates.

## Structure

### Disease biology

**The Philadelphia chromosome:**
- **t(9;22)(q34;q11.2):** Translocation places ABL1 exons 2+ under control of BCR regulatory sequences → BCR-ABL1 fusion mRNA
- **p210 BCR-ABL:** Most common; BCR breakpoint in major breakpoint cluster region (M-bcr, exons 13-14); 210 kDa; characteristic of CML and ~25% of adult ALL
- **p190 BCR-ABL:** BCR breakpoint in minor bcr (e1); 190 kDa; more common in Ph+ ALL; higher constitutive kinase activity → more aggressive

**BCR-ABL signaling pathways:**
1. **RAS-MAPK:** GRB2 binds pY177-BCR → SOS → RAS-GTP → ERK1/2 → proliferation
2. **STAT5:** BCR-ABL directly phosphorylates STAT5 → BCL-XL, MCL-1, MYC → survival and self-renewal of LSCs
3. **PI3K-AKT-mTOR:** PI3K recruitment via BCR-ABL/IRS-1 → AKT → mTOR → protein synthesis
4. **SRC-family kinases:** BCR-ABL activates LYN, HCK, FGR → additional survival signals

### Bone marrow pathology

**Peripheral blood:** Leukocytosis (WBC typically 50,000-500,000/μL), left-shifted granulocytes (all stages), basophilia (hallmark), thrombocytosis in ~50%, anemia
**Bone marrow:** Hypercellular (>90%), myeloid:erythroid ratio markedly elevated, megakaryocyte dysplasia ("dwarf" megakaryocytes), minimal blast increase in CP
**Cytogenetics:** Ph+ in >95% (FISH or karyotype); ~5% have variant translocations involving additional chromosomes

### Molecular monitoring

**BCR-ABL1 quantitative PCR (qPCR):**
- Reported on the **International Scale (IS)** as BCR-ABL1/ABL1 % transcript ratio
- Standardized so that 100% IS = pre-treatment CML
- **Major molecular response (MMR, MR3):** ≤0.1% IS — 3-log reduction; durability correlates with OS
- **MR4:** ≤0.01% IS (4-log reduction)
- **MR4.5:** ≤0.0032% IS (4.5-log reduction) — threshold for TFR attempt eligibility

## Function

### Normal BCR and ABL1 physiology

**Normal ABL1:**
- Non-receptor tyrosine kinase; regulated by N-terminal myristoyl cap folding into hydrophobic pocket → autoinhibition
- Functions in DNA damage response, cytoskeletal remodeling, cell migration
- Shuttles between nucleus (DNA repair) and cytoplasm (actin dynamics)

**Normal BCR:**
- BCR protein has RAS-GAP activity → normally attenuates RAS signaling
- In BCR-ABL, BCR contributes: coiled-coil dimerization (constitutive activation), pY177-GRB2 docking (RAS activation), but loses GAP function

**BCR-ABL constitutive activation:**
- Myristoyl cap cannot engage kinase → always active
- Coiled-coil dimerization → trans-autophosphorylation → further activation
- BCR-ABL is cytoplasmic (unlike nuclear ABL) → signal transduction bias

## Pathology

### Disease progression and blast crisis

**Mechanisms of progression to blast crisis:**
- Acquisition of additional cytogenetic abnormalities ("clonal evolution"): +8 (most common), i(17q), +Ph, +19
- Epigenetic silencing of differentiation factors (GATA2, C/EBPα)
- TP53 mutation, CDKN2A deletion, RUNX1 mutation
- BCR-ABL kinase domain mutation (conferring TKI resistance) + genetic instability from genomic crisis
- **Lymphoid BC:** Acquisition of IKZF1 deletions (Ikaros) → lymphoid blast crisis mimicking Ph+ ALL

**Leukemic stem cell (LSC) persistence:**
- Quiescent CD34+CD38- CML LSCs are relatively TKI-insensitive (not cycling → reduced dependence on BCR-ABL kinase)
- LSC persistence → molecular relapse upon TKI discontinuation in ~50% of patients
- LSC-targeting strategies: BCL-2 inhibitors (venetoclax), smoothened inhibitors (hedgehog pathway), combination immunotherapy — under investigation

### TKI resistance mechanisms

**Kinase domain mutations:**
- **T315I ("gatekeeper"):** Loss of imatinib/nilotinib/dasatinib/bosutinib contact threonine → resistance to all first/second-generation TKIs; requires ponatinib or asciminib (allosteric STAMP); frequency ~15-20% of resistant patients
- **F317L/V:** Dasatinib resistance; imatinib or nilotinib active
- **Y253H/E255K:** Nilotinib resistance; dasatinib active
- **F359V:** Nilotinib resistance; dasatinib active
- Compound mutations (e.g., T315I + V299L): ponatinib resistance; asciminib may retain activity

**BCR-ABL kinase-independent resistance:**
- SRC-family kinase overexpression (LYN amplification)
- Epigenetic silencing of drug transport (MDR1/ABCB1 upregulation, OCT1/SLC22A1 downregulation → reduced imatinib uptake)
- LSC quiescence (kinase-independent survival)

### Clinical presentations and complications

**Splenomegaly:** Result of extramedullary hematopoiesis in CML; can be massive (10-20 cm below costal margin); resolves with TKI; hydroxyurea used for cytoreduction prior to TKI initiation in symptomatic leukocytosis

**Leukostasis:** WBC >300,000/μL → slugging in microvasculature → pulmonary, cerebral ischemia; leukapheresis as bridge

**TKI-specific toxicities:**
- Imatinib: fluid retention, periorbital edema, myalgias, hepatotoxicity, QTc (rare); well-tolerated long-term
- Nilotinib: cardiovascular (PAD, AMI, stroke) — "off-target" PDGFR/c-KIT inhibition → metabolic syndrome risk; QTc prolongation; pancreatitis
- Dasatinib: pleural effusion (~20-35% cumulative), pulmonary arterial hypertension (rare, ~0.5%); platelet dysfunction; lymphocytosis (NK/T expansion → immune-mediated benefit in TFR)
- Ponatinib: arterial thrombosis (major concern); dose-optimization (45mg → 15mg after MR) reduces CV risk; pancreatitis; hypertension
- Asciminib: well-tolerated; hypertension; increased lipase; rare cardiovascular events

## Connections

- `connects-to` → **[ABL1](../../03-molecular/abl1/README.md)** — CML is caused by BCR-ABL fusion (t(9;22)); ABL1 kinase domain is the drug target; imatinib/dasatinib/nilotinib/bosutinib inhibit ABL1; T315I gatekeeper → ponatinib or asciminib (STAMP); MR4.5 molecular response enables treatment-free remission attempts.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — BCR-ABL constitutively phosphorylates STAT5 (and STAT3) → transcription of BCL-XL, MYC, and cyclin D1 → blast survival and proliferation; STAT5 activation is a dominant signaling output of BCR-ABL; TKI response correlates with STAT5 dephosphorylation.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — BCR-ABL → PI3K-AKT → mTORC1 → S6K and 4EBP1 → protein synthesis and survival; mTOR pathway activation mediates imatinib resistance in some CML clones; dual PI3K-mTOR inhibitors studied as combination with TKIs in BCR-ABL-positive blast crisis.
- `connects-to` → **[SRC kinase](../../03-molecular/src-kinase/README.md)** — BCR-ABL activates SRC-family kinases (LYN, HCK, FGR) in CML; SRC kinases promote blast crisis transformation and TKI resistance; dasatinib and bosutinib inhibit both ABL and SRC-family kinases — dual ABL/SRC inhibition relevant in lymphoid blast crisis.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — BCR-ABL → PI3K → AKT → mTOR → S6K/4EBP1 → protein synthesis and cell survival; AKT phosphorylates BAD → prevents apoptosis in CML cells; imatinib resistance associated with PI3K/AKT activation independent of BCR-ABL; AKT inhibition synergizes with TKIs in blast crisis CML.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — BCR-ABL → STAT5/NF-κB → MYC transcription → G1/S acceleration; MYC amplification is common in blast crisis transformation; MYC overexpression promotes self-renewal of CML LSCs; BRD4 inhibitors (JQ1) reduce MYC expression and overcome TKI resistance in CML blast crisis models.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — RB1 inactivated in CML blast crisis via CDK4/6 hyperactivation; E2F release drives myeloid or lymphoid blast transformation; BCR-ABL accelerates CDK2-mediated RB1 inactivation; palbociclib (CDK4/6 inhibitor) re-engages RB1 and sensitizes TKI-resistant blast crisis to apoptosis.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — CML is defined by uncontrolled expansion of the neutrophil lineage: BCR-ABL drives massive leukocytosis with granulocytes at all maturation stages and hallmark basophilia; unlike normal neutrophils they retain function early, so infection is not the initial problem.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — The CML marrow is markedly hypercellular with a high myeloid:erythroid ratio and 'dwarf' megakaryocytes; the Philadelphia chromosome t(9;22) is detected here, and marrow blast percentage defines chronic phase (<10%), accelerated (10-19%), and blast crisis (≥20%).
- `connects-to` → **[CLL](../cll/README.md)** — CLL and CML are the two chronic adult leukemias from opposite lineages: CLL is a B-lymphoid accumulation of mature CD5+ cells driven by BCR/BTK signaling, while CML is a myeloid proliferation driven by the BCR-ABL fusion kinase — different cells, drivers, and targeted drugs.
- `connects-to` → **[Myeloproliferative Neoplasms](../myeloproliferative-neoplasms/README.md)** — CML is the BCR-ABL1-positive classic myeloproliferative neoplasm: like PV, ET and myelofibrosis it is a clonal stem-cell overproduction of mature myeloid cells, but its Philadelphia chromosome and exquisite TKI sensitivity set it apart from the JAK2/CALR-driven MPNs.
- `connects-to` → **[AML](../aml/README.md)** — CML's natural history is progression to acute leukemia: untreated, the chronic phase accelerates into a blast crisis that behaves like acute leukemia—myeloid (AML-like) in ~70%, lymphoid in the rest—so TKI therapy aims to prevent this transformation, which remains hard to treat.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — Splenomegaly is a hallmark of CML: massive extramedullary myeloid proliferation enlarges the spleen, causing early satiety and left-upper-quadrant pain at presentation; spleen size featured in old prognostic scores and shrinks rapidly once tyrosine-kinase inhibitors control it.
- `connects-to` → **[Acute Lymphoblastic Leukemia](../all/README.md)** — CML and Philadelphia-positive ALL are united by the BCR-ABL fusion: the same t(9;22) drives chronic myeloid leukemia and a subset of acute lymphoblastic leukemia, so BCR-ABL tyrosine kinase inhibitors treat both—though Ph+ ALL is far more aggressive.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — CML often presents with a high platelet count alongside leukocytosis: the BCR-ABL clone expands the megakaryocyte lineage too, so thrombocytosis and basophilia accompany the neutrophilia—distinguishing CML from reactive leukocytosis and sometimes causing thrombosis.
- `connects-to` → **[Myelodysplastic Syndromes](../mds/README.md)** — CML and MDS sit at opposite poles of clonal myeloid disease: CML is a proliferative BCR-ABL-driven overproduction of mature myeloid cells, while MDS is a dysplastic, cytopenia-causing marrow failure—but both are clonal stem-cell disorders that can progress to AML.
- `connects-to` → **[JAK2](../../03-molecular/jak2/README.md)** — CML and JAK2-driven neoplasms are mirror-image myeloproliferative diseases: CML is defined by the BCR-ABL fusion kinase, while polycythemia vera and kin are driven by JAK2 mutations—both activate growth signaling, so testing distinguishes them and guides therapy.
- `connects-to` → **[Polycythemia Vera](../polycythemia-vera/README.md)** — CML and polycythemia vera are both myeloproliferative neoplasms but molecularly distinct: CML is BCR-ABL-positive and treated with TKIs, while PV is JAK2-mutant with red-cell overproduction—yet both feature splenomegaly and a risk of transforming to acute leukemia.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — CML enlarges the liver and spleen via extramedullary hematopoiesis: massive granulocyte overproduction and organ infiltration cause hepatosplenomegaly, often with early satiety from a huge spleen—signs that regress dramatically once TKI therapy controls the clone.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — CML disturbs red-cell production amid the myeloid overgrowth: marrow packed with granulocyte precursors crowds erythropoiesis, so anemia is common at diagnosis even as white cells soar—part of the imbalance the BCR-ABL clone imposes on blood formation.
- `connects-to` → **[Gout](../gout/README.md)** — CML can trigger gout through high cell turnover: the massive proliferation and breakdown of leukemic cells floods the blood with uric acid, which crystallizes in joints, so hyperuricemia and gout—or urate kidney stones—accompany the disease and its treatment.
- `connects-to` → **[Essential Thrombocythemia](../essential-thrombocythemia/README.md)** — CML and essential thrombocythemia are both myeloproliferative neoplasms but driven by different lesions: CML by BCR-ABL, ET usually by JAK2/CALR/MPL, so the Philadelphia chromosome distinguishes CML from the BCR-ABL-negative MPNs in the differential.
- `connects-to` → **[Immune System](../immune-system/README.md)** — CML pioneered treatment-free remission through the immune system: after deep response to TKIs, some patients stop the drug and stay in remission, because immune surveillance appears to hold residual leukemic stem cells in check.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Cytotoxic T and NK cells help control CML: immune effectors recognize leukemia-associated antigens, contributing to deep responses and the durability of treatment-free remission—so immunity complements the TKIs that block BCR-ABL.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Ionizing radiation can cause CML: survivors of the atomic bombs had sharply higher CML rates, evidence that X-ray and gamma photons damaging blood stem cells can create the BCR-ABL translocation that drives the disease.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — CML's stem cells survive TKIs by autophagy: leukemic stem cells recycle their contents to weather imatinib, so they persist despite a controlled blood count—why combining TKIs with autophagy blockers is studied to enable treatment-free remission.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — NK cells help control CML and predict cure: robust natural killer activity is linked to keeping leukemia in check, and patients with strong NK responses are likelier to stay in remission after stopping their TKI.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — CML's huge white-cell counts can fake high potassium: massive numbers of leukocytes and platelets leak potassium after blood is drawn, producing pseudohyperkalemia—a lab artifact to recognize before treating a number that isn't real in the body.
- `connects-to` → **[Wnt/beta-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Wnt/beta-catenin keeps CML's stem cells alive: this pathway sustains the leukemic stem cells that survive BCR-ABL inhibitors, so it helps explain why the disease persists on therapy and can progress to blast crisis.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — CML can poison the kidneys through tumor lysis: the huge white-cell mass releases uric acid that, especially as treatment kills cells, crystallizes in the kidney and causes urate nephropathy, linking the leukemia to gout and renal injury.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells can spring from the CML clone itself: because the leukemia is a stem cell disease, even antigen-presenting cells carry BCR-ABL, and harnessing dendritic cells is explored to boost immune control after drug therapy.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Extreme CML counts can starve tissues of oxygen: when white cells soar, the sludgy blood (leukostasis) clogs small vessels, so organs are starved of oxygen—an emergency needing urgent cytoreduction.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — CML leukostasis can strike the brain: a sky-high white-cell mass sludges cerebral vessels, causing headaches, confusion, strokes, and visual loss, the neurologic face of hyperleukocytosis.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — CML's clone reaches into the macrophage lineage: because BCR-ABL arises in a myeloid stem cell, the expanded output includes monocytes and macrophages, part of the broad granulocytic overgrowth that defines the disease.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — CML's high cell turnover spills purines and phosphate: hyperuricemia causes the gout it is known for, and tumor lysis at blast crisis or on treatment releases phosphate and potassium.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — CML's huge white-cell mass clogs the eye's vessels: leukostasis causes retinal hemorrhages and engorged veins, visible on fundoscopy as a warning sign of dangerous hyperleukocytosis.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — CML can scar its marrow: reticulin and collagen fibrosis increase as the disease progresses and predict a worse response, blurring the line toward myelofibrosis.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows CML's overflowing granulocyte line: the marrow and blood teem with neutrophils at every stage of maturation plus a telltale rise in basophils, the expanded myeloid spectrum that the BCR-ABL kinase drives.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — A sky-high white count can clog the lungs: in CML's accelerated phase, leukostasis from the sheer mass of circulating cells sludges the pulmonary vessels, causing breathlessness and respiratory distress.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — CML can surface on the skin: leukemia cutis deposits tumor cells in the skin, and the neutrophilic Sweet syndrome can erupt with fever and tender plaques, sometimes heralding transformation to blast crisis.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — The targeted drugs that tamed CML can wound the vessels: the newer TKIs — nilotinib and especially ponatinib — drive arterial thrombosis, hypertension, and cardiac events, a vascular toll weighed against their potency.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Lifelong TKI therapy collides with childbearing: imatinib and its successors are teratogenic, so conception must be planned around treatment interruptions, a central concern now that CML is a chronic, survivable disease.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — The pills upset the gut: diarrhea is among the commonest TKI side effects — pronounced with bosutinib — and managing it is part of keeping patients on the daily therapy that controls the leukemia.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Some TKIs injure the vessel lining: nilotinib and ponatinib damage endothelial cells and accelerate atherosclerosis, raising the risk of arterial occlusion, peripheral artery disease and heart attack — the vascular toxicity that shapes which drug a CML patient receives.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-beta hides CML from cure: it keeps the leukemic stem cells quiescent through FOXO signaling, and these dormant cells survive even deep BCR-ABL inhibition — why most patients must keep taking TKIs and why stem-cell-targeting strategies are sought.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Long-term imatinib reshapes bone mineral handling: by blocking PDGFR and KIT on bone cells it lowers bone turnover and can disturb calcium and phosphate balance, an under-recognized metabolic effect of years on TKI therapy.
- `connects-to` → **[Graft-Versus-Host Disease](../gvhd/README.md)** — Transplant was CML's first cure: before TKIs, allogeneic stem-cell transplant offered the only cure through its graft-versus-leukemia effect, at the cost of graft-versus-host disease — still the fallback for TKI-resistant or blast-crisis disease.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — The immune system can help hold CML down: regulatory T cells that blunt anti-leukemia immunity rise with disease, and their balance shapes the immune control that lets some patients stop TKIs and stay in remission.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — Inflammation feeds the leukemic niche: BCR-ABL drives IL-6 release that remodels the marrow microenvironment to favor the leukemic stem cells over normal hematopoiesis.
- `connects-to` → **[Myelofibrosis](../myelofibrosis/README.md)** — CML can scar the marrow it fills: marrow fibrosis develops with advanced or accelerated disease and, like primary myelofibrosis, reflects the megakaryocyte-driven, cytokine-rich stroma of a myeloproliferative neoplasm.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — Blast crisis leans on anti-apoptosis: BCR-ABL props up BCL-2-family survival signals, and adding the BCL-2 inhibitor venetoclax to a TKI is a strategy to kill the resistant blasts of advanced-phase CML.
- `connects-to` → **[Stroke](../stroke/README.md)** — Extreme white counts can clog the brain's vessels: the massive leukocytosis of CML can cause leukostasis, a hyperviscosity emergency that sludges cerebral flow and can present as stroke before the diagnosis is even known.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — BCR-ABL routes survival through NF-κB: the fusion kinase activates NF-κB among its downstream pathways, supporting leukemic-cell survival and contributing to the resistance that emerges in advanced-phase disease.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Some of its drugs damage vessels: the later-generation TKIs nilotinib and especially ponatinib cause arterial and venous vascular events, so thrombosis is a recognized hazard of long-term CML therapy.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Advanced disease strips the defenses: blast crisis and its intensive chemotherapy cause the neutropenia and immune failure that make febrile neutropenia and sepsis a danger in progressive CML.
- `connects-to` → **[Pulmonary Arterial Hypertension](../pulmonary-arterial-hypertension/README.md)** — One of its drugs scars the lung vessels: dasatinib, a second-generation TKI for CML, causes pleural effusions and a reversible pulmonary arterial hypertension, a distinctive class toxicity needing monitoring.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Later TKIs strain the heart: nilotinib and ponatinib used in CML carry cardiovascular toxicity — arterial events, hypertension and cardiac dysfunction — that can contribute to heart failure over long-term therapy.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Lifelong treatment weighs on mood: the open-ended daily TKI therapy, its chronic side effects and the psychological weight of living with leukemia contribute to depression and reduced quality of life in CML.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Some of its TKIs harden the arteries: nilotinib and ponatinib used for CML accelerate atherosclerosis and cause arterial occlusive events, a major vascular toxicity of these later-line drugs.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Marrow crowding and TKIs lower the count: the expanded myeloid clone and the myelosuppression of tyrosine-kinase inhibitor therapy can produce an anemia with a chronic-disease component.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Blast crisis and its chemo open the lung to mold: progression of CML to blast crisis requires intensive chemotherapy that causes deep neutropenia, allowing inhaled Aspergillus to invade.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Its TKIs and big spleen upset the gut: tyrosine-kinase inhibitors cause nausea, diarrhoea and hepatotoxicity, and the massive splenomegaly of CML presses on the stomach causing early satiety.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Its targeted drugs mark the skin: imatinib and other TKIs commonly cause rashes and periorbital oedema, and they can characteristically lighten skin pigmentation through KIT inhibition.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Lifelong therapy and PCR monitoring breed worry: the indefinite tyrosine-kinase-inhibitor treatment and the scrutiny of molecular-response blood tests in CML foster chronic health anxiety alongside depression.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It massively swells the spleen: overproduction of myeloid cells enlarges the spleen, often dramatically, causing early satiety and left-upper-quadrant pain with risk of splenic infarction.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — One of its drugs floods the chest: the tyrosine-kinase inhibitor dasatinib characteristically causes pleural effusions, sometimes large and recurrent, requiring dose change or drainage.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Its inhibitors disturb metabolism: nilotinib can raise blood glucose and cause hyperglycaemia, and tyrosine-kinase inhibitors affect thyroid function and growth in children.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its newer drugs clog arteries: TKIs like nilotinib and ponatinib raise the risk of arterial occlusive events — peripheral arterial disease, heart attack and stroke — needing cardiovascular monitoring.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Treatment aches in muscle and bone: imatinib commonly causes muscle cramps and bone-aching, and the expanding marrow of untreated CML brings bone pain.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Rapid cell turnover and drugs reach the kidney: tumour lysis at the start of therapy and the nephrotoxicity of some TKIs can impair kidney function.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — The archetype of targeted therapy: BCR-ABL1 tyrosine-kinase inhibitors (imatinib and successors) turned CML from fatal into a chronic, often treatment-free-remission disease, the founding success of precision oncology.
- `connects-to` → **[GIST](../gist/README.md)** — A shared imatinib target: gastrointestinal stromal tumour, driven by KIT, responds to imatinib just as BCR-ABL-driven CML does, the same drug treating two unrelated cancers.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Before and beyond the TKIs: hydroxyurea, busulfan and interferon controlled CML before imatinib, and intensive chemotherapy is still needed if it transforms to blast crisis.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — Its drugs harm the arteries: the TKIs that control CML, especially nilotinib and ponatinib, accelerate atherosclerosis and cause arterial occlusive events — peripheral, coronary and cerebral — a key long-term toxicity to monitor.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Marrow overgrowth aches the bones: the massive myeloid hyperplasia of CML expands the marrow and can cause bone pain, while high cell turnover and infiltration stress the skeleton.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — TKIs can stress the heart: beyond arterial events, CML tyrosine-kinase inhibitors cause fluid retention, QT prolongation and, with ponatinib, heart failure, so cardiac function is monitored during long-term therapy.
- `connects-to` → **[CMML](../cmml/README.md)** — Ph-negative myeloproliferation: CMML is a myelodysplastic/myeloproliferative overlap that lacks the BCR-ABL fusion of CML, the key distinction in a patient with leukocytosis, monocytosis and splenomegaly.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Extramedullary disease in the liver: in advanced or blast-phase CML, leukaemic cells and extramedullary haematopoiesis infiltrate the hepatic lobule, contributing to hepatomegaly.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — A price of long-term TKIs: the BCR-ABL inhibitor nilotinib raises blood glucose and worsens insulin resistance, so diabetes and arterial disease are monitored during the chronic therapy that now makes CML survivable.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — TKI cardiac effects: BCR-ABL inhibitors like nilotinib prolong the QT interval and (with ponatinib) provoke vascular events, disturbing the cardiac conduction system during long-term therapy.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Dasatinib's pleural effusions: the second-generation TKI dasatinib commonly causes pleural effusions, fluid collecting around the lung's alveolar surface—a class-specific toxicity needing dose adjustment.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — An unexpected antiviral angle: BCR-ABL TKIs like imatinib were studied as COVID-19 therapeutics for their effects on viral entry and inflammation, and CML patients on TKIs largely tolerated infection well.
- `connects-to` → **[KIT](../../03-molecular/kit/README.md)** — Off-target reach: imatinib and nilotinib also inhibit KIT, which is why these BCR-ABL drugs are effective in GIST and mast-cell disease—the same kinase explains some of their side effects.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — Survival signal switched off: BCR-ABL drives PI3K-AKT signalling that inactivates FOXO transcription factors, suppressing apoptosis and quiescence and helping leukaemic stem cells persist under therapy.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Protective hypoxic niche: HIF-1α-driven adaptation in the hypoxic bone-marrow niche shelters CML stem cells from TKIs, contributing to disease persistence and relapse on stopping treatment.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Blast-crisis epigenetics: EZH2 and PRC2 enforce a repressive chromatin state that contributes to the progression of CML from chronic phase to aggressive blast crisis.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Cell-cycle drive: BCR-ABL signalling upregulates cyclin D and the cell-cycle machinery, pushing myeloid progenitors into the expanded proliferation of chronic myeloid leukaemia.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Marrow angiogenesis: BCR-ABL raises VEGF, increasing bone-marrow microvessel density to support the expanded leukaemic population of CML.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — RAS-ERK signalling: BCR-ABL constitutively activates the RAS-RAF-ERK cascade, a key proliferative output of the fusion kinase driving the myeloid expansion of chronic myeloid leukaemia.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — Stem-cell niche: CXCL12-CXCR4 signalling anchors leukaemic stem cells in the protective marrow niche, a sanctuary that shelters quiescent CML cells from tyrosine-kinase inhibitors.
- `connects-to` → **[RUNX1](../../03-molecular/runx1/README.md)** — Blast-crisis transformation: acquired RUNX1 alterations contribute to the progression of chronic-phase CML to the aggressive, treatment-resistant blast crisis.
- `connects-to` → **[SMO](../../03-molecular/smo/README.md)** — Hedgehog signaling through Smoothened sustains the leukemic stem cells that persist beneath TKI therapy in CML, the quiescent reservoir responsible for molecular relapse after treatment-free-remission attempts.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Imatinib and later BCR-ABL inhibitors kill CML cells by relieving the fusion kinase's block on caspase-3-mediated apoptosis, restoring the cell-death program the oncoprotein suppresses to drive the leukemia.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — Progressive telomere attrition and telomerase changes accompany the evolution of chronic-phase CML toward blast crisis, reflecting the accumulating genomic instability of disease progression.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — CML was the disease in which donor T- and NK-cell perforin-mediated killing of leukemic cells—graft-versus-leukemia, the basis of donor lymphocyte infusion—was first proven curative, the paradigm of cellular immunotherapy.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — Additional mutations such as DNMT3A acquired on the BCR-ABL background drive the progression of chronic-phase CML to accelerated phase and blast crisis, the transformation that TKIs do not by themselves prevent.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — TP53 inactivation, often through MDM2 overexpression, accompanies the transformation of CML to blast crisis, removing the apoptotic brake and conferring the resistance that makes advanced-phase disease so hard to treat.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — BCR-ABL1 activates RAS, driving the MAPK-ERK cascade (ERK1/2 already mapped) that is a core proliferative output of the Philadelphia-chromosome fusion kinase.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — BCR-ABL1 engages PI3K, initiating the AKT-mTOR signaling (both already mapped) that provides the survival limb cooperating with proliferative RAS-MAPK and JAK-STAT signaling in CML.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — BCR-ABL1 signaling pushes the cyclin-D1-RB axis (cyclin-D1 and RB1 already mapped) to release E2F1, and CDKN2A loss in lymphoid blast crisis further unleashes this proliferative transcription.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 inactivation drives the transformation from chronic phase to the aggressive, treatment-resistant blast crisis of CML.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A/p16 deletion is a recurrent lesion in the progression of CML to lymphoid blast crisis, removing a cell-cycle brake on the proliferating clone.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — NRF2 antioxidant signaling protects CML cells — including leukemic stem cells — from oxidative stress and contributes to resistance against tyrosine-kinase inhibitors.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 in the bone-marrow niche promotes leukemic-stem-cell survival and tyrosine-kinase-inhibitor resistance in chronic myeloid leukemia.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN restraint of PI3K-AKT-mTOR signaling (AKT, PIK3CA and mTOR mapped) downstream of BCR-ABL shapes CML-cell proliferation and survival.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β and FOXO mapped) maintains the quiescent leukemic stem cells that resist BCR-ABL-targeted therapy in CML.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling underlies the antileukemic effect of interferon-α, a historic and adjunctive therapy in chronic myeloid leukemia.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING modulates the inflammatory bone-marrow microenvironment of chronic myeloid leukemia.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6-cyclin-D activity (cyclin-D1 and RB1 already mapped) drives the cell-cycle progression downstream of BCR-ABL in chronic myeloid leukemia.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β misregulation in CML blast crisis impairs myeloid differentiation and supports leukemic stem-cell self-renewal.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the inflammatory bone-marrow niche of chronic myeloid leukemia.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK1/2-STAT5 signaling (JAK2 and STAT3 already mapped) is co-opted by BCR-ABL to sustain leukemic survival in chronic myeloid leukemia.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation and quiescence of the leukemic stem cells of chronic myeloid leukemia.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — CCL2-driven monocyte and macrophage recruitment contributes to the inflammatory bone-marrow niche of chronic myeloid leukemia.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — NOTCH signaling participates in the maintenance of the leukemic stem cells of chronic myeloid leukemia.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-family chemokine signaling (CXCL12/CXCR4 already mapped) participates in the bone-marrow homing and microenvironment of chronic myeloid leukemia.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic dysregulation of chronic myeloid leukemia.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β signaling in the bone-marrow niche contributes to the leukemic stem-cell maintenance and inflammatory microenvironment of chronic myeloid leukemia.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the inflammatory bone-marrow microenvironment of chronic myeloid leukemia.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory bone-marrow microenvironment of chronic myeloid leukemia.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory microenvironment of chronic myeloid leukemia.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the leukemic-stem-cell and immune signaling of chronic myeloid leukemia.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine signaling participates in the immunosuppressive bone-marrow microenvironment of chronic myeloid leukemia.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin participates in the leukemic-stem-cell-niche and bone-marrow-microenvironment interactions of chronic myeloid leukemia.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Immune control and remission: CML is the model for treatment-free remission, where MHC-restricted T-cell and NK responses against the BCR-ABL-driven clone help maintain remission after stopping tyrosine-kinase inhibitors.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Hyperuricaemia: the high cell turnover of chronic myeloid leukaemia releases purines that xanthine oxidase converts to uric acid, causing the hyperuricaemia and gout risk managed with allopurinol at diagnosis and during cytoreduction.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Immune surveillance: IL-2 drives the expansion of the T and NK cells that provide the immunological control believed to sustain treatment-free remission in chronic myeloid leukaemia after tyrosine-kinase-inhibitor withdrawal.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Anaemia: marrow crowding by the leukaemic clone and, later, transformation lower haemoglobin, and the anaemia adds to the fatigue of chronic myeloid leukaemia, usually improving as tyrosine-kinase inhibition restores normal haematopoiesis.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — TKI vascular toxicity: nilotinib and ponatinib cause arterial-occlusive and cardiac events, and troponin elevation marks the myocardial injury of the vascular toxicity that shapes tyrosine-kinase-inhibitor selection in CML.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Nilotinib hyperglycaemia: nilotinib impairs glucose handling and raises the risk of hyperglycaemia and diabetes through effects on insulin signalling, a metabolic toxicity that factors into tyrosine-kinase-inhibitor choice in CML.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — TKI endothelial toxicity: ponatinib and nilotinib impair endothelial nitric oxide and function, promoting the arterial-occlusive and cardiovascular events (troponin already mapped) that are a defining toxicity shaping tyrosine-kinase-inhibitor selection in CML.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Nilotinib dyslipidaemia: nilotinib raises cholesterol and drives an atherogenic dyslipidaemia that, with its glucose effects (insulin already mapped), contributes to the vascular risk of the second-generation tyrosine-kinase inhibitors in CML.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Anaemia and transfusion: the marrow disruption of CML and its tyrosine-kinase-inhibitor therapy causes anaemia (haemoglobin already mapped) that can require transfusion, whose repeated support can load the body with iron.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage niche: IL-4 polarises the marrow macrophages toward an M2 phenotype that helps shelter the leukaemic stem cells in the bone-marrow (already mapped) microenvironment of CML.
- `connects-to` → **[PF4](../../03-molecular/pf4/README.md)** — Thrombocytosis and platelets: CML commonly raises the platelet count, and platelet factor 4 from the expanded, sometimes dysfunctional platelets reflects the thrombo-haemorrhagic dimension of the myeloproliferation.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Marrow adipose crosstalk: the marrow adipocytes and their adipokine leptin signal to the leukaemic stem cells, part of the bone-marrow (already mapped) microenvironment that influences the persistence of the CML clone.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Marrow-adipocyte adipokine: adiponectin, with leptin (already mapped), from the marrow adipose tissue signals to the leukaemic stem cells of the bone-marrow (already mapped) microenvironment of CML.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipokine milieu: resistin, with leptin and adiponectin (already mapped), completes the marrow-adipocyte adipokine signalling of the microenvironment influencing the CML clone.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Anaemia and transfusion iron: the anaemia (haemoglobin already mapped) of CML and the iron overload of the transfusion support during the blast-phase treatment reflect the disturbed iron handling of the leukaemia.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Thrombocytosis: CML often causes the thrombocytosis (the megakaryocytic proliferation; PF4 already mapped), part of the myeloproliferation of the leukaemia.
- `connects-to` → **[AML](../aml/README.md)** — Myeloid blast crisis: CML can transform to the acute myeloid leukaemia (the myeloid blast crisis; RUNX1 already mapped), a terminal accelerated phase.
- `connects-to` → **[ALL](../all/README.md)** — Lymphoid blast crisis: CML can also transform to a lymphoid (Ph+ ALL-like) blast crisis (ABL1 already mapped), treated as the Ph+ ALL.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — IFN-α therapy/immune control: the type-I interferon (IFN-α) was the pre-TKI standard therapy of CML and, downstream of cGAS-STING (already mapped), underlies the immune surveillance relevant to the treatment-free remission.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 anti-leukaemic arm: the IFN-γ of the T and NK cells (perforin already mapped) is the type-II interferon arm of the anti-leukaemic immunity relevant to the immune control of CML.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of chronic myeloid leukaemia.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of chronic myeloid leukaemia (and the eosinophilia of some myeloproliferative overlaps).
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 arm: IL-13, with IL-4 (already mapped), completes the type-2 immune arm of the immune microenvironment of chronic myeloid leukaemia.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory bone-marrow (already mapped) microenvironment of chronic myeloid leukaemia.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) links the complement to the myeloid inflammation of the chronic-myeloid-leukaemia bone-marrow (already mapped) microenvironment.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Basophil/mast lineage: the mast cells, sharing the myeloid basophil lineage that is expanded (the basophilia) in chronic myeloid leukaemia, are part of the leukaemic myeloid output.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — Immune surveillance: the CD4 T-helper cells contribute to the antileukaemic immunity that supports the treatment-free remission after the tyrosine-kinase-inhibitor therapy of chronic myeloid leukaemia.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) are part of the myeloid inflammatory dimension of the chronic-myeloid-leukaemia marrow microenvironment.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the inflammatory marrow niche of chronic myeloid leukaemia.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Leukaemia iron: transferrin, the iron carrier, reflects the disordered iron handling of the anaemia and the high cell turnover of chronic myeloid leukaemia.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-marrow axis: TSLP, from marrow stromal cells and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2/Treg imbalance of the inflammatory leukaemia marrow microenvironment of CML.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-marrow axis: bradykinin, via B1/B2 receptors on marrow endothelium (already mapped) and BCR-ABL-driven stromal cells, amplifies the vascular permeability and the cytokine milieu of the CML marrow microenvironment.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Erythropoietic failure: the BCR-ABL-driven CML leukaemia marrow (already mapped) displaces the normal erythropoiesis, and erythropoietin supports the management of the anaemia of CML.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell CML marrow axis: histamine, from the expanded mast-cell pool (already mapped) in the CML marrow niche, amplifies the BCR-ABL-driven (already mapped) angiogenesis (already mapped) and the inflammatory cytokine milieu of the CML stroma.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian-BCR-ABL axis: melatonin, via MT1/MT2 receptors on CML haematopoietic progenitors (already mapped), modulates the oxidative stress of the BCR-ABL-driven (already mapped) clonal expansion and the inflammatory marrow niche of CML.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical complement regulation: the C1-esterase inhibitor regulates the classical complement pathway (C5 and C5aR1 already mapped) whose activation contributes to the inflammatory leukaemia marrow microenvironment of chronic myeloid leukaemia.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — CML testosterone: testosterone, via androgen receptors on macrophages (already mapped) and T-cytotoxic cells (already mapped), modulates the CML TME; testosterone deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) BCR-ABL survival cascade of CML.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — CML serotonin: serotonin, via 5-HT receptors on macrophages (already mapped) and mast cells (already mapped), modulates the CML TME; serotonin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) BCR-ABL cascade of CML.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — CML prolactin: prolactin, via PRLR on macrophages (already mapped) and mast cells (already mapped), promotes CML immune escape; hyperprolactinaemia amplifies the NF-κB (already mapped) and IL-6 (already mapped) leukaemic survival cascade of CML.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — CML oxytocin: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates the BCR-ABL (already mapped)-driven TME inflammation; oxytocin deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) leukaemic survival cascade of CML.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — CML vasopressin: vasopressin, via V1aR on macrophages (already mapped) and mast cells (already mapped), modulates the CML marrow vascular milieu; vasopressin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) BCR-ABL cascade of CML.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — CML selenium: selenium, as GPx in macrophages (already mapped) and T-cytotoxic cells (already mapped), scavenges BCR-ABL-driven ROS; selenium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) oxidative leukaemia cascade of CML.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — CML iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) polarisation and T-cytotoxic (already mapped) surveillance; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) BCR-ABL leukaemia cascade of CML.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — CML sodium: sodium dysregulation in macrophages (already mapped) and leukaemic stem cells (already mapped) amplifies ionic stress; osmotic changes worsen NF-κB (already mapped) and IL-6 (already mapped) and BCR-ABL tumour-promoting cascade of CML.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — CML magnesium: magnesium cofactors kinase signalling in macrophages (already mapped) and T-cytotoxic cells (already mapped); magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCR-ABL leukaemic signalling cascade of CML.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — copper, via SOD in macrophage (already mapped) and T-cytotoxic cell (already mapped), counters BCR-ABL-driven ROS; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCR-ABL leukaemic cascade of CML.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — zinc cofactors kinase signalling in macrophage (already mapped) and T-cytotoxic cell (already mapped); zinc deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCR-ABL leukaemic survival cascade of CML.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — chloride channels on macrophage (already mapped) and leukaemic stem cell (already mapped) regulate membrane potential; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCR-ABL cascade of CML.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — CML carbon: carbon backbone of nucleotides in macrophages (already mapped) and leukaemic stem cells (already mapped) fuels tumour proliferation; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCR-ABL leukaemic cascade of CML.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — CML hydrogen: hydrogen via ROS from macrophages (already mapped) and leukaemic stem cells (already mapped) modulates redox homeostasis; hydrogen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCR-ABL leukaemic cascade of CML.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — CML nitrogen: nitrogen in DNA bases of macrophages (already mapped) and leukaemic stem cells (already mapped) sustains tumour growth; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCR-ABL leukaemic cascade of CML.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^druker-2006-iris-5year]: Druker BJ, Guilhot F, O'Brien SG, et al. Five-year follow-up of patients receiving imatinib for chronic myeloid leukemia. *N Engl J Med.* 2006;355(23):2408-2417. [doi:10.1056/NEJMoa062867](https://doi.org/10.1056/NEJMoa062867) · [PubMed 17151364](https://pubmed.ncbi.nlm.nih.gov/17151364/)
[^hochhaus-2019-dasatinib]: Hochhaus A, Saglio G, Hughes TP, et al. Long-term benefits and risks of frontline nilotinib vs imatinib for chronic myeloid leukemia in chronic phase: 5-year update of the randomized ENESTnd trial. *Leukemia.* 2016;30(5):1044-1054. [doi:10.1038/leu.2016.5](https://doi.org/10.1038/leu.2016.5) · [PubMed 26816503](https://pubmed.ncbi.nlm.nih.gov/26816503/)
