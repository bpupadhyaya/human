---
schema: medicine-entry/v1
id: ace-inhibitors
name: ACE inhibitors
atlas: 03-medicine
scale: 01-modern
status: draft
last_reviewed: 2026-06-03
summary: "Angiotensin-converting enzyme inhibitors — competitive ACE inhibitors preventing angiotensin I→II conversion and potentiating bradykinin. First-line for HFrEF (CONSENSUS 1987, SOLVD 1991), hypertension, diabetic nephropathy, and post-MI. Reduce mortality in HFrEF ~27%."
aliases: ["ACE inhibitors", "ACEi", "angiotensin-converting enzyme inhibitors", "captopril", "enalapril", "lisinopril", "ramipril"]
sources:
  - id: consensus-1987
    type: peer-reviewed
    cite: "CONSENSUS Trial Study Group. Effects of enalapril on mortality in severe congestive heart failure. N Engl J Med. 1987;316(23):1429-35."
    doi: "10.1056/NEJM198706043162301"
    pmid: "2883575"
    url: "https://doi.org/10.1056/NEJM198706043162301"
  - id: solvd-1991
    type: peer-reviewed
    cite: "The SOLVD Investigators. Effect of enalapril on survival in patients with reduced left ventricular ejection fractions and congestive heart failure. N Engl J Med. 1991;325(5):293-302."
    doi: "10.1056/NEJM199108013250501"
    pmid: "2057034"
    url: "https://doi.org/10.1056/NEJM199108013250501"
  - id: save-1992
    type: peer-reviewed
    cite: "Pfeffer MA, Braunwald E, Moye LA, et al. Effect of captopril on mortality and morbidity in patients with left ventricular dysfunction after myocardial infarction. N Engl J Med. 1992;327(10):669-77."
    doi: "10.1056/NEJM199209033271001"
    pmid: "1386652"
    url: "https://doi.org/10.1056/NEJM199209033271001"
  - id: hope-2000
    type: peer-reviewed
    cite: "Yusuf S, Sleight P, Pogue J, et al. Effects of an angiotensin-converting-enzyme inhibitor, ramipril, on cardiovascular events in high-risk patients. N Engl J Med. 2000;342(3):145-53."
    doi: "10.1056/NEJM200001203420301"
    pmid: "10639539"
    url: "https://doi.org/10.1056/NEJM200001203420301"
  - id: heidenreich-2022-hf-guideline
    type: clinical-guideline
    cite: "Heidenreich PA, Bozkurt B, Aguilar D, et al. 2022 AHA/ACC/HFSA Guideline for the Management of Heart Failure. Circulation. 2022;145(18):e895-e1032."
    doi: "10.1161/CIR.0000000000001063"
    pmid: "35363499"
    url: "https://doi.org/10.1161/CIR.0000000000001063"
cross_links:
  - target: 01-human/07-system/cardiovascular-system
    relation: acts-on
    note: "ACE inhibitors reduce systemic vascular resistance (lower afterload), reduce aldosterone-mediated salt/water retention (lower preload), and interrupt RAAS-driven adverse cardiac remodelling — system-level benefits in HFrEF and hypertension."
  - target: 01-human/06-organ/heart
    relation: acts-on
    note: "ACE inhibitors reverse adverse ventricular remodelling in HFrEF: reduce LV end-diastolic and end-systolic volumes, prevent progressive LV dilation, and improve ejection fraction over months of therapy."
  - target: 01-human/06-organ/kidney
    relation: treats
    note: "ACE inhibitors reduce intraglomerular hypertension via efferent arteriolar dilation, decrease proteinuria by 30–50%, and slow CKD progression in diabetic and non-diabetic proteinuric nephropathy — independent of blood pressure lowering."
  - target: 01-human/07-system/renal-system
    relation: treats
    note: "RAAS blockade with ACE inhibitors is first-line for proteinuric CKD (any cause): reduces ESRD incidence by ~30% in diabetic nephropathy (RENAAL, IDNT trials) and slows GFR decline in IgA nephropathy."
---

# ACE inhibitors

## Overview

ACE inhibitors (angiotensin-converting enzyme inhibitors) are a class of drugs that competitively inhibit **ACE (kininase II, EC 3.4.15.1)**, the enzyme responsible for converting the inactive decapeptide **angiotensin I** into the potent vasoconstrictor **angiotensin II** in the renin-angiotensin-aldosterone system (RAAS). ACE also degrades **bradykinin** — a vasodilatory peptide — so ACE inhibition potentiates bradykinin effects, producing additional vasodilation (and the characteristic dry cough side effect via bradykinin-stimulated pulmonary C-fibres) [^consensus-1987].

