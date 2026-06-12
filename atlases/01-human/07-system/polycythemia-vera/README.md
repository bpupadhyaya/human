---
schema: human-scale-entry/v1
id: polycythemia-vera
name: Polycythemia Vera
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Polycythemia vera is a JAK2-driven MPN with erythrocytosis, thrombocytosis, and leukocytosis; JAK2 V617F ~99%; phlebotomy + low-dose aspirin for all; hydroxyurea or ropeginterferon alfa-2b for high-risk; ruxolitinib for HU-resistant; MF/AML transformation risk."
aliases: ["polycythemia vera", "PV", "polycythaemia vera", "primary polycythemia", "JAK2 V617F polycythemia", "polycythemia rubra vera"]
sources:
  - id: vannucchi-2015-response
    type: peer-reviewed
    cite: "Vannucchi AM, Kiladjian JJ, Griesshammer M, et al. Ruxolitinib versus standard therapy for the treatment of polycythemia vera. N Engl J Med. 2015;372(5):426-435."
    doi: "10.1056/NEJMoa1409630"
    pmid: "25577388"
    url: "https://doi.org/10.1056/NEJMoa1409630"
  - id: gisslinger-2020-proud-pv
    type: peer-reviewed
    cite: "Gisslinger H, Gotic M, Holowiecki J, et al. Ropeginterferon alfa-2b versus standard therapy for polycythaemia vera (PROUD-PV and CONTINUATION-PV): a randomised, non-inferiority, phase 3 trial and its extension study. Lancet Haematol. 2020;7(3):e196-e208."
    doi: "10.1016/S2352-3026(19)30236-4"
    pmid: "32046833"
    url: "https://doi.org/10.1016/S2352-3026(19)30236-4"
cross_links:
  - target: 01-human/03-molecular/epas1
    relation: connects-to
    note: "HIF-2α (EPAS1) drives EPO transcription; VHL loss or EPAS1 GOF mutations → secondary/hereditary erythrocytosis; PHD2/EGLN1 mutations stabilize HIF-2α; PV distinguished from secondary erythrocytosis by low serum EPO + JAK2 V617F mutation."
  - target: 01-human/03-molecular/jak2
    relation: connects-to
    note: "JAK2 V617F is present in ~99% PV; GOF in JH2 pseudokinase domain → constitutive JAK2/STAT5 → EPO-independent erythroid proliferation; ruxolitinib (RESPONSE: Hct control 21% vs 1%) FDA-approved for HU-resistant/intolerant PV."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Serum EPO is suppressed in PV (WHO minor criterion) due to constitutive JAK2 erythropoiesis; secondary erythrocytosis (hypoxia, VHL mutation) shows elevated EPO; EPO level distinguishes primary from secondary polycythemia; ropeginterferon reduces EPO-driven clonal expansion."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "PV transforms to post-PV myelofibrosis (~10-15% at 10 years); megakaryocyte-derived TGF-β1 → collagen deposition → reticulin/collagen fibrosis; momelotinib and luspatercept address TGF-β-driven anemia in post-PV MF."
  - target: 01-human/07-system/myeloproliferative-neoplasms
    relation: connects-to
    note: "Polycythemia vera is the erythroid-dominant member of the BCR-ABL-negative myeloproliferative neoplasms (with ET and myelofibrosis), nearly always JAK2-driven (~99% V617F); it shares their thrombosis risk and capacity to evolve into post-PV myelofibrosis or AML."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "JAK2 V617F makes erythroid progenitors expand without EPO (endogenous erythroid colonies), raising red-cell mass and blood viscosity → arterial and venous thrombosis; phlebotomy to hematocrit <45% cuts cardiovascular events ~45% (CYTO-PV) by lowering that viscosity."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "Splenomegaly affects ~70% of PV from extramedullary hematopoiesis, causing early satiety and, when massive, infarction risk; it worsens as disease evolves toward post-PV myelofibrosis, and the JAK1/2 inhibitor ruxolitinib reduces spleen volume in HU-resistant patients."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Thrombosis is the leading cause of death in polycythemia vera, arterial events dominating: raised red-cell mass, JAK2 hyperviscosity, and activated platelets cause stroke, MI, and Budd-Chiari/splanchnic-vein thrombosis; phlebotomy to hematocrit <45% and aspirin cut these events."
  - target: 01-human/07-system/essential-thrombocythemia
    relation: connects-to
    note: "Polycythemia vera and essential thrombocythemia are sibling JAK2-driven myeloproliferative neoplasms on a continuum: PV expands the erythroid lineage (high hematocrit) and ET the megakaryocytic (high platelets), but both carry thrombosis risk and can evolve to myelofibrosis."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Polycythemia vera is a clonal bone marrow stem-cell disease: a JAK2 V617F-mutant hematopoietic stem cell produces panmyelosis — hypercellular marrow with trilineage (especially erythroid) proliferation — and a low EPO; over years the marrow can scar into post-PV myelofibrosis."
