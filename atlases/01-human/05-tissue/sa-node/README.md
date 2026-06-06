---
schema: human-scale-entry/v1
id: sa-node
name: Sinoatrial Node
atlas: 01-human
scale: 05-tissue
status: draft
last_reviewed: 2026-06-06
summary: "Specialized cardiac pacemaker tissue at the right atrium–SVC junction; generates spontaneous rhythmic action potentials via HCN4 funny current and L-type Ca²⁺ channels. Autonomic modulation sets resting heart rate 60–100 bpm; failure produces sick sinus syndrome."
aliases: ["SA node", "sinoatrial node", "sinus node", "cardiac pacemaker"]
sources:
  - id: mangoni-2008-automaticity
    type: peer-reviewed
    cite: "Mangoni ME, Nargeot J. Genesis and regulation of the heart automaticity. Physiol Rev. 2008;88(3):919-982."
    doi: "10.1152/physrev.00018.2007"
    pmid: "18626064"
    url: "https://doi.org/10.1152/physrev.00018.2007"
  - id: difrancesco-2010-funny-current
    type: peer-reviewed
    cite: "DiFrancesco D. The role of the funny current in pacemaker activity. Circ Res. 2010;106(3):434-446."
    doi: "10.1161/CIRCRESAHA.109.208041"
    pmid: "20167941"
    url: "https://doi.org/10.1161/CIRCRESAHA.109.208041"
  - id: lakatta-2010-coupled-clocks
    type: peer-reviewed
    cite: "Lakatta EG, Maltsev VA, Vinogradova TM. A coupled SYSTEM of intracellular Ca2+ clocks and surface membrane voltage clocks controls the timekeeping mechanism of the heart's pacemaker. Circ Res. 2010;106(4):659-673."
    doi: "10.1161/CIRCRESAHA.109.206078"
    pmid: "20203315"
    url: "https://doi.org/10.1161/CIRCRESAHA.109.206078"
cross_links:
  - target: 01-human/04-cellular/sa-node-cell
    relation: contains
    note: "SA node tissue is composed of specialized SA node pacemaker cells (nodal cells) that exhibit spontaneous phase 4 diastolic depolarization; smaller and less organized than working atrial cardiomyocytes, with abundant HCN4 and T-type/L-type Ca²⁺ channels."
  - target: 01-human/03-molecular/hcn4
    relation: contains
    note: "HCN4 (hyperpolarization-activated cyclic nucleotide-gated channel 4) is the primary molecular determinant of the funny current (If) in SA node cells; cAMP binding accelerates If and increases heart rate in response to sympathetic stimulation."
  - target: 01-human/03-molecular/beta1-adrenergic-receptor
    relation: modulated-by
    note: "β₁-adrenergic receptor activation (by norepinephrine/epinephrine) increases cAMP → PKA phosphorylation of HCN4 and L-type Ca²⁺ channels → faster spontaneous depolarization (chronotropy); muscarinic M2 receptors decrease cAMP for the opposing vagal effect."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: part-of
    note: "The SA node is the primary pacemaker of the cardiac conduction system, initiating each heartbeat; impulses propagate via internodal pathways to the AV node, bundle of His, and Purkinje system."
  - target: 01-human/06-organ/heart
    relation: part-of
    note: "The SA node is embedded in the epicardial surface of the right atrium at the junction with the superior vena cava (crista terminalis region); it is the anatomical and functional pacemaker of the heart."
---

# Sinoatrial Node

## Overview

The **sinoatrial (SA) node** is a small (~15 × 3 × 1 mm) crescent-shaped region of specialized cardiac tissue located at the junction of the **right atrium** and the **superior vena cava**, near the crista terminalis. It is the **primary cardiac pacemaker** — the structure that initiates each cardiac cycle by generating spontaneous, rhythmic electrical impulses that propagate through the atria and conduction system to drive coordinated ventricular contraction.

