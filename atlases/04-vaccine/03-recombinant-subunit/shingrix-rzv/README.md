---
schema: vaccine-entry/v1
id: shingrix-rzv
name: "Shingrix (RZV)"
atlas: 04-vaccine
platform: 03-recombinant-subunit
status: active
last_reviewed: 2026-06-06
summary: "Adjuvanted recombinant subunit zoster vaccine; VZV glycoprotein E antigen + AS01B adjuvant (MPL + QS-21 liposomes). Two IM doses 2–6 months apart. ZOE-50: 97% efficacy in adults ≥50; ZOE-70: 91% in ≥70. Preferred over live-attenuated Zostavax; approved for immunocompromised."
target_pathogens:
  - varicella-zoster-virus
antigens:
  - "Varicella-zoster virus glycoprotein E (gE) — 50 μg per dose, expressed in CHO cells"
delivery_system: "lyophilized antigen reconstituted with liquid AS01B adjuvant system (MPL + QS-21 in liposome formulation)"
adjuvants:
  - "AS01B (monophosphoryl lipid A [MPL] + QS-21 saponin in liposomes)"
route_of_administration: intramuscular
dose_schedule: "2-dose series: dose 1 at election, dose 2 two to six months later; no booster currently recommended"
manufacturer: "GlaxoSmithKline (GSK)"
regulatory_status: "FDA approved 2017 (adults ≥50); FDA expanded 2021 (adults ≥18 at increased risk); EMA approved 2018; WHO prequalified; ACIP preferred zoster vaccine over Zostavax"
cold_chain: "2–8°C; do not freeze; store in original packaging to protect from light; reconstituted vaccine must be used within 6 hours"
discontinued: false
tags:
  - herpes-zoster
  - shingles
  - varicella-zoster
  - VZV
  - recombinant-subunit
  - AS01B
  - adjuvanted
  - RZV
  - glycoprotein-E
  - immunocompromised
sources:
  - id: lal-2015-zoe50
    type: peer-reviewed
    cite: "Lal H, Cunningham AL, Godeaux O, et al. Efficacy of an adjuvanted herpes zoster subunit vaccine in older adults. N Engl J Med. 2015;372(22):2087-2096."
    doi: "10.1056/NEJMoa1501184"
    pmid: "25981865"
    url: "https://doi.org/10.1056/NEJMoa1501184"
  - id: cunningham-2016-zoe70
    type: peer-reviewed
    cite: "Cunningham AL, Lal H, Kovac M, et al. Efficacy of the herpes zoster subunit vaccine in adults 70 years of age or older. N Engl J Med. 2016;375(11):1019-1032."
    doi: "10.1056/NEJMoa1603800"
    pmid: "27626517"
    url: "https://doi.org/10.1056/NEJMoa1603800"
  - id: dagnew-2019-immunocompromised
    type: peer-reviewed
    cite: "Dagnew AF, Ilhan O, Lee WS, et al. Immunogenicity and safety of the adjuvanted recombinant zoster vaccine in adults with haematological malignancies: a phase 3, randomised, clinical trial and post-hoc efficacy analysis. Lancet Infect Dis. 2019;19(9):988-1000."
    doi: "10.1016/S1473-3099(19)30163-X"
    pmid: "31285139"
    url: "https://doi.org/10.1016/S1473-3099(19)30163-X"
cross_links:
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: immunizes-against
    evidence: lal-2015-zoe50
    note: "Shingrix prevents herpes zoster (shingles) — the reactivation disease of latent VZV from dorsal root ganglia. gE antigen is the dominant surface glycoprotein and primary target of VZV-neutralizing antibodies; 97% efficacy in ZOE-50 vs 51% for live-attenuated Zostavax."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "RZV AS01B adjuvant (MPL + QS-21) drives strong Th1-biased CD4+ polyfunctional T cells (IFN-γ + CD40L + IL-2 + TNF-α) and memory B-cell responses even in immunosenescent elderly; superior CD4+ response explains >97% VE (ZOE-50) vs 51% for Zostavax."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Shingrix generates anti-gE IgG geometric mean concentrations >10× baseline after 2 doses; high-titer anti-gE IgG plus polyfunctional CD4+ T cells are dual correlates of protection; seroprotection sustained ≥9 years in long-term follow-up of ZOE-50 cohort."
  - target: 01-human/04-cellular/t-helper-cell
    relation: elicits
    note: "AS01B (MPL+QS-21) drives potent Th1-biased polyfunctional CD4+ T cells (IFN-γ + CD40L + IL-2 + TNF-α simultaneously); CD4+ T cell magnitude explains 97% VE (ZOE-50) vs 51% Zostavax; response maintained in immunosenescent elderly (ZOE-70: 91.3% VE ≥70)."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: prevents-damage-to
    note: "VZV reactivates in dorsal root ganglia → travels along peripheral sensory nerves causing herpes zoster; gE mediates virion spread via nerve cell-to-cell transmission; Shingrix prevents peripheral nerve VZV invasion, acute neuritis, and postherpetic neuralgia lasting months."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: activates
    note: "AS01B QS-21 activates NLRP3 inflammasome → IL-1β/IL-18; MPL activates TLR4 → NF-κB innate cytokines; dual NLRP3+TLR4 activation drives DC maturation and robust adaptive immunity; AS01B dual innate pathway activation explains RZV superiority over alum-only adjuvanted vaccines."
