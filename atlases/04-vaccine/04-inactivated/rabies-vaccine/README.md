---
schema: vaccine-entry/v1
id: rabies-vaccine
name: "Rabies Vaccine (Inactivated)"
atlas: 04-vaccine
platform: 04-inactivated
status: draft
last_reviewed: 2026-06-05
summary: "Inactivated whole-virus vaccine (HDCV, PCECV, PVRV) preventing rabies via pre- or post-exposure prophylaxis. PEP is nearly 100% effective if given promptly; once neurological symptoms appear, survival is near-zero. ~59,000 deaths/year remain preventable."
aliases: ["HDCV", "PCECV", "PVRV", "Rabipur", "RabAvert", "Imovax", "Verorab"]
target_pathogens:
  - target: 02-pathogen/01-viruses/rabies-virus
    antigen: "inactivated whole rabies virus (street/CVS or Pitman-Moore strain)"
    coverage:
      - "Rabies lyssavirus (classical rabies)"
delivery_system: "inactivated whole virus in cell-culture supernatant, aluminium phosphate adjuvant (some formulations)"
adjuvants:
  - "aluminium phosphate (HDCV formulation; PCECV/PVRV may be adjuvant-free)"
route_of_administration: intramuscular (deltoid); intradermal (approved for some formulations in resource-limited settings)
dose_schedule: |
  Pre-exposure prophylaxis (PrEP): 2-dose IM series Day 0 and Day 7 (WHO 2018 schedule); traditional 3-dose Day 0/7/21-28 also accepted.
  Post-exposure prophylaxis (PEP): 4–5 doses IM on Days 0/3/7/14 (Essen) or Days 0/3/7 (Zagreb 2-site), combined with rabies immune globulin (RIG) on Day 0 for previously unvaccinated patients.
manufacturer: "Sanofi Pasteur (HDCV — Imovax), Bavarian Nordic/GSK (PCECV — RabAvert/Rabipur), Sanofi Pasteur (PVRV — Verorab), and others"
regulatory_status: "HDCV licensed in US and EU since 1980; PCECV (RabAvert) US-licensed 1997; PVRV (Verorab) WHO prequalified; all three WHO-recommended platforms"
cold_chain: "2–8°C; do not freeze; lyophilized formulations (HDCV, some PCECV) reconstitute before use; liquid PVRV single-dose vials"
discontinued: false
status: active
tags:
  - rabies
  - inactivated
  - whole-virus
  - hdcv
  - pcecv
  - pvrv
  - post-exposure-prophylaxis
  - pre-exposure-prophylaxis
  - zoonosis
  - neurotropic
  - rig
  - beta-propiolactone
sources:
  - id: fooks-2014-nat-rev-dis-primers
    type: peer-reviewed
    cite: "Fooks AR, Banyard AC, Horton DL, et al. Current status of rabies and prospects for elimination. Lancet. 2014;384(9951):1389-1399."
    doi: "10.1016/S0140-6736(13)62707-5"
    url: "https://doi.org/10.1016/S0140-6736(13)62707-5"
    pmid: "25078306"
    note: "Comprehensive review of rabies epidemiology, virology, and elimination prospects."
  - id: who-2018-rabies-vaccines-position-paper
    type: guideline
    cite: "World Health Organization. Rabies vaccines: WHO position paper – April 2018. Wkly Epidemiol Rec. 2018;93(16):201-220."
    url: "https://www.who.int/publications/i/item/who-wer9316"
    note: "Authoritative WHO guidance on PrEP 2-dose schedule, PEP regimens, and RIG use."
  - id: hampson-2015-plos-neg-trop-dis-burden
    type: peer-reviewed
    cite: "Hampson K, Coudeville L, Lembo T, et al. Estimating the global burden of endemic canine rabies. PLoS Negl Trop Dis. 2015;9(4):e0003709."
    doi: "10.1371/journal.pntd.0003709"
    url: "https://doi.org/10.1371/journal.pntd.0003709"
    pmid: "25881058"
    note: "Definitive burden estimate: ~59,000 human deaths/year, 99% from dog bites, 40% in children under 15."
  - id: wilde-1996-nejm-pep-review
    type: peer-reviewed
    cite: "Wilde H, Sirikawin S, Sabcharoen A, et al. Failure of postexposure treatment of rabies in children. Clin Infect Dis. 1996;22(2):228-232."
    doi: "10.1093/clinids/22.2.228"
    url: "https://doi.org/10.1093/clinids/22.2.228"
    pmid: "8838177"
    note: "Critical analysis of PEP failures; highlights the time-dependence of efficacy and importance of wound washing plus RIG."
