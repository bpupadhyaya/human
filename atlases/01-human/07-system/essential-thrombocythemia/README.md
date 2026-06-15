---
schema: human-scale-entry/v1
id: essential-thrombocythemia
name: Essential Thrombocythemia
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Essential thrombocythemia is a JAK2/CALR/MPL-driven MPN with megakaryocytic hyperplasia and thrombocytosis; JAK2 V617F ~55-60%; CALR ~20-25%; MPL ~5-8%; risk-stratified aspirin ± hydroxyurea; anagrelide second-line; post-ET MF (~1-2%) and AML (<1%) transformation risk."
aliases: ["essential thrombocythemia", "ET", "essential thrombocytosis", "primary thrombocythemia", "JAK2 thrombocythemia", "CALR ET"]
sources:
  - id: harrison-2005-pt1-et
    type: peer-reviewed
    cite: "Harrison CN, Campbell PJ, Buck G, et al. Hydroxyurea compared with anagrelide in high-risk essential thrombocythemia. N Engl J Med. 2005;353(1):33-45."
    doi: "10.1056/NEJMoa043800"
    pmid: "16000354"
    url: "https://doi.org/10.1056/NEJMoa043800"
  - id: barbui-2012-ipset
    type: peer-reviewed
    cite: "Barbui T, Finazzi G, Carobbio A, et al. Development and validation of an International Prognostic Score of thrombosis in World Health Organization-essential thrombocythemia (IPSET-thrombosis). Blood. 2012;120(26):5128-5133."
    doi: "10.1182/blood-2012-07-444067"
    pmid: "23086758"
    url: "https://doi.org/10.1182/blood-2012-07-444067"
