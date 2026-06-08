---
schema: human-scale-entry/v1
id: fibrinogen
name: Fibrinogen
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-05
summary: "340 kDa plasma glycoprotein (hexamer [AαBβγ]₂); synthesised by hepatocytes at 2–4 g/L. Thrombin cleaves fibrinopeptides A and B → fibrin → crosslinked clot (FXIIIa). Positive acute-phase reactant; elevated fibrinogen is an independent CVD risk factor."
aliases: ["factor I", "fibrin", "Fg", "fibrin monomer", "fibrin clot"]
sources:
  - id: stryer-biochemistry
    type: textbook
    cite: "Berg JM, Tymoczko JL, Stryer L. Biochemistry. 9th ed. W.H. Freeman; 2019."
    url: "https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X"
    accessed: "2026-06-05"
  - id: janeway-immunobiology
    type: textbook
    cite: "Murphy K, Weaver C. Janeway's Immunobiology. 9th ed. Garland Science; 2017."
    url: "https://www.garlandscience.com/product/isbn/9780815345053"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/04-cellular/hepatocyte
    relation: expresses
    note: "Fibrinogen hexamer (Aα/Bβ/γ chains) is synthesised exclusively by hepatocytes at ~2 g/day; upregulated 3–5× during the acute-phase response via IL-6/STAT3. Serum fibrinogen is a surrogate marker of hepatic synthetic function."
  - target: 01-human/07-system/cardiovascular-system
    relation: modulates
    note: "Fibrinogen is the terminal coagulation cascade step (thrombin→fibrin + platelet binding via αIIbβ3); elevated fibrinogen is an independent CVD risk factor; fibrin clot density determines thrombotic vs haemorrhagic risk balance."
  - target: 01-human/04-cellular/platelet
    relation: modulates
    note: "Fibrinogen/fibrin bridges platelets via αIIbβ3 (GPIIb/IIIa) integrin — RGD on Aα chain + γ-chain C-terminal AGDV dodecapeptide; the platelet-fibrin scaffold forms the definitive haemostatic plug at sites of vascular injury."
  - target: 01-human/07-system/disseminated-intravascular-coagulation
    relation: connects-to
    note: "Fibrinogen is consumed in DIC by uncontrolled thrombin generation (sepsis, obstetric catastrophe, malignancy); fibrinogen <1.5 g/L in DIC is both diagnostic and a trigger for cryoprecipitate replacement; D-dimer from fibrin cross-links confirms active fibrinolysis in DIC."
---

# Fibrinogen

## Overview

Fibrinogen (coagulation factor I) is the largest soluble plasma glycoprotein and the terminal substrate of the coagulation cascade. At a normal plasma concentration of **2–4 g/L** (half-life ~4 days), it represents one of the most abundant plasma proteins. Fibrinogen is synthesized exclusively by **hepatocytes** and is a **positive acute-phase reactant**: its concentration rises 3–5-fold during acute inflammation, driven predominantly by IL-6 signaling to hepatic STAT3 [^stryer-biochemistry].

The critical physiological role of fibrinogen is the formation of a **fibrin clot**. Thrombin (factor IIa), itself the product of the coagulation cascade, cleaves fibrinopeptides from fibrinogen to generate fibrin monomers that spontaneously polymerize into a viscoelastic gel — the structural scaffold of the haemostatic plug. Factor XIIIa (transglutaminase) then covalently crosslinks adjacent fibrin chains, creating a clot that is mechanically robust and resistant to fibrinolysis [^stryer-biochemistry].

Beyond haemostasis, fibrinogen is a significant **cardiovascular risk marker**: the Northwick Park Heart Study identified plasma fibrinogen as one of the top three independent predictors of myocardial infarction alongside LDL-C and cigarette smoking. This association reflects both thrombotic (pro-coagulant) and rheological (↑blood viscosity, ↑erythrocyte aggregation) effects [^janeway-immunobiology].

## Structure

### Trinodular hexamer

Fibrinogen has a characteristic **trinodular** architecture visible by electron microscopy:

- **Two distal D-domains** (outer nodules) — each composed of the C-terminal regions of one Bβ and one γ chain, with the βC and γC modules containing the fibrin polymerization sites
- **Central E-domain** (inner nodule) — contains the N-termini of all 6 chains joined by a **disulfide ring** (the N-terminal disulfide knot, NDK); fibrinopeptides A and B are located in the E-domain

### Chain composition

| Chain | Gene | MW | Key features |
|:---|:---|:---|:---|
| **Aα** | *FGA* | ~95 kDa | Fibrinopeptide A (16 aa) at N-terminus; RGD sequence (platelet αIIbβ3 binding) |
| **Bβ** | *FGB* | ~55 kDa | Fibrinopeptide B (14 aa) at N-terminus; cleaved second by thrombin |
| **γ** | *FGG* | ~47 kDa | C-terminal AGDV dodecapeptide (platelet αIIbβ3); Lys406/Gln398-407 (FXIIIa crosslink sites for γ-γ dimer) |

