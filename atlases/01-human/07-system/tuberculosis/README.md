---
schema: human-scale-entry/v1
id: tuberculosis
name: Tuberculosis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Tuberculosis (MTB; Mycobacterium tuberculosis) causes ~10M cases and 1.3M deaths annually; inhaled droplet nuclei → macrophage phagosome arrest → granuloma; HRZE 6-month regimen for drug-sensitive TB; BPaL (bedaquiline-pretomanid-linezolid) for MDR-TB."
aliases: ["TB", "pulmonary tuberculosis", "Mycobacterium tuberculosis", "MTB", "MTBC", "LTBI", "latent TB", "MDR-TB", "XDR-TB", "Pott's disease", "phthisis", "consumption"]
sources:
  - id: who-tb-report-2023
    type: clinical-guideline
    cite: "World Health Organization. Global Tuberculosis Report 2023. Geneva: WHO; 2023."
    url: "https://www.who.int/teams/global-tuberculosis-programme/tb-reports/global-tuberculosis-report-2023"
    accessed: "2026-06-08"
  - id: nahid-2016-tb-treatment
    type: peer-reviewed
    cite: "Nahid P, Dorman SE, Alipanah N, et al. Official ATS/CDC/IDSA Clinical Practice Guidelines: Treatment of Drug-Susceptible Tuberculosis. Clin Infect Dis. 2016;63(7):e147-e195."
    doi: "10.1093/cid/ciw376"
    pmid: "27516382"
    url: "https://doi.org/10.1093/cid/ciw376"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "IL-12/IFN-γ axis is essential for granuloma formation and MTB containment; IL12B or IL12RB1 loss of function → MSMD (recurrent BCG/NTM disease); ustekinumab (anti-p40) and other IL-12 pathway inhibitors → latent TB reactivation; IGRA screening before therapy."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "TNF-α is essential for granuloma formation and maintenance in TB; anti-TNF agents → 4-25× increased TB reactivation risk; antibody-based anti-TNF (infliximab/adalimumab) carries higher TB risk than etanercept; IGRA/TST mandatory before anti-TNF initiation."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "IFN-γ activates macrophages to restrict MTB growth (phagosome acidification, ROS burst, cathelicidin production); IFN-γ from MTB-sensitized T cells is the basis of IGRA diagnostic tests; IFNGR1/IFNGR2 mutations → MSMD phenotype with disseminated MTB/BCG disease."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "TB is a classic cause of ACD: sustained MTB infection → IL-6 + TNF-α + IFN-γ → hepcidin elevation → functional iron deficiency; TB treatment → inflammation subsides → ACD recovers; ACD severity correlates with TB disease activity (smear positivity, extent of lung disease)."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "MTB evades innate immunity by arresting phagosome maturation, secreting ESAT-6 to escape to cytosol, inhibiting MHC-II antigen presentation, and inducing regulatory T cells; CD4+ Th1 cells orchestrate granuloma; AIDS → CD4+ loss → TB reactivation is the paradigmatic example."
---

# Tuberculosis

## Overview

Tuberculosis (TB), caused by *Mycobacterium tuberculosis* (MTB), is the world's leading infectious disease killer among single pathogens, responsible for approximately **10 million new cases** and **1.3 million deaths** annually as of 2023 [^who-tb-report-2023]. An estimated one-quarter of the global population carries latent TB infection (LTBI); roughly 5–10% of these individuals will develop active TB over their lifetime, with the lifetime risk rising to >50% in people living with HIV.

TB is an airborne disease: an infectious person exhales droplet nuclei (1–5 μm diameter) that remain suspended in air and can be inhaled by contacts. As few as one to ten inhaled bacilli suffice for infection. High-burden regions include South-East Asia (India, Indonesia, Philippines), Africa, and Central Asia; multidrug-resistant TB (MDR-TB) is a particular threat in Eastern Europe and former Soviet states.

The WHO End TB Strategy targets a 90% reduction in incidence and 95% reduction in mortality by 2035 compared to 2015 baselines, requiring universal access to diagnosis, treatment, and prevention.