---

# Shingrix (RZV)

## Overview

**Shingrix** (recombinant zoster vaccine, RZV) is a **non-live adjuvanted subunit vaccine** developed by GlaxoSmithKline for prevention of **herpes zoster (shingles)** — the reactivation disease of latent varicella-zoster virus (VZV) in dorsal root ganglia. It was FDA-approved in 2017 for adults ≥50 years and has rapidly become the preferred zoster vaccine, superseding the older live-attenuated Zostavax (ZVL, ~51% efficacy) due to its substantially higher and more durable protection.

Shingrix comprises a single antigen — **varicella-zoster virus glycoprotein E (gE)** — adjuvanted with the **AS01B adjuvant system**, a proprietary GSK combination of monophosphoryl lipid A (MPL, a TLR4 agonist) and QS-21 (saponin extract of *Quillaja saponaria*) in liposomes. AS01B is the same adjuvant platform used in the RTS,S/AS01B malaria vaccine. It activates both innate (via TLR4/MPL and NLRP3/QS-21 pathways) and adaptive immunity, driving robust CD4⁺ T-cell and antibody responses even in older adults with immunosenescence.

A landmark clinical development was FDA approval in 2021 for adults ≥18 years who are immunocompromised or at increased risk — making Shingrix one of the few vaccines safe and effective in severely immunocompromised patients (including those with hematological malignancies, solid organ transplant, HIV, and autologous stem cell transplant recipients).

## Immunogenicity

**Antigen: Glycoprotein E (gE)**

gE (gene 68) is the **most abundant envelope glycoprotein** of VZV, expressed on both the virion surface and infected cell membranes. It plays roles in virus spread via cell-to-cell transmission and is the dominant target of VZV-specific memory CD4⁺ T cells and neutralizing antibodies. Using full-length recombinant gE as the sole antigen, combined with AS01B, produces:
- High-titer anti-gE IgG (geometric mean concentrations >10× baseline after 2 doses)
- Robust gE-specific CD4⁺ T-cell responses (IFN-γ + CD40L + IL-2 + TNF-α polyfunctional cells)
- Durable responses: seroprotection maintained for ≥9 years post-vaccination in follow-up studies

**ZOE-50 Trial** (n=15,411, ≥50 years) [^lal-2015-zoe50]:
- Vaccine efficacy (VE) against herpes zoster: **97.2%** (95% CI 93.7–99.0%)
- VE against postherpetic neuralgia (PHN): **91.2%**
- VE consistent across age groups (50–59: 96.6%; 60–69: 97.4%; ≥70: 97.9%)

**ZOE-70 Trial** (n=13,900, ≥70 years) [^cunningham-2016-zoe70]:
- VE in ≥70 years: **91.3%** (95% CI 86.8–94.5%)
- Pooled ZOE-50/ZOE-70 data for ≥70 years: 90.0% VE

**Comparison with Zostavax (ZVL):** Live-attenuated VZV (Oka/Merck strain) Zostavax achieved ~51% efficacy overall; drops to ~18% by age ≥80. Shingrix maintains >90% efficacy across all age groups and is durable over longer follow-up.

**Immunocompromised populations** [^dagnew-2019-immunocompromised]:
- Hematological malignancies: 87% VE in lymphoid cancers; immunogenicity inferior to immunocompetent but clinically meaningful
- ZOSTER-039 (HSCT recipients): 68% VE in autologous HSCT
- HIV (CD4 ≥200): 6-dose exploratory protocol shows robust immunogenicity

## Safety

**Reactogenicity (common, expected):**
- Injection site pain: 78% (vs 52% placebo)
- Injection site redness/swelling: ~48%
- Myalgia: 45%
- Fatigue: 45%
- Headache: 38%
- Shivering: 27%
- Fever: 21%
- Grade 3 injection site pain: ~5–9%
- Symptoms typically resolve within 1–3 days; result from AS01B-driven innate immune activation

