---
schema: human-scale-entry/v1
id: type-1-diabetes
name: Type 1 Diabetes
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Autoimmune destruction of pancreatic beta cells → absolute insulin deficiency; CD8+ and CD4+ Th1 cells target GAD65, IA-2, and insulin antigens. Staged by autoantibody seropositivity; teplizumab (anti-CD3) delays clinical onset; managed with insulin replacement."
aliases: ["T1D", "type 1 diabetes mellitus", "T1DM", "juvenile diabetes", "insulin-dependent diabetes mellitus", "IDDM", "autoimmune diabetes"]
sources:
  - id: atkinson-2014-t1d-lancet
    type: peer-reviewed
    cite: "Atkinson MA, Eisenbarth GS, Michels AW. Type 1 diabetes. Lancet. 2014;383(9911):69-82."
    doi: "10.1016/S0140-6736(13)60591-7"
    pmid: "23890997"
    url: "https://doi.org/10.1016/S0140-6736(13)60591-7"
  - id: herold-2019-teplizumab-t1d
    type: peer-reviewed
    cite: "Herold KC, Bundy BN, Long SA, et al. An anti-CD3 antibody, teplizumab, in relatives at risk for type 1 diabetes. N Engl J Med. 2019;381(7):603-613."
    doi: "10.1056/NEJMoa1905155"
    pmid: "31180675"
    url: "https://doi.org/10.1056/NEJMoa1905155"
  - id: insel-2015-t1d-staging
    type: peer-reviewed
    cite: "Insel RA, Dunne JL, Atkinson MA, et al. Staging presymptomatic type 1 diabetes: a scientific statement of JDRF, the Endocrine Society, and the American Diabetes Association. Diabetes Care. 2015;38(10):1964-1974."
    doi: "10.2337/dc15-1419"
    pmid: "26404926"
    url: "https://doi.org/10.2337/dc15-1419"
cross_links:
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "CD8+ CTLs are the primary beta cell destroyers in T1D: autoreactive CTLs recognize HLA-A2-restricted GAD65, IGRP, and insulin peptides → perforin/granzyme and Fas-FasL → beta cell apoptosis; islet CTL infiltration (insulitis) precedes clinical T1D onset by years."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4+ Th1 cells coordinate T1D autoimmunity: HLA-DQ8/DQ2-restricted presentation of beta cell antigens → IFN-gamma, IL-2 → CTL priming and macrophage activation; Treg insufficiency allows unchecked Th1 expansion; teplizumab (anti-CD3) shifts Th1/Treg balance."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Treg insufficiency is a core T1D mechanism: FOXP3+ Tregs normally suppress autoreactive T cells in pancreatic lymph nodes and islets; NOD mice have Treg functional defects; low-dose IL-2 therapy expands Tregs → ongoing clinical trials to delay T1D progression."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "B cells act as APCs for beta cell antigens and produce autoantibodies (anti-GAD65, anti-IA-2, anti-ZnT8, anti-insulin) used for T1D staging (Stage 1: ≥2 Ab, normoglycemia; Stage 2: ≥2 Ab, dysglycemia); rituximab transiently preserves C-peptide in new-onset T1D."
---

# Type 1 Diabetes

## Overview

**Type 1 diabetes (T1D)** is a **chronic autoimmune disease** in which T lymphocyte-mediated destruction of **insulin-producing pancreatic beta cells** in the islets of Langerhans leads to **absolute insulin deficiency**, requiring lifelong insulin replacement for survival [^atkinson-2014-t1d-lancet]. T1D accounts for ~5-10% of all diabetes (type 2 diabetes accounts for 90-95%) but is the predominant form in children and young adults, with peak incidence at 4-6 years and 10-14 years. The global incidence is rising ~3-4% per year, particularly in young children, with highest rates in Finland, Sardinia, and northern European countries (~60 per 100,000 per year).