---

# Polycythemia Vera

## Overview

**Polycythemia vera (PV)** is a BCR-ABL1-negative **myeloproliferative neoplasm (MPN)** characterized by clonal expansion of a hematopoietic stem cell driven by **JAK2 gain-of-function mutations** in virtually all cases (~99% JAK2 V617F; ~1% JAK2 exon 12 mutations). PV presents with absolute erythrocytosis (elevated red cell mass), variable thrombocytosis and leukocytosis, splenomegaly, and the pathognomonic symptom of **aquagenic pruritus**. The principal clinical risks are thrombosis (arterial and venous), bleeding, and long-term transformation to post-PV myelofibrosis (PPV-MF, ~10-15% at 10 years) or acute myeloid leukemia (AML, ~2-5% at 10 years). Treatment is risk-stratified: all patients receive phlebotomy (target Hematocrit <45%) and low-dose aspirin; high-risk patients (age ≥60 or prior thrombosis) additionally receive cytoreductive therapy with **hydroxyurea** (first-line) or **ropeginterferon alfa-2b** (Besremi, FDA approved 2021) — PROUD-PV/CONTINUATION-PV showed superior molecular response for ropeginterferon at 36 months [^gisslinger-2020-proud-pv]. **Ruxolitinib** (JAK1/2 inhibitor, Jakafi) is approved for hydroxyurea-resistant/intolerant PV — RESPONSE trial: Hct control 21% vs 1%, spleen volume reduction ≥35% 38% vs 1% [^vannucchi-2015-response].

**Epidemiology:**
- Incidence: ~2-3 per 100,000/year; prevalence ~22 per 100,000
- Median age at diagnosis: ~60 years; rare in patients <40 years
- Male predominance (male:female ~2:1)
- Median overall survival: 14-19 years from diagnosis with modern treatment; shortened by thrombotic events and transformation

## Structure

### WHO 2022 diagnostic criteria

**Major criteria:**
1. Hemoglobin >16.5 g/dL (men) or >16.0 g/dL (women), OR Hematocrit >49% (men) or >48% (women), OR elevated red cell mass (>25% above predicted)
2. Bone marrow biopsy: hypercellularity for age with trilineage growth (panmyelosis) — prominent erythroid, granulocytic, and megakaryocytic proliferation; megakaryocytes are pleomorphic (large and small, hyperlobated and hypolobated nuclei)
3. Presence of JAK2 V617F or JAK2 exon 12 mutation

**Minor criterion:**
4. Subnormal serum erythropoietin level (EPO below normal reference range)

**Diagnosis:** All three major criteria, OR first two major + minor criterion.

*Note: Bone marrow biopsy is required except if Hgb >18.5 g/dL (men)/16.5 g/dL (women) with JAK2 mutation and subnormal EPO.*

### Molecular landscape

**JAK2 V617F (Val617Phe, ~98-99%):**
Exon 14 point mutation in the JH2 pseudokinase (regulatory) domain; normally JH2 auto-inhibits JH1 kinase; V617F disrupts JH2 auto-inhibition → constitutive JAK2 kinase activity → STAT5/STAT3 phosphorylation → proliferative and anti-apoptotic gene programs → erythroid, megakaryocytic, and granulocytic expansion independent of cytokine ligands. Homozygous JAK2 V617F (~25% of PV cases, via mitotic recombination) correlates with higher allele burden, more erythrocytosis, more frequent aquagenic pruritus, and higher MF transformation risk.

**JAK2 exon 12 mutations (~1-2%):**
In-frame deletions/insertions in exon 12 of JAK2 → isolated erythrocytosis (predominantly erythroid phenotype, unlike V617F which causes panhyperplasia); subnormal EPO; JAK2 V617F negative; require exon 12 sequencing; clinically similar prognosis to JAK2 V617F PV.

**Co-mutations:**
Additional somatic mutations in ~30-50% PV at diagnosis: TET2 (most common, ~16%), DNMT3A (~7%), ASXL1 (~5%), SRSF2 (~4%), IDH2 (<5%); ASXL1/SRSF2/IDH1/2/EZH2 co-mutations → increased MF and AML transformation risk; molecular profiling (NGS) increasingly used to assess transformation risk.

