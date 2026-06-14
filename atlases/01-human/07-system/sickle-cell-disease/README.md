---
schema: human-scale-entry/v1
id: sickle-cell-disease
name: Sickle Cell Disease
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Sickle cell disease (SCD; HbS β-globin E6V; chr11p15.4) is a haemoglobinopathy causing HbS polymerization → RBC sickling → haemolytic anaemia, vaso-occlusion, end-organ damage; hydroxyurea ↑ HbF and reduces crises; voxelotor and crizanlizumab are newer FDA-approved therapies."
aliases: ["SCD", "sickle cell disease", "sickle cell anemia", "sickle cell anaemia", "HbSS", "HbSC disease", "haemoglobin S disease", "sickle-cell anaemia", "SCA"]
sources:
  - id: steinberg-1999-scd-management
    type: peer-reviewed
    cite: "Steinberg MH. Management of sickle cell disease. N Engl J Med. 1999;340(13):1021-1030."
    doi: "10.1056/NEJM199904013401307"
    pmid: "10099145"
    url: "https://doi.org/10.1056/NEJM199904013401307"
  - id: vichinsky-2000-acs-scd
    type: peer-reviewed
    cite: "Vichinsky EP, Neumayr LD, Earles AN, et al. Causes and outcomes of the acute chest syndrome in sickle cell disease. N Engl J Med. 2000;342(25):1855-1865."
    doi: "10.1056/NEJM200006223422502"
    pmid: "10861320"
    url: "https://doi.org/10.1056/NEJM200006223422502"
  - id: niaid-2014-scd-guidelines
    type: clinical-guideline
    cite: "Yawn BP, Buchanan GR, Afenyi-Annan AN, et al. Management of sickle cell disease: summary of the 2014 evidence-based report by expert panel members. JAMA. 2014;312(10):1033-1048."
    doi: "10.1001/jama.2014.10517"
    pmid: "25205765"
    url: "https://doi.org/10.1001/jama.2014.10517"
