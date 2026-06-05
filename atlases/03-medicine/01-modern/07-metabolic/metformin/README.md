---
schema: medicine-entry/v1
id: metformin
name: Metformin
atlas: 03-medicine
scale: 01-modern
status: draft
last_reviewed: 2026-06-04
summary: "Biguanide; global first-line for type 2 diabetes. Inhibits mitochondrial Complex I → AMPK → suppressed PEPCK/G6Pase → ↓ hepatic gluconeogenesis. HbA1c −1–2%; weight-neutral; no hypoglycemia monotherapy. UKPDS: 36% mortality reduction. 120 million users."
aliases: ["metformin", "Glucophage", "Fortamet", "Glumetza", "dimethylbiguanide", "1,1-dimethylbiguanide"]
sources:
  - id: ukpds-1998-metformin
    type: peer-reviewed
    cite: "UK Prospective Diabetes Study (UKPDS) Group. Effect of intensive blood-glucose control with metformin on complications in overweight patients with type 2 diabetes (UKPDS 34). Lancet. 1998;352(9131):854-65."
    doi: "10.1016/S0140-6736(98)07037-8"
    pmid: "9742977"
    url: "https://doi.org/10.1016/S0140-6736(98)07037-8"
  - id: foretz-2014-metformin-mechanism
    type: peer-reviewed
    cite: "Foretz M, Guigas B, Bertrand L, Pollak M, Viollet B. Metformin: from mechanisms of action to therapies. Cell Metab. 2014;20(6):953-66."
    doi: "10.1016/j.cmet.2014.09.018"
    pmid: "25456737"
    url: "https://doi.org/10.1016/j.cmet.2014.09.018"
  - id: ada-2024-standards
    type: clinical-guideline
    cite: "American Diabetes Association Professional Practice Committee. Standards of Care in Diabetes — 2024. Diabetes Care. 2024;47(Suppl 1):S1-S321."
    doi: "10.2337/dc24-Sint"
    url: "https://doi.org/10.2337/dc24-Sint"
    accessed: "2026-06-04"
  - id: zhang-2014-metformin-ct50
    type: peer-reviewed
    cite: "Zhang CS, Li M, Ma T, et al. Metformin activates AMPK through the lysosomal pathway. Cell Metab. 2016;24(4):521-522."
    doi: "10.1016/j.cmet.2016.09.003"
    pmid: "27732831"
    url: "https://doi.org/10.1016/j.cmet.2016.09.003"
cross_links:
  - target: 01-human/03-molecular/insulin
    relation: modulates
    evidence: foretz-2014-metformin-mechanism
    note: "Metformin potentiates insulin signaling by reducing hepatic insulin resistance; lower fasting glucose allows the same insulin concentration to suppress gluconeogenesis more effectively; metformin does not increase insulin secretion, avoiding hypoglycemia in monotherapy."
  - target: 01-human/06-organ/liver
    relation: treats
    evidence: ukpds-1998-metformin
    note: "The primary site of metformin action is the liver; OCT1-mediated accumulation in hepatocytes reaches 50–500× plasma concentrations; Complex I inhibition raises AMP/ATP ratio → AMPK activation → ACC phosphorylation (↓ malonyl-CoA) + CREB-TORC2 disruption → ↓ PEPCK and G6Pase transcription → ↓ hepatic gluconeogenesis, the dominant mechanism of fasting hyperglycemia in T2DM."
---

# Metformin

## Overview

**Metformin** (1,1-dimethylbiguanide) is the most widely prescribed oral antidiabetic drug in history — an estimated **120 million people** worldwide take it daily, and it is the first-line pharmacotherapy for type 2 diabetes mellitus (T2DM) in every major clinical guideline including ADA (American Diabetes Association), EASD (European Association for the Study of Diabetes), and WHO Essential Medicines List.

Despite being in clinical use since the 1950s (derived from the guanidine-containing plant *Galega officinalis*, used in medieval European herbal medicine), metformin's primary molecular mechanism was only elucidated between 2001–2016: **inhibition of Complex I (NADH:ubiquinone oxidoreductase) of the mitochondrial electron transport chain** in hepatocytes, raising the cellular AMP/ATP ratio and activating **AMPK** [^foretz-2014-metformin-mechanism].

Metformin occupies a unique niche: it lowers glucose effectively, is weight-neutral or modestly weight-reducing, causes no hypoglycemia as monotherapy, has a strong safety profile over 60+ years of use, and has demonstrated **mortality benefit** in the landmark UKPDS 34 trial — a 36% reduction in all-cause mortality compared with conventional treatment in overweight patients with T2DM [^ukpds-1998-metformin].

