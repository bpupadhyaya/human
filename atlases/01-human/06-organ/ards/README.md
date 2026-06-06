---
schema: human-scale-entry/v1
id: ards
name: Acute Respiratory Distress Syndrome
atlas: 01-human
scale: 06-organ
status: draft
last_reviewed: 2026-06-06
summary: "Diffuse alveolar damage causing hypoxemic respiratory failure (PaO2/FiO2 <300, bilateral infiltrates, non-cardiac). Berlin grades: mild/moderate/severe. Exudative phase: neutrophil-mediated injury, protein-rich edema. Treatment: lung-protective ventilation, prone, dexamethasone."
aliases: ["ARDS", "acute respiratory distress syndrome", "diffuse alveolar damage", "DAD", "adult RDS"]
sources:
  - id: ardsnet-2000-arma
    type: peer-reviewed
    cite: "The Acute Respiratory Distress Syndrome Network. Ventilation with lower tidal volumes as compared with traditional tidal volumes for acute lung injury and the acute respiratory distress syndrome. N Engl J Med. 2000;342(18):1301-1308."
    doi: "10.1056/NEJM200005043421801"
    pmid: "10793162"
    url: "https://doi.org/10.1056/NEJM200005043421801"
  - id: ranieri-2012-berlin-ards
    type: peer-reviewed
    cite: "Ranieri VM, Rubenfeld GD, Thompson BT, et al. Acute respiratory distress syndrome: the Berlin Definition. JAMA. 2012;307(23):2526-2533."
    doi: "10.1001/jama.2012.5669"
    pmid: "22797452"
    url: "https://doi.org/10.1001/jama.2012.5669"
cross_links:
  - target: 01-human/06-organ/lung
    relation: part-of
    note: "ARDS is the most severe form of acute lung injury, affecting the entire lung parenchyma bilaterally; it represents the lung's final common pathway response to diverse systemic and pulmonary insults."
  - target: 01-human/04-cellular/macrophage
    relation: modulated-by
    note: "Alveolar macrophages are central orchestrators of ARDS: early release of TNF-α, IL-6, IL-8, and IL-1β amplifies neutrophil recruitment and epithelial/endothelial injury; macrophage phenotype shift (M1→M2) is required for resolution."
  - target: 01-human/03-molecular/tgf-beta
    relation: modulated-by
    note: "TGF-β1 is markedly elevated in ARDS bronchoalveolar lavage; it impairs alveolar fluid clearance (inhibits ENaC expression), promotes fibroproliferation, and drives the proliferative/fibrotic phase of ARDS."
  - target: 01-human/04-cellular/type-ii-pneumocyte
    relation: contains
    note: "Type II pneumocyte hyperplasia in the proliferative phase of ARDS represents attempted alveolar re-epithelialization; type II cells produce surfactant and can differentiate into type I cells to restore the gas-exchange surface."
---

# Acute Respiratory Distress Syndrome

## Overview

Acute Respiratory Distress Syndrome (ARDS) is a **life-threatening inflammatory lung syndrome** characterized by diffuse alveolar damage, protein-rich pulmonary edema, and severe hypoxemic respiratory failure. It represents the lung's catastrophic response to a variety of direct and indirect insults — trauma, sepsis, pneumonia, aspiration, pancreatitis — and carries a global mortality of ~35–45% in moderate-severe disease [^ranieri-2012-berlin-ards].

ARDS is defined clinically by the **Berlin 2012 criteria** [^ranieri-2012-berlin-ards]:
1. **Acute onset** within 1 week of a known insult or new/worsening respiratory symptoms
2. **Bilateral opacities** on chest imaging (CXR or CT), not fully explained by effusions, atelectasis, or nodules
3. **Respiratory failure not fully explained by cardiac failure** or fluid overload (objective assessment, e.g., echocardiography, if no risk factor present)
4. **PaO₂/FiO₂ ratio** (P/F ratio) on PEEP ≥5 cmH₂O:
   - **Mild ARDS**: PaO₂/FiO₂ >200 and ≤300 mmHg
   - **Moderate ARDS**: PaO₂/FiO₂ >100 and ≤200 mmHg
   - **Severe ARDS**: PaO₂/FiO₂ ≤100 mmHg

