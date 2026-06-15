---
schema: human-scale-entry/v1
id: thrombotic-thrombocytopenic-purpura
name: Thrombotic Thrombocytopenic Purpura
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "TTP is a life-threatening TMA caused by ADAMTS13 deficiency (<10%); ULVWF-platelet microthrombi → MAHA + thrombocytopenia + end-organ ischemia. Caplacizumab (anti-VWF; FDA 2019) + plasma exchange + rituximab is current first-line; untreated mortality ~90%."
aliases: ["TTP", "thrombotic thrombocytopenic purpura", "iTTP", "immune TTP", "Upshaw-Schulman syndrome", "congenital TTP", "hereditary TTP", "thrombotic microangiopathy TTP", "MAHA TTP"]
sources:
  - id: scully-2019-caplacizumab-hercules
    type: peer-reviewed
    cite: "Scully M, Cataland SR, Peyvandi F, et al. Caplacizumab treatment for acquired thrombotic thrombocytopenic purpura. N Engl J Med. 2019;380(4):335-346."
    doi: "10.1056/NEJMoa1806311"
    pmid: "30625070"
    url: "https://doi.org/10.1056/NEJMoa1806311"
  - id: george-2010-ttp-review
    type: peer-reviewed
    cite: "George JN. Clinical practice. Thrombotic thrombocytopenic purpura. N Engl J Med. 2006;354(18):1927-1935."
    doi: "10.1056/NEJMcp053024"
    pmid: "16672704"
    url: "https://doi.org/10.1056/NEJMcp053024"
  - id: coppo-2019-rituximab-ttp
    type: peer-reviewed
    cite: "Coppo P, Busson M, Veyradier A, et al. HLA-DRB1*11: a strong risk factor for acquired severe ADAMTS13 deficiency-related thrombotic thrombocytopenic purpura in Caucasians. J Thromb Haemost. 2010;8(11):2466-2469."
    doi: "10.1111/j.1538-7836.2010.04028.x"
    pmid: "20735727"
    url: "https://doi.org/10.1111/j.1538-7836.2010.04028.x"