## Structure

### *Mycobacterium tuberculosis* Cell Biology

MTB is a **slow-growing, obligate aerobic, acid-fast bacillus** with several distinctive structural features:

| Feature | Detail |
|:--------|:-------|
| **Growth rate** | Doubling time 18–24 hours; colonies visible on solid media in 3–6 weeks |
| **Staining** | Acid-fast (Ziehl-Neelsen stain: pink bacilli on blue background); fluorochrome (auramine-rhodamine) for screening |
| **Cell wall** | Unusually thick: mycolic acids (C60–C90 fatty acids) + arabinogalactan + peptidoglycan core; the mycolic acid layer is the basis of acid-fastness and confers innate resistance to complement and many antibiotics |
| **Genome** | ~4.4 Mb circular chromosome; ~4,000 genes; highly conserved; GC content ~65% |
| **Virulence factors** | ESAT-6 (6-kDa early secretory antigen-6, ESX-1 secretion system); ManLAM (mannose-capped lipoarabinomannan, TLR2 agonist and phagosome maturation inhibitor); PE/PPE protein family |

**Key virulence mechanisms:**
- **ESAT-6** (encoded by *esxA*) is secreted via the ESX-1 (Type VII secretion) system → phagosomal membrane perforation → MTB escapes to cytosol → activates inflammasome and cGAS-STING (innate DNA sensing) while avoiding phagolysosomal killing
- **ManLAM** binds TLR2 → IL-10 production (suppressing IL-12); blocks phagosome acidification by preventing Rab7-mediated late-endosome fusion
- **Catalase-peroxidase (KatG)** detoxifies reactive oxygen species; *katG* mutations → isoniazid resistance

### Granuloma Architecture

The **granuloma** is the pathological hallmark of TB — a structured immune containment structure:

```
Central caseous necrosis (MTB + dead cells)
↓
Epithelioid macrophages (MTB-infected, activated)
↓
Langhans giant cells (macrophage fusion, horseshoe nucleus)
↓
CD4+ T cells (Th1, IFN-γ producing) + CD8+ CTLs
↓
B cells (follicle-like aggregates in chronic TB)
↓
Fibroblasts + fibrous capsule (outer containment)
```

In **latent TB**, granulomas are intact and immunologically active; MTB persists in a non-replicating or slowly-replicating state. In **active TB**, granuloma walls break down → caseous necrosis liquefies → cavity formation (providing aerobic niche for explosive MTB growth) → sputum-positive transmission.

## Function

### Infection Dynamics

**Primary infection:**
1. Inhaled droplet nuclei reach alveoli → alveolar macrophages phagocytose MTB via multiple receptors (complement receptors CR3/CR4, mannose receptor, DC-SIGN)
2. MTB arrests phagosome maturation → survives in early endosome (pH ~6.4 rather than 4.5)
3. Intracellular multiplication → macrophage lysis → infects neighbouring macrophages and DCs
4. DCs migrate to regional lymph nodes → prime CD4⁺ T cells (2–8 weeks incubation period) → T cell-mediated immunity begins → granuloma forms → bacillary replication controlled

**Latent TB infection (LTBI):**
- ~90% of immunocompetent adults who are infected do not develop active disease
- MTB persists in granulomas in a state of relative dormancy
- IGRA/TST converts to positive (indicates immune sensitisation, not necessarily active disease)
- Reactivation triggers: HIV (CD4 depletion), anti-TNF therapy, diabetes mellitus, malnutrition (BMI <18.5), silicosis, corticosteroids, ageing, organ transplant

**Transmission:**
- Pulmonary TB (especially smear-positive) is the main source; laryngeal TB is highly infectious
- Extrapulmonary TB (except laryngeal) is non-infectious
- Infectiousness falls dramatically within 2 weeks of effective treatment

### Immune Evasion

