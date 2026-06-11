---
schema: human-scale-entry/v1
id: antiphospholipid-syndrome
name: Antiphospholipid Syndrome
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Antiphospholipid syndrome (APS) is an autoimmune thrombophilia from anti-B2GPI and antiphospholipid antibodies; thrombosis (DVT, stroke) and obstetric morbidity; triple-positive aPL = highest risk. Indefinite anticoagulation (warfarin INR 2-3); LMWH + aspirin for obstetric APS."
aliases: ["APS", "antiphospholipid syndrome", "Hughes syndrome", "antiphospholipid antibody syndrome", "APLS", "catastrophic APS", "CAPS", "obstetric APS"]
sources:
  - id: miyakis-2006-sydney-aps
    type: peer-reviewed
    cite: "Miyakis S, Lockshin MD, Atsumi T, et al. International consensus statement on an update of the classification criteria for definite antiphospholipid syndrome (APS). J Thromb Haemost. 2006;4(2):295-306."
    doi: "10.1111/j.1538-7836.2006.01753.x"
    pmid: "16420554"
    url: "https://doi.org/10.1111/j.1538-7836.2006.01753.x"
  - id: barbhaiya-2023-acreular-aps
    type: peer-reviewed
    cite: "Barbhaiya M, Zuily S, Naden R, et al. The 2023 ACR/EULAR antiphospholipid syndrome classification criteria. Ann Rheum Dis. 2023;82(10):1258-1270."
    doi: "10.1136/ard-2023-224609"
    pmid: "37643823"
    url: "https://doi.org/10.1136/ard-2023-224609"
cross_links:
  - target: 01-human/03-molecular/beta2-glycoprotein-1
    relation: connects-to
    note: "Anti-B2GPI IgG (domain I-specific; R39-R43 epitope) are the highest-risk pathogenic antibody in APS; B2GPI on phospholipid surfaces is the cofactor for anti-cardiolipin binding; triple aPL positivity (LA + aCL + anti-B2GPI) confers >10% annual thrombotic risk."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "APS is driven by IgG antiphospholipid antibodies (anti-B2GPI IgG, anti-cardiolipin IgG, lupus anticoagulant); IgG titers correlate with thrombotic risk; NOACs (rivaroxaban, dabigatran) are inferior to warfarin in APS (TRAPS trial); FcRn inhibitors under investigation."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Complement activation is central to APS thrombosis: anti-B2GPI → C3b deposition → C5a → neutrophil/platelet priming and TF expression; C5 inhibition (eculizumab) is used off-label for catastrophic APS (CAPS; ~37% mortality) refractory to anticoagulation and plasmapheresis."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "Secondary APS occurs in ~30% of SLE patients with persistent aPL; SLE+APS patients have higher stroke/DVT risk than either condition alone; hydroxychloroquine is recommended in all SLE+aPL patients; the 2023 ACR/EULAR APS criteria incorporate SLE as a risk modifier."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "APS causes recurrent DVT/PE in young adults; triple-positive aPL (LA + aCL + anti-B2GPI) confers >10% annual VTE risk; warfarin INR 2-3 is superior to DOACs in APS (TRAPS: rivaroxaban doubled arterial event risk in triple-positive patients); indefinite anticoagulation."
  - target: 01-human/07-system/inherited-thrombophilia
    relation: connects-to
    note: "APS and inherited thrombophilias (FV Leiden, prothrombin G20210A, protein C/S or AT deficiency) both cause recurrent VTE in young adults; co-existing aPL with thrombophilic mutations compounds risk multiplicatively; test for both in young patients with unexplained DVT/PE."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Antiphospholipid antibodies turn the endothelium prothrombotic: anti-β2GPI immune complexes engage endothelial TLR4 → NF-κB → tissue factor, converting the vessel lining from anticoagulant to clot-promoting — one of three converging hits driving APS thrombosis."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Antiphospholipid syndrome is a leading cause of stroke in the young: arterial APS produces ischemic stroke and TIA, so aPL testing is mandatory in stroke under 50, and arterial APS is anticoagulated to a higher INR (2.5-3.5), with warfarin beating DOACs."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "Half of APS is obstetric: antiphospholipid antibodies injure the placenta through both decidual-vessel thrombosis and direct, complement-(C5a)-mediated trophoblast damage, causing recurrent miscarriage, fetal loss, and pre-eclampsia — treated with LMWH plus low-dose aspirin."
---

# Antiphospholipid Syndrome

## Overview

