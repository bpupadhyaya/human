---
schema: pathogen-entry/v1
id: hpv-16
name: HPV-16
atlas: 02-pathogen
scale: 01-viruses
status: active
last_reviewed: 2026-06-05
summary: "Double-stranded DNA papillomavirus (~8 kb). E6 degrades p53 via E6AP ubiquitin ligase; E7 binds Rb family, releasing E2F and deregulating the cell cycle. Causative in 50-60% of cervical cancers and oropharyngeal, anal, vulvar, and penile malignancies. Preventable by Gardasil-9."
taxonomy:
  family: Papillomaviridae
  genus: Alphapapillomavirus
  species: Human papillomavirus type 16
genome:
  type: DNA
  description: "~7.9 kb circular double-stranded DNA; episomal in benign infection; integrates into host genome during malignant progression"
replication_site: "Stratified squamous epithelium (keratinocytes); mucosal and cutaneous surfaces; transformation zone of cervix"
transmission:
  - sexual contact (primary)
  - skin-to-skin genital contact
  - oral-genital contact (oropharyngeal HPV)
  - mother-to-child (perinatal, rare)
aliases: ["HPV16", "human papillomavirus 16", "HPV type 16", "high-risk HPV"]
tags: [papillomaviridae, oncovirus, cervical-cancer, oropharyngeal-cancer, e6, e7, p53, rb, gardasil, transformation]
sources:
  - id: zur-hausen-1983-hpv-cancer
    type: peer-reviewed
    cite: "zur Hausen H. Human genital cancer: synergism between two virus infections or synergism between a virus infection and initiating events? Lancet. 1982;2(8312):1370-2."
    doi: "10.1016/S0140-6736(82)91273-X"
    pmid: "6128601"
    url: "https://doi.org/10.1016/S0140-6736(82)91273-X"
  - id: schiffman-2007-hpv-cancer-review
    type: peer-reviewed
    cite: "Schiffman M, Castle PE, Jeronimo J, Rodriguez AC, Wacholder S. Human papillomavirus and cervical cancer. Lancet. 2007;370(9590):890-907."
    doi: "10.1016/S0140-6736(07)61416-0"
    pmid: "17826171"
    url: "https://doi.org/10.1016/S0140-6736(07)61416-0"
  - id: munger-1989-e7-rb
    type: peer-reviewed
    cite: "Munger K, Werness BA, Dyson N, Phelps WC, Harlow E, Howley PM. Complex formation of human papillomavirus E7 proteins with the retinoblastoma tumor suppressor gene product. EMBO J. 1989;8(13):4099-105."
    doi: "10.1002/j.1460-2075.1989.tb08594.x"
    pmid: "2556261"
    url: "https://doi.org/10.1002/j.1460-2075.1989.tb08594.x"
  - id: schiller-2012-hpv-vaccine
    type: peer-reviewed
    cite: "Schiller JT, Castellsague X, Garland SM. A review of clinical trials of human papillomavirus prophylactic vaccines. Vaccine. 2012;30(Suppl 5):F123-38."
    doi: "10.1016/j.vaccine.2012.04.108"
    pmid: "23199956"
    url: "https://doi.org/10.1016/j.vaccine.2012.04.108"
  - id: sung-2021-global-cancer
    type: peer-reviewed
    cite: "Sung H, Ferlay J, Siegel RL, et al. Global Cancer Statistics 2020: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries. CA Cancer J Clin. 2021;71(3):209-249."
    doi: "10.3322/caac.21660"
    pmid: "33538338"
    url: "https://doi.org/10.3322/caac.21660"
  - id: stanley-2012-hpv-immune
    type: peer-reviewed
    cite: "Stanley M. Immunobiology of HPV and HPV vaccines. Gynecol Oncol. 2010;118(1 Suppl):S12-6."
    doi: "10.1016/j.ygyno.2010.04.015"
    pmid: "20494223"
    url: "https://doi.org/10.1016/j.ygyno.2010.04.015"
cross_links:
  - target: 01-human/04-cellular/dendritic-cell
    relation: infects
    note: "HPV infects mucosal keratinocytes at the basement membrane; Langerhans cells (skin DCs) may present HPV antigen but HPV suppresses DC activation via NF-κB inhibition, impairing downstream adaptive responses."
  - target: 01-human/07-system/immune-system
    relation: damages
    note: "HPV E6/E7 suppress innate immunity by impairing IFN-β production; E7 degrades IRF3 and inhibits TLR9 signalling, enabling persistent infection and eventual oncogenic transformation in cervical epithelium."
  - target: 01-human/07-system/immune-system
    relation: prevents
    note: "Gardasil-9 generates neutralising IgG against HPV-16/18/31/33/45/52/58 L1 VLP antigens, preventing cervical and oropharyngeal cancers; efficacy exceeds 90% against high-grade cervical lesions in seronegative recipients."
