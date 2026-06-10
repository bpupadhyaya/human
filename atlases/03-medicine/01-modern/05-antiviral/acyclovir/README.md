---
schema: medicine-entry/v1
id: acyclovir
name: Acyclovir
atlas: 03-medicine
scale: 01-modern
status: draft
last_reviewed: 2026-06-06
summary: "Nucleoside analogue prodrug selectively activated by viral thymidine kinase to acyclovir triphosphate, which chain-terminates HSV/VZV DNA polymerase. First-line for HSV-1, HSV-2, VZV infections. Elion 1988 Nobel Prize in Physiology or Medicine."
aliases: ["aciclovir", "Zovirax", "acycloguanosine", "ACV", "9-(2-hydroxyethoxymethyl)guanine"]
drug_class: nucleoside analogue antiviral
modality: small molecule
key_agents:
  - acyclovir
  - valacyclovir (prodrug with improved bioavailability)
  - famciclovir (related prodrug)
atc: J05AB01
sources:
  - id: elion-1977-acyclovir
    type: peer-reviewed
    cite: "Elion GB, Furman PA, Fyfe JA, et al. Selectivity of action of an antiherpetic agent, 9-(2-hydroxyethoxymethyl) guanine. Proc Natl Acad Sci USA. 1977;74(12):5716-20."
    doi: "10.1073/pnas.74.12.5716"
    pmid: "202961"
    url: "https://doi.org/10.1073/pnas.74.12.5716"
  - id: whitley-1986-acyclovir-hsv
    type: peer-reviewed
    cite: "Whitley RJ, Gnann JW Jr. Acyclovir: a decade later. N Engl J Med. 1992;327(11):782-9."
    doi: "10.1056/NEJM199209103271108"
    pmid: "1501651"
    url: "https://doi.org/10.1056/NEJM199209103271108"
  - id: skoldenberg-1984-hsv-encephalitis
    type: peer-reviewed
    cite: "Skoldenberg B, Forsgren M, Alestig K, et al. Acyclovir versus vidarabine in herpes simplex encephalitis. Randomised multicentre study in consecutive Swedish patients. Lancet. 1984;2(8405):707-11."
    doi: "10.1016/S0140-6736(84)92623-0"
    pmid: "6148571"
    url: "https://doi.org/10.1016/S0140-6736(84)92623-0"
cross_links:
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: treats
    evidence: whitley-1986-acyclovir-hsv
    note: "Acyclovir (oral or IV) is first-line treatment for varicella (chickenpox) in adults, immunocompromised patients, and neonates, and for herpes zoster (shingles); VZV thymidine kinase (ORF36) is less efficient than HSV TK, requiring higher doses."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: modulates
    note: "By limiting HSV/VZV replication, acyclovir reduces viral antigen load and the pathological CD8+ T cell-mediated neuroinflammation in herpes encephalitis, allowing immune resolution."
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: "Acyclovir suppresses viral replication but does not eliminate latency; immunocompetent host immune response required for complete viral clearance. In immunocompromised patients, prolonged therapy prevents dissemination."
  - target: 02-pathogen/01-viruses/herpesvirus
    relation: treats
    note: "Acyclovir is first-line therapy for alphaherpesvirinae (HSV-1, HSV-2, VZV); 3000-fold selective phosphorylation by viral TK (UL23/ORF36) over host TK-1; ACV-TP chain-terminates viral DNA polymerase; valacyclovir prodrug achieves 3-5× higher oral bioavailability."
  - target: 02-pathogen/01-viruses/epstein-barr-virus
    relation: modulates
    note: "Acyclovir inhibits EBV lytic replication via BGLF4 kinase-mediated phosphorylation; IV acyclovir reduces EBV viral load in severe mononucleosis and post-transplant lymphoproliferative disease; minimal effect on latent EBV — does not prevent PTLD but controls lytic replication."
  - target: 01-human/06-organ/kidney
    relation: damages
    note: "High-dose IV acyclovir crystallises in renal tubules → crystalline nephropathy (obstructive AKI); risk: dehydration, rapid infusion, CKD; dose adjustment: CrCl 25-50 → 50% dose; CrCl <25 → 25% dose; adequate hydration (≥500 mL/h) prevents crystalluria during infusion."
  - target: 01-human/06-organ/brain
    relation: treats
    note: "IV acyclovir (10-15 mg/kg q8h × 14-21 days) is life-saving in HSV encephalitis: reduced mortality 70%→19% (Skoldenberg 1984 Lancet); empirical treatment must start immediately on clinical suspicion before CSF PCR result; delays >48h worsen neurological outcome."