**JAK2 allele burden (VAF):**
JAK2 V617F variant allele frequency (VAF): PV typically VAF 25-100% (compared to ET typically VAF 1-50%); higher allele burden in PV → more symptomatic disease; cytoreductive therapy (interferon, ruxolitinib) lowers VAF; complete molecular response (CMR, VAF <1%) achievable with sustained ropeginterferon therapy; CMR correlates with reduced clonal burden and possibly reduced transformation risk.

## Function

### JAK2-driven pathophysiology

**EPO-independent erythropoiesis:**
JAK2 V617F → constitutive EPOR/JAK2/STAT5 signaling → erythroid progenitors (BFU-E, CFU-E) proliferate without EPO → endogenous erythroid colony (EEC) formation in semi-solid media without added EPO — a diagnostic functional assay. Elevated red cell mass → increased blood viscosity → sludging → thrombosis risk; phlebotomy reduces Hct to target <45% → reduces thrombotic risk by ~45% (CYTO-PV trial).

**Thromboembolic risk:**
Both arterial (MI, stroke) and venous (DVT, PE, splanchnic vein thrombosis — Budd-Chiari, portal vein) events occur at high rates. JAK2 V617F platelets are activated; JAK2 V617F neutrophils release NETs (neutrophil extracellular traps) → endothelial activation → thrombosis. Splanchnic vein thrombosis (Budd-Chiari syndrome, portal vein thrombosis) in young women → screen for JAK2 V617F as PV may be the underlying diagnosis. Low-dose aspirin (100 mg/day) reduces thrombosis risk in PV (ECLAP trial: RR 0.41, p=0.02).

**Aquagenic pruritus:**
~40-65% of PV patients; generalized pruritus triggered by water contact (bathing, shower) regardless of temperature; pathophysiology: JAK2 V617F → mast cell JAK2 activation → histamine release + prostaglandin production → cutaneous pruritic stimuli; treatment: antihistamines (limited efficacy), aspirin, SSRIs (paroxetine effective), JAK inhibitors (ruxolitinib highly effective for pruritus).

**Splenomegaly:**
~70% at diagnosis; caused by extramedullary hematopoiesis; correlates with disease burden; ruxolitinib reduces spleen volume; symptomatic splenomegaly → early satiety, pain; massive splenomegaly → concerns for splenic infarct or rupture.

## Pathology

### Risk stratification

**Low-risk PV:** Age <60 years AND no prior thrombosis
- Treatment: Phlebotomy (Hct <45%) + low-dose aspirin 81-100 mg/day

**High-risk PV:** Age ≥60 years OR prior thrombosis (either arterial or venous)
- Treatment: Phlebotomy + aspirin + cytoreductive therapy

**Very high-risk features (no formal WHO category):** Extreme leukocytosis (WBC >15 × 10⁹/L), extreme thrombocytosis (platelet >1,500 × 10⁹/L — paradoxically ↑ bleeding from acquired von Willebrand syndrome), prior major bleeding; consider cytoreduction in low-risk patients with these features.

### Treatment

**Phlebotomy:**
Target Hct <45% in all patients (CYTO-PV: Hct <45% → 38% reduction in cardiovascular death/major thrombosis vs <50%); 1 unit (~450 mL) removed per session; iron deficiency induced by phlebotomy is intentional and not supplemented (limits erythropoiesis); frequency: initially weekly, then as needed to maintain Hct <45%; iron-deficiency symptoms may require iron supplementation titration.

**Low-dose aspirin:**
81-100 mg/day in all PV patients without contraindications; reduces major thrombosis (arterial events especially); caution at very high platelet counts (>1,500 × 10⁹/L) due to acquired von Willebrand syndrome → risk of bleeding; discontinue or adjust dose if platelet count >1,500 × 10⁹/L.

**Hydroxyurea (first-line cytoreduction):**
Ribonucleotide reductase inhibitor → reduces all cell lines; Hct control within weeks; dose: 500-2,000 mg/day orally; monitoring: CBC every 3-4 months; resistance criteria (ELN 2009): need phlebotomy despite ≥2 g/day HU; platelet >400 × 10⁹/L or WBC >10 × 10⁹/L at ≥2 g/day; toxicities: myelosuppression, skin ulcers (particularly leg ulcers), oral mucositis; long-term: HU slightly increases AML risk in some series (confounded by disease progression).

