---
schema: pathogen-entry/v1
id: epstein-barr-virus
name: Epstein-Barr Virus
atlas: 02-pathogen
scale: 01-viruses
status: draft
last_reviewed: 2026-06-05
summary: "Gammaherpesvirinae; dsDNA ~170 kb; enveloped. Infects B cells via CD21. Causes infectious mononucleosis; establishes latency in memory B cells. Associated with Burkitt lymphoma, Hodgkin lymphoma, NPC, PTLD, and gastric carcinoma."
aliases: ["EBV", "HHV-4", "human herpesvirus 4", "lymphocryptovirus", "EBV-1", "EBV-2"]
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
  - target: 01-human/04-cellular/b-cell
    relation: infects
    note: "EBV infects B cells via gp350/220 binding CD21 (CR2); gHgL mediates membrane fusion; LMP1 (CD40 mimic, NF-κB activation), LMP2A (BCR mimic), and EBNA-2 (Notch mimic) drive polyclonal B cell immortalisation (Latency III)."
  - target: 01-human/07-system/immune-system
    relation: damages
    note: "EBV-driven B cell immortalisation triggers massive CD8+ CTL expansion in IM (atypical lymphocytes); CTL-mediated immunopathology causes pharyngitis, lymphadenopathy, splenomegaly; immune evasion via EBNA-1 GA repeat (avoids MHC-I presentation)."
  - target: 01-human/06-organ/liver
    relation: damages
    note: "EBV-associated hepatitis in ~80% of IM cases (elevated ALT/AST, rarely jaundice); EBV infects periportal hepatocytes; atypical lymphocyte infiltrates in portal tracts; fulminant hepatic failure rare; anti-i haemolytic anaemia compounds liver dysfunction."
  - target: 01-human/04-cellular/dendritic-cell
    relation: infects
    note: "EBV can infect plasmacytoid and myeloid DCs; DCs present EBV antigens via MHC-II to CD4+ Tfh and MHC-I to CD8+ CTLs; LMP1 in DCs activates NF-κB → ↑IL-6, IL-10, IL-12 altering DC maturation and T cell polarisation."
---

# Epstein-Barr Virus

## Overview

Epstein-Barr virus (EBV), formally human herpesvirus 4 (HHV-4), is a gammaherpesvirus with worldwide prevalence exceeding **95% in adults** — one of the most successful human pathogens in terms of host penetrance. It belongs to the subfamily **Gammaherpesvirinae**, genus **Lymphocryptovirus**, and is the only known human lymphotropic herpesvirus with proven oncogenic potential [^fields-virology].

EBV was discovered in 1964 by Epstein, Barr, and Achong in cultured Burkitt lymphoma cells — the first human virus demonstrated to be causally linked to a cancer. It has since been associated with a spectrum of malignancies: **Burkitt lymphoma** (BL), **Hodgkin lymphoma** (HL), **nasopharyngeal carcinoma** (NPC), **post-transplant lymphoproliferative disorder** (PTLD), EBV-positive diffuse large B-cell lymphoma, and **EBV-associated gastric carcinoma** [^mandell-principles].

In immunocompetent individuals, primary infection causes **infectious mononucleosis (IM)** — the "kissing disease" of young adults — a self-limiting condition characterised by pharyngitis, cervical lymphadenopathy, splenomegaly, and a vigorous CD8+ T cell response. After resolution of IM, EBV establishes lifelong latency in the resting memory B cell pool, where it persists with minimal gene expression detectable by immune surveillance.

## Structure

### Virion Architecture

| Component | Description |
|:---|:---|
| **Envelope** | Host-derived lipid bilayer; ~200 nm diameter |
| **gp350/220** | Major envelope glycoprotein; binds CD21 (complement receptor 2/CR2) on B cells; immunodominant antibody target |
| **gHgL** | Fusion helper complex; also binds αv integrins on epithelial cells; required for membrane fusion |
| **BMRF2** | Envelope protein; binds β1/β5 integrins; aids epithelial cell attachment |
| **gB** | Fusion glycoprotein |
| **Tegument** | Contains BNRF1 (immunoevasin), BGLF2, VP16-like transactivators |
| **Capsid** | Icosahedral; houses dsDNA genome |

