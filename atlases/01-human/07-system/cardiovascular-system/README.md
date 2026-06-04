---
schema: human-scale-entry/v1
id: cardiovascular-system
name: Cardiovascular system
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-03
summary: "Heart, vasculature, and blood, organized into two circuits in series — pulmonary and systemic. The body's transport network: oxygen, CO₂, nutrients, waste, hormones, immune cells, heat."
aliases: ["circulatory system", "cardiovascular system"]
sources:
  - id: openstax-anatomy-19-1
    type: textbook
    cite: "OpenStax. Anatomy & Physiology 2e, Ch. 19.1: Heart Anatomy."
    url: "https://openstax.org/books/anatomy-and-physiology-2e/pages/19-1-heart-anatomy"
    accessed: "2026-06-03"
  - id: openstax-anatomy-20-1
    type: textbook
    cite: "OpenStax. Anatomy & Physiology 2e, Ch. 20.1: Structure and Function of Blood Vessels."
    url: "https://openstax.org/books/anatomy-and-physiology-2e/pages/20-1-structure-and-function-of-blood-vessels"
    accessed: "2026-06-03"
  - id: openstax-anatomy-20-2
    type: textbook
    cite: "OpenStax. Anatomy & Physiology 2e, Ch. 20.2: Blood Flow, Blood Pressure, and Resistance."
    url: "https://openstax.org/books/anatomy-and-physiology-2e/pages/20-2-blood-flow-blood-pressure-and-resistance"
    accessed: "2026-06-03"
  - id: nhlbi-heart-overview
    type: regulatory
    cite: "U.S. National Heart, Lung, and Blood Institute (NHLBI). How the Heart Works."
    url: "https://www.nhlbi.nih.gov/health/heart/anatomy"
    accessed: "2026-06-03"
cross_links:
  - target: 01-human/06-organ/heart
    relation: contains
    note: "The pump driving the entire cardiovascular system."
taxonomy:
  uberon: "UBERON:0004535"
  fma: "FMA:7161"
---

# Cardiovascular system

## Overview

The cardiovascular system is the body's **transport network** — heart, blood vessels, and blood, integrated into two circuits in series that move oxygen, carbon dioxide, nutrients, metabolic waste, hormones, immune cells, and heat to and from every tissue [^openstax-anatomy-19-1]. It is the only system most cells of the body interact with directly: every cell in every other tissue lives within ~100 µm of a capillary, because beyond that distance, diffusion alone cannot keep up.

Functionally, the system has three components — a **pump** (the [heart](../../06-organ/heart/README.md)), a **distribution network** (arteries → arterioles → capillaries → venules → veins), and a **carrier fluid** (blood) — each of which has its own pathologies and its own therapeutic targets, but which function only as a coordinated whole.

## Structure

### The two circuits

The cardiovascular system is **two circuits in series**, sharing the heart as a common pump:

```
                    ┌──────────────┐
                    │  Pulmonary   │   low pressure
                    │  circulation │   (RV peak ~25 mmHg)
                    │   (lungs)    │
                    └──────────────┘
                       ↑        ↓
                  ┌─────────────────┐
                  │  Heart (4 chambers) │
                  │  R-side  ←  L-side  │
                  └─────────────────┘
                       ↑        ↓
                ┌────────────────────┐
                │     Systemic       │   high pressure
                │     circulation    │   (LV peak ~120 mmHg)
                │   (body — brain,   │
                │    muscle, gut,    │
                │    kidneys, …)     │
                └────────────────────┘
```

- **Pulmonary circuit.** Right ventricle → pulmonary trunk → pulmonary arteries → pulmonary capillaries (gas exchange) → pulmonary veins → left atrium. Low pressure, high compliance — the lung capillary bed is enormous and permeable to low driving pressures.
- **Systemic circuit.** Left ventricle → aorta → arteries → arterioles → capillaries (exchange) → venules → veins → vena cavae → right atrium. High pressure, multiple parallel beds (cerebral, coronary, renal, splanchnic, muscular, cutaneous), each with autoregulation matching local flow to local demand.

### Vessels

| Vessel class | Wall composition | Role |
|:---|:---|:---|
| **Elastic arteries** (aorta, large arteries) | Thick tunica media rich in elastin | Damp ventricular pulsations into smoother flow ("Windkessel" effect) |
| **Muscular arteries** | Smooth muscle dominant | Distribute blood; modest tone control |
| **Arterioles** | Smooth muscle dominant; small diameter | Primary site of **systemic vascular resistance** — adjustable, sympathetically innervated |
| **Capillaries** | Single endothelial cell layer + basement membrane | Site of all exchange (gas, nutrients, waste, water, immune cells) |
| **Venules / veins** | Thin walls, low pressure, valves in extremities | Capacitance reservoir — hold ~70 % of blood volume; venous return tunable via tone and pump action |

