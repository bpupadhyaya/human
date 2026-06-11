---
schema: human-scale-entry/v1
id: sclc
name: Small Cell Lung Cancer
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Small cell lung cancer is a high-grade neuroendocrine carcinoma with near-universal RB1 and TP53 loss; atezolizumab or durvalumab + carboplatin/etoposide is first-line for extensive stage; DLL3-targeting tarlatamab is approved for relapsed disease; 5-year OS <10%."
aliases: ["SCLC", "small cell lung cancer", "small cell carcinoma", "limited stage SCLC", "extensive stage SCLC", "oat cell carcinoma", "SCLC-A", "neuroendocrine lung cancer", "lurbinectedin SCLC", "tarlatamab SCLC"]
sources:
  - id: horn-2018-impower133
    type: peer-reviewed
    cite: "Horn L, Mansfield AS, Szczęsna A, et al. First-line atezolizumab plus chemotherapy in extensive-stage small-cell lung cancer. N Engl J Med. 2018;379(23):2220-2229."
    doi: "10.1056/NEJMoa1809064"
    pmid: "30280641"
    url: "https://doi.org/10.1056/NEJMoa1809064"
  - id: paz-ares-2019-caspian
    type: peer-reviewed
    cite: "Paz-Ares L, Dvorkin M, Chen Y, et al. Durvalumab plus platinum-etoposide versus platinum-etoposide in first-line treatment of extensive-stage small-cell lung cancer (CASPIAN): a randomised, controlled, open-label, phase 3 trial. Lancet. 2019;394(10212):1929-1939."
    doi: "10.1016/S0140-6736(19)32222-6"
    pmid: "31590988"
    url: "https://doi.org/10.1016/S0140-6736(19)32222-6"
cross_links:
  - target: 01-human/03-molecular/dll3
    relation: connects-to
    note: "DLL3 overexpressed in >80% of SCLC (especially ASCL1-high subtype); drives Notch cis-inhibition → neuroendocrine identity; tarlatamab (DLL3×CD3 bispecific, FDA 2024): ORR 40%, CNS response 52%; first immunotherapy specifically approved for relapsed SCLC."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "RB1 biallelic loss in >90% of SCLC is the defining molecular event; RB1 loss releases E2F → ASCL1 → neuroendocrine program (DLL3, synaptophysin, chromogranin); RB1 loss also confers vulnerability to CDK4/6 inhibitor combinations in experimental models."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Atezolizumab (PD-L1) + carboplatin/etoposide (IMpower133: OS 12.3 vs 10.3 months) and durvalumab + platinum/etoposide (CASPIAN: OS 12.9 vs 10.5 months) are approved first-line regimens; PD-L1 expression does not predict benefit in SCLC; SCLC is immunologically cold."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 biallelic mutation co-occurs with RB1 loss in >90% of SCLC; p53 loss → unchecked DNA damage response → rapid proliferation; platinum/etoposide sensitivity partly attributable to p53-null apoptotic priming; SCLC lacks targetable TP53 restoration options."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Small cell lung cancer (~13-15% of lung cancer) is the most aggressive subtype, smoking-driven, arising centrally as a bulky hilar mass that often causes superior vena cava syndrome; it disseminates early, so ~70% present extensive-stage with brain, liver, or bone metastases."
  - target: 01-human/07-system/nsclc
    relation: connects-to
    note: "SCLC and NSCLC are the two divisions of lung cancer with opposite therapeutic logic: NSCLC is rich in targetable drivers, whereas SCLC has near-universal RB1 and TP53 loss with no actionable oncogene, relying on platinum-etoposide, immunotherapy, and DLL3-directed tarlatamab."
  - target: 01-human/07-system/neuroendocrine-tumors
    relation: connects-to
    note: "SCLC is the poorly differentiated, high-grade end of the pulmonary neuroendocrine spectrum (Ki-67 >50%, synaptophysin/INSM1+), unlike indolent carcinoid NETs; whereas SSTR2-high NETs use somatostatin analogs and PRRT, SCLC is treated as a chemo-driven carcinoma."