---

# HPV-16

## Overview

Human Papillomavirus type 16 (HPV-16) is a **double-stranded DNA oncovirus** of the family *Papillomaviridae* and the most prevalent high-risk HPV type, responsible for approximately **50–60% of cervical cancers** globally and a rising burden of oropharyngeal, anal, vulvar, vaginal, and penile cancers [^sung-2021-global-cancer]. The causal link between HPV and cervical cancer was established by Harald zur Hausen, work recognised with the Nobel Prize in Physiology or Medicine in 2008 [^zur-hausen-1983-hpv-cancer].

More than **300 million people** are estimated to harbour HPV-16/18 infection at any given time, and **virtually all cervical cancer** has an HPV aetiology. HPV-16 is classified as a Group 1 human carcinogen by the IARC. Approximately **14 million new HPV infections** occur in the United States each year; most are cleared within 1–2 years by the immune system, but persistent infection with high-risk HPV types is the necessary (though not sufficient) cause of cervical carcinogenesis.

The development of **Gardasil-9** (9-valent HPV vaccine) and **Cervarix** (bivalent) represents a landmark achievement in cancer prevention vaccinology [^schiller-2012-hpv-vaccine].

## Structure

### Virion Architecture

HPV-16 is a non-enveloped icosahedral particle approximately **55 nm in diameter**. It has no lipid envelope — making it intrinsically resistant to desiccation and ether.

| Component | Description |
|:---|:---|
| **L1 major capsid protein** | 72 pentamers arranged in a T=7 icosahedral lattice; binds heparan sulphate proteoglycans (HSPGs) for initial attachment; basis of virus-like particle (VLP) vaccines |
| **L2 minor capsid protein** | Resides within the capsid cavity; facilitates endosomal escape by membrane penetration; contains cross-reactive neutralising epitopes |
| **Viral genome** | ~7.9 kb circular dsDNA; histones-like chromatin state inside the capsid |

### Genome Organisation

The HPV-16 genome is divided into three functional regions:

| Region | Genes / Elements | Function |
|:---:|:---|:---|
| **Early (E) region** | E1, E2, E4, E5, E6, E7 | Replication and oncogenesis; E1/E2 are replication initiators; E6 and E7 are the primary oncoproteins |
| **Late (L) region** | L1, L2 | Structural capsid proteins expressed only in fully differentiated keratinocytes |
| **Long control region (LCR)** | Origin of replication + promoters | Regulates viral DNA replication and transcription; contains E2 binding sites |

## Infection Mechanism

### Entry and Initial Infection

HPV-16 exclusively infects **stratified squamous epithelium**, requiring access to the **basal keratinocyte layer** (the proliferating stem cell compartment) through microtraumas or wounds. The cervical **transformation zone (squamocolumnar junction)** is particularly vulnerable due to metaplasia at this boundary.

Entry sequence:
1. **L1 binds heparan sulphate proteoglycans (HSPGs)** on basal keratinocytes and the extracellular matrix exposed at wound sites
2. Conformational change in L1 reveals the L2 N-terminus for secondary receptor engagement (likely α6 integrin, growth factor receptors)
3. Slow (12–24 h) clathrin- or caveolin-mediated **endocytosis**
4. **L2-mediated endosomal escape:** L2 inserts into the endosomal membrane as it acidifies, redirecting the viral genome to the **trans-Golgi network** and ultimately to the nucleus
5. Genome is delivered to the nucleus as a minichromosome; early gene transcription initiates from the **p97 promoter** (HPV-16 numbering)

### E6 Oncoprotein: p53 Degradation

The E6 protein (158 aa) drives cell immortalisation by degrading the **p53 tumour suppressor**:

- E6 binds the **E6AP ubiquitin ligase** (UBE3A), forming a ternary E6–E6AP–p53 complex
- E6AP ubiquitinates p53 → **26S proteasome degradation**
- Loss of p53 disables the G1/S checkpoint, prevents apoptosis in damaged cells, and impairs DNA damage responses
- E6 also activates **telomerase (hTERT)** transcription — conferring replicative immortality — and targets PDZ-domain proteins (Dlg, Scribble) that regulate cell polarity and tissue organisation

### E7 Oncoprotein: Rb Family Inactivation

The E7 protein (98 aa) drives cell cycle entry by inactivating the **retinoblastoma (Rb) tumour suppressor** [^munger-1989-e7-rb]:

- E7 binds the LXCXE motif-binding cleft of pRb, p107, and p130
- Binding disrupts the pRb–E2F complex → **free E2F transcription factors** activate S-phase gene expression (cyclin E, DHFR, PCNA)
- E7 also promotes pRb proteasomal degradation (distinct from simple binding)
- High-risk HPV E7 has ~100-fold higher affinity for Rb than low-risk HPV E7 (key determinant of oncogenic potential)
- E7 additionally inactivates **p21** (CDKN1A) and **p27** (CDKN1B) cyclin-dependent kinase inhibitors, further driving proliferation

