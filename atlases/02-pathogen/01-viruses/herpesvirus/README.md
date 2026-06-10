---
schema: pathogen-entry/v1
id: herpesvirus
name: Herpesviridae
atlas: 02-pathogen
scale: 01-viruses
status: draft
last_reviewed: 2026-06-06
summary: "Family of enveloped dsDNA viruses (~150–230 nm) with icosahedral capsid, tegument, and lipid envelope. Nine human herpesviruses. Defining trait: lifelong latency as nuclear episomes. Reactivation driven by immune suppression, UV, or stress."
aliases: ["herpesvirus", "human herpesvirus", "HHV", "Herpesviridae family", "alphaherpesvirinae", "betaherpesvirinae", "gammaherpesvirinae"]
sources:
  - id: roizman-fields-virology
    type: textbook
    cite: "Knipe DM, Howley PM, eds. Fields Virology. 7th ed. Wolters Kluwer; 2021. Section on Herpesviridae."
    url: "https://www.lww.com/product/9781975112547"
  - id: davison-2009-herpesvirus-evolution
    type: peer-reviewed
    cite: "Davison AJ, Eberle R, Ehlers B, et al. The order Herpesvirales. Arch Virol. 2009;154(1):171-177."
    doi: "10.1007/s00705-008-0278-4"
    pmid: "19066710"
    url: "https://doi.org/10.1007/s00705-008-0278-4"
  - id: whitley-2001-herpes-latency
    type: peer-reviewed
    cite: "Whitley RJ, Roizman B. Herpes simplex virus infections. Lancet. 2001;357(9267):1513-1518."
    doi: "10.1016/S0140-6736(00)04638-9"
    pmid: "11377626"
    url: "https://doi.org/10.1016/S0140-6736(00)04638-9"
cross_links:
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "VZV (HHV-3) is an Alphaherpesvirinae member of this family; establishes latency in dorsal root and cranial nerve ganglia; reactivates as herpes zoster (shingles)."
  - target: 02-pathogen/01-viruses/epstein-barr-virus
    relation: connects-to
    note: "EBV (HHV-4) is a Gammaherpesvirinae member; establishes latency in memory B cells; associated with infectious mononucleosis and multiple lymphoid malignancies."
  - target: 01-human/04-cellular/neuron
    relation: targets
    note: "HSV-1, HSV-2, and VZV establish latency in sensory neurons (dorsal root ganglia, trigeminal ganglia); viral genomes persist as circular episomes in the nucleus without productive infection."
  - target: 03-medicine/01-modern/05-antiviral/acyclovir
    relation: treated-by
    note: "Acyclovir (valacyclovir prodrug) is first-line therapy for HSV-1, HSV-2, and VZV infections; selectivity depends on 3000-fold preferential phosphorylation by viral TK (UL23/ORF36); VZV TK less efficient, requiring higher doses; foscarnet for TK-deficient resistant strains."
  - target: 01-human/07-system/immune-system
    relation: damages
    note: "All nine human herpesviruses encode dedicated immune evasion genes: HSV ICP47/CMV US6 block MHC-I via TAP inhibition; CMV UL16-21 downregulate NKG2D ligands; all subfamilies antagonize IFN signaling (PKR, IRF3, STING); latency renders infected cells invisible to CTLs."
  - target: 01-human/04-cellular/b-cell
    relation: infects
    note: "EBV (HHV-4) establishes latency in memory B cells via EBNA-1-mediated episome maintenance and LMP1/LMP2A mimicking activated B cell receptors; Gammaherpesvirinae-driven B cell transformation underlies Burkitt lymphoma, Hodgkin lymphoma, PTLD, and NPC."
---

# Herpesviridae

## Overview

Herpesviridae is a large family of enveloped double-stranded DNA viruses that share a highly conserved virion architecture and a defining biological property: the ability to establish **lifelong latency** in host cells. The family is divided into three subfamilies based on biological properties, host range, and phylogeny:

