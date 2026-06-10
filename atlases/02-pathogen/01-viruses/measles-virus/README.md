---
schema: pathogen-entry/v1
id: measles-virus
name: Measles Virus
atlas: 02-pathogen
scale: 01-viruses
status: draft
last_reviewed: 2026-06-05
summary: "Paramyxoviridae morbillivirus; (−)ssRNA, ~16 kb; enveloped. R₀ = 12–18 (highest known). Binds CD150/SLAM on lymphocytes and Nectin-4 on airway epithelium. Causes profound immune amnesia lasting 2–3 years post-infection."
aliases: ["MeV", "measles morbillivirus", "rubeola", "paramyxovirus"]
sources:
  - id: mandell-principles
    type: textbook
    cite: "Bennett JE, Dolin R, Blaser MJ. Mandell, Douglas, and Bennett's Principles and Practice of Infectious Diseases. 9th ed. Elsevier; 2020."
    url: "https://www.elsevier.com/books/mandell-douglas-and-bennetts-principles-and-practice-of-infectious-diseases/bennett/978-0-323-48255-4"
    accessed: "2026-06-05"
  - id: fields-virology
    type: textbook
    cite: "Knipe DM, Howley PM, eds. Fields Virology. 7th ed. Wolters Kluwer; 2021."
    url: "https://www.lww.com/product/9781975112547"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/04-cellular/t-helper-cell
    relation: infects
    note: "MeV H protein binds CD150/SLAM on activated CD4+ T cells and DCs as primary immune entry receptor; direct T cell infection → apoptosis and lymphopenia; suppresses T cell proliferation causing weeks-long post-measles immunosuppression."
  - target: 01-human/04-cellular/dendritic-cell
    relation: infects
    note: "Lung DCs express CD150/SLAM and are the first cells infected after respiratory exposure; MeV-infected DCs travel to regional lymph nodes, amplifying viremia while failing to mount effective IFN response due to V-protein-mediated STAT1/2 degradation."
  - target: 01-human/07-system/immune-system
    relation: damages
    note: "Measles causes profound immunosuppression lasting 2–3 years post-infection: direct lymphocyte killing, abolition of immunological memory (immune amnesia), ↓B cell plasma cell output; secondary bacterial pneumonia (S. pneumoniae, S. aureus) is the leading cause of measles mortality."
  - target: 01-human/06-organ/lung
    relation: damages
    note: "Measles-associated pneumonia occurs from direct viral bronchitis/pneumonitis plus secondary bacterial superinfection; in immunocompromised patients, giant cell pneumonia (Warthin-Finkeldey syncytia) is progressive and frequently fatal."
  - target: 01-human/07-system/measles
    relation: causes
    note: "Measles disease is caused by MeV (Morbillivirus); SLAM/CD150 tropism drives lymphoid spread and immune amnesia; nectin-4 tropism enables respiratory shedding; MMR vaccine confers >97% protection; SSPE is a fatal late complication from hypermutated persistent MeV in CNS neurons."
---

# Measles Virus

## Overview

Measles virus (MeV) is the causative agent of measles (rubeola), an acute highly contagious febrile exanthem and one of the most important vaccine-preventable diseases in human history. It belongs to the family **Paramyxoviridae**, genus **Morbillivirus**, and is a non-segmented, enveloped, negative-sense single-stranded RNA virus [^fields-virology]. With a basic reproduction number (R₀) of **12–18** — the highest confirmed among all studied human pathogens — measles spreads almost exclusively through the air, with virus-laden droplet nuclei persisting in enclosed spaces for up to two hours after an infectious individual has left [^mandell-principles].

MeV has only a **single serotype** and only a **single known natural reservoir: humans**. This makes global eradication theoretically achievable, though populations require ≥95% vaccine coverage to achieve herd immunity — a threshold frequently not met, leading to measles resurgences worldwide.

Beyond its acute febrile illness, MeV is uniquely notable for causing **immune amnesia**: a depletion of pre-existing immunological memory that can leave survivors susceptible to previously-mastered pathogens for two to three years after infection, a phenomenon now documented by serological and VDJ sequencing studies.

## Structure

### Virion Architecture

| Component | Description |
|:---|:---|
| **Envelope** | Lipid bilayer derived from host plasma membrane; ~100–300 nm diameter |
| **H protein (Haemagglutinin)** | Attachment glycoprotein; binds CD150/SLAM, Nectin-4, CD46 (vaccine strains); forms tetramers; no neuraminidase activity |
| **F protein (Fusion)** | Class I fusion protein; cleaved by furin into F1/F2 disulfide-linked heterodimer; β-sheet stalk + heptad repeat coiled-coil drives membrane fusion |
| **M protein (Matrix)** | Lines inner envelope face; coordinates assembly and budding |
| **N protein (Nucleoprotein)** | Encapsidates the genomic RNA; N-RNA forms helical ribonucleoprotein (RNP) |
| **P protein** | Polymerase cofactor; also encodes V and C proteins via RNA editing/alternative ORF |
| **L protein (Large)** | RNA-dependent RNA polymerase (RdRp); capped mRNA synthesis and genome replication |

