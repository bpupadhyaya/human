---
schema: vaccine-entry/v1
id: pcv13
name: "PCV13 (Prevnar 13)"
atlas: 04-vaccine
platform: 08-conjugate
status: active
last_reviewed: 2026-06-06
summary: "13-valent pneumococcal conjugate vaccine (Prevnar 13); CPS from 13 S. pneumoniae serotypes conjugated to CRM197 toxoid. Enables T-cell-dependent infant immunization with memory. Reduced invasive pneumococcal disease >80% in children <5."
target_pathogens:
  - streptococcus-pneumoniae
antigens:
  - "Pneumococcal capsular polysaccharide serotype 1 — CRM197 conjugate"
  - "Pneumococcal capsular polysaccharide serotype 3 — CRM197 conjugate"
  - "Pneumococcal capsular polysaccharide serotype 4 — CRM197 conjugate"
  - "Pneumococcal capsular polysaccharide serotype 5 — CRM197 conjugate"
  - "Pneumococcal capsular polysaccharide serotype 6A — CRM197 conjugate"
  - "Pneumococcal capsular polysaccharide serotype 6B — CRM197 conjugate"
  - "Pneumococcal capsular polysaccharide serotype 7F — CRM197 conjugate"
  - "Pneumococcal capsular polysaccharide serotype 9V — CRM197 conjugate"
  - "Pneumococcal capsular polysaccharide serotype 14 — CRM197 conjugate"
  - "Pneumococcal capsular polysaccharide serotype 18C — CRM197 conjugate"
  - "Pneumococcal capsular polysaccharide serotype 19A — CRM197 conjugate"
  - "Pneumococcal capsular polysaccharide serotype 19F — CRM197 conjugate"
  - "Pneumococcal capsular polysaccharide serotype 23F — CRM197 conjugate"
delivery_system: "protein-polysaccharide conjugate in aluminium phosphate adjuvant"
adjuvants:
  - aluminium phosphate
route_of_administration: intramuscular
dose_schedule: "3+1 schedule (doses at 2, 4, 6 months + booster at 12–15 months); 2+1 acceptable in some programs"
manufacturer: "Pfizer (formerly Wyeth)"
regulatory_status: "FDA approved 2010 (pediatric); 2011 (adults ≥50); EMA approved; WHO prequalified; ACIP recommended"
cold_chain: "2–8°C; do not freeze (freezing denatures protein-polysaccharide conjugate)"
discontinued: false
tags:
  - pneumococcal
  - streptococcus-pneumoniae
  - conjugate
  - PCV13
  - prevnar
  - CRM197
  - polysaccharide
  - T-cell-dependent
  - IPD
  - pneumonia
  - meningitis
  - otitis-media
sources:
  - id: mahon-2019-NEJM-CAPITA
    type: peer-reviewed
    cite: "Bonten MJM, Huijts SM, Bolkenbaas M, et al. Polysaccharide Conjugate Vaccine against Pneumococcal Pneumonia in Adults. N Engl J Med. 2015;372(12):1114-1125."
    doi: "10.1056/NEJMoa1408544"
    url: "https://doi.org/10.1056/NEJMoa1408544"
    pmid: "25785969"
    note: "CAPiTA trial — first RCT demonstrating PCV13 efficacy against community-acquired pneumonia in adults ≥65."
  - id: hicks-2007-pediatrics-IMPACT
    type: peer-reviewed
    cite: "Kellner JD, Vanderkooi OG, MacDonald J, Church DL, Tyrrell GJ, Scheifele DW. Changing epidemiology of invasive pneumococcal disease in Canada after the introduction of the 7-valent conjugate vaccine. CMAJ. 2009;180(2):E28-E37."
    doi: "10.1503/cmaj.081499"
    url: "https://doi.org/10.1503/cmaj.081499"
    pmid: "19153394"
    note: "Canadian IMPACT surveillance — documents impact of PCV7 and subsequent serotype replacement, informing PCV13 expansion."
  - id: pilishvili-2010-JID-pcv7-impact
    type: peer-reviewed
    cite: "Pilishvili T, Lexau C, Farley MM, et al. Sustained Reductions in Invasive Pneumococcal Disease in the Era of Conjugate Vaccine. J Infect Dis. 2010;201(1):32-41."
    doi: "10.1086/648593"
    url: "https://doi.org/10.1086/648593"
    pmid: "19947881"
    note: "Active Bacterial Core surveillance — documents >80% reduction in PCV7-serotype IPD in children <5 after universal PCV7 vaccination."
  - id: prevnar13-fda-label
    type: regulatory
    cite: "Pfizer. Prevnar 13 (pneumococcal 13-valent conjugate vaccine) package insert. Philadelphia, PA: Pfizer Inc; 2023."
    url: "https://www.fda.gov/vaccines-blood-biologics/vaccines/prevnar-13"
    note: "FDA-approved label; efficacy, safety, and immunogenicity data for pediatric and adult indications."
