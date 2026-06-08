---
schema: human-scale-entry/v1
id: bnp
name: BNP
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "BNP is a ventricular peptide hormone that activates NPR-A → cGMP → natriuresis and vasodilation, counteracting RAAS in heart failure; plasma BNP/NT-proBNP are gold-standard HF biomarkers; sacubitril inhibits neprilysin → raises natriuretic peptides → reduces HFrEF mortality."
aliases: ["BNP", "NPPB", "B-type natriuretic peptide", "brain natriuretic peptide", "NT-proBNP", "natriuretic peptide", "ANP", "NPPA", "neprilysin", "sacubitril", "ARNI"]
cross_links:
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "BNP is released by ventricular myocytes under wall stress → NPR-A → cGMP → natriuresis and vasodilation; BNP/NT-proBNP diagnose and prognosticate HF; sacubitril (neprilysin inhibitor in ARNI) raises ANP/BNP → PARADIGM-HF: 20% RRR vs. ACE-I in HFrEF."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "BNP binds NPR-A (particulate guanylyl cyclase) → cGMP → PKG → vasodilation, converging with eNOS-derived NO/cGMP; both pathways relax vascular smooth muscle; neprilysin inhibition raises BNP, amplifying the shared cGMP pool in the vasculature."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "NT-proBNP is renally cleared → elevated in CKD regardless of HF; BNP is less GFR-dependent; elevated natriuretic peptides in CKD reflect cardiorenal syndrome; age-adjusted NT-proBNP thresholds (>900 pg/mL for HF) apply in impaired renal function."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "ANP/BNP directly suppress aldosterone secretion from adrenal zona glomerulosa and reduce renin release → counteract RAAS-driven sodium retention in HF; MRA and ARNI act on complementary pathways to reduce cardiorenal fluid overload."
sources:
  - id: maisel-2002-bnp-diagnosis
    type: peer-reviewed
    cite: "Maisel AS, Krishnaswamy P, Nowak RM, et al. Rapid measurement of B-type natriuretic peptide in the emergency diagnosis of heart failure. N Engl J Med. 2002;347(3):161-167."
    doi: "10.1056/NEJMoa020233"
    pmid: "12124404"
    url: "https://doi.org/10.1056/NEJMoa020233"
  - id: mcmurray-2014-paradigm-hf
    type: peer-reviewed
    cite: "McMurray JJV, Packer M, Desai AS, et al. Angiotensin-neprilysin inhibition versus enalapril in heart failure. N Engl J Med. 2014;371(11):993-1004."
    doi: "10.1056/NEJMoa1409077"
    pmid: "25176015"
    url: "https://doi.org/10.1056/NEJMoa1409077"
---

# BNP

## Overview

**BNP** (B-type natriuretic peptide; gene *NPPB*, chromosome 1p36.22) is a **cardiac hormone** produced predominantly by **ventricular myocytes** in response to increased wall stress and volume overload. Together with ANP (atrial natriuretic peptide; *NPPA*), BNP forms the natriuretic peptide axis — the heart's intrinsic counter-regulatory system opposing the renin-angiotensin-aldosterone system (RAAS) and sympathetic nervous system in heart failure.

Circulating BNP and its inactive co-secreted fragment **NT-proBNP** are the **gold-standard biomarkers for heart failure** diagnosis, prognosis, and therapy monitoring, with a negative predictive value >95% for ruling out HF when levels are below threshold [^maisel-2002-bnp-diagnosis]. The **PARADIGM-HF trial** demonstrated that sacubitril-valsartan (ARNI), by inhibiting neprilysin (the primary natriuretic peptide-degrading enzyme), reduces cardiovascular death and HF hospitalization by 20% compared to enalapril in HFrEF [^mcmurray-2014-paradigm-hf].

The natriuretic peptide family includes three members:
- **ANP (NPPA):** Primarily secreted by atrial myocytes; responds to atrial stretch; shorter half-life (~2 min) than BNP
- **BNP (NPPB):** Secreted mainly by ventricular myocytes; responds to ventricular wall stress; half-life ~20 min; preferred acute biomarker
- **CNP (NPPC):** Produced by vascular endothelium and brain; acts locally via NPR-B; vasodilatory but not a cardiac biomarker