cross_links:
  - target: 01-human/03-molecular/mpl
    relation: connects-to
    note: "MPL W515L/K mutations (~5-8% ET) cause constitutive JAK2/STAT5 activation independent of TPO; MPL-mutant ET is clinically similar to CALR-mutant ET (lower thrombosis risk vs JAK2); TPO-receptor agonists (eltrombopag, romiplostim) act on wild-type MPL."
  - target: 01-human/03-molecular/jak2
    relation: connects-to
    note: "JAK2 V617F (~55-60% ET) causes constitutive erythroid/megakaryocytic/granulocytic proliferation; JAK2-positive ET has higher thrombosis risk than CALR-mutant ET; ruxolitinib is active in JAK2 V617F ET but is not FDA-approved for ET."
  - target: 01-human/03-molecular/calr
    relation: connects-to
    note: "CALR mutations (~20-25% ET); type 2 ins5bp is predominant in ET (vs type 1 del52bp in PMF); CALR-mutant ET has lower thrombosis risk, younger age, and longer OS than JAK2-mutant ET; JAK2/CALR/MPL mutations are mutually exclusive."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "ET transforms to post-ET MF (~1-2% at 10 years); megakaryocyte-derived TGF-β1 → reticulin → collagen fibrosis; co-mutations (ASXL1, EZH2, SRSF2) accelerate MF transformation; momelotinib targets ACVR1 to address anemia in post-ET MF."
  - target: 01-human/03-molecular/von-willebrand-factor
    relation: connects-to
    note: "At platelet counts >1,500 ×10⁹/L, ET causes acquired von Willebrand syndrome — platelet GPIb adsorbs high-molecular-weight VWF multimers and depletes them, impairing primary hemostasis → paradoxical bleeding; aspirin is contraindicated until cytoreduction normalizes the count."
  - target: 01-human/07-system/polycythemia-vera
    relation: connects-to
    note: "PV and ET are both JAK2-driven MPNs on a phenotypic continuum; PV (JAK2 nearly 100%, often homozygous) skews erythroid while ET skews megakaryocytic; JAK2 V617F-ET can drift toward a PV phenotype; ET has lower post-MF and AML transformation risk than PV."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Clonal megakaryocytic hyperplasia drives sustained thrombocytosis; JAK2 V617F platelets are constitutively activated (resting P-selectin) → platelet-leukocyte aggregates and thrombosis; erythromelalgia from platelet microvascular occlusion responds rapidly to aspirin."
  - target: 01-human/07-system/disseminated-intravascular-coagulation
    relation: connects-to
    note: "Essential thrombocythemia and DIC are opposite poles of platelet pathology: ET clonally overproduces platelets causing thrombosis (and, at extreme counts, acquired von Willebrand bleeding), while DIC systemically consumes platelets and clotting factors — too many versus too few."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Essential thrombocythemia is a clonal bone marrow disease: a JAK2, CALR, or MPL mutation drives autonomous megakaryocyte hyperplasia, so the marrow shows large, mature, clustered megakaryocytes without the dense fibrosis of primary myelofibrosis — a key WHO distinction."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "Mild splenomegaly is common in essential thrombocythemia from extramedullary hematopoiesis and pooling; progressive splenic enlargement signals transformation to post-ET myelofibrosis, and prior splenectomy paradoxically raises platelet counts and thrombosis risk."
  - target: 01-human/07-system/myeloproliferative-neoplasms
    relation: connects-to
    note: "Essential thrombocythemia is one of the three classic Philadelphia-negative myeloproliferative neoplasms (with PV and PMF): a JAK2/CALR/MPL-driven clonal overproduction—here of platelets—sharing thrombosis risk and the capacity to evolve into myelofibrosis or AML."
  - target: 01-human/07-system/myelofibrosis
    relation: connects-to
    note: "Essential thrombocythemia can progress to post-ET myelofibrosis: over years the clone drives marrow reticulin fibrosis, so the platelet-rich blood picture gives way to splenomegaly, cytopenias and a leukoerythroblastic film, converging with primary myelofibrosis."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Thrombosis—not bleeding—is the main danger of essential thrombocythemia: the dysfunctional excess platelets and JAK2 mutation create a prothrombotic state causing arterial and venous events, including VTE and unusual-site (splanchnic) thrombosis; aspirin lowers risk."
  - target: 01-human/07-system/cml
    relation: connects-to
    note: "ET and CML are both chronic myeloproliferative neoplasms but driven differently: CML by the BCR-ABL fusion tyrosine kinase (treatable with imatinib), ET by JAK2/CALR/MPL mutations driving platelet overproduction—both can progress to fibrosis or acute leukemia."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "ET predisposes to stroke: the excess, often dysfunctional platelets promote arterial thrombosis, so TIAs and stroke are feared complications—low-dose aspirin and cytoreduction lower this risk, a rare case where too many platelets cause clots, not bleeding."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "ET and polycythemia vera show how one marrow can overproduce different lineages: ET expands megakaryocytes and platelets while PV expands erythrocytes, yet both arise from JAK2-pathway mutations—lineage skewing of a shared clonal stem-cell defect sets the phenotype."
  - target: 01-human/03-molecular/thrombin
    relation: connects-to
    note: "Excess platelets in essential thrombocythemia tip toward thrombin-driven clotting: the high, often dysfunctional platelet mass promotes both arterial and venous thrombosis, so low-dose aspirin and cytoreduction lower the clotting risk that dominates ET's morbidity."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "Essential thrombocythemia carries a small but real risk of transforming to AML: as a clonal myeloproliferative neoplasm, ET can evolve through myelofibrosis to acute leukemia, a risk raised by some cytoreductive drugs—the feared long-term endpoint."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Essential thrombocythemia often raises neutrophils too: the JAK2-driven clone expands multiple myeloid lineages, so leukocytosis often accompanies the thrombocytosis and itself predicts higher thrombosis risk—ET is a panmyeloid, not platelet-only, disease."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Essential thrombocythemia clots at the endothelium: excess, often dysfunctional platelets interact with the vessel lining to cause microvascular and large-vessel thrombosis, so antiplatelet therapy targeting this platelet-endothelial interface prevents the main complication."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Essential thrombocythemia is a classic cause of splanchnic vein thrombosis: the prothrombotic platelet excess can clot the hepatic or portal veins (Budd-Chiari), so unexplained abdominal vein thrombosis should prompt testing for JAK2 and an underlying MPN."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Essential thrombocythemia produces distinctive neurovascular symptoms: microvascular platelet plugging causes headaches, visual disturbance and erythromelalgia, and it raises stroke and TIA risk—so the nervous system often signals the disease before a major clot occurs."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "Essential thrombocythemia complicates pregnancy through the placenta: the thrombotic tendency causes placental clots, miscarriage, and growth restriction, so pregnant patients are managed with low-dose aspirin and sometimes heparin to protect the placenta."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Essential thrombocythemia announces itself in the skin as erythromelalgia: platelet microthrombi in small vessels cause burning, red, painful hands and feet, a near-specific symptom that dramatically improves with low-dose aspirin."
  - target: 01-human/07-system/gout
    relation: connects-to
    note: "Essential thrombocythemia's high cell turnover can cause gout: rapid platelet and cell production raises uric acid, so hyperuricemia and gout flares accompany this and other myeloproliferative neoplasms."
  - target: 01-human/03-molecular/thrombopoietin
    relation: connects-to
    note: "Essential thrombocythemia hijacks thrombopoietin signaling: TPO normally tells the marrow how many platelets to make through the MPL receptor, but ET's JAK2, CALR, and MPL mutations switch that pathway on permanently, churning out platelets without the hormone's command."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "All of ET's driver mutations converge on STAT: JAK2, CALR, and MPL defects all end up activating STAT transcription factors, the shared switch that turns on the genes driving runaway platelet production—why JAK-STAT inhibitors are used in the disease."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Platelets in essential thrombocythemia clot through calcium: calcium signaling triggers platelet activation and aggregation, so the vast excess of platelets, primed to release and respond to calcium, tips patients toward the thromboses that menace them."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Platelet-rich blood in essential thrombocythemia can fake high potassium: the enormous platelet mass leaks potassium after the sample clots, producing pseudohyperkalemia—a lab artifact to recognize before treating a number that isn't real."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Essential thrombocythemia strikes the brain's small vessels: excess platelets cause headaches, visual disturbance, TIAs and burning red extremities (erythromelalgia), microvascular symptoms that low-dose aspirin often relieves."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 marks the line between reactive and clonal thrombocytosis: this cytokine drives platelet production in inflammation, so a high count from infection or cancer must be told apart from the clonal overproduction that defines essential thrombocythemia."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Essential thrombocythemia starves fingertips of oxygen: clumps of excess platelets plug tiny vessels, causing the burning, red, oxygen-starved hands and feet of erythromelalgia and risking digital ischemia."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Essential thrombocythemia threatens the heart: its thrombotic tendency raises the risk of coronary clots and heart attacks, part of why even symptom-free patients may need aspirin and cytoreduction."
  - target: 01-human/03-molecular/fibrinogen
    relation: connects-to
    note: "Essential thrombocythemia turns fibrinogen into clots: the swollen platelet mass, activating with fibrinogen, builds the thromboses—strokes, heart attacks, and vein clots—that are the disease's main danger."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "ET is confirmed under the microscope: the marrow biopsy shows clusters of enlarged, staghorn megakaryocytes, the clue that with JAK2 and CALR testing distinguishes it from reactive thrombocytosis."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "ET clots the gut's veins: splanchnic and mesenteric vein thrombosis can be the first sign, so an unprovoked abdominal-vein clot prompts testing for the JAK2 mutation behind the disease."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "ET can scar into myelofibrosis: over years, reticulin and collagen fibrosis gradually replace the marrow, the feared post-ET transformation that brings cytopenias and splenomegaly."