### Genome Organisation

MeV has a single non-segmented ~16 kb (−)ssRNA genome encoding **6 structural genes** in the order: **3′-N-P/V/C-M-F-H-L-5′**. The P gene uniquely encodes three proteins — P (full-length transcript), V (via cotranscriptional editing, +1 G insertion), and C (alternative ORF) — all of which serve immune evasion roles.

### Receptor Binding Proteins

Three confirmed cellular receptors for MeV H protein:

| Receptor | Cell types | Role |
|:---|:---|:---|
| **CD150/SLAM** | Activated lymphocytes, monocytes, DCs, endothelial cells | Primary immune cell entry; high-affinity; wild-type and vaccine strains |
| **Nectin-4 (PVRL4)** | Basolateral surface of airway epithelial cells | Airborne egress; viral shedding from host |
| **CD46** | All nucleated cells | Vaccine strains (Edmonston) and laboratory-adapted strains ONLY; not used by wild-type clinical isolates |

## Infection Mechanism

### Entry and Initial Infection

1. **Respiratory exposure:** Infectious droplet nuclei reach the upper respiratory tract and, critically, the lower respiratory epithelium [^fields-virology].
2. **Dendritic cell infection:** Alveolar and submucosal DCs expressing **CD150/SLAM** are the first cells infected. MeV H protein engages CD150/SLAM; F protein triggers membrane fusion → viral RNP delivered to cytoplasm.
3. **Lymph node amplification:** Infected DCs migrate to regional lymph nodes, where they infect additional CD150/SLAM-expressing activated lymphocytes → massive viremia over ~4 days; prodromal phase.
4. **Epithelial shedding:** During viremia, MeV reaches the basolateral surface of airway epithelial cells where **Nectin-4** is expressed → apical shedding into respiratory secretions → contagion.
5. **Skin:** CD150-expressing immune cells in the dermis are infected; rash is immune-mediated (CD8+ T cell cytotoxicity + small vessel vasculitis).

### Replication Cycle

MeV replicates exclusively in the cytoplasm. The L protein synthesises capped, poly-adenylated mRNAs by a **transcription gradient** (3′ genes transcribed more abundantly than 5′ genes — N most abundant, L least). Genome replication proceeds via a positive-sense antigenome intermediate. New RNPs bud as enveloped virions from the plasma membrane.

### Immune Evasion

| Protein | Mechanism |
|:---|:---|
| **V protein** | Binds DDB1-Cullin4A E3 ubiquitin ligase → targets STAT1 and STAT2 for proteasomal degradation → blocks IFN-α/β and IFN-γ signalling |
| **C protein** | Binds STAT1; inhibits IFN-β promoter activation; counteracts RIG-I signalling |
| **N protein** | Binds MDA5; interferes with dsRNA sensing (innate pattern recognition) |
| **P protein** | Blocks IRF3 phosphorylation via STAT binding domain |

Together these proteins create a broad innate immune evasion window enabling the extreme R₀ of 12–18.

## Host Interactions

### Lymphocyte Depletion and Immune Amnesia

MeV directly infects **CD150+ activated lymphocytes** — both CD4+ T helper cells and B cells — via H-CD150 binding and F-mediated fusion. Infected lymphocytes undergo apoptosis; additionally, bystander lymphocytes are suppressed from proliferating by mechanisms including FasL upregulation and FcγR cross-linking on antigen-presenting cells [^mandell-principles].

The most clinically significant long-term consequence is **immune amnesia**: MeV depletes pre-existing memory B cells (plasma cells and circulating memory B cells) that carry immunological recall to previously-encountered pathogens. Studies using VDJ deep sequencing demonstrate that measles eliminates 11–73% of pre-existing B cell receptor diversity in unvaccinated children, leaving them susceptible to previously mastered pathogens for **2–3 years** post-infection [^fields-virology].

### Giant Cell (Syncytium) Formation

The F protein drives cell-cell fusion of CD150+ immune cells → **Warthin-Finkeldey multinucleated giant cells** in lymph nodes, lungs, and tonsils. These giant cells are the histological hallmark of measles and represent immunopathological fusion products rather than productive viral factories.

### The Rash

The maculopapular measles rash is **immune-mediated**, not due to direct viral cytolysis of skin cells. CD8+ cytotoxic T cells attacking MeV-infected dermal immune cells, together with MeV-induced endothelial activation (vasculitis), produce the characteristic cephalocaudal spreading exanthem.