| Subfamily | Members | Primary latency site |
|:---|:---|:---|
| **Alphaherpesvirinae** | HSV-1 (HHV-1), HSV-2 (HHV-2), VZV (HHV-3) | Sensory neurons (DRG, trigeminal ganglia) |
| **Betaherpesvirinae** | CMV (HHV-5), HHV-6A, HHV-6B, HHV-7 | Monocytes, myeloid progenitors, salivary glands |
| **Gammaherpesvirinae** | EBV (HHV-4), KSHV (HHV-8) | Memory B cells (EBV); B/endothelial cells (KSHV) |

The nine human herpesviruses collectively infect the vast majority of the human population: **HSV-1 seroprevalence exceeds 50–80%** in most adult populations, **VZV approaches 100%** in adults without vaccination, and **EBV exceeds 95%** in adults worldwide [^roizman-fields-virology].

## Structure

### Virion Architecture

All herpesviruses share a conserved four-layer structure [^davison-2009-herpesvirus-evolution]:

1. **Icosahedral capsid** (~100–125 nm): T=16 icosahedral capsid assembled in the nucleus; contains the dsDNA genome wound around a protein core (the scaffold). Major capsid protein (MCP/UL19 in HSV) plus a pentonless penton at 11 of 12 vertices; portal complex at the 12th vertex (genome packaging).

2. **Tegument** (~200+ proteins in CMV/HSV): Amorphous proteinaceous layer between capsid and envelope. Contains viral regulatory proteins delivered immediately upon entry (VHS in HSV degrades host mRNAs; pp65 of CMV blocks antigen presentation; VP16 of HSV transactivates immediate-early genes). Tegument proteins vary by subfamily and subfamily-specific biology.

3. **Lipid envelope**: Derived from host cell membranes (trans-Golgi network and endosomal compartments) during secondary envelopment. Houses multiple glycoproteins required for cell attachment and fusion.

4. **Envelope glycoproteins**: A conserved core fusion machinery — gB (fusion), gH, gL — is shared across the family. Receptor-binding glycoproteins are subfamily-specific (gC/gD in HSV; gp350/220 in EBV).

### Genome Organisation

| Property | Detail |
|:---|:---|
| **Type** | Linear dsDNA; circularises immediately upon nuclear entry |
| **Size** | ~125 kb (HSV-1, VZV) to ~230 kb (CMV) |
| **Structure** | Unique long (UL) and unique short (US) regions flanked by inverted repeat sequences; CMV has unique features (b sequence, etc.) |
| **Latency form** | Circular episome (not integrated) maintained in host cell nucleus; replicated by host DNA polymerase as cells divide (EBV) or maintained in non-dividing neurons (HSV/VZV) |
| **Gene count** | ~70 genes (VZV) to ~230+ genes (CMV); conserved core of ~40 genes across subfamilies |

## Infection Mechanism

### Lytic Replication

All herpesviruses follow a common lytic gene expression cascade, though specific proteins differ:

1. **Attachment**: Envelope glycoproteins engage host surface molecules (HSV gC/gD → heparan sulfate and HVEM/nectin; EBV gp350 → CD21; CMV gB → PDGFR/integrins).
2. **Fusion and nuclear import**: gB/gH/gL mediate viral envelope fusion with the cell or endosomal membrane; capsid is transported to the nuclear pore; viral DNA is injected into the nucleus.
3. **Immediate-early (IE) gene expression**: Tegument transactivators (e.g., VP16, pp71) activate IE genes (ICP0, ICP4 in HSV; IE1/IE2 in CMV) without de novo protein synthesis.
4. **Early gene expression**: DNA replication machinery (DNA polymerase, helicase-primase, single-strand binding protein); these are encoded by early genes.
5. **DNA replication**: Viral DNA polymerase replicates the genome; progeny genomes accumulate in the nucleus.
6. **Late gene expression**: Structural proteins (capsid, tegument, envelope glycoproteins) synthesized.
7. **Assembly and egress**: Capsid assembly in the nucleus → primary envelopment at inner nuclear membrane → de-envelopment → secondary envelopment at TGN → exocytosis.

### Establishment of Latency

The defining feature of herpesviruses is their ability to transition from lytic to **latent infection** — a state where:
- Viral DNA persists as a **circular nuclear episome**
- Lytic gene expression is suppressed (by viral and host epigenetic mechanisms)
- Only a small subset of viral genes is expressed (Latency Associated Transcripts in HSV; EBNAs/LMPs in EBV)
- The cell survives indefinitely; the immune system cannot eliminate infection

