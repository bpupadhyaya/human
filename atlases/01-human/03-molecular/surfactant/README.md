---
schema: human-scale-entry/v1
id: surfactant
name: Pulmonary Surfactant
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Phospholipid-protein mixture (~90% lipid, ~10% protein) secreted by type II pneumocytes. DPPC reduces alveolar surface tension per Laplace law, preventing collapse. SP-A/D mediate innate immunity; SP-B/C enable spreading. Deficiency causes NRDS."
aliases: ["surfactant", "pulmonary surfactant", "DPPC", "SP-A", "SP-B"]
sources:
  - id: avery-1959-surfactant
    type: peer-reviewed
    cite: "Avery ME, Mead J. Surface properties in relation to atelectasis and hyaline membrane disease. AMA J Dis Child. 1959;97(5):517-523."
    doi: "10.1001/archpedi.1959.02070010519001"
    pmid: "13649082"
    url: "https://doi.org/10.1001/archpedi.1959.02070010519001"
  - id: clements-1957-surfactant
    type: peer-reviewed
    cite: "Clements JA. Surface tension of lung extracts. Proc Soc Exp Biol Med. 1957;95(1):170-172."
    doi: "10.3181/00379727-95-23156"
    pmid: "13432809"
    url: "https://doi.org/10.3181/00379727-95-23156"
cross_links:
  - target: 01-human/04-cellular/type-ii-pneumocyte
    relation: expressed-by
    note: "Pulmonary surfactant is synthesized and secreted by type II alveolar epithelial cells (pneumocytes) via lamellar bodies; recycling occurs by re-uptake into type II cells."
  - target: 01-human/06-organ/lung
    relation: modulates
    note: "Surfactant lines the air-liquid interface of the entire lung alveolar surface (~70 m²), reducing surface tension and maintaining alveolar patency during the breathing cycle."
  - target: 01-human/05-tissue/alveolus
    relation: modulates
    note: "Within alveoli, surfactant forms a monolayer at the air-liquid interface; its concentration-dependent surface tension reduction prevents alveolar collapse at end-expiration (Laplace law: P=2γ/r)."
  - target: 01-human/06-organ/ards
    relation: connects-to
    note: "SP-B, SP-C, and DPPC are degraded by phospholipases A₂ released during ARDS; BAL surfactant protein content falls 80–90% and surface tension rises → atelectrauma; exogenous beractant/poractant alfa restore alveolar mechanics but mortality benefit in adult ARDS remains uncertain."
  - target: 02-pathogen/01-viruses/sars-cov-2
    relation: connects-to
    note: "SARS-CoV-2 targets type II pneumocytes (ACE2-high) → lytic infection depletes surfactant pool; SP-D binds SARS-CoV-2 spike N-terminal domain, mediating virus aggregation; surfactant dysfunction is an early driver of hypoxaemic respiratory failure in severe COVID-19."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "SFTPC mutations (e.g., L188Q, Δexon4) cause SP-C misfolding → ER stress in type II cells → IPF; TGF-β1 suppresses SFTPB/SFTPC transcription; DPPC-containing surfactant therapy is explored to slow early fibrotic remodelling in SFTPC-mutation IPF."
  - target: 01-human/03-molecular/influenza-ha
    relation: connects-to
    note: "SP-D binds influenza HA mannose-rich N-glycans via calcium-dependent CRD → viral aggregation and opsonization; SP-D-deficient mice develop worse influenza pneumonitis; Asp11Asn SP-D polymorphism reduces HA binding; SP-D is a critical innate defense against influenza A."
---

# Pulmonary Surfactant

## Overview

Pulmonary surfactant is the **complex lipoprotein mixture** lining the alveolar air-liquid interface, essential for breathing mechanics and innate pulmonary defense. Its discovery as the cause of neonatal respiratory distress syndrome (NRDS) by Avery and Mead in 1959 [^avery-1959-surfactant] and the pioneering surface tension measurements by Clements [^clements-1957-surfactant] represent landmarks in pulmonary biology. The clinical consequence — surfactant replacement therapy for premature infants — has saved hundreds of thousands of lives annually.

Surfactant composition is approximately **90% lipid and 10% protein** by dry weight. The dominant phospholipid, **dipalmitoylphosphatidylcholine (DPPC, ~45%)**, is responsible for the unique ability to compress to very low surface tensions (approaching 0 mN/m) during exhalation and rapidly re-spread during inspiration. Without surfactant, each breath would require enormous respiratory effort, and alveoli would progressively collapse.

## Structure

### Lipid Composition

| Component | Fraction (~) | Role |
|:---|:---|:---|
| **DPPC** | 45% | Primary surface-tension-reducing lipid; compresses to near-zero γ at end-expiration |
| Unsaturated phosphatidylcholines | 25% | Aid DPPC spreading and film fluidity |
| Phosphatidylglycerol (PG) | 10% | Enhances monolayer spreading; reduced in infection/ARDS |
| Cholesterol | 8% | Modulates lipid packing and fluidity |
| Other phospholipids | ~12% | Sphingomyelin, PI, PE |

### Surfactant Proteins

Four surfactant proteins are encoded by dedicated genes and serve distinct functions:

| Protein | Type | Gene | Key function |
|:---|:---|:---|:---|
| **SP-A** | Hydrophilic collectin (sialic-acid-rich) | *SFTPA1/2* | Pattern recognition (PAMPs), opsonization, regulation of tubular myelin, feedback regulation of surfactant secretion |
| **SP-B** | Small hydrophobic (~8 kDa) | *SFTPB* | Essential for lamellar body formation, DPPC insertion into monolayer, rapid film adsorption; SP-B knockout is lethal |
| **SP-C** | Very small hydrophobic (~4 kDa, poly-Val TM helix) | *SFTPC* | Facilitates lipid film spreading and monolayer stability; mutations cause familial interstitial lung disease |
| **SP-D** | Hydrophilic collectin (trimeric, dodecameric) | *SFTPD* | Pattern recognition of viral/bacterial PAMPs, agglutination of pathogens, regulation of alveolar macrophage function |