**Ropeginterferon alfa-2b (Besremi, FDA approved 2021):**
Mono-PEGylated IFN-α2b administered every 2 weeks subcutaneously; mechanism: suppresses JAK2-mutant clone via STAT1/2 upregulation → anti-proliferative → preferential elimination of JAK2 V617F HSCs; PROUD-PV (Phase 3, non-inferiority vs HU): similar control arm response at 12 months (non-inferior), superior molecular response (JAK2 allele burden reduction ≥50%: 61% vs 21% at 36 months in CONTINUATION-PV extension) [^gisslinger-2020-proud-pv]; PROUD-PV-2 randomized vs HU in low-risk PV (less common use); adverse effects: flu-like symptoms, fatigue, autoimmune thyroiditis, depression, neuropsychiatric effects; suitable for women of childbearing potential (preferred over HU in pregnancy considerations); achieves CMR (JAK2 VAF <1%) in ~15-20% with sustained therapy.

**Ruxolitinib (Jakafi, FDA approved 2014 for HU-resistant/intolerant PV):**
JAK1/JAK2 inhibitor; RESPONSE trial (Phase 3, N=222): ruxolitinib vs best available therapy (BAT); primary endpoint: Hct control without phlebotomy at week 32 + spleen volume reduction ≥35% → 21% vs 1% (p<0.001); secondary: Hct control 60% vs 20%; pruritus resolution ~51% vs ~5%; complete hematologic response 24% vs 9% [^vannucchi-2015-response]; dose: 10 mg BID (starting); adverse effects: anemia, thrombocytopenia, weight gain, herpes zoster reactivation (prophylaxis with valacyclovir), increased infection risk; does NOT achieve molecular remission as effectively as interferon; approved for HU-resistant/intolerant PV.

**Busulfan (third-line):**
Alkylating agent; used for elderly HU-intolerant patients; short courses (0.1 mg/kg/day × weeks) achieve prolonged remission; myelosuppressive; mutagenic potential limits use.

**Investigational agents:**
- Ropeginterferon combinations with ruxolitinib: Phase 2 trials
- Rusfertide (PTG-300, hepcidin mimetic): Phase 2/3 — reduces phlebotomy frequency by raising serum iron threshold; normalizes iron without phlebotomy burden
- Navitoclax (BCL-2/BCL-XL inhibitor): Phase 2 in combination with ruxolitinib
- Idasanutlin (MDM2 inhibitor): Phase 2 for MDM2-expressing PV

### MF/AML transformation

**Post-PV myelofibrosis (PPV-MF):**
~10-15% at 10 years; ~20-25% at 15 years; defined by WHO criteria: development of reticulin/collagen fibrosis + anemia requiring transfusion or cytoreduction discontinuation + splenomegaly + leukoerythroblastic blood film; treatment: ruxolitinib (most effective), fedratinib, pacritinib; allo-SCT is the only curative option for eligible patients; median OS after PPV-MF ~4-5 years.

**AML transformation:**
~2-5% at 10 years; higher risk with ASXL1/SRSF2/EZH2/IDH1-2 co-mutations; cytogenetic abnormalities frequent at transformation (del17p, +8, +9, complex); PV-associated AML is highly chemotherapy-resistant (>80% fail to achieve CR); allo-SCT after achieving blast control with azacitidine+venetoclax if eligible; prognosis poor (median OS <12 months).

**Monitoring:**
- CBC every 3-6 months; JAK2 VAF annually (molecular monitoring)
- BM biopsy if peripheral blood suggests MF (leukoerythroblastic picture, rising LDH, new splenomegaly, cytopenia)
- NGS panel at diagnosis; repeat at transformation
- Screen for VTE, cardiovascular events at each visit

### Secondary polycythemia — differential diagnosis

PV must be distinguished from secondary erythrocytosis (elevated EPO, JAK2 wild-type):
- **Hypoxia-driven:** Sleep apnea, COPD, cyanotic heart disease, high-altitude residence → elevated EPO → erythrocytosis
- **EPO-producing tumors:** RCC, HCC, uterine fibroid, cerebellar hemangioblastoma → elevated EPO
- **VHL disease/Chuvash polycythemia:** EPAS1 or VHL mutations → HIF-2α constitutive → EPO excess → erythrocytosis with low-normal EPO (partial VHL function loss allows some degradation)
- **EPAS1 GOF/PHD2 mutations:** Hereditary erythrocytosis; subnormal EPO, JAK2 negative, family history
- **Relative (spurious) polycythemia:** Dehydration, diuretics → plasma volume contraction → hemoconcentration; red cell mass normal; EPO normal/low

