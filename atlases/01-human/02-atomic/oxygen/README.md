---
schema: human-scale-entry/v1
id: oxygen
name: Oxygen
atlas: 01-human
scale: 02-atomic
status: draft
last_reviewed: 2026-06-03
summary: "Oxygen (O, Z=8, [He] 2s² 2p⁴). Biologically as O₂ (respiratory substrate, ~250 mL/min at rest), O²⁻ (superoxide, ROS), and cofactor in oxidases. Carried by haemoglobin in erythrocytes; released by Bohr effect. Rises 20-fold in maximal exercise."
aliases: ["O", "O2", "dioxygen", "molecular oxygen", "O₂"]
sources:
  - id: west-respiratory-physiology
    type: textbook
    cite: "West JB, Luks AM. West's Respiratory Physiology: The Essentials. 10th ed. Wolters Kluwer; 2016. ISBN 978-1-4963-1011-1."
    url: "https://www.lww.com/Product/9781496310118"
    accessed: "2026-06-03"
  - id: perutz-1979-haemoglobin
    type: peer-reviewed
    cite: "Perutz MF. Regulation of oxygen affinity of hemoglobin: influence of structure of the globin on the heme iron. Annu Rev Biochem. 1979;48:327-86."
    doi: "10.1146/annurev.bi.48.070179.001551"
    pmid: "382986"
    url: "https://doi.org/10.1146/annurev.bi.48.070179.001551"
  - id: weibel-2004-symmorphosis
    type: peer-reviewed
    cite: "Weibel ER, Taylor CR, Hoppeler H. The concept of symmorphosis: a testable hypothesis of structure-function relationship. Proc Natl Acad Sci USA. 1991;88(22):10357-61."
    doi: "10.1073/pnas.88.22.10357"
    pmid: "1720538"
    url: "https://doi.org/10.1073/pnas.88.22.10357"
  - id: stryer-biochemistry
    type: textbook
    cite: "Berg JM, Tymoczko JL, Stryer L. Biochemistry. 9th ed. W.H. Freeman; 2019. ISBN 978-1-319-11467-1."
    url: "https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X"
    accessed: "2026-06-03"
cross_links:
  - target: 01-human/04-cellular/cardiomyocyte
    relation: modulates
    note: "O₂ is the terminal electron acceptor of oxidative phosphorylation in cardiomyocyte mitochondria; ~95% of cardiac ATP production depends on aerobic O₂ consumption."
  - target: 01-human/01-subatomic/electron
    relation: modulated-by
    note: "The electron configuration of O ([He] 2s² 2p⁴) determines O₂ reactivity: two unpaired electrons in π* antibonding orbitals make O₂ paramagnetic and a diradical, explaining its reduction to superoxide (O₂⁻) and water (H₂O) in mitochondrial electron transport."
  - target: 01-human/04-cellular/erythrocyte
    relation: modulated-by
    evidence: perutz-1979-haemoglobin
    note: "Erythrocytes carry ~250 million haemoglobin tetramers each; 25 trillion RBCs deliver ~250 mL O₂/min at rest, binding O₂ cooperatively in the lungs (P₅₀ ~26 mmHg) and releasing it via the Bohr effect in tissues."
taxonomy:
  element_symbol: "O"
  atomic_number: 8
  atomic_mass: "15.999"
  cas: "7782-44-7"
---

# Oxygen

## Overview

Oxygen (symbol O, atomic number 8, atomic mass 15.999 u) is the eighth element of the periodic table and the **most abundant element by mass in the human body** (~65%), where it exists primarily in water molecules (H₂O). Its ground-state electron configuration is [He] 2s² 2p⁴ — with two unpaired electrons in the 2p shell that make molecular oxygen (O₂) a **paramagnetic diradical**, explaining its unusual reactivity: O₂ does not readily accept two electrons simultaneously (spin barrier), so it is reduced one electron at a time in biological systems, yielding the reactive oxygen species (ROS) superoxide (O₂⁻·), hydrogen peroxide (H₂O₂), and hydroxyl radical (HO·) as intermediates [^stryer-biochemistry].