cross_links:
  - target: 02-pathogen/01-viruses/rabies-virus
    relation: prevents
    note: "Neutralizing antibodies (≥0.5 IU/mL) block viral attachment to nAChR and p75NTR; PEP interrupts retrograde axonal transport before virus reaches CNS. No effective treatment once encephalitis begins."
  - target: 01-human/07-system/nervous-system
    relation: protects
    note: "Rabies virus invades via peripheral nerves and ascends to the CNS at ~12–24 mm/day. PEP must precede neuroinvasion; once the virus enters the spinal cord and brainstem, the vaccine is ineffective."
  - target: 01-human/04-cellular/b-cell
    relation: elicits
    note: "B cells produce virus-neutralizing IgG targeting the rabies glycoprotein G; titer ≥0.5 IU/mL (WHO threshold) correlates with protection. Memory B-cell responses allow rapid anamnestic rise on booster or re-exposure."
  - target: 01-human/04-cellular/dendritic-cell
    relation: elicits
    note: "Inactivated virus particles are processed by dendritic cells at the injection site; antigen presentation via MHC II drives CD4+ T-helper priming and supports germinal centre B-cell responses for high-affinity IgG."
---

# Rabies Vaccine (Inactivated)

## Overview

**Rabies vaccine** is an inactivated whole-virus vaccine that prevents the invariably fatal encephalitis caused by *Rabies lyssavirus*. It is the only proven intervention against a disease with a near-100% case-fatality rate once clinical symptoms appear — making timely post-exposure prophylaxis (PEP) one of the most consequential clinical decisions in medicine.

### Historical development

The first rabies vaccine was created by **Louis Pasteur and Émile Roux** in 1885, using desiccated spinal cord from rabies-infected rabbits — a crude preparation that nonetheless saved the life of young Joseph Meister after a severe dog bite. For most of the 20th century, vaccines were manufactured in **nervous tissue** (sheep or suckling mouse brain), carrying significant risk of post-vaccination neuroparalytic accidents (incidence ~1 in 200–2,000) due to myelin basic protein contamination. These preparations are now largely replaced but still used in parts of Africa and Asia due to cost.

The modern era of rabies vaccines began with the development of the **Human Diploid Cell Vaccine (HDCV)** by Wiktor, Koprowski, and colleagues at the Wistar Institute, licensed in France in 1974 and in the US in 1980 under the trade name **Imovax** (Sanofi Pasteur). HDCV established the template for safe, immunogenic, cell-culture-based inactivated rabies vaccines. It was followed by the **Purified Chick Embryo Cell Vaccine (PCECV)** — marketed as **Rabipur** (Europe) and **RabAvert** (US/Canada) — and the **Purified Vero Cell Rabies Vaccine (PVRV)**, marketed as **Verorab** (Sanofi Pasteur), which is the most cost-effective and most widely distributed formulation globally, now WHO prequalified.

### Three principal modern platforms

| Platform | Brand name(s) | Cell substrate | Market |
|:---|:---|:---|:---|
| HDCV | Imovax Rabies | Human diploid (MRC-5) fibroblasts | US, EU, high-income |
| PCECV | RabAvert (US), Rabipur (EU) | Embryonated hen eggs (chick embryo cells) | Global, high-income |
| PVRV | Verorab, Abhayrab, others | Vero (African green monkey kidney) cells | Global, WHO prequalified, LMICs |

