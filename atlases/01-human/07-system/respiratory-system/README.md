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
  - target: 02-pathogen/02-bacteria/streptococcus-pneumoniae
    relation: infected-by
    note: "S. pneumoniae colonizes the nasopharynx asymptomatically in 5–70% of children; lower respiratory tract invasion causes lobar pneumonia, bacteremia (20–30% of CAP), and meningitis; the respiratory system is its primary site of pathology."
  - target: 02-pathogen/02-bacteria/streptococcus-pneumoniae
    relation: damaged-by
    note: "Pneumococcal pneumonia causes acute alveolar consolidation, fibrinopurulent exudate, impaired gas exchange, and — in severe disease — respiratory failure; pneumolysin contributes to alveolar epithelial damage."
  - target: 03-medicine/01-modern/02-respiratory/corticosteroids
    relation: treated-by
    note: "Inhaled corticosteroids (ICS) are the cornerstone maintenance therapy for persistent asthma, reducing airway inflammation and exacerbation frequency by 50–60%; systemic corticosteroids are first-line for COPD exacerbations and acute severe asthma."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: damaged-by
    evidence: west-respiratory-physiology
    note: "A. fumigatus conidia inhaled into the respiratory system germinate in the bronchi and alveoli of immunocompromised hosts, causing invasive pulmonary aspergillosis with angioinvasion and haemoptysis."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: modulated-by
    note: "Modulated by Smooth Muscle Cell."
  - target: 02-pathogen/01-viruses/respiratory-syncytial-virus
    relation: damaged-by
    note: "Damaged by Respiratory Syncytial Virus."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: damaged-by
    note: "Damaged by Pneumocystis jirovecii (formerly carinii)."
  - target: 03-medicine/01-modern/05-antiviral/oseltamivir
    relation: treated-by
    note: "Oseltamivir reduces influenza A/B symptom duration by ~17 hours (Dobson meta-analysis, Lancet 2015); reduces hospitalization in high-risk patients (elderly, immunocompromised, pregnant); must be started within 48h of symptom onset for maximal benefit."
  - target: 01-human/07-system/asthma
    relation: connects-to
    note: "Asthma is the commonest chronic disease of the respiratory system's airways: reversible bronchoconstriction and type-2 inflammation narrow the bronchi, causing wheeze and breathlessness—so the conducting airways, not the gas-exchange surface, bear the brunt of asthma."
  - target: 01-human/07-system/copd
    relation: connects-to
    note: "COPD is the major irreversible obstructive disease of the respiratory system: smoking-driven inflammation destroys alveoli (emphysema) and scars airways (chronic bronchitis), permanently limiting airflow—the chief cause of chronic respiratory failure in older adults."
  - target: 01-human/04-cellular/type-ii-pneumocyte
    relation: connects-to
    note: "Type II pneumocytes keep the respiratory system's gas-exchange surface working: they secrete surfactant that prevents alveolar collapse and act as progenitors regenerating the alveolar lining after injury—so their loss in ARDS and pneumonia drives respiratory failure."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Oxygen is the gas the respiratory system exists to capture: alveoli transfer O2 across the air-blood barrier into hemoglobin for tissue delivery, while CO2 is exhaled—so lung disease that impairs this exchange causes hypoxemia, the central threat in respiratory failure."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Hemoglobin completes what the respiratory system starts: lungs load O2 onto red-cell hemoglobin, which carries it to tissues and returns CO2 for exhalation—so anemia or abnormal hemoglobin can mimic lung disease by limiting oxygen delivery despite healthy lungs."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "The alveolus is the functional unit of the respiratory system: hundreds of millions of these thin-walled sacs create the vast surface where gas exchange occurs, so diseases that flood, collapse, or stiffen alveoli directly cause the hypoxemia of respiratory failure."
  - target: 01-human/03-molecular/surfactant
    relation: connects-to
    note: "Pulmonary surfactant keeps the respiratory system inflatable: secreted by type II pneumocytes, it lowers alveolar surface tension so the lung doesn't collapse on exhalation—its deficiency causes neonatal respiratory distress and contributes to ARDS in adults."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "COVID-19 is the respiratory system's defining modern threat: SARS-CoV-2 attacks airway and alveolar cells, and severe disease causes diffuse alveolar damage and hypoxemic respiratory failure—showing how a single virus can overwhelm the gas-exchange apparatus."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "Pulmonary arterial hypertension is where the respiratory and circulatory systems collide: remodeling of the lung's small arteries raises pulmonary pressure until the right heart fails, so this is a vascular disease that presents as breathlessness."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Breathing is run by the nervous system: brainstem respiratory centers set the rhythm and chemoreceptors sensing CO2 and oxygen adjust it breath by breath, so the respiratory system is only as reliable as the neural drive—lost in opioid overdose or brainstem stroke."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Respiration exists to trade carbon dioxide for oxygen: cells make CO2, blood carries it as bicarbonate, and the lungs exhale it, so the respiratory system is the body's main route to dump carbon—and CO2 levels set blood pH and the urge to breathe."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Alveolar macrophages guard the respiratory system: stationed in the air sacs, they engulf inhaled microbes and debris as the lung's first cellular defense, so their function (and dysfunction in smoking or COPD) shapes vulnerability to pneumonia."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Red cells complete the respiratory system's job: the lungs load oxygen onto erythrocyte hemoglobin and unload carbon dioxide, so breathing and the blood's red cells are one continuous gas-exchange system—lung disease and anemia both starve tissues of oxygen."
  - target: 01-human/07-system/cystic-fibrosis
    relation: connects-to
    note: "Cystic fibrosis is the respiratory system's archetypal genetic disease: a chloride-channel defect thickens airway mucus, trapping bacteria and causing the chronic infection and bronchiectasis that destroy the lungs—now transformed by CFTR-modulator drugs."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Nitric oxide fine-tunes the lungs' blood flow: it dilates pulmonary vessels to match perfusion with ventilation, and inhaled NO is used to open lung vessels in pulmonary hypertension and newborn respiratory failure."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "The respiratory system is the body's fast acid-base dial: by speeding or slowing breathing it controls how much CO2—and thus acid (hydrogen ions)—leaves the blood, so the lungs and kidneys together hold blood pH in its narrow safe range."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Breathing is commanded by the brain: the brainstem's respiratory centers set the rhythm and adjust it to CO2 and oxygen sensors, so the respiratory system is only as reliable as the neural drive behind it—lost in overdose or stroke."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells make the airways reactive: lining the bronchial walls, they release histamine and other mediators that constrict and inflame airways in asthma and allergy, a key cellular trigger of the wheezing respiratory diseases."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "Air is mostly nitrogen, and the lungs must reckon with it: this inert gas makes up most of each breath without being used, but under pressure it dissolves into blood and, on fast ascent from diving, bubbles out to cause decompression sickness."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils both defend and damage the airways: they swarm into infected or inflamed lungs to kill microbes, but in COPD, cystic fibrosis, and ARDS their flood of enzymes also digests lung tissue, driving chronic damage."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "The lungs and right heart are one circuit: the right ventricle pumps all the blood through the lungs for gas exchange, so chronic lung disease that stiffens this circuit overloads and fails the right heart (cor pulmonale)."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "The lungs are read in X-ray photons: chest radiographs and CT reveal pneumonia, tumors, fibrosis and collapse, the first window into respiratory disease."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Scarring stiffens the lungs: pulmonary fibrosis thickens the alveolar walls so oxygen can't cross and the lungs lose their stretch, the end-stage of many chronic lung diseases."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Lungs and kidneys jointly guard blood pH: the lungs blow off acid as CO2 while the kidneys excrete it, so each compensates when the other fails, the core of acid-base balance."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reveals the gossamer blood-air barrier: alveolar epithelium and capillary endothelium fuse into a membrane thin enough for oxygen to cross, while type II cells store surfactant in lamellar bodies and airway cells wave their cilia."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "The skin betrays failing lungs: when oxygen runs short, deoxygenated hemoglobin turns the lips and fingertips blue in cyanosis, making the skin a visible readout of how well the respiratory system is working."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "The gut and lungs share an immune conversation: through the gut-lung axis, the intestinal microbiome shapes airway immunity, so gut health influences susceptibility to asthma and respiratory infection."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "The airway is a frontline of immunity: with every breath the lungs meet airborne microbes, so mucociliary clearance, alveolar macrophages, and bronchus-associated lymphoid tissue form a vast immune barrier between the outside air and the blood."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "The vagus nerve tunes the airways with acetylcholine: parasympathetic cholinergic tone constricts bronchial smooth muscle and drives mucus, which is why anticholinergics (ipratropium, tiotropium) open the airways in asthma and COPD."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "One faulty channel ties lung to pancreas: in cystic fibrosis a defective CFTR thickens secretions in both, clogging the airways with mucus while blocking the pancreatic ducts that should deliver digestive enzymes."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "The airway mucosa is an antibody barrier: secretory IgA coats it to trap inhaled pathogens, while monoclonal antibodies against IgE and IL-5 now treat severe asthma — and misdirected antibody drives autoimmune lung disease like Goodpasture."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "A gut-lung axis links the two surfaces: the airway has its own microbiome, and gut flora shape lung immunity and allergic-asthma risk through circulating microbial metabolites — distant microbes tuning the respiratory tract."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Breathing bends to pregnancy and begins before birth: progesterone drives the increased ventilation and breathlessness of pregnancy, while fetal lung maturation and surfactant production set the timing of safe delivery."
  - target: 01-human/06-organ/ards
    relation: connects-to
    note: "ARDS is the respiratory system's final common failure: diffuse alveolar injury floods the gas-exchange surface with fluid, collapsing oxygenation and forcing the mechanical ventilation that defines critical respiratory illness."
  - target: 01-human/07-system/tuberculosis
    relation: connects-to
    note: "Tuberculosis is the archetypal chronic lung infection: Mycobacterium tuberculosis cavitates the parenchyma over months and remains among the leading infectious killers worldwide, a defining disease of the respiratory tract."
  - target: 01-human/07-system/rsv
    relation: connects-to
    note: "RSV is the leading cause of infant lower-respiratory infection: it inflames and plugs the small bronchioles, the commonest reason babies are hospitalized for trouble breathing."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Histamine narrows the airways: released from bronchial mast cells it constricts smooth muscle, swells the mucosa, and floods secretions, the rapid mediator behind allergic wheeze and a driver of airway hyper-reactivity."
  - target: 01-human/07-system/influenza
    relation: connects-to
    note: "Influenza is the recurring epidemic threat to the respiratory system: the virus strips the airway epithelium and can progress to viral pneumonia and ARDS, and its seasonal waves drive much of winter respiratory illness."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Obesity mechanically loads the respiratory system: excess chest and abdominal fat restrict lung expansion and, with upper-airway crowding, cause obstructive sleep apnoea and obesity hypoventilation that blunt ventilation."
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
- **Connects-to** → [Asthma](../asthma/README.md): The commonest chronic airway disease of the respiratory system — reversible bronchoconstriction and type-2 inflammation narrow the bronchi, so the conducting airways, not the gas-exchange surface, bear the brunt of asthma.
- **Connects-to** → [COPD](../copd/README.md): The major irreversible obstructive disease of the respiratory system — smoking-driven inflammation destroys alveoli (emphysema) and scars airways (chronic bronchitis), permanently limiting airflow and causing chronic respiratory failure.
- **Connects-to** → [Type II pneumocyte](../../04-cellular/type-ii-pneumocyte/README.md): These cells keep the gas-exchange surface working — secreting surfactant that prevents alveolar collapse and acting as progenitors that regenerate the alveolar lining, so their loss in ARDS and pneumonia drives respiratory failure.
- **Connects-to** → [Oxygen](../../02-atomic/oxygen/README.md): Oxygen is the gas the respiratory system exists to capture: alveoli transfer O2 across the air-blood barrier into hemoglobin for tissue delivery, while CO2 is exhaled—so lung disease that impairs this exchange causes hypoxemia, the central threat in respiratory failure.
- **Connects-to** → [Hemoglobin](../../03-molecular/hemoglobin/README.md): Hemoglobin completes what the respiratory system starts: lungs load O2 onto red-cell hemoglobin, which carries it to tissues and returns CO2 for exhalation—so anemia or abnormal hemoglobin can mimic lung disease by limiting oxygen delivery despite healthy lungs.
- **Connects-to** → [Alveolus](../../05-tissue/alveolus/README.md): The alveolus is the functional unit of the respiratory system: hundreds of millions of these thin-walled sacs create the vast surface where gas exchange occurs, so diseases that flood, collapse, or stiffen alveoli directly cause the hypoxemia of respiratory failure.
- **Connects-to** → [Pulmonary Surfactant](../../03-molecular/surfactant/README.md): Pulmonary surfactant keeps the respiratory system inflatable: secreted by type II pneumocytes, it lowers alveolar surface tension so the lung doesn't collapse on exhalation—its deficiency causes neonatal respiratory distress and contributes to ARDS in adults.
- **Connects-to** → [COVID-19 Disease](../covid-19-disease/README.md): COVID-19 is the respiratory system's defining modern threat: SARS-CoV-2 attacks airway and alveolar cells, and severe disease causes diffuse alveolar damage and hypoxemic respiratory failure—showing how a single virus can overwhelm the gas-exchange apparatus.
- **Connects-to** → [Pulmonary Arterial Hypertension](../pulmonary-arterial-hypertension/README.md): Pulmonary arterial hypertension is where the respiratory and circulatory systems collide: remodeling of the lung's small arteries raises pulmonary pressure until the right heart fails, so this is a vascular disease that presents as breathlessness.
- **Connects-to** → [Nervous System](../nervous-system/README.md): Breathing is run by the nervous system: brainstem respiratory centers set the rhythm and chemoreceptors sensing CO2 and oxygen adjust it breath by breath, so the respiratory system is only as reliable as the neural drive—lost in opioid overdose or brainstem stroke.
- **Connects-to** → [Carbon](../../02-atomic/carbon/README.md): Respiration exists to trade carbon dioxide for oxygen: cells make CO2, blood carries it as bicarbonate, and the lungs exhale it, so the respiratory system is the body's main route to dump carbon—and CO2 levels set blood pH and the urge to breathe.
- **Connects-to** → [Macrophage](../../04-cellular/macrophage/README.md): Alveolar macrophages guard the respiratory system: stationed in the air sacs, they engulf inhaled microbes and debris as the lung's first cellular defense, so their function (and dysfunction in smoking or COPD) shapes vulnerability to pneumonia.
- **Connects-to** → [Erythrocyte](../../04-cellular/erythrocyte/README.md): Red cells complete the respiratory system's job: the lungs load oxygen onto erythrocyte hemoglobin and unload carbon dioxide, so breathing and the blood's red cells are one continuous gas-exchange system—lung disease and anemia both starve tissues of oxygen.
- **Connects-to** → [Cystic Fibrosis](../cystic-fibrosis/README.md): Cystic fibrosis is the respiratory system's archetypal genetic disease: a chloride-channel defect thickens airway mucus, trapping bacteria and causing the chronic infection and bronchiectasis that destroy the lungs—now transformed by CFTR-modulator drugs.
- **Connects-to** → [Nitric Oxide](../../03-molecular/nitric-oxide/README.md): Nitric oxide fine-tunes the lungs' blood flow: it dilates pulmonary vessels to match perfusion with ventilation, and inhaled NO is used to open lung vessels in pulmonary hypertension and newborn respiratory failure.
- **Connects-to** → [Hydrogen](../../02-atomic/hydrogen/README.md): The respiratory system is the body's fast acid-base dial: by speeding or slowing breathing it controls how much CO2—and thus acid (hydrogen ions)—leaves the blood, so the lungs and kidneys together hold blood pH in its narrow safe range.
- **Connects-to** → [Brain](../../06-organ/brain/README.md): Breathing is commanded by the brain: the brainstem's respiratory centers set the rhythm and adjust it to CO2 and oxygen sensors, so the respiratory system is only as reliable as the neural drive behind it—lost in overdose or stroke.
- **Connects-to** → [Mast Cell](../../04-cellular/mast-cell/README.md): Mast cells make the airways reactive: lining the bronchial walls, they release histamine and other mediators that constrict and inflame airways in asthma and allergy, a key cellular trigger of the wheezing respiratory diseases.
- **Connects-to** → [Nitrogen](../../02-atomic/nitrogen/README.md): Air is mostly nitrogen, and the lungs must reckon with it: this inert gas makes up most of each breath without being used, but under pressure it dissolves into blood and, on fast ascent from diving, bubbles out to cause decompression sickness.
- **Connects-to** → [Neutrophil](../../04-cellular/neutrophil/README.md): Neutrophils both defend and damage the airways: they swarm into infected or inflamed lungs to kill microbes, but in COPD, cystic fibrosis, and ARDS their flood of enzymes also digests lung tissue, driving chronic damage.
- **Connects-to** → [Heart](../../06-organ/heart/README.md): The lungs and right heart are one circuit: the right ventricle pumps all the blood through the lungs for gas exchange, so chronic lung disease that stiffens this circuit overloads and fails the right heart (cor pulmonale).
- **Connects-to** → [Photon](../../01-subatomic/photon/README.md): The lungs are read in X-ray photons: chest radiographs and CT reveal pneumonia, tumors, fibrosis and collapse, the first window into respiratory disease.
- **Connects-to** → [Fibrosis](../../05-tissue/fibrosis/README.md): Scarring stiffens the lungs: pulmonary fibrosis thickens the alveolar walls so oxygen can't cross and the lungs lose their stretch, the end-stage of many chronic lung diseases.
- **Connects-to** → [Kidney](../../06-organ/kidney/README.md): Lungs and kidneys jointly guard blood pH: the lungs blow off acid as CO2 while the kidneys excrete it, so each compensates when the other fails, the core of acid-base balance.
- **Connects-to** → [Electron](../../01-subatomic/electron/README.md): Electron microscopy reveals the gossamer blood-air barrier: alveolar epithelium and capillary endothelium fuse into a membrane thin enough for oxygen to cross, while type II cells store surfactant in lamellar bodies and airway cells wave their cilia.
- **Connects-to** → [Skin](../../06-organ/skin/README.md): The skin betrays failing lungs: when oxygen runs short, deoxygenated hemoglobin turns the lips and fingertips blue in cyanosis, making the skin a visible readout of how well the respiratory system is working.
- **Connects-to** → [Large Intestine](../../06-organ/large-intestine/README.md): The gut and lungs share an immune conversation: through the gut-lung axis, the intestinal microbiome shapes airway immunity, so gut health influences susceptibility to asthma and respiratory infection.
- **Damaged-by** → [Influenza A virus](../../../02-pathogen/01-viruses/influenza-a/README.md): Influenza A is primarily a respiratory pathogen, causing tracheobronchitis, viral pneumonitis, and ARDS; severe disease impairs the system's ventilatory and gas-exchange functions.
- **Treated-by** → [Oseltamivir](../../../03-medicine/01-modern/05-antiviral/oseltamivir/README.md): Reduces influenza A/B symptom duration by ~17 hours (Dobson, Lancet 2015); reduces hospitalization in high-risk patients; must be started within 48h of symptom onset for maximal benefit.
- **Damaged-by** → [Acute Respiratory Distress Syndrome](../../06-organ/ards/README.md): ARDS is the respiratory system's final common failure: diffuse alveolar injury floods the gas-exchange surface with fluid, collapsing oxygenation and forcing the mechanical ventilation that defines critical respiratory illness.
- **Damaged-by** → [Tuberculosis](../tuberculosis/README.md): Tuberculosis is the archetypal chronic lung infection: Mycobacterium tuberculosis cavitates the parenchyma over months and remains among the leading infectious killers worldwide, a defining disease of the respiratory tract.
- **Damaged-by** → [RSV](../rsv/README.md): RSV is the leading cause of infant lower-respiratory infection: it inflames and plugs the small bronchioles, the commonest reason babies are hospitalized for trouble breathing.
- **Connects-to** → [Histamine](../../03-molecular/histamine/README.md): Histamine narrows the airways: released from bronchial mast cells it constricts smooth muscle, swells the mucosa, and floods secretions, the rapid mediator behind allergic wheeze and a driver of airway hyper-reactivity.
- **Connects-to** → [Influenza](../influenza/README.md): Influenza is the recurring epidemic threat to the respiratory system: the virus strips the airway epithelium and can progress to viral pneumonia and ARDS, and its seasonal waves drive much of winter respiratory illness.
- **Connects-to** → [Obesity](../obesity/README.md): Obesity mechanically loads the respiratory system: excess chest and abdominal fat restrict lung expansion and, with upper-airway crowding, cause obstructive sleep apnoea and obesity hypoventilation that blunt ventilation.
- `prevented-by` → **[PCV13 (Prevnar 13)](../../../../04-vaccine/08-conjugate/pcv13/README.md)** — CAPiTA RCT (N=84,496 adults ≥65): PCV13 achieved 45.6% VE against vaccine-type CAP and 75% VE against invasive pneumococcal disease; prevents pneumococcal pneumonia, the leading infectious cause of respiratory hospitalisation in older adults.

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

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
