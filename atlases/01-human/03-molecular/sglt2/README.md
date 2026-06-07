---
schema: human-scale-entry/v1
id: sglt2
name: SGLT2
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "SGLT2 is a sodium-glucose cotransporter in the proximal tubule reabsorbing ~90% of filtered glucose; SGLT2 inhibitors (dapagliflozin, empagliflozin) reduce blood glucose, intraglomerular pressure, and cardiac preload; proven to reduce CV death, HHF, and CKD progression."
aliases: ["SGLT2", "SLC5A2", "sodium-glucose cotransporter 2", "SGLT2 inhibitor", "dapagliflozin target", "empagliflozin target", "canagliflozin target", "gliflozin", "SGLT2i"]
cross_links:
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "EMPA-REG OUTCOME (empagliflozin, T2D + CVD): 14% MACE reduction, 35% CV death reduction, 35% HHF reduction; SGLT2 inhibitors reduce HbA1c ~0.7-1.0% with glucose-dependent mechanism avoiding hypoglycemia; first-line therapy in T2D with established ASCVD or heart failure."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "DAPA-HF (dapagliflozin, HFrEF): 25% reduction in worsening HF + CV death in T2D and non-T2D; EMPEROR-Reduced (empagliflozin): 25% reduction; SGLT2 inhibitors are the fourth pillar of GDMT, reducing HHF and CV death independent of diabetes status."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "CREDENCE (canagliflozin): 30% reduction in kidney endpoint in T2D + CKD; DAPA-CKD (dapagliflozin): 39% reduction in eGFR decline/dialysis/renal death in CKD with and without T2D; SGLT2 inhibitors slow CKD progression via tubuloglomerular feedback and anti-fibrotic effects."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "SGLT2 inhibitors reduce NLRP3 inflammasome activation in renal tubular cells and macrophages, decreasing IL-1β and IL-18 production; this anti-inflammatory mechanism contributes to cardiorenal protection beyond glucose lowering in diabetic kidney disease."
sources:
  - id: zinman-2015-empa-reg
    type: peer-reviewed
    cite: "Zinman B, Wanner C, Lachin JM, et al. Empagliflozin, cardiovascular outcomes, and mortality in type 2 diabetes. N Engl J Med. 2015;373(22):2117-2128."
    doi: "10.1056/NEJMoa1504720"
    pmid: "26378978"
    url: "https://doi.org/10.1056/NEJMoa1504720"
  - id: mcmurray-2019-dapa-hf
    type: peer-reviewed
    cite: "McMurray JJV, Solomon SD, Inzucchi SE, et al. Dapagliflozin in patients with heart failure and reduced ejection fraction. N Engl J Med. 2019;381(21):1995-2008."
    doi: "10.1056/NEJMoa1911303"
    pmid: "31535829"
    url: "https://doi.org/10.1056/NEJMoa1911303"
---

# SGLT2

## Overview

**SGLT2** (sodium-glucose cotransporter 2; gene *SLC5A2*, chromosome 16p11.2) is an apical membrane transporter of the **proximal convoluted tubule (S1 segment)** responsible for reabsorbing ~90% of the ~180 g of glucose filtered daily by the kidney. Under physiological conditions, virtually all filtered glucose is reclaimed — glucosuria begins only when plasma glucose exceeds the **renal threshold (~180 mg/dL)**, at which point SGLT2 becomes saturated.

SGLT2 inhibitors (gliflozins) — **dapagliflozin** (Farxiga), **empagliflozin** (Jardiance), **canagliflozin** (Invokana), **ertugliflozin** (Steglatro) — were developed as glucose-lowering agents but proved transformative across three organ systems. The EMPA-REG OUTCOME trial (2015) demonstrated a 35% reduction in cardiovascular death with empagliflozin in type 2 diabetes (T2D) — a magnitude unseen with any prior glucose-lowering drug — driven primarily by hemodynamic and renal mechanisms rather than glycemic improvement [^zinman-2015-empa-reg]. DAPA-HF (2019) extended SGLT2 inhibitor benefit to heart failure patients without diabetes, establishing a new standard of care [^mcmurray-2019-dapa-hf]. CREDENCE (canagliflozin) and DAPA-CKD (dapagliflozin) confirmed nephroprotective effects independent of glycemic control.

**SGLT2 inhibitor approved indications (2025):**

| Drug | T2D glycemic | CV risk reduction | HFrEF | HFpEF | CKD |
|---|---|---|---|---|---|
| Empagliflozin | Yes | Yes (established CVD) | Yes | Yes | Yes |
| Dapagliflozin | Yes | Yes | Yes | Yes | Yes |
| Canagliflozin | Yes | Yes | No | No | Yes |
| Ertugliflozin | Yes | Yes (HHF) | No | No | No |

