---
schema: human-scale-entry/v1
id: lung-slice
name: Lung Slice
atlas: 01-human
scale: 05-tissue
status: draft
last_reviewed: 2026-06-06
summary: "Precision-cut lung slices (PCLS): 200–300 μm ex vivo tissue sections retaining intact alveolar and airway architecture. Research models for airway pharmacology, viral infection (SARS-CoV-2, RSV), and pulmonary drug toxicology without live animal experiments."
aliases: ["PCLS", "precision-cut lung slices", "lung tissue slices", "ex vivo lung model"]
sources:
  - id: placke-1987-pcls
    type: peer-reviewed
    cite: "Placke ME, Fisher GL. Adult peripheral lung organ culture — a model for respiratory tract toxicology. Toxicol Appl Pharmacol. 1987;90(2):284-298."
    doi: "10.1016/0041-008X(87)90338-7"
    pmid: "3616891"
    url: "https://doi.org/10.1016/0041-008X(87)90338-7"
  - id: bergner-2002-airway-pcls
    type: peer-reviewed
    cite: "Bergner A, Sanderson MJ. Airway contractility and smooth muscle Ca2+ signaling in lung slices from different mouse strains. J Appl Physiol. 2002;93(4):1300-1309."
    doi: "10.1152/japplphysiol.00349.2002"
    pmid: "12235026"
    url: "https://doi.org/10.1152/japplphysiol.00349.2002"
  - id: neuhaus-2017-pcls-human
    type: peer-reviewed
    cite: "Neuhaus V, Schaudien D, Golovina T, et al. Assessment of long-term cultivated human precision-cut lung slices as a model system for research in respiratory medicine. J Occup Med Toxicol. 2017;12:13."
    doi: "10.1186/s12995-017-0158-5"
    pmid: "28473872"
    url: "https://doi.org/10.1186/s12995-017-0158-5"
cross_links:
  - target: 01-human/06-organ/lung
    relation: part-of
    note: "PCLS are thin sections of the intact lung organ, prepared by agarose inflation and vibratome cutting; they retain the three-dimensional architecture of alveoli, airways, and vascular structures present in whole lung tissue."
  - target: 01-human/05-tissue/alveolus
    relation: contains
    note: "Precision-cut lung slices contain multiple alveolar units with intact alveolar epithelium (type I and II pneumocytes), alveolar macrophages, and capillary endothelium — the same structures found in the alveolus — enabling direct observation of alveolar responses to stimuli."
  - target: 01-human/04-cellular/type-ii-pneumocyte
    relation: contains
    note: "PCLS retain functional type II pneumocytes (surfactant production, alveolar repair) and their interactions with alveolar macrophages; type II pneumocyte responses to SARS-CoV-2, toxicants, and growth factors can be studied in situ without cell isolation artifacts."
---

# Lung Slice

## Overview

**Precision-cut lung slices (PCLS)** are thin (200–300 μm) ex vivo tissue sections prepared from animal or human lung tissue using an agarose inflation–vibratome cutting technique. They represent the closest approximation to the intact lung microenvironment that can be maintained in culture: retaining the three-dimensional architecture of alveoli, small airways, pulmonary vasculature, and resident immune cells (alveolar macrophages, dendritic cells, interstitial macrophages) in a physiologically relevant tissue context.

Originally developed by Placke and Fisher in 1987 for pulmonary toxicology [^placke-1987-pcls], PCLS have evolved into a versatile platform for:
- **Airway pharmacology:** Bronchoconstriction/bronchodilation responses, smooth muscle Ca²⁺ signaling, mucin secretion
- **Respiratory virology:** Viral infection studies (influenza, RSV, SARS-CoV-2, rhinovirus) with intact epithelial cell diversity and mucociliary function
- **Toxicology and drug screening:** Assessment of pulmonary drug toxicity, inhaled particle effects, and nanomaterial clearance
- **Fibrosis and inflammation models:** TGF-β-induced fibrotic responses, cytokine release, immune cell function

Human PCLS prepared from donor or surgical resection lung tissue increasingly bridge the gap between rodent models and clinical relevance, addressing the species-specific differences in airway anatomy, receptor expression, and immune responses that confound murine pulmonary research.

## Structure

### Preparation technique

**Standard PCLS preparation:**
1. **Agarose inflation:** Freshly explanted lung tissue is inflated via the bronchus with warm (37°C) low-melting-point agarose (1.5–2% in DMEM/Hanks buffer) → agarose polymerizes at room temperature → provides uniform mechanical support
2. **Vibratome cutting:** The agarose-filled tissue block is sectioned perpendicular to the airways using a vibratome (oscillating blade) at 200–300 μm thickness; slice thickness is optimized to maintain viability while preserving airway structure
3. **Agarose removal:** Slices are washed at 37°C to melt and elute the agarose; repeated DMEM washes remove debris
4. **Cultivation:** PCLS are maintained in DMEM + penicillin/streptomycin at 37°C/5% CO₂; rodent PCLS remain viable for 24–72 hours; human PCLS can be maintained for 4–6 weeks with appropriate medium (e.g., SAGM supplemented medium) [^neuhaus-2017-pcls-human]

### Structural features preserved

