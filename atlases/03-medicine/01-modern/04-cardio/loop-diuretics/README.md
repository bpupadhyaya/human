---
schema: medicine-entry/v1
id: loop-diuretics
name: Loop diuretics
atlas: 03-medicine
scale: 01-modern
status: draft
last_reviewed: 2026-06-03
summary: "Loop diuretics (furosemide, bumetanide, torasemide) — NKCC2 inhibitors in the thick ascending limb, blocking ~25% of filtered Na⁺. Most potent diuretics; first-line for ADHF volume overload. IV furosemide: diuresis within 30 min."
aliases: ["loop diuretics", "furosemide", "frusemide", "bumetanide", "torasemide", "torsemide", "ethacrynic acid"]
sources:
  - id: brater-1998-diuretics
    type: peer-reviewed
    cite: "Brater DC. Diuretic therapy. N Engl J Med. 1998;339(6):387-95."
    doi: "10.1056/NEJM199808063390607"
    pmid: "9691107"
    url: "https://doi.org/10.1056/NEJM199808063390607"
  - id: felker-2011-dose-trial
    type: peer-reviewed
    cite: "Felker GM, Lee KL, Bull DA, et al. Diuretic strategies in patients with acute decompensated heart failure. N Engl J Med. 2011;364(9):797-805."
    doi: "10.1056/NEJMoa1005419"
    pmid: "21366472"
    url: "https://doi.org/10.1056/NEJMoa1005419"
  - id: felker-2012-diuretics-review
    type: peer-reviewed
    cite: "Felker GM, Mentz RJ. Diuretics and ultrafiltration in acute decompensated heart failure. J Am Coll Cardiol. 2012;59(24):2145-53."
    doi: "10.1016/j.jacc.2011.10.907"
    pmid: "22676935"
    url: "https://doi.org/10.1016/j.jacc.2011.10.907"
  - id: heidenreich-2022-hf-guideline
    type: clinical-guideline
    cite: "Heidenreich PA, Bozkurt B, Aguilar D, et al. 2022 AHA/ACC/HFSA Guideline for the Management of Heart Failure. Circulation. 2022;145(18):e895-e1032."
    doi: "10.1161/CIR.0000000000001063"
    pmid: "35363499"
    url: "https://doi.org/10.1161/CIR.0000000000001063"
cross_links:
  - target: 01-human/07-system/cardiovascular-system
    relation: acts-on
    note: "Loop diuretics reduce intravascular volume, lowering cardiac preload (ventricular filling pressures) and reducing pulmonary venous congestion — the defining haemodynamic benefit in acute decompensated heart failure."
  - target: 01-human/06-organ/heart
    relation: acts-on
    note: "By reducing preload, loop diuretics reduce wall stress and oxygen demand in the volume-overloaded heart; rapid IV furosemide also has acute venodilatory effects reducing pulmonary oedema within minutes of administration."
---

# Loop diuretics

## Overview

Loop diuretics are the **most potent class of diuretic agents** available in clinical medicine, capable of inducing massive natriuresis and diuresis even in the setting of reduced glomerular filtration rate. They act by inhibiting the **Na⁺-K⁺-2Cl⁻ cotransporter (NKCC2)** in the thick ascending limb of the loop of Henle, blocking reabsorption of approximately **25% of filtered sodium** (compared to 3–8% for thiazides) [^brater-1998-diuretics].

The three principal agents in clinical use:

| Agent | Bioavailability (oral) | Duration of action | Potency equivalence |
|:---|:---:|:---:|:---:|
| **Furosemide (frusemide)** | 10–90% (highly variable) | 4–6 h | 40 mg reference |
| **Bumetanide** | ~80% (more reliable) | 4–6 h | 1 mg ≈ furosemide 40 mg |
| **Torasemide (torsemide)** | ~80% (reliable) | 12–16 h | 10–20 mg ≈ furosemide 40 mg |

Loop diuretics are **first-line therapy for** [^heidenreich-2022-hf-guideline]:
- Acute decompensated heart failure (ADHF) with volume overload — the most common indication for hospitalisation in HFrEF
- Chronic HFrEF and HFpEF — to maintain euvolaemia and control symptoms
- Refractory oedema (hepatic cirrhosis, nephrotic syndrome, hypoalbuminaemia)
- Hypertensive emergencies (IV furosemide for fluid overload component)
- Hypercalcaemia (calciuresis)

