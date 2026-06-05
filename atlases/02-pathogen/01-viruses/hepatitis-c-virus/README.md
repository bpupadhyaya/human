---
schema: pathogen-entry/v1
id: hepatitis-c-virus
name: Hepatitis C Virus
atlas: 02-pathogen
scale: 01-viruses
status: active
last_reviewed: 2026-06-05
summary: "(+)ssRNA Hepacivirus; 9.6 kb genome. NS3/4A protease cleaves MAVS/TRIF, disabling innate immune sensing. Infects hepatocytes via CD81/SR-B1/CLDN1/OCLN entry. 75% chronic infection rate; leading cause of cirrhosis and HCC globally. Curable with DAAs (NS5B/NS5A inhibitors)."
taxonomy:
  family: Flaviviridae
  genus: Hepacivirus
  species: Hepatitis C virus
genome:
  type: RNA
  description: "~9.6 kb single-stranded positive-sense RNA; single open reading frame flanked by 5' and 3' UTRs with IRES element"
replication_site: "Hepatocytes (primary); low-level replication in B lymphocytes"
transmission:
  - parenteral (blood/blood-products, needles)
  - sexual contact (lower efficiency)
  - mother-to-child (perinatal, ~5%)
aliases: ["HCV", "hepatitis C", "non-A non-B hepatitis virus", "NANBH"]
tags: [flaviviridae, hepacivirus, cirrhosis, hcc, hepatocellular-carcinoma, daa, ns3, ns5a, ns5b, chronic-hepatitis]
sources:
  - id: choo-1989-hcv-cloning
    type: peer-reviewed
    cite: "Choo QL, Kuo G, Weiner AJ, et al. Isolation of a cDNA clone derived from a blood-borne non-A, non-B viral hepatitis genome. Science. 1989;244(4902):359-62."
    doi: "10.1126/science.2523562"
    pmid: "2523562"
    url: "https://doi.org/10.1126/science.2523562"
  - id: lindenbach-2013-hcv-review
    type: peer-reviewed
    cite: "Lindenbach BD, Rice CM. The ins and outs of hepatitis C virus entry and assembly. Nat Rev Microbiol. 2013;11(10):688-700."
    doi: "10.1038/nrmicro3098"
    pmid: "24018384"
    url: "https://doi.org/10.1038/nrmicro3098"
  - id: li-2017-ns3-mavs
    type: peer-reviewed
    cite: "Li XD, Sun L, Seth RB, Pineda G, Chen ZJ. Hepatitis C virus protease NS3/4A cleaves mitochondrial antiviral signalling protein off the mitochondria to evade innate immunity. Proc Natl Acad Sci USA. 2005;102(49):17717-22."
    doi: "10.1073/pnas.0508531102"
    pmid: "16301520"
    url: "https://doi.org/10.1073/pnas.0508531102"
  - id: pawlotsky-2021-daa-review
    type: peer-reviewed
    cite: "Pawlotsky JM. COVID-19 and the liver-related deaths to come. Nat Rev Gastroenterol Hepatol. 2020;17(5):255-256. [see also: Pawlotsky JM. Hepatitis C virus resistance to direct-acting antiviral drugs. Gastroenterology. 2016;151(1):70-86.]"
    doi: "10.1053/j.gastro.2016.04.003"
    pmid: "27147299"
    url: "https://doi.org/10.1053/j.gastro.2016.04.003"
  - id: who-hcv-2023
    type: regulatory
    cite: "World Health Organization. Hepatitis C. WHO Fact Sheet. 2023."
    url: "https://www.who.int/news-room/fact-sheets/detail/hepatitis-c"
    accessed: "2026-06-05"
  - id: sung-2021-global-cancer
    type: peer-reviewed
    cite: "Sung H, Ferlay J, Siegel RL, et al. Global Cancer Statistics 2020: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries. CA Cancer J Clin. 2021;71(3):209-249."
    doi: "10.3322/caac.21660"
    pmid: "33538338"
    url: "https://doi.org/10.3322/caac.21660"
