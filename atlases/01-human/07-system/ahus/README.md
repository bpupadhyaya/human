---
schema: human-scale-entry/v1
id: ahus
name: Atypical HUS
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Atypical hemolytic uremic syndrome (aHUS) is a complement-mediated thrombotic microangiopathy (MAHA + thrombocytopenia + AKI); Factor H mutations are most common (20-30%); uncontrolled alternative pathway at renal endothelium → microthrombi. Eculizumab is standard of care."
aliases: ["aHUS", "atypical HUS", "atypical hemolytic uremic syndrome", "complement-mediated TMA", "CFH-HUS", "HUS", "thrombotic microangiopathy complement"]
sources:
  - id: fakhouri-2017-ahus-lancet
    type: peer-reviewed
    cite: "Fakhouri F, Zuber J, Frémeaux-Bacchi V, Loirat C. Haemolytic uraemic syndrome. Lancet. 2017;390(10095):681-696."
    doi: "10.1016/S0140-6736(17)30062-4"
    pmid: "28242109"
    url: "https://doi.org/10.1016/S0140-6736(17)30062-4"
  - id: legendre-2013-eculizumab-ahus-nejm
    type: peer-reviewed
    cite: "Legendre CM, Licht C, Muus P, et al. Terminal complement inhibitor eculizumab in atypical hemolytic-uremic syndrome. N Engl J Med. 2013;368(23):2169-2181."
    doi: "10.1056/NEJMoa1208981"
    pmid: "23738544"
    url: "https://doi.org/10.1056/NEJMoa1208981"
  - id: goodship-2017-ahus-consensus
    type: clinical-guideline
    cite: "Goodship TH, Cook HT, Fakhouri F, et al. Atypical hemolytic uremic syndrome and C3 glomerulopathy: conclusions from a 'Kidney Disease: Improving Global Outcomes' (KDIGO) Controversies Conference. Kidney Int. 2017;91(3):539-551."
    doi: "10.1016/j.kint.2016.10.005"
    pmid: "28062089"
    url: "https://doi.org/10.1016/j.kint.2016.10.005"