## Mechanism

### NKCC2 Inhibition in the Thick Ascending Limb (TAL)

The thick ascending limb of Henle is the site of **active NaCl reabsorption without water** (the limb is impermeable to water). This reabsorption is mediated by **NKCC2 (SLC12A1)**:

```
Lumen → NKCC2: 1 Na⁺ + 1 K⁺ + 2 Cl⁻ enter together → reabsorbed into the tubular cell
Then: K⁺ recycled back into lumen (ROMK channel) → allows NKCC2 to continue
      Na⁺ exits via basolateral Na⁺/K⁺-ATPase → interstitium
      Cl⁻ exits via basolateral Cl⁻ channels → interstitium
```

This process generates the **medullary interstitial concentration gradient** (the osmolality gradient from 300 to ~1200 mOsm in the inner medulla) that drives water reabsorption in the collecting duct (via ADH/aquaporin-2). By blocking NKCC2:

1. Na⁺, Cl⁻, and water are not reabsorbed → **massive natriuresis and diuresis**
2. Medullary concentration gradient is abolished → even ADH-stimulated collecting duct cannot concentrate urine → **inability to concentrate urine during loop diuretic action**
3. Increased distal tubule Na⁺ delivery → increased aldosterone-sensitive Na⁺/K⁺ exchange → **hypokalaemia** (a major side effect)
4. Increased distal Mg²⁺ and Ca²⁺ loss → **hypomagnesaemia, hypocalcaemia** (unlike thiazides, which spare Ca²⁺)

Loop diuretics also increase prostaglandin E₂ and prostacyclin production in the kidney, contributing to their venodilatory effect (inhibited by NSAIDs — an important drug interaction).

### Acute Haemodynamic Effect of IV Furosemide

Within **5–15 minutes** of IV furosemide administration (before significant diuresis begins), there is an acute **venodilatory effect**:
- Increased renal prostaglandins → venodilation → ↓venous return → ↓preload → ↓pulmonary capillary wedge pressure
- This rapid venodilation relieves pulmonary oedema before the diuresis begins
- It is inhibited by NSAIDs and absent with oral furosemide — explaining why IV administration is superior in acute pulmonary oedema

Diuresis then follows: onset ~30 minutes, peak ~2 h, duration ~4–6 h for furosemide.

### Renal Handling

Loop diuretics are **secreted** into the tubular lumen by the organic anion transporter (OAT1/OAT3) from the peritubular capillary — they work from the **luminal side** of NKCC2. In severe CKD:
- Reduced GFR → less drug filtered
- Competing organic anions (uremic toxins) reduce OAT-mediated secretion
- Higher doses required to achieve sufficient luminal concentration; torasemide and bumetanide have more predictable bioavailability
- Furosemide dose ceiling: ~400–600 mg IV/day before diminishing returns; above this, increasing Na⁺ delivery to distal segments triggers aldosterone-mediated adaptation

## Clinical Use

### Acute Decompensated Heart Failure (ADHF)

The primary use of loop diuretics in cardiology:
- **Goal:** Achieve negative fluid balance of 1–2 L/day to relieve congestion while monitoring renal function, electrolytes, and haemodynamics
- **Route:** IV preferred over oral in ADHF (more reliable absorption, faster onset)
- **Dosing:** Start at ≥1× the patient's prior oral maintenance dose IV (e.g., if on furosemide 40 mg oral, start 40 mg IV); in diuretic-resistant patients, escalate dose or add thiazide (metolazone) for synergistic blockade

### Chronic Heart Failure (HFrEF and HFpEF)

- Loop diuretics maintain euvolaemia and relieve congestion symptoms in chronic HF
- **Dose-titration:** Flexible, patient-directed diuresis — adjust based on daily weight monitoring and symptoms
- **Critical caveat:** Loop diuretics have **no mortality benefit** in HF — they are symptom-relief agents. The mortality benefit in HFrEF comes from beta-blockers, ACE inhibitors/ARBs/ARNIs, MRAs, and SGLT2 inhibitors.

### Comparison: Furosemide vs Torasemide