## Function

### Surface Tension Reduction

The fundamental mechanical role of surfactant follows the **Laplace law**: P = 2γ/r (where P = pressure to keep sphere open, γ = surface tension, r = radius). Without surfactant, smaller alveoli (lower r) would require greater distending pressure — resulting in smaller alveoli emptying into larger ones and progressive atelectasis. Surfactant reduces γ from ~70 mN/m (pure water) to <5 mN/m during exhalation, eliminating the radius-dependent pressure differential and allowing stable ventilation across the alveolar size distribution.

Key functional properties of the surfactant film:
- **Dynamic surface tension:** DPPC compresses during exhalation to very low γ; unsaturated lipids and proteins enable rapid re-spreading during inhalation
- **Film adsorption:** SP-B and SP-C accelerate insertion of phospholipids from the hypophase (aqueous sub-layer) into the air-liquid interface
- **Stability at low lung volumes:** Maintains alveolar patency at functional residual capacity (FRC), reducing the work of breathing by ~10-fold compared to surfactant-free lungs

### Innate Immune Functions

SP-A and SP-D are **collectin-class pattern recognition molecules** of the innate immune system:
- Bind carbohydrate PAMPs on bacteria, viruses (influenza, RSV), and fungi via calcium-dependent lectin domains (CRDs)
- Enhance alveolar macrophage phagocytosis through opsonization
- SP-A directly neutralizes LPS; SP-D agglutinates and opsonizes influenza A via hemagglutinin binding
- Regulate alveolar macrophage oxidative burst and cytokine release (tonically suppress excessive inflammation)

## Mechanism

### Synthesis and Secretion

The surfactant biogenesis pathway in type II pneumocytes involves sequential compartments:

1. **Endoplasmic reticulum** → lipid synthesis (phospholipids via CDP-choline pathway), SP-B/SP-C proprotein processing
2. **Golgi apparatus** → glycosylation of SP-A/SP-D; proprotein sorting
3. **Lamellar bodies** (specialized lysosome-related organelles) → condensed storage of lipid-protein complexes; SP-B is essential for lamellar body biogenesis
4. **Exocytosis** → regulated secretion into alveolar hypophase; triggered by mechanical stretch, beta-adrenergic signaling, ATP (purinergic receptors), and SP-A feedback
5. **Tubular myelin** (extracellular lattice) → intermediate form; SP-A + SP-B form lattice structure from which lipid film is generated
6. **Monolayer formation** → DPPC film at air-liquid interface
7. **Recycling** → ~90% of secreted lipids are re-taken up by type II cells via clathrin-coated pits; remainder is degraded by alveolar macrophages

### Regulation of Secretion

Surfactant secretion is upregulated by:
- **Mechanical stretch** (tidal breathing, sighing) — major physiological driver
- **Beta-2 adrenergic agonists** — accelerate secretion (clinical use: betamethasone in preterm labor to accelerate fetal lung maturation via glucocorticoid induction of SP-B/SP-C gene expression)
- **Purinergic signaling** (ATP, adenosine) — via P2Y receptors on type II cells

## Connections

- `expressed-by` → **[Type II Pneumocyte](../../04-cellular/type-ii-pneumocyte/README.md)** — sole cellular source of pulmonary surfactant
- `acts-on` → **[Lung](../../06-organ/lung/README.md)** — reduces surface tension across ~70 m² alveolar surface
- `acts-on` → **[Alveolus](../../05-tissue/alveolus/README.md)** — directly maintains alveolar stability at the air-liquid interface
- `connects-to` → **[ARDS](../../06-organ/ards/README.md)** — SP-B/SP-C degraded by ARDS phospholipases; surfactant replacement (beractant, poractant alfa) is standard of care for NRDS and studied in adult ARDS
- `connects-to` → **[SARS-CoV-2](../../../../02-pathogen/01-viruses/sars-cov-2/README.md)** — SARS-CoV-2 depletes type II pneumocyte surfactant pool; SP-D binds viral spike N-terminal domain, contributing to innate antiviral defense
- `connects-to` → **[Fibrosis](../fibrosis/README.md)** — SFTPC mutations cause SP-C misfolding and IPF; TGF-β1 suppresses surfactant protein gene transcription in alveolar epithelial injury
- `connects-to` → **[Influenza Hemagglutinin](../influenza-ha/README.md)** — SP-D binds influenza HA mannose-rich N-glycans via calcium-dependent CRD → viral aggregation and opsonization; SP-D-deficient mice have worse influenza outcomes; Asp11Asn polymorphism reduces HA-binding affinity.

[^avery-1959-surfactant]: Avery ME, Mead J. Surface properties in relation to atelectasis and hyaline membrane disease. *AMA J Dis Child.* 1959;97(5):517-523. [doi:10.1001/archpedi.1959.02070010519001](https://doi.org/10.1001/archpedi.1959.02070010519001) · [PubMed 13649082](https://pubmed.ncbi.nlm.nih.gov/13649082/)
[^clements-1957-surfactant]: Clements JA. Surface tension of lung extracts. *Proc Soc Exp Biol Med.* 1957;95(1):170-172. [doi:10.3181/00379727-95-23156](https://doi.org/10.3181/00379727-95-23156) · [PubMed 13432809](https://pubmed.ncbi.nlm.nih.gov/13432809/)

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
