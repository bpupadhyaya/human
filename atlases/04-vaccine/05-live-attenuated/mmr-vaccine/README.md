---
schema: vaccine-entry/v1
id: mmr-vaccine
name: "MMR Vaccine (M-M-R II / Priorix)"
atlas: 04-vaccine
platform: 05-live-attenuated
status: active
last_reviewed: 2026-06-06
summary: "Combined live-attenuated vaccine containing three separately propagated viruses: Edmonston B measles virus (Merck M-M-R II) or Schwarz/Moraten (Priorix), Jeryl Lynn mumps virus, and RA 27/3 rubella virus. Two-dose schedule (12–15 months + 4–6 years) achieves >97% seroconversion for all three components; 95% population coverage required for measles herd immunity. Wakefield 1998 Lancet fraud (Retracted 2010) falsely linked MMR to autism, creating a lasting vaccine hesitancy movement — definitively refuted by >15 large cohort studies including the 2019 Danish cohort (n=650,000)."
target_pathogens:
  - measles-virus
  - mumps-virus
  - rubella-virus
antigens:
  - "live attenuated measles virus (Edmonston B strain, Merck M-M-R II; or Schwarz/Moraten, Priorix)"
  - "live attenuated mumps virus (Jeryl Lynn strain, B-level)"
  - "live attenuated rubella virus (RA 27/3 strain)"
delivery_system: "lyophilized live attenuated viruses"
adjuvants: []
route_of_administration: subcutaneous
dose_schedule: "Dose 1: 12–15 months; Dose 2: 4–6 years. Minimum interval: 4 weeks between doses."
manufacturer: "Merck (M-M-R II); GSK (Priorix); Serum Institute of India (Tresivac); sanofi (discontinued)"
regulatory_status: "FDA licensed 1971 (original MMR); M-M-R II licensed 1978; Priorix licensed EU 1997; WHO prequalified; ACIP recommended; included in all national immunisation programs globally"
cold_chain: "2–8°C (in dark); reconstituted vaccine must be used within 8 hours; discard unused reconstituted vaccine"
discontinued: false
tags:
  - measles
  - mumps
  - rubella
  - MMR
  - Edmonston
  - Jeryl-Lynn
  - RA27/3
  - live-attenuated
  - Wakefield
  - autism
  - herd-immunity
  - elimination
  - congenital-rubella
sources:
  - id: madsen-2002-NEJM-autism
    type: peer-reviewed
    cite: "Madsen KM, Hviid A, Vestergaard M, et al. A Population-Based Study of Measles, Mumps, and Rubella Vaccination and Autism. N Engl J Med. 2002;347(19):1477-1482."
    doi: "10.1056/NEJMoa021134"
    url: "https://doi.org/10.1056/NEJMoa021134"
    pmid: "12421889"
    note: "Danish cohort n=537,303; found no association between MMR vaccination and autism."
  - id: hviid-2019-annals-danish
    type: peer-reviewed
    cite: "Hviid A, Hansen JV, Frisch M, Melbye M. Measles, Mumps, Rubella Vaccination and Autism: A Nationwide Cohort Study. Ann Intern Med. 2019;170(8):513-520."
    doi: "10.7326/M18-2101"
    url: "https://doi.org/10.7326/M18-2101"
    pmid: "30831578"
    note: "Danish cohort n=650,172; definitive large-scale refutation of MMR-autism link; RR for autism among MMR-vaccinated vs unvaccinated 0.93 (95% CI 0.85–1.02)."
  - id: wakefield-1998-retracted
    type: retracted
    cite: "Wakefield AJ, et al. Ileal-lymphoid-nodular hyperplasia, non-specific colitis, and pervasive developmental disorder in children. Lancet. 1998;351(9103):637-641. RETRACTED February 2010."
    url: "https://doi.org/10.1016/S0140-6736(97)11096-0"
    note: "Original fraudulent Lancet paper (n=12) falsely claiming MMR caused autism and bowel disease. Retracted in full by The Lancet on 2 February 2010. Wakefield subsequently struck from UK medical register."
  - id: chen-2004-pediatrics-MMR-safety
    type: peer-reviewed
    cite: "Demicheli V, Rivetti A, Debalini MG, Di Pietrantonj C. Vaccines for measles, mumps and rubella in children. Cochrane Database Syst Rev. 2012;2:CD004407."
    doi: "10.1002/14651858.CD004407.pub3"
    url: "https://doi.org/10.1002/14651858.CD004407.pub3"
    pmid: "22336803"
    note: "Cochrane systematic review; 57 studies; confirms safety and efficacy of MMR; no credible link to autism, IBD, or other serious adverse events."
  - id: who-measles-elimination
    type: report
    cite: "World Health Organization. Global Measles and Rubella: Strategic Plan 2012–2020. Geneva: WHO; 2012."
    url: "https://apps.who.int/iris/handle/10665/44855"
    note: "WHO framework for measles and rubella elimination; 95% coverage threshold for herd immunity; regional elimination criteria."
