---
schema: human-scale-entry/v1
id: ryr2
name: Ryanodine receptor 2 (RyR2)
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-03
summary: "Cardiac SR Ca²⁺-release channel (gene RYR2). CICR amplifier: a small Cav1.2 trigger Ca²⁺ current activates RyR2 tetramers on junctional SR, releasing ~75% of Ca²⁺ driving each heartbeat. PKA (Ser2808) and CaMKII (Ser2814) phosphorylation increase spark frequency."
aliases: ["RyR2", "RYR2", "cardiac ryanodine receptor", "type 2 ryanodine receptor"]
sources:
  - id: bers-2002-cardiac-ec-coupling
    type: peer-reviewed
    cite: "Bers DM. Cardiac excitation-contraction coupling. Nature. 2002;415(6868):198-205."
    doi: "10.1038/415198a"
    pmid: "11805843"
    url: "https://doi.org/10.1038/415198a"
  - id: marks-1989-ryr2-cloning
    type: peer-reviewed
    cite: "Marks AR, Fleischer S, Bhatt DL. Ryanodine receptor 2, a calcium release channel in the sarcoplasmic reticulum. J Clin Invest. 1989;83(3):872-878."
    doi: "10.1172/JCI113967"
    pmid: "2537625"
    url: "https://doi.org/10.1172/JCI113967"
  - id: wehrens-2003-pka-ryr2
    type: peer-reviewed
    cite: "Wehrens XH, Lehnart SE, Reiken SR, et al. Ca2+/calmodulin-dependent protein kinase II phosphorylation regulates the cardiac ryanodine receptor. Circ Res. 2004;94(6):e61-70."
    doi: "10.1161/01.RES.0000125626.33738.E2"
    pmid: "15016728"
    url: "https://doi.org/10.1161/01.RES.0000125626.33738.E2"
  - id: priori-2001-cpvt-ryr2
    type: peer-reviewed
    cite: "Priori SG, Napolitano C, Tiso N, et al. Mutations in the cardiac ryanodine receptor gene (hRyR2) underlie catecholaminergic polymorphic ventricular tachycardia. Circulation. 2001;103(2):196-200."
    doi: "10.1161/01.CIR.103.2.196"
    pmid: "11208676"
    url: "https://doi.org/10.1161/01.CIR.103.2.196"
cross_links:
  - target: 01-human/02-atomic/calcium
    relation: modulates
    note: "RyR2 is the primary Ca²⁺ release channel of the junctional SR; its opening during CICR accounts for ~75% of the Ca²⁺ driving each cardiac contraction."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: expressed-by
    note: "RyR2 is expressed exclusively in cardiomyocytes among muscle cell types; it forms the junctional SR release units at T-tubule dyads."
  - target: 01-human/03-molecular/beta1-adrenergic-receptor
    relation: modulated-by
    note: "β1-AR/PKA phosphorylates RyR2 at Ser2808 and CaMKII phosphorylates Ser2814, increasing channel open probability and SR Ca²⁺ spark frequency."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "CaMKII hyperactivation in HFrEF → RyR2 Ser2814 hyperphosphorylation → increased diastolic Ca²⁺ leak → SR Ca²⁺ depletion + delayed afterdepolarizations → arrhythmia; diastolic RyR2 leak links Ca²⁺ cycling dysfunction to sudden cardiac death in heart failure."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "RyR2 CICR amplifies a small Cav1.2 trigger into full cardiac Ca²⁺ transient (~75% SR-derived); RyR2 gating kinetics set contractile force; PKA/CaMKII phosphorylation mediates sympathetic inotropy; RyR2 GOF mutations cause CPVT — life-threatening adrenergic arrhythmia."
taxonomy:
  uniprot: "Q92736"
  gene_symbol: "RYR2"
  chromosome: "1q43"
---

# Ryanodine receptor 2 (RyR2)

## Overview

The ryanodine receptor type 2 (RyR2) is the **cardiac sarcoplasmic reticulum (SR) Ca²⁺-release channel** — the molecular amplifier at the heart of every heartbeat. Its gene, `RYR2`, encodes a massive ~560 kDa subunit that assembles as a **homotetramer (~2.2 MDa)** on the membrane of the junctional SR, positioned precisely opposite the L-type Ca²⁺ channels (Cav1.2) in the T-tubule membrane at the dyadic cleft [^bers-2002-cardiac-ec-coupling].

During each action potential, a small Ca²⁺ current through Cav1.2 (~6 pA for a few hundred milliseconds) raises local [Ca²⁺] in the 10–15 nm dyadic cleft to ~10–100 µM, triggering the opening of RyR2 tetramers. This **calcium-induced calcium release (CICR)** allows a tiny trigger signal to release a much larger Ca²⁺ store from the SR — the mechanism that amplifies each action potential into a forceful, full-scale contraction.

