---
schema: human-scale-entry/v1
id: alveolus
name: Alveolus
atlas: 01-human
scale: 05-tissue
status: draft
last_reviewed: 2026-06-03
summary: "Functional gas-exchange unit of the lung — 0.2 mm diameter air sac lined by AT1 (95% surface, flat) and AT2 (5% surface, cuboidal/surfactant) cells on a shared basement membrane apposed to pulmonary capillaries. ~300 million alveoli provide ~70 m² surface area."
aliases: ["alveoli", "air sac", "pulmonary alveolus"]
sources:
  - id: weibel-2017-alveolar-dimensions
    type: peer-reviewed
    cite: "Weibel ER. Lung morphometry: the link between structure and function. Cell Tissue Res. 2017;367(3):413-26."
    doi: "10.1007/s00441-016-2541-4"
    pmid: "27981371"
    url: "https://doi.org/10.1007/s00441-016-2541-4"
  - id: crapo-1982-alveolar-morphometry
    type: peer-reviewed
    cite: "Crapo JD, Barry BE, Gehr P, Bachofen M, Weibel ER. Cell number and cell characteristics of the normal human lung. Am Rev Respir Dis. 1982;125(6):740-5."
    doi: "10.1164/arrd.1982.125.6.740"
    pmid: "7044530"
    url: "https://doi.org/10.1164/arrd.1982.125.6.740"
  - id: west-respiratory-physiology
    type: textbook
    cite: "West JB, Luks AM. West's Respiratory Physiology: The Essentials. 10th ed. Wolters Kluwer; 2016. ISBN 978-1-4963-1011-1."
    url: "https://www.lww.com/Product/9781496310118"
    accessed: "2026-06-03"
  - id: maina-2002-alveolar-structure
    type: peer-reviewed
    cite: "Maina JN, West JB. Thin and strong! The bioengineering dilemma in the structural and functional design of the blood-gas barrier. Physiol Rev. 2005;85(3):811-44."
    doi: "10.1152/physrev.00022.2004"
    pmid: "15987797"
    url: "https://doi.org/10.1152/physrev.00022.2004"
cross_links:
  - target: 01-human/04-cellular/type-ii-pneumocyte
    relation: composed-of
    note: "AT2 cells are the surfactant-producing and progenitor cells of the alveolar epithelium; they constitute ~60% of alveolar epithelial cells by number and occupy ~5% of the alveolar surface area."
  - target: 01-human/06-organ/lung
    relation: part-of
    note: "~300 million alveoli constitute the gas-exchange parenchyma of the lung, providing ~70 m² of surface area across which O₂ and CO₂ are exchanged."
  - target: 02-pathogen/02-bacteria/mycobacterium-tuberculosis
    relation: damaged-by
    note: "M. tuberculosis infects alveolar macrophages residing within alveoli, then spreads to the alveolar epithelium and parenchyma, causing granuloma formation and caseating necrosis that destroys alveolar structure."
  - target: 01-human/03-molecular/hemoglobin
    relation: modulated-by
    note: "Modulated by Hemoglobin."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: infected-by
    note: "Infected by Pneumocystis jirovecii (formerly carinii)."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: damaged-by
    note: "A. fumigatus conidia (2-3 µm) deposit in terminal alveoli; alveolar macrophages phagocytose via Dectin-1 within 4-8h; in neutropenic hosts, RodA hydrophobin shields conidia from Dectin-1 → germination → hyphal invasion of alveolar walls and vasculature."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "O₂ diffuses from alveolar gas (PAO₂ ~100 mmHg) across the 0.2-µm blood-gas barrier into pulmonary capillary blood (PO₂ ~40 mmHg venous); complete equilibration by ~0.25 s (one-third of capillary transit); Fick's law: V̇O₂ = D × A × ΔP/T defines efficiency."
taxonomy:
  uberon: "UBERON:0002299"
  fma: "FMA:7318"
---

# Alveolus

## Overview

The alveolus (Latin: *small cavity*; plural: alveoli) is the **functional unit of pulmonary gas exchange** — the terminal air sac at the end of the branching airways where inhaled oxygen diffuses into pulmonary capillary blood and CO₂ diffuses out. The lungs contain approximately **300 million alveoli** in the adult human [^crapo-1982-alveolar-morphometry], with a total internal surface area of approximately **70 m²** (the size of a small apartment floor) — an extraordinary surface-to-volume ratio engineered by evolution for maximal gas exchange.

