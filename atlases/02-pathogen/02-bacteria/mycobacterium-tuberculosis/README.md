---
schema: pathogen-entry/v1
id: mycobacterium-tuberculosis
name: Mycobacterium tuberculosis
atlas: 02-pathogen
scale: 02-bacteria
status: draft
last_reviewed: 2026-06-03
summary: "Aerobic acid-fast bacillus (Mycobacteriaceae). Causes TB — leading infectious disease killer (~1.5 million deaths/year). Resides in alveolar macrophages by blocking phagosome-lysosome fusion. Transmitted by aerosolised droplet nuclei."
aliases: ["Mtb", "M. tuberculosis", "TB bacillus", "Koch's bacillus", "MTBC"]
sources:
  - id: dartois-2022-mtb-review
    type: peer-reviewed
    cite: "Dartois VA, Rubin EJ. Anti-tuberculosis treatment strategies and drug development: challenges and priorities. Nat Rev Microbiol. 2022;20(11):685-701."
    doi: "10.1038/s41579-022-00731-y"
    pmid: "35478222"
    url: "https://doi.org/10.1038/s41579-022-00731-y"
  - id: who-tb-report-2023
    type: regulatory
    cite: "World Health Organization. Global Tuberculosis Report 2023. WHO; 2023."
    url: "https://www.who.int/teams/global-tuberculosis-programme/tb-reports/global-tuberculosis-report-2023"
    accessed: "2026-06-03"
  - id: russell-2010-mtb-macrophage
    type: peer-reviewed
    cite: "Russell DG, Barry CE 3rd, Flynn JL. Tuberculosis: what we don't know can, and does, hurt us. Science. 2010;328(5980):852-6."
    doi: "10.1126/science.1184563"
    pmid: "20466922"
    url: "https://doi.org/10.1126/science.1184563"
  - id: ehrt-2009-mtb-virulence
    type: peer-reviewed
    cite: "Ehrt S, Schnappinger D. Mycobacterial survival strategies in the phagosome: defence against host stresses. Cell Microbiol. 2009;11(8):1170-8."
    doi: "10.1111/j.1462-5822.2009.01335.x"
    pmid: "19438517"
    url: "https://doi.org/10.1111/j.1462-5822.2009.01335.x"
cross_links:
  - target: 01-human/06-organ/lung
    relation: damages
    note: "Pulmonary TB causes caseating granulomas, cavitation, and progressive parenchymal destruction; upper-lobe predominance reflects higher O₂ tension. Radiographic consolidation, cavities, and tree-in-bud pattern are hallmarks."
  - target: 01-human/05-tissue/alveolus
    relation: damages
    note: "Mtb infects alveolar macrophages residing within alveoli; granuloma formation destroys alveolar architecture and the caseating necrosis of primary and reactivation TB obliterates alveolar structure."
  - target: 01-human/07-system/immune-system
    relation: damages
    note: "Mtb actively evades immune clearance: ESX-1 secretion system disrupts phagosome acidification, LpqH/LprG lipoproteins block MHC-II antigen presentation, and T cell exhaustion in chronic TB progressively impairs adaptive immunity."
  - target: 01-human/07-system/digestive-system
    relation: damages
    note: "Extrapulmonary TB causes peritoneal TB (ascites, bowel obstruction), ileocecal TB mimicking Crohn's disease, and hepatic TB — occurring in 5–15% of TB cases globally."
---

# Mycobacterium tuberculosis

## Overview

*Mycobacterium tuberculosis* (Mtb) is the causative agent of **tuberculosis (TB)** — the leading single-pathogen infectious disease killer in the world, responsible for approximately **1.5 million deaths per year** and 10 million new cases annually [^who-tb-report-2023]. One quarter of the global population is estimated to carry latent Mtb infection.

Mtb is an **aerobic, non-motile, obligate pathogen** of the order Actinomycetales, family Mycobacteriaceae. It is classified as an **acid-fast bacillus (AFB)** — its lipid-rich cell wall (unique mycolic acid layer, ~60% of dry weight) retains carbol fuchsin stain after acid-alcohol decolorisation (Ziehl-Neelsen staining), a property exploited for rapid diagnostic smear microscopy.

The organism occupies a unique niche: it is an **obligate intracellular pathogen** that resides primarily in alveolar macrophages, evading destruction by blocking phagosome-lysosome fusion — turning the cell designed to destroy it into its replication and persistence compartment [^russell-2010-mtb-macrophage].

Mtb belongs to the **Mycobacterium tuberculosis complex (MTBC)**, which includes *M. bovis* (cattle and humans, attenuated BCG vaccine derived), *M. africanum*, *M. microti*, and others with varying host ranges.

## Structure

### Cell Wall Architecture

The Mtb cell wall is the most complex and therapeutically important feature of the organism:

| Layer (inside-out) | Composition | Function |
|:---|:---|:---|
| **Plasma membrane** | Conventional phospholipid bilayer | Ion transport, protein anchoring |
| **Peptidoglycan** | Cross-linked NAM-NAG chains | Structural rigidity (target of isoniazid, cycloserine) |
| **Arabinogalactan** | Branched arabinose-galactose polymer, covalently linked to peptidoglycan | Scaffold for mycolic acid attachment |
| **Mycolic acids** | Very-long-chain α-branched, β-hydroxylated fatty acids (C70–C90); outermost inner layer | Creates hydrophobic barrier; accounts for low outer membrane permeability; target of isoniazid (via InhA) |
| **Capsule-like outer layer** | Loosely associated polysaccharides, lipoglycans, proteins | Immune evasion; receptor-ligand interactions with macrophage |

This cell wall structure makes Mtb:
- Extraordinarily impermeable to most hydrophilic antibiotics
- Intrinsically resistant to common disinfectants
- Slow-growing (generation time ~15–20 h vs. ~20 min for *E. coli*) — dictating the need for months of antibiotic therapy

### Genome

- **Genome size:** 4.4 Mb; GC content 65.6%
- **~4,000 genes**; unusually large lipid metabolism gene family reflecting the cell wall's complexity
- **ESX secretion systems (T7SS):** ESX-1, ESX-3, ESX-5 — key virulence determinants secreting ESAT-6 and CFP-10 (T cell antigens; diagnostic use in IGRA tests)
- No plasmids in H37Rv reference strain; few mobile genetic elements → slow genome evolution vs. horizontal gene transfer

## Infection Mechanism

### Transmission

Mtb is transmitted via **aerosolised droplet nuclei** — particles of 1–5 µm generated by coughing, sneezing, or singing from an infectious person with active pulmonary TB. These tiny particles (containing as few as 1–5 bacilli) can remain suspended in air for hours and penetrate to the alveolar level on inhalation. Larger droplets settle rapidly and are intercepted by the mucociliary escalator.

- **Infectious dose:** Estimated to be as low as 1–10 bacilli for susceptible hosts
- **Secondary attack rate:** ~25–50% of household contacts of smear-positive TB develop latent infection; <10% develop active disease

### Alveolar Deposition and Macrophage Infection

1. Droplet nuclei land on alveolar surfaces → **alveolar macrophages** phagocytose Mtb via multiple surface receptors (mannose receptor, complement receptors CR3/CR4, Fcγ receptors)
2. Normally, the phagosome matures (pH falls to ~5.0, fuses with lysosomes) and destroys bacteria. Mtb evades this by:
   - **Preventing phagosomal acidification** (secretes lipid phosphatase SapM, which depletes PI3P; blocks V-ATPase recruitment)
   - **Arresting phagosome maturation** (ESX-1-secreted ESAT-6 permeabilises the phagosomal membrane; Mtb escapes into cytosol in some cells)
   - **Recruiting host lipids** (Mtb induces lipid body formation; uses host cholesterol and fatty acids as carbon/energy sources)
3. Intracellular Mtb multiplies slowly (~15–20 h/generation) within the phagosomal compartment, eventually killing the macrophage

### Primary Infection and Ghon Complex

The primary (Ghon) focus forms at the alveolar entry site (typically lower/middle lobes — highest ventilation). Bacilli drain to hilar lymph nodes → Ghon complex (primary focus + hilar lymph node enlargement). In ~90–95% of immunocompetent adults, this is contained by:
- Innate responses (macrophage activation, neutrophil killing)
- Adaptive T-cell responses (CD4⁺ Th1: IFN-γ → activates macrophages; CD8⁺ T cells: kill infected macrophages)
- **Granuloma formation:** Organised structure of infected/uninfected macrophages, epithelioid macrophages, Langhans giant cells, lymphocytes, fibroblasts; walls off but rarely sterilises the infection

**Latent TB infection (LTBI):** Bacteriologically contained but not eradicated; Mtb persists in a metabolically dormant (non-replicating) state within granulomas. LTBI has ~5–10% lifetime risk of progression to active disease (higher with HIV, TNF-α inhibitors, silicosis, malnutrition).

## Host Interactions

### Granuloma Biology

The granuloma is Mtb's unique host-pathogen interface [^russell-2010-mtb-macrophage]:

| Granuloma zone | Composition | Function |
|:---|:---|:---|
| **Necrotic core** | Caseous (cheese-like) necrosis; abundant Mtb (potentially) | Nutrient-poor, low O₂, acid pH — limits Mtb growth but also limits immune effector access |
| **Epithelioid macrophage ring** | Fused macrophages (Langhans giant cells); closest to bacteria | Attempt to kill/contain bacteria via ROS, RNS, autophagy |
| **Lymphocyte mantle** | CD4⁺ and CD8⁺ T cells; B-cell follicle-like structures in some granulomas | Provide IFN-γ for macrophage activation; cytotoxic T cells kill heavily infected cells |
| **Fibroblast rim** | Collagen deposition | Structural containment; limits dissemination |