The SA node dominates heart rate because its intrinsic pacemaker rate (~70 bpm at rest) exceeds that of all subsidiary pacemakers (AV node: ~40–50 bpm; ventricular escape: ~20–40 bpm). This rate hierarchy ensures that the fastest pacemaker (normally the SA node) controls heart rhythm; loss of SA node function ("sick sinus syndrome") allows slower latent pacemakers to take over, producing symptomatic bradycardia.

Autonomic regulation continuously modulates SA node firing rate: **sympathetic stimulation** (β₁-adrenergic → cAMP → If acceleration) increases heart rate; **vagal stimulation** (M2 muscarinic → decreased cAMP + IKACh) slows it. Resting heart rate (60–100 bpm) reflects the balance of these tonic inputs.

## Structure

### Cellular composition

SA node tissue is histologically distinct from surrounding atrial myocardium:
- **Nodal (pacemaker) cells:** Small (5–10 μm diameter), ovoid, poorly organized; sparse myofilaments (weak contractile function); abundant **HCN4 channels** and T-type Ca²⁺ channels (CaV3.1); low levels of Nav1.5 (slow upstroke; Vmax ~10 V/s vs ~250 V/s in atrial muscle) [^mangoni-2008-automaticity]
- **Transitional cells:** Intermediate zone between central nodal cells and surrounding atrial myocytes; modulate conduction velocity and SA node impulse exit block
- **Working atrial cardiomyocytes:** Peripheral; transmit impulses from the node to atrial muscle

**Intercellular coupling:** SA node cells have **low gap junction (connexin) density** — primarily connexin45 (Cx45) with very low Cx43/Cx40 expression. Low coupling is essential for pacemaking: tight electrical coupling to the large atrial mass would hyperpolarize nodal cells and suppress automaticity (the "source-sink" problem).

### Anatomical boundaries

The SA node occupies the subepicardial fat at the sulcus terminalis; it receives dual blood supply from the **SA nodal artery** (from the right coronary artery in ~55% or left circumflex in ~45% of individuals). The node is richly innervated by both sympathetic (stellate ganglia) and parasympathetic (right vagus) fibers.

## Function

### Mechanism of automaticity: the "coupled clock" model

Spontaneous pacemaking results from the interaction of two coupled oscillators [^lakatta-2010-coupled-clocks]:

**Voltage (membrane) clock:**
- Phase 4 diastolic depolarization begins immediately after repolarization (~−65 mV)
- **Funny current (If, HCN4):** Inward Na⁺ current activated by hyperpolarization; provides the initial slow depolarizing slope; accelerated by cAMP (sympathetic) [^difrancesco-2010-funny-current]
- **T-type Ca²⁺ current (ICaT, CaV3.1):** Activates at ~−55 mV; contributes mid-phase depolarization
- **L-type Ca²⁺ current (ICaL, CaV1.2/1.3):** The main upstroke current (replaces fast Nav1.5-driven upstroke absent in nodal cells); threshold ~−40 mV; produces the action potential overshoot

**Ca²⁺ (intracellular) clock:**
- Rhythmic spontaneous Ca²⁺ release from the SR via **RyR2** during late diastole (local Ca²⁺ sparks)
- Sparks activate **NCX1** (Na⁺/Ca²⁺ exchanger, 3 Na⁺ in : 1 Ca²⁺ out) → net inward current → further depolarization
- The Ca²⁺ clock amplifies and entrains the membrane clock; together they create robust, reliable pacemaking

**Autonomic modulation:**
- **Sympathetic (β₁-AR → cAMP → PKA):** Phosphorylates HCN4 → leftward shift of If activation → faster diastolic depolarization; also phosphorylates CaV1.2 and RyR2 → stronger Ca²⁺ clock → higher heart rate
- **Parasympathetic (M2 → Gi → ↓cAMP + IKACh):** Decreased If + K⁺ current hyperpolarization → slower phase 4 → lower heart rate; atropine blocks this to increase rate