cross_links:
  - target: 02-pathogen/01-virus/measles-virus
    relation: immunizes-against
    note: "Edmonston B or Schwarz/Moraten strain; 97%+ seroconversion after 2 doses; measles herd immunity threshold 95% coverage (R0=12–18)."
  - target: 02-pathogen/01-virus/varicella-zoster-virus
    relation: platform-peer
    note: "Both live-attenuated herpesvirus / paramyxovirus vaccines; both combined as MMRV (ProQuad / Priorix-Tetra) with VZV Oka strain; MMRV has slightly higher febrile seizure rate vs. MMR+V separately in first dose."
---

# MMR Vaccine (M-M-R II / Priorix)

## Overview

The **MMR vaccine** is a combined **live-attenuated vaccine** containing three independently developed, separately propagated attenuated viruses that are lyophilized together:

1. **Measles:** Edmonston B strain (Merck M-M-R II) or Schwarz/Moraten strain (Priorix, GSK)
2. **Mumps:** Jeryl Lynn B strain (Merck; named after Jeryl Lynn Hilleman, daughter of Maurice Hilleman, who developed it from her own tonsils in 1963)
3. **Rubella:** RA 27/3 strain (RA = Rubella Abortus; isolated by Stanley Plotkin from an aborted fetus in 1965 in Philadelphia)

The combined MMR formulation was first licensed in **1971**; the current M-M-R II formulation in **1978**. It is the standard vaccine against three of the most historically significant infectious diseases in pediatric medicine — measles (the leading cause of childhood blindness and encephalitis globally), mumps (parotitis, orchitis, deafness), and rubella (teratogen causing congenital rubella syndrome — CHD, cataracts, deafness, intellectual disability).

**Public health significance:**

MMR is one of the highest-impact vaccines in history:
- **Measles:** From ~530,000 US cases/year in 1960 to 37–1,000 cases/year post-vaccine; global measles mortality fell from ~2.6 million/year (pre-vaccine era) to ~128,000 (2021 WHO estimate) — though measles resurged in 2018–2019 due to declining vaccine coverage
- **Rubella/CRS:** Congenital rubella syndrome (CRS) — the leading preventable cause of childhood deafness and CHD in the pre-vaccine era — has been eliminated from all WHO regions that have achieved sustained high MMR coverage
- **Mumps:** Orchitis (leading to subfertility), viral meningitis, and sensorineural hearing loss substantially reduced in vaccinated populations

**The Wakefield fraud:**

In 1998, Andrew Wakefield published a paper in *The Lancet* (n=12 children) claiming MMR vaccination caused intestinal inflammation that led to autism. The paper was fraudulent — data were falsified, ethical approvals violated, and Wakefield was receiving undisclosed payments from plaintiff attorneys. The paper was **fully retracted by The Lancet in February 2010**; Wakefield was struck from the UK medical register. The scientific community's response has been unambiguous: more than 15 large epidemiological studies involving millions of children across multiple countries have found **no association between MMR and autism**. The 2019 Danish cohort (Hviid et al., *Annals of Internal Medicine*, n=650,172) — the largest and most rigorous — found an RR of 0.93 (95% CI 0.85–1.02) for autism among vaccinated vs. unvaccinated children. Despite this, Wakefield's paper seeded a durable vaccine hesitancy movement that continues to suppress MMR coverage in multiple countries and has caused measles outbreaks.

## Antigen Design

**Measles — Edmonston B and Schwarz/Moraten strains:**

