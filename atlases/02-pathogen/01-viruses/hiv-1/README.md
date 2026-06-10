---
schema: pathogen-entry/v1
id: hiv-1
name: Human Immunodeficiency Virus type 1
atlas: 02-pathogen
scale: 01-viruses
status: active
last_reviewed: 2026-06-04
summary: "Lentivirus (Retroviridae). ~9.7 kb diploid ssRNA genome. CD4-tropic; gp120/gp41-mediated entry; reverse transcriptase drives rapid diversification; proviral integration establishes latent reservoir; causes AIDS via CD4+ T cell depletion."
taxonomy:
  family: Retroviridae
  genus: Lentivirus
  species: HIV-1
genome:
  type: RNA
  description: "~9.7 kb single-stranded positive-sense RNA (diploid); two copies per virion"
replication_site: "CD4+ T cells, macrophages, dendritic cells"
transmission:
  - sexual contact
  - blood/needle sharing
  - mother-to-child (perinatal, breastfeeding)
aliases: ["HIV", "HIV type 1", "human immunodeficiency virus", "AIDS virus"]
tags: [retrovirus, lentivirus, aids, cd4, immunodeficiency, reverse-transcriptase, integrase]
sources:
  - id: gallo-1984-isolation
    type: peer-reviewed
    cite: "Gallo RC, Salahuddin SZ, Popovic M, et al. Frequent detection and isolation of cytopathic retroviruses (HTLV-III) from patients with AIDS and at risk for AIDS. Science. 1984;224(4648):500-3."
    pmid: "6200935"
    url: "https://pubmed.ncbi.nlm.nih.gov/6200935/"
  - id: chun-1997-latent-reservoir
    type: peer-reviewed
    cite: "Chun TW, Stuyver L, Mizell SB, et al. Presence of an inducible HIV-1 latent reservoir during highly active antiretroviral therapy. Proc Natl Acad Sci USA. 1997;94(24):13193-7."
    pmid: "9353114"
    url: "https://pubmed.ncbi.nlm.nih.gov/9353114/"
  - id: lundgren-2015-start-trial
    type: peer-reviewed
    cite: "Lundgren JD, Babiker AG, Gordin F, et al. Initiation of Antiretroviral Therapy in Early Asymptomatic HIV Infection (START). N Engl J Med. 2015;373(9):795-807."
    doi: "10.1056/NEJMoa1506816"
    url: "https://doi.org/10.1056/NEJMoa1506816"
cross_links:
  - target: 01-human/04-cellular/t-helper-cell
    relation: infects
    note: "gp120 binds CD4 on T helper (CD4+) cells; CXCR4 co-receptor preferentially used by X4-tropic strains. Productive infection depletes the CD4+ T cell pool driving immunodeficiency."
  - target: 01-human/04-cellular/dendritic-cell
    relation: infects
    note: "HIV-1 infects dendritic cells via DC-SIGN-mediated capture and CD4/CCR5 entry; DCs act as a Trojan horse trafficking virus to lymph nodes where CD4+ T cell infection is amplified."
  - target: 01-human/07-system/immune-system
    relation: damages
    note: "Progressive CD4+ T cell depletion causes generalised immunosuppression; loss of mucosal immunity, NK cell dysfunction, and B cell dysregulation underlie susceptibility to opportunistic infections."
  - target: 01-human/04-cellular/t-helper-cell
    relation: damages
    note: "Productive HIV-1 replication causes cytolysis of CD4+ T cells; viral proteins Vpr and Nef drive non-cytolytic CD4 depletion via bystander apoptosis and downregulation of cell survival signals."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: target-of
    note: "Broadly neutralising antibodies (bNAbs) targeting gp120 conserved epitopes (V3/CD4bs/MPER) are a primary adaptive humoral defence; anti-gp41 IgG antibodies contribute to ADCC-mediated viral clearance."
  - target: 01-human/07-system/aicardi-goutieres-syndrome
    relation: connects-to
    note: "SAMHD1 (AGS gene) is the principal HIV-1 restriction factor: dNTP hydrolase depletes viral dNTP pool → inhibits reverse transcription; HIV-2/SIVsm Vpx degrades SAMHD1; SAMHD1-LOF in AGS links innate antiviral immunity to monogenic neuroinflammation."
