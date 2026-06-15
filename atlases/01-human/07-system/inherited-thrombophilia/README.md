---
schema: human-scale-entry/v1
id: inherited-thrombophilia
name: Inherited Thrombophilia
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Inherited thrombophilias are genetic risk factors for VTE; Factor V Leiden R506Q (5% Europeans; APC resistance) and prothrombin G20210A are most common; protein C/S and antithrombin deficiencies are rarer but higher-risk. Duration of anticoagulation is the main clinical impact."
aliases: ["inherited thrombophilia", "hereditary thrombophilia", "thrombophilia", "factor V Leiden", "FVL", "prothrombin G20210A", "APC resistance", "thrombophilic disorder"]
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
  - id: kearon-2016-antithrombotic-therapy
    type: clinical-guideline
    cite: "Kearon C, Akl EA, Ornelas J, et al. Antithrombotic therapy for VTE disease: CHEST guideline and expert panel report. Chest. 2016;149(2):315-352."
    doi: "10.1016/j.chest.2015.11.026"
    pmid: "26867832"
    url: "https://doi.org/10.1016/j.chest.2015.11.026"
cross_links:
  - target: 01-human/03-molecular/protein-c
    relation: connects-to
    note: "Protein C deficiency is the third most common inherited thrombophilia (0.3% prevalence; 5-10× VTE risk); APC pathway inactivates FVa/FVIIIa → thrombosis risk from impaired anticoagulant mechanism; warfarin-induced skin necrosis risk on protein C–deficient patients."
  - target: 01-human/03-molecular/thrombin
    relation: connects-to
    note: "Factor V Leiden (R506Q) causes APC resistance: thrombin-activated FVa at Arg506 cannot be cleaved → uncontrolled prothrombinase complex → excess thrombin; thrombomodulin-bound thrombin activates protein C → the central anticoagulant checkpoint that FVL undermines."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "VTE (DVT/PE) is the primary manifestation of inherited thrombophilia; risk is multiplicative (FVL + OCP = 35× VTE risk); thrombophilia guides anticoagulation duration (indefinite for AT deficiency, homozygous FVL, compound heterozygous); do not test during acute VTE."
  - target: 01-human/07-system/antiphospholipid-syndrome
    relation: connects-to
    note: "APS is the most important acquired thrombophilia, causing indistinguishable VTE and arterial thrombosis to inherited thrombophilia; combined APS + inherited thrombophilia (e.g., FVL + triple-positive aPL) confers extreme thrombotic risk; APS is excluded by thrombophilia workup."
  - target: 01-human/03-molecular/antithrombin
    relation: connects-to
    note: "Antithrombin deficiency (0.02-0.04% prevalence; 25-50× VTE risk) is the highest-risk inherited thrombophilia; type IIa reactive-site mutations (Arg393His) most thrombogenic; UFH/LMWH require AT for efficacy; AT concentrate needed peri-surgery/delivery."
  - target: 01-human/07-system/hemophilia-a
    relation: connects-to
    note: "Inherited thrombophilia is the mirror image of hemophilia — a clotting excess versus a bleeding deficiency; the contrast is mechanistic, since factor V Leiden makes FVa resist shutdown by activated protein C, whose downstream targets are missing or weak in hemophilia."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver synthesizes nearly all coagulation proteins, including the anticoagulants protein C, protein S, and antithrombin whose inherited deficiencies cause thrombophilia; hepatic failure causes a mixed coagulopathy, and warfarin blocks vitamin-K-dependent factor synthesis."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Inherited thrombophilias (factor V Leiden, prothrombin G20210A) cause venous, not arterial, thrombosis — so they are not established risk factors for ischemic stroke or MI and do not warrant anticoagulation for arterial events; antiphospholipid syndrome is the exception."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Healthy endothelium is antithrombotic, displaying thrombomodulin that activates protein C and heparan sulfate for antithrombin; inherited thrombophilias (factor V Leiden, protein C/S or antithrombin deficiency) cripple these endothelial-anchored brakes, tilting toward clotting."
  - target: 01-human/07-system/heparin-induced-thrombocytopenia
    relation: connects-to
    note: "Both are prothrombotic but differ in origin: inherited thrombophilia is a germline anticoagulant defect, HIT an acquired antibody-mediated platelet activation; a thrombophilic patient who develops HIT faces compounded clot risk, and both demand non-heparin anticoagulation."
  - target: 01-human/07-system/pnh
    relation: connects-to
    note: "PNH is an acquired thrombophilia: loss of GPI-anchored complement regulators drives hemolysis and platelet activation → thrombosis in unusual sites (hepatic, cerebral); like inherited thrombophilias it presents with unexplained VTE, but its mechanism is complement, not factors."
  - target: 01-human/07-system/polycythemia-vera
    relation: connects-to
    note: "Inherited thrombophilia and polycythemia vera are inherited versus acquired prothrombotic states: thrombophilia (factor V Leiden, prothrombin G20210A) tilts toward clotting, while PV's JAK2 thickens the blood—both raise venous thrombosis, including splanchnic clots."
  - target: 01-human/07-system/disseminated-intravascular-coagulation
    relation: connects-to
    note: "Inherited thrombophilia and DIC are opposite ends of clotting dysregulation: thrombophilia is a stable inherited tilt toward thrombosis, while DIC is acute systemic coagulation activation consuming factors and platelets—paradoxically causing both clotting and bleeding."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Inherited thrombophilia mainly raises venous, not arterial, thrombosis—unlike atherosclerosis: factor V Leiden and prothrombin mutations drive DVT and PE, while atherosclerotic thrombosis is plaque-driven, so thrombophilia testing is reserved for venous events."
  - target: 01-human/07-system/myeloproliferative-neoplasms
    relation: connects-to
    note: "Myeloproliferative neoplasms are a major acquired thrombophilia: JAK2-mutant blood is intrinsically prothrombotic, causing arterial and venous (including splanchnic) clots like inherited thrombophilias—so unexplained thrombosis at unusual sites warrants JAK2 testing."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "Inherited thrombophilia can cause pulmonary hypertension: recurrent pulmonary emboli that fail to resolve organize into fibrotic obstruction, causing chronic thromboembolic pulmonary hypertension (CTEPH)—a complication surgically curable by endarterectomy."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Platelets are central to the arterial thrombosis of thrombophilia: while inherited thrombophilias mainly drive venous clots, platelet activation drives arterial events—so antiplatelet and anticoagulant therapy target different arms of clot formation."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Estrogen multiplies the clot risk of inherited thrombophilia: oral contraceptives, hormone therapy and pregnancy raise clotting factors, so a factor V Leiden carrier faces sharply higher venous thrombosis risk on estrogen—central to contraceptive counseling."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Pulmonary embolism is the feared endpoint of inherited thrombophilia: deep vein clots break off and lodge in the lungs, so a young or recurrent unprovoked PE prompts thrombophilia testing—and the risk guides how long anticoagulation continues."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Inherited thrombophilia causes clots in unusual sites like the cerebral veins: prothrombotic mutations, especially with estrogen, predispose to cerebral venous sinus thrombosis—so an unexplained young stroke or sinus thrombosis warrants a thrombophilia workup."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "Inherited thrombophilia threatens the placenta: clots in the placental circulation are linked to recurrent miscarriage, pre-eclampsia, growth restriction, and stillbirth—so obstetric complications are a major reason thrombophilia is tested for in women."
  - target: 01-human/03-molecular/fibrinogen
    relation: connects-to
    note: "Fibrinogen ties to thrombophilia at both ends: rare inherited dysfibrinogenemia can make a clot-prone fibrin, and high fibrinogen levels are themselves prothrombotic—so the very protein that forms clots can be a hereditary or acquired thrombosis risk."
  - target: 01-human/07-system/sickle-cell-disease
    relation: connects-to
    note: "Sickle cell disease is a hypercoagulable state in its own right: chronic hemolysis, activated platelets, and endothelial damage tip blood toward clotting, so it compounds inherited thrombophilia and raises venous thromboembolism risk beyond its vaso-occlusive crises."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium is coagulation Factor IV, central to the clotting that thrombophilia tips toward excess: it bridges clotting-factor complexes to membranes, so it underlies the cascade—and citrate that chelates it keeps lab tubes and stored blood from clotting."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "The liver's hepatocytes make both sides of the clotting balance: they synthesize procoagulant factors and the natural anticoagulants protein C, protein S and antithrombin—so inherited deficiencies of these hepatocyte products cause thrombophilia."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Obesity compounds inherited thrombophilia: excess adipose tissue raises clotting factors and inflammation and impairs fibrinolysis, so it multiplies the venous-thrombosis risk of a Factor V Leiden or prothrombin variant—gene meets environment."
  - target: 01-human/03-molecular/von-willebrand-factor
    relation: connects-to
    note: "High von Willebrand factor is itself a thrombophilia: elevated vWF—from genes, inflammation, or aging—makes platelets stickier and raises clot risk, adding to the inherited deficiencies of natural anticoagulants behind familial thrombosis."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Thrombophilia is amplified by neutrophil NETs: neutrophils cast out DNA webs (NETs) that scaffold platelets and clotting factors into clots, so this immunothrombosis turns inflammation into the venous thrombi that thrombophilia predisposes to."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Low oxygen and stasis tip thrombophilia into clots: immobility and hypoxia (long flights, illness) slow venous flow and switch on procoagulant signals, providing the trigger that turns an inherited clotting tendency into an actual thrombosis."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Thrombophilia can clot the kidney's veins: renal vein thrombosis is a classic unusual-site clot, abruptly causing flank pain, blood in the urine, and swelling as the kidney's venous drainage is blocked."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "Thrombophilia drives clots in the splanchnic veins: thrombosis of the splenic and portal veins draining the spleen and gut is a hallmark unusual-site event, causing splenomegaly and portal hypertension."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "Thrombophilia can infarct the adrenal glands: thrombosis of their veins triggers hemorrhagic adrenal infarction, which can precipitate life-threatening adrenal failure—a rare but lethal unusual-site complication."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Confirming thrombophilia's clots relies on imaging: CT angiography and lung scans read in X-ray photons locate the deep-vein thromboses and pulmonary emboli that prompt a hypercoagulable workup."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Red cells thicken thrombophilic blood: in polycythemia and sickle cell disease, excess or misshapen erythrocytes raise viscosity and slow flow, promoting the clotting these prothrombotic states are known for."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Some thrombophilias are born in the bone marrow: JAK2-driven myeloproliferative neoplasms overproduce blood cells that clot readily, so marrow output itself becomes a cause of thrombosis."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows the clot that won't quit: in factor V Leiden, the mutated factor resists shutdown by activated protein C, so thrombin keeps firing and weaves an extra-dense, stable fibrin mesh that resists dissolving."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Thrombophilia can reach arteries through a back door: a venous clot can cross a patent foramen ovale in the heart and shoot to the brain as a paradoxical embolism, an unexpected cause of stroke in the young."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Old clots leave lasting scar: when a deep vein thrombosis only partly clears, the vein wall fibroses into post-thrombotic syndrome, and unresolved lung clots organize into the fibrotic obstruction of chronic thromboembolic pulmonary hypertension."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Protein C deficiency writes itself on the skin: starting warfarin can trigger paradoxical skin necrosis as protein C falls fastest, and homozygous deficiency causes neonatal purpura fulminans, dark patches of skin infarction in the newborn."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Thrombophilia can clot the eye's veins: retinal vein occlusion, especially in the young, prompts a search for an inherited hypercoagulable state, the clot in the retina blurring or dimming vision suddenly."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Clots in the brain's drainage threaten neurons: inherited thrombophilia is a leading cause of cerebral venous sinus thrombosis, where backed-up pressure and infarction injure neurons, causing headache, seizures, and focal deficits."