**Antiphospholipid syndrome (APS; Hughes syndrome)** is an **autoimmune thrombophilia** defined by the combination of:
1. **Clinical criteria**: arterial or venous thrombosis, OR pregnancy morbidity
2. **Laboratory criteria**: persistent antiphospholipid antibodies (aPL) — lupus anticoagulant (LA), anti-cardiolipin IgG/IgM (aCL), or anti-beta-2 glycoprotein I IgG/IgM (anti-B2GPI) — on ≥2 occasions ≥12 weeks apart [^miyakis-2006-sydney-aps]

APS is the most common acquired thrombophilia in young adults and the leading identifiable cause of recurrent early pregnancy loss. It exists in two forms:
- **Primary APS:** No underlying systemic autoimmune disease
- **Secondary APS:** Associated with systemic lupus erythematosus (SLE; ~30% of aPL-positive SLE patients), other autoimmune conditions, or infections

**Key statistics:**
- Prevalence: ~40-50 per 100,000 population; F:M ratio ~3:1 for primary APS
- Annual thrombotic risk: ~1-5% per year in aPL-positive patients; up to >10% per year in triple-positive patients
- Recurrence: ~50% thrombotic recurrence without anticoagulation; recurrence rate drops to 5-10% with warfarin INR 2-3
- **Catastrophic APS (CAPS):** <1% of APS patients; multi-organ thrombosis within days; mortality ~37%

## Structure

### Classification of aPL antibody profiles

**2006 Revised Sapporo/Sydney criteria** (clinical + laboratory):

**Clinical criteria:**
- Vascular thrombosis: ≥1 confirmed episode of arterial/venous/small vessel thrombosis
- Pregnancy morbidity: ≥1 fetal death ≥10 weeks; ≥3 unexplained consecutive losses <10 weeks; ≥1 premature birth <34 weeks due to eclampsia/IUGR

**Laboratory criteria (must be present on ≥2 occasions ≥12 weeks apart):**
- Lupus anticoagulant (LA) — detected by dRVVT or aPTT-based assay; most thrombogenic single test
- Anti-cardiolipin IgG/IgM ≥40 GPL/MPL units
- Anti-B2GPI IgG/IgM ≥40 units or >99th percentile

**2023 ACR/EULAR classification criteria** — major update introducing risk stratification [^barbhaiya-2023-acreular-aps]:
- Entry criterion: aPL positivity; exclusion of mimics (infection, drug-induced)
- Weighted domain scoring (aPL profile + clinical domains)
- Emphasizes **high-risk aPL profile**: LA positive, and/or triple positivity, and/or anti-B2GPI IgG >40 units
- Separates thrombotic APS, obstetric APS, and CAPS into distinct clinical domains

### Risk stratification by aPL profile

| aPL profile | Annual thrombotic risk | Clinical management |
|:-----------|:----------------------|:-------------------|
| Single aPL positive (low titer) | ~1-2% | Aspirin 100 mg/day; risk factor modification |
| Isolated LA positive | ~3-5% | Aspirin; consider warfarin in high-risk settings |
| Double positive (any 2 of 3) | ~5-8% | Warfarin INR 2-3; HCQ in SLE |
| **Triple positive (LA + aCL + anti-B2GPI)** | **>10%** | **Warfarin INR 2-3 indefinitely; aspirin** |

## Function

### Normal hemostasis disrupted in APS

B2GPI normally functions as an anticoagulant by:
- Inhibiting factor Xa and the tenase complex
- Competing with prothrombin for phospholipid binding
- Inhibiting ADP-induced platelet aggregation

In APS, anti-B2GPI IgG bound to B2GPI on phospholipid surfaces converts this anticoagulant into a pro-thrombotic surface activator — one of the most elegant mechanisms of autoimmune disease.

## Pathology

### Pathogenesis: three converging mechanisms

**Mechanism 1 — Endothelial activation:**
- Anti-B2GPI IgG + B2GPI on endothelial surface → TLR4 engagement → MyD88 → NF-κB → tissue factor (TF) upregulation, E-selectin, VCAM-1, ICAM-1
- Endothelial TF initiates extrinsic coagulation cascade → thrombin generation → fibrin → thrombus

**Mechanism 2 — Platelet activation:**
- B2GPI on activated platelet surface (PS exposed) + anti-B2GPI IgG → GPIbα receptor interaction → direct platelet activation
- FcγRIIA-dependent (Fc-mediated) platelet priming by anti-B2GPI IgG-B2GPI immune complexes

**Mechanism 3 — Complement activation:**
- Anti-B2GPI immune complexes → classical complement C1q → C3b → C5 → C5a
- C5a primes neutrophils and platelets → TF expression → thrombus amplification
- **Obstetric APS:** C5a at placental decidua → trophoblast injury independent of thrombosis → placental insufficiency, fetal loss, IUGR