In medicine and physiology, oxygen is primarily considered as the **terminal electron acceptor** of aerobic metabolism: the mitochondrial electron transport chain passes electrons from NADH and FADH₂ through Complexes I–IV to O₂, generating ~32 ATP per molecule of glucose oxidised — compared to only 2 ATP by anaerobic glycolysis. This ~16-fold energetic advantage of aerobic over anaerobic metabolism is why all high-demand tissues (brain, heart, exercising muscle) are absolutely dependent on continuous O₂ delivery.

## Structure

### Atomic Properties

| Property | Value |
|:---|:---|
| Atomic number (Z) | 8 |
| Atomic mass | 15.999 u |
| Electron configuration | [He] 2s² 2p⁴ |
| Common valence | −2 (in most biological molecules) |
| Electronegativity (Pauling) | 3.44 (second only to fluorine) |
| Atomic radius | 66 pm |

### O₂ Molecular Properties

Molecular dioxygen (O₂) is formed by covalent combination of two oxygen atoms sharing a triple bond equivalent (one σ + one π from each unpaired 2p electron → actually one σ + two degenerate π*):

| Property | O₂ |
|:---|:---|
| Bond order | 2 (double bond) |
| Bond length | 121 pm |
| Dipole moment | 0 (homonuclear, symmetrical) |
| Solubility in blood plasma at 37°C | ~0.003 mL O₂/mL/mmHg (Henry's law constant) |
| Paramagnetic | Yes (2 unpaired electrons in degenerate π* orbitals) |
| Boiling point | −183°C (makes liquid O₂ therapy possible) |

The low aqueous solubility of O₂ (~0.25 mL/100 mL plasma at PaO₂ 100 mmHg) is why haemoglobin is essential: it increases O₂ carrying capacity ~70-fold (blood carries ~20 mL O₂/100 mL vs. 0.3 mL dissolved) [^west-respiratory-physiology].

## Function

### O₂ as the Terminal Electron Acceptor

Mitochondrial oxidative phosphorylation is the dominant O₂-consuming process in aerobic organisms. The chain:

1. Glucose (or fatty acids) → acetyl-CoA → TCA cycle → NADH + FADH₂
2. Complex I (NADH dehydrogenase) → electrons flow to CoQ
3. Complex III (cytochrome bc₁) → cytochrome c
4. **Complex IV (cytochrome c oxidase):** transfers 4 electrons + 4H⁺ to O₂ → **2 H₂O**; simultaneously pumps 4 H⁺ into the intermembrane space
5. ATP synthase uses the proton gradient to phosphorylate ADP → ATP

At rest, the whole body consumes approximately **250 mL O₂/min** (VO₂ rest); during maximal aerobic exercise, VO₂max rises to **3,000–6,000 mL/min** in trained athletes — a 12–24-fold range. The heart muscle alone consumes ~8–10 mL O₂/100 g/min at rest (compared to ~0.3 mL/100 g/min in resting skeletal muscle), reflecting its continuous ATP demand [^weibel-2004-symmorphosis].

### O₂ Delivery — The Fick Principle

Total O₂ delivery (DO₂) to tissues:

$$\text{DO}_2 = CO \times CaO_2$$

where CO is cardiac output and CaO₂ is arterial O₂ content:

$$CaO_2 = (Hb \times 1.34 \times SaO_2) + (PaO_2 \times 0.003)$$

At rest: CO ~5 L/min × CaO₂ ~20 mL/dL = **DO₂ ~1,000 mL/min**, with VO₂ ~250 mL/min → O₂ extraction ratio ~25%. Tissues have substantial O₂ extraction reserve, allowing VO₂ to rise 4-fold before anaerobic threshold.

### O₂ and Haemoglobin — The Bohr Effect

Haemoglobin (Hb) binds O₂ cooperatively (Hill coefficient ~2.8) at the haem iron:

$$\text{HbFe}^{2+} + \text{O}_2 \rightleftharpoons \text{HbFe}^{2+}\text{-O}_2$$

The sigmoidal O₂-dissociation curve (ODC) means:
- At the lungs (PO₂ ~100 mmHg): Hb is ~98% saturated
- At resting tissues (PO₂ ~40 mmHg): Hb falls to ~75% saturated → releases ~25% of carried O₂
- The **Bohr effect**: rising PCO₂ and falling pH (from tissue CO₂ production) shift the ODC rightward, enhancing O₂ delivery to metabolically active tissues [^perutz-1979-haemoglobin]
- **2,3-BPG** in erythrocytes further right-shifts the ODC by stabilising the deoxy-Hb (T-state) conformation

## Connections

- **Modulates** → [Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md): O₂ is the terminal electron acceptor for oxidative phosphorylation in cardiomyocyte mitochondria; O₂ deprivation (ischemia) leads to ATP depletion and irreversible cardiomyocyte injury within ~20–40 minutes.
- **Modulated-by** → [Electron](../../01-subatomic/electron/README.md): The electronic structure of O₂ — two unpaired electrons in degenerate π* molecular orbitals — determines its paramagnetic character, its step-wise reduction to water through ROS intermediates, and its role as the terminal electron acceptor in Complex IV.

## Pathology

| Condition | O₂ mechanism |
|:---|:---|
| **Hypoxia** | Reduced PaO₂ → reduced CaO₂ → reduced DO₂ → tissue anaerobic metabolism → lactic acidosis; Hb-O₂ dissociation curve allows detection of reserve (pulse oximetry) |
| **Ischemia** | O₂ supply cut without global hypoxia; local demand exceeds supply → myocardial infarction, stroke |
| **Reactive oxygen species (ROS)** | One- and two-electron partial reduction of O₂ → O₂⁻· (superoxide), H₂O₂, HO· — damage proteins, lipids, DNA; generated by mitochondria under stress; normally scavenged by SOD, catalase, glutathione peroxidase |
| **Hyperoxia (high-dose O₂ therapy)** | Supraphysiological PO₂ → increased ROS generation → lung injury (O₂ toxicity); relevant in ICU/NICU settings |
| **Anaemia** | Low Hb → reduced CaO₂ → reduced DO₂ even with normal PaO₂ → compensatory tachycardia and increased cardiac output |

## See Also

- [Electron](../../01-subatomic/electron/README.md) — the particle transferred in O₂ reduction.
- [Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md) — major O₂ consumer.
- [Lung](../../06-organ/lung/README.md) — the organ that loads O₂ into haemoglobin.
- [Respiratory system](../../07-system/respiratory-system/README.md) — the system that delivers O₂ to the blood.

[^west-respiratory-physiology]: West JB, Luks AM. *West's Respiratory Physiology: The Essentials.* 10th ed. Wolters Kluwer; 2016. [lww.com/Product/9781496310118](https://www.lww.com/Product/9781496310118)
[^perutz-1979-haemoglobin]: Perutz MF. Regulation of oxygen affinity of hemoglobin. *Annu Rev Biochem.* 1979;48:327-86. [doi:10.1146/annurev.bi.48.070179.001551](https://doi.org/10.1146/annurev.bi.48.070179.001551) · [PubMed 382986](https://pubmed.ncbi.nlm.nih.gov/382986/)
[^weibel-2004-symmorphosis]: Weibel ER, Taylor CR, Hoppeler H. The concept of symmorphosis. *Proc Natl Acad Sci USA.* 1991;88(22):10357-61. [doi:10.1073/pnas.88.22.10357](https://doi.org/10.1073/pnas.88.22.10357) · [PubMed 1720538](https://pubmed.ncbi.nlm.nih.gov/1720538/)
[^stryer-biochemistry]: Berg JM, Tymoczko JL, Stryer L. *Biochemistry.* 9th ed. W.H. Freeman; 2019. [macmillanlearning.com](https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X)
