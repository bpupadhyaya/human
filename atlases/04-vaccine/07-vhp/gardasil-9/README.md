---
schema: vaccine-entry/v1
id: gardasil-9
name: Gardasil 9 (HPV9)
atlas: 04-vaccine
platform: 07-vhp
status: draft
last_reviewed: 2026-06-04
summary: "Nonavalent HPV L1 VLP vaccine; types 6/11/16/18/31/33/45/52/58 from *S. cerevisiae*. Prevents ~90% of cervical cancers and most HPV anogenital/oropharyngeal cancers. 2-dose (ages ≤14) or 3-dose schedule. FDA 2014; Swedish registry: 88% reduction in invasive cervical cancer."
aliases: ["Gardasil-9", "HPV9", "9-valent HPV vaccine", "nonavalent HPV vaccine", "V503"]
target_pathogens:
  - target: 02-pathogen/01-viruses/human-papillomavirus
    antigen: L1-capsid-protein-vlp-9-types
    coverage: ["HPV6", "HPV11", "HPV16", "HPV18", "HPV31", "HPV33", "HPV45", "HPV52", "HPV58"]
antigens:
  - name: "HPV L1 VLPs — 9 types"
    source_pathogen: 02-pathogen/01-viruses/human-papillomavirus
    modification: "HPV L1 major capsid protein for each of 9 types expressed in *Saccharomyces cerevisiae*; self-assembles into 55 nm VLPs composed of 72 L1 pentamers (360 copies total); no nucleic acid; structurally identical to native HPV virion capsid surface"
    encoded_as: "recombinant protein (VLP)"
delivery_system: "Aluminum-containing adjuvant (AAHS — amorphous aluminum hydroxyphosphate sulfate, 500 µg per dose); intramuscular injection"
adjuvants: ["AAHS (amorphous aluminum hydroxyphosphate sulfate)"]
route_of_administration: "intramuscular"
dose_schedule:
  two_dose_young: "Ages 9–14: 2 doses, 6–12 months apart (non-inferior to 3-dose in 16–26 year olds)"
  three_dose_older: "Ages 15–26 (or immunocompromised): 3 doses at 0, 2, 6 months"
  catch_up_fda: "Ages 27–45: shared decision-making (FDA-approved 2018 extension; ACIP recommends selective use)"
manufacturer:
  developer: "Merck Sharp & Dohme (MSD)"
  partners: ["CSL Behring (manufacturing)"]
regulatory_status:
  - body: "FDA"
    status: "Licensed (BLA 125508)"
    date: "2014-12-10"
  - body: "EMA"
    status: "Marketing Authorization"
    date: "2015-06-10"
  - body: "WHO"
    status: "Prequalified"
    date: "2017-09-28"
  - body: "FDA"
    status: "BLA expanded — through age 45"
    date: "2018-10-05"
cold_chain: "2°C–8°C; do not freeze; 3-year shelf life"
discontinued: false
xrefs:
  rxnorm: "1861991"
  vo: "VO:0004931"
clinical_trials:
  - id: "NCT00543543"
    tag: "FUTURE I/II — Phase 3 (quadrivalent Gardasil predecessor); HPV 6/11/16/18 efficacy in women 16–26"
  - id: "NCT01651949"
    tag: "V503-002 — Phase 3 (Gardasil 9 pivotal); 14,215 women ages 16–26; non-inferiority vs. Gardasil 4 + superiority for types 31/33/45/52/58"
sources:
  - id: joura-2015-gardasil9-nejm
    type: peer-reviewed
    cite: "Joura EA, Giuliano AR, Iversen OE, et al. A 9-valent HPV vaccine against infection and intraepithelial neoplasia in women. N Engl J Med. 2015;372(8):711-23."
    doi: "10.1056/NEJMoa1405044"
    pmid: "25693011"
    url: "https://doi.org/10.1056/NEJMoa1405044"
  - id: who-2022-hpv-position
    type: clinical-guideline
    cite: "World Health Organization. Human papillomavirus vaccines: WHO position paper, December 2022. Wkly Epidemiol Rec. 2022;97(50):645-672."
    url: "https://www.who.int/publications/i/item/who-wer9750"
    accessed: "2026-06-04"
  - id: brawley-2018-hpv-cancers
    type: peer-reviewed
    cite: "Lei J, Ploner A, Elfström KM, et al. HPV Vaccination and the Risk of Invasive Cervical Cancer. N Engl J Med. 2020;383(14):1340-1348."
    doi: "10.1056/NEJMoa1917338"
    pmid: "33007079"
    url: "https://doi.org/10.1056/NEJMoa1917338"