cross_links:
  - target: 01-human/04-cellular/hepatocyte
    relation: infects
    note: "HCV enters hepatocytes via CD81, SR-B1, claudin-1, and occludin receptors. NS3/4A serine protease cleaves MAVS and TRIF, blocking RIG-I and TLR3 innate immune sensing to enable persistent infection."
  - target: 01-human/06-organ/liver
    relation: damages
    note: "Chronic HCV triggers portal inflammation, HSC activation via TGF-β, progressive fibrosis, and cirrhosis; 20–30% of chronically infected patients develop cirrhosis within 20 years, with HCC risk rising thereafter."
  - target: 01-human/07-system/immune-system
    relation: damages
    note: "HCV drives T cell exhaustion via PD-1 and TIM-3 upregulation; chronic antigen stimulation depletes HCV-specific CD8+ T cells, enabling persistence and impairing broad antiviral immunity over years."
  - target: 01-human/04-cellular/hepatocyte
    relation: prevents
    note: "DAAs (sofosbuvir/ledipasvir, glecaprevir/pibrentasvir) achieve >95% SVR12, preventing further hepatocyte damage and reducing HCC incidence by eliminating active HCV replication."
---

# Hepatitis C Virus

## Overview

Hepatitis C Virus (HCV) is a **positive-sense single-stranded RNA virus** of the family *Flaviviridae*, genus *Hepacivirus*, and the causative agent of hepatitis C — a chronic liver infection affecting an estimated **58 million people** worldwide and responsible for approximately 290,000 deaths per year, predominantly from cirrhosis and hepatocellular carcinoma (HCC) [^who-hcv-2023].

HCV was first molecularly characterised in 1989 by Choo, Kuo, and colleagues at Chiron Corporation, who identified its genome by immunoscreening a cDNA library derived from a chimpanzee chronically infected with "non-A, non-B hepatitis" virus [^choo-1989-hcv-cloning]. Before this landmark discovery, the agent had been called NANBH (non-A, non-B hepatitis) and was the leading cause of post-transfusion hepatitis.

HCV exists as **seven major genotypes (1–7)** with multiple subtypes; genotype 1 (subtypes 1a, 1b) is the most prevalent globally. Unlike hepatitis B, there is no approved vaccine for HCV, but pangenotypic **direct-acting antivirals (DAAs)** now achieve **sustained virological response (SVR12)** rates exceeding 95%, effectively constituting a cure [^pawlotsky-2021-daa-review].

The WHO's target is to eliminate viral hepatitis as a public health threat by 2030 — an ambitious goal given that the majority of HCV-infected individuals remain undiagnosed.

## Structure

### Virion Architecture

HCV is a spherical enveloped particle approximately **50–60 nm in diameter**. The icosahedral capsid encloses the genomic RNA.

| Component | Description |
|:---|:---|
| **Envelope glycoproteins E1/E2** | Heterodimer on the virion surface; E2 binds CD81 and SR-B1; E1 mediates membrane fusion at endosomal pH; highly variable hypervariable region 1 (HVR1) on E2 enables immune escape |
| **Core protein (p21)** | Forms the nucleocapsid; RNA-binding; also localises to lipid droplets where it participates in assembly |
| **Lipoviroparticle (LVP)** | HCV circulates in blood associated with very-low-density lipoprotein (VLDL) and LDL as lipoviroparticles; this association masks viral epitopes from neutralising antibodies |

### Genome Organisation

The ~9.6 kb genome encodes a single large **open reading frame (ORF)** flanked by highly conserved 5' and 3' untranslated regions (UTRs). The 5' UTR contains an **internal ribosomal entry site (IRES)** that drives cap-independent translation.

| Protein region | Protein(s) | Function |
|:---:|:---|:---|
| **Structural** | Core, E1, E2 | Nucleocapsid; envelope glycoproteins mediating entry and fusion |
| **p7** | Viroporin | Ion channel; essential for virion assembly and release |
| **NS2** | NS2 protease | Cleaves NS2–NS3 junction; required for assembly |
| **NS3/4A** | Serine protease + helicase | Processes downstream nonstructural proteins; **cleaves MAVS and TRIF to disable innate immune signalling** |
| **NS4B** | Membrane protein | Induces ER membrane rearrangements to form the membranous web (replication organelle) |
| **NS5A** | Phosphoprotein | Replication complex scaffold; assembly factor; target of NS5A inhibitors (ledipasvir, velpatasvir, pibrentasvir) |
| **NS5B** | RNA-dependent RNA polymerase (RdRp) | Replicates the viral genome; lacks proofreading → high mutation rate; target of NS5B inhibitors (sofosbuvir) |

### Quasispecies Diversity