The two halves of the hexamer ([AαBβγ]₂) are connected by coiled-coil domains running between the E and D nodules. The total molecular weight of the glycosylated hexamer is ~340 kDa.

### Fibrin polymerization sites

After thrombin cleavage, fibrin polymerization is driven by three complementary knob-hole interactions:
- **Knob A** (exposed in Aα after FpA removal) fits into **hole a** in the γC domain of an adjacent molecule
- **Knob B** (exposed in Bβ after FpB removal) fits into **hole b** in the βC domain
- **D:D interface** (γ-module contacts) — lateral association of protofibrils

## Function

### Coagulation cascade endpoint

Fibrinogen is the soluble precursor that is converted to insoluble **fibrin** at the final step of both the intrinsic (contact activation) and extrinsic (tissue factor) coagulation pathways. It is the structural material of blood clots rather than an enzymatic participant in the cascade itself [^stryer-biochemistry].

### Platelet scaffold

Fibrinogen/fibrin provides the molecular bridges between activated platelets:
- **Soluble fibrinogen** binds activated αIIbβ3 (GPIIb/IIIa) on two adjacent activated platelets → platelet aggregation (primary platelet plug)
- **Fibrin polymer** binds αIIbβ3 → outside-in signaling → platelet spreading, clot retraction, and further stabilization of the haemostatic plug

### Acute-phase protein

During systemic inflammation (infection, surgery, trauma, autoimmune disease), hepatic fibrinogen synthesis rises 3–5-fold [^janeway-immunobiology]:
- **Driver**: IL-6 → gp130/JAK1 → STAT3 → binds STAT3-response elements in *FGA*, *FGB*, *FGG* promoters
- **Result**: ↑plasma fibrinogen → ↑ESR (erythrocyte sedimentation rate, a clinical surrogate of acute-phase response), ↑blood viscosity, ↑thrombotic risk

### Cardiovascular risk

Elevated fibrinogen (>3.5 g/L) is associated with increased risk of:
- Myocardial infarction (independent of LDL-C; Northwick Park Heart Study)
- Ischaemic stroke
- Peripheral arterial disease

The mechanism is multifactorial: pro-coagulant (fibrin clot formation), pro-inflammatory (fibrinogen fragments activate leukocytes via Mac-1/CR3), and rheological (elevated fibrinogen → ↑erythrocyte aggregation → ↑blood viscosity → ↑shear stress on endothelium).

## Mechanism

### Thrombin cleavage and fibrin polymerization

The conversion of fibrinogen to fibrin proceeds in three steps [^stryer-biochemistry]:

1. **Thrombin cleaves fibrinopeptide A (FpA)** from the Aα chain (Arg16-Gly17 bond) → exposure of knob A → rapid (seconds) end-to-middle polymerization (D:E interactions) → fibrin protofibrils (half-staggered, double-stranded)
2. **Thrombin cleaves fibrinopeptide B (FpB)** from the Bβ chain (slower) → exposure of knob B → lateral association of protofibrils → thicker fibres and branching → fibrin gel
3. **Factor XIIIa crosslinking**: Thrombin + Ca²⁺ activates factor XIII (transglutaminase) → FXIIIa:
   - **γ-γ crosslinks**: isopeptide bond between Lys406 of one γ-chain and Gln398/399 of another → γ-γ dimer (extremely rapid, minutes)
   - **α-chain crosslinks**: multiple Lys-Gln isopeptide bonds between Aα chains → high-molecular-weight α-polymer (slower, hours)
   - **α₂-antiplasmin incorporation**: FXIIIa also crosslinks α₂-antiplasmin and fibronectin into clot → resistance to fibrinolysis

### Fibrinolysis

The clot is resolved by the fibrinolytic system:
1. **tPA** (tissue plasminogen activator, released by endothelium) and **uPA** (urokinase) convert **plasminogen → plasmin**
2. Plasmin cleaves fibrin at Lys and Arg residues → **fibrin degradation products (FDPs)**
3. The γ-γ crosslinked D-D fragment (**D-dimer**) is specific for plasmin action on crosslinked fibrin — not fibrinogen itself — making it a diagnostic marker for active fibrinolysis (DVT/PE/DIC when elevated)
4. **α₂-antiplasmin** rapidly neutralizes free plasmin (half-life in plasma ~0.1 s)
5. **PAI-1** (plasminogen activator inhibitor-1) inhibits tPA/uPA; elevated in obesity, insulin resistance, and metabolic syndrome → hypofibrinolytic state → thrombotic risk

### Fibrin clot architecture determinants

