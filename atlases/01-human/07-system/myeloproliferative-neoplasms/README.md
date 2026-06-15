---
schema: human-scale-entry/v1
id: myeloproliferative-neoplasms
name: Myeloproliferative Neoplasms
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Myeloproliferative neoplasms (PV, ET, MF) are driven by JAK2 V617F in >95% of PV and ~50-60% of ET/MF; CALR and MPL mutations account for remaining cases. Ruxolitinib (JAK1/2 inhibitor) is standard for myelofibrosis and PV; alloSCT is curative for high-risk MF."
aliases: ["myeloproliferative neoplasms", "MPN", "polycythemia vera", "PV", "essential thrombocythemia", "ET", "myelofibrosis", "MF", "primary myelofibrosis", "JAK2 V617F MPN", "Philadelphia-negative MPN"]
sources:
  - id: verstovsek-2012-comfort-i
    type: peer-reviewed
    cite: "Verstovsek S, Mesa RA, Gotlib J, et al. A double-blind, placebo-controlled trial of ruxolitinib for myelofibrosis. N Engl J Med. 2012;366(9):799-807."
    doi: "10.1056/NEJMoa1110557"
    pmid: "22375971"
    url: "https://doi.org/10.1056/NEJMoa1110557"
  - id: vannucchi-2015-response
    type: peer-reviewed
    cite: "Vannucchi AM, Kiladjian JJ, Griesshammer M, et al. Ruxolitinib versus standard therapy for the treatment of polycythemia vera. N Engl J Med. 2015;372(5):426-435."
    doi: "10.1056/NEJMoa1409002"
    pmid: "25426978"
    url: "https://doi.org/10.1056/NEJMoa1409002"