cross_links:
  - target: 01-human/03-molecular/adamts13
    relation: connects-to
    note: "ADAMTS13 deficiency (<10% activity) is the defining pathophysiology of TTP; acquired iTTP: anti-ADAMTS13 IgG4 antibodies; hereditary Upshaw-Schulman syndrome: ADAMTS13 biallelic mutations; caplacizumab blocks VWF A1 domain → prevents ULVWF-platelet binding."
  - target: 01-human/03-molecular/von-willebrand-factor
    relation: connects-to
    note: "ULVWF from Weibel-Palade bodies accumulates in TTP (ADAMTS13 deficiency) → GPIb-mediated platelet aggregation → microthrombi; caplacizumab (anti-VWF A1 nanobody; FDA 2019) blocks ULVWF-platelet tethering → fastest reversal of acute microthrombus formation."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Anti-ADAMTS13 autoantibodies are predominantly IgG4 (inhibiting spacer domain) in iTTP; IgG1 non-inhibiting antibodies accelerate ADAMTS13 clearance; rituximab (anti-CD20) depletes antibody-producing B cells → ADAMTS13 recovery; anti-ADAMTS13 IgG titer guides therapy duration."
  - target: 01-human/07-system/ahus
    relation: connects-to
    note: "TTP (ADAMTS13 <10%) and aHUS (complement gene mutations; ADAMTS13 ≥10%) are the two most important complement/coagulation TMAs: both cause MAHA + thrombocytopenia + AKI; TTP is treated with PEX + caplacizumab + rituximab; aHUS with eculizumab — never interchange these therapies."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "ULVWF binds GPIbα on platelets → platelet-rich microthrombi in arterioles/capillaries → consumption; thrombocytopenia <30,000/μL is characteristic; caplacizumab blocks ULVWF-GPIbα → fastest microthrombus resolution; platelet count >150,000/μL × 2 days marks clinical remission."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "ULVWF-platelet microthrombi → ischemic endothelial injury → local C3 deposition; refractory iTTP shows elevated sC5b-9; TTP-aHUS overlap responds to eculizumab + PEX; C3d/sC5b-9 studied as TTP severity biomarkers; complement distinguishes refractory TTP from typical iTTP."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Endothelial Weibel-Palade bodies store ULVWF; endothelial activation → ULVWF secretion → ADAMTS13 normally cleaves; TTP: ADAMTS13 failure → ULVWF accumulates on endothelial surface → platelet tethering; endothelial injury from microthrombi → ULVWF release → amplification loop."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "The kidney is a TTP target organ: VWF-platelet microthrombi lodge in the renal microvasculature, causing acute kidney injury — usually milder than in aHUS, where renal failure dominates; this difference in renal severity helps separate the two thrombotic microangiopathies."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Neurologic involvement is TTP's most dangerous feature: cerebral microthrombi cause fluctuating confusion, headache, focal deficits, seizures, or coma — part of the classic pentad — that can come and go within hours, so suspected TTP needs urgent plasma exchange."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "TTP shears red cells: as erythrocytes squeeze through platelet-rich microthrombi they fragment into schistocytes, producing microangiopathic hemolytic anemia with high LDH, low haptoglobin, negative Coombs — schistocytes plus thrombocytopenia trigger ADAMTS13 testing."
  - target: 01-human/07-system/immune-thrombocytopenia
    relation: connects-to
    note: "TTP and immune thrombocytopenia both cause severe thrombocytopenia but differ: ITP is antibody-mediated platelet destruction without hemolysis, while TTP adds microangiopathic hemolysis and organ ischemia from ADAMTS13 deficiency—an emergency needing plasma exchange."
  - target: 01-human/07-system/disseminated-intravascular-coagulation
    relation: connects-to
    note: "TTP and DIC both produce thrombocytopenia and schistocytes but are distinguished by coagulation tests: DIC consumes clotting factors and prolongs PT/PTT with high D-dimer, while TTP leaves coagulation times normal—because its clots are platelet-VWF, not fibrin."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "Lupus can trigger or mimic TTP: SLE may produce acquired ADAMTS13 deficiency or a TTP-like thrombotic microangiopathy, and the two share features (hemolysis, low platelets, neuro/renal signs), so a lupus flare with schistocytes demands urgent ADAMTS13 testing."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "TTP can present as stroke: ADAMTS13 deficiency lets VWF-platelet microthrombi lodge in the cerebral microvasculature, causing fluctuating confusion and focal deficits—so an unexplained stroke with thrombocytopenia and hemolysis should trigger urgent TTP work-up."
  - target: 01-human/07-system/antiphospholipid-syndrome
    relation: connects-to
    note: "TTP and catastrophic antiphospholipid syndrome are both thrombotic microangiopathies occluding small vessels: TTP from ADAMTS13 deficiency, CAPS from antiphospholipid antibodies—overlapping clinically, so antibody testing helps separate these emergencies."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "HIV is a recognized cause of secondary TTP: the infection can trigger ADAMTS13 autoantibodies, producing thrombotic microangiopathy—so a new TTP diagnosis warrants HIV testing, and antiretroviral therapy plus plasma exchange treats the HIV-associated form."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Plasma cells make the anti-ADAMTS13 antibody behind acquired TTP: long-lived autoantibody-secreting cells block the enzyme that cleaves von Willebrand factor, so giant VWF multimers clump platelets—why plasma exchange (removing antibody) and rituximab treat TTP."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "The heart is a major, underrecognized TTP target: microthrombi in coronary microvasculature cause troponin rise, arrhythmia and sudden death, so cardiac involvement is a leading cause of TTP mortality—reason to start plasma exchange urgently on suspicion."
  - target: 01-human/03-molecular/thrombin
    relation: connects-to
    note: "TTP clots without activating thrombin: unlike DIC, the microthrombi are platelet-VWF aggregates formed without triggering the coagulation cascade, so thrombin generation and clotting times stay normal—distinguishing it from consumptive coagulopathy."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Acquired TTP is autoantibody-driven, so B cells are a treatment target: rituximab (anti-CD20) depletes the B cells making anti-ADAMTS13 antibodies, raising enzyme levels, preventing relapse, and increasingly used upfront alongside plasma exchange."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Most TTP is autoimmune: the immune system generates IgG autoantibodies against ADAMTS13, crippling the enzyme that cleaves von Willebrand factor—so unchecked VWF multimers trigger platelet microthrombi, distinguishing acquired TTP from the hereditary enzyme deficiency."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "The spleen links to TTP through antibody handling: its reticuloendothelial cells clear autoantibody-coated platelets and produce immunoglobulin, and historically splenectomy was used for refractory or relapsing immune TTP before rituximab became standard."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "Acquired TTP is treated by depleting B cells via CD20: rituximab, an anti-CD20 antibody, removes the B cells making anti-ADAMTS13 autoantibodies, reducing relapse alongside plasma exchange and the anti-vWF nanobody caplacizumab."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "Pregnancy can precipitate TTP: ADAMTS13 activity falls naturally in pregnancy, unmasking congenital deficiency or triggering acquired TTP, so it must be distinguished from preeclampsia and HELLP—a diagnostic challenge with very different treatments."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Acquired TTP is an autoimmune disease needing T-cell help: helper T cells recognizing ADAMTS13 drive B cells to make the inhibitory autoantibodies, so the disorder reflects a breakdown of tolerance to the body's own vWF-cleaving enzyme."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "TTP shreds red cells and spills hemoglobin: platelet-vWF microthrombi slice passing red cells (microangiopathic hemolysis), producing schistocytes, free hemoglobin, low haptoglobin and high LDH—the lab fingerprint that flags the emergency."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Treating TTP with plasma exchange drains calcium: the citrate anticoagulant in the apheresis circuit binds calcium, causing the tingling and cramps of hypocalcemia, so calcium is monitored and replaced during the daily exchanges that are lifesaving."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Acquired TTP is calmed with cortisol: corticosteroids suppress the autoantibody response against ADAMTS13 and are given alongside plasma exchange (with rituximab and caplacizumab) to bring the immune-driven disease under control."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "TTP starves organs of oxygen with platelet microthrombi: clumps of platelets plug small vessels throughout the body, cutting oxygen to brain, heart and kidney, so the ischemic organ damage—not bleeding—drives its danger."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells help start acquired TTP: by presenting ADAMTS13 fragments to T cells they break tolerance, licensing the autoantibodies that disable the enzyme—the autoimmune trigger upstream of the microthrombi."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "TTP can strike the gut with microvascular clots: ischemia of the bowel causes abdominal pain, nausea and even pancreatitis, so gastrointestinal symptoms are common and sometimes the presenting feature of the disease."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "TTP can spill potassium into the blood: brisk microangiopathic hemolysis releases potassium from shattered red cells, and the acute kidney injury compounds it, risking dangerous hyperkalemia."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "TTP can injure the pancreas: microthrombi in its small vessels cause ischemic damage that disturbs blood sugar and raises pancreatic enzymes, another organ the microangiopathy quietly strikes."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "The marrow races to refill what TTP destroys: as microangiopathy shears red cells and consumes platelets, the bone marrow ramps up production, though it cannot keep pace with the relentless destruction."