Wild measles virus (*Measles morbillivirus*, Paramyxoviridae) was first isolated by John Enders and Thomas Peebles in 1954 from David Edmonston, a student at Fay School in Massachusetts. The **Edmonston strain** was serially passaged in human kidney cells, amnion cells, and chick embryo cells over years to attenuate it. The current Merck M-M-R II uses the **Edmonston B** strain (propagated in chick embryo fibroblast cells, WI-38 or MRC-5 human diploid cells). Priorix uses the **Schwarz** and **Moraten** strains, derived from further passage of Edmonston — with slightly different cell substrates and passage histories but comparable immunogenicity.

Key attenuation features:
- Loss of wild-type glycoprotein fusion efficiency (reduced ability to cause cell-to-cell spread in neural tissue)
- Reduced replication efficiency in lymphoid tissue (reduced viraemia)
- Preserved replication in respiratory epithelium and lymphoid tissue sufficient to generate protective immunity
- No reversion mechanism — attenuation is multi-factorial (not a single point mutation) and genetically stable

**Mumps — Jeryl Lynn B strain:**

Isolated by Maurice Hilleman from his daughter Jeryl Lynn Hilleman's throat swab in 1963 during her mumps illness. The strain was passaged in embryonated eggs and then chick embryo fibroblast cells to attenuate it. The **Jeryl Lynn vaccine** actually contains two genetic subpopulations — JL1 and JL2 — present at an approximately 80:20 ratio. Both contribute to immunogenicity. The Jeryl Lynn strain is the only mumps strain used in M-M-R II and is the most widely used globally; it has the strongest safety and efficacy record among all mumps vaccine strains.

Mumps attenuating changes: reduced parotid tropism, reduced neurotropism; preserved immunogenicity via hemagglutinin-neuraminidase (HN) and fusion protein (F) surface antigens.

**Rubella — RA 27/3 strain:**

Developed by **Stanley Plotkin** at the Wistar Institute, Philadelphia, in 1965–1969. The strain was isolated from an aborted fetus (RA = Rubella Abortus; "27/3" = 27th specimen, 3rd explant passage) during the 1964–65 rubella pandemic — the same pandemic that caused >11,000 fetal deaths and 20,000 infants born with CRS in the US. The virus was passaged in WI-38 human diploid cells, preserving its ability to grow in human tissue while losing pathogenicity. RA 27/3 has supplanted all earlier rubella strains globally because of its superior immunogenicity (induces high-titre IgG and mucosal IgA against the E1 glycoprotein) and its long safety record.

## Immunological Mechanism

**Mechanism of attenuation and immune induction:**

Each component of MMR undergoes limited replication after subcutaneous injection — in local lymphoid tissue, draining lymph nodes, and transiently in other lymphoid organs. This replication is sufficient to:
- Generate presentation of viral antigens via MHC class I (to CD8+ CTL) and MHC class II (to CD4+ T helper)
- Drive robust Th1-biased cellular immunity (critical for anti-viral defence, particularly against measles)
- Stimulate germinal center reactions with affinity maturation → high-titre, high-affinity IgG
- Establish long-lived memory B cells and plasma cells

Because these are live-attenuated viruses (not killed or subunit), they replicate and present antigens over days to weeks, providing prolonged antigen exposure without sustained viraemia or clinical disease in immunocompetent hosts. This "natural infection mimic" is why MMR generates more durable immunity than inactivated vaccines against the same pathogens.

**Correlates of protection:**

| Component | Correlate | Threshold |
|:---|:---|:---:|
| Measles | Serum neutralising Ab (PRNT) or measles IgG (ELISA) | ≥120 mIU/mL (ELISA); ≥1:8 (PRNT) |
| Mumps | Serum neutralising Ab or mumps IgG | ≥1:4 neutralising Ab titre (approximate; no WHO standard) |
| Rubella | Serum rubella IgG (HAI or ELISA) | ≥10 IU/mL (protective against CRS); ≥15 IU/mL (WHO) |

**Herd immunity and the 95% threshold:**

Measles is one of the most transmissible human pathogens, with a basic reproduction number (R0) of **12–18** (each case generates 12–18 secondary cases in a fully susceptible population). This extreme transmissibility means that **herd immunity requires ≥95% population immunity** — the threshold below which measles reintroduction into a susceptible cluster causes explosive outbreaks. Achieving and sustaining ≥95% coverage in all geographic pockets is the critical operational challenge of measles control programs. Even small geographic gaps (communities with 85–90% coverage) can sustain measles transmission.