cross_links:
  - target: 02-pathogen/02-bacteria/streptococcus-pneumoniae
    relation: immunizes-against
    evidence: pilishvili-2010-JID-pcv7-impact
    note: ">80% reduction in vaccine-type invasive pneumococcal disease in children <5 after universal PCV introduction; herd protection extends to unvaccinated elderly."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "PCV13 generates T-cell-dependent anti-capsular polysaccharide IgG via CRM197 conjugation; opsonophagocytic IgG ≥0.35 μg/mL (ELISA) or OPKA ≥1:8 correlates with protection; second-dose boosting (vs. PPSV23 hyporesponsiveness) confirms TD mechanism."
  - target: 01-human/07-system/respiratory-system
    relation: prevents
    evidence: mahon-2019-NEJM-CAPITA
    note: "CAPiTA trial (N=84,496): PCV13 achieved 45.6% VE against vaccine-type community-acquired pneumonia in adults ≥65; 75% VE against vaccine-type invasive pneumococcal disease; first RCT demonstrating pneumococcal vaccine prevents pneumonia in elderly adults."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "CRM197 conjugation converts T-independent (TI-2) CPS antigen to T-dependent; triggers germinal center reaction, affinity maturation, class-switch to IgG2/IgG1; enables infant immunization from 6 weeks; herd protection via carriage reduction extends to unvaccinated elderly."
---

# PCV13 (Prevnar 13)

## Overview

**PCV13** (Prevnar 13, manufactured by Pfizer) is a **13-valent pneumococcal conjugate vaccine** that contains capsular polysaccharide (CPS) antigens from 13 serotypes of *Streptococcus pneumoniae*, each individually conjugated to the **CRM197** carrier protein — a non-toxic diphtheria toxin mutant (G52E point mutation abolishes ADP-ribosylating activity). It is the most clinically impactful pneumococcal vaccine ever produced, responsible for a greater-than-80% reduction in invasive pneumococcal disease (IPD) in vaccinated age groups.

*Streptococcus pneumoniae* is encapsulated with a thick polysaccharide capsule that determines serotype identity, enables immune evasion (resisting phagocytosis), and is the primary target of protective antibodies. There are >100 known pneumococcal serotypes. The **13 serotypes in PCV13** (1, 3, 4, 5, 6A, 6B, 7F, 9V, 14, 18C, 19A, 19F, 23F) were selected because they caused the majority of invasive pneumococcal disease (IPD — bacteraemia, meningitis, bacteraemic pneumonia) in children and adults in the pre-vaccine era.

**The conjugate vaccine evolution:**

| Vaccine | Serotypes | Year Licensed | Key Addition |
|:---|:---:|:---:|:---|
| PCV7 (Prevnar) | 4, 6B, 9V, 14, 18C, 19F, 23F | 2000 | First pneumococcal conjugate; proof of principle |
| PCV10 (Synflorix, GSK) | PCV7 + 1, 5, 7F | 2009 | Expanded coverage for LMIC-prevalent serotypes |
| **PCV13 (Prevnar 13)** | PCV10 + 3, 6A, 19A | **2010** | Added 19A (then dominant post-PCV7 replacement serotype) |
| PCV15 (Vaxneuvance, Merck) | PCV13 + 22F, 33F | 2021 | Two additional serotypes |
| PCV20 (Prevnar 20, Pfizer) | PCV13 + 8, 10A, 11A, 12F, 15B | 2021 | Broadest coverage; adult indication |

