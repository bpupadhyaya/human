---
schema: vaccine-entry/v1
id: bnt162b2
name: BNT162b2 (Comirnaty)
atlas: 04-vaccine
platform: 01-mrna
status: stub
last_reviewed: 2026-06-04
summary: "Modified-nucleoside mRNA vaccine encoding the SARS-CoV-2 prefusion-stabilized (2P) spike, delivered in a lipid nanoparticle. Co-developed by Pfizer and BioNTech; first authorized vaccine against COVID-19 (UK, Dec 2 2020; FDA EUA Dec 11 2020)."
aliases: ["Comirnaty", "Pfizer-BioNTech COVID-19 vaccine", "tozinameran"]
target_pathogens:
  - target: 02-pathogen/01-viruses/sars-cov-2
    antigen: spike-prefusion-2P
    coverage: ["wild-type (Wuhan-Hu-1)", "alpha", "beta", "delta", "omicron-BA.1", "omicron-BA.4/5", "XBB"]
antigens:
  - name: "SARS-CoV-2 spike (prefusion-stabilized, 2P)"
    source_pathogen: 02-pathogen/01-viruses/sars-cov-2
    modification: "K986P + V987P (2P stabilization, Graham/McLellan/Corbett)"
    encoded_as: "modified-nucleoside mRNA with N1-methylpseudouridine"
delivery_system: "lipid-nanoparticle (LNP); ALC-0315 ionizable lipid (Acuitas), ALC-0159 PEG-lipid, cholesterol, DSPC"
adjuvants: []
route_of_administration: "intramuscular"
dose_schedule:
  primary_series_adult: "2 doses, 21 days apart, 30 µg each (adults ≥12)"
  pediatric_10ug: "2 doses, 21 days apart, 10 µg (ages 5–11)"
  pediatric_3ug: "3 doses, 3 µg each (ages 6 months–4 years)"
  booster: "single 30 µg dose; updated bivalent / monovalent formulations followed"
manufacturer:
  developer: "BioNTech SE (Mainz, Germany) and Pfizer Inc. (New York)"
  partners: ["Acuitas Therapeutics (LNP IP)", "Polymun Scientific (early LNP manufacturing)"]
regulatory_status:
  - body: "MHRA"
    status: "Conditional authorization (first globally)"
    date: "2020-12-02"
  - body: "FDA"
    status: "EUA"
    date: "2020-12-11"
  - body: "EMA"
    status: "Conditional Marketing Authorization"
    date: "2020-12-21"
  - body: "WHO"
    status: "Emergency Use Listing"
    date: "2020-12-31"
  - body: "FDA"
    status: "BLA-approved (Comirnaty)"
    date: "2021-08-23"
cold_chain: "Originally −80°C ultra-cold (6 months); reformulated to −20°C (10 weeks) and 2–8°C (10 weeks)"
discontinued: false
xrefs:
  drugbank: "DB15696"
  rxnorm: "2468231"
  vo: "VO:0005176"
sources:
  - id: polack-2020-c4591001
    type: peer-reviewed
    cite: "Polack FP, Thomas SJ, Kitchin N, et al. Safety and Efficacy of the BNT162b2 mRNA Covid-19 Vaccine. NEJM. 2020;383(27):2603-2615."
    doi: "10.1056/NEJMoa2034577"
    pmid: "33301246"
  - id: walsh-2020-phase-1
    type: peer-reviewed
    cite: "Walsh EE, Frenck RW Jr, Falsey AR, et al. Safety and Immunogenicity of Two RNA-Based Covid-19 Vaccine Candidates. NEJM. 2020;383(25):2439-2450."
    doi: "10.1056/NEJMoa2027906"
    pmid: "33053279"