Rubella herd immunity threshold: ~83–85% (R0=5–7), lower than measles but still requiring sustained high coverage.

## Efficacy

**Two-dose MMR efficacy:**

| Component | Dose 1 Seroconversion | Dose 2 Seroconversion |
|:---|:---:|:---:|
| Measles | 90–95% | >97% |
| Mumps | 85–95% | >90% (per Jeryl Lynn strain studies) |
| Rubella | 95–99% | ~99% |

**Against measles elimination — US data:**

- 1963 (pre-vaccine): ~500,000 reported measles cases/year; estimated 3–4 million actual cases
- 2000: Measles declared **eliminated in the US** (no sustained domestic transmission for >12 months)
- 2019: Largest US measles outbreak since 1992 (1,282 cases) — concentrated in communities with low MMR coverage, driven by imported cases from Israel and Ukraine; containment required emergency vaccination campaigns

**Against CRS (Congenital Rubella Syndrome):**

- 1964–65 US rubella pandemic: >11,000 spontaneous abortions, ~20,000 infants with CRS (deaf, blind, CHD)
- Post-MMR US: CRS eliminated — 0–9 cases/year since 2001 in the US (all imported or in unvaccinated individuals)
- **WHO Regional Elimination:** Americas — rubella eliminated since 2015; European Region — rubella certified eliminated in 35/53 member states as of 2021

**Mumps efficacy:**

- Two doses: ~85–92% effective against clinical mumps
- Mumps is the component with the most modest VE — Jeryl Lynn strain provides somewhat lower protection than measles or rubella components
- Mumps outbreaks have occurred in highly vaccinated college populations (2006, 2016–2017 US outbreaks) due to waning immunity — a third MMR dose is now recommended in outbreak settings

**MMR vs. autism — definitive studies:**

| Study | Design | n | Finding |
|:---|:---|:---:|:---:|
| Madsen 2002, Denmark | Prospective cohort | 537,303 | No association (RR ~1.0) |
| Hviid 2019, Denmark | Nationwide cohort | 650,172 | RR 0.93 (95% CI 0.85–1.02) — **no association** |
| Cochrane Review 2012 | Systematic review, 57 studies | Millions | No credible link to autism, IBD, Crohn's disease, asthma, or other serious AEs |
| IOM 2011 | Systematic review of causality | All evidence | Found no causal relation between MMR and autism |

## Safety

**Common adverse events (mild, self-limiting):**

| Adverse Event | Frequency | Timing | Notes |
|:---|:---:|:---:|:---|
| Injection-site pain, redness | 20–25% | Immediate | Subcutaneous; no alum adjuvant; milder than IM vaccines with alum |
| Low-grade fever | 5–15% | Days 5–12 post-dose | Related to attenuated measles replication; earlier than injection-site reactions |
| Measles-like rash | 5% | Days 7–14 | Transient, mild maculopapular rash; not contagious; no infectious virus in rash |
| Transient thrombocytopenia (ITP) | ~1:30,000–40,000 doses | Days 15–35 | Self-limiting; platelet count usually >50,000; treatment rarely required |
| Febrile seizure | ~1:3,000 doses (dose 1) | Days 5–12 | Associated with fever from measles component; no long-term sequelae |
| Parotitis / mild mumps-like symptoms | ~1% | Days 10–14 | Attenuated mumps replication; mild |
| Mild rubella arthralgia | 10–25% (adult women) | Days 10–21 | Joint pain/stiffness; more common in post-pubertal women; self-limiting <1 week |

**Serious but rare adverse events:**

| Adverse Event | Frequency | Notes |
|:---|:---:|:---|
| Anaphylaxis | ~1–2 per million doses | Gelatin or neomycin component; not egg allergy (current formulations safe in egg allergy) |
| Encephalitis (post-vaccine) | ~1 per 3 million doses (if causal) | Background rate of encephalitis in this age group makes causality difficult to establish; wild measles encephalitis: 1/1,000 cases — far higher |
| SSPE (Subacute Sclerosing Panencephalitis) | **None from vaccine** | SSPE is caused by wild-type measles virus persistent infection; MMR prevents SSPE by preventing wild measles infection |

