---
schema: human-scale-entry/v1
id: rsv
name: RSV
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "RSV (pneumovirus; negative-sense ssRNA) is the leading cause of infant bronchiolitis and severe LRTI in elderly/immunocompromised; NS1/NS2 block MAVS/IFN-β; nirsevimab (anti-F mAb) prevents severe infant RSV; mRNA-1345 (Abrysvo) and mResvia approved 2023 for adults 60+."
aliases: ["RSV", "respiratory syncytial virus", "RSV bronchiolitis", "infant RSV", "nirsevimab", "Beyfortus", "palivizumab", "Synagis", "Abrysvo", "mResvia", "mRNA-1345", "RSV-A", "RSV-B", "RSV pneumonia", "pneumovirus", "RSV vaccine"]
sources:
  - id: shi-2017-rsv-global-burden
    type: peer-reviewed
    cite: "Shi T, McAllister DA, O'Brien KL, et al. Global, regional, and national disease burden estimates of acute lower respiratory infections due to respiratory syncytial virus in young children in 2015: a systematic review and modelling study. Lancet. 2017;390(10098):946-958."
    doi: "10.1016/S0140-6736(17)30938-8"
    pmid: "28689664"
    url: "https://doi.org/10.1016/S0140-6736(17)30938-8"
    accessed: "2026-06-08"
  - id: hammitt-2022-nirsevimab-trial
    type: peer-reviewed
    cite: "Hammitt LL, Dagan R, Yuan Y, et al. Nirsevimab for Prevention of RSV in Healthy Late-Preterm and Term Infants. N Engl J Med. 2022;386(9):837-846."
    doi: "10.1056/NEJMoa2110275"
    pmid: "35196424"
    url: "https://doi.org/10.1056/NEJMoa2110275"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/rsv-f-protein
    relation: connects-to
    note: "RSV F (fusion) protein mediates attachment and viral-host membrane fusion → syncytium formation; prefusion F (site Ø) is the primary neutralizing epitope; nirsevimab (site Ø mAb) and mRNA vaccines (mRNA-1345) target prefusion F for RSV prevention."
  - target: 01-human/03-molecular/mavs
    relation: connects-to
    note: "RSV NS1 degrades TRIM25 → prevents RIG-I K63-ubiquitination → impairs RIG-I/MAVS signaling; NS2 blocks STAT2 → suppresses ISGs; NS1+NS2 blunt IFN-β → RSV replicates in immunocompetent airways; IFN-λ (type III IFN) is the dominant innate mucosal antiviral defense against RSV."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "RSV airway epithelial infection → IL-33 release (DAMP) from epithelial nuclei → ST2+ ILC2 activation → IL-4/IL-5/IL-13 → type 2 inflammation, eosinophilia, mucus; RSV-IL-33 axis drives early-life wheeze and subsequent asthma sensitization."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "RSV-induced airway epithelial damage → TSLP release → TSLP receptor on ILC2/basophils → IL-4/IL-13 → Th2 polarization and IgE production; neonatal TSLP sensitization after RSV infection may explain the RSV-asthma epidemiological link in childhood; tezepelumab blocks TSLP."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "RSV NS1/NS2 cooperatively block type I IFN: NS1 targets TRIM25/IRF3; NS2 prevents STAT2 nuclear translocation → ISG suppression; IFN-λ (type III) dominates innate mucosal defense against RSV; preterm infants with immature IFN response have more severe RSV bronchiolitis."
  - target: 02-pathogen/01-viruses/respiratory-syncytial-virus
    relation: connects-to
    note: "Respiratory syncytial virus, a negative-sense RNA pneumovirus, fuses airway cells into syncytia and blunts interferon with NS1/NS2; it reinfects throughout life because the G protein varies and memory is short, yet prefusion-F antibodies and vaccines now prevent severe disease."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "RSV is the top cause of infant bronchiolitis and a major cause of pneumonia in the elderly and immunocompromised: it infects ciliated airway epithelium, sloughing cells and plugging small airways with mucus → air trapping, hypoxia, and wheeze; care is supportive."
  - target: 01-human/07-system/asthma
    relation: connects-to
    note: "Severe RSV bronchiolitis in infancy is the strongest environmental risk factor for childhood asthma: epithelial damage releases IL-33 and TSLP that activate ILC2s toward type-2 inflammation, biasing the developing airway toward allergic sensitization and recurrent wheeze."