Each alveolus is approximately **0.2 mm** in diameter — invisible to the naked eye — and is lined by a **continuous epithelium** composed of two principal cell types: the **alveolar type I (AT1)** cell (thin, flat, occupying ~95% of surface area) and the **alveolar type II (AT2)** cell (cuboidal, secretory, occupying ~5% of surface area but comprising ~60% of cells by count). The epithelium rests on a **shared basement membrane** apposed directly to the capillary endothelium — the two basement membranes are fused at many points, reducing the air-blood barrier to as little as 0.2–0.5 µm.

## Structure

### Alveolar Wall Architecture

The alveolar wall (septum) is an anatomical unit shared between adjacent alveoli:

| Layer | Components | Thickness |
|:---|:---|:---|
| **Type I epithelium** | Squamous AT1 cells (>95% surface); tight junctions | 50–200 nm (individual cell thickness) |
| **Type II epithelium** | Cuboidal AT2 cells; lamellar bodies; tight junctions | — (cellular) |
| **Epithelial basement membrane** | Collagen IV, laminin, fibronectin | ~50–100 nm |
| **Interstitium** | Variable; contains fibroblasts, elastic fibres, capillaries (thin/thick sides) | 0 at fused membrane → several µm |
| **Capillary basement membrane** | Collagen IV, laminin | ~50–100 nm |
| **Capillary endothelium** | Continuous fenestrated endothelium | ~200–300 nm |

The air-blood barrier has a **"thin" side** where the two basement membranes are fused and the barrier is ~0.2 µm — this is where most gas exchange occurs — and a **"thick" side** where an interstitial space allows capillary fluid exchange and immune cell passage. This structural asymmetry is beautifully described by Maina and West [^maina-2002-alveolar-structure].

### Alveolar Surface Film

The alveolar surface is covered by a thin (~0.02–0.1 µm) hypophase of fluid containing pulmonary surfactant secreted by AT2 cells. Surfactant reduces surface tension from ~70 mN/m (water) to <5 mN/m at minimum alveolar volume, preventing collapse. The surfactant layer also contains SP-A and SP-D (collectins), which are critical pattern-recognition molecules of the innate immune system — binding pathogens and facilitating macrophage phagocytosis.

### Alveolar Macrophage

Resident alveolar macrophages (AMs) patrol the alveolar surface, phagocytosing particles, debris, and pathogens. They are the most abundant leukocyte in the lung (~93% of bronchoalveolar lavage cells) and the first cellular responder to inhaled pathogens including *M. tuberculosis*.

### Dimensions

| Parameter | Value |
|:---|:---|
| Number of alveoli (adult) | ~300–500 million [^crapo-1982-alveolar-morphometry] |
| Mean alveolar diameter | ~0.2 mm |
| Total alveolar surface area | ~70 m² |
| Air-blood barrier thickness (thin side) | 0.2–0.5 µm |
| Alveolar volume at FRC | ~2.5 mL total / ~8 µL per alveolus |

## Function

### Gas Exchange by Passive Diffusion

Gas exchange across the alveolar-capillary membrane is driven entirely by **partial pressure gradients** and governed by Fick's law of diffusion:

$$V_{gas} = D \times A \times \frac{\Delta P}{T}$$

Where D is the diffusivity of the gas, A is the surface area, ΔP is the partial pressure difference, and T is membrane thickness.

At rest:
- **O₂:** Alveolar PO₂ ~100 mmHg; pulmonary capillary PO₂ ~40 mmHg (mixed venous) → gradient of ~60 mmHg → O₂ diffuses into blood
- **CO₂:** Alveolar PCO₂ ~40 mmHg; venous PCO₂ ~46 mmHg → gradient of ~6 mmHg → CO₂ diffuses into alveolus (CO₂ is ~20× more soluble than O₂ → smaller gradient sufficient)

Equilibration is virtually complete within ~0.25 s of the ~0.75 s capillary transit time at rest — giving a 3-fold safety margin. At maximal exercise (capillary transit time falls to ~0.25 s), the margin is eliminated and diffusion limitation may contribute to exercise hypoxaemia in elite athletes [^west-respiratory-physiology].

### Ventilation-Perfusion Matching (V̇/Q̇)

Each alveolus must receive both air (ventilation) and blood (perfusion) in matched proportions. The ideal V̇/Q̇ ratio is ~0.8–1.0. Gravity distributes both V̇ and Q̇ unevenly in the lung (dependent zones receive more of both), but Q̇ is more gravity-dependent → V̇/Q̇ is higher at the apex and lower at the base. V̇/Q̇ mismatch is the most common cause of hypoxaemia in respiratory disease.

