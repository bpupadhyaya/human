---
schema: vaccine-entry/v1
id: nvx-cov2373
name: NVX-CoV2373 (Nuvaxovid)
atlas: 04-vaccine
platform: 03-recombinant-subunit
status: draft
last_reviewed: 2026-06-04
summary: "Recombinant full-length trimeric spike nanoparticle vaccine (baculovirus/Sf9 expression) + Matrix-M saponin adjuvant. Developed by Novavax. 90.4% efficacy in PREVENT-19 (US/Mexico). Refrigerator-stable; no mRNA or viral DNA."
aliases: ["Nuvaxovid", "NVX-CoV2373", "Novavax COVID-19 vaccine", "Covovax"]
target_pathogens:
  - target: 02-pathogen/01-viruses/sars-cov-2
    antigen: spike-trimeric-nanoparticle
    coverage: ["wild-type (Wuhan-Hu-1)", "alpha", "beta (partial)", "delta (partial)", "omicron (reduced)"]
antigens:
  - name: "SARS-CoV-2 spike protein (full-length trimeric nanoparticle)"
    source_pathogen: 02-pathogen/01-viruses/sars-cov-2
    modification: "Full-length recombinant spike protein; self-assembles into ~35 nm nanoparticles (~14 trimers per particle) on a polysorbate 80 micelle scaffold; no 2P prefusion stabilization in original sequence; furin cleavage site intact"
    encoded_as: "Protein produced in Spodoptera frugiperda (Sf9) insect cells using a baculovirus expression vector system (BEVS); purified by chromatography and combined with polysorbate 80 lipid nanoparticle scaffold"
delivery_system: "Purified spike protein nanoparticles (~35 nm) co-administered with Matrix-M adjuvant (saponin-based immune stimulating complex)"
adjuvants:
  - name: "Matrix-M"
    description: "Cage-like ~40 nm particles derived from purified Quillaja saponaria Molina bark saponins (QS-21 and QS-7); formulated with cholesterol and phospholipids; activates innate immune DCs, drives Th1 and Th2 responses, and enhances MHC I cross-presentation to CD8⁺ T cells"
route_of_administration: "intramuscular"
dose_schedule:
  primary_series_adult: "2 doses, 21 days apart, 5 µg spike protein + 50 µg Matrix-M each"
  booster: "Single booster authorized in some jurisdictions; heterologous use as booster after mRNA or viral-vector primary series authorized in several countries"
manufacturer:
  developer: "Novavax, Inc. (Gaithersburg, Maryland, USA)"
  partners: ["Serum Institute of India (Covovax — global access/COVAX supply)", "SK Bioscience (South Korea)", "Takeda (Japan — TAK-019)", "BARDA (US government funding)", "CEPI (Coalition for Epidemic Preparedness Innovations)"]
regulatory_status:
  - body: "EMA"
    status: "Conditional Marketing Authorization (Nuvaxovid)"
    date: "2021-12-20"
  - body: "WHO"
    status: "Emergency Use Listing"
    date: "2021-12-17"
  - body: "FDA"
    status: "Emergency Use Authorization"
    date: "2022-07-13"
  - body: "FDA"
    status: "Biologics License Application (BLA) approved — adults 18+"
    date: "2022-07-13"
cold_chain: "2°C to 8°C standard refrigeration; 6-month shelf life; no freeze-thaw cycles required — fully compatible with routine vaccine cold chain worldwide"
discontinued: false
xrefs:
  who_atc: "J07BX03"
  nct_primary: "NCT04611802"
  vo: "VO:0005367"
clinical_trials:
  - id: "NCT04368988"
    tag: "Phase 1/2 2019nCoV-101 (UK)"
  - id: "NCT04533399"
    tag: "Phase 2b/3 2019nCoV-301 (South Africa)"
  - id: "NCT04611802"
    tag: "Phase 3 PREVENT-19 (US/Mexico)"
  - id: "NCT04742738"
    tag: "Phase 3 30002 (Europe)"
