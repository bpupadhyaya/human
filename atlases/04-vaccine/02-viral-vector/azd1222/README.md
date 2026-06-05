---
schema: vaccine-entry/v1
id: azd1222
name: AZD1222 (Vaxzevria, ChAdOx1-S)
atlas: 04-vaccine
platform: 02-viral-vector
status: draft
last_reviewed: 2026-06-04
summary: "Non-replicating chimpanzee adenovirus (ChAdOx1) vector encoding the SARS-CoV-2 full-length spike protein. Developed by Oxford/AstraZeneca. Refrigerator-stable; ~67–70% efficacy against original strain; rare VITT adverse event."
aliases: ["Vaxzevria", "ChAdOx1-S", "ChAdOx1 nCoV-19", "COVID-19 Vaccine AstraZeneca", "Covishield", "AZD1222"]
target_pathogens:
  - target: 02-pathogen/01-viruses/sars-cov-2
    antigen: spike-full-length
    coverage: ["wild-type (Wuhan-Hu-1)", "alpha", "delta (partial)", "omicron (reduced)"]
antigens:
  - name: "SARS-CoV-2 spike protein (full-length, no prefusion stabilization in original)"
    source_pathogen: 02-pathogen/01-viruses/sars-cov-2
    modification: "Full-length spike including furin cleavage site; tissue plasminogen activator (tPA) signal peptide for secretion; no 2P stabilization in original design"
    encoded_as: "Double-stranded DNA transgene inside E1/E3-deleted ChAdOx1 adenovirus; CMV promoter drives spike expression"
delivery_system: "Replication-deficient chimpanzee adenovirus (ChAdOx1); E1- and E3-deleted; cannot replicate in human cells"
adjuvants: []
route_of_administration: "intramuscular"
dose_schedule:
  primary_series_adult: "2 doses, 4–12 weeks apart, 5×10¹⁰ viral particles each; 8–12 weeks interval associated with higher efficacy (62–90%)"
  booster: "Heterologous mRNA booster widely used in many countries post-primary series"
manufacturer:
  developer: "University of Oxford / AstraZeneca (Cambridge, UK)"
  partners: ["Serum Institute of India (Covishield — primary global supply)", "BARDA (US government funding)", "Fiocruz (Brazil)", "SK Bioscience (South Korea)"]
regulatory_status:
  - body: "MHRA"
    status: "Conditional Marketing Authorization"
    date: "2021-01-04"
  - body: "EMA"
    status: "Conditional Marketing Authorization"
    date: "2021-01-29"
  - body: "WHO"
    status: "Emergency Use Listing"
    date: "2021-02-15"
  - body: "FDA"
    status: "Not authorized in the United States"
    date: "—"
cold_chain: "2°C to 8°C (standard refrigerator temperature); major logistical advantage over mRNA vaccines for low-resource settings; 6-month shelf life refrigerated"
discontinued: false
xrefs:
  who_atc: "J07BX03"
  eudract: "2020-001228-32"
clinical_trials:
  - id: "NCT04324606"
    tag: "Phase 1/2 COV001 (UK)"
  - id: "NCT04400838"
    tag: "Phase 2/3 COV002 (UK)"
  - id: "ISRCTN89951424"
    tag: "Phase 3 pooled interim (UK/Brazil/South Africa)"
  - id: "NCT04516746"
    tag: "D8110C00001 Phase 3 US/Chile/Peru"