### Manufacturing process

All three platforms share the same essential workflow:

1. **Seed virus**: A fixed (passaged, non-pathogenic) rabies virus strain — either the **CVS (Challenge Virus Standard)** strain or the **Pitman-Moore (PM)** strain — is propagated in the appropriate cell substrate.
2. **Harvest**: Culture supernatant is collected after lytic infection; Vero-based vaccines may use roller-bottle or bioreactor suspension culture.
3. **Inactivation**: Whole virus is inactivated using either **β-propiolactone (BPL)**, which alkylates viral RNA while preserving surface glycoprotein integrity, or **binary ethylenimine (BEI)** in some formulations. BPL is the standard for HDCV and PCECV; it is highly effective and leaves no biologically active residue after hydrolysis.
4. **Concentration and purification**: Ultrafiltration and sucrose density gradient centrifugation remove cellular debris and concentrate virus particles. PCECV uses zonal centrifugation; PVRV uses membrane filtration.
5. **Formulation**: The purified, inactivated virus is formulated into single-dose vials. HDCV and some PCECV formulations are **lyophilized** (freeze-dried) and must be reconstituted with supplied diluent immediately before use. PVRV is typically available as a **liquid single-dose** formulation (0.5 mL or 1 mL), requiring no reconstitution, simplifying field use.

The critical antigen is the **rabies glycoprotein G** — the sole surface protein that generates virus-neutralizing antibodies. Inactivation conditions are carefully optimized to preserve the native trimeric conformation of glycoprotein G so that the neutralizing epitope sites (antigenic sites I, II, III) remain intact and immunogenic after BPL treatment.

### Dose schedules

**Pre-exposure prophylaxis (PrEP):**

The **2018 WHO updated schedule** recommends a simplified **2-dose IM series on Day 0 and Day 7** — a schedule change from the previous 3-dose Day 0/7/21-28 regimen, based on immunogenicity data showing equivalent seroconversion. Doses are given in the **deltoid muscle** (never gluteal, which produces suboptimal responses). PrEP is indicated for veterinarians, animal handlers, laboratory workers, spelunkers, travelers to high-risk areas, and residents of endemic regions.

PrEP does not eliminate the need for PEP after an exposure, but it dramatically simplifies it: pre-immunized patients require only **2 PEP booster doses** on Days 0 and 3, with **no RIG** (because their existing memory B-cell response produces adequate neutralizing antibodies within 24–48 hours of the booster, whereas unimmunized patients cannot mount IgG rapidly enough to block neuroinvasion during the critical first days).

**Post-exposure prophylaxis (PEP):**

For previously unvaccinated patients after a category III exposure (bites penetrating skin, scratches drawing blood, mucous membrane contamination):

- **Wound care first** — immediate, thorough washing of the wound with soap and water for ≥15 minutes, followed by povidone-iodine, is the single most effective first step and can reduce viral inoculum by up to 90%.
- **Rabies Immune Globulin (RIG)** — passive immunization administered on Day 0 only, infiltrated around the wound and remainder given IM at a distant site. Human RIG (HRIG) dose: 20 IU/kg body weight; equine RIG (ERIG) dose: 40 IU/kg. RIG provides immediate passive protection during the 7–14-day lag before active vaccine-induced antibodies reach protective titers. RIG must NOT be given beyond Day 7 (it can suppress the active immune response).
- **Vaccine series** — 4 or 5 doses depending on regimen:
  - **Essen regimen** (original): Days 0, 3, 7, 14, and 28 (5 doses IM)
  - **Zagreb regimen** (2-site): 2 doses on Day 0 (different sites) + 1 dose on Days 7 and 21 (4 doses, 2 visits after Day 0)
  - **WHO 2018 abbreviated** (updated Essen): 4 doses on Days 0, 3, 7, 14 IM — the 28-day dose eliminated based on non-inferiority data