Total length of human vasculature is on the order of **~100,000 km** (rough estimate); total capillary surface area, ~5,000–7,000 m².

### Blood

About 5 L of blood, distributed roughly as:

| Compartment | Share of total blood volume |
|:---|:---:|
| Systemic veins | ~64 % |
| Pulmonary circulation | ~9 % |
| Heart chambers | ~7 % |
| Systemic arteries | ~13 % |
| Capillaries | ~7 % |

Blood is a tissue in its own right (plasma + erythrocytes + leukocytes + platelets) and will receive its own entry — at the tissue scale.

### Lymphatic system

The lymphatics return to circulation the ~3 L/day of fluid that filters out of capillaries beyond what is reabsorbed at the venous end. Functionally it is the **return-leg complement** to the cardiovascular system; anatomically it merges with venous circulation at the thoracic duct → left subclavian vein. (Lymphatic system entry pending.)

## Function

### Cardiac output

Cardiac output (CO) — the volume of blood pumped per minute — is the system's primary throughput metric:

$$
CO = HR \times SV
$$

| Variable | Resting | Peak exercise |
|:---|:---:|:---:|
| Heart rate (HR) | 60–80 bpm | 180–200 bpm |
| Stroke volume (SV) | ~70 mL | ~120–150 mL |
| **Cardiac output** | **~5 L/min** | **~25 L/min** |

This 5-fold dynamic range allows the system to scale oxygen delivery to demand — the major reason aerobic exercise capacity is set largely by cardiovascular function rather than muscle metabolism.

### Pressure, flow, resistance

Across any vascular bed, the relationship is

