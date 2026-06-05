---
schema: human-scale-entry/v1
id: type-ii-pneumocyte
name: Type II pneumocyte
atlas: 01-human
scale: 04-cellular
status: draft
last_reviewed: 2026-06-03
summary: "Alveolar type II (AT2) cells — cuboidal surfactant-secreting cells (~5% of alveolar surface area, ~60% of alveolar epithelial cells by count). Synthesise pulmonary surfactant via lamellar bodies; regenerate alveolar epithelium after injury (alveolar stem cell)."
aliases: ["AT2 cell", "alveolar type II cell", "AT2", "type 2 alveolar cell", "great alveolar cell"]
sources:
  - id: fehrenbach-2001-at2-review
    type: peer-reviewed
    cite: "Fehrenbach H. Alveolar epithelial type II cell: defender of the alveolus revisited. Respir Res. 2001;2(1):33-46."
    doi: "10.1186/rr36"
    pmid: "11686863"
    url: "https://doi.org/10.1186/rr36"
  - id: whitsett-2002-surfactant-biology
    type: peer-reviewed
    cite: "Whitsett JA, Wert SE, Trapnell BC. Genetic disorders influencing lung formation and function at birth. Hum Mol Genet. 2004;13 Spec No 2:R207-15."
    doi: "10.1093/hmg/ddh252"
    pmid: "15358728"
    url: "https://doi.org/10.1093/hmg/ddh252"
  - id: mason-2006-at2-biology
    type: peer-reviewed
    cite: "Mason RJ. Biology of alveolar type II cells. Respirology. 2006;11(Suppl):S12-5."
    doi: "10.1111/j.1440-1843.2006.00800.x"
    pmid: "16423262"
    url: "https://doi.org/10.1111/j.1440-1843.2006.00800.x"
  - id: desai-2014-at2-stem-cell
    type: peer-reviewed
    cite: "Desai TJ, Brownfield DG, Krasnow MA. Alveolar progenitor and stem cells in lung development, renewal, and cancer. Nature. 2014;507(7491):190-4."
    doi: "10.1038/nature12930"
    pmid: "24499815"
    url: "https://doi.org/10.1038/nature12930"
cross_links:
  - target: 01-human/05-tissue/alveolus
    relation: part-of
    note: "AT2 cells are one of the two principal epithelial cell types lining the alveolar wall; they occupy ~5% of alveolar surface area but account for ~60% of alveolar epithelial cells by number."
  - target: 01-human/06-organ/lung
    relation: part-of
    note: "AT2 cells are distributed throughout the lung alveolar network; their surfactant secretion and stem-cell function are essential to normal lung physiology."
  - target: 02-pathogen/01-viruses/influenza-a
    relation: infected-by
    note: "Influenza A virus infects AT2 cells via sialic acid receptors; AT2 cells are a primary target in severe influenza, leading to diffuse alveolar damage and respiratory failure."
  - target: 02-pathogen/01-viruses/respiratory-syncytial-virus
    relation: infected-by
    note: "Infected by Respiratory Syncytial Virus."
taxonomy:
  cell_ontology: "CL:0002063"
  lineage: "endoderm — foregut — lung endoderm → NKX2.1+ progenitor → AT2"
---

# Type II pneumocyte

## Overview

The alveolar type II (AT2) pneumocyte is the **secretory, regenerative, and immunologically active** cell of the alveolar epithelium. While the alveolar type I (AT1) cell — a vast, extremely flat cell — covers approximately 95% of the alveolar surface and is the primary site of gas exchange, AT2 cells occupy only ~5% of the surface area but constitute approximately **60% of all alveolar epithelial cells by number** [^fehrenbach-2001-at2-review].

AT2 cells have three critical functions that make them indispensable to normal lung physiology:

1. **Surfactant synthesis and secretion:** The production and recycling of pulmonary surfactant — without which alveolar surface tension would cause alveolar collapse at end-expiration (atelectasis) and lung compliance would plummet.
2. **Alveolar epithelial repair (stem cell function):** Following injury, AT2 cells proliferate and differentiate into AT1 cells, regenerating the gas-exchange surface [^desai-2014-at2-stem-cell].
3. **Ion and fluid transport:** Active Na⁺ transport (via ENaC and Na⁺/K⁺-ATPase) drives reabsorption of alveolar fluid, maintaining a dry gas-exchange surface.

AT2 cells are also important targets for respiratory pathogens — particularly influenza A virus, SARS-CoV-2, and *Mycobacterium tuberculosis* — making their dysfunction central to the pathophysiology of many severe respiratory diseases.