## Structure

### Domain Architecture

Each RyR2 subunit (~4967 amino acids in humans) is one of the largest ion-channel proteins known:

| Domain region | Function |
|:---|:---|
| **N-terminal SPRY domains (1–1530)** | Protein–protein interactions; binding of FK506-binding protein 12.6 (FKBP12.6/calstabin) |
| **Central domain / handle domain** | Mechanical transduction of conformational changes |
| **EF-hand domains** | Ca²⁺ sensing — Ca²⁺ binding here contributes to both activation (cytoplasmic) and inactivation (luminal) |
| **Channel-forming transmembrane domain (C-terminus)** | 6 transmembrane helices (S1–S6); S5–S6 form the pore; similar topology to Kv channels |
| **Selectivity filter** | Weakly selective for Ca²⁺ over K⁺/Na⁺; conductance ~80–100 pS in symmetrical Ca²⁺ solutions |

The assembled tetramer has fourfold symmetry visible by cryo-EM: four cytoplasmic "clover-leaf" domains (~80 Å in diameter each) project into the SR lumen and cytoplasm, surrounding the central pore.

### Regulatory Proteins

RyR2 function is tightly controlled by a network of associated proteins:

| Protein | Location | Effect |
|:---|:---|:---|
| **FKBP12.6 (calstabin-2)** | Cytoplasmic face, one per subunit | Stabilizes closed state; maintains Ca²⁺ spark frequency; dissociated by PKA hyperphosphorylation |
| **Calsequestrin-2 (CASQ2)** | SR lumen | High-capacity SR Ca²⁺ buffer; luminal Ca²⁺ sensor; mutations cause CPVT2 |
| **Triadin / Junctin** | SR lumen, transmembrane | Links CASQ2 to RyR2 at the junctional face |
| **Calmodulin (CaM)** | Cytoplasmic | Inhibitory at high [Ca²⁺]; one CaM per RyR2 subunit |
| **PKA (via mAKAP scaffold)** | Cytoplasmic | Phosphorylates Ser2808 → increased Po |
| **CaMKII** | Cytoplasmic | Phosphorylates Ser2814 → increased Ca²⁺ spark rate in chronic heart failure |

## Mechanism

### CICR at the Dyadic Cleft

The CICR sequence in a single heartbeat:

1. **Phase 2 action potential:** Cav1.2 channels in the T-tubule open → ~6 pA Ca²⁺ influx, raising local [Ca²⁺] at the dyadic cleft from ~100 nM to ~10–100 µM.
2. **RyR2 gating:** The elevated dyadic Ca²⁺ binds to the cytoplasmic activation site on RyR2. Channel open probability (Po) rises steeply — the Hill coefficient is ~2–3 (cooperative). Clusters of 5–50 RyR2 tetramers open together to produce a **Ca²⁺ spark** (detected by confocal microscopy as a brief, local fluorescence signal).
3. **Spatial summation:** Sparks from hundreds of dyadic junctions sum globally across the cell to produce the **Ca²⁺ transient** (peak ~1 µM), which activates the contractile apparatus.
4. **Inactivation:** As SR [Ca²⁺] depletes, luminal Ca²⁺ falls, leading to RyR2 closure (Ca²⁺-dependent inactivation). The Mg²⁺ concentration (competitive inhibitor at the cytoplasmic site) and rising cytoplasmic [Ca²⁺] also promote closure.

### Spark Termination

Individual Ca²⁺ sparks last ~50 ms and terminate despite continued Cav1.2 activity. Termination is ensured by:
- SR Ca²⁺ depletion → luminal [Ca²⁺] falls below the threshold sustaining RyR2 opening
- Stochastic attrition — individual RyR2 channels within the cluster randomly close when luminal Ca²⁺ falls
- STOC-SPAN model: spatial separation between clusters prevents global propagation

## Function

### Contribution to Ca²⁺ Transient

The relative contributions to each cardiac Ca²⁺ transient:

| Source | % of total Ca²⁺ transient |
|:---:|:---:|
| SR via RyR2 (CICR) | ~75% |
| L-type channel (Cav1.2) | ~25% |

This 75:25 ratio is the basis of the phrase "trigger:amplifier" — the L-type channel provides the trigger, RyR2 provides the amplification. In failing myocardium, SR Ca²⁺ content falls (SERCA2a down-regulated, PLN hyper-inhibited), reducing the SR contribution.

### Spark Frequency at Rest

