---
schema: human-scale-entry/v1
id: renal-cell-carcinoma
name: Renal Cell Carcinoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Clear cell RCC (~75%) is driven by VHL loss → HIF activation → VEGF angiogenesis; papillary type driven by MET and CDKN2A. Nivolumab+ipilimumab and pembrolizumab+axitinib are first-line for advanced RCC; cabozantinib is active after ICI progression."
aliases: ["renal cell carcinoma", "RCC", "clear cell RCC", "ccRCC", "papillary RCC", "chromophobe RCC", "kidney cancer", "renal carcinoma", "VHL-mutant RCC"]
sources:
  - id: motzer-2018-checkmate214
    type: peer-reviewed
    cite: "Motzer RJ, Tannir NM, McDermott DF, et al. Nivolumab plus ipilimumab versus sunitinib in advanced renal-cell carcinoma. N Engl J Med. 2018;378(14):1277-1290."
    doi: "10.1056/NEJMoa1712126"
    pmid: "29562145"
    url: "https://doi.org/10.1056/NEJMoa1712126"
  - id: rini-2019-keynote426
    type: peer-reviewed
    cite: "Rini BI, Plimack ER, Stus V, et al. Pembrolizumab plus axitinib versus sunitinib for advanced renal-cell carcinoma. N Engl J Med. 2019;380(12):1116-1127."
    doi: "10.1056/NEJMoa1816714"
    pmid: "30779529"
    url: "https://doi.org/10.1056/NEJMoa1816714"
cross_links:
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Sunitinib and pazopanib (VEGFR TKIs) were first-line RCC standards; cabozantinib (VEGFR+MET+AXL) approved 1st-line for poor/intermediate-risk (CABOSUN) and 2nd-line (METEOR); ICI+VEGFR TKI combinations (pembro+axitinib, nivo+cabo) now preferred in first-line."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Nivolumab+ipilimumab (CheckMate 214) improved OS in intermediate/poor-risk RCC; pembrolizumab+axitinib (KEYNOTE-426) improved OS vs. sunitinib; nivolumab+cabozantinib (CheckMate 9ER) PFS 16.6 vs. 8.3 months; ICI combinations are standard first-line for advanced RCC."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Everolimus (mTOR inhibitor) approved for 2nd-line RCC after VEGFR TKI failure (RECORD-1: PFS 4.9 vs. 1.9 months); temsirolimus improved OS vs. IFN-α in poor-risk RCC; lenvatinib+everolimus approved 2nd-line; mTOR inhibitors largely displaced by ICI+VEGFR combinations."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "VHL loss → constitutive HIF-1α/HIF-2α stabilization → VEGF, GLUT1, EPO, PDGF transcription in ccRCC; HIF-2α (EPAS1) is the primary oncogenic HIF isoform; belzutifan (HIF-2α inhibitor) FDA approved 2021 for VHL disease and 2023 for 3rd-line ccRCC."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Most RCCs arise from the kidney's proximal tubule; small T1a tumors are often found incidentally on CT and cured by nephron-sparing partial nephrectomy, while VHL-null tumor cells secrete EPO, renin, or PTHrP — causing paraneoplastic polycythemia, hypertension, or hypercalcemia."
  - target: 01-human/07-system/vhl-disease
    relation: connects-to
    note: "Von Hippel-Lindau disease (germline VHL loss) predisposes to bilateral, multifocal, early-onset clear-cell RCC alongside hemangioblastomas and pheochromocytomas; the same VHL→HIF-2α pseudohypoxia drives both hereditary and the >90% of sporadic ccRCC, and belzutifan targets it."
  - target: 01-human/03-molecular/met
    relation: connects-to
    note: "Type 1 papillary RCC is driven by MET activation (amplification or germline mutation in hereditary papillary RCC), distinct from VHL-driven clear-cell disease; these tumors respond poorly to VEGFR TKIs, so the MET/VEGFR2 inhibitor cabozantinib is the preferred targeted agent."
---

# Renal Cell Carcinoma

## Overview

**Renal cell carcinoma (RCC)** is a heterogeneous group of kidney malignancies arising from the renal tubular epithelium, with **clear cell RCC (ccRCC)** accounting for ~75% of cases. The hallmark of ccRCC is biallelic inactivation of the **VHL tumor suppressor** — present in >90% of ccRCC — leading to constitutive HIF-1α/HIF-2α stabilization and a transcriptional program that drives neoangiogenesis via VEGF, PDGF, TGF-α, and EPO. This molecular dependency on HIF/VEGF has underpinned two decades of targeted therapy development: from the first VEGFR TKIs (sunitinib, 2006) through combined immunotherapy+VEGFR TKI regimens that are now standard of care in the frontline setting [^motzer-2018-checkmate214].