### Genome Organisation

EBV genome is **~170–180 kb dsDNA** encoding 80+ genes. The genome contains **terminal repeats (TR)** flanking a unique region. Two subtypes exist (EBV-1/EBV-2, distinguished by EBNA-2/3 sequence variation) with EBV-1 predominating globally and having stronger B cell immortalising capacity.

Key oncogenic and latency proteins:

| Protein/RNA | Gene | Function |
|:---|:---:|:---|
| **EBNA-1** | BKRF1 | Episomal maintenance (ori-P binding); GA repeat domain blocks proteasomal processing → MHC-I presentation evasion; expressed in all EBV+ tumours |
| **EBNA-2** | BYRF1 | Notch pathway mimic; binds RBP-Jκ → drives c-Myc, cyclin D2, CD23, LMP1 transcription; required for B cell immortalisation in Latency III |
| **LMP1** | BNLF1 | 6-TM domain oncoprotein; constitutive NF-κB activation (CTAR1: TRAF2/3/5/6; CTAR2: TRADD, IRAK1); functional CD40 mimic; ↑Bcl-2, ↑XIAP → anti-apoptotic; activates JAK-STAT and PI3K-Akt |
| **LMP2A/2B** | BLLF2/3 | ITAM-containing TM proteins; LMP2A mimics constitutive BCR signalling → B cell survival without antigen stimulation |
| **EBER1/2** | non-coding RNA | Most abundant viral transcripts in latently infected cells; activate innate sensors (RIG-I, TLR3); block PKR → prevent IFN-induced apoptosis |
| **BART miRNAs** | ~44 miRNAs | Suppress MHC-I antigen presentation; suppress pro-apoptotic signals (target BIM/BCL2L11); regulate viral and host gene expression |
| **BHRF1 miRNAs** | ~3 miRNAs | Targets BIM; Bcl-2 homologue; anti-apoptotic during lytic replication |

## Infection Mechanism

### Entry into B Cells and Epithelial Cells

**B cell entry:**
1. **gp350/220** binds **CD21 (CR2)** on B cells; CD35 co-receptor stabilises attachment.
2. **gHgL** engages an as-yet uncharacterised B cell receptor → triggers membrane fusion mediated by gB.
3. Naked capsid released into cytoplasm → nuclear pore import → circularisation into episome.

**Epithelial cell entry (oropharynx, salivary glands):**
1. **gHgL** binds **αv integrins** (αvβ5, αvβ6, αvβ8) on epithelial cells → attachment.
2. **BMRF2** binds β1 and β5 integrins → additional stabilisation.
3. gB mediates fusion; epithelial replication produces infectious virions shed into saliva [^fields-virology].

### Latency Programmes

EBV adopts distinct latency programmes depending on the cellular context, each characterised by expression of a defined subset of latency genes. This allows EBV to maintain persistence while minimising antigen exposure to immune surveillance:

| Latency Programme | Genes expressed | Associated disease |
|:---:|:---|:---|
| **Latency 0** | None (only BARTs) | Resting memory B cells — normal persistence |
| **Latency I** | EBNA-1 only | Burkitt lymphoma; minimal immunogenic targets |
| **Latency II** | EBNA-1, LMP1, LMP2A, EBERs, BARTs | EBV+ Hodgkin lymphoma, nasopharyngeal carcinoma, EBV+ gastric carcinoma |
| **Latency III** | All 9 EBNAs + LMPs + EBERs + BARTs | Post-transplant lymphoproliferative disorder, DLBCL in immunocompromised, infectious mononucleosis |

### The Lytic Cycle

Reactivation from latency (triggered by B cell differentiation signals, BCR crosslinking, or TGF-β withdrawal) initiates the lytic cycle:
1. **BZLF1 (Zta/ZEBRA):** key lytic switch transactivator; binds ZREs (Zta response elements) in immediate-early gene promoters.
2. **BRFL1 (Rta):** co-activator; together with Zta drives lytic gene cascade.
3. Viral DNA replication, capsid assembly, secondary envelopment → release of infectious virions.