The absolute primacy of PEP in rabies control cannot be overstated: **PEP is essentially 100% effective** if initiated promptly after exposure, before the virus has entered peripheral nerve axons and begun its retrograde march to the CNS. There are no documented cases of rabies in patients who received complete, correctly administered PEP (vaccine + RIG) promptly. Conversely, PEP is entirely futile once clinical encephalitis begins — there is no licensed antiviral treatment for rabies, and only a handful of survivors have been reported worldwide, almost all with profound neurological sequelae.

### Global burden and elimination context

Rabies kills an estimated **59,000 people per year** [^hampson-2015-plos-neg-trop-dis-burden], with **95% of deaths in Asia and Africa**, overwhelmingly caused by domestic dog bites. Children under 15 account for 40% of deaths. The WHO **"Zero by 30"** initiative (zero human rabies deaths from dog-mediated rabies by 2030) relies on three simultaneous strategies: mass dog vaccination (70% coverage breaks transmission), expanded access to affordable PEP for bite victims, and improved surveillance. Economic modeling shows that investing in these three pillars is highly cost-effective relative to the current human and economic burden.

## Immunogenicity

### The correlate of protection

The established **correlate of protection** for rabies vaccines is a **virus-neutralizing antibody (VNA) titer of ≥0.5 IU/mL**, as measured by the Rapid Fluorescent Focus Inhibition Test (RFFIT) or the Fluorescent Antibody Virus Neutralization (FAVN) test. This threshold was established by WHO based on clinical and experimental data and is the regulatory benchmark for lot release testing and assessment of individual immune response adequacy.

Virtually all immunocompetent individuals seroconvert after a standard PrEP or PEP series: reported seroconversion rates for HDCV, PCECV, and PVRV are uniformly **>99%** in healthy adults, with geometric mean titers typically reaching 5–20 IU/mL after the primary series — well above the 0.5 IU/mL threshold.

### Mechanism of antibody-mediated protection

The primary protective mechanism is **virus-neutralizing IgG** directed against the **rabies glycoprotein G**, the trimeric type I transmembrane protein that mediates viral attachment to host cell receptors and membrane fusion in the endosome [^fooks-2014-nat-rev-dis-primers]:

- **Attachment inhibition**: Neutralizing antibodies block the interaction between glycoprotein G and the two principal cell-entry receptors — **nicotinic acetylcholine receptor (nAChR)** at the neuromuscular junction and **p75 neurotrophin receptor (p75NTR)** on peripheral nerve terminals. By blocking receptor binding, antibodies prevent viral entry into the initial target cells at the bite site.
- **Post-attachment neutralization**: Antibodies against conformational epitopes on glycoprotein G also neutralize virus after attachment but before membrane fusion, inhibiting the low-pH-triggered conformational change required for endosomal escape.
- **Key antigenic sites**: Site III (the immunodominant site, amino acids 330–338) and Site II (conformational, two discontinuous loops) are the principal targets of potent neutralizing antibodies. Mutations at Arg333 in site III are the most common determinant of vaccine escape, though this is rare with fixed vaccine strains.

### CD4+ T-helper cell support

Inactivated rabies vaccines, like all inactivated vaccines, produce their antibody response through **T-dependent B-cell activation** [^who-2018-rabies-vaccines-position-paper]. Inactivated viral particles are taken up and processed by antigen-presenting cells (primarily **dendritic cells** at the injection site and draining lymph nodes), which present glycoprotein G-derived peptides on **MHC class II** molecules to naive CD4+ T-helper cells. The resulting CD4+ Th2/Tfh (T follicular helper) response provides the cognate help required for B-cell class switching to IgG, affinity maturation in germinal centers, and long-lived plasma cell differentiation. This CD4+ Th response is why rabies VNA titers fall progressively after vaccination and why periodic boosters are recommended for individuals in continuous-risk occupations.

