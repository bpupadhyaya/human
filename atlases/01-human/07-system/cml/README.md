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

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^druker-2006-iris-5year]: Druker BJ, Guilhot F, O'Brien SG, et al. Five-year follow-up of patients receiving imatinib for chronic myeloid leukemia. *N Engl J Med.* 2006;355(23):2408-2417. [doi:10.1056/NEJMoa062867](https://doi.org/10.1056/NEJMoa062867) · [PubMed 17151364](https://pubmed.ncbi.nlm.nih.gov/17151364/)
[^hochhaus-2019-dasatinib]: Hochhaus A, Saglio G, Hughes TP, et al. Long-term benefits and risks of frontline nilotinib vs imatinib for chronic myeloid leukemia in chronic phase: 5-year update of the randomized ENESTnd trial. *Leukemia.* 2016;30(5):1044-1054. [doi:10.1038/leu.2016.5](https://doi.org/10.1038/leu.2016.5) · [PubMed 26816503](https://pubmed.ncbi.nlm.nih.gov/26816503/)