**Epidemiology:**
- ~81,000 new cases/year in the US; ~14,000 deaths/year; incidence rising (incidental detection on CT)
- Male:Female ~2:1; median age at diagnosis ~64 years
- 5-year survival: ~76% overall; ~93% for localized; ~15% for metastatic disease
- Risk factors: Smoking (1.5-2× risk), obesity, hypertension, occupational cadmium/trichloroethylene, analgesic nephropathy; hereditary syndromes (VHL disease, Birt-Hogg-Dubé, hereditary papillary RCC, TSC)

**RCC versus urothelial carcinoma:**
RCC arises from the renal parenchyma (tubular cells); urothelial carcinoma arises from the transitional epithelium of the renal pelvis/ureter. Both can present with hematuria but have completely different molecular biology and treatment.

## Structure

### RCC subtypes and molecular features

**Clear cell RCC (ccRCC, ~75%):**
- VHL inactivation >90%; chromosome 3p loss (VHL locus) universal
- Co-mutations: PBRM1 (~40%), BAP1 (~15%), SETD2 (~15%), KDM5C, MTOR (~5%), TP53 (~10% in sarcomatoid variant)
- Highly vascular (VEGF-driven) → VEGFR TKI-sensitive
- Sarcomatoid differentiation (~5-10%): Aggressive; TP53 mutation; PD-L1 high → especially ICI-responsive

**Papillary RCC (pRCC, ~15%):**
- Type 1: MET amplification/mutation (~80%); indolent; hereditary papillary RCC (germline MET mutation)
- Type 2: CDKN2A deletion, SETD2 mutation, CpG island methylation → fumarate hydratase (FH) mutations in hereditary leiomyomatosis and RCC (HLRCC); type 2 is more aggressive
- Fewer VEGFR TKI responders; cabozantinib (MET+VEGFR2 inhibitor) most active VEGFR TKI
- ICI active in high-grade pRCC; sunitinib inferior to ICI/cabozantinib

**Chromophobe RCC (chRCC, ~5%):**
- Monosomy of multiple chromosomes (1, 2, 6, 10, 13, 17); TP53 mutations in oncocytoma-like variants
- Birt-Hogg-Dubé (FLCN germline mutation) → multifocal chRCC/oncocytoma/hybrid tumors + lung cysts + fibrofolliculomas
- mTOR pathway activation in ~25%; generally indolent; VEGFR TKIs less effective; platinum-based in aggressive Bellini duct carcinoma (collecting duct RCC)

**Rare RCC subtypes:**
- Collecting duct (Bellini duct) carcinoma: Aggressive; cisplatin-based chemotherapy; poor prognosis
- Medullary RCC: Sickle cell trait-associated; aggressive; responds poorly to standard RCC therapies; EZH2-driven (SMARCB1 loss)
- Translocation RCC: TFE3 or TFEB fusions; ~15% of pediatric RCC; mTOR pathway activated

### IMDC risk classification (International Metastatic RCC Database Consortium)

Risk factors: Karnofsky PS <80%, time from diagnosis to systemic therapy <1 year, hemoglobin < LLN, calcium > ULN, neutrophils > ULN, platelets > ULN.
- **Favorable risk (0 factors):** Median OS ~43 months
- **Intermediate risk (1-2 factors):** Median OS ~23 months
- **Poor risk (≥3 factors):** Median OS ~7.8 months

## Function

### Normal kidney tubular biology

**Proximal tubular cells (PCT):**
Primary site of ccRCC origin. PCT reabsorbs ~67% of filtered solute; relies on oxidative phosphorylation; highly metabolically active; rich in mitochondria. VHL normally maintains oxygen homeostasis in these cells; VHL loss → pseudohypoxic state despite normal pO₂.

**Tubular-to-mesenchymal biology in ccRCC:**
ccRCC cells accumulate lipid (lipid droplets give "clear cell" appearance on H&E after lipid extraction); lipid droplets composed of cholesterol esters — driven by HIF-1α activation of lipogenic genes (FASN, ACLY); CCND1 amplification, PI3K-AKT activation cooperate with HIF → lipid-accumulating, angiogenic tumors.