cross_links:
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "HbS (α2βS2; β-globin E6V GAG→GTG) polymerizes when deoxygenated → long fibres → RBC sickling; HbF (α2γ2) inhibits HbS polymerization; HbSC (one HbS + HbC E6K allele) → milder but significant disease; HbSβ-thalassemia → intermediate severity."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "SCD is the most common cause of stroke in children <10 years (cerebral vasculopathy; large vessel stenosis from repetitive sickling → moyamoya pattern); transcranial Doppler screening + chronic RBC transfusion reduces stroke risk by 92% (STOP trial)."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Renal medullary sickling (high osmolarity + low pO2 in vasa recta) → hyposthenuria; progressive CKD in ~30% HbSS by age 40; albuminuria → nephrotic syndrome; ACE inhibitors + hydroxyurea slow CKD progression; sickle cell nephropathy is a distinct histological entity."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Chronic haemolysis → NO scavenging by free haemoglobin → pulmonary hypertension (PAH; tricuspid regurgitation velocity >2.5 m/s predicts mortality); cardiomegaly + high-output failure from chronic anaemia; sildenafil for SCD-PAH; echocardiographic screening at age 10."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Chronic transfusion in SCD (stroke prevention, recurrent ACS; target HbS <30%) causes transfusional iron overload; serum ferritin >1,000 ng/mL → deferasirox chelation required; cardiac MRI T2* monitors iron deposition; TSAT 100% → NTBI → cardiomyopathy risk."
  - target: 01-human/07-system/thalassemia
    relation: connects-to
    note: "HbSβ-thalassemia (HbS + β-thal allele) is a common SCD genotype; β⁰ allele severity = HbSS; β⁺ = milder; shared gene therapy targets: Casgevy (CRISPR BCL11A derepression of γ-globin/HbF) is FDA-approved for both β-thal major and sickle cell disease."
  - target: 01-human/03-molecular/g6pd
    relation: connects-to
    note: "G6PD A− deficiency (10-20% sub-Saharan Africans) co-occurs with HbSS in ~5-10% of SCD patients; G6PD deficiency + SCD → additive oxidant haemolysis risk; avoid dapsone, rasburicase, and nitrofurantoin in G6PD-deficient SCD; G6PD screening recommended."
  - target: 01-human/07-system/malaria
    relation: connects-to
    note: "HbAS (sickle trait) confers ~60% protection against severe malaria (balanced polymorphism); HbSS patients in endemic regions face compounded risk: fever + dehydration → sickling crises; antimalarial prophylaxis planning is essential for HbSS in endemic areas."
  - target: 01-human/03-molecular/protein-c
    relation: connects-to
    note: "Acquired protein C deficiency is common in SCD: vaso-occlusive crisis → local thrombin burst → APC consumption; protein C levels inversely correlate with VOC frequency; SCD patients have reduced EPCR expression on ECs → impaired APC generation during hemolytic crises."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Sickle cell disease is fundamentally a red-cell disease: HbS polymerizes when deoxygenated, distorting erythrocytes into rigid sickle shapes that hemolyze (anemia) and jam microvessels (vaso-occlusion); dehydration and adhesion molecules make the cells sticky and short-lived."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "The spleen is an early casualty of sickle cell disease: repeated sickling infarcts it, causing splenic sequestration crises in children then autosplenectomy in adults; the resulting functional asplenia raises infection risk, mandating vaccines and penicillin prophylaxis."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Sickle cell disease is a hypercoagulable state: chronic hemolysis exposes phosphatidylserine and frees hemoglobin, activating platelets and coagulation while consuming protein C/S; VTE and pulmonary embolism are markedly increased atop the in-situ thrombosis of vaso-occlusion."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "Pulmonary hypertension is a deadly complication of sickle cell disease: chronic hemolysis scavenges nitric oxide and releases free hemoglobin and arginase, raising pulmonary vascular tone—an elevated tricuspid regurgitant jet marks much higher mortality."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Pain in sickle cell disease is not only ischemic but increasingly neuropathic: repeated vaso-occlusive crises sensitize central and peripheral pain pathways, so chronic SCD pain takes on a neuropathic, opioid-resistant quality—calling for anticonvulsant adjuncts."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Splenic macrophages drive the extravascular hemolysis of sickle cell disease: they recognize and destroy rigid, sickled red cells, and recurrent splenic sequestration and infarction eventually leave patients functionally asplenic—hence lifelong sepsis risk."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Nitric oxide depletion drives sickle-cell vasculopathy: free hemoglobin from hemolysis scavenges NO, so vessels lose vasodilation and platelets activate—linking chronic hemolysis to pulmonary hypertension, stroke and leg ulcers beyond the acute vaso-occlusive crises."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Oxygen tension triggers the sickling itself: deoxygenated HbS polymerizes and deforms red cells, so hypoxia, dehydration and acidosis precipitate vaso-occlusive crises—which is why low oxygen at altitude or in infection can set off a painful sickle crisis."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "The kidney is a major target of sickle-cell disease: the hypoxic, acidic renal medulla promotes sickling that damages the concentrating mechanism and glomeruli, causing impaired urine concentration, hematuria and progressive sickle nephropathy toward chronic kidney disease."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Sickle cell disease is a disease of the endothelium as much as the red cell: sickled cells and free hemoglobin scavenge nitric oxide and inflame the vessel lining, so endothelial activation and adhesion trigger the painful vaso-occlusive crises."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Sickle cell disease drives the bone marrow into overdrive: chronic hemolysis spurs erythroid hyperplasia that expands marrow and can cause aplastic crises when parvovirus halts it—and replacing the marrow by transplant or gene therapy can cure the disease."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Sickle cell disease causes functional asplenia and immune vulnerability: repeated splenic infarction destroys the organ early in childhood, so patients are dangerously prone to encapsulated-bacterial sepsis—why prophylactic penicillin and vaccination are lifesaving."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "The lung is sickle cell disease's deadliest battleground: acute chest syndrome—sickling and infection in the pulmonary vessels—causes fever, chest pain, and hypoxia and is a leading cause of death, so it is treated urgently with transfusion and antibiotics."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Sickle cell disease attacks the musculoskeletal system: vaso-occlusion infarcts bone, causing painful crises, dactylitis in infants, and avascular necrosis of the hip, so the skeleton bears much of the chronic damage and disability of the disease."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Sickle cell disease threatens sight: sickling in the tiny retinal vessels causes ischemia and proliferative sickle retinopathy with fragile new vessels that bleed or detach the retina—so regular eye screening protects vision in older patients."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Chronic transfusions for sickle cell load the body with iron: repeated red-cell transfusions for stroke prevention and anemia deposit iron in the heart, liver and endocrine organs, so iron chelation is needed to prevent overload damage."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils help trigger sickle cell pain crises: activated neutrophils and adhesion molecules glue sickled cells to vessel walls, starting the vaso-occlusion behind painful crises—so anti-adhesion therapy (crizanlizumab) targets this step."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Sickle cell disease burdens the liver: chronic hemolysis forms pigment gallstones, and sickling in hepatic vessels can cause sequestration and crises, so right-upper-quadrant pain in sickle cell needs evaluation of gallbladder and liver."
