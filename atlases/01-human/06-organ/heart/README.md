---
schema: human-scale-entry/v1
id: heart
name: Heart
atlas: 01-human
scale: 06-organ
status: draft
last_reviewed: 2026-06-03
summary: "The four-chambered muscular pump of the cardiovascular system. Beats ~100,000 times per day to circulate ~7,500 L of blood through the body's vasculature."
aliases: ["cor", "cardiac muscle organ"]
sources:
  - id: openstax-anatomy-19-1
    type: textbook
    cite: "OpenStax. Anatomy & Physiology 2e, Ch. 19.1: Heart Anatomy."
    url: "https://openstax.org/books/anatomy-and-physiology-2e/pages/19-1-heart-anatomy"
    accessed: "2026-06-03"
  - id: openstax-anatomy-19-3
    type: textbook
    cite: "OpenStax. Anatomy & Physiology 2e, Ch. 19.3: Cardiac Cycle."
    url: "https://openstax.org/books/anatomy-and-physiology-2e/pages/19-3-cardiac-cycle"
    accessed: "2026-06-03"
  - id: openstax-anatomy-19-4
    type: textbook
    cite: "OpenStax. Anatomy & Physiology 2e, Ch. 19.4: Cardiac Physiology."
    url: "https://openstax.org/books/anatomy-and-physiology-2e/pages/19-4-cardiac-physiology"
    accessed: "2026-06-03"
  - id: bers-2002-cardiac-ec-coupling
    type: peer-reviewed
    cite: "Bers DM. Cardiac excitation-contraction coupling. Nature. 2002;415(6868):198-205."
    doi: "10.1038/415198a"
    pmid: "11805843"
  - id: heidenreich-2022-hf-guideline
    type: clinical-guideline
    cite: "Heidenreich PA, Bozkurt B, Aguilar D, et al. 2022 AHA/ACC/HFSA Guideline for the Management of Heart Failure. Circulation. 2022;145(18):e895-e1032."
    doi: "10.1161/CIR.0000000000001063"
    pmid: "35363499"
  - id: nhlbi-heart-overview
    type: regulatory
    cite: "U.S. National Heart, Lung, and Blood Institute (NHLBI). How the Heart Works."
    url: "https://www.nhlbi.nih.gov/health/heart/anatomy"
    accessed: "2026-06-03"
cross_links:
  - target: 01-human/05-tissue/myocardium
    relation: contains
    note: "The bulk of the heart wall — the contractile layer."
  - target: 01-human/07-system/cardiovascular-system
    relation: part-of
    note: "The heart is the pump driving the cardiovascular system."
  - target: 01-human/05-tissue/endocardium
    relation: contains
    note: "The endocardium lines all four chambers and valve surfaces, forming the blood-contacting barrier."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: contains
    note: "The conduction system (SA node → AV node → His–Purkinje) generates and distributes the electrical impulse that coordinates every heartbeat."
  - target: 01-human/04-cellular/sa-node-cell
    relation: contains
    note: "SA node pacemaker cells reside in the right atrium and set the intrinsic heart rate."
  - target: 01-human/08-whole-body/human-body
    relation: part-of
    note: "The heart is a component of the cardiovascular system and of the integrated human body."
taxonomy:
  uberon: "UBERON:0000948"
  fma: "FMA:7088"
simulator: docs/heart.html
---

# Heart

## Overview

The heart is a four-chambered muscular organ that pumps blood through the body's vasculature, sustaining the circulation that delivers oxygen, nutrients, hormones, and immune cells to every tissue and removes carbon dioxide and metabolic waste [^openstax-anatomy-19-1]. It sits in the middle mediastinum of the thoracic cavity, behind the sternum and between the lungs, with its apex pointing inferiorly and to the left. In an adult at rest, the heart beats roughly 60–100 times per minute, ejecting about 70 mL of blood with each beat — a cardiac output near 5 L/min, the entire blood volume circulated approximately once every minute [^openstax-anatomy-19-4].

Functionally, the heart is two pumps in series: the **right heart** (right atrium + right ventricle) drives the **pulmonary circulation**, sending deoxygenated blood through the lungs; the **left heart** (left atrium + left ventricle) drives the **systemic circulation**, sending oxygenated blood to the rest of the body. The two pumps share a wall (the interventricular septum) and beat in synchrony but face very different mechanical loads — the left ventricle works against systemic resistance about five times higher than the pulmonary, and is correspondingly thicker.

## Structure

### Gross anatomy