cross_links:
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Ruxolitinib (JAK1/2 inhibitor, COMFORT-I/II) reduces spleen volume >35% in ~40% of MF patients and prolongs OS; ruxolitinib also standard for PV (RESPONSE: reduced HCT and spleen); fedratinib and pacritinib are alternative JAK2 inhibitors for MF with cytopenias."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "JAK2 V617F → constitutive STAT5 phosphorylation → EPO-independent erythropoiesis in PV; STAT5 is the primary effector of JAK2 → BCL-XL, CCND1, MYC → erythroid survival; STAT3 mediates inflammatory cytokine production in MF (IL-6, IL-8)."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "EPO → EPOR → JAK2 → STAT5 is the normal erythropoiesis axis; JAK2 V617F bypasses EPO requirement → autonomous red cell production → polycythemia in PV; serum EPO is suppressed in PV (EPO-independent erythropoiesis) and elevated in secondary polycythemia."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β1 secreted by MPN megakaryocytes drives collagen deposition → bone marrow fibrosis in MF; TGF-β/SMAD pathway activation is central to MF fibrosis; luspatercept (activin receptor ligand trap targeting SMAD2/3) approved for MF-associated anemia (INDEPENDENCE trial)."
  - target: 01-human/07-system/polycythemia-vera
    relation: connects-to
    note: "Polycythemia vera is the erythroid-predominant MPN — JAK2 V617F (often homozygous via 9p uniparental disomy) drives EPO-independent erythrocytosis, raising thrombosis risk; managed with phlebotomy to HCT <45% and aspirin, and it can evolve to post-PV myelofibrosis."
  - target: 01-human/03-molecular/jak2
    relation: connects-to
    note: "The JAK2 V617F mutation in the JH2 pseudokinase domain unifies the MPNs — present in ~95% of PV and ~55-60% of ET and MF — by removing autoinhibition for constitutive JAK-STAT signaling; allele burden tracks phenotype (heterozygous→ET, homozygous→PV)."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "MPNs are clonal stem-cell diseases of the bone marrow: panmyeloid hypercellularity in PV, megakaryocytic hyperplasia in ET, and progressive reticulin/collagen fibrosis (MF-0 to MF-3) in myelofibrosis that drives marrow failure and extramedullary hematopoiesis with splenomegaly."
  - target: 01-human/07-system/cmml
    relation: connects-to
    note: "Chronic myelomonocytic leukemia is the MDS/MPN-overlap cousin of the classic myeloproliferative neoplasms: it shares their JAK2/RAS-driven proliferation, splenomegaly, and JAK-inhibitor responsiveness, but adds the peripheral monocytosis and dysplasia of MDS."
  - target: 01-human/07-system/myelofibrosis
    relation: connects-to
    note: "Myelofibrosis is the most aggressive classic MPN: JAK2/CALR/MPL-driven megakaryocytes secrete TGF-β that scars the marrow with reticulin and collagen, forcing extramedullary hematopoiesis (splenomegaly) and marrow failure; it arises de novo or evolves from PV or ET."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "Splenomegaly is the clinical signature of the myeloproliferative neoplasms, most extreme in myelofibrosis where the spleen takes over blood production (extramedullary hematopoiesis) and can fill the abdomen; JAK inhibitors (ruxolitinib) shrink it, splenectomy a last resort."
  - target: 01-human/07-system/essential-thrombocythemia
    relation: connects-to
    note: "Essential thrombocythemia is one of the three classic BCR-ABL-negative myeloproliferative neoplasms, alongside polycythemia vera and myelofibrosis: a JAK2, CALR, or MPL mutation drives clonal megakaryocyte overproduction and a high platelet count, with thrombosis the main risk."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Platelets are central to MPN morbidity: clonal megakaryocytes overproduce platelets that are also qualitatively abnormal, so essential thrombocythemia and polycythemia vera cause both thrombosis and—at very high counts—bleeding from acquired von Willebrand defects."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Thrombosis is the leading cause of death in myeloproliferative neoplasms: JAK2-mutant blood is prothrombotic, producing arterial and venous clots including splanchnic-vein thromboses (Budd-Chiari, portal vein)—so cytoreduction and aspirin aim to prevent VTE."
  - target: 01-human/07-system/cml
    relation: connects-to
    note: "CML is the classic BCR-ABL-positive myeloproliferative neoplasm, set apart from the JAK2/CALR/MPL-driven 'Philadelphia-negative' MPNs: all overproduce mature myeloid cells, but CML's defining t(9;22) kinase makes it uniquely controllable with imatinib."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "Myeloproliferative neoplasms can transform into acute myeloid leukemia: chronic clonal proliferation accumulates mutations until differentiation fails and blasts take over—post-MPN AML carries a grim prognosis, the feared endpoint of these diseases."
  - target: 01-human/07-system/gout
    relation: connects-to
    note: "MPNs commonly cause secondary gout: the high cell turnover floods the blood with purines that break down to uric acid, so hyperuricemia and gout flares accompany polycythemia vera and myelofibrosis—sometimes the first clue to an underlying MPN."
  - target: 01-human/03-molecular/calr
    relation: connects-to
    note: "CALR mutation is a major MPN driver alongside JAK2: in JAK2-negative essential thrombocythemia and myelofibrosis, calreticulin mutations activate the same thrombopoietin-receptor pathway, so CALR testing completes the molecular workup of myeloproliferative neoplasms."
  - target: 01-human/03-molecular/mpl
    relation: connects-to
    note: "MPL, the thrombopoietin receptor, is the third classic MPN driver: activating MPL mutations switch on JAK-STAT signaling in a minority of essential thrombocythemia and myelofibrosis, so JAK2, CALR and MPL together explain most myeloproliferative neoplasms."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Overproduction of red cells defines polycythemia vera within the MPN family: JAK2-driven erythroid expansion thickens the blood and raises clot risk, illustrating how each MPN over-makes one lineage—red cells here, platelets in ET, fibrosis in myelofibrosis."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Myeloproliferative neoplasms overproduce mature myeloid cells including neutrophils: the JAK2/CALR/MPL-driven clone expands granulocytes along with red cells and platelets, so leukocytosis is common and itself contributes to the thrombotic risk that defines MPN morbidity."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Thrombosis is the leading complication of myeloproliferative neoplasms: thick, sticky blood from excess cells and an activated, inflammatory clone causes arterial events including stroke, so cytoreduction and antiplatelet therapy aim to prevent these clots."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Myeloproliferative neoplasms classically cause splanchnic vein thrombosis: the prothrombotic clone clots the hepatic or portal veins (Budd-Chiari), so unexplained abdominal-vein thrombosis should prompt JAK2 testing—sometimes the first sign of an occult MPN."
  - target: 01-human/03-molecular/thrombopoietin
    relation: connects-to
    note: "MPNs hijack thrombopoietin signaling: CALR and MPL mutations make blood cells respond as if flooded with thrombopoietin even when levels are normal, driving the runaway platelet and megakaryocyte production of essential thrombocythemia and myelofibrosis."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Myelofibrosis is the scarring face of MPNs: clonal megakaryocytes pour out cytokines that drive fibroblasts to lay down marrow fibrosis, choking blood production and forcing the spleen and liver to take over—the hallmark of advanced disease."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Polycythemia vera ties MPNs to iron: overproduction of red cells consumes iron and therapeutic phlebotomy deliberately induces iron deficiency to limit red-cell mass, so iron balance is both a consequence and a lever of treatment."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Myeloproliferative neoplasms smolder with IL-6 and inflammation: the JAK2-mutant clone pumps out IL-6 and other cytokines that cause fevers, weight loss, and itching and drive progression to fibrosis—why JAK inhibitors relieve symptoms so well."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Immune surveillance by NK cells shapes myeloproliferative neoplasms: natural killer cells help police the mutant clone, and their exhaustion or dysfunction may let the disease expand—an angle for immune-based approaches alongside JAK inhibitors."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "MPN stem cells use autophagy to persist through treatment: the clonal cells recycle their contents to survive stress and JAK inhibition, so blocking autophagy is studied as a way to deepen responses and target the disease at its root."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "High blood counts in MPN can fake high potassium: the huge numbers of platelets and white cells leak potassium after the sample clots, producing pseudohyperkalemia—a lab artifact to recognize before treating a number that isn't real."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "MPNs threaten the brain with clots: thickened, sticky blood from too many cells raises the risk of stroke and cerebral vein thrombosis, so controlling counts and using aspirin aim to protect against these neurologic catastrophes."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Inflammation via NF-kB fuels the myeloproliferative clone: alongside JAK-STAT, the mutated stem cells drive NF-kB signaling that pours out cytokines, feeding the symptoms, marrow fibrosis and clonal expansion of these neoplasms."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "MPNs itch through the skin: aquagenic pruritus—intense itching minutes after a warm shower—is a classic symptom, especially of polycythemia vera, sometimes appearing before the diagnosis."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "MPN itching is driven by mast cells: the expanded clone's basophils and mast cells release histamine, which fires skin itch nerves to cause the aquagenic pruritus that torments these patients."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Polycythemia overrides the body's oxygen control: normally low oxygen raises erythropoietin to make red cells, but the JAK2 clone churns them out regardless, thickening the blood independent of oxygen need."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Radioactive phosphorus once tamed these clones with electrons: P-32 concentrates in marrow and emits beta particles — fast electrons — that suppress the overactive blood-cell factory, a historic polycythemia treatment now reserved for select older patients."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Myeloproliferative disease can choke the lungs: extramedullary hematopoiesis and microvascular thrombosis raise pulmonary pressures, so pulmonary hypertension and clots are recognized complications, especially in myelofibrosis."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "The kidney bears the brunt of high cell turnover: the massive production and breakdown of blood cells floods the blood with uric acid, which crystallizes in the tubules and can drive urate nephropathy and stones."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Myeloproliferative disease clots the arteries too: the thick, sticky blood and activated platelets drive arterial thrombosis, so heart attacks join the strokes and venous clots that menace these patients."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "MPN is a leading cause of unusual-site clots: thrombosis of the splanchnic veins draining the gut — portal, mesenteric, and the hepatic veins of Budd-Chiari — can be the first sign, sometimes before the blood counts even rise."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "The frenzied cell turnover spills phosphorus: the constant birth and death of blood cells, and their lysis under treatment, release phosphate and urate, the metabolic overflow that strains the kidneys and provokes gout."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Thrombosis is the central danger of MPN: the JAK2-mutant, thickened blood plus an activated, sticky endothelial-cell lining drives clots in both arteries and veins, the strokes and heart attacks that are the leading cause of death in these disorders."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "A maddening itch after a warm bath marks polycythemia vera: basophils and mast cells expanded by the MPN clone dump histamine, the aquagenic pruritus that water triggers being one of the disease's most distinctive complaints."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Sludgy blood blurs the vision: the hyperviscosity of a high red-cell or platelet count slows retinal flow, causing visual disturbances and engorged retinal veins, while erythromelalgia's burning can be matched by ocular symptoms in advanced disease."
