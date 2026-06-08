---
schema: human-scale-entry/v1
id: protein-c
name: Protein C
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "Protein C (PROC; chr2q14.3) is a vitamin K–dependent anticoagulant zymogen; thrombin-thrombomodulin → APC; APC + Protein S inactivate FVa and FVIIIa → brakes thrombin. Deficiency → inherited thrombophilia; FV Leiden R506Q blocks APC cleavage → most common inherited thrombophilia."
aliases: ["protein C", "PROC", "APC", "activated protein C", "anticoagulant protein C", "PC", "drotrecogin alfa"]
sources:
  - id: dahlback-2008-protein-c-review
    type: peer-reviewed
    cite: "Dahlbäck B. Advances in understanding pathogenic mechanisms of thrombophilic disorders. Blood. 2008;112(1):19-27."
    doi: "10.1182/blood-2008-01-077909"
    pmid: "18574048"
    url: "https://doi.org/10.1182/blood-2008-01-077909"
  - id: bertina-1994-factor-v-leiden
    type: peer-reviewed
    cite: "Bertina RM, Koeleman BP, Koster T, et al. Mutation in blood coagulation factor V associated with resistance to activated protein C. Nature. 1994;369(6475):64-67."
    doi: "10.1038/369064a0"
    pmid: "8164741"
    url: "https://doi.org/10.1038/369064a0"
cross_links:
  - target: 01-human/07-system/inherited-thrombophilia
    relation: connects-to
    note: "Protein C deficiency (PROC mutations) is one of the 5 major inherited thrombophilias alongside FV Leiden, prothrombin G20210A, protein S deficiency, and AT deficiency; type I = low antigen + activity; type II = low activity with normal antigen; 5-10× VTE risk in heterozygotes."
  - target: 01-human/03-molecular/thrombin
    relation: connects-to
    note: "Thrombin bound to endothelial thrombomodulin cleaves protein C activation peptide → APC; high thrombin paradoxically activates the anticoagulant pathway; thrombin-thrombomodulin also activates TAFI (thrombin-activatable fibrinolysis inhibitor) → fibrin protection from lysis."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Protein C deficiency → 5-10× VTE risk (heterozygous) vs. 50-100× (rare homozygous → neonatal purpura fulminans); warfarin-induced skin necrosis from rapid protein C drop at warfarin initiation; APC is consumed in sepsis-DIC → purpura fulminans in acquired PC deficiency."
---

# Protein C

## Overview

**Protein C** (gene *PROC*, chromosome 2q14.3; also called autoprothrombin IIA) is a **vitamin K-dependent plasma glycoprotein** and the central element of the **protein C anticoagulant pathway** — the body's primary mechanism for inactivating coagulation co-factors FVa and FVIIIa and thereby shutting down thrombin generation at physiological sites [^dahlback-2008-protein-c-review]. Circulating as an inactive zymogen at ~4 μg/mL (65 nM), protein C requires **activation by the thrombin-thrombomodulin complex** on endothelial surfaces to become **activated protein C (APC)**, a serine protease.

The protein C pathway is elegantly paradoxical: **thrombin itself — the primary pro-coagulant enzyme — is also responsible for activating the anticoagulant pathway**. When thrombin escapes the site of vascular injury and encounters intact endothelium, thrombomodulin captures it → APC is generated → FVa/FVIIIa are destroyed → thrombin generation is limited. This built-in feedback mechanism confines the clotting response to the injury site.

**Factor V Leiden (FV R506Q)** — the most common inherited thrombophilia (~5% of Europeans; ~1 in 20 Caucasians) — is a missense mutation at the primary APC cleavage site in FV/FVa (Arg506 → Gln) [^bertina-1994-factor-v-leiden]. This single amino acid substitution renders FVa **resistant to APC cleavage**, abolishing the primary feedback mechanism of the protein C pathway and leading to persistent, uncontrolled prothrombinase complex activity and thrombin generation → DVT/PE risk 4-8× higher in heterozygotes, 50-80× in homozygotes.

## Structure

### Protein C domain architecture

Protein C is a **62 kDa two-chain zymogen** (light chain + heavy chain linked by a single disulfide bond):

| Domain | Chain | Features |
|:-------|:------|:---------|
| **Gla domain** | Light | N-terminal; 9 γ-carboxyglutamate (Gla) residues; vitamin K-dependent; binds Ca²⁺ + phospholipid → membrane anchoring |
| **EGF-like domain 1** | Light | Ca²⁺-binding; binds thrombomodulin and EPCR |
| **EGF-like domain 2** | Light | Structural scaffold |
| **Activation peptide** | Heavy | 12 aa; cleaved by thrombin-thrombomodulin → generates APC |
| **Serine protease domain** | Heavy | Catalytic triad Ser360-His211-Asp257; cleaves FVa at Arg506 (primary) and Arg306 (secondary); cleaves FVIIIa at Arg336 |

