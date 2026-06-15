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
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "HIV-AIDS is the most important co-factor for TB reactivation globally: HIV depletes CD4+ Th1 cells and destroys granuloma integrity → latent TB reactivates; TB is the leading cause of AIDS-related death; concurrent ART + HRZE treatment mandatory; IRIS risk with early ART."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-γ → STAT1 → IRF1 → iNOS → NO kills intracellular Mtb; Mtb ManLAM and phenolic glycolipid suppress STAT1 signaling → impaired macrophage activation; STAT1 LOF → MSMD with disseminated BCG after vaccination and NTM susceptibility — demonstrating STAT1 is non-redundant."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "The lung is tuberculosis's primary battleground: inhaled M. tuberculosis seeds the alveoli, where Th1 granulomas wall it off; reactivation in oxygen-rich upper lobes makes caseating cavities that shed bacilli in cough — the infectious form — and a Ghon focus marks healed disease."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "The macrophage is host and battleground in tuberculosis: M. tuberculosis is phagocytosed but blocks phagosome maturation to survive inside, while IFN-γ-activated macrophages fight back with NO; the granuloma is a ball of infected macrophages that contains but rarely clears it."
  - target: 02-pathogen/02-bacteria/mycobacterium-tuberculosis
    relation: connects-to
    note: "Tuberculosis is caused by Mycobacterium tuberculosis: its waxy mycolic-acid wall (acid-fast) resists killing and drives the slow granulomatous response; it grows slowly (weeks to culture) and demands months of multidrug RIPE therapy, while MDR/XDR-TB resistance grows."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Diabetes roughly triples the risk of active tuberculosis: hyperglycemia impairs macrophage and T-cell function, so diabetics reactivate latent TB more readily and fare worse—bidirectional, as TB also worsens glycemic control."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Control of tuberculosis depends on Th1 helper T cells: IFN-γ from CD4+ Th1 cells activates infected macrophages to kill the bacillus and maintain the granuloma, which is why HIV-driven CD4 loss so dramatically raises TB reactivation and dissemination."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Mycobacterium tuberculosis subverts dendritic cells to delay immunity: by slowing DC migration and antigen presentation to T cells in lymph nodes, the bacillus buys weeks before an adaptive Th1 response forms—part of why TB establishes a foothold before containment."
  - target: 01-human/07-system/copd
    relation: connects-to
    note: "Tuberculosis and COPD interact in both directions: past TB scarring causes airflow obstruction resembling COPD, while COPD and its inhaled steroids raise TB risk—so in high-burden regions chronic cough and obstruction warrant testing for active or prior TB."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D underpins macrophage defense against tuberculosis: vitamin-D signaling induces the antimicrobial peptide cathelicidin that helps macrophages kill M. tuberculosis, so deficiency raises TB risk—the old link behind 'sunlight and cod-liver oil' sanatorium cures."
  - target: 01-human/07-system/nsclc
    relation: connects-to
    note: "Tuberculosis and lung cancer overlap clinically: both can present as a cavitary or spiculated lung mass, old TB scars raise later lung-cancer risk, and chronic granulomatous inflammation may promote carcinogenesis—so a 'mass' in an endemic area needs both worked up."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Type I interferon is harmful in tuberculosis, unlike in viral infection: a type I IFN signature marks active, severe TB because it suppresses the protective IFN-gamma/macrophage response—so the same cytokine family that fights viruses helps Mtb evade killing."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils are a double-edged sword in tuberculosis: they swarm to infected lung but, when overwhelmed, drive the tissue necrosis and cavitation that spreads Mtb—so a neutrophil-dominated response marks severe, transmissible disease rather than control."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "Tuberculosis is a classic cause of adrenal insufficiency: hematogenous spread can destroy both adrenal glands, producing Addison's disease—historically the leading cause—so adrenal calcification or new Addison's should prompt a search for TB."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Cytotoxic CD8 T cells help contain tuberculosis: alongside CD4 help, they kill infected macrophages that fail to clear the bacillus and secrete IFN-γ, so they are central to granuloma immunity and a key target for next-generation TB vaccines."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Tuberculosis often localizes to the lymphatic system: cervical node TB (scrofula) is the classic extrapulmonary form, and lymphatic and bloodstream spread of the bacillus seeds miliary disease throughout the body when immunity fails."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Tuberculosis can invade the brain: hematogenous seeding causes TB meningitis and tuberculomas, among the deadliest forms—so suspected CNS TB demands urgent treatment with steroids, since inflammation, not just infection, drives the damage."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Tuberculosis frequently spreads to the kidney: genitourinary TB is a leading extrapulmonary form, seeding the kidney to cause sterile pyuria, scarring and ureteral strictures—so persistent urinary symptoms with negative routine cultures should raise suspicion."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Macrophages kill tuberculosis partly with nitric oxide: activated by IFN-gamma, they generate reactive nitrogen species via iNOS to attack the bacterium inside the phagosome, a key defense the pathogen evolves to resist and survive within the granuloma."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Regulatory T cells help tuberculosis persist: by dampening the protective Th1 response, expanded Tregs can let M. tuberculosis survive in latency, part of the immune balance that keeps the infection contained yet not cleared."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "TB is an oxygen-seeking infection: aerobic M. tuberculosis favors the oxygen-rich upper lung where reactivation strikes, while deep in the granuloma's hypoxic, oxygen-starved core the bacteria turn dormant—the latency that makes TB so hard to cure."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Healed TB leaves fibrosis behind: granulomas resolve with dense scarring, apical fibrosis, and traction bronchiectasis that permanently damage the lung, so survivors often carry lasting post-TB lung disease even after cure."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "NK cells join the early fight against TB: alongside macrophages they pour out interferon-gamma to activate killing of the bacteria, an innate first line before the slower T-cell granuloma response takes over."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Healed TB leaves a calcium signature: the Ghon focus and lymph node it drains often calcify into the Ranke complex, so flecks of calcium on a chest X-ray mark old, walled-off infection that can later reactivate."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "TB can settle in the gut: swallowed bacteria or bloodborne spread seed intestinal tuberculosis, especially the ileocecal region, mimicking Crohn's disease with pain, obstruction and weight loss."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1beta shapes the TB granuloma's balance: the inflammasome cytokine helps control the bacteria but, in excess, drives the tissue destruction and cavitation that spread infection, so it sits at the knife-edge of protection and damage."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Tuberculosis is a fight over iron: the bacterium needs iron to grow and scavenges it from the host, while the body locks iron away to starve it—a tug-of-war in which iron overload tilts toward the microbe."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Tuberculosis can wrap the heart: TB pericarditis fills the sac with fluid and later scars it into a constricting shell, a dangerous extrapulmonary form especially common with HIV."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Miliary tuberculosis seeds the bone marrow: bloodborne spread studs the marrow with granulomas, suppressing blood production and causing the pancytopenia of disseminated disease."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photons hunt tuberculosis throughout its course: the chest X-ray shows the upper-lobe cavities and the fine 'millet seed' miliary spread, CT maps the damage, and old calcified Ghon foci mark where a long-healed infection once smoldered."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "Miliary tuberculosis peppers the spleen: bloodborne bacilli seed it with countless tiny granulomas, swelling the organ — splenomegaly studded with white tubercles is a classic finding of disseminated disease at autopsy."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Spinal tuberculosis threatens the nerves it surrounds: Pott's disease erodes the vertebrae and forms a cold abscess that compresses the spinal cord and its roots, causing the paraplegia that is TB's most feared skeletal complication."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Curing TB endangers the liver: the core drugs — isoniazid, rifampin, and pyrazinamide — are all hepatotoxic, so transaminases are watched and the regimen held if they climb, balancing the risk against leaving the infection untreated."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "TB walls itself in with collagen: the granuloma rings its caseous core with epithelioid cells and a fibrous, collagen-rich cuff, and healing leaves the scarred, calcified lesions and lung cavities that mark old or arrested disease."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "TB's stain hangs on a waxy wall: Mycobacterium tuberculosis sheathes itself in mycolic-acid lipids that electron microscopy resolves as a thick envelope — the layer that traps the Ziehl-Neelsen dye and makes the bacillus acid-fast."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "TB is fought by cells, not antibodies: the response is T-cell and macrophage driven, so antibody serology is too unreliable for diagnosis that the WHO recommends against it, and detection rests instead on IGRA, smear, culture, and molecular tests."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "TB can eat into the skeleton: spread to the spine causes Pott's disease, collapsing vertebrae into a gibbus deformity, while tuberculous arthritis and dactylitis mark its reach into bone and joint beyond the lung."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "The cure is hard on the liver: isoniazid, rifampin, and pyrazinamide are all hepatotoxic, injuring hepatocytes into a drug-induced hepatitis that is the chief reason TB therapy must be monitored and sometimes interrupted."
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
- `connects-to` → **[HIV/AIDS](../hiv-aids/README.md)** — HIV is the single most powerful risk factor for TB reactivation; HIV-driven CD4⁺ T cell depletion collapses granuloma integrity → latent TB reactivates; TB is the leading cause of AIDS-related mortality worldwide; concurrent ART + HRZE are required; IRIS (immune reconstitution inflammatory syndrome) complicates early ART initiation in TB-HIV co-infection.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-γ → STAT1 → IRF1 → iNOS → NO kills intracellular Mtb; Mtb ManLAM and phenolic glycolipid suppress STAT1 signaling → impaired macrophage activation; STAT1 LOF → MSMD with disseminated BCG after vaccination and NTM susceptibility — demonstrating STAT1 is non-redundant.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — The lung is tuberculosis's primary battleground: inhaled M. tuberculosis seeds the alveoli, where Th1 granulomas wall it off; reactivation in oxygen-rich upper lobes makes caseating cavities that shed bacilli in cough — the infectious form — and a Ghon focus marks healed disease.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — The macrophage is host and battleground in tuberculosis: M. tuberculosis is phagocytosed but blocks phagosome maturation to survive inside, while IFN-γ-activated macrophages fight back with NO; the granuloma is a ball of infected macrophages that contains but rarely clears it.
- `connects-to` → **[Mycobacterium tuberculosis](../../../02-pathogen/02-bacteria/mycobacterium-tuberculosis/README.md)** — Tuberculosis is caused by Mycobacterium tuberculosis: its waxy mycolic-acid wall (acid-fast) resists killing and drives the slow granulomatous response; it grows slowly (weeks to culture) and demands months of multidrug RIPE therapy, while MDR/XDR-TB resistance grows.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Diabetes roughly triples the risk of active tuberculosis: hyperglycemia impairs macrophage and T-cell function, so diabetics reactivate latent TB more readily and fare worse—bidirectional, as TB also worsens glycemic control.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Control of tuberculosis depends on Th1 helper T cells: IFN-γ from CD4+ Th1 cells activates infected macrophages to kill the bacillus and maintain the granuloma, which is why HIV-driven CD4 loss so dramatically raises TB reactivation and dissemination.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Mycobacterium tuberculosis subverts dendritic cells to delay immunity: by slowing DC migration and antigen presentation to T cells in lymph nodes, the bacillus buys weeks before an adaptive Th1 response forms—part of why TB establishes a foothold before containment.
- `connects-to` → **[COPD](../copd/README.md)** — Tuberculosis and COPD interact in both directions: past TB scarring causes airflow obstruction resembling COPD, while COPD and its inhaled steroids raise TB risk—so in high-burden regions chronic cough and obstruction warrant testing for active or prior TB.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D underpins macrophage defense against tuberculosis: vitamin-D signaling induces the antimicrobial peptide cathelicidin that helps macrophages kill M. tuberculosis, so deficiency raises TB risk—the old link behind 'sunlight and cod-liver oil' sanatorium cures.
- `connects-to` → **[NSCLC](../nsclc/README.md)** — Tuberculosis and lung cancer overlap clinically: both can present as a cavitary or spiculated lung mass, old TB scars raise later lung-cancer risk, and chronic granulomatous inflammation may promote carcinogenesis—so a 'mass' in an endemic area needs both worked up.
- `connects-to` → **[Type I Interferon](../../03-molecular/type-i-interferon/README.md)** — Type I interferon is harmful in tuberculosis, unlike in viral infection: a type I IFN signature marks active, severe TB because it suppresses the protective IFN-gamma/macrophage response—so the same cytokine family that fights viruses helps Mtb evade killing.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Neutrophils are a double-edged sword in tuberculosis: they swarm to infected lung but, when overwhelmed, drive the tissue necrosis and cavitation that spreads Mtb—so a neutrophil-dominated response marks severe, transmissible disease rather than control.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — Tuberculosis is a classic cause of adrenal insufficiency: hematogenous spread can destroy both adrenal glands, producing Addison's disease—historically the leading cause—so adrenal calcification or new Addison's should prompt a search for TB.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Cytotoxic CD8 T cells help contain tuberculosis: alongside CD4 help, they kill infected macrophages that fail to clear the bacillus and secrete IFN-γ, so they are central to granuloma immunity and a key target for next-generation TB vaccines.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Tuberculosis often localizes to the lymphatic system: cervical node TB (scrofula) is the classic extrapulmonary form, and lymphatic and bloodstream spread of the bacillus seeds miliary disease throughout the body when immunity fails.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Tuberculosis can invade the brain: hematogenous seeding causes TB meningitis and tuberculomas, among the deadliest forms—so suspected CNS TB demands urgent treatment with steroids, since inflammation, not just infection, drives the damage.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Tuberculosis frequently spreads to the kidney: genitourinary TB is a leading extrapulmonary form, seeding the kidney to cause sterile pyuria, scarring and ureteral strictures—so persistent urinary symptoms with negative routine cultures should raise suspicion.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — Macrophages kill tuberculosis partly with nitric oxide: activated by IFN-gamma, they generate reactive nitrogen species via iNOS to attack the bacterium inside the phagosome, a key defense the pathogen evolves to resist and survive within the granuloma.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Regulatory T cells help tuberculosis persist: by dampening the protective Th1 response, expanded Tregs can let M. tuberculosis survive in latency, part of the immune balance that keeps the infection contained yet not cleared.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — TB is an oxygen-seeking infection: aerobic M. tuberculosis favors the oxygen-rich upper lung where reactivation strikes, while deep in the granuloma's hypoxic, oxygen-starved core the bacteria turn dormant—the latency that makes TB so hard to cure.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Healed TB leaves fibrosis behind: granulomas resolve with dense scarring, apical fibrosis, and traction bronchiectasis that permanently damage the lung, so survivors often carry lasting post-TB lung disease even after cure.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — NK cells join the early fight against TB: alongside macrophages they pour out interferon-gamma to activate killing of the bacteria, an innate first line before the slower T-cell granuloma response takes over.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Healed TB leaves a calcium signature: the Ghon focus and lymph node it drains often calcify into the Ranke complex, so flecks of calcium on a chest X-ray mark old, walled-off infection that can later reactivate.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — TB can settle in the gut: swallowed bacteria or bloodborne spread seed intestinal tuberculosis, especially the ileocecal region, mimicking Crohn's disease with pain, obstruction and weight loss.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1beta shapes the TB granuloma's balance: the inflammasome cytokine helps control the bacteria but, in excess, drives the tissue destruction and cavitation that spread infection, so it sits at the knife-edge of protection and damage.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Tuberculosis is a fight over iron: the bacterium needs iron to grow and scavenges it from the host, while the body locks iron away to starve it—a tug-of-war in which iron overload tilts toward the microbe.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Tuberculosis can wrap the heart: TB pericarditis fills the sac with fluid and later scars it into a constricting shell, a dangerous extrapulmonary form especially common with HIV.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Miliary tuberculosis seeds the bone marrow: bloodborne spread studs the marrow with granulomas, suppressing blood production and causing the pancytopenia of disseminated disease.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photons hunt tuberculosis throughout its course: the chest X-ray shows the upper-lobe cavities and the fine 'millet seed' miliary spread, CT maps the damage, and old calcified Ghon foci mark where a long-healed infection once smoldered.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — Miliary tuberculosis peppers the spleen: bloodborne bacilli seed it with countless tiny granulomas, swelling the organ — splenomegaly studded with white tubercles is a classic finding of disseminated disease at autopsy.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Spinal tuberculosis threatens the nerves it surrounds: Pott's disease erodes the vertebrae and forms a cold abscess that compresses the spinal cord and its roots, causing the paraplegia that is TB's most feared skeletal complication.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Curing TB endangers the liver: the core drugs — isoniazid, rifampin, and pyrazinamide — are all hepatotoxic, so transaminases are watched and the regimen held if they climb, balancing the risk against leaving the infection untreated.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — TB walls itself in with collagen: the granuloma rings its caseous core with epithelioid cells and a fibrous, collagen-rich cuff, and healing leaves the scarred, calcified lesions and lung cavities that mark old or arrested disease.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — TB's stain hangs on a waxy wall: Mycobacterium tuberculosis sheathes itself in mycolic-acid lipids that electron microscopy resolves as a thick envelope — the layer that traps the Ziehl-Neelsen dye and makes the bacillus acid-fast.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — TB is fought by cells, not antibodies: the response is T-cell and macrophage driven, so antibody serology is too unreliable for diagnosis that the WHO recommends against it, and detection rests instead on IGRA, smear, culture, and molecular tests.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — TB can eat into the skeleton: spread to the spine causes Pott's disease, collapsing vertebrae into a gibbus deformity, while tuberculous arthritis and dactylitis mark its reach into bone and joint beyond the lung.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — The cure is hard on the liver: isoniazid, rifampin, and pyrazinamide are all hepatotoxic, injuring hepatocytes into a drug-induced hepatitis that is the chief reason TB therapy must be monitored and sometimes interrupted.

## See Also

- [^who-tb-report-2023] World Health Organization. *Global Tuberculosis Report 2023.* Geneva: WHO; 2023.
- [^nahid-2016-tb-treatment] Nahid P et al. Official ATS/CDC/IDSA Clinical Practice Guidelines: Treatment of Drug-Susceptible Tuberculosis. *Clin Infect Dis.* 2016;63(7):e147-e195. [doi:10.1093/cid/ciw376](https://doi.org/10.1093/cid/ciw376) · [PubMed 27516382](https://pubmed.ncbi.nlm.nih.gov/27516382/)
- Related entries: [il-12](../../03-molecular/il-12/README.md), [tnf-alpha](../../03-molecular/tnf-alpha/README.md), [ifn-gamma](../../03-molecular/ifn-gamma/README.md), [anemia-of-chronic-disease](../anemia-of-chronic-disease/README.md), [immune-system](../immune-system/README.md)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
