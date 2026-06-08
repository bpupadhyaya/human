---
schema: human-scale-entry/v1
id: heart-failure
name: Heart Failure
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Syndrome of impaired cardiac output inadequate for tissue metabolic demands. HFrEF (EF<40%), HFmrEF (40-49%), HFpEF (≥50%). ~64 million affected. GDMT: ACE-I/ARBs, beta-blockers, MRA, SGLT2i, ARNI (sacubitril-valsartan)."
aliases: ["heart failure", "HF", "congestive heart failure", "CHF", "HFrEF", "HFpEF", "cardiac failure"]
sources:
  - id: mcmurray-2014-paradigm-hf
    type: peer-reviewed
    cite: "McMurray JJV, Packer M, Desai AS, et al. Angiotensin-neprilysin inhibition versus enalapril in heart failure. N Engl J Med. 2014;371(11):993-1004."
    doi: "10.1056/NEJMoa1409077"
    pmid: "25176015"
    url: "https://doi.org/10.1056/NEJMoa1409077"
  - id: ponikowski-2016-esc-hf
    type: peer-reviewed
    cite: "Ponikowski P, Voors AA, Anker SD, et al. 2016 ESC Guidelines for the diagnosis and treatment of acute and chronic heart failure. Eur Heart J. 2016;37(27):2129-2200."
    doi: "10.1093/eurheartj/ehw128"
    pmid: "27206819"
    url: "https://doi.org/10.1093/eurheartj/ehw128"
cross_links:
  - target: 01-human/06-organ/heart
    relation: part-of
    note: "Heart failure is the systemic manifestation of impaired cardiac pump function; the heart is the primary failing organ, with downstream consequences affecting lungs, kidneys, liver, and skeletal muscle."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: modulated-by
    note: "Angiotensin II is a central driver of heart failure progression: causes vasoconstriction (increased afterload), aldosterone-mediated sodium retention (volume overload), direct cardiac myocyte hypertrophy, and cardiac fibrosis via TGF-β induction."
  - target: 01-human/03-molecular/aldosterone
    relation: modulated-by
    note: "Aldosterone promotes sodium and water retention, myocardial fibrosis (collagen I deposition in cardiac interstitium), and potassium/magnesium depletion; MRA (spironolactone/eplerenone) blockade reduces mortality in HFrEF."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: contains
    note: "Cardiomyocytes are the primary failing cells in heart failure: adaptive hypertrophy, calcium handling dysfunction (reduced SERCA2a, elevated diastolic Ca2+), sarcomeric disarray, mitochondrial dysfunction, and ultimately apoptosis drive the progression to heart failure."
  - target: 01-human/03-molecular/pcsk9
    relation: connects-to
    note: "Elevated LDL-C from PCSK9 GOF mutations accelerates coronary atherosclerosis → MI → ischemic cardiomyopathy and heart failure; PCSK9 inhibitors reduce MI risk in high-risk CVD patients; PCSK9 may also have direct myocardial effects via apoE and apoB receptor pathways."
  - target: 01-human/03-molecular/sglt2
    relation: connects-to
    note: "DAPA-HF (dapagliflozin, HFrEF): 25% reduction in worsening HF + CV death in T2D and non-T2D; EMPEROR-Reduced (empagliflozin): 25% reduction; SGLT2 inhibitors are the fourth pillar of GDMT, reducing HHF and CV death independent of diabetes status."
  - target: 01-human/03-molecular/fgf23
    relation: connects-to
    note: "Elevated FGF23 in CKD activates cardiac FGFR4 independent of αKlotho → HDAC4 nuclear translocation → cardiac hypertrophic gene program → LVH and HF; FGF23 is an independent predictor of incident heart failure and cardiovascular death in CKD and the general population."
  - target: 01-human/03-molecular/bnp
    relation: connects-to
    note: "BNP is released by ventricular myocytes under wall stress → NPR-A → cGMP → natriuresis and vasodilation; BNP/NT-proBNP diagnose and prognosticate HF; sacubitril (neprilysin inhibitor in ARNI) raises ANP/BNP → PARADIGM-HF: 20% RRR vs. ACE-I in HFrEF."
---

# Heart Failure

## Overview

Heart failure (HF) is a **clinical syndrome** in which the heart cannot pump sufficient blood to meet the body's metabolic demands, or can only do so at the cost of elevated filling pressures. It represents the final common pathway of most cardiac diseases and is a major global health burden: approximately **64 million people** worldwide live with HF, with a 5-year mortality (~50%) comparable to many malignancies [^ponikowski-2016-esc-hf].

HF is classified by **left ventricular ejection fraction (LVEF)**:
- **HFrEF** (Heart Failure with Reduced EF, EF <40%): "systolic" heart failure; cardiomyocyte loss and contractile dysfunction; GDMT most evidence-based here
- **HFmrEF** (Mildly Reduced EF, 40–49%): intermediate phenotype; overlapping features; GDMT may benefit
- **HFpEF** (Preserved EF, ≥50%): "diastolic" heart failure; impaired ventricular relaxation and compliance; major unmet treatment need (heterogeneous syndrome)