$$
\Delta P = Q \times R \quad\text{(an analog of Ohm's law)}
$$

where ΔP is the pressure drop across the bed, Q is flow, and R is resistance [^openstax-anatomy-20-2]. Resistance scales with viscosity (η) and inversely with the **fourth power** of vessel radius (Poiseuille):

$$
R \propto \frac{8 \eta L}{\pi r^4}
$$

This radius-to-the-fourth dependence is why **arterioles dominate systemic resistance** — small changes in arteriolar tone produce large changes in flow distribution. It is also why most cardiovascular drugs that lower blood pressure work by relaxing arterioles (or by reducing cardiac output, or both).

Mean arterial pressure is approximately:

$$
MAP \approx CO \times SVR
$$

(Strictly, MAP ≈ DBP + (1/3)(SBP − DBP); SVR is systemic vascular resistance.) Resting MAP ~93 mmHg in a healthy adult.

### Regulation

The system is regulated on three timescales — beat-to-beat, minutes-to-hours, days-to-weeks:

| Timescale | Mechanism | Effectors |
|:---|:---|:---|
| **Seconds** | Baroreceptor reflex | Carotid sinus + aortic arch baroreceptors → medullary CV centers → autonomic outflow modulating heart rate (β1, M2) and arteriolar tone (α1) |
| **Seconds** | Chemoreceptor reflex | Carotid + aortic chemoreceptors detect hypoxia/hypercapnia → reflex CV/respiratory response |
| **Minutes** | Catecholamines (adrenal medulla) | Epinephrine acts at **β1AR** (cardiac, renin), β2AR (vasodilation, bronchodilation), α1 (vasoconstriction) |
| **Hours** | Renin–angiotensin–aldosterone system (RAAS) | Renal JG cells → renin → angiotensin II (vasoconstrictor) → aldosterone (Na⁺/H₂O retention) |
| **Hours** | Antidiuretic hormone (vasopressin) | Plasma osmolality + volume sensors → posterior pituitary → renal water retention; vascular V1 receptors → vasoconstriction |
| **Days–weeks** | Pressure–natriuresis, vascular remodeling, capillary density adaptation | Kidneys, vasculature, heart |

The β1-adrenergic receptor sits at the intersection of the seconds-to-minutes layer (sympathetic tone) and the cardiac response (chronotropy + inotropy + lusitropy + renin release) — a single molecule with leverage over four of the system's main control variables.

### Local autoregulation

Each major vascular bed has **autoregulation** — a local mechanism that holds flow constant across a range of arterial pressures. Cerebral circulation autoregulates from MAP ~60–150 mmHg; coronary, renal, and splanchnic each have their own ranges. Mechanisms include myogenic responses (smooth muscle contracts when stretched), metabolic vasodilation (adenosine, CO₂, K⁺, lactate), and endothelial signaling (NO, endothelin, prostaglandins).

## Connections

- **Down (constituent organ):** the cardiovascular system `contains` the **[heart](../../06-organ/heart/README.md)** as the pump. (Vasculature and blood will be added as separate entries — large arteries, capillary network, venous network, blood as tissue.)
- **Sideways (interacting systems):**
  - **Respiratory system** — gas exchange in the pulmonary circuit (entry pending).
  - **Renal system** — fluid/electrolyte balance, RAAS regulation (entry pending).
  - **Endocrine system** — catecholamines, ANP/BNP, vasopressin, RAAS (entry pending).
  - **Nervous system** — autonomic CV regulation (entry pending).
  - **Immune system** — leukocyte trafficking via the vascular network; site of vascular inflammation (entry pending).
- **Cross-atlas (planned in Phase 3):** pathogens that act systemically (sepsis, viremia) and medicines that target the system as a whole (vasopressors, vasodilators, anticoagulants) link in here.

## Pathology

System-level cardiovascular disease — pathologies that can't be assigned cleanly to a single organ:

| Disease | Mechanism |
|:---|:---|
| **Hypertension** | Sustained arterial pressure elevation; multifactorial (genetic, sodium, RAAS, sympathetic tone, vascular stiffness). The single largest modifiable risk factor for cardiovascular and cerebrovascular disease globally. |
| **Atherosclerosis** | Lipid deposition + inflammation in the intima of large/medium arteries; progressive plaque growth; rupture or erosion → thrombosis → tissue infarction. The substrate of myocardial infarction, ischemic stroke, and peripheral arterial disease. |
| **Shock states** | Failure of perfusion. Subtypes: hypovolemic (volume loss), cardiogenic (pump failure), distributive (sepsis, anaphylaxis, neurogenic — vasodilation + capillary leak), obstructive (tamponade, pulmonary embolism, tension pneumothorax). |
| **Pulmonary hypertension** | Sustained elevated pulmonary artery pressure → right-heart failure. Several distinct etiologies (idiopathic, drug-induced, left-heart disease, hypoxic, thromboembolic). |
| **Cardiac arrest** | Cessation of effective circulation, typically from ventricular fibrillation or asystole. Survival depends on time-to-defibrillation. |
| **Thromboembolic disease** | Inappropriate clot formation (deep vein thrombosis, pulmonary embolism, atrial-fibrillation–related cardioembolic stroke). Antithrombotic / anticoagulant therapy targets this. |
| **Vasculitis** | Inflammation of vessel walls — broad family (Takayasu, giant cell, ANCA-associated, Kawasaki, …). |

## Variation

- **Sex.** Men have higher rates of coronary artery disease at any given age until menopause; women's risk catches up post-menopause. Some heart-failure phenotypes (HFpEF) are over-represented in women, others (HFrEF) in men.
- **Age.** Arterial stiffness increases with age; baroreceptor sensitivity declines; orthostatic hypotension becomes more common. Hypertension prevalence rises steeply.
- **Genetics + ancestry + environment.** Hypertension, lipid metabolism, and atherosclerosis all show population-level variation in prevalence and treatment response, driven by complex genetic and environmental interactions.
- **Athletic adaptation.** Endurance training produces lower resting heart rate, larger stroke volume, expanded blood volume, and greater capillary density.

## Open questions

- **HFpEF** — pathophysiology and effective therapy remain incomplete despite recent advances (SGLT2 inhibitors, MRAs).
- **Microvascular disease** — coronary microvascular dysfunction, INOCA (ischemia with no obstructive coronary artery disease), and microvascular contributions to dementia and renal disease are under-recognized and undertreated.
- **Vascular aging** — what drives the difference between "biological" and chronological vascular age, and how to slow it, is an active research frontier with implications across cardiovascular and neurological disease.

## See also

- [`heart`](../../06-organ/heart/README.md) — the pump.
- [`myocardium`](../../05-tissue/myocardium/README.md) — the contractile tissue.
- [`cardiomyocyte`](../../04-cellular/cardiomyocyte/README.md) — the contractile cell.
- [`troponin-complex`](../../03-molecular/troponin-complex/README.md) — molecular calcium switch.
- [`beta1-adrenergic-receptor`](../../03-molecular/beta1-adrenergic-receptor/README.md) — primary sympathetic relay.

[^openstax-anatomy-19-1]: OpenStax. *Anatomy & Physiology 2e*, Ch. 19.1: Heart Anatomy. [Read online →](https://openstax.org/books/anatomy-and-physiology-2e/pages/19-1-heart-anatomy)
[^openstax-anatomy-20-2]: OpenStax. *Anatomy & Physiology 2e*, Ch. 20.2: Blood Flow, Blood Pressure, and Resistance. [Read online →](https://openstax.org/books/anatomy-and-physiology-2e/pages/20-2-blood-flow-blood-pressure-and-resistance)
