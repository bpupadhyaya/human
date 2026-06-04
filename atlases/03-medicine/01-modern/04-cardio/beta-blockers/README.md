---
schema: medicine-entry/v1
id: beta-blockers
name: Beta-blockers
atlas: 03-medicine
scale: 01-modern
status: draft
last_reviewed: 2026-06-03
summary: "Competitive β-adrenergic receptor antagonists (primarily β1-selective). First-line therapy for HFrEF, hypertension, angina, post-MI prophylaxis, and arrhythmias. Reduce all-cause mortality in HFrEF ~34% by reversing chronic catecholamine toxicity and cardiac remodeling."
aliases: ["beta-adrenergic blockers", "beta-adrenoreceptor antagonists", "β-blockers"]
sources:
  - id: merit-hf-1999
    type: peer-reviewed
    cite: "MERIT-HF Study Group. Effect of metoprolol CR/XL in chronic heart failure: Metoprolol CR/XL Randomised Intervention Trial in Congestive Heart Failure (MERIT-HF). Lancet. 1999;353(9169):2001-7."
    doi: "10.1016/S0140-6736(99)04440-2"
    pmid: "10376614"
    url: "https://doi.org/10.1016/S0140-6736(99)04440-2"
  - id: cibis-ii-1999
    type: peer-reviewed
    cite: "CIBIS-II Investigators and Committees. The Cardiac Insufficiency Bisoprolol Study II (CIBIS-II): a randomised trial. Lancet. 1999;353(9146):9-13."
    doi: "10.1016/S0140-6736(98)11181-9"
    pmid: "10023943"
    url: "https://doi.org/10.1016/S0140-6736(98)11181-9"
  - id: copernicus-2001
    type: peer-reviewed
    cite: "Packer M, Coats AJ, Fowler MB, et al. Effect of carvedilol on survival in severe chronic heart failure. N Engl J Med. 2001;344(22):1651-8."
    doi: "10.1056/NEJM200105313442201"
    pmid: "11386263"
    url: "https://doi.org/10.1056/NEJM200105313442201"
  - id: bristow-2000-bar-failure
    type: peer-reviewed
    cite: "Bristow MR. Beta-adrenergic receptor blockade in chronic heart failure. Circulation. 2000;101(5):558-69."
    doi: "10.1161/01.CIR.101.5.558"
    pmid: "10662755"
    url: "https://doi.org/10.1161/01.CIR.101.5.558"
  - id: heidenreich-2022-hf-guideline
    type: clinical-guideline
    cite: "Heidenreich PA, Bozkurt B, Aguilar D, et al. 2022 AHA/ACC/HFSA Guideline for the Management of Heart Failure. Circulation. 2022;145(18):e895-e1032."
    doi: "10.1161/CIR.0000000000001063"
    pmid: "35363499"
    url: "https://doi.org/10.1161/CIR.0000000000001063"
cross_links:
  - target: 01-human/03-molecular/beta1-adrenergic-receptor
    relation: targets
    note: "Beta-blockers competitively antagonize β1-adrenergic receptors on cardiomyocytes, SA-nodal cells, and renal juxtaglomerular cells."
  - target: 01-human/07-system/cardiovascular-system
    relation: acts-on
    note: "Reduce heart rate, contractility, cardiac output, and blood pressure at the system level."
  - target: 01-human/06-organ/heart
    relation: acts-on
    note: "Reduce myocardial oxygen demand, prevent catecholamine-mediated toxicity, improve ventricular function over weeks-to-months in HFrEF."
---

# Beta-blockers

## Overview

Beta-blockers (β-adrenergic receptor antagonists) are one of the most widely prescribed and mortality-proven drug classes in cardiovascular medicine. They act by **competitive, reversible antagonism at β-adrenergic receptors** — primarily the β1 subtype (cardiac, renal) for the agents most used in heart disease — blocking the physiological actions of norepinephrine and epinephrine at those receptors [^bristow-2000-bar-failure].

Their clinical utility spans multiple indications:

- **HFrEF:** Reduce all-cause mortality by ~34% compared with placebo, one of the strongest survival effects in pharmacology [^merit-hf-1999][^cibis-ii-1999][^copernicus-2001]
- **Hypertension:** Lower cardiac output and, over time, vascular resistance; first-line or adjunct therapy
- **Stable angina:** Reduce heart rate and myocardial oxygen demand; extend time-to-ischemia on exercise testing
- **Post-MI prophylaxis:** Reduce reinfarction and sudden cardiac death
- **AF rate control:** Slow AV nodal conduction → control ventricular rate in atrial fibrillation
- **Certain arrhythmias:** CPVT (catecholaminergic polymorphic VT), long QT, inappropriate sinus tachycardia

