---
schema: medicine-entry/v1
id: warfarin
name: Warfarin
atlas: 03-medicine
scale: 01-modern
status: draft
last_reviewed: 2026-06-06
summary: "Vitamin K antagonist anticoagulant; inhibits VKORC1 → depletes γ-carboxylated clotting factors II, VII, IX, X. Narrow therapeutic index (INR 2–3); major food/drug interactions via CYP2C9/VKORC1. Cornerstone of AF stroke prevention for 60+ years."
aliases: ["warfarin", "Coumadin", "Jantoven", "Marevan", "(RS)-4-hydroxy-3-(3-oxo-1-phenylbutyl)-2H-chromen-2-one"]
sources:
  - id: link-1943-warfarin-discovery
    type: peer-reviewed
    cite: "Link KP. The discovery of dicumarol and its sequels. Circulation. 1959;19(1):97-107."
    doi: "10.1161/01.CIR.19.1.97"
    pmid: "13619027"
    url: "https://doi.org/10.1161/01.CIR.19.1.97"
  - id: connolly-2009-re-ly
    type: peer-reviewed
    cite: "Connolly SJ, Ezekowitz MD, Yusuf S, et al. Dabigatran versus warfarin in patients with atrial fibrillation. N Engl J Med. 2009;361(12):1139-51."
    doi: "10.1056/NEJMoa0905561"
    pmid: "19717844"
    url: "https://doi.org/10.1056/NEJMoa0905561"
  - id: hart-2007-warfarin-af-meta
    type: peer-reviewed
    cite: "Hart RG, Pearce LA, Aguilar MI. Meta-analysis: antithrombotic therapy to prevent stroke in patients who have nonvalvular atrial fibrillation. Ann Intern Med. 2007;146(12):857-67."
    doi: "10.7326/0003-4819-146-12-200706190-00007"
    pmid: "17577005"
    url: "https://doi.org/10.7326/0003-4819-146-12-200706190-00007"
  - id: johnson-2011-warfarin-pharmacogenomics
    type: peer-reviewed
    cite: "Johnson JA, Gong L, Whirl-Carrillo M, et al. Clinical pharmacogenomics implementation consortium guidelines for CYP2C9 and VKORC1 genotypes and warfarin dosing. Clin Pharmacol Ther. 2011;90(4):625-9."
    doi: "10.1038/clpt.2011.185"
    pmid: "21900891"
    url: "https://doi.org/10.1038/clpt.2011.185"
cross_links:
  - target: 01-human/03-molecular/coagulation-cascade
    relation: modulates
    evidence: hart-2007-warfarin-af-meta
    note: "Warfarin depletes γ-carboxylated forms of factors II (prothrombin), VII, IX, X and anticoagulant proteins C and S by blocking VKORC1 — preventing vitamin K recycling required for γ-glutamyl carboxylase activity in the liver."
  - target: 01-human/06-organ/liver
    relation: targets
    note: "Liver is the primary site of warfarin action — hepatic γ-glutamyl carboxylase and VKORC1 are the molecular targets; CYP2C9 in liver microsomes is the major metabolizing enzyme."
---

# Warfarin

## Overview

**Warfarin** (Coumadin) is the archetypal **vitamin K antagonist (VKA)** anticoagulant and has been the dominant oral anticoagulant for over 60 years. Originally developed as a rodenticide (derived from dicumarol, the compound responsible for sweet clover disease — a hemorrhagic diathesis in cattle eating spoiled sweet clover hay), warfarin entered human medicine in the 1950s and rapidly became the standard of care for stroke prevention in atrial fibrillation, venous thromboembolism (VTE) treatment, and thromboprophylaxis in prosthetic heart valves [^link-1943-warfarin-discovery].

Its narrow therapeutic index, complex drug and food interactions, and the requirement for regular INR monitoring define warfarin's use — and explain the appeal of the direct oral anticoagulants (DOACs) that have superseded it for most non-valvular AF and VTE indications since 2009.

## Mechanism

**Vitamin K cycle and VKORC1:**
1. **Vitamin K function:** Dietary vitamin K (phylloquinone, K1) and bacterially synthesized menaquinone (K2) are required cofactors for **γ-glutamyl carboxylase (GGCX)** — an enzyme in the endoplasmic reticulum of hepatocytes that adds a carboxyl group to specific glutamate residues on vitamin K-dependent clotting factors (II, VII, IX, X) and anticoagulant proteins (C, S, Z)
2. **γ-carboxylation:** Glutamate residues in the Gla domain of clotting factors are converted to γ-carboxyglutamate (Gla) residues — this allows the proteins to bind Ca²⁺ and thereby bind phospholipid surfaces (platelet membrane) — **essential for factor activation in the coagulation cascade**
3. **VKORC1 (Vitamin K epoxide reductase complex subunit 1):** During γ-carboxylation, vitamin K hydroquinone (KH₂) is oxidized to vitamin K epoxide (KO). VKORC1 reduces KO back to KH₂ — **recycling vitamin K**. Without VKORC1 activity, vitamin K stores are rapidly depleted
4. **Warfarin mechanism:** Warfarin competitively inhibits VKORC1 → vitamin K epoxide accumulates → vitamin K hydroquinone levels fall → GGCX cannot carboxylate new clotting factor molecules → **production of non-functional (des-γ-carboxylated) clotting factors** (also called PIVKA — Proteins Induced by Vitamin K Absence)