MTB is an expert intracellular pathogen with multiple immune evasion strategies:
- Phagosome maturation arrest (blocks Rab7, LAMP-1, lysosomal cathepsins)
- ESAT-6-mediated phagosome perforation → cytosolic MTB → blocks cGAS-STING → limits type I interferon activation (beneficial for the host: excessive IFN-β from MTB promotes bacterial growth)
- ManLAM → TLR2 → IL-10 → suppresses DC IL-12 production
- Inhibits MHC-II antigen loading → impairs CD4⁺ T cell priming
- Induces FoxP3⁺ Treg expansion → dampens effector T cell response
- Adapts to nutrient deprivation by metabolising host cholesterol as carbon source

## Pathology

### Disease Spectrum

| Category | Definition | Characteristics |
|:---------|:-----------|:----------------|
| **LTBI** | MTB infection, positive IGRA/TST, no symptoms, normal CXR | Non-infectious; 5-10% lifetime reactivation risk; treat if high-risk |
| **Primary TB** | Active disease in a newly infected individual | Often hilar adenopathy + lower/middle lobe infiltrate (Ghon complex); can progress in immunocompromised or young children |
| **Post-primary TB** | Reactivation in previously infected person | Upper lobe cavitary disease; highest infectiousness; cough + haemoptysis + night sweats + weight loss |
| **Miliary TB** | Haematogenous dissemination → seeding of all organs | 1–3 mm nodules on CXR (millet seed pattern); high mortality; common in HIV |
| **Extrapulmonary TB** | Any organ outside lungs | TB meningitis (highest mortality), Pott's disease (vertebral), genitourinary, pericardial, pleural, lymph node (scrofula) |

### Drug-Sensitive TB Treatment

Standard **HRZE** regimen [^nahid-2016-tb-treatment]:
- **Intensive phase (2 months):** Isoniazid (H) + Rifampicin (R) + Pyrazinamide (Z) + Ethambutol (E)
- **Continuation phase (4 months):** Isoniazid + Rifampicin
- Total duration: 6 months (can extend to 9 months for cavitary disease with positive 2-month culture)
- Treatment completion rate target: >90%

**Drug mechanisms:**
| Drug | Target | Key Side Effects |
|:-----|:-------|:----------------|
| Isoniazid | KatG → active form inhibits InhA (mycolic acid synthesis) | Hepatotoxicity, peripheral neuropathy (supplement B6) |
| Rifampicin | RNA polymerase β subunit (RpoB) | Hepatotoxicity, orange urine, drug interactions (CYP450 inducer) |
| Pyrazinamide | PncA → active acid disrupts membrane potential | Hyperuricaemia, hepatotoxicity; active only in acidic phagolysosome |
| Ethambutol | EmbB (arabinogalactan synthesis) | Optic neuritis (dose-dependent; monitor visual acuity) |

### MDR-TB and XDR-TB

- **MDR-TB:** Resistant to both isoniazid and rifampicin (~500,000 cases/year)
- **XDR-TB:** MDR + resistant to fluoroquinolones + at least one of bedaquiline/linezolid
- **BPaL regimen** (ZeNix trial 2022): Bedaquiline (ATP synthase inhibitor) + Pretomanid (nitroimidazole, respiratory chain) + Linezolid (oxazolidinone, 50S) × 6 months → ~89% cure rate for XDR-TB and treatment-intolerant MDR-TB; WHO-approved 2022

### Diagnosis

