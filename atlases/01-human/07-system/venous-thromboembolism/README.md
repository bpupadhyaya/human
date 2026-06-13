---
schema: human-scale-entry/v1
id: venous-thromboembolism
name: Venous Thromboembolism
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Venous thromboembolism (VTE; DVT + PE) affects ~1-2 per 1,000 adults/year; Virchow's triad (stasis, hypercoagulability, endothelial injury) drives pathogenesis. DOACs (apixaban, rivaroxaban) are first-line; catheter-directed thrombolysis and ECMO for massive PE."
aliases: ["VTE", "venous thromboembolism", "DVT", "deep vein thrombosis", "PE", "pulmonary embolism", "deep venous thrombosis", "thrombosis venous", "venous clot"]
sources:
  - id: agnelli-2013-amplify-apixaban-vte
    type: peer-reviewed
    cite: "Agnelli G, Buller HR, Cohen A, et al. Oral apixaban for the treatment of acute venous thromboembolism. N Engl J Med. 2013;369(9):799-808."
    doi: "10.1056/NEJMoa1302507"
    pmid: "23808982"
    url: "https://doi.org/10.1056/NEJMoa1302507"
  - id: bauersachs-2010-einstein-rivaroxaban
    type: peer-reviewed
    cite: "EINSTEIN Investigators. Oral rivaroxaban for symptomatic venous thromboembolism. N Engl J Med. 2010;363(26):2499-2510."
    doi: "10.1056/NEJMoa1007903"
    pmid: "21128814"
    url: "https://doi.org/10.1056/NEJMoa1007903"
  - id: konstantinides-2020-esc-pe
    type: peer-reviewed
    cite: "Konstantinides SV, Meyer G, Becattini C, et al. 2019 ESC Guidelines for the diagnosis and management of acute pulmonary embolism. Eur Heart J. 2020;41(4):543-603."
    doi: "10.1093/eurheartj/ehz405"
    pmid: "31504429"
    url: "https://doi.org/10.1093/eurheartj/ehz405"
