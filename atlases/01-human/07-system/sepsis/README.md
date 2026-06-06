---
schema: human-scale-entry/v1
id: sepsis
name: Sepsis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Life-threatening organ dysfunction from dysregulated host response to infection (Sepsis-3: SOFA ≥2). LPS triggers TLR4→NF-κB and NLRP3 inflammasome; cytokine storm causes vasodilation, DIC, and organ failure. Mortality 20–30%; treated with antibiotics and vasopressors."
aliases: ["septicemia", "bacteremia", "septic shock", "SIRS", "systemic inflammatory response syndrome"]
sources:
  - id: singer-2016-sepsis3
    type: peer-reviewed
    cite: "Singer M, Deutschman CS, Seymour CW, et al. The Third International Consensus Definitions for Sepsis and Septic Shock (Sepsis-3). JAMA. 2016;315(8):801-810."
    doi: "10.1001/jama.2016.0287"
    pmid: "26903338"
    url: "https://doi.org/10.1001/jama.2016.0287"
  - id: vanderpoll-2017-sepsis-immunopathology
    type: peer-reviewed
    cite: "van der Poll T, van de Veerdonk FL, Scicluna BP, Netea MG. The immunopathology of sepsis and potential therapeutic targets. Nat Rev Immunol. 2017;17(7):407-420."
    doi: "10.1038/nri.2017.36"
    pmid: "28436424"
    url: "https://doi.org/10.1038/nri.2017.36"
  - id: evans-2021-surviving-sepsis
    type: peer-reviewed
    cite: "Evans L, Rhodes A, Alhazzani W, et al. Surviving Sepsis Campaign: International Guidelines for Management of Sepsis and Septic Shock 2021. Intensive Care Med. 2021;47(11):1181-1247."
    doi: "10.1007/s00134-021-06506-y"
    pmid: "34599691"
    url: "https://doi.org/10.1007/s00134-021-06506-y"
cross_links:
  - target: 01-human/07-system/cytokine-storm
    relation: connects-to
    note: "Severe sepsis can evolve into cytokine storm; TNF-α, IL-1β, IL-6, and HMGB1 drive vascular leak, DIC, and multi-organ failure; overlap with macrophage activation syndrome (MAS) and HLH makes distinguishing sepsis from primary hyperinflammation difficult."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "LPS and bacterial DAMPs activate NLRP3 inflammasome in macrophages → caspase-1 → IL-1β/IL-18 and pyroptotic cell death → amplify the septic inflammatory cascade; NLRP3 inhibition (MCC950) attenuates organ injury in preclinical sepsis models."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "TLR4 (LPS) and TLR2 (lipoteichoic acid) signal via MyD88/TRIF → IRAK4→TRAF6→TAK1→IKK → NF-κB nuclear translocation → TNF-α, IL-1β, IL-6, iNOS, COX-2; NF-κB is the master transcription factor of the innate immune activation in gram-negative and gram-positive sepsis."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "TNF-α is an early dominant mediator of septic shock; TLR4 → NF-κB → rapid TNF-α release from macrophages → iNOS-mediated NO → vasodilation → distributive shock; despite strong preclinical rationale, anti-TNF therapy has consistently failed to improve sepsis survival in RCTs."
---

# Sepsis

## Overview

**Sepsis** is a life-threatening syndrome of **organ dysfunction caused by a dysregulated host response to infection** — defined by the **Sepsis-3 consensus** (Singer et al., 2016) as a suspected or confirmed infection plus an acute increase in the **SOFA (Sequential Organ Failure Assessment) score ≥2** [^singer-2016-sepsis3]. The definition deliberately shifted from the earlier SIRS (systemic inflammatory response syndrome) criteria, which were non-specific and did not require organ dysfunction, recognizing that the pathological hallmark of sepsis is **aberrant immune activation causing collateral organ damage**, not merely systemic inflammation.

**Septic shock** is the most severe form: sepsis plus vasopressor requirement to maintain mean arterial pressure ≥65 mmHg plus serum lactate >2 mmol/L (despite adequate volume resuscitation) — in-hospital mortality ~40%.

**Epidemiology:**
- ~49 million cases of sepsis globally per year; ~11 million deaths (~20% of all global deaths; Global Burden of Disease 2017)
- In ICUs, sepsis is the leading cause of mortality in high-income countries
- Disproportionate burden in low- and middle-income countries due to limited diagnostic and therapeutic resources
- Risk factors: extremes of age, immunocompromise, cancer, CKD, diabetes, prior hospitalization, invasive devices

**Common causative organisms:**
- Gram-negative bacteria (E. coli, Klebsiella, Pseudomonas, Acinetobacter): LPS-mediated TLR4 activation
- Gram-positive bacteria (S. aureus, Streptococcus, Enterococcus): lipoteichoic acid (TLR2), peptidoglycan, superantigens (TCR Vβ cross-linking → massive cytokine release)
- Fungi (Candida, Aspergillus): typically in immunocompromised hosts
- Viral (COVID-19, influenza): cytokine storm with features overlapping bacterial sepsis