## Structure

### Cell Morphology

| Feature | Value |
|:---|:---|
| Shape | Cuboidal; polygonal in flat sections |
| Diameter | ~8–10 µm |
| Location | Corners/junctions of alveolar walls ("nooks"), on basement membrane |
| Apical surface | Microvilli (abundant, unlike AT1 cells); lamellar body secretion occurs here |
| Tight junctions | Well-formed apical tight junctions (claudin-3, claudin-4, ZO-1) maintain epithelial barrier |

### Characteristic Organelles

- **Lamellar bodies:** The defining organelle of AT2 cells — lysosome-related organelles, 0.2–1 µm diameter, containing tightly wound phospholipid membranes (primarily dipalmitoylphosphatidylcholine, DPPC) and surfactant proteins (SP-B, SP-C essential for compaction and stability; SP-A, SP-D for innate immunity). Exocytosis of lamellar bodies releases surfactant into the alveolar fluid layer.
- **Multivesicular bodies:** Precursors to lamellar bodies; site of surfactant phospholipid trafficking
- **Abundant mitochondria:** Reflecting the high metabolic demand of continuous surfactant synthesis
- **Extensive rough ER and Golgi:** For surfactant protein synthesis and processing

### Surface Markers

Key proteins expressed by AT2 cells (used for identification):

| Marker | Gene | Function |
|:---|:---|:---|
| **Surfactant protein C (SP-C)** | `SFTPC` | Small hydrophobic protein essential for tubular myelin formation; AT2-specific marker |
| **Surfactant protein B (SP-B)** | `SFTPB` | Required for lamellar body biogenesis; without it, newborns die of respiratory failure |
| **ABCA3 transporter** | `ABCA3` | Transports phospholipids into lamellar bodies; mutations → surfactant deficiency disease |
| **TTF1/NKX2.1** | `NKX2-1` | Transcription factor driving SP-C, SP-B, ABCA3, and HopX expression; AT2 lineage marker |
| **HopX (HOP homeobox)** | `HOPX` | Expressed in AT2 and AT1 cells; marks AT2 stem cell subpopulation |
| **ACE2** | `ACE2` | Entry receptor for SARS-CoV-2 (and possibly SARS-CoV-1) |

## Function

### Surfactant Production and Secretion

Pulmonary surfactant is a complex mixture of phospholipids (~80–90%) and proteins (~10%), whose primary function is to **lower alveolar surface tension**, preventing alveolar collapse at end-expiration. The LaPlace law (P = 2γ/r) predicts that at the small radius (r ~0.05–0.1 mm) of a fully deflated alveolus, the collapsing pressure would be enormous without surfactant reducing γ from ~70 mN/m (water surface tension) to <5 mN/m at end-expiration [^mason-2006-at2-biology].

The surfactant synthesis cycle in AT2 cells:

1. **Lipid synthesis:** Phosphatidylcholine and DPPC synthesised in the ER via the Kennedy pathway; phospholipid transfer to lamellar bodies via ABCA3
2. **Protein synthesis:** SP-B and SP-C synthesised as proproteins in the ER; processed to mature forms in multivesicular bodies
3. **Lamellar body secretion:** Triggered by elevated [Ca²⁺]i, stretch, or β-agonists; lamellar body membranes fuse with the apical membrane (regulated exocytosis) → tubular myelin forms in the alveolar hypophase
4. **Recycling:** ~75% of secreted surfactant is recaptured by AT2 cells and recycled (the "alveolar surfactant pool" is maintained without continuous de novo synthesis for every molecule)

### Alveolar Epithelial Repair

AT2 cells serve as **self-renewing progenitors** for the alveolar epithelium:
- Under homeostatic conditions, AT2 cells slowly self-renew (~turnover ~80–120 days)
- After AT1 cell injury (viral pneumonitis, toxic exposure, mechanical injury), AT2 cells proliferate and differentiate into AT1 cells to restore the gas-exchange surface [^desai-2014-at2-stem-cell]
- This repair capacity is the basis for recovery from ARDS when the causative injury is resolved

### Ion and Fluid Transport

AT2 cells actively transport Na⁺ from the alveolar space into the interstitium via:
- Apical: ENaC (epithelial Na⁺ channel) + CFTR (Cl⁻ channel)
- Basolateral: Na⁺/K⁺-ATPase

This active Na⁺ transport is the primary mechanism clearing alveolar oedema fluid. Failure of this transport (as in early ARDS) impairs alveolar fluid clearance and worsens gas exchange.