---

# Human Immunodeficiency Virus type 1

## Overview

Human Immunodeficiency Virus type 1 (HIV-1) is a **lentivirus** in the family *Retroviridae*, the causative agent of Acquired Immunodeficiency Syndrome (AIDS) and the driver of the most significant infectious disease pandemic of the 20th and 21st centuries. The virus was isolated and characterised in 1983–1984 by Luc Montagnier, Françoise Barré-Sinoussi, and Robert Gallo [^gallo-1984-isolation].

HIV-1 originated from multiple zoonotic cross-species transmission events from chimpanzees (*Pan troglodytes troglodytes*) in central Africa — the major pandemic lineage, **Group M**, is estimated to have entered the human population around 1920 in the Congo Basin. Group M has diversified into subtypes A–K and numerous circulating recombinant forms (CRFs) with distinct global distributions: subtype B dominates in North America and Europe; subtype C accounts for ~50% of global infections and predominates in sub-Saharan Africa and South Asia.

Approximately **39 million people** were living with HIV globally as of 2022, with approximately **1.3 million new infections per year**. ART (antiretroviral therapy) has transformed HIV from a uniformly fatal illness into a manageable chronic condition; individuals starting ART with preserved CD4 counts now have near-normal life expectancy.

## Structure

### Virion Architecture

HIV-1 is an enveloped spherical particle approximately **120 nm in diameter**. The cone-shaped capsid encloses the two copies of the genomic RNA along with the viral enzymes required for early replication.

| Component | Description |
|:---|:---|
| **Envelope (Env/gp160)** | Trimeric spike glycoprotein; processed into gp120 (surface unit) + gp41 (transmembrane unit); mediates CD4/co-receptor binding and membrane fusion |
| **Matrix (MA/p17)** | Lines the inner face of the lipid bilayer; anchors Env; directs nuclear import of the pre-integration complex |
| **Capsid (CA/p24)** | Forms the conical core; encloses 2 copies of genomic RNA + viral enzymes; p24 antigen is the basis of 4th-generation HIV diagnostic assays |
| **Nucleocapsid (NC/p7)** | RNA-binding protein; packages genomic RNA; chaperones reverse transcription |
| **Reverse transcriptase (RT/p66/p51)** | RNA-dependent DNA polymerase + RNase H; error-prone (~3×10⁻⁵ substitutions/site/replication cycle); no proofreading activity |
| **Integrase (IN/p32)** | Catalyses insertion of proviral dsDNA into host chromatin; target of integrase strand transfer inhibitors (INSTIs) |
| **Protease (PR/p11)** | Cleaves the Gag-Pol polyprotein during virion maturation; target of protease inhibitors (PIs) |

### Genome Organisation

The ~9.7 kb ssRNA genome encodes three major structural polyproteins and six accessory/regulatory genes:

| Gene | Protein(s) | Function |
|:---:|:---|:---|
| *gag* | p55→ MA, CA, NC, p6 | Core structural proteins |
| *pol* | p160→ PR, RT, IN | Replication enzymes |
| *env* | gp160→ gp120, gp41 | Envelope glycoproteins; entry |
| *tat* | Tat | Transcriptional transactivator; binds TAR element; essential for viral gene expression |
| *rev* | Rev | Shuttles unspliced/singly-spliced viral mRNA from nucleus |
| *nef* | Nef | Downregulates CD4 and MHC-I; enhances viral infectivity; promotes immune evasion |
| *vif* | Vif | Counteracts APOBEC3G/F restriction factors |
| *vpr* | Vpr | Facilitates nuclear import of PIC; arrests cell cycle at G2 |
| *vpu* | Vpu | Degrades CD4; counteracts tetherin (BST-2); promotes virion release |