The paradox that agents reducing contractility benefit patients with already-reduced contractility (HFrEF) was one of the great surprises of 20th-century cardiology. It is now understood through the lens of chronic catecholamine toxicity: in HFrEF, persistently elevated sympathetic drive down-regulates and functionally uncouples β1-AR, promotes cardiomyocyte apoptosis, and drives pathological remodeling. Beta-blockers interrupt this vicious cycle [^bristow-2000-bar-failure].

## Mechanism

### Molecular Target

Beta-blockers bind competitively to the **orthosteric binding pocket** of β-adrenergic receptors — the same pocket occupied by norepinephrine/epinephrine. By occupying this pocket without activating Gαs, they prevent receptor coupling to adenylyl cyclase. Key consequences in the heart:

| PKA substrate normally phosphorylated | Beta-blocker effect |
|:---|:---|
| Cav1.2 (L-type Ca²⁺ channel) | Reduced Ca²⁺ influx → reduced contractility (acute) |
| RyR2 | Reduced Ca²⁺ release; less diastolic Ca²⁺ leak |
| Phospholamban | Reduced SERCA disinhibition; slower but still functional relaxation |
| Troponin I | Less reduction in myofilament Ca²⁺ sensitivity |
| HCN4 (SA node) | Slowed diastolic depolarization → reduced heart rate |

### Acute vs. Chronic Effects

The acute effect of beta-blockers — reduced HR, contractility, and CO — is what naive physiology predicts and what makes their use in acute decompensated heart failure dangerous. Their benefit in HFrEF is a **chronic remodeling effect** that becomes apparent over weeks to months:

1. Chronic β1-AR overstimulation drives receptor down-regulation (by ~50% in advanced HFrEF), increased GRK2 expression, and uncoupling.
2. Beta-blocker therapy, by reducing β1-AR activation, allows **receptor up-regulation** — receptor density increases over weeks.
3. Reduced catecholamine-driven apoptosis → less ongoing cardiomyocyte loss.
4. Reversal of **adverse cardiac remodeling**: ventricles often decrease in volume, EF improves (sometimes dramatically — from 15% to 35%) — a phenomenon called **reverse remodeling**.

The time course of benefit (weeks-to-months) explains why patients who feel worse acutely often improve dramatically at 3–6 months if the drug is tolerated.

## Clinical Use

| Indication | Level of evidence | Comment |
|:---|:---|:---|
| **HFrEF (EF < 40%)** | Class I, Level A [^heidenreich-2022-hf-guideline] | Carvedilol, metoprolol succinate, or bisoprolol — these three specifically |
| **Hypertension** | Class I | β1-selective preferred; avoid in asthma/COPD |
| **Stable angina** | Class I | Reduce ischemic burden and exercise-induced angina |
| **Post-MI (LVEF < 40%)** | Class I, Level A | Start within 24 h of stabilization in STEMI |
| **AF — rate control** | Class I | Metoprolol, bisoprolol; caution in decompensated HF |
| **CPVT** | Class I | Nadolol often preferred (non-selective) |

## Key Agents

| Agent | Selectivity | Notable pharmacology | Key trial |
|:---|:---:|:---|:---|
| **Metoprolol succinate** (CR/XL) | β1-selective | Extended-release; lipophilic; CYP2D6 substrate | MERIT-HF (34% mortality reduction in HFrEF) [^merit-hf-1999] |
| **Bisoprolol** | β1-selective (highest) | Once daily; renal and hepatic excretion; minimal lipophilicity | CIBIS-II (34% mortality reduction in HFrEF) [^cibis-ii-1999] |
| **Carvedilol** | Non-selective β + α1 | α1-blockade adds vasodilation; also antioxidant; lipophilic | COPERNICUS (35% mortality reduction in severe HFrEF) [^copernicus-2001] |
| **Atenolol** | β1-selective | Hydrophilic; once daily; renal excretion; less CNS penetration | Not studied in HFrEF; used in HTN/angina |
| **Propranolol** | Non-selective | Lipophilic; CNS penetration; used in tremor, migraine prophylaxis, HOCM | Historical; not preferred in HFrEF |
| **Nadolol** | Non-selective | Long half-life; hydrophilic; preferred in CPVT (non-selective needed) | — |

**Note:** Only metoprolol succinate, bisoprolol, and carvedilol have demonstrated mortality benefit in HFrEF RCTs. Other beta-blockers should NOT be substituted.

## Pharmacology

### Selectivity

β1-selectivity is dose-dependent. At therapeutic doses:
- Metoprolol: ~75× more potent at β1 vs β2
- Bisoprolol: ~100× more potent at β1 vs β2
- Carvedilol: non-selective (β1 = β2), plus α1 blockade

At higher doses, "cardioselective" agents lose β2 selectivity — important in asthma/COPD patients.

### Lipophilicity and CNS Penetration

