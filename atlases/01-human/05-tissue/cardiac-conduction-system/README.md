---
schema: human-scale-entry/v1
id: cardiac-conduction-system
name: Cardiac conduction system
atlas: 01-human
scale: 05-tissue
status: draft
last_reviewed: 2026-06-03
summary: "Specialized tissue routing the cardiac impulse: SA node → AV node → Bundle of His → bundle branches → Purkinje fibers. The AV delay (~120 ms PR interval) ensures atrial kick before ventricular systole; Purkinje network synchronizes ventricular activation for efficient ejection."
aliases: ["conduction system", "cardiac impulse system", "specialized conduction tissue"]
sources:
  - id: dobrzynski-2007-sa-node-pacemaking
    type: peer-reviewed
    cite: "Dobrzynski H, Boyett MR, Anderson RH. New insights into pacemaker activity: promoting understanding of sick sinus syndrome. Circulation. 2007;115(14):1921-32."
    doi: "10.1161/CIRCULATIONAHA.106.616011"
    pmid: "17420362"
    url: "https://doi.org/10.1161/CIRCULATIONAHA.106.616011"
  - id: openstax-anatomy-19-2
    type: textbook
    cite: "OpenStax. Anatomy & Physiology 2e, Ch. 19.2: Cardiac Muscle and Electrical Activity."
    url: "https://openstax.org/books/anatomy-and-physiology-2e/pages/19-2-cardiac-muscle-and-electrical-activity"
    accessed: "2026-06-03"
  - id: bers-2002-cardiac-ec-coupling
    type: peer-reviewed
    cite: "Bers DM. Cardiac excitation-contraction coupling. Nature. 2002;415(6868):198-205."
    doi: "10.1038/415198a"
    pmid: "11805843"
    url: "https://doi.org/10.1038/415198a"
cross_links:
  - target: 01-human/06-organ/heart
    relation: part-of
    note: "The cardiac conduction system is the electrical infrastructure of the heart, routing impulses from the SA node to every cardiomyocyte in the ventricles."
  - target: 01-human/04-cellular/sa-node-cell
    relation: composed-of
    note: "SA node cells (automaticity cells) are the cellular component of the sinoatrial node, the dominant pacemaker site within the conduction system."
---

# Cardiac conduction system

## Overview

The cardiac conduction system is a network of **specialized cardiac muscle tissue** whose principal function is to generate, route, delay, and distribute the electrical impulse that initiates each heartbeat. It is distinct from the working myocardium in electrophysiology, gene expression, and architecture: conduction-system cells are smaller, less contractile, and possess ion-channel profiles optimized for either automaticity (pacemaking) or rapid impulse propagation, not for generating mechanical force [^openstax-anatomy-19-2].

The system is architecturally hierarchical:

```
SA node (right atrium, near SVC junction)
    ↓  ~0.05 m/s  [atrial conduction, ~0 ms]
Internodal tracts (anterior, middle, posterior) and Bachmann's bundle (→ LA)
    ↓  0.3–1.0 m/s across atrial myocardium
AV node (lower interatrial septum / AV junction)
    ↓  ~0.02–0.05 m/s  [deliberate slow: introduces ~100–150 ms PR delay]
Bundle of His (penetrates fibrous annulus)
    ↓  ~1.0–2.0 m/s
Left bundle branch (further divides: anterior and posterior fascicles)
Right bundle branch
    ↓  ~2–4 m/s  [fastest cardiac conduction]
Purkinje fibers (subendocardial: apex-to-base, then out to papillary muscles and walls)
    ↓
Working ventricular myocardium  (~0.3–1.0 m/s, cell-to-cell via gap junctions)
```

The total time from SA node firing to complete ventricular activation is approximately **160–200 ms** in the healthy heart — the PR interval on the ECG.

## Structure

### SA Node

The SA node (~15 mm × 5 mm × 1–2 mm) sits in the crista terminalis of the right atrium, at the junction of the superior vena cava. It contains the **leading pacemaker cells** (see [SA node cell](../../04-cellular/sa-node-cell/README.md)) and transitional cells. Its spontaneous rate (60–100 bpm intrinsic) suppresses all downstream pacemakers through overdrive suppression.

### AV Node

The **atrioventricular (AV) node** lies in the Koch triangle of the right atrium (bounded by the tricuspid annulus, tendon of Todaro, and coronary sinus os). Key properties:

| Feature | Value / significance |
|:---|:---|
| **Conduction velocity** | ~0.02–0.05 m/s — the slowest in the conduction system |
| **Intrinsic automaticity** | ~40–60 bpm (junctional escape rate if SA node fails) |
| **Refractory period** | Long — limits maximum ventricular rate in atrial flutter/fibrillation |
| **Blood supply** | AV nodal artery, usually from RCA (~90%) or LCx (left-dominant) |
| **Decremental conduction** | APs slow progressively with faster rates — Wenckebach phenomenon |

The AV node delay (~100–150 ms) is physiologically essential: it ensures the atria have time to contract and fill the ventricles before the ventricular contraction begins.

### Bundle of His, Bundle Branches, Purkinje Fibers

| Structure | Conduction velocity | Role |
|:---|:---:|:---|
| **Bundle of His** | ~1–2 m/s | Penetrates the fibrous skeleton (electrically insulating annuli) — only normal electrical connection between atria and ventricles |
| **Right bundle branch** | ~2–4 m/s | Runs along right side of interventricular septum to right ventricular apex |
| **Left bundle branch (LBB)** | ~2–4 m/s | Broad, fan-like; divides early into **anterior** (LAF) and **posterior** (LPF) fascicles |
| **Purkinje fibers** | ~2–4 m/s | Subendocardial network; deliver wavefront to apex first, then walls; ensure nearly simultaneous ventricular activation |