## Infection Mechanism

### Entry

HIV-1 entry is a sequential three-step process:

1. **CD4 binding:** The gp120 outer domain contacts the CD4 receptor on the T helper cell or macrophage surface, inducing a conformational change in gp120 that exposes the co-receptor binding site (V3 loop + bridging sheet).

2. **Co-receptor engagement:** gp120 binds either **CCR5** (R5-tropic strains — predominant during transmission and early infection) or **CXCR4** (X4-tropic — emerge in ~50% of untreated individuals late in disease). This second conformational change exposes the gp41 fusion peptide. R5-tropic strains transmit preferentially; individuals homozygous for the CCR5-Δ32 deletion are highly resistant to HIV-1 infection.

3. **Membrane fusion:** The gp41 fusion peptide inserts into the target cell membrane; six-helix bundle formation drives lipid bilayer merger and viral core delivery into the cytoplasm.

### Reverse Transcription and Nuclear Import

The viral RNA is reverse transcribed into double-stranded DNA (dsDNA) in the cytoplasm within the partially dismantled capsid. RT lacks 3'→5' proofreading exonuclease activity, generating an **error rate of ~3×10⁻⁵ substitutions/site/replication cycle**. Combined with a generation time of ~1–2 days and the high replication rate (~10¹⁰ new virions/day in an untreated host), this produces enormous genetic diversity, enabling rapid immune escape and drug resistance evolution.

The pre-integration complex (PIC) is actively transported into the nucleus — a distinguishing property of lentiviruses that allows infection of non-dividing cells such as macrophages and dendritic cells.

### Integration and Provirus

Integrase catalyses insertion of the viral dsDNA into the host genome, creating the **provirus**. HIV-1 preferentially integrates into actively transcribed genes. Once integrated, the provirus is a permanent genetic element: it persists for the life of the cell and is silently replicated with host DNA.

In **resting CD4+ memory T cells**, the provirus enters a deeply silenced state — the **latent reservoir** — which is established early in infection and persists indefinitely even in patients on suppressive ART [^chun-1997-latent-reservoir]. This reservoir is the principal barrier to HIV cure.

## Host Interactions

### CD4+ T Cell Depletion

The hallmark of HIV-1 disease is progressive loss of **CD4+ T cells**:

- **Normal range:** 500–1,500 cells/μL blood
- **Treatment threshold (historical):** <350 cells/μL; current guidelines recommend ART at any CD4 count regardless of level [^lundgren-2015-start-trial]
- **AIDS-defining threshold:** <200 cells/μL or AIDS-defining illness

Depletion occurs via direct viral cytolysis of productively infected cells, bystander apoptosis of uninfected CD4+ T cells, pyroptotic death of abortively infected CD4+ T cells (inflammasome activation), and chronic immune activation accelerating T cell turnover.

### Innate and Adaptive Immune Evasion

HIV-1 employs multiple immune evasion strategies:

- **Nef** downregulates surface MHC-I, reducing recognition by cytotoxic CD8+ T cells; also downregulates CD4 and CD28 to avoid signalling.
- **Vif** targets APOBEC3G and APOBEC3F for proteasomal degradation, preventing hypermutation of the viral genome in infected cells.
- **gp120 glycan shield:** Dense N-linked glycosylation of the gp120 surface shields conserved epitopes from antibody recognition.
- **Antigenic diversity:** RT-driven error rate + high replication → quasi-species swarms that rapidly escape T cell and antibody responses.

### Macrophages and Dendritic Cells as Reservoirs

Macrophages infected with R5-tropic HIV-1 support long-term viral production without cytolysis. Dendritic cells (both myeloid and plasmacytoid) capture HIV via DC-SIGN and traffic it to lymph nodes, where T cell infection is amplified in immune synapses.

## Connections