---

# Acyclovir

## Overview

Acyclovir (aciclovir; trade name **Zovirax**) is a **synthetic acyclic nucleoside analogue** — the first selective antiviral agent and the prototype of a drug class that transformed the management of herpesvirus infections. Developed by Gertrude Elion and colleagues at Burroughs Wellcome in the 1970s, acyclovir represented a paradigm shift in antiviral pharmacology: the demonstration that antivirals could be designed to exploit enzymatic differences between viral and host cells to achieve selective toxicity [^elion-1977-acyclovir]. Elion received the **Nobel Prize in Physiology or Medicine in 1988**, shared with George Hitchings and Sir James Black, partly for this discovery.

Acyclovir is active against **Herpes simplex virus 1 and 2 (HSV-1, HSV-2)** and **Varicella-Zoster virus (VZV)**, and has moderate activity against **Epstein-Barr virus (EBV)** and **cytomegalovirus (CMV)** (though CMV lacks the viral TK that efficiently phosphorylates acyclovir; ganciclovir is preferred for CMV). It has no activity against non-herpesvirus families.

Acyclovir is listed on the **WHO List of Essential Medicines** and remains a cornerstone of antiviral therapy globally. Its orally bioavailable prodrug **valacyclovir** (Valtrex) achieves ~3-5× higher plasma concentrations and is the preferred oral formulation for most indications.

## Mechanism

### Viral Thymidine Kinase-Mediated Activation (Selectivity Basis)

Acyclovir (9-(2-hydroxyethoxymethyl)guanine) is an **acyclic nucleoside**: it contains the guanine base but lacks the 3'-OH group of the deoxyribose sugar — the structural modification that makes it an obligate chain terminator. In its unphosphorylated form it has no antiviral activity. Selective activation depends on a three-step phosphorylation cascade:

| Step | Enzyme | Product | Compartment |
|:---|:---|:---|:---|
| **1st phosphorylation (rate-limiting)** | Viral thymidine kinase (HSV TK, gene UL23; VZV TK, ORF36) | Acyclovir monophosphate (ACV-MP) | Infected cell only |
| **2nd phosphorylation** | Host cellular guanylate kinase (GK) | Acyclovir diphosphate (ACV-DP) | Infected + uninfected cells |
| **3rd phosphorylation** | Host nucleoside diphosphate kinase (NDPK) | Acyclovir triphosphate (ACV-TP) | Infected + uninfected cells |

The critical selectivity resides in **Step 1**: HSV thymidine kinase (TK) phosphorylates acyclovir ~3,000-fold more efficiently than human thymidine kinase-1 (TK1). Thus, acyclovir triphosphate accumulates to concentrations ~40–100× higher in HSV-infected cells than in uninfected host cells. VZV TK is less efficient (~10-fold preference vs. HSV TK), requiring higher acyclovir doses for VZV infections.

### Chain Termination of Viral DNA Polymerase

Acyclovir triphosphate (ACV-TP) acts as a **competitive inhibitor** and **obligate chain terminator** of viral DNA polymerase (HSV UL30, VZV ORF28):

1. ACV-TP competes with dGTP for binding to the viral DNA polymerase active site
2. ACV-TP is incorporated into the growing viral DNA chain at guanine positions
3. Because acyclovir lacks a 3'-OH group, no further nucleotide addition is possible — **chain elongation terminates**
4. The polymerase-template-ACV-TP complex is further stabilised in a non-productive "dead-end" complex, resulting in irreversible enzyme inactivation
5. Viral DNA replication halts; progeny virion production ceases

The selectivity ratio of ACV-TP for viral vs. host DNA polymerase-δ/ε is approximately **30–100-fold**, providing a wide therapeutic index. This combined selectivity (TK-step and polymerase-step) makes acyclovir remarkably non-toxic to normal host cells.