cross_links:
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "CFH mutations (SCR19-20) are the most common cause of aHUS (~20-30%); Factor H regulates alternative C3 convertase on renal endothelial surfaces; anti-CFH autoantibodies (CFHR1-CFHR3 deletion) cause aHUS in ~6-10%; eculizumab/ravulizumab target downstream C5."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Uncontrolled alternative C3 convertase (C3bBb) from CFH/CFI/CD46 defects → persistent C3 consumption → hypocomplementemia; serum C3 is low-normal in many aHUS cases; C3 nephritic factor (C3NeF) stabilizes C3bBb → C3 glomerulopathy (related complement-mediated nephropathy)."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Uncontrolled alternative complement (from CFH/CFI mutations) generates C5 convertase → C5a (neutrophil priming, endothelial injury) + C5b-9 (MAC → TMA); eculizumab (anti-C5 mAb) and ravulizumab block C5 → normalize platelets and renal function in >80% of aHUS patients."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "aHUS causes progressive CKD from repeated TMA episodes; ~50% of untreated patients reach ESRD within 1 year; eculizumab/ravulizumab prevent and partially reverse renal injury; renal transplant in aHUS requires continued C5 inhibition to prevent TMA recurrence in the allograft."
  - target: 01-human/03-molecular/adamts13
    relation: connects-to
    note: "ADAMTS13 activity is the first test to exclude TTP from the aHUS differential; in TMA workup, ADAMTS13 <10% = TTP → plasma exchange + caplacizumab, NOT eculizumab; ADAMTS13 ≥10% + complement workup → aHUS; the distinction is critical since treatments are non-interchangeable."
  - target: 01-human/07-system/thrombotic-thrombocytopenic-purpura
    relation: connects-to
    note: "TTP (ADAMTS13 <10%) is the primary differential diagnosis of aHUS; both cause TMA (MAHA + thrombocytopenia + AKI) but TTP is treated with plasma exchange + caplacizumab and aHUS with eculizumab; TTP tends to spare the kidneys more; aHUS tends to dominate with AKI over neuro."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "The kidney is aHUS's main target: uncontrolled alternative complement strikes the glomerular endothelium, seeding microthrombi that occlude capillaries → acute kidney injury and, over repeated episodes, CKD and ESRD; aHUS recurs in transplants unless C5 inhibition continues."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "aHUS is a disease of the glomerular endothelial cell: because mutant Factor H cannot be recruited to the cell surface, the alternative pathway runs unchecked there → MAC sublytically injures the endothelium → VWF release and platelet adhesion → the microthrombi of TMA."
  - target: 02-pathogen/02-bacteria/escherichia-coli
    relation: connects-to
    note: "aHUS must be separated from typical HUS caused by Shiga-toxin-producing E. coli: STEC-HUS follows bloody diarrhoea, hits young children, is usually self-limited, and does not respond to eculizumab — whereas complement-driven aHUS does, making the stool toxin test a key fork."
  - target: 01-human/07-system/gvhd
    relation: connects-to
    note: "aHUS and transplant-associated TMA (TA-TMA) in GVHD overlap: both injure endothelium and activate complement to drive microvascular thrombosis with schistocytes, thrombocytopenia and kidney injury; complement variants predispose to TA-TMA, and C5 inhibition can treat both."
  - target: 01-human/07-system/pnh
    relation: connects-to
    note: "aHUS and PNH are the archetypal complement-mediated diseases treated by C5 blockade: PNH lacks GPI-anchored complement regulators causing hemolysis and thrombosis, while aHUS has uncontrolled alternative-pathway activation on endothelium causing TMA; eculizumab transformed both."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "aHUS is a thrombotic microangiopathy that consumes platelets: complement-injured endothelium triggers platelet adhesion and microthrombi in the renal microvasculature, dropping the count while sparing large vessels; consumed platelets and schistocytes are diagnostic clues."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "aHUS shreds red cells like all thrombotic microangiopathies: erythrocytes passing through complement-damaged, microthrombus-laden glomerular capillaries fragment into schistocytes, producing the hemolytic anemia that, with thrombocytopenia and AKI, defines the TMA triad."
  - target: 01-human/07-system/disseminated-intravascular-coagulation
    relation: connects-to
    note: "aHUS and DIC both cause thrombocytopenia with microthrombi but differ in coagulation: DIC consumes clotting factors with prolonged PT/PTT, while aHUS is complement-driven with normal clotting times—so normal coagulation amid a microangiopathy points to aHUS."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "Lupus can trigger a secondary thrombotic microangiopathy resembling aHUS: complement activation and antiphospholipid antibodies in SLE injure endothelium and cause a TMA, so distinguishing aHUS from lupus or TTP guides eculizumab vs immunosuppression vs plasma exchange."
  - target: 01-human/07-system/heparin-induced-thrombocytopenia
    relation: connects-to
    note: "aHUS and HIT both cause thrombocytopenia with thrombosis but by different mechanisms: aHUS is uncontrolled complement attacking endothelium, while HIT is PF4-heparin antibodies activating platelets—both consume platelets while clotting, needing different treatment."
  - target: 01-human/07-system/immune-thrombocytopenia
    relation: connects-to
    note: "aHUS and immune thrombocytopenia both lower platelets but differ fundamentally: aHUS consumes platelets in complement-driven microthrombi, while ITP is isolated antibody-mediated platelet destruction—the smear and renal function separate them."
  - target: 01-human/07-system/malaria
    relation: connects-to
    note: "aHUS and severe malaria can both present as thrombotic microangiopathy: malaria's infected red cells and inflammation damage the microvasculature much as complement does in aHUS—so in endemic areas falciparum infection enters the differential of TMA."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "aHUS strikes the glomerulus hardest: uncontrolled complement injures glomerular endothelium, triggering the thrombotic microangiopathy that shears red cells and clogs capillaries—so renal failure with microangiopathic hemolysis is the disease's hallmark."
  - target: 01-human/03-molecular/von-willebrand-factor
    relation: connects-to
    note: "aHUS shares thrombotic-microangiopathy machinery with TTP via von Willebrand factor: complement-injured endothelium releases ultralarge VWF multimers that snare platelets into microthrombi—the same VWF that ADAMTS13 deficiency unleashes in TTP."
  - target: 01-human/04-cellular/podocyte
    relation: connects-to
    note: "aHUS injures the glomerular filter including its podocytes: complement-driven endothelial damage and microthrombi disrupt the filtration barrier, contributing to the proteinuria, hematuria and progressive renal failure that mark the disease."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "Pregnancy can trigger atypical HUS: the complement stress of pregnancy and especially the postpartum period unmasks aHUS in women with regulatory mutations, so a thrombotic microangiopathy around delivery must be distinguished from pre-eclampsia and HELLP."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "Severe hypertension and aHUS form a vicious circle: complement-driven microvascular injury in the kidney drives malignant hypertension, and the high pressure further shears endothelium—so accelerated hypertension can both trigger and result from the microangiopathy."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "aHUS is not confined to the kidney—it can strike the brain: complement-mediated microthrombi in cerebral vessels cause seizures, confusion, and stroke, so neurological signs in a thrombotic microangiopathy mark severe, extrarenal aHUS needing urgent complement blockade."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "aHUS is driven by runaway complement reaching C5a: uncontrolled activation cleaves C5 to C5a, which through its receptor C5aR1 inflames and injures endothelium—why C5-blocking eculizumab transformed this once-lethal disease."
  - target: 01-human/03-molecular/thrombin
    relation: connects-to
    note: "aHUS is a thrombotic microangiopathy fueled by thrombin: complement-injured endothelium becomes prothrombotic, generating thrombin and platelet-fibrin microthrombi that shred red cells and clog the kidney's small vessels."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Complement's C5a recruits neutrophils that worsen aHUS: drawn to the activated endothelium, neutrophils release enzymes and oxidants that amplify the microvascular injury, linking the complement defect to the destructive inflammation in the kidney."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "aHUS is the 'H' of hemolytic-uremic: uncontrolled complement injures small-vessel endothelium, and the fibrin and platelet strands shear passing red cells (microangiopathic hemolysis), spilling hemoglobin and producing schistocytes."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "aHUS damages the kidney enough to raise potassium: complement-driven microthrombi block glomerular capillaries, causing the acute kidney injury that—with hemolysis releasing potassium—drives dangerous hyperkalemia needing urgent care."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages clean up aHUS's destroyed red cells: as complement shears erythrocytes, splenic and hepatic macrophages clear the damaged cells and free hemoglobin, the reticuloendothelial cleanup behind the hemolytic anemia of the disease."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "aHUS can strike the heart: the same complement-driven microthrombi that clog the kidney lodge in cardiac vessels, causing ischemia and cardiomyopathy, one of the extrarenal manifestations that mark severe disease."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "aHUS chokes off oxygen across organs: widespread microvascular clots block blood flow while the hemolytic anemia leaves less to carry oxygen, so tissues throughout the body are starved during an acute episode."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "aHUS can injure the pancreas: microthrombi in its small vessels cause ischemic pancreatitis and can disturb blood sugar, another extrarenal site of the thrombotic microangiopathy that defines the disease."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "aHUS is confirmed on the kidney biopsy under the microscope: thrombotic microangiopathy—fibrin clots and swollen endothelium in the glomeruli, read in light—distinguishes it from other causes of failing kidneys."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Recurrent aHUS scars the kidney: repeated thrombotic injury heals with glomerular and interstitial fibrosis, driving the chronic kidney disease that can follow even after attacks are controlled."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "aHUS can injure the gut: mesenteric microthrombi cause abdominal pain and ischemic colitis, part of the multi-organ thrombotic reach that sets it apart from a purely renal disease."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reveals aHUS's lesion in the kidney's filters: the glomerular endothelium swells and lifts off, widening the subendothelial space and trapping platelet-fibrin microthrombi — the thrombotic microangiopathy unchecked complement drives."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "The complement storm can reach the lungs: aHUS occasionally causes pulmonary thrombotic microangiopathy with hemorrhage and respiratory failure, evidence its endothelial injury is systemic, not confined to the kidney."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "aHUS can blur the eye: microthrombi and the malignant hypertension it provokes injure the retinal vessels, producing a Purtscher-like retinopathy of cotton-wool spots and hemorrhages that can threaten vision."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "aHUS reaches the brain through its tiniest vessels: microthrombi in the cerebral microcirculation injure neurons, causing the seizures, confusion, and stroke that complicate severe disease in up to half of patients."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Some aHUS is antibody-made: a subset is driven by autoantibodies against complement factor H (often with CFHR deletions), and the disease's mainstay treatment, eculizumab, is itself a monoclonal antibody that blocks C5."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The microangiopathy can scar more than the kidney: aHUS is a systemic TMA, and clots in the hepatic and mesenteric microvessels can derange the liver and bowel as part of its multi-organ reach."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Pregnancy is a classic trigger: complement-mediated aHUS often erupts in the peripartum period, especially postpartum, and must be told apart from HELLP and preeclampsia, which it can closely mimic in a sick mother."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "The damage remodels the small arteries: aHUS injures arterioles into the concentric 'onion-skin' thickening of smooth-muscle and matrix layers, the chronic vascular lesion of thrombotic microangiopathy seen on biopsy."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Microthrombi reach the brain: aHUS is not confined to the kidney — clots in the cerebral microvessels cause seizures, encephalopathy, and stroke, the CNS face of its systemic thrombotic microangiopathy."