---

# Thrombotic Thrombocytopenic Purpura

## Overview

**Thrombotic thrombocytopenic purpura (TTP)** is a **life-threatening thrombotic microangiopathy (TMA)** caused by severe **ADAMTS13 deficiency (<10% of normal activity)**, leading to accumulation of ultra-large von Willebrand factor (ULVWF) multimers → platelet-rich microthrombi in arterioles and capillaries → ischemic end-organ injury [^george-2010-ttp-review].

TTP is defined by the **TMA pentad** (though all five features are present in <10% of cases at diagnosis):
1. **Microangiopathic hemolytic anemia (MAHA)** — schistocytes on peripheral blood smear; Coombs-negative; LDH elevated
2. **Thrombocytopenia** — typically <30,000/μL (often <20,000/μL)
3. **Neurological symptoms** — headache, confusion, focal deficits, seizures, coma (cerebral arteriolar microthrombi)
4. **Renal dysfunction** — mild AKI (creatinine elevation); cf. HUS which has severe renal failure
5. **Fever** — present in ~25%; no longer required for diagnosis

**In practice:** The combination of MAHA + thrombocytopenia in a patient without DIC or other obvious TMA cause should prompt **empiric treatment (plasma exchange) before ADAMTS13 results return** — the diagnosis is a clinical emergency.

