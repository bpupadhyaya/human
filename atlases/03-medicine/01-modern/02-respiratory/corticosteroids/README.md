---
schema: medicine-entry/v1
id: corticosteroids
name: Corticosteroids
atlas: 03-medicine
scale: 01-modern
status: draft
last_reviewed: 2026-06-04
summary: "Glucocorticoid receptor agonists; most potent anti-inflammatory class. Suppress NF-κB/AP-1 → ↓ cytokines, eosinophils, permeability. ICS for asthma/COPD; systemic for acute asthma, ARDS, anaphylaxis. RECOVERY trial: dexamethasone 6 mg/d cut COVID-19 ventilator mortality 36%."
aliases: ["glucocorticoids", "steroids", "corticosteroids", "ICS", "inhaled corticosteroids", "systemic corticosteroids", "prednisolone", "dexamethasone", "budesonide", "fluticasone", "methylprednisolone", "hydrocortisone"]
sources:
  - id: hench-1949-cortisone
    type: peer-reviewed
    cite: "Hench PS, Kendall EC, Slocumb CH, Polley HF. The effect of a hormone of the adrenal cortex (17-hydroxy-11-dehydrocorticosterone: compound E) and of pituitary adrenocortical hormone in arthritis. Proc Staff Meet Mayo Clin. 1949;24(8):181-97."
    pmid: "18134783"
    url: "https://pubmed.ncbi.nlm.nih.gov/18134783/"
  - id: gina-2023-asthma-guidelines
    type: clinical-guideline
    cite: "Global Initiative for Asthma. Global Strategy for Asthma Management and Prevention. GINA; 2023."
    url: "https://ginasthma.org/2023-gina-main-report/"
    accessed: "2026-06-04"
  - id: recovery-2021-dexamethasone
    type: peer-reviewed
    cite: "RECOVERY Collaborative Group. Dexamethasone in Hospitalized Patients with Covid-19. N Engl J Med. 2021;384(8):693-704."
    doi: "10.1056/NEJMoa2021436"
    pmid: "32678530"
    url: "https://doi.org/10.1056/NEJMoa2021436"
  - id: gold-2023-copd-guidelines
    type: clinical-guideline
    cite: "Global Initiative for Chronic Obstructive Lung Disease. Global Strategy for the Diagnosis, Management, and Prevention of COPD. GOLD; 2023."
    url: "https://goldcopd.org/2023-gold-report-2/"
    accessed: "2026-06-04"
cross_links:
  - target: 01-human/07-system/respiratory-system
    relation: treats
    evidence: gina-2023-asthma-guidelines
    note: "Inhaled corticosteroids (ICS) are the cornerstone of persistent asthma management (GINA Steps 2–5); suppression of airway eosinophil recruitment, mast cell degranulation, mucus secretion, and bronchial hyperresponsiveness reduces exacerbation frequency by 50–60%. Systemic corticosteroids are first-line for acute severe asthma and COPD exacerbations."
  - target: 01-human/03-molecular/il-6
    relation: modulates
    evidence: recovery-2021-dexamethasone
    note: "Corticosteroids suppress IL-6 transcription via GR-mediated transrepression of NF-κB and AP-1 at the IL-6 promoter; dexamethasone in the RECOVERY trial reduced mortality in ventilated COVID-19 patients by 36%, with the benefit attributable in part to suppression of IL-6-driven hyperinflammation."
  - target: 01-human/06-organ/ards
    relation: treats
    note: "Dexamethasone (DEXA-ARDS trial) 20 mg IV × 5d then 10 mg × 5d increased ventilator-free days and reduced 60-day mortality (29.3% vs 44.8%); methylprednisolone reduces ARDS duration; dexamethasone is the most evidence-based corticosteroid for ARDS."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: treats
    note: "Prednisolone is bridge therapy in RA (5–10 mg/day) while DMARDs take effect (8–12 weeks latency); reduces radiographic progression in early RA (COBRA, BeSt trials); long-term use requires osteoporosis prophylaxis (bisphosphonates + calcium/vitamin D)."
  - target: 01-human/07-system/covid-19-disease
    relation: treats
    evidence: recovery-2021-dexamethasone
    note: "RECOVERY trial (2021): dexamethasone 6 mg/d × 10 days; 36% mortality reduction in mechanically ventilated COVID-19 (RR 0.64); 18% reduction in those requiring oxygen only; no benefit and possible harm in patients not requiring supplemental oxygen."
---

# Corticosteroids

## Overview

**Corticosteroids** (glucocorticoids used clinically) are **steroid hormones that bind and activate the glucocorticoid receptor (GR, NR3C1)**, producing the most potent anti-inflammatory effect of any drug class in clinical medicine. The class encompasses both **endogenous cortisol** (hydrocortisone) and a large range of synthetic derivatives with enhanced anti-inflammatory potency, altered pharmacokinetics, and reduced mineralocorticoid activity.

The therapeutic era began in 1948 when Philip Hench administered **compound E** (cortisone) to a bedridden patient with severe rheumatoid arthritis — within two days she could walk; within weeks, her debilitating disease was in remission [^hench-1949-cortisone]. Hench, Kendall, and Reichstein shared the 1950 Nobel Prize in Physiology or Medicine for this work.