---

# Atypical HUS

## Overview

**Atypical hemolytic uremic syndrome (aHUS)** is a **thrombotic microangiopathy (TMA)** caused by **uncontrolled activation of the complement alternative pathway**, primarily at the glomerular endothelium. It presents with the classic TMA triad:
1. **Microangiopathic hemolytic anemia (MAHA):** Schistocytes, elevated LDH, low/absent haptoglobin, Coombs-negative
2. **Thrombocytopenia:** Platelet consumption in microthrombi
3. **Acute kidney injury (AKI):** From glomerular microvascular occlusion

aHUS is distinguished from **STEC-HUS** (Shiga-toxin–producing *E. coli* HUS; more common, especially in children, self-limited) and **TTP** (ADAMTS13 deficiency; predominantly neurological) — all three are TMAs but have distinct mechanisms, prognosis, and treatment [^fakhouri-2017-ahus-lancet].

**Epidemiology:**
- Incidence: ~1-2 per million/year; affects all ages (children and adults; bimodal distribution)
- ~40-60% have identifiable complement gene mutations; ~6-10% have anti-CFH antibodies; ~30-40% have no identified mutation ("unknown/idiopathic")
- Without treatment: ~50% reach ESRD within 1 year; ~25% die in the acute phase
- With eculizumab: >80% achieve hematologic normalization and renal recovery [^legendre-2013-eculizumab-ahus-nejm]

