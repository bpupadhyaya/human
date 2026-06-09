---
schema: human-scale-entry/v1
id: lung
name: Lung
atlas: 01-human
scale: 06-organ
status: draft
last_reviewed: 2026-06-03
summary: "Paired gas-exchange organs: right (3 lobes) and left (2 lobes). Branching airways (23 generations, Weibel) connect trachea to ~300 million alveoli (70 m² surface). Dual circulation: pulmonary + bronchial. TLC ~6 L; tidal volume ~0.5 L at rest."
aliases: ["lungs", "pulmo", "pulmones"]
sources:
  - id: west-respiratory-physiology
    type: textbook
    cite: "West JB, Luks AM. West's Respiratory Physiology: The Essentials. 10th ed. Wolters Kluwer; 2016. ISBN 978-1-4963-1011-1."
    url: "https://www.lww.com/Product/9781496310118"
    accessed: "2026-06-03"
  - id: weibel-1963-morphometry
    type: peer-reviewed
    cite: "Weibel ER. Morphometry of the Human Lung. Academic Press; 1963. [Springer reprint: doi:10.1007/978-3-642-87553-3]"
    doi: "10.1007/978-3-642-87553-3"
    url: "https://doi.org/10.1007/978-3-642-87553-3"
  - id: nhlbi-lung-how-lungs-work
    type: regulatory
    cite: "National Heart, Lung, and Blood Institute (NHLBI). How the Lungs Work. U.S. Department of Health and Human Services."
    url: "https://www.nhlbi.nih.gov/health/lungs"
    accessed: "2026-06-03"
  - id: crapo-1982-alveolar-morphometry
    type: peer-reviewed
    cite: "Crapo JD, Barry BE, Gehr P, Bachofen M, Weibel ER. Cell number and cell characteristics of the normal human lung. Am Rev Respir Dis. 1982;125(6):740-5."
    doi: "10.1164/arrd.1982.125.6.740"
    pmid: "7044530"
    url: "https://doi.org/10.1164/arrd.1982.125.6.740"
cross_links:
  - target: 01-human/05-tissue/alveolus
    relation: contains
    note: "~300 million alveoli constitute the gas-exchange parenchyma of the lung, providing ~70 m² of surface area for O₂–CO₂ exchange."
  - target: 01-human/04-cellular/type-ii-pneumocyte
    relation: contains
    note: "AT2 cells throughout the alveolar surface produce surfactant and repair the alveolar epithelium; they are distributed across both lungs."
  - target: 01-human/07-system/respiratory-system
    relation: part-of
    note: "The lungs are the principal gas-exchange organs of the respiratory system; they house the alveoli and receive ventilation from the conducting airways."
  - target: 02-pathogen/01-viruses/sars-cov-2
    relation: damaged-by
    note: "SARS-CoV-2 causes diffuse alveolar damage and acute respiratory distress syndrome (ARDS); severe COVID-19 pneumonia destroys alveolar epithelium and produces bilateral lung infiltrates."
  - target: 02-pathogen/01-viruses/influenza-a
    relation: damaged-by
    note: "Influenza A virus causes primary viral pneumonitis targeting AT1 and AT2 cells, leading to alveolar damage, haemorrhage, and secondary bacterial pneumonia."
  - target: 02-pathogen/02-bacteria/mycobacterium-tuberculosis
    relation: damaged-by
    note: "Pulmonary tuberculosis causes caseating granulomas, cavitation, and progressive parenchymal destruction within the lung; upper lobe predominance reflects higher O₂ tension."
  - target: 02-pathogen/02-bacteria/streptococcus-pneumoniae
    relation: infected-by
    note: "S. pneumoniae is the most common cause of community-acquired bacterial pneumonia; aspiration of colonized nasopharyngeal secretions seeds alveolar spaces, causing lobar consolidation, fibrinous exudate, and impaired gas exchange."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: damaged-by
    note: "Damaged by Varicella-Zoster Virus."
  - target: 02-pathogen/01-viruses/respiratory-syncytial-virus
    relation: damaged-by
    note: "Damaged by Respiratory Syncytial Virus."
  - target: 02-pathogen/01-viruses/measles-virus
    relation: damaged-by
    note: "Damaged by Measles Virus."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: damaged-by
    note: "Damaged by Pneumocystis jirovecii (formerly carinii)."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "PAH obliterates pulmonary arterioles (<500 µm) via medial hypertrophy, intimal fibrosis, and plexiform lesions → RV pressure overload → cor pulmonale; RHC required for diagnosis; mPAP >20 mmHg + PVR ≥2 WU + PAWP ≤15 mmHg."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Periostin drives fibrotic remodeling in chronic lung disease: TGF-β + IL-13 → POSTN in lung fibroblasts → collagen matrix assembly → subepithelial fibrosis; serum periostin correlates with lung function decline in asthma and IPF; marks remodeling distinct from acute inflammation."