- **Infects** → [T Helper Cell](../../../01-human/04-cellular/t-helper-cell/README.md): gp120 binds CD4; co-receptor CCR5 or CXCR4 required; productive infection depletes the CD4+ T cell pool and is the proximate cause of AIDS.
- **Infects** → [Dendritic Cell](../../../01-human/04-cellular/dendritic-cell/README.md): DC-SIGN-mediated capture and CD4/CCR5 entry; DCs amplify infection by trafficking virus to lymphoid tissue.
- **Damages** → [Immune System](../../../01-human/07-system/immune-system/README.md): CD4+ T cell depletion drives generalised immunosuppression; NK and B cell dysfunction contribute; loss of immune surveillance enables opportunistic infections and AIDS-defining malignancies.
- **Damages** → [T Helper Cell](../../../01-human/04-cellular/t-helper-cell/README.md): Direct viral cytolysis, bystander apoptosis, and pyroptosis of CD4+ T cells.
- **Target of** → [Immunoglobulin G](../../../01-human/03-molecular/immunoglobulin-g/README.md): Broadly neutralising antibodies targeting gp120 conserved sites are the basis for vaccine design; anti-gp41 IgG mediates ADCC.
- **Connects-to** → [Aicardi-Goutières Syndrome](../../../01-human/07-system/aicardi-goutieres-syndrome/README.md): SAMHD1 (AGS gene) is the principal HIV-1 restriction factor: dNTP hydrolase depletes viral dNTP pool → inhibits reverse transcription; HIV-2/SIVsm Vpx degrades SAMHD1; SAMHD1-LOF in AGS links innate antiviral immunity to monogenic neuroinflammation.

## Pathology

### Clinical Stages

| Stage | CD4 (cells/μL) | Features |
|:---|:---:|:---|
| **Acute HIV infection** | Variable (↓ transiently) | Mononucleosis-like illness: fever, lymphadenopathy, pharyngitis, rash; high plasma viremia; window period before seroconversion |
| **Chronic infection (asymptomatic)** | 350–500 | Clinically silent; ongoing viral replication; progressive CD4 decline at ~50–100/μL per year untreated |
| **Symptomatic HIV (non-AIDS)** | 200–350 | Recurrent bacterial infections, oral candidiasis, hairy leukoplakia, shingles |
| **AIDS** | <200 or AIDS-defining illness | Opportunistic infections + AIDS-defining malignancies |

### AIDS-Defining Opportunistic Infections

- **Pneumocystis pneumonia (PCP):** Most common AIDS-defining OI; caused by *Pneumocystis jirovecii* (CD4 <200)
- **Toxoplasmosis:** CNS ring-enhancing lesions; reactivation of latent *Toxoplasma gondii* (CD4 <100)
- **CMV retinitis:** Leading cause of blindness in untreated AIDS (CD4 <50)
- **Mycobacterium avium complex (MAC):** Disseminated mycobacterial infection (CD4 <50)
- **Cryptococcal meningitis:** *Cryptococcus neoformans*; characteristic CSF India ink positivity (CD4 <100)
- **Oesophageal candidiasis**
- **Cryptosporidiosis** (severe, chronic diarrhoea)

### AIDS-Defining Malignancies

- **Kaposi's sarcoma (KS):** HHV-8-driven vascular tumour; skin, mucosa, lung, GI (CD4 <200)
- **Non-Hodgkin lymphoma (NHL):** EBV-associated; CNS lymphoma especially at very low CD4
- **Invasive cervical carcinoma:** HPV-driven

### Neurological Complications

- **HIV-associated neurocognitive disorders (HAND) / AIDS dementia complex:** HIV crosses the blood-brain barrier via infected monocytes; monocyte-derived macrophages and microglia serve as CNS reservoir; neuroinflammation and excitotoxicity drive cognitive impairment.
- **HIV-associated sensory neuropathy**
- **Vacuolar myelopathy**

### Wasting Syndrome