## Structure

### Genetic causes and complement proteins

**Frequency of complement gene mutations in aHUS:**

| Gene | Protein | Mechanism | Frequency | Notes |
|:-----|:--------|:----------|:----------|:------|
| **CFH** | Factor H | Loss-of-function (SCR19-20 hotspot) → impaired surface C3b regulation | ~20-30% | Most common; SCR19-20 mutations disrupt surface-specific regulation |
| **CD46 (MCP)** | Membrane Cofactor Protein | Loss-of-function → reduced Factor I cofactor on cell surface | ~5-15% | Good prognosis with eculizumab; high recurrence post-transplant without it |
| **CFI** | Factor I | Loss-of-function → loss of C3b inactivation (iC3b generation impaired) | ~5-10% | Phenotypically indistinguishable from CFH-aHUS |
| **C3** | Complement C3 | Gain-of-function → C3b resistant to Factor H/I regulation | ~5% | Associated with C3 glomerulopathy overlap |
| **CFB** | Factor B | Gain-of-function → hyperactive C3 convertase (C3bBb more stable) | ~2% | Rare; often severe infantile presentation |
| **THBD** | Thrombomodulin | Loss-of-function → reduced complement regulation on endothelium | ~3-5% | Triggers TMA at endothelial level |
| **Anti-CFH antibodies** | — | Autoimmune blockade of Factor H surface binding | ~6-10% | Predominantly children; CFHR1-CFHR3 homozygous deletion predisposes |

**Key insight:** Most mutations impair the ability of host cells to **recruit Factor H to their surface** (not fluid-phase regulation) — this explains why complement levels (C3, C4) can be normal or mildly reduced in aHUS, unlike C3 deficiency states.

### Pathophysiological cascade

```
CFH/CFI/CD46 mutation (or anti-CFH antibody)
        ↓
Impaired surface C3b regulation on glomerular endothelium
        ↓
C3b amplification → C3bBb (alternative C3 convertase) not inactivated
        ↓
C3bBbC3b (alternative C5 convertase) → C5 cleavage
        ↓
C5a: neutrophil priming → TF expression → pro-thrombotic state
C5b-9 (MAC): sublytic endothelial injury → VWF release → platelet adhesion
        ↓
Intravascular microthrombi (platelets + fibrin) in glomerular capillaries
        ↓
Glomerular occlusion → AKI  +  RBC fragmentation → MAHA  +  Platelet consumption → thrombocytopenia
        ↓
Repeated TMA episodes → glomerular fibrosis → CKD → ESRD
```

**Common triggers for aHUS episodes:**
- Infections (upper respiratory, GI — especially in children; infection activates complement independently)
- Pregnancy (especially peripartum; pregnancy + complement mutation → severe TMA)
- Combined oral contraceptives (OCP → complement activation + endothelial stress)
- Vaccination (rare)
- Malignancy
- Solid organ transplantation (donor organ → ischemia-reperfusion → complement activation)

## Function

### Diagnosis

**The diagnostic challenge:** aHUS is a diagnosis of exclusion — TTP and STEC-HUS must be ruled out first.

**Step-by-step diagnostic workup:**

1. **Confirm TMA:** CBC (low platelets, anemia), blood smear (schistocytes ≥1% → MAHA), LDH (elevated), haptoglobin (undetectable), Coombs test (negative), creatinine (elevated)

2. **Exclude TTP (priority):**
   - **ADAMTS13 activity:** <10% → TTP; ≥10% → not TTP; send URGENTLY (treatment differs fundamentally — TTP needs PEX, not eculizumab)
   - Anti-ADAMTS13 antibodies (in immune TTP)

3. **Exclude STEC-HUS:**
   - Stool cultures and O157:H7 Shiga toxin PCR
   - STEC-HUS: usually age <5 years, prodromal bloody diarrhea, seasonal (summer), no family history, self-limited without eculizumab

4. **Complement workup (once TTP excluded):**