cross_links:
  - target: 01-human/03-molecular/thrombin
    relation: connects-to
    note: "Thrombin (FIIa) generates fibrin at the core of venous thrombi; stasis → contact activation → FXI → FIXa → FX → thrombin → fibrin-rich clot; DOACs (dabigatran, rivaroxaban, apixaban) target thrombin or FXa → prevent and treat VTE; LMWH inhibits thrombin via antithrombin."
  - target: 01-human/07-system/antiphospholipid-syndrome
    relation: connects-to
    note: "APS causes recurrent DVT/PE in young adults; triple-positive aPL (LA + aCL + anti-B2GPI) confers >10% annual thrombotic risk; warfarin INR 2-3 is superior to DOACs for VTE in APS; rivaroxaban doubled arterial event risk in triple-positive APS (TRAPS trial)."
  - target: 01-human/03-molecular/von-willebrand-factor
    relation: connects-to
    note: "Elevated VWF promotes venous thrombosis by augmenting platelet recruitment and fibrin network formation; VWF is an acute-phase protein elevated in surgery, infection, cancer → increased VTE risk; ABO blood group affects VWF level (type O ~25% lower VWF → lower baseline VTE risk)."
  - target: 01-human/03-molecular/protein-c
    relation: connects-to
    note: "Protein C deficiency (PROC mutations) is a rare but high-risk inherited thrombophilia (0.3% prevalence; 5-10× VTE risk); APC inactivates FVa/FVIIIa; warfarin-induced skin necrosis is uniquely dangerous in protein C-deficient patients starting warfarin without heparin bridge."
  - target: 01-human/07-system/inherited-thrombophilia
    relation: connects-to
    note: "Inherited thrombophilia testing guides anticoagulation duration in VTE: FV Leiden and prothrombin G20210A heterozygotes require 3-6 months for first provoked VTE; high-risk deficiencies (AT, protein C/S) or recurrent unprovoked VTE → indefinite anticoagulation."
  - target: 01-human/07-system/heparin-induced-thrombocytopenia
    relation: connects-to
    note: "HIT causes paradoxical DVT/PE (venous) and arterial thrombosis (HITT); occurs 5-10 days after heparin exposure; anti-PF4/heparin IgG → platelet activation → thrombin; argatroban, bivalirudin, and fondaparinux replace heparin in HIT; DOACs used for bridging to warfarin."
  - target: 01-human/03-molecular/antithrombin
    relation: connects-to
    note: "Antithrombin deficiency (SERPINC1 mutations; 1:2,000-5,000) is the most severe inherited thrombophilia (25-50× lifetime VTE risk); UFH/LMWH efficacy requires AT → AT-deficient patients may need AT concentrate; functional AT assay needed for diagnosis."
  - target: 01-human/07-system/hemophilia-a
    relation: connects-to
    note: "Severe HA (FVIII <1%) confers significant VTE protection; historical VTE rate in HA ~0.5/1000 PY vs. ~1.5-3/1000 general population; emicizumab reconstitutes intrinsic tenase; avoid high-dose APCC with emicizumab → TMA; gene therapy raising FVIII >150% increases VTE risk."
  - target: 03-medicine/01-modern/09-hematology/warfarin
    relation: treated-by
    note: "Warfarin treats DVT/PE at INR 2.0–3.0 × 3–6 months for provoked VTE; indefinite for unprovoked high-risk; largely superseded by DOACs for most VTE; remains first-line for antiphospholipid syndrome; LMWH bridging required at initiation."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Endothelial injury is one arm of Virchow's triad driving VTE: damaged endothelium loses its antithrombotic surface (thrombomodulin, heparan sulfate) and exposes tissue factor and von Willebrand factor, nucleating clot—why surgery, inflammation and indwelling lines provoke it."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "The lung is where venous thromboembolism turns deadly: a deep-vein thrombus that breaks loose lodges in the pulmonary arteries as a pulmonary embolism, causing hypoxia, acute right-heart strain and sudden death; CT angiography diagnoses it and large clots may need thrombolysis."
  - target: 01-human/07-system/sickle-cell-disease
    relation: connects-to
    note: "Sickle cell disease is a strong, often overlooked VTE risk factor: chronic hemolysis, phosphatidylserine exposure and inflammation create a hypercoagulable state, so VTE and pulmonary embolism rates are markedly raised, overlapping with in-situ pulmonary vaso-occlusion."
  - target: 01-human/07-system/polycythemia-vera
    relation: connects-to
    note: "Polycythemia vera is a major acquired cause of venous thromboembolism: high hematocrit and JAK2-mutant prothrombotic blood drive clots, including splanchnic-vein thromboses (Budd-Chiari, portal vein) that can be the first sign—so unusual-site VTE prompts JAK2 testing."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "Cancer is a leading cause of venous thromboembolism, and pancreatic cancer is the classic high-risk tumor (Trousseau syndrome): mucin and tissue factor make the blood intensely prothrombotic, so migratory or unprovoked VTE can be the presenting clue to an occult malignancy."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "COVID-19 dramatically raises venous thromboembolism risk: SARS-CoV-2 endothelial injury and intense inflammation drive immunothrombosis, so hospitalized patients develop DVT and pulmonary embolism at high rates and receive thromboprophylaxis, with D-dimer marking severity."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Platelets help build venous thrombi: though VTE is a fibrin-rich red clot, activated platelets still seed and propagate it, which is why some antiplatelet therapy reduces recurrence—blurring the old line between arterial and venous clots."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Estrogen is a leading reversible cause of VTE: oral contraceptives, hormone therapy and pregnancy raise clotting factors and lower anticoagulant proteins, multiplying thrombosis risk—especially when combined with factor V Leiden or other inherited thrombophilias."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Obesity steadily raises VTE risk: adipose-driven inflammation, higher clotting factors and venous stasis from immobility combine to promote thrombosis, so weight is an independent, modifiable risk factor that compounds surgery, pregnancy and hormonal triggers."
