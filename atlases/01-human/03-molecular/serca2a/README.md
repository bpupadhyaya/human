---
schema: human-scale-entry/v1
id: serca2a
name: SERCA2a
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-03
summary: "SR/ER Ca²⁺-ATPase isoform 2a (gene ATP2A2). Cardiac SR Ca²⁺ reuptake pump: uses 2 ATP per cycle to transport 2 Ca²⁺ from cytosol to SR lumen, restoring diastolic [Ca²⁺]i to ~100 nM. Tonically inhibited by phospholamban; β1-AR/PKA disinhibits via PLN phosphorylation."
aliases: ["SERCA2a", "ATP2A2", "SR Ca2+-ATPase", "sarcoendoplasmic reticulum calcium ATPase 2a"]
sources:
  - id: maclennan-2003-serca-pln
    type: peer-reviewed
    cite: "MacLennan DH, Kranias EG. Phospholamban: a crucial regulator of cardiac contractility. Nat Rev Mol Cell Biol. 2003;4(7):566-77."
    doi: "10.1038/nrm1151"
    pmid: "12838339"
    url: "https://doi.org/10.1038/nrm1151"
  - id: bers-2002-cardiac-ec-coupling
    type: peer-reviewed
    cite: "Bers DM. Cardiac excitation-contraction coupling. Nature. 2002;415(6868):198-205."
    doi: "10.1038/415198a"
    pmid: "11805843"
    url: "https://doi.org/10.1038/415198a"
  - id: periasamy-1999-serca-review
    type: peer-reviewed
    cite: "Periasamy M, Bhargava V. Sarcoplasmic reticulum calcium ATPase pump expression and its relevance to cardiac muscle physiology and pathology. Cardiovasc Res. 1999;42(3):583-597."
    doi: "10.1016/S0008-6363(99)00042-4"
    pmid: "10533672"
    url: "https://doi.org/10.1016/S0008-6363(99)00042-4"
  - id: jessup-2011-serca2a-gene-therapy
    type: peer-reviewed
    cite: "Jessup M, Greenberg B, Mancini D, et al. Calcium upregulation by percutaneous administration of gene therapy in cardiac disease (CUPID). Circulation. 2011;124(3):304-13."
    doi: "10.1161/CIRCULATIONAHA.111.022889"
    pmid: "21709064"
    url: "https://doi.org/10.1161/CIRCULATIONAHA.111.022889"
cross_links:
  - target: 01-human/02-atomic/calcium
    relation: modulates
    note: "SERCA2a is the primary Ca²⁺ reuptake pump of the cardiac SR, responsible for ~70% of Ca²⁺ removal from the cytosol after each contraction, restoring diastolic [Ca²⁺]i."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: expressed-by
    note: "SERCA2a is the dominant SERCA isoform in adult ventricular cardiomyocytes, localised to the longitudinal SR membrane."
  - target: 01-human/03-molecular/beta1-adrenergic-receptor
    relation: modulated-by
    note: "β1-AR/PKA phosphorylates phospholamban (PLN) at Ser16, relieving PLN inhibition of SERCA2a → faster Ca²⁺ reuptake → faster relaxation (lusitropy) and larger SR Ca²⁺ load."
  - target: 01-human/03-molecular/phospholamban
    relation: modulated-by
    note: "Dephosphorylated phospholamban (PLN) binds SERCA2a and reduces its Ca²⁺ affinity (Km from ~0.2 µM to ~0.6 µM); PLN phosphorylation by PKA/CaMKII relieves this inhibition."
taxonomy:
  uniprot: "P16615"
  gene_symbol: "ATP2A2"
  chromosome: "12q24.11"
---

# SERCA2a

## Overview

SERCA2a (Sarco/Endoplasmic Reticulum Ca²⁺-ATPase isoform 2a) is the **dominant Ca²⁺ reuptake pump of the cardiac sarcoplasmic reticulum (SR)** and the molecular engine of diastolic Ca²⁺ removal. Encoded by `ATP2A2`, it is an ~110 kDa P-type ATPase residing in the longitudinal SR membrane of cardiomyocytes. Each catalytic cycle couples the hydrolysis of **one ATP** to the active transport of **two Ca²⁺ ions** from the cytosol into the SR lumen against a steep electrochemical gradient [^maclennan-2003-serca-pln].

At the physiological level, SERCA2a is responsible for approximately **70% of cytosolic Ca²⁺ removal** following each systole in human ventricular myocytes (the remaining ~28% is handled by the Na⁺/Ca²⁺ exchanger NCX1, with minor contributions from the sarcolemmal Ca²⁺-ATPase and mitochondrial uniporter). By refilling the SR Ca²⁺ store, SERCA2a simultaneously:

1. Lowers cytosolic [Ca²⁺] back to ~100 nM → enables muscle relaxation (lusitropy)
2. Refills the SR → provides the Ca²⁺ available for the next contraction cycle

SERCA2a function is tonically inhibited by **phospholamban (PLN)** — a 52-amino acid micropeptide that is the principal physiological brake on pump activity. This PLN–SERCA2a binary interaction is a central node of sympathetic heart rate and contractility regulation [^maclennan-2003-serca-pln].

## Structure

### P-type ATPase Architecture

SERCA2a shares the canonical P-type ATPase fold: a single 110 kDa polypeptide with **10 transmembrane (TM) helices** and three cytoplasmic domains:

| Domain | Location | Function |
|:---|:---|:---|
| **Actuator domain (A)** | Cytoplasmic, N-terminal | Couples ATP hydrolysis to TM motion; contains the invariant Glu-239 |
| **Nucleotide-binding domain (N)** | Cytoplasmic, central | ATP binding; the largest cytoplasmic domain |
| **Phosphorylation domain (P)** | Cytoplasmic, between TM4–5 | Catalytic Asp-351; phosphorylated transiently during the E1P→E2P catalytic cycle |
| **TM1–TM10 bundle** | Membrane | Ca²⁺ binding sites (site I: Asn-768/Glu-771/Thr-799/Asp-800; site II: Glu-309/Asn-796/Asp-800/Glu-908); conformational change drives Ca²⁺ translocation |

### Isoforms

The `ATP2A` gene family encodes three SERCA genes:

| Gene | Isoform | Predominant tissue |
|:---|:---|:---|
| `ATP2A1` | SERCA1a/1b | Fast-twitch skeletal muscle |
| **`ATP2A2`** | **SERCA2a** | **Cardiac and slow-twitch skeletal muscle** |
| `ATP2A2` | SERCA2b | Ubiquitous (longer C-terminus, higher Ca²⁺ affinity) |
| `ATP2A3` | SERCA3 | Platelets, immune cells, epithelium |

SERCA2a differs from SERCA2b only in its shorter C-terminal extension; this structural difference lowers its Ca²⁺ affinity (higher Km) relative to SERCA2b, which is the basis of the regulatory modulation by PLN.

## Mechanism

### Catalytic Cycle (Post-Albers Model)

SERCA2a alternates between two principal conformational states:

```
E1 · 2Ca²⁺ + ATP  →  E1P · 2Ca²⁺  →  E2P  →  E2 + 2Ca²⁺(lumen)  →  E1
     (cytosol)         (phospho-E1)   (occluded)     (Ca²⁺ released)
```

1. **E1 state:** High affinity for cytosolic Ca²⁺ (Km ~0.2 µM when uninhibited). Binds 2 Ca²⁺ at the luminal sites I and II.
2. **Phosphorylation:** ATP transfers its γ-phosphate to Asp-351 → phosphoenzyme (E1P).
3. **Conformational change:** TM helices move, occluding and then releasing the 2 Ca²⁺ into the SR lumen at low affinity (Ca²⁺ cannot re-bind from the lumen in E2P).
4. **Dephosphorylation:** Pi released → pump returns to E1 state, ready for the next cycle.

**Km for Ca²⁺:** ~0.2 µM (uninhibited SERCA2a) vs. ~0.6 µM (PLN-bound, dephosphorylated SERCA2a). This threefold shift in affinity is the mechanism by which PLN reduces pump rate at diastolic [Ca²⁺] levels.

### Regulation by Phospholamban

Unphosphorylated PLN inserts its transmembrane helix alongside TM2 of SERCA2a, stabilizing the E2 conformation and reducing the apparent Ca²⁺ affinity. PKA-mediated phosphorylation of PLN at **Ser16** (and CaMKII-mediated phosphorylation at **Thr17**) disrupts this interaction, allowing SERCA2a to operate at its intrinsic higher Ca²⁺ affinity — resulting in faster Ca²⁺ reuptake, faster relaxation, and greater SR Ca²⁺ loading [^maclennan-2003-serca-pln].

## Function

### Contribution to Ca²⁺ Removal and Relaxation

In human ventricular myocytes, the fractional Ca²⁺ removal by each pathway per beat:

| Pathway | Fractional removal |
|:---:|:---:|
| **SERCA2a (SR uptake)** | ~70% |
| NCX1 (extrusion) | ~28% |
| Sarcolemmal Ca²⁺-ATPase | ~1% |
| Mitochondrial uniporter | ~1% |

The predominance of SERCA2a (vs. NCX1 in some species) means that in human myocardium, most of the Ca²⁺ released each beat is recaptured into the SR, maintaining SR Ca²⁺ content relatively constant beat-to-beat. This contrasts with rabbit myocytes where NCX1 contributes ~50%.