---

# Myeloproliferative Neoplasms

## Overview

**Myeloproliferative neoplasms (MPN)** are a group of clonal hematopoietic stem cell disorders characterized by excessive production of mature blood cells — erythrocytes (polycythemia vera, PV), platelets (essential thrombocythemia, ET), or fibrotic marrow remodeling with panmyeloid dysregulation (myelofibrosis, MF) — without significant dysplasia (distinguishing MPN from MDS). The unifying molecular basis of "Philadelphia-negative MPN" (classical MPN — PV, ET, MF) is constitutive JAK-STAT pathway activation, most commonly via the **JAK2 V617F** somatic mutation (~95% of PV, ~55% of ET, ~60% of MF) or, in JAK2 V617F-negative cases, calreticulin (CALR) frameshift mutations (~25% of ET/MF) or MPL (thrombopoietin receptor) mutations (~5%). Ruxolitinib, a JAK1/2 inhibitor, is the primary targeted therapy for MF and refractory PV; allogeneic stem cell transplantation remains the only curative option for high-risk MF [^verstovsek-2012-comfort-i].

**Epidemiology:**
- PV: ~3 per 100,000/year; median age ~60; M:F ~1.2:1; JAK2 V617F ~95-97%
- ET: ~1-2.5 per 100,000/year; bimodal distribution (young women, older patients); JAK2 V617F ~55%
- Primary MF: ~0.5-1.5 per 100,000/year; most common older patients; median age ~67; worst prognosis of classical MPN
- MPN transformation: PV → post-PV MF (~15-20% at 15 years); ET → post-ET MF (~5-10% at 10 years); blast-phase (AML transformation) ~5-10% for MF, ~2-3% for PV/ET
- Post-PV MF and post-ET MF are treated like primary MF