**Epidemiology:**
- Incidence: ~3-10 per million per year; F>M (~2:1); median age 40 years
- HLA-DRB1*11 is the strongest genetic risk factor for acquired iTTP in European populations
- Triggers: infections (most common), pregnancy (obstetric TTP; first trimester → think congenital; second/third → acquired iTTP), autoimmune disease (SLE, inflammatory bowel disease), HIV, medications (ticlopidine, clopidogrel, quinine — "drug-induced TMA"; ADAMTS13 may or may not be <10%)

## Structure

### Classification of TTP

**Acquired iTTP (immune-mediated; ~95% of TTP cases):**
- Anti-ADAMTS13 IgG autoantibodies inhibit ADAMTS13 activity or accelerate clearance → ADAMTS13 <10%
- Predominantly IgG4 subclass targeting the ADAMTS13 spacer domain (inhibiting); also IgG1 non-inhibiting clearance antibodies
- Episodic: acute event → remission (ADAMTS13 recovers to >50% off therapy) → potential relapse (anti-ADAMTS13 IgG returns)
- Relapse rate: ~30-40% at 5 years without rituximab; <10% with rituximab-based immunosuppression

**Congenital TTP (Upshaw-Schulman syndrome; cTTP; ~5%):**
- Biallelic *ADAMTS13* mutations → absent or severely reduced constitutive ADAMTS13 activity
- Onset: neonatal (unexplained neonatal jaundice + thrombocytopenia) or childhood
- Triggers: pregnancy (ULVWF release from placental endothelium), infections, surgeries
- Treatment: FFP infusion every 2-3 weeks (prophylactic ADAMTS13 replacement); recombinant ADAMTS13 (rADAMTS13; Tasigna; FDA 2023) now available

**TMA differential diagnosis — not TTP:**

| Condition | ADAMTS13 | Key distinguishing features |
|:---------|:---------|:---------------------------|
| TTP | <10% | Neurological dominant; platelet count very low; renal mild |
| HUS (Shiga toxin) | Normal | Shiga toxin + (STEC O157:H7 → bloody diarrhea); severe AKI; complement activation |
| aHUS | Normal | Complement dysregulation (CFH/CFI/C3/MCP mutations); severe AKI; eculizumab treatment |
| DIC | Variable | Elevated PT, D-dimer, fibrinogen consumption; underlying trigger (sepsis, malignancy) |
| Malignant hypertension | Normal | DBP >120 mmHg; hypertensive crisis |
| Drug-induced TMA | Variable | Drug exposure (quinine, gemcitabine, VEGF inhibitors); some ADAMTS13-dependent |
| Pregnancy (HELLP) | Normal (or mildly low) | Preeclampsia features; elevated LFTs; 3rd trimester; resolves with delivery |

### PLASMIC score for iTTP probability

The PLASMIC score guides empiric treatment decisions when ADAMTS13 result is pending:

| Variable | Points |
|:---------|:-------|
| Platelet count <30 × 10⁹/L | 1 |
| Combined hemolysis (reticulocyte >2.5% or haptoglobin undetectable or indirect bilirubin >2 mg/dL) | 1 |
| Absence of active cancer | 1 |
| Absence of stem cell/solid organ transplant | 1 |
| MCV <90 fL | 1 |
| INR <1.5 | 1 |
| Creatinine <2 mg/dL | 1 |
| **Score 6-7 (high probability):** | ADAMTS13 <10% in ~90%; treat empirically with PEX |

## Function

### Normal ADAMTS13 physiology

In healthy individuals, ADAMTS13 (~190 kDa plasma glycoprotein; hepatic synthesis) maintains VWF multimer size by cleaving ULVWF at Tyr1605-Met1606 in the VWF A2 domain under shear stress — preventing spontaneous platelet aggregation in the microcirculation. Normal plasma ADAMTS13 activity: 50-150%; physiological reserve means TTP only manifests when activity falls below ~10%.

## Pathology

### Clinical manifestations

**Neurological (~75% of iTTP):**
- Headache, confusion, aphasia, visual changes → cerebral arteriolar microthrombi
- Fluctuating: relapsing-remitting over hours as microthrombi form and lyse
- Seizures (typically during severe thrombocytopenia/anemia)
- Stroke (hemorrhagic or ischemic; thrombocytopenia + anticoagulation risk)
- **Key teaching:** Neurological symptoms often precede MAHA recognition → TTP must be in the differential for any unexplained acute neurological syndrome + thrombocytopenia