who_essential_medicine: false
sources:
  - id: folegatti-2020-phase1
    type: peer-reviewed
    cite: "Folegatti PM, Ewer KJ, Aley PK, et al. Safety and immunogenicity of the ChAdOx1 nCoV-19 vaccine against SARS-CoV-2: a preliminary report of a phase 1/2, single-blind, randomised controlled trial. Lancet. 2020;396(10249):467-478."
    doi: "10.1016/S0140-6736(20)31604-4"
    pmid: "32702298"
    url: "https://doi.org/10.1016/S0140-6736(20)31604-4"
  - id: voysey-2021-phase3
    type: peer-reviewed
    cite: "Voysey M, Clemens SAC, Madhi SA, et al. Safety and efficacy of the ChAdOx1 nCoV-19 vaccine (AZD1222) against SARS-CoV-2: an interim analysis of four randomised controlled trials in Brazil, South Africa, and the UK. Lancet. 2021;397(10269):99-111."
    doi: "10.1016/S0140-6736(20)32661-1"
    pmid: "33306989"
    url: "https://doi.org/10.1016/S0140-6736(20)32661-1"
  - id: greinacher-2021-vitt
    type: peer-reviewed
    cite: "Greinacher A, Thiele T, Warkentin TE, et al. Thrombotic Thrombocytopenia after ChAdOx1 nCov-19 Vaccination. N Engl J Med. 2021;384(22):2092-2101."
    doi: "10.1056/NEJMoa2104840"
    pmid: "33835769"
    url: "https://doi.org/10.1056/NEJMoa2104840"
  - id: sadoff-2021-azd1222-review
    type: peer-reviewed
    cite: "Knoll MD, Wonodi C. Oxford-AstraZeneca COVID-19 vaccine efficacy. Lancet. 2021;397(10269):72-74."
    doi: "10.1016/S0140-6736(20)32623-4"
    pmid: "33306990"
    url: "https://doi.org/10.1016/S0140-6736(20)32623-4"
  - id: shah-2021-effectiveness
    type: peer-reviewed
    cite: "Sheikh A, McMenamin J, Taylor B, Robertson C; Public Health Scotland and the EAVE II Collaborators. SARS-CoV-2 Delta VOC in Scotland: demographics, risk of hospital admission, and vaccine effectiveness. Lancet. 2021;397(10293):2461-2462."
    doi: "10.1016/S0140-6736(21)01358-1"
    pmid: "34139198"
    url: "https://doi.org/10.1016/S0140-6736(21)01358-1"
cross_links:
  - target: 02-pathogen/01-viruses/sars-cov-2
    relation: immunizes-against
    note: "AZD1222 induces anti-spike IgG and spike-specific CD4⁺/CD8⁺ T-cell responses that protect against symptomatic and severe COVID-19; efficacy ~67% in original pooled analysis, with ~62–90% depending on dose interval."
  - target: 01-human/07-system/immune-system
    relation: elicits
    note: "ChAdOx1 vector induces strong innate (TLR2/4/9-mediated) activation at injection site; vector-mediated antigen expression drives B-cell and T-cell immunity; spike-specific IgG and memory B cells are the primary correlates of protection."
  - target: 01-human/04-cellular/dendritic-cell
    relation: elicits
    note: "Adenovirus vector infects antigen-presenting cells at the injection site; dendritic cells process and present spike peptides to CD4⁺ and CD8⁺ T cells, initiating adaptive immunity."
  - target: 01-human/04-cellular/b-cell
    relation: elicits
    note: "Anti-spike IgG titers peak ~28 days after dose 2; 8–12 week interval between doses allows more robust germinal center maturation and higher antibody titers than 4-week interval."
  - target: 01-human/04-cellular/t-helper-cell
    relation: elicits
    note: "Strong spike-specific Th1-biased CD4⁺ T-cell responses demonstrated in Phase 1; 8–12 week interval associated with significantly higher spike-specific T-cell responses."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: elicits
    note: "Neutralizing IgG targeting the spike receptor-binding domain is the primary correlate of protection; post-dose-2 IgG titers at 8-week interval significantly exceed 4-week schedule titers."
  - target: 01-mrna/mrna-1273
    relation: same-platform-as
    note: "Both target SARS-CoV-2 spike antigen as primary immunogen; diverge in delivery platform (viral vector vs LNP-mRNA), cold-chain requirements, and T-cell response profiles."