**Clinical thresholds:**

| Peptide | Rule-out HF | Likely HF | Notes |
|---|---|---|---|
| BNP | <100 pg/mL | >400 pg/mL | Less affected by renal function; preferred in AKI/CKD |
| NT-proBNP | <300 pg/mL (acute) | >900 pg/mL (any age, acute) | Renally cleared; age-adjusted for chronic HF: >125 (<75y), >450 (≥75y) |

**Obesity paradox:** BNP/NT-proBNP are paradoxically low in obese patients despite high HF prevalence — adipose tissue expresses NPR-C (clearance receptor), acting as a BNP "sink," and has reduced NPR-A expression. Obesity lowers natriuretic peptide levels by ~50% → lower diagnostic sensitivity of standard thresholds in obese individuals.

## Structure

BNP is synthesized as a **134-amino acid prepro-BNP** → signal peptide cleavage → **proBNP-108** (stored in secretory granules) → enzymatic cleavage by **furin** and **corin** at the proBNP ring junction → two co-secreted fragments:

**BNP-32 (active peptide):**
- 32 amino acids; 17-amino-acid ring formed by a disulfide bond between Cys10 and Cys26
- The ring is essential for NPR-A binding (linear analogs have reduced activity)
- Half-life: ~20 minutes; cleared by NPR-C internalization and **neprilysin** (neutral endopeptidase, NEP/MME) degradation
- Neprilysin also degrades ANP, bradykinin, substance P, angiotensin II, and adrenomedullin

**NT-proBNP (inactive N-terminal fragment):**
- 76 amino acids; no disulfide bond; biologically inert
- Half-life: ~60–120 minutes (longer than BNP); primarily renally cleared
- More stable for laboratory measurement; preferred in outpatient and chronic HF monitoring
- Rises ~6–12 hours before BNP in acute decompensation (larger pool)

**Receptor biology:**
- **NPR-A (natriuretic peptide receptor-A):** ANP and BNP receptor; transmembrane guanylyl cyclase → cGMP ↑ → PKG activation
- **NPR-B:** CNP-specific receptor; primarily vascular and skeletal tissue
- **NPR-C (clearance receptor):** Binds all natriuretic peptides; no cGMP signaling; receptor-mediated internalization → degradation; acts as a buffer limiting peptide levels

## Function

**Renal effects (natriuresis):**
- NPR-A → cGMP → PKG → phosphodiesterase 3 inhibition → afferent arteriole dilation + efferent arteriole constriction → increased GFR
- Inhibits ENaC (epithelial Na+ channel) in the collecting duct → reduced Na+ reabsorption → natriuresis and diuresis
- Suppresses renin secretion from juxtaglomerular cells → reduces angiotensin II and aldosterone
- Direct aldosterone suppression from adrenal zona glomerulosa via NPR-A → cGMP

**Vascular effects (vasodilation):**
- PKG → myosin light chain phosphatase activation → vascular smooth muscle relaxation → vasodilation
- Reduces preload (venodilatation) and afterload (arterial vasodilation) → reduced cardiac wall stress
- Inhibits vascular smooth muscle proliferation and migration → anti-hypertrophic

**Cardiac effects (anti-fibrotic/anti-hypertrophic):**
- PKG → phosphodiesterase 5 regulation → reduces TGF-β-driven collagen synthesis in cardiac fibroblasts
- Suppresses endothelin-1 secretion from endothelium → reduced cardiac hypertrophy
- Inhibits aldosterone-mediated cardiac fibrosis (complementary to MRA therapy)

**Central nervous system effects:**
- Reduces sympathetic outflow from the CNS
- Antagonizes the thirst and vasopressin secretion driven by volume depletion and angiotensin II

## Mechanism

**Neprilysin and ARNI therapy:**