Even at diastole, individual RyR2 clusters occasionally open spontaneously — producing **diastolic sparks** (~1–3 per cell per second at rest). This low spark rate is controlled by FKBP12.6/calstabin. If diastolic Ca²⁺ spark frequency rises excessively (as in CPVT or heart failure), the cumulative Ca²⁺ release activates NCX forward mode → net inward current → **delayed afterdepolarization (DAD)** → triggered arrhythmia.

## Connections

- `modulates` → **[Calcium](../../02-atomic/calcium/README.md)** — RyR2 is the dominant source of SR Ca²⁺ released each heartbeat; its gating directly controls the cytosolic Ca²⁺ transient amplitude.
- `expressed-by` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — RyR2 is the cardiac-specific SR release channel, expressed throughout working and conduction-system cardiomyocytes.
- `modulated-by` → **[β1-Adrenergic Receptor](../beta1-adrenergic-receptor/README.md)** — PKA downstream of β1-AR phosphorylates Ser2808; CaMKII (activated by the same Ca²⁺ transient it gates) phosphorylates Ser2814, both increasing Ca²⁺ spark frequency and SR Ca²⁺ release gain.
- `connects-to` → **[Heart Failure](../../07-system/heart-failure/README.md)** — CaMKII hyperactivation in HFrEF → RyR2 Ser2814 hyperphosphorylation → increased diastolic Ca²⁺ leak → SR Ca²⁺ depletion + delayed afterdepolarizations → arrhythmia; diastolic RyR2 leak links Ca²⁺ cycling dysfunction to sudden cardiac death in heart failure.
- `connects-to` → **[Cardiovascular System](../../07-system/cardiovascular-system/README.md)** — RyR2 CICR amplifies a small Cav1.2 trigger into full cardiac Ca²⁺ transient (~75% SR-derived); RyR2 gating kinetics set contractile force; PKA/CaMKII phosphorylation mediates sympathetic inotropy; RyR2 GOF mutations cause CPVT — life-threatening adrenergic arrhythmia.

## Pathology

| Disease | RyR2 mechanism |
|:---|:---|
| **Catecholaminergic polymorphic VT (CPVT1)** | Gain-of-function mutations in RYR2 (>200 known); increased diastolic Ca²⁺ leak → DADs → arrhythmia under adrenergic stress. Autosomal dominant; life-threatening without beta-blocker or flecainide therapy [^priori-2001-cpvt-ryr2] |
| **Heart failure** | CaMKII hyperactivation → Ser2814 hyperphosphorylation → increased diastolic Ca²⁺ leak → reduced SR Ca²⁺ load (contributing to impaired contractility) + increased arrhythmia risk |
| **Arrhythmogenic cardiomyopathy (ACM)** | Rare RYR2 mutations distinct from CPVT; disrupted channel gating with structural remodeling |

## See Also

- [Calcium](../../02-atomic/calcium/README.md) — the ion RyR2 releases and senses.
- [Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md) — the cell expressing RyR2.
- [SERCA2a](serca2a/README.md) — the SR pump that refills the SR after RyR2 release.
- [β1-adrenergic receptor](beta1-adrenergic-receptor/README.md) — upstream modulator via PKA.

[^bers-2002-cardiac-ec-coupling]: Bers DM. Cardiac excitation-contraction coupling. *Nature.* 2002;415(6868):198-205. [doi:10.1038/415198a](https://doi.org/10.1038/415198a) · [PubMed 11805843](https://pubmed.ncbi.nlm.nih.gov/11805843/)
[^marks-1989-ryr2-cloning]: Marks AR, Fleischer S, Bhatt DL. Ryanodine receptor 2, a calcium release channel in the sarcoplasmic reticulum. *J Clin Invest.* 1989;83(3):872-878. [doi:10.1172/JCI113967](https://doi.org/10.1172/JCI113967) · [PubMed 2537625](https://pubmed.ncbi.nlm.nih.gov/2537625/)
[^wehrens-2003-pka-ryr2]: Wehrens XH, Lehnart SE, Reiken SR, et al. Ca2+/calmodulin-dependent protein kinase II phosphorylation regulates the cardiac ryanodine receptor. *Circ Res.* 2004;94(6):e61-70. [doi:10.1161/01.RES.0000125626.33738.E2](https://doi.org/10.1161/01.RES.0000125626.33738.E2) · [PubMed 15016728](https://pubmed.ncbi.nlm.nih.gov/15016728/)
[^priori-2001-cpvt-ryr2]: Priori SG, Napolitano C, Tiso N, et al. Mutations in the cardiac ryanodine receptor gene (hRyR2) underlie catecholaminergic polymorphic ventricular tachycardia. *Circulation.* 2001;103(2):196-200. [doi:10.1161/01.CIR.103.2.196](https://doi.org/10.1161/01.CIR.103.2.196) · [PubMed 11208676](https://pubmed.ncbi.nlm.nih.gov/11208676/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