### Pharmacokinetics

| Parameter | Acyclovir (oral) | Valacyclovir (oral prodrug) |
|:---|:---|:---|
| **Bioavailability** | 10–20% | ~55% (converted to acyclovir by intestinal/hepatic valacyclovirase) |
| **Peak plasma (Cmax)** | ~0.5–1.0 µg/mL (200 mg dose) | ~2.0–3.0 µg/mL equivalent |
| **Half-life (plasma)** | 2.5–3.3 hours (normal renal function) | Similar after conversion |
| **Elimination** | Renal; 85% unchanged via glomerular filtration + tubular secretion | Same |
| **CNS penetration** | ~50% of serum levels; sufficient for herpes encephalitis (IV dosing) | |
| **Dose adjustment** | Required for CrCl <25 mL/min | Required for renal impairment |

## Clinical Use

### Indications

| Indication | Route/Dose | Duration |
|:---|:---|:---|
| **Genital herpes simplex (primary episode)** | Valacyclovir 1 g PO BID or acyclovir 400 mg PO TID | 7–10 days |
| **Genital HSV (recurrent)** | Valacyclovir 500 mg PO BID or acyclovir 800 mg PO TID | 3–5 days |
| **HSV suppressive therapy** | Valacyclovir 500–1000 mg PO daily | Indefinite |
| **Herpes labialis (cold sores)** | Valacyclovir 2 g PO BID × 1 day | 1 day |
| **Herpes zoster (shingles)** | Valacyclovir 1 g PO TID or famciclovir 500 mg TID | 7 days |
| **Varicella in adults** | Valacyclovir 1 g PO TID | 5–7 days |
| **Herpes simplex encephalitis** | Acyclovir 10–15 mg/kg IV every 8h | 14–21 days |
| **Neonatal HSV (disseminated/CNS)** | Acyclovir 20 mg/kg IV every 8h | 14–21 days |
| **VZV/HSV in immunocompromised** | Acyclovir 10 mg/kg IV every 8h | 7–14 days |

### Resistance

Acyclovir resistance occurs primarily through **thymidine kinase mutations** (TK-deficient or TK-altered strains); polymerase mutations (UL30) are less common. Resistance is rare (<0.5%) in immunocompetent patients but occurs in 3–5% of immunocompromised patients with prolonged or repeated acyclovir exposure (transplant recipients, HIV/AIDS). TK-deficient mutants are **cross-resistant to valacyclovir, ganciclovir, and penciclovir** (all requiring viral TK for activation). **Foscarnet** (pyrophosphate analogue, directly inhibits viral polymerase without TK activation) is the treatment of choice for acyclovir-resistant HSV/VZV.

## Evidence

### Landmark Trial — Herpes Simplex Encephalitis

The Skoldenberg et al. randomized trial (Lancet 1984) [^skoldenberg-1984-hsv-encephalitis] compared IV acyclovir vs. IV vidarabine in 47 patients with biopsy-confirmed herpes simplex encephalitis (HSE):

- **Mortality at 6 months:** acyclovir 19% vs. vidarabine 50% — absolute reduction of 31%
- **Neurological outcomes:** significantly better in acyclovir group (fewer severely disabled survivors)
- Established IV acyclovir as standard of care for HSE — maintained to this day

This trial was considered among the most practice-changing antiviral studies ever conducted, as HSE was uniformly fatal or severely disabling before acyclovir.

### Genital Herpes and Suppression

Multiple RCTs established that:
- Acyclovir/valacyclovir reduces recurrence frequency by ~70–80% in chronic suppressive therapy
- **Valacyclovir suppressive therapy reduces HSV-2 transmission to seronegative partners by ~48%** (Corey et al., NEJM 2004) — the first antiviral proven to reduce STI transmission
- Episodic therapy shortens outbreak duration by 1–2 days and reduces viral shedding

### Neonatal HSV

IV acyclovir reduces neonatal HSV mortality from ~65% (untreated) to ~4% for disseminated disease and from 50% to ~6% for CNS disease (Kimberlin et al., Pediatr Infect Dis J 2001). High-dose IV followed by oral suppression for 6 months significantly improves neurodevelopmental outcomes in neonates with HSV CNS disease.