**The MMR-autism evidence base:**

There is **no credible scientific evidence** that MMR causes autism spectrum disorder (ASD). The biologically plausible mechanisms proposed by Wakefield (gut-brain axis via inflammatory bowel disease) have not been reproducible. The scientific consensus — based on cohort studies involving >1.5 million vaccinated children — is that MMR does not increase the risk of autism.

The Wakefield paper was retracted following investigation by journalist Brian Deer (BMJ 2011) and the General Medical Council (UK), which found that:
- Patient data were manipulated and misrepresented
- Ethical approval was violated
- Wakefield held undisclosed financial conflicts of interest (paid by plaintiff attorneys)
- The 12 children's clinical findings did not match what was published

**Contraindications:**

- Severe immunodeficiency (SCID, hematologic malignancies with severe lymphopenia, high-dose immunosuppression) — the live viruses can cause severe or fatal disease in the immunocompromised
- Pregnancy — RA 27/3 rubella strain is theoretically teratogenic (though no cases of CRS from vaccine virus have been documented); women should avoid pregnancy for 4 weeks post-MMR
- Prior anaphylaxis to MMR components (neomycin, gelatin)
- Note: **Egg allergy is NOT a contraindication** — current MMR formulations are grown in chick embryo fibroblast cells, not egg white, and contain trace levels of egg proteins well below allergic thresholds

**MMRV (combination with varicella — Oka strain VZV):**

MMR is also available combined with live-attenuated varicella zoster virus (VZV Oka strain) as **MMRV (ProQuad, Merck; Priorix-Tetra, GSK)**. The MMRV combination has a slightly higher rate of febrile seizure (~1:1,250 doses) compared to separate MMR + varicella vaccines at the same visit (~1:2,500) — a difference attributable to the higher measles-virus content in the combination. ACIP recommends either option; if MMRV is used, providers should discuss the modestly elevated febrile seizure risk with parents.

## Cold Chain & Logistics

- **Storage:** Lyophilized (freeze-dried) powder at 2–8°C in darkness; protect from light (the live virus is degraded by UV)
- **Reconstitution:** Supplied diluent added immediately before use; reconstituted vaccine must be used within 8 hours and kept at 2–8°C in the dark
- **After reconstitution:** Discard any unused vaccine — multi-dose use is not recommended for reconstituted MMR
- **Freeze sensitivity:** The reconstituted vaccine is more heat-sensitive than the lyophilized powder; however the lyophilized powder is also sensitive to excessive heat — standard VVM monitoring should be applied
- **No VVM on MMR in most presentations** — cold chain management relies on temperature monitoring at storage facilities

## Connections

- **Immunizes against** → [`02-pathogen/01-virus/measles-virus`](../../../../02-pathogen/01-virus/measles-virus/README.md) — Edmonston B / Schwarz-Moraten; 97%+ seroconversion after 2 doses; measles herd immunity threshold 95% (R0 12–18)
- **MMRV platform** → [`02-pathogen/01-virus/varicella-zoster-virus`](../../../../02-pathogen/01-virus/varicella-zoster-virus/README.md) — Oka strain VZV is combined with MMR in ProQuad/Priorix-Tetra; modestly higher febrile seizure risk with MMRV vs. separate MMR+V
- **Platform peers** → [`04-vaccine/05-live-attenuated/bcg`](../bcg/README.md) and [`04-vaccine/05-live-attenuated/oral-polio-vaccine`](../oral-polio-vaccine/README.md) — all live-attenuated vaccines; BCG and OPV are single-pathogen; MMR is the most complex live-attenuated combination vaccine in widespread use
- **Historical context** → Wakefield 1998 Lancet (retracted 2010): foundational fraudulent paper claiming MMR-autism link; its legacy continues to suppress vaccine coverage globally; definitively refuted by Hviid 2019 (n=650,172, RR 0.93)
- **Congenital rubella** → Rubella component of MMR eliminates CRS — once a leading cause of congenital deafness and CHD globally; Americas region declared rubella-free 2015

---

**[← Platform 05 (Live-Attenuated)](../README.md)** · **[← Vaccine Atlas](../../README.md)** · **[Schema](../../../../schemas/vaccine-entry.schema.md)**