The addition of **serotype 19A** in PCV13 was particularly critical — serotype 19A had expanded dramatically in the post-PCV7 era due to **serotype replacement** (a phenomenon where vaccination pressure against PCV7 serotypes allowed non-vaccine serotypes to expand into the ecological niche vacated by eliminated strains).

## Platform & Antigen Design

**The Conjugation Problem — T-cell-independent to T-cell-dependent:**

Capsular polysaccharides (CPS) are T-cell-independent (TI-2) antigens. When CPS alone is administered (as in the older 23-valent PPSV23, Pneumovax), it:
- Directly cross-links B-cell receptors (BCRs) without T-cell help
- Generates rapid IgM → IgG2 class-switch with limited affinity maturation
- Does not induce germinal center reactions or long-lived memory B cells
- Fails to immunise infants under 2 years (B-cell TI-2 signalling is functionally immature before age ~2)
- Elicits **hyporesponsiveness** on repeat dosing (immune tolerance rather than booster response)

**Conjugation to CRM197 converts CPS to a T-cell-dependent (TD) antigen:**

```
Polysaccharide capsule (CPS, serotype-specific)
        │  Chemical conjugation (reductive amination, CDAP, or other)
        ▼
CRM197 carrier protein — non-toxic diphtheria toxin variant (G52E)
        │
        ▼
CPS-CRM197 conjugate
        │
        ▼
Antigen-presenting cell (dendritic cell / macrophage) takes up conjugate
        │
        ├─ Polysaccharide portion → B cell directly (antigen binding via BCR)
        │
        └─ CRM197 protein → MHC II presentation → CD4+ T-helper cell
                    │  (CRM197 is T-cell immunogenic; prior diphtheria
                    │   vaccination primes CRM197-specific T cells)
                    ▼
           T-cell help (CD40L/CD40 + cytokines: IL-4, IL-21)
                    │
                    ▼
           Germinal center reaction → affinity maturation → class switch
           → IgG1/IgG2 anti-polysaccharide antibodies
           → Long-lived memory B cells + plasma cells
```

This transformation — from TI-2 to TD antigen via conjugation — is the foundational innovation of modern conjugate vaccinology, pioneered for *Haemophilus influenzae* type b (Hib) by Robbins, Schneerson, and colleagues in the 1980s. PCV applies the same principle to pneumococcus.

**CRM197 advantages as carrier:**
- Genetically inactivated — cannot revert to active toxin (unlike formalin toxoid)
- Produced in *Corynebacterium diphtheriae* or *Pseudomonas fluorescens*
- Highly immunogenic T-cell antigen; prior diphtheria vaccination (universal) boosts CRM197-specific T-helper cells, priming the carrier-mediated T-cell help mechanism

**Aluminium phosphate adjuvant:** PCV13 uses aluminium phosphate (distinct from the aluminium hydroxide in DTP), which enhances antigen uptake at the injection site and activates NLRP3 inflammasome-mediated innate signalling, further enhancing the adaptive response.

## Immunogenicity

**Opsonophagocytic killing as the primary protective mechanism:**

Protection against pneumococcus is predominantly mediated by **opsonising IgG antibodies** against capsular polysaccharide. Anti-CPS IgG opsonises pneumococcal cells, enabling Fc-receptor-mediated phagocytosis by neutrophils and macrophages in blood and tissues. The **opsonophagocytic killing assay (OPKA)** is the established functional correlate of protection — generally, OPKA titres ≥1:8 (or anti-CPS IgG ≥0.35 µg/mL by ELISA) are considered seroprotective, though this threshold varies by serotype.