---

# Essential Thrombocythemia

## Overview

**Essential thrombocythemia (ET)** is a **BCR-ABL1-negative myeloproliferative neoplasm (MPN)** defined by clonal megakaryocytic hyperplasia with sustained thrombocytosis (platelet count ≥450 × 10⁹/L) driven by gain-of-function mutations in JAK2 (~55-60%), CALR (~20-25%), or MPL (~5-8%) — the three major mutually exclusive MPN driver mutations that all constitutively activate the JAK2→STAT5 megakaryopoietic axis. ET is characterized by a generally favorable prognosis with median overall survival approaching that of the general population, but with significant morbidity from **thrombosis** (arterial and venous), **microvascular symptoms** (erythromelalgia, headache, visual disturbances), and **bleeding** at extreme platelet counts. Treatment is risk-stratified using the revised IPSET-Thrombosis score: all high-risk patients (age ≥60 or prior thrombosis) receive aspirin plus cytoreductive therapy — **hydroxyurea** is first-line (PT-1 trial: superior to anagrelide in arterial thrombosis prevention, MF rate, and bleeding) [^harrison-2005-pt1-et]; low-risk and very low-risk patients receive observation or aspirin alone. Long-term complications include post-ET myelofibrosis (~1-2% at 10 years) and AML transformation (<1% at 10 years) [^barbui-2012-ipset].

**Epidemiology:**
- Incidence: ~0.6-2.5 per 100,000/year; prevalence ~30-40 per 100,000
- Median age at diagnosis: ~60 years; bimodal distribution with a younger peak in women aged 30-50 (CALR-associated)
- Slight female predominance overall; younger ET predominantly female (CALR-driven)
- Median OS: approaching general population for low/intermediate risk; high-risk has shortened OS due to thrombotic events and transformation