**Hematological:**
- Microangiopathic hemolytic anemia: schistocytes ≥1% on peripheral blood smear (helmet cells, fragmented RBCs from mechanical destruction in narrowed vessels)
- LDH markedly elevated (hemolysis + ischemic tissue damage); haptoglobin undetectable
- Coombs-negative hemolysis (non-immune; cf. Evans syndrome or AIHA)
- Platelet count typically <30,000/μL; often <10,000/μL

**Cardiac:**
- TTP-related cardiac events in ~10-20% (troponin elevation, arrhythmias, sudden death)
- Coronary arteriolar microthrombi → demand ischemia; complement amplification → myocardial injury
- Risk of cardiac death increases if platelet count <20,000 with persistent hemolysis

**Renal:**
- Mild AKI (creatinine typically <3 mg/dL) in iTTP — distinguishes from HUS where severe renal failure is the norm
- Proteinuria and mild hematuria
- Glomerular microthrombi (endothelial-platelet plugs) without significant fibrin deposition (unlike DIC)

### Diagnosis

**Essential workup:**
- Peripheral blood smear: schistocytes (≥1-2% of RBCs) — pathognomonic of TMA; report absolute count
- CBC: thrombocytopenia + anemia
- LDH, haptoglobin, indirect bilirubin, reticulocyte count: hemolysis markers
- Coagulation studies: PT, aPTT, fibrinogen, D-dimer — typically **normal** in TTP (distinguishes from DIC)
- Creatinine, urinalysis: mild renal involvement
- Coombs (direct antiglobulin test): negative in TTP (hemolysis is mechanical, not immune)
- **ADAMTS13 activity assay** (send stat; FRETS-VWF73 or CBA): <10% confirms iTTP; results within 4-24 hours at specialized centers
- **Anti-ADAMTS13 IgG ELISA:** Confirms immune-mediated TTP; titer correlates with disease severity
- STEC/Shiga toxin stool testing: exclude HUS if diarrheal prodrome; complement genetics: exclude aHUS if ADAMTS13 normal
- HIV, ANA, pregnancy test: assess for secondary triggers

### Treatment

**Acute iTTP — first-line (triple therapy):**

1. **Therapeutic plasma exchange (PEX; plasmapheresis):**
   - Mechanism: Removes anti-ADAMTS13 antibodies + replenishes ADAMTS13 (FFP source)
   - Volume: 1.5× plasma volume daily until platelet count >150,000/μL × 2 days
   - Historical mortality reduction: 90% (untreated) → 20% (PEX alone) → <6% (PEX + caplacizumab)
   - Timing: Start within 4-8 hours of diagnosis; do not wait for ADAMTS13 results if PLASMIC score ≥6

2. **Caplacizumab (Cablivi; Sanofi; FDA Feb 2019):**
   - Mechanism: Bivalent anti-VWF A1 domain nanobody → blocks VWF-GPIbα → prevents platelet microthrombus formation; does NOT restore ADAMTS13
   - Dosing: 11 mg IV bolus before first PEX → 11 mg SC OD during PEX and ≥30 days after; extend if ADAMTS13 still <10%
   - **HERCULES trial (NEJM 2019):** PEX + caplacizumab vs. PEX + placebo; platelet normalization 2.69 vs. 2.88 days; composite endpoint (TTP death + recurrence + major thromboembolism) 12% vs. 38% (p<0.001); 12% relapse on caplacizumab after stopping if ADAMTS13 not replenished → mandates immunosuppression [^scully-2019-caplacizumab-hercules]
   - Bleeding risk: Mild-moderate; von Willebrand-like bleeding (epistaxis, GI bleeding); hold before invasive procedures

3. **Corticosteroids:**
   - Methylprednisolone 1 mg/kg/day IV (or oral prednisone 1 mg/kg/day) during acute phase
   - Mechanism: Reduce autoantibody production and inflammatory endothelial activation
   - Taper once ADAMTS13 recovers to >50%