who_essential_medicine: false
sources:
  - id: heath-2021-phase1
    type: peer-reviewed
    cite: "Heath PT, Galiza EP, Baxter DN, et al. Safety and Efficacy of NVX-CoV2373 Covid-19 Vaccine. N Engl J Med. 2021;385(13):1172-1183."
    doi: "10.1056/NEJMoa2107659"
    pmid: "34192426"
    url: "https://doi.org/10.1056/NEJMoa2107659"
  - id: dunkle-2022-prevent19
    type: peer-reviewed
    cite: "Dunkle LM, Kotloff KL, Gay CL, et al. Efficacy and Safety of NVX-CoV2373 in Adults in the United States and Mexico. N Engl J Med. 2022;386(6):531-543."
    doi: "10.1056/NEJMoa2116185"
    pmid: "34986284"
    url: "https://doi.org/10.1056/NEJMoa2116185"
  - id: shinde-2021-south-africa
    type: peer-reviewed
    cite: "Shinde V, Bhikha S, Hoosain Z, et al. Efficacy of NVX-CoV2373 Covid-19 Vaccine against the B.1.351 Variant. N Engl J Med. 2021;384(20):1899-1909."
    doi: "10.1056/NEJMoa2103055"
    pmid: "33951374"
    url: "https://doi.org/10.1056/NEJMoa2103055"
  - id: novavax-ema-assessment
    type: regulatory
    cite: "European Medicines Agency. Nuvaxovid — Assessment report. EMA/462845/2021. EMA; 2021."
    url: "https://www.ema.europa.eu/en/medicines/human/EPAR/nuvaxovid"
    accessed: "2026-06-04"
  - id: keech-2020-phase1
    type: peer-reviewed
    cite: "Keech C, Albert G, Cho I, et al. Phase 1-2 Trial of a SARS-CoV-2 Recombinant Spike Protein Nanoparticle Vaccine. N Engl J Med. 2020;383(24):2320-2332."
    doi: "10.1056/NEJMoa2026920"
    pmid: "32877576"
    url: "https://doi.org/10.1056/NEJMoa2026920"
cross_links:
  - target: 02-pathogen/01-viruses/sars-cov-2
    relation: immunizes-against
    note: "NVX-CoV2373 induces anti-spike IgG and T-cell responses; 90.4% efficacy against symptomatic COVID-19 (predominantly Alpha/other non-Delta strains) in PREVENT-19; ~51% efficacy in South Africa against the Beta variant."
  - target: 01-human/07-system/immune-system
    relation: elicits
    note: "Matrix-M adjuvant activates innate immunity and promotes Th1/Th2 balanced adaptive responses; spike nanoparticle antigen mimics viral surface to optimize BCR engagement."
  - target: 01-human/04-cellular/dendritic-cell
    relation: elicits
    note: "Matrix-M activates DCs at the injection site, promoting MHC I and MHC II antigen presentation; drives both humoral and cellular arms of immunity."
  - target: 01-human/04-cellular/b-cell
    relation: elicits
    note: "Spike nanoparticles efficiently crosslink B-cell receptors due to repetitive antigen display (~14 trimers per particle); Matrix-M adjuvant supports germinal center formation and affinity maturation."
  - target: 01-human/04-cellular/t-helper-cell
    relation: elicits
    note: "Matrix-M drives Th1-biased CD4⁺ T-cell responses supporting IgG class-switching and CD8⁺ T-cell help; both spike-specific Th1 and Th2 cells detected after vaccination."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: elicits
    note: "Anti-spike IgG titers — particularly IgG1 and IgG3 subclasses — are the primary correlate of protection; pseudovirus neutralization titers after NVX-CoV2373 are approximately 4-fold higher than convalescent plasma benchmarks."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: elicits
    note: "Matrix-M facilitates cross-presentation via MHC II, enabling CD4⁺ T-cell help for antibody responses; antigen uptake by DCs at injection site is enhanced by adjuvant-driven inflammation."
---

# NVX-CoV2373 (Nuvaxovid)

## Overview

NVX-CoV2373 — marketed as **Nuvaxovid** (EU/US) and **Covovax** (India/COVAX) — is a recombinant protein subunit COVID-19 vaccine developed by Novavax. It delivers a **purified, full-length trimeric spike protein nanoparticle** combined with **Matrix-M**, a saponin-based adjuvant. Unlike mRNA or viral-vector vaccines, NVX-CoV2373 contains **no mRNA, no DNA, and no live viral material** — it is a conventional protein subunit vaccine using a well-established vaccine platform [^keech-2020-phase1].

The vaccine demonstrated **90.4% efficacy** against symptomatic COVID-19 (predominantly Alpha variant) in the phase 3 PREVENT-19 trial in the United States and Mexico [^dunkle-2022-prevent19]. In the UK COV005 trial against predominantly Alpha variant, efficacy was 89.7%. Against the Beta variant in South Africa, efficacy dropped to ~51% — demonstrating the antigenic distance challenge even for protein-based vaccines when variants substantially alter the spike [^shinde-2021-south-africa].

NVX-CoV2373 achieved regulatory authorization later than mRNA and viral-vector vaccines but fulfilled an important role: it offered a **protein-based option for populations hesitant about mRNA or viral-vector platforms**, and its **standard 2–8°C cold chain** made it deployable wherever routine vaccines are delivered. Its authorized use as a **heterologous booster** after mRNA or viral-vector primary series demonstrated cross-platform booster utility.