### Kinetics: the PEP window

A critical immunological concept for PEP is the **antibody kinetics window** relative to viral neuroinvasion. After a primary vaccination series, VNA titers typically:
- Day 7: Detectable in most individuals (>0.5 IU/mL in ~50% after first dose)
- Day 14: Protective titers in virtually all immunocompetent individuals
- Day 28: Peak titers; decline begins over months to years

Rabies virus, after inoculation at a bite site, replicates locally in muscle tissue for a period ranging from **days to weeks** (depending on viral load, wound site, and distance from CNS), then enters unmyelinated nerve terminals at the neuromuscular junction via receptor-mediated endocytosis. Retrograde axonal transport proceeds at **12–24 mm/day**. This transport phase — from bite site to spinal cord — represents the **critical PEP window**: if VNA titers reach 0.5 IU/mL before the virus enters the spinal cord, infection is aborted. Once the virus clears this boundary, it is effectively beyond humoral neutralization because the CNS parenchyma has very limited antibody access and the blood-brain barrier further restricts IgG penetration.

This race between antibody kinetics and axonal transport explains why:
1. **RIG on Day 0** is non-negotiable for unvaccinated patients — it provides immediate passive VNA while the vaccine-induced response mounts.
2. **Delays in PEP initiation** are directly correlated with rare PEP failures.
3. **Bites to the face, head, or neck** are the highest risk — shorter axonal distance to the CNS compresses the window to days.

### Memory and durability

After a complete primary series, memory B cells and long-lived plasma cells persist for years. In studies of individuals who received PrEP, detectable VNA titers (>0.5 IU/mL) were found in the majority of participants for **2–5 years** post-vaccination, with rapid anamnestic booster responses (within 48 hours) on re-exposure or booster. This is the basis for:
- **Occupational titer monitoring**: Workers in continuous-risk settings (e.g., bat biologists, virologists, veterinarians) should have VNA checked every 6 months to 2 years; a booster is administered if titers fall below 0.5 IU/mL.
- **Simplified PEP for pre-immunized**: Only 2 booster doses (Day 0 and 3) are needed; no RIG, because memory B-cell-derived antibodies rise within 24–48 hours — fast enough to cover the transport window even for high-risk bites.

## Safety

Inactivated rabies vaccines have been administered to **hundreds of millions** of individuals over more than four decades and have an excellent safety record. Because they contain no live virus, they are **safe in immunocompromised patients, pregnant women, and neonates** — populations for whom live-attenuated vaccines carry specific contraindications.

### Common adverse reactions

Local reactions are the most frequently reported adverse events [^who-2018-rabies-vaccines-position-paper]:
- **Injection site pain, erythema, swelling, and induration**: 30–74% of vaccinees; mild and self-limiting (1–2 days).
- **Systemic reactions**: Headache (~15%), nausea (~10%), myalgia (~5–10%), mild fever (<5%). These are all mild and short-lived.

### Serious adverse events

**Type III hypersensitivity (serum sickness-like reaction) — HDCV specific:**

The most clinically important serious adverse event associated with modern cell-culture vaccines is a **serum sickness-like reaction** reported specifically with **HDCV boosters** (not primary series), with an incidence of approximately **6% in re-vaccinated adults**. The reaction occurs 2–21 days after a booster dose and manifests as urticaria, angioedema, arthralgias, and malaise. It is caused by immune complex formation between pre-existing anti-HDCV IgG and beta-propiolactone-altered human albumin present as a trace manufacturing contaminant in HDCV — an antigen absent in PCECV and PVRV formulations. Management is symptomatic (antihistamines, short-course corticosteroids); anaphylaxis is rare (<1 in 10,000). The reaction led to reformulation efforts and is a driver of PCECV/PVRV preference for occupational boosters.

**Anaphylaxis:**