**Leading etiologies:**
- Ischemic heart disease (CAD, prior MI) — most common in developed world
- Hypertension — LVH → diastolic dysfunction → HFpEF; also causes HFrEF
- Dilated cardiomyopathy — idiopathic, familial (TTN mutations), viral, alcohol, chemotherapy (anthracyclines, trastuzumab)
- Valvular heart disease — mitral regurgitation (volume overload), aortic stenosis (pressure overload)
- Arrhythmias — tachycardia-induced cardiomyopathy

## Structure

### Cardiac Remodeling

The failing heart undergoes **maladaptive structural remodeling** driven by neurohumoral overactivation:

**Hypertrophy patterns:**
- **Concentric hypertrophy** (pressure overload — hypertension, AS): wall thickening with normal/reduced cavity, increased wall:cavity ratio; → diastolic dysfunction
- **Eccentric hypertrophy** (volume overload — MR, AI; post-MI): cavity dilation with proportional wall thinning; → systolic dysfunction; myocyte elongation (series sarcomere addition)

**Cellular changes in failing cardiomyocytes:**
- Calcium handling: ↓ SERCA2a expression/activity → impaired SR Ca²⁺ reuptake → elevated diastolic Ca²⁺ → impaired relaxation → diastolic dysfunction; depleted SR Ca²⁺ → reduced systolic Ca²⁺ transient → reduced contractility
- Sarcomeric changes: fetal gene program reactivation (β-MHC ↑, α-MHC ↓; ANP, BNP re-expression); reduced actomyosin ATPase activity → reduced contractile velocity
- Mitochondrial dysfunction: impaired fatty acid oxidation (primary fuel) → shift to glucose; reduced ATP production → energetic deficit
- Cardiomyocyte apoptosis: via mitochondrial (cytochrome c release → caspase-9) and death receptor (TNFR1 → caspase-8) pathways

**Extracellular matrix remodeling:**
- Cardiac fibrosis: aldosterone → cardiac fibroblast activation → collagen I/III deposition → increased passive stiffness → diastolic dysfunction; reduced electrical coupling → arrhythmia risk
- MMP/TIMP imbalance: early: MMP2/9 upregulation → collagen degradation → dilation; chronic: TIMP upregulation → fibrosis

### Neurohormonal Activation

The neurohormonal response to reduced CO is **initially compensatory but ultimately maladaptive**:

| System | Compensatory effect | Maladaptive effect |
|:---|:---|:---|
| **SNS** (norepinephrine) | ↑ HR, ↑ contractility, vasoconstriction | Tachyarrhythmias; cardiomyocyte toxicity; β-receptor downregulation; ↑ myocardial O₂ demand |
| **RAAS** (Ang II/aldosterone) | Na+ and water retention (volume) | Cardiac fibrosis; hypertrophy; vasoconstriction ↑ afterload; renal dysfunction |
| **ADH (vasopressin)** | Water retention | Hyponatremia; further volume overload |
| **BNP/ANP** | Natriuresis, vasodilation, anti-fibrotic (compensatory) | Progressively overwhelmed in severe HF; used as biomarker |

## Function

### Pathophysiology of Symptoms

HF symptoms arise from two fundamental abnormalities:

**Backward failure (congestion):**
- Left-sided: elevated left ventricular filling pressure → pulmonary venous hypertension → pulmonary capillary wedge pressure ↑ → pulmonary edema → dyspnea, orthopnea, PND
- Right-sided: elevated RV filling pressure → systemic venous hypertension → JVD, hepatomegaly, ascites, peripheral edema

**Forward failure (reduced output):**
- Reduced CO → poor peripheral perfusion → fatigue, exercise intolerance, muscle wasting (cardiac cachexia), reduced renal perfusion → cardiorenal syndrome, prerenal azotemia

### Frank-Starling Mechanism (Blunted)

Normal hearts increase stroke volume with increasing preload (Starling curve). The failing heart has a **depressed, flattened Starling curve**: increases in preload yield minimal SV improvement but cause significant pulmonary and systemic congestion. This is the physiological basis for the therapeutic approach: reduce preload (diuretics, venodilators) and afterload (vasodilators, RAAS blockade) while supporting contractility.

### Exercise Physiology in HF

- Reduced peak VO₂ (maximal oxygen uptake) — primary determinant of functional capacity and prognosis in HF
- Blunted chronotropic response (reduced HR reserve) — beta-receptor downregulation; blunted SNS reserve
- Peripheral factors: skeletal muscle atrophy (sarcopenia), reduced capillary density, mitochondrial dysfunction → impaired O₂ extraction

## Connections