---

# Inherited Thrombophilia

## Overview

**Inherited thrombophilias** are genetic conditions that increase susceptibility to venous thromboembolism (VTE) — primarily deep vein thrombosis (DVT) and pulmonary embolism (PE) — due to constitutional imbalances in the coagulation system. The discovery of **Factor V Leiden** in 1994 [^bertina-1994-factor-v-leiden] established the molecular basis for the most common inherited thrombophilia and transformed understanding of thrombosis genetics.

Inherited thrombophilias collectively account for an identifiable cause in ~30-50% of patients with unprovoked VTE, and identifying them influences counseling, duration of anticoagulation, and screening of family members. However, **many individuals with thrombophilia never develop VTE** — additional risk factors (surgery, immobility, pregnancy, hormonal therapy, malignancy) are usually required to trigger the first event. Conversely, most VTE events occur in people without identified thrombophilia.

**Population prevalence and VTE risk:**

| Condition | Mechanism | Prevalence | Heterozygous VTE risk | Notes |
|:----------|:----------|:-----------|:---------------------|:------|
| **Factor V Leiden (FVL)** | F5 R506Q → APC resistance | ~5% Caucasians; 1-2% African, <1% Asian | 4-8× | Most common; predominantly venous (not arterial) |
| **Prothrombin G20210A** | F2 3'-UTR → ↑prothrombin levels | ~2-3% Caucasians | 2-3× | Second most common; associated with cerebral vein thrombosis |
| **Protein C deficiency** | PROC loss-of-function | ~0.3% | 5-10× | Warfarin-induced skin necrosis risk; neonatal purpura fulminans (homozygous) |
| **Protein S deficiency** | PROS1 mutations | ~0.1% | 5-10× | Type I (antigen + activity low), II (activity low), III (free PS low) |
| **Antithrombin deficiency** | SERPINC1 mutations | ~0.05% | 10-20× | Most severe; heparin requires AT → heparin resistance |
| **Homozygous FVL** | Both alleles R506Q | ~0.02% | 50-80× | High-risk; often warrants indefinite anticoagulation |
| **Compound heterozygous** | FVL + PT G20210A | ~0.01% | 10-20× | High-risk; very high with additional triggers |

