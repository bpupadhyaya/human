---
schema: human-scale-entry/v1
id: copd
name: COPD
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Chronic obstructive pulmonary disease from cigarette smoke-induced alveolar destruction (emphysema) and airway remodeling; FEV1/FVC <0.7 defines obstruction. Bronchodilators (LABA/LAMA) are first-line; inhaled corticosteroids reduce exacerbations in eosinophilic COPD."
aliases: ["chronic obstructive pulmonary disease", "emphysema", "chronic bronchitis", "COPD-asthma overlap", "ACO"]
sources:
  - id: rabe-2017-gold-copd
    type: peer-reviewed
    cite: "Rabe KF, Watz H. Chronic obstructive pulmonary disease. Lancet. 2017;389(10082):1931-1940."
    doi: "10.1016/S0140-6736(17)31222-9"
    pmid: "28513453"
    url: "https://doi.org/10.1016/S0140-6736(17)31222-9"
  - id: vestbo-2013-gold-strategy
    type: peer-reviewed
    cite: "Vestbo J, Hurd SS, Agustí AG, et al. Global strategy for the diagnosis, management, and prevention of chronic obstructive pulmonary disease: GOLD executive summary. Am J Respir Crit Care Med. 2013;187(4):347-365."
    doi: "10.1164/rccm.201204-0596PP"
    pmid: "22878278"
    url: "https://doi.org/10.1164/rccm.201204-0596PP"
  - id: jones-2017-dupilumab-copd
    type: peer-reviewed
    cite: "Bhatt SP, Rabe KF, Hanania NA, et al. Dupilumab for COPD with Type 2 Inflammation Indicated by Eosinophil Counts. N Engl J Med. 2023;389(3):205-214."
    doi: "10.1056/NEJMoa2303966"
    pmid: "37272521"
    url: "https://doi.org/10.1056/NEJMoa2303966"
cross_links:
  - target: 01-human/07-system/respiratory-system
    relation: targets
    note: "COPD irreversibly destroys the respiratory system: emphysema enlarges and ruptures alveolar walls → reduced gas exchange surface; airway remodeling (smooth muscle hypertrophy, mucous gland hyperplasia) → chronic airflow obstruction; both processes are largely irreversible."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-beta1 mediates small airway fibrosis and remodeling in COPD; cigarette smoke-activated macrophages produce TGF-beta → subepithelial fibrosis → airway wall thickening → fixed obstruction; TGF-beta also impairs alveolar repair after smoke-induced damage."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Alveolar macrophages are central COPD effectors; cigarette smoke activates macrophages → MMP-9/12 secretion → elastin and collagen degradation → emphysema; COPD macrophages are also defective at clearing bacteria and apoptotic cells → susceptibility to exacerbations."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils accumulate in COPD airways (especially during exacerbations); neutrophil elastase degrades alpha-1 antitrypsin and lung matrix; NETosis releases DNA and proteases; IL-8 drives neutrophil recruitment; neutrophilic COPD does not respond to inhaled corticosteroids."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "COPD destroys lung architecture: emphysema ruptures alveolar walls → reduced gas exchange; chronic bronchitis remodels small airways → fixed obstruction; both largely irreversible; GOLD staging (FEV1/FVC <0.7, GOLD 1-4) guides risk stratification and treatment selection."
  - target: 01-human/07-system/asthma
    relation: connects-to
    note: "COPD-asthma overlap (ACO) affects ~10-15% of COPD patients: combined fixed obstruction (COPD) and eosinophilia/reversibility (asthma); ACO has more frequent exacerbations; dupilumab approved for COPD with eosinophilia ≥300/µL (NOTUS/BOREAS trials: 30% exacerbation reduction)."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β is a key COPD exacerbation amplifier: NLRP3 inflammasome activation by smoke → IL-1β release → neutrophil and macrophage recruitment → airway inflammation; IL-1β promotes goblet cell hyperplasia → mucus hypersecretion; canakinumab (IL-1β mAb) studied in COPD."
  - target: 01-human/07-system/cystic-fibrosis
    relation: connects-to
    note: "COPD and cystic fibrosis are chronic obstructive airway diseases: COPD is acquired emphysema from decades of cigarette smoke, while CF is inherited CFTR failure causing childhood bronchiectasis — yet both end in neutrophilic airway destruction and respiratory failure."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Severe COPD strains the right heart: chronic hypoxia drives pulmonary vasoconstriction and arteriolar remodeling → pulmonary hypertension (WHO Group 3) → right ventricular hypertrophy and failure (cor pulmonale), with raised JVP and peripheral edema."
  - target: 02-pathogen/02-bacteria/streptococcus-pneumoniae
    relation: connects-to
    note: "Bacterial infection — often Streptococcus pneumoniae, Haemophilus influenzae, or Moraxella — drives roughly a quarter of COPD exacerbations; purulent sputum guides antibiotics, and pneumococcal vaccination is recommended to help prevent them."
  - target: 01-human/07-system/nsclc
    relation: connects-to
    note: "COPD and lung cancer are smoking's twin diseases that frequently coexist: shared tobacco-driven inflammation, oxidative stress and impaired DNA repair mean COPD independently raises NSCLC risk, COPD limits surgery, and both are screened together with low-dose CT in heavy smokers."
  - target: 01-human/07-system/rsv
    relation: connects-to
    note: "RSV is an underappreciated driver of COPD exacerbations: it infects airway epithelium to provoke neutrophilic inflammation and bronchospasm, accounting for a notable share of hospitalized flares in older adults; new adult RSV vaccines (Arexvy, Abrysvo) help reduce this burden."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Cigarette smoke is the dominant cause of COPD: inhaled carbon-rich particulates and combustion chemicals trigger protease-antiprotease imbalance and chronic neutrophilic inflammation → emphysema and small-airway fibrosis; cessation is the only intervention that slows decline."