---

# Venous Thromboembolism

## Overview

**Venous thromboembolism (VTE)** is the collective term for **deep vein thrombosis (DVT)** — thrombosis in the proximal or distal veins of the leg (or upper extremity) — and **pulmonary embolism (PE)** — occlusion of the pulmonary arterial tree by thrombus, typically originating from DVT. They represent a single disease on a pathophysiological spectrum: ~50% of proximal DVTs embolize to the pulmonary circulation [^konstantinides-2020-esc-pe].

**Epidemiology:**
- Incidence: ~1-2 per 1,000 adults per year in the general population; third most common cardiovascular disease after MI and stroke
- Recurrence: ~30% within 5-10 years after stopping anticoagulation
- Mortality: Massive PE (hemodynamic instability) → ~15-30% in-hospital mortality; untreated proximal DVT → ~15-25% risk of symptomatic PE; fatal PE risk ~0.2-0.5% with anticoagulation

**Virchow's Triad** (1856) — three interacting mechanisms:
1. **Venous stasis:** Reduced blood flow (immobilization, heart failure, air travel, varicose veins) → thrombin accumulation, activated clotting factor pooling
2. **Hypercoagulability:** Inherited thrombophilias (Factor V Leiden, prothrombin G20210A, protein C/S deficiency, antithrombin deficiency, APS) or acquired (cancer, pregnancy, OCP, HRT, inflammation)
3. **Endothelial injury:** Surgery, central venous catheters, trauma → exposed subendothelial TF → FVIIa/TF → extrinsic pathway activation → thrombin → fibrin

## Structure

### Classification of DVT

**By location:**
- **Proximal DVT** (popliteal, femoral, iliac veins): Higher risk of PE; anticoagulation mandatory
- **Distal DVT** (calf veins, tibial, peroneal): Controversial management; higher rate of spontaneous resolution; ~15-20% propagate to proximal if untreated; treat if symptomatic or if PE risk is high
- **Upper extremity DVT:** Effort thrombosis (Paget-Schroetter; subclavian vein; thoracic outlet syndrome) vs. catheter-related; treat with anticoagulation; thrombolysis for effort thrombosis

**By provocation:**
- **Provoked VTE:** Clear transient risk factor (surgery, immobilization, trauma, pregnancy) → lower recurrence after stopping anticoagulation (3-6 months); shorter treatment course
- **Unprovoked VTE:** No identifiable transient risk factor → recurrence risk ~30% at 5 years; long-term (indefinite) anticoagulation generally recommended after first unprovoked proximal DVT or PE
- **Cancer-associated VTE:** VTE in active malignancy; highest recurrence risk (~20% per year); LMWH (first-line historically) or DOAC (apixaban/rivaroxaban with caution for GI bleeding in GI cancers)

### Classification of PE

**2019 ESC risk stratification (by hemodynamic stability and RV dysfunction):**

| Risk | Hemodynamics | Imaging | Biomarkers | Mortality | Treatment |
|:-----|:------------|:--------|:-----------|:---------|:---------|
| **Massive/High** | Shock or arrest | RV dilation | Troponin+/BNP+ | ~15-30% | Systemic thrombolysis or catheter-directed therapy + anticoagulation |
| **Submassive/Intermediate-high** | Stable | RV dilation | Troponin+/BNP+ | ~5-15% | Anticoagulation; consider advanced therapy if deterioration |
| **Intermediate-low** | Stable | RV dilation OR biomarker+ | Either | ~2-5% | Anticoagulation |
| **Low** | Stable | No RV dilation | Both negative | <1% | DOAC; outpatient if low PESI |

**Simplified PESI score** (Pulmonary Embolism Severity Index): Predicts 30-day mortality; score ≥1 of: age >80, cancer, cardiopulmonary disease, HR ≥110, SBP <100, O2 sat <90% → inpatient management; score 0 → low risk, outpatient eligible.

## Function

### Inherited thrombophilias

