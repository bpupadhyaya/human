---
schema: human-scale-entry/v1
id: vasopressin
name: Vasopressin
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-05
summary: "9 aa cyclic neuropeptide from hypothalamic SON/PVN neurons. V2R on collecting duct → AQP2 → urine concentration; V1aR on vasculature → vasoconstriction. Deficiency causes diabetes insipidus; excess causes SIADH hyponatraemia."
aliases: ["ADH", "antidiuretic hormone", "AVP", "arginine vasopressin", "argipressin"]
sources:
  - id: stryer-biochemistry
    type: textbook
    cite: "Berg JM, Tymoczko JL, Stryer L. Biochemistry. 9th ed. W.H. Freeman; 2019."
    url: "https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X"
    accessed: "2026-06-05"
  - id: guyton-hall
    type: textbook
    cite: "Hall JE, Hall ME. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2021."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/06-organ/kidney
    relation: modulates
    note: "V2R on collecting duct principal cells → cAMP → PKA → AQP2 apical trafficking → ↑water permeability → urine up to 1200 mOsm/kg; V2R mutations → X-linked nephrogenic DI; lithium blocks V2R–cAMP signalling."
  - target: 01-human/07-system/cardiovascular-system
    relation: modulates
    note: "V1aR on vascular smooth muscle → Gq → Ca²⁺ → vasoconstriction; IV vasopressin (0.03–0.04 u/min) is used in septic shock to restore MAP; V1aR also improves splanchnic vasoconstriction in hepatorenal syndrome."
  - target: 01-human/07-system/nervous-system
    relation: modulates
    note: "Vasopressin is synthesised in hypothalamic SON/PVN neurons and transported to posterior pituitary; CNS isoforms mediate social bonding and anxiety; V1bR on corticotrophs synergises with CRH for ACTH release during stress."
  - target: 01-human/07-system/renal-system
    relation: modulates
    note: "AVP is the master regulator of urinary concentration; urine osmolality ranges 50–1200 mOsm/kg depending on AVP level; urine osmolality <300 mOsm/kg with elevated serum Na⁺ and polyuria (>3 L/day) defines diabetes insipidus."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "SON/PVN neurons release AVP into systemic circulation (posterior pituitary) and limbic regions; V1aR in lateral septum mediates social memory and pair bonding; V1bR (V3R) on corticotrophs synergises with CRH for ACTH release; central AVP circuits modulate aggression and anxiety."
  - target: 01-human/07-system/ptsd
    relation: connects-to
    note: "CSF vasopressin is elevated in PTSD; AVP-CRH synergy at corticotroph V1bR potentiates ACTH when CRH receptors desensitise; elevated AVP sustains HPA hyperactivation; V1bR antagonists show anxiolytic effects and are a proposed PTSD pharmacotherapy."
  - target: 01-human/07-system/autism-spectrum-disorder
    relation: connects-to
    note: "AVPR1A promoter microsatellites (RS1, RS3) associate with ASD social behavior; V1aR in lateral septum mediates social recognition memory; V1aR-KO mice show impaired social memory; intranasal vasopressin is in Phase 2 trials for ASD social communication deficits."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "AVP is elevated in PVN and CSF of depressed patients; V1bR co-drives HPA hyperactivation with CRH → excess ACTH and cortisol; V1b antagonist SSR149415 showed antidepressant effects in Phase 2; SSRIs normalise hypersecretion of both CRH and AVP."
---

# Vasopressin

## Overview

Vasopressin (arginine vasopressin, AVP; also antidiuretic hormone, ADH) is a 9-amino-acid cyclic neuropeptide that serves two master regulatory functions: **urinary water conservation** and **vascular tone maintenance**. It is synthesised in magnocellular neurons of the hypothalamic supraoptic (SON) and paraventricular (PVN) nuclei, transported along axons to the posterior pituitary, and released into systemic circulation in response to rising plasma osmolality or falling blood volume [^guyton-hall].

Through its V2 receptor on renal collecting duct principal cells, AVP is the single most important determinant of urine concentration — controlling whether the kidney produces 50 mL/h of dilute urine (50 mOsm/kg) or 0.5 mL/h of maximally concentrated urine (1200 mOsm/kg). Through its V1a receptor on vascular smooth muscle, AVP is a potent vasoconstrictor exploited clinically in septic shock (where catecholamine receptors are downregulated) [^stryer-biochemistry].

The synthetic analog **desmopressin (dDAVP)** — V2-selective with long half-life (~8 h vs. 5–15 min for native AVP) — is one of the most clinically versatile small peptides in medicine, used for central diabetes insipidus, nocturnal enuresis, haemophilia A, and von Willebrand disease.

## Structure

Vasopressin is a **nonapeptide** with a ring formed by a disulfide bridge:

```
Cys¹-Tyr²-Phe³-Gln⁴-Asn⁵-Cys⁶-Pro⁷-Arg⁸-Gly⁹-NH₂
 └──────────────────────────────┘
         disulfide bridge
```