- **TRANSFORM-HF trial (2023):** No difference in all-cause mortality or hospitalisations between furosemide and torasemide in HF — despite torasemide's theoretical advantages (more reliable bioavailability, longer duration). Both are acceptable; agent choice should follow patient-specific pharmacokinetic considerations.

## Evidence

### Key Trials

| Trial | Drug | Population | Key result |
|:---|:---|:---|:---|
| **DOSE (2011)** | Furosemide IV | 308 ADHF patients | High-dose (2.5× oral maintenance) vs low-dose IV furosemide: no difference in global assessment; high-dose → better diuresis + slightly more creatinine rise; both strategies acceptable [^felker-2011-dose-trial] |
| **Felker & Mentz review (2012)** | Loop diuretics + ultrafiltration | ADHF | Ultrafiltration non-inferior to diuretics with no renal advantage; guideline position remains loop diuretics first-line [^felker-2012-diuretics-review] |
| **2022 AHA/ACC/HFSA Guideline** | Class I | Symptomatic HF with volume overload | Loop diuretics recommended for all patients with HF and signs/symptoms of volume overload [^heidenreich-2022-hf-guideline] |

### Side Effects

| Adverse effect | Mechanism | Management |
|:---|:---|:---|
| **Hypokalaemia** | Increased distal K⁺ secretion | Oral KCl supplementation; concomitant MRA (spironolactone, eplerenone) in HFrEF (also has mortality benefit) |
| **Hypomagnesaemia** | Urinary Mg²⁺ loss | Oral Mg supplementation |
| **Hypocalcaemia** | Urinary Ca²⁺ loss (unlike thiazides) | Monitor; supplement if symptomatic |
| **Volume depletion / prerenal AzN** | Excessive diuresis | Dose titration; daily weight |
| **Ototoxicity** | Cochlear NKCC endolymph disruption | Avoid rapid high-dose IV administration; greatest risk with aminoglycoside combination |
| **Hyperuricaemia / gout** | Competition with urate for OAT secretion | Allopurinol if symptomatic |
| **Sulfonamide allergy** | Structural sulphonamide group in furosemide | Use ethacrynic acid (not sulfonamide-based) in true sulfa allergy |

## Connections

- **Acts on** → [Cardiovascular system](../../../../01-human/07-system/cardiovascular-system/README.md): Reducing intravascular volume and venous return reduces cardiac preload and pulmonary venous pressure throughout the cardiovascular system.
- **Acts on** → [Heart](../../../../01-human/06-organ/heart/README.md): By reducing preload, loop diuretics reduce ventricular end-diastolic volume and wall tension in the volume-overloaded failing heart; acute IV furosemide additionally causes venodilation that relieves pulmonary oedema within minutes.

[^brater-1998-diuretics]: Brater DC. Diuretic therapy. *N Engl J Med.* 1998;339(6):387-95. [doi:10.1056/NEJM199808063390607](https://doi.org/10.1056/NEJM199808063390607) · [PubMed 9691107](https://pubmed.ncbi.nlm.nih.gov/9691107/)
[^felker-2011-dose-trial]: Felker GM, Lee KL, Bull DA, et al. Diuretic strategies in patients with acute decompensated heart failure (DOSE). *N Engl J Med.* 2011;364(9):797-805. [doi:10.1056/NEJMoa1005419](https://doi.org/10.1056/NEJMoa1005419) · [PubMed 21366472](https://pubmed.ncbi.nlm.nih.gov/21366472/)
[^felker-2012-diuretics-review]: Felker GM, Mentz RJ. Diuretics and ultrafiltration in acute decompensated heart failure. *J Am Coll Cardiol.* 2012;59(24):2145-53. [doi:10.1016/j.jacc.2011.10.907](https://doi.org/10.1016/j.jacc.2011.10.907) · [PubMed 22676935](https://pubmed.ncbi.nlm.nih.gov/22676935/)
[^heidenreich-2022-hf-guideline]: Heidenreich PA, Bozkurt B, Aguilar D, et al. 2022 AHA/ACC/HFSA Guideline for the Management of Heart Failure. *Circulation.* 2022;145(18):e895–e1032. [doi:10.1161/CIR.0000000000001063](https://doi.org/10.1161/CIR.0000000000001063) · [PubMed 35363499](https://pubmed.ncbi.nlm.nih.gov/35363499/)