## Structure

### WHO 2022 diagnostic criteria

All four criteria must be met:

1. **Platelet count ≥450 × 10⁹/L persistently** (sustained on ≥2 measurements at least 1 month apart)
2. **Bone marrow biopsy:** Proliferation of the megakaryocytic lineage with large, mature megakaryocytes with hyperlobated "staghorn" nuclei; no significant increase or left shift in neutrophil granulopoiesis or erythropoiesis; rarely any minor reticulin fibrosis (Grade 1)
3. **Not meeting WHO criteria for:** BCR-ABL1+ CML, PV, PMF, MDS, or other myeloid neoplasms
4. **Presence of JAK2 V617F, CALR exon 9 (del/ins), or MPL exon 10 mutation;** OR in absence of mutation: exclusion of secondary thrombocytosis (reactive: infection, inflammation, iron deficiency, splenectomy) and clonal marker by NGS

### Molecular landscape

**JAK2 V617F (~55-60% of ET):**
Exon 14 GOF mutation in JH2 pseudokinase → constitutive JAK2/STAT5; in ET, JAK2 V617F allele burden (VAF) is typically 25-50% (lower than in PV where VAF is often >50% and frequently homozygous); heterozygous JAK2 in ET → preferential megakaryocytic phenotype (compared to erythroid in PV); JAK2-positive ET has higher thrombosis risk (arterial) than CALR-mutant ET.

**CALR exon 9 mutations (~20-25% of ET):**
Frameshift insertions/deletions generating a novel positively charged C-terminus that binds MPL ECD → constitutive JAK2/STAT5; **type 2 ins5bp** is the predominant CALR mutation in ET (vs type 1 del52bp which predominates in PMF); type 2 CALR → weaker MPL activation → milder megakaryocytic phenotype → ET (not PMF); CALR-mutant ET: younger patients, higher platelet counts, lower thrombosis risk, longer overall survival than JAK2-mutant ET; lower risk of transformation to AML.

**MPL exon 10 mutations (~5-8% of ET):**
W515L, W515K, S505, Y591 — transmembrane/juxtatransmembrane domain GOF → constitutive JAK2 activation without TPO; clinically similar to CALR-mutant ET (younger age, higher platelets, lower thrombosis risk); less common and may be underdiagnosed due to limited panel coverage.

**Triple-negative ET (~15%):**
JAK2/CALR/MPL wild-type; requires careful exclusion of reactive thrombocytosis, early MDS, and atypical CML; if truly clonal (demonstrated by NGS identifying other somatic mutations), prognosis generally good; higher proportion may represent polyclonal reactive conditions.

**Co-mutations:**
Additional mutations in ~20-30% at diagnosis: TET2 (~11%), DNMT3A (~6%), ASXL1 (~5%), SF3B1 (<5%); ASXL1 co-mutation → increased MF transformation risk; SF3B1 co-mutation with JAK2 or CALR → consider whether MDS overlap (ring sideroblasts + thrombocytosis → WHO entity "MDS/MPN with ring sideroblasts and thrombocytosis").

## Function

### Pathophysiology of megakaryocytic expansion

**JAK2/STAT5 → megakaryopoiesis:**
Constitutive JAK2 activation (via JAK2 V617F, CALR/MPL) → STAT5 phosphorylation → BCL-XL (megakaryocyte survival), CCND1 (proliferation), MPL itself (positive feedback) → expanded CFU-MK pool → increased endomitosis → large hyperlobated megakaryocytes → excessive proplatelet formation → sustained thrombocytosis (platelet count 450-2,000+ × 10⁹/L).

**Thrombosis mechanisms:**
- Platelet activation: JAK2 V617F platelets have surface P-selectin expression at rest → activated state → platelet-leukocyte interactions → thrombosis
- NETosis: Neutrophil JAK2 V617F → increased NET formation → endothelial activation → venous thrombosis (DVT, PE, splanchnic vein)
- Platelet count contribution: Platelet count correlates weakly with thrombosis risk — JAK2 allele burden, leukocyte count, and cardiovascular risk factors are better predictors (IPSET model)