PCLS retain key lung microarchitecture across rodent and human preparations:
- **Alveolar units:** Intact alveolar walls (alveolar epithelium, capillary endothelium, basement membrane); alveolar macrophages in airspace
- **Small airways:** Intact bronchiolar epithelium (ciliated cells, club cells, goblet cells) with functional mucociliary clearance observable in real time
- **Smooth muscle:** Bronchiolar smooth muscle and pulmonary vascular smooth muscle retain contractile function
- **Vasculature:** Small pulmonary arterioles and venules with endothelium and perivascular cells
- **Resident immunity:** Alveolar macrophages, interstitial macrophages, dendritic cells, mast cells — not lost during preparation (unlike BAL or cell isolation)

### Species and source differences

| Feature | Rodent (mouse/rat) | Human PCLS |
|:---|:---|:---|
| Airway branching | Monopodial (one main bronchus) | Dichotomous |
| Airway cells | Club cells dominant; few goblet cells | Goblet cells abundant; MUC5B/MUC5AC |
| ACE2 expression | Lower; mouse ACE2 doesn't bind WT SARS-CoV-2 spike | High; primary target for SARS-CoV-2 |
| Viability duration | 48–72 h standard | 2–6 weeks with optimization |
| Availability | Unlimited; terminal procedure | Donor/resection; limited supply |

## Function

**Airway pharmacology [^bergner-2002-airway-pcls]:** PCLS enable real-time imaging of airway lumen diameter changes: methacholine (muscarinic agonist) produces bronchoconstriction; β₂-agonists (salbutamol) reverse this. Ca²⁺ imaging with Fura-2 in PCLS reveals the coordination of airway smooth muscle Ca²⁺ oscillations driving rhythmic bronchoconstriction. PCLS are used for evaluation of novel bronchodilators and mast cell mediator effects without confounds from blood-derived cells.

**Respiratory viral infection modeling:** SARS-CoV-2 infection of human PCLS recapitulates key features of COVID-19 pneumonitis: ACE2-dependent viral entry, type II pneumocyte tropism, interferon response (delayed), and cytokine release (IL-6, CXCL10). RSV and influenza infection of rodent PCLS have established roles in antiviral drug screening. PCLS support direct comparison of viral pathogenesis across cell types within intact tissue context.

**Pulmonary fibrosis:** TGF-β₁ stimulation of PCLS drives myofibroblast activation, collagen deposition, and airway remodeling over days to weeks — providing an ex vivo fibrosis model relevant to IPF and COVID-19-associated lung fibrosis.

**Drug toxicology:** Inhaled drugs, nanoparticles, and environmental toxicants can be applied to PCLS surfaces or perfused through airways to assess cellular toxicity, surfactant disruption, inflammatory cytokine release, and mucociliary function — replacing some animal inhalation studies.

**Limitations:**
- Loss of perfusion: vascular flow-dependent physiology (shear stress, hypoxic vasoconstriction) is absent
- Loss of systemic immunity: circulating immune cells, humoral factors absent
- Limited ventilatory mechanics: respiratory cycle mechanics cannot be recapitulated
- For human PCLS: donor variability (age, smoking history, disease), limited availability, ethical considerations

## Connections

- `part-of` → **[Lung](../../06-organ/lung/README.md)** — PCLS are thin sections of whole lung tissue, preserving the 3D microarchitecture of the lung parenchyma and airways in an ex vivo format.
- `contains` → **[Alveolus](../alveolus/README.md)** — PCLS contain multiple intact alveolar units with functioning type I and type II pneumocytes, alveolar macrophages, and capillary endothelium — making them a rich model for alveolar biology.
- `contains` → **[Type II Pneumocyte](../../04-cellular/type-ii-pneumocyte/README.md)** — type II pneumocytes are the primary SARS-CoV-2 infection target in PCLS and the main source of surfactant and alveolar repair responses observed in lung slice experiments.

[^placke-1987-pcls]: Placke ME, Fisher GL. Adult peripheral lung organ culture — a model for respiratory tract toxicology. *Toxicol Appl Pharmacol.* 1987;90(2):284-298. [doi:10.1016/0041-008X(87)90338-7](https://doi.org/10.1016/0041-008X(87)90338-7) · [PubMed 3616891](https://pubmed.ncbi.nlm.nih.gov/3616891/)
[^bergner-2002-airway-pcls]: Bergner A, Sanderson MJ. Airway contractility and smooth muscle Ca2+ signaling in lung slices from different mouse strains. *J Appl Physiol.* 2002;93(4):1300-1309. [doi:10.1152/japplphysiol.00349.2002](https://doi.org/10.1152/japplphysiol.00349.2002) · [PubMed 12235026](https://pubmed.ncbi.nlm.nih.gov/12235026/)
[^neuhaus-2017-pcls-human]: Neuhaus V, Schaudien D, Golovina T, et al. Assessment of long-term cultivated human precision-cut lung slices as a model system for research in respiratory medicine. *J Occup Med Toxicol.* 2017;12:13. [doi:10.1186/s12995-017-0158-5](https://doi.org/10.1186/s12995-017-0158-5) · [PubMed 28473872](https://pubmed.ncbi.nlm.nih.gov/28473872/)
