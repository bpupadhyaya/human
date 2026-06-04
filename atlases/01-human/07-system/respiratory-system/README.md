---
schema: human-scale-entry/v1
id: respiratory-system
name: Respiratory system
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-03
summary: "Airways, lungs, chest wall, and diaphragm forming the gas-exchange apparatus: ~6 L/min ventilation to 300 million alveoli. Coupled to the cardiovascular system via the pulmonary circuit. Controlled by medullary respiratory centres and chemoreceptors."
aliases: ["respiratory system", "pulmonary system", "ventilatory system"]
sources:
  - id: west-respiratory-physiology
    type: textbook
    cite: "West JB, Luks AM. West's Respiratory Physiology: The Essentials. 10th ed. Wolters Kluwer; 2016. ISBN 978-1-4963-1011-1."
    url: "https://www.lww.com/Product/9781496310118"
    accessed: "2026-06-03"
  - id: weibel-2017-alveolar-dimensions
    type: peer-reviewed
    cite: "Weibel ER. Lung morphometry: the link between structure and function. Cell Tissue Res. 2017;367(3):413-26."
    doi: "10.1007/s00441-016-2541-4"
    pmid: "27981371"
    url: "https://doi.org/10.1007/s00441-016-2541-4"
  - id: openstax-anatomy-ch22
    type: textbook
    cite: "OpenStax. Anatomy & Physiology 2e, Ch. 22: The Respiratory System."
    url: "https://openstax.org/books/anatomy-and-physiology-2e/pages/22-introduction"
    accessed: "2026-06-03"
cross_links:
  - target: 01-human/06-organ/lung
    relation: contains
    note: "The paired lungs are the gas-exchange organs of the respiratory system, containing ~300 million alveoli and a ~70 m² surface area for O₂–CO₂ exchange."
  - target: 01-human/08-whole-body/human-body
    relation: part-of
    note: "The respiratory system is one of the eleven major organ systems of the human body; it interacts most closely with the cardiovascular system via the pulmonary circuit."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "The respiratory and cardiovascular systems are functionally inseparable: the pulmonary circuit carries deoxygenated blood to the alveolar capillaries and returns oxygenated blood to the left heart, coupling gas exchange to systemic O₂ delivery."
  - target: 02-pathogen/01-viruses/influenza-a
    relation: damaged-by
    note: "Influenza A is primarily a respiratory pathogen; severe disease causes viral pneumonitis, ARDS, and respiratory failure through destruction of the alveolar-capillary interface."
taxonomy:
  uberon: "UBERON:0001004"
  fma: "FMA:7161"
---

# Respiratory system

## Overview

The respiratory system is the body's **gas-exchange apparatus** — the integrated set of structures that moves O₂ from ambient air into the bloodstream and removes CO₂ in the opposite direction, maintaining the arterial blood gas tensions (PaO₂ ~100 mmHg, PaCO₂ ~40 mmHg, pH ~7.40) essential for normal cellular function. It comprises:

1. **Upper airway** — nose, mouth, pharynx, larynx: filter, warm, humidify inspired air
2. **Conducting airways** — trachea → bronchi → bronchioles: transport air; no gas exchange; anatomical dead space ~150 mL
3. **Lungs and alveoli** — the gas-exchange parenchyma: ~300 million alveoli, ~70 m² surface area [^weibel-2017-alveolar-dimensions]
4. **Chest wall and diaphragm** — the mechanical pump: inspiratory muscles (diaphragm primary; external intercostals, accessory muscles) generate negative intrapleural pressure to drive air inward
5. **Pleura** — visceral and parietal pleura, maintaining the pressure linkage between lung and chest wall

The respiratory system cannot function in isolation — it is tightly coupled to the **cardiovascular system** via the pulmonary circuit, and its rhythm is driven by medullary and pontine **respiratory centres** modulated by chemoreceptors detecting PaO₂, PaCO₂, and arterial pH.

## Structure

### Upper Airway

The upper airway filters (nasal turbinates), warms, and humidifies inspired air. Key structures:

- **Nose/nasal cavity:** Mucociliary clearance; ~3 L/min airflow at rest through both nares
- **Nasopharynx / oropharynx:** Convergence of nasal and oral airstreams; site of tonsils and adenoids
- **Larynx:** Glottis (vocal cords) — the narrowest part of the adult upper airway; site of croup, epiglottitis, and intubation
- **Eustachian tube openings, sinuses:** Connected cavities whose inflammation (sinusitis, otitis) affects the upper respiratory tract collectively

### Conducting Airways (Trachea → Terminal Bronchioles)

- **Trachea:** ~11 cm long, 18 mm diameter; 16–20 C-shaped cartilage rings; lined by pseudostratified ciliated columnar epithelium with goblet cells (mucociliary escalator)
- **Bronchi:** 23 airway generations (Weibel) branch dichotomously; cartilage present to generation ~12–14; smooth muscle present throughout; innervated by autonomic nervous system (β2-AR → bronchodilation; M3 → bronchoconstriction)
- **Terminal bronchioles (generation 16):** ~0.5 mm diameter; no cartilage; pure smooth muscle wall; the last purely conducting airway segment

### Respiratory Zone (Generations 17–23)

- **Respiratory bronchioles:** First airways with alveolar outpouchings; begin gas exchange
- **Alveolar ducts / sacs / alveoli:** Full gas exchange; alveolar surface area 70 m² (see [Alveolus](../../05-tissue/alveolus/README.md))

### Respiratory Muscles

| Muscle | Role | Innervation |
|:---|:---|:---|
| **Diaphragm** | Primary inspiratory muscle; generates ~70% of inspiratory effort at rest | Phrenic nerve (C3–C5) |
| **External intercostals** | Elevate ribs → increase chest volume → inspiration | Intercostal nerves T1–T11 |
| **Accessory muscles** (sternocleidomastoid, scalenes) | Recruited in exercise and respiratory distress | Cranial and cervical nerves |
| **Internal intercostals / abdominals** | Active expiration (normally expiration is passive via lung recoil) | Intercostal and lumbar nerves |

**Diaphragm failure** (e.g., phrenic nerve injury in high cervical SCI, C3–C5 demyelination in Guillain-Barré) requires mechanical ventilation.

### Neural Control

The respiratory rhythm originates in the **medullary respiratory centres**:

- **Pre-Bötzinger complex** (ventral respiratory group, VRG): the respiratory rhythm generator; produces the ~12–16/min oscillatory inspiratory drive
- **Pneumotaxic centre** (pontine respiratory group): modulates breath timing, limits inspiratory duration
- **Ventral and dorsal respiratory groups:** Output to phrenic and intercostal motor neurons

**Chemoreceptor feedback:**
- **Central chemoreceptors** (medullary surface): respond to PCO₂/pH in CSF; most powerful driver of ventilation; rising PCO₂ → increased ventilation within seconds
- **Peripheral chemoreceptors** (carotid body, aortic body): respond to PaO₂ (<60 mmHg triggers significant activation), PaCO₂, and pH; primary O₂ sensors; important in acclimatisation to altitude

## Function

### Ventilation and Gas Exchange

At rest:
- **Respiratory rate:** 12–16 breaths/min
- **Tidal volume (VT):** ~500 mL
- **Minute ventilation (V̇E):** ~6–8 L/min
- **Alveolar ventilation (V̇A):** ~5.25 L/min (VE - dead space ventilation)

At maximal exercise:
- V̇E rises to **100–200 L/min** (20–30× resting)
- VT increases to ~3 L; RR increases to ~40–60/min
- O₂ uptake (VO₂max): 3,000–6,000 mL/min in trained athletes

The ventilatory control loop maintains PACO₂ at ~40 mmHg (and thus PaCO₂ ~40 mmHg) across this 20–30-fold change in metabolic rate — a remarkable regulatory achievement.

### Acid-Base Regulation

The respiratory system contributes to acid-base homeostasis via CO₂ regulation. The Henderson-Hasselbalch relationship:

$$\text{pH} = 6.1 + \log\frac{[\text{HCO}_3^-]}{0.0306 \times \text{PaCO}_2}$$

- **Respiratory acidosis:** Hypoventilation → ↑PaCO₂ → ↓pH (COPD exacerbation, opioid overdose, respiratory failure)
- **Respiratory alkalosis:** Hyperventilation → ↓PaCO₂ → ↑pH (anxiety, altitude, pulmonary embolism, early sepsis)
- **Metabolic acidosis:** Compensated by hypervention → ↓PaCO₂ (Kussmaul breathing in DKA)

