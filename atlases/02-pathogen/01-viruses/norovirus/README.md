---
schema: pathogen-entry/v1
id: norovirus
name: Norovirus
atlas: 02-pathogen
scale: 01-viruses
status: draft
last_reviewed: 2026-06-05
summary: "Caliciviridae; non-enveloped icosahedral ssRNA virus (~7.7 kb). Binds HBGAs for cell entry; infective dose ~18 particles. Leading cause of foodborne illness globally (~685 million cases/year); 200,000 deaths/year. No approved antiviral or vaccine."
aliases: ["Norwalk virus", "NV", "stomach flu", "winter vomiting bug", "human calicivirus"]
sources:
  - id: mandell-principles
    type: textbook
    cite: "Bennett JE, Dolin R, Blaser MJ. Mandell, Douglas, and Bennett's Principles and Practice of Infectious Diseases. 9th ed. Elsevier; 2020."
    url: "https://www.elsevier.com/books/mandell-douglas-and-bennetts-principles-and-practice-of-infectious-diseases/bennett/978-0-323-48255-4"
    accessed: "2026-06-05"
  - id: murray-microbiology
    type: textbook
    cite: "Murray PR, Rosenthal KS, Pfaller MA. Medical Microbiology. 9th ed. Elsevier; 2021."
    url: "https://www.elsevier.com/books/medical-microbiology/murray/978-0-323-67378-4"
    accessed: "2026-06-05"
  - id: bartsch-2016-burden
    type: peer-reviewed
    cite: "Bartsch SM, Lopman BA, Ozawa S, Hall AJ, Lee BY. Global economic burden of norovirus gastroenteritis. PLoS ONE. 2016;11(4):e0151219."
    doi: "10.1371/journal.pone.0151219"
    pmid: "27049645"
    url: "https://doi.org/10.1371/journal.pone.0151219"
    accessed: "2026-06-05"
  - id: karst-2016-pathogenesis
    type: peer-reviewed
    cite: "Karst SM. The influence of commensal bacteria on infection with enteric viruses. Nat Rev Microbiol. 2016;14(4):197-204."
    doi: "10.1038/nrmicro.2015.25"
    pmid: "26775934"
    url: "https://doi.org/10.1038/nrmicro.2015.25"
    accessed: "2026-06-05"
  - id: vinjé-2015-taxonomy
    type: peer-reviewed
    cite: "Vinjé J. Advances in laboratory methods for detection and typing of norovirus. J Clin Microbiol. 2015;53(2):373-381."
    doi: "10.1128/JCM.01535-14"
    pmid: "25056323"
    url: "https://doi.org/10.1128/JCM.01535-14"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/07-system/digestive-system
    relation: damages
    note: "Norovirus disrupts digestive-system absorptive and secretory function causing acute gastroenteritis; outbreaks spread rapidly in closed settings via fomites, aerosolized vomitus, and contaminated food or water."
  - target: 01-human/06-organ/small-intestine
    relation: infects
    note: "Norovirus replicates in villus tip enterocytes of the proximal small intestine, causing villous blunting and transient malabsorption without the mucosal inflammation typical of bacterial enteropathogens."
  - target: 01-human/04-cellular/dendritic-cell
    relation: damages
    note: "Norovirus infects gut-associated dendritic cells, impairing antigen presentation and contributing to short-lived immunity that permits repeated reinfections across a lifetime with the same genogroup."
  - target: 01-human/07-system/immune-system
    relation: damages
    note: "Norovirus protease NS6 cleaves STAT1/STAT2, blocking interferon signalling and dampening innate immune responses, enabling high-titre replication before adaptive immunity can mount an effective clearance response."
---

# Norovirus

## Overview

Norovirus is a **non-enveloped, positive-sense single-stranded RNA virus** (family *Caliciviridae*, genus *Norovirus*) and the leading cause of acute gastroenteritis worldwide. The genus comprises at least 10 genogroups (GI–GX), of which genogroups **GI, GII, and GIV** infect humans. Genotype **GII.4** has dominated global circulations since the mid-1990s, periodically generating new pandemic variants through antigenic drift in the VP1 capsid protein [^vinjé-2015-taxonomy].

With approximately **685 million cases and 200,000 deaths per year** — the vast majority in children under 5 and the elderly in low-resource settings — norovirus accounts for a greater share of global foodborne illness mortality than any other pathogen [^bartsch-2016-burden]. It is the most common cause of epidemic gastroenteritis in healthcare facilities, cruise ships, schools, and military settings. The virus is extraordinarily infectious: the median **human infectious dose (HID50) is estimated at ~18 viral particles**, viral shedding in feces can exceed 10^11 particles per gram, and the virus survives on surfaces for days to weeks and resists many disinfectants.