| Thrombophilia | Prevalence (general pop.) | VTE lifetime risk | Recurrence risk | Notes |
|:-------------|:------------------------|:-----------------|:----------------|:------|
| Factor V Leiden (heterozygous) | ~5% Caucasian | ~3-5× increase | Moderate | R506Q; FVa resistant to APC; most common thrombophilia |
| Factor V Leiden (homozygous) | ~0.02% | ~50-80× increase | High | |
| Prothrombin G20210A (heterozygous) | ~2-3% Caucasian | ~2-3× increase | Moderate | ↑ prothrombin levels |
| Protein C deficiency | ~0.3% | ~8-10× increase | High | Autosomal dominant; warfarin-induced skin necrosis risk |
| Protein S deficiency | ~0.3% | ~5-8× increase | High | Cofactor for APC |
| Antithrombin deficiency | ~0.02-0.04% | ~25-50× increase | Very high | Most severe inherited thrombophilia |
| APS (acquired) | ~0.5% | High (varies) | Very high | Triple-positive: >10%/yr; warfarin superior to DOACs |

**Thrombophilia testing:** Not recommended during acute VTE (acute phase reactant changes confound results); test ≥3 months after anticoagulation stopped; screen in: unprovoked VTE <50 years, unusual location (cerebral, splanchnic, upper extremity), family history, recurrent VTE, APS suspicion.

## Pathology

### Clinical features

**DVT:**
- Classic: Unilateral leg swelling, warmth, erythema, tenderness along deep vein tract, Homans' sign (calf pain on dorsiflexion — poor specificity)
- **Wells score for DVT (pre-test probability):** Active cancer +1, paralysis/plaster +1, bedridden >3 days +1, tenderness along vein +1, swollen leg +1, calf >3 cm larger +1, pitting edema +1, previous DVT +1, alternative diagnosis equally likely −2; score ≤0 = low probability (treat as unlikely), score ≥2 = high probability (treat as likely)
- **D-dimer:** Negative D-dimer (<500 ng/mL; age-adjusted: 500 + age × 10 >50 years) effectively rules out DVT in low/intermediate probability patients; elevated D-dimer is non-specific (any fibrin turnover)
- **Duplex ultrasound:** Non-compressibility of vein = diagnostic for DVT; sensitivity ~95% for proximal, ~75% for distal

**Pulmonary embolism:**
- Classic: Pleuritic chest pain (peripheral infarct), hemoptysis (lung infarction), dyspnea (central/massive), tachycardia (most common sign), hypoxemia, right heart strain
- Massive PE: Syncope, hypotension (SBP <90 mmHg), right heart failure (elevated JVP, S3, RV heave), cyanosis, cardiac arrest (PEA)
- **Wells score for PE:** DVT symptoms +3, alternative less likely +3, HR >100 +1.5, immobilization/surgery +1.5, prior DVT/PE +1.5, hemoptysis +1, malignancy +1; score <2 = low probability, score ≥5 = high probability
- **CTPA (CT pulmonary angiography):** Diagnostic gold standard; RV/LV diameter ratio >0.9 on CT = RV dysfunction; sensitivity/specificity >95% for subsegmental and larger PE
- **Echocardiography:** McConnell's sign (RV free wall hypokinesis with apical sparing) in massive PE; right heart thrombus = surgical emergency; not diagnostic alone
- **Biomarkers:** Troponin (RV myocardial injury), BNP/NT-proBNP (RV wall stress) → prognostic in hemodynamically stable PE

### Diagnosis

**Diagnostic algorithm:**
1. Calculate Wells score + D-dimer (if low/intermediate probability)
2. Low probability + negative D-dimer → VTE excluded
3. High probability or positive D-dimer → imaging (ultrasound for DVT; CTPA for PE)
4. For PE with hemodynamic instability → bedside echo first (if CTPA not safe); systemic thrombolysis if massive PE confirmed

### Treatment

**Anticoagulation — acute VTE (first 3-6 months):**