## Connections

- **Infects** → [T-helper cell](../../../01-human/04-cellular/t-helper-cell/README.md): MeV H protein binds CD150/SLAM on activated CD4+ T cells as primary immune entry receptor; direct infection leads to apoptosis, lymphopenia, and suppression of T cell proliferation — the basis of post-measles immunosuppression lasting weeks to months.
- **Infects** → [Dendritic cell](../../../01-human/04-cellular/dendritic-cell/README.md): Lung DCs expressing CD150/SLAM are the first cells infected after respiratory exposure; MeV-infected DCs amplify viremia by seeding regional lymph nodes while failing to mount an effective IFN response due to V-protein-mediated STAT1/2 degradation.
- **Damages** → [Immune system](../../../01-human/07-system/immune-system/README.md): Measles causes profound immunosuppression lasting 2–3 years post-infection through direct lymphocyte killing, abolition of pre-existing immunological memory (immune amnesia), and reduced B cell plasma cell output; secondary bacterial pneumonia (S. pneumoniae, S. aureus) is the leading cause of measles mortality worldwide.
- **Damages** → [Lung](../../../01-human/06-organ/lung/README.md): Measles-associated pneumonia arises from direct viral bronchitis/pneumonitis plus secondary bacterial superinfection; in immunocompromised patients, giant cell pneumonia (Warthin-Finkeldey syncytia) is progressive and frequently fatal.
- `causes` → **[Measles](../../../01-human/07-system/measles/README.md)** — MV (Morbillivirus; R₀ 12-18) causes measles disease; SLAM/CD150 tropism drives lymphoid spread and immune amnesia; nectin-4 enables respiratory shedding; MMR vaccine confers >97% protection; hypermutated persistent MeV in CNS neurons causes SSPE.

## Pathology

### Clinical Course

| Phase | Timing | Features |
|:---|:---|:---|
| **Incubation** | Days 1–10 | Asymptomatic viral amplification |
| **Prodrome** | Days 10–14 | High fever (39–40 °C); 3 Cs: **C**ough, **C**oryza, **C**onjunctivitis |
| **Koplik spots** | Days 12–13 | Pathognomonic: white/blue-grey dots on erythematous buccal mucosa opposite molars; appear 1–2 days before the rash |
| **Exanthem** | Days 14–18 | Maculopapular rash — begins behind ears/hairline, spreads cephalocaudally; lasts 4–5 days; immune-mediated |
| **Recovery** | Days 18–21 | Fever resolves; rash fades; lymphopenia persists for weeks |

### Complications

| Complication | Notes |
|:---|:---|
| **Pneumonia** | Most common cause of measles death; giant cell pneumonia (immunocompromised) or secondary bacterial (S. pneumoniae, S. aureus, H. influenzae) |
| **Otitis media** | Most common acute complication in children |
| **Croup** | Laryngotracheobronchitis; hoarseness, stridor |
| **Acute measles encephalitis** | 1 in 1,000–2,000 cases; immune-mediated; high mortality/morbidity |
| **Measles inclusion body encephalitis (MIBE)** | Immunocompromised; rapid onset weeks to months post-infection; frequently fatal |
| **Subacute sclerosing panencephalitis (SSPE)** | Very rare (1:8,000–1:100,000); onset 6–15 years post-infection; hypermutated MeV RNA persists in CNS neurons → progressive encephalitis → dementia, myoclonus, death; uniformly fatal |
| **Immune amnesia** | Depletion of pre-existing memory B cells; 2–3 years of increased susceptibility to other pathogens |

### Epidemiology and Prevention

Before widespread vaccination, measles caused an estimated **2.6 million deaths annually**. With the MMR vaccine (live-attenuated Edmonston-Zagreb or Moraten strains; 2 doses ≥93% efficacy per dose), global measles deaths fell to ~136,000 in 2022 [^mandell-principles]. Achieving and sustaining **≥95% population coverage** is required for herd immunity given the extraordinary R₀.

### Treatment

There is no specific antiviral for measles. Management is supportive:
- **Vitamin A supplementation** (WHO-recommended in all hospitalised measles cases): reduces severity and mortality, especially in vitamin A-deficient populations by restoring mucosal immune function.
- **Ribavirin**: used off-label in SSPE and severe measles in immunocompromised patients; limited clinical evidence for efficacy in acute measles.
- **Antibiotics**: for confirmed secondary bacterial pneumonia or otitis media.

[^mandell-principles]: Bennett JE, Dolin R, Blaser MJ. *Mandell, Douglas, and Bennett's Principles and Practice of Infectious Diseases.* 9th ed. Elsevier; 2020.
[^fields-virology]: Knipe DM, Howley PM, eds. *Fields Virology.* 7th ed. Wolters Kluwer; 2021.
