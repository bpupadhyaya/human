---
schema: human-scale-entry/v1
id: sa-node-cell
name: SA node cell
atlas: 01-human
scale: 04-cellular
status: draft
last_reviewed: 2026-06-03
summary: "SA node pacemaker cell with no stable resting potential. Spontaneous depolarization via funny current (HCN4/I_f), L-type and T-type Ca²⁺ channels, and Ca-clock SR release. Intrinsic rate 60–100 bpm; tuned by sympathetic (β1-AR → +chronotropy) and vagal (M2 → −chronotropy) input."
aliases: ["sinoatrial node cell", "SA nodal cell", "pacemaker cell", "P cell"]
sources:
  - id: difrancesco-2010-funny-current
    type: peer-reviewed
    cite: "DiFrancesco D. The role of the funny current in pacemaker activity. Circ Res. 2010;106(3):434-46."
    doi: "10.1161/CIRCRESAHA.109.208041"
    pmid: "20167941"
    url: "https://doi.org/10.1161/CIRCRESAHA.109.208041"
  - id: boyett-2000-sa-node
    type: peer-reviewed
    cite: "Boyett MR, Honjo H, Kodama I. The sinoatrial node, a heterogeneous pacemaker structure. Cardiovasc Res. 2000;47(4):658-87."
    doi: "10.1016/S0008-6363(00)00135-8"
    pmid: "10974216"
    url: "https://doi.org/10.1016/S0008-6363(00)00135-8"
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
cross_links:
  - target: 01-human/06-organ/heart
    relation: part-of
    note: "SA node cells are the dominant automaticity cells of the sinoatrial node, which resides in the right atrium and generates the electrical impulse that initiates every heartbeat."
  - target: 01-human/03-molecular/beta1-adrenergic-receptor
    relation: expresses
    note: "SA node cells express β1-AR; Gαs/PKA signaling phosphorylates HCN4 and Cav1.2, shifting If activation and increasing action potential frequency — positive chronotropy."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: part-of
    note: "SA node cells are the automaticity cells of the sinoatrial node — the leading pacemaker and first node of the cardiac conduction system."
  - target: 01-human/03-molecular/hcn4
    relation: expresses
    note: "HCN4 is the dominant pacemaker channel of SA node cells; its hyperpolarisation-activated current (I_f) drives diastolic depolarisation and sets intrinsic heart rate."
  - target: 01-human/03-molecular/ncx1
    relation: expresses
    note: "NCX1 is expressed in SA node pacemaker cells; reverse-mode NCX1 generates an inward depolarising current during Ca²⁺ spark events (Ca²⁺ clock), contributing to pacemaker automaticity."
  - target: 01-human/02-atomic/potassium
    relation: modulated-by
    evidence: difrancesco-2010-funny-current
    note: "IKr (hERG) and IKs (KCNQ1) repolarise the SA node AP; EK sets the maximum diastolic potential; hypokalaemia prolongs repolarisation and alters pacemaking rate."
---

# SA node cell

## Overview

The sinoatrial (SA) node cell is the heart's **automaticity cell** — a specialized cardiomyocyte-lineage cell that, unlike working ventricular or atrial cardiomyocytes, has **no stable resting potential**. Instead, it undergoes a rhythmic spontaneous depolarization that generates action potentials at a rate of approximately 60–100 beats per minute intrinsically, establishing the heart's rhythm [^openstax-anatomy-19-2]. The SA node, embedded in the crista terminalis of the right atrium near the entry of the superior vena cava, is the hierarchy-dominant pacemaker of the entire heart — its rate overrides the slower intrinsic rates of the AV node (~40–60 bpm) and Purkinje fibers (~20–40 bpm).

SA node cells are anatomically and electrophysiologically distinct from working cardiomyocytes:
- **Smaller cells** (~5–10 µm diameter vs. 10–20 µm for ventricular myocytes)
- **No T-tubules** — Ca²⁺ release relies on peripheral SR
- **No fast Na⁺ current** (Nav1.5 absent or very low) — upstroke depends on ICaL (L-type Ca²⁺)
- **Absent stable Phase 4** — spontaneous diastolic depolarization drives automaticity

## Structure

### Key Ion Channels

