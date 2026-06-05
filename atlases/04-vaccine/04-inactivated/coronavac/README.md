---
schema: vaccine-entry/v1
id: coronavac
name: CoronaVac
atlas: 04-vaccine
platform: 04-inactivated
status: draft
last_reviewed: 2026-06-04
summary: "Whole inactivated SARS-CoV-2 vaccine (CZ02 strain, Vero-cell propagated, BPL-inactivated, alum-adjuvanted) by Sinovac Biotech. 2-dose IM schedule. WHO EUL June 2021. Pivotal role in COVAX and LMICs; 65.9% VE hospitalization, 86.3% VE death in Chile real-world (Jara 2021 NEJM)."
target_pathogens:
  - sars-cov-2
antigens:
  - "inactivated whole SARS-CoV-2 virion (CZ02 strain)"
delivery_system: "aluminum hydroxide adjuvanted inactivated virus"
adjuvants:
  - aluminum hydroxide
route_of_administration: intramuscular
dose_schedule: "2 doses, 0 and 14 days (or 0 and 28 days)"
manufacturer: "Sinovac Biotech (China)"
regulatory_status: "WHO EUL 2021-06-01; approved in 50+ countries"
cold_chain: "2–8°C (refrigerator stable)"
discontinued: false
status: active
tags:
  - coronavac
  - sinovac
  - inactivated
  - sars-cov-2
  - covid-19
  - alum
  - brazil
  - chile
  - china
sources:
  - id: zhang-2021-jama-phase-1-2
    type: peer-reviewed
    cite: "Zhang Y, Zeng G, Pan H, et al. Safety, tolerability, and immunogenicity of an inactivated SARS-CoV-2 vaccine in healthy adults aged 18–59 years: a randomised, double-blind, placebo-controlled, phase 1/2 clinical trial. JAMA. 2021;326(1):35-45."
    doi: "10.1001/jama.2020.22136"
    url: "https://doi.org/10.1001/jama.2020.22136"
  - id: tanriover-2021-lancet-turkey-phase-3
    type: peer-reviewed
    cite: "Tanriover MD, Doğanay HL, Akova M, et al. Efficacy and safety of an inactivated whole-virion SARS-CoV-2 vaccine (CoronaVac): interim results of a double-blind, randomised, placebo-controlled, phase 3 trial in Turkey. Lancet. 2021;398(10296):213-222."
    doi: "10.1016/S0140-6736(21)01429-X"
    url: "https://doi.org/10.1016/S0140-6736(21)01429-X"
  - id: jara-2021-nejm-chile-realworld
    type: peer-reviewed
    cite: "Jara A, Undurraga EA, González C, et al. Effectiveness of an Inactivated SARS-CoV-2 Vaccine in Chile. N Engl J Med. 2021;385(10):875-884."
    doi: "10.1056/NEJMoa2106715"
    url: "https://doi.org/10.1056/NEJMoa2106715"
cross_links:
  - target: 02-pathogen/01-viruses/sars-cov-2
    relation: immunizes-against
    evidence: jara-2021-nejm-chile-realworld
    note: "Chile real-world: 65.9% VE hospitalization, 87.5% VE ICU, 86.3% VE death (2-dose, mid-2021 population)."
  - target: 01-human/07-system/immune-system
    relation: elicits
    note: "Whole-virion inactivated antigen drives broad humoral and cellular immune response via Th2-skewed alum adjuvant environment."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: elicits
    evidence: zhang-2021-jama-phase-1-2
    note: "Seroconversion ~92–100% after 2-dose series; neutralizing IgG titers lower than mRNA platforms but protective against severe disease endpoints."
---

# CoronaVac

## Overview

**CoronaVac** is a whole-virion inactivated SARS-CoV-2 vaccine developed by **Sinovac Biotech** (Beijing, China). It belongs to the oldest and most globally deployed vaccine technology family — the same platform as the Salk inactivated poliovirus vaccine (1955), inactivated influenza vaccines, and hepatitis A vaccines. CoronaVac presented the SARS-CoV-2 immune system with an **entire inactivated virion** rather than a single protein, giving it the broadest antigen repertoire of any COVID-19 vaccine deployed at scale.

The vaccine was manufactured at massive scale from early in the pandemic. Sinovac produced **over 2.3 billion doses** — the single largest production run of any COVID-19 vaccine globally. It was central to Brazil's early 2021 rollout (the Butantan Institute study), Turkey's Phase 3 trial (83.5% VE vs. symptomatic COVID), and Chile's national immunization campaign — the subject of one of the most influential real-world effectiveness studies of the pandemic (Jara et al., *NEJM* 2021 [^jara-2021-nejm-chile-realworld]).