taxonomy:
  uberon: "UBERON:0002048"
  fma: "FMA:7195"
---

# Lung

## Overview

The lungs are the **paired organs of pulmonary gas exchange** — the anatomical interface at which atmospheric oxygen loads into haemoglobin in erythrocytes and CO₂ produced by cellular metabolism unloads into expired air. Situated in the thoracic cavity on either side of the heart, they are enclosed by the pleural membranes and their mechanics are intimately coupled to the chest wall and diaphragm [^west-respiratory-physiology].

The right lung (3 lobes: upper, middle, lower) is larger, comprising approximately **57% of total lung volume**; the left lung (2 lobes: upper, lower) is smaller to accommodate the leftward displacement of the heart. Together they contain:
- **23 generations of branching airways** (Weibel's airway model) from the trachea (generation 0) to the respiratory bronchioles and alveolar sacs
- **~300 million alveoli** providing ~70 m² of gas-exchange surface [^crapo-1982-alveolar-morphometry]
- **~1,500 km of airways** (including bronchioles)

The lung has a **dual blood supply**: the pulmonary circulation (right heart → pulmonary artery → pulmonary capillaries → pulmonary veins → left heart) for gas exchange, and the bronchial circulation (from the aorta) for nutrition of the airway walls.

## Structure

### Airway Generations (Weibel Model)

Weibel's 1963 morphometry [^weibel-1963-morphometry] defined the human lung airway tree:

| Generation | Structure | Number | Diameter (approx.) |
|:---:|:---|:---:|:---:|
| 0 | Trachea | 1 | ~18 mm |
| 1–4 | Main, lobar, segmental bronchi | 2–16 | 12–4 mm |
| 5–14 | Small bronchi / bronchioles | 32–16,384 | 3–1 mm |
| 15–16 | Terminal bronchioles | ~65,536 | ~0.5–0.6 mm |
| 17–19 | Respiratory bronchioles | ~500,000 | ~0.4 mm |
| 20–22 | Alveolar ducts | ~8 million | ~0.4 mm |
| 23 | Alveolar sacs | ~300 million openings | — |

Generations 0–16 are the **conducting zone** (dead space, no gas exchange) — ~150 mL total volume. Generations 17–23 are the **respiratory zone** (gas exchange) — ~2,500–3,000 mL at FRC.

### Alveolar Structure

See the [Alveolus](../../05-tissue/alveolus/README.md) entry for detailed description of AT1/AT2 cell architecture, air-blood barrier dimensions, and surfactant physiology.

### Lobes and Segments

| Lung | Lobes | Segments (bronchopulmonary) |
|:---|:---:|:---:|
| Right | 3 (upper, middle, lower) | 10 |
| Left | 2 (upper [with lingula], lower) | 8–9 |

**Bronchopulmonary segments** are the functional surgical units of the lung, each supplied by its own segmental bronchus and pulmonary artery branch, making them independently resectable.

### Pleura

Each lung is enclosed in two pleural layers (visceral and parietal) with a fluid-filled potential space between (~5–20 mL pleural fluid at normal pressure ~−5 cmH₂O). This negative intrapleural pressure holds the lung "open" — the elasticity of the lung (inward recoil) is balanced by the chest wall (outward recoil) at FRC.

### Vascular Anatomy

| Circuit | Function | Pressure |
|:---|:---|:---:|
| **Pulmonary arteries** | Deoxygenated blood from RV to alveolar capillaries | Systolic ~25 mmHg; mean ~15 mmHg |
| **Pulmonary capillaries** | Gas exchange at alveolar wall | ~8–10 mmHg |
| **Pulmonary veins** | Oxygenated blood to LA | ~5–8 mmHg |
| **Bronchial arteries** (from aorta) | Nutrition of bronchial walls to generation ~14–16 | ~100 mmHg (systemic) |

## Function

### Ventilation

Tidal breathing (~0.5 L at rest, 12–16 breaths/min = ~6–8 L/min minute ventilation) moves fresh air to the alveoli. The **alveolar ventilation rate** is:

$$\dot{V}_A = f \times (V_T - V_D) = 15 \times (500 - 150) = 5,250 \text{ mL/min}$$

where V_D is the anatomical dead space (~150 mL). Alveolar ventilation determines alveolar PCO₂ (PACO₂ ≈ 5,250/40 × 0.863 ≈ 40 mmHg at rest).

### Gas Exchange

Gas exchange is governed by Fick's law (see [Alveolus](../../05-tissue/alveolus/README.md)). The diffusing capacity of the lung for CO (DLCO) is a clinical measure of the gas-exchange surface area × diffusivity product — it falls in emphysema (lost surface area) and pulmonary fibrosis (thickened membrane).

### Pulmonary Mechanics

Key lung volumes:

| Parameter | Volume (adult) |
|:---|:---:|
| Total lung capacity (TLC) | ~6.0 L |
| Functional residual capacity (FRC) | ~2.5 L |
| Residual volume (RV) | ~1.2 L |
| Tidal volume (VT) at rest | ~0.5 L |
| Vital capacity (VC) | ~4.8 L |
| Inspiratory reserve volume (IRV) | ~3.0 L |
| Expiratory reserve volume (ERV) | ~1.1 L |

Lung compliance (C = ΔV/ΔP) and airway resistance (R) determine the work of breathing. Normal FEV₁/FVC ≥0.7; obstruction (asthma, COPD) reduces FEV₁/FVC; restriction (fibrosis) reduces both FEV₁ and FVC proportionally.

### Non-Respiratory Functions

The lung is not purely a gas exchanger:
- **Metabolic:** Converts angiotensin I → angiotensin II (ACE); degrades bradykinin; inactivates serotonin; synthesises prostaglandins
- **Filtration:** Traps microemboli in the pulmonary microvasculature
- **Immune surveillance:** Alveolar macrophages, dendritic cells, MALT (mucosa-associated lymphoid tissue) in airways

## Connections

- **Contains** → [Alveolus](../../05-tissue/alveolus/README.md): ~300 million alveoli form the gas-exchange parenchyma; each is a 0.2 mm air sac with AT1/AT2 epithelium apposed to pulmonary capillaries.
- **Contains** → [Type II pneumocyte](../../04-cellular/type-ii-pneumocyte/README.md): AT2 cells distributed throughout alveoli produce surfactant and repair the epithelium after injury.
- **Part-of** → [Respiratory system](../../07-system/respiratory-system/README.md): The lungs are the gas-exchange organ of the respiratory system; they receive ventilation from the conducting airways and are perfused by the pulmonary circulation.
- **Damaged-by** → [SARS-CoV-2](../../../02-pathogen/01-viruses/sars-cov-2/README.md): SARS-CoV-2 causes bilateral diffuse alveolar damage and ARDS — the most lethal manifestation of COVID-19.
- **Damaged-by** → [Influenza A virus](../../../02-pathogen/01-viruses/influenza-a/README.md): Influenza A causes viral pneumonitis, primary influenza pneumonia, and secondary bacterial pneumonia — all causing alveolar and parenchymal lung damage.
- **Damaged-by** → [Mycobacterium tuberculosis](../../../02-pathogen/02-bacteria/mycobacterium-tuberculosis/README.md): Pulmonary TB destroys upper-lobe parenchyma via caseating granulomas, cavities, and progressive fibrosis.
- `connects-to` → **[Pulmonary Arterial Hypertension](../../07-system/pulmonary-arterial-hypertension/README.md)** — PAH obliterates pulmonary arterioles (<500 µm) via medial hypertrophy, intimal fibrosis, and plexiform lesions → RV pressure overload → cor pulmonale; RHC required for diagnosis; mPAP >20 mmHg + PVR ≥2 WU + PAWP ≤15 mmHg.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Periostin drives fibrotic remodeling in chronic lung disease: TGF-β + IL-13 → POSTN in lung fibroblasts → collagen matrix assembly → subepithelial fibrosis; serum periostin correlates with lung function decline in asthma and IPF; marks remodeling distinct from acute inflammation.

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

## Pathology

| Disease | Pathophysiology |
|:---|:---|
| **COPD / emphysema** | Proteolytic destruction of alveolar walls (smoking → neutrophil/macrophage elastase) → reduced surface area → reduced DLCO → airflow obstruction (air trapping) |
| **Asthma** | Airway inflammation → bronchospasm → reversible airflow obstruction; lung parenchyma often preserved |
| **Idiopathic pulmonary fibrosis (IPF)** | Progressive fibrotic replacement of alveoli → restriction → impaired DLCO → progressive hypoxaemia; no proven disease-modifying therapy except anti-fibrotics (nintedanib, pirfenidone) and transplant |
| **Lung cancer** | Leading cause of cancer death; ~85% non-small cell (adenocarcinoma, squamous, large cell); ~15% small cell; most strongly associated with tobacco smoking |
| **Pneumonia** | Bacterial (Streptococcus pneumoniae most common; Staphylococcus in influenza superinfection), viral (COVID-19, influenza), atypical; causes consolidation of one or more segments/lobes |
| **Pulmonary hypertension** | Sustained elevated PAP → right-heart pressure overload → right heart failure; multiple etiologies (WHO Groups 1–5) |
| **Pleural disease** | Pneumothorax (air in pleural space → lung collapse), pleural effusion (fluid → compressive atelectasis), empyema (infected effusion), malignant mesothelioma |

## See Also

- [Alveolus](../../05-tissue/alveolus/README.md) — gas-exchange tissue unit.
- [Type II pneumocyte](../../04-cellular/type-ii-pneumocyte/README.md) — surfactant and stem cell.
- [Respiratory system](../../07-system/respiratory-system/README.md) — the system the lungs are part of.
- [Oxygen](../../02-atomic/oxygen/README.md) — the gas the lung delivers.

[^west-respiratory-physiology]: West JB, Luks AM. *West's Respiratory Physiology: The Essentials.* 10th ed. Wolters Kluwer; 2016. [lww.com/Product/9781496310118](https://www.lww.com/Product/9781496310118)
[^weibel-1963-morphometry]: Weibel ER. *Morphometry of the Human Lung.* Academic Press; 1963. [doi:10.1007/978-3-642-87553-3](https://doi.org/10.1007/978-3-642-87553-3)
[^nhlbi-lung-how-lungs-work]: National Heart, Lung, and Blood Institute. How the Lungs Work. [nhlbi.nih.gov/health/lungs](https://www.nhlbi.nih.gov/health/lungs)
[^crapo-1982-alveolar-morphometry]: Crapo JD, Barry BE, Gehr P, Bachofen M, Weibel ER. Cell number and cell characteristics of the normal human lung. *Am Rev Respir Dis.* 1982;125(6):740-5. [doi:10.1164/arrd.1982.125.6.740](https://doi.org/10.1164/arrd.1982.125.6.740) · [PubMed 7044530](https://pubmed.ncbi.nlm.nih.gov/7044530/)