### Impulse propagation

SA node action potentials exit via transitional cells into the crista terminalis and interatrial septum → propagate rapidly through atrial working myocardium (Cx40/Cx43 coupling) → converge at the **AV node** → conducted to ventricles via His–Purkinje system.

**Conduction velocity within SA node:** ~0.02–0.05 m/s (slow, due to low Cx density and slow upstroke); this allows only the leading edge of depolarization to exit — the node acts as a current source driving the atrial sink.

### Clinical correlates

- **Sick sinus syndrome:** SA node dysfunction (fibrosis, ischemia, autonomic imbalance) → bradycardia, sinus arrest, tachycardia-bradycardia syndrome; treated with permanent pacemaker implantation
- **Inappropriate sinus tachycardia:** Enhanced automaticity or blunted vagal input → resting HR >100 bpm despite normal sinus node structure; treatment includes ivermectin (HCN4 blocker) or beta-blockers
- **If inhibitor (Ivabradine):** Selectively blocks HCN4 → reduces heart rate without negative inotropy; used in heart failure and stable angina to reduce cardiac oxygen demand
- **RyR2 mutations:** Gain-of-function → catecholaminergic polymorphic ventricular tachycardia (CPVT) via Ca²⁺ clock overactivation; also affects sinus node Ca²⁺ oscillations

## Connections

- `contains` → **[SA Node Cell](../../04-cellular/sa-node-cell/README.md)** — nodal pacemaker cells are the cellular substrate of SA node automaticity; their unique ion channel composition (HCN4-rich, Nav1.5-poor) enables spontaneous phase 4 depolarization.
- `contains` → **[HCN4](../../03-molecular/hcn4/README.md)** — the funny current channel is the dominant molecular pacemaking mechanism; ivabradine (HCN4 blocker) selectively reduces SA node firing rate without impairing contractility.
- `modulated-by` → **[β₁-Adrenergic Receptor](../../03-molecular/beta1-adrenergic-receptor/README.md)** — sympathetic activation of β₁-AR in SA node increases cAMP, accelerates HCN4 and L-type Ca²⁺ channels, and speeds the Ca²⁺ clock — the primary molecular basis of exercise-induced tachycardia.
- `part-of` → **[Cardiac Conduction System](../cardiac-conduction-system/README.md)** — the SA node is the primary pacemaker of the conduction system; it initiates each heartbeat and sets the rate for downstream conduction (AV node → His → Purkinje).
- `part-of` → **[Heart](../../06-organ/heart/README.md)** — the SA node is anatomically embedded in the right atrium at the SVC junction and is the master timekeeper of the heart's contractile cycle.

[^mangoni-2008-automaticity]: Mangoni ME, Nargeot J. Genesis and regulation of the heart automaticity. *Physiol Rev.* 2008;88(3):919-982. [doi:10.1152/physrev.00018.2007](https://doi.org/10.1152/physrev.00018.2007) · [PubMed 18626064](https://pubmed.ncbi.nlm.nih.gov/18626064/)
[^difrancesco-2010-funny-current]: DiFrancesco D. The role of the funny current in pacemaker activity. *Circ Res.* 2010;106(3):434-446. [doi:10.1161/CIRCRESAHA.109.208041](https://doi.org/10.1161/CIRCRESAHA.109.208041) · [PubMed 20167941](https://pubmed.ncbi.nlm.nih.gov/20167941/)
[^lakatta-2010-coupled-clocks]: Lakatta EG, Maltsev VA, Vinogradova TM. A coupled SYSTEM of intracellular Ca2+ clocks and surface membrane voltage clocks controls the timekeeping mechanism of the heart's pacemaker. *Circ Res.* 2010;106(4):659-673. [doi:10.1161/CIRCRESAHA.109.206078](https://doi.org/10.1161/CIRCRESAHA.109.206078) · [PubMed 20203315](https://pubmed.ncbi.nlm.nih.gov/20203315/)