## Structure

### Sepsis as a systemic syndrome: organ-by-organ dysfunction

Sepsis is not localized to one system — it manifests as dysfunction across multiple organs simultaneously, scored by SOFA:

| SOFA Component | Measurement | Score 0-4 based on severity |
|:---|:---|:---|
| Respiratory | PaO₂/FiO₂ ratio | Normal >400 → severe ARDS <100 |
| Coagulation | Platelet count | Normal >150K → <50K |
| Liver | Bilirubin | <1.2 → ≥12 mg/dL |
| Cardiovascular | MAP or vasopressors | No vasopressors → high-dose dual vasopressors |
| CNS | GCS | 15 → <6 |
| Renal | Creatinine or urine output | <1.2 mg/dL → ≥5 mg/dL or <200 mL/day |

**Key pathological processes:**

1. **Septic cardiomyopathy:** Cytokines (TNF-α, IL-1β, NO) suppress myocardial contractility → biventricular dysfunction; usually reversible if patient survives
2. **Septic encephalopathy:** BBB disruption (NF-κB, COX-2, iNOS in brain endothelium), neuroinflammation, cerebral hypoperfusion → delirium (most common ICU complication); long-term cognitive impairment in survivors
3. **Acute Kidney Injury (AKI):** Renal hypoperfusion + direct cytokine toxicity + tubular apoptosis → oliguric AKI; renal replacement therapy required in ~5% of sepsis patients
4. **Disseminated Intravascular Coagulation (DIC):** Endothelial injury + thrombin generation + consumption of platelets and coagulation factors → simultaneous microvascular thrombosis and hemorrhage

## Function

### Pathophysiology: the immune cascade [^vanderpoll-2017-sepsis-immunopathology]

**Phase 1 — Pattern recognition and innate activation:**
- Bacterial PAMPs (pathogen-associated molecular patterns): LPS (gram-negative), LTA and peptidoglycan (gram-positive), flagellin, bacterial DNA (CpG)
- Host DAMPs (damage-associated molecular patterns): HMGB1 (released by necrotic cells), mitochondrial DNA, ATP, heat shock proteins — released as organ injury progresses
- **TLR4 (LPS receptor):** LPS → CD14/MD-2/TLR4 complex → MyD88→IRAK4→TRAF6→TAK1→IKK → NF-κB (TNF-α, IL-1β, IL-6, IL-8, MCP-1, iNOS, COX-2) and TRIF→IRF3 → IFN-β
- **TLR2 (gram-positive):** LTA → heterodimer TLR2/1 or TLR2/6 → MyD88 → NF-κB (same cytokine program)

**Phase 2 — Cytokine storm amplification:**
- TNF-α (first peak, 1-2 hours): Primary mediator of cardiovascular collapse; causes iNOS induction in endothelium and smooth muscle → NO → vasodilation → distributive shock; also induces endothelial E-selectin, VCAM-1 → neutrophil adhesion → tissue damage
- IL-1β (NLRP3 inflammasome-derived): Amplifies TNF-α effects; promotes tissue factor expression → DIC; pyrogenic
- IL-6 (12-24 hours): Acute phase response (liver: CRP, fibrinogen, SAA); drives Th17 differentiation; best temporal correlate of sepsis mortality
- **HMGB1 (late, 16-32 hours):** Alarmin released from necrotic cells; sustains late-phase inflammation; explains why late anti-inflammatory interventions fail

**Phase 3 — Immune paralysis (late phase):**
- Paradoxically, most late sepsis deaths occur in an immunosuppressed state — "immunoparalysis":
- Lymphocyte apoptosis (massive T and B cell death via mitochondrial apoptosis, FasL/Fas, and BCL-2-dependent pathways) → lymphopenia
- Monocyte deactivation: reduced HLA-DR expression → impaired antigen presentation → secondary infections
- NK cell and NK-T cell exhaustion
- PD-1/PD-L1 upregulation on T cells → functional exhaustion (checkpoint therapy [anti-PD-1] in clinical trials for sepsis immunoparalysis)

### Coagulation dysfunction in sepsis: DIC

1. Endothelial injury + inflammatory cytokines → **tissue factor (TF, FIII) upregulation** on monocytes and endothelial cells → activates extrinsic coagulation cascade → thrombin burst
2. Thrombin → fibrinogen → fibrin → microvascular thrombi (consume platelets, FIII, FV, FVIII, fibrinogen) → thrombocytopenia + prolonged PT/aPTT + low fibrinogen + high D-dimer
3. Plasminogen activator inhibitor-1 (PAI-1) upregulated by cytokines → impairs fibrinolysis → fibrin clots persist → microangiopathy → AKI, ARDS, gut ischemia
4. Simultaneous hemorrhage from consumption of factors → bleeding complications

**DIC management:** Treat underlying sepsis; platelet/FFP transfusion for active bleeding or prophylaxis at <10K or <50K (procedural); recombinant thrombomodulin (approved in Japan) — modest mortality benefit in DIC-complicated sepsis.