**Bleeding at high platelet counts:**
Platelet count >1,500 × 10⁹/L → acquired von Willebrand syndrome (AVWS): platelet surface GPIb absorbs large VWF multimers → depletion of high-molecular-weight VWF → impaired primary hemostasis → paradoxical bleeding (GI bleeding, epistaxis); aspirin contraindicated at platelet count >1,500 × 10⁹/L; cytoreduction first (reduce platelets to safe range); AVWS improves with platelet count normalization.

**Microvascular symptoms:**
- **Erythromelalgia:** Burning, redness, warmth of extremities (hands/feet); caused by platelet-mediated microvascular occlusion + prostaglandin release; aspirin highly effective (within 48 hours)
- **Headache, visual disturbances:** Platelet microthrombi in cerebral microvasculature → transient neurological symptoms; aspirin provides relief
- **Pruritus:** Less prominent than in PV but can occur with JAK2-positive ET

## Pathology

### Risk stratification — revised IPSET-Thrombosis

| Risk Category | Criteria | Annual Thrombosis Rate | Treatment |
|---|---|---|---|
| Very low | Age <60, JAK2-negative, no prior thrombosis | ~0.5%/year | Observation vs aspirin |
| Low | Age <60, JAK2-positive, no prior thrombosis | ~1.5%/year | Aspirin 81-100 mg/day |
| Intermediate | Age ≥60, JAK2-negative, no prior thrombosis | ~2%/year | Aspirin ± cytoreduction (debated) |
| High | Prior thrombosis (any age) OR age ≥60 + JAK2-positive | ~3-5%/year | Aspirin + cytoreduction |

Cardiovascular risk factors (hypertension, diabetes, smoking, dyslipidemia) multiplicatively increase thrombosis risk; leukocytosis (WBC >11 × 10⁹/L) is an additional adverse factor.

### Treatment

**Aspirin:**
Low-dose aspirin 81-100 mg/day is the foundation of ET treatment for symptomatic and JAK2-positive patients; mechanism: irreversible COX-1 inhibition → reduced thromboxane A2 → reduced platelet aggregation; effective for microvascular symptoms (erythromelalgia, headache) and reduces thrombotic events; aspirin carries bleeding risk (especially GI) — balance against thrombosis risk; contraindicated when platelet count >1,500 × 10⁹/L (AVWS → bleeding risk outweighs thrombosis prevention).

**Hydroxyurea (first-line cytoreduction):**
Ribonucleotide reductase inhibitor; reduces all lineages; effective platelet reduction within weeks; PT-1 trial: hydroxyurea + aspirin vs anagrelide + aspirin in high-risk ET; HU arm: fewer arterial thromboses (3.6% vs 9.3% at 2 years), less MF transformation (7.0% vs 13.7%), less bleeding [^harrison-2005-pt1-et]; dose: 500-2,000 mg/day titrated to platelet target <400 × 10⁹/L; standard target: platelet <400 × 10⁹/L + WBC 2-10 × 10⁹/L; toxicities: leg ulcers (~5%), myelosuppression, mucositis; resistance criteria (ELN): platelet >600 × 10⁹/L at ≥2 g/day, or toxicity.

**Anagrelide (second-line):**
Phosphodiesterase 3A (PDE3A) inhibitor → specifically impairs megakaryocyte differentiation → reduces platelet count without significantly affecting other lineages; mechanism unique (not cytotoxic, not RNR inhibition); dose: 0.5-3 mg/day orally in divided doses; PT-1 demonstrated anagrelide inferiority to HU in high-risk ET (more arterial thromboses, more MF, more bleeding); preferred in HU-intolerant patients or women of childbearing age (HU teratogenic); cardiovascular side effects: palpitations, fluid retention, headache (PDE3A also expressed in cardiac tissue).

**Interferon-alpha (IFN-α):**
Pegylated IFN-α (ropeginterferon alfa-2b, peginterferon alfa-2a): suppresses JAK2-mutant clone via STAT1 upregulation → anti-proliferative → preferred in younger patients (<60) and pregnant/potentially pregnant women (safety data better than HU); IFN is not teratogenic (recommended for ET in pregnancy); achieves molecular responses (JAK2 VAF reduction); adverse effects: flu-like symptoms, autoimmune thyroiditis, depression; not FDA-approved specifically for ET (off-label use; approved for PV).

**Ruxolitinib:**
JAK1/2 inhibitor; active in ET (reduces platelet count and spleen) but not FDA-approved for ET; may be considered for HU-intolerant patients in clinical trial settings; RESPONSE-2 trial focused on PV, not ET; ongoing trials evaluating ruxolitinib in ET with high burden.

