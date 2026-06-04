---
schema: pathogen-entry/v1
id: influenza-a
name: Influenza A virus
atlas: 02-pathogen
scale: 01-viruses
status: draft
last_reviewed: 2026-06-03
summary: "Enveloped, segmented −ssRNA virus (Orthomyxoviridae). 8 genome segments; HA (18 subtypes) + NA (11 subtypes). Infects respiratory epithelium via sialic acid; antigenic drift/shift drives annual epidemics and pandemic potential."
aliases: ["influenza A", "flu", "IAV", "H1N1", "H3N2", "influenza type A virus"]
sources:
  - id: palese-2004-influenza-review
    type: peer-reviewed
    cite: "Palese P. Influenza: old and new threats. Nat Med. 2004;10(12 Suppl):S82-7."
    doi: "10.1038/nm1141"
    pmid: "15577936"
    url: "https://doi.org/10.1038/nm1141"
  - id: webster-1992-influenza-review
    type: peer-reviewed
    cite: "Webster RG, Bean WJ, Gorman OT, Chambers TM, Kawaoka Y. Evolution and ecology of influenza A viruses. Microbiol Rev. 1992;56(1):152-79."
    doi: "10.1128/mr.56.1.152-179.1992"
    pmid: "1579108"
    url: "https://doi.org/10.1128/mr.56.1.152-179.1992"
  - id: taubenberger-2006-1918-flu
    type: peer-reviewed
    cite: "Taubenberger JK, Morens DM. 1918 influenza: the mother of all pandemics. Emerg Infect Dis. 2006;12(1):15-22."
    doi: "10.3201/eid1201.050979"
    pmid: "16494711"
    url: "https://doi.org/10.3201/eid1201.050979"
  - id: who-influenza-factsheet
    type: regulatory
    cite: "World Health Organization. Influenza (seasonal) Fact Sheet. WHO; 2023."
    url: "https://www.who.int/news-room/fact-sheets/detail/influenza-(seasonal)"
    accessed: "2026-06-03"
cross_links:
  - target: 01-human/04-cellular/type-ii-pneumocyte
    relation: infects
    note: "Influenza A infects AT2 cells expressing α-2,3 sialic acid receptors (avian-like strains, e.g., H5N1) and α-2,6 sialic acid receptors (human strains, H1N1/H3N2); AT2 destruction causes loss of surfactant and alveolar repair capacity."
  - target: 01-human/06-organ/lung
    relation: damages
    note: "Influenza A causes primary viral pneumonitis (bilateral interstitial infiltrates), secondary bacterial pneumonia (classically Staphylococcus aureus, Streptococcus pneumoniae), and ARDS in severe cases — all causing acute lung damage."
  - target: 01-human/07-system/respiratory-system
    relation: damages
    note: "Influenza A is primarily a respiratory tract pathogen: upper respiratory illness in most cases; in severe disease, tracheobronchitis, viral pneumonitis, and ARDS impair ventilation and gas exchange throughout the respiratory system."
---

# Influenza A virus

## Overview

Influenza A virus (IAV) is a member of the family **Orthomyxoviridae** — an enveloped, **segmented, negative-sense single-stranded RNA (−ssRNA) virus** whose genome is divided into **8 discrete RNA segments** encoding 10–14 proteins depending on the strain. IAV infects a wide range of avian and mammalian species and is the cause of the most significant respiratory epidemics and pandemics in human history, including the catastrophic 1918 H1N1 influenza pandemic that killed an estimated 50–100 million people [^taubenberger-2006-1918-flu].

IAV is classified by its two major surface glycoproteins:
- **Haemagglutinin (HA):** 18 subtypes (H1–H18) — mediates receptor binding and membrane fusion
- **Neuraminidase (NA):** 11 subtypes (N1–N11) — mediates virion release from infected cells

Current human seasonal influenza A strains are primarily **H1N1** (first pandemic 1918; re-emerged 2009 as "swine flu") and **H3N2** (emerged 1968 Hong Kong pandemic). Avian IAV strains (H5N1, H7N9) have high pandemic potential if they acquire efficient human-to-human transmission.

## Structure

### Virion Architecture

