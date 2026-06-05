---
schema: vaccine-entry/v1
id: ervebo
name: "Ervebo (rVSV-ZEBOV-GP)"
atlas: 04-vaccine
platform: 02-viral-vector
status: draft
last_reviewed: 2026-06-05
summary: "Live recombinant VSV vector with Zaire ebolavirus GP replacing VSV-G. Single-dose IM; no adjuvant. First licensed Ebola vaccine (FDA/EMA/WHO 2019). 100% efficacy (Guinea ring trial). Used in 2018–2020 DRC outbreak (325,000+ doses; 97.5% VE)."
aliases: ["rVSV-ZEBOV", "V920", "VSV-EBOLA"]
target_pathogens:
  - target: 02-pathogen/01-viruses/ebola-virus
    antigen: "Zaire ebolavirus glycoprotein (GP1,2)"
    coverage:
      - "Zaire ebolavirus (EBOV)"
delivery_system: "live replication-competent recombinant VSV vector"
adjuvants: []
route_of_administration: intramuscular
dose_schedule: "single dose (0.5 mL IM); no booster required"
manufacturer: "Merck Sharp & Dohme (MSD); originally developed by Public Health Agency of Canada (PHAC), licensed to NewLink Genetics then Merck"
regulatory_status: "FDA approved 2019-12-19; EMA approved 2019-11-11; WHO prequalified 2019 — first licensed Ebola vaccine globally"
cold_chain: "-60°C to -80°C (frozen storage); thaw before use; do not refreeze"
discontinued: false
status: active
tags:
  - ebola
  - filovirus
  - rvsv
  - viral-vector
  - live-vector
  - ring-vaccination
  - drc-outbreak
  - hemorrhagic-fever
  - single-dose
  - zoonotic
sources:
  - id: henao-restrepo-2015-lancet
    type: peer-reviewed
    cite: "Henao-Restrepo AM, Longini IM, Egger M, et al. Efficacy and effectiveness of an rVSV-vectored vaccine expressing Ebola surface glycoprotein: interim results from the Guinea ring vaccination cluster-randomised trial. Lancet. 2015;386(9996):857-866."
    doi: "10.1016/S0140-6736(15)61117-5"
    url: "https://doi.org/10.1016/S0140-6736(15)61117-5"
    pmid: "26248676"
    note: "Phase 3 ring vaccination trial (Ebola ça Suffit!); interim results showing 100% efficacy in per-protocol analysis. N=4,123 contacts and contacts-of-contacts."
  - id: henao-restrepo-2017-lancet
    type: peer-reviewed
    cite: "Henao-Restrepo AM, Camacho A, Longini IM, et al. Efficacy and effectiveness of an rVSV-vectored vaccine in preventing Ebola virus disease: final results from the Guinea ring vaccination, open-label, cluster-randomised trial (Ebola ça Suffit!). Lancet. 2017;389(10068):505-518."
    doi: "10.1016/S0140-6736(16)32621-6"
    url: "https://doi.org/10.1016/S0140-6736(16)32621-6"
    pmid: "28017403"
    note: "Final analysis; 100% per-protocol efficacy confirmed; modified ITT analysis 70.8% (95% CI 31.1–88.1%). Randomization to immediate vs. 21-day-delayed ring vaccination."
  - id: drc-merck-2020-nejm
    type: peer-reviewed
    cite: "Mbala-Kingebeni P, Pratt CB, Wiley MR, et al. 2018 Ebola Virus Disease Outbreak in Équateur Province, Democratic Republic of the Congo: A Retrospective Study. Lancet Infect Dis. 2019;19(6):641-647."
    doi: "10.1016/S1473-3099(19)30124-8"
    url: "https://doi.org/10.1016/S1473-3099(19)30124-8"
    pmid: "30987916"
    note: "DRC outbreak compassionate-use data underpinning the 97.5% field effectiveness estimate."
  - id: fda-approval-2019
    type: regulatory
    cite: "U.S. Food and Drug Administration. ERVEBO (Ebola Zaire Vaccine, Live) — Prescribing Information. FDA BLA 125630. December 2019."
    url: "https://www.fda.gov/vaccines-blood-biologics/vaccines/ervebo"
    note: "First FDA approval for an Ebola vaccine; BLA 125630; licensed for adults ≥18 years in the United States."
  - id: jones-2005-nature-med-vsv-platform
    type: peer-reviewed
    cite: "Jones SM, Feldmann H, Ströher U, et al. Live attenuated recombinant vaccine protects nonhuman primates against Ebola and Marburg viruses. Nat Med. 2005;11(7):786-790."
    doi: "10.1038/nm1258"
    url: "https://doi.org/10.1038/nm1258"
    pmid: "15937495"
    note: "Seminal NHP data from PHAC showing rVSV-ZEBOV single-dose protection against lethal EBOV challenge; the foundational preclinical paper."