**Class-switch recombination and memory:**

Following the TD antigen pathway activated by conjugation:
- Germinal centers form in draining lymph nodes
- Affinity maturation selects high-affinity anti-CPS IgG clones
- Long-lived plasma cells home to bone marrow → sustained serum IgG levels
- Memory B cells circulate; rapid anamnestic (booster) response on re-exposure
- Unlike PPSV23, PCV13 shows **robust hysteresis** — re-vaccination boosts rather than suppresses the response

**Infant-specific efficacy:**

PCV13 is effective from 6 weeks of age. The T-cell dependent mechanism matures much earlier than B-cell TI-2 responsiveness, enabling effective immunisation of infants. This is the central public health advantage of conjugate over polysaccharide vaccines — the highest-risk period for IPD is the first 2 years of life.

**Herd protection:**

PCV13 prevents nasopharyngeal carriage of vaccine-type pneumococci, interrupting transmission. Vaccinating children creates herd protection that extends to unvaccinated elderly adults — a critical indirect effect documented by US Active Bacterial Core (ABC) surveillance showing IPD reduction in adults >65 even before adult PCV recommendations were implemented.

## Efficacy

**Pediatric — against invasive pneumococcal disease (IPD):**

| Study / Surveillance | Population | Design | Outcome |
|:---|:---|:---|:---:|
| IMPACT (Canada, PCV7 era; informs PCV13 extrapolation) | Children <16 y | Active bacterial core surveillance pre/post vaccine | **>80% ↓** in PCV7-type IPD within 3 years of universal recommendation |
| US ABCs Surveillance (PCV13 era, Pilishvili 2010 + follow-up) | All ages | Population surveillance | **88% ↓** vaccine-type IPD in children <5 by 2011 (2 years post-PCV13 introduction) |
| Herd protection (US elderly, passive) | Adults ≥65 | Unvaccinated cohort surveillance | **>70% ↓** PCV13-type IPD in unvaccinated elderly attributable to pediatric vaccination |

**Adult — CAPiTA trial (N Engl J Med, 2015):**

The **CAPiTA (Community-Acquired Pneumonia Immunization Trial in Adults)** was a randomised, double-blind, placebo-controlled trial in **84,496 Dutch adults ≥65 years** — the only large RCT of any pneumococcal vaccine in adults.

| Endpoint | PCV13 VE | 95% CI |
|:---|:---:|:---:|
| Vaccine-type community-acquired pneumonia (VT-CAP) | **45.6%** | 21.8–62.5% |
| Vaccine-type non-bacteraemic CAP | **45.0%** | 14.2–65.3% |
| Vaccine-type IPD | **75.0%** | 41.4–91.0% |

CAPiTA was the first RCT to demonstrate that a pneumococcal vaccine reduces pneumonia incidence in elderly adults — not only IPD. This evidence led the US FDA to approve PCV13 for adults ≥50 and led ACIP to recommend sequential PCV13→PPSV23 vaccination in older adults.

**Serotype 19A — the critical addition over PCV7:**

Serotype 19A became the dominant invasive serotype in the US and Europe after PCV7 introduction — a textbook case of serotype replacement. Its inclusion in PCV13 (but not PCV7 or PCV10) led to a measurable additional reduction in 19A IPD following the PCV7-to-PCV13 switch, validating the expansion strategy.

## Safety

**PCV13 has an excellent safety record** across >500 million doses administered globally. Common adverse events are injection-site reactions attributable to aluminium adjuvant.

| Adverse Event | Frequency | Notes |
|:---|:---:|:---|
| Injection site pain, redness, swelling | Very common (>60% of doses) | Alum depot; resolves 24–48 hours |
| Low-grade fever (<38.5°C) | ~25–40% (infants) | Within 24–48 hours; antipyretics as needed |
| Irritability, drowsiness (infants) | Common | Transient, 24–48 hours |
| Febrile seizure | Very rare (~1:3,000 if co-administered with some flu vaccines in certain age groups) | No increased risk with standard EPI co-administration |
| Anaphylaxis | Very rare (<1/million doses) | Contraindication to repeated dosing if severe prior reaction |