**Latency mechanisms by subfamily:**
- **Alphaherpesvirinae (HSV/VZV)**: LAT (Latency Associated Transcript) is the major transcript in latently infected neurons; LAT RNA promotes neuronal survival and prevents apoptosis; viral genome is maintained by epigenetic silencing (heterochromatin deposition on lytic promoters).
- **Gammaherpesvirinae (EBV)**: EBNA-1 binds episomal origin of plasmid replication (oriP) to maintain the genome through cell division; multiple latency programmes (0–III) allow viral persistence with variable immune recognition.
- **Betaherpesvirinae (CMV)**: Latency in CD34+ hematopoietic progenitors; LUNA (latency unique nuclear antigen) and UL138 maintain latent state.

### Reactivation

Reactivation from latency is triggered by stimuli that alter the cellular or systemic immune environment:

| Trigger | Affected virus | Mechanism |
|:---|:---|:---|
| UV radiation (sunlight) | HSV-1 | Induces NGF withdrawal, JNK signalling, HSP70 expression in neurons → lytic cycle re-entry |
| Systemic immunosuppression | All HHVs (especially CMV, EBV, VZV) | Loss of CD8+ T cell surveillance → reactivation; seen post-transplant, HIV, chemotherapy |
| Physical/emotional stress | HSV-1/2, VZV | Corticosteroid-mediated epigenetic changes in neurons; sympathetic activation |
| Fever/illness | HSV-1 (febrile blisters) | Elevated temperature + systemic inflammation alter LAT/lytic promoter balance |
| Aging | VZV (herpes zoster) | Waning CD4+ T cell immunity to VZV; zoster incidence rises sharply after age 50 |

## Host Interactions

### Immune Evasion — Shared Strategies

All human herpesviruses encode multiple dedicated immune evasion genes, the diversity and sophistication of which is unmatched outside poxviruses [^whitley-2001-herpes-latency]:

| Mechanism | Family members | Target |
|:---|:---|:---|
| MHC-I downregulation | HSV ICP47, CMV US6, US11 | Block TAP (transporter associated with antigen processing) → prevent peptide loading → reduced CD8+ T cell recognition |
| IFN antagonism | All; VZV ORF47 kinase, CMV TRS1/IRS1 | Block PKR, IRF3, STING, or JAK-STAT signalling |
| NK cell evasion | CMV UL16-21, UL40; HSV gC | Downregulate NKG2D ligands; express MHC-I mimics |
| Complement evasion | HSV gC, CMV gp68 | Complement component capture/degradation |
| Apoptosis inhibition | HSV US3 kinase, BHRF1 (EBV), vIAP (CMV) | Block caspase activation; promote infected cell survival |

### Antiviral Drug Targets

The shared enzyme machinery of herpesviruses — particularly the **viral DNA polymerase** (UL30 in HSV) and **thymidine kinase** (UL23 in HSV) — provides selective drug targets:

| Drug | Mechanism | Spectrum |
|:---|:---|:---|
| Aciclovir/valaciclovir | Viral TK phosphorylation → DNA polymerase chain terminator | HSV-1, HSV-2, VZV |
| Ganciclovir/valganciclovir | Viral kinase (pUL97 in CMV) phosphorylation → DNA polymerase inhibition | CMV, also HSV |
| Foscarnet | Pyrophosphate analogue; inhibits viral DNA polymerase directly (TK-independent) | CMV, HSV (TK-resistant), VZV |
| Letermovir | CMV terminase complex (pUL51/pUL56/pUL89) inhibition | CMV-specific; prophylaxis in transplant recipients |

## Connections