**Classification (WHO 2022):**
- Polycythemia vera (PV): Absolute erythrocytosis + JAK2 mutation (minor criterion: BM hypercellularity + low EPO)
- Essential thrombocythemia (ET): Platelets >450 × 10⁹/L + MPN driver mutation (JAK2/CALR/MPL) + BM megakaryocytic hyperplasia + no other MPN
- Primary myelofibrosis (PMF): Megakaryocytic atypia + BM fibrosis (MF grade 1-3) + MPN driver mutation + exclusion of ET/PV/CML
- Prefibrotic MF (pre-PMF): Early stage before significant fibrosis; megakaryocytic atypia without significant fibrosis; distinguishable from ET by BM findings

## Structure

### Molecular drivers of MPN

**JAK2 V617F (Val617→Phe in exon 14):**
Located in the pseudokinase domain (JH2) of JAK2 → abolishes JH2 autoinhibitory constraint on JH1 (active kinase domain) → constitutive JAK2 activity → autonomous STAT5/STAT3/PI3K/ERK activation independent of EPO/TPO/G-CSF binding. Allele burden correlates with MPN phenotype: heterozygous V617F (lower burden) → ET; homozygous V617F (uniparental disomy 9p, higher burden) → PV.

**JAK2 exon 12 mutations:**
Insertion/deletion mutations in exon 12 (in-frame); found in ~3% of PV (JAK2 V617F-negative); cause EPO-independent erythrocytosis specifically (less thrombocytosis/leukocytosis than V617F); STAT5 activation primarily erythroid-biased.

**CALR mutations (exon 9 frameshift):**
- Type I CALR: 52-bp deletion → generates novel C-terminus; activates MPL → TPO-independent megakaryopoiesis; ET and MF
- Type II CALR: 5-bp insertion; less potent MPL activation; predominantly ET
- CALR-mutant CALR protein binds and activates MPL via novel C-terminus; activates JAK2 downstream → STAT5; CALR-mutant ET: lower thrombosis risk than JAK2 V617F ET; CALR type I more associated with MF transformation

**MPL W515L/K (exon 10 mutations):**
Activating mutations in the thrombopoietin receptor (MPL); ~5% of JAK2/CALR-negative ET/MF; constitutive MPL → JAK2 → STAT5 activation; megakaryocyte-dominant phenotype.

**Co-mutations (MF prognosis):**
- ASXL1 mutations: ~25-35% of MF; poor prognosis; chromatin remodeling
- EZH2 mutations: ~5-10%; worst prognosis group with ASXL1 and IDH1/2
- IDH1/2: ~5%; associated with blast transformation
- SRSF2: Splicing factor; ~10%; poor prognosis
- TP53: ~5-10% of blast-phase MF; leukemic transformation
- U2AF1: Splicing factor; ~15%; clinical trials targeting splicing

**MIPSS70+ v2.0 (Mutation-enhanced International Prognostic Scoring System for MF):**
Integrates JAK2/CALR/MPL mutation status, co-mutations (ASXL1, EZH2, IDH1/2, SRSF2, U2AF1), karyotype, hemoglobin, platelets, leukocytes, symptoms, and age → stratifies MF into very low/low/intermediate/high/very high risk; informs alloSCT timing.

### MPN disease biology

**PV pathophysiology:**
JAK2 V617F → constitutive EPOR-JAK2-STAT5 signaling → erythroid progenitor expansion → absolute erythrocytosis (elevated Hgb/HCT) → increased blood viscosity → venous and arterial thrombosis (Budd-Chiari syndrome, CVA, MI, DVT/PE are leading causes of morbidity). EPO levels suppressed (EPO-independent erythropoiesis). Aquagenic pruritus (JAK2 → mast cell degranulation after water contact) characteristic.

**ET pathophysiology:**
Platelet hyperproduction → thrombocytosis (>450 × 10⁹/L) → paradoxical thrombosis (smaller platelets, acquired vWF deficiency at very high platelet counts >1500 × 10⁹/L → bleeding) and clot formation; large platelets; megakaryocytic hyperplasia in BM with stag-horn megakaryocytes.

**MF pathophysiology:**
Abnormal megakaryocytes → TGF-β1/PDGF secretion → fibroblast activation → collagen deposition → BM fibrosis → hematopoietic failure → extramedullary hematopoiesis in spleen/liver → massive splenomegaly → early satiety, weight loss, cachexia; cytopenia (anemia, thrombocytopenia); constitutional symptoms (night sweats, fatigue, pruritus).