HCV's RdRp error rate (~10⁻⁴–10⁻⁵ substitutions/site/replication cycle) combined with rapid replication (~10¹² virions/day) generates a **quasispecies swarm** — a cloud of closely related but distinct genomes. This diversity enables rapid selection of drug-resistance mutations and persistent escape from neutralising antibodies.

## Infection Mechanism

### Cellular Entry

HCV entry into hepatocytes is a multistep, receptor-coordinated process [^lindenbach-2013-hcv-review]:

1. **Initial attachment:** E2 engages scavenger receptor class B type I (SR-B1) and CD81 on the hepatocyte surface, facilitating low-affinity initial attachment.
2. **Tight junction migration:** The virus-receptor complex migrates to the tight junctions, where it engages **claudin-1 (CLDN1)** and **occludin (OCLN)** — tight junction proteins essential for productive entry.
3. **Clathrin-mediated endocytosis:** The complete entry complex (E1/E2 + CD81 + CLDN1 + OCLN) is internalised via clathrin-coated pits.
4. **Endosomal fusion:** Low endosomal pH triggers E1-mediated membrane fusion, releasing the nucleocapsid into the cytoplasm.

### Replication

After uncoating, the genomic (+)ssRNA is directly translated at the **IRES** element. The resulting polyprotein (~3,000 amino acids) is co- and post-translationally processed by both host signal peptidases and the viral NS3/4A protease.

Genome replication occurs in a specialised membrane compartment called the **membranous web** — a remodelling of the ER membrane induced by NS4B. Here, NS5B RdRp synthesises a complementary (−)ssRNA intermediate, which serves as template for (+)ssRNA progeny genomes.

### Innate Immune Evasion — NS3/4A Protease

The NS3/4A serine protease is the master immune evasion factor [^li-2017-ns3-mavs]:

- **MAVS cleavage:** Mitochondrial antiviral signalling protein (MAVS/IPS-1/CARDIF), the central adaptor for RIG-I–like receptor (RLR) signalling, is cleaved at Cys-508 by NS3/4A, releasing it from the mitochondrial outer membrane and disabling downstream IRF3 phosphorylation and type I IFN production.
- **TRIF cleavage:** NS3/4A also cleaves TRIF (TICAM-1), the TLR3 adaptor, further blocking dsRNA-sensing and IFN-β induction.
- **Net effect:** Infected hepatocytes produce minimal IFN-β/IFN-λ, creating a cytokine-poor environment that permits viral persistence.

### Virion Assembly and Release

HCV assembly is closely coupled to **lipid droplet biogenesis** and VLDL secretion. Core protein accumulates on lipid droplets, recruits NS5A and the replication complex, and nascent virions bud into the ER lumen. HCV is released via the **VLDL secretory pathway**, explaining its low buoyant density and lipoviroparticle form in blood.

## Host Interactions

### Viral Persistence — Chronic Infection

The majority (~75%) of HCV-infected individuals fail to clear the virus and develop **chronic infection**. Mechanisms include:

- **Impaired innate sensing** (NS3/4A-mediated MAVS/TRIF cleavage)
- **T cell exhaustion:** Persistent high-level antigenemia drives progressive upregulation of **PD-1**, **TIM-3**, and **CTLA-4** checkpoint receptors on HCV-specific CD8⁺ T cells, impairing their effector functions
- **Viral escape:** HCV rapidly mutates epitopes targeted by cytotoxic T lymphocytes (CTLs) and antibodies, outrunning adaptive immune surveillance
- **Regulatory T cell expansion:** Tregs and IL-10-producing cells suppress HCV-specific immune responses in the liver

Acute resolvers (spontaneous clearers) typically mount a broad, vigorous, polyfunctional CD4⁺/CD8⁺ T cell response with early and sustained CD4⁺ Th1 help — a correlate of protection.

### Hepatic Stellate Cell Activation and Fibrosis

In chronic infection, persistent hepatocyte damage and inflammatory cytokines (TNF-α, IL-6, IL-1β) activate **hepatic stellate cells (HSCs)** — the principal fibrogenic cells of the liver:

- Activated HSCs transdifferentiate into myofibroblasts under **TGF-β1** and **PDGF** signalling
- Myofibroblasts secrete collagen (predominantly type I/III), replacing normal parenchyma with fibrous scar tissue
- Progressive fibrosis leads to **cirrhosis** — distorted liver architecture with regenerative nodules and portal hypertension
- In cirrhosis, **HCC** develops at ~2–5% per year — driven by chronic inflammation, oxidative stress, mitochondrial dysfunction, and HCV-driven transcriptional activation of oncogenes (including activation of Wnt/β-catenin and STAT3 pathways)

### HCV and B Lymphocytes

HCV also infects B lymphocytes at low levels via CD81. This tropism drives:
- **Cryoglobulinaemia** — mixed cryoglobulins (type II: monoclonal IgM rheumatoid factor against polyclonal IgG); causes systemic vasculitis
- **B cell non-Hodgkin lymphoma** risk is increased ~2-fold in chronic HCV carriers
- B cell stimulation via CD81/E2 interaction may contribute to clonal B cell expansion

## Connections

- **Infects** → [Hepatocyte](../../../01-human/04-cellular/hepatocyte/README.md): HCV enters hepatocytes via CD81, SR-B1, claudin-1, and occludin; NS3/4A disables MAVS/TRIF innate sensing; hepatocytes are the primary replication compartment.
- **Damages** → [Liver](../../../01-human/06-organ/liver/README.md): Chronic HCV causes portal inflammation, fibrosis via TGF-β/HSC activation, cirrhosis, and HCC; the leading indication for liver transplantation in many countries.
- **Damages** → [Immune System](../../../01-human/07-system/immune-system/README.md): HCV drives CD8⁺ T cell exhaustion (PD-1/TIM-3 upregulation) and impairs CD4⁺ Th1 help; persistent NS3/4A-mediated innate immune blockade enables chronicity.
- **Prevents** → [Hepatocyte](../../../01-human/04-cellular/hepatocyte/README.md): DAAs (sofosbuvir/ledipasvir, glecaprevir/pibrentasvir) achieve >95% SVR12, eliminating active HCV replication and preventing ongoing hepatocyte damage.

## Pathology

### Clinical Stages

| Stage | Timing | Features |
|:---|:---:|:---|
| **Acute hepatitis C** | 0–6 months post-infection | Usually subclinical; 20–30% symptomatic (fatigue, jaundice, RUQ discomfort); ALT/AST elevated; HCV RNA detectable 1–2 weeks after exposure |
| **Spontaneous clearance** | Within 6 months | ~25% of acutely infected persons clear HCV; higher rates with IL28B CC genotype, female sex, and symptomatic acute infection |
| **Chronic infection** | >6 months | Persistent HCV RNA; most asymptomatic for years; ongoing hepatocyte inflammation and fibrosis accumulate silently |
| **Compensated cirrhosis** | F4 fibrosis | Asymptomatic or mild portal hypertension; variceal formation begins; HCC risk ~2–5%/year |
| **Decompensated cirrhosis** | Advanced cirrhosis | Ascites, variceal haemorrhage, hepatic encephalopathy, spontaneous bacterial peritonitis; liver transplant is definitive therapy |
| **HCC** | Variable | Most occur on background of cirrhosis; 5-year survival <15% without resection or transplant [^sung-2021-global-cancer] |

### Extrahepatic Manifestations

| Manifestation | Mechanism |
|:---|:---|
| **Mixed cryoglobulinaemia** | B cell expansion → IgM rheumatoid factors; vasculitis (purpura, neuropathy, glomerulonephritis) |
| **Membranoproliferative glomerulonephritis (MPGN)** | Cryoglobulin immune complex deposition in glomerular capillaries |
| **Non-Hodgkin lymphoma** | Chronic B cell stimulation → lymphomagenesis |
| **Insulin resistance / type 2 diabetes** | HCV directly impairs insulin signalling via NS5A-mediated Akt/mTOR disruption |
| **Thyroid disorders** | Interferon therapy-associated thyroiditis (less relevant post-DAA era); direct viral thyroid tropism proposed |

### Fibrosis Staging

The **METAVIR score** classifies liver fibrosis (F0–F4):

| Score | Description |
|:---:|:---|
| F0 | No fibrosis |
| F1 | Portal fibrosis without septa |
| F2 | Few septa |
| F3 | Numerous septa without cirrhosis |
| F4 | Cirrhosis |

Non-invasive alternatives: **FIB-4 index**, **liver elastography (FibroScan)** — reduce the need for liver biopsy.