| Channel | Gene | Current | Role in pacemaking |
|:---|:---:|:---:|:---|
| **HCN4** | `HCN4` | I_f ("funny current") | Activated by hyperpolarization at end of action potential; depolarizing inward current (mixed Na⁺/K⁺) drives spontaneous diastolic depolarization |
| **L-type Ca²⁺ (Cav1.2)** | `CACNA1C` | ICaL | Generates the action potential upstroke (replaces INa in SA node) |
| **T-type Ca²⁺ (Cav3.1)** | `CACNA1G` | ICaT | Contributes to late diastolic depolarization |
| **IKr (hERG)** | `KCNH2` | IKr | Repolarization |
| **IKs (KCNQ1/KCNE1)** | `KCNQ1` | IKs | Repolarization |
| **IKAch (Kir3.1/3.4)** | `KCNJ3/5` | IKAch | Parasympathetic: Gi → opens IKAch → hyperpolarization → slows rate |

### The Funny Current (I_f) and HCN4

The **funny current (I_f)** is the defining current of pacemaker cells, discovered and characterized by Dario DiFrancesco [^difrancesco-2010-funny-current]. It is "funny" because it activates upon **hyperpolarization** (opposite to most voltage-gated channels) and carries a **mixed inward Na⁺/K⁺ current** at physiological potentials.

HCN4 (Hyperpolarization-activated Cyclic Nucleotide-gated channel 4) is the dominant HCN isoform in the SA node:
- Activates between approximately **−40 mV and −70 mV**
- Produces a slow inward current that depolarizes the membrane during phase 4
- Is directly gated by cAMP binding to its cyclic nucleotide-binding domain (CNBD): when cAMP binds, the activation curve shifts ~+10 mV → channels open at less negative potentials → faster depolarization → higher firing rate

This cAMP sensitivity is the molecular mechanism of **sympathetic chronotropy**.

### The Calcium Clock

SA node pacemaking involves a dual-oscillator system [^boyett-2000-sa-node]:

1. **Membrane clock (M-clock):** voltage-dependent cycling of ion channels (I_f, ICaL, ICaT, IKr, IKs) producing the diastolic depolarization and action potential.
2. **Calcium clock (Ca-clock):** rhythmic, spontaneous SR Ca²⁺ release events (Ca²⁺ sparks via RyR) during late diastole. These sparks activate NCX forward mode (Ca²⁺ out, 3 Na⁺ in) → net inward current → additional late-diastolic depolarization → assists in triggering the next action potential.

The two clocks are mutually entrained and together produce robust, physiologically tunable pacemaking.

## Function

### Action Potential Shape

The SA node action potential is markedly different from the working cardiomyocyte AP:

| Phase | Working ventricular cell | SA node cell |
|:---:|:---|:---|
| **Phase 4 (diastole)** | Stable at ~−85 mV (IK1 dominant) | Slow depolarization from ~−60 mV (I_f, ICaT, Ca-clock) |
| **Phase 0 (upstroke)** | Rapid (+200 V/s) via Nav1.5 | Slow (+1–10 V/s) via ICaL |
| **Peak** | ~+30 mV | ~+15 mV |
| **Repolarization** | IKr, IKs | IKr, IKs |
| **Maximum diastolic potential** | ~−85 mV | ~−60 mV |

The absence of a rapid Nav1.5 upstroke and a stable resting potential is what makes SA node cells intrinsically slow-conducting but reliably autonomous.

### Autonomic Modulation

The heart rate set by the SA node is continuously tuned by the autonomic nervous system:

**Sympathetic (positive chronotropy):**
- Norepinephrine (or epinephrine) → β1-AR → Gαs → adenylyl cyclase → ↑cAMP → PKA
- cAMP directly activates HCN4 (shifts activation + 10 mV → more I_f at any given voltage → faster phase 4)
- PKA phosphorylates Cav1.2 (faster, larger ICaL upstroke) and RyR2 (more Ca-clock Ca²⁺ sparks)
- Net: heart rate rises from ~75 to 130–200 bpm during exercise/stress

**Parasympathetic (negative chronotropy):**
- Acetylcholine → M2 muscarinic receptor → Gi/Go → ↓cAMP (reduced HCN4 I_f) + direct IKAch activation
- IKAch (Kir3.1/3.4 inward-rectifier) opens → outward K⁺ current → hyperpolarizes membrane → slower diastolic depolarization → fewer APs per minute
- Net: heart rate slows from 75 to 40–50 bpm in trained athletes at rest (high vagal tone)