Despite decades of intensive research, **no approved antiviral therapy or vaccine** exists for norovirus. The difficulty of propagating the virus in cell culture historically limited mechanistic research, though the development of murine norovirus (MNV) models, human intestinal enteroid (HIE) culture systems, and gnotobiotic pig models has greatly accelerated understanding of pathogenesis. Human challenge studies using the Norwalk strain (GI.1) have provided the most detailed human data on immunity and pathogenesis [^mandell-principles].

## Structure

| Component | Detail |
|:---|:---|
| **Genome** | ~7.7 kb positive-sense ssRNA; 3 ORFs |
| **ORF1** | Encodes non-structural polyprotein (NS1-7): VPg, 2C-like NTPase, NS6 protease (3Cpro), NS7 RNA-dependent RNA polymerase (RdRp) |
| **ORF2** | Major capsid protein VP1 (58 kDa); S (shell) and P (protruding) domains; P2 subdomain is hypervariable — site of HBGA binding and antibody neutralization |
| **ORF3** | Minor capsid protein VP2 (23 kDa); stabilizes VP1; required for capsid assembly |
| **Particle** | 38 nm icosahedral; T=3 symmetry; 180 copies of VP1 arranged as 90 dimers; no lipid envelope |
| **Entry receptor** | Histo-blood group antigens (HBGAs) on gut epithelium; also bile acids (GII.3) |

### Genogroup and Genotype Classification

Norovirus is classified by phylogenetic analysis of the VP1 P2 domain. GII.4 variants are designated by first detection year (e.g., GII.4 Sydney 2012, GII.4 Osaka 2022). Host susceptibility to GI.1 infection is strongly linked to secretor status (FUT2 gene): ~20% of humans are "non-secretors" (Lewis-negative, ABH-negative on gut mucosa) and are resistant to GI.1 but may be susceptible to other strains via alternative HBGA subtypes.

## Infection Mechanism

### 1. Attachment via HBGAs

The VP1 P2 subdomain binds **histo-blood group antigens (HBGAs)** — fucosylated glycoconjugates on the surface of intestinal epithelial cells and in secretions — as its primary attachment factor. Different norovirus strains exhibit distinct HBGA-binding specificity (e.g., GI.1 preferentially binds H type 1; GII.4 binds Lewis b and H3). HBGAs do not appear to mediate internalization per se but concentrate virus at the cell surface for engagement with the true entry receptor, which remains incompletely characterized [^karst-2016-pathogenesis].

### 2. Cell Entry and Replication

Following HBGA-mediated attachment, norovirus enters enterocytes via **receptor-mediated endocytosis**. Within the endosome, low pH and possible protease cleavage facilitate genome release. The positive-sense genome is directly translated by host ribosomes, producing the ORF1 polyprotein, which is autocatalytically cleaved by the NS6 3C-like protease into six non-structural proteins. The RdRp (NS7) replicates the genome via a negative-sense intermediate using the viral genome-linked protein (VPg) as the primer. New genomes are packaged into VP1/VP2 capsids and released by cell lysis [^mandell-principles].

### 3. Infectious Dose and Transmission

The HID50 of ~18 particles makes norovirus one of the most efficiently transmitted human pathogens. Routes include:
- **Fecal-oral** (most common): person-to-person contact, contaminated food (shellfish bioaccumulate virus), contaminated water
- **Vomitus aerosol**: aerosolized particles during vomiting events — a major driver of healthcare outbreaks
- **Environmental fomites**: virus persists on surfaces at room temperature for days; partial chlorine resistance at typical water-treatment concentrations

## Host Interactions

### Immune Evasion

Norovirus has evolved multiple strategies to antagonize the host innate immune response:

- **NS6 protease cleaves STAT1 and STAT2**, blocking interferon (IFN) signaling downstream of both IFN-α/β receptor and IFN-γ receptor, preventing transcription of interferon-stimulated genes (ISGs) [^karst-2016-pathogenesis]
- **NS3 NTPase** has been implicated in disrupting NF-κB signaling in some models
- **Gut microbiota interactions**: Murine norovirus persistence requires commensal bacteria; bacterial LPS and HBGA-expressing bacteria may enhance human norovirus attachment, implicating the microbiome in susceptibility

### Cell Tropism and Immunity

Norovirus primarily infects **villus tip enterocytes** in the proximal small intestine. In human challenge models, biopsy-confirmed infection shows villous blunting without significant inflammatory infiltrate, explaining the rapid onset (12–48 h) and spontaneous resolution (24–72 h) of symptoms in immunocompetent adults. Immunity is strain-specific, short-lived (6–24 months), and incomplete — individuals can be repeatedly reinfected, particularly by new GII.4 variants. Serum IgA and blocking antibody titers against VP1 correlate with protection in challenge studies [^mandell-principles].