---

# Small Cell Lung Cancer

## Overview

**Small cell lung cancer (SCLC)** is a high-grade neuroendocrine carcinoma of the lung characterized by rapid growth, early metastasis, and initial chemosensitivity followed by near-universal relapse and drug resistance. SCLC accounts for ~13-15% of all lung cancers (~35,000 new cases/year in the USA), with a dismal 5-year overall survival of <10% for extensive-stage disease. Pathologically, SCLC is a poorly differentiated neuroendocrine carcinoma (WHO: NEC) with characteristic small cells, scant cytoplasm, salt-and-pepper chromatin, high mitotic rate (Ki-67 typically >50-70%), and necrosis. The defining molecular events — **biallelic RB1 loss** (>90%) and **TP53 biallelic mutation** (>90%) — cooperate to eliminate the two fundamental barriers to uncontrolled proliferation; no actionable oncogene driver (EGFR, ALK, RAS) is present. The treatment paradigm has been transformed by addition of anti-PD-L1/PD-1 immunotherapy to platinum/etoposide (IMpower133 and CASPIAN trials) in first-line, and by approval of **tarlatamab** (DLL3×CD3 bispecific) for relapsed disease [^horn-2018-impower133] [^paz-ares-2019-caspian].

**Epidemiology and risk factors:**
- Incidence: ~35,000 cases/year USA; declining with smoking reduction; accounts for 13-15% of all lung cancers
- **Smoking causation:** >95% of SCLC attributable to cigarette smoking; among the strongest smoking-cancer associations; typically develops after 30+ pack-years; rare in never-smokers
- Presentation: Rapid onset; hilar/mediastinal mass; superior vena cava syndrome; paraneoplastic syndromes (SIADH from ectopic ADH in ~10%; ACTH from ectopic CRH/ACTH → Cushing's in ~5%; Lambert-Eaton myasthenic syndrome from VGCC autoantibodies; paraneoplastic encephalitis from Hu/Ri antibodies)
- Staging: Two-stage system (Veterans Affairs): Limited stage (LS-SCLC, ~30%): Tumor confined to one hemithorax + regional nodes, can be encompassed in one radiation field; Extensive stage (ES-SCLC, ~70%): Beyond limited stage; includes most patients with liver, adrenal, bone, and brain metastases; TNM staging also used per AJCC 8th

**Molecular landscape:**
- RB1 biallelic loss (deletion, frameshift, missense): >90% of SCLC; the central molecular driver
- TP53 biallelic mutation: >90%; near-universal alongside RB1
- MYCL1/MYCN amplification: ~20% of SCLC; associated with SCLC-A subtype; poor prognosis
- SOX2 amplification: ~30%; squamous-like feature
- CREBBP/EP300 mutations: ~20%; chromatin regulators
- PTEN loss: ~10%
- FGFR1 amplification: ~6%; gefitinib active in preclinical models
- PIK3CA: ~6%
- No EGFR, KRAS, ALK, ROS1 driver alterations in SCLC (these define non-SCLC adenocarcinoma)

## Structure

### Pathological features and molecular subtypes

**Histopathology:**
- Tumor cells: Small (2× lymphocyte size), round-to-oval, scant cytoplasm, finely granular nuclear chromatin (salt-and-pepper), indistinct nucleoli, nuclear molding, numerous mitoses (>11 per 2 mm²), geographic necrosis
- IHC: Synaptophysin+, chromogranin A+ (variable), INSM1+ (highly specific), CD56/NCAM+; TTF-1+ in ~80%; Ki-67 >50-70%; CK AE1/3+ (dot-like pattern); RB1 protein absent/dim (correlates with RB1 gene loss)
- DLL3 IHC: >80% of SCLC; especially SCLC-A; semi-quantitative scoring
- Distinguishing SCLC from LCNEC: SCLC has smaller cells, no prominent nucleolus, nuclear molding; LCNEC has large cells, vesicular chromatin, prominent nucleoli; both are NEC; CD56/synaptophysin/chromogranin distinguish from non-NEC; Ki-67 >40% in both
- Crush artifact: SCLC is fragile → bronchoscopic biopsy specimens often show crush artifact (basophilic smeared nuclei) → diagnosis still possible from minimal material with IHC

**SCLC molecular subtypes (Rudin 2019):**
- **SCLC-A (ASCL1-high, ~70%):** DLL3+ high; Notch-low; synaptophysin/CgA+; most common; first-line chemo-responsive; tarlatamab most active
- **SCLC-N (NEUROD1-high, ~18%):** Less neuroendocrine; DLL3 intermediate; brain metastasis-prone; MYC high; responds to checkpoint inhibitors (higher TMB subgroup)
- **SCLC-P (POU2F3-high, ~10%):** Tuft cell-like; distinct from NE subtypes; DLL3 low/absent; FGFR1 amplification enriched; response to tarlatamab lower
- **SCLC-Y (YAP1-high, ~2%):** Non-NE, mesenchymal-like; aggressive; platinum-resistant; DLL3 low

**Paraneoplastic syndromes:**
- **SIADH (~10-15%):** Ectopic vasopressin (ADH) from SCLC → hyponatremia; fluid restriction + treatment of SCLC
- **Ectopic ACTH (~5%):** Ectopic CRH/ACTH → pituitary-independent Cushing's → severe hypokalemia, proximal myopathy, hyperglycemia; metyrapone or ketoconazole for cortisol control; treat SCLC
- **Lambert-Eaton myasthenic syndrome (LEMS, ~3%):** Autoimmodies to P/Q-type voltage-gated calcium channels (VGCC) → impaired neuromuscular transmission → proximal limb weakness, hyporeflexia, autonomic dysfunction; VGCC antibodies (anti-VGCC-α1); 3,4-diaminopyridine + immunosuppression; treat SCLC
- **Paraneoplastic encephalitis/limbic encephalitis (~1-2%):** Anti-Hu (ANNA-1) antibodies → encephalitis, sensory neuropathy; anti-CV2/CRMP5; MRI limbic changes; IVIG/steroids + SCLC treatment

### Diagnosis and staging

**Workup:**
- Chest CT + contrast: Hilar/mediastinal mass (central tumor typical); effusion; SVC obstruction
- PET/CT: Staging; brain MRI (mandatory for all SCLC due to high rate of occult brain mets ~10% at diagnosis)
- Bronchoscopy + biopsy: Central lesions; bronchoscopic sampling with cytology
- Bone marrow biopsy: No longer routine (PET/CT adequate for staging)
- Serum: LDH (prognostic); sodium (SIADH); ACTH/cortisol (ectopic ACTH)
- Endobronchial ultrasound (EBUS): Mediastinal lymph node sampling if limited stage considered

**Limited Stage SCLC (LS-SCLC) — concurrent chemoradiation:**
- Cisplatin + etoposide × 4 cycles + concurrent thoracic radiation (45 Gy BID or 60-66 Gy daily); NCCN preferred approach; concurrent = superior to sequential
- Prophylactic cranial irradiation (PCI): For patients with CR/PR to first-line therapy → 25 Gy/10 fractions; reduces CNS relapse from ~50% to ~25%; controversy: MRI surveillance vs. PCI (Japanese JIROG trial showed MRI surveillance non-inferior with preserved cognitive function → shifting practice toward MRI surveillance)
- 5-year OS: ~20-30% for LS-SCLC; curative intent

## Function

### Tumor biology — chemosensitivity and resistance

**Initial chemosensitivity:**
SCLC is initially highly sensitive to platinum-based chemotherapy (ORR ~80% for ES-SCLC) due to: RB1 loss → constitutive proliferation → more cells in S/G2/M phase (chemo-sensitive phases); p53 loss → reduced G1 checkpoint → cells do not arrest before lethal DNA damage; high apoptotic priming (BCL-2 high → venetoclax active in preclinical models); rapid tumor doubling time (~30-60 days).

**Acquired resistance ("transformation" and relapse):**
SCLC almost universally relapses within 6-12 months of first-line therapy; resistant SCLC has acquired: SLFN11 (Schlafen 11) downregulation (SLFN11 is a DNA/RNA helicase that promotes replication fork collapse under DNA damage → SLFN11 loss → SCLC cells repair platinum damage more effectively → chemo-resistance); phenotypic subtype switching (SCLC-A → SCLC-P or SCLC-Y → DLL3 downregulation → tarlatamab resistance); MYC amplification (acquired) → CDK1-dependent G2/M checkpoint reliance.

## Pathology

### First-line and relapsed treatment

**Extensive Stage SCLC — First-line:**

**Carboplatin (AUC 5) + etoposide × 4-6 cycles** (or cisplatin + etoposide for cisplatin-eligible patients): Standard backbone.

**+ Atezolizumab (anti-PD-L1, IMpower133):** [^horn-2018-impower133]
- 403 patients ES-SCLC; carboplatin/etoposide ± atezolizumab; maintenance atezolizumab
- OS 12.3 vs 10.3 months (HR 0.70); PFS 5.2 vs 4.3 months; ORR 60.2% vs 64.4%
- FDA approved March 2019; first immunotherapy + chemo regimen for SCLC; PD-L1 expression did NOT predict benefit
- Atezolizumab maintenance (16 cycles or progression) added to OS benefit

**+ Durvalumab (anti-PD-L1, CASPIAN):** [^paz-ares-2019-caspian]
- 805 patients ES-SCLC; platinum/etoposide ± durvalumab ± tremelimumab (CTLA-4)
- OS 12.9 vs 10.5 months (HR 0.75) for durvalumab + chemo vs. chemo alone
- FDA approved March 2020; durvalumab ± tremelimumab arm did not improve further over durvalumab alone
- Both atezolizumab and durvalumab + carbo/etoposide are NCCN Category 1 preferred regimens

**Second-line (relapsed within 6 months = platinum-resistant):**
- **Lurbinectedin (Zepzelca):** FDA accelerated approval July 2020; 105 patients R/R SCLC; ORR 35.2%; mDOR 5.3 months; mechanism: RNA polymerase II inhibitor → transcription addiction in SCLC → DNA damage; platinum-resistant ORR ~22%, platinum-sensitive ~45%
- **Topotecan:** Standard 2nd-line (OS ~6 months); modest activity; hematologic toxicity; FDA approved 1998; oral and IV formulations
- **Tarlatamab (FDA accelerated approval May 2024):** DLL3×CD3 BiTE; DeLLphi-301 Phase 2 (R/R ≥2 lines): 10 mg cohort ORR 40%, 100 mg ORR 32%; mDOR 9.7 months (10 mg); CNS ORR 52% (10 mg) — exceptional CNS activity; PFS 4.9 months; OS 14.3 months; approved for ≥2 prior lines; CRS management critical
- **Reinduction with platinum/etoposide:** For platinum-sensitive relapse (>6 months post-platinum); ORR ~50-60% for re-treatment; not standard after immunotherapy era
- **Nivolumab + ipilimumab:** CheckMate 032 basket: ORR 21.7% for combination in R/R SCLC; FDA approved 2020 for 3rd+ line (withdrawn from market 2023 due to CheckMate 451 maintenance failure)

**Third-line and beyond:**
- Tarlatamab (if not yet used): ORR ~40% in biomarker-unselected SCLC
- Temozolomide: Active in SCLC with brain metastases (CNS-penetrant)
- Irinotecan: ORR ~15-20% in R/R SCLC (Japan: cisplatin + irinotecan equivalent to cisplatin + etoposide in first-line for Japanese population)
- Clinical trial preferred

**Brain metastases:**
SCLC has highest rate of brain metastases among solid tumors (~50% at 2 years); SRS (stereotactic radiosurgery) for oligometastatic; WBRT (whole-brain RT) for multiple brain mets; tarlatamab shows 52% CNS ORR → may reduce need for WBRT in R/R SCLC; temozolomide for CNS-only progression.

## Connections

- `connects-to` → **[DLL3](../../03-molecular/dll3/README.md)** — DLL3 overexpressed in >80% of SCLC (especially ASCL1-high subtype); drives Notch cis-inhibition → neuroendocrine identity; tarlatamab (DLL3×CD3 bispecific, FDA 2024): ORR 40%, CNS response 52%; first immunotherapy specifically approved for relapsed SCLC.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — RB1 biallelic loss in >90% of SCLC is the defining molecular event; RB1 loss releases E2F → ASCL1 → neuroendocrine program (DLL3, synaptophysin, chromogranin); RB1 loss also confers vulnerability to CDK4/6 inhibitor combinations in experimental models.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Atezolizumab (PD-L1) + carboplatin/etoposide (IMpower133: OS 12.3 vs 10.3 months) and durvalumab + platinum/etoposide (CASPIAN: OS 12.9 vs 10.5 months) are approved first-line regimens; PD-L1 expression does not predict benefit in SCLC; SCLC is immunologically cold.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 biallelic mutation co-occurs with RB1 loss in >90% of SCLC; p53 loss → unchecked DNA damage response → rapid proliferation; platinum/etoposide sensitivity partly attributable to p53-null apoptotic priming; SCLC lacks targetable TP53 restoration options.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Small cell lung cancer (~13-15% of lung cancer) is the most aggressive subtype, smoking-driven, arising centrally as a bulky hilar mass that often causes superior vena cava syndrome; it disseminates early, so ~70% present extensive-stage with brain, liver, or bone metastases.
- `connects-to` → **[NSCLC](../nsclc/README.md)** — SCLC and NSCLC are the two divisions of lung cancer with opposite therapeutic logic: NSCLC is rich in targetable drivers, whereas SCLC has near-universal RB1 and TP53 loss with no actionable oncogene, relying on platinum-etoposide, immunotherapy, and DLL3-directed tarlatamab.
- `connects-to` → **[Neuroendocrine Tumors](../neuroendocrine-tumors/README.md)** — SCLC is the poorly differentiated, high-grade end of the pulmonary neuroendocrine spectrum (Ki-67 >50%, synaptophysin/INSM1+), unlike indolent carcinoid NETs; whereas SSTR2-high NETs use somatostatin analogs and PRRT, SCLC is treated as a chemo-driven carcinoma.

[^horn-2018-impower133]: Horn L, Mansfield AS, Szczęsna A, et al. First-line atezolizumab plus chemotherapy in extensive-stage small-cell lung cancer. *N Engl J Med.* 2018;379(23):2220-2229. [doi:10.1056/NEJMoa1809064](https://doi.org/10.1056/NEJMoa1809064) · [PubMed 30280641](https://pubmed.ncbi.nlm.nih.gov/30280641/)
[^paz-ares-2019-caspian]: Paz-Ares L, Dvorkin M, Chen Y, et al. Durvalumab plus platinum-etoposide versus platinum-etoposide in first-line treatment of extensive-stage small-cell lung cancer (CASPIAN). *Lancet.* 2019;394(10212):1929-1939. [doi:10.1016/S0140-6736(19)32222-6](https://doi.org/10.1016/S0140-6736(19)32222-6) · [PubMed 31590988](https://pubmed.ncbi.nlm.nih.gov/31590988/)
