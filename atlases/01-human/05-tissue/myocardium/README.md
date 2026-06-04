---
schema: human-scale-entry/v1
id: myocardium
name: Myocardium
atlas: 01-human
scale: 05-tissue
status: draft
last_reviewed: 2026-06-03
summary: "The contractile cardiac-muscle tissue that forms the bulk of the heart wall — a syncytium of cardiomyocytes electrically coupled through intercalated discs, supported by fibroblasts, capillaries, and a collagen scaffold."
aliases: ["cardiac muscle", "heart muscle"]
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
  - id: bergmann-2009-cardiomyocyte-renewal
    type: peer-reviewed
    cite: "Bergmann O, Bhardwaj RD, Bernard S, et al. Evidence for cardiomyocyte renewal in humans. Science. 2009;324(5923):98-102."
    doi: "10.1126/science.1164680"
    pmid: "19342590"
cross_links:
  - target: 01-human/06-organ/heart
    relation: part-of
    note: "The myocardium forms the muscular wall of the heart's chambers."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: composed-of
    note: "The contractile cell type — about 30–40% of cells by count, ~75% by volume."
taxonomy:
  uberon: "UBERON:0002349"
  fma: "FMA:9462"
---

# Myocardium

## Overview

The myocardium is the cardiac-muscle tissue that forms the **middle and dominant layer** of the heart wall, sandwiched between the inner endocardium and outer epicardium. It generates every heartbeat by orchestrating the synchronous contraction of millions of cardiomyocytes electrically coupled into a single functional unit — a **syncytium** — whose excitation can be triggered from a single pacemaker site (the SA node) and propagate cell-to-cell across the entire wall in tens of milliseconds [^openstax-anatomy-19-2].

Histologically, cardiac muscle is **striated** (like skeletal muscle, because both are built from organized sarcomeres) but **involuntary** (like smooth muscle, because it is autonomic-regulated and self-pacing). It is also unique among striated muscles in having short, branched cells joined end-to-end by intercalated discs — structures that are simultaneously mechanical (transmitting force) and electrical (passing depolarizing current).

## Structure

### Cellular composition

The myocardium is **not** purely cardiomyocyte. By volume the cardiomyocyte dominates (~75 %), but by cell count the **non-myocyte** population is comparable or larger:

| Cell type | Approximate share by count | Role |
|:---|:---:|:---|
| **Cardiomyocyte** | 30–40 % | Contraction. See **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)**. |
| **Cardiac fibroblast** | 25–40 % | Synthesizes and remodels extracellular matrix; key actor in fibrosis. *Entry pending.* |
| **Endothelial cell** | 20–30 % | Lines coronary capillaries; one capillary per cardiomyocyte typical. *Entry pending.* |
| **Pericyte / vascular smooth muscle** | small % | Microvascular tone. *Entry pending.* |
| **Resident macrophage** | small % | Tissue immune surveillance; participate in conduction at the AV node. *Entry pending.* |

This composition matters clinically: the **non-myocyte** population is responsible for fibrosis after injury, the local inflammatory response in myocarditis, and the immune environment that drives transplant rejection.

### Architecture

- **Cardiomyocytes** are roughly **10–20 µm in diameter and 50–100 µm long**, branched, and joined end-to-end at **intercalated discs**. Each disc contains:
  - **Fascia adherens** and **desmosomes** — mechanical cell-cell adhesion that transmits contractile force.
  - **Gap junctions** (predominantly **connexin-43**, encoded by `GJA1`) — low-resistance pores allowing direct passage of ions and small molecules between adjacent cells. These are what make the myocardium an electrical syncytium.
- **Sarcomeres** within each cardiomyocyte are aligned end-to-end, producing the cross-striations visible by light microscopy. See [Cardiomyocyte → Structure](../../04-cellular/cardiomyocyte/README.md) and [Troponin complex](../../03-molecular/troponin-complex/README.md) for the molecular machinery.
- **Fiber orientation** across the ventricular wall is **helical**: subepicardial fibers run in a right-handed helix, midwall fibers nearly circumferential, subendocardial fibers in a left-handed helix. This three-dimensional architecture produces the heart's characteristic **twisting (torsional) motion** during contraction, which is mechanically more efficient than a simple axial squeeze.
- **Extracellular matrix** is mostly **type I and type III collagen** organized into endomysium (around individual cells), perimysium (around fiber bundles), and epimysium (around the whole layer). This collagen scaffold transmits force and prevents over-stretching.
- **Microvasculature** is exceptionally dense: roughly **one capillary per cardiomyocyte**, ensuring oxygen delivery keeps pace with the heart's high resting metabolic demand (~6–10 mL O₂/100 g/min, 5–10× resting skeletal muscle).