---

# COPD

## Overview

**Chronic obstructive pulmonary disease (COPD)** is a common, preventable, and treatable chronic respiratory disease characterized by persistent, progressive **airflow limitation** that is not fully reversible, associated with an enhanced chronic inflammatory response in the airways and lung to noxious particles or gases — principally **cigarette smoke**. COPD is the **third leading cause of death globally** (~3.3 million deaths/year, WHO 2019) and a leading cause of disability [^rabe-2017-gold-copd].

COPD encompasses two overlapping pathological processes:
- **Emphysema:** Permanent enlargement and destruction of airspaces distal to the terminal bronchiole → loss of alveolar surface area → reduced gas exchange → hypoxemia; also destruction of elastic recoil → air trapping → hyperinflation
- **Chronic bronchitis:** Productive cough on most days for ≥3 months in ≥2 consecutive years; airway inflammation → mucus hypersecretion → small airway remodeling → fixed obstruction

**Global burden (GBD 2019):** ~390 million people affected globally; COPD is severely underdiagnosed (only ~25% of patients receive diagnosis); 90% of COPD deaths occur in low-to-middle income countries where spirometry is limited.

**Risk factors:**
- **Cigarette smoking (dominant):** ~80-90% of COPD in high-income countries; pack-year dose-response; passive smoking in childhood → accelerated lung function decline
- **Biomass fuel exposure:** Wood smoke from cooking fires → COPD in women in developing countries (accounts for ~50% of global COPD burden)
- **Occupational exposures:** Coal dust, silica, cadmium, isocyanates
- **Genetic:** Alpha-1 antitrypsin (AAT) deficiency (AATD) — Z allele (Glu342Lys) → polymerization and intracellular retention → panacinar emphysema by age 40 in smokers (earlier); SERPINA1 Pi*ZZ genotype; 1-2% of COPD
- **Early life factors:** Prematurity, low birth weight, childhood respiratory infections → reduced peak lung function → lower FEV1 trajectory → COPD risk in adulthood

## Structure