## Function

### Normal megakaryocyte-platelet biology

**Thrombopoiesis:**
TPO (hepatic) → MPL on megakaryocyte precursors → JAK2 → STAT5 → megakaryocyte differentiation and endomitosis (polyploidization up to 128N) → proplatelet formation → platelet release into blood (~150,000-400,000 platelets/μL). Platelets are anucleate cytoplasmic fragments; lifespan ~7-10 days.

**Megakaryocyte niche:**
Megakaryocytes reside in the BM sinusoidal niche; proplatelet extensions penetrate sinusoidal endothelium → platelets released into blood. In MF, abnormal megakaryocytes secrete TGF-β1, PDGF → fibroblast activation → progressive marrow fibrosis.

### Leukocytosis and thrombotic risk

In PV and ET, JAK2 V617F also affects myeloid progenitors → granulocytosis and monocytosis. Leukocytosis (WBC >11 × 10⁹/L) is an independent thrombosis risk factor in PV, independent of HCT. JAK2 V617F-positive leukocytes have enhanced PI3K/AKT/NF-κB activity → pro-inflammatory/pro-thrombotic microenvironment.

## Pathology

### Diagnostic criteria and workup

**PV (WHO 2022 major/minor):**
- Major: (1) Hemoglobin >16.5 g/dL (M) / >16 g/dL (F) or HCT >49%/48%; (2) BM hypercellularity (panmyelosis) with megakaryocytic proliferation; (3) JAK2 V617F or JAK2 exon 12 mutation
- Minor: EPO below normal reference range
- PV diagnosis: All 3 major or 2 major + minor

**ET (WHO 2022 major):**
1. Platelet count >450 × 10⁹/L
2. BM: Megakaryocytic proliferation, mature large megakaryocytes with hyperlobated nuclei; no significant granulocyte or erythroid proliferation; no/minimal reticulin fibrosis
3. Criteria for PV, PMF, BCR-ABL1+ CML, MDS not met
4. Presence of JAK2 V617F, CALR exon 9, or MPL exon 10 mutation OR another clonal marker (or no reactive thrombocytosis)

**MF grading (WHO fibrosis grade):**
- MF-0: No reticulin fibrosis
- MF-1: Loose reticulin network; no collagen
- MF-2: Diffuse dense reticulin + collagen (confirmed by trichrome stain); no osteosclerosis
- MF-3: Dense reticulin + coarse collagen ± osteosclerosis

**Staging workup:**
- CBC with differential, reticulocyte count, LDH, uric acid, ferritin, EPO level
- Peripheral blood smear: Teardrop cells (dacrocytes) in MF; giant platelets in ET; immature myeloids (leukoerythroblastic pattern) in MF
- Bone marrow biopsy + aspirate: Morphology, reticulin/trichrome staining for fibrosis grade; cytogenetics
- Molecular: JAK2 V617F (allele-specific PCR or NGS); if negative → CALR exon 9, MPL exon 10; next-generation sequencing panel (ASXL1, IDH1/2, EZH2, SRSF2, TP53) for MF risk stratification
- Abdominal imaging (ultrasound/CT): Spleen and liver size; extramedullary hematopoiesis

### Treatment

**PV management:**
- **All patients:** Phlebotomy (target HCT <45%; CYTO-PV: HCT <45% vs. 45-50% → 4× lower cardiovascular events); low-dose aspirin (100 mg/day) for thrombosis prophylaxis
- **Low-risk (age <60, no thrombosis history):** Phlebotomy + aspirin; observe
- **High-risk (age ≥60 or prior thrombosis):** Cytoreduction with hydroxyurea (HU) first-line; interferon-α (pegylated: ropeginterferon alfa-2b — Besremi; disease-modifying, can induce molecular remission)
- **HU-resistant/intolerant:** Ruxolitinib (RESPONSE trial) [^vannucchi-2015-response]: HCT control + spleen reduction vs. standard; FDA approved 2014; ropeginterferon alfa-2b as alternative

**ET management:**
- **Risk stratification (IPSET-thrombosis revised):**
  - Low risk: Age <60, no thrombosis history, JAK2 V617F positive
  - Very low risk: Age <60, no thrombosis, JAK2 V617F negative
  - Intermediate risk: Age ≥60, no thrombosis history, JAK2 V617F negative
  - High risk: Age ≥60 or prior thrombosis (any JAK2 status)
- **Very low/low risk:** Observation or low-dose aspirin
- **Intermediate risk:** May observe or add aspirin; cytoreduction if symptomatic
- **High risk:** Cytoreduction with hydroxyurea first-line; anagrelide (platelet-selective) as alternative; interferon-α for young/fertile patients; ruxolitinib for HU-resistant/intolerant

**Myelofibrosis management:**