**Key distinctions from Type 2 Diabetes:**
| Feature | T1D | T2D |
|---|---|---|
| Pathogenesis | Autoimmune beta cell destruction | Insulin resistance + relative beta cell failure |
| Insulin secretion | Near-zero (absolute deficiency) | Reduced but not absent (especially early) |
| Onset | Classically pediatric/young adult; 40% diagnosed >30 | Adult-onset; increasing in children |
| Body habitus | Any (classically non-obese) | Associated with obesity |
| Autoantibodies | Present (GAD65, IA-2, ZnT8, insulin) | Absent |
| Treatment | Insulin required from diagnosis | Lifestyle → oral agents → injectable/insulin |
| Ketoacidosis | Common at diagnosis; recurrent risk | Uncommon |

**Latent autoimmune diabetes in adults (LADA / Type 1.5):**
- Slowly progressive autoimmune diabetes presenting in adults (often >30 years); initially resembles T2D but GADA (anti-GAD65) positive; C-peptide declines over 1-5 years → insulin-dependence; accounts for ~2-12% of adult-onset diabetes; frequently misdiagnosed as T2D

**DKA (diabetic ketoacidosis) at T1D onset:**
- Absolute insulin deficiency → glucagon-dominant state → hepatic gluconeogenesis, glycogenolysis → hyperglycemia; concurrent lipolysis → FFAs → hepatic beta-oxidation → acetyl-CoA excess → ketone body synthesis (beta-hydroxybutyrate, acetoacetate) → metabolic acidosis; DKA mortality <1% in modern care; hallmark: high anion gap metabolic acidosis + hyperglycemia + ketonemia/ketonuria

## Structure

### Immunopathogenesis — T1D as autoimmune insulitis [^atkinson-2014-t1d-lancet]

**Genetic susceptibility:**
- **HLA (40-50% of T1D heritability):**
  - **HLA-DR3-DQ2 (DQB1*02:01/DQA1*05:01) and HLA-DR4-DQ8 (DQB1*03:02/DQA1*03:01):** Highest risk haplotypes (~10-15× increased T1D risk); DR3-DQ2/DR4-DQ8 heterozygotes have highest risk (~1 in 20 chance by age 15 in relatives); HLA controls antigen presentation of beta cell peptides to T cells
  - **HLA-DR15-DQ6 (DQB1*06:02):** Protective — dominant protection even in DQ8/DQ2 carriers
  - Mechanism: DQ8 molecule fails to efficiently tolerize autoreactive T cells to proinsulin and GAD65 peptides during thymic selection → escape of autoreactive repertoire into periphery
- **Non-HLA genes (50-60% of heritability):**
  - **INS VNTR (insulin gene promoter):** Short VNTR → reduced thymic insulin expression → impaired central tolerance to insulin → autoreactive T cells escape; long VNTR → more thymic insulin → better tolerance
  - **PTPN22 (protein tyrosine phosphatase N22, R620W variant):** Gain-of-function → increased T cell receptor signaling threshold → impaired negative selection; also risk factor for RA, SLE, Graves' disease
  - **IL2RA (CD25):** IL-2 signaling → Treg function; multiple T1D risk variants in IL2RA and IL2 gene regions
  - **CTLA4, PTPN2, IFIH1 (MDA5):** T cell co-stimulation, innate viral sensing → modulate T1D risk

**Environmental triggers:**
- **Enteroviruses (Coxsackievirus B):** Molecular mimicry (CB virus protein 2C shares sequence homology with GAD65); direct beta cell infection (CB virus receptor CAR expressed on beta cells); insulitis observed at CB virus-positive T1D diagnosis; CB virus exposure correlates with T1D incidence in longitudinal studies
- **Gut microbiome:** Reduced microbial diversity and specific dysbiosis patterns precede T1D in high-risk children (TEDDY/DIPP studies); loss of Lactobacillus → impaired SCFAs → impaired Treg differentiation → autoimmunity; germ-free NOD mice develop accelerated T1D
- **Vitamin D deficiency:** Inverse correlation with T1D incidence (northern latitudes, lower UV); vitamin D receptor expressed on Tregs → Treg maintenance; supplementation trials in high-risk children ongoing