**Busulfan:**
For elderly HU-intolerant patients; short courses achieve prolonged platelet reduction; limited by mutagenic potential.

### Post-ET myelofibrosis (post-ET MF)

**Transformation rate:** ~1-2% at 10 years (much lower than PV → post-PV MF); ~4-6% at 15-20 years; defined by new BM reticulin fibrosis ≥2, new anemia, leukoerythroblastic blood film, splenomegaly; co-mutations (ASXL1, SRSF2, EZH2) accelerate transformation; CALR-mutant ET has lower MF risk than JAK2-mutant ET.

**Treatment of post-ET MF:**
Similar to PMF: ruxolitinib for symptomatic splenomegaly; fedratinib; momelotinib (ACVR1/JAK1/2, addresses TGF-β-driven anemia); luspatercept for anemia; allo-SCT for eligible intermediate/high-risk post-ET MF.

### AML/blast transformation

**Rate:** <1-2% lifetime risk from ET (lowest of the MPNs); substantially higher in anaplastic progression or with HU-induced myelosuppression in retrospective series (debated); prior alkylator exposure (busulfan, pipobroman) → higher AML risk; JAK2-mutant ET → higher AML risk than CALR-mutant ET; AML from ET: TP53 mutations acquired at transformation; treated as secondary AML (poor prognosis with standard induction; azacitidine+venetoclax if eligible; allo-SCT).

### ET in pregnancy

ET carries risks of:
- **Maternal:** First-trimester miscarriage (placental microvascular thrombosis), thrombosis
- **Fetal:** Placental insufficiency, IUGR, stillbirth
Management:
- Low-risk ET in pregnancy: aspirin 81 mg/day throughout; heparin peri-delivery
- High-risk (prior thrombosis, prior pregnancy loss ×2): add IFN-α (not HU — teratogenic); aspirin + LMWH peri-delivery
- Platelet count typically falls in second trimester (hemodilution) → may not require cytoreduction
- Avoid anagrelide (crosses placenta), HU (teratogenic), ruxolitinib (insufficient data) in pregnancy

## Connections