### Lung pathology in COPD

**Small airways disease (obstructive bronchiolitis):**
- Airway wall infiltrated by macrophages, CD8+ T cells (Tc1), and neutrophils
- Goblet cell hyperplasia → excess mucus → airway plugging → V/Q mismatch
- Subepithelial fibrosis (TGF-beta-driven) → irreversible narrowing of airways <2 mm diameter
- Loss of small airways (airway "pruning") is the primary determinant of FEV1 decline in early COPD

**Emphysema:**
- **Centrilobular (centriacinar):** Destruction centered on respiratory bronchioles; most common; upper-lobe predominant; smoking-related; macrophage and neutrophil elastase/MMP-12 → elastin degradation → alveolar wall rupture
- **Panacinar (panlobular):** Uniform destruction of entire acinus; lower-lobe predominant; associated with AAT deficiency (unopposed neutrophil elastase); can occur in severe smoking-related COPD
- **Paraseptal:** Subpleural; associated with spontaneous pneumothorax
- **Functional effect:** Loss of alveolar attachments → small airway collapse on exhalation → dynamic hyperinflation → increased residual volume (RV) and total lung capacity (TLC) → barrel chest; diaphragm flattened → mechanical disadvantage → dyspnea

**Pulmonary vasculature:**
- Hypoxic pulmonary vasoconstriction → remodeling of pulmonary arterioles (smooth muscle hypertrophy, intimal thickening) → **pulmonary hypertension** (COPD-PH, WHO Group 3)
- Cor pulmonale: RV hypertrophy and failure in severe COPD-PH (peripheral edema, elevated JVP, right heart strain on EKG)

### COPD inflammatory cells [^vestbo-2013-gold-strategy]

**Macrophages:** Central effectors — cigarette smoke → TLR4/TLR2 → NF-kB → MMP-9/MMP-12 → elastin degradation → emphysema; also defective phagocytosis (efferocytosis) → bacteria not cleared → exacerbations
**Neutrophils:** Elevated in airway lumen during exacerbations; neutrophil elastase overwhelms AAT → matrix destruction; NETosis in COPD exacerbations (bacterial/viral)
**CD8+ T cells (Tc1):** Predominant adaptive immune cell in COPD; release IFN-gamma, perforin → alveolar epithelial damage
**Innate lymphoid cells (ILC2, ILC3):** ILC2 → IL-5/IL-13 in eosinophilic COPD overlap; ILC3 → IL-22 in type 3 COPD responses
**Epithelial cells:** EMT (epithelial-mesenchymal transition) in COPD → fibrosis; loss of ciliary function → mucociliary clearance impairment → microbiome dysbiosis

## Function

### Clinical presentation

**Symptoms:**
- **Dyspnea:** Progressive, "more breathless than same-age peers"; initially on exertion, eventually at rest; **mMRC scale (0-4)**: grade 2 = "walks slower than peers on level ground"
- **Chronic productive cough:** With mucopurulent sputum; "smoker's cough"; worse in morning
- **Wheeze and chest tightness:** Variable
- **Extrapulmonary manifestations:** Skeletal muscle wasting (cachexia) — ubiquitin-proteasome and autophagy-mediated; osteoporosis (smoking, steroids); cardiovascular disease (systemic inflammation, shared risk factors); depression/anxiety; lung cancer (shared smoking risk)

**Physical examination:**
- Barrel chest (increased AP diameter), hyperresonance on percussion
- Reduced breath sounds, prolonged expiratory phase, crackles with secretions
- Accessory muscle use, pursed-lip breathing
- JVP elevation, peripheral edema (cor pulmonale)
- **Clubbing is NOT a feature of COPD** — its presence should prompt evaluation for lung cancer or interstitial lung disease

### Spirometry: GOLD staging [^vestbo-2013-gold-strategy]

**Diagnosis requires post-bronchodilator FEV1/FVC <0.70** (LLN [lower limit of normal] preferred in elderly to reduce over-diagnosis):