---

# Sickle Cell Disease

## Overview

**Sickle cell disease (SCD)** is the most common serious monogenic haemoglobinopathy worldwide, affecting ~100,000 people in the United States and 5–8 million globally. It is caused by a point mutation in the **β-globin gene (*HBB*, chromosome 11p15.4)**: a Glu→Val substitution at position 6 (E6V; GAG→GTG codon) — creating **haemoglobin S (HbS)**. The disease is inherited as an autosomal recessive disorder; disease manifestations require at least one HbS allele plus a second defective β-globin allele [^steinberg-1999-scd-management].

**Pathophysiological mechanism:**
1. Deoxygenated HbS polymerizes into long rigid fibres within red blood cells (RBCs)
2. Polymer formation distorts RBCs into the characteristic sickle shape
3. Sickled RBCs are rigid, adherent, and prone to haemolysis and vascular occlusion
4. Result: chronic haemolytic anaemia + acute vaso-occlusive crises + progressive end-organ damage

**Genotypes causing SCD:**

| Genotype | HbS% | HbA% | HbF% | Severity |
|:---------|:-----|:-----|:-----|:---------|
| HbSS (classic SCA) | 85-95% | 0% | 2-20% | Most severe |
| HbSC | ~50% HbS, ~50% HbC | 0% | 1-5% | Moderate; retinal/AVN complications |
| HbSβ⁰-thalassemia | 80-90% | 0% | 5-15% | Severe (similar to HbSS) |
| HbSβ⁺-thalassemia | 60-75% | 10-30% | 5-15% | Mild-moderate |
| HbSS + hereditary persistence of HbF | ~70% HbS | 0% | >25% | Milder course |
| HbS trait (carrier) | 35-40% | 55-60% | 1-2% | No haemolysis; exertional rhabdomyolysis risk |

**Epidemiology:**
- Highest prevalence: Sub-Saharan Africa (Nigeria, DRC, Ghana), Middle East, Mediterranean, India
- US: ~100,000 patients; predominantly African-American ancestry; prevalence 1:365 births
- Malaria protection: HbAS trait confers ~60% protection against severe *P. falciparum* malaria (balanced polymorphism explaining high allele frequency)

## Structure

### Molecular basis of HbS polymerization

**HbS structure:** Normal adult haemoglobin (HbA) is α2β2 tetramer; HbS is α2βS2 where β-globin Glu6→Val replaces a charged residue with a hydrophobic one on the outer surface of the β-globin chain.

**Polymerization mechanism:**
- In oxygenated HbS: T→R quaternary shift; Val6 is partially buried → minimal polymerization
- In deoxygenated HbS (T state): Val6 fully exposed → inserts into a hydrophobic "acceptor pocket" on an adjacent HbS molecule (Ala70, Phe85, Leu88 of β-globin) → nucleation of double-stranded protofibrils → lateral aggregation → long 14-stranded polymer fibres (~12.7 nm diameter)
- **Critical concentration (Cs):** HbS polymerization is sigmoidal with a delay period (nucleation phase); delay time is exquisitely sensitive to HbS concentration (log-linear relationship): ~30× faster at MCHC 37 g/dL vs. 35 g/dL
- **HbF inhibition:** γ-globin chains (HbF: α2γ2) cannot participate in the polymer acceptor pocket → HbF dilutes HbS concentration within the cell → dramatically prolongs delay time → prevents sickling