**Insulitis (islet lymphocytic infiltrate):**
- Pathologically: CD8+ T cells (dominant), CD4+ T cells, macrophages, B cells infiltrate islets → "insulitis"; occurs years before clinical diagnosis
- CD8+ CTLs recognizing HLA-A2-restricted epitopes of IGRP (islet-specific glucose-6-phosphatase catalytic subunit-related protein), preproinsulin, GAD65, and IA-2 → perforin/granzyme B → beta cell apoptosis
- Progressive beta cell destruction: ~80% of beta cell mass lost before overt hyperglycemia (residual mass maintains near-normal glucose until critical threshold lost)

## Function

### Clinical presentation

**Classic triad at T1D diagnosis (DKA or polyuria/polydipsia):**
- **Polyuria, polydipsia, nocturia:** Hyperglycemia → glycosuria → osmotic diuresis → water loss → polydipsia
- **Weight loss:** Absolute insulin deficiency → catabolic state → muscle wasting, fat lipolysis
- **Fatigue:** Cellular glucose deprivation despite hyperglycemia (glucose cannot enter cells without insulin)
- **DKA (30-40% of new diagnoses):** Vomiting, abdominal pain, Kussmaul respirations (deep rapid breathing → compensating metabolic acidosis), fruity breath (acetone), altered consciousness at severe stage
- **Honeymoon period:** In first months post-diagnosis, residual beta cells recover temporarily (DKA stress resolved, inflammation subsides) → reduced insulin requirements (exogenous insulin suppresses autoimmune beta cell death); lasts weeks to months; eventually immune destruction resumes

**Chronic complications (shared with T2D, accelerated by glucose variability):**
- **Microvascular:** Diabetic retinopathy (leading cause of blindness, working-age adults), nephropathy (leading cause of ESRD in developed countries), neuropathy (peripheral > autonomic)
- **Macrovascular:** Cardiovascular disease accelerated 2-4× vs. age-matched controls; stroke; peripheral arterial disease
- **Hypoglycemia unawareness:** Loss of autonomic warning symptoms (sweating, tremor) from recurrent hypoglycemia → dangerous hypoglycemia risk; impaired hypoglycemia-associated autonomic failure (HAAF)

## Pathology

### Staging and screening [^insel-2015-t1d-staging]

**Three-stage T1D model (JDRF/ADA/Endocrine Society, 2015):**
- **Stage 1:** Multiple positive autoantibodies (≥2), normoglycemia, no symptoms — active autoimmunity, beta cell destruction underway; risk of progression to clinical T1D: ~75% at 10 years
- **Stage 2:** Multiple positive autoantibodies + dysglycemia (impaired fasting glucose or IGT, or HbA1c 5.7-6.4%) — 70-80% progress to clinical T1D within 5 years
- **Stage 3:** Clinical T1D (symptomatic hyperglycemia meeting diabetes diagnostic criteria)

**Autoantibody screening:**
- Autoantibodies: anti-GAD65 (most common, 75-80%), anti-IA-2/ICA512 (60-75%), anti-ZnT8 (60-70%), anti-insulin (most specific in young children <5 years, disappears with insulin therapy)
- Recommended screening in first-degree relatives and general population high-risk individuals (HLA-DR3/DR4); NIDDK Autoimmunity Screening for Kids (ASK) trial; commercial screening programs (TrialNet)

### Treatment

**Insulin therapy (all T1D patients require insulin):**
- **Multiple daily injections (MDI):** Basal insulin (glargine, detemir, degludec → once or twice daily) + bolus insulin (aspart, lispro, glulisine → with meals); "basal-bolus" regimen mimics physiological insulin; carbohydrate counting required for accurate bolus dosing
- **Continuous subcutaneous insulin infusion (CSII, insulin pump):** Delivers basal rate + bolus via subcutaneous catheter; allows variable basal rates (e.g., lower overnight, higher dawn phenomenon); hybrid closed-loop systems (Control-IQ, Omnipod 5, MiniMed 780G) combine pump + CGM + algorithm for semi-automated insulin delivery
- **Continuous glucose monitoring (CGM):** Real-time glucose readings (every 1-5 min); Dexcom G7 (10-day sensor), Libre 3 (14-day); factory calibrated; dramatically reduces HbA1c variability, hypoglycemia, DKA; time-in-range (70-180 mg/dL) is the key therapeutic target (>70% TIR associated with reduced complications)