**Onset of anticoagulation:**
- Factors already in circulation remain functional — anticoagulant effect requires synthesis of new, non-functional factors
- Factor VII (shortest half-life, ~6h): INR begins rising within 12–24h
- Full anticoagulant effect (factors II, IX, X): 3–5 days
- This explains why bridging anticoagulation (LMWH) is required if rapid anticoagulation is needed

**Metabolism — CYP2C9 and pharmacogenomics:**
- S-warfarin (4× more potent than R-warfarin) is primarily metabolized by **CYP2C9**
- **CYP2C9*2 and *2C9*3** variants (reduced function) → substantially higher warfarin concentrations → increased bleeding risk; require lower doses
- **VKORC1 -1639G>A (rs9923231):** The A allele reduces VKORC1 expression → greater sensitivity to warfarin → require lower doses
- Together, CYP2C9 and VKORC1 variants explain ~40–50% of warfarin dose variability; FDA recommends pharmacogenomic testing (CPIC guidelines available) [^johnson-2011-warfarin-pharmacogenomics]

## Clinical Use

**Indications:**
- **Non-valvular atrial fibrillation:** Stroke prevention; target INR 2.0–3.0; 64% relative risk reduction in stroke (meta-analysis) [^hart-2007-warfarin-af-meta]; largely superseded by DOACs but still used in resource-limited settings
- **VTE (DVT/PE) treatment:** INR 2.0–3.0; 3–6 months for provoked; indefinite for unprovoked or high-risk
- **Mechanical prosthetic heart valves:** INR 2.5–3.5; DOACs are contraindicated in mechanical valves — only indication where warfarin remains preferred
- **Antiphospholipid syndrome with thrombosis:** INR 2.0–3.0 (or 3.0–4.0 for high-risk triple-positive); DOACs inferior in this setting

**Dosing:**
- Highly variable — typical maintenance dose 2–10 mg/day (mean ~5 mg)
- Initiation: 5 mg loading day 1–2, then titrate by INR
- Elderly/debilitated/CYP2C9 poor metabolizers/high sensitivity VKORC1: start 2–2.5 mg
- Genetic dosing algorithms (Warfarin Dosing Service, CPIC) improve time-in-therapeutic-range

**Monitoring:**
- INR (International Normalized Ratio): standardized PT ratio; target 2.0–3.0 for most indications
- Monitor weekly during initiation, then monthly when stable

**Major drug interactions:**
- **Enhances anticoagulation (↑ INR, ↑ bleeding risk):** Amiodarone (CYP2C9 inhibition), fluconazole/azole antifungals (CYP2C9 inhibition), metronidazole, cotrimoxazole, aspirin/NSAIDs (GI mucosal injury + antiplatelet), clarithromycin
- **Reduces anticoagulation (↓ INR):** Rifampicin (potent CYP2C9 inducer), carbamazepine, St. John's Wort; increased dietary vitamin K (green leafy vegetables)

**Bleeding reversal:**
- Hold warfarin + vitamin K1 (phytomenadione) for non-major/minor elevation
- Major bleeding: 4-factor PCC (prothrombin complex concentrate) + IV vitamin K — immediate reversal

## Evidence

| Trial / Review | Key Finding |
|:---|:---|
| Meta-analysis AF stroke prevention (Hart 2007) [^hart-2007-warfarin-af-meta] | Warfarin reduces stroke by 64% in AF; aspirin reduces stroke by 22%; warfarin clearly superior in high-risk patients (CHA₂DS₂-VASc ≥2) |
| RE-LY (Connolly 2009) [^connolly-2009-re-ly] | Dabigatran 150 mg BD: 34% relative RRR in stroke vs. warfarin; dabigatran 110 mg BD non-inferior; both with lower intracranial hemorrhage (ICH). Pivotal trial that launched the DOAC era |
| ARISTOTLE, ROCKET-AF, ENGAGE AF | Apixaban, rivaroxaban, edoxaban all non-inferior or superior to warfarin in stroke prevention with less major bleeding; ICH consistently lower with DOACs |
| Pharmacogenomics RCTs (EU-PACT, COAG) | Genotype-guided warfarin dosing: EU-PACT improved time-in-therapeutic-range; COAG showed no benefit over clinical algorithm in mixed-ancestry population — pharmacogenomics most useful in European/Asian ancestry |

## Connections

- **Modulates** → [Coagulation Cascade](../../../../../01-human/03-molecular/coagulation-cascade/README.md): Inhibits VKORC1 → depletes functional (γ-carboxylated) factors II, VII, IX, X → both intrinsic and extrinsic pathways impaired; anticoagulant proteins C and S also depleted (transient pro-thrombotic risk at initiation).
- **Targets** → [Liver](../../../../../01-human/06-organ/liver/README.md): VKORC1 and CYP2C9 in hepatocytes are the primary molecular targets and metabolic enzymes; hepatic synthetic function drives all drug interactions.