### Mechanical Properties

The alveolar surface tension is the dominant determinant of lung compliance (C = ΔV/ΔP). Normal lung compliance ~200 mL/cmH₂O. Without surfactant (as in neonatal RDS or ARDS), compliance falls dramatically, requiring high inspiratory pressures to achieve adequate tidal volume.

## Connections

- **Composed-of** → [Type II pneumocyte](../../04-cellular/type-ii-pneumocyte/README.md): AT2 cells produce surfactant and serve as the alveolar stem cell; they constitute most alveolar epithelial cells by number and are concentrated at alveolar corners.
- **Part-of** → [Lung](../../06-organ/lung/README.md): Alveoli form the gas-exchange parenchyma of the lung; ~300 million alveoli account for most of the lung's internal volume.
- **Damaged-by** → [Mycobacterium tuberculosis](../../../02-pathogen/02-bacteria/mycobacterium-tuberculosis/README.md): Mtb infects alveolar macrophages, replicates intracellularly, and triggers granuloma formation that can cavitate and destroy alveolar structure, causing the pathological hallmark of pulmonary TB.
- `damaged-by` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — conidia (2-3 µm) deposit in terminal alveoli; alveolar macrophages phagocytose via Dectin-1 within 4-8h; in neutropenic hosts, RodA hydrophobin shields conidia from Dectin-1 → germination → hyphal invasion of alveolar walls and vasculature.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — O₂ diffuses from alveolar gas (PAO₂ ~100 mmHg) across the 0.2-µm blood-gas barrier; equilibration in ~0.25 s (one-third of capillary transit); Fick's law: V̇O₂ = D × A × ΔP/T defines gas transfer efficiency.

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

## Pathology

| Disease | Alveolar mechanism |
|:---|:---|
| **Acute respiratory distress syndrome (ARDS)** | Diffuse alveolar damage (DAD): epithelial and endothelial injury → flooding with protein-rich exudate (hyaline membranes), loss of surfactant → alveolar collapse → severe hypoxaemia |
| **Pneumonia** | Bacterial or viral invasion → inflammatory exudate fills alveoli → consolidation → impaired gas exchange |
| **Pulmonary fibrosis (IPF)** | Progressive replacement of normal alveolar architecture with fibrotic tissue → loss of gas-exchange units → restrictive ventilatory defect and diffusion impairment |
| **Emphysema** | Protease-mediated destruction of alveolar walls (septal destruction) → fewer, larger airspaces → reduced surface area → impaired O₂ diffusion |
| **Pulmonary oedema** | Alveolar flooding with fluid from elevated capillary hydrostatic pressure (cardiogenic) or capillary leak (non-cardiogenic) → impaired gas exchange |

## See Also

- [Type II pneumocyte](../../04-cellular/type-ii-pneumocyte/README.md) — the surfactant cell and alveolar stem cell.
- [Lung](../../06-organ/lung/README.md) — the organ composed of alveoli.
- [Oxygen](../../02-atomic/oxygen/README.md) — the gas exchanged.

[^weibel-2017-alveolar-dimensions]: Weibel ER. Lung morphometry: the link between structure and function. *Cell Tissue Res.* 2017;367(3):413-26. [doi:10.1007/s00441-016-2541-4](https://doi.org/10.1007/s00441-016-2541-4) · [PubMed 27981371](https://pubmed.ncbi.nlm.nih.gov/27981371/)
[^crapo-1982-alveolar-morphometry]: Crapo JD, Barry BE, Gehr P, Bachofen M, Weibel ER. Cell number and cell characteristics of the normal human lung. *Am Rev Respir Dis.* 1982;125(6):740-5. [doi:10.1164/arrd.1982.125.6.740](https://doi.org/10.1164/arrd.1982.125.6.740) · [PubMed 7044530](https://pubmed.ncbi.nlm.nih.gov/7044530/)
[^west-respiratory-physiology]: West JB, Luks AM. *West's Respiratory Physiology: The Essentials.* 10th ed. Wolters Kluwer; 2016. [lww.com/Product/9781496310118](https://www.lww.com/Product/9781496310118)
[^maina-2002-alveolar-structure]: Maina JN, West JB. Thin and strong! The bioengineering dilemma in the structural and functional design of the blood-gas barrier. *Physiol Rev.* 2005;85(3):811-44. [doi:10.1152/physrev.00022.2004](https://doi.org/10.1152/physrev.00022.2004) · [PubMed 15987797](https://pubmed.ncbi.nlm.nih.gov/15987797/)