### Episomal vs. Integrated Genome

In **productive (lytic) infection**: HPV DNA is maintained as a circular **episome** (50–200 copies/cell) and depends on E1/E2 for replication. Full productive replication and virion assembly occur only in **terminally differentiated keratinocytes** (spinous and granular layers).

In **malignant transformation**: HPV-16 DNA frequently integrates into the host genome, disrupting the **E2 ORF**. Loss of E2 eliminates its repressor function on the **E6/E7 promoter**, causing overexpression of E6 and E7 — the molecular switch from latent to oncogenic infection.

## Host Interactions

### Immune Evasion

HPV has evolved multiple strategies to persist in epithelium without triggering immune activation [^stanley-2012-hpv-immune]:

- **No systemic viraemia:** HPV replication is confined to the epithelial surface; no cytolysis of basal cells during initial infection; virus is shed from superficial (dying) cells
- **No acute inflammation:** HPV downregulates innate sensing by suppressing IFN signalling; E7 degrades IRF-3 and inhibits TLR9-mediated IFN production
- **Impaired DC activation:** Langerhans cells in HPV-infected epithelium are functionally impaired; E6/E7 suppress NF-κB activation, reducing pro-inflammatory cytokines (IL-1α, IL-8, TNF-α) that would normally alert the immune system
- **No keratinocyte death signal:** Infected basal cells remain alive and proliferating; the absence of necrosis or danger signals prevents inflammasome activation and DC maturation

Despite these evasion mechanisms, most HPV infections are eventually cleared (median ~1 year) by adaptive T cell responses and HPV-specific IgG antibodies, typically targeting L1 and E7 epitopes. Persistence occurs in ~10% of women and is associated with high viral load, immunosuppression, and certain HLA alleles.

### Oncogenesis: A Multistep Process

Cervical carcinogenesis proceeds through defined precursor lesions:

| Stage | Histology / Terminology | HPV Molecular Events |
|:---:|:---|:---|
| **Normal cervix** | Normal squamous/columnar epithelium | HPV absent or productive episomal infection |
| **CIN 1 (LSIL)** | Low-grade squamous intraepithelial lesion | Productive HPV replication; most regress spontaneously |
| **CIN 2–3 (HSIL)** | High-grade SIL; immediate cancer precursor | E6/E7 overexpression; Rb/p53 pathway disruption; chromosomal instability |
| **Invasive cervical cancer** | Squamous cell carcinoma (~75%), adenocarcinoma (~25%) | HPV integration; loss of E2 repression; TP53/CDKN2A somatic mutations |

Additional co-factors in cervical carcinogenesis include **smoking**, **high parity**, **OCP use**, **coinfection with other STIs** (C. trachomatis, HSV-2), and **HIV-related immunosuppression** (up to 22-fold increased cervical cancer risk in HIV-positive women).

## Connections

- **Infects** → [Dendritic Cell](../../../01-human/04-cellular/dendritic-cell/README.md): HPV infects mucosal keratinocytes; Langerhans cells (skin DCs) encounter HPV but are functionally suppressed by E6/E7-mediated NF-κB inhibition, impairing adaptive immune priming.
- **Damages** → [Immune System](../../../01-human/07-system/immune-system/README.md): E6/E7 suppress IFN-β induction, degrade IRF3, and inhibit TLR9; immune evasion is necessary for persistent infection and oncogenic transformation.
- **Prevents** → [Immune System](../../../01-human/07-system/immune-system/README.md): Gardasil-9 VLP vaccine generates potent neutralising IgG against HPV-16 L1, preventing infection and thus preventing oncogenesis; >90% efficacy against high-grade lesions in seronegative individuals.

## Pathology

### HPV-Associated Cancers

| Cancer site | HPV-attributable fraction | HPV types |
|:---|:---:|:---|
| **Cervical cancer** | ~100% | 16, 18 account for 70%; 16>18 |
| **Oropharyngeal squamous cell carcinoma (OPSCC)** | ~70% and rising | 16 dominant (90%+ of HPV+ OPSCC) |
| **Anal cancer** | ~90% | 16, 18 |
| **Vulvar cancer** | ~50% (HPV-dependent subset) | 16 |
| **Vaginal cancer** | ~65% | 16 |
| **Penile cancer** | ~40% | 16, 18 |

Globally, HPV-associated cancers account for approximately **690,000 new cancers per year** (2018 data) [^sung-2021-global-cancer].

### Oropharyngeal HPV Epidemiology

