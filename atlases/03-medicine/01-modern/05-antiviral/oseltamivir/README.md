---
schema: medicine-entry/v1
id: oseltamivir
name: Oseltamivir
atlas: 03-medicine
scale: 01-modern
status: draft
last_reviewed: 2026-06-04
summary: "Neuraminidase inhibitor prodrug used for influenza A and B treatment and prophylaxis. Reduces symptom duration ~1 day; reduces hospitalizations in high-risk patients. WHO Essential Medicine; government-stockpiled pandemic backbone. Resistance via H274Y mutation in N1."
aliases: ["Tamiflu", "oseltamivir phosphate", "GS-4104", "Ro 64-0796"]
drug_class: neuraminidase inhibitor
modality: small molecule
key_agents:
  - oseltamivir phosphate
who_essential_medicine: true
atc: J05AH02
tags:
  - antiviral
  - influenza
  - neuraminidase
  - prodrug
  - tamiflu
  - pandemic
sources:
  - id: von-itzstein-1993
    type: peer-reviewed
    cite: "von Itzstein M, Wu WY, Kok GB, et al. Rational design of potent sialidase-based inhibitors of influenza virus replication. Nature. 1993;363(6428):418-23."
    doi: "10.1038/363418a0"
    url: "https://doi.org/10.1038/363418a0"
  - id: jefferson-2014-cochrane
    type: systematic-review
    cite: "Jefferson T, Jones MA, Doshi P, et al. Oseltamivir for influenza in adults and children: systematic review of clinical study reports and summary of regulatory comments. BMJ. 2014;348:g2545. (Cochrane review series)"
    doi: "10.1002/14651858.CD001265.pub4"
    url: "https://doi.org/10.1002/14651858.CD001265.pub4"
  - id: dobson-2015-lancet
    type: peer-reviewed
    cite: "Dobson J, Whitley RJ, Pocock S, Monto AS. Oseltamivir treatment for influenza in adults: a meta-analysis of randomised controlled trials. Lancet. 2015;385(9979):1729-37."
    doi: "10.1016/S0140-6736(15)60459-2"
    url: "https://doi.org/10.1016/S0140-6736(15)60459-2"
cross_links:
  - target: 02-pathogen/01-viruses/influenza-a
    relation: treats
    note: "Oseltamivir reduces influenza A (and B) symptom duration and severity by inhibiting neuraminidase-mediated viral egress; first-line treatment for seasonal influenza and pandemic strains including H5N1 and H1N1pdm09."
  - target: 02-pathogen/01-viruses/influenza-a
    relation: modulates
    note: "Blocks neuraminidase (NA) cleavage of sialic acid on host glycoproteins; newly assembled virions remain tethered to the host cell surface, preventing spread to uninfected cells. Selection pressure from oseltamivir drives H274Y resistance mutation in N1 neuraminidase."
  - target: 01-human/07-system/respiratory-system
    relation: treats
    note: "Oseltamivir reduces influenza A/B symptom duration by ~17 hours (Dobson meta-analysis, Lancet 2015); reduces hospitalization in high-risk patients (elderly, immunocompromised, pregnant); must be started within 48h of symptom onset for maximal benefit."
  - target: 01-human/06-organ/ards
    relation: connects-to
    note: "Severe influenza (H5N1, H1N1pdm09) causes viral ARDS via type II pneumocyte destruction and cytokine storm; early oseltamivir reduces ICU admission and ARDS risk; WHO recommends early treatment for severely ill regardless of >48h symptom delay."
  - target: 01-human/07-system/cytokine-storm
    relation: connects-to
    note: "Severe influenza triggers cytokine storm (IL-6, TNF-α, IFN-γ) proportional to viral load; oseltamivir limits viral replication → attenuates cytokine storm magnitude; key rationale for treatment in H5N1 and severe seasonal influenza beyond the 48h window."
---

# Oseltamivir

## Overview

Oseltamivir (trade name **Tamiflu**) is a **neuraminidase inhibitor** — an antiviral small molecule that competitively and reversibly inhibits influenza neuraminidase (NA), the surface glycoprotein enzyme essential for viral release from infected cells. It is active against influenza A (all NA subtypes N1–N9) and influenza B viruses.

Oseltamivir is administered as an **oral prodrug** (oseltamivir phosphate ethyl ester) that is converted by hepatic esterases to the active carboxylate form (oseltamivir carboxylate, GS-4071), achieving systemic bioavailability of ~80%. It is the most widely used antiviral for influenza globally, listed on the **WHO List of Essential Medicines**, and maintained in strategic national stockpiles as a pandemic-preparedness measure following its pivotal role in the H5N1 avian influenza threat and the H1N1 pandemic of 2009.

Oseltamivir grew from the rational drug design programme pioneered by von Itzstein et al. [^von-itzstein-1993], who identified that transition-state analogues of sialic acid could potently inhibit influenza neuraminidase — the same structural rationale that produced zanamivir (inhaled route).