---

# RSV

## Overview

**Respiratory syncytial virus (RSV)** is a non-segmented, negative-sense single-stranded RNA virus of the family *Pneumoviridae* (genus *Orthopneumovirus*), formerly classified within the family *Paramyxoviridae*. RSV is the **leading cause of acute lower respiratory tract illness (LRTI) in young children worldwide** — the 2017 Global Burden of Disease analysis estimated RSV causes ~33 million LRTI episodes in children <5 years annually, accounting for approximately 100,000 deaths, primarily in low- and middle-income countries [^shi-2017-rsv-global-burden]. RSV also causes significant severe disease in elderly adults (>60 years) and immunocompromised patients.

Two major subtypes exist — **RSV-A** and **RSV-B** — distinguished primarily by sequence variation in the attachment glycoprotein G. Both subtypes co-circulate, with RSV-A tending to dominate in epidemic years with higher hospitalization rates. Nearly all children are infected with RSV by age 2, and reinfections occur throughout life due to incomplete immunological memory, particularly against the highly variable G protein.

The RSV vaccine story is one of the most dramatic in vaccinology — from the tragic **formalin-inactivated RSV (FI-RSV) vaccine failure** of the 1960s (vaccine-enhanced disease, VED, with eosinophilic immunopathology on natural RSV exposure) to the **2023 vaccine revolution** when three separate RSV vaccines targeting prefusion F protein were approved within months: Abrysvo (Pfizer, adults + maternal), Arexvy (GSK, adults), and mResvia (Moderna, mRNA-1345, adults 60+). Simultaneously, nirsevimab (Beyfortus) — a single-dose long-acting anti-F monoclonal antibody — transformed infant RSV prophylaxis.

**Clinical spectrum:**
- **Infants/toddlers**: Upper respiratory symptoms → bronchiolitis (expiratory wheeze, hyperinflation, tachypnea, hypoxia, feeding difficulty); most common cause of infant hospitalization in high-income countries; ~100,000 US hospitalizations/year in infants <12 months
- **Older children**: Cold-like illness; RSV is the most common cause of childhood wheezing illness
- **Elderly adults (60+)**: Pneumonia, exacerbations of COPD/CHF; ~14,000 deaths/year in US adults ≥65 years
- **Immunocompromised**: Prolonged shedding, high mortality in HSCT recipients (>40% if RSV-pneumonia with respiratory failure); no standard approved therapy

**Risk factors for severe infant RSV:** Prematurity (<29 weeks GA), chronic lung disease of prematurity, congenital heart disease with hemodynamic compromise, severe combined immunodeficiency, neuromuscular disorders, Down syndrome, age <6 weeks

## Structure

### RSV genome and proteins

RSV has a ~15.2 kb negative-sense ssRNA genome encoding **11 proteins** in order: 3′-NS1-NS2-N-P-M-SH-G-F-M2(1 and 2)-L-5′

| Protein | Function |
|---------|----------|
| **NS1** | Non-structural; primary IFN antagonist: degrades TRIM25 (blocks RIG-I ubiquitination); inhibits IRF3 phosphorylation; targets STAT2; suppresses MAVS signaling |
| **NS2** | Non-structural; synergizes with NS1: blocks STAT2 nuclear translocation → ISG suppression; targets RIG-I for proteasomal degradation |
| **N (nucleoprotein)** | Encapsidates genomic RNA → nucleocapsid; essential for replication |
| **P (phosphoprotein)** | L polymerase cofactor; regulatory; scaffold for replication complex |
| **M (matrix protein)** | Virion assembly and budding from cell surface |
| **SH (small hydrophobic)** | Viroporin (ion channel); blocks TNF-α-mediated apoptosis; promotes viral release |
| **G (attachment glycoprotein)** | Attachment to CX3CR1 (fractalkine receptor) on airway epithelium; highly variable sequence (immune evasion); acts as CX3CL1 mimic → misdirects NK cells |
| **F (fusion protein)** | Viral-cell membrane fusion → viral entry; syncytium formation; prefusion F (site Ø) is the dominant neutralizing epitope; target of nirsevimab and all approved RSV vaccines |
| **M2-1** | Transcription processivity factor |
| **M2-2** | Regulates shift from transcription to replication |
| **L (large protein)** | RNA-dependent RNA polymerase (RdRp) + mRNA capping enzyme |