cross_links:
  - target: 01-human/07-system/immune-system
    relation: elicits
    evidence: joura-2015-gardasil9-nejm
    note: "Gardasil 9 elicits type-specific neutralizing IgG against all 9 HPV L1 VLP types; geometric mean titers are 5–50-fold higher than those seen after natural HPV infection; AAHS adjuvant activates dendritic cells and drives robust Th2-biased responses with long-lived germinal center B-cell activation."
  - target: 01-human/04-cellular/b-cell
    relation: elicits
    evidence: joura-2015-gardasil9-nejm
    note: "Multivalent VLP display (72 L1 pentamers per VLP; 360 copies of L1) enables B-cell receptor cross-linking and strong T-independent plus T-dependent B-cell activation; germinal center reactions in draining lymph nodes produce high-affinity IgG1 and IgG4 with long-lived plasma cell differentiation."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: elicits
    evidence: who-2022-hpv-position
    note: "Type-specific anti-L1 IgG is the correlate of protection; neutralizing antibodies prevent HPV virion attachment to heparan sulfate proteoglycans and α6 integrin on cervical basal epithelial cells; WHO 2022 estimates that the 5 highest-risk types in Gardasil 9 (16/18/31/33/45/52/58) cause ~90% of cervical cancers."
  - target: 01-human/07-system/cervical-cancer
    relation: prevents
    note: "Gardasil 9 prevents HPV-16/18/31/33/45/52/58-driven cervical cancer; Swedish register: vaccination before age 17 reduces invasive cervical cancer by 88% (adj RR 0.12); HPV types 16+18 cause 70% of cervical cancers; WHO target: 90% girl vaccination by age 15 for elimination."
  - target: 02-pathogen/01-viruses/hpv-16
    relation: immunizes-against
    note: "HPV-16 is the most oncogenic type (causes ~50% of cervical cancers and most HPV-associated oropharyngeal cancers); Gardasil 9 L1 VLP from S. cerevisiae; anti-HPV-16 IgG 5-50× natural infection titers; 97.4% VE against HPV-16/18-related CIN2+ (FUTURE I/II)."
  - target: 01-human/04-cellular/dendritic-cell
    relation: elicits
    note: "AAHS adjuvant activates TLR4 and NLRP3 at injection site → DC maturation and migration to draining lymph nodes; 55 nm L1 VLPs phagocytosed by DCs → MHC-II presentation → CD4+ T helper priming → GC reactions → anti-L1 IgG with 5-50× natural infection titers."
---

# Gardasil 9 (HPV9)

## Overview

**Gardasil 9** is a **nonavalent virus-like particle (VLP) vaccine** that protects against nine human papillomavirus (HPV) types responsible for **~90% of cervical cancers** and the majority of other HPV-associated cancers (anal, oropharyngeal, vulvar, vaginal, penile) and genital warts. It represents the most cancer-preventive single vaccine in clinical use.

HPV is the most common sexually transmitted infection worldwide — virtually all sexually active people encounter HPV at some point. Of the 200+ HPV types, approximately 14 are classified as **high-risk oncogenic types** (causing ~570,000 new cervical cancer cases and ~311,000 deaths annually); low-risk types 6 and 11 cause ~90% of genital warts. Gardasil 9 covers the five most common high-risk types (16, 18, 31, 33, 45, 52, 58) plus two low-risk types (6, 11).

The vaccine was approved by the FDA in December 2014 based on pivotal Phase 3 data showing **97.4% efficacy** against cervical, vulvar, and vaginal disease caused by the five new high-risk types (31/33/45/52/58), and non-inferiority to the previous quadrivalent Gardasil for types 16 and 18 [^joura-2015-gardasil9-nejm].

Real-world impact: A landmark Swedish national register study (2020) found that vaccination before age 17 was associated with an **88% reduction in invasive cervical cancer incidence** (adjusted RR 0.12, 95% CI 0.00–0.34) compared to unvaccinated women [^brawley-2018-hpv-cancers]. In countries with high adolescent vaccination coverage, cervical cancer is on track for elimination within a generation.

## Immunogenicity