**VHL-HIF in normal renal oxygen sensing:**
Kidney → primary site of EPO production under hypoxia; VHL-intact renal interstitial cells sense hypoxia → PHD inhibited → VHL cannot bind hydroxylated HIF-2α → HIF-2α stabilized → EPO transcription → erythropoiesis. RCC patients often have paraneoplastic polycythemia (excess EPO from VHL-null tumor cells).

## Pathology

### Staging and diagnosis

**TNM staging:**
- T1: ≤7 cm, confined to kidney (T1a ≤4 cm)
- T2: >7 cm, confined to kidney
- T3: Renal vein/IVC involvement or perirenal fat extension (T3a/b/c)
- T4: Beyond Gerota's fascia or invades adjacent organs
- M1: Metastatic → includes lymph node (rare hematogenous spread to lung, bone, liver, brain)

**Paraneoplastic syndromes in RCC:**
- Polycythemia: EPO secretion from tumor
- Hypercalcemia: PTHrP secretion (~5%)
- Hypertension: Renin secretion
- Stauffer syndrome (non-metastatic hepatic dysfunction): Reversible with nephrectomy
- Fever/cachexia: Cytokine (IL-6, TNF-α) secretion

**Diagnosis:**
- Incidental finding on CT (~50% of localized RCC) or presentation with hematuria, flank pain, abdominal mass (classic triad: <10% of patients)
- CT chest/abdomen/pelvis with contrast: Standard staging; RCC is hypervascular on arterial phase
- Bone scan/brain MRI: If symptomatic; ~10% brain metastasis at diagnosis
- Biopsy before systemic therapy: Recommended to confirm histology; percutaneous core biopsy under CT guidance; >95% diagnostic accuracy

**Surgical management:**
- **Partial nephrectomy:** Standard for T1a (<4 cm), favored for T1b if technically feasible; equivalent oncologic outcomes to radical nephrectomy for T1-T2; preserves renal function
- **Radical nephrectomy:** T2-T3 or technically complex tumors; laparoscopic/robotic preferred over open for most
- **Cytoreductive nephrectomy (CN):** Historical standard before targeted therapy era; CARMENA trial (2018): Sunitinib alone non-inferior to CN+sunitinib in IMDC intermediate/poor-risk; CN reserved for favorable-risk patients or symptom control
- **Metastasectomy:** Curative in select patients with solitary resectable metastasis

### Treatment

**First-line (favorable risk):**
- **Pembrolizumab + axitinib (KEYNOTE-426):** [^rini-2019-keynote426] OS and PFS benefit vs. sunitinib across all IMDC groups; FDA approved 2019; ORR 59%; OS benefit at 30 months (68% vs. 58%)
- **Sunitinib** (historically): PFS 11 months; still used in select patients; VEGFR1/2/3/PDGFR/KIT/FLT3 inhibitor; alternative to ICI-based therapy (if ICI contraindicated)

**First-line (intermediate/poor risk):**
- **Nivolumab + ipilimumab (CheckMate 214):** [^motzer-2018-checkmate214] OS 47.0 vs. 26.6 months vs. sunitinib in intermediate/poor risk; ORR 42% vs. 27%; FDA approved 2018; ~11% complete responses; 4-year OS 43% vs. 31%
- **Pembrolizumab + axitinib:** Active across risk groups; OS benefit regardless of IMDC risk
- **Nivolumab + cabozantinib (CheckMate 9ER):** PFS 16.6 vs. 8.3 months vs. sunitinib; FDA approved 2021; ORR 56%

**Second-line and beyond:**
- **Cabozantinib (CABOMETYX, METEOR trial):** VEGFR+MET+AXL+RET inhibitor; PFS 7.4 vs. 3.8 months vs. everolimus; ORR 21%; standard post-VEGFR TKI; also active after ICI (CONTACT-03 trial used as backbone)
- **Nivolumab (CheckMate 025):** OS 25 vs. 19 months vs. everolimus in 2nd-line; FDA approved 2015; first ICI in RCC; now part of 1st-line combination
- **Belzutifan (LITESPARK-005):** PFS 5.6 vs. 3.5 months vs. everolimus; ORR 22%; FDA approved 2023 for RCC after prior anti-PD-1+anti-VEGFR
- **Lenvatinib + everolimus (Study 205):** ORR 43% vs. 6% everolimus; PFS 14.6 vs. 5.5 months; 2nd-line option
- **Lenvatinib + pembrolizumab (CLEAR trial):** PFS 23.9 vs. 9.2 months vs. sunitinib; FDA approved 2021 as first-line option; ORR 71%
- **Axitinib:** 2nd/3rd-line VEGFR TKI (now primarily used with pembrolizumab in 1st line)
- **Everolimus:** mTOR inhibitor; largely supplanted; still used after 2+ TKIs or as belzutifan comparator