Neprilysin (NEP; gene *MME*, chromosome 3q25.2) is a **zinc metallopeptidase** on the luminal surface of endothelial cells, renal tubular cells, and cardiac fibroblasts. It is the dominant enzyme degrading ANP and BNP:

1. BNP secretion ↑ (ventricular wall stress, β-adrenergic stimulation, angiotensin II)
2. Neprilysin cleaves BNP at the ring → rapid inactivation
3. **Sacubitril** (prodrug) → sacubitrilat (active) → competitive neprilysin inhibitor
4. Reduced BNP degradation → BNP accumulates → greater NPR-A stimulation → enhanced natriuresis, vasodilation, anti-fibrosis
5. Combined with valsartan (ARB): blocks AT1 receptor → prevents angiotensin II-driven hypertension and fibrosis
6. PARADIGM-HF: sacubitril-valsartan vs. enalapril in HFrEF (EF ≤40%): **20% RRR** in CV death + HHF; NNT ~21 over 27 months; recommended as GDMT over ACE-I/ARB in all HFrEF patients who can tolerate it

**BNP vs. NT-proBNP in clinical monitoring:**
- BNP reflects real-time biology (shorter half-life) — preferred for acute decompensation and in-hospital titration
- NT-proBNP preferred for outpatient chronic HF monitoring (more stable, less influenced by short-term fluctuations)
- "BNP-guided therapy" (GUIDE-IT, PRIMA trials): targeting NT-proBNP <1000 pg/mL or BNP <250 pg/mL in chronic HF to guide GDMT intensification — evidence mixed but guideline-endorsed as management adjunct

**Natriuretic peptide biomarker interpretation pitfalls:**
- Low BNP/NT-proBNP does NOT exclude HFpEF (preserved EF) reliably — HFpEF patients have lower NP levels than HFrEF even at same filling pressures
- Elevated NPs in non-HF conditions: PE, AF, severe COPD, sepsis, critical illness, renal failure → always interpret in clinical context
- "Grey zone" (BNP 100–400 pg/mL): includes HF plus non-cardiac causes (RV failure, AF, renal failure); use echocardiography to confirm

## Connections

BNP is released by ventricular myocytes under wall stress → NPR-A → cGMP → natriuresis and vasodilation; BNP/NT-proBNP diagnose and prognosticate HF; sacubitril (neprilysin inhibitor in ARNI) raises ANP/BNP → PARADIGM-HF: 20% RRR vs. ACE-I in HFrEF.

BNP binds NPR-A (particulate guanylyl cyclase) → cGMP → PKG → vasodilation, converging with eNOS-derived NO/cGMP; both pathways relax vascular smooth muscle; neprilysin inhibition raises BNP, amplifying the shared cGMP pool in the vasculature.

NT-proBNP is renally cleared → elevated in CKD regardless of HF; BNP is less GFR-dependent; elevated natriuretic peptides in CKD reflect cardiorenal syndrome; age-adjusted NT-proBNP thresholds (>900 pg/mL for HF) apply in impaired renal function.

ANP/BNP directly suppress aldosterone secretion from adrenal zona glomerulosa and reduce renin release → counteract RAAS-driven sodium retention in HF; MRA and ARNI act on complementary pathways to reduce cardiorenal fluid overload.

[^maisel-2002-bnp-diagnosis]: Maisel AS, Krishnaswamy P, Nowak RM, et al. Rapid measurement of B-type natriuretic peptide in the emergency diagnosis of heart failure. *N Engl J Med.* 2002;347(3):161-167. [doi:10.1056/NEJMoa020233](https://doi.org/10.1056/NEJMoa020233) · [PubMed 12124404](https://pubmed.ncbi.nlm.nih.gov/12124404/)
[^mcmurray-2014-paradigm-hf]: McMurray JJV, Packer M, Desai AS, et al. Angiotensin-neprilysin inhibition versus enalapril in heart failure. *N Engl J Med.* 2014;371(11):993-1004. [doi:10.1056/NEJMoa1409077](https://doi.org/10.1056/NEJMoa1409077) · [PubMed 25176015](https://pubmed.ncbi.nlm.nih.gov/25176015/)