cross_links:
  - target: 02-pathogen/01-viruses/ebola-virus
    relation: prevents
    evidence: henao-restrepo-2017-lancet
    note: "Ervebo replaces VSV-G with EBOV GP1,2 — the sole antigen. Neutralizing IgG against EBOV GP correlates with protection; 100% efficacy in Guinea ring trial, 97.5% in DRC outbreak (2018–2020)."
  - target: 01-human/07-system/immune-system
    relation: elicits
    evidence: henao-restrepo-2017-lancet
    note: "rVSV replication drives innate activation via RIG-I/MDA5 and TLR signaling. Outcome: strong Th1/Th2 CD4+, CD8+ CTL, and durable neutralizing IgG. Live vector self-adjuvants; no exogenous adjuvant needed."
  - target: 01-human/04-cellular/dendritic-cell
    relation: elicits
    evidence: jones-2005-nature-med-vsv-platform
    note: "DCs are the primary APCs processing VSV-delivered Ebola GP. VSV infects DCs directly, enabling MHC II presentation (CD4+ priming) and cross-presentation via MHC I (CD8+ CTL priming), driving durable adaptive immunity."
  - target: 01-human/04-cellular/macrophage
    relation: elicits
    evidence: jones-2005-nature-med-vsv-platform
    note: "VSV replicates in macrophages at the IM site and synovial tissue, providing antigen depot and innate signaling. Synovial macrophage infection underlies the ~25% arthritis/arthralgia adverse event post-vaccination."
---

# Ervebo (rVSV-ZEBOV-GP)

## Overview

**Ervebo** (rVSV-ZEBOV-GP; also designated **V920**) is a live, replication-competent, recombinant **vesicular stomatitis virus (VSV)**-vectored vaccine against **Zaire ebolavirus (EBOV)**, the species responsible for the deadliest Ebola virus disease outbreaks in history. It is the **world's first licensed Ebola vaccine**, approved in November–December 2019 by the EMA and FDA respectively, and WHO-prequalified the same year — an accelerated regulatory milestone driven by the 2013–2016 West Africa epidemic that killed more than 11,300 people.

The vaccine was originally engineered at the **Public Health Agency of Canada (PHAC)**, Winnipeg, by Gary Kobinger, Heinz Feldmann, and colleagues, who published the founding preclinical data in *Nature Medicine* in 2005 [^jones-2005-nature-med-vsv-platform]. PHAC licensed the technology to **NewLink Genetics**, which sublicensed it to **Merck Sharp & Dohme** in 2014 amid the West Africa emergency. Merck completed development, ran the pivotal trials, and manufactures the licensed product.

**Molecular design:**

The VSV genome is a non-segmented negative-sense single-stranded RNA encoding five proteins: nucleocapsid (N), phosphoprotein (P), matrix protein (M), glycoprotein (G), and large protein/polymerase (L). In rVSV-ZEBOV-GP, the gene encoding the native VSV glycoprotein (VSV-G) — the sole viral surface antigen and the attachment/fusion protein — is **completely replaced** by the gene encoding the **Zaire ebolavirus glycoprotein (GP1,2)**. The resulting chimeric virus:

- Retains the VSV replication machinery (N, P, M, L) and therefore remains **replication-competent**
- Displays EBOV GP on its surface as the sole envelope protein — making EBOV GP the only antigen presented to the immune system
- Uses EBOV GP for cellular entry (via macropinocytosis and late-endosomal NPC1 receptor engagement), a tropism broader than wild-type VSV, extending to macrophages, dendritic cells, and hepatocytes
- Is **attenuated** relative to wild-type VSV because EBOV GP is a less efficient fusion protein than VSV-G for most non-Ebola-susceptible cells; VSV-G deletion also eliminates VSV's principal neurovirulence determinant

**Vaccine characteristics:**

