---
schema: human-scale-entry/v1
id: troponin-complex
name: Troponin complex
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-03
summary: "Heterotrimeric calcium switch on the thin filament — TnC binds Ca²⁺, TnI inhibits actomyosin in its absence, TnT anchors the complex to tropomyosin. The molecular gate of every heartbeat."
aliases: ["cardiac troponin", "Tn complex", "TnC-TnI-TnT"]
sources:
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
  - id: uniprot-p63316-tnnc1
    type: database
    cite: "UniProt P63316 — Troponin C, slow skeletal and cardiac muscles (TNNC1, human)."
    url: "https://www.uniprot.org/uniprotkb/P63316/entry"
    accessed: "2026-06-03"
  - id: uniprot-p19429-tnni3
    type: database
    cite: "UniProt P19429 — Troponin I, cardiac muscle (TNNI3, human)."
    url: "https://www.uniprot.org/uniprotkb/P19429/entry"
    accessed: "2026-06-03"
  - id: uniprot-p45379-tnnt2
    type: database
    cite: "UniProt P45379 — Troponin T, cardiac muscle (TNNT2, human)."
    url: "https://www.uniprot.org/uniprotkb/P45379/entry"
    accessed: "2026-06-03"
  - id: thygesen-2018-mi-definition
    type: clinical-guideline
    cite: "Thygesen K, Alpert JS, Jaffe AS, et al. Fourth Universal Definition of Myocardial Infarction (2018). J Am Coll Cardiol. 2018;72(18):2231-64."
    doi: "10.1016/j.jacc.2018.08.1038"
    pmid: "30153967"
cross_links:
  - target: 01-human/04-cellular/cardiomyocyte
    relation: expressed-by
    note: "Cardiac troponin isoforms (TnC TNNC1, TnI TNNI3, TnT TNNT2) are expressed by cardiomyocytes and assembled onto every thin filament."
taxonomy:
  uniprot: "P63316,P19429,P45379"
  gene_symbol: "TNNC1,TNNI3,TNNT2"
---

# Troponin complex

## Overview

The troponin complex is a **three-subunit calcium switch** on the thin filament of striated muscle. In its absence-of-calcium state, it holds tropomyosin over the myosin-binding sites on actin — the muscle is **off**. When cytosolic Ca²⁺ rises and binds to one subunit, the whole complex undergoes a conformational shift that exposes those binding sites — the muscle is **on** [^bers-2002-cardiac-ec-coupling]. Every heartbeat is one cycle of this switch, repeated synchronously in every sarcomere of every cardiomyocyte.

The complex has three subunits, named for what they do:

- **Troponin C (TnC)** — *calcium*-binding subunit. Cardiac isoform encoded by `TNNC1` [^uniprot-p63316-tnnc1].
- **Troponin I (TnI)** — *inhibitory* subunit. Cardiac isoform encoded by `TNNI3` [^uniprot-p19429-tnni3].
- **Troponin T (TnT)** — *tropomyosin*-binding subunit. Cardiac isoform encoded by `TNNT2` [^uniprot-p45379-tnnt2].

The cardiac isoforms differ from the slow-skeletal and fast-skeletal isoforms in regulatory detail, and — critically — in their tissue specificity. Cardiac TnI and cardiac TnT are expressed nowhere else in the body. This is why a serum cardiac-troponin elevation is a near-specific signal of cardiomyocyte injury, and why the high-sensitivity cardiac troponin assay is the cornerstone of acute myocardial infarction diagnosis [^thygesen-2018-mi-definition].

## Structure

### The trimer

Each troponin complex is **one TnC + one TnI + one TnT**, sitting on the thin filament approximately every **seven actin monomers**, alongside one tropomyosin dimer. The thin filament therefore presents a regularly repeating regulatory unit along its length.