**What is NOT a high-yield inherited thrombophilia (no longer routinely tested):**
- **MTHFR C677T/A1298C:** Mild hyperhomocysteinemia; NOT an independent VTE risk factor; not recommended for testing (ACCP, ASH guidelines)
- **PAI-1 4G/5G polymorphism:** Population data weak; not tested routinely

## Structure

### Molecular mechanisms of inherited thrombophilias

**1. Factor V Leiden — APC resistance**

Factor V (F5) has three main functional roles:
- **Pro-coagulant:** As FVa (activated by thrombin or FXa), acts as co-factor for FXa in the prothrombinase complex → 300,000× acceleration of thrombin generation
- **Anticoagulant:** Intact FV (non-activated) acts as APC co-factor for FVIIIa cleavage → amplifies APC anticoagulant function
- **APC cleavage sites in FVa:** Arg506 (primary, rapid; abolishes most prothrombinase activity), Arg306 (secondary, slow; requires protein S), Arg679 (minor)

**FVL R506Q effect:**
- Prevents APC cleavage at Arg506 → FVa 10-20× more stable → prolonged prothrombinase → sustained thrombin
- Also impairs FV anticoagulant function → reduces APC-mediated FVIIIa inactivation
- Result: doubly impaired anticoagulation → hypercoagulability