**Sickling cascade in vivo:**
1. In capillaries (pO2 ~40 mmHg), HbS deoxygenation exceeds Cs → polymer nucleation → sickling
2. Sickled cells: rigid, low deformability → mechanical haemolysis in spleen/marrow; adhesion to endothelium (via VLA-4/VCAM-1, P-selectin/PSGL-1)
3. Repeated sickling-unsickling → membrane oxidative damage → irreversibly sickled cells (ISCs): permanently deformed even when reoxygenated; rapidly haemolysed (RBC lifespan ~15-20 days vs. 120 days normally)
4. ISCs contribute to vaso-occlusion, dense cell formation, and free haemoglobin release

### Vaso-occlusion: multi-cellular mechanism

SCD vaso-occlusion is not just from sickled RBCs mechanically blocking vessels — it involves a complex multi-cellular cascade:
- **Activated endothelium:** Thrombin, inflammatory cytokines (TNF-α, IL-1β) → endothelial P-selectin, VCAM-1, tissue factor upregulation
- **Neutrophil-platelet-RBC aggregates:** HbS RBCs → oxidative stress → endothelial NADPH oxidase → ROS → NF-κB → inflammatory adhesion molecules; neutrophils bind endothelium → trap flowing sickle RBCs
- **Nitric oxide (NO) depletion:** Free haemoglobin from haemolysis → reacts with NO at near-diffusion-limited rates → converts vasodilatory NO to nitrate → vasoconstriction, platelet activation, endothelial dysfunction
- **Coagulation activation:** Phosphatidylserine exposure on sickle RBC membranes → procoagulant surface → thrombin generation → fibrin deposition in microvessels

## Function

### Acute complications

**Vaso-occlusive (painful) crisis (VOC):**
- Most common SCD complication; accounts for >90% of acute care visits
- Mechanism: microvascular obstruction → tissue ischaemia → acute pain (bone marrow infarction is primary source: ribs, vertebrae, femur, humerus)
- Precipitants: cold, dehydration, infection, stress, altitude
- Treatment: Aggressive IV hydration, IV opioids (morphine, hydromorphone, patient-controlled analgesia), NSAIDs for adjunctive analgesia, supplemental oxygen if hypoxic, incentive spirometry to prevent ACS

**Acute Chest Syndrome (ACS) [^vichinsky-2000-acs-scd]:**
- Definition: New pulmonary infiltrate on CXR + respiratory symptoms (fever, cough, hypoxia, chest pain) in a patient with SCD
- Mechanisms: Fat embolism from infarcted bone marrow (most common in adults), pulmonary vaso-occlusion, infection (*Chlamydophila*, *Mycoplasma*, viral — most common in children)
- Most dangerous acute complication; leading cause of SCD mortality
- Treatment: Broad-spectrum antibiotics (macrolide + cephalosporin), bronchodilators, incentive spirometry, **simple transfusion** (target Hb ~10 g/dL) or **exchange transfusion** for severe ACS; mechanical ventilation for respiratory failure
- Prevention: Hydroxyurea (reduces ACS by 50%); incentive spirometry during painful crises

**Stroke:**
- Ischaemic stroke: Most common <10 years (cerebral vasculopathy from repetitive sickling → large vessel narrowing/occlusion → moyamoya pattern); haemorrhagic stroke more common in adults
- **STOP trial:** Transcranial Doppler (TCD) velocity >200 cm/s → chronic transfusion (monthly exchange/simple transfusion; target HbS <30%) → 92% relative risk reduction in primary stroke
- **STOP II:** Stopping transfusion → 50% stroke recurrence within 30 months → indefinite chronic transfusion or HCT (haematopoietic cell transplant) required
- Hydroxyurea alone insufficient for high-TCD-velocity primary prevention; chronic transfusion is standard