Purkinje fibers are the largest cardiomyocyte-lineage cells (up to 80 µm diameter, vs. 10–20 µm for ventricular cells), have abundant glycogen, sparse myofibrils, and express very high levels of Cx40 (connexin-40, a high-conductance gap junction isoform) — enabling rapid cell-to-cell conduction.

### Fibrous Skeleton as Electrical Insulator

The **cardiac fibrous skeleton** (rings of collagen at the AV and arterial orifices, plus the central fibrous body) electrically insulates the atria from the ventricles everywhere except the Bundle of His. This isolation is what makes the AV delay possible and what makes accessory pathways (which bypass this insulation, as in Wolff-Parkinson-White) pathological.

## Function

### Ensuring Sequential AV Activation

The most important function of the conduction system is **temporal sequencing**:

1. SA node fires → atria depolarize and contract → blood moves from atria to ventricles (~20–25% of EDV at rest).
2. AV node delay (~120 ms) → ventricles are filled before they contract.
3. Purkinje system → ventricles depolarize near-simultaneously from apex upward → organized wringing contraction → efficient ejection.

Disruption of any part of this sequence alters cardiac output:
- **Loss of AV synchrony** (e.g., complete AV block, atrial fibrillation) → loss of atrial kick → up to 20–25% reduction in CO at rest (more at high HR)
- **Left bundle branch block (LBBB)** → delayed LV activation → dyssynchronous contraction → reduced EF → CRT (cardiac resynchronization therapy) can restore synchrony

### Overdrive Suppression

When the SA node fires at 75 bpm, it constantly overrides the AV node (45–60 bpm intrinsic) and Purkinje fibers (20–40 bpm). This **overdrive suppression** occurs because faster pacing accumulates Na⁺ inside the cell (from repeated rapid depolarizations), activating the Na⁺/K⁺-ATPase more aggressively, which hyperpolarizes the downstream pacemaker — keeping it silent. When the SA node fails, the downstream pacemaker takes a moment to escape.

## Connections

- **Part-of** → [Heart](../../06-organ/heart/README.md): The conduction system is the heart's electrical infrastructure; its dysfunction is responsible for a large fraction of cardiac arrhythmias and sudden cardiac death.
- **Composed-of** → [SA node cell](../../04-cellular/sa-node-cell/README.md): Automaticity cells generate the primary impulse; different cell types populate each conduction system segment.

## Pathology

| Disease | Mechanism | ECG signature |
|:---|:---|:---|
| **Sick sinus syndrome** | SA node failure (fibrosis, aging, ischemia) → bradycardia, sinus arrest, sinoatrial exit block | Sinus bradycardia, pauses, tachy-brady syndrome |
| **1st-degree AV block** | Slowed AV nodal conduction | PR > 200 ms |
| **2nd-degree AV block — Mobitz I (Wenckebach)** | Progressive AV nodal fatigue → dropped beat | Progressively lengthening PR → dropped QRS |
| **2nd-degree AV block — Mobitz II** | Below-nodal block (bundle branches) | Fixed PR, intermittently dropped QRS |
| **3rd-degree (complete) AV block** | No conduction from atria to ventricles | P waves and QRS dissociated; escape rhythm at 20–40 bpm |
| **Left bundle branch block (LBBB)** | Block in LBB; LV depolarizes late via right-to-left spread | Wide QRS (≥120 ms), notched R in lateral leads |
| **Right bundle branch block (RBBB)** | Block in RBB; RV depolarizes late | Wide QRS, rsR' in V1, wide S in lateral leads |
| **Wolff-Parkinson-White (WPW)** | Accessory pathway (bundle of Kent) bypasses AV node → premature ventricular activation | Delta wave, short PR; risk of rapid conduction of atrial flutter/fibrillation → VF |

## Open Questions

- **Regeneration of the conduction system.** After ischemic injury, Purkinje fibers do not regenerate. Whether stem cells or reprogrammed cells can restore normal conduction tissue is not established.
- **Genetic basis of conduction disease.** Mutations in `SCN5A` (Nav1.5), `SCN1B`, `KCNQ1`, `HCN4`, and gap junction genes (Cx40, Cx43) cause inherited conduction disorders. The full genetic map remains incomplete.
- **AV node heterogeneity and dual-pathway physiology.** The AV node contains anatomically and functionally distinct fast and slow pathways — the substrate for AV nodal re-entrant tachycardia (AVNRT, the most common supraventricular tachycardia). The structural basis of dual-pathway conduction is debated [^dobrzynski-2007-sa-node-pacemaking].

## See Also

- [Heart](../../06-organ/heart/README.md)
- [SA node cell](../../04-cellular/sa-node-cell/README.md)
- [Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)

[^dobrzynski-2007-sa-node-pacemaking]: Dobrzynski H, Boyett MR, Anderson RH. New insights into pacemaker activity. *Circulation.* 2007;115(14):1921-32. [doi:10.1161/CIRCULATIONAHA.106.616011](https://doi.org/10.1161/CIRCULATIONAHA.106.616011) · [PubMed 17420362](https://pubmed.ncbi.nlm.nih.gov/17420362/)
[^openstax-anatomy-19-2]: OpenStax. *Anatomy & Physiology 2e*, Ch. 19.2: Cardiac Muscle and Electrical Activity. [Read online →](https://openstax.org/books/anatomy-and-physiology-2e/pages/19-2-cardiac-muscle-and-electrical-activity)
[^bers-2002-cardiac-ec-coupling]: Bers DM. Cardiac excitation-contraction coupling. *Nature.* 2002;415(6868):198-205. [doi:10.1038/415198a](https://doi.org/10.1038/415198a) · [PubMed 11805843](https://pubmed.ncbi.nlm.nih.gov/11805843/)