WHO Emergency Use Listing was granted on **June 1, 2021**, enabling CoronaVac to be procured and distributed through COVAX to low- and middle-income countries that lacked the ultra-cold chain infrastructure needed for mRNA vaccines.

## Antigen & Adjuvant

**Antigen — whole inactivated SARS-CoV-2 virion (CZ02 strain):**

CoronaVac is produced by propagating the **CZ02 strain** of SARS-CoV-2 (a clinical isolate) in **Vero cells** (African green monkey kidney cells, the same substrate used for many classical inactivated viral vaccines). The virus is grown to high titer, then inactivated by **beta-propiolactone (BPL)**, a small alkylating agent that modifies viral nucleic acids to abolish replication capacity while leaving surface proteins (spike, envelope, membrane) and internal proteins (nucleocapsid) largely intact.

This whole-virion approach means the immune system encounters:
- **Spike (S) glycoprotein** — the primary neutralizing-antibody target; full-length, conformationally authentic (not recombinant or modified), in both prefusion and other conformational states present on the native virion surface
- **Nucleocapsid (N) protein** — highly conserved across SARS-CoV-2 variants; dominant T-cell antigen
- **Membrane (M) and Envelope (E) proteins** — additional B- and T-cell targets

The broader antigen repertoire is theoretically advantageous for cross-variant T-cell responses because N, M, and E are far more conserved than spike across Omicron lineages. In practice, variant escape was still observed for neutralizing antibody against Omicron.

**Adjuvant — aluminum hydroxide:**

Each 0.5 mL dose contains aluminum hydroxide (alum) adjuvant. Alum works by a **depot mechanism** at the injection site, slowing antigen release and recruiting innate immune cells. It activates the NLRP3 inflammasome and promotes uptake by antigen-presenting cells, skewing the response toward **Th2-mediated humoral immunity** (IgG1 and IgE isotypes in animal models; IgG1/3 predominant in humans). This Th2 skew is the primary reason alum-adjuvanted inactivated vaccines tend to produce strong antibody responses but comparatively weaker Th1/CD8+ T-cell cytotoxic responses than live-attenuated or mRNA vaccines.

**Cold chain:** 2–8°C — standard medical refrigerator, no ultra-cold infrastructure required. This was operationally decisive for deployment in Brazil, Indonesia, Turkey, Chile, and much of the developing world.

## Immunogenicity

**Seroconversion and neutralizing antibody:**

Zhang et al. (*JAMA* Phase 1/2, China) [^zhang-2021-jama-phase-1-2] showed seroconversion rates of **92–100%** (varying by schedule and age) after the 2-dose series, measured by microneutralisation assay. Peak neutralizing antibody titers were **lower than mRNA vaccines** — approximately 2–4× lower than post-dose-2 BNT162b2 or mRNA-1273 in head-to-head comparisons — but were achieved consistently across age groups including the elderly.

**T-cell response:**

Limited T-cell immunogenicity data compared to mRNA platforms. Antigen-specific CD4+ and CD8+ T cells are induced (whole-virion presents peptides via both MHC II and cross-presentation via MHC I), though magnitude is lower than replication-competent platforms. The nucleoprotein-specific T-cell response is a potential advantage for cross-variant protection.

**Waning and variants:**

Neutralizing antibody titers decline substantially by 6 months post-primary series, at rates comparable to or faster than mRNA vaccines. Against **Omicron BA.1**, neutralizing titers fell below detection thresholds in the majority of CoronaVac-vaccinated individuals who had not received a booster — the most pronounced drop of any platform. This drove aggressive heterologous booster campaigns.

**Heterologous boosting:**

Chile, Thailand, Hong Kong, and Brazil all deployed **mRNA boosters after CoronaVac primary series** starting late 2021. Heterologous mRNA boost (BNT162b2 or mRNA-1273 after 2× CoronaVac) produced substantially higher neutralizing titers than homologous CoronaVac booster, including improved Omicron cross-neutralization. This has been interpreted as immune response broadening driven by different antigen presentation modalities.

## Efficacy & Effectiveness

**Phase 3 — Turkey (Tanriover 2021, *Lancet*) [^tanriover-2021-lancet-turkey-phase-3]:**

- **~10,000 participants**, healthcare workers, 0-and-14 day schedule
- VE against symptomatic COVID-19: **83.5%** (95% CI 65.4–92.1) in the per-protocol primary analysis
- At the time of this readout, the dominant strain was the **ancestral / Alpha lineage**, before the global emergence of Delta or Omicron

**Phase 3 — Brazil / Butantan:**