## Platform Technology

### Spike Protein Nanoparticle

The antigen in NVX-CoV2373 is the **full-length SARS-CoV-2 spike protein** expressed in *Spodoptera frugiperda* Sf9 insect cells using a **baculovirus expression vector system (BEVS)** — the same platform used to produce Cervarix (HPV) and Flublok (influenza) antigens.

Key structural features:
- Spike protein trimers are combined with a **polysorbate 80 micelle scaffold** and self-assemble into **~35 nm nanoparticles** containing approximately 14 spike trimers per particle
- The repetitive display of antigen on a nanoparticle surface is designed to efficiently crosslink B-cell receptors, improving B-cell activation beyond what soluble monomer antigen can achieve
- The nanoparticle structure mimics the spike density on the authentic SARS-CoV-2 virion surface
- Unlike the 2P-stabilized spike used in mRNA vaccines, the original NVX-CoV2373 spike is full-length without engineering for prefusion stability (though post-fusion conformation may be partly represented)

### Matrix-M Adjuvant

Matrix-M is a **saponin-based immune-stimulating complex (ISCOM)** derived from the inner bark of *Quillaja saponaria* Molina (soapbark tree). Composition:

- Purified saponin fractions **QS-21** and **QS-7** combined with cholesterol and phospholipid to form ~40 nm cage-like particles
- Promotes antigen uptake by dendritic cells at the injection site
- Activates multiple innate pathways: **NF-κB, NLRP3 inflammasome, type I IFN**
- Drives a balanced **Th1/Th2** adaptive response — producing both IgG1 and IgG3 (Th1-associated) and IgG2/IgG4 (Th2-associated) antibodies
- Uniquely promotes **MHC I cross-presentation**, enabling CD8⁺ T-cell responses even though the protein is delivered extracellularly
- Matrix-M is also the adjuvant in **Shingrix** (RZV, Zoster subunit vaccine — the most effective subunit vaccine in clinical use, >97% efficacy)

The combination of nanoparticle antigen + Matrix-M is critical: spike protein alone without adjuvant elicits weak immunogenicity. Matrix-M provides the "danger signal" that activates innate immunity and amplifies adaptive responses.

## Immunogenicity

### Humoral Response

Phase 1/2 data showed **robust anti-spike IgG titers** after 2-dose vaccination, with:
- Pseudovirus neutralization titers after dose 2 approximately **4-fold higher than convalescent serum** benchmarks at comparable timepoints
- Both IgG1 (Th1-associated) and IgG4 (Th2-associated) subclasses induced
- Antibodies targeting the receptor-binding domain (RBD) and N-terminal domain (NTD) of spike

[^keech-2020-phase1]

### T-Cell Response

- Spike-specific **CD4⁺ T cells** detected in PBMC assays post-vaccination; predominantly Th1 phenotype (IFN-γ/TNF-producing)
- **CD8⁺ T-cell responses** detectable above background — unusual for a subunit vaccine, attributable to Matrix-M's cross-presentation capability
- T-cell responses may contribute to protection against severe disease even as antibody titers wane over months post-vaccination

## Efficacy

### Phase 3 Clinical Trials

| Trial | Region | Primary circulating variant | Efficacy |
|:---|:---|:---|:---|
| PREVENT-19 (NCT04611802) | USA/Mexico | Alpha/ancestral (~90% Alpha at end of enrollment) | **90.4%** (95% CI: 82.9–94.6%) |
| COV005 UK | UK | Alpha | **89.7%** |
| Phase 2b/3 South Africa | South Africa | Beta (B.1.351) | **51.0%** (95% CI: −0.6 to 76.2%) |
| Phase 3 Europe (NCT04742738) | EU | Delta (later phase) | ~79–82% (preliminary) |

The South Africa data highlighted that Beta variant, with three RBD mutations (K417N, E484K, N501Y), substantially reduced antibody neutralization — a cross-platform finding also seen with mRNA vaccines.

### As Heterologous Booster

NVX-CoV2373 was authorized as a heterologous booster in the US and EU after mRNA or viral-vector primary series. Studies demonstrated:
- Non-inferior anti-spike IgG titers vs homologous mRNA booster
- Particularly favorable reactogenicity profile as a booster (lower fever/fatigue rates vs mRNA boosters)
- Utility for individuals seeking a protein-based vaccine option for their booster dose

## Safety

### Common Adverse Events

| Adverse event | Rate | Onset |
|:---|:---|:---|
| Injection site pain/tenderness | Very common (>70%) | Day 1–2 |
| Fatigue, headache, myalgia | Common (30–50%) | Day 1–2 |
| Low-grade fever | Uncommon (<15%) | Day 1–2 |
| Nausea | Uncommon | Day 1–2 |