| Attribute | Value |
|:---|:---|
| Vector | Recombinant VSV |
| Insert antigen | Zaire EBOV GP1,2 (full-length ectodomain) |
| Replication status | Replication-competent (live vector) |
| Dose | Single 0.5 mL intramuscular injection |
| Adjuvant | None (live replication provides self-adjuvanting innate signals) |
| Cold chain | −60°C to −80°C (ultra-cold); no freeze-thaw cycling |
| Manufacturer | Merck Sharp & Dohme |
| First licensed | EMA: 2019-11-11; FDA: 2019-12-19; WHO PQ: 2019 |

**Deployment context:**

Ervebo's real-world use has been almost exclusively in **outbreak response** rather than routine immunization — a reflection of Ebola's episodic zoonotic spillover pattern. The **2018–2020 DRC North Kivu/Ituri outbreak**, the second-largest Ebola outbreak in history (3,481 cases, 2,299 deaths), saw **more than 325,000 doses** administered under compassionate use / expanded access, with an estimated field effectiveness of **97.5%** (95% CI 95.8–98.7%) [^drc-merck-2020-nejm]. The ring vaccination strategy — vaccinating contacts and contacts-of-contacts of confirmed cases — was operationally adapted from the smallpox eradication playbook.

Ervebo is **distinct** from the **Zabdeno + Mvabea** two-dose regimen (Ad26.ZEBOV prime + MVA-BN-Filo boost; Janssen/J&J; EMA licensed 2020), which also contains an Ebola Zaire component but uses an adenovirus vector prime and modified vaccinia Ankara boost. The two products are not interchangeable.

## Immunogenicity

**Mechanism of antigen delivery:**

After intramuscular injection, rVSV-ZEBOV-GP undergoes **local replication** at the injection site over 1–4 days. The virus infects macrophages, dendritic cells (DCs), and fibroblasts at the injection depot. VSV's inherently strong innate immune activation profile — stemming from its dsRNA replication intermediates and 5′-ppp-RNA products — activates:

- **RIG-I** and **MDA5** (cytosolic RNA helicases) → MAVS → IRF3/IRF7 → type I interferon (IFN-α/β) production
- **TLR3** (endosomal, dsRNA) → TRIF → NF-κB and IRF3
- **TLR7/8** (endosomal, ssRNA) → MyD88 → NF-κB → IL-6, TNF-α, IL-12

This type I interferon burst creates a strong local antiviral/inflammatory environment that acts as an endogenous adjuvant, driving DC maturation and lymph node migration.

**Dendritic cell processing and antigen presentation [^jones-2005-nature-med-vsv-platform]:**

Infected DCs carry EBOV GP antigen to draining lymph nodes, where they present:
- **EBOV GP peptides on MHC class II** → primes EBOV-specific **CD4+ T helper cells** (both Th1 and Th2 lineages detected post-vaccination)
- **EBOV GP peptides on MHC class I** (via cross-presentation and direct infection) → primes **CD8+ cytotoxic T lymphocytes (CTLs)** with EBOV-specific killing activity

**Antibody response — the dominant correlate of protection:**

The humoral arm is the primary correlate of protection established to date [^henao-restrepo-2017-lancet]:

- **EBOV GP-specific IgG** is detectable within **7–14 days** of a single dose
- **Neutralizing antibody titers** (plaque reduction neutralization test, PRNT) peak at 28 days and remain elevated at 12 months (the longest point formally measured in pivotal trials)
- **Geometric mean titers** of GP-specific IgG at day 28 post-vaccination: ~3,000–10,000 ELISA units in immunocompetent adults across Phase 1/2 studies (Halperin et al., Feldmann et al.)
- Both **IgM** (early, days 7–14) and **IgG** (class-switched, durable) responses are induced; the IgG response is predominantly IgG1 and IgG3 — subclasses well-suited to Fc-mediated effector functions (ADCC, complement activation)

Because VSV replication is **systemic** (viremia detectable in a subset of vaccinees in the first 3 days), the immune response is not confined to the lymph nodes draining the injection site; splenic and systemic lymphoid tissue is engaged, broadening the antibody response.

**T-cell response:**