ACE inhibitors are among the most impactful drug classes in the history of cardiovascular medicine. Their landmark trials — beginning with CONSENSUS (1987) and SOLVD (1991) — established that RAAS blockade reduces **all-cause mortality in HFrEF** and transformed heart failure therapy. They are now first-line therapy for:

- **Heart failure with reduced ejection fraction (HFrEF)**
- **Hypertension** (particularly with concurrent CKD, diabetes, or HF)
- **Diabetic nephropathy** (reduce proteinuria and slow CKD progression)
- **Post-myocardial infarction** (especially with LV dysfunction, LVEF <40%)
- **High cardiovascular risk** (secondary prevention — HOPE trial)

## Mechanism

### RAAS Pathway and ACE Inhibition

The RAAS cascade:

```
Angiotensinogen (liver) → Renin (JG cells, kidney) → Angiotensin I (10 aa)
                                                         ↓ ACE (lung, endothelium)
                                                     Angiotensin II (8 aa)
                                                         ↓
                          AT1 receptor → vasoconstriction, aldosterone release, 
                                          norepinephrine release, fibrosis
```

ACE inhibitors (e.g., enalaprilat, the active form of enalapril) bind the **zinc-containing active site** of ACE with high affinity, blocking angiotensin I cleavage. This produces:

1. **↓Angiotensin II** → less AT1 receptor stimulation → arterial and venous vasodilation (↓afterload, ↓preload) → ↓cardiac work
2. **↓Aldosterone** → less renal Na⁺/H₂O retention → ↓blood volume → ↓preload; renal potassium retention (risk of hyperkalaemia)
3. **↑Bradykinin** → bradykinin-mediated vasodilation (eNOS activation → NO → vasodilation); also responsible for the bradykinin-mediated cough (25–40%) and rare angioedema (<0.5%)
4. **Anti-fibrotic effects:** Angiotensin II drives cardiac fibroblast activation, myocardial fibrosis, and ventricular remodelling. ACE inhibition reverses these processes over weeks-to-months → **reverse remodelling** in HFrEF

### Haemodynamic Effects

| Effect | Mechanism | Clinical relevance |
|:---|:---|:---|
| ↓Afterload | Arteriolar dilation (↓Ang II) | Reduces cardiac work → allows ventricular function to improve at same energy cost |
| ↓Preload | Venodilation + ↓aldosterone | Reduces filling pressures; reduces pulmonary congestion |
| ↑Cardiac output | Both ↓afterload and ↓preload | Net effect in HFrEF: CO increases despite ↓BP |
| ↑Renal blood flow | ↓efferent arteriolar tone (Ang II predominantly constricts efferent) | Usually beneficial; may reduce GFR in bilateral renal artery stenosis (risk) |

## Clinical Use

### Indications

| Indication | Evidence | Key agents |
|:---|:---|:---|
| **HFrEF (EF <40%)** | Class I, Level A [^heidenreich-2022-hf-guideline] | Enalapril, lisinopril, ramipril, captopril |
| **Hypertension** | Class I; first-line with CKD/DM/HF | Any ACEi |
| **Post-MI with LV dysfunction** | Class I | Captopril (SAVE), ramipril (AIRE) |
| **Diabetic nephropathy (T1DM with proteinuria)** | Class I | Any ACEi |
| **High CV risk without HF** | Class IIa | Ramipril (HOPE); perindopril (EUROPA) |

### Key Agents

| Drug | Prodrug? | Key pharmacology |
|:---|:---:|:---|
| **Captopril** | No (active) | Oldest ACEi; thiol group (SH) → different side-effect profile; 3× daily |
| **Enalapril** | Yes (enalaprilat) | The SOLVD/CONSENSUS drug; twice daily |
| **Lisinopril** | No | Once daily; renal excretion; not lipophilic |
| **Ramipril** | Yes (ramiprilat) | HOPE trial; high-potency; once daily |
| **Perindopril** | Yes | Long-acting; EUROPA trial |

### Dosing Principle

ACE inhibitors must be **titrated to target dose** in HFrEF — the same doses proven to reduce mortality in trials. Starting at low dose (e.g., enalapril 2.5 mg BD) and doubling every 2 weeks to target (e.g., enalapril 10 mg BD) is standard. The mortality benefit is dose-dependent and under-dosing is a common clinical error [^heidenreich-2022-hf-guideline].

### Contraindications