**Serious adverse events:** Rates equivalent to placebo in ZOE-50/70 (<1% in each group). No increased risk of autoimmune conditions in post-licensure surveillance.

**Contraindications:**
- Hypersensitivity to any vaccine component (including gelatin is NOT a concern since Shingrix is non-live)
- Active primary varicella infection (theoretical; defer)
- Note: Shingrix CAN be given to immunocompromised patients (unlike Zostavax); no restriction for HIV, chemotherapy, biologic therapy, or immunosuppressants

**Interaction with other vaccines:** Can be co-administered with seasonal influenza vaccine; 4-week minimum interval not required.

## Connections

- `immunizes-against` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — Shingrix prevents herpes zoster (shingles), the reactivation disease of latent VZV; gE antigen is the dominant target of VZV-neutralizing antibodies and memory T cells.
- `connects-to` → **[Immune System](../../../../01-human/07-system/immune-system/README.md)** — RZV AS01B adjuvant (MPL + QS-21) drives strong Th1-biased CD4⁺ polyfunctional T cells (IFN-γ + CD40L + IL-2 + TNF-α) and memory B-cell responses even in immunosenescent elderly; superior CD4⁺ response explains >97% VE (ZOE-50) vs 51% for Zostavax.
- `connects-to` → **[Immunoglobulin G](../../../../01-human/03-molecular/immunoglobulin-g/README.md)** — Shingrix generates anti-gE IgG geometric mean concentrations >10× baseline after 2 doses; high-titer anti-gE IgG plus polyfunctional CD4⁺ T cells are dual correlates of protection; seroprotection sustained ≥9 years in long-term follow-up of ZOE-50 cohort.
- `elicits` → **[T-Helper Cell](../../../../01-human/04-cellular/t-helper-cell/README.md)** — AS01B (MPL+QS-21) drives potent Th1-biased polyfunctional CD4+ T cells (IFN-γ + CD40L + IL-2 + TNF-α simultaneously); CD4+ T cell magnitude explains 97% VE (ZOE-50) vs 51% Zostavax; response maintained in immunosenescent elderly (ZOE-70: 91.3% VE ≥70).
- `prevents-damage-to` → **[Peripheral Nerve](../../../../01-human/05-tissue/peripheral-nerve/README.md)** — VZV reactivates in dorsal root ganglia → travels along peripheral sensory nerves causing herpes zoster; gE mediates virion spread via nerve cell-to-cell transmission; Shingrix prevents peripheral nerve VZV invasion, acute neuritis, and postherpetic neuralgia lasting months.
- `activates` → **[NLRP3 Inflammasome](../../../../01-human/03-molecular/nlrp3-inflammasome/README.md)** — AS01B QS-21 activates NLRP3 inflammasome → IL-1β/IL-18; MPL activates TLR4 → NF-κB innate cytokines; dual NLRP3+TLR4 activation drives DC maturation and robust adaptive immunity; AS01B dual innate pathway activation explains RZV superiority over alum-only adjuvanted vaccines.

[^lal-2015-zoe50]: Lal H, Cunningham AL, Godeaux O, et al. Efficacy of an adjuvanted herpes zoster subunit vaccine in older adults. *N Engl J Med.* 2015;372(22):2087-2096. [doi:10.1056/NEJMoa1501184](https://doi.org/10.1056/NEJMoa1501184) · [PubMed 25981865](https://pubmed.ncbi.nlm.nih.gov/25981865/)
[^cunningham-2016-zoe70]: Cunningham AL, Lal H, Kovac M, et al. Efficacy of the herpes zoster subunit vaccine in adults 70 years of age or older. *N Engl J Med.* 2016;375(11):1019-1032. [doi:10.1056/NEJMoa1603800](https://doi.org/10.1056/NEJMoa1603800) · [PubMed 27626517](https://pubmed.ncbi.nlm.nih.gov/27626517/)
[^dagnew-2019-immunocompromised]: Dagnew AF, Ilhan O, Lee WS, et al. Immunogenicity and safety of the adjuvanted recombinant zoster vaccine in adults with haematological malignancies. *Lancet Infect Dis.* 2019;19(9):988-1000. [doi:10.1016/S1473-3099(19)30163-X](https://doi.org/10.1016/S1473-3099(19)30163-X) · [PubMed 31285139](https://pubmed.ncbi.nlm.nih.gov/31285139/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