## Mechanism

### Prodrug Activation

Oseltamivir phosphate (the oral form) is an ethyl ester prodrug with modest intrinsic activity. After oral absorption:

1. Intestinal absorption is rapid and nearly complete (~80%)
2. **Hepatic carboxylesterase 1 (CES1)** cleaves the ethyl ester → oseltamivir carboxylate (active metabolite, GS-4071)
3. Peak plasma concentration of active metabolite: ~3–4 hours after oral administration
4. Renal clearance (active tubular secretion via organic anion transporters OAT1/OAT3); dose reduction required when creatinine clearance <30 mL/min

### Neuraminidase Inhibition

Influenza neuraminidase (NA) is a **tetrameric surface glycoprotein** (NA subtype designates H1N1, H3N2, H5N1, etc.) that cleaves sialic acid (N-acetylneuraminic acid) from glycoprotein chains on host cell surfaces:

| Step in viral life cycle | NA role | Effect of oseltamivir |
|:---|:---|:---|
| **Viral entry** | Minor role — cleaves decoy receptors in mucus | Blocked; virus may have slightly impaired penetration through mucus layer |
| **Viral budding** | Essential — cleaves sialic acid anchoring nascent virions to infected cell surface | Blocked → newly assembled virions remain tethered to the host cell membrane |
| **Viral spread** | Releases free virions to infect new cells | Prevented → virion aggregates form at cell surface; infection spread to uninfected cells dramatically reduced |

Oseltamivir carboxylate is a **transition-state analogue** of sialic acid: it occupies the enzyme active site with higher affinity than the natural substrate (sialic acid), forming a stable complex that competitively excludes substrate binding. The binding is reversible but with sufficiently high affinity (Ki ~1 nM range) to be clinically effective at therapeutic concentrations.

### Secondary Effects

At concentrations achieved clinically, oseltamivir may also:
- Inhibit **viral haemagglutinin (HA)** from binding sialic acid on new host cells (mild, secondary mechanism)
- Reduce pro-inflammatory cytokine release (partial mechanistic basis for severity reduction beyond simple antiviral effect)
- Reduce bacterial co-infection risk by preserving respiratory epithelial barrier integrity

## Clinical Use

### Indications

| Indication | Timing | Population |
|:---|:---|:---|
| **Treatment of influenza A or B** | Must begin within **48 hours** of symptom onset for maximum benefit; may still benefit hospitalised patients if started later | Adults and children ≥2 weeks old |
| **Post-exposure prophylaxis** | Start within 48h of contact; continue 10 days | Household contacts of confirmed influenza; healthcare workers post-exposure |
| **Seasonal prophylaxis** | During outbreak periods; 6-week community outbreaks | Immunocompromised; elderly in care facilities; when vaccination is contraindicated |
| **Pandemic use** | H5N1 avian flu; H1N1 2009 pandemic | All ages per public health guidance; priority to hospitalised and high-risk |

### Dosing

- **Adults (treatment):** 75 mg orally twice daily × 5 days
- **Adults (prophylaxis):** 75 mg once daily × 10 days (post-exposure) or up to 6 weeks (community)
- **Children:** Weight-based dosing for <40 kg (30–75 mg per dose depending on weight); paediatric suspension available
- **Renal impairment:** Dose reduction to 75 mg once daily for treatment (CrCl 10–30 mL/min); 30 mg once daily for prophylaxis

### High-Risk Populations

Oseltamivir reduces hospitalisation and serious complications in:
- Adults ≥65 years
- Children <2 years (especially infants)
- Pregnancy (influenza carries excess maternal and fetal morbidity)
- Severe immunosuppression (HIV, transplant, chemotherapy)
- Chronic cardiopulmonary disease, diabetes, obesity

## Evidence

### Efficacy in Uncomplicated Influenza

The Dobson et al. meta-analysis (Lancet 2015) [^dobson-2015-lancet], using individual patient data from 9 Roche-sponsored RCTs (n=4,328), found:

- **Time to alleviation of illness reduced by 17.6 hours** (~1 day) in adults treated within 48h
- **Reduction in hospitalisation risk** in adults (OR 0.37, 95% CI 0.17–0.81) — a significant finding that partially resolved earlier controversy
- **Benefit in high-risk patients** was more pronounced than in otherwise healthy adults

### The Cochrane Controversy

The Jefferson et al. Cochrane review (2014) [^jefferson-2014-cochrane], which analysed both published and unpublished clinical study reports (CSRs) obtained from Roche and EMA, reached more cautious conclusions:

- Confirmed ~17-hour reduction in symptom duration in adults (consistent with Dobson)
- **Could not confirm** statistically robust reduction in hospitalisations or pneumonia complications based on the full CSR dataset — in contrast to the published trial reports
- Raised concerns about publication bias in the original trial literature
- Prompted Roche to release full CSR data to the Cochrane group — a landmark event for clinical trial transparency

