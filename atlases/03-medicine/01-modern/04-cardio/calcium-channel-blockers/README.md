---
schema: medicine-entry/v1
id: calcium-channel-blockers
name: Calcium Channel Blockers
atlas: 03-medicine
scale: 01-modern
status: draft
last_reviewed: 2026-06-04
summary: "Block voltage-gated L-type calcium channels. Two subclasses: dihydropyridines (vasodilation-predominant; e.g. amlodipine) and non-dihydropyridines (cardiac rate/conduction; e.g. verapamil, diltiazem). First-line for hypertension and angina."
drug_class: calcium channel antagonist
modality: small molecule
key_agents: [amlodipine, nifedipine, diltiazem, verapamil, felodipine, nicardipine, clevidipine]
who_essential_medicine: false
atc: C08
aliases: ["CCB", "calcium antagonists", "calcium channel antagonists", "amlodipine", "nifedipine", "diltiazem", "verapamil"]
tags: [ccb, calcium-channel, hypertension, angina, dihydropyridine, verapamil, diltiazem, vasodilation]
sources:
  - id: allhat-2002
    type: peer-reviewed
    cite: "ALLHAT Officers and Coordinators for the ALLHAT Collaborative Research Group. Major outcomes in high-risk hypertensive patients randomized to angiotensin-converting enzyme inhibitor or calcium channel blocker vs diuretic. JAMA. 2002;288(23):2981-97."
    doi: "10.1001/jama.288.23.2981"
    url: "https://doi.org/10.1001/jama.288.23.2981"
  - id: camelot-2004
    type: peer-reviewed
    cite: "Nissen SE, Tuzcu EM, Libby P, et al. Effect of antihypertensive agents on cardiovascular events in patients with coronary disease and normal blood pressure: the CAMELOT study: a randomized controlled trial. N Engl J Med. 2004;350(23):2352-8."
    doi: "10.1056/NEJMoa042761"
    url: "https://doi.org/10.1056/NEJMoa042761"
  - id: staessen-2001
    type: peer-reviewed
    cite: "Staessen JA, Gasowski J, Wang JG, et al. Risks of untreated and treated isolated systolic hypertension in the elderly: meta-analysis of outcome trials. Lancet. 2000;355(9207):865-72."
    pmid: "11289345"
    url: "https://pubmed.ncbi.nlm.nih.gov/11289345/"
  - id: value-2004
    type: peer-reviewed
    cite: "Julius S, Kjeldsen SE, Weber M, et al. Outcomes in hypertensive patients at high cardiovascular risk treated with regimens based on valsartan or amlodipine: the VALUE randomised trial. Lancet. 2004;363(9426):2022-31."
    doi: "10.1016/S0140-6736(04)16451-9"
    pmid: "15207952"
    url: "https://doi.org/10.1016/S0140-6736(04)16451-9"
cross_links:
  - target: 01-human/07-system/cardiovascular-system
    relation: treats
    note: "CCBs are first-line antihypertensives and anti-anginal agents. DHP CCBs reduce SVR via vascular smooth muscle relaxation; non-DHP CCBs also reduce heart rate and AV conduction velocity, providing rate control in atrial fibrillation and treatment of PSVT."
  - target: 01-human/07-system/cardiovascular-system
    relation: modulates
    note: "L-type calcium channel blockade modulates vascular tone, cardiac contractility, SA node automaticity, and AV node conduction — differentially depending on subclass tissue selectivity."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: modulates
    note: "Modulates by Smooth Muscle Cell."
---

# Calcium Channel Blockers

## Overview

Calcium channel blockers (CCBs) are a diverse class of drugs that **block voltage-gated L-type calcium channels (Cav1.2)**, reducing calcium influx into vascular smooth muscle cells and cardiomyocytes. Calcium is the direct trigger for smooth muscle contraction and myocyte excitation-contraction coupling; blocking its entry produces vasodilation, reduced cardiac contractility, and — in the non-dihydropyridine subclass — slowed sinus and AV node conduction.

CCBs are among the most prescribed drug classes worldwide and are first-line agents for:

- **Hypertension** (particularly in older adults, Black patients, isolated systolic hypertension, and concurrent angina or Raynaud's)
- **Stable angina** and **vasospastic (Prinzmetal) angina**
- **Rate control in atrial fibrillation** (non-DHP CCBs: verapamil, diltiazem)
- **PSVT termination and prophylaxis** (verapamil IV)
- **Raynaud's phenomenon** (DHP CCBs)

Despite this clinical breadth, the two CCB subclasses — **dihydropyridines** and **non-dihydropyridines** — have substantially different pharmacological profiles, indications, and contraindications and should not be considered interchangeable.

## Mechanism

### L-type Calcium Channel Biology

Voltage-gated L-type channels open when membrane potential reaches approximately −40 mV (depolarisation). In different tissues, Ca²⁺ influx drives:

| Tissue | Channel subtype | Physiological role |
|:---|:---:|:---|
| Vascular smooth muscle | Cav1.2 | Contraction → vasoconstriction |
| Ventricular cardiomyocytes | Cav1.2 | Excitation-contraction coupling; contractility |
| SA node (pacemaker) | Cav1.3 + Cav1.2 | Spontaneous depolarisation phase 0/4 → heart rate |
| AV node | Cav1.2 | Slow conduction, refractory period → PR interval |

CCBs bind to the alpha-1 subunit of the L-type channel, stabilising it in the **inactivated state** and preventing calcium entry. They are **use-dependent** in electrically active tissue (more effect at faster rates), which underpins their efficacy in tachyarrhythmias.

### Subclass Differences: Tissue Selectivity

The defining pharmacological distinction between CCB subclasses is **tissue selectivity**:

#### 1. Dihydropyridines (DHPs)

Agents: amlodipine, nifedipine, felodipine, nicardipine, clevidipine, lercanidipine

- **Predominantly vascular smooth muscle selectivity** — binding site overlaps only weakly with the cardiac channel conformation during normal sinus rhythm
- Reduce **systemic vascular resistance (SVR)** → decrease blood pressure and afterload
- **Minimal direct cardiac effect** on contractility, HR, or AV conduction at therapeutic doses
- Reflex sympathetic activation (baroreceptor response to vasodilation) may cause **reflex tachycardia** — more pronounced with short-acting agents (nifedipine IR); attenuated with amlodipine due to its slow onset and long half-life
- **Amlodipine** (t½ 35–50 h): once-daily dosing; gradual vasodilation minimises reflex activation; most studied DHP in outcomes trials

#### 2. Non-Dihydropyridines (non-DHPs)

**Verapamil** (phenylalkylamine): Greatest cardiac selectivity; equipotent vascular and cardiac effects; negative chronotropy, dromotropy, and inotropy

**Diltiazem** (benzothiazepine): Intermediate selectivity; balanced cardiac and vascular effects; less negative inotropy than verapamil

Both non-DHPs:
- Slow **SA node automaticity** → ↓ heart rate (negative chronotropy)
- Slow **AV node conduction** → ↑ PR interval; rate control in AF; can terminate PSVT (AV nodal re-entry)
- Reduce **myocardial contractility** (negative inotropy) → avoid in HFrEF (decompensation risk)

### Haemodynamic Summary

```
DHP CCBs (amlodipine, nifedipine):
  SVR ↓↓  |  HR ↔ (or ↑ reflex)  |  Contractility ↔  |  AV conduction ↔

Non-DHP CCBs (verapamil):
  SVR ↓    |  HR ↓↓                |  Contractility ↓↓ |  AV conduction ↓↓

Non-DHP CCBs (diltiazem):
  SVR ↓    |  HR ↓↓                |  Contractility ↓   |  AV conduction ↓↓
```

## Clinical Use

### Indications

| Indication | Preferred subclass | Key agents |
|:---|:---:|:---|
| **Hypertension** | DHP | Amlodipine, felodipine, nifedipine XL |
| **Stable angina** | Both | DHP: amlodipine; non-DHP: diltiazem, verapamil |
| **Vasospastic (Prinzmetal) angina** | DHP (first choice) | Nifedipine, amlodipine |
| **Rate control in AF/AFL** | Non-DHP | Diltiazem, verapamil |
| **PSVT (AV nodal re-entry)** | Non-DHP | Verapamil IV, diltiazem IV |
| **Raynaud's phenomenon** | DHP | Nifedipine, amlodipine |
| **Subarachnoid haemorrhage vasospasm** | DHP | Nimodipine (CNS-selective) |
| **Hypertensive emergency** (IV) | DHP | Clevidipine, nicardipine IV |

### Key Agents

| Drug | Subclass | t½ | Notes |
|:---|:---:|:---:|:---|
| **Amlodipine** | DHP | 35–50 h | Once daily; no reflex tachycardia; most studied; first-line for hypertension and stable angina |
| **Nifedipine** | DHP | 2 h (IR) / 8–16 h (XL) | IR: rapid vasodilation, reflex tachycardia; use XL formulation only |
| **Felodipine** | DHP | 11–16 h | High vascular selectivity; CYP3A4 substrate (grapefruit interaction) |
| **Nicardipine** | DHP | 8 h | IV formulation available; used in hypertensive emergencies |
| **Clevidipine** | DHP | 1 min (IV) | Ultra-short-acting IV; used in perioperative hypertension; metabolised by blood esterases |
| **Diltiazem** | Non-DHP | 3–5 h (SR: 6–8 h) | Rate control AF; angina; less negative inotropy than verapamil |
| **Verapamil** | Non-DHP | 6–12 h | Rate control AF; PSVT; HOCM; constipation common; strongest negative inotropy |

### Contraindications and Cautions

- **Non-DHP CCBs + beta-blockers**: Additive AV block and bradycardia risk; combination is **generally contraindicated** (can cause complete AV block or asystole)
- **Non-DHP CCBs in HFrEF**: Negative inotropy can precipitate acute decompensation; **avoid verapamil and diltiazem** in HFrEF with systolic dysfunction
- **DHP CCBs in HFrEF**: Amlodipine and felodipine are safe (PRAISE and V-HeFT III studies); do not worsen outcomes
- **Verapamil + digoxin**: Verapamil increases digoxin levels (↓ renal clearance); risk of digoxin toxicity
- **Pre-excitation syndromes (WPW)**: Non-DHPs can accelerate conduction via accessory pathway → risk of ventricular fibrillation; **contraindicated**
- **Grapefruit juice**: Inhibits CYP3A4 in the gut wall → increased bioavailability of felodipine, nifedipine, and (less so) amlodipine

### Side Effects

| Side effect | Subclass | Mechanism |
|:---|:---:|:---|
| **Peripheral oedema** | DHP (amlodipine especially) | Preferential dilation of pre-capillary arterioles → ↑ capillary hydrostatic pressure → fluid transudation; not true fluid retention |
| **Reflex tachycardia** | DHP (short-acting > long-acting) | Baroreceptor response to rapid vasodilation |
| **Constipation** | Verapamil | Smooth muscle relaxation in GI tract; dose-related; very common |
| **Flushing, headache** | DHP | Vasodilation |
| **Bradycardia, AV block** | Non-DHP | Direct SA/AV node depression |
| **Gingival hyperplasia** | DHP (CCBs in general) | Mechanism unclear; dose-related; amlodipine and nifedipine most reported |

## Evidence

### Landmark Randomised Controlled Trials

| Trial | Drug | Population | Key result |
|:---|:---|:---|:---|
| **ALLHAT (2002)** | Amlodipine vs chlorthalidone vs lisinopril | 33,357 hypertensive patients ≥55 years with ≥1 CV risk factor | Amlodipine comparable to chlorthalidone for primary outcome (fatal CHD + non-fatal MI); **amlodipine better than lisinopril for stroke prevention** (NNT ~250 over 5 years) [^allhat-2002] |
| **CAMELOT (2004)** | Amlodipine vs enalapril vs placebo | 1,991 patients with stable CAD and normal BP | **Amlodipine reduced adverse cardiovascular events by 31%** vs placebo; IVUS sub-study: amlodipine slowed atherosclerosis progression; enalapril did not reach significance [^camelot-2004] |
| **Staessen et al. / Syst-Eur / SHEP meta-analysis (2001)** | CCBs vs placebo/diuretic | Elderly patients with isolated systolic hypertension | CCBs (nitrendipine) reduce stroke by ~42%, cardiac events by ~26% in isolated systolic hypertension [^staessen-2001] |
| **VALUE (2004)** | Amlodipine vs valsartan | 15,245 hypertensive patients at high CV risk | Primary endpoint (cardiac morbidity/mortality) not significantly different; amlodipine achieved earlier BP control; better stroke reduction early in trial [^value-2004] |

### Comparison with Other Antihypertensive Classes

The ALLHAT trial (n=33,357) provided the most definitive head-to-head comparison:

- **CCB (amlodipine) vs thiazide (chlorthalidone)**: No difference in CHD; equivalent for mortality; CCB had more HF events (possibly due to chlorthalidone's superior volume control)
- **CCB vs ACE-I (lisinopril)**: CCB was **superior for stroke** and non-inferior for CHD; ACE-I had higher rates of HF, peripheral arterial disease, angina in this population
- Both findings support CCBs as equal first-line choices to diuretics for most hypertensive patients

### CAMELOT — Anti-Atherosclerotic Effects

The CAMELOT trial is notable for demonstrating that amlodipine's benefits in stable CAD extend beyond blood pressure reduction. The IVUS sub-study showed **atherosclerotic plaque volume stabilisation or slight regression** in the amlodipine arm, suggesting direct anti-atherosclerotic properties — possibly via oxidative stress reduction, NO bioavailability, or direct anti-inflammatory effects on the vascular wall.

## Connections

- **Treats** → [Cardiovascular system](../../../../01-human/07-system/cardiovascular-system/README.md): CCBs are first-line agents for hypertension and angina. DHP CCBs lower SVR and blood pressure; non-DHP CCBs provide rate control in arrhythmias and anti-anginal effect — critical functional interventions across the cardiovascular system.
- **Modulates** → [Cardiovascular system](../../../../01-human/07-system/cardiovascular-system/README.md): L-type channel blockade modulates vascular tone (all CCBs), SA node automaticity (non-DHP), AV conduction (non-DHP), and myocardial contractility (non-DHP) — reflecting direct modulation of cardiovascular cellular physiology.
- **Compare with** → [Beta-blockers](../beta-blockers/README.md): Both classes reduce heart rate and are used for angina. Beta-blockers preferred in HFrEF and post-MI; CCBs preferred in vasospastic angina and where beta-blockers are contraindicated (severe asthma, peripheral arterial disease). Combination of non-DHP CCB + beta-blocker risks AV block.
- **Compare with** → [ACE inhibitors](../ace-inhibitors/README.md): ALLHAT shows CCBs superior to ACE-I for stroke; ACE-I superior for HFrEF and diabetic nephropathy. Often combined: CCB + RAS blocker is a recommended two-drug antihypertensive combination (ACCOMPLISH trial: amlodipine + benazepril superior to HCTZ + benazepril).
- **Compare with** → [ARBs](../arbs/README.md): VALUE trial compared amlodipine with valsartan head-to-head; equivalent primary outcomes with earlier BP control by amlodipine. CCB + ARB is a preferred dual combination for hypertension when RAS blockade is indicated.

[^allhat-2002]: ALLHAT Officers and Coordinators for the ALLHAT Collaborative Research Group. Major outcomes in high-risk hypertensive patients randomized to angiotensin-converting enzyme inhibitor or calcium channel blocker vs diuretic. *JAMA.* 2002;288(23):2981-97. [doi:10.1001/jama.288.23.2981](https://doi.org/10.1001/jama.288.23.2981)
[^camelot-2004]: Nissen SE, Tuzcu EM, Libby P, et al. Effect of antihypertensive agents on cardiovascular events in patients with coronary disease and normal blood pressure: the CAMELOT study. *N Engl J Med.* 2004;350(23):2352-8. [doi:10.1056/NEJMoa042761](https://doi.org/10.1056/NEJMoa042761)
[^staessen-2001]: Staessen JA, Gasowski J, Wang JG, et al. Risks of untreated and treated isolated systolic hypertension in the elderly: meta-analysis of outcome trials. *Lancet.* 2000;355(9207):865-72. [PubMed 11289345](https://pubmed.ncbi.nlm.nih.gov/11289345/)
[^value-2004]: Julius S, Kjeldsen SE, Weber M, et al. Outcomes in hypertensive patients at high cardiovascular risk treated with regimens based on valsartan or amlodipine: the VALUE randomised trial. *Lancet.* 2004;363(9426):2022-31. [doi:10.1016/S0140-6736(04)16451-9](https://doi.org/10.1016/S0140-6736(04)16451-9) · [PubMed 15207952](https://pubmed.ncbi.nlm.nih.gov/15207952/)