**Direct oral anticoagulants (DOACs) — first-line:**
- **Apixaban (Eliquis; AMPLIFY trial):** 10 mg BID × 7 days → 5 mg BID; recurrent VTE 2.3% vs. 2.7% LMWH/VKA (non-inferior); major bleeding 0.6% vs. 1.8% (superior); FDA approved DVT/PE treatment [^agnelli-2013-amplify-apixaban-vte]; preferred in cancer (CARAVAGGIO trial non-inferior to dalteparin)
- **Rivaroxaban (Xarelto; EINSTEIN-DVT/PE):** 15 mg BID × 21 days → 20 mg QD with evening meal; non-inferior to LMWH/VKA for recurrent VTE; bleeding comparable; convenient single-drug approach [^bauersachs-2010-einstein-rivaroxaban]
- **Edoxaban (Savaysa; Hokusai-VTE):** 5-10 days LMWH run-in → edoxaban 60 mg QD; reduces dose to 30 mg if CrCl 15-50 mL/min or body weight ≤60 kg
- **Dabigatran (Pradaxa; RE-COVER):** 5-10 days LMWH run-in → dabigatran 150 mg BID; renal clearance ~80% → requires dose adjustment in CKD; reversed by idarucizumab

**LMWH (Low-molecular-weight heparin):**
- Dalteparin, enoxaparin, tinzaparin; SC injection; anti-Xa monitoring in renal impairment, obesity, pregnancy
- Preferred in pregnancy (DOACs teratogenic/unknown fetal safety) and cancer-associated VTE
- Cancer + VTE: Dalteparin (CLOT trial: 50% VTE recurrence reduction vs. warfarin) or DOAC (apixaban/rivaroxaban now preferred based on ADAM-VTE, CARAVAGGIO, SELECT-D trials)

**Anticoagulation duration:**
- Provoked VTE (major transient risk factor): 3 months
- Unprovoked proximal DVT or PE: ≥3 months; extend indefinitely if recurrence risk high and bleeding risk acceptable; D-dimer testing at 1 month off anticoagulation predicts recurrence risk (elevated D-dimer → higher recurrence)
- Cancer-associated VTE: Treat until cancer is in remission; typically indefinite during active cancer
- Extended prophylaxis: **Apixaban 2.5 mg BID** (AMPLIFY-EXT trial: 80% relative risk reduction of VTE vs. placebo over 12 additional months with minimal bleeding increase) — approved for extended treatment after ≥6 months initial therapy

**Massive PE (hemodynamic instability) — advanced therapy:**
- **Systemic thrombolysis:** Alteplase 100 mg IV over 2 hours (or 10 mg bolus + 90 mg over 2h); direct action on pulmonary artery thrombus → rapid hemodynamic improvement; 50% mortality reduction vs. anticoagulation alone in massive PE; major bleeding 10%; ICH 1-3% → contraindicated if recent surgery, stroke, or hemorrhage
- **Catheter-directed thrombolysis (CDT):** Lower-dose tPA (1-2 mg/h per catheter) directly into pulmonary artery; reduces systemic bleeding; PERFECT registry evidence; used for intermediate-high risk PE with contraindication to systemic thrombolysis
- **Surgical embolectomy:** Open cardiac surgery; for massive PE refractory to thrombolysis or immediate hemodynamic collapse; requires cardiopulmonary bypass; high mortality but may be lifesaving
- **ECMO (VA-ECMO):** Right heart failure + cardiac arrest → veno-arterial ECMO provides circulatory support while thrombolysis or embolectomy performed; emerging as bridge to definitive therapy

**VTE prophylaxis:**
- **Hospitalized surgical patients:** LMWH (enoxaparin 40 mg SC QD) or UFH (5,000 U SC TID) + mechanical compression (sequential compression devices); extended prophylaxis (LMWH × 28-35 days) for major abdominal/pelvic cancer surgery (FAME registry)
- **Medical patients:** LMWH or UFH for bed-bound patients with acute illness; DOAC prophylaxis (rivaroxaban, betrixaban, apixaban) inferior to LMWH in most hospitalized medical patients (excess bleeding); exception: extended prophylaxis post-hospitalization (MAGELLAN, APEX trials) shows modest VTE reduction
- **Travel thrombosis:** Flights >6 h + risk factors → aspirin and/or LMWH prophylaxis; graduated compression stockings; ambulation; hydration
- **Inferior vena cava (IVC) filter:** For VTE + absolute contraindication to anticoagulation; retrievable filters preferred; does not reduce mortality; prophylactic filters not recommended routinely

