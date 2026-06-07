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

[^verstovsek-2012-comfort-i]: Verstovsek S, Mesa RA, Gotlib J, et al. A double-blind, placebo-controlled trial of ruxolitinib for myelofibrosis. *N Engl J Med.* 2012;366(9):799-807. [doi:10.1056/NEJMoa1110557](https://doi.org/10.1056/NEJMoa1110557) · [PubMed 22375971](https://pubmed.ncbi.nlm.nih.gov/22375971/)
[^vannucchi-2015-response]: Vannucchi AM, Kiladjian JJ, Griesshammer M, et al. Ruxolitinib versus standard therapy for the treatment of polycythemia vera. *N Engl J Med.* 2015;372(5):426-435. [doi:10.1056/NEJMoa1409002](https://doi.org/10.1056/NEJMoa1409002) · [PubMed 25426978](https://pubmed.ncbi.nlm.nih.gov/25426978/)
