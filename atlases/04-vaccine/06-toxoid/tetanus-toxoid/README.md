---
schema: vaccine-entry/v1
id: tetanus-toxoid
name: Tetanus Toxoid (TT / Td / DTaP)
atlas: 04-vaccine
platform: 06-toxoid
status: draft
last_reviewed: 2026-06-04
summary: "Formaldehyde-inactivated tetanospasmin from *Clostridium tetani*; >95% seroconversion after 3-dose primary series. Protective IgG ≥0.1 IU/mL. Given as TT, Td, DTaP, or DTP. Core WHO EPI vaccine; eliminated neonatal tetanus in >90% of countries. Boosters every 10 years."
aliases: ["TT", "Td", "DTaP", "DTP", "tetanus toxoid", "tetanus vaccine", "diphtheria-tetanus-acellular pertussis"]
target_pathogens:
  - target: 02-pathogen/02-bacteria/clostridium-tetani
    antigen: tetanospasmin-toxoid
    coverage: ["*Clostridium tetani* (all strains — toxin is antigenically conserved)"]
antigens:
  - name: "Tetanus toxoid (tetanospasmin, formalin-inactivated)"
    source_pathogen: 02-pathogen/02-bacteria/clostridium-tetani
    modification: "Native 150 kDa tetanospasmin (TeNT) treated with formaldehyde (0.2–0.4%; 37°C, 3–4 weeks) → toxoid; toxic activity destroyed but epitope structure preserved; adsorbed to aluminum hydroxide or aluminum phosphate adjuvant"
    encoded_as: "protein (inactivated toxin)"
delivery_system: "Intramuscular or subcutaneous injection; toxoid adsorbed to alum adjuvant (Al(OH)₃ or AlPO₄)"
adjuvants: ["aluminum hydroxide (alum)", "aluminum phosphate"]
route_of_administration: "intramuscular (preferred) or subcutaneous"
dose_schedule:
  primary_series_infant_dtap: "3 doses at 2, 4, 6 months (DTaP, diphtheria-tetanus-acellular pertussis)"
  booster_infant: "DTaP at 15–18 months and 4–6 years"
  adolescent_booster: "Td (tetanus-diphtheria) at 11–12 years"
  adult_boosters: "Td every 10 years; Tdap (with acellular pertussis) once as adult"
  wound_prophylaxis: "TT if last dose >5 years before tetanus-prone wound; tetanus immune globulin (TIG) if unvaccinated"
manufacturer:
  developer: "Multiple WHO-qualified manufacturers (Sanofi Pasteur, GSK, Serum Institute of India, Bio Farma, Biological E., others)"
  partners: []
regulatory_status:
  - body: "WHO"
    status: "WHO Essential Medicines List (EML) — prequalified multiple sources"
    date: "1974-01-01"
  - body: "FDA"
    status: "Licensed — multiple formulations (Td, DTaP, Tdap)"
    date: "1938-01-01"
cold_chain: "2°C–8°C; do not freeze (freezing destroys adsorbed toxoid)"
discontinued: false
xrefs:
  rxnorm: "1887365"
  vo: "VO:0000738"
clinical_trials:
  - id: "Historical"
    tag: "Phase 3 equivalent — established pre-modern-trial era; effectiveness data from >100 RCTs of booster schedules"
sources:
  - id: who-2017-tetanus-vaccine-position
    type: clinical-guideline
    cite: "World Health Organization. Tetanus vaccines: WHO position paper — February 2017. Wkly Epidemiol Rec. 2017;92(6):53-76."
    url: "https://www.who.int/publications/i/item/who-wer9206"
    accessed: "2026-06-04"
  - id: dietz-2000-tetanus-review
    type: peer-reviewed
    cite: "Roper MH, Vandelaer JH, Gasse FL. Maternal and neonatal tetanus. Lancet. 2007;370(9603):1947-59."
    doi: "10.1016/S0140-6736(07)61619-5"
    pmid: "18021961"
    url: "https://doi.org/10.1016/S0140-6736(07)61619-5"
  - id: veronesi-1981-tetanus
    type: peer-reviewed
    cite: "Humeau Y, Doussau F, Grant NJ, Poulain B. How botulinum and tetanus neurotoxins block neurotransmitter release. Biochimie. 2000;82(5):427-46."
    doi: "10.1016/s0300-9084(00)00216-9"
    pmid: "10865130"
    url: "https://doi.org/10.1016/s0300-9084(00)00216-9"
cross_links:
  - target: 01-human/07-system/immune-system
    relation: elicits
    evidence: who-2017-tetanus-vaccine-position
    note: "Tetanus toxoid elicits strong T-helper cell-dependent IgG response; anti-TT IgG ≥0.1 IU/mL (measured by in vivo toxin neutralization or ELISA) is the protective threshold; 3-dose primary series achieves >95% seroprotection."
  - target: 01-human/04-cellular/t-helper-cell
    relation: elicits
    evidence: who-2017-tetanus-vaccine-position
    note: "Alum-adjuvanted tetanus toxoid activates CD4⁺ T helper 2 (Th2) cells; Th2 cytokines (IL-4, IL-13) drive IgG1 and IgE class switching; CD4⁺ T-cell memory is key for long-lived antibody responses to booster doses."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: elicits
    evidence: who-2017-tetanus-vaccine-position
    note: "Anti-tetanus-toxoid IgG is the primary correlate of protection; titre ≥0.1 IU/mL is protective, ≥1.0 IU/mL is considered long-term protective. Protective IgG persists ≥10 years after primary series; boosters maintain high titers."