cross_links:
  - target: 02-pathogen/01-viruses/sars-cov-2
    relation: immunizes-against
    evidence: polack-2020-c4591001
    note: "Phase 3 C4591001: 95.0% efficacy (95% CI 90.3–97.6) against symptomatic COVID-19, ≥7 days after dose 2."
  - target: 02-pathogen/01-viruses/sars-cov-2
    relation: targets-antigen-of
    note: "Encodes SARS-CoV-2 spike (S) glycoprotein with 2P prefusion stabilization (K986P + V987P)."
  - target: 04-vaccine/01-mrna/mrna-1273
    relation: same-platform-as
    note: "Both modified-nucleoside mRNA-LNP encoding 2P-stabilized spike. Differ in lipid composition (ALC-0315 vs SM-102), dose (30 µg vs 100 µg), and dose interval (21 vs 28 days)."
---

# BNT162b2 (Comirnaty)

## Overview

**BNT162b2** is a modified-nucleoside mRNA vaccine encoding the SARS-CoV-2 prefusion-stabilized (2P) spike protein, delivered in a lipid nanoparticle (LNP). It was co-developed by **BioNTech SE** (founded by Uğur Şahin and Özlem Türeci, originally as a personalized mRNA cancer-vaccine platform company) and **Pfizer**, who joined as the manufacturing and global distribution partner in March 2020.

BNT162b2 was selected from four parallel candidates (BNT162-a1, -b1, -b2, -b3) tested in early-phase trials, differing in mRNA chemistry (modified-nucleoside vs unmodified) and antigen (full-length spike vs RBD-only) [^walsh-2020-phase-1]. The b2 candidate — modified-nucleoside, full-length 2P spike — won on the strength of its balanced immunogenicity and reactogenicity profile.

It was the **first vaccine globally authorized against COVID-19** (UK MHRA, December 2, 2020), and the first mRNA vaccine of any kind to receive full regulatory approval (FDA, August 23, 2021). Phase 3 efficacy was 95.0% [^polack-2020-c4591001].

This is a **stub entry** — to be expanded with full Platform / Antigen design / Mechanism of immunity / Manufacturing / Trials / Regulatory / Safety / Variation / Equity & access / Open questions sections, parallel to the [mRNA-1273 entry](../mrna-1273/README.md).

## Immunogenicity

*(Stub — to be expanded.)* Phase 1/2 data (Walsh 2020): robust spike-specific IgG and neutralizing antibody responses in all age groups after 2 doses (21-day interval). Th1-biased CD4⁺ T-cell responses. Anti-RBD IgG titer correlates with protection against symptomatic COVID-19 and severe disease. Immunogenicity wanes over 4–8 months; boosters restore peak titers.

## Safety

*(Stub — to be expanded.)* Phase 3 C4591001 (Polack 2020): well-tolerated; common adverse events local pain, fatigue, headache, chills, fever (mostly grade 1–2, resolving within 1–2 days). Post-marketing: rare myocarditis/pericarditis signal (mRNA-specific; younger males, dose 2 > dose 1; typically self-limited). No VITT. Cold chain originally −80°C; reformulated for −20°C and 2–8°C storage.

## Connections

- **Target pathogen**: [`02-pathogen/01-viruses/sars-cov-2`](../../../02-pathogen/01-viruses/sars-cov-2/README.md)
- **Sibling mRNA vaccine**: [`04-vaccine/01-mrna/mrna-1273`](../mrna-1273/README.md) (Moderna, SM-102 LNP, 100 µg)
- **Antigen**: Prefusion-stabilized (2P) spike protein; same design principle as mRNA-1273
- **Immune effectors**: Anti-spike neutralizing IgG (IgG1/IgG3), spike-specific CD4⁺ Th1, CD8⁺ T cells

## See also

- [`04-vaccine/01-mrna/mrna-1273`](../mrna-1273/README.md) — sibling mRNA-LNP vaccine (Moderna)
- [`02-pathogen/01-viruses/sars-cov-2`](../../../02-pathogen/01-viruses/sars-cov-2/README.md) — target pathogen
- [`04-vaccine/01-mrna/README.md`](../README.md) — platform overview