| Test | Interpretation |
|:-----|:--------------|
| Serum C3 | Low-normal in ~40-50% of aHUS (not always abnormal) |
| Serum C4 | Normal (alternative pathway activation; C4 not consumed) |
| Factor H antigen | Low → type I CFH mutation or anti-CFH antibodies; normal → type II (SCR19-20 functional mutation) |
| Factor H functional activity | Low → loss-of-function mutation |
| Factor I antigen + activity | Low → CFI mutation |
| CD46 (MCP) on neutrophils (flow) | Reduced → CD46 mutation |
| Anti-CFH antibodies | Present → autoimmune aHUS (CFHR1-CFHR3 deletion) |
| Complement genetic panel (CFH, CFI, CD46, C3, CFB, THBD, CFHRs) | Gold standard; guides long-term therapy and recurrence risk |

5. **Renal biopsy (when diagnosis uncertain):**
   - Characteristic: TMA histology — fibrin/platelet thrombi in glomerular capillaries; endothelial swelling; ischemic glomerular collapse
   - No immune deposits (distinguishes from immune complex GN)
   - May show MPGN pattern if C3 glomerulopathy overlap

**Differential diagnosis of TMA:**

| Feature | aHUS | TTP | STEC-HUS | HELLP/obstetric TMA |
|:--------|:-----|:----|:---------|:--------------------|
| Mechanism | Complement | ADAMTS13 deficiency | Shiga toxin | Placental/hormonal |
| Age | All | Adults (F > M) | <5 years | Pregnant/peripartum |
| Diarrhea | No | No | Yes (bloody) | No |
| Neurological sx | Mild | Dominant | Minimal | Variable |
| Renal sx | Dominant | Mild | Dominant | Variable |
| ADAMTS13 activity | ≥10% | <10% | ≥10% | ≥10% |
| C3 | Low-normal | Normal | Normal | Normal |
| Stool Shiga toxin | Negative | Negative | Positive | Negative |
| Family history | Often positive | No | No | No |
| Treatment | Eculizumab | PEX + immunosuppression | Supportive | Delivery |

## Pathology

### Acute treatment [^legendre-2013-eculizumab-ahus-nejm]

**Eculizumab (Soliris) — standard of care:**
- **Dose:** 900 mg IV weekly × 4, then 1200 mg IV every 2 weeks (adults); weight-based dosing in pediatrics
- **Mechanism:** Anti-C5 monoclonal antibody (humanized IgG2/4κ); blocks C5 cleavage → prevents C5a and C5b-9 generation
- **Efficacy (NEJM 2013):** Platelet normalization in 80-88% within 1 week; eGFR improvement in 65-80%; complete TMA response in 75%
- **Meningococcal prophylaxis MANDATORY:** Eculizumab blocks terminal complement → prevents lysis of encapsulated bacteria → *N. meningitidis* risk ×1000-2000×; **vaccinate with MenACWY + MenB ≥2 weeks before first dose; if urgent: prophylactic antibiotics (penicillin/ciprofloxacin) from day 1**
- **Duration:** Typically lifelong for high-risk mutations (CFH, CFI); trial discontinuation possible for CFH-antibody aHUS after titer suppression and in some CD46 patients with close monitoring

**Ravulizumab (Ultomiris) — long-acting C5 inhibitor:**
- Same efficacy as eculizumab; half-life extended by FcRn recycling modification (Met428Leu, Asn434Ser in Fc)
- **Dose:** Weight-based IV loading, then maintenance Q8W (adults); reduces infusion burden significantly
- FDA approved for aHUS 2019; now preferred for many patients

**Before eculizumab — Plasma Exchange (PEX):**
- PEX (or FFP infusion) replenishes Factor H in plasma → may temporarily stabilize complement
- Still used: (1) diagnostic uncertainty (covers TTP while ADAMTS13 returns); (2) anti-CFH antibody aHUS (removes antibody)
- Do NOT delay eculizumab for PEX if diagnosis of aHUS is clear

**Anti-CFH antibody aHUS — additional treatment:**
- Plasma exchange (removes antibody + replenishes CFH) + immunosuppression (rituximab, mycophenolate) → reduce antibody titer
- Eculizumab continues to block downstream C5 while antibody is cleared
- Goal: antibody-negative remission → consider weaning eculizumab

### Renal transplantation