- `connects-to` → **[Varicella-Zoster Virus](../varicella-zoster-virus/README.md)** — VZV (HHV-3) is the Alphaherpesvirinae member responsible for varicella and herpes zoster; establishes latency in dorsal root and cranial nerve ganglia.
- `connects-to` → **[Epstein-Barr Virus](../epstein-barr-virus/README.md)** — EBV (HHV-4) is the Gammaherpesvirinae member causing infectious mononucleosis and associated with Burkitt lymphoma, Hodgkin lymphoma, and NPC.
- `targets` → **[Neuron](../../../01-human/04-cellular/neuron/README.md)** — HSV-1, HSV-2, and VZV establish lifelong latency in sensory neurons (dorsal root and trigeminal ganglia) as circular episomal genomes.
- `treated-by` → **[Acyclovir](../../../../03-medicine/01-modern/05-antiviral/acyclovir/README.md)** — acyclovir (valacyclovir prodrug) is first-line for HSV-1, HSV-2, and VZV; 3000-fold selective viral TK phosphorylation; ACV-TP chain-terminates viral DNA polymerase; foscarnet for TK-deficient resistant strains.
- `damages` → **[Immune System](../../../01-human/07-system/immune-system/README.md)** — dedicated immune evasion genes include MHC-I downregulation (HSV ICP47/CMV US6), NKG2D ligand downregulation (CMV UL16-21), and IFN antagonism (PKR, IRF3, STING); latency renders infected cells invisible to CTLs.
- `infects` → **[B Cell](../../../01-human/04-cellular/b-cell/README.md)** — EBV establishes latency in memory B cells via EBNA-1/LMP1/LMP2A; drives Burkitt lymphoma, Hodgkin lymphoma, PTLD, and NPC; KSHV infects B cells causing primary effusion lymphoma.

## Pathology

### Clinical Diseases by Member

| Virus | Primary disease | Latency disease | Oncogenic |
|:---|:---|:---|:---:|
| **HSV-1 (HHV-1)** | Oral herpes (cold sores), keratitis, encephalitis | Recurrent oral/labial lesions | No |
| **HSV-2 (HHV-2)** | Genital herpes | Recurrent genital ulcers, neonatal HSV | No |
| **VZV (HHV-3)** | Varicella (chickenpox) | Herpes zoster (shingles), postherpetic neuralgia | No |
| **EBV (HHV-4)** | Infectious mononucleosis | Burkitt lymphoma, Hodgkin, NPC, PTLD | Yes |
| **CMV (HHV-5)** | Congenital CMV; retinitis/colitis in immunocompromised | Transplant disease, graft rejection | No |
| **HHV-6A/6B** | Roseola infantum (exanthem subitum) | Encephalitis (HHV-6B) in HSCT recipients | Possibly (glioma) |
| **HHV-7** | Roseola (co-infection); pityriasis rosea | Encephalitis rare | Unknown |
| **KSHV (HHV-8)** | Subclinical primary infection | Kaposi sarcoma, primary effusion lymphoma, Castleman disease | Yes |

### Disease Burden and Epidemiology

- **HSV-1**: ~3.7 billion people infected worldwide (<50 years); leading cause of infectious corneal blindness; neonatal HSV encephalitis (HSV-2 >> HSV-1 vertical transmission).
- **CMV**: Most significant cause of non-genetic congenital hearing loss; #1 viral threat in solid organ and hematopoietic stem cell transplantation.
- **EBV**: >95% of adults infected; 200,000 EBV-attributable cancers per year globally.
- **KSHV**: Endemic in sub-Saharan Africa; Kaposi sarcoma remains the most common AIDS-defining malignancy.

[^roizman-fields-virology]: Knipe DM, Howley PM, eds. *Fields Virology.* 7th ed. Wolters Kluwer; 2021.
[^davison-2009-herpesvirus-evolution]: Davison AJ, Eberle R, Ehlers B, et al. The order Herpesvirales. *Arch Virol.* 2009;154(1):171-177. [doi:10.1007/s00705-008-0278-4](https://doi.org/10.1007/s00705-008-0278-4) · [PubMed 19066710](https://pubmed.ncbi.nlm.nih.gov/19066710/)
[^whitley-2001-herpes-latency]: Whitley RJ, Roizman B. Herpes simplex virus infections. *Lancet.* 2001;357(9267):1513-1518. [doi:10.1016/S0140-6736(00)04638-9](https://doi.org/10.1016/S0140-6736(00)04638-9) · [PubMed 11377626](https://pubmed.ncbi.nlm.nih.gov/11377626/)

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