- `part-of` → **[Heart](../../06-organ/heart/README.md)** — heart failure is the systemic consequence of impaired cardiac pump function
- `modulated-by` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — drives vasoconstriction, volume expansion, cardiac fibrosis, and hypertrophy in HF; ACE-I/ARBs block this arm of GDMT
- `modulated-by` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — cardiac fibrosis, sodium retention, and potassium wasting; MRAs (spironolactone/eplerenone) reduce mortality in HFrEF
- `contains` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — the primary failing cell type; cardiomyocyte loss, hypertrophy, and calcium handling dysfunction are the central cellular mechanisms of HFrEF
- `connects-to` → **[PCSK9](../../03-molecular/pcsk9/README.md)** — elevated LDL-C from PCSK9 GOF mutations accelerates coronary atherosclerosis → MI → ischemic cardiomyopathy and heart failure; PCSK9 inhibitors reduce MI risk in high-risk CVD patients; PCSK9 may also have direct myocardial effects via apoE and apoB receptor pathways.
- `connects-to` → **[SGLT2](../../03-molecular/sglt2/README.md)** — DAPA-HF (dapagliflozin, HFrEF): 25% reduction in worsening HF + CV death in T2D and non-T2D; EMPEROR-Reduced (empagliflozin): 25% reduction; SGLT2 inhibitors are the fourth pillar of GDMT, reducing HHF and CV death independent of diabetes status.
- `connects-to` → **[FGF23](../../03-molecular/fgf23/README.md)** — elevated FGF23 in CKD activates cardiac FGFR4 independent of αKlotho → HDAC4 nuclear translocation → cardiac hypertrophic gene program → LVH and HF; FGF23 is an independent predictor of incident heart failure and cardiovascular death in CKD and the general population.
- `connects-to` → **[BNP](../../03-molecular/bnp/README.md)** — BNP is released by ventricular myocytes under wall stress → NPR-A → cGMP → natriuresis and vasodilation; BNP/NT-proBNP diagnose and prognosticate HF; sacubitril (neprilysin inhibitor in ARNI) raises ANP/BNP → PARADIGM-HF: 20% RRR vs. ACE-I in HFrEF.

## Pathology

### Guideline-Directed Medical Therapy (GDMT) for HFrEF

Four pillars of GDMT reduce mortality in HFrEF (each independently significant):

| Drug class | Example | Mortality benefit | Mechanism |
|:---|:---|:---|:---|
| **ACE-I/ARB** | Enalapril, Losartan | 16–23% RRR | RAAS blockade → reduced afterload, anti-fibrotic, anti-hypertrophic |
| **Beta-blocker** | Carvedilol, Metoprolol succinate, Bisoprolol | 34% RRR | Reduces SNS toxicity; anti-arrhythmic; allows β-receptor re-sensitization; reduces HR |
| **MRA** | Spironolactone, Eplerenone | 25–30% RRR | Aldosterone blockade → reduced cardiac fibrosis, K+/Mg2+ preservation, reduced arrhythmia |
| **ARNI** | Sacubitril-valsartan | 20% additional RRR vs. ACE-I | Neprilysin inhibition → BNP/ANP ↑ → natriuresis + vasodilation + anti-fibrotic; supersedes ACE-I in HFrEF [^mcmurray-2014-paradigm-hf] |
| **SGLT2 inhibitor** | Dapagliflozin, Empagliflozin | 25% RRR in DAPA-HF/EMPEROR-R | Volume reduction, RAAS modulation, anti-fibrotic, improved mitochondrial function; the fourth pillar |

### HFpEF: An Unmet Need

HFpEF (EF ≥50%) accounts for ~50% of all HF and has limited evidence-based therapy:
- **EMPEROR-Preserved (Empagliflozin)** and **DELIVER (Dapagliflozin)**: SGLT2i reduce HF hospitalizations in HFpEF — the first drug class with clear benefit
- Diuretics for symptom relief (decongestion); no mortality benefit demonstrated for any drug historically
- Pathophysiology: impaired myocardial relaxation, increased passive stiffness, inadequate cardiac reserve; multiple phenotypes (obesity-related, atrial fibrillation, CKD, hypertensive)

### Acute Decompensated Heart Failure (ADHF)

Acute presentation with acute-on-chronic or de novo severe congestion:
- IV diuretics (furosemide) — primary therapy for congestion relief
- Vasodilators (nitroglycerin, nesiritide) — if hypertensive
- Inotropes (dobutamine, milrinone) — for cardiogenic shock/severe low-output; bridge to advanced therapies
- Advanced HF: **LVADs** (left ventricular assist devices) as destination therapy or bridge-to-transplant; cardiac transplantation remains gold standard for refractory HF (limited by donor availability)

[^mcmurray-2014-paradigm-hf]: McMurray JJV et al. Angiotensin-neprilysin inhibition versus enalapril in heart failure. *N Engl J Med.* 2014;371(11):993-1004. [doi:10.1056/NEJMoa1409077](https://doi.org/10.1056/NEJMoa1409077) · [PubMed 25176015](https://pubmed.ncbi.nlm.nih.gov/25176015/)
[^ponikowski-2016-esc-hf]: Ponikowski P et al. 2016 ESC Guidelines for the diagnosis and treatment of acute and chronic heart failure. *Eur Heart J.* 2016;37(27):2129-2200. [doi:10.1093/eurheartj/ehw128](https://doi.org/10.1093/eurheartj/ehw128) · [PubMed 27206819](https://pubmed.ncbi.nlm.nih.gov/27206819/)