Reactogenicity was notably **milder than mRNA vaccines** in comparative studies — particularly lower rates of fever and severe systemic reactions. This mild reactogenicity profile contributed to NVX-CoV2373's appeal to vaccine-hesitant populations.

### Rare Adverse Events

- **Myocarditis/pericarditis:** Very rare cases reported post-authorization (estimated rate: ~1–4 per 100,000 doses, primarily young males after dose 2); lower rate than observed with mRNA vaccines in this demographic
- No VITT-equivalent safety signal identified (unlike ChAdOx1 platforms)

## Significance for the Vaccine Atlas

NVX-CoV2373 represents a critical **proof of concept** that the protein-subunit platform — with modern adjuvants — can match the efficacy of mRNA vaccines against original strain SARS-CoV-2 while maintaining the logistical advantages of standard cold chain. Its weaker performance against Beta and reduced Omicron protection illustrate the same antigen-design constraint faced by all first-generation COVID-19 vaccines: full-length, unmodified spike antigens do not confer cross-protective immunity against antigenically divergent variants.

From the vaccine design perspective, NVX-CoV2373 vs mRNA-1273 demonstrates that **antigen design** (2P-stabilized vs unmodified spike) and **antigen persistence** (mRNA vs protein) matter as much as adjuvant for determining T-cell responses, while **adjuvant choice** (Matrix-M vs LNP's intrinsic adjuvanticity) shapes the cellular immune profile.

## Connections

- `immunizes-against` → **[SARS-CoV-2](../../../../02-pathogen/01-viruses/sars-cov-2/README.md)** — 90.4% efficacy in PREVENT-19; ~51% against Beta variant
- `elicits` → **[Immune System](../../../../01-human/07-system/immune-system/README.md)** — innate activation + Th1/Th2 adaptive response
- `elicits` → **[Dendritic Cell](../../../../01-human/04-cellular/dendritic-cell/README.md)** — Matrix-M activates DCs; drives antigen presentation via MHC I and II
- `elicits` → **[B Cell](../../../../01-human/04-cellular/b-cell/README.md)** — nanoparticle multivalent display drives BCR crosslinking and germinal center reaction
- `elicits` → **[T Helper Cell](../../../../01-human/04-cellular/t-helper-cell/README.md)** — Th1-biased CD4⁺ response supports IgG class-switching and CD8⁺ help
- `elicits` → **[IgG](../../../../01-human/03-molecular/immunoglobulin-g/README.md)** — anti-spike IgG1/IgG3 are primary correlates of protection
- `elicits` → **[MHC Class II](../../../../01-human/03-molecular/mhc-class-ii/README.md)** — Matrix-M facilitates MHC II antigen presentation and cross-presentation

[^keech-2020-phase1]: Keech C, Albert G, Cho I, et al. Phase 1-2 Trial of a SARS-CoV-2 Recombinant Spike Protein Nanoparticle Vaccine. *N Engl J Med.* 2020;383(24):2320-2332. [doi:10.1056/NEJMoa2026920](https://doi.org/10.1056/NEJMoa2026920) · [PubMed 32877576](https://pubmed.ncbi.nlm.nih.gov/32877576/)
[^heath-2021-phase1]: Heath PT, Galiza EP, Baxter DN, et al. Safety and Efficacy of NVX-CoV2373 Covid-19 Vaccine. *N Engl J Med.* 2021;385(13):1172-1183. [doi:10.1056/NEJMoa2107659](https://doi.org/10.1056/NEJMoa2107659) · [PubMed 34192426](https://pubmed.ncbi.nlm.nih.gov/34192426/)
[^dunkle-2022-prevent19]: Dunkle LM, Kotloff KL, Gay CL, et al. Efficacy and Safety of NVX-CoV2373 in Adults in the United States and Mexico. *N Engl J Med.* 2022;386(6):531-543. [doi:10.1056/NEJMoa2116185](https://doi.org/10.1056/NEJMoa2116185) · [PubMed 34986284](https://pubmed.ncbi.nlm.nih.gov/34986284/)
[^shinde-2021-south-africa]: Shinde V, Bhikha S, Hoosain Z, et al. Efficacy of NVX-CoV2373 Covid-19 Vaccine against the B.1.351 Variant. *N Engl J Med.* 2021;384(20):1899-1909. [doi:10.1056/NEJMoa2103055](https://doi.org/10.1056/NEJMoa2103055) · [PubMed 33951374](https://pubmed.ncbi.nlm.nih.gov/33951374/)
[^novavax-ema-assessment]: European Medicines Agency. Nuvaxovid — Assessment report. EMA/462845/2021. [ema.europa.eu](https://www.ema.europa.eu/en/medicines/human/EPAR/nuvaxovid)