## Pathology

### Disease Spectrum

| Presentation | Typical Host | Key Features |
|:---|:---|:---|
| Acute self-limited gastroenteritis | Healthy adults, older children | Nausea, vomiting, watery non-bloody diarrhea, low-grade fever; resolves 24–72 h |
| Severe dehydrating diarrhea | Children <5, elderly | Significant morbidity; requires oral rehydration therapy (ORT) or IV fluids |
| Prolonged/chronic infection | Immunocompromised (transplant, HIV, primary immunodeficiency) | Weeks to months of diarrhea; evolving viral quasi-species detected in serial stool samples |
| Asymptomatic shedding | Any age | Common; prolongs outbreak transmission |

### Pathophysiology of Diarrhea

Villous blunting reduces the absorptive surface area and brush-border enzyme (lactase, sucrase) activity, producing an **osmotic component** to diarrhea from undigested carbohydrates. Secretory mechanisms are also activated: norovirus has been proposed to trigger enteroendocrine cell mediators (5-HT, substance P) that stimulate intestinal fluid secretion and activate the enteric nervous system to induce vomiting via vagal afferents [^karst-2016-pathogenesis].

### Treatment

No antiviral therapy is approved. Nitazoxanide has shown marginal benefit in immunocompetent patients in one RCT. Management is supportive:
- **Oral rehydration therapy (ORT)** — WHO low-osmolarity ORS solution is first-line
- **IV fluids** for severe dehydration or inability to tolerate oral intake
- **Antiemetics** (ondansetron) in selected patients
- **Infection control**: alcohol-based hand rubs are less effective than soap-and-water for norovirus; bleach disinfection (≥1000 ppm) of contaminated surfaces

## Connections

- **Damages** → [Digestive System](../../../01-human/07-system/digestive-system/README.md): Norovirus disrupts digestive-system absorptive and secretory function causing acute gastroenteritis; outbreaks spread rapidly in closed settings via fomites, aerosolized vomitus, and contaminated food or water.
- **Infects** → [Small Intestine](../../../01-human/06-organ/small-intestine/README.md): Norovirus replicates in villus tip enterocytes of the proximal small intestine, causing villous blunting and transient malabsorption without the mucosal inflammation typical of bacterial enteropathogens.
- **Damages** → [Dendritic Cell](../../../01-human/04-cellular/dendritic-cell/README.md): Norovirus infects gut-associated dendritic cells, impairing antigen presentation and contributing to short-lived immunity that permits repeated reinfections across a lifetime with the same genogroup.
- **Damages** → [Immune System](../../../01-human/07-system/immune-system/README.md): Norovirus protease NS6 cleaves STAT1/STAT2, blocking interferon signalling and dampening innate immune responses, enabling high-titre replication before adaptive immunity can mount an effective clearance response.

---

> **AI co-maintenance notice:** This entry was drafted with AI assistance and is subject to expert review. Content reflects published literature as of the last_reviewed date. Errors may be present; verify critical facts against primary sources before clinical or research use.

[^mandell-principles]: Bennett JE, Dolin R, Blaser MJ. *Mandell, Douglas, and Bennett's Principles and Practice of Infectious Diseases.* 9th ed. Elsevier; 2020.
[^murray-microbiology]: Murray PR, Rosenthal KS, Pfaller MA. *Medical Microbiology.* 9th ed. Elsevier; 2021.
[^bartsch-2016-burden]: Bartsch SM, Lopman BA, Ozawa S, Hall AJ, Lee BY. Global economic burden of norovirus gastroenteritis. *PLoS ONE.* 2016;11(4):e0151219. [doi:10.1371/journal.pone.0151219](https://doi.org/10.1371/journal.pone.0151219) · [PubMed 27049645](https://pubmed.ncbi.nlm.nih.gov/27049645/)
[^karst-2016-pathogenesis]: Karst SM. The influence of commensal bacteria on infection with enteric viruses. *Nat Rev Microbiol.* 2016;14(4):197-204. [doi:10.1038/nrmicro.2015.25](https://doi.org/10.1038/nrmicro.2015.25) · [PubMed 26775934](https://pubmed.ncbi.nlm.nih.gov/26775934/)
[^vinjé-2015-taxonomy]: Vinjé J. Advances in laboratory methods for detection and typing of norovirus. *J Clin Microbiol.* 2015;53(2):373-381. [doi:10.1128/JCM.01535-14](https://doi.org/10.1128/JCM.01535-14) · [PubMed 25056323](https://pubmed.ncbi.nlm.nih.gov/25056323/)