**2. Prothrombin G20210A — elevated prothrombin**

The G20210A mutation is in the **3'-untranslated region (3'-UTR)** of the prothrombin (F2) gene, specifically at the polyadenylation cleavage site:
- G→A transition → increased mRNA stability/efficiency → 20-30% higher plasma prothrombin (factor II) levels
- More prothrombin → more thrombin potential → greater thrombin burst when coagulation is triggered
- Less dramatic APC resistance effect than FVL; primarily quantitative hypercoagulability

**3. Protein C deficiency (PROC)**

See [Protein C molecular entry](../../03-molecular/protein-c/README.md) for full detail.
- Type I (80%): Low antigen + low activity (quantitative deficiency)
- Type II (20%): Normal antigen + low activity (dysfunctional protein)
- APC cannot shut down FVa/FVIIIa → thrombin generation unchecked

**4. Protein S deficiency (PROS1)**

Protein S has three clinical subtypes:
- Type I: Low total antigen, low free antigen, low activity (quantitative loss)
- Type II: Normal antigen (total + free), low activity (qualitative)
- Type III: Normal total antigen, low **free** protein S (increased binding to C4BP); most common type
- Free protein S is the active APC co-factor; bound (to C4BP) is inactive
- Normal in pregnancy: C4BP rises → free PS falls → physiological acquired thrombophilia

**5. Antithrombin deficiency (SERPINC1)**

Antithrombin (ATIII) is the primary plasma inhibitor of thrombin, FXa, FIXa, and FXIa:
- Type I (quantitative): Low antigen + low activity; more severe
- Type II (qualitative): Normal antigen, low activity; specific subtypes affecting heparin binding site (HBS) vs. reactive site (RS)
- **AT deficiency + heparin resistance:** Heparin works by accelerating AT-mediated thrombin inactivation (~1000-fold); if AT is severely depleted → heparin is less effective → clinical heparin resistance → may need AT concentrate first
- Most severe inherited thrombophilia: unprovoked DVT often at young age, frequent recurrence; typically warrants indefinite anticoagulation

## Function

### Clinical presentation of inherited thrombophilia