### Frequency-Dependent Augmentation

At higher heart rates, increased CaMKII activity phosphorylates PLN at Thr17, partially disinhibiting SERCA2a → more SR Ca²⁺ loading per cycle → larger Ca²⁺ transient → stronger contraction (positive force-frequency relationship / Bowditch effect). This is one mechanism underlying increased contractility during exercise even without exogenous catecholamine stimulation.

## Connections

- **Modulates** → [Calcium](../../02-atomic/calcium/README.md): SERCA2a controls the rate and extent of cytosolic Ca²⁺ removal, setting the kinetics of cardiac relaxation and the SR Ca²⁺ load available for the next contraction.
- **Expressed-by** → [Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md): SERCA2a is the cardiac SR pump, targeted to the longitudinal SR membrane of ventricular and atrial cardiomyocytes.
- **Modulated-by** → [β1-adrenergic receptor](beta1-adrenergic-receptor/README.md): PKA downstream of β1-AR phosphorylates PLN, relieving SERCA2a inhibition → faster Ca²⁺ reuptake → lusitropy + increased SR loading.
- **Modulated-by** → [Phospholamban](phospholamban/README.md): Dephosphorylated PLN is the tonic inhibitor of SERCA2a at the physiological [Ca²⁺] of diastole; phosphorylation relieves this brake.

## Pathology

| Disease | SERCA2a mechanism |
|:---|:---|
| **Heart failure with reduced EF (HFrEF)** | SERCA2a expression and activity are reduced by 30–50%; Ca²⁺ reuptake is slower; diastolic [Ca²⁺] is elevated; SR Ca²⁺ load is reduced → reduced systolic Ca²⁺ transient → reduced contractility and impaired relaxation [^periasamy-1999-serca-review] |
| **Diastolic dysfunction (HFpEF)** | Impaired SERCA2a kinetics prolong Ca²⁺ transient decay → slower isovolumic relaxation time (IVRT) → elevated filling pressures |
| **SERCA2a gene therapy** | AAV1-SERCA2a (CUPID trial) delivered by intracoronary infusion in HFrEF patients; improved NYHA class and hospitalisations in phase 2a; phase 2b/3 showed no significant benefit — ongoing investigation into vector efficiency and patient selection [^jessup-2011-serca2a-gene-therapy] |
| **Darier disease** | Autosomal dominant mutations in `ATP2A2`; keratinocyte SERCA2 (isoform 2b) dysfunction → acantholytic skin disorder; cardiac isoform 2a spared in skin, but cardiac SERCA2 may be mildly affected in some patients |

## See Also

- [Phospholamban](phospholamban/README.md) — tonic inhibitor and PKA-regulatory node.
- [RyR2](ryr2/README.md) — the Ca²⁺ release channel refilled by SERCA2a.
- [Calcium](../../02-atomic/calcium/README.md) — the ion transported.
- [Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md) — the expressing cell.

[^maclennan-2003-serca-pln]: MacLennan DH, Kranias EG. Phospholamban: a crucial regulator of cardiac contractility. *Nat Rev Mol Cell Biol.* 2003;4(7):566-77. [doi:10.1038/nrm1151](https://doi.org/10.1038/nrm1151) · [PubMed 12838339](https://pubmed.ncbi.nlm.nih.gov/12838339/)
[^bers-2002-cardiac-ec-coupling]: Bers DM. Cardiac excitation-contraction coupling. *Nature.* 2002;415(6868):198-205. [doi:10.1038/415198a](https://doi.org/10.1038/415198a) · [PubMed 11805843](https://pubmed.ncbi.nlm.nih.gov/11805843/)
[^periasamy-1999-serca-review]: Periasamy M, Bhargava V. Sarcoplasmic reticulum calcium ATPase pump expression and its relevance to cardiac muscle physiology and pathology. *Cardiovasc Res.* 1999;42(3):583-597. [doi:10.1016/S0008-6363(99)00042-4](https://doi.org/10.1016/S0008-6363(99)00042-4) · [PubMed 10533672](https://pubmed.ncbi.nlm.nih.gov/10533672/)
[^jessup-2011-serca2a-gene-therapy]: Jessup M, Greenberg B, Mancini D, et al. Calcium upregulation by percutaneous administration of gene therapy in cardiac disease (CUPID). *Circulation.* 2011;124(3):304-13. [doi:10.1161/CIRCULATIONAHA.111.022889](https://doi.org/10.1161/CIRCULATIONAHA.111.022889) · [PubMed 21709064](https://pubmed.ncbi.nlm.nih.gov/21709064/)