**Disease-modifying therapy:**
- **Teplizumab (Tzield, anti-CD3 Fc-modified humanized antibody):** FDA approved 2022 for delaying Stage 3 T1D in Stage 2 (≥8 years old) — first approved T1D prevention therapy; anti-CD3 → T cell exhaustion and Treg expansion → slows beta cell destruction; median delay of clinical onset: 3 years in Stage 2 patients (TrialNet 2019 NEJM trial: 48 vs. 24 months median before Stage 3) [^herold-2019-teplizumab-t1d]; 14-day IV course; adverse effects: rash, cytokine release, transient EBV reactivation
- **Abatacept (CTLA-4 Ig):** T cell co-stimulation blockade (CD80/86-CD28 blockade) → reduced T cell priming; TrialNet trial: slows C-peptide decline in new-onset T1D at 2 years but effect wanes
- **Rituximab (anti-CD20):** B cell depletion → reduces antigen presentation and autoantibodies; C-peptide preservation at 1 year in new-onset T1D; no sustained long-term benefit

**Emerging and investigational:**
- **Low-dose IL-2:** Selectively expands Tregs (IL-2R high on Tregs); Phase 2 trials in new-onset T1D (DIPIT, ACT1ON)
- **Stem cell-derived islets (VX-880, Vertex):** SC-islets transplanted into portal vein → insulin production; early trials show insulin independence in severe T1D; requires immunosuppression
- **Encapsulated islets (ViaCyte, CRISPR-edited "immune invisible" beta cells):** Avoids immunosuppression requirement
- **Closed-loop insulin delivery + immunotherapy combinations:** Future frontier to both replace and protect beta cell function

## Connections

- `connects-to` → **[T Cytotoxic Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — CD8+ CTLs are the primary beta cell destroyers in T1D: autoreactive CTLs recognize HLA-A2-restricted GAD65, IGRP, and insulin peptides → perforin/granzyme and Fas-FasL → beta cell apoptosis; islet CTL infiltration (insulitis) precedes clinical onset by years.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — CD4+ Th1 cells coordinate T1D autoimmunity: HLA-DQ8/DQ2-restricted beta cell antigen presentation → IFN-gamma, IL-2 → CTL priming and macrophage activation; Treg insufficiency allows unchecked Th1 expansion; teplizumab shifts Th1/Treg balance.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Treg insufficiency is a core T1D mechanism: FOXP3+ Tregs suppress autoreactive T cells in pancreatic lymph nodes and islets; NOD mice have Treg functional defects; low-dose IL-2 expands Tregs → ongoing clinical trials to delay T1D progression.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — B cells act as APCs for beta cell antigens and produce autoantibodies (anti-GAD65, anti-IA-2, anti-ZnT8, anti-insulin) used for T1D staging (Stage 1: ≥2 Ab, normoglycemia; Stage 2: ≥2 Ab, dysglycemia); rituximab transiently preserves C-peptide in new-onset T1D.

[^atkinson-2014-t1d-lancet]: Atkinson MA, Eisenbarth GS, Michels AW. Type 1 diabetes. *Lancet.* 2014;383(9911):69-82. [doi:10.1016/S0140-6736(13)60591-7](https://doi.org/10.1016/S0140-6736(13)60591-7) · [PubMed 23890997](https://pubmed.ncbi.nlm.nih.gov/23890997/)
[^herold-2019-teplizumab-t1d]: Herold KC, Bundy BN, Long SA, et al. An anti-CD3 antibody, teplizumab, in relatives at risk for type 1 diabetes. *N Engl J Med.* 2019;381(7):603-613. [doi:10.1056/NEJMoa1905155](https://doi.org/10.1056/NEJMoa1905155) · [PubMed 31180675](https://pubmed.ncbi.nlm.nih.gov/31180675/)
[^insel-2015-t1d-staging]: Insel RA, Dunne JL, Atkinson MA, et al. Staging presymptomatic type 1 diabetes. *Diabetes Care.* 2015;38(10):1964-1974. [doi:10.2337/dc15-1419](https://doi.org/10.2337/dc15-1419) · [PubMed 26404926](https://pubmed.ncbi.nlm.nih.gov/26404926/)