### Treatment: Direct-Acting Antivirals (DAAs)

DAAs target HCV-specific proteins, achieving >95% SVR12 (cure) with 8–12 weeks of once-daily oral therapy [^pawlotsky-2021-daa-review]:

| DAA class | Mechanism | Examples |
|:---|:---|:---|
| **NS5A inhibitors** | Block NS5A phosphoprotein (replication + assembly) | Ledipasvir, velpatasvir, pibrentasvir |
| **NS5B nucleotide analogues** | Chain termination at RdRp active site | Sofosbuvir |
| **NS5B non-nucleoside inhibitors** | Allosteric RdRp inhibition | Dasabuvir |
| **NS3/4A protease inhibitors** | Block polyprotein processing | Glecaprevir, grazoprevir |

Current pangenotypic regimens: **sofosbuvir/velpatasvir** (12 weeks) and **glecaprevir/pibrentasvir** (8 weeks for treatment-naive, non-cirrhotic). Post-SVR, cirrhosis can partially reverse (regression of fibrosis), and HCC risk falls substantially — but does not reach the level of uninfected individuals.

### Why No Vaccine?

HCV vaccine development faces fundamental challenges:
- **Extreme genetic diversity:** 7 genotypes, >60 subtypes; antibody responses are often genotype-specific
- **Immune evasion:** HVR1 variability on E2 allows escape from neutralising antibodies; NS3/4A disables the innate sensing needed to prime adaptive immunity
- **No small animal model:** Chimpanzees were the only non-human primate susceptible; now replaced by humanised mouse models with limitations
- Active research focuses on broadly cross-neutralising monoclonal antibodies targeting conserved E2 epitopes and on T cell-based vaccine strategies.

## See Also

- [Hepatocyte](../../../01-human/04-cellular/hepatocyte/README.md) — primary infected cell
- [Liver](../../../01-human/06-organ/liver/README.md) — target organ
- [Immune System](../../../01-human/07-system/immune-system/README.md) — evaded immune compartment

[^choo-1989-hcv-cloning]: Choo QL, Kuo G, Weiner AJ, et al. Isolation of a cDNA clone derived from a blood-borne non-A, non-B viral hepatitis genome. *Science.* 1989;244(4902):359-62. [doi:10.1126/science.2523562](https://doi.org/10.1126/science.2523562) · [PubMed 2523562](https://pubmed.ncbi.nlm.nih.gov/2523562/)
[^lindenbach-2013-hcv-review]: Lindenbach BD, Rice CM. The ins and outs of hepatitis C virus entry and assembly. *Nat Rev Microbiol.* 2013;11(10):688-700. [doi:10.1038/nrmicro3098](https://doi.org/10.1038/nrmicro3098) · [PubMed 24018384](https://pubmed.ncbi.nlm.nih.gov/24018384/)
[^li-2017-ns3-mavs]: Li XD, Sun L, Seth RB, Pineda G, Chen ZJ. Hepatitis C virus protease NS3/4A cleaves mitochondrial antiviral signalling protein off the mitochondria to evade innate immunity. *Proc Natl Acad Sci USA.* 2005;102(49):17717-22. [doi:10.1073/pnas.0508531102](https://doi.org/10.1073/pnas.0508531102) · [PubMed 16301520](https://pubmed.ncbi.nlm.nih.gov/16301520/)
[^pawlotsky-2021-daa-review]: Pawlotsky JM. Hepatitis C virus resistance to direct-acting antiviral drugs. *Gastroenterology.* 2016;151(1):70-86. [doi:10.1053/j.gastro.2016.04.003](https://doi.org/10.1053/j.gastro.2016.04.003) · [PubMed 27147299](https://pubmed.ncbi.nlm.nih.gov/27147299/)
[^who-hcv-2023]: World Health Organization. Hepatitis C. *WHO Fact Sheet.* 2023. [who.int/news-room/fact-sheets/detail/hepatitis-c](https://www.who.int/news-room/fact-sheets/detail/hepatitis-c)
[^sung-2021-global-cancer]: Sung H, Ferlay J, Siegel RL, et al. Global Cancer Statistics 2020: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries. *CA Cancer J Clin.* 2021;71(3):209-249. [doi:10.3322/caac.21660](https://doi.org/10.3322/caac.21660) · [PubMed 33538338](https://pubmed.ncbi.nlm.nih.gov/33538338/)