## Lifecycle

AT2 cells originate from NKX2.1-expressing endodermal progenitors during lung development (weeks 4–6 in the human embryo) and persist throughout adult life. Unlike cardiomyocytes, AT2 cells retain regenerative capacity. In homeostasis, the AT2 pool is maintained by slow self-renewal; in injury, a subset of AT2 cells (marked by HopX, TRP63, or Krt5 in transitional states) rapidly expands and differentiates. Dysregulation of this repair process contributes to the fibrotic remodelling of idiopathic pulmonary fibrosis (IPF), where hyperplastic AT2 cells fail to properly differentiate into AT1 cells [^fehrenbach-2001-at2-review].

## Connections

- **Part-of** → [Alveolus](../../05-tissue/alveolus/README.md): AT2 cells are a key constituent of the alveolar epithelium, concentrated in the alveolar corners where they produce surfactant and serve as progenitors.
- **Part-of** → [Lung](../../06-organ/lung/README.md): AT2 cells populate the alveolar surfaces throughout both lungs; their function is essential to normal lung mechanics and gas exchange at the organ scale.
- **Infected-by** → [Influenza A virus](../../../02-pathogen/01-viruses/influenza-a/README.md): AT2 cells express α-2,3 sialic acid receptors (preferred by avian H5N1 strains) and α-2,6 sialic acid receptors; influenza A infects and destroys AT2 cells, causing diffuse alveolar damage.

## Pathology

| Disease | AT2 mechanism |
|:---|:---|
| **ARDS (acute respiratory distress syndrome)** | Diffuse alveolar damage — extensive AT1 and AT2 cell death → alveolar flooding, loss of surfactant → reduced compliance, hypoxaemic respiratory failure |
| **Neonatal respiratory distress syndrome (RDS)** | Surfactant deficiency due to developmental immaturity of AT2 cells (<32 weeks GA); treated with exogenous surfactant and antenatal corticosteroids (accelerate AT2 maturation) |
| **Idiopathic pulmonary fibrosis (IPF)** | Repeated subclinical AT2 injury → aberrant repair → fibroblast activation → progressive fibrosis; SFTPC mutations cause familial IPF |
| **Influenza A / SARS-CoV-2** | Primary infection and destruction of AT2 cells → loss of surfactant production + loss of repair capacity → ARDS |
| **Lung cancer (adenocarcinoma)** | Malignant transformation of AT2 cell lineage is a major pathway to pulmonary adenocarcinoma (KRAS, EGFR mutations in NKX2.1+ AT2-like progenitors) |

## See Also

- [Alveolus](../../05-tissue/alveolus/README.md) — the tissue unit containing AT2 cells.
- [Lung](../../06-organ/lung/README.md) — the organ.
- [Influenza A virus](../../../02-pathogen/01-viruses/influenza-a/README.md) — pathogen targeting AT2 cells.

[^fehrenbach-2001-at2-review]: Fehrenbach H. Alveolar epithelial type II cell: defender of the alveolus revisited. *Respir Res.* 2001;2(1):33-46. [doi:10.1186/rr36](https://doi.org/10.1186/rr36) · [PubMed 11686863](https://pubmed.ncbi.nlm.nih.gov/11686863/)
[^whitsett-2002-surfactant-biology]: Whitsett JA, Wert SE, Trapnell BC. Genetic disorders influencing lung formation and function at birth. *Hum Mol Genet.* 2004;13 Spec No 2:R207-15. [doi:10.1093/hmg/ddh252](https://doi.org/10.1093/hmg/ddh252) · [PubMed 15358728](https://pubmed.ncbi.nlm.nih.gov/15358728/)
[^mason-2006-at2-biology]: Mason RJ. Biology of alveolar type II cells. *Respirology.* 2006;11(Suppl):S12-5. [doi:10.1111/j.1440-1843.2006.00800.x](https://doi.org/10.1111/j.1440-1843.2006.00800.x) · [PubMed 16423262](https://pubmed.ncbi.nlm.nih.gov/16423262/)
[^desai-2014-at2-stem-cell]: Desai TJ, Brownfield DG, Krasnow MA. Alveolar progenitor and stem cells in lung development, renewal, and cancer. *Nature.* 2014;507(7491):190-4. [doi:10.1038/nature12930](https://doi.org/10.1038/nature12930) · [PubMed 24499815](https://pubmed.ncbi.nlm.nih.gov/24499815/)