| Component | Description |
|:---|:---|
| **Chambers** | Right atrium, right ventricle, left atrium, left ventricle. Atria are receiving chambers (thinner walls, lower pressure); ventricles are output chambers (thicker walls, higher pressure). |
| **Valves** | **Tricuspid** (RA → RV), **pulmonary** (RV → pulmonary artery), **mitral / bicuspid** (LA → LV), **aortic** (LV → aorta). The atrioventricular valves are anchored by chordae tendineae to papillary muscles; the semilunar valves are passive. |
| **Septa** | Interatrial septum, interventricular septum — separate left and right circulations after birth. |
| **Wall layers** | **Endocardium** (innermost: endothelium + connective tissue, lines chambers and valves), **myocardium** (middle: cardiac muscle, the bulk of the wall — see [`myocardium`](../../05-tissue/myocardium/README.md)), **epicardium** (outermost: visceral pericardium, mesothelium + connective tissue + coronary vasculature). |
| **Pericardium** | Fibrous sac surrounding the whole organ. Inner serous layer (visceral = epicardium; parietal = lining of fibrous sac) with pericardial fluid between, allowing low-friction motion. |
| **Coronary vasculature** | **Left coronary artery** branches into the left anterior descending (LAD) and circumflex (LCx); the **right coronary artery** (RCA) supplies the right side and, in most people ("right-dominant"), the posterior descending. Coronary venous return drains via the coronary sinus into the right atrium. |
| **Conduction system** | **Sinoatrial (SA) node** in the right atrium initiates the heartbeat (~60–100 bpm intrinsic rate). Impulse spreads across atria → **atrioventricular (AV) node** at the AV junction (introduces a ~0.1 s delay) → **bundle of His** → left and right bundle branches → **Purkinje fibers** that propagate the wavefront rapidly across the ventricular endocardium. |

Adult heart mass is typically 250–350 g; volume varies with body size, training status, and pathology. The chamber walls are not uniformly thick — the left ventricular wall is roughly 10–12 mm at end-diastole, the right ventricular wall 3–5 mm, the atria 2–3 mm.

### Sub-gross structure

Below the organ scale, the heart is built from coordinated tissues:

- **Working myocardium** — the contractile muscle of atria and ventricles. See **[Myocardium](../../05-tissue/myocardium/README.md)**.
- **Endocardium** — endothelial lining, continuous with the endothelium of the great vessels. *Entry pending.*
- **Epicardium / pericardium** — outer protective layers. *Entry pending.*
- **Valve leaflets and chordae** — connective-tissue specializations. *Entry pending.*
- **Cardiac skeleton** — fibrous rings at the AV and arterial junctions, electrically insulating atria from ventricles and anchoring valves. *Entry pending.*

## Function

### The cardiac cycle

Each heartbeat is one rotation through a four-phase cycle, lasting about 0.8 s at a resting heart rate of 75 bpm [^openstax-anatomy-19-3]:

1. **Atrial systole / late ventricular filling** (~0.1 s) — atria contract, topping off the ventricles with the final ~20–25 % of their end-diastolic volume.
2. **Isovolumetric contraction** (~0.05 s) — ventricles begin to contract; pressure rises; AV valves snap shut (heart sound **S1**). Aortic and pulmonary valves remain closed because ventricular pressure has not yet exceeded arterial pressure.
3. **Ejection** (~0.3 s) — ventricular pressure exceeds arterial; semilunar valves open; blood is ejected. The volume ejected per beat is the **stroke volume** (≈ 70 mL at rest); the fraction ejected of end-diastolic volume is the **ejection fraction** (normally 55–70 %).
4. **Isovolumetric relaxation + early/passive filling** (~0.35 s) — ventricles relax; pressure drops; semilunar valves close (heart sound **S2**). When ventricular pressure drops below atrial, AV valves open and passive filling resumes.

### Excitation–contraction coupling

The ventricles do not contract because they are filled — they contract because they are *commanded to* by an electrical signal that propagates through the conduction system and triggers calcium release inside every cardiomyocyte simultaneously. The mechanism, **excitation–contraction coupling**, links membrane depolarization to mechanical force [^bers-2002-cardiac-ec-coupling]:

1. Depolarization arrives → opens voltage-gated **L-type Ca²⁺ channels** in the sarcolemma and T-tubules.
2. Trigger Ca²⁺ entry causes a much larger **calcium-induced calcium release (CICR)** from the sarcoplasmic reticulum via ryanodine receptors (RyR2).
3. Cytosolic Ca²⁺ binds **troponin C** on the thin filament — see **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — moving tropomyosin off myosin-binding sites.
4. Myosin cross-bridges cycle, pulling actin filaments inward; the sarcomere shortens; the cell contracts.
5. Relaxation requires Ca²⁺ removal: **SERCA2a** pumps Ca²⁺ back into the sarcoplasmic reticulum, and the **Na⁺/Ca²⁺ exchanger** (NCX) extrudes the residual to the extracellular space.