## Structure

SGLT2 is a **672 amino acid glycoprotein** with 14 transmembrane helices. It is a member of the **SLC5A solute carrier family**, sharing structural homology with bacterial vSGLT (Vibrio parahaemolyticus) for which crystal structures defined the alternating-access mechanism.

**Key structural features:**
- **Na⁺:glucose stoichiometry: 1:1** — lower-affinity, high-capacity transporter (Km ~5 mM glucose); drives reabsorption of bulk filtered glucose
- **Location: S1 segment of proximal convoluted tubule** (apical membrane) — the high-capacity, low-affinity site; handles ~90% of filtered glucose
- **SGLT1 (SLC5A1) comparison:** Located in S3 segment (distal proximal tubule); 2:1 Na⁺:glucose stoichiometry; higher affinity (Km ~0.3 mM), lower capacity; handles remaining ~10% of filtered glucose. Also expressed in intestinal brush border (primary intestinal glucose absorption transporter).
- **Basolateral exit:** GLUT2 (facilitated diffusion) exports glucose from tubular cell to peritubular capillary

**Inhibitor binding:** SGLT2 inhibitors are glucose mimetics that occupy the sugar-binding site in an outward-facing conformation, competitively inhibiting Na⁺-coupled glucose transport. Most gliflozins have >1000-fold selectivity for SGLT2 over SGLT1 (canagliflozin has the lowest selectivity ratio ~250×, contributing to GI side effects via intestinal SGLT1 inhibition).

## Function

**Normal renal glucose handling:**
- Glomerular filtration: ~180 g glucose/day at euglycemia (GFR 180 L/day × plasma glucose ~1 g/L)
- SGLT2 (S1): reabsorbs ~90% (~162 g/day) via Na⁺ cotransport
- SGLT1 (S3): reabsorbs remaining ~10% (~18 g/day)
- Net: virtually zero urinary glucose under normal conditions

**SGLT2 inhibitor pharmacodynamics:**
- Block SGLT2 → glucosuria of ~70–90 g/day at euglycemia → ~300 kcal/day caloric loss → modest weight reduction (~2–3 kg) and HbA1c lowering (~0.7–1.0%)
- Urinary glucose excretion is **glucose-concentration-dependent**: the more hyperglycemic, the greater the glucosuria — inherently self-limiting at low glucose levels → **minimal hypoglycemia risk** (unlike sulfonylureas or insulin)
- The maximum urinary glucose excretion (~90 g/day) occurs when SGLT1 also becomes rate-limiting

**Downstream hemodynamic effects:**
- **Osmotic diuresis:** Glucosuria → water follows osmotically → ~500–1000 mL/day natriuresis/diuresis → reduced plasma volume, reduced preload, reduced ventricular filling pressures
- **Natriuresis:** Proximal tubule Na⁺ cotransport with glucose is inhibited → more distal Na⁺ delivery → modest natriuresis (enhanced by blocked proximal Na⁺-H⁺ exchanger activity)

## Mechanism

**Six cardiorenal mechanisms of SGLT2 inhibitors:**

1. **Tubuloglomerular feedback (TGF) restoration:**
   - Diabetic hyperfiltration → elevated single-nephron GFR → glomerular capillary hypertension → podocyte injury → progressive nephron loss
   - SGLT2 inhibition → reduced proximal Na⁺/glucose reabsorption → increased distal delivery to macula densa → afferent arteriole vasoconstriction (TGF signal) → reduced intraglomerular pressure → nephroprotection
   - This is the dominant mechanism of CKD progression reduction — independent of glucose control

2. **Volume/preload reduction:**
   - Glucosuria + natriuresis → ~3–5% plasma volume reduction → reduced cardiac filling pressures → reduced pulmonary congestion in HF
   - Distinct from loop diuretics: SGLT2i cause sustained hemodynamic relief without reflex RAAS activation

3. **Metabolic fuel shift (ketone body hypothesis):**
   - Caloric loss (glucosuria) + insulin reduction → hepatic ketogenesis → mild elevation of β-hydroxybutyrate (β-OHB, ~0.3–0.5 mM vs normal <0.1 mM)
   - β-OHB is a more oxygen-efficient cardiac fuel than glucose or fatty acids (generates more ATP per O₂ consumed) → improved myocardial energetics in the energy-starved failing heart

4. **NLRP3 inflammasome inhibition:**
   - β-OHB directly inhibits NLRP3 by preventing ASC oligomerization → ↓IL-1β, ↓IL-18 production
   - SGLT2 inhibition in renal tubular cells reduces oxidative stress → reduced NLRP3 priming
   - Contributes to anti-fibrotic effect in both kidney and heart