Global incidence is ~3–10 million cases/year; in the ICU setting, ARDS accounts for ~10% of all admissions and ~23% of mechanically ventilated patients.

## Structure

### Histopathology: Diffuse Alveolar Damage (DAD)

The pathological substrate of ARDS is **diffuse alveolar damage (DAD)**, which evolves in distinct phases:

**Exudative phase (Days 1–7):**
- Alveolar capillary endothelial injury → increased permeability → protein-rich edema floods alveolar spaces
- Type I alveolar epithelial cell necrosis (type I cells cover ~95% of alveolar surface)
- **Hyaline membrane formation** — condensed plasma proteins (fibrin, fibronectin, albumin) line denuded alveolar walls; pathognomonic on histology
- Neutrophilic alveolitis — massive neutrophil recruitment into alveolar space; neutrophil-derived proteases (elastase, MMP-8), ROS, and NETs amplify injury
- Surfactant dysfunction — dilution and protein inhibition of surfactant → increased surface tension → microatelectasis

**Proliferative phase (Days 7–21):**
- Type II pneumocyte hyperplasia — attempt at re-epithelialization; type II cells are progenitors that can differentiate into type I cells
- Myofibroblast activation (TGF-β1-driven) → fibroproliferation
- Organizing exudate in alveolar spaces
- Some patients progress to fibrosis; others resolve

**Fibrotic phase (Weeks 3+, minority of patients):**
- Dense fibrosis replaces alveolar architecture
- Honeycombing, traction bronchiectasis on CT
- Severely impaired gas exchange; reduced compliance

### Radiographic Appearance

- **CXR**: Bilateral opacities ("whiteout"), not in a cardiomegaly/vascular pattern; air bronchograms common
- **CT chest**: Dependent consolidation (gravity-dependent zones collapse due to edema weight); dorsal consolidation, anterior ground-glass; "sponge lung" model

## Function

### Pathophysiology: From Injury to Hypoxemia

ARDS hypoxemia results from two principal mechanisms:

1. **Intrapulmonary shunting** — alveoli filled with edema/exudate are perfused but not ventilated → venous blood passes to arterial circulation without O₂ loading; shunt fraction can reach 50–70% in severe ARDS (vs. <5% normal). Supplemental oxygen has limited effect on shunt hypoxemia — distinguishing ARDS from other causes of hypoxemia.

2. **Ventilation-perfusion (V/Q) mismatch** — uneven distribution of edema creates regions of low V/Q where blood is partially oxygenated; complements shunting.

**Reduced lung compliance** — edema, atelectasis, and surfactant loss make lungs stiff (compliance <30 mL/cmH₂O vs. normal ~200 mL/cmH₂O); pressure required to ventilate increases dramatically, causing ventilator-induced lung injury (VILI) at traditional tidal volumes.

### Cellular Mediators of Injury

| Mediator | Source | Mechanism of injury |
|:---|:---|:---|
| **Neutrophil elastase** | Activated neutrophils | Degrades alveolar basement membrane, surfactant proteins, and endothelial junctions |
| **CXCL8 (IL-8)** | Macrophages, epithelial cells | Primary neutrophil chemokine; drives massive alveolar neutrophilia |
| **TNF-α, IL-1β** | Alveolar macrophages | Upregulate endothelial ICAM-1/E-selectin; increase permeability; activate neutrophils |
| **ROS / reactive nitrogen species** | Neutrophils, xanthine oxidase | Lipid peroxidation of membranes; protein carbonylation; surfactant oxidation |
| **Platelet-activating factor (PAF)** | Endothelial cells, macrophages | Potent neutrophil activator; increases vascular permeability |
| **TGF-β1** | Macrophages, platelets | Impairs Na/K-ATPase (alveolar fluid clearance); drives fibroproliferation |

