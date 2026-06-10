---
schema: vaccine-entry/v1
id: varivax
name: Varivax
atlas: 04-vaccine
platform: 05-live-attenuated
status: active
last_reviewed: 2026-06-06
summary: "Live-attenuated VZV Oka strain varicella vaccine. Two-dose schedule (12-15 months + 4-6 years) achieves >95% seroconversion; 97-100% protection against severe varicella. Contraindicated in immunocompromised patients and pregnancy."
target_pathogens:
  - varicella-zoster-virus
antigens:
  - "Live attenuated varicella-zoster virus (Oka/Merck strain); minimum 1350 PFU per dose"
delivery_system: "lyophilized live attenuated virus; reconstituted with sterile water"
adjuvants: []
route_of_administration: subcutaneous
dose_schedule: "2-dose series: dose 1 at 12-15 months; dose 2 at 4-6 years (minimum interval 3 months). Previously 1-dose schedule 1995-2006."
manufacturer: "Merck Sharp & Dohme (Merck)"
regulatory_status: "FDA licensed 1995 (1-dose, ≥12 months); 2-dose ACIP recommendation 2007; WHO prequalified; included in national immunisation schedules of >100 countries"
cold_chain: "Frozen storage at -15°C or colder during shipping; 2–8°C for up to 72 hours post-thaw; use immediately once reconstituted; discard if not used within 30 minutes"
discontinued: false
tags:
  - varicella
  - chickenpox
  - VZV
  - Oka-strain
  - live-attenuated
  - MMRV
  - ProQuad
sources:
  - id: weibel-1984-varivax
    type: peer-reviewed
    cite: "Weibel RE, Neff BJ, Kuter BJ, et al. Live attenuated varicella virus vaccine: efficacy trial in healthy children. N Engl J Med. 1984;310(22):1409-1415."
    doi: "10.1056/NEJM198405313102201"
    pmid: "6325883"
    url: "https://doi.org/10.1056/NEJM198405313102201"
  - id: vazquez-1996-varivax-efficacy
    type: peer-reviewed
    cite: "Vazquez M, LaRussa PS, Gershon AA, Steinberg SP, Freudigman K, Shapiro ED. The effectiveness of the varicella vaccine in clinical practice. N Engl J Med. 2001;344(13):955-960."
    doi: "10.1056/NEJM200103293441302"
    pmid: "11274621"
    url: "https://doi.org/10.1056/NEJM200103293441302"
  - id: marin-2007-2dose-acip
    type: clinical-guideline
    cite: "Marin M, Güris D, Chaves SS, Schmid S, Seward JF. Prevention of varicella: recommendations of the Advisory Committee on Immunization Practices (ACIP). MMWR Recomm Rep. 2007;56(RR-4):1-40."
    pmid: "17585291"
    url: "https://www.cdc.gov/mmwr/preview/mmwrhtml/rr5604a1.htm"
cross_links:
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: immunizes-against
    evidence: weibel-1984-varivax
    note: "Varivax prevents primary varicella (chickenpox) — VZV infection in susceptible individuals; 2-dose series provides 98-100% protection against severe varicella and reduces breakthrough infections by 85-90%."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Varivax (Oka/Merck VZV) elicits CD4+ and CD8+ VZV-specific T cells and anti-gB/gE/gC IgG; 2-dose schedule achieves >99% seroconversion; VZV-specific T-cell immunity prevents shingles reactivation; subcutaneous injection drives limited viraemia and DC antigen presentation."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Anti-VZV IgG (FAMA titer ≥1:4) is the primary seroprotection correlate for Varivax; gB, gE, gC, and gH/gL are immunodominant targets; 2-dose schedule generates durable IgG titers detectable ≥20 years post-vaccination via bone marrow plasma cells."
---

# Varivax

## Overview

**Varivax** is a **live-attenuated varicella vaccine** containing the **Oka strain** of varicella-zoster virus (VZV), originally isolated in Japan by Michiaki Takahashi in 1972 from a healthy child named Oka, and subsequently serially passaged in human and guinea pig embryo fibroblast cells and WI-38 human diploid cells to reduce neurovirulence while preserving immunogenicity. The Merck formulation (Oka/Merck strain) was licensed in the United States in **1995** — making it the first varicella vaccine licensed in the US — and transformed varicella from a universal childhood disease into a vaccine-preventable infection.

Before the vaccine, ~4 million US cases of varicella occurred annually, causing ~10,000 hospitalizations and 100–150 deaths. Following universal vaccination recommendation in 1996 and two-dose schedule adoption in 2006, varicella incidence fell by >97% in the US by 2014.

The Oka strain is also used in:
- **ProQuad (MMRV):** Combined measles-mumps-rubella-varicella vaccine (Merck); 2-dose schedule at 12–15 months and 4–6 years; slightly higher febrile seizure risk (1 in ~2,300) vs. MMR + separate varicella in the first dose
- **Zostavax:** Higher-titer (14× more PFU) formulation for shingles prevention in adults ≥50; largely superseded by Shingrix (RZV) which has superior efficacy

## Immunogenicity