**Splenic sequestration:**
- Acute: Sickle RBCs trapped in spleen → sudden massive splenomegaly + anaemia (Hb drop >2 g/dL from baseline) → circulatory shock; treat: blood transfusion; splenectomy for recurrent episodes
- Chronic: Repeated microinfarction → functional asplenia by age 4-5 in HbSS → loss of IgM-mediated opsonisation → susceptibility to encapsulated bacteria (*Streptococcus pneumoniae*, *Haemophilus influenzae*, *Neisseria meningitidis*) → overwhelming post-splenectomy infection (OPSI)
- Prevention: Pneumococcal vaccines (PCV13 + PPSV23), meningococcal vaccines, penicillin prophylaxis until age 5 (or indefinitely in high-risk patients)

**Aplastic crisis:**
- Parvovirus B19 infects erythroid progenitors → transient reticulocytopenia → rapid anaemia in patients with baseline high RBC turnover; self-limited (1-2 weeks); transfuse if symptomatic

**Priapism:**
- Uncontrolled, ischaemic erection > 4 hours; NO depletion → failure of penile smooth muscle relaxation; treat: hydration + analgesics; aspiration + phenylephrine injection for >4h; exchange transfusion; prevention: hydroxyurea, PDE5 inhibitors (sildenafil, tadalafil)

### Chronic complications

**Pulmonary arterial hypertension (PAH):**
- Mechanism: Chronic haemolysis → free haemoglobin → NO scavenging → reduced prostacyclin → vasoconstriction + endothelial proliferation → PAH
- Prevalence: ~6-10% HbSS patients have echocardiographic PAH (TRV >2.5 m/s); RHC-confirmed PAH ~10% of elevated TRV cases
- Mortality: PAH is a major contributor to premature death; TRV >2.5 m/s → HR 10.6 for death in 2 years
- Treatment: Hydroxyurea; chronic transfusion; sildenafil (PDE5 inhibitor; improves exercise capacity in SCD-PAH); endothelin receptor antagonists; HSCT curative

**Avascular necrosis (AVN):**
- Bilateral femoral and humeral head AVN from vascular occlusion of nutrient arteries
- Prevalence: ~50% HbSS by age 35
- Management: Conservative (PT, analgesia, crutches); core decompression; total hip/shoulder arthroplasty

**Sickle nephropathy (CKD):**
- Renal medullary microenvironment (high osmolarity, low pH, low pO2) → sickling in vasa recta → renal medullary ischaemia → hyposthenuria, haematuria, renal papillary necrosis
- Progressive glomerulopathy (hyperfiltration, podocyte injury) → proteinuria → nephrotic syndrome → CKD (ESRD in ~30% by age 40)
- Management: ACE inhibitors for proteinuria; hydroxyurea; avoid nephrotoxic agents; dialysis/transplant for ESRD

**Leg ulcers:**
- Chronic medial malleolar ulcers from haemolysis (low NO) + vascular occlusion
- Painful, slow-healing; treat with wound care, pain control, hydroxyurea; exchange transfusion for refractory ulcers

## Pathology

### Diagnosis

**Newborn screening (gold standard):** Haemoglobin electrophoresis (isoelectric focusing or HPLC) in first week of life; all US states mandate SCD screening; early detection allows penicillin prophylaxis initiation by age 3 months.

**Laboratory findings:**
- Anaemia: Hb 6-9 g/dL (HbSS); 10-12 g/dL (HbSC)
- Reticulocytosis: 5-25% (compensatory; absent in aplastic crisis)
- Blood smear: Sickle cells (drepanocytes), target cells, polychromasia, Howell-Jolly bodies (functional asplenia)
- LDH elevated (haemolysis marker); unconjugated bilirubin elevated
- Haemoglobin electrophoresis: Confirms HbS genotype

### Treatment

**Disease-modifying therapies:**