Corticosteroids are used across virtually every medical specialty:
- **Pulmonology**: Inhaled corticosteroids (ICS) — budesonide, fluticasone, beclomethasone — are Step 2 and above therapy for asthma, and systemic steroids are first-line for COPD exacerbations and severe asthma
- **Critical care**: Dexamethasone, methylprednisolone — ARDS, septic shock, COVID-19
- **Rheumatology**: Prednisolone/prednisone — RA, SLE, vasculitis
- **Allergy/emergency**: Hydrocortisone/methylprednisolone — anaphylaxis, angioedema
- **Oncology/hematology**: Dexamethasone — multiple myeloma, lymphoma, anti-emesis

## Mechanism

**Genomic (primary) mechanism:**
1. Diffusion through cell membrane → cytoplasmic GR binding → GR–ligand complex dissociates from heat-shock protein chaperones (HSP90)
2. GR homodimer translocates to nucleus; binds **glucocorticoid response elements (GRE)** in DNA → **transactivation** of anti-inflammatory genes: IκBα (NF-κB inhibitor), GILZ, Annexin-1, MKP-1 (inactivates MAPK)
3. GR monomer tethers directly to **NF-κB p65** and **AP-1 (c-Fos/c-Jun)** → **transrepression** — prevents binding to pro-inflammatory gene promoters → ↓ TNF-α, IL-1β, IL-6, IL-8, COX-2, iNOS, VCAM-1, ICAM-1

**Non-genomic (rapid) mechanism:**
- Minutes timescale; GR membrane-associated signaling; cAMP elevation; relevant for emergency bronchodilator augmentation and acute anti-edema effects in anaphylaxis

**Net pharmacological effects:**
- ↓ Eosinophil survival and airway eosinophilia
- ↓ Mast cell mediator release
- ↓ Dendritic cell antigen presentation
- ↓ Cytokine storm (TNF-α, IL-1β, IL-6, IL-8 synthesis)
- ↑ Airway β₂-adrenergic receptor expression (synergy with β₂-agonists)
- ↓ Vascular permeability (reduces mucosal edema, airway secretions)

## Clinical Use

**Inhaled corticosteroids (asthma):**
- First-line maintenance for persistent asthma (GINA Steps 2–5) [^gina-2023-asthma-guidelines]
- Reduce exacerbation rate 50–60%, hospitalizations 80%, and near-fatal asthma
- Key agents: Budesonide, fluticasone propionate/furoate, beclomethasone, mometasone, ciclesonide
- Doses: Low, medium, high (by agent-specific tables); high doses approach systemic equivalence

**Systemic corticosteroids (acute severe asthma/COPD):**
- Oral prednisolone 30–40 mg/day × 5–7 days for COPD exacerbation (GOLD 2023) [^gold-2023-copd-guidelines]
- IV methylprednisolone for hospitalized severe asthma
- Reduce treatment failure, hospitalization duration, relapse rate

**Dexamethasone in COVID-19 / ARDS (RECOVERY trial):**
- Dexamethasone 6 mg/day × 10 days reduced 28-day mortality by **36% in mechanically ventilated** COVID-19 patients (RR 0.64; 95% CI 0.51–0.81) and by 18% in those requiring oxygen only [^recovery-2021-dexamethasone]
- No benefit (possible harm) in patients not requiring oxygen — benefit restricted to hyperinflammatory phase
- Effect is the clearest landmark evidence that corticosteroids save lives in severe viral pneumonia when inflammatory pathology dominates

## Evidence

| Indication | Trial / Guideline | Key finding |
|:---|:---|:---|
| Asthma maintenance | GINA 2023 [^gina-2023-asthma-guidelines] | ICS Step 2+ reduces exacerbations 50–60% |
| COPD exacerbation | GOLD 2023 [^gold-2023-copd-guidelines] | Prednisolone 40 mg/d × 5d: fewer treatment failures, shorter stay |
| COVID-19 / ARDS | RECOVERY 2021 [^recovery-2021-dexamethasone] | Dexamethasone 6 mg/d: −36% 28d mortality in ventilated patients |
| Asthma emergency | Standard of care | IV hydrocortisone / oral prednisolone: reduces relapse after ED discharge |

## Connections

- **Treats** → [Respiratory System](../../../../../01-human/07-system/respiratory-system/README.md): ICS are the cornerstone pharmacotherapy for persistent asthma; systemic corticosteroids are first-line for COPD exacerbations, acute severe asthma, and inflammatory lung disease.
- **Modulates** → [Interleukin-6](../../../../../01-human/03-molecular/il-6/README.md): GR-mediated NF-κB transrepression suppresses IL-6 transcription; this mechanism underlies the mortality benefit in COVID-19 and is central to corticosteroid action in cytokine-driven lung injury.
- **Treats** → [ARDS](../../../../../01-human/06-organ/ards/README.md): Dexamethasone (DEXA-ARDS trial) 20 mg IV × 5d then 10 mg × 5d increased ventilator-free days and reduced 60-day mortality (29.3% vs 44.8%); most evidence-based corticosteroid for ARDS.
- **Treats** → [Rheumatoid Arthritis](../../../../../01-human/07-system/rheumatoid-arthritis/README.md): Prednisolone bridge therapy (5–10 mg/day) while DMARDs take effect (8–12 weeks latency); reduces radiographic progression in early RA; long-term use requires osteoporosis prophylaxis.
- **Treats** → [COVID-19 Disease](../../../../../01-human/07-system/covid-19-disease/README.md): RECOVERY trial (2021): dexamethasone 6 mg/d × 10 days; 36% mortality reduction in mechanically ventilated patients (RR 0.64); 18% reduction in oxygen-requiring patients.

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