## Connections

- `connects-to` → **[Thrombin](../../03-molecular/thrombin/README.md)** — Thrombin (FIIa) generates fibrin at the core of venous thrombi; stasis → contact activation → FXI → FIXa → FX → thrombin → fibrin-rich clot; DOACs (dabigatran, rivaroxaban, apixaban) target thrombin or FXa to prevent and treat VTE; LMWH inhibits thrombin via antithrombin.
- `connects-to` → **[Antiphospholipid Syndrome](../antiphospholipid-syndrome/README.md)** — APS is the most important thrombophilia causing recurrent DVT/PE in young adults; triple-positive aPL (LA + aCL + anti-B2GPI) confers >10% annual thrombotic risk; warfarin INR 2-3 is superior to DOACs for VTE in APS; rivaroxaban doubled arterial event risk in triple-positive APS (TRAPS trial).
- `connects-to` → **[Von Willebrand Factor](../../03-molecular/von-willebrand-factor/README.md)** — Elevated VWF promotes venous thrombosis by augmenting platelet recruitment and fibrin network formation; VWF is an acute-phase protein elevated in surgery, infection, cancer → increased VTE risk; ABO blood group affects VWF level (type O ~25% lower VWF → lower baseline VTE risk).
- `connects-to` → **[Protein C](../../03-molecular/protein-c/README.md)** — Protein C deficiency (PROC mutations) is a rare but high-risk inherited thrombophilia (0.3% prevalence; 5-10× VTE risk); APC inactivates FVa/FVIIIa; warfarin-induced skin necrosis is uniquely dangerous in protein C-deficient patients starting warfarin without heparin bridge.
- `connects-to` → **[Inherited Thrombophilia](../inherited-thrombophilia/README.md)** — Inherited thrombophilia testing guides anticoagulation duration in VTE: FV Leiden and prothrombin G20210A heterozygotes require 3-6 months for first provoked VTE; high-risk deficiencies (AT, protein C/S) or recurrent unprovoked VTE → indefinite anticoagulation.
- `connects-to` → **[Heparin-Induced Thrombocytopenia](../heparin-induced-thrombocytopenia/README.md)** — HIT causes paradoxical DVT/PE (venous) and arterial thrombosis (HITT); occurs 5-10 days after heparin exposure; anti-PF4/heparin IgG → platelet activation → thrombin; argatroban, bivalirudin, and fondaparinux replace heparin in HIT; DOACs used for bridging to warfarin.
- `connects-to` → **[Antithrombin](../../03-molecular/antithrombin/README.md)** — Antithrombin deficiency (SERPINC1 mutations; 1:2,000-5,000) is the most severe inherited thrombophilia (25-50× lifetime VTE risk); UFH/LMWH efficacy requires AT → AT-deficient patients may need AT concentrate; functional AT assay needed for diagnosis.
- `connects-to` → **[Hemophilia A](../hemophilia-a/README.md)** — Severe HA (FVIII <1%) confers significant VTE protection; historical VTE rate in HA ~0.5/1000 PY vs. ~1.5-3/1000 general population; emicizumab reconstitutes intrinsic tenase; avoid high-dose APCC with emicizumab → TMA; gene therapy raising FVIII >150% increases VTE risk.
- `treated-by` → **[Warfarin](../../../03-medicine/01-modern/09-hematology/warfarin/README.md)** — Warfarin treats DVT/PE at INR 2.0–3.0 × 3–6 months for provoked VTE; indefinite for unprovoked high-risk; largely superseded by DOACs; remains first-line for antiphospholipid syndrome; LMWH bridging required at initiation.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Endothelial injury is one arm of Virchow's triad driving VTE: damaged endothelium loses its antithrombotic surface (thrombomodulin, heparan sulfate) and exposes tissue factor and von Willebrand factor, nucleating clot—why surgery, inflammation and indwelling lines provoke it.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — The lung is where venous thromboembolism turns deadly: a deep-vein thrombus that breaks loose lodges in the pulmonary arteries as a pulmonary embolism, causing hypoxia, acute right-heart strain and sudden death; CT angiography diagnoses it and large clots may need thrombolysis.
- `connects-to` → **[Sickle Cell Disease](../sickle-cell-disease/README.md)** — Sickle cell disease is a strong, often overlooked VTE risk factor: chronic hemolysis, phosphatidylserine exposure and inflammation create a hypercoagulable state, so VTE and pulmonary embolism rates are markedly raised, overlapping with in-situ pulmonary vaso-occlusion.
- `connects-to` → **[Polycythemia Vera](../polycythemia-vera/README.md)** — Polycythemia vera is a major acquired cause of venous thromboembolism: high hematocrit and JAK2-mutant prothrombotic blood drive clots, including splanchnic-vein thromboses (Budd-Chiari, portal vein) that can be the first sign—so unusual-site VTE prompts JAK2 testing.
- `connects-to` → **[Pancreatic Cancer](../pancreatic-cancer/README.md)** — Cancer is a leading cause of venous thromboembolism, and pancreatic cancer is the classic high-risk tumor (Trousseau syndrome): mucin and tissue factor make the blood intensely prothrombotic, so migratory or unprovoked VTE can be the presenting clue to an occult malignancy.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — COVID-19 dramatically raises venous thromboembolism risk: SARS-CoV-2 endothelial injury and intense inflammation drive immunothrombosis, so hospitalized patients develop DVT and pulmonary embolism at high rates and receive thromboprophylaxis, with D-dimer marking severity.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Platelets help build venous thrombi: though VTE is a fibrin-rich red clot, activated platelets still seed and propagate it, which is why some antiplatelet therapy reduces recurrence—blurring the old line between arterial and venous clots.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Estrogen is a leading reversible cause of VTE: oral contraceptives, hormone therapy and pregnancy raise clotting factors and lower anticoagulant proteins, multiplying thrombosis risk—especially when combined with factor V Leiden or other inherited thrombophilias.
- `connects-to` → **[Obesity](../obesity/README.md)** — Obesity steadily raises VTE risk: adipose-driven inflammation, higher clotting factors and venous stasis from immobility combine to promote thrombosis, so weight is an independent, modifiable risk factor that compounds surgery, pregnancy and hormonal triggers.