---

# AZD1222 (Vaxzevria, ChAdOx1-S)

## Overview

AZD1222 — marketed as **Vaxzevria** (Europe) and **Covishield** (India) — is a non-replicating viral-vector COVID-19 vaccine developed by the University of Oxford and AstraZeneca. It uses a **chimpanzee adenovirus (ChAdOx1)** as a delivery vehicle: the adenovirus has been engineered to be replication-deficient (E1/E3 genes deleted) and carries a gene encoding the **full-length SARS-CoV-2 spike protein**. When injected, the vector infects cells at the injection site and regional lymph nodes, which then express the spike protein and trigger an immune response [^folegatti-2020-phase1].

AZD1222 was one of the first COVID-19 vaccines to demonstrate clinical efficacy and received its first Emergency Use Listing from the WHO in February 2021. Its **refrigerator-stable formulation (2–8°C)** made it a cornerstone of global vaccine rollout through COVAX, particularly in low- and middle-income countries (LMICs) where ultra-cold chain infrastructure is unavailable. Covishield, produced by the Serum Institute of India, became the **most widely administered COVID-19 vaccine globally** by number of doses during 2021.

A critical safety signal emerged in early 2021: a rare syndrome — **vaccine-induced immune thrombocytopenia and thrombosis (VITT)** — occurring at ~1 in 100,000 doses primarily in younger adults. This led several countries to restrict or discontinue its use in younger age groups while maintaining use in older adults [^greinacher-2021-vitt].

## Platform Technology

### ChAdOx1 Viral Vector

**ChAdOx1** (chimpanzee adenovirus Oxford 1) is derived from the Y25 chimpanzee adenovirus. It was selected over human adenovirus serotypes (Ad5, Ad26) specifically because **pre-existing immunity to ChAdOx1 is rare in the human population** — unlike Ad5, for which seroprevalence exceeds 50% in many countries, which would blunt vaccine immunogenicity.

Key modifications:
- **E1 deletion:** Prevents viral replication in human cells (the cell cannot produce new virions)
- **E3 deletion:** Removes immune evasion genes; makes room for the transgene insert
- **Transgene:** Full-length SARS-CoV-2 spike gene under a cytomegalovirus (CMV) promoter with a tissue plasminogen activator (tPA) leader sequence for efficient secretion

Unlike the mRNA vaccines, which use prefusion-stabilized spike (2P substitutions), the original AZD1222 construct expresses **full-length unmodified spike** including the furin cleavage site. This remains immunogenic but may allow some post-fusion conformation expression.

### Mechanism of Antigen Delivery

```
Injection → ChAdOx1 vector infects muscle/APC cells
→ Spike gene transcribed → spike mRNA → spike protein expressed on cell surface
→ CD4⁺ T cells recognize spike peptides on MHC II → help B cells and CD8⁺ T cells
→ CD8⁺ T cells recognize spike on MHC I → cytotoxic T lymphocyte response
→ B cells differentiate → germinal center reaction → somatic hypermutation → affinity maturation
→ Anti-spike IgG antibodies + memory B cells + memory T cells
```

The adenovirus vector also acts as an **intrinsic adjuvant** — pattern recognition receptors (TLR2, TLR4, TLR9) recognize adenovirus components and activate innate immunity, amplifying the adaptive response.

## Immunogenicity

### Humoral Response

Phase 1/2 data showed **spike-specific IgG** peaking at ~28 days after dose 2 in all age groups. The dose interval critically affected antibody titers: an **8–12 week interval** between doses produced significantly higher neutralizing antibody titers compared to the 4-week interval used in early trials — because a longer interval allows full germinal center maturation and higher-affinity B-cell selection [^folegatti-2020-phase1].

Anti-spike IgG and pseudovirus neutralization titers were lower after AZD1222 than after mRNA-1273 or BNT162b2 in head-to-head comparisons; however, real-world effectiveness against severe disease and hospitalization was comparable or only modestly lower.

