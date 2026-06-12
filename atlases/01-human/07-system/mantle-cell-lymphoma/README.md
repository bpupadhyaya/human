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

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^wang-2013-ibrutinib-mcl]: Wang ML, Rule S, Martin P, et al. Targeting BTK with ibrutinib in relapsed or refractory mantle-cell lymphoma. *N Engl J Med.* 2013;369(6):507-516. [doi:10.1056/NEJMoa1306220](https://doi.org/10.1056/NEJMoa1306220) · [PubMed 23782157](https://pubmed.ncbi.nlm.nih.gov/23782157/)
[^wang-2020-brexu-zuma2]: Wang M, Munoz J, Goy A, et al. KTE-X19 CAR T-cell therapy in relapsed or refractory mantle-cell lymphoma. *N Engl J Med.* 2020;382(14):1331-1342. [doi:10.1056/NEJMoa1914347](https://doi.org/10.1056/NEJMoa1914347) · [PubMed 32242358](https://pubmed.ncbi.nlm.nih.gov/32242358/)