**Vitamin K dependence:** Gla residues require vitamin K-dependent γ-carboxylation by GGCX (γ-glutamyl carboxylase) in hepatocytes. Warfarin inhibits VKORC1 (vitamin K epoxide reductase complex subunit 1) → prevents Gla domain carboxylation → non-functional protein C (and factors II, VII, IX, X) → anticoagulation. **Critical: protein C has the shortest half-life (~8h) among all vitamin K-dependent factors**, making it the first to fall when warfarin is started → transient hypercoagulable state → risk of warfarin-induced skin necrosis in protein C-deficient patients.

### Thrombomodulin and EPCR

**Thrombomodulin (THBD):**
- Endothelial transmembrane glycoprotein; binds thrombin with high affinity → conformational change in thrombin
- Thrombin-thrombomodulin complex: thrombin loses fibrinogen/PAR-1 cleavage activity (anticoagulant switch) and gains protein C activation activity → APC generated 1000× faster than by free thrombin
- Thrombomodulin also mediates TAFI activation → antifibrinolysis

**EPCR (endothelial protein C receptor; PROCR):**
- GPI-anchored endothelial receptor; binds protein C and APC via the Gla domain
- EPCR + thrombomodulin = optimal protein C activation (EPCR presents protein C to the thrombin-TM complex)
- EPCR-bound APC has additional cytoprotective effects: via PAR-1 cleavage → anti-inflammatory, anti-apoptotic, and barrier-protective signaling in endothelium
- Soluble EPCR (sEPCR) shed by ADAM17/10 → blocks EPCR-bound protein C activation; elevated in sepsis and autoimmune disease

### Protein S (co-factor)

**Protein S (PROS1):**
- Vitamin K-dependent non-enzymatic co-factor for APC
- Exists in two forms: ~60% bound to C4b-binding protein (C4BP) — inactive; ~40% free — active APC co-factor
- Free protein S dramatically enhances APC cleavage of FVa (especially at Arg306, the secondary site) and FVIIIa → synergistic anticoagulant effect
- Protein S deficiency → reduced APC co-factor activity → thrombophilia (similar to protein C deficiency)
- Estrogen and pregnancy → ↑C4BP → ↓free protein S → acquired thrombophilia (partial explanation for pregnancy-associated VTE risk)

## Function

### Anticoagulant mechanism

**APC anticoagulant pathway:**

1. **APC cleaves FVa at Arg506** (primary; FV Leiden blocks this) and **Arg306** (secondary; protein S-dependent) → destruction of FVa → disassembly of prothrombinase complex (FXa + FVa + phospholipid + Ca²⁺) → cessation of thrombin generation
2. **APC cleaves FVIIIa at Arg336** (and Arg562) → destruction of FVIIIa → disassembly of tenase complex → cessation of FXa generation
3. **Net effect:** APC simultaneously dismantles both the tenase and prothrombinase complexes → thrombin generation stops → self-limiting clot

**Factor V Leiden pathophysiology:**
- FV Leiden (R506Q) → FVa resistant to cleavage at Arg506 by APC; only the Arg306 site (protein S–dependent) remains susceptible
- Result: FVa is 10-20× more stable in the presence of APC → prolonged prothrombinase activity → persistent thrombin generation → VTE risk
- FV Leiden also impairs FV's normal APC co-factor function (in inactivating FVIIIa) → further loss of anticoagulant activity
- APC resistance is tested by: APC-resistance ratio (clotting assay) or, more specifically, DNA-based genotyping of the G1691A (R506Q) mutation

### Cytoprotective effects of APC

Beyond anticoagulation, APC has **direct cellular effects** mediated through EPCR-coupled PAR-1 signaling:
- **Endothelial barrier protection:** APC → Rac1/Cdc42 → VE-cadherin stabilization → reduces vascular permeability (anti-edema)
- **Anti-inflammatory:** Inhibits NF-κB → ↓TNF/IL-6/IL-8 → reduced leukocyte adhesion and transmigration
- **Anti-apoptotic:** PI3K/Akt → Bcl-2 → endothelial and neuronal survival
- **Anti-thrombotic (indirect):** ↓PAI-1 → promotes fibrinolysis