Lipophilic agents (metoprolol, carvedilol, propranolol) cross the blood-brain barrier → greater CNS side effects (vivid dreams, fatigue, depression). Hydrophilic agents (atenolol, nadolol, bisoprolol intermediate) have less CNS penetration.

### Half-life and Dosing

| Agent | Half-life | Dosing |
|:---|:---:|:---|
| Bisoprolol | ~10–12 h | Once daily |
| Metoprolol succinate | ~3–7 h (extended-release matrix ~24 h) | Once daily |
| Carvedilol | ~7–10 h | Twice daily (or carvedilol phosphate CR once daily) |

## Side Effects

- **Bradycardia and AV block** — dose-limiting; monitor HR and PR interval
- **Hypotension** — especially with carvedilol (α1 blockade); initiate at low dose, titrate
- **Fatigue** — common at initiation; often improves
- **Worsening HF symptoms at initiation** — if decompensated, defer; start when euvolemic
- **Bronchospasm** — avoid non-selective agents in asthma; β1-selective agents can be used with caution in stable COPD
- **Sexual dysfunction** — particularly with non-selective and lipophilic agents
- **Masking hypoglycemia** — in insulin-dependent diabetics (blunts tachycardia, not sweating)

## Evidence

### Key Randomised Controlled Trials

| Trial | Drug | Population | Key result |
|:---|:---|:---|:---|
| **MERIT-HF (1999)** | Metoprolol CR/XL | 3,991 HFrEF patients (EF ≤ 40%) | 34% reduction in all-cause mortality vs placebo [^merit-hf-1999] |
| **CIBIS-II (1999)** | Bisoprolol | 2,647 HFrEF patients (NYHA III–IV) | 34% reduction in all-cause mortality; trial stopped early [^cibis-ii-1999] |
| **COPERNICUS (2001)** | Carvedilol | 2,289 severe HFrEF (EF < 25%) | 35% reduction in all-cause mortality [^copernicus-2001] |

The convergence of three independent trials with three different agents — all showing ~34–35% mortality reduction — is among the most compelling evidence in cardiovascular pharmacology. These results established beta-blockers as mandatory therapy for HFrEF in current guidelines [^heidenreich-2022-hf-guideline].

## Connections

- **Targets** → [β1-adrenergic receptor](../../../../01-human/03-molecular/beta1-adrenergic-receptor/README.md): The primary molecular target. β-blockers competitively occupy the orthosteric binding pocket, blocking Gαs coupling.
- **Acts on** → [Heart](../../../../01-human/06-organ/heart/README.md): Reduces heart rate (chronotropy), contractility (inotropy), and over weeks promotes reverse remodeling in HFrEF.
- **Acts on** → [Cardiovascular System](../../../../01-human/07-system/cardiovascular-system/README.md): Lowers cardiac output and, via RAAS modulation (reduced renal β1-AR → less renin), blood pressure.

[^merit-hf-1999]: MERIT-HF Study Group. Effect of metoprolol CR/XL in chronic heart failure. *Lancet.* 1999;353(9169):2001-7. [doi:10.1016/S0140-6736(99)04440-2](https://doi.org/10.1016/S0140-6736(99)04440-2) · [PubMed 10376614](https://pubmed.ncbi.nlm.nih.gov/10376614/)
[^cibis-ii-1999]: CIBIS-II Investigators. The Cardiac Insufficiency Bisoprolol Study II (CIBIS-II). *Lancet.* 1999;353(9146):9-13. [doi:10.1016/S0140-6736(98)11181-9](https://doi.org/10.1016/S0140-6736(98)11181-9) · [PubMed 10023943](https://pubmed.ncbi.nlm.nih.gov/10023943/)
[^copernicus-2001]: Packer M, Coats AJ, Fowler MB, et al. Effect of carvedilol on survival in severe chronic heart failure. *N Engl J Med.* 2001;344(22):1651-8. [doi:10.1056/NEJM200105313442201](https://doi.org/10.1056/NEJM200105313442201) · [PubMed 11386263](https://pubmed.ncbi.nlm.nih.gov/11386263/)
[^bristow-2000-bar-failure]: Bristow MR. β-Adrenergic receptor blockade in chronic heart failure. *Circulation.* 2000;101(5):558-69. [doi:10.1161/01.CIR.101.5.558](https://doi.org/10.1161/01.CIR.101.5.558) · [PubMed 10662755](https://pubmed.ncbi.nlm.nih.gov/10662755/)
[^heidenreich-2022-hf-guideline]: Heidenreich PA, Bozkurt B, Aguilar D, et al. 2022 AHA/ACC/HFSA Guideline for the Management of Heart Failure. *Circulation.* 2022;145(18):e895–e1032. [doi:10.1161/CIR.0000000000001063](https://doi.org/10.1161/CIR.0000000000001063) · [PubMed 35363499](https://pubmed.ncbi.nlm.nih.gov/35363499/)
