---
schema: human-scale-entry/v1
id: calcium
name: Calcium
atlas: 01-human
scale: 02-atomic
status: draft
last_reviewed: 2026-06-03
summary: "Ca²⁺ — the preeminent intracellular second messenger. In the heart, a 10-fold cytosolic Ca²⁺ transient (100 nM → 1 µM during systole) triggers troponin C and every contraction via CICR from the SR. β1-AR/PKA signaling and SERCA2a tune the Ca²⁺ transient."
aliases: ["Ca", "Ca²⁺", "calcium ion", "calcium signaling"]
sources:
  - id: clapham-2007-calcium-signaling
    type: peer-reviewed
    cite: "Clapham DE. Calcium signaling. Cell. 2007;131(6):1047-58."
    doi: "10.1016/j.cell.2007.11.028"
    pmid: "18083096"
    url: "https://doi.org/10.1016/j.cell.2007.11.028"
  - id: bers-2002-cardiac-ec-coupling
    type: peer-reviewed
    cite: "Bers DM. Cardiac excitation-contraction coupling. Nature. 2002;415(6868):198-205."
    doi: "10.1038/415198a"
    pmid: "11805843"
    url: "https://doi.org/10.1038/415198a"
  - id: carafoli-1987-calcium-homeostasis
    type: peer-reviewed
    cite: "Carafoli E. Intracellular calcium homeostasis. Annu Rev Biochem. 1987;56:395-433."
    doi: "10.1146/annurev.bi.56.070187.002143"
    pmid: "2885786"
    url: "https://doi.org/10.1146/annurev.bi.56.070187.002143"
  - id: stryer-biochemistry
    type: textbook
    cite: "Berg JM, Tymoczko JL, Stryer L. Biochemistry. 9th ed. W.H. Freeman; 2019."
    url: "https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X"
    accessed: "2026-06-03"
cross_links:
  - target: 01-human/03-molecular/troponin-complex
    relation: modulates
    note: "Ca²⁺ binds to the EF-hand domain of troponin C (site II, low-affinity regulatory site), triggering the conformational shift that gates actin-myosin cross-bridge cycling."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: modulates
    note: "The cytosolic Ca²⁺ transient — rising from ~100 nM at rest to ~1 µM during systole — is the primary trigger of EC coupling in the cardiomyocyte."
  - target: 01-human/03-molecular/beta1-adrenergic-receptor
    relation: modulates
    note: "β1-AR/PKA signaling modulates Ca²⁺ handling: PKA phosphorylates Cav1.2 (more Ca²⁺ in), RyR2, phospholamban (faster Ca²⁺ reuptake to SR) — all changing Ca²⁺ transient amplitude and kinetics."
  - target: 01-human/01-subatomic/electron
    relation: modulated-by
    note: "The electron configuration of Ca ([Ar] 4s²) determines its ionization to Ca²⁺ and the electrostatic basis of EF-hand coordination chemistry."
---

# Calcium

## Overview

Calcium (symbol Ca, atomic number 20) is an **alkaline earth metal** in Group 2 of the periodic table, with atomic mass 40.078 u. Its ground-state electron configuration is [Ar] 4s², and in all biologically relevant chemistry it loses both 4s electrons to form the **divalent cation Ca²⁺** (ionic radius 0.099 nm). This simple chemistry belies calcium's extraordinary importance: it is the **most abundant mineral in the human body** (~1 kg in a 70 kg adult, >99% in bone and teeth as hydroxyapatite [Ca₁₀(PO₄)₆(OH)₂]) and simultaneously the **most versatile intracellular second messenger** in biology [^clapham-2007-calcium-signaling].

The coexistence of these two roles — structural mineral and regulatory ion — is possible because the two pools are maintained in near-total isolation. The free cytosolic Ca²⁺ concentration ([Ca²⁺]i) at rest is approximately **100 nM** (10⁻⁷ M), while the extracellular concentration is ~1.2 mM and the sarcoplasmic reticulum (SR) lumen in cardiomyocytes contains ~1 mM. These gradients — 10,000-fold across the SR membrane, ~100,000-fold across the plasma membrane — are the thermodynamic reservoir that makes Ca²⁺ signaling both powerful and fast [^carafoli-1987-calcium-homeostasis].

## Structure

### Atomic Properties

| Property | Value |
|:---|:---|
| Atomic number (Z) | 20 |
| Atomic mass | 40.078 u |
| Electron configuration | [Ar] 4s² |
| Ionic form in biology | Ca²⁺ (loses both 4s electrons) |
| Ionic radius (Ca²⁺) | 0.099 nm (99 pm) |
| Coordination number | 6–8 in aqueous environments; 7 in EF-hand motifs |
| Electronegativity (Pauling) | 1.00 |