## Pathology

### Mortality predictors and risk stratification

- **Lactate >4 mmol/L:** Tissue hypoperfusion marker; 3-hour lactate >4 = septic shock mortality 40-50%
- **SOFA score:** 1-point increase = ~10% increase in ICU mortality
- **Procalcitonin (PCT):** Reflects bacterial translocation and cytokine-driven hepatic synthesis; PCT-guided antibiotic de-escalation reduces antibiotic exposure
- **Low monocyte HLA-DR (<30%):** Marks immunoparalysis → risk of secondary nosocomial infection

### Treatment: Surviving Sepsis Campaign 2021 [^evans-2021-surviving-sepsis]

**Hour-1 bundle (targets to initiate within 1 hour):**
1. **Measure lactate** (repeat if initial >2 mmol/L)
2. **Blood cultures** before antibiotics (≥2 sets; do not delay antibiotics >45 minutes for cultures)
3. **Broad-spectrum antibiotics within 1 hour** of sepsis recognition — every hour of antibiotic delay increases mortality by ~7%
4. **30 mL/kg IV crystalloid** bolus if hypotension or lactate ≥4
5. **Vasopressors** (norepinephrine first-line) if MAP <65 during/after fluid resuscitation

**Subsequent management:**
- **Source control:** Drainage of abscess, catheter removal, debridement within 6-12 hours
- **Norepinephrine:** First-line vasopressor; targets MAP ≥65; add vasopressin (0.03 U/min, spares norepinephrine dose) for refractory shock
- **Corticosteroids:** Hydrocortisone 200 mg/day IV for vasopressor-refractory septic shock (APROCCHSS/ADRENAL trials — reduces shock duration, modest impact on mortality)
- **Glucose control:** Target 140-180 mg/dL (NICE-SUGAR trial: tight control 80-110 mg/dL worsened survival)
- **Lung-protective ventilation:** Tidal volume ≤6 mL/kg IBW, PEEP as per ARDSnet protocol for sepsis-associated ARDS

**Failed immunomodulatory strategies:**
- Anti-TNF-α (filgrastim, lenercept, afelimomab): multiple Phase III trials — no survival benefit
- Recombinant IL-1ra (anakinra): Phase III negative; promising in macrophage activation syndrome-associated sepsis
- Activated protein C (drotrecogin alfa): approved 2001, withdrawn 2011 (PROWESS-SHOCK: no benefit, bleeding risk)
- Anti-HMGB1: preclinical only; no approved therapy
- IL-7 (reverse immunoparalysis): Phase II positive signals — ongoing trials

## Connections

- `connects-to` → **[Cytokine Storm](../cytokine-storm/README.md)** — severe sepsis can evolve into cytokine storm with massive TNF-α, IL-1β, IL-6, and HMGB1 release; DIC, vascular leak, and multi-organ failure overlap with macrophage activation syndrome; pathological immune amplification is the shared mechanism.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — LPS and bacterial DAMPs activate NLRP3 in macrophages → IL-1β/IL-18 secretion and pyroptosis → amplify the septic inflammatory cascade; NLRP3 inhibitors are in preclinical development for sepsis.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — TLR4→MyD88→NF-κB is the master signaling axis of innate immune activation in sepsis; NF-κB drives all major pro-inflammatory mediators including TNF-α, IL-1β, IL-6, iNOS, and COX-2.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — TNF-α is the dominant early mediator of septic cardiovascular collapse; despite strong mechanistic rationale, anti-TNF therapies have failed in sepsis RCTs — demonstrating that blocking individual cytokines cannot overcome the redundant inflammatory cascade of systemic sepsis.

[^singer-2016-sepsis3]: Singer M, Deutschman CS, Seymour CW, et al. The Third International Consensus Definitions for Sepsis and Septic Shock (Sepsis-3). *JAMA.* 2016;315(8):801-810. [doi:10.1001/jama.2016.0287](https://doi.org/10.1001/jama.2016.0287) · [PubMed 26903338](https://pubmed.ncbi.nlm.nih.gov/26903338/)
[^vanderpoll-2017-sepsis-immunopathology]: van der Poll T, van de Veerdonk FL, Scicluna BP, Netea MG. The immunopathology of sepsis and potential therapeutic targets. *Nat Rev Immunol.* 2017;17(7):407-420. [doi:10.1038/nri.2017.36](https://doi.org/10.1038/nri.2017.36) · [PubMed 28436424](https://pubmed.ncbi.nlm.nih.gov/28436424/)
[^evans-2021-surviving-sepsis]: Evans L, Rhodes A, Alhazzani W, et al. Surviving Sepsis Campaign: International Guidelines for Management of Sepsis and Septic Shock 2021. *Intensive Care Med.* 2021;47(11):1181-1247. [doi:10.1007/s00134-021-06506-y](https://doi.org/10.1007/s00134-021-06506-y) · [PubMed 34599691](https://pubmed.ncbi.nlm.nih.gov/34599691/)