### T-Cell Response

AZD1222 induces notably strong **spike-specific CD4⁺ and CD8⁺ T-cell responses** — arguably superior to mRNA vaccines in the cellular compartment, particularly for CD8⁺ responses. This is consistent with adenoviral vector platforms' known CD8⁺ immunogenicity via cytoplasmic antigen presentation and MHC I loading. T-cell responses to spike peptides were detectable ≥1 year after vaccination and may contribute to durable protection against severe disease even as neutralizing titers wane.

## Efficacy

### Phase 3 Pooled Analysis

The primary efficacy analysis pooled four trials in UK, Brazil, and South Africa [^voysey-2021-phase3]:

| Regimen | Efficacy (symptomatic COVID-19) |
|:---|:---|
| 2 × standard dose (SD/SD), ≥6-week interval | **62.1%** |
| Low dose / standard dose (LD/SD) | **90.0%** |
| Pooled analysis | **70.4%** |
| Standard dose, 12-week interval (UK) | **~82.4%** |

The unexpectedly high efficacy of the LD/SD regimen (discovered due to a manufacturing error in one trial site) was never fully explained and could not be replicated in a dedicated phase 3 trial.

**Real-world effectiveness (against Delta, UK, 2021):** ~67% against symptomatic disease; ~92% against hospitalization after 2 doses [^shah-2021-effectiveness].

**Against Omicron:** Substantially reduced protection against symptomatic infection; protection against severe disease/hospitalization partially maintained but lower than for mRNA vaccines, particularly without heterologous mRNA booster.

### Heterologous Boosting

Countries widely adopted **heterologous (mix-and-match) boosting** — mRNA vaccine (BNT162b2 or mRNA-1273) after AZD1222 primary series — which produced substantially higher neutralizing titers than homologous AZD1222 boosting. The UK COMCOV trial and Com-COV2 study demonstrated this strategy's superior immunogenicity [NCT04649840].

## Safety

### Common Adverse Events

| Adverse event | Rate | Onset |
|:---|:---|:---|
| Injection site pain/tenderness | Very common (>80%) | Day 1–2 |
| Fatigue, headache, myalgia | Very common (>60%) | Day 1–2 |
| Low-grade fever (37.5–38.5°C) | Common (20–30%) | Day 1–2 |
| Severe systemic reactions | Uncommon (<1%) | Day 1–2 |

Reactogenicity is generally more pronounced after dose 1 than dose 2 — the reverse of mRNA vaccines. Prophylactic paracetamol (acetaminophen) reduced reactogenicity in trials.

### VITT — Vaccine-Induced Immune Thrombocytopenia and Thrombosis

A rare but serious adverse event identified in April 2021 [^greinacher-2021-vitt]:

- **Incidence:** ~1–3 per 100,000 doses (dose 1 > dose 2); higher in younger adults, possibly higher in women
- **Presentation:** Thrombosis at unusual sites (cerebral venous sinus thrombosis, portal vein thrombosis, splanchnic vein thrombosis) + thrombocytopenia, typically 4–28 days post-vaccination
- **Mechanism:** PF4-reactive IgG antibodies activate platelets via FcγRIIa — mechanistically similar to heparin-induced thrombocytopenia (HIT) but heparin-independent
- **Treatment:** IVIG + non-heparin anticoagulants (argatroban, danaparoid); avoid heparin, which can worsen platelet activation
- **Regulatory impact:** Several European countries and Canada restricted AZD1222 to older adults (≥40–60 years); the UK maintained use in all adults with individualized informed consent counseling

Mortality risk from VITT is ~20–25% of confirmed cases, but absolute risk is extremely low (~1 in 500,000 doses in confirmed cases). The benefit-risk calculation favored vaccination in older adults and in settings where COVID-19 mortality risk was high.

## Manufacturing and Supply