### Immune Evasion

| Mechanism | Detail |
|:---|:---|
| **Phagosome arrest** | SapM phosphatase, ESAT-6/CFP-10 — prevent phagosomal maturation and acidification |
| **Antioxidant defences** | KatG (catalase-peroxidase), SodA/SodC (superoxide dismutases) neutralise macrophage ROS/RNS |
| **Lipid utilisation** | Beta-oxidation of host cholesterol/fatty acids via mce4 operon; survival during nutritional stress |
| **T-cell evasion** | ESAT-6 is a T-cell antigen but also a membrane-damaging toxin that disrupts immune synapses; PtpA phosphatase impairs MHC-II presentation |

## Connections

- **Damages** → [Lung](../../../01-human/06-organ/lung/README.md): Pulmonary TB — the most common presentation — causes caseating granulomas, cavitation, and progressive parenchymal destruction in the lung; upper lobe predominance due to high local O₂ tension and poorer lymphatic clearance.
- **Damages** → [Alveolus](../../../01-human/05-tissue/alveolus/README.md): Granuloma formation within alveoli destroys normal alveolar architecture; caseating necrosis eliminates gas-exchange units; healing granulomas calcify (Ghon/Ranke complex) and may be visible on chest X-ray.

## Pathology

### Clinical Presentations

| Presentation | Features |
|:---|:---|
| **Primary TB** | Usually asymptomatic or mild febrile illness; Ghon complex on chest X-ray; 90–95% self-limited |
| **Primary progressive TB** | Occurs in infants, HIV-infected, severely immunosuppressed; primary focus progresses to pneumonia or miliary spread |
| **Reactivation TB (most adult TB)** | Upper lobe cavitary disease; chronic cough, haemoptysis, fever, night sweats, weight loss; classic "consumption" |
| **Miliary TB** | Haematogenous dissemination → millet-seed-sized granulomas in lungs, liver, spleen, meninges; uniformly fatal if untreated |
| **Extrapulmonary TB** | Pleural (~20%), lymph node (TB adenitis — commonest extrapulmonary), spinal (Pott's disease), renal, pericardial, meningeal |
| **Drug-resistant TB** | MDR-TB (resistant to isoniazid + rifampicin): ~400,000 cases/year; XDR-TB: additional resistance to fluoroquinolones and bedaquiline/linezolid |

### Treatment

Standard regimen for drug-sensitive TB: **2 months of RIPE** (rifampicin, isoniazid, pyrazinamide, ethambutol) → **4 months of RI** — total 6 months. Shorter regimens (4 months: 2 months HRZE + 2 months rifapentine/moxifloxacin) now validated for drug-sensitive TB [^dartois-2022-mtb-review].

Prevention: **BCG vaccine** (live-attenuated *M. bovis*): highly effective against miliary/meningeal TB in children; variable efficacy against pulmonary TB (0–80% in trials). **LTBI treatment** (isoniazid 6 months, or 3HP/1HP shorter regimens) reduces reactivation risk by ~60–90%.

## See Also

- [Lung](../../../01-human/06-organ/lung/README.md) — primary site of TB disease.
- [Alveolus](../../../01-human/05-tissue/alveolus/README.md) — the tissue unit hosting granulomas.
- [Respiratory system](../../../01-human/07-system/respiratory-system/README.md) — the system affected.

[^dartois-2022-mtb-review]: Dartois VA, Rubin EJ. Anti-tuberculosis treatment strategies and drug development: challenges and priorities. *Nat Rev Microbiol.* 2022;20(11):685-701. [doi:10.1038/s41579-022-00731-y](https://doi.org/10.1038/s41579-022-00731-y) · [PubMed 35478222](https://pubmed.ncbi.nlm.nih.gov/35478222/)
[^who-tb-report-2023]: World Health Organization. *Global Tuberculosis Report 2023.* [who.int/teams/global-tuberculosis-programme/tb-reports](https://www.who.int/teams/global-tuberculosis-programme/tb-reports/global-tuberculosis-report-2023)
[^russell-2010-mtb-macrophage]: Russell DG, Barry CE 3rd, Flynn JL. Tuberculosis: what we don't know can, and does, hurt us. *Science.* 2010;328(5980):852-6. [doi:10.1126/science.1184563](https://doi.org/10.1126/science.1184563) · [PubMed 20466922](https://pubmed.ncbi.nlm.nih.gov/20466922/)
[^ehrt-2009-mtb-virulence]: Ehrt S, Schnappinger D. Mycobacterial survival strategies in the phagosome: defence against host stresses. *Cell Microbiol.* 2009;11(8):1170-8. [doi:10.1111/j.1462-5822.2009.01335.x](https://doi.org/10.1111/j.1462-5822.2009.01335.x) · [PubMed 19438517](https://pubmed.ncbi.nlm.nih.gov/19438517/)