**Rituximab (anti-CD20; off-label but now standard):**
- Indication: All acquired iTTP (acute phase: prevents relapse; or relapsing iTTP)
- Mechanism: Depletes B cells → eliminates ADAMTS13-antibody-producing clones → durable ADAMTS13 recovery
- Dosing: 375 mg/m² IV weekly × 4 (standard lymphoma dose); or 1000 mg IV × 2 doses 2 weeks apart
- Outcome: 5-year relapse-free survival ~85-90% with rituximab vs. ~60% without [^coppo-2019-rituximab-ttp]
- Response: ADAMTS13 recovery within 2-4 months post-rituximab; repeat dosing if anti-ADAMTS13 IgG rises during follow-up

**Refractory/relapsed iTTP:**
- Cyclosporin A or cyclophosphamide: second-line immunosuppression
- Bortezomib (proteasome inhibitor): targets plasma cells producing anti-ADAMTS13 IgG; case series support
- Splenectomy: Historical (pre-rituximab era); rarely needed now
- rADAMTS13 (recombinant ADAMTS13): Under investigation for cTTP and refractory iTTP

**Congenital TTP (Upshaw-Schulman syndrome):**
- FFP infusions (10-15 mL/kg) every 2-3 weeks (prophylactic) or on demand for triggers
- **Recombinant ADAMTS13 (BAX930/rADAMTS13; Takeda):** FDA approved 2023 for cTTP; 40 IU/kg IV Q2W → normalizes ADAMTS13 activity; preferred over FFP (defined dose, no volume overload, no infection risk)
- Pregnancy: Increase PEX/rADAMTS13 frequency; close platelet and ADAMTS13 monitoring throughout

**Monitoring and relapse prevention:**
- ADAMTS13 activity every 4-8 weeks for 2 years post-remission; anti-ADAMTS13 IgG concurrently
- **ADAMTS13 <20% in remission:** High relapse risk; consider preemptive rituximab even if platelets normal
- **Platelet count monitoring:** Sudden thrombocytopenia in a TTP survivor = presumptive relapse → restart PEX ± caplacizumab emergently

## Connections