## Connections

- `part-of` → **[Lung](../../06-organ/lung/README.md)** — ARDS is the most severe manifestation of acute lung injury, affecting bilateral lung parenchyma
- `modulated-by` → **[Macrophage](../../04-cellular/macrophage/README.md)** — central orchestrators of ARDS inflammation: early IL-8/TNF-α release driving neutrophil recruitment; later M2 transition for resolution
- `modulated-by` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — elevated in ARDS BAL; impairs alveolar fluid clearance; drives fibroproliferative phase
- `contains` → **[Type II Pneumocyte](../../04-cellular/type-ii-pneumocyte/README.md)** — type II cell hyperplasia in proliferative phase represents attempted re-epithelialization of denuded alveolar surface

## Pathology

### ARMA Trial: Lung-Protective Ventilation

The landmark ARDSNet ARMA trial (2000) [^ardsnet-2000-arma] established **6 mL/kg predicted body weight (PBW)** tidal volume as standard of care, demonstrating a 22% reduction in 28-day mortality compared to traditional 12 mL/kg ventilation. The mechanism: avoiding alveolar overdistension (volutrauma) and cyclical opening-closing (atelectrauma), both of which release injurious cytokines (biotrauma) into the systemic circulation.

**Lung-protective ventilation protocol:**
- Tidal volume: 4–8 mL/kg PBW (target 6 mL/kg)
- Plateau pressure (Pplat): ≤30 cmH₂O
- Driving pressure (Pplat − PEEP): target ≤15 cmH₂O
- PEEP: set per ARDS Network PEEP/FiO₂ table to maintain oxygenation and prevent derecruitment
- SpO₂ target: 88–95% / PaO₂ 55–80 mmHg (permissive hypoxemia acceptable to limit FiO₂ toxicity)

### Prone Positioning

PROSEVA trial (2013): **16 hours/day prone positioning** in severe ARDS (P/F <150) → 28-day mortality 16% vs. 32.8% (supine). Mechanism: redistribution of ventilation to dorsal lung (reduces V/Q mismatch), reduced compression atelectasis, improved secretion drainage, and reduced VILI.

### Pharmacological Management

| Intervention | Evidence | Mechanism |
|:---|:---|:---|
| **Dexamethasone** | RECOVERY trial (COVID-ARDS); DEXA-ARDS | Suppresses inflammatory/fibroproliferative phases; reduces ventilator days |
| **Neuromuscular blockade** | ACURASYS (2010): reduced mortality in severe ARDS; ROSE (2019): no benefit — now controversial | Abolishes patient-ventilator dyssynchrony and spontaneous breathing effort (P-SILI) |
| **Inhaled nitric oxide (iNO)** | Improves oxygenation; no mortality benefit | Selectively vasodilates ventilated regions → improved V/Q matching |
| **Surfactant replacement** | Effective in neonatal RDS; NOT effective in adult ARDS | Surfactant delivery to injured adult lung is technically and mechanically challenging |
| **ECMO** | EOLIA trial: no survival benefit as early rescue; used as salvage in severe refractory ARDS | Extracorporeal gas exchange allowing complete lung rest |

[^ardsnet-2000-arma]: The Acute Respiratory Distress Syndrome Network. Ventilation with lower tidal volumes as compared with traditional tidal volumes for ALI and ARDS. *N Engl J Med.* 2000;342(18):1301-1308. [doi:10.1056/NEJM200005043421801](https://doi.org/10.1056/NEJM200005043421801) · [PubMed 10793162](https://pubmed.ncbi.nlm.nih.gov/10793162/)
[^ranieri-2012-berlin-ards]: Ranieri VM et al. Acute respiratory distress syndrome: the Berlin Definition. *JAMA.* 2012;307(23):2526-2533. [doi:10.1001/jama.2012.5669](https://doi.org/10.1001/jama.2012.5669) · [PubMed 22797452](https://pubmed.ncbi.nlm.nih.gov/22797452/)