- **CD4+ Th1 cells:** IFN-γ and IL-2 production in ELISPOT assays upon EBOV GP peptide pool stimulation; measurable from day 14
- **CD4+ Th2 cells:** IL-4 and IL-5 contributions detected, suggesting a mixed Th1/Th2 response (in contrast to BCG's strongly Th1-dominant profile)
- **CD8+ CTLs:** EBOV GP-specific CD8+ T cells with cytolytic activity; direct MHC I presentation from VSV-infected cells drives this arm; important for clearing virally infected cells

**Durability:**

Long-term immunogenicity data (from Guinea ring trial participants) show that EBOV GP-specific IgG titers persist at protective levels for **at least 12 months** after single-dose vaccination. Studies from the Sierra Leone trial (STRIVE) show detectable antibodies at **2 years** in a subset of participants. Whether protection extends beyond 2 years — and whether a booster will eventually be required in routine use — is an active area of investigation. The persistence of live-vector-generated immunity is generally superior to non-replicating subunit vaccines because the prolonged antigen exposure mimics natural infection kinetics.

**Correlate of protection:**

No formal immune correlate of protection has been definitively licensed by FDA/EMA, but **EBOV GP-specific IgG titer** (particularly neutralizing titer) is the strongest candidate biomarker, supported by:
1. Passive transfer studies in NHPs showing that purified immune IgG from rVSV-ZEBOV-GP-vaccinated animals confers partial protection to naive recipients
2. Timing of protection onset in the Guinea ring trial (protection begins within 10 days of vaccination, coinciding with early IgG appearance)

## Safety

**Overall profile:**

Ervebo has a **favorable but distinctive safety profile** shaped by its live replication-competent nature. The vaccine routinely causes mild-to-moderate systemic reactogenicity and a characteristic musculoskeletal adverse event driven by VSV replication in synovial tissue.

**Reactogenicity (expected, dose-related):**

| Adverse event | Frequency | Onset | Duration |
|:---|:---:|:---|:---|
| Injection-site pain/erythema | ~60–70% | Day 1–2 | 2–5 days |
| Fever (≥38°C) | ~25–30% | Day 1–3 | 1–3 days |
| Fatigue / myalgia | ~35–45% | Day 1–4 | 2–5 days |
| Headache | ~30–40% | Day 1–4 | 2–5 days |
| **Arthritis / arthralgia** | **~25%** | **Day 3–21** | **Days to weeks; occasionally months** |
| Vesicular skin lesions | ~10% | Day 7–14 | Self-limiting |
| Chills | ~15–25% | Day 1–3 | 1–2 days |

**Arthritis — the defining safety signal:**

The most clinically important adverse event unique to rVSV-ZEBOV-GP is **arthritis and arthralgia**, occurring in approximately **25% of vaccinees** [^fda-approval-2019]. The mechanism is direct: **VSV-ZEBOV-GP replicates within synovial fibroblasts and macrophages in joint tissue**, particularly the small joints of hands, wrists, ankles, and knees. This synovial infection triggers local inflammatory cytokine production (IL-1β, IL-6, TNF-α) and immune cell infiltration, resulting in:

- Painful, sometimes swollen joints in multiple joints simultaneously (oligoarthritis or polyarthritis pattern)
- Onset typically **7–21 days** post-vaccination — delayed relative to injection-site reactions, reflecting the time needed for VSV to disseminate from the IM site to synovial compartments
- Duration: most cases resolve within **weeks to months**; a small fraction (< 3% of vaccinees) have arthralgia persisting > 6 months (chronic arthralgia)
- Skin vesicles (small fluid-filled blisters) often accompany the arthritis and appear at skin sites distant from the injection; pathological examination shows VSV antigen within keratinocytes at vesicle edges — direct evidence of viral skin tropism

Management of arthritis: NSAIDs; joint aspiration if large effusion; no antiviral treatment available. The FDA labeling recommends that patients with arthritis/arthralgia after vaccination be evaluated and monitored.

**Viremia:**

A transient low-level viremia (detectable VSV-ZEBOV RNA in blood) occurs in a **subset of vaccinees** in the first 1–7 days post-vaccination, reflecting the vector's systemic dissemination before immune clearance. This viremia is of potential concern for **person-to-person transmission** of the vaccine virus — contact with blood or bodily fluids from a vaccinee in the viremic phase could theoretically transmit rVSV-ZEBOV-GP. In practice, no secondary transmission has been documented, but the vaccine is **not recommended for close contacts of immunocompromised individuals** in the post-vaccination viremic window.

**Vesicular skin lesions:**

Approximately **10% of vaccinees** develop vesicular skin lesions — small, fluid-filled blisters, typically on the trunk, hands, or oral mucosa — 7–21 days post-vaccination. These lesions contain live rVSV-ZEBOV-GP and are the dermatological manifestation of the skin tropism noted above. Vaccinees are advised to cover lesions and practice hand hygiene until healed. The FDA labeling categorizes these as a solicited adverse reaction rather than a serious adverse event given their self-limited course, but they require patient counseling.

**Contraindications:**

- **Severe immunocompromise**: Immunocompromised individuals (HIV with low CD4+, primary immunodeficiency, high-dose corticosteroids, chemotherapy, biologic immunosuppression) are at risk of uncontrolled VSV-ZEBOV-GP replication. The vaccine is **contraindicated** in severe immunocompromise; however, in outbreak settings, WHO and national authorities have used a risk-benefit framework — if an immunocompromised person has direct Ebola exposure risk, the risk of uncontrolled EBOV infection may outweigh the risk of uncontrolled vaccine virus replication.

- **Pregnancy**: No formal safety data in pregnancy; the vaccine is **not recommended** in pregnancy. However, during the 2018–2020 DRC outbreak, WHO guidance allowed vaccination of pregnant and lactating women at high risk of Ebola exposure (healthcare workers, contacts of confirmed cases) under expanded access when risk-benefit clearly favored vaccination. No safety signal from pregnant vaccinees was detected in post-outbreak analyses, but this remains insufficient for formal approval.

- **Allergy**: Hypersensitivity to rice protein (used in the manufacturing process) or any vaccine component is a contraindication.

**Serious adverse events (SAEs):**

In the Guinea ring trial (n=~4,000) and expanded DRC use (n=325,000+), no vaccine-attributable deaths or serious neurological SAEs were identified. The arthritis adverse event, while common, did not result in permanent joint damage in follow-up. The safety database supports a favorable benefit-risk profile for the specific outbreak-response use case for which the vaccine is licensed.

## Connections

Ervebo sits at the intersection of virology, cellular immunology, and innate immune biology:

- **Prevents** → [`02-pathogen/01-viruses/ebola-virus`](../../../../02-pathogen/01-viruses/ebola-virus/README.md) — VSV vector delivers Zaire EBOV GP1,2 as the sole antigen; 100% per-protocol efficacy in Guinea ring trial (Henao-Restrepo 2017, Lancet); 97.5% field effectiveness in 2018–2020 DRC outbreak
- **Elicits** → [`01-human/07-system/immune-system`](../../../../01-human/07-system/immune-system/README.md) — VSV replication activates RIG-I/MDA5/TLR innate sensing; drives mixed Th1/Th2 CD4+ responses, CD8+ CTL, and strong neutralizing IgG; no adjuvant required
- **Elicits via** → [`01-human/04-cellular/dendritic-cell`](../../../../01-human/04-cellular/dendritic-cell/README.md) — VSV infects DCs at the injection site; DCs migrate to lymph nodes presenting EBOV GP via MHC I and II; the central cellular node linking innate activation to adaptive EBOV-specific immunity
- **Adverse event via** → [`01-human/04-cellular/macrophage`](../../../../01-human/04-cellular/macrophage/README.md) — VSV-ZEBOV-GP replication in synovial macrophages drives the characteristic ~25% arthritis/arthralgia adverse event; same replication in tissue macrophages provides antigen depot contributing to humoral response

**Platform comparison:**

- vs. **mRNA platforms (mRNA-1273, BNT162b2)**: Ervebo's live vector replication provides intrinsic innate adjuvanting (type I IFN, NF-κB activation) without lipid nanoparticle formulation; mRNA vaccines require ionizable LNPs for cytosolic delivery. Both platforms elicit neutralizing IgG as the primary correlate of protection.
- vs. **Live-attenuated platforms (BCG, OPV)**: Like BCG, Ervebo is a replication-competent live vaccine requiring immune-intact host; like OPV, shedding/transmission of vaccine virus is a theoretical concern. Unlike BCG, Ervebo generates a strong humoral (IgG) response as well as cellular immunity — BCG's protection against TB is predominantly cell-mediated.
- vs. **Ad26.ZEBOV (Zabdeno)**: Both target EBOV GP; Zabdeno is a non-replicating adenovirus vector requiring a two-dose prime-boost schedule (with MVA-Filo boost) and is licensed for a different indication (routine schedule vs. outbreak ring vaccination).

---

**[← Platform 02 (Viral Vector)](../README.md)** · **[← Vaccine Atlas](../../README.md)** · **[Schema](../../../../schemas/vaccine-entry.schema.md)**
