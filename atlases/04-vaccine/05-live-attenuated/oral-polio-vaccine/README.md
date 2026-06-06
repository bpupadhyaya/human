---
schema: vaccine-entry/v1
id: oral-polio-vaccine
name: "OPV (Oral Polio Vaccine / Sabin trivalent)"
atlas: 04-vaccine
platform: 05-live-attenuated
status: active
last_reviewed: 2026-06-06
summary: "Live-attenuated trivalent oral polio vaccine (tOPV) containing Sabin strains of poliovirus types 1, 2, and 3. Administered orally; replicates in the gut, inducing mucosal IgA and systemic neutralising IgG. Core tool of the WHO Global Polio Eradication Initiative; led to elimination of wild poliovirus type 2 (2015) and type 3 (2019) globally. Carries a small risk of vaccine-associated paralytic poliomyelitis (VAPP, ~1:750,000 first doses) and circulating vaccine-derived poliovirus (cVDPV)."
target_pathogens:
  - poliovirus-type-1
  - poliovirus-type-2
  - poliovirus-type-3
antigens:
  - "live attenuated poliovirus type 1 (Sabin strain LSc-2ab)"
  - "live attenuated poliovirus type 2 (Sabin strain P712/ch/2ab)"
  - "live attenuated poliovirus type 3 (Sabin strain Leon 12a1b)"
delivery_system: "live attenuated virus, oral solution"
adjuvants: []
route_of_administration: oral
dose_schedule: "3 doses at 6, 10, 14 weeks (EPI schedule); can be given at birth as a 0-dose; booster at 18 months"
manufacturer: "multiple (Bio Farma, Serum Institute of India, Panacea Biotec, BCHT, Sanofi)"
regulatory_status: "WHO prequalified; used in global polio eradication campaigns; tOPV replaced by bOPV (types 1+3) in 2016 after WPV2 eradication; mOPV2 used in outbreak response"
cold_chain: "2–8°C; heat-sensitive; VVM (vaccine vial monitor) mandatory"
discontinued: false
tags:
  - polio
  - poliovirus
  - sabin
  - live-attenuated
  - oral
  - eradication
  - mucosal-immunity
  - cVDPV
  - VAPP
  - intestinal-immunity
sources:
  - id: sabin-1957-original
    type: historical
    cite: "Sabin AB, Hennessen WA, Winsser J. Studies on variants of poliomyelitis virus. J Exp Med. 1954;99(6):551-576."
    url: "https://doi.org/10.1084/jem.99.6.551"
    note: "Foundational work establishing attenuated poliovirus strains capable of inducing immunity without disease."
  - id: WHO-eradication-2023
    type: report
    cite: "World Health Organization. Polio Global Eradication Initiative. Annual Report 2023. Geneva: WHO; 2024."
    url: "https://polioeradication.org/wp-content/uploads/2024/06/GPEI-Annual-Report-2023.pdf"
    note: "Documents current global poliovirus surveillance, OPV/IPV use, and cVDPV outbreak data."
  - id: nathanson-kew-2010
    type: peer-reviewed
    cite: "Nathanson N, Kew OM. From Emergence to Eradication: The Epidemiology of Poliomyelitis Deconstructed. Am J Epidemiol. 2010;172(11):1213-1229."
    doi: "10.1093/aje/kwq320"
    url: "https://doi.org/10.1093/aje/kwq320"
    pmid: "20978089"
  - id: molodecky-2018-lancet-VAPP
    type: peer-reviewed
    cite: "Platt LR, Estivariz CF, Sutter RW. Vaccine-associated paralytic poliomyelitis: a review of the epidemiology and estimation of the global burden. J Infect Dis. 2014;210(suppl 1):S380-S389."
    doi: "10.1093/infdis/jiu184"
    url: "https://doi.org/10.1093/infdis/jiu184"
    pmid: "25316866"
cross_links:
  - target: 04-vaccine/05-live-attenuated/bcg
    relation: platform-peer
    note: "Both are live-attenuated oral/mucosal vaccines with replication in host; BCG drives trained innate immunity whereas OPV drives mucosal IgA."
  - target: 04-vaccine/05-live-attenuated/rotarix
    relation: platform-peer
    note: "Both are live oral vaccines; rotarix uses Vero cell production; both replicate in gut; both can be impaired by maternal antibodies and enteric co-infections in LMICs."
---