Lytic replication is required for horizontal transmission (via saliva) but is actively suppressed in latently infected memory B cells by epigenetic silencing of BZLF1.

## Host Interactions

### B Cell Immortalisation

In the immunocompetent host, EBV drives newly infected B cells into a **Latency III programme** (growth programme) with all latency genes expressed. This mimics physiological B cell activation signals:
- **EBNA-2** → Notch signalling → c-Myc, cyclin D2 → cell cycle entry
- **LMP1** → constitutive CD40 → NF-κB → survival, proliferation, Bcl-2 upregulation
- **LMP2A** → constitutive BCR → PI3K-Akt → survival without antigen

The resulting polyclonal blast transformation is countered by an overwhelming **CD8+ cytotoxic T lymphocyte (CTL) response** in IM — the atypical lymphocytes (10–70% of peripheral WBCs) seen on the blood film are largely VZV-reactive EBV-specific CTLs. This CTL response, together with NK cells, eliminates most infected B cell blasts and pushes surviving EBV+ cells into the silent Latency 0 state in resting memory B cells [^mandell-principles].

### Immune Evasion

| Mechanism | Detail |
|:---|:---|
| **EBNA-1 GA repeat domain** | ~800–1,800 bp glycine-alanine encoding region resists ubiquitin-proteasome degradation → peptides not presented by MHC-I → EBNA-1 is the only Latency I protein and is therefore invisible to CD8+ CTLs |
| **EBER-mediated PKR blockade** | EBERs bind and sequester PKR → prevent eIF2α phosphorylation → blunt IFN-induced translational shutdown |
| **BART miRNA-mediated MHC-I suppression** | BART6-5p and related miRNAs target the DICER-processing pathway; multiple BARTs suppress antigen presentation |
| **BHRF1 (viral Bcl-2)** | Anti-apoptotic Bcl-2 homologue; expressed during lytic replication; prevents premature apoptosis of infected cells |
| **IL-10 homologue (BCRF1/vIL-10)** | EBV encodes a viral IL-10 homologue; suppresses Th1 responses and NK cell activation |

## Connections

- **Infects** → [B cell](../../../01-human/04-cellular/b-cell/README.md): EBV infects B cells via gp350/220 binding CD21 (CR2); gHgL mediates membrane fusion; LMP1 (constitutive CD40/NF-κB), LMP2A (BCR mimic), and EBNA-2 (Notch mimic) drive polyclonal B cell immortalisation in Latency III — the basis of infectious mononucleosis and B cell malignancies.
- **Damages** → [Immune system](../../../01-human/07-system/immune-system/README.md): EBV-driven B cell immortalisation triggers massive CD8+ CTL expansion in infectious mononucleosis (atypical lymphocytosis); CTL-mediated immunopathology causes pharyngitis, lymphadenopathy, and splenomegaly; EBNA-1 GA repeat evades MHC-I surveillance enabling lifelong latency.
- **Damages** → [Liver](../../../01-human/06-organ/liver/README.md): EBV-associated hepatitis occurs in ~80% of IM cases (elevated ALT/AST, rarely jaundice); periportal hepatocyte infection and atypical lymphocyte infiltration in portal tracts; fulminant hepatic failure is rare; anti-i IgM haemolytic anaemia (anti-cold agglutinin) compounds hepatic dysfunction.
- **Infects** → [Dendritic cell](../../../01-human/04-cellular/dendritic-cell/README.md): EBV infects plasmacytoid and myeloid DCs; DCs present EBV antigens via MHC-II to CD4+ T follicular helper cells and via MHC-I to CD8+ CTLs; LMP1 expression in DCs activates NF-κB → altered secretion of IL-6, IL-10, and IL-12, shaping T cell polarisation.

## Pathology

### Infectious Mononucleosis