AZD1222 was produced at unprecedented scale under a non-profit access agreement during the pandemic:
- **Serum Institute of India:** Produced >1.5 billion doses as Covishield; primary source for COVAX distribution to LMICs
- **AstraZeneca (UK/EU):** Production disrupted by supply chain issues in 2021 — contributed to global vaccine access inequity discussions
- **Fiocruz (Brazil):** Technology transfer for South American supply
- **Cold chain:** 2–8°C, 6-month shelf life — fully compatible with existing routine vaccine infrastructure

## Connections

- `immunizes-against` → **[SARS-CoV-2](../../../../02-pathogen/01-viruses/sars-cov-2/README.md)** — elicits anti-spike IgG and T-cell responses protective against COVID-19
- `elicits` → **[Immune System](../../../../01-human/07-system/immune-system/README.md)** — initiates innate and adaptive immune cascades
- `elicits` → **[Dendritic Cell](../../../../01-human/04-cellular/dendritic-cell/README.md)** — adenoviral transduction of APCs triggers T-cell priming
- `elicits` → **[B Cell](../../../../01-human/04-cellular/b-cell/README.md)** — drives germinal center reaction and anti-spike IgG production
- `elicits` → **[T Helper Cell](../../../../01-human/04-cellular/t-helper-cell/README.md)** — strong Th1-biased CD4⁺ responses; CD8⁺ T cells via MHC I cross-presentation
- `elicits` → **[IgG](../../../../01-human/03-molecular/immunoglobulin-g/README.md)** — anti-spike neutralizing IgG is primary correlate of protection

[^folegatti-2020-phase1]: Folegatti PM, Ewer KJ, Aley PK, et al. Safety and immunogenicity of the ChAdOx1 nCoV-19 vaccine against SARS-CoV-2. *Lancet.* 2020;396(10249):467-478. [doi:10.1016/S0140-6736(20)31604-4](https://doi.org/10.1016/S0140-6736(20)31604-4) · [PubMed 32702298](https://pubmed.ncbi.nlm.nih.gov/32702298/)
[^voysey-2021-phase3]: Voysey M, Clemens SAC, Madhi SA, et al. Safety and efficacy of the ChAdOx1 nCoV-19 vaccine (AZD1222) against SARS-CoV-2. *Lancet.* 2021;397(10269):99-111. [doi:10.1016/S0140-6736(20)32661-1](https://doi.org/10.1016/S0140-6736(20)32661-1) · [PubMed 33306989](https://pubmed.ncbi.nlm.nih.gov/33306989/)
[^greinacher-2021-vitt]: Greinacher A, Thiele T, Warkentin TE, et al. Thrombotic Thrombocytopenia after ChAdOx1 nCov-19 Vaccination. *N Engl J Med.* 2021;384(22):2092-2101. [doi:10.1056/NEJMoa2104840](https://doi.org/10.1056/NEJMoa2104840) · [PubMed 33835769](https://pubmed.ncbi.nlm.nih.gov/33835769/)
[^shah-2021-effectiveness]: Sheikh A, McMenamin J, Taylor B, Robertson C. SARS-CoV-2 Delta VOC in Scotland: demographics, risk of hospital admission, and vaccine effectiveness. *Lancet.* 2021;397(10293):2461-2462. [doi:10.1016/S0140-6736(21)01358-1](https://doi.org/10.1016/S0140-6736(21)01358-1) · [PubMed 34139198](https://pubmed.ncbi.nlm.nih.gov/34139198/)
[^knoll-2021-review]: Knoll MD, Wonodi C. Oxford–AstraZeneca COVID-19 vaccine efficacy. *Lancet.* 2021;397(10269):72-74. [doi:10.1016/S0140-6736(20)32623-4](https://doi.org/10.1016/S0140-6736(20)32623-4) · [PubMed 33306990](https://pubmed.ncbi.nlm.nih.gov/33306990/)