**No association** with:
- Asthma, atopy, autoimmune disease
- Autism spectrum disorder
- Sudden infant death syndrome (SIDS)

**Carrier suppression (theoretical concern):**
Repeated high doses of CRM197 across multiple conjugate vaccines (Hib, meningococcal, PCV) could theoretically reduce anti-CRM197 T-cell help through carrier-induced epitope suppression. In practice, immunogenicity data from combined vaccine schedules have not shown clinically meaningful reduction in anti-polysaccharide responses.

## Cold Chain & Logistics

- **Storage:** 2–8°C; do not freeze — freezing irreversibly denatures the protein-polysaccharide conjugate structure
- **Shelf life:** 36 months at 2–8°C
- **Vial:** Single-dose prefilled syringe (0.5 mL) or single-dose vial; reduces wastage vs. multi-dose vials for conjugate vaccines
- **Cold chain complexity:** Standard refrigerator cold chain; no ultra-cold requirement; feasible in LMIC settings with functioning EPI cold chain
- **Manufacturing complexity:** High — each of the 13 polysaccharide-protein conjugates must be manufactured, QC-tested, and blended separately; conjugation chemistry requires cGMP-level control for consistent hapten density

## Connections

- `immunizes-against` → **[Streptococcus pneumoniae](../../../../02-pathogen/02-bacteria/streptococcus-pneumoniae/README.md)** — 13 capsular serotypes; >80% reduction in vaccine-type IPD in children <5; herd protection extends to unvaccinated elderly.
- `connects-to` → **[Immunoglobulin G](../../../../01-human/03-molecular/immunoglobulin-g/README.md)** — PCV13 generates T-cell-dependent anti-capsular polysaccharide IgG via CRM197 conjugation; OPKA ≥1:8 or anti-CPS IgG ≥0.35 μg/mL is the seroprotection threshold; memory B cells and LLPCs sustain titers vs. PPSV23 hyporesponsiveness.
- `prevents` → **[Respiratory System](../../../../01-human/07-system/respiratory-system/README.md)** — CAPiTA trial (N=84,496 adults ≥65): PCV13 achieved 45.6% VE against vaccine-type community-acquired pneumonia and 75% VE against invasive pneumococcal disease; first RCT demonstrating pneumococcal vaccine prevents pneumonia in the elderly.
- `connects-to` → **[Immune System](../../../../01-human/07-system/immune-system/README.md)** — CRM197 conjugation converts T-independent (TI-2) CPS antigen to T-dependent; triggers germinal center reaction, affinity maturation, class-switch to IgG2/IgG1; enables infant immunization from 6 weeks; herd protection via carriage reduction extends to unvaccinated elderly.
- **Platform evolution** → PCV7 (Prevnar, 2000) → PCV13 (Prevnar 13, 2010) → PCV15/PCV20 (2021–2023); each expansion driven by serotype replacement epidemiology
- **Platform contrast** → PPSV23 (Pneumovax23) — 23-valent plain polysaccharide; TI-2 response; no infant efficacy; no memory; recommended in adults as complementary to PCV; herd protection not conferred
- **Conjugation platform comparison** → Hib conjugate (HbOC, PRP-T, PRP-OMP); meningococcal conjugate (MenACWY-CRM, MenB-FHbp) — all use CRM197 or other protein carriers; PCV13 is the most complex conjugate vaccine in terms of valency
- **Carrier protein** → CRM197 (non-toxic diphtheria toxin G52E mutant) — same carrier used in Hib-CRM197 (HibTITER), MenACWY-CRM (Menveo); diphtheria vaccination primes CRM197-specific T-helper cells, potentially enhancing conjugate vaccine responses

---

**[← Platform 08 (Conjugate)](../README.md)** · **[← Vaccine Atlas](../../README.md)** · **[Schema](../../../../schemas/vaccine-entry.schema.md)**

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