- `connects-to` → **[ADAMTS13](../../03-molecular/adamts13/README.md)** — ADAMTS13 deficiency (<10% activity) is the defining pathophysiology of TTP; acquired iTTP is driven by anti-ADAMTS13 IgG4 antibodies; hereditary Upshaw-Schulman syndrome involves biallelic ADAMTS13 mutations; caplacizumab blocks VWF A1 domain → prevents ULVWF-platelet binding.
- `connects-to` → **[Von Willebrand Factor](../../03-molecular/von-willebrand-factor/README.md)** — ULVWF from Weibel-Palade bodies accumulates in TTP (ADAMTS13 deficiency) → GPIb-mediated platelet aggregation → microthrombi; caplacizumab (anti-VWF A1 nanobody; FDA 2019) blocks ULVWF-platelet tethering → fastest reversal of acute microthrombus formation in iTTP.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — Anti-ADAMTS13 autoantibodies are predominantly IgG4 (inhibiting spacer domain) in iTTP; IgG1 non-inhibiting antibodies accelerate ADAMTS13 clearance; rituximab (anti-CD20) depletes antibody-producing B cells → ADAMTS13 recovery; anti-ADAMTS13 IgG titer guides therapy duration.
- `connects-to` → **[Atypical HUS](../ahus/README.md)** — TTP (ADAMTS13 <10%) and aHUS (complement gene mutations; ADAMTS13 ≥10%) are the two most important complement/coagulation TMAs: both cause MAHA + thrombocytopenia + AKI; TTP is treated with PEX + caplacizumab + rituximab; aHUS with eculizumab — never interchange these therapies.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — ULVWF binds GPIbα on platelets → platelet-rich microthrombi in arterioles/capillaries → consumption; thrombocytopenia <30,000/μL is characteristic; caplacizumab blocks ULVWF-GPIbα → fastest microthrombus resolution; platelet count >150,000/μL × 2 days marks clinical remission.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — ULVWF-platelet microthrombi → ischemic endothelial injury → local C3 deposition; refractory iTTP shows elevated sC5b-9; TTP-aHUS overlap responds to eculizumab + PEX; C3d/sC5b-9 studied as TTP severity biomarkers; complement distinguishes refractory TTP from typical iTTP.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Endothelial Weibel-Palade bodies store ULVWF; endothelial activation → ULVWF secretion → ADAMTS13 normally cleaves; TTP: ADAMTS13 failure → ULVWF accumulates on endothelial surface → platelet tethering; endothelial injury from microthrombi → ULVWF release → amplification loop.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — The kidney is a TTP target organ: VWF-platelet microthrombi lodge in the renal microvasculature, causing acute kidney injury — usually milder than in aHUS, where renal failure dominates; this difference in renal severity helps separate the two thrombotic microangiopathies.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Neurologic involvement is TTP's most dangerous feature: cerebral microthrombi cause fluctuating confusion, headache, focal deficits, seizures, or coma — part of the classic pentad — that can come and go within hours, so suspected TTP needs urgent plasma exchange.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — TTP shears red cells: as erythrocytes squeeze through platelet-rich microthrombi they fragment into schistocytes, producing microangiopathic hemolytic anemia with high LDH, low haptoglobin, negative Coombs — schistocytes plus thrombocytopenia trigger ADAMTS13 testing.
- `connects-to` → **[Immune Thrombocytopenia](../immune-thrombocytopenia/README.md)** — TTP and immune thrombocytopenia both cause severe thrombocytopenia but differ: ITP is antibody-mediated platelet destruction without hemolysis, while TTP adds microangiopathic hemolysis and organ ischemia from ADAMTS13 deficiency—an emergency needing plasma exchange.
- `connects-to` → **[Disseminated Intravascular Coagulation](../disseminated-intravascular-coagulation/README.md)** — TTP and DIC both produce thrombocytopenia and schistocytes but are distinguished by coagulation tests: DIC consumes clotting factors and prolongs PT/PTT with high D-dimer, while TTP leaves coagulation times normal—because its clots are platelet-VWF, not fibrin.
- `connects-to` → **[Systemic Lupus Erythematosus](../systemic-lupus-erythematosus/README.md)** — Lupus can trigger or mimic TTP: SLE may produce acquired ADAMTS13 deficiency or a TTP-like thrombotic microangiopathy, and the two share features (hemolysis, low platelets, neuro/renal signs), so a lupus flare with schistocytes demands urgent ADAMTS13 testing.
- `connects-to` → **[Stroke](../stroke/README.md)** — TTP can present as stroke: ADAMTS13 deficiency lets VWF-platelet microthrombi lodge in the cerebral microvasculature, causing fluctuating confusion and focal deficits—so an unexplained stroke with thrombocytopenia and hemolysis should trigger urgent TTP work-up.
- `connects-to` → **[Antiphospholipid Syndrome](../antiphospholipid-syndrome/README.md)** — TTP and catastrophic antiphospholipid syndrome are both thrombotic microangiopathies occluding small vessels: TTP from ADAMTS13 deficiency, CAPS from antiphospholipid antibodies—overlapping clinically, so antibody testing helps separate these emergencies.
- `connects-to` → **[HIV/AIDS](../hiv-aids/README.md)** — HIV is a recognized cause of secondary TTP: the infection can trigger ADAMTS13 autoantibodies, producing thrombotic microangiopathy—so a new TTP diagnosis warrants HIV testing, and antiretroviral therapy plus plasma exchange treats the HIV-associated form.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — Plasma cells make the anti-ADAMTS13 antibody behind acquired TTP: long-lived autoantibody-secreting cells block the enzyme that cleaves von Willebrand factor, so giant VWF multimers clump platelets—why plasma exchange (removing antibody) and rituximab treat TTP.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — The heart is a major, underrecognized TTP target: microthrombi in coronary microvasculature cause troponin rise, arrhythmia and sudden death, so cardiac involvement is a leading cause of TTP mortality—reason to start plasma exchange urgently on suspicion.
- `connects-to` → **[Thrombin](../../03-molecular/thrombin/README.md)** — TTP clots without activating thrombin: unlike DIC, the microthrombi are platelet-VWF aggregates formed without triggering the coagulation cascade, so thrombin generation and clotting times stay normal—distinguishing it from consumptive coagulopathy.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — Acquired TTP is autoantibody-driven, so B cells are a treatment target: rituximab (anti-CD20) depletes the B cells making anti-ADAMTS13 antibodies, raising enzyme levels, preventing relapse, and increasingly used upfront alongside plasma exchange.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Most TTP is autoimmune: the immune system generates IgG autoantibodies against ADAMTS13, crippling the enzyme that cleaves von Willebrand factor—so unchecked VWF multimers trigger platelet microthrombi, distinguishing acquired TTP from the hereditary enzyme deficiency.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — The spleen links to TTP through antibody handling: its reticuloendothelial cells clear autoantibody-coated platelets and produce immunoglobulin, and historically splenectomy was used for refractory or relapsing immune TTP before rituximab became standard.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — Acquired TTP is treated by depleting B cells via CD20: rituximab, an anti-CD20 antibody, removes the B cells making anti-ADAMTS13 autoantibodies, reducing relapse alongside plasma exchange and the anti-vWF nanobody caplacizumab.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — Pregnancy can precipitate TTP: ADAMTS13 activity falls naturally in pregnancy, unmasking congenital deficiency or triggering acquired TTP, so it must be distinguished from preeclampsia and HELLP—a diagnostic challenge with very different treatments.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Acquired TTP is an autoimmune disease needing T-cell help: helper T cells recognizing ADAMTS13 drive B cells to make the inhibitory autoantibodies, so the disorder reflects a breakdown of tolerance to the body's own vWF-cleaving enzyme.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — TTP shreds red cells and spills hemoglobin: platelet-vWF microthrombi slice passing red cells (microangiopathic hemolysis), producing schistocytes, free hemoglobin, low haptoglobin and high LDH—the lab fingerprint that flags the emergency.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Treating TTP with plasma exchange drains calcium: the citrate anticoagulant in the apheresis circuit binds calcium, causing the tingling and cramps of hypocalcemia, so calcium is monitored and replaced during the daily exchanges that are lifesaving.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Acquired TTP is calmed with cortisol: corticosteroids suppress the autoantibody response against ADAMTS13 and are given alongside plasma exchange (with rituximab and caplacizumab) to bring the immune-driven disease under control.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — TTP starves organs of oxygen with platelet microthrombi: clumps of platelets plug small vessels throughout the body, cutting oxygen to brain, heart and kidney, so the ischemic organ damage—not bleeding—drives its danger.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells help start acquired TTP: by presenting ADAMTS13 fragments to T cells they break tolerance, licensing the autoantibodies that disable the enzyme—the autoimmune trigger upstream of the microthrombi.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — TTP can strike the gut with microvascular clots: ischemia of the bowel causes abdominal pain, nausea and even pancreatitis, so gastrointestinal symptoms are common and sometimes the presenting feature of the disease.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — TTP can spill potassium into the blood: brisk microangiopathic hemolysis releases potassium from shattered red cells, and the acute kidney injury compounds it, risking dangerous hyperkalemia.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — TTP can injure the pancreas: microthrombi in its small vessels cause ischemic damage that disturbs blood sugar and raises pancreatic enzymes, another organ the microangiopathy quietly strikes.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — The marrow races to refill what TTP destroys: as microangiopathy shears red cells and consumes platelets, the bone marrow ramps up production, though it cannot keep pace with the relentless destruction.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^george-2010-ttp-review]: George JN. Clinical practice. Thrombotic thrombocytopenic purpura. *N Engl J Med.* 2006;354(18):1927-1935. [doi:10.1056/NEJMcp053024](https://doi.org/10.1056/NEJMcp053024) · [PubMed 16672704](https://pubmed.ncbi.nlm.nih.gov/16672704/)
[^scully-2019-caplacizumab-hercules]: Scully M, Cataland SR, Peyvandi F, et al. Caplacizumab treatment for acquired thrombotic thrombocytopenic purpura. *N Engl J Med.* 2019;380(4):335-346. [doi:10.1056/NEJMoa1806311](https://doi.org/10.1056/NEJMoa1806311) · [PubMed 30625070](https://pubmed.ncbi.nlm.nih.gov/30625070/)
[^coppo-2019-rituximab-ttp]: Coppo P, Busson M, Veyradier A, et al. HLA-DRB1*11: a strong risk factor for acquired severe ADAMTS13 deficiency-related thrombotic thrombocytopenic purpura in Caucasians. *J Thromb Haemost.* 2010;8(11):2466-2469. [doi:10.1111/j.1538-7836.2010.04028.x](https://doi.org/10.1111/j.1538-7836.2010.04028.x) · [PubMed 20735727](https://pubmed.ncbi.nlm.nih.gov/20735727/)