These effects provided the rationale for **drotrecogin alfa (recombinant human APC)** in severe sepsis. The PROWESS trial showed initial mortality benefit (2001), but PROWESS-SHOCK trial (2011, 1697 patients) showed no mortality benefit in septic shock → drotrecogin alfa was withdrawn from the market in 2011. The failure underscores the complexity of the cytoprotective vs. anticoagulant balance of APC in sepsis.

## Mechanism

### Warfarin initiation — the protein C paradox

**Warfarin-induced skin necrosis:**
1. Warfarin inhibits VKORC1 → reduced vitamin K recycling → impaired γ-carboxylation of all vitamin K-dependent proteins
2. **Protein C has the shortest half-life** (~8h) among vitamin K-dependent proteins (factor VII: 6h; factor IX: 24h; factor X: 36h; factor II: 60h)
3. Rapid warfarin initiation → protein C drops immediately → pro-coagulant factors still functional (longer half-lives) → **transient hypercoagulable state on day 2-4 of warfarin** → dermal vessel thrombosis → skin necrosis (especially breast, abdomen, thigh, buttocks)
4. **Prevention:** Overlap warfarin with parenteral anticoagulation (heparin, LMWH) for ≥5 days and until INR is therapeutic for ≥2 consecutive days; slower warfarin initiation
5. **Highest risk:** Protein C or S-deficient patients; hereditary PC deficiency patients starting warfarin without heparin bridge

### Neonatal purpura fulminans

**Homozygous/compound heterozygous protein C deficiency** is rare (~1:500,000 to 1:1,000,000) but presents at birth (within hours to days) with:
- Disseminated microvascular thrombosis → purpura fulminans (skin infarction), DIC, ophthalmologic thrombosis (blindness), CNS thrombosis
- Requires **immediate protein C concentrate (Ceprotin)** IV + fresh frozen plasma → lifelong anticoagulation (LMWH + protein C concentrate for acute episodes)
- Without treatment: rapidly fatal

### Clinical testing

| Test | Purpose | Caveats |
|:-----|:--------|:--------|
| Protein C antigen (ELISA) | Detects type I (low) vs. type II (normal) | Acute phase protein; slightly rises in inflammation |
| Protein C activity (functional) | Detects both type I and II deficiency | Must NOT test during acute thrombosis or while on anticoagulation (falsely low) |
| Genetic testing (PROC sequencing) | Confirms mutations | Best done when off anticoagulation; tests family members |
| APC resistance ratio | Screen for FV Leiden | Replaced by DNA genotyping for R506Q (more specific) |
| FV Leiden genotype (PCR) | G1691A (R506Q) | Gold standard; test unaffected by anticoagulation |

## Connections

- `connects-to` → **[Inherited Thrombophilia](../../07-system/inherited-thrombophilia/README.md)** — Protein C deficiency (PROC mutations) is one of the 5 major inherited thrombophilias alongside FV Leiden, prothrombin G20210A, protein S deficiency, and AT deficiency; type I = low antigen + activity; type II = low activity with normal antigen; 5-10× VTE risk in heterozygotes.
- `connects-to` → **[Thrombin](../thrombin/README.md)** — Thrombin bound to endothelial thrombomodulin cleaves protein C activation peptide → APC; high thrombin paradoxically activates the anticoagulant pathway; thrombin-thrombomodulin also activates TAFI (thrombin-activatable fibrinolysis inhibitor) → fibrin protection from lysis.
- `connects-to` → **[Venous Thromboembolism](../../07-system/venous-thromboembolism/README.md)** — Protein C deficiency → 5-10× VTE risk (heterozygous) vs. 50-100× (rare homozygous → neonatal purpura fulminans); warfarin-induced skin necrosis from rapid protein C drop at warfarin initiation; APC is consumed in sepsis-DIC → purpura fulminans in acquired PC deficiency.

[^dahlback-2008-protein-c-review]: Dahlbäck B. Advances in understanding pathogenic mechanisms of thrombophilic disorders. *Blood.* 2008;112(1):19-27. [doi:10.1182/blood-2008-01-077909](https://doi.org/10.1182/blood-2008-01-077909) · [PubMed 18574048](https://pubmed.ncbi.nlm.nih.gov/18574048/)
[^bertina-1994-factor-v-leiden]: Bertina RM, Koeleman BP, Koster T, et al. Mutation in blood coagulation factor V associated with resistance to activated protein C. *Nature.* 1994;369(6475):64-67. [doi:10.1038/369064a0](https://doi.org/10.1038/369064a0) · [PubMed 8164741](https://pubmed.ncbi.nlm.nih.gov/8164741/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