**aHUS recurs in transplant kidneys** (the genetic defect persists → same endothelial vulnerability in allograft):
- **CFH mutations:** ~75-90% recurrence without C5 inhibition → prohibitive without eculizumab coverage
- **CD46 mutations:** <15% recurrence (donor kidney has normal CD46; patient's circulating complement is sufficient with normal CD46)
- **CFI mutations:** ~50-70% recurrence
- **Anti-CFH antibody aHUS:** Continue immunosuppression + eculizumab perioperatively → antibody-negative remission required before transplant
- **Standard:** Eculizumab prophylaxis on day of transplant + continued maintenance for high-risk genotypes; may allow discontinuation in low-risk mutations after 6-12 months

**Liver transplantation for CFH aHUS:**
- CFH is synthesized primarily in the liver → liver transplant (or combined liver-kidney for ESRD) could theoretically cure CFH-aHUS
- High surgical risk; pursued rarely in children refractory to eculizumab; eculizumab bridge perioperatively essential

### Long-term monitoring

- Monthly: CBC, creatinine, LDH, haptoglobin, urinalysis while on eculizumab
- Complement C3, C4, factor H levels: periodically (especially after eculizumab discontinuation trial)
- Renal function: eGFR every 3-6 months
- Screen first-degree relatives with complement genetic panel (autosomal dominant CFH/CFI/C3/CFB mutations; ~50% penetrance)

## Connections

- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — CFH mutations (SCR19-20) are the most common cause of aHUS (~20-30%); Factor H regulates alternative C3 convertase on renal endothelial surfaces; anti-CFH autoantibodies (CFHR1-CFHR3 deletion) cause aHUS in ~6-10%; eculizumab/ravulizumab target downstream C5.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Uncontrolled alternative C3 convertase (C3bBb) from CFH/CFI/CD46 defects → persistent C3 consumption → hypocomplementemia; serum C3 is low-normal in many aHUS cases; C3 nephritic factor (C3NeF) stabilizes C3bBb → C3 glomerulopathy (related complement-mediated nephropathy).
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Uncontrolled alternative complement (from CFH/CFI mutations) generates C5 convertase → C5a (neutrophil priming, endothelial injury) + C5b-9 (MAC → TMA); eculizumab (anti-C5 mAb) and ravulizumab block C5 → normalize platelets and renal function in >80% of aHUS patients.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — aHUS causes progressive CKD from repeated TMA episodes; ~50% of untreated patients reach ESRD within 1 year; eculizumab/ravulizumab prevent and partially reverse renal injury; renal transplant in aHUS requires continued C5 inhibition to prevent TMA recurrence in the allograft.
- `connects-to` → **[ADAMTS13](../../03-molecular/adamts13/README.md)** — ADAMTS13 activity is the first test to exclude TTP from the aHUS differential; in TMA workup, ADAMTS13 <10% = TTP → plasma exchange + caplacizumab, NOT eculizumab; ADAMTS13 ≥10% + complement workup → aHUS; the distinction is critical since treatments are non-interchangeable.
- `connects-to` → **[Thrombotic Thrombocytopenic Purpura](../thrombotic-thrombocytopenic-purpura/README.md)** — TTP (ADAMTS13 <10%) is the primary differential diagnosis of aHUS; both cause TMA (MAHA + thrombocytopenia + AKI) but TTP is treated with plasma exchange + caplacizumab and aHUS with eculizumab; TTP tends to spare the kidneys more; aHUS tends to dominate with AKI over neuro.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — The kidney is aHUS's main target: uncontrolled alternative complement strikes the glomerular endothelium, seeding microthrombi that occlude capillaries → acute kidney injury and, over repeated episodes, CKD and ESRD; aHUS recurs in transplants unless C5 inhibition continues.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — aHUS is a disease of the glomerular endothelial cell: because mutant Factor H cannot be recruited to the cell surface, the alternative pathway runs unchecked there → MAC sublytically injures the endothelium → VWF release and platelet adhesion → the microthrombi of TMA.
- `connects-to` → **[Escherichia coli](../../../02-pathogen/02-bacteria/escherichia-coli/README.md)** — aHUS must be separated from typical HUS caused by Shiga-toxin-producing E. coli: STEC-HUS follows bloody diarrhoea, hits young children, is usually self-limited, and does not respond to eculizumab — whereas complement-driven aHUS does, making the stool toxin test a key fork.
- `connects-to` → **[Graft-Versus-Host Disease](../gvhd/README.md)** — aHUS and transplant-associated TMA (TA-TMA) in GVHD overlap: both injure endothelium and activate complement to drive microvascular thrombosis with schistocytes, thrombocytopenia and kidney injury; complement variants predispose to TA-TMA, and C5 inhibition can treat both.
- `connects-to` → **[Paroxysmal Nocturnal Hemoglobinuria](../pnh/README.md)** — aHUS and PNH are the archetypal complement-mediated diseases treated by C5 blockade: PNH lacks GPI-anchored complement regulators causing hemolysis and thrombosis, while aHUS has uncontrolled alternative-pathway activation on endothelium causing TMA; eculizumab transformed both.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — aHUS is a thrombotic microangiopathy that consumes platelets: complement-injured endothelium triggers platelet adhesion and microthrombi in the renal microvasculature, dropping the count while sparing large vessels; consumed platelets and schistocytes are diagnostic clues.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — aHUS shreds red cells like all thrombotic microangiopathies: erythrocytes passing through complement-damaged, microthrombus-laden glomerular capillaries fragment into schistocytes, producing the hemolytic anemia that, with thrombocytopenia and AKI, defines the TMA triad.
- `connects-to` → **[Disseminated Intravascular Coagulation](../disseminated-intravascular-coagulation/README.md)** — aHUS and DIC both cause thrombocytopenia with microthrombi but differ in coagulation: DIC consumes clotting factors with prolonged PT/PTT, while aHUS is complement-driven with normal clotting times—so normal coagulation amid a microangiopathy points to aHUS.
- `connects-to` → **[Systemic Lupus Erythematosus](../systemic-lupus-erythematosus/README.md)** — Lupus can trigger a secondary thrombotic microangiopathy resembling aHUS: complement activation and antiphospholipid antibodies in SLE injure endothelium and cause a TMA, so distinguishing aHUS from lupus or TTP guides eculizumab vs immunosuppression vs plasma exchange.
- `connects-to` → **[Heparin-Induced Thrombocytopenia](../heparin-induced-thrombocytopenia/README.md)** — aHUS and HIT both cause thrombocytopenia with thrombosis but by different mechanisms: aHUS is uncontrolled complement attacking endothelium, while HIT is PF4-heparin antibodies activating platelets—both consume platelets while clotting, needing different treatment.
- `connects-to` → **[Immune Thrombocytopenia](../immune-thrombocytopenia/README.md)** — aHUS and immune thrombocytopenia both lower platelets but differ fundamentally: aHUS consumes platelets in complement-driven microthrombi, while ITP is isolated antibody-mediated platelet destruction—the smear and renal function separate them.
- `connects-to` → **[Malaria](../malaria/README.md)** — aHUS and severe malaria can both present as thrombotic microangiopathy: malaria's infected red cells and inflammation damage the microvasculature much as complement does in aHUS—so in endemic areas falciparum infection enters the differential of TMA.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — aHUS strikes the glomerulus hardest: uncontrolled complement injures glomerular endothelium, triggering the thrombotic microangiopathy that shears red cells and clogs capillaries—so renal failure with microangiopathic hemolysis is the disease's hallmark.
- `connects-to` → **[Von Willebrand Factor](../../03-molecular/von-willebrand-factor/README.md)** — aHUS shares thrombotic-microangiopathy machinery with TTP via von Willebrand factor: complement-injured endothelium releases ultralarge VWF multimers that snare platelets into microthrombi—the same VWF that ADAMTS13 deficiency unleashes in TTP.
- `connects-to` → **[Podocyte](../../04-cellular/podocyte/README.md)** — aHUS injures the glomerular filter including its podocytes: complement-driven endothelial damage and microthrombi disrupt the filtration barrier, contributing to the proteinuria, hematuria and progressive renal failure that mark the disease.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — Pregnancy can trigger atypical HUS: the complement stress of pregnancy and especially the postpartum period unmasks aHUS in women with regulatory mutations, so a thrombotic microangiopathy around delivery must be distinguished from pre-eclampsia and HELLP.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — Severe hypertension and aHUS form a vicious circle: complement-driven microvascular injury in the kidney drives malignant hypertension, and the high pressure further shears endothelium—so accelerated hypertension can both trigger and result from the microangiopathy.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — aHUS is not confined to the kidney—it can strike the brain: complement-mediated microthrombi in cerebral vessels cause seizures, confusion, and stroke, so neurological signs in a thrombotic microangiopathy mark severe, extrarenal aHUS needing urgent complement blockade.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — aHUS is driven by runaway complement reaching C5a: uncontrolled activation cleaves C5 to C5a, which through its receptor C5aR1 inflames and injures endothelium—why C5-blocking eculizumab transformed this once-lethal disease.
- `connects-to` → **[Thrombin](../../03-molecular/thrombin/README.md)** — aHUS is a thrombotic microangiopathy fueled by thrombin: complement-injured endothelium becomes prothrombotic, generating thrombin and platelet-fibrin microthrombi that shred red cells and clog the kidney's small vessels.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Complement's C5a recruits neutrophils that worsen aHUS: drawn to the activated endothelium, neutrophils release enzymes and oxidants that amplify the microvascular injury, linking the complement defect to the destructive inflammation in the kidney.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — aHUS is the 'H' of hemolytic-uremic: uncontrolled complement injures small-vessel endothelium, and the fibrin and platelet strands shear passing red cells (microangiopathic hemolysis), spilling hemoglobin and producing schistocytes.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — aHUS damages the kidney enough to raise potassium: complement-driven microthrombi block glomerular capillaries, causing the acute kidney injury that—with hemolysis releasing potassium—drives dangerous hyperkalemia needing urgent care.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages clean up aHUS's destroyed red cells: as complement shears erythrocytes, splenic and hepatic macrophages clear the damaged cells and free hemoglobin, the reticuloendothelial cleanup behind the hemolytic anemia of the disease.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — aHUS can strike the heart: the same complement-driven microthrombi that clog the kidney lodge in cardiac vessels, causing ischemia and cardiomyopathy, one of the extrarenal manifestations that mark severe disease.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — aHUS chokes off oxygen across organs: widespread microvascular clots block blood flow while the hemolytic anemia leaves less to carry oxygen, so tissues throughout the body are starved during an acute episode.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — aHUS can injure the pancreas: microthrombi in its small vessels cause ischemic pancreatitis and can disturb blood sugar, another extrarenal site of the thrombotic microangiopathy that defines the disease.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — aHUS is confirmed on the kidney biopsy under the microscope: thrombotic microangiopathy—fibrin clots and swollen endothelium in the glomeruli, read in light—distinguishes it from other causes of failing kidneys.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Recurrent aHUS scars the kidney: repeated thrombotic injury heals with glomerular and interstitial fibrosis, driving the chronic kidney disease that can follow even after attacks are controlled.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — aHUS can injure the gut: mesenteric microthrombi cause abdominal pain and ischemic colitis, part of the multi-organ thrombotic reach that sets it apart from a purely renal disease.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reveals aHUS's lesion in the kidney's filters: the glomerular endothelium swells and lifts off, widening the subendothelial space and trapping platelet-fibrin microthrombi — the thrombotic microangiopathy unchecked complement drives.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — The complement storm can reach the lungs: aHUS occasionally causes pulmonary thrombotic microangiopathy with hemorrhage and respiratory failure, evidence its endothelial injury is systemic, not confined to the kidney.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — aHUS can blur the eye: microthrombi and the malignant hypertension it provokes injure the retinal vessels, producing a Purtscher-like retinopathy of cotton-wool spots and hemorrhages that can threaten vision.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — aHUS reaches the brain through its tiniest vessels: microthrombi in the cerebral microcirculation injure neurons, causing the seizures, confusion, and stroke that complicate severe disease in up to half of patients.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Some aHUS is antibody-made: a subset is driven by autoantibodies against complement factor H (often with CFHR deletions), and the disease's mainstay treatment, eculizumab, is itself a monoclonal antibody that blocks C5.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The microangiopathy can scar more than the kidney: aHUS is a systemic TMA, and clots in the hepatic and mesenteric microvessels can derange the liver and bowel as part of its multi-organ reach.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Pregnancy is a classic trigger: complement-mediated aHUS often erupts in the peripartum period, especially postpartum, and must be told apart from HELLP and preeclampsia, which it can closely mimic in a sick mother.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — The damage remodels the small arteries: aHUS injures arterioles into the concentric 'onion-skin' thickening of smooth-muscle and matrix layers, the chronic vascular lesion of thrombotic microangiopathy seen on biopsy.
- `connects-to` → **[Stroke](../stroke/README.md)** — Microthrombi reach the brain: aHUS is not confined to the kidney — clots in the cerebral microvessels cause seizures, encephalopathy, and stroke, the CNS face of its systemic thrombotic microangiopathy.

[^fakhouri-2017-ahus-lancet]: Fakhouri F, Zuber J, Frémeaux-Bacchi V, Loirat C. Haemolytic uraemic syndrome. *Lancet.* 2017;390(10095):681-696. [doi:10.1016/S0140-6736(17)30062-4](https://doi.org/10.1016/S0140-6736(17)30062-4) · [PubMed 28242109](https://pubmed.ncbi.nlm.nih.gov/28242109/)
[^legendre-2013-eculizumab-ahus-nejm]: Legendre CM, Licht C, Muus P, et al. Terminal complement inhibitor eculizumab in atypical hemolytic-uremic syndrome. *N Engl J Med.* 2013;368(23):2169-2181. [doi:10.1056/NEJMoa1208981](https://doi.org/10.1056/NEJMoa1208981) · [PubMed 23738544](https://pubmed.ncbi.nlm.nih.gov/23738544/)
[^goodship-2017-ahus-consensus]: Goodship TH, Cook HT, Fakhouri F, et al. Atypical hemolytic uremic syndrome and C3 glomerulopathy: conclusions from a KDIGO Controversies Conference. *Kidney Int.* 2017;91(3):539-551. [doi:10.1016/j.kint.2016.10.005](https://doi.org/10.1016/j.kint.2016.10.005) · [PubMed 28062089](https://pubmed.ncbi.nlm.nih.gov/28062089/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