**When to suspect inherited thrombophilia:**
- **Unprovoked** VTE (DVT/PE without surgery, immobility, trauma, cancer, pregnancy)
- VTE at young age (<45-50 years)
- **Recurrent** VTE (2+ events)
- **Unusual site** thrombosis: cerebral vein thrombosis, portal vein thrombosis, splenic vein, Budd-Chiari syndrome — especially in young patients or those not receiving estrogen
- VTE during pregnancy or oral contraceptive use
- Strong **family history** of VTE (1st-degree relative with unprovoked VTE)
- **Warfarin-induced skin necrosis** → screen for protein C or S deficiency

**Risk amplification — multiplicative effects:**

| Combination | Approximate VTE risk (vs. baseline ~1/1000/year) |
|:-----------|:--------------------------------------------------|
| OCP use alone | 4× |
| FVL heterozygous alone | 7× |
| FVL + OCP | **35×** (multiplicative, not additive) |
| AT deficiency alone | 10-20× |
| Pregnancy alone | 4-5× |
| AT deficiency + pregnancy | 70-100× |
| Triple-positive APS | 100-200× |

### When NOT to test

- **During acute VTE event:** Coagulation factors are consumed/altered → falsely low protein C, S, AT; FVL and prothrombin G20210A genotype testing are unaffected (DNA-based)
- **While on anticoagulation:** Warfarin reduces protein C and S (vitamin K-dependent) → falsely low; heparin/LMWH may slightly affect AT; DOACs variably affect functional assays; wait 4-6 weeks after stopping warfarin, 24h after stopping DOACs
- **During pregnancy:** Protein S falls physiologically; test postpartum
- **Active infection/inflammation:** C4BP rises → free protein S falls (type III-like picture); AT may fall as acute-phase reactant

## Pathology

### Thrombophilia testing — what to order

**Standard thrombophilia workup:**
1. **FV Leiden genotype** (PCR, G1691A) — unaffected by anticoagulation
2. **Prothrombin G20210A genotype** (PCR) — unaffected by anticoagulation
3. **Protein C activity** (functional assay) — wait until off anticoagulation
4. **Protein S activity** (functional; free PS antigen) — wait; unreliable in pregnancy/OCP/warfarin
5. **Antithrombin activity** (functional) — wait; heparin may slightly lower AT
6. **Antiphospholipid antibodies** (lupus anticoagulant, anticardiolipin IgG/IgM, anti-β2GPI IgG/IgM) — always test; APS is most clinically actionable acquired thrombophilia

**NOT routinely recommended:**
- MTHFR genotype (not an independent VTE risk factor)
- Factor VIII levels (acute phase reactant; elevated transiently)
- Homocysteine levels (not proven to benefit from treatment)

### Treatment and duration of anticoagulation [^kearon-2016-antithrombotic-therapy]

**First event, provoked VTE (surgery, trauma, major transient risk):**
- 3 months anticoagulation — same as for patients without thrombophilia
- Thrombophilia testing rarely changes management here

**First event, unprovoked VTE + low-risk thrombophilia (FVL heterozygous, PT G20210A):**
- At least 3-6 months; extended (indefinite) therapy is debated — shared decision-making based on bleeding risk vs. benefit
- Men have higher recurrence risk after stopping anticoagulation than women — weight in decisions

**First event, unprovoked VTE + high-risk thrombophilia:**
- **AT deficiency:** Indefinite anticoagulation after first unprovoked VTE
- **Protein C or S deficiency:** Indefinite generally recommended after first unprovoked VTE
- **Homozygous FVL or compound heterozygous:** Indefinite anticoagulation after first unprovoked VTE

**Arterial thrombosis (stroke, MI) + thrombophilia:**
- Isolated inherited thrombophilias (FVL, PT G20210A) are **NOT** established risk factors for arterial thrombosis — anticoagulation not indicated for arterial events unless APS is concurrent
- APS (acquired) → warfarin for stroke; rivaroxaban/apixaban have higher recurrence rates in APS (TRAPS trial)

**Pregnancy management:**
- FVL or PT G20210A heterozygous + prior VTE: Prophylactic LMWH throughout pregnancy + postpartum 6 weeks
- AT deficiency + prior VTE: Therapeutic-dose LMWH throughout pregnancy; AT concentrate for delivery
- No prior VTE, but high-risk thrombophilia: Individualize risk — some use postpartum LMWH; avoid estrogen-containing OCP postpartum