Clot structural properties depend on polymerization kinetics:
- **Coarse fibrin** (thick fibres, open porous network): formed at low thrombin concentrations, low ionic strength → more permeable, easier to lyse (physiological haemostatic clots)
- **Fine fibrin** (thin fibres, dense network): formed at high fibrinogen concentrations, elevated thrombin, DM/CVD context → denser, less permeable, more resistant to fibrinolysis → higher thrombotic risk

## Connections

- `expresses` → **[hepatocyte](../../04-cellular/hepatocyte/README.md)** — sole site of fibrinogen synthesis; all three chains (Aα, Bβ, γ) are made by hepatocytes and upregulated 3–5× during acute-phase response via IL-6/STAT3 [^stryer-biochemistry]
- `modulates` → **[cardiovascular-system](../../07-system/cardiovascular-system/README.md)** — fibrin mesh is the definitive haemostatic scaffold; elevated fibrinogen drives CVD risk via thrombotic, rheological, and inflammatory mechanisms [^stryer-biochemistry]
- `modulates` → **[platelet](../../04-cellular/platelet/README.md)** — fibrinogen/fibrin bridges adjacent platelets via αIIbβ3 (RGD on Aα and AGDV on γ-chain); platelet-fibrin scaffold forms the definitive haemostatic plug [^stryer-biochemistry]
- `connects-to` → **[Disseminated Intravascular Coagulation](../../07-system/disseminated-intravascular-coagulation/README.md)** — Fibrinogen is consumed in DIC by uncontrolled thrombin generation (sepsis, obstetric catastrophe, malignancy); fibrinogen <1.5 g/L in DIC is diagnostic and triggers cryoprecipitate replacement; D-dimer from fibrin cross-links confirms active fibrinolysis in DIC.

## Pathology

| Condition | Mechanism | Clinical features |
|:---|:---|:---|
| **Afibrinogenaemia** | Autosomal recessive; null mutations in *FGA*, *FGB*, or *FGG* → no fibrinogen | Severe bleeding from birth (umbilical cord, circumcision), haemarthroses; paradoxically also thrombosis |
| **Hypofibrinogenaemia** | Heterozygous loss-of-function mutations; fibrinogen <1.5 g/L | Mild-moderate bleeding tendency; often asymptomatic |
| **Dysfibrinogenaemia** | Structural variants → poor polymerization (bleeding) or fibrinolysis resistance (thrombosis); >700 variants described | Fibrinogen antigen normal but functional assay (Clauss) reduced; PT/APTT may be prolonged |
| **Disseminated intravascular coagulation (DIC)** | Systemic thrombin generation → fibrinogen consumption → ↓fibrinogen + ↑D-dimer; sepsis, obstetric catastrophe, malignancy | Diffuse microvascular thrombosis + haemorrhage; treat underlying cause; FFP + cryoprecipitate |
| **Venous thromboembolism (DVT/PE)** | Fibrin-rich "red thrombus" (Virchow triad: stasis, hypercoagulability, endothelial injury) | Anticoagulation (LMWH, DOACs); D-dimer screening test |
| **Elevated fibrinogen / CVD risk** | ↑Plasma fibrinogen → ↑viscosity, ↑thrombotic potential, ↑platelet reactivity; fibrinogen fragments activate leukocyte Mac-1 | Independent MI risk predictor; addressed via statins (modest fibrinogen reduction), lifestyle, treatment of inflammation |
| **Hyperfibrinogenaemia in inflammation** | Acute-phase response → fibrinogen 3–5× → ↑ESR (classic marker); chronic elevation in RA, IBD, malignancy | Treat underlying inflammatory disease |

## See Also

- [Hemoglobin](../hemoglobin/README.md) — another major blood protein; erythrocyte aggregation in high-fibrinogen states raises ESR
- [IL-6](../il-6/README.md) — primary driver of fibrinogen upregulation during acute-phase response
- [STAT3](../stat3/README.md) — transcription factor through which IL-6 activates fibrinogen gene expression in hepatocytes
- [Cardiovascular system](../../07-system/cardiovascular-system/README.md) — organ system context for haemostasis and thrombosis
- [Hepatic lobule](../../05-tissue/hepatic-lobule/README.md) — tissue context for hepatocyte fibrinogen synthesis
- [ACE inhibitors](../../../03-medicine/01-modern/04-cardio/ace-inhibitors/README.md) — anticoagulation-adjacent therapies reducing CVD risk

[^stryer-biochemistry]: Berg JM, Tymoczko JL, Stryer L. *Biochemistry.* 9th ed. W.H. Freeman; 2019. [Macmillan Learning](https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X)
[^janeway-immunobiology]: Murphy K, Weaver C. *Janeway's Immunobiology.* 9th ed. Garland Science; 2017. [Garland Science](https://www.garlandscience.com/product/isbn/9780815345053)