---

# Tetanus Toxoid (TT / Td / DTaP)

## Overview

**Tetanus toxoid** is one of the oldest and most effective vaccines in the history of medicine. Tetanus — caused by the neurotoxin **tetanospasmin** produced by *Clostridium tetani* — was one of humanity's most feared diseases before vaccination: the infection caused generalized muscle spasms (risus sardonicus, opisthotonos), respiratory failure, and death in 10–90% of cases without intensive care. Neonatal tetanus (trismus neonatorum) killed hundreds of thousands of newborns annually through unsterile umbilical cord care.

Formalin-inactivated tetanus toxoid was developed in the 1920s by Gaston Ramon at the Institut Pasteur and introduced widely in the 1930s–1940s. Since its introduction into childhood immunization programs, tetanus has been **eliminated in >90% of countries** and neonatal tetanus has been reduced from ~800,000 deaths/year to <25,000/year [^who-2017-tetanus-vaccine-position].

**The toxoid vaccine principle:** Tetanospasmin is inactivated with formaldehyde, destroying its enzymatic toxic activity (zinc metalloprotease cleavage of synaptobrevin/VAMP) while preserving its protein structure and B-cell/T-cell epitopes. Neutralizing anti-toxoid IgG produced after vaccination recognizes and neutralizes the native toxin.

## Immunogenicity

**Antibody response:**
- 3-dose primary series (infancy): >95% achieve protective anti-TT IgG ≥0.1 IU/mL
- After 5th dose (kindergarten booster): >99.9% seroprotection; titers often >10 IU/mL
- Protective titers persist ≥10 years in immunocompetent adults after adequate primary series; 10-year boosters maintain long-term protection [^who-2017-tetanus-vaccine-position]

**T-cell responses:**
Alum-adjuvanted toxoid drives strong Th2-biased CD4⁺ T-cell response; memory T cells persist for decades and enable rapid recall antibody response on re-exposure or booster. The long-lived plasma cells in bone marrow sustain antibody titers between boosters.

**Toxin mechanism (what the vaccine prevents):**
Tetanospasmin (150 kDa A-B toxin; same structural family as botulinum toxin) is transported retroaxonally from the wound to spinal inhibitory interneurons and the brainstem. It cleaves **VAMP/synaptobrevin** (the v-SNARE) in Renshaw cells and glycinergic interneurons, blocking release of inhibitory neurotransmitters (glycine, GABA) → **spastic paralysis** (inability to relax muscles). Neutralizing IgG intercepts toxin in blood before axonal uptake [^veronesi-1981-tetanus].

**Correlate of protection:** Anti-TT IgG ≥0.1 IU/mL (ELISA or in vivo mouse neutralization bioassay). This threshold was established empirically from surveillance of immunized vs. non-immunized populations.

## Safety

Tetanus toxoid has an excellent safety record across 80+ years of mass use:

**Local reactions (common, self-limited):**
- Pain, redness, swelling at injection site: 25–85% (more frequent with Td than DTaP)
- Axillary lymphadenopathy: rare
- Arthur's phenomenon (localized hypersensitivity): rare; more common with too-frequent boosters

**Systemic reactions (uncommon):**
- Low-grade fever, fatigue, headache: 5–10%
- Anaphylaxis: ~0.4 per 1,000,000 doses (monitor 15 min post-injection)

**Contraindications:**
- Prior anaphylaxis to tetanus toxoid or any vaccine component
- Encephalopathy within 7 days of DTaP (withhold pertussis component, continue Td)

**Vaccine safety during pregnancy:**
Td vaccination during pregnancy (2nd/3rd trimester) is recommended by WHO for prevention of maternal and neonatal tetanus; no adverse fetal outcomes documented in extensive surveillance.

**GBS (Guillain-Barré Syndrome):**
Early 1970s observational data suggested possible signal; subsequent controlled studies found no significant association. Tetanus toxoid does not carry a GBS warning.

## Connections

- **Elicits** → [Immune System](../../../01-human/07-system/immune-system/README.md): Adsorbed tetanus toxoid is a classical T-cell-dependent antigen; the immune system generates long-lived anti-toxoid memory B cells, plasma cells, and CD4⁺ T memory cells that enable rapid recall responses upon booster.
- **Elicits** → [T-Helper Cell](../../../01-human/04-cellular/t-helper-cell/README.md): Tetanus toxoid is the canonical model T-helper cell antigen in immunology; Th2-biased CD4⁺ T memory to TT antigens drives robust, long-lasting IgG antibody responses.
- **Elicits** → [Immunoglobulin G](../../../01-human/03-molecular/immunoglobulin-g/README.md): Anti-tetanus-toxoid IgG ≥0.1 IU/mL is the protective correlate; neutralizing IgG intercepts circulating tetanospasmin before it enters motor neurons — the mechanism by which vaccination prevents disease.