| Test | Mechanism | Sensitivity / Specificity | Notes |
|:-----|:----------|:--------------------------|:------|
| **Sputum smear (ZN/fluorescence)** | Acid-fast bacillus visualisation | Sens ~50-70% / Spec ~99% | Rapid, cheap; misses paucibacillary disease |
| **MGIT liquid culture** | Growth in Mycobacteria Growth Indicator Tube | Sens ~90% / Spec ~99% | Gold standard; results in 1–3 weeks |
| **Xpert MTB/RIF** | Real-time PCR + RIF resistance probe | Sens ~85-90% / Spec ~99% | 2-hour result; WHO recommended first-line |
| **TST (Mantoux)** | T cell recall response to PPD | Variable; cross-reactive with BCG/NTM | 48–72h reading; induration ≥5 mm (HIV), ≥10 mm (high-risk), ≥15 mm (low-risk) |
| **IGRA (QuantiFERON/T-SPOT)** | Ex vivo IFN-γ release to ESAT-6/CFP-10 | Sens ~80-90% / Spec ~95-99% | Not affected by BCG; preferred in vaccinated populations |
| **ADA (adenosine deaminase)** | Pleural/CSF marker of T cell activity | High sensitivity for pleural/meningeal TB | Useful for extrapulmonary TB diagnosis |

### Prevention

- **BCG vaccine (Bacillus Calmette-Guérin):** Live-attenuated *M. bovis*; given at birth in high-burden countries; 80% protection against severe childhood TB (meningeal, miliary); variable protection against adult pulmonary TB (~0–80%)
- **LTBI treatment:** Isoniazid × 6–9 months, or 3HP (isoniazid + rifapentine weekly × 12 doses), or 4R (rifampicin × 4 months) — reduces reactivation risk by ~60–90%
- **Airborne precautions:** Negative-pressure isolation rooms; N95 respirators for healthcare workers; UV germicidal irradiation

## Connections

- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — IL-12/IFN-γ axis is essential for granuloma formation and MTB containment; IL12B or IL12RB1 loss-of-function → MSMD with recurrent BCG/NTM disease; ustekinumab (anti-p40) → latent TB reactivation risk; IGRA screening mandatory before anti-IL-12 therapy initiation.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — TNF-α is required for granuloma assembly and maintenance; anti-TNF biologic therapy (infliximab, adalimumab, certolizumab) → 4–25× increased TB reactivation risk; TNF receptor fusion proteins (etanercept) carry lower risk; mandatory IGRA/TST screening and LTBI treatment before anti-TNF initiation.
- `connects-to` → **[IFN-γ](../../03-molecular/ifn-gamma/README.md)** — IFN-γ activates macrophages to restrict MTB growth via phagosome acidification, ROS burst, and cathelicidin (LL-37) production; IFN-γ released by MTB-sensitised T cells in response to ESAT-6/CFP-10 is the molecular basis of IGRA diagnostic tests; IFNGR1/IFNGR2 loss → MSMD with disseminated MTB/BCG disease.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — TB is a classic ACD cause: MTB-driven IL-6 + TNF-α + IFN-γ → hepcidin elevation → functional iron deficiency; ACD severity tracks TB disease activity (smear positivity, cavitary extent); successful treatment resolves ACD within weeks to months.
- `connects-to` → **[Immune System](../immune-system/README.md)** — MTB exemplifies intracellular immune evasion: phagosome maturation arrest, ESAT-6-mediated cytosolic escape, MHC-II inhibition, Treg induction; CD4⁺ Th1 cells orchestrate granuloma through IFN-γ and IL-2; HIV-related CD4⁺ depletion → TB reactivation is the archetypal immunodeficiency-pathogen interaction.

## See Also

- [^who-tb-report-2023] World Health Organization. *Global Tuberculosis Report 2023.* Geneva: WHO; 2023.
- [^nahid-2016-tb-treatment] Nahid P et al. Official ATS/CDC/IDSA Clinical Practice Guidelines: Treatment of Drug-Susceptible Tuberculosis. *Clin Infect Dis.* 2016;63(7):e147-e195. [doi:10.1093/cid/ciw376](https://doi.org/10.1093/cid/ciw376) · [PubMed 27516382](https://pubmed.ncbi.nlm.nih.gov/27516382/)
- Related entries: [il-12](../../03-molecular/il-12/README.md), [tnf-alpha](../../03-molecular/tnf-alpha/README.md), [ifn-gamma](../../03-molecular/ifn-gamma/README.md), [anemia-of-chronic-disease](../anemia-of-chronic-disease/README.md), [immune-system](../immune-system/README.md)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