## Lifecycle

SA node cells are postmitotic in adults. Automaticity is maintained throughout life, though:
- The intrinsic rate declines with age (~1–2 bpm per decade)
- HCN4 expression may decline subtly with age, contributing to lower maximum HR in older adults
- SA node fibrosis (senile amyloid, calcification) is a common cause of sick sinus syndrome in the elderly

## Connections

- **Part-of** → [Heart](../../06-organ/heart/README.md): SA node cells constitute the dominant automaticity center of the cardiac conduction system, initiating each heartbeat.
- **Expresses** → [β1-adrenergic receptor](../../03-molecular/beta1-adrenergic-receptor/README.md): β1-AR on SA node cells relays sympathetic input → cAMP → HCN4 activation → positive chronotropy.
- **Composed of (conduction system)** → [Cardiac conduction system](../../05-tissue/cardiac-conduction-system/README.md): SA node cells are the cellular component of the SA node within the broader conduction system tissue.

## Pathology

| Disease | SA node mechanism |
|:---|:---|
| **Sick sinus syndrome (SSS)** | Structural or electrical dysfunction of the SA node — sinus bradycardia, sinus arrest, sinoatrial exit block. Most common cause of permanent pacemaker implantation in the elderly. |
| **Inappropriate sinus tachycardia (IST)** | Enhanced I_f or autonomic dysregulation; HCN4 gain-of-function rare. Treatment: ivabradine (I_f blocker), beta-blockers. |
| **Ivabradine pharmacology** | Ivabradine is a specific HCN4 I_f blocker — reduces HR without affecting contractility. Used in HFrEF with persistent tachycardia on beta-blockers, and in IST. |
| **Long COVID HRV/POTS** | Dysautonomia with inappropriate sinus tachycardia on standing is one of the most common cardiac symptoms of long COVID. SA node hyperactivation via sympathetic excess. |

## Open Questions

- **Heterogeneity of SA node cells.** The SA node contains a gradient from leading pacemaker cells (center: slower, smallest, highest I_f) to transitional cells (periphery: larger, faster upstroke). How the "leading pacemaker site" shifts dynamically with autonomic state is not fully characterized [^dobrzynski-2007-sa-node-pacemaking].
- **Regeneration.** Can functional SA node pacemaker cells be regenerated or implanted as a biological pacemaker? Progress has been made in reprogramming atrial cells to SA-node-like phenotype with HCN4 overexpression, but clinical application remains distant.

## See Also

- [Heart](../../06-organ/heart/README.md)
- [β1-adrenergic receptor](../../03-molecular/beta1-adrenergic-receptor/README.md)
- [Cardiac conduction system](../../05-tissue/cardiac-conduction-system/README.md)

[^difrancesco-2010-funny-current]: DiFrancesco D. The role of the funny current in pacemaker activity. *Circ Res.* 2010;106(3):434-46. [doi:10.1161/CIRCRESAHA.109.208041](https://doi.org/10.1161/CIRCRESAHA.109.208041) · [PubMed 20167941](https://pubmed.ncbi.nlm.nih.gov/20167941/)
[^boyett-2000-sa-node]: Boyett MR, Honjo H, Kodama I. The sinoatrial node, a heterogeneous pacemaker structure. *Cardiovasc Res.* 2000;47(4):658-87. [doi:10.1016/S0008-6363(00)00135-8](https://doi.org/10.1016/S0008-6363(00)00135-8) · [PubMed 10974216](https://pubmed.ncbi.nlm.nih.gov/10974216/)
[^dobrzynski-2007-sa-node-pacemaking]: Dobrzynski H, Boyett MR, Anderson RH. New insights into pacemaker activity. *Circulation.* 2007;115(14):1921-32. [doi:10.1161/CIRCULATIONAHA.106.616011](https://doi.org/10.1161/CIRCULATIONAHA.106.616011) · [PubMed 17420362](https://pubmed.ncbi.nlm.nih.gov/17420362/)
[^openstax-anatomy-19-2]: OpenStax. *Anatomy & Physiology 2e*, Ch. 19.2: Cardiac Muscle and Electrical Activity. [Read online →](https://openstax.org/books/anatomy-and-physiology-2e/pages/19-2-cardiac-muscle-and-electrical-activity)