### Wall thickness

Myocardial thickness varies dramatically by chamber, reflecting the pressure each must generate:

- **Left ventricular wall:** ~10–12 mm at end-diastole.
- **Right ventricular wall:** ~3–5 mm.
- **Atrial walls:** ~2–3 mm.

## Function

### Coordinated contraction

The myocardium's job is to convert the electrical signal arriving from the conduction system into mechanical force, **simultaneously and uniformly across the whole wall**. The chain of events in each cell is described in [Cardiomyocyte → Function](../../04-cellular/cardiomyocyte/README.md) and underpinned by **excitation–contraction coupling** [^bers-2002-cardiac-ec-coupling]; the tissue-scale property is that all of those cells fire and contract *in step*.

This requires:

1. **Electrical coupling** — gap junctions at the intercalated discs let depolarization spread from cell to cell at ~0.3–1 m/s in working myocardium (faster, ~2–4 m/s, in Purkinje fibers), without any synapse or chemical signal.
2. **Mechanical coupling** — desmosomes and fasciae adherentes transmit force end-to-end, so an isolated cell's shortening becomes wall-scale contraction.
3. **Spatially organized recruitment** — the conduction system (Purkinje fibers in the subendocardium) initiates depolarization at the apex first; the wave then spreads outward and apex-to-base, producing the wringing motion that ejects blood efficiently into the great vessels.

### Force–length and rate–force relationships

Cardiac muscle exhibits two emergent properties at the tissue scale that are essential to whole-organ function:

- **Frank–Starling mechanism.** Within physiological range, increasing end-diastolic stretch increases the force of the next contraction — a tissue-level property arising from length-dependent calcium sensitivity at the sarcomere. This lets each ventricle automatically match its output to its filling.
- **Force–frequency (Bowditch) relationship.** In healthy cardiac muscle, increasing stimulation frequency **increases** developed force (positive staircase). This is opposite to skeletal muscle and is mediated by frequency-dependent intracellular Ca²⁺ accumulation. The force–frequency relationship is **flattened or inverted** in failing myocardium — a useful tissue-level signature of disease.

### Metabolic profile

The myocardium is **highly oxidative**: about 95 % of ATP comes from oxidative phosphorylation, primarily fueled by fatty acids (60–70 %) and glucose/lactate (30–40 %) at rest. It is exquisitely sensitive to ischemia — irreversible cardiomyocyte injury begins within ~20–40 minutes of complete coronary occlusion. This metabolic profile is also why heart failure responds (in part) to therapies that shift substrate use.

### Limited regenerative capacity

Adult human cardiomyocytes turn over at roughly **~1 %/year in early adulthood, declining to <0.5 %/year past age 50** [^bergmann-2009-cardiomyocyte-renewal]. After significant injury (e.g., myocardial infarction), lost cardiomyocytes are not replaced — the void fills with collagenous scar produced by fibroblasts. This is the central reason ischemic heart disease becomes chronic heart failure: every infarct is a permanent reduction in contractile mass.

## Connections

- **Up (containing organ):** the myocardium is `part-of` the **[heart](../../06-organ/heart/README.md)**.
- **Down (constituent cell):** the myocardium is `composed-of` the **[cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)**, plus several non-myocyte cell types whose entries will follow (fibroblast, endothelial cell, resident macrophage).
- **Sideways (extracellular):** type I and type III collagen, fibronectin, and laminins — molecular-scale entries that operate at the tissue scale (entries to come).
- **Cross-atlas (planned in Phase 3):** the myocardium is the tissue-scale victim of **myocarditis** — inflammation triggered by viral infection (e.g., Coxsackievirus B), autoimmune mechanisms, or toxic exposures.

## Pathology

(Not strictly required at the tissue scale, but worth recording — most cardiac pathology can be traced to myocardial-tissue–level mechanisms.)