### Herpes Zoster

Acyclovir/valacyclovir initiated within 72 hours of rash onset:
- Reduces acute zoster pain duration
- Accelerates rash healing
- Reduces (but does not eliminate) risk of postherpetic neuralgia — benefit modest but real in adults >50 years
- Does not eliminate VZV latency

## Connections

- `treats` → **[Varicella-Zoster Virus](../../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — first-line oral (valacyclovir) or IV treatment for varicella in adults and immunocompromised patients, and for herpes zoster; VZV TK less efficient than HSV TK, requiring higher doses.
- `modulates` → **[Cytotoxic T Cell](../../../../01-human/04-cellular/t-cytotoxic-cell/README.md)** — by suppressing viral replication and antigen load, acyclovir reduces HSV/VZV-driven CD8+ T cell-mediated neuroinflammation, enabling immune resolution in herpes encephalitis.
- `modulates` → **[Immune System](../../../../01-human/07-system/immune-system/README.md)** — suppresses viral replication but does not eliminate latency; host cellular immunity required for complete viral control; prolonged therapy prevents dissemination in immunocompromised patients.
- `treats` → **[Herpesviridae](../../../../02-pathogen/01-viruses/herpesvirus/README.md)** — acyclovir is first-line therapy for alphaherpesvirinae (HSV-1, HSV-2, VZV); 3000-fold selective phosphorylation by viral TK over host TK-1; ACV-TP chain-terminates viral DNA polymerase; valacyclovir prodrug achieves 3-5× higher oral bioavailability.
- `modulates` → **[Epstein-Barr Virus](../../../../02-pathogen/01-viruses/epstein-barr-virus/README.md)** — acyclovir inhibits EBV lytic replication via BGLF4 kinase-mediated phosphorylation; reduces EBV viral load in severe infectious mononucleosis; minimal activity on latent EBV — does not prevent post-transplant lymphoproliferative disease (PTLD) but controls lytic viral burden.
- `damages` → **[Kidney](../../../../01-human/06-organ/kidney/README.md)** — high-dose IV acyclovir can crystallise in renal tubules → crystalline nephropathy (obstructive AKI); risk factors: dehydration, rapid infusion, pre-existing CKD; dose reduction required for CrCl <50 mL/min; adequate IV hydration prevents crystalluria.
- `treats` → **[Brain](../../../../01-human/06-organ/brain/README.md)** — IV acyclovir (10–15 mg/kg q8h × 14–21 days) is life-saving in HSV encephalitis, reducing mortality from 70% to 19% (Skoldenberg 1984); empirical treatment must start immediately on clinical suspicion, before CSF PCR confirmation; treatment delays >48h worsen neurological outcomes.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^elion-1977-acyclovir]: Elion GB, Furman PA, Fyfe JA, et al. Selectivity of action of an antiherpetic agent, 9-(2-hydroxyethoxymethyl) guanine. *Proc Natl Acad Sci USA.* 1977;74(12):5716-20. [doi:10.1073/pnas.74.12.5716](https://doi.org/10.1073/pnas.74.12.5716) · [PubMed 202961](https://pubmed.ncbi.nlm.nih.gov/202961/)
[^whitley-1986-acyclovir-hsv]: Whitley RJ, Gnann JW Jr. Acyclovir: a decade later. *N Engl J Med.* 1992;327(11):782-9. [doi:10.1056/NEJM199209103271108](https://doi.org/10.1056/NEJM199209103271108) · [PubMed 1501651](https://pubmed.ncbi.nlm.nih.gov/1501651/)
[^skoldenberg-1984-hsv-encephalitis]: Skoldenberg B, Forsgren M, Alestig K, et al. Acyclovir versus vidarabine in herpes simplex encephalitis. Randomised multicentre study in consecutive Swedish patients. *Lancet.* 1984;2(8405):707-11. [doi:10.1016/S0140-6736(84)92623-0](https://doi.org/10.1016/S0140-6736(84)92623-0) · [PubMed 6148571](https://pubmed.ncbi.nlm.nih.gov/6148571/)