| Feature | Detail |
|:---|:---|
| **Transmission** | Saliva (kissing disease); also blood transfusion, organ transplant |
| **Age at peak incidence** | 15–25 years (developing countries: childhood, usually subclinical) |
| **Classic triad** | Pharyngitis + cervical lymphadenopathy + fever |
| **Splenomegaly** | ~50% of cases; avoid contact sports for 3–4 weeks (splenic rupture risk) |
| **Atypical lymphocytes** | 10–70% of WBCs; EBV-specific CD8+ CTLs; Downey type II lymphocytes |
| **Heterophile antibodies** | IgM antibodies (Monospot/Paul-Bunnell); agglutinate sheep/horse RBCs; 85% sensitivity; negative early in disease and in children <5 years |
| **Specific serology** | VCA-IgM (acute), VCA-IgG (lifelong), EBNA-IgG (appears ~6 weeks, persists lifelong) |
| **Ampicillin/amoxicillin rash** | Maculopapular rash in ~80% of IM patients given ampicillin/amoxicillin — drug-EBV-lymphocyte interaction |

### Complications of IM

| Complication | Details |
|:---|:---|
| **Splenic rupture** | Rare but life-threatening; avoid strenuous activity and contact sports for 3–4 weeks |
| **Airway obstruction** | Tonsillar hypertrophy → ± peritonsillar abscess; may require corticosteroids or intubation |
| **Haematological** | Autoimmune haemolytic anaemia (anti-i IgM cold agglutinin), thrombocytopenia, neutropenia |
| **Neurological** | Encephalitis (rare), Guillain-Barré syndrome, Bell's palsy, optic neuritis, transverse myelitis |
| **Cardiac** | Myocarditis (rare, ~1%) |

### EBV-Associated Malignancies

| Malignancy | EBV association | Latency | Key molecular event |
|:---|:---:|:---:|:---|
| **Burkitt lymphoma (BL)** | 95% endemic; 15–20% sporadic | I | c-Myc translocation t(8;14)/t(8;22)/t(2;8); c-Myc drives uncontrolled proliferation; CHOP/BFM chemotherapy |
| **Hodgkin lymphoma (HL)** | ~40% mixed cellularity | II | LMP1/LMP2 in Reed-Sternberg cells; NF-κB-driven survival |
| **Nasopharyngeal carcinoma (NPC)** | ~100% undifferentiated types | II | EBER+, LMP1/2+; high incidence Southern China, N. Africa, Inuit; radiosensitive |
| **PTLD** | >90% | III | Unrestricted Latency III after T cell immunosuppression; treat by reducing IS ± rituximab |
| **EBV+ gastric carcinoma** | ~9% of gastric cancers | I/II | Extreme CpG island methylation, PIK3CA mutation |
| **CAEBV** | 100% | II/III | T/NK cell EBV infection; haemophagocytic syndrome; rare; allogeneic HSCT only curative option |

### Treatment

There is no approved antiviral for EBV that has proven clinical efficacy in well-powered trials. Specific approaches:
- **Infectious mononucleosis:** Supportive care; corticosteroids for severe airway compromise or haematological complications; avoid ampicillin/amoxicillin.
- **PTLD:** Reduce immunosuppression; rituximab (anti-CD20 → depletes EBV+ B cells); chemotherapy for resistant cases; EBV-specific CTL infusions.
- **EBV-associated cancers:** Standard tumour-directed therapy; EBV-specific immunotherapy (CTL therapy) in clinical trials for NPC and PTLD.
- **Antivirals (aciclovir/ganciclovir):** Active against lytic-phase replication (VCA+ cells) but not against latently infected cells (which carry the transforming latency programme); no proven benefit in IM or EBV-associated malignancies.

[^mandell-principles]: Bennett JE, Dolin R, Blaser MJ. *Mandell, Douglas, and Bennett's Principles and Practice of Infectious Diseases.* 9th ed. Elsevier; 2020.
[^fields-virology]: Knipe DM, Howley PM, eds. *Fields Virology.* 7th ed. Wolters Kluwer; 2021.