- Conducted in healthcare workers across multiple sites; 0-and-28 day schedule; dominant strain during accrual shifted to include **Gamma (P.1)** variant
- VE against all symptomatic COVID-19 (any severity, including mild): **50.7%** — headline figure that caused significant media concern and is frequently misquoted
- VE against moderate/severe disease: ~78–83% in pre-specified subgroup
- Context: Gamma (P.1) was an early immune-escape variant, and the switch from 0-and-14 to 0-and-28 day schedule in the Brazilian study reduced peak titers. The 50.7% figure captures all-severity disease in a healthcare-worker cohort with high occupational exposure during a P.1 surge — the most demanding real-world test condition.

**Real-world — Chile (Jara 2021, *NEJM*) [^jara-2021-nejm-chile-realworld]:**

The most widely cited CoronaVac effectiveness study. Using Chile's national health records linkage across 10.2 million vaccinees:

| Endpoint | VE (fully vaccinated, ≥14 days post-dose 2) |
|:---|:---:|
| Symptomatic COVID-19 | 65.9% |
| Hospitalization | 87.5% |
| ICU admission | 90.3% |
| COVID-19 death | 86.3% |

The steep gradient from symptomatic disease VE (~66%) to death VE (~86%) mirrors the pattern seen with mRNA vaccines in similar real-world studies: vaccines that partially prevent symptomatic infection are highly effective at preventing the severe end of the clinical spectrum. During mid-2021 in Chile, the dominant circulating lineage included Gamma (P.1) and early Delta.

## Connections

CoronaVac's role in the four-atlas knowledge graph:

- **Immunizes against** → [`02-pathogen/01-viruses/sars-cov-2`](../../../../02-pathogen/01-viruses/sars-cov-2/README.md) — full virion presents spike, N, M, E to the immune system
- **Elicits response in** → [`01-human/immune-system`](../../../../01-human/immune-system/README.md) — Th2-skewed humoral response; alum NLRP3 pathway; germinal-center IgG maturation
- **Produces** → [`01-human/03-molecular/immunoglobulin-g`](../../../../01-human/03-molecular/immunoglobulin-g/README.md) — anti-spike and anti-nucleocapsid IgG; seroconversion 92–100%
- **Same-platform-as** → `04-vaccine/04-inactivated/sinopharm` (BBIBP-CorV), `04-vaccine/04-inactivated/covaxin` (BBV152)
- **Contrasts-with** → [`04-vaccine/01-mrna/mrna-1273`](../../01-mrna/mrna-1273/README.md) — 2–4× lower peak neutralizing titers; no mRNA-associated myocarditis signal; refrigerator-stable cold chain

## Safety

CoronaVac has the **safety profile expected of a traditional alum-adjuvanted inactivated viral vaccine** — favorable and well-established. It does not carry the risks associated with replication-competent vaccines (disseminated infection) or replication-incompetent viral vectors (VITT), and does not carry the mRNA-platform-associated myocarditis signal.

**Common reactogenicity** (within 1–3 days of injection):
- Local: injection-site pain (~30–40%, lower frequency than mRNA vaccines), erythema, induration
- Systemic: fatigue, headache, mild fever (~10–15%) — generally milder than mRNA vaccines; dose 2 reactogenicity similar to dose 1 (unlike mRNA vaccines where dose 2 is significantly more reactive)

**No established association** with:
- Thrombosis with thrombocytopenia syndrome (VITT) — no adenovirus vector component
- Myocarditis — no mRNA/LNP component; no signal observed in large post-authorization surveillance datasets from Chile, Brazil, or Turkey
- Vaccine-enhanced disease — no signal from Phase 3 or real-world data; pre-immunization SARS-CoV-1 animal model concerns for alum-adjuvanted inactivated coronavirus vaccines were not replicated in clinical data

**Post-authorization safety:**

Large pharmacovigilance datasets from Brazil (~100 million doses) and Chile (~20 million doses) show a safety profile consistent with background rates for standard vaccine adverse events. The WHO's Global Advisory Committee on Vaccine Safety reviewed CoronaVac in 2021–2022 and did not identify new safety signals beyond what would be expected for an inactivated alum-adjuvanted vaccine.

**Special populations:**

- **Immunocompromised:** may be given (no live pathogen), but immunogenicity is reduced; additional doses recommended
- **Pregnancy:** WHO and multiple national guidelines recommend CoronaVac as an acceptable option during pregnancy given favorable safety precedent for inactivated vaccines in pregnancy broadly
- **Elderly:** phase 3 data and real-world data support use in older adults; waning is faster, favoring early booster

---

**[← Platform 04 (Inactivated)](../README.md)** · **[← Vaccine Atlas](../../README.md)** · **[Schema](../../../../schemas/vaccine-entry.schema.md)**