## Connections

- `connects-to` → **[EPAS1](../../03-molecular/epas1/README.md)** — HIF-2α (EPAS1) drives EPO transcription; VHL loss or EPAS1 GOF mutations → secondary/hereditary erythrocytosis; PHD2/EGLN1 mutations stabilize HIF-2α; PV distinguished from secondary erythrocytosis by low serum EPO + JAK2 V617F mutation.
- `connects-to` → **[JAK2](../../03-molecular/jak2/README.md)** — JAK2 V617F is present in ~99% PV; GOF in JH2 pseudokinase domain → constitutive JAK2/STAT5 → EPO-independent erythroid proliferation; ruxolitinib (RESPONSE: Hct control 21% vs 1%) FDA-approved for HU-resistant/intolerant PV.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Serum EPO is suppressed in PV (WHO minor criterion) due to constitutive JAK2 erythropoiesis; secondary erythrocytosis (hypoxia, VHL mutation) shows elevated EPO; EPO level distinguishes primary from secondary polycythemia; ropeginterferon reduces EPO-driven clonal expansion.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — PV transforms to post-PV myelofibrosis (~10-15% at 10 years); megakaryocyte-derived TGF-β1 → collagen deposition → reticulin/collagen fibrosis; momelotinib and luspatercept address TGF-β-driven anemia in post-PV MF.
- `connects-to` → **[Myeloproliferative Neoplasms](../myeloproliferative-neoplasms/README.md)** — Polycythemia vera is the erythroid-dominant member of the BCR-ABL-negative myeloproliferative neoplasms (with ET and myelofibrosis), nearly always JAK2-driven (~99% V617F); it shares their thrombosis risk and capacity to evolve into post-PV myelofibrosis or AML.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — JAK2 V617F makes erythroid progenitors expand without EPO (endogenous erythroid colonies), raising red-cell mass and blood viscosity → arterial and venous thrombosis; phlebotomy to hematocrit <45% cuts cardiovascular events ~45% (CYTO-PV) by lowering that viscosity.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — Splenomegaly affects ~70% of PV from extramedullary hematopoiesis, causing early satiety and, when massive, infarction risk; it worsens as disease evolves toward post-PV myelofibrosis, and the JAK1/2 inhibitor ruxolitinib reduces spleen volume in HU-resistant patients.
- `connects-to` → **[Stroke](../stroke/README.md)** — Thrombosis is the leading cause of death in polycythemia vera, arterial events dominating: raised red-cell mass, JAK2 hyperviscosity, and activated platelets cause stroke, MI, and Budd-Chiari/splanchnic-vein thrombosis; phlebotomy to hematocrit <45% and aspirin cut these events.
- `connects-to` → **[Essential Thrombocythemia](../essential-thrombocythemia/README.md)** — Polycythemia vera and essential thrombocythemia are sibling JAK2-driven myeloproliferative neoplasms on a continuum: PV expands the erythroid lineage (high hematocrit) and ET the megakaryocytic (high platelets), but both carry thrombosis risk and can evolve to myelofibrosis.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Polycythemia vera is a clonal bone marrow stem-cell disease: a JAK2 V617F-mutant hematopoietic stem cell produces panmyelosis — hypercellular marrow with trilineage (especially erythroid) proliferation — and a low EPO; over years the marrow can scar into post-PV myelofibrosis.

[^vannucchi-2015-response]: Vannucchi AM, Kiladjian JJ, Griesshammer M, et al. Ruxolitinib versus standard therapy for the treatment of polycythemia vera. *N Engl J Med.* 2015;372(5):426-435. [doi:10.1056/NEJMoa1409630](https://doi.org/10.1056/NEJMoa1409630) · [PubMed 25577388](https://pubmed.ncbi.nlm.nih.gov/25577388/)
[^gisslinger-2020-proud-pv]: Gisslinger H, Gotic M, Holowiecki J, et al. Ropeginterferon alfa-2b versus standard therapy for polycythaemia vera (PROUD-PV and CONTINUATION-PV): a randomised, non-inferiority, phase 3 trial and its extension study. *Lancet Haematol.* 2020;7(3):e196-e208. [doi:10.1016/S2352-3026(19)30236-4](https://doi.org/10.1016/S2352-3026(19)30236-4) · [PubMed 32046833](https://pubmed.ncbi.nlm.nih.gov/32046833/)