### RSV entry

1. G protein binds CX3CR1 on airway epithelial cells and ciliated cells; also binds heparan sulfate proteoglycans
2. F protein (prefusion conformation) binds nucleolin and IGFR1 (co-receptors)
3. Viral-host membrane fusion at the cell surface (pH-independent) → nucleocapsid enters cytoplasm
4. Transcription from 3′ end of genome → mRNA synthesis by L/P complex
5. Genomic replication in cytoplasmic inclusion bodies (IBs) — inclusion body factories
6. Assembly at cell membrane → budding

## Function

### Innate immune evasion — NS1/NS2 system

RSV has evolved a two-protein innate immune evasion system unique among pneumoviruses:

**NS1** (targeting RNA sensing):
- Degrades TRIM25 (E3 ubiquitin ligase) via proteasomal pathway → prevents K63-linked ubiquitination of RIG-I CARD (Lys172) → RIG-I cannot activate MAVS
- Directly binds IRF3 → prevents TBK1-mediated IRF3 Ser396 phosphorylation → blocks IFN-β transcription
- Interacts with STAT2 at nuclear pore → reduces STAT2 function

**NS2** (targeting IFN signaling):
- Binds STAT2 and blocks its nuclear translocation after IFN-α/β stimulation → ISG expression suppressed
- Targets RIG-I for proteasomal degradation (some strains)
- NS1+NS2 together reduce IFN-β production ~10-fold and IFN-α/β signaling ~5-fold

**Net effect**: RSV can replicate in immunocompetent airway epithelium despite RIG-I/MAVS and type I IFN being present — the dominant innate defense against RSV is **IFN-λ (type III)** at mucosal surfaces, which is less impaired by NS1/NS2 and represents the main protection in immunocompetent adults.

### Type 2 immunopathology — RSV and asthma

RSV causes not just acute bronchiolitis but also sensitizes the airway toward type 2 (allergic) inflammation:

1. **Airway epithelial damage** → IL-33 (from epithelial nuclei) and TSLP → "alarm signals"
2. **IL-33 → ST2+ ILC2** → IL-4, IL-5, IL-13 → eosinophilia, mucus, airway hyperresponsiveness (AHR)
3. **TSLP → TSLP receptor on ILC2/basophils** → Th2 polarization, IgE class switching
4. **Th2 sensitization**: Neonatal RSV exposure during a critical window may bias immunity toward Th2 → risk of subsequent asthma (epidemiological association: RSV bronchiolitis in infancy is the strongest environmental risk factor for childhood asthma)
5. **G protein CX3CL1 mimicry** → attracts CX3CR1+ NK cells and T cells → misdirects innate response → promotes type 2 bias

**FI-RSV VED mechanism (historical lesson)**: Formalin destroyed prefusion F → only post-fusion F antibodies made (poor neutralization) → also primed Th2-biased immune response → on natural RSV exposure, Th2-mediated eosinophilic immunopathology occurred; no cytotoxic T cell response → enhanced disease. This explains why prefusion F stabilization is essential for safe RSV vaccines.

### Adaptive immunity and RSV-specific T cells