HPV-16-positive OPSCC (tonsillar and base-of-tongue cancer) has dramatically increased in incidence in North America and Europe since the 1990s, driven by changing sexual behaviours. HPV-positive OPSCC has a **significantly better prognosis** (5-year survival ~80–85% vs. ~40% for HPV-negative) due to greater radiosensitivity.

### Diagnosis

- **Cervical cytology (Pap smear):** Detects morphological changes (koilocytosis, dysplasia) in cervical cells
- **HPV DNA testing:** High-sensitivity PCR or signal amplification (Hybrid Capture 2); now primary screening in many countries
- **HPV genotyping:** Identifies high-risk types (16, 18 ± others)
- **p16/Ki-67 dual stain:** Immunohistochemical surrogate for E7-mediated Rb inactivation; used as a triage test
- **p16 IHC in OPSCC:** High p16 expression is a surrogate marker for HPV positivity in oropharyngeal tumours

### Prevention and Treatment

**Prevention:**

- **Gardasil-9** (9-valent HPV vaccine): Covers HPV 6, 11, 16, 18, 31, 33, 45, 52, 58; ~90% of HPV-attributable cervical cancers; >95% efficacy against CIN2/3 caused by covered types in seronegative recipients [^schiller-2012-hpv-vaccine]
- **Cervical screening:** Cytology and/or HPV testing from age 21–25; co-testing or primary HPV testing every 3–5 years

**Treatment of precancerous lesions:**
- CIN 1: Observation (most regress)
- CIN 2–3: Loop electrosurgical excision procedure (LEEP), cryotherapy, cold coagulation, or cone biopsy

**Treatment of invasive cervical cancer:**
- Early stage: Surgery (radical hysterectomy ± pelvic lymph node dissection) or concurrent chemoradiotherapy
- Advanced/metastatic: Platinum-based chemotherapy ± bevacizumab; pembrolizumab (anti-PD-1) approved for recurrent/metastatic PD-L1-positive cervical cancer

No approved antiviral agents directly target HPV replication.

## See Also

- [Dendritic Cell](../../../01-human/04-cellular/dendritic-cell/README.md) — antigen presentation and immune evasion target
- [Immune System](../../../01-human/07-system/immune-system/README.md) — evaded defence and vaccine target

[^zur-hausen-1983-hpv-cancer]: zur Hausen H. Human genital cancer: synergism between two virus infections or synergism between a virus infection and initiating events? *Lancet.* 1982;2(8312):1370-2. [doi:10.1016/S0140-6736(82)91273-X](https://doi.org/10.1016/S0140-6736(82)91273-X) · [PubMed 6128601](https://pubmed.ncbi.nlm.nih.gov/6128601/)
[^schiffman-2007-hpv-cancer-review]: Schiffman M, Castle PE, Jeronimo J, Rodriguez AC, Wacholder S. Human papillomavirus and cervical cancer. *Lancet.* 2007;370(9590):890-907. [doi:10.1016/S0140-6736(07)61416-0](https://doi.org/10.1016/S0140-6736(07)61416-0) · [PubMed 17826171](https://pubmed.ncbi.nlm.nih.gov/17826171/)
[^munger-1989-e7-rb]: Munger K, Werness BA, Dyson N, Phelps WC, Harlow E, Howley PM. Complex formation of human papillomavirus E7 proteins with the retinoblastoma tumor suppressor gene product. *EMBO J.* 1989;8(13):4099-105. [doi:10.1002/j.1460-2075.1989.tb08594.x](https://doi.org/10.1002/j.1460-2075.1989.tb08594.x) · [PubMed 2556261](https://pubmed.ncbi.nlm.nih.gov/2556261/)
[^schiller-2012-hpv-vaccine]: Schiller JT, Castellsague X, Garland SM. A review of clinical trials of human papillomavirus prophylactic vaccines. *Vaccine.* 2012;30(Suppl 5):F123-38. [doi:10.1016/j.vaccine.2012.04.108](https://doi.org/10.1016/j.vaccine.2012.04.108) · [PubMed 23199956](https://pubmed.ncbi.nlm.nih.gov/23199956/)
[^sung-2021-global-cancer]: Sung H, Ferlay J, Siegel RL, et al. Global Cancer Statistics 2020: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries. *CA Cancer J Clin.* 2021;71(3):209-249. [doi:10.3322/caac.21660](https://doi.org/10.3322/caac.21660) · [PubMed 33538338](https://pubmed.ncbi.nlm.nih.gov/33538338/)
[^stanley-2012-hpv-immune]: Stanley M. Immunobiology of HPV and HPV vaccines. *Gynecol Oncol.* 2010;118(1 Suppl):S12-6. [doi:10.1016/j.ygyno.2010.04.015](https://doi.org/10.1016/j.ygyno.2010.04.015) · [PubMed 20494223](https://pubmed.ncbi.nlm.nih.gov/20494223/)