[^agnelli-2013-amplify-apixaban-vte]: Agnelli G, Buller HR, Cohen A, et al. Oral apixaban for the treatment of acute venous thromboembolism. *N Engl J Med.* 2013;369(9):799-808. [doi:10.1056/NEJMoa1302507](https://doi.org/10.1056/NEJMoa1302507) · [PubMed 23808982](https://pubmed.ncbi.nlm.nih.gov/23808982/)
[^bauersachs-2010-einstein-rivaroxaban]: EINSTEIN Investigators. Oral rivaroxaban for symptomatic venous thromboembolism. *N Engl J Med.* 2010;363(26):2499-2510. [doi:10.1056/NEJMoa1007903](https://doi.org/10.1056/NEJMoa1007903) · [PubMed 21128814](https://pubmed.ncbi.nlm.nih.gov/21128814/)
[^konstantinides-2020-esc-pe]: Konstantinides SV, Meyer G, Becattini C, et al. 2019 ESC Guidelines for the diagnosis and management of acute pulmonary embolism. *Eur Heart J.* 2020;41(4):543-603. [doi:10.1093/eurheartj/ehz405](https://doi.org/10.1093/eurheartj/ehz405) · [PubMed 31504429](https://pubmed.ncbi.nlm.nih.gov/31504429/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