| GOLD Grade | FEV1 (% predicted) | Severity |
|:---|:---|:---|
| GOLD 1 | ≥80% | Mild |
| GOLD 2 | 50-79% | Moderate |
| GOLD 3 | 30-49% | Severe |
| GOLD 4 | <30% | Very severe |

**GOLD ABCD Group Assessment (2023 revision — symptoms + exacerbation risk):**
- **Group A (low risk, few symptoms):** GOLD 1-2, 0-1 exacerbations, CAT <10 → SABA PRN or LABA or LAMA
- **Group B (low risk, more symptoms):** GOLD 1-2, 0-1 exacerbations, CAT ≥10 → LABA+LAMA
- **Group E (high exacerbation risk):** GOLD 3-4 or ≥2 exacerbations → LABA+LAMA; add ICS if blood eosinophils ≥300/μL

### COPD exacerbations

**Acute exacerbation of COPD (AECOPD):** Acute worsening of respiratory symptoms beyond normal daily variation requiring a change in medication.

**Triggers:**
- Respiratory viruses (rhinovirus, influenza, RSV): ~50-70% of exacerbations
- Bacteria (H. influenzae, Streptococcus pneumoniae, Moraxella catarrhalis, Pseudomonas in severe COPD): ~25%
- Air pollution, temperature changes

**Impact:** Each exacerbation accelerates lung function decline; hospitalizations associated with 10% in-hospital mortality and 25% 1-year mortality; leading cause of COPD-related healthcare expenditure.

**Treatment of AECOPD:**
- **Bronchodilators:** Short-acting beta-2 agonists (salbutamol/albuterol) + short-acting muscarinic antagonists (ipratropium) via nebulizer or MDI
- **Systemic corticosteroids:** Prednisone 40 mg × 5 days (equivalent to 14 days) — reduces hospitalization duration and treatment failure
- **Antibiotics:** If purulent sputum, elevated CRP, or severity indicates bacterial cause — amoxicillin/clavulanate, azithromycin, or doxycycline (mild-moderate); tailor to local resistance patterns; anti-pseudomonal (ciprofloxacin) for frequent exacerbators with risk factors
- **Oxygen:** Target SpO2 88-92% (avoid over-oxygenation → suppress hypoxic drive in CO2 retainers)
- **Non-invasive ventilation (NIV/BiPAP):** pH <7.35 with PaCO2 >45 mmHg (hypercapnic respiratory failure) → reduces intubation rate and mortality

## Pathology

### COPD and lung cancer

- Smokers with COPD have **3-5× higher lung cancer risk** than smokers without COPD — shared carcinogenic burden AND chronic inflammation → NF-kB/STAT3 → tumor-promoting milieu
- COPD (obstructed airflow) is an independent lung cancer risk factor even after adjusting for smoking (FEV1 as predictor)
- Annual low-dose CT screening (NLST/NELSON criteria) recommended for high-risk smokers — reduces lung cancer mortality by ~20%

### Treatment [^jones-2017-dupilumab-copd]

**Chronic pharmacotherapy:**

*Bronchodilators (first-line):*
- **LABA (long-acting beta-2 agonist):** Salmeterol, formoterol, indacaterol, olodaterol; relax airway smooth muscle; QD or BID
- **LAMA (long-acting muscarinic antagonist):** Tiotropium, umeclidinium, glycopyrronium; block M3 receptors on smooth muscle → bronchodilation + mucus reduction; QD; tiotropium reduces exacerbations ~14%
- **LABA+LAMA combination:** Superior to monotherapy in all GOLD groups B/E; ICS not added unless eosinophils ≥300 or persistent exacerbations
- **Triple therapy (ICS+LABA+LAMA):** IMPACT trial → ICS/UMEC/VI (Trelegy) vs. LABA+LAMA: ORR 21% reduction in moderate/severe exacerbations; lung cancer signal with ICS overuse