| Feature | Detail |
|:---|:---|
| **Molecular weight** | 1084 Da |
| **Ring structure** | Cys1–Cys6 disulfide (6-membered ring); essential for receptor binding |
| **C-terminal** | Gly9-amide (amidation required for full activity) |
| **Comparison to oxytocin** | Differs only at positions 3 (Phe vs. Ile) and 8 (Arg vs. Leu); explains partial cross-reactivity |

Vasopressin is synthesised as **pre-pro-vasopressin** (164 aa): signal peptide + AVP (9 aa) + neurophysin II (93 aa, carrier protein) + copeptin (39 aa, C-terminal glycopeptide). During axonal transport, enzymatic cleavage liberates AVP from neurophysin II. **Copeptin** is released equimolarly with AVP and is a stable, easily measurable surrogate for AVP secretion in clinical diagnosis (AVP itself is unstable and hard to measure).

**Key engineered analogs:**
- **Desmopressin (dDAVP):** 1-desamino-8-D-arginine vasopressin — desaminoCys1 (removes vasopressor activity, prolongs t½), D-Arg8 (resists aminopeptidase cleavage); V2-selective; t½ ~8–12 h
- **Terlipressin:** Triglycyl-lysine vasopressin (prodrug); V1aR-selective; t½ ~6 h; used in variceal bleeding and hepatorenal syndrome
- **Ornipressin:** V1aR agonist; used in local vasoconstriction during surgery

## Function

Vasopressin coordinates three major physiological functions:

**1. Antidiuresis (V2R-mediated):**
- Principal cells of collecting duct → V2R → Gs → adenylyl cyclase → ↑cAMP → PKA
- PKA phosphorylates AQP2 (Ser256, Ser264, Ser269, Ser271) → vesicle insertion into apical membrane → ↑water permeability
- Water moves osmotically from tubular lumen (low osmolality ~100 mOsm/kg) into hypertonic medullary interstitium (up to ~1200 mOsm/kg, maintained by countercurrent multiplier)
- Also: PKA activates urea transporter UT-A1 in papillary collecting duct → ↑urea reabsorption → enhances medullary hypertonicity (urea recycling)
- AQP3/4 on basolateral membrane provides exit for reabsorbed water into peritubular capillaries

**2. Vasoconstriction (V1aR-mediated):**
- Vascular smooth muscle V1aR → Gq → PLC → IP₃ + DAG → Ca²⁺ release + PKC → MLCK → vasoconstriction → ↑TPR → ↑MAP
- At physiological concentrations, this effect is minor; becomes significant in haemorrhage (non-osmotic release) and when administered pharmacologically

**3. ACTH facilitation (V1bR/V3R-mediated):**
- Anterior pituitary corticotrophs → V1bR → Gq → IP₃/Ca²⁺ → synergises with CRH-driven cAMP → ↑ACTH secretion
- Critical during prolonged stress when CRH receptors desensitise; AVP sustains HPA axis activation

## Mechanism

### Stimuli for AVP Release

| Stimulus | Threshold / Magnitude |
|:---|:---|
| **Hyperosmolality** | 1% rise in osmolality above threshold (~285 mOsm/kg); linear response (~0.4 pg/mL per mOsm/kg); sensed by OVLT and SFO (peri-BBB circumventricular organs) |
| **Hypovolaemia** | 20% reduction in blood volume → robust AVP release; sensed by cardiopulmonary (low-pressure) and arterial (high-pressure) baroreceptors via vagal/glossopharyngeal afferents to nucleus tractus solitarius → PVN |
| **Nausea** | Most potent single stimulus; AVP spikes 100–1000-fold within minutes; mediated by CTZ/AP → NTS |
| **Pain, stress, hypoglycaemia** | All activate PVN magnocellular neurons via noradrenergic brainstem projections |
| **Angiotensin II** | Acts on OVLT/SFO → reinforces osmotic-driven AVP release; links RAAS to water conservation |

At extreme volume depletion, **volume override osmolality** — the body prioritises blood pressure over tonicity; this is why patients with severe diarrhoea can develop hypernatraemia even with ↑AVP (urine is concentrated but insufficient to replace loss).

### V2R–AQP2 Trafficking in Detail

1. Resting state: AQP2 resides in subapical vesicles (recycling endosomes); collecting duct is water-impermeable
2. AVP → PKA → phospho-Ser256 on AQP2 → interaction with 14-3-3 proteins → microtubule-dependent vesicle trafficking → apical fusion (SNARE-mediated)
3. Long-term: AVP → ↑AQP2 gene transcription (CREB-dependent, Ser256p-driven nuclear signalling) → ↑total AQP2 protein pool
4. AVP withdrawal → phosphatase (PP2B) dephosphorylates AQP2 → internalisation via clathrin-coated pits → lysosomal degradation or recycling endosome storage

Lithium blocks V2R–cAMP coupling by inhibiting adenylyl cyclase and impairing vesicle trafficking (via GSK3 effects on AQP2 phosphorylation), causing **nephrogenic DI** in 20–40% of long-term lithium users.