**Mechanism of attenuation:**
The Oka strain contains multiple attenuating mutations compared to wild-type VZV — primarily in ORF62 (IE62, the major transactivating protein) and ORF10 (tegument protein). These reduce replication efficiency in neurons (reducing potential neurovirulence) while preserving the ability to replicate in lymphocytes and skin fibroblasts.

**Immune response:**
- Subcutaneous injection → local replication in skin → virus reaches regional lymph nodes → limited viraemia → VZV antigen presentation by DCs
- **Anti-VZV antibody:** Glycoprotein B (gB), gC, gE, gH/gL are primary antibody targets; FAMA (fluorescent antibody to membrane antigen) titer ≥1:4 correlates with protection
- **T-cell responses:** CD4⁺ and CD8⁺ VZV-specific T cells generated; important for long-term protection and prevention of reactivation

**Efficacy [^weibel-1984-varivax] [^vazquez-1996-varivax-efficacy]:**
- **1-dose schedule (1995–2006):** ~85–90% protection against all varicella; ~97–100% protection against moderate-to-severe varicella
- **2-dose schedule (2007+):** ~98–99% protection against varicella; significantly reduces breakthrough disease and secondary household transmission
- Immunological persistence: antibody titers detectable for ≥20 years in vaccine recipients

## Safety

**Common reactions:**
- Injection site soreness/erythema: ~25%
- Fever (>102°F/39°C): 10–15%
- Mild varicella-like rash (vaccinee rash): 3–5% after dose 1, ~1% after dose 2
- The vaccinee rash indicates vaccine virus replication; recipients with rash may rarely transmit to susceptible close contacts (especially immunocompromised)

**Serious adverse events (rare):**
- Febrile seizures: reported but not higher than background rate with 2-dose schedule if Varivax and MMR given separately
- Vaccine-strain VZV pneumonitis, hepatitis: extremely rare (<1 per million doses), typically in immunocompromised recipients
- Secondary transmission: vaccine virus can transmit to susceptible contacts, but this has generally resulted only in mild illness (no reported severe disease in contacts)

**Contraindications:**
- **Immunosuppression:** Severely immunocompromised patients (blood dyscrasias, leukemia, lymphoma, cellular immune deficiency, high-dose corticosteroids ≥2 mg/kg/day prednisolone); exceptions: HIV with CD4 ≥15% may receive varivax on case-by-case basis
- **Pregnancy:** VZV can cause congenital varicella syndrome; avoid in pregnancy; advise 4-week contraception post-vaccination
- Gelatin/neomycin hypersensitivity (both present in Varivax)
- Febrile illness (defer until resolved)

**MMRV vs. MMR + V:**
ACIP 2008: For dose 1 at 12–15 months, prefer giving MMR and Varivax as separate injections (lower febrile seizure rate); MMRV acceptable for dose 2 at 4–6 years.

## Connections

- `immunizes-against` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — Varivax prevents primary varicella infection (chickenpox); 2-dose schedule provides ~98-99% protection against disease; also reduces zoster risk by maintaining VZV-specific T-cell immunity.
- `connects-to` → **[Immune System](../../../../01-human/07-system/immune-system/README.md)** — Varivax (Oka/Merck VZV) elicits CD4⁺ and CD8⁺ VZV-specific T cells and anti-gB/gE/gC IgG; 2-dose schedule achieves >99% seroconversion; VZV-specific T-cell immunity prevents shingles reactivation; subcutaneous injection drives limited viraemia and DC antigen presentation.
- `connects-to` → **[Immunoglobulin G](../../../../01-human/03-molecular/immunoglobulin-g/README.md)** — Anti-VZV IgG (FAMA titer ≥1:4) is the primary seroprotection correlate for Varivax; gB, gE, gC, and gH/gL are immunodominant targets; 2-dose schedule generates durable IgG titers detectable ≥20 years post-vaccination via bone marrow plasma cells.

[^weibel-1984-varivax]: Weibel RE, Neff BJ, Kuter BJ, et al. Live attenuated varicella virus vaccine: efficacy trial in healthy children. *N Engl J Med.* 1984;310(22):1409-1415. [doi:10.1056/NEJM198405313102201](https://doi.org/10.1056/NEJM198405313102201) · [PubMed 6325883](https://pubmed.ncbi.nlm.nih.gov/6325883/)
[^vazquez-1996-varivax-efficacy]: Vazquez M, LaRussa PS, Gershon AA, et al. The effectiveness of the varicella vaccine in clinical practice. *N Engl J Med.* 2001;344(13):955-960. [doi:10.1056/NEJM200103293441302](https://doi.org/10.1056/NEJM200103293441302) · [PubMed 11274621](https://pubmed.ncbi.nlm.nih.gov/11274621/)
[^marin-2007-2dose-acip]: Marin M, Güris D, Chaves SS, Schmid S, Seward JF. Prevention of varicella: recommendations of the ACIP. *MMWR Recomm Rep.* 2007;56(RR-4):1-40. [PubMed 17585291](https://pubmed.ncbi.nlm.nih.gov/17585291/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