Progressive involuntary weight loss (>10% body weight) + chronic diarrhoea or fever; driven by cytokine-mediated hypermetabolism and malabsorption.

### Viral Load and Disease Progression

Setpoint plasma viral load (RNA copies/mL) established after acute infection is the strongest predictor of long-term disease progression. Untreated patients with setpoint VL >100,000 copies/mL progress to AIDS in a median ~5 years; those with VL <10,000 copies/mL may remain asymptomatic for >10 years ("long-term non-progressors"). Elite controllers maintain VL <50 copies/mL without ART.

### Treatment

**ART (antiretroviral therapy)** — formerly HAART — combines drugs from multiple mechanistic classes to suppress viral replication below the limit of detection (<50 copies/mL):

| Drug class | Mechanism | Examples |
|:---|:---|:---|
| NRTIs | Nucleoside RT inhibitors (chain terminators) | Tenofovir (TDF/TAF), emtricitabine, abacavir |
| NNRTIs | Non-nucleoside RT inhibitors (allosteric) | Efavirenz, rilpivirine, doravirine |
| PIs | Protease inhibitors | Darunavir (boosted with ritonavir/cobicistat) |
| INSTIs | Integrase strand transfer inhibitors | Dolutegravir, bictegravir, cabotegravir |
| Entry inhibitors | CCR5 antagonists / fusion inhibitors | Maraviroc (CCR5); enfuvirtide (fusion) |

Current standard of care: INSTI-based two or three-drug regimens. Plasma VL suppression to <50 copies/mL is the treatment goal; at undetectable VL, sexual transmission risk is effectively zero (U=U: Undetectable = Untransmittable).

### Latent Reservoir and Cure Research

The latent reservoir in **resting CD4+ memory T cells** — estimated at ~1 million cells in a treated patient — is not eliminated by ART [^chun-1997-latent-reservoir]. Two major cure strategies are under investigation:

- **Shock-and-kill (reactivation + elimination):** Latency-reversing agents (LRAs — HDAC inhibitors, PKC agonists) to reactivate latent virus → immune clearance of reactivated cells. Limited clinical success to date.
- **Block-and-lock (deep latency):** Epigenetic silencing agents (e.g., dCA targeting Tat) to achieve durable silencing without reactivation, converting active infection into a permanently silent state.

The Berlin patient (Timothy Ray Brown, 2009) and London/City of Hope patients achieved functional cure via CCR5-Δ32 allogeneic stem cell transplant — proof of concept for eliminating the reservoir, but not a scalable therapy.

## See Also

- [T Helper Cell](../../../01-human/04-cellular/t-helper-cell/README.md) — primary target cell
- [Dendritic Cell](../../../01-human/04-cellular/dendritic-cell/README.md) — reservoir and trafficking vehicle
- [Immune System](../../../01-human/07-system/immune-system/README.md) — system-level damage

[^gallo-1984-isolation]: Gallo RC, Salahuddin SZ, Popovic M, et al. Frequent detection and isolation of cytopathic retroviruses (HTLV-III) from patients with AIDS and at risk for AIDS. *Science.* 1984;224(4648):500-3. [PubMed 6200935](https://pubmed.ncbi.nlm.nih.gov/6200935/)
[^chun-1997-latent-reservoir]: Chun TW, Stuyver L, Mizell SB, et al. Presence of an inducible HIV-1 latent reservoir during highly active antiretroviral therapy. *Proc Natl Acad Sci USA.* 1997;94(24):13193-7. [PubMed 9353114](https://pubmed.ncbi.nlm.nih.gov/9353114/)
[^lundgren-2015-start-trial]: Lundgren JD, Babiker AG, Gordin F, et al. Initiation of Antiretroviral Therapy in Early Asymptomatic HIV Infection (START). *N Engl J Med.* 2015;373(9):795-807. [doi:10.1056/NEJMoa1506816](https://doi.org/10.1056/NEJMoa1506816)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