**VLP design:**
Each dose contains L1 VLPs for all 9 HPV types, produced by expressing recombinant HPV L1 capsid protein in *Saccharomyces cerevisiae*. Each VLP is ~55 nm in diameter, composed of 72 pentamers of L1 (360 copies total) — structurally identical to the native HPV virion surface. Key advantages of VLP display:
- **High density B-cell receptor cross-linking** (~360 antigen copies per particle) activates B cells more efficiently than monomeric antigen
- **No nucleic acid** — cannot replicate; no oncogenic risk
- **AAHS adjuvant** (amorphous aluminum hydroxyphosphate sulfate): activates innate sensing at injection site, promotes dendritic cell maturation and Th2 polarization, drives germinal center formation and affinity maturation

**Antibody response:**
- Geometric mean IgG titers after Gardasil 9: 5–50× higher than after natural HPV infection (which generates only low-level IgG in most people)
- Seroconversion rates: >99% for all 9 types in girls/women aged 9–26 after 3-dose series; >98% for 2-dose series in ages 9–14
- Antibody persistence: Detectable titers to all 9 types ≥12 years post-vaccination in cohorts followed to date; no vaccine failure reported in individuals with documented pre-vaccination seronegative status [^who-2022-hpv-position]

**Correlate of protection:**
Anti-L1 VLP IgG is the functional correlate; neutralizing antibodies prevent HPV entry into basal cervical keratinocytes via blockade of heparan sulfate proteoglycan + α6 integrin receptor binding. Exact minimum protective titer not established (no vaccinated breakthrough cases), but all seroconverted individuals appear protected.

## Safety

**Extensive safety record — >200 million doses administered:**

**Common (>10%):**
- Injection site: Pain (85%), swelling (25%), erythema (25%)
- Systemic: Headache (15%), fatigue (10%), dizziness (4%)

**Serious adverse events:**
- Syncope (vasovagal): Observe 15 minutes post-injection; occurs with Gardasil at same rate as other adolescent vaccines (~2/100,000 doses) — not a vaccine-specific reaction
- Anaphylaxis: ~1.7/1,000,000 doses (background rate similar to other vaccines)
- POTS (postural orthostatic tachycardia syndrome): Investigated extensively; large controlled studies (EMA 2015, FDA, ACOG 2019) found **no causal relationship** between HPV vaccination and POTS, CRPS, or fibromyalgia [^who-2022-hpv-position]

**Autoimmunity signals:**
VAERS reports examined for multiple autoimmune conditions; no consistent causal signal identified in controlled studies. WHO Global Advisory Committee on Vaccine Safety (GACVS): Gardasil has an acceptable safety profile; benefits far outweigh risks.

**Pregnancy:**
Not recommended during pregnancy (insufficient data). No adverse pregnancy outcomes documented in women inadvertently vaccinated while pregnant.

## Connections

- **Elicits** → [Immune System](../../../01-human/07-system/immune-system/README.md): AAHS-adjuvanted L1 VLPs activate innate sensing and drive robust type-specific IgG responses; the multivalent VLP display is a prototypical B-cell activating antigen architecture.
- **Elicits** → [B Cell](../../../01-human/04-cellular/b-cell/README.md): Dense multivalent L1 display cross-links B-cell receptors, driving strong germinal center reactions and long-lived plasma cell differentiation; the basis for antibody titers that exceed natural infection.
- **Elicits** → [Immunoglobulin G](../../../01-human/03-molecular/immunoglobulin-g/README.md): Type-specific anti-L1 IgG is the vaccine's correlate of protection — neutralizing antibodies prevent HPV virion binding to cervical basal epithelium before integration and oncogenic transformation can occur.
- **Prevents** → [Cervical Cancer](../../../01-human/07-system/cervical-cancer/README.md): Swedish national register (2020) found vaccination before age 17 associated with 88% reduction in invasive cervical cancer; WHO target: 90% coverage of girls by age 15 to eliminate cervical cancer as a public health problem.
- **Immunizes against** → [HPV-16](../../../02-pathogen/01-viruses/hpv-16/README.md): HPV-16 is the dominant oncogenic HPV type (~50% of cervical cancers, most oropharyngeal HPV cancers); Gardasil 9 L1 VLP for HPV-16 drives anti-HPV-16 IgG 5–50× higher than natural infection titers; 97.4% VE against CIN2+ in trials.
- **Elicits** → [Dendritic Cell](../../../01-human/04-cellular/dendritic-cell/README.md): AAHS activates innate sensing at injection site → DC maturation; 55 nm L1 VLPs are efficiently phagocytosed by DCs → MHC-II presentation of L1 peptides → CD4+ T helper cell priming → germinal center reactions for high-affinity, long-lived anti-L1 IgG.

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