### Clinical manifestations

**Thrombotic APS:**
| Site | Manifestation | Notes |
|:-----|:-------------|:------|
| Venous (most common, ~60%) | DVT, PE, cerebral venous thrombosis | Often young patients; all without provoking factors should be tested for aPL |
| Arterial (~30%) | Stroke, TIA, MI, limb ischemia, retinal artery occlusion | Stroke in young patients <50 years: aPL testing mandatory |
| Microvascular | Livedo reticularis, Sneddon syndrome (livedo + stroke), thrombotic nephropathy | LA most strongly associated |

**Obstetric APS:**
- ≥3 consecutive early losses (<10 weeks): attributed to endometrial dysfunction + embryo implantation failure
- Fetal loss ≥10 weeks: placental thrombosis, decidual vasculopathy
- Preeclampsia, IUGR, placental abruption (≥34 weeks): placental inflammation + impaired placentation

**Catastrophic APS (CAPS):**
- Multi-organ thrombosis within <1 week; microvascular predominant
- Triggers: infection (most common), surgery, withdrawal of anticoagulation, OCP
- Organs: kidney (most common), lung, brain, heart, skin (livedo fulminans), adrenal (infarction → crisis)
- Mortality ~37% despite treatment; treated with anticoagulation + glucocorticoids + IVIG or plasma exchange; eculizumab (anti-C5) for refractory CAPS

**Non-criteria APS manifestations:**
- Thrombocytopenia (~30%): anti-B2GPI on platelet surfaces → immune destruction + FcγRIIa-mediated platelet activation
- Hemolytic anemia
- Cardiac: Libman-Sacks endocarditis (non-bacterial verrucous endocarditis; predisposes to embolic stroke)
- Cognitive dysfunction, migraine, chorea (CNS aPL deposition)
- Skin: livedo reticularis, superficial thrombophlebitis, skin necrosis

### Diagnosis

**Laboratory testing:**
- **Lupus anticoagulant (LA):** Most predictive of thrombosis; detected by phospholipid-dependent clotting assays (dRVVT, aPTT-based): prolonged clotting time that does NOT correct with mixing study + corrects with excess phospholipid
- **Anti-cardiolipin IgG/IgM:** ELISA ≥40 GPL/MPL or >99th percentile; IgG more clinically significant than IgM
- **Anti-B2GPI IgG/IgM:** ELISA ≥40 units or >99th percentile; domain I-specific assays available; IgG more clinically significant
- **Confirmation:** Must be positive on ≥2 occasions ≥12 weeks apart (transient aPL from infection does not qualify)

**Imaging:**
- Thrombosis: Doppler ultrasound (DVT), CT-PA (PE), MRI/MRA (stroke), echocardiography (Libman-Sacks)
- Placenta: pathology showing placental infarction, avascular villi, spiral artery thrombosis

### Treatment

**Thrombotic APS (indefinite anticoagulation):**
- **Warfarin (VKA) target INR 2.0-3.0:** First-line for venous APS; superior to NOACs (TRAPS trial: rivaroxaban vs. warfarin in triple-positive APS — rivaroxaban doubled arterial thrombosis risk)
- **INR 2.5-3.5:** For arterial APS (stroke, TIA, MI) or recurrent thrombosis on standard INR
- **NOACs (rivaroxaban, dabigatran, apixaban):** NOT recommended for high-risk aPL profiles; RAPS trial (rivaroxaban non-inferior in venous APS for primary outcomes but increased risk in triple-positive); avoid in triple-positive or LA-positive patients
- **Aspirin 75-100 mg/day:** Added to warfarin for arterial APS; or monotherapy for primary thromboprophylaxis in asymptomatic aPL positivity

**Obstetric APS:**
- **LMWH (prophylactic doses) + aspirin 75-100 mg/day** throughout pregnancy and 6-12 weeks post-partum
- Full-dose LMWH for prior thrombotic APS
- Refractory obstetric APS: IVIG, hydroxychloroquine, low-dose prednisone (evidence limited)
- Pravastatin: under investigation for obstetric APS (anti-inflammatory and anti-thrombotic effects)

**Catastrophic APS (CAPS):**
- **Immediate anticoagulation** (heparin IV → LMWH) — mainstay
- **High-dose corticosteroids** (methylprednisolone 500-1000 mg/day × 3 days then oral taper) — for immune component and adrenal insufficiency
- **IVIG** (2 g/kg over 5 days) — immunomodulation; removal of aPL
- **Plasmapheresis** — aPL removal + fresh frozen plasma replacement
- **Eculizumab** (anti-C5; off-label): case series support for refractory CAPS — blocks terminal complement
- **Rituximab** (anti-CD20; off-label): depletes aPL-producing B cells; used for refractory CAPS and chronic thrombocytopenia