*Inhaled corticosteroids (ICS):*
- Added for GOLD E with eosinophils ≥300/μL or repeated exacerbations
- Fluticasone/salmeterol (Advair), budesonide/formoterol (Symbicort)
- Risk of pneumonia (especially fluticasone at high doses in severe COPD)

*Phosphodiesterase-4 (PDE-4) inhibitor:*
- **Roflumilast (Daliresp):** Oral; reduces cyclic AMP degradation → anti-inflammatory; add in severe COPD (FEV1 <50%) with chronic bronchitis and frequent exacerbations; 17% reduction in exacerbations; side effects: nausea, diarrhea, weight loss, depression

*AAT replacement:*
- **Alpha-1 proteinase inhibitor (Prolastin, Zemaira):** Weekly IV infusion for PiZZ AATD with FEV1 35-65% → slows radiological emphysema progression (RAPID trial: CT density loss -1.45 vs -2.19 g/L/year) — expensive, modestly effective

*Oxygen therapy:*
- **Long-term oxygen therapy (LTOT):** PaO2 ≤55 mmHg or SpO2 ≤88% at rest → >15 h/day oxygen use improves survival (MRC and NOTT trials); does NOT improve survival in moderate hypoxemia (LOTT trial, PaO2 56-69)
- Ambulatory oxygen for exercise desaturation

*Biologic therapy (emerging):*
- **Dupilumab (anti-IL-4R-alpha, Dupixent):** Blocks IL-4 and IL-13 signaling; approved 2024 for COPD with type 2 inflammation (blood eosinophils ≥300/μL); BOREAS trial: 34% reduction in moderate/severe exacerbations vs. placebo; first biologic approved for COPD [^jones-2017-dupilumab-copd]

**Pulmonary rehabilitation:**
- Exercise training + education + self-management; 6-8 weeks; most effective intervention for dyspnea, exercise tolerance, and quality of life; does not alter FEV1 decline; under-utilized

**Surgical/interventional:**
- **Lung volume reduction surgery (LVRS):** Remove most diseased emphysema tissue (upper-lobe) → reduces hyperinflation → improves diaphragm mechanics; NETT trial: mortality benefit in upper-lobe predominant emphysema with low exercise capacity
- **Bronchoscopic lung volume reduction (BLVR):** Endobronchial valves (Zephyr) → lobar collapse → reduces hyperinflation; approved for heterogeneous emphysema with intact interlobar fissures; no collateral ventilation required (Chartis measurement)
- **Lung transplantation:** Single or bilateral; reserved for GOLD 4 with poor prognosis; 5-year survival ~55%

## Connections