5. **TGF-β/fibrosis suppression:**
   - SGLT2i reduce TGF-β1 signaling in tubular cells and glomerular mesangial cells → ↓fibronectin, ↓collagen IV deposition → slowed interstitial fibrosis
   - Mechanism partly via reduced oxidative stress (NADPH oxidase) and reduced angiotensin II signaling

6. **Hematocrit increase / erythropoiesis:**
   - SGLT2i consistently raise hematocrit 1–3% via volume contraction AND increased erythropoietin secretion
   - Improved O₂-carrying capacity → may contribute to improved exercise tolerance and reduced cardiac workload

**Clinical trial evidence summary:**

| Trial | Drug | Population | Primary endpoint | HR (95% CI) |
|---|---|---|---|---|
| EMPA-REG OUTCOME | Empagliflozin | T2D + CVD | 3-P MACE | 0.86 (0.74–0.99) |
| CANVAS | Canagliflozin | T2D + high CV risk | 3-P MACE | 0.86 (0.75–0.97) |
| DAPA-HF | Dapagliflozin | HFrEF (T2D + non-T2D) | Worsening HF + CV death | 0.74 (0.65–0.85) |
| EMPEROR-Reduced | Empagliflozin | HFrEF | Worsening HF + CV death | 0.75 (0.65–0.86) |
| CREDENCE | Canagliflozin | T2D + CKD (eGFR 30–90) | Composite kidney endpoint | 0.70 (0.59–0.82) |
| DAPA-CKD | Dapagliflozin | CKD stages 2–4 (T2D + non-T2D) | Composite kidney endpoint | 0.61 (0.51–0.72) |

**Key adverse effects:**
- **Genital mycotic infections** (5–10% women, 2–4% men) — most common; due to glucosuria providing substrate for Candida; manageable with antifungals
- **UTI:** Modest increase; glucosuria can promote bacteriuria
- **Volume depletion/hypotension:** Elderly, diuretic users; rarely symptomatic
- **Euglycemic DKA:** Rare but serious; occurs during fasting, surgery, illness; serum glucose may be normal; check ketones
- **Canagliflozin-specific:** Lower extremity amputations (HR 1.97, CANVAS); fracture risk — class effect vs. canagliflozin-specific debated; mechanism possibly RANKL/PTH effects
- **SGLT2i contraindicated** in eGFR <20–30 mL/min (glycemic efficacy reduced; approved for renal/HF indications at lower eGFR for some agents)

## Connections

EMPA-REG OUTCOME (empagliflozin, T2D + CVD): 14% MACE reduction, 35% CV death reduction, 35% HHF reduction; SGLT2 inhibitors reduce HbA1c ~0.7-1.0% with glucose-dependent mechanism avoiding hypoglycemia; first-line therapy in T2D with established ASCVD or heart failure.

DAPA-HF (dapagliflozin, HFrEF): 25% reduction in worsening HF + CV death in T2D and non-T2D; EMPEROR-Reduced (empagliflozin): 25% reduction; SGLT2 inhibitors are the fourth pillar of GDMT, reducing HHF and CV death independent of diabetes status.

CREDENCE (canagliflozin): 30% reduction in kidney endpoint in T2D + CKD; DAPA-CKD (dapagliflozin): 39% reduction in eGFR decline/dialysis/renal death in CKD with and without T2D; SGLT2 inhibitors slow CKD progression via tubuloglomerular feedback and anti-fibrotic effects.

SGLT2 inhibitors reduce NLRP3 inflammasome activation in renal tubular cells and macrophages, decreasing IL-1β and IL-18 production; this anti-inflammatory mechanism contributes to cardiorenal protection beyond glucose lowering in diabetic kidney disease.

[^zinman-2015-empa-reg]: Zinman B, Wanner C, Lachin JM, et al. Empagliflozin, cardiovascular outcomes, and mortality in type 2 diabetes. *N Engl J Med.* 2015;373(22):2117-2128. [doi:10.1056/NEJMoa1504720](https://doi.org/10.1056/NEJMoa1504720) · [PubMed 26378978](https://pubmed.ncbi.nlm.nih.gov/26378978/)
[^mcmurray-2019-dapa-hf]: McMurray JJV, Solomon SD, Inzucchi SE, et al. Dapagliflozin in patients with heart failure and reduced ejection fraction. *N Engl J Med.* 2019;381(21):1995-2008. [doi:10.1056/NEJMoa1911303](https://doi.org/10.1056/NEJMoa1911303) · [PubMed 31535829](https://pubmed.ncbi.nlm.nih.gov/31535829/)