| Subunit | Mass | UniProt (human cardiac) | Gene | What it does |
|:---|:---:|:---:|:---:|:---|
| **TnC** | ~18 kDa | [P63316](https://www.uniprot.org/uniprotkb/P63316/entry) | `TNNC1` | Binds Ca²⁺ at low-affinity regulatory site; transduces Ca²⁺ signal into conformation change |
| **TnI** | ~24 kDa | [P19429](https://www.uniprot.org/uniprotkb/P19429/entry) | `TNNI3` | Inhibits actomyosin in absence of Ca²⁺; releases when TnC is loaded |
| **TnT** | ~37 kDa | [P45379](https://www.uniprot.org/uniprotkb/P45379/entry) | `TNNT2` | Binds tropomyosin; anchors the whole complex to the thin filament |

### TnC (troponin C)

TnC is a member of the **EF-hand calcium-binding protein** superfamily. It has four EF-hand domains, but in the **cardiac isoform**, **site I is non-functional** because of an evolutionary substitution in a key calcium-coordinating residue. Effectively only **sites II, III, and IV** bind Ca²⁺:

- **Site II** — the **low-affinity, regulatory site** in the N-terminal lobe. This is the calcium switch that gates contraction. Binding here is the trigger.
- **Sites III and IV** — high-affinity sites in the C-terminal lobe, occupied by Mg²⁺ at rest and only slowly exchangeable with Ca²⁺. They serve a structural role, anchoring TnC to TnI.

### TnI (troponin I)

TnI has an N-terminal extension found only in the cardiac isoform — about 30 extra residues containing two **PKA phosphorylation sites at Ser23 and Ser24**. Phosphorylation here is a key node where β-adrenergic signaling tunes contraction (see *Mechanism*).

The C-terminal half contains the **inhibitory peptide** and a **switch peptide**. In the off state, the inhibitory peptide engages actin and tropomyosin to lock them in the blocking position. When TnC's regulatory site fills with Ca²⁺, the switch peptide is captured by TnC's hydrophobic patch — and TnI's grip on actin is released.

### TnT (troponin T)

TnT is elongated and largely structural. It has two functional ends:

- **TnT1** (N-terminal) — anchors the complex to tropomyosin along the thin filament.
- **TnT2** (C-terminal globular domain) — binds TnI and TnC, organizing the trimer.

TnT also stiffens tropomyosin's interaction with actin and is required for cooperative regulation along the entire thin filament.

## Function

The troponin complex's function is to translate cytosolic [Ca²⁺] into the **on/off state of the thin filament**, with high cooperativity (Hill coefficient ~3–5 in cardiac muscle) and on a timescale (~10–30 ms) compatible with each heartbeat.

In a single cardiomyocyte, every contraction follows the same Ca²⁺ trajectory:

| Time | [Ca²⁺]_cytosol | Troponin state | Filament state |
|:---|:---|:---|:---|
| Diastole | ~100 nM | Site II empty | OFF — tropomyosin blocking |
| Systole peak | ~1 µM | Site II saturated | ON — myosin can bind |
| Late systole / early diastole | falling | Site II releasing | OFF — relaxation |

The **steepness** of the response (small Ca²⁺ changes producing large force changes) is what makes the heart's contraction modulable: a doubling of Ca²⁺ transient amplitude can increase developed force several-fold.

## Mechanism

### The Ca²⁺-triggered conformational shift

In the **off** state (low Ca²⁺):

1. TnI's inhibitory + switch peptides bind actin and stabilize tropomyosin in its **blocking position** over actin's myosin-binding interface.
2. Tropomyosin physically occludes the myosin head's binding site.
3. No cross-bridge formation. No force.

When cytosolic Ca²⁺ rises and binds TnC's regulatory site II:

1. TnC undergoes a hydrophobic-patch opening conformational change in its N-terminal lobe.
2. The exposed patch grabs the **switch peptide of TnI**.
3. TnI's inhibitory + switch peptides **release from actin**.
4. Tropomyosin slides azimuthally around the thin filament from the **blocked** through **closed** to **open** position (the "three-state" model of thin-filament regulation).
5. Myosin heads can now form cross-bridges with actin, hydrolyze ATP, and pull the thin filament inward.

When Ca²⁺ falls (SERCA2a pumping back into the SR, NCX1 extruding to extracellular):

1. Site II releases Ca²⁺.
2. TnC closes; releases the switch peptide.
3. TnI re-engages actin; tropomyosin returns to its blocking position.
4. Cross-bridges detach (with ATP turnover); the cell relaxes.

### β-adrenergic modulation via PKA phosphorylation

Sympathetic activation reaches the cardiomyocyte through the **[β1-adrenergic receptor](beta1-adrenergic-receptor/README.md)**, raising intracellular cAMP and activating PKA. Among many PKA targets, **TnI Ser23/24 phosphorylation** has a specific consequence on the troponin complex:

- Phosphorylated TnI **lowers the Ca²⁺ affinity of TnC's regulatory site II** — the switch becomes less sensitive.
- The result: **faster relaxation** (lusitropy) — Ca²⁺ falls off TnC sooner — and matched timing with the parallel PKA effects on phospholamban (faster SR re-uptake) and L-type channels (more Ca²⁺ in).

Together with PKA's effects on phospholamban and Cav1.2, TnI phosphorylation lets the heart **beat faster and harder while still relaxing in time** — a non-trivial feat at high heart rates.

## Connections

- **Up (containing cell):** the troponin complex is `part-of` the **[cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)**, where it sits on every thin filament of every sarcomere.
- **Sideways (interactions):** binds tropomyosin (a separate thin-filament regulator), is regulated by free Ca²⁺ (released from the sarcoplasmic reticulum during EC coupling), and is phosphorylated by **PKA** — the kinase activated downstream of [β1-adrenergic receptor](beta1-adrenergic-receptor/README.md) signaling. Entries to come.
- **Cross-atlas:** cardiac troponin (specifically cTnI and cTnT) is the **diagnostic biomarker** for myocardial infarction; entries describing MI and the troponin assay will reside in the Pathology / Clinical Atlases (planned).

## Pathology

(Not strictly required at the molecular scale, but central to heart disease.)

| Process | Mechanism |
|:---|:---|
| **Acute myocardial infarction** | Cardiomyocyte necrosis releases cTnI and cTnT into circulation; high-sensitivity assays detect rises within hours of injury — the basis for the *Universal Definition of MI* [^thygesen-2018-mi-definition]. |
| **Hypertrophic cardiomyopathy (HCM)** | Mutations in `TNNT2` and `TNNI3` (and many other sarcomeric genes) destabilize the regulatory complex, often increasing myofilament Ca²⁺ sensitivity. Hypertrophy, myocyte disarray, and predisposition to ventricular arrhythmia follow. |
| **Dilated cardiomyopathy (DCM)** | Some `TNNT2` and `TNNI3` mutations cause weakened force generation and chamber dilation. |
| **Restrictive cardiomyopathy (RCM)** | Rarer; certain `TNNI3` mutations produce restrictive physiology. |

## Variation

- **Cardiac vs. skeletal isoforms.** Slow-skeletal TnC is encoded by the same gene (`TNNC1`) as cardiac TnC; fast-skeletal TnC is encoded by `TNNC2`. Skeletal TnI/TnT are encoded by separate genes (`TNNI1`/`TNNI2`, `TNNT1`/`TNNT3`). The cardiac isoforms are unique in their PKA-phosphorylation site (TnI Ser23/24) and in non-functional TnC site I.
- **Fetal vs. adult.** Fetal cardiomyocytes express **slow-skeletal TnI** alongside (or instead of) cardiac TnI; the developmental switch to cardiac TnI is a hallmark of postnatal maturation and is incomplete in some forms of heart failure.
- **Mutations.** Many disease-causing variants in the troponin genes have been characterized, with phenotype severity ranging from sub-clinical to lethal. The *MYH7-MYBPC3-TNNT2-TNNI3* sarcomeric gene family accounts for the majority of familial HCM.

## Open questions

- **Why does HCM kill cells?** How sarcomeric mutations producing increased Ca²⁺ sensitivity translate into hypertrophy, fibrosis, and arrhythmia is incompletely understood. Energetic stress, altered tension–length relationships, and disturbed Ca²⁺ handling are leading hypotheses.
- **Therapeutic targeting.** **Mavacamten** (cardiac myosin inhibitor) targets the thick filament; analogous thin-filament-modulating drugs that work via troponin (positive or negative) are under active investigation.
- **TnI dephosphorylation balance.** The phosphatases that reverse PKA's effect on TnI (PP1, PP2A) are imperfectly mapped in vivo; their dysregulation may contribute to the abnormal Ca²⁺ sensitivity of failing myocardium.

## See also

- [`cardiomyocyte`](../../04-cellular/cardiomyocyte/README.md) — the cell whose contraction this complex regulates.
- [`beta1-adrenergic-receptor`](beta1-adrenergic-receptor/README.md) — the receptor whose PKA cascade phosphorylates TnI.
- [`myocardium`](../../05-tissue/myocardium/README.md) — the tissue.
- [`heart`](../../06-organ/heart/README.md) — the organ.

[^bers-2002-cardiac-ec-coupling]: See entry frontmatter.
[^uniprot-p63316-tnnc1]: See entry frontmatter.
[^uniprot-p19429-tnni3]: See entry frontmatter.
[^uniprot-p45379-tnnt2]: See entry frontmatter.
[^thygesen-2018-mi-definition]: See entry frontmatter.