### Why Ca²⁺ is the Perfect Signaling Ion

Five properties make Ca²⁺ essentially irreplaceable as a second messenger [^clapham-2007-calcium-signaling]:

1. **Charge density** — the 2+ charge on a small ion creates a high charge density that allows tight, specific coordination by protein binding sites (EF-hand motifs). The EF-hand's 7 coordinating residues provide an exact complementary fit for Ca²⁺ with nanomolar affinity; Mg²⁺ (similar charge but smaller) and Na⁺/K⁺ (larger radii, lower charge) cannot substitute.

2. **Steep gradient** — the 10,000-fold gradient across the SR and ~100,000-fold gradient across the plasma membrane means that even a small Ca²⁺ influx produces a large fractional increase in cytosolic [Ca²⁺], enabling large-amplitude signals from small ion movements.

3. **Fast on/off kinetics** — Ca²⁺ binding to and dissociation from EF-hand proteins is fast (milliseconds), compatible with the millisecond timescale of the cardiac action potential and contraction.

4. **Multiple return mechanisms** — SERCA (SR Ca²⁺-ATPase, pumps Ca²⁺ back into SR), NCX (Na⁺/Ca²⁺ exchanger, extrudes Ca²⁺ across the plasma membrane), plasma membrane Ca²⁺-ATPase (PMCA), and mitochondrial Ca²⁺ uniporter all restore resting [Ca²⁺]i, enabling signal termination and the next signaling cycle.

5. **Chemical incompatibility with phosphate at physiological pH** — Ca²⁺ would precipitate as calcium phosphate if it were free in the cytosol at millimolar concentrations (which is why it cannot be). The strict nanomolar maintenance is a thermodynamic necessity that biology has turned into a signaling asset.

## Function

### Ca²⁺ as a Universal Second Messenger

In non-cardiac cells, Ca²⁺ signals control exocytosis (secretion from endocrine and exocrine cells, neurotransmitter release), smooth muscle contraction, gene transcription (via calcineurin/NFAT, CaMKII/CREB pathways), cell proliferation, and apoptosis. The signaling toolkit includes:

- **Calmodulin (CaM)** — ubiquitous four-EF-hand Ca²⁺ sensor; bound Ca²⁺-CaM activates CaM kinase II (CaMKII), eNOS, myosin light chain kinase, phosphodiesterase, and calcineurin.
- **IP₃ receptors (IP₃R)** — ER Ca²⁺-release channels triggered by IP₃ (from PLC activation); ubiquitous in non-cardiac cells; minor in cardiac CICR.
- **Ryanodine receptors (RyR)** — SR Ca²⁺-release channels; dominant in cardiac and skeletal muscle.

### Ca²⁺ in the Cardiomyocyte: EC Coupling

In the heart, the cytosolic Ca²⁺ transient is the signal linking every action potential to every contraction [^bers-2002-cardiac-ec-coupling]:

| Phase | [Ca²⁺]i | Source / sink | Event |
|:---|:---:|:---|:---|
| **Diastole** | ~100 nM | SERCA and NCX maintain low level | Troponin C site II empty; tropomyosin blocking |
| **Systole onset** | ↑ to ~1 µM | ~25% from L-type Cav1.2 (trigger); ~75% from SR via RyR2 (CICR) | Troponin C site II saturates; cross-bridge cycling |
| **Relaxation** | ↓ back to 100 nM | ~70% SERCA2a (SR uptake); ~28% NCX (extrusion) | Ca²⁺ leaves troponin C; muscle relaxes |

**Ca²⁺-induced Ca²⁺ release (CICR):** The small trigger Ca²⁺ entering via Cav1.2 in the T-tubule raises local [Ca²⁺] in the dyadic cleft, activating RyR2 clusters on the apposed junctional SR. RyR2 activation is cooperatively amplified — a small trigger releases a large Ca²⁺ load from the SR. This gain-of-signal is what allows the L-type channel current (tiny) to trigger a full, forceful contraction.

### Systolic Ca²⁺ Amplitude and Cardiac Force

The developed force of myocardial contraction depends on the peak Ca²⁺ transient amplitude in a highly non-linear way (Hill coefficient ~3–5), because the troponin switch has high cooperativity. A modest increase in SR Ca²⁺ load (e.g., through β1-adrenergic PKA phosphorylation of phospholamban → more SERCA activity → more SR filling) produces a disproportionately larger increase in systolic force — this is the mechanistic basis of inotropic reserve.

## In the Heart: β1-AR Modulation of Ca²⁺ Handling

Sympathetic activation (via β1-adrenergic receptor → Gαs → cAMP → PKA) modifies Ca²⁺ handling at four points simultaneously:

| PKA phosphorylation target | Effect on Ca²⁺ |
|:---|:---|
| **Cav1.2** (L-type channel) | More Ca²⁺ enters per beat (trigger Ca²⁺ ↑) |
| **RyR2** | More cooperative SR Ca²⁺ release |
| **Phospholamban** (PLN) | Relieves SERCA2a inhibition → faster SR Ca²⁺ reuptake → faster relaxation + larger SR load → next beat is stronger |
| **Troponin I** (Ser23/24) | Reduces TnC Ca²⁺ affinity → faster cross-bridge detachment → faster lusitropy |

This coordinated response allows the heart to beat faster, stronger, and still relax fully between beats during exercise or stress — a feat impossible to achieve by tuning any single Ca²⁺ step alone.

## Connections

- **Modulates** → [Troponin complex](../../03-molecular/troponin-complex/README.md): Ca²⁺ binding to TnC site II is the molecular switch that gates every contraction.
- **Modulates** → [Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md): The Ca²⁺ transient is the trigger and the terminator of EC coupling in every working cardiomyocyte.
- **Modulated by** → [β1-adrenergic receptor](../../03-molecular/beta1-adrenergic-receptor/README.md): PKA downstream of β1-AR simultaneously amplifies Ca²⁺ entry, SR release, SR reuptake, and myofilament Ca²⁺ sensitivity.
- **Sub-atomic basis** → [Electron](../../01-subatomic/electron/README.md): Ca²⁺'s ionic charge and radius — both consequences of its electron configuration — determine why EF-hand domains bind it selectively.

## Pathology

| Disease | Ca²⁺ mechanism |
|:---|:---|
| **Heart failure (HFrEF)** | Reduced SR Ca²⁺ load (SERCA2a down-regulation, phospholamban hyper-inhibited); reduced systolic Ca²⁺ transient → reduced contractility |
| **Hypertrophic cardiomyopathy** | Sarcomeric mutations (e.g., TNNT2, TNNI3) increase myofilament Ca²⁺ sensitivity → hypercontractility, impaired relaxation, diastolic dysfunction |
| **Catecholaminergic polymorphic VT (CPVT)** | RyR2 gain-of-function mutations (or calsequestrin-2 loss-of-function) → diastolic SR Ca²⁺ leak → delayed afterdepolarizations → arrhythmia under adrenergic stress |
| **Hypercalcemia** | Elevated extracellular Ca²⁺ shortens the action potential, can cause bradycardia and aortic calcification |
| **Hypocalcemia** | Increased neuronal and cardiac excitability; QT prolongation; severe cases cause tetany and arrhythmia |

## Open Questions

- **SR Ca²⁺ sensing mechanisms:** How do RyR2 and SERCA2a each sense SR Ca²⁺ concentration independently? What controls the luminal threshold for spontaneous Ca²⁺ sparks?
- **CaMKII in disease:** CaMKII (activated by Ca²⁺/calmodulin) phosphorylates RyR2 and increases spark frequency — contributing to arrhythmia in heart failure. Whether CaMKII inhibition is a viable therapeutic target is under investigation.
- **Sex differences:** Female cardiomyocytes have subtly different Ca²⁺ handling — higher RyR2 activity, different phospholamban expression — which may underlie differences in HF phenotype and arrhythmia susceptibility.

## See Also

- [Troponin complex](../../03-molecular/troponin-complex/README.md) — molecular switch activated by Ca²⁺.
- [Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md) — cell-scale Ca²⁺ cycling.
- [Electron](../../01-subatomic/electron/README.md) — subatomic basis of Ca²⁺ chemistry.

[^clapham-2007-calcium-signaling]: Clapham DE. Calcium signaling. *Cell.* 2007;131(6):1047-58. [doi:10.1016/j.cell.2007.11.028](https://doi.org/10.1016/j.cell.2007.11.028) · [PubMed 18083096](https://pubmed.ncbi.nlm.nih.gov/18083096/)
[^bers-2002-cardiac-ec-coupling]: Bers DM. Cardiac excitation-contraction coupling. *Nature.* 2002;415(6868):198-205. [doi:10.1038/415198a](https://doi.org/10.1038/415198a) · [PubMed 11805843](https://pubmed.ncbi.nlm.nih.gov/11805843/)
[^carafoli-1987-calcium-homeostasis]: Carafoli E. Intracellular calcium homeostasis. *Annu Rev Biochem.* 1987;56:395-433. [doi:10.1146/annurev.bi.56.070187.002143](https://doi.org/10.1146/annurev.bi.56.070187.002143) · [PubMed 2885786](https://pubmed.ncbi.nlm.nih.gov/2885786/)
[^stryer-biochemistry]: Berg JM, Tymoczko JL, Stryer L. *Biochemistry.* 9th ed. W.H. Freeman; 2019. [macmillanlearning.com](https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X)