True IgE-mediated anaphylaxis is rare across all platforms (<1 in 100,000 doses). Patients who experience anaphylaxis during a PEP series should be managed in consultation with allergy-immunology; the series generally must be continued because rabies exposure is life-threatening — options include switching to a different vaccine platform or administering doses under medical supervision with epinephrine available.

**Neurological adverse events:**

Neuroparalytic events (Guillain-Barré-like presentations) were the major safety hazard of the old nervous tissue vaccines, occurring at a rate of ~1 in 200 with suckling mouse brain vaccines. With modern cell-culture vaccines (HDCV, PCECV, PVRV), the incidence of neurological adverse events is not statistically distinguishable from background population rates. No causal neurological risk is attributed to modern inactivated rabies vaccines. This is a foundational safety improvement that drove the transition away from nervous tissue vaccines.

### Special populations

- **Immunocompromised patients**: No contraindication to inactivated rabies vaccines. However, immune response may be attenuated — VNA titer should be checked after the primary series, and additional doses given if titer is below 0.5 IU/mL. RIG is especially important in PEP for immunocompromised individuals regardless of prior vaccination history.
- **Pregnancy**: No contraindication. Rabies exposure during pregnancy is a medical emergency; PEP should never be withheld. No teratogenic risk has been identified with inactivated vaccines, and vertical transmission of rabies virus would be uniformly fatal to both mother and fetus.
- **Infants and children**: Safe at any age. Dose volume and site are the same as adults (0.5–1 mL IM deltoid or anterolateral thigh in infants). Seroconversion rates are equivalent.
- **Chloroquine and immunosuppressants**: Chloroquine (antimalarial) and systemic corticosteroids can suppress rabies vaccine seroconversion. Intradermal PrEP is particularly susceptible; IM PrEP is preferred if the patient is on chloroquine.

### What does NOT apply to inactivated rabies vaccines

Unlike live-attenuated vaccines:
- No risk of **vaccine-derived viral disease** — the inactivated virus cannot replicate.
- No risk of **shedding or secondary transmission**.
- No contraindication in **SCID, HIV, or other cellular immunodeficiencies** from a safety standpoint (though efficacy may be impaired).
- **No intussusception risk** (relevant distinction from some live oral vaccines).
- **No reversion to virulence**.

## Connections

The rabies vaccine sits at the intersection of virology, neuroscience, and immunology — its life-or-death clinical calculus is governed by the race between viral axonal transport and vaccine-induced antibody kinetics.

- **Prevents** → [`02-pathogen/01-viruses/rabies-virus`](../../../../02-pathogen/01-viruses/rabies-virus/README.md) — neutralizing IgG against glycoprotein G blocks receptor-mediated entry; PEP aborts infection before CNS invasion; 59,000 deaths/year remain preventable with timely administration [^hampson-2015-plos-neg-trop-dis-burden]
- **Protects** → [`01-human/07-system/nervous-system`](../../../../01-human/07-system/nervous-system/README.md) — rabies virus exploits retrograde axonal transport (12–24 mm/day) to reach the brainstem and limbic system; VNA from vaccine must exceed 0.5 IU/mL before the virus clears the spinal cord entry point
- **Elicits** → [`01-human/04-cellular/b-cell`](../../../../01-human/04-cellular/b-cell/README.md) — glycoprotein G-specific B cells undergo germinal center affinity maturation, class switching to IgG, and long-lived plasma cell differentiation; memory B cells enable the rapid anamnestic PEP response in pre-immunized patients [^who-2018-rabies-vaccines-position-paper]
- **Elicits** → [`01-human/04-cellular/dendritic-cell`](../../../../01-human/04-cellular/dendritic-cell/README.md) — inactivated virions processed by dendritic cells at the injection site drive MHC II antigen presentation to CD4+ Tfh cells, providing cognate B-cell help for IgG class switching and affinity maturation

---

**[← Platform 04 (Inactivated)](../README.md)** · **[← Vaccine Atlas](../../README.md)** · **[Schema](../../../../schemas/vaccine-entry.schema.md)**