| Component | Description |
|:---|:---|
| **Envelope** | Lipid bilayer derived from host plasma membrane |
| **Haemagglutinin (HA)** | Homotrimer; ~500 copies per virion; binds sialic acid; responsible for receptor tropism and antigenic classification |
| **Neuraminidase (NA)** | Homotetramer; ~100 copies per virion; cleaves sialic acid to release virions from cells; target of oseltamivir/zanamivir |
| **M2 ion channel** | Proton channel; required for viral uncoating; target of amantadine/rimantadine (now largely ineffective due to resistance) |
| **Matrix protein M1** | Lines the inner face of the envelope; scaffolds the virion |
| **8 RNA segments (vRNA)** | Encapsidated in ribonucleoprotein (RNP) complexes with nucleoprotein (NP) and the RNA-dependent RNA polymerase complex (PB1, PB2, PA) |
| **Virion size** | ~80–120 nm diameter (pleomorphic: spherical to filamentous) |

### Genome Segments

| Segment | Encoded protein(s) | Function |
|:---:|:---|:---|
| 1 | PB2 | RNA polymerase subunit; cap-binding |
| 2 | PB1, PB1-F2 | RNA polymerase catalytic subunit; virulence factor |
| 3 | PA, PA-X | RNA polymerase subunit; endonuclease; host shutoff |
| 4 | Haemagglutinin (HA) | Receptor binding, membrane fusion |
| 5 | Nucleoprotein (NP) | RNA encapsidation; vRNP assembly |
| 6 | Neuraminidase (NA) | Virion release; sialic acid cleavage |
| 7 | M1, M2 | Matrix protein; ion channel |
| 8 | NS1, NS2/NEP | Interferon antagonist; nuclear export |

## Infection Mechanism

### Receptor Binding and Cell Tropism

Influenza A HA binds to **sialic acid (Sia)** residues on glycoproteins and glycolipids of respiratory epithelial cells. The linkage of sialic acid to the penultimate galactose determines tropism:

- **α-2,6 Sia:** Predominant in human upper respiratory epithelium (trachea, bronchi); recognised by human H1N1 and H3N2 HA → seasonal human influenza infects the upper respiratory tract preferentially
- **α-2,3 Sia:** Predominant in avian intestinal epithelium and in human lower respiratory tract (alveolar epithelium, AT2 cells); recognised by avian H5N1 HA → avian flu infects the lower respiratory tract directly → high rate of severe pneumonitis

After HA binding, the virus is endocytosed. Endosomal acidification (pH ~5.0) triggers:
1. HA conformational change → fusion peptide exposes and inserts into the endosomal membrane
2. M2 ion channel allows H⁺ influx into the virion → vRNP release into cytoplasm
3. vRNPs import into the nucleus → viral RNA replication begins

### Replication Cycle

1. **Binding** → endocytosis
2. **Uncoating:** M2 proton channel + HA conformational change → vRNP into cytoplasm
3. **Nuclear import:** vRNPs enter nucleus
4. **Transcription:** PB1-PB2-PA complex synthesises (+)mRNA by "cap-snatching" (PB2 caps + PA cleaves host pre-mRNA caps)
5. **Replication:** PB1 synthesises complementary RNA (cRNA) → amplifies vRNA
6. **Assembly:** New vRNPs export from nucleus via NS2/NEP + M1; package into 8 distinct segments via specific packaging signals
7. **Budding:** New virions bud from the apical surface of epithelial cells; NA cleaves sialic acid on released virions to prevent re-attachment
8. **Release:** Progeny virions released to infect adjacent cells; incubation period 1–4 days

## Host Interactions

### Innate Immunity

IAV is detected by innate immune sensors:
- **RIG-I:** Cytoplasmic dsRNA sensor; detects replication intermediates → IFN-β production
- **TLR3/7/8:** Endosomal ssRNA/dsRNA sensors in plasmacytoid DCs → IFN-α production

**NS1** is IAV's primary interferon antagonist: binds dsRNA to prevent RIG-I activation; binds and inactivates PKR; sequesters 3'-polyadenylation factors to inhibit host mRNA processing.

### Innate Response Evasion and Immunopathology

In severe influenza (especially H5N1 avian strains), NS1-mediated IFN suppression is followed by an exuberant delayed innate response — a **cytokine storm** with high levels of IL-6, TNF-α, IP-10, MCP-1. This dysregulated inflammation, rather than viral cytolysis alone, drives the severe alveolar damage seen in H5N1 and 1918 pandemic influenza.

### Adaptive Immunity and Antigenic Variation

Humoral immunity to influenza is strain-specific, directed primarily at **HA** and **NA**. This is why influenza can reinfect the same person annually — the virus evades prior immunity by:

- **Antigenic drift:** Accumulation of point mutations in HA/NA under immune selection pressure → gradual antigenic change → seasonal epidemic strains requiring annual vaccine updates [^webster-1992-influenza-review]
- **Antigenic shift:** Reassortment of genome segments between different IAV strains infecting the same cell (e.g., a mixed human–avian infection in a pig) → sudden emergence of a novel HA subtype to which humans have no immunity → **pandemic potential** (e.g., 1968 H3N2, 2009 H1N1)