**Hydroxyurea (hydroxycarbamide) [^niaid-2014-scd-guidelines]:**
- Mechanism: ↑ HbF synthesis (via ↑ γ-globin gene expression, S-nitrosylation of sGC → cGMP → Hb switching); NO-donor activity → vasodilation; ↓ neutrophil/platelet counts → reduced vaso-occlusion
- Dosing: Start 15 mg/kg/day PO → titrate to maximum tolerated dose (MTD; typically 20-35 mg/kg/day); monitor CBC (target ANC >2,000/μL, platelets >80,000/μL)
- Efficacy: MSH trial — hydroxyurea reduced painful crisis rate by 44%, ACS by 50%, transfusions by 50%, hospitalizations by 40%; 17-year follow-up showed 40% mortality reduction
- Indication: All HbSS and HbSβ⁰ patients ≥9 months old (NHLBI 2014 guidelines); HbSC/HbSβ⁺ with severe complications

**Voxelotor (Oxbryta; FDA 2019):**
- Mechanism: Covalently binds HbS in the oxygenated state → shifts oxygen affinity → prevents T-state deoxygenation → inhibits HbS polymerization
- Efficacy (HOPE trial): 72% of patients achieved Hb increase ≥1 g/dL; reduced haemolysis markers; did not reduce VOC in pivotal trial
- Dosing: 1,500 mg PO once daily; withdrawn from US market in 2024 due to HOPE-KIDS 2 interim analysis showing trend toward higher mortality — ongoing regulatory evaluation
- Note: Voxelotor's status should be verified with current regulatory guidance

**Crizanlizumab (Adakveo; FDA 2019):**
- Mechanism: Monoclonal antibody targeting P-selectin on activated platelets and endothelium → blocks P-selectin/PSGL-1 interactions → prevents neutrophil-platelet-RBC aggregate formation → reduces vaso-occlusion
- Efficacy (SUSTAIN trial): 45% reduction in annual pain crisis rate vs. placebo; beneficial regardless of hydroxyurea use
- Dosing: 5 mg/kg IV every 4 weeks; can be combined with hydroxyurea
- Note: FDA reviewing postmarket data

**Chronic transfusion therapy:**
- **Simple transfusion:** Raises Hb, dilutes HbS%; used for ACS, priapism, pre-surgical preparation (target HbS <30% for major surgery), acute stroke treatment
- **Exchange transfusion (erythrocytapheresis):** Removes HbS RBCs while adding HbA RBCs; targets HbS <30%; avoids hyperviscosity; gold standard for acute stroke, severe ACS, peri-operative preparation
- **Chronic monthly transfusion:** Primary and secondary stroke prevention (target HbS <30%); iron overload is the main complication → iron chelation (deferasirox, deferoxamine)

**Haematopoietic cell transplantation (HCT):**
- Only currently available cure for SCD
- **Matched sibling donor HCT:** ~90% event-free survival in children without end-organ damage; ideal for high-risk children (prior stroke, frequent VOC despite hydroxyurea, multiple ACS episodes)
- **Haploidentical/matched unrelated donor:** Higher graft-versus-host disease risk; increasingly feasible with improved conditioning regimens (reduced-intensity conditioning for adults)
- **Gene therapy/gene editing (emerging):**
  - **Betibeglogene autotemcel (Zynteglo; FDA 2023):** Lentiviral vector adding anti-sickling βA-T87Q-globin gene to autologous HSCs; 94% of HbSS patients became transfusion-independent in the HGB-206 trial
  - **Exagamglogene autotemcel (Casgevy; FDA 2023):** First CRISPR-Cas9 gene editing therapy approved; reactivates HbF by disrupting BCL11A enhancer → BCL11A silenced → γ-globin re-expressed → HbF >20% → suppresses HbS polymerization; durable responses

## Connections

- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — HbS (α2βS2; β-globin E6V GAG→GTG) polymerizes when deoxygenated → long fibres → RBC sickling; HbF (α2γ2) inhibits HbS polymerization; HbSC (one HbS + HbC E6K allele) → milder but significant disease; HbSβ-thalassemia → intermediate severity.
- `connects-to` → **[Stroke](../stroke/README.md)** — SCD is the most common cause of stroke in children <10 years (cerebral vasculopathy; large vessel stenosis from repetitive sickling → moyamoya pattern); transcranial Doppler screening + chronic RBC transfusion reduces stroke risk by 92% (STOP trial).
- `connects-to` → **[CKD](../ckd/README.md)** — Renal medullary sickling (high osmolarity + low pO2 in vasa recta) → hyposthenuria; progressive CKD in ~30% HbSS by age 40; albuminuria → nephrotic syndrome; ACE inhibitors + hydroxyurea slow CKD progression; sickle cell nephropathy is a distinct histological entity.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Chronic haemolysis → NO scavenging by free haemoglobin → pulmonary hypertension (PAH; tricuspid regurgitation velocity >2.5 m/s predicts mortality); cardiomegaly + high-output failure from chronic anaemia; sildenafil for SCD-PAH; echocardiographic screening at age 10.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Chronic transfusion in SCD (stroke prevention, recurrent ACS; target HbS <30%) causes transfusional iron overload; serum ferritin >1,000 ng/mL → deferasirox chelation required; cardiac MRI T2* monitors iron deposition; TSAT 100% → NTBI → cardiomyopathy risk.
- `connects-to` → **[Thalassemia](../thalassemia/README.md)** — HbSβ-thalassemia (HbS + β-thal allele) is a common SCD genotype; β⁰ allele severity = HbSS; β⁺ = milder; shared gene therapy targets: Casgevy (CRISPR BCL11A derepression of γ-globin/HbF) is FDA-approved for both β-thal major and sickle cell disease.
- `connects-to` → **[G6PD](../../03-molecular/g6pd/README.md)** — G6PD A− deficiency (10-20% sub-Saharan Africans) co-occurs with HbSS in ~5-10% of SCD patients; G6PD deficiency + SCD → additive oxidant haemolysis risk; avoid dapsone, rasburicase, and nitrofurantoin in G6PD-deficient SCD; G6PD screening recommended.
- `connects-to` → **[Malaria](../malaria/README.md)** — HbAS (sickle trait) confers ~60% protection against severe malaria (balanced polymorphism); HbSS patients in endemic regions face compounded risk: fever + dehydration → sickling crises; antimalarial prophylaxis planning is essential for HbSS in endemic areas.
- `connects-to` → **[Protein C](../../03-molecular/protein-c/README.md)** — Acquired protein C deficiency is common in SCD: vaso-occlusive crisis → local thrombin burst → APC consumption; protein C levels inversely correlate with VOC frequency; SCD patients have reduced EPCR expression on ECs → impaired APC generation during hemolytic crises.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Sickle cell disease is fundamentally a red-cell disease: HbS polymerizes when deoxygenated, distorting erythrocytes into rigid sickle shapes that hemolyze (anemia) and jam microvessels (vaso-occlusion); dehydration and adhesion molecules make the cells sticky and short-lived.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — The spleen is an early casualty of sickle cell disease: repeated sickling infarcts it, causing splenic sequestration crises in children then autosplenectomy in adults; the resulting functional asplenia raises infection risk, mandating vaccines and penicillin prophylaxis.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Sickle cell disease is a hypercoagulable state: chronic hemolysis exposes phosphatidylserine and frees hemoglobin, activating platelets and coagulation while consuming protein C/S; VTE and pulmonary embolism are markedly increased atop the in-situ thrombosis of vaso-occlusion.
- `connects-to` → **[Pulmonary Arterial Hypertension](../pulmonary-arterial-hypertension/README.md)** — Pulmonary hypertension is a deadly complication of sickle cell disease: chronic hemolysis scavenges nitric oxide and releases free hemoglobin and arginase, raising pulmonary vascular tone—an elevated tricuspid regurgitant jet marks much higher mortality.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Pain in sickle cell disease is not only ischemic but increasingly neuropathic: repeated vaso-occlusive crises sensitize central and peripheral pain pathways, so chronic SCD pain takes on a neuropathic, opioid-resistant quality—calling for anticonvulsant adjuncts.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Splenic macrophages drive the extravascular hemolysis of sickle cell disease: they recognize and destroy rigid, sickled red cells, and recurrent splenic sequestration and infarction eventually leave patients functionally asplenic—hence lifelong sepsis risk.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — Nitric oxide depletion drives sickle-cell vasculopathy: free hemoglobin from hemolysis scavenges NO, so vessels lose vasodilation and platelets activate—linking chronic hemolysis to pulmonary hypertension, stroke and leg ulcers beyond the acute vaso-occlusive crises.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Oxygen tension triggers the sickling itself: deoxygenated HbS polymerizes and deforms red cells, so hypoxia, dehydration and acidosis precipitate vaso-occlusive crises—which is why low oxygen at altitude or in infection can set off a painful sickle crisis.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — The kidney is a major target of sickle-cell disease: the hypoxic, acidic renal medulla promotes sickling that damages the concentrating mechanism and glomeruli, causing impaired urine concentration, hematuria and progressive sickle nephropathy toward chronic kidney disease.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Sickle cell disease is a disease of the endothelium as much as the red cell: sickled cells and free hemoglobin scavenge nitric oxide and inflame the vessel lining, so endothelial activation and adhesion trigger the painful vaso-occlusive crises.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Sickle cell disease drives the bone marrow into overdrive: chronic hemolysis spurs erythroid hyperplasia that expands marrow and can cause aplastic crises when parvovirus halts it—and replacing the marrow by transplant or gene therapy can cure the disease.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Sickle cell disease causes functional asplenia and immune vulnerability: repeated splenic infarction destroys the organ early in childhood, so patients are dangerously prone to encapsulated-bacterial sepsis—why prophylactic penicillin and vaccination are lifesaving.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — The lung is sickle cell disease's deadliest battleground: acute chest syndrome—sickling and infection in the pulmonary vessels—causes fever, chest pain, and hypoxia and is a leading cause of death, so it is treated urgently with transfusion and antibiotics.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Sickle cell disease attacks the musculoskeletal system: vaso-occlusion infarcts bone, causing painful crises, dactylitis in infants, and avascular necrosis of the hip, so the skeleton bears much of the chronic damage and disability of the disease.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Sickle cell disease threatens sight: sickling in the tiny retinal vessels causes ischemia and proliferative sickle retinopathy with fragile new vessels that bleed or detach the retina—so regular eye screening protects vision in older patients.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Chronic transfusions for sickle cell load the body with iron: repeated red-cell transfusions for stroke prevention and anemia deposit iron in the heart, liver and endocrine organs, so iron chelation is needed to prevent overload damage.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Neutrophils help trigger sickle cell pain crises: activated neutrophils and adhesion molecules glue sickled cells to vessel walls, starting the vaso-occlusion behind painful crises—so anti-adhesion therapy (crizanlizumab) targets this step.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Sickle cell disease burdens the liver: chronic hemolysis forms pigment gallstones, and sickling in hepatic vessels can cause sequestration and crises, so right-upper-quadrant pain in sickle cell needs evaluation of gallbladder and liver.

[^steinberg-1999-scd-management]: Steinberg MH. Management of sickle cell disease. *N Engl J Med.* 1999;340(13):1021-1030. [doi:10.1056/NEJM199904013401307](https://doi.org/10.1056/NEJM199904013401307) · [PubMed 10099145](https://pubmed.ncbi.nlm.nih.gov/10099145/)
[^vichinsky-2000-acs-scd]: Vichinsky EP, Neumayr LD, Earles AN, et al. Causes and outcomes of the acute chest syndrome in sickle cell disease. *N Engl J Med.* 2000;342(25):1855-1865. [doi:10.1056/NEJM200006223422502](https://doi.org/10.1056/NEJM200006223422502) · [PubMed 10861320](https://pubmed.ncbi.nlm.nih.gov/10861320/)
[^niaid-2014-scd-guidelines]: Yawn BP, Buchanan GR, Afenyi-Annan AN, et al. Management of sickle cell disease: summary of the 2014 evidence-based report by expert panel members. *JAMA.* 2014;312(10):1033-1048. [doi:10.1001/jama.2014.10517](https://doi.org/10.1001/jama.2014.10517) · [PubMed 25205765](https://pubmed.ncbi.nlm.nih.gov/25205765/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