- `connects-to` → **[MPL](../../03-molecular/mpl/README.md)** — MPL W515L/K mutations (~5-8% ET) cause constitutive JAK2/STAT5 activation independent of TPO; MPL-mutant ET is clinically similar to CALR-mutant ET (lower thrombosis risk vs JAK2); TPO-receptor agonists (eltrombopag, romiplostim) act on wild-type MPL.
- `connects-to` → **[JAK2](../../03-molecular/jak2/README.md)** — JAK2 V617F (~55-60% ET) causes constitutive erythroid/megakaryocytic/granulocytic proliferation; JAK2-positive ET has higher thrombosis risk than CALR-mutant ET; ruxolitinib is active in JAK2 V617F ET but is not FDA-approved for ET.
- `connects-to` → **[CALR](../../03-molecular/calr/README.md)** — CALR mutations (~20-25% ET); type 2 ins5bp is predominant in ET (vs type 1 del52bp in PMF); CALR-mutant ET has lower thrombosis risk, younger age, and longer OS than JAK2-mutant ET; JAK2/CALR/MPL mutations are mutually exclusive.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — ET transforms to post-ET MF (~1-2% at 10 years); megakaryocyte-derived TGF-β1 → reticulin → collagen fibrosis; co-mutations (ASXL1, EZH2, SRSF2) accelerate MF transformation; momelotinib targets ACVR1 to address anemia in post-ET MF.
- `connects-to` → **[Von Willebrand Factor](../../03-molecular/von-willebrand-factor/README.md)** — At platelet counts >1,500 ×10⁹/L, ET causes acquired von Willebrand syndrome — platelet GPIb adsorbs high-molecular-weight VWF multimers and depletes them, impairing primary hemostasis → paradoxical bleeding; aspirin is contraindicated until cytoreduction normalizes the count.
- `connects-to` → **[Polycythemia Vera](../polycythemia-vera/README.md)** — PV and ET are both JAK2-driven MPNs on a phenotypic continuum; PV (JAK2 nearly 100%, often homozygous) skews erythroid while ET skews megakaryocytic; JAK2 V617F-ET can drift toward a PV phenotype; ET has lower post-MF and AML transformation risk than PV.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Clonal megakaryocytic hyperplasia drives sustained thrombocytosis; JAK2 V617F platelets are constitutively activated (resting P-selectin) → platelet-leukocyte aggregates and thrombosis; erythromelalgia from platelet microvascular occlusion responds rapidly to aspirin.
- `connects-to` → **[Disseminated Intravascular Coagulation](../disseminated-intravascular-coagulation/README.md)** — Essential thrombocythemia and DIC are opposite poles of platelet pathology: ET clonally overproduces platelets causing thrombosis (and, at extreme counts, acquired von Willebrand bleeding), while DIC systemically consumes platelets and clotting factors — too many versus too few.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Essential thrombocythemia is a clonal bone marrow disease: a JAK2, CALR, or MPL mutation drives autonomous megakaryocyte hyperplasia, so the marrow shows large, mature, clustered megakaryocytes without the dense fibrosis of primary myelofibrosis — a key WHO distinction.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — Mild splenomegaly is common in essential thrombocythemia from extramedullary hematopoiesis and pooling; progressive splenic enlargement signals transformation to post-ET myelofibrosis, and prior splenectomy paradoxically raises platelet counts and thrombosis risk.
- `connects-to` → **[Myeloproliferative Neoplasms](../myeloproliferative-neoplasms/README.md)** — Essential thrombocythemia is one of the three classic Philadelphia-negative myeloproliferative neoplasms (with PV and PMF): a JAK2/CALR/MPL-driven clonal overproduction—here of platelets—sharing thrombosis risk and the capacity to evolve into myelofibrosis or AML.
- `connects-to` → **[Myelofibrosis](../myelofibrosis/README.md)** — Essential thrombocythemia can progress to post-ET myelofibrosis: over years the clone drives marrow reticulin fibrosis, so the platelet-rich blood picture gives way to splenomegaly, cytopenias and a leukoerythroblastic film, converging with primary myelofibrosis.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Thrombosis—not bleeding—is the main danger of essential thrombocythemia: the dysfunctional excess platelets and JAK2 mutation create a prothrombotic state causing arterial and venous events, including VTE and unusual-site (splanchnic) thrombosis; aspirin lowers risk.
- `connects-to` → **[Chronic Myeloid Leukemia](../cml/README.md)** — ET and CML are both chronic myeloproliferative neoplasms but driven differently: CML by the BCR-ABL fusion tyrosine kinase (treatable with imatinib), ET by JAK2/CALR/MPL mutations driving platelet overproduction—both can progress to fibrosis or acute leukemia.
- `connects-to` → **[Stroke](../stroke/README.md)** — ET predisposes to stroke: the excess, often dysfunctional platelets promote arterial thrombosis, so TIAs and stroke are feared complications—low-dose aspirin and cytoreduction lower this risk, a rare case where too many platelets cause clots, not bleeding.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — ET and polycythemia vera show how one marrow can overproduce different lineages: ET expands megakaryocytes and platelets while PV expands erythrocytes, yet both arise from JAK2-pathway mutations—lineage skewing of a shared clonal stem-cell defect sets the phenotype.
- `connects-to` → **[Thrombin](../../03-molecular/thrombin/README.md)** — Excess platelets in essential thrombocythemia tip toward thrombin-driven clotting: the high, often dysfunctional platelet mass promotes both arterial and venous thrombosis, so low-dose aspirin and cytoreduction lower the clotting risk that dominates ET's morbidity.
- `connects-to` → **[AML](../aml/README.md)** — Essential thrombocythemia carries a small but real risk of transforming to AML: as a clonal myeloproliferative neoplasm, ET can evolve through myelofibrosis to acute leukemia, a risk raised by some cytoreductive drugs—the feared long-term endpoint.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Essential thrombocythemia often raises neutrophils too: the JAK2-driven clone expands multiple myeloid lineages, so leukocytosis often accompanies the thrombocytosis and itself predicts higher thrombosis risk—ET is a panmyeloid, not platelet-only, disease.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Essential thrombocythemia clots at the endothelium: excess, often dysfunctional platelets interact with the vessel lining to cause microvascular and large-vessel thrombosis, so antiplatelet therapy targeting this platelet-endothelial interface prevents the main complication.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Essential thrombocythemia is a classic cause of splanchnic vein thrombosis: the prothrombotic platelet excess can clot the hepatic or portal veins (Budd-Chiari), so unexplained abdominal vein thrombosis should prompt testing for JAK2 and an underlying MPN.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Essential thrombocythemia produces distinctive neurovascular symptoms: microvascular platelet plugging causes headaches, visual disturbance and erythromelalgia, and it raises stroke and TIA risk—so the nervous system often signals the disease before a major clot occurs.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — Essential thrombocythemia complicates pregnancy through the placenta: the thrombotic tendency causes placental clots, miscarriage, and growth restriction, so pregnant patients are managed with low-dose aspirin and sometimes heparin to protect the placenta.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Essential thrombocythemia announces itself in the skin as erythromelalgia: platelet microthrombi in small vessels cause burning, red, painful hands and feet, a near-specific symptom that dramatically improves with low-dose aspirin.
- `connects-to` → **[Gout](../gout/README.md)** — Essential thrombocythemia's high cell turnover can cause gout: rapid platelet and cell production raises uric acid, so hyperuricemia and gout flares accompany this and other myeloproliferative neoplasms.
- `connects-to` → **[Thrombopoietin](../../03-molecular/thrombopoietin/README.md)** — Essential thrombocythemia hijacks thrombopoietin signaling: TPO normally tells the marrow how many platelets to make through the MPL receptor, but ET's JAK2, CALR, and MPL mutations switch that pathway on permanently, churning out platelets without the hormone's command.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — All of ET's driver mutations converge on STAT: JAK2, CALR, and MPL defects all end up activating STAT transcription factors, the shared switch that turns on the genes driving runaway platelet production—why JAK-STAT inhibitors are used in the disease.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Platelets in essential thrombocythemia clot through calcium: calcium signaling triggers platelet activation and aggregation, so the vast excess of platelets, primed to release and respond to calcium, tips patients toward the thromboses that menace them.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Platelet-rich blood in essential thrombocythemia can fake high potassium: the enormous platelet mass leaks potassium after the sample clots, producing pseudohyperkalemia—a lab artifact to recognize before treating a number that isn't real.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Essential thrombocythemia strikes the brain's small vessels: excess platelets cause headaches, visual disturbance, TIAs and burning red extremities (erythromelalgia), microvascular symptoms that low-dose aspirin often relieves.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6 marks the line between reactive and clonal thrombocytosis: this cytokine drives platelet production in inflammation, so a high count from infection or cancer must be told apart from the clonal overproduction that defines essential thrombocythemia.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Essential thrombocythemia starves fingertips of oxygen: clumps of excess platelets plug tiny vessels, causing the burning, red, oxygen-starved hands and feet of erythromelalgia and risking digital ischemia.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Essential thrombocythemia threatens the heart: its thrombotic tendency raises the risk of coronary clots and heart attacks, part of why even symptom-free patients may need aspirin and cytoreduction.
- `connects-to` → **[Fibrinogen](../../03-molecular/fibrinogen/README.md)** — Essential thrombocythemia turns fibrinogen into clots: the swollen platelet mass, activating with fibrinogen, builds the thromboses—strokes, heart attacks, and vein clots—that are the disease's main danger.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — ET is confirmed under the microscope: the marrow biopsy shows clusters of enlarged, staghorn megakaryocytes, the clue that with JAK2 and CALR testing distinguishes it from reactive thrombocytosis.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — ET clots the gut's veins: splanchnic and mesenteric vein thrombosis can be the first sign, so an unprovoked abdominal-vein clot prompts testing for the JAK2 mutation behind the disease.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — ET can scar into myelofibrosis: over years, reticulin and collagen fibrosis gradually replace the marrow, the feared post-ET transformation that brings cytopenias and splenomegaly.

[^harrison-2005-pt1-et]: Harrison CN, Campbell PJ, Buck G, et al. Hydroxyurea compared with anagrelide in high-risk essential thrombocythemia. *N Engl J Med.* 2005;353(1):33-45. [doi:10.1056/NEJMoa043800](https://doi.org/10.1056/NEJMoa043800) · [PubMed 16000354](https://pubmed.ncbi.nlm.nih.gov/16000354/)
[^barbui-2012-ipset]: Barbui T, Finazzi G, Carobbio A, et al. Development and validation of an International Prognostic Score of thrombosis in World Health Organization-essential thrombocythemia (IPSET-thrombosis). *Blood.* 2012;120(26):5128-5133. [doi:10.1182/blood-2012-07-444067](https://doi.org/10.1182/blood-2012-07-444067) · [PubMed 23086758](https://pubmed.ncbi.nlm.nih.gov/23086758/)