## Connections

- **Infects** → [Type II pneumocyte](../../../01-human/04-cellular/type-ii-pneumocyte/README.md): Influenza A binds sialic acid receptors on AT2 cells and infects them, destroying surfactant-producing progenitor cells and impairing alveolar repair capacity.
- **Damages** → [Lung](../../../01-human/06-organ/lung/README.md): Primary viral pneumonitis, secondary bacterial pneumonia (Staphylococcus aureus, Streptococcus pneumoniae), and ARDS caused by widespread alveolar damage.
- **Damages** → [Respiratory system](../../../01-human/07-system/respiratory-system/README.md): IAV causes upper and lower respiratory tract disease ranging from mild tracheobronchitis to fulminant respiratory failure; severe disease impairs both ventilation and gas exchange at the system level.

## Pathology

### Clinical Spectrum

| Severity | Features | Pathology |
|:---|:---|:---|
| **Uncomplicated (most common)** | Fever, myalgia, cough, rhinorrhoea, 5–7 days | Tracheobronchitis; no parenchymal involvement |
| **Complicated — primary viral pneumonia** | Bilateral infiltrates, hypoxaemia, rapid progression | Diffuse alveolar damage: AT1 and AT2 cell death, hyaline membranes, alveolar haemorrhage |
| **Complicated — secondary bacterial pneumonia** | Pneumonia following 5–7 days of improvement | Focal consolidation; Staphylococcus aureus commonest; very high mortality |
| **ARDS** | PaO₂/FiO₂ <200, bilateral infiltrates | Extensive DAD; ICU-level care required |
| **Pandemic / avian strain** | H5N1, 1918 H1N1, 2009 H1N1 | Cytokine storm, multi-organ failure, very high mortality in young adults (W-shaped mortality curve in 1918) |

### Epidemiology

- Annual seasonal influenza: ~1 billion infections; ~3–5 million severe cases; **290,000–650,000 deaths/year** globally [^who-influenza-factsheet]
- 1918 pandemic: estimated 50–100 million deaths [^taubenberger-2006-1918-flu]
- 2009 pandemic (H1N1): ~284,000 deaths in first year; disproportionate mortality in younger adults

### Treatment and Prevention

- **Antivirals:** Oseltamivir (Tamiflu), zanamivir (Relenza), baloxavir (Xofluza) — most effective within 48 h of symptom onset; reduce severity and duration; reduce hospitalisation in high-risk patients
- **Vaccination:** Inactivated or live-attenuated influenza vaccine (IIV, LAIV); updated annually to match predicted circulating strains; ~40–60% efficacy in well-matched seasons; near-universal recommendation for healthcare workers and high-risk groups [^who-influenza-factsheet]

## See Also

- [Type II pneumocyte](../../../01-human/04-cellular/type-ii-pneumocyte/README.md) — primary infected cell in severe disease.
- [Lung](../../../01-human/06-organ/lung/README.md) — the organ damaged.
- [Respiratory system](../../../01-human/07-system/respiratory-system/README.md) — the system level impact.

[^palese-2004-influenza-review]: Palese P. Influenza: old and new threats. *Nat Med.* 2004;10(12 Suppl):S82-7. [doi:10.1038/nm1141](https://doi.org/10.1038/nm1141) · [PubMed 15577936](https://pubmed.ncbi.nlm.nih.gov/15577936/)
[^webster-1992-influenza-review]: Webster RG, Bean WJ, Gorman OT, Chambers TM, Kawaoka Y. Evolution and ecology of influenza A viruses. *Microbiol Rev.* 1992;56(1):152-79. [doi:10.1128/mr.56.1.152-179.1992](https://doi.org/10.1128/mr.56.1.152-179.1992) · [PubMed 1579108](https://pubmed.ncbi.nlm.nih.gov/1579108/)
[^taubenberger-2006-1918-flu]: Taubenberger JK, Morens DM. 1918 influenza: the mother of all pandemics. *Emerg Infect Dis.* 2006;12(1):15-22. [doi:10.3201/eid1201.050979](https://doi.org/10.3201/eid1201.050979) · [PubMed 16494711](https://pubmed.ncbi.nlm.nih.gov/16494711/)
[^who-influenza-factsheet]: World Health Organization. Influenza (seasonal) Fact Sheet. [who.int/news-room/fact-sheets/detail/influenza-(seasonal)](https://www.who.int/news-room/fact-sheets/detail/influenza-(seasonal))