# OPV (Oral Polio Vaccine / Sabin)

## Overview

**OPV** (the Oral Polio Vaccine, Sabin formulation) is a **live-attenuated trivalent (tOPV)** preparation containing all three serotypes of poliovirus: **type 1** (Sabin strain LSc-2ab), **type 2** (P712/ch/2ab), and **type 3** (Leon 12a1b). Each strain was selected by **Albert Sabin** at the University of Cincinnati through serial passage in non-human primate cells to produce variants that replicate robustly in the human intestine but have severely reduced neurovirulence — the ability to cause paralytic poliomyelitis.

OPV was first licensed in 1961 and became the cornerstone of the **WHO Global Polio Eradication Initiative (GPEI)**, launched in 1988. At that point, polio paralyzed an estimated **350,000 children per year** in 125 countries. By 2023, wild poliovirus type 1 (WPV1) transmission had been limited to two countries — Afghanistan and Pakistan — with **<10 reported WPV1 cases**. Wild poliovirus type 2 was declared eradicated in **2015**; type 3 in **2019**.

The success of OPV in eradication rests on two biological properties that no other vaccine can replicate:

1. **Intestinal mucosal immunity** — OPV replicates in the small intestine (Peyer's patches, lamina propria) and induces **secretory IgA (sIgA)** at the intestinal surface — the portal of poliovirus entry. This mucosal IgA blocks virus replication in the gut and interrupts fecal-oral transmission, which is essential for eradication.
2. **Contact spread (herd immunity amplification)** — Shed attenuated OPV virus can spread to unvaccinated contacts, immunising them passively. In high-density populations with poor sanitation, this "community immunisation" effect amplifies herd immunity beyond what vaccination coverage alone would achieve.

In 2016, the global switch from trivalent (tOPV) to **bivalent OPV (bOPV, types 1+3)** was executed on a single day across 155 countries, eliminating the type 2 Sabin strain from routine use after WPV2 eradication. Monovalent type 2 OPV (mOPV2) is now stockpiled by WHO and UNICEF for outbreak response against circulating vaccine-derived poliovirus type 2 (cVDPV2).

## Platform & Antigen Design

**Live-Attenuated Oral Poliovirus — Sabin Strain Mechanism:**

Each Sabin strain was attenuated through a combination of **specific point mutations** in the viral genome that reduce neurovirulence. The key molecular changes:

**Type 1 LSc-2ab:** Attenuation primarily driven by a **C-to-U transition at nucleotide 480** in the 5′ non-translated region (5′NTR) — a site critical for IRES (internal ribosome entry site) activity in neural cells. This mutation reduces translational efficiency specifically in neural tissue (motor neurons) while preserving intestinal tropism.

**Type 2 P712/ch/2ab:** Primary attenuation mutation at **nucleotide 481** (5′NTR, same IRES domain). Type 2 was the most genetically stable Sabin strain and paradoxically the most prone to reversion — an observation that contributed to the decision to remove it from routine OPV first.

**Type 3 Leon 12a1b:** Dual attenuating mutations at **nucleotide 472** (5′NTR) and **Ser→Phe substitution at VP3 codon 91** (capsid protein). Type 3 has the highest genetic instability and most frequent reversion events, explaining the higher VAPP risk for type 3.

**Intestinal immunisation pathway:**

```
Oral administration (2 drops on tongue or sugar cube)
        │
        ▼
Poliovirus (attenuated) binds CD155 (poliovirus receptor / Nectin-5)
on enterocytes of small intestine
        │
        ▼
Replication in gut epithelium and Peyer's patches (M cells → submucosa)
        │  ← NO neurovirulence in CNS (IRES mutation blocks neural translation)
        │
        ▼
Activation of GALT (gut-associated lymphoid tissue)
        │
        ├─ LOCAL MUCOSAL IMMUNITY
        │    B cells in lamina propria → IgA class switch → sIgA dimers
        │    Secretory IgA transported across epithelium by poly-Ig receptor
        │    Blocks poliovirus at entry portal (intestinal surface)
        │
        ├─ SYSTEMIC IMMUNITY
        │    Virus spreads to draining mesenteric lymph nodes (transient viraemia)
        │    Systemic IgG (neutralising Ab) raised against all 3 serotypes
        │    CD4⁺ and CD8⁺ T-cell responses to viral capsid proteins
        │
        └─ COMMUNITY TRANSMISSION
             Shed OPV virus in stool for 4–6 weeks post-vaccination
             Infects non-immune contacts → passive community immunisation
             (Desirable in LMIC settings; cVDPV risk if under-vaccinated community)
```

**Manufacturing:**
Sabin strains are grown in **Vero cells** (African green monkey kidney cells) or **MRC-5** human diploid cells under controlled conditions. The virus is harvested, pooled, concentrated, filtered, and blended to achieve the required potency for each serotype (per WHO standards: ≥10^6.0 CCID50/dose for type 1; ≥10^5.0 for type 2; ≥10^5.5 for type 3). The monovalent bulks are combined into trivalent or bivalent formulations. Magnesium chloride stabiliser (MgCl2 1M) is added to protect the live virus during storage. The liquid vaccine is filled into multidose vials (10 or 20 dose) with a **Vaccine Vial Monitor (VVM)** label that indicates cumulative heat exposure.

## Immunological Mechanism

**Mucosal IgA — the eradication-relevant immune response:**

The primary immunological advantage of OPV over **inactivated polio vaccine (IPV)** is its induction of **intestinal secretory IgA (sIgA)**. IPV, being injected IM, generates excellent serum IgG that prevents viraemia and paralysis but provides minimal mucosal immunity — meaning IPV-immunised individuals can still harbor and shed wild poliovirus in the gut (and therefore transmit it), whereas OPV-immunised individuals develop sIgA that blocks gut replication entirely.

This distinction is critical for eradication: only a vaccine that prevents fecal-oral transmission (not merely paralysis) can end transmission chains.

**Neutralising IgG:**

After OPV, serum neutralising IgG to each serotype rises to protective levels (≥1:8 dilution; typically ≥1:64 after 3 doses). Protective serum IgG prevents viraemia and spinal cord invasion (the mechanism of paralysis), providing sterilising systemic immunity even if gut sIgA wanes.

**T-cell responses:**

CD4+ Th1 and Th2 responses to poliovirus capsid proteins (VP1–VP4), along with CD8+ CTL responses, contribute to long-term memory and assist B-cell affinity maturation. However, the humoral (IgA + IgG) responses are the primary correlates of protection.

**Problem in LMICs — interference:**

In low-income tropical settings, OPV seroconversion rates after 3 doses can be as low as **70–75% per serotype** (vs. >95% in high-income settings). Proposed mechanisms:
- **Maternal antibodies:** Transplacental IgG against poliovirus can neutralize OPV before gut replication — reduced by delaying doses or adding a birth dose.
- **Enteric co-infections:** Concurrent gut pathogens (*Campylobacter*, *Cryptosporidium*, other enteroviruses) compete for replication niches, impair enterocyte function, and may enhance innate interferon responses that limit OPV replication.
- **Gut microbiome composition:** Enteral flora in LMIC infants differs markedly from HIC infants; specific bacterial species may interfere with poliovirus receptor availability or innate antiviral responses.
- **Nutritional status:** Malnutrition impairs mucosal immune function (IgA production, Peyer's patch architecture).

This "immunisation gap" in LMICs drove the Global Polio Eradication Initiative's strategy of repeated **National Immunisation Days (NIDs)** — targeting every child under 5 with OPV regardless of prior vaccination status, multiple times per year, in countries with known circulation.

## Efficacy

**Against paralytic poliomyelitis (wild poliovirus):**

The foundational efficacy data comes from WHO eradication program surveillance rather than classical placebo-controlled RCTs (conducting a placebo-controlled trial once wild poliovirus was circulating would have been unethical after OPV's safety and efficacy were established). Key data:

| Endpoint | Data Source | Outcome |
|:---|:---|:---:|
| Seroconversion per dose (type 1) | Multiple immunogenicity studies (India, Bangladesh) | 73–95% per dose (HIC); 70–80% cumulative after 3 doses (LMIC) |
| Seroconversion (type 2) | Global tOPV era data | >95% after 3 doses in most settings |
| Seroconversion (type 3) | Same | 80–95% after 3 doses |
| Reduction in WPV1 incidence, 1988–2023 | WHO GPEI global surveillance | >99.9% reduction (from ~350,000 cases/year to <10 in 2023) |
| WPV2 eradication | WHO declaration, September 2015 | Last detected WPV2: 1999 (India) |
| WPV3 eradication | WHO declaration, October 2019 | Last detected WPV3: 2012 (Nigeria) |

**OPV vs. IPV — mucosal immunity comparison:**

Studies in India, Pakistan, and Egypt comparing OPV with IPV directly demonstrated that OPV recipients shed significantly less poliovirus after challenge and have measurably higher intestinal sIgA titres, confirming that mucosal immunity — not systemic IgG alone — is essential for transmission interruption.

## Safety

**VAPP (Vaccine-Associated Paralytic Poliomyelitis):**

The most significant adverse event of OPV. The attenuating mutations in the Sabin strains can revert during replication in the vaccinee's gut. If enough reversions accumulate, the virus recovers neurovirulence and can cause flaccid paralysis clinically indistinguishable from wild poliovirus paralysis.

| VAPP Risk | Rate |
|:---|:---:|
| First dose (highest risk — naive gut, longest replication) | ~1 per 750,000 first doses |
| Subsequent doses | ~1 per 5.1 million doses |
| Contact VAPP (household contacts of recent vaccinees) | ~1 per 6.7 million doses distributed |

Risk factors for VAPP: immunodeficiency (particularly B-cell defects — agammaglobulinemia, CVID), type 3 serotype (highest reversion rate), first dose.

**cVDPV (Circulating Vaccine-Derived Poliovirus):**

A more serious long-term problem than VAPP. If OPV virus circulates in an under-vaccinated community for months (typically >12 months of continuous circulation), sequential replication and genetic evolution can restore full neurovirulence. The resulting cVDPV is genetically >1% diverged from the parent Sabin strain and can cause outbreaks of paralytic poliomyelitis in unimmunised populations.

cVDPV2 (derived from the type 2 Sabin strain) has emerged as the dominant cause of paralytic polio globally since the 2016 bOPV switch — because removing OPV type 2 from routine immunisation left gaps in population type 2 immunity that allow cVDPV2 to circulate in under-vaccinated areas.

**No association** with:
- Intussusception (unlike Rotashield rotavirus vaccine, OPV has no association)
- Long-term neurological sequelae in immunocompetent vaccinees
- Any systemic inflammatory disease

**Contraindications:**
- Known or suspected immunodeficiency (primary — particularly B-cell disorders — or secondary via HIV with severe immunosuppression, or high-dose immunosuppression)
- Household contacts of immunocompromised individuals should receive IPV instead to avoid contact VAPP
- Pregnancy (theoretical risk — use IPV if travel to endemic area while pregnant)

## Cold Chain & Logistics

OPV's one critical operational vulnerability is **heat sensitivity**. The live virus is inactivated by sustained heat exposure; OPV requires a continuous cold chain from manufacturer to point-of-use at 2–8°C, with a maximum of 6 months at -20°C for long-term storage.

Every multidose vial carries a **Vaccine Vial Monitor (VVM)** — a heat-sensitive label that provides cumulative temperature exposure history. The VVM changes irreversibly if the vial has been stored too warm, allowing health workers to reject compromised stock. This was a major operational innovation that enabled mass campaigns in remote areas.

One important advantage over many other vaccines: **OPV does not require injection equipment or trained injection staff** — it can be administered by lay health workers with minimal training. This enabled massive scale-up during National Immunisation Days, where thousands of volunteers administered OPV to tens of millions of children in a single day.

## Connections

- **Platform peer** → [`04-vaccine/05-live-attenuated/bcg`](../bcg/README.md) — both live-attenuated; BCG induces trained innate immunity via intradermal route; OPV induces mucosal sIgA via oral route
- **Platform peer** → [`04-vaccine/05-live-attenuated/rotarix`](../rotarix/README.md) — both live oral enteric vaccines; both face the same LMIC seroconversion challenge from maternal Ab and enteric co-infections; both use Vero cell production
- **IPV contrast** → Inactivated polio vaccine (IPV) generates systemic IgG without mucosal sIgA; protects individual from paralysis but cannot interrupt transmission — the fundamental limitation that makes IPV alone insufficient for eradication
- **Pathogen** → Poliovirus (Picornaviridae, Enterovirus C) — non-enveloped ssRNA virus; CD155 (Nectin-5) receptor; 3 serotypes; fecal-oral transmission; replicates in gut before rare CNS invasion via viraemia

---

**[← Platform 05 (Live-Attenuated)](../README.md)** · **[← Vaccine Atlas](../../README.md)** · **[Schema](../../../../schemas/vaccine-entry.schema.md)**