- Primary RSV infection in infants generates RSV-specific CD8+ T cells (CTLs) that clear infection
- However, RSV suppresses T cell responses: NS1/NS2 reduce DC function and IL-12 production
- RSV-specific memory T cells in adults are short-lived and wane rapidly → susceptibility to reinfection
- CD8+ T cells against conserved F protein epitopes provide better cross-subtype protection than anti-G responses
- In immunocompromised hosts: RSV-specific T cells critical; absence → prolonged shedding, high mortality

## Pathology

### Bronchiolitis pathophysiology

In infants, RSV bronchiolitis follows a characteristic pattern:
1. Infection of ciliated airway epithelium → loss of ciliary function → mucus pooling → peribronchiolar lymphocytic infiltrate
2. Syncytium formation (F protein-mediated) → large multinucleated cells → epithelial sloughing → airway debris
3. Submucosal edema + mucus plugs → small airway obstruction → air trapping → hyperinflation
4. Ventilation-perfusion mismatch → hypoxemia → respiratory distress

Radiological findings: Hyperinflation, peribronchial thickening, occasional atelectasis (right upper lobe common)

### Diagnosis

- **Clinical** (in infants <2 years during RSV season): No testing needed; classic presentation
- **Rapid antigen test (RAT)**: Point-of-care; ~80% sensitivity; useful in hospital triage
- **RSV PCR (multiplex respiratory panel)**: Gold standard; >95% sensitivity; preferred for immunocompromised and adults
- **RSV culture**: Research use; not clinical standard

### Treatment

**No approved antiviral therapy for standard RSV:**
- **Supportive care**: Primary treatment for bronchiolitis; oxygen, high-flow nasal cannula (HFNC) for hypoxia; minimal suctioning; feeding support (NG tube if needed)
- **Ribavirin** (aerosolized): FDA-approved for severe RSV in immunocompromised; evidence weak; used selectively (HSCT, lung transplant with respiratory failure)
- **IVIG/palivizumab IV**: Not recommended therapeutically
- **Bronchodilators (albuterol, epinephrine)**: Not recommended in bronchiolitis (no consistent benefit; 2014 AAP guidelines)
- **Corticosteroids**: Not recommended in bronchiolitis (multiple RCTs negative)
- **HFNC vs. standard O2**: HFNC preferred for moderate-severe bronchiolitis with hypoxia; reduces escalation to PICU

### Prevention — the 2023 paradigm shift

#### Nirsevimab (Beyfortus; AstraZeneca/Sanofi)

- **Class**: Long-acting monoclonal antibody targeting prefusion RSV F protein at site Ø
- **Half-life extended**: YTE (M252Y/S254T/T256E) Fc mutations → ~70-day half-life vs. ~20 days for palivizumab → single dose provides 5-month protection (one RSV season)
- **MELODY trial (healthy infants)**: 74.5% efficacy against medically attended RSV LRTI
- **NIRSEVIMAB-MEDICALLY ATTENDED trial (high-risk infants)**: 70.1% efficacy; **77% against RSV hospitalization**
- **FDA approval**: 2023; universal recommendation for all infants <8 months entering first RSV season (2023 ACIP guidance)
- **Replaces palivizumab**: Palivizumab (site II mAb; monthly injections) was limited to high-risk infants and required 5 monthly doses; nirsevimab covers all infants with one dose

#### RSV vaccines approved in 2023

| Vaccine | Platform | Approval | Population | Efficacy (LRTI) |
|---------|---------|----------|-----------|-----------------|
| **Abrysvo (Pfizer RSVpreF)** | Bivalent protein subunit (RSV-A + RSV-B preF) | May 2023 | Adults 60+; maternal (Aug 2023) | 88.9% vs. severe LRTI (adults); 82% vs. infant (maternal 0-90 days) |
| **Arexvy (GSK RSVPreF3-AS01E)** | Protein subunit + AS01E adjuvant | May 2023 | Adults 60+ | 82.6% vs. RSV-LRTD |
| **mResvia (mRNA-1345, Moderna)** | mRNA encoding prefusion-stabilized F | May 2024 | Adults 60+ | 83.7% vs. RSV-LRTD (RENOIR trial) |