- **Bilateral renal artery stenosis / severe aortic stenosis** — may precipitate acute renal failure
- **Pregnancy** (Category D) — fetal ACE II is essential for kidney development; ACEi causes oligohydramnios, renal tubular dysplasia, skull hypoplasia ("ACE inhibitor fetopathy")
- **Hyperkalaemia** (K⁺ >5.5 mmol/L) — significant risk, especially with concomitant MRA/ARB
- **Known angioedema** from prior ACEi — switch to ARB (slightly lower angioedema risk, but not zero)
- **Severe hypotension** (SBP <90 mmHg at initiation)

## Evidence

### Landmark Randomised Controlled Trials

| Trial | Drug | Population | Key result |
|:---|:---|:---|:---|
| **CONSENSUS (1987)** | Enalapril | 253 patients, NYHA IV HFrEF | **40% reduction in 6-month mortality** vs placebo; trial stopped early [^consensus-1987] |
| **SOLVD (1991)** | Enalapril | 2,569 patients, LVEF ≤35%, symptomatic HFrEF | **16% reduction in all-cause mortality; 26% reduction in hospitalisations** [^solvd-1991] |
| **SAVE (1992)** | Captopril | 2,231 post-MI patients, LVEF ≤40% | **19% reduction in all-cause mortality; 25% reduction in HF hospitalisation** [^save-1992] |
| **HOPE (2000)** | Ramipril | 9,297 high-risk patients (no HF, no known LV dysfunction) | **22% reduction in composite CV death, MI, stroke** vs placebo [^hope-2000] |

The convergence of multiple large trials with different agents, populations, and endpoints across three decades established ACE inhibitors as a cornerstone of cardiovascular prevention and treatment.

### ACEi vs ARB vs ARNI

In HFrEF:
- **ARBs** (e.g., valsartan, candesartan): Non-inferior to ACEi in most trials; preferred when ACEi cough is intolerable; lower angioedema risk
- **ARNI (sacubitril/valsartan):** Superior to enalapril in PARADIGM-HF (20% further reduction in CV death/HF hospitalisation) — now preferred over ACEi alone in HFrEF; ACEi must be stopped 36 h before starting ARNI to avoid angioedema

## Connections

- **Acts on** → [Cardiovascular system](../../../../01-human/07-system/cardiovascular-system/README.md): ACE inhibitors reduce SVR, blood pressure, aldosterone-mediated volume, and RAAS-driven adverse remodelling — affecting the entire cardiovascular system at the system level.
- **Acts on** → [Heart](../../../../01-human/06-organ/heart/README.md): At the organ level, ACE inhibitors reduce LV volumes (reverse remodelling), improve ejection fraction, and reduce the heart's long-term structural deterioration in HFrEF.

[^consensus-1987]: CONSENSUS Trial Study Group. Effects of enalapril on mortality in severe congestive heart failure. *N Engl J Med.* 1987;316(23):1429-35. [doi:10.1056/NEJM198706043162301](https://doi.org/10.1056/NEJM198706043162301) · [PubMed 2883575](https://pubmed.ncbi.nlm.nih.gov/2883575/)
[^solvd-1991]: The SOLVD Investigators. Effect of enalapril on survival in patients with reduced left ventricular ejection fractions and congestive heart failure. *N Engl J Med.* 1991;325(5):293-302. [doi:10.1056/NEJM199108013250501](https://doi.org/10.1056/NEJM199108013250501) · [PubMed 2057034](https://pubmed.ncbi.nlm.nih.gov/2057034/)
[^save-1992]: Pfeffer MA, Braunwald E, Moye LA, et al. Effect of captopril on mortality and morbidity in patients with left ventricular dysfunction after myocardial infarction. *N Engl J Med.* 1992;327(10):669-77. [doi:10.1056/NEJM199209033271001](https://doi.org/10.1056/NEJM199209033271001) · [PubMed 1386652](https://pubmed.ncbi.nlm.nih.gov/1386652/)
[^hope-2000]: Yusuf S, Sleight P, Pogue J, et al. Effects of an angiotensin-converting-enzyme inhibitor, ramipril, on cardiovascular events in high-risk patients. *N Engl J Med.* 2000;342(3):145-53. [doi:10.1056/NEJM200001203420301](https://doi.org/10.1056/NEJM200001203420301) · [PubMed 10639539](https://pubmed.ncbi.nlm.nih.gov/10639539/)
[^heidenreich-2022-hf-guideline]: Heidenreich PA, Bozkurt B, Aguilar D, et al. 2022 AHA/ACC/HFSA Guideline for the Management of Heart Failure. *Circulation.* 2022;145(18):e895–e1032. [doi:10.1161/CIR.0000000000001063](https://doi.org/10.1161/CIR.0000000000001063) · [PubMed 35363499](https://pubmed.ncbi.nlm.nih.gov/35363499/)