### Mucociliary Defence

The mucociliary escalator (ciliated cells + goblet cell mucus) continuously clears particles, bacteria, and debris from the airways. Mucociliary dysfunction (cystic fibrosis, primary ciliary dyskinesia, chronic bronchitis) predisposes to recurrent pulmonary infection.

## Connections

- **Contains** → [Lung](../../06-organ/lung/README.md): The lungs are the gas-exchange organs, housing the alveolar parenchyma and branching airways.
- **Part-of** → [Human body](../../08-whole-body/human-body/README.md): The respiratory system is one of eleven major organ systems, interdependent with all others — cardiovascular, nervous, endocrine, immune.
- **Connects-to** → [Cardiovascular system](../../07-system/cardiovascular-system/README.md): The pulmonary circuit is the anatomical link: deoxygenated blood from the right heart passes through pulmonary capillaries for gas exchange, then oxygenated blood returns to the left heart for systemic distribution. The two systems share the alveolar-capillary interface and cannot be studied or treated in isolation.
- **Damaged-by** → [Influenza A virus](../../../02-pathogen/01-viruses/influenza-a/README.md): Influenza A is primarily a respiratory pathogen, causing tracheobronchitis, viral pneumonitis, and ARDS; severe disease impairs the system's ventilatory and gas-exchange functions.

## Pathology

| Disease | Mechanism | Physiological signature |
|:---|:---|:---|
| **COPD** | Smoke-induced airway inflammation, emphysema, mucus hypersecretion | Obstruction (FEV₁/FVC <0.7), air trapping, ↑RV, ↓DLCO |
| **Asthma** | Eosinophilic airway inflammation, smooth-muscle hyper-reactivity, mucus plugging | Reversible obstruction; ↑ variability in peak flow |
| **Pulmonary fibrosis** | Alveolar injury → fibroblast activation → fibrosis | Restriction (↓TLC, ↓FVC), ↓DLCO, progressive hypoxaemia |
| **Pulmonary embolism** | Thrombus in pulmonary arteries → V̇/Q̇ mismatch, dead space increase, ↑RV afterload | Acute dyspnoea, hypoxaemia, tachycardia, possible shock |
| **ARDS** | Diffuse alveolar damage → bilateral alveolar flooding → severe hypoxaemia | PaO₂/FiO₂ <300 (mild), <200 (moderate), <100 (severe); ↓compliance |
| **Obstructive sleep apnoea** | Upper airway collapse during sleep → repetitive hypoxia, hypercapnia, arousal | Daytime somnolence, cardiovascular sequelae (hypertension, AF, heart failure) |
| **Lung cancer** | Malignant transformation of bronchial/alveolar epithelium | Cough, haemoptysis, dyspnoea; systemic effects via metastases and paraneoplastic syndromes |

## See Also

- [Lung](../../06-organ/lung/README.md) — the gas-exchange organ.
- [Alveolus](../../05-tissue/alveolus/README.md) — the functional unit of gas exchange.
- [Cardiovascular system](../../07-system/cardiovascular-system/README.md) — the linked circulation system.
- [Human body](../../08-whole-body/human-body/README.md) — the whole-body scale.

[^west-respiratory-physiology]: West JB, Luks AM. *West's Respiratory Physiology: The Essentials.* 10th ed. Wolters Kluwer; 2016. [lww.com/Product/9781496310118](https://www.lww.com/Product/9781496310118)
[^weibel-2017-alveolar-dimensions]: Weibel ER. Lung morphometry: the link between structure and function. *Cell Tissue Res.* 2017;367(3):413-26. [doi:10.1007/s00441-016-2541-4](https://doi.org/10.1007/s00441-016-2541-4) · [PubMed 27981371](https://pubmed.ncbi.nlm.nih.gov/27981371/)
[^openstax-anatomy-ch22]: OpenStax. *Anatomy & Physiology 2e*, Ch. 22: The Respiratory System. [Read online →](https://openstax.org/books/anatomy-and-physiology-2e/pages/22-introduction)