## Connections

- `modulates` → **[kidney](../../06-organ/kidney/README.md)** — V2R on collecting duct → PKA → AQP2 apical trafficking → urine concentration; V2R mutations cause X-linked nephrogenic DI; lithium blocks V2R–cAMP signalling
- `modulates` → **[cardiovascular-system](../../07-system/cardiovascular-system/README.md)** — V1aR on vascular smooth muscle → Gq → Ca²⁺ → vasoconstriction; IV vasopressin used in septic shock and hepatorenal syndrome
- `modulates` → **[nervous-system](../../07-system/nervous-system/README.md)** — synthesised in hypothalamic SON/PVN neurons; CNS vasopressin (V1aR, V1bR) regulates social behaviour, anxiety, and stress-axis (HPA); V1bR on corticotrophs drives ACTH
- `modulates` → **[renal-system](../../07-system/renal-system/README.md)** — master regulator of urinary concentration and water homeostasis; urine osmolality 50–1200 mOsm/kg depending on AVP; polyuria + dilute urine + ↑plasma Na⁺ defines diabetes insipidus
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — SON/PVN neurons release AVP into systemic circulation (posterior pituitary) and limbic regions; V1aR in lateral septum mediates social memory and pair bonding; V1bR (V3R) on corticotrophs synergises with CRH for ACTH release; central AVP circuits modulate aggression and anxiety
- `connects-to` → **[PTSD](../../07-system/ptsd/README.md)** — CSF vasopressin is elevated in PTSD; AVP-CRH synergy at corticotroph V1bR potentiates ACTH when CRH receptors desensitise; elevated AVP sustains HPA hyperactivation; V1bR antagonists show anxiolytic effects and are a proposed PTSD pharmacotherapy
- `connects-to` → **[Autism Spectrum Disorder](../../07-system/autism-spectrum-disorder/README.md)** — AVPR1A promoter microsatellites (RS1, RS3) associate with ASD social behavior; V1aR in lateral septum mediates social recognition memory; V1aR-KO mice show impaired social memory; intranasal vasopressin is in Phase 2 trials for ASD social communication deficits
- `connects-to` → **[Major Depressive Disorder](../../07-system/major-depressive-disorder/README.md)** — AVP is elevated in PVN and CSF of depressed patients; V1bR co-drives HPA hyperactivation with CRH → excess ACTH and cortisol; V1b antagonist SSR149415 showed antidepressant effects in Phase 2; SSRIs normalise hypersecretion of both CRH and AVP

## Pathology

| Condition | Mechanism | Key Features |
|:---|:---|:---|
| **Central (neurogenic) diabetes insipidus** | Destruction of SON/PVN neurons or posterior pituitary (trauma, neurosurgery, craniopharyngioma, histiocytosis, Wolfram syndrome [DIDMOAD]) → ↓/absent AVP secretion | Polyuria (3–20 L/day), polydipsia, dilute urine (<300 mOsm/kg), ↑serum Na⁺; water deprivation test + dDAVP challenge; treat with intranasal/oral dDAVP |
| **Nephrogenic diabetes insipidus** | AVP present/elevated but V2R or AQP2 dysfunctional: X-linked AVPR2 mutations (~90% of hereditary NDI), AQP2 mutations (~10%); acquired: lithium, demeclocycline, hypercalcaemia, hypokalaemia | Same polyuria/polydipsia; no response to dDAVP challenge; treat with thiazides (paradoxical ↓urine output via volume contraction), amiloride (lithium-NDI), NSAIDs |
| **SIADH** | Ectopic or inappropriate AVP secretion: SCLC (AVP gene expression), pneumonia, CNS disease (meningitis, stroke), SSRIs, carbamazepine, cyclophosphamide → ↑water retention → dilutional hyponatraemia with concentrated urine | Serum Na⁺ <135, urine Na⁺ >20 mEq/L, urine osmolality >100 mOsm/kg (inappropriately concentrated); treat: fluid restriction (mild), vaptans (tolvaptan/conivaptan, V2R antagonists), hypertonic saline (3% NaCl) for severe/symptomatic (<120 mEq/L) |
| **Haemorrhagic/septic shock AVP depletion** | AVP stores exhausted during prolonged shock → relative AVP deficiency despite low MAP | Low AVP in septic shock vasoplegic phase; replacement doses (0.03–0.04 u/min IV) restore vascular tone; higher doses → mesenteric ischaemia risk |

## See Also

- [^stryer-biochemistry] Berg JM, Tymoczko JL, Stryer L. *Biochemistry.* 9th ed. W.H. Freeman; 2019.
- [^guyton-hall] Hall JE, Hall ME. *Guyton and Hall Textbook of Medical Physiology.* 14th ed. Elsevier; 2021.
- Related entries: [kidney](../../06-organ/kidney/README.md), [renal-system](../../07-system/renal-system/README.md), [cortisol](../cortisol/README.md), [nervous-system](../../07-system/nervous-system/README.md)