**Symptom-directed therapy:**
- **Ruxolitinib (COMFORT-I, COMFORT-II):** [^verstovsek-2012-comfort-i] Spleen volume reduction ≥35% at 24 weeks in ~41% vs. 0% placebo; OS benefit at 3 years; FDA approved 2011; starting dose based on platelet count (200 × 10⁹/L: 20 mg BID; 100-200 × 10⁹/L: 15 mg BID; 50-100 × 10⁹/L: 5 mg BID)
- **Fedratinib (JAKARTA trial):** FDA approved 2019; option for ruxolitinib-refractory/intolerant MF; caution for thiamine deficiency
- **Pacritinib (PERSIST-2, PAC203):** FDA approved 2022 for MF with platelets <50 × 10⁹/L; spares JAK1 → less cytopenia; option for severely thrombocytopenic MF
- **Momelotinib (MOMENTUM trial):** FDA approved 2023; superior transfusion independence vs. danazol; ACVR1 inhibition → reduced hepcidin → improves anemia

**Anemia-directed therapy:**
- Luspatercept (INDEPENDENCE trial): Activin receptor ligand trap → reduces SMAD2/3 signaling → improves erythroid maturation; approved for MF-associated anemia on ruxolitinib
- Danazol: Androgen; modest benefit for anemia in MF
- Erythropoiesis-stimulating agents (ESA): Limited utility in MF (EPO often elevated)
- Transfusion support for severe anemia

**Curative therapy (alloSCT):**
- Only curative approach for MF; indicated for intermediate-2 or high-risk disease (DIPSS-plus ≥4) in eligible patients
- Reduced-intensity conditioning (RIC) allows older patients to proceed; 5-year OS ~50% in DIPSS-plus intermediate-2/high risk
- Ruxolitinib pre-transplant → reduce spleen size → better engraftment; ruxolitinib tapering post-transplant under investigation

**Blast-phase MPN (AML transformation):**
- Standard induction chemotherapy (7+3) + venetoclax in eligible patients; IDH1/2 inhibitors for IDH-mutated cases; high allografting priority

## Connections

- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Ruxolitinib (JAK1/2 inhibitor, COMFORT-I/II) reduces spleen volume >35% in ~40% of MF patients and prolongs OS; ruxolitinib also standard for PV (RESPONSE: reduced HCT and spleen); fedratinib and pacritinib are alternative JAK2 inhibitors for MF with cytopenias.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — JAK2 V617F → constitutive STAT5 phosphorylation → EPO-independent erythropoiesis in PV; STAT5 is the primary effector of JAK2 → BCL-XL, CCND1, MYC → erythroid survival; STAT3 mediates inflammatory cytokine production in MF (IL-6, IL-8).
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — EPO → EPOR → JAK2 → STAT5 is the normal erythropoiesis axis; JAK2 V617F bypasses EPO requirement → autonomous red cell production → polycythemia in PV; serum EPO is suppressed in PV (EPO-independent erythropoiesis) and elevated in secondary polycythemia.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — TGF-β1 secreted by MPN megakaryocytes drives collagen deposition → bone marrow fibrosis in MF; TGF-β/SMAD pathway activation is central to MF fibrosis; luspatercept (activin receptor ligand trap targeting SMAD2/3) approved for MF-associated anemia (INDEPENDENCE trial).
- `connects-to` → **[Polycythemia Vera](../polycythemia-vera/README.md)** — Polycythemia vera is the erythroid-predominant MPN — JAK2 V617F (often homozygous via 9p uniparental disomy) drives EPO-independent erythrocytosis, raising thrombosis risk; managed with phlebotomy to HCT <45% and aspirin, and it can evolve to post-PV myelofibrosis.
- `connects-to` → **[JAK2](../../03-molecular/jak2/README.md)** — The JAK2 V617F mutation in the JH2 pseudokinase domain unifies the MPNs — present in ~95% of PV and ~55-60% of ET and MF — by removing autoinhibition for constitutive JAK-STAT signaling; allele burden tracks phenotype (heterozygous→ET, homozygous→PV).
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — MPNs are clonal stem-cell diseases of the bone marrow: panmyeloid hypercellularity in PV, megakaryocytic hyperplasia in ET, and progressive reticulin/collagen fibrosis (MF-0 to MF-3) in myelofibrosis that drives marrow failure and extramedullary hematopoiesis with splenomegaly.
- `connects-to` → **[Chronic Myelomonocytic Leukemia](../cmml/README.md)** — Chronic myelomonocytic leukemia is the MDS/MPN-overlap cousin of the classic myeloproliferative neoplasms: it shares their JAK2/RAS-driven proliferation, splenomegaly, and JAK-inhibitor responsiveness, but adds the peripheral monocytosis and dysplasia of MDS.
- `connects-to` → **[Myelofibrosis](../myelofibrosis/README.md)** — Myelofibrosis is the most aggressive classic MPN: JAK2/CALR/MPL-driven megakaryocytes secrete TGF-β that scars the marrow with reticulin and collagen, forcing extramedullary hematopoiesis (splenomegaly) and marrow failure; it arises de novo or evolves from PV or ET.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — Splenomegaly is the clinical signature of the myeloproliferative neoplasms, most extreme in myelofibrosis where the spleen takes over blood production (extramedullary hematopoiesis) and can fill the abdomen; JAK inhibitors (ruxolitinib) shrink it, splenectomy a last resort.
- `connects-to` → **[Essential Thrombocythemia](../essential-thrombocythemia/README.md)** — Essential thrombocythemia is one of the three classic BCR-ABL-negative myeloproliferative neoplasms, alongside polycythemia vera and myelofibrosis: a JAK2, CALR, or MPL mutation drives clonal megakaryocyte overproduction and a high platelet count, with thrombosis the main risk.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Platelets are central to MPN morbidity: clonal megakaryocytes overproduce platelets that are also qualitatively abnormal, so essential thrombocythemia and polycythemia vera cause both thrombosis and—at very high counts—bleeding from acquired von Willebrand defects.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Thrombosis is the leading cause of death in myeloproliferative neoplasms: JAK2-mutant blood is prothrombotic, producing arterial and venous clots including splanchnic-vein thromboses (Budd-Chiari, portal vein)—so cytoreduction and aspirin aim to prevent VTE.
- `connects-to` → **[Chronic Myeloid Leukemia](../cml/README.md)** — CML is the classic BCR-ABL-positive myeloproliferative neoplasm, set apart from the JAK2/CALR/MPL-driven 'Philadelphia-negative' MPNs: all overproduce mature myeloid cells, but CML's defining t(9;22) kinase makes it uniquely controllable with imatinib.
- `connects-to` → **[AML](../aml/README.md)** — Myeloproliferative neoplasms can transform into acute myeloid leukemia: chronic clonal proliferation accumulates mutations until differentiation fails and blasts take over—post-MPN AML carries a grim prognosis, the feared endpoint of these diseases.
- `connects-to` → **[Gout](../gout/README.md)** — MPNs commonly cause secondary gout: the high cell turnover floods the blood with purines that break down to uric acid, so hyperuricemia and gout flares accompany polycythemia vera and myelofibrosis—sometimes the first clue to an underlying MPN.
- `connects-to` → **[CALR](../../03-molecular/calr/README.md)** — CALR mutation is a major MPN driver alongside JAK2: in JAK2-negative essential thrombocythemia and myelofibrosis, calreticulin mutations activate the same thrombopoietin-receptor pathway, so CALR testing completes the molecular workup of myeloproliferative neoplasms.
- `connects-to` → **[MPL](../../03-molecular/mpl/README.md)** — MPL, the thrombopoietin receptor, is the third classic MPN driver: activating MPL mutations switch on JAK-STAT signaling in a minority of essential thrombocythemia and myelofibrosis, so JAK2, CALR and MPL together explain most myeloproliferative neoplasms.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Overproduction of red cells defines polycythemia vera within the MPN family: JAK2-driven erythroid expansion thickens the blood and raises clot risk, illustrating how each MPN over-makes one lineage—red cells here, platelets in ET, fibrosis in myelofibrosis.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Myeloproliferative neoplasms overproduce mature myeloid cells including neutrophils: the JAK2/CALR/MPL-driven clone expands granulocytes along with red cells and platelets, so leukocytosis is common and itself contributes to the thrombotic risk that defines MPN morbidity.
- `connects-to` → **[Stroke](../stroke/README.md)** — Thrombosis is the leading complication of myeloproliferative neoplasms: thick, sticky blood from excess cells and an activated, inflammatory clone causes arterial events including stroke, so cytoreduction and antiplatelet therapy aim to prevent these clots.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Myeloproliferative neoplasms classically cause splanchnic vein thrombosis: the prothrombotic clone clots the hepatic or portal veins (Budd-Chiari), so unexplained abdominal-vein thrombosis should prompt JAK2 testing—sometimes the first sign of an occult MPN.
- `connects-to` → **[Thrombopoietin](../../03-molecular/thrombopoietin/README.md)** — MPNs hijack thrombopoietin signaling: CALR and MPL mutations make blood cells respond as if flooded with thrombopoietin even when levels are normal, driving the runaway platelet and megakaryocyte production of essential thrombocythemia and myelofibrosis.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Myelofibrosis is the scarring face of MPNs: clonal megakaryocytes pour out cytokines that drive fibroblasts to lay down marrow fibrosis, choking blood production and forcing the spleen and liver to take over—the hallmark of advanced disease.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Polycythemia vera ties MPNs to iron: overproduction of red cells consumes iron and therapeutic phlebotomy deliberately induces iron deficiency to limit red-cell mass, so iron balance is both a consequence and a lever of treatment.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — Myeloproliferative neoplasms smolder with IL-6 and inflammation: the JAK2-mutant clone pumps out IL-6 and other cytokines that cause fevers, weight loss, and itching and drive progression to fibrosis—why JAK inhibitors relieve symptoms so well.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Immune surveillance by NK cells shapes myeloproliferative neoplasms: natural killer cells help police the mutant clone, and their exhaustion or dysfunction may let the disease expand—an angle for immune-based approaches alongside JAK inhibitors.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — MPN stem cells use autophagy to persist through treatment: the clonal cells recycle their contents to survive stress and JAK inhibition, so blocking autophagy is studied as a way to deepen responses and target the disease at its root.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — High blood counts in MPN can fake high potassium: the huge numbers of platelets and white cells leak potassium after the sample clots, producing pseudohyperkalemia—a lab artifact to recognize before treating a number that isn't real.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — MPNs threaten the brain with clots: thickened, sticky blood from too many cells raises the risk of stroke and cerebral vein thrombosis, so controlling counts and using aspirin aim to protect against these neurologic catastrophes.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Inflammation via NF-kB fuels the myeloproliferative clone: alongside JAK-STAT, the mutated stem cells drive NF-kB signaling that pours out cytokines, feeding the symptoms, marrow fibrosis and clonal expansion of these neoplasms.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — MPNs itch through the skin: aquagenic pruritus—intense itching minutes after a warm shower—is a classic symptom, especially of polycythemia vera, sometimes appearing before the diagnosis.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — MPN itching is driven by mast cells: the expanded clone's basophils and mast cells release histamine, which fires skin itch nerves to cause the aquagenic pruritus that torments these patients.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Polycythemia overrides the body's oxygen control: normally low oxygen raises erythropoietin to make red cells, but the JAK2 clone churns them out regardless, thickening the blood independent of oxygen need.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Radioactive phosphorus once tamed these clones with electrons: P-32 concentrates in marrow and emits beta particles — fast electrons — that suppress the overactive blood-cell factory, a historic polycythemia treatment now reserved for select older patients.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Myeloproliferative disease can choke the lungs: extramedullary hematopoiesis and microvascular thrombosis raise pulmonary pressures, so pulmonary hypertension and clots are recognized complications, especially in myelofibrosis.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — The kidney bears the brunt of high cell turnover: the massive production and breakdown of blood cells floods the blood with uric acid, which crystallizes in the tubules and can drive urate nephropathy and stones.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Myeloproliferative disease clots the arteries too: the thick, sticky blood and activated platelets drive arterial thrombosis, so heart attacks join the strokes and venous clots that menace these patients.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — MPN is a leading cause of unusual-site clots: thrombosis of the splanchnic veins draining the gut — portal, mesenteric, and the hepatic veins of Budd-Chiari — can be the first sign, sometimes before the blood counts even rise.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — The frenzied cell turnover spills phosphorus: the constant birth and death of blood cells, and their lysis under treatment, release phosphate and urate, the metabolic overflow that strains the kidneys and provokes gout.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Thrombosis is the central danger of MPN: the JAK2-mutant, thickened blood plus an activated, sticky endothelial-cell lining drives clots in both arteries and veins, the strokes and heart attacks that are the leading cause of death in these disorders.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — A maddening itch after a warm bath marks polycythemia vera: basophils and mast cells expanded by the MPN clone dump histamine, the aquagenic pruritus that water triggers being one of the disease's most distinctive complaints.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Sludgy blood blurs the vision: the hyperviscosity of a high red-cell or platelet count slows retinal flow, causing visual disturbances and engorged retinal veins, while erythromelalgia's burning can be matched by ocular symptoms in advanced disease.

[^verstovsek-2012-comfort-i]: Verstovsek S, Mesa RA, Gotlib J, et al. A double-blind, placebo-controlled trial of ruxolitinib for myelofibrosis. *N Engl J Med.* 2012;366(9):799-807. [doi:10.1056/NEJMoa1110557](https://doi.org/10.1056/NEJMoa1110557) · [PubMed 22375971](https://pubmed.ncbi.nlm.nih.gov/22375971/)
[^vannucchi-2015-response]: Vannucchi AM, Kiladjian JJ, Griesshammer M, et al. Ruxolitinib versus standard therapy for the treatment of polycythemia vera. *N Engl J Med.* 2015;372(5):426-435. [doi:10.1056/NEJMoa1409002](https://doi.org/10.1056/NEJMoa1409002) · [PubMed 25426978](https://pubmed.ncbi.nlm.nih.gov/25426978/)