**Outcome:** WHO reviewed both analyses and **maintained oseltamivir on the Essential Medicines List**, accepting the symptom-duration benefit as real and the hospitalisation signal from individual patient data (Dobson) as supportive evidence for high-risk use. The controversy produced lasting policy reform in clinical trial data access.

### Pandemic and Avian Influenza

- **H5N1 avian influenza:** Oseltamivir reduced mortality in H5N1-infected patients when given early; resistance (H274Y) emerged in some treated cases
- **H1N1 2009 pandemic:** Backbone of pandemic pharmacological response globally; observational data showed benefit in hospitalised patients when started within 48h; oseltamivir reduced ICU admission and death in severely ill patients across multiple cohort studies
- **Zanamivir comparison:** Both neuraminidase inhibitors are similarly efficacious; zanamivir (inhaled) is preferred when oseltamivir resistance is suspected; intravenous zanamivir and intravenous peramivir are options for critically ill patients unable to receive oral/inhaled agents

### Resistance

| Mutation | NA subtype | Effect |
|:---|:---|:---|
| **H274Y** (His274Tyr, N2 numbering H275Y) | N1 (including H1N1, H5N1) | Oseltamivir-resistant; zanamivir-sensitive; confers ~270-fold reduction in oseltamivir binding affinity |
| **R292K** | N2 | Dual resistance (oseltamivir and zanamivir); rare |
| **E119V** | N2 | Oseltamivir reduced susceptibility; clinical significance uncertain |

The **H274Y mutation** became clinically significant when oseltamivir-resistant seasonal H1N1 strains circulated globally in 2008–2009, predominating in some countries; this strain was subsequently displaced by H1N1pdm09 (which was oseltamivir-sensitive). Resistance surveillance (WHO FluNet) is ongoing.

### Adverse Effects

| Effect | Frequency | Notes |
|:---|:---|:---|
| **Nausea and vomiting** | ~10–15% (dose-dependent) | Most common; reduced by taking with food |
| **Headache, dizziness** | ~5–10% | Generally mild |
| **Neuropsychiatric events** | Rare; signal from Japan (self-injury, abnormal behaviour in children/adolescents) | FDA added warning; no causal relationship conclusively established; monitoring recommended in paediatric use; Japan issued stronger warnings |
| **Renal clearance reduction** | Relevant in elderly/CKD | Monitor renal function; dose-adjust |

## Connections

- **Treats** → [Influenza A](../../../../02-pathogen/01-viruses/influenza-a/README.md): reduces symptom duration, severe disease, and transmission risk; neuraminidase inhibition prevents virion egress from infected cells.
- **Modulates** → [Influenza A](../../../../02-pathogen/01-viruses/influenza-a/README.md): blocks NA-mediated virion release; H274Y resistance mutation selected by drug pressure; zanamivir retains activity against H274Y strains.
- **Treats** → [Respiratory System](../../../../01-human/07-system/respiratory-system/README.md): Reduces influenza A/B symptom duration by ~17 hours (Dobson, Lancet 2015); reduces hospitalization in high-risk patients; must be started within 48h of onset for maximal benefit.
- **Connects-to** → [ARDS](../../../../01-human/06-organ/ards/README.md): Severe influenza (H5N1, H1N1pdm09) causes viral ARDS via type II pneumocyte destruction; early oseltamivir reduces ICU admission and ARDS risk; WHO recommends treatment for severely ill regardless of 48h window.
- **Connects-to** → [Cytokine Storm](../../../../01-human/07-system/cytokine-storm/README.md): Severe influenza triggers cytokine storm (IL-6, TNF-α, IFN-γ) proportional to viral load; oseltamivir limits viral replication → attenuates cytokine storm; key rationale for treatment in H5N1 and severe seasonal influenza.

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^von-itzstein-1993]: von Itzstein M, Wu WY, Kok GB, et al. Rational design of potent sialidase-based inhibitors of influenza virus replication. *Nature.* 1993;363(6428):418-23. [doi:10.1038/363418a0](https://doi.org/10.1038/363418a0)
[^jefferson-2014-cochrane]: Jefferson T, Jones MA, Doshi P, et al. Oseltamivir for influenza in adults and children: systematic review of clinical study reports and summary of regulatory comments. *BMJ.* 2014;348:g2545. Cochrane review: [doi:10.1002/14651858.CD001265.pub4](https://doi.org/10.1002/14651858.CD001265.pub4)
[^dobson-2015-lancet]: Dobson J, Whitley RJ, Pocock S, Monto AS. Oseltamivir treatment for influenza in adults: a meta-analysis of randomised controlled trials. *Lancet.* 2015;385(9979):1729-37. [doi:10.1016/S0140-6736(15)60459-2](https://doi.org/10.1016/S0140-6736(15)60459-2)