This entire sequence happens hundreds of millions of times per heart over a lifetime, in step with every heartbeat.

### Output regulation

Cardiac output (CO = HR × SV) is tuned moment-to-moment by:

- **Heart rate** — set by the SA node, modulated by autonomic tone. Sympathetic input via **β1-adrenergic receptors** — see **[β1-adrenergic receptor](../../03-molecular/beta1-adrenergic-receptor/README.md)** — accelerates the SA node and increases AV conduction; parasympathetic input via the vagus nerve and muscarinic M2 receptors slows the heart.
- **Contractility (inotropy)** — how forcefully each fiber shortens at a given preload. Sympathetic activation raises contractility primarily through β1-mediated PKA phosphorylation of L-type Ca²⁺ channels, RyR2, phospholamban, and troponin I.
- **Preload** — venous filling pressure stretching the ventricle at end-diastole. Within physiological range, increased preload increases stroke volume (the **Frank–Starling** relationship).
- **Afterload** — the arterial pressure the ventricle must overcome to eject. Higher afterload reduces stroke volume at a given preload and contractility.

## Connections

- **Down (constituent tissue):** the heart `contains` the **[myocardium](../../05-tissue/myocardium/README.md)** — and, in entries to come, the endocardium, epicardium, valve tissue, and the conduction-system tissue.
- **Up (containing system):** the heart is `part-of` the **[cardiovascular system](../../07-system/cardiovascular-system/README.md)**, which integrates the heart with the systemic and pulmonary vasculature and the blood itself.
- **Cross-atlas (planned in Phase 3):** entries in the Pathogen Atlas and Medicine Atlas will link into the heart at the appropriate scale — for example, **Coxsackievirus B** damages the heart at the cellular scale (cardiomyocyte cytolysis) and **metoprolol** modulates the heart at the molecular scale (β1-adrenergic blockade).

## Pathology

Heart disease is the leading cause of death globally. Major categories:

| Category | Mechanism |
|:---|:---|
| **Coronary artery disease / myocardial infarction** | Atherosclerotic narrowing or acute thrombotic occlusion of a coronary artery; downstream myocardium becomes ischemic and, if perfusion is not restored, infarcts. |
| **Heart failure** | The heart cannot deliver adequate cardiac output at acceptable filling pressures. Subdivided by ejection fraction: **HFrEF** (reduced EF), **HFmrEF** (mildly reduced), **HFpEF** (preserved EF). Driven by ischemic, hypertensive, valvular, infiltrative, genetic, infectious, and idiopathic causes [^heidenreich-2022-hf-guideline]. |
| **Hypertensive heart disease** | Chronic afterload elevation drives left ventricular hypertrophy; over time, diastolic dysfunction and fibrosis lead to HFpEF. |
| **Valvular disease** | **Stenosis** (narrowed valve, increased resistance) or **regurgitation** (incompetent valve, backflow). Aortic stenosis and mitral regurgitation are the commonest in adults. |
| **Arrhythmias** | Disorders of impulse formation or conduction. Atrial fibrillation (chaotic atrial activity), ventricular tachycardia, ventricular fibrillation (typically lethal without defibrillation), AV block, bundle-branch block, long-QT syndrome. |
| **Cardiomyopathies** | Primary disease of myocardium itself. **DCM** (dilated), **HCM** (hypertrophic, often genetic — `MYH7`, `MYBPC3` mutations), **RCM** (restrictive), **ARVC** (arrhythmogenic right ventricular). |
| **Myocarditis** | Inflammation of the myocardium, classically viral (e.g., Coxsackievirus B, parvovirus B19, SARS-CoV-2) but also autoimmune or drug-induced. |
| **Endocarditis** | Infection of the endocardium, usually a valve. *Streptococcus viridans*, *Staphylococcus aureus*, *Enterococcus* are common organisms. |
| **Pericarditis / pericardial effusion / tamponade** | Inflammation of the pericardium; fluid accumulation in the pericardial sac can compress the heart and impair filling. |
| **Congenital heart disease** | Structural anomalies present at birth: ventricular and atrial septal defects, tetralogy of Fallot, coarctation of the aorta, transposition of the great arteries. |

Each of these will eventually have its own entry — typically in the Clinical Atlas (planned), with cross-links into the relevant scales of this Human Atlas, into the Pathogen Atlas where infectious, and into the Medicine Atlas for treatments.

## Variation

A model of *the* heart that ignores variation is a model of one person, not of human biology. Significant axes of natural variation:

- **Sex.** Male hearts average ~25–30 % more mass than female at the same body size; women have higher resting heart rates (by ~3–5 bpm), shorter QT intervals after correction, and different heart-failure phenotypes (HFpEF more common in women, HFrEF more common in men).
- **Age.** Heart-rate variability declines with age; LV diastolic function stiffens; arterial stiffness increases afterload. Resting heart rate is highest in newborns (~120–160 bpm) and falls through childhood.
- **Athletic training.** Endurance athletes develop physiological **eccentric hypertrophy** — chamber dilation with proportional wall thickening, a healthy adaptation distinguishable from pathological HCM by absence of fibrosis and preserved diastolic function. Resting heart rates of 40–50 bpm are common.
- **Genetics.** ~1 in 500 people carry a hypertrophic cardiomyopathy mutation, most commonly in the genes for sarcomeric proteins (`MYH7`, `MYBPC3`, `TNNT2`, `TNNI3`). Penetrance and expressivity vary widely. Long-QT syndromes have multiple subtypes, each from a different ion-channel gene.
- **Population.** Heart-failure phenotypes, hypertension severity, response to common cardiovascular drugs (e.g., ACE inhibitors, β-blockers, hydralazine + isosorbide dinitrate), and prevalence of specific cardiomyopathies differ across ancestral populations — driven by genetic variation, epigenetic factors, and social determinants of health that all converge on heart biology.
- **Anatomic.** Coronary dominance is right-dominant in ~85 % of people, left-dominant in ~7 %, codominant in ~8 %. Variant accessory conduction pathways (e.g., Wolff–Parkinson–White) occur in roughly 0.1–0.3 %.

## Open questions

- **HFpEF mechanism.** Heart failure with preserved ejection fraction is heterogeneous and only partially understood mechanistically; targeted therapies remain limited compared with HFrEF.
- **Cardiomyocyte regeneration.** Adult mammalian cardiomyocytes have very limited proliferative capacity; whether this can be safely enhanced therapeutically (and which signals — Hippo, Erbb2, others — to target) is an active research area.
- **Genotype–phenotype mapping in HCM.** Two carriers of the same `MYH7` variant can have radically different clinical courses; modifier genes and environmental factors are incompletely characterized.
- **Sex-specific cardiovascular biology.** Most basic cardiac research has historically used male animal models; sex-specific mechanisms in arrhythmia, heart failure, and drug response are an open frontier.
- **Long-term sequelae of viral myocarditis.** Distinguishing transient inflammation from progression to dilated cardiomyopathy after a single viral hit remains imperfect.

## See also

- [`atlases/01-human/05-tissue/myocardium`](../../05-tissue/myocardium/README.md) — the contractile tissue of the heart wall.
- [`atlases/01-human/04-cellular/cardiomyocyte`](../../04-cellular/cardiomyocyte/README.md) — the contractile cell.
- [`atlases/01-human/03-molecular/troponin-complex`](../../03-molecular/troponin-complex/README.md) — calcium switch on the thin filament.
- [`atlases/01-human/03-molecular/beta1-adrenergic-receptor`](../../03-molecular/beta1-adrenergic-receptor/README.md) — receptor through which the sympathetic nervous system tunes the heart.
- [`atlases/01-human/07-system/cardiovascular-system`](../../07-system/cardiovascular-system/README.md) — the system the heart drives.
- [Schema](../../../../schemas/human-scale-entry.schema.md) this entry conforms to.

[^openstax-anatomy-19-1]: OpenStax. *Anatomy & Physiology 2e*, Ch. 19.1: Heart Anatomy. [Read online →](https://openstax.org/books/anatomy-and-physiology-2e/pages/19-1-heart-anatomy)
[^openstax-anatomy-19-3]: OpenStax. *Anatomy & Physiology 2e*, Ch. 19.3: Cardiac Cycle. [Read online →](https://openstax.org/books/anatomy-and-physiology-2e/pages/19-3-cardiac-cycle)
[^openstax-anatomy-19-4]: OpenStax. *Anatomy & Physiology 2e*, Ch. 19.4: Cardiac Physiology. [Read online →](https://openstax.org/books/anatomy-and-physiology-2e/pages/19-4-cardiac-physiology)
[^bers-2002-cardiac-ec-coupling]: Bers DM. Cardiac excitation-contraction coupling. *Nature.* 2002;415(6868):198-205. [doi:10.1038/415198a](https://doi.org/10.1038/415198a) · [PubMed 11805843](https://pubmed.ncbi.nlm.nih.gov/11805843/)
[^heidenreich-2022-hf-guideline]: Heidenreich PA, Bozkurt B, Aguilar D, et al. 2022 AHA/ACC/HFSA Guideline for the Management of Heart Failure. *Circulation.* 2022;145(18):e895–e1032. [doi:10.1161/CIR.0000000000001063](https://doi.org/10.1161/CIR.0000000000001063) · [PubMed 35363499](https://pubmed.ncbi.nlm.nih.gov/35363499/)