**OCP/HRT counseling:**
- FVL heterozygous + OCP: ~35× VTE risk → avoid estrogen-containing OCP; use progestin-only, IUD, barrier methods
- AT deficiency: Avoid estrogen-containing OCP; progestin-only acceptable
- Screening relatives for thrombophilia before starting OCP: Not universally recommended (cost-effectiveness debated); consider for high-risk families

### Drug considerations

| Thrombophilia | Special drug consideration |
|:-------------|:--------------------------|
| AT deficiency | Heparin resistance (needs more heparin or AT concentrate); DOACs preferred for long-term |
| Protein C/S deficiency | Warfarin-induced skin necrosis risk — always bridge with parenteral anticoagulation when starting warfarin; DOACs do not cause skin necrosis |
| FVL + OCP | OCP is major modifiable risk factor — strongly counsel to switch contraception |
| APS | Warfarin superior to DOACs for arterial APS (rivaroxaban inferior in TRAPS trial); target INR 2.0-3.0 for venous APS; some centers use INR 3.0-4.0 for triple-positive APS |

## Connections

- `connects-to` → **[Protein C](../../03-molecular/protein-c/README.md)** — Protein C deficiency (0.3% prevalence; 5-10× VTE risk) impairs APC-mediated FVa/FVIIIa inactivation → thrombosis; warfarin-induced skin necrosis risk on protein C–deficient patients.
- `connects-to` → **[Thrombin](../../03-molecular/thrombin/README.md)** — Factor V Leiden (R506Q) causes APC resistance: thrombin-activated FVa at Arg506 cannot be cleaved → uncontrolled prothrombinase complex → excess thrombin; thrombomodulin-bound thrombin activates protein C → the central anticoagulant checkpoint that FVL undermines.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — VTE (DVT/PE) is the primary manifestation of inherited thrombophilia; risk is multiplicative (FVL + OCP = 35× VTE risk); thrombophilia guides anticoagulation duration (indefinite for AT deficiency, homozygous FVL, compound heterozygous); do not test during acute VTE.
- `connects-to` → **[Antiphospholipid Syndrome](../antiphospholipid-syndrome/README.md)** — APS is the most important acquired thrombophilia, causing indistinguishable VTE and arterial thrombosis to inherited thrombophilia; combined APS + inherited thrombophilia (e.g., FVL + triple-positive aPL) confers extreme thrombotic risk; APS is excluded by thrombophilia workup.
- `connects-to` → **[Antithrombin](../../03-molecular/antithrombin/README.md)** — Antithrombin deficiency (0.02-0.04% prevalence; 25-50× VTE risk) is the highest-risk inherited thrombophilia; type IIa reactive-site mutations (Arg393His) most thrombogenic; UFH/LMWH require AT for efficacy; AT concentrate needed peri-surgery/delivery.
- `connects-to` → **[Hemophilia A](../hemophilia-a/README.md)** — Inherited thrombophilia is the mirror image of hemophilia — a clotting excess versus a bleeding deficiency; the contrast is mechanistic, since factor V Leiden makes FVa resist shutdown by activated protein C, whose downstream targets are missing or weak in hemophilia.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver synthesizes nearly all coagulation proteins, including the anticoagulants protein C, protein S, and antithrombin whose inherited deficiencies cause thrombophilia; hepatic failure causes a mixed coagulopathy, and warfarin blocks vitamin-K-dependent factor synthesis.
- `connects-to` → **[Stroke](../stroke/README.md)** — Inherited thrombophilias (factor V Leiden, prothrombin G20210A) cause venous, not arterial, thrombosis — so they are not established risk factors for ischemic stroke or MI and do not warrant anticoagulation for arterial events; antiphospholipid syndrome is the exception.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Healthy endothelium is antithrombotic, displaying thrombomodulin that activates protein C and heparan sulfate for antithrombin; inherited thrombophilias (factor V Leiden, protein C/S or antithrombin deficiency) cripple these endothelial-anchored brakes, tilting toward clotting.
- `connects-to` → **[Heparin-Induced Thrombocytopenia](../heparin-induced-thrombocytopenia/README.md)** — Both are prothrombotic but differ in origin: inherited thrombophilia is a germline anticoagulant defect, HIT an acquired antibody-mediated platelet activation; a thrombophilic patient who develops HIT faces compounded clot risk, and both demand non-heparin anticoagulation.
- `connects-to` → **[Paroxysmal Nocturnal Hemoglobinuria](../pnh/README.md)** — PNH is an acquired thrombophilia: loss of GPI-anchored complement regulators drives hemolysis and platelet activation → thrombosis in unusual sites (hepatic, cerebral); like inherited thrombophilias it presents with unexplained VTE, but its mechanism is complement, not factors.
- `connects-to` → **[Polycythemia Vera](../polycythemia-vera/README.md)** — Inherited thrombophilia and polycythemia vera are inherited versus acquired prothrombotic states: thrombophilia (factor V Leiden, prothrombin G20210A) tilts toward clotting, while PV's JAK2 thickens the blood—both raise venous thrombosis, including splanchnic clots.
- `connects-to` → **[Disseminated Intravascular Coagulation](../disseminated-intravascular-coagulation/README.md)** — Inherited thrombophilia and DIC are opposite ends of clotting dysregulation: thrombophilia is a stable inherited tilt toward thrombosis, while DIC is acute systemic coagulation activation consuming factors and platelets—paradoxically causing both clotting and bleeding.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Inherited thrombophilia mainly raises venous, not arterial, thrombosis—unlike atherosclerosis: factor V Leiden and prothrombin mutations drive DVT and PE, while atherosclerotic thrombosis is plaque-driven, so thrombophilia testing is reserved for venous events.
- `connects-to` → **[Myeloproliferative Neoplasms](../myeloproliferative-neoplasms/README.md)** — Myeloproliferative neoplasms are a major acquired thrombophilia: JAK2-mutant blood is intrinsically prothrombotic, causing arterial and venous (including splanchnic) clots like inherited thrombophilias—so unexplained thrombosis at unusual sites warrants JAK2 testing.
- `connects-to` → **[Pulmonary Arterial Hypertension](../pulmonary-arterial-hypertension/README.md)** — Inherited thrombophilia can cause pulmonary hypertension: recurrent pulmonary emboli that fail to resolve organize into fibrotic obstruction, causing chronic thromboembolic pulmonary hypertension (CTEPH)—a complication surgically curable by endarterectomy.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Platelets are central to the arterial thrombosis of thrombophilia: while inherited thrombophilias mainly drive venous clots, platelet activation drives arterial events—so antiplatelet and anticoagulant therapy target different arms of clot formation.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Estrogen multiplies the clot risk of inherited thrombophilia: oral contraceptives, hormone therapy and pregnancy raise clotting factors, so a factor V Leiden carrier faces sharply higher venous thrombosis risk on estrogen—central to contraceptive counseling.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Pulmonary embolism is the feared endpoint of inherited thrombophilia: deep vein clots break off and lodge in the lungs, so a young or recurrent unprovoked PE prompts thrombophilia testing—and the risk guides how long anticoagulation continues.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Inherited thrombophilia causes clots in unusual sites like the cerebral veins: prothrombotic mutations, especially with estrogen, predispose to cerebral venous sinus thrombosis—so an unexplained young stroke or sinus thrombosis warrants a thrombophilia workup.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — Inherited thrombophilia threatens the placenta: clots in the placental circulation are linked to recurrent miscarriage, pre-eclampsia, growth restriction, and stillbirth—so obstetric complications are a major reason thrombophilia is tested for in women.
- `connects-to` → **[Fibrinogen](../../03-molecular/fibrinogen/README.md)** — Fibrinogen ties to thrombophilia at both ends: rare inherited dysfibrinogenemia can make a clot-prone fibrin, and high fibrinogen levels are themselves prothrombotic—so the very protein that forms clots can be a hereditary or acquired thrombosis risk.
- `connects-to` → **[Sickle Cell Disease](../sickle-cell-disease/README.md)** — Sickle cell disease is a hypercoagulable state in its own right: chronic hemolysis, activated platelets, and endothelial damage tip blood toward clotting, so it compounds inherited thrombophilia and raises venous thromboembolism risk beyond its vaso-occlusive crises.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium is coagulation Factor IV, central to the clotting that thrombophilia tips toward excess: it bridges clotting-factor complexes to membranes, so it underlies the cascade—and citrate that chelates it keeps lab tubes and stored blood from clotting.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — The liver's hepatocytes make both sides of the clotting balance: they synthesize procoagulant factors and the natural anticoagulants protein C, protein S and antithrombin—so inherited deficiencies of these hepatocyte products cause thrombophilia.
- `connects-to` → **[Obesity](../obesity/README.md)** — Obesity compounds inherited thrombophilia: excess adipose tissue raises clotting factors and inflammation and impairs fibrinolysis, so it multiplies the venous-thrombosis risk of a Factor V Leiden or prothrombin variant—gene meets environment.
- `connects-to` → **[Von Willebrand Factor](../../03-molecular/von-willebrand-factor/README.md)** — High von Willebrand factor is itself a thrombophilia: elevated vWF—from genes, inflammation, or aging—makes platelets stickier and raises clot risk, adding to the inherited deficiencies of natural anticoagulants behind familial thrombosis.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Thrombophilia is amplified by neutrophil NETs: neutrophils cast out DNA webs (NETs) that scaffold platelets and clotting factors into clots, so this immunothrombosis turns inflammation into the venous thrombi that thrombophilia predisposes to.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Low oxygen and stasis tip thrombophilia into clots: immobility and hypoxia (long flights, illness) slow venous flow and switch on procoagulant signals, providing the trigger that turns an inherited clotting tendency into an actual thrombosis.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Thrombophilia can clot the kidney's veins: renal vein thrombosis is a classic unusual-site clot, abruptly causing flank pain, blood in the urine, and swelling as the kidney's venous drainage is blocked.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — Thrombophilia drives clots in the splanchnic veins: thrombosis of the splenic and portal veins draining the spleen and gut is a hallmark unusual-site event, causing splenomegaly and portal hypertension.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — Thrombophilia can infarct the adrenal glands: thrombosis of their veins triggers hemorrhagic adrenal infarction, which can precipitate life-threatening adrenal failure—a rare but lethal unusual-site complication.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Confirming thrombophilia's clots relies on imaging: CT angiography and lung scans read in X-ray photons locate the deep-vein thromboses and pulmonary emboli that prompt a hypercoagulable workup.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Red cells thicken thrombophilic blood: in polycythemia and sickle cell disease, excess or misshapen erythrocytes raise viscosity and slow flow, promoting the clotting these prothrombotic states are known for.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Some thrombophilias are born in the bone marrow: JAK2-driven myeloproliferative neoplasms overproduce blood cells that clot readily, so marrow output itself becomes a cause of thrombosis.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows the clot that won't quit: in factor V Leiden, the mutated factor resists shutdown by activated protein C, so thrombin keeps firing and weaves an extra-dense, stable fibrin mesh that resists dissolving.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Thrombophilia can reach arteries through a back door: a venous clot can cross a patent foramen ovale in the heart and shoot to the brain as a paradoxical embolism, an unexpected cause of stroke in the young.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Old clots leave lasting scar: when a deep vein thrombosis only partly clears, the vein wall fibroses into post-thrombotic syndrome, and unresolved lung clots organize into the fibrotic obstruction of chronic thromboembolic pulmonary hypertension.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Protein C deficiency writes itself on the skin: starting warfarin can trigger paradoxical skin necrosis as protein C falls fastest, and homozygous deficiency causes neonatal purpura fulminans, dark patches of skin infarction in the newborn.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Thrombophilia can clot the eye's veins: retinal vein occlusion, especially in the young, prompts a search for an inherited hypercoagulable state, the clot in the retina blurring or dimming vision suddenly.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Clots in the brain's drainage threaten neurons: inherited thrombophilia is a leading cause of cerebral venous sinus thrombosis, where backed-up pressure and infarction injure neurons, causing headache, seizures, and focal deficits.

[^bertina-1994-factor-v-leiden]: Bertina RM, Koeleman BP, Koster T, et al. Mutation in blood coagulation factor V associated with resistance to activated protein C. *Nature.* 1994;369(6475):64-67. [doi:10.1038/369064a0](https://doi.org/10.1038/369064a0) · [PubMed 8164741](https://pubmed.ncbi.nlm.nih.gov/8164741/)
[^dahlback-2008-protein-c-review]: Dahlbäck B. Advances in understanding pathogenic mechanisms of thrombophilic disorders. *Blood.* 2008;112(1):19-27. [doi:10.1182/blood-2008-01-077909](https://doi.org/10.1182/blood-2008-01-077909) · [PubMed 18574048](https://pubmed.ncbi.nlm.nih.gov/18574048/)
[^kearon-2016-antithrombotic-therapy]: Kearon C, Akl EA, Ornelas J, et al. Antithrombotic therapy for VTE disease: CHEST guideline and expert panel report. *Chest.* 2016;149(2):315-352. [doi:10.1016/j.chest.2015.11.026](https://doi.org/10.1016/j.chest.2015.11.026) · [PubMed 26867832](https://pubmed.ncbi.nlm.nih.gov/26867832/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