- `targets` → **[Respiratory System](../respiratory-system/README.md)** — COPD irreversibly destroys alveolar structure (emphysema) and remodels small airways (chronic bronchiolitis), reducing gas exchange surface area and creating fixed airflow obstruction; hyperinflation flattens the diaphragm, worsening the mechanical disadvantage and dyspnea.
- `connects-to` → **[TGF-beta](../../03-molecular/tgf-beta/README.md)** — cigarette smoke-activated macrophages produce TGF-beta1 → subepithelial airway fibrosis and smooth muscle hypertrophy → fixed obstruction; TGF-beta also impairs alveolar epithelial repair and drives EMT, contributing to COPD pathogenesis and lung cancer progression.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — alveolar macrophages are primary COPD effectors; cigarette smoke activates macrophages → MMP-9/MMP-12 secretion → elastin degradation → emphysema; COPD macrophages also fail at bacterial clearance → susceptibility to infectious exacerbations.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — neutrophils accumulate in COPD airways during exacerbations; neutrophil elastase overwhelms AAT → matrix proteolysis; IL-8-driven neutrophil recruitment is the dominant exacerbation amplifier; NETosis releases extracellular traps that contribute to airway inflammation.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — COPD destroys lung architecture: emphysema ruptures alveolar walls reducing gas exchange surface; chronic bronchitis remodels small airways creating fixed obstruction; GOLD spirometric staging (FEV1/FVC <0.7) classifies severity and guides treatment selection.
- `connects-to` → **[Asthma](../asthma/README.md)** — COPD-asthma overlap (ACO) affects ~10-15% of COPD patients with combined fixed obstruction and type 2 eosinophilic inflammation; ACO has higher exacerbation frequency; dupilumab (anti-IL-4Rα) is approved for COPD with eosinophils ≥300/μL.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β amplifies COPD exacerbations: NLRP3 inflammasome activated by smoke particles releases IL-1β → neutrophil and macrophage recruitment → airway inflammation and goblet cell hyperplasia → mucus hypersecretion; IL-1β blockade (canakinumab) is under investigation.
- `connects-to` → **[Cystic Fibrosis](../cystic-fibrosis/README.md)** — COPD and cystic fibrosis are chronic obstructive airway diseases: COPD is acquired emphysema from decades of cigarette smoke, while CF is inherited CFTR failure causing childhood bronchiectasis — yet both end in neutrophilic airway destruction and respiratory failure.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Severe COPD strains the right heart: chronic hypoxia drives pulmonary vasoconstriction and arteriolar remodeling → pulmonary hypertension (WHO Group 3) → right ventricular hypertrophy and failure (cor pulmonale), with raised JVP and peripheral edema.
- `connects-to` → **[Streptococcus pneumoniae](../../../02-pathogen/02-bacteria/streptococcus-pneumoniae/README.md)** — Bacterial infection — often Streptococcus pneumoniae, Haemophilus influenzae, or Moraxella — drives roughly a quarter of COPD exacerbations; purulent sputum guides antibiotics, and pneumococcal vaccination is recommended to help prevent them.
- `connects-to` → **[NSCLC](../nsclc/README.md)** — COPD and lung cancer are smoking's twin diseases that frequently coexist: shared tobacco-driven inflammation, oxidative stress and impaired DNA repair mean COPD independently raises NSCLC risk, COPD limits surgery, and both are screened together with low-dose CT in heavy smokers.
- `connects-to` → **[RSV](../rsv/README.md)** — RSV is an underappreciated driver of COPD exacerbations: it infects airway epithelium to provoke neutrophilic inflammation and bronchospasm, accounting for a notable share of hospitalized flares in older adults; new adult RSV vaccines (Arexvy, Abrysvo) help reduce this burden.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Cigarette smoke is the dominant cause of COPD: inhaled carbon-rich particulates and combustion chemicals trigger protease-antiprotease imbalance and chronic neutrophilic inflammation → emphysema and small-airway fibrosis; cessation is the only intervention that slows decline.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^rabe-2017-gold-copd]: Rabe KF, Watz H. Chronic obstructive pulmonary disease. *Lancet.* 2017;389(10082):1931-1940. [doi:10.1016/S0140-6736(17)31222-9](https://doi.org/10.1016/S0140-6736(17)31222-9) · [PubMed 28513453](https://pubmed.ncbi.nlm.nih.gov/28513453/)
[^vestbo-2013-gold-strategy]: Vestbo J, Hurd SS, Agustí AG, et al. Global strategy for the diagnosis, management, and prevention of chronic obstructive pulmonary disease: GOLD executive summary. *Am J Respir Crit Care Med.* 2013;187(4):347-365. [doi:10.1164/rccm.201204-0596PP](https://doi.org/10.1164/rccm.201204-0596PP) · [PubMed 22878278](https://pubmed.ncbi.nlm.nih.gov/22878278/)
[^jones-2017-dupilumab-copd]: Bhatt SP, Rabe KF, Hanania NA, et al. Dupilumab for COPD with Type 2 Inflammation Indicated by Eosinophil Counts. *N Engl J Med.* 2023;389(3):205-214. [doi:10.1056/NEJMoa2303966](https://doi.org/10.1056/NEJMoa2303966) · [PubMed 37272521](https://pubmed.ncbi.nlm.nih.gov/37272521/)