## Mechanism

**Primary hepatic mechanism:**
1. **Uptake:** Metformin is a positively charged hydrophilic molecule (MW 165 Da) that enters hepatocytes through **OCT1** (organic cation transporter 1, SLC22A1); accumulates to 50–500× plasma concentrations in hepatocyte cytoplasm and mitochondria
2. **Complex I inhibition:** Metformin inhibits Complex I of the mitochondrial ETC (NADH dehydrogenase); the mechanism involves direct binding to the ND1 subunit; this modestly reduces mitochondrial ATP production while increasing AMP
3. **AMPK activation (indirect):** Elevated AMP/ATP ratio activates **AMPK** (AMP-activated protein kinase, the cellular energy sensor) both allosterically and via LKB1-mediated phosphorylation of Thr172; AMPK also activated directly via lysosomal pathway [^zhang-2014-metformin-ct50]
4. **Gluconeogenesis suppression:**
   - AMPK phosphorylates and inactivates **ACC** (acetyl-CoA carboxylase) → ↓ malonyl-CoA → ↑ CPT1 activity → ↑ fatty acid oxidation (secondary effect)
   - AMPK phosphorylates **CRTC2** (CREB-regulated transcription coactivator 2) and **HDAC5**, disrupting CREB-TORC2 complex that drives *PEPCK* (PCK1) and *G6Pase* (G6PC) transcription → ↓ gluconeogenic gene expression
   - Net effect: ↓ hepatic glucose output, the dominant driver of fasting hyperglycemia in T2DM
5. **Peripheral effects:** Modest improvements in insulin sensitivity in skeletal muscle and adipose tissue; reduced intestinal glucose absorption; gut microbiome modulation (increased *Akkermansia muciniphila*, lactate-producing bacteria)

**Insulin interaction:**
Metformin does not stimulate insulin secretion. Its effect is to reduce the need for high insulin concentrations to suppress gluconeogenesis — improving hepatic insulin sensitivity and lowering fasting glucose without causing hypoglycemia [^foretz-2014-metformin-mechanism].

## Clinical Use

**Type 2 diabetes — first-line:**
- ADA Standard of Care 2024: Metformin remains the preferred initial pharmacological agent when lifestyle modification alone is insufficient; can be used across the spectrum of T2DM [^ada-2024-standards]
- HbA1c reduction: **1.0–2.0 percentage points** from baseline; comparable to most second-line agents
- Titration: Start 500 mg with meals; increase by 500 mg/week to 2000 mg/day (max 2550 mg/day); extended-release formulation reduces GI side effects

**Contraindications:**
- eGFR <30 mL/min/1.73m² (FDA) / <30 mL/min (EMA): risk of lactic acidosis
- Acute illness with hemodynamic instability, significant hepatic failure, active alcoholism
- Hold 48h before/after iodinated contrast (eGFR <60 mL/min)

**Lactic acidosis risk:**
Historically overestimated. At therapeutic doses and in patients without contraindications, lactic acidosis incidence is ~3 per 100,000 patient-years — lower than sulfonylureas (hypoglycemia mortality). Mechanism: elevated lactate from intestinal cells (metformin inhibits lactate oxidation in enterocytes); systemic lactic acidosis only in context of renal failure (impairs metformin excretion) or severe hypoxia.

## Evidence

| Trial / Review | Key finding |
|:---|:---|
| UKPDS 34 (1998) [^ukpds-1998-metformin] | 36% reduction in all-cause mortality, 39% reduction in MI vs. conventional treatment in overweight T2DM |
| Multiple meta-analyses | HbA1c reduction 1–2%; modest weight reduction (0.5–3 kg vs. comparators); no hypoglycemia in monotherapy |
| AMPK/mechanistic studies [^foretz-2014-metformin-mechanism] | Complex I inhibition → AMPK → gluconeogenesis suppression established as primary mechanism |
| ADA/EASD 2024 [^ada-2024-standards] | Retained as first-line; SGLT2i/GLP-1RA added as preferred in CKD/CVD comorbidities |

## Connections

- **Modulates** → [Insulin](../../../../../01-human/03-molecular/insulin/README.md): Metformin reduces hepatic insulin resistance, allowing lower insulin concentrations to suppress gluconeogenesis; it improves insulin sensitivity without stimulating secretion, avoiding hypoglycemia.
- **Treats** → [Liver](../../../../../01-human/06-organ/liver/README.md): The primary site of metformin action — OCT1-mediated hepatocyte uptake → Complex I inhibition → AMPK activation → suppression of PEPCK and G6Pase → reduced hepatic glucose output.