**Key scientific principle**: All approved vaccines encode/contain **prefusion-stabilized F protein** with engineered proline substitutions (DS-Cav1 mutations or equivalent) that lock F in the prefusion conformation → expose site Ø → much higher neutralizing antibody titers vs. post-fusion F (the basis of the 1960s FI-RSV failure).

**Maternal immunization (Abrysvo)**: Pregnant persons at 32-36 weeks gestation → maternal IgG transfers to fetus → infant protected in first months of life; MATISSE trial showed 82% efficacy in infants 0-90 days; concern about potential RSV-specific immune interference with subsequent immunizations (under monitoring).

## Connections

**→ [RSV F Protein](../../../03-molecular/rsv-f-protein/)**: RSV F protein mediates attachment to nucleolin and heparan sulfate and viral-host membrane fusion → syncytium formation; prefusion F (site Ø) is the dominant neutralizing epitope; nirsevimab (site Ø mAb), Abrysvo (Pfizer bivalent preF), Arexvy (GSK preF3 + AS01E), and mResvia (Moderna mRNA-1345) all target prefusion F for RSV prevention.

**→ [MAVS](../../../03-molecular/mavs/)**: RSV NS1 protein degrades TRIM25 → prevents RIG-I K63-ubiquitination → impairs RIG-I/MAVS signaling → reduced IFN-β production; RSV NS2 blocks STAT2 nuclear translocation → ISGs suppressed; NS1+NS2 together reduce MAVS-driven IFN-β ~10-fold; IFN-λ (type III) at mucosal surfaces is the dominant innate mucosal defense against RSV that NS1/NS2 cannot fully block.

**→ [IL-33](../../../03-molecular/il-33/)**: RSV airway epithelial infection and syncytium-mediated mechanical damage release IL-33 from epithelial nuclei (danger signal/DAMP) → ST2+ ILC2 activation → IL-4/IL-5/IL-13 → type 2 inflammation, eosinophilia, mucus hypersecretion, and airway hyperresponsiveness; RSV-IL-33-ILC2 axis is a key mechanism linking RSV bronchiolitis to subsequent childhood asthma.

**→ [TSLP](../../../03-molecular/tslp/)**: RSV-induced airway epithelial damage and dsRNA replication intermediates trigger TSLP release from airway epithelium → TSLP receptor on ILC2 and basophils → IL-4/IL-13 → Th2 polarization and IgE class switching; neonatal RSV-driven TSLP sensitization during a critical early developmental window may explain the epidemiological RSV-asthma link; tezepelumab (anti-TSLP) is being investigated in RSV-triggered wheeze.

**→ [Type I Interferon](../../../03-molecular/type-i-interferon/)**: RSV NS1/NS2 cooperatively suppress type I IFN at multiple levels: NS1 targets TRIM25 and IRF3, preventing IFN-β transcription; NS2 blocks STAT2 nuclear translocation, preventing ISG induction; premature infants with immature IFN signaling systems have more severe RSV bronchiolitis; IFN-λ (type III IFN at mucosal surfaces) is less susceptible to NS1/NS2 and represents the dominant innate mucosal defense.

- `connects-to` → **[Respiratory Syncytial Virus](../../../02-pathogen/01-viruses/respiratory-syncytial-virus/README.md)** — Respiratory syncytial virus, a negative-sense RNA pneumovirus, fuses airway cells into syncytia and blunts interferon with NS1/NS2; it reinfects throughout life because the G protein varies and memory is short, yet prefusion-F antibodies and vaccines now prevent severe disease.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — RSV is the top cause of infant bronchiolitis and a major cause of pneumonia in the elderly and immunocompromised: it infects ciliated airway epithelium, sloughing cells and plugging small airways with mucus → air trapping, hypoxia, and wheeze; care is supportive.
- `connects-to` → **[Asthma](../asthma/README.md)** — Severe RSV bronchiolitis in infancy is the strongest environmental risk factor for childhood asthma: epithelial damage releases IL-33 and TSLP that activate ILC2s toward type-2 inflammation, biasing the developing airway toward allergic sensitization and recurrent wheeze.