**Secondary prophylaxis and risk reduction:**
- **Hydroxychloroquine (HCQ):** Reduces aPL titers and thrombotic risk in all SLE+aPL patients; reduces aPL levels in primary APS; recommended broadly
- **Statin therapy:** Modulates endothelial activation and aPL-mediated TF expression
- **Estrogen avoidance:** Combined OCP contraindicated in APS; progesterone-only or IUD preferred
- **Treat modifiable CV risk factors:** BP control, smoking cessation, weight loss

## Connections

- `connects-to` → **[Beta-2 Glycoprotein I](../../03-molecular/beta2-glycoprotein-1/README.md)** — Anti-B2GPI IgG (domain I-specific; R39-R43 epitope) are the highest-risk pathogenic antibody in APS; B2GPI on phospholipid surfaces is the cofactor for anti-cardiolipin binding; triple aPL positivity (LA + aCL + anti-B2GPI) confers >10% annual thrombotic risk.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — APS is driven by IgG antiphospholipid antibodies (anti-B2GPI IgG, anti-cardiolipin IgG, lupus anticoagulant); IgG titers correlate with thrombotic risk; NOACs (rivaroxaban, dabigatran) are inferior to warfarin in APS (TRAPS trial); FcRn inhibitors under investigation.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Complement activation is central to APS thrombosis: anti-B2GPI → C3b deposition → C5a → neutrophil/platelet priming and TF expression; C5 inhibition (eculizumab) is used off-label for catastrophic APS (CAPS; ~37% mortality) refractory to anticoagulation and plasmapheresis.
- `connects-to` → **[Systemic Lupus Erythematosus](../../07-system/systemic-lupus-erythematosus/README.md)** — Secondary APS occurs in ~30% of SLE patients with persistent aPL; SLE+APS patients have higher stroke/DVT risk than either condition alone; hydroxychloroquine is recommended in all SLE+aPL patients; the 2023 ACR/EULAR APS classification criteria incorporate SLE as a risk modifier.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — APS causes recurrent DVT/PE in young adults; triple-positive aPL (LA + aCL + anti-B2GPI) confers >10% annual VTE risk; warfarin INR 2-3 is superior to DOACs in APS (TRAPS: rivaroxaban doubled arterial event risk vs. warfarin in triple-positive patients); indefinite anticoagulation recommended.
- `connects-to` → **[Inherited Thrombophilia](../inherited-thrombophilia/README.md)** — APS and inherited thrombophilias (FV Leiden, prothrombin G20210A, protein C/S or AT deficiency) both cause recurrent VTE in young adults; co-existing aPL with thrombophilic mutations compounds risk multiplicatively; test for both in young patients with unexplained DVT/PE.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Antiphospholipid antibodies turn the endothelium prothrombotic: anti-β2GPI immune complexes engage endothelial TLR4 → NF-κB → tissue factor, converting the vessel lining from anticoagulant to clot-promoting — one of three converging hits driving APS thrombosis.
- `connects-to` → **[Stroke](../stroke/README.md)** — Antiphospholipid syndrome is a leading cause of stroke in the young: arterial APS produces ischemic stroke and TIA, so aPL testing is mandatory in stroke under 50, and arterial APS is anticoagulated to a higher INR (2.5-3.5), with warfarin beating DOACs.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — Half of APS is obstetric: antiphospholipid antibodies injure the placenta through both decidual-vessel thrombosis and direct, complement-(C5a)-mediated trophoblast damage, causing recurrent miscarriage, fetal loss, and pre-eclampsia — treated with LMWH plus low-dose aspirin.

[^miyakis-2006-sydney-aps]: Miyakis S, Lockshin MD, Atsumi T, et al. International consensus statement on an update of the classification criteria for definite antiphospholipid syndrome (APS). *J Thromb Haemost.* 2006;4(2):295-306. [doi:10.1111/j.1538-7836.2006.01753.x](https://doi.org/10.1111/j.1538-7836.2006.01753.x) · [PubMed 16420554](https://pubmed.ncbi.nlm.nih.gov/16420554/)
[^barbhaiya-2023-acreular-aps]: Barbhaiya M, Zuily S, Naden R, et al. The 2023 ACR/EULAR antiphospholipid syndrome classification criteria. *Ann Rheum Dis.* 2023;82(10):1258-1270. [doi:10.1136/ard-2023-224609](https://doi.org/10.1136/ard-2023-224609) · [PubMed 37643823](https://pubmed.ncbi.nlm.nih.gov/37643823/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