**Non-clear cell RCC:**
- Papillary: Cabozantinib (SWOG 1500, PAPMET) preferred VEGFR TKI; ICI combinations active
- Sarcomatoid: ICI+VEGFR TKI combinations → especially effective (ORR ~50-60% with nivo+ipi or pembro+ax in sarcomatoid component)
- Medullary/collecting duct: Platinum+gemcitabine or carboplatin+paclitaxel; experimental EZH2 inhibitors

## Connections

- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Sunitinib and pazopanib (VEGFR TKIs) were first-line RCC standards; cabozantinib (VEGFR+MET+AXL) approved 1st-line for poor/intermediate-risk (CABOSUN) and 2nd-line (METEOR); ICI+VEGFR TKI combinations (pembro+axitinib, nivo+cabo) now preferred in first-line.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Nivolumab+ipilimumab (CheckMate 214) improved OS in intermediate/poor-risk RCC; pembrolizumab+axitinib (KEYNOTE-426) improved OS vs. sunitinib; nivolumab+cabozantinib (CheckMate 9ER) PFS 16.6 vs. 8.3 months; ICI combinations are standard first-line for advanced RCC.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Everolimus (mTOR inhibitor) approved for 2nd-line RCC after VEGFR TKI failure (RECORD-1: PFS 4.9 vs. 1.9 months); temsirolimus improved OS vs. IFN-α in poor-risk RCC; lenvatinib+everolimus approved 2nd-line; mTOR inhibitors largely displaced by ICI+VEGFR combinations.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — VHL loss → constitutive HIF-1α/HIF-2α stabilization → VEGF, GLUT1, EPO, PDGF transcription in ccRCC; HIF-2α (EPAS1) is the primary oncogenic HIF isoform; belzutifan (HIF-2α inhibitor) FDA approved 2021 for VHL disease and 2023 for 3rd-line ccRCC.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Most RCCs arise from the kidney's proximal tubule; small T1a tumors are often found incidentally on CT and cured by nephron-sparing partial nephrectomy, while VHL-null tumor cells secrete EPO, renin, or PTHrP — causing paraneoplastic polycythemia, hypertension, or hypercalcemia.
- `connects-to` → **[VHL Disease](../vhl-disease/README.md)** — Von Hippel-Lindau disease (germline VHL loss) predisposes to bilateral, multifocal, early-onset clear-cell RCC alongside hemangioblastomas and pheochromocytomas; the same VHL→HIF-2α pseudohypoxia drives both hereditary and the >90% of sporadic ccRCC, and belzutifan targets it.
- `connects-to` → **[MET](../../03-molecular/met/README.md)** — Type 1 papillary RCC is driven by MET activation (amplification or germline mutation in hereditary papillary RCC), distinct from VHL-driven clear-cell disease; these tumors respond poorly to VEGFR TKIs, so the MET/VEGFR2 inhibitor cabozantinib is the preferred targeted agent.

[^motzer-2018-checkmate214]: Motzer RJ, Tannir NM, McDermott DF, et al. Nivolumab plus ipilimumab versus sunitinib in advanced renal-cell carcinoma. *N Engl J Med.* 2018;378(14):1277-1290. [doi:10.1056/NEJMoa1712126](https://doi.org/10.1056/NEJMoa1712126) · [PubMed 29562145](https://pubmed.ncbi.nlm.nih.gov/29562145/)
[^rini-2019-keynote426]: Rini BI, Plimack ER, Stus V, et al. Pembrolizumab plus axitinib versus sunitinib for advanced renal-cell carcinoma. *N Engl J Med.* 2019;380(12):1116-1127. [doi:10.1056/NEJMoa1816714](https://doi.org/10.1056/NEJMoa1816714) · [PubMed 30779529](https://pubmed.ncbi.nlm.nih.gov/30779529/)