| Process | Tissue-level signature |
|:---|:---|
| **Ischemic injury** | Coagulation necrosis (early), neutrophil infiltration (24–72 h), granulation tissue (1–2 weeks), collagenous scar (6+ weeks). |
| **Hypertrophy** | Cardiomyocyte enlargement (no proliferation), increased sarcomere assembly, often accompanied by interstitial fibrosis. **Concentric** (pressure overload) vs. **eccentric** (volume overload) patterns. |
| **Fibrosis** | Excess collagen deposition by activated fibroblasts; **replacement fibrosis** (scar at sites of cell loss) vs. **interstitial / reactive fibrosis** (diffuse). Stiffens the wall, slows conduction, predisposes to arrhythmia. |
| **Myocarditis** | Inflammatory infiltrate within the myocardium — lymphocytic (viral, autoimmune), eosinophilic (drug-induced), or granulomatous (sarcoid, giant-cell). Damage to cardiomyocytes ranges from sublethal stunning to widespread cytolysis. |
| **Infiltrative disease** | Extracellular deposition of abnormal material — amyloid (light chain or transthyretin), iron (hemochromatosis), glycogen (storage diseases). Restrictive physiology results. |
| **Conduction-system disease** | Fibrotic replacement or selective injury to specialized conduction tissue produces blocks (SA, AV, bundle branches) and ectopic / re-entrant arrhythmias. |

## Variation

- **Sex.** Female myocardium has slightly more interstitial collagen and a different gene-expression profile (estrogen-receptor signaling) — relevant to the higher prevalence of HFpEF in women.
- **Athletic training.** Endurance training produces eccentric remodeling without fibrosis; resistance training produces concentric remodeling. Both are reversible (within ~6 months of detraining for the most part).
- **Age.** Interstitial fibrosis increases gradually through adult life; cardiomyocyte size increases modestly; myocardial mass-to-cell number ratio rises.
- **Genetic.** Sarcomeric protein mutations (`MYH7`, `MYBPC3`, `TNNT2`, `TNNI3`) produce hypertrophic or dilated cardiomyopathy with specific tissue-level signatures (myocyte disarray in HCM, dilation with mild fibrosis in DCM).

## Open questions

- **Therapeutic regeneration.** Can adult cardiomyocyte renewal be safely accelerated to repair injury? Hippo-pathway inhibition (YAP activation), Erbb2 signaling, and direct reprogramming of fibroblasts to cardiomyocytes are active research lines, none yet clinical.
- **Quantifying fibrosis non-invasively.** Cardiac MRI with T1 mapping is improving, but clinical decision-making based on tissue-level fibrosis burden is still evolving.
- **Mechanical–electrical coupling.** Stretch-activated channels and mechano-electric feedback can trigger arrhythmias, but the rules under which a stretched-but-not-yet-damaged myocardium becomes arrhythmic are incompletely understood.

## See also

- [`heart`](../../06-organ/heart/README.md) — the organ this tissue forms.
- [`cardiomyocyte`](../../04-cellular/cardiomyocyte/README.md) — the cell that gives the myocardium its identity.
- [`troponin-complex`](../../03-molecular/troponin-complex/README.md) — calcium switch on the thin filament.

[^openstax-anatomy-19-2]: OpenStax. *Anatomy & Physiology 2e*, Ch. 19.2: Cardiac Muscle and Electrical Activity. [Read online →](https://openstax.org/books/anatomy-and-physiology-2e/pages/19-2-cardiac-muscle-and-electrical-activity)
[^bers-2002-cardiac-ec-coupling]: Bers DM. Cardiac excitation-contraction coupling. *Nature.* 2002;415(6868):198-205. [doi:10.1038/415198a](https://doi.org/10.1038/415198a) · [PubMed 11805843](https://pubmed.ncbi.nlm.nih.gov/11805843/)
[^bergmann-2009-cardiomyocyte-renewal]: Bergmann O, Bhardwaj RD, Bernard S, et al. Evidence for cardiomyocyte renewal in humans. *Science.* 2009;324(5923):98-102. [doi:10.1126/science.1164680](https://doi.org/10.1126/science.1164680) · [PubMed 19342590](https://pubmed.ncbi.nlm.nih.gov/19342590/)
