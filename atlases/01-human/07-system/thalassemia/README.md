---
schema: human-scale-entry/v1
id: thalassemia
name: Thalassemia
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Thalassaemias are haemoglobinopathies from α- or β-globin chain imbalance; β-thalassaemia major requires lifelong transfusion; ineffective erythropoiesis → iron overload despite anaemia; betibeglogene autotemcel (Zynteglo) and CRISPR-based Casgevy are approved gene therapies."
aliases: ["thalassaemia", "thalassemia", "beta-thalassemia", "alpha-thalassemia", "β-thalassaemia major", "Cooley's anaemia", "thal major", "HbH disease", "hydrops fetalis", "thal trait"]
sources:
  - id: weatherall-2008-thalassemia-review
    type: peer-reviewed
    cite: "Weatherall DJ. The inherited diseases of hemoglobin are an emerging global health burden. Blood. 2010;115(22):4331-4336."
    doi: "10.1182/blood-2010-01-251348"
    pmid: "20233970"
    url: "https://doi.org/10.1182/blood-2010-01-251348"
  - id: cappellini-2014-thalassemia-guidelines
    type: clinical-guideline
    cite: "Cappellini MD, Cohen A, Porter J, et al. (eds). Guidelines for the Management of Transfusion Dependent Thalassaemia (TDT). 3rd ed. Thalassaemia International Federation; 2014."
    url: "https://thalassaemia.org.cy/publications/tif-publications/guidelines-management-transfusion-dependent-thalassaemia-tdt-3rd-edition-2014/"
    accessed: "2026-06-08"
  - id: thompson-2018-zynteglo-nejm
    type: peer-reviewed
    cite: "Thompson AA, Walters MC, Kwiatkowski J, et al. Gene therapy in patients with transfusion-dependent β-thalassemia. N Engl J Med. 2018;378(16):1479-1493."
    doi: "10.1056/NEJMoa1705342"
    pmid: "29669226"
    url: "https://doi.org/10.1056/NEJMoa1705342"
cross_links:
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Thalassaemias arise from imbalanced α- or β-globin chain synthesis; excess unpaired chains precipitate → ineffective erythropoiesis and haemolysis; HbA₂ (α2δ2) elevation >3.5% diagnoses β-thal trait; HbH (β4 tetramers) is the signature of 3-gene α-thal deletion."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "β-thal major: ineffective erythropoiesis → ERFE ↑ → hepcidin suppression → unconstrained iron absorption → TSAT 100% → NTBI → tissue deposition; deferasirox (oral) and deferoxamine (parenteral) are the mainstay chelators targeting transferrin-bound and NTBI iron."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Ineffective erythropoiesis in β-thalassaemia → ERFE (erythroferrone from stress erythroblasts) → suppresses BMP-SMAD → ↓ hepcidin → ↑ ferroportin → unconstrained iron absorption despite anemia; luspatercept (ActRIIA ligand trap) ↑ ERFE pathway and ↓ ineffective erythropoiesis."
  - target: 01-human/07-system/sickle-cell-disease
    relation: connects-to
    note: "HbSβ-thalassemia (HbS + β-thal allele) is a common SCD genotype; severity depends on β-thal allele type (β⁰ = severe SCA-like; β⁺ = milder); gene therapy approaches (Zynteglo, Casgevy) target both SCD and β-thal major as overlapping haemoglobinopathies."
  - target: 01-human/03-molecular/g6pd
    relation: connects-to
    note: "Thalassaemia (HbE/β-thal most common in SEA) co-occurs with G6PD Mahidol/Viangchan; G6PD deficiency + beta-thalassaemia → additive oxidant haemolysis; G6PD screening is recommended in thalassaemia; both adaptations cluster in malaria-endemic regions by balanced selection."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "Activin A/B → ActRIIB on late erythroblasts → SMAD2/3 → maturation block → ineffective erythropoiesis in beta-thalassemia; luspatercept (BELIEVE trial: 21% achieved ≥33% transfusion reduction vs. 4.5% placebo) traps activin A/B → accelerates terminal erythroid differentiation."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "In thalassemia the imbalance of α and β globin leaves unpaired chains that precipitate inside red cells, so most erythroblasts die in the marrow before maturing (ineffective erythropoiesis) and survivors are microcytic, hypochromic target cells that haemolyse."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Thalassemia causes iron overload despite anaemia: ineffective erythropoiesis releases erythroferrone that suppresses hepcidin, so dietary iron pours in unchecked and transfusions add more; the excess poisons heart, liver, and endocrine glands, making chelation lifesaving."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Iron-loaded cardiomyocytes make the heart the leading killer in undertreated thalassaemia major: NTBI enters via calcium channels → Fenton free radicals → arrhythmia and cardiomyopathy; cardiac MRI T2* (<10 ms = severe) guides chelation before heart failure."
  - target: 01-human/07-system/malaria
    relation: connects-to
    note: "Thalassemia, like sickle trait, is a malaria-protective hemoglobinopathy: its high gene frequency across the Mediterranean, Middle East and Asia reflects balancing selection, as α- and β-thalassemia carriers resist severe Plasmodium falciparum—matching the historic malaria map."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Thalassemia is driven by ineffective erythropoiesis: unbalanced globin chains precipitate and kill red-cell precursors in the marrow, which expands massively (skeletal deformities, extramedullary hematopoiesis); luspatercept eases this block and transfusions suppress the marrow."
  - target: 01-human/07-system/iron-deficiency-anemia
    relation: connects-to
    note: "Thalassemia trait is the key differential of iron-deficiency anemia: both cause microcytic, hypochromic cells, but thalassemia has normal/high iron, a low Mentzer index and raised HbA2 while IDA shows low ferritin—mislabeling it as IDA causes harmful needless iron use."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "The spleen bears the brunt of thalassemia: it works overtime clearing defective red cells and hosts extramedullary hematopoiesis, enlarging massively and worsening anemia by trapping blood—so splenectomy is sometimes needed but leaves patients prone to sepsis."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver is a major casualty of transfusion-dependent thalassemia: lifelong transfusions and increased gut iron absorption load the liver with iron, causing cirrhosis unless iron chelation is maintained—and hepatic iron quantified by MRI guides chelation therapy."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Thalassemia causes a distinctive osteoporosis: marrow expansion from chronic anemia thins cortical bone, while iron overload and endocrine damage impair osteoblasts and sex hormones—so fragility fractures are common and bone-density monitoring is part of care."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Erythropoietin runs high in thalassemia: severe anemia drives massive EPO release, but defective globin chains make erythropoiesis ineffective, so the marrow expands uselessly—causing skeletal deformities and extramedullary hematopoiesis instead of functional red cells."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Thalassemia impairs oxygen delivery at its root: too few normal hemoglobin tetramers mean less oxygen per red cell, so tissues stay hypoxic despite a racing marrow—and the hypoxic drive fuels the bone expansion and high-output cardiac strain of severe disease."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Iron overload makes thalassemia an endocrine disease: transfusion and gut iron deposit in glands, causing diabetes, hypogonadism, hypothyroidism and growth failure, so the endocrine system bears much of the chronic morbidity—and iron chelation aims to prevent it."
  - target: 01-human/03-molecular/ferroportin
    relation: connects-to
    note: "Ferroportin sits at the heart of thalassemia's iron overload: ineffective erythropoiesis suppresses hepcidin, freeing ferroportin to pump excess dietary iron into blood, so iron accumulates in heart and liver—the main cause of death in transfused patients."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Iron-overload cardiomyopathy is the leading killer in thalassemia: years of transfusion and gut iron absorption deposit iron in the myocardium, causing heart failure and arrhythmia, so iron chelation and cardiac MRI monitoring are central to survival."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Thalassemia reshapes the skeleton: chronic anemia drives massive marrow expansion that thins and deforms bones—frontal bossing, a 'hair-on-end' skull and fracture-prone osteoporosis—so the musculoskeletal changes are a visible signature of untreated disease."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "The placenta marks thalassemia's most severe form: alpha-thalassemia major (loss of all four genes) leaves the fetus unable to make functional hemoglobin, causing hydrops fetalis and stillbirth—so prenatal screening and intrauterine transfusion are how it is managed."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Thalassemia shapes reproductive choices and function: carrier screening and genetic counseling guide family planning, while iron overload from transfusions damages the pituitary and gonads, causing delayed puberty and infertility—so fertility care is part of treatment."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Thalassemia's anemia is largely macrophage-driven: defective red cells and their precursors are destroyed by splenic and marrow macrophages (extravascular hemolysis and ineffective erythropoiesis), so splenomegaly and iron recycling stem from this clearance."
---

# Thalassemia

## Overview

**Thalassaemias** are the most common single-gene disorders globally, affecting ~5% of the world's population as carriers and causing significant morbidity in ~300,000 new cases annually [^weatherall-2008-thalassemia-review]. They arise from mutations or deletions in the **α-globin genes (*HBA1, HBA2*, chromosome 16p13.3)** or **β-globin gene (*HBB*, chromosome 11p15.4)** that reduce or abolish synthesis of the corresponding globin chains, creating an imbalance in the α:β chain ratio.

**Pathophysiological principle:** Normal haemoglobin requires stoichiometric synthesis of α and β chains. When one chain is reduced:
- **Excess unpaired chains:** The remaining chains form unstable homotetramers (e.g., HbH = β₄ in α-thalassaemia; γ₄ = Hb Bart's in hydrops fetalis) or precipitate as inclusion bodies (excess α chains in β-thalassaemia) → membrane damage → premature RBC destruction
- **Ineffective erythropoiesis:** In β-thalassaemia major, 70-80% of erythroblasts die in the bone marrow before maturing (vs. ~5-10% normally) → massive compensatory erythropoietic expansion → extramedullary haematopoiesis (liver, spleen) → bone marrow expansion → facial/skull deformity (chipmunk facies, frontal bossing)
- **Haemolytic anaemia:** Surviving abnormal RBCs haemolyse in circulation → chronic anaemia → high-output cardiac failure if untransfused

**Global distribution:**
- Highest prevalence: Mediterranean, Middle East, South/Southeast Asia, Africa (malaria-endemic regions — heterozygous advantage)
- β-thal carrier frequency: ~3-5% in Mediterranean; ~1-2% in UK South Asian population; ~15-20% in Cyprus and Sardinia
- α-thal gene deletions: highest in Southeast Asia (up to 30% carrier frequency); significant in sub-Saharan Africa

## Structure

### α-Thalassemia: Deletion subtypes

Normal: 4 α-globin genes (2 per chromosome 16: αα/αα)

| Genotype | Deletion | Phenotype | Hb findings |
|:---------|:---------|:---------|:-----------|
| **α-Thal trait (2-gene deletion)** | -α/-α (trans) or --/αα (cis) | Mild microcytic anaemia; usually asymptomatic | HbA₂ normal; MCV ↓; MCH ↓ |
| **HbH disease (3-gene deletion)** | --/-α | Moderate haemolytic anaemia (Hb 7-10 g/dL); splenomegaly | HbH (β₄) on Hb HPLC; Heinz bodies |
| **Hydrops fetalis (4-gene deletion)** | --/-- | Severe fetal anaemia + hydrops → stillbirth or early neonatal death | Hb Bart's (γ₄) ~80-90%; requires in utero transfusion |
| **Silent carrier (1-gene deletion)** | -α/αα | Normal; occasional MCH/MCV borderline ↓ | Normal Hb HPLC |

**Cis vs trans deletions:**
- **Cis (--/αα):** Both deletions on same chromosome → high risk of hydrops fetalis if partner also carries cis deletion; common in Southeast Asian and Chinese populations
- **Trans (-α/-α):** One deletion per chromosome → cannot produce hydrops; common in African populations

**Non-deletion α-thalassaemia:** Point mutations in HBA2 (e.g., Hb Constant Spring, Hb Paksé) → frameshift → elongated α-chain that is unstable; found in Southeast Asia; similar phenotype to HbH disease

### β-Thalassemia: Severity spectrum

| Severity | Genotype | Hb without transfusion | Clinical features |
|:---------|:---------|:-----------------------|:-----------------|
| **β-Thal trait (minor)** | β/β⁰ or β/β⁺ | Normal or mildly ↓ (10-13 g/dL) | Microcytic hypochromic; HbA₂ >3.5%; no treatment needed |
| **β-Thal intermedia** | β⁺/β⁺ (mild alleles) or β/β⁰ with HbF inducers | 7-10 g/dL | Moderate; splenomegaly; episodic transfusion; iron overload from GI absorption |
| **β-Thal major** | β⁰/β⁰ or β⁰/β⁺ (severe) | 3-6 g/dL without Tx | Severe; transfusion-dependent; iron overload; skeletal deformity; hydroxyurea or luspatercept to ↑HbF or ↓ineffective erythropoiesis |

**Common HBB mutations by population:**
- IVS1-110 (G→A): Mediterranean; severe β⁺
- Codon 39 (C→T): Sardinian, Algerian; β⁰
- IVS1-1 (G→T): Indian subcontinent, Chinese; β⁰
- IVS2-1 (G→A): South Asian; β⁰
- -28 (A→G): Chinese; mild β⁺

**β⁰ = no β-globin production; β⁺ = reduced β-globin production; β++ = very mildly reduced**

### Hb F induction — the therapeutic target

Foetal haemoglobin (HbF, α₂γ₂) is normally silenced after birth by BCL11A (downregulates γ-globin genes) and ZBTB7A/LRF. HbF:
- Compensates for HbS (dilutes polymer fraction) and HbβS (provides functional Hb)
- HbF >30% of total Hb → significantly ameliorates clinical course in both SCD and β-thal
- Spontaneously high HbF producers (hereditary persistence of fetal haemoglobin, HPFH) have very mild β-thal major or SCD

## Function

### Pathophysiology of iron overload in β-Thalassemia

**Mechanism of paradoxical iron overload despite anaemia:**
1. Severe anaemia + hypoxia → massive EPO secretion → stress erythropoiesis (BFU-E and CFU-E expansion in bone marrow + liver/spleen)
2. Stressed erythroblasts secrete **ERFE (erythroferrone; FAMP-domain protein)** → ERFE binds and sequesters BMPs (BMP2, BMP6) in liver → suppresses BMP-SMAD signaling → ↓ hepcidin transcription
3. Low hepcidin → ferroportin maintained on duodenal enterocytes + macrophages → unconstrained iron absorption (3-5× normal) and recycling
4. In transfused β-thal major patients: transfusion iron + GI absorption → combined overload
5. Once TSAT approaches 100%: NTBI forms → ZIP14-mediated uptake by hepatocytes, cardiomyocytes, pituitary → Fenton chemistry → ROS → fibrosis and cell death

**Target organs of iron overload:**
- **Liver:** Hepatic fibrosis → cirrhosis; monitor with serum ferritin + liver iron concentration (MRI T2* or R2)
- **Heart (most critical):** Cardiac iron deposition → arrhythmia, LV dysfunction, heart failure → most common cause of death in inadequately chelated thal major; monitor cardiac MRI T2* (>20 ms = normal; <10 ms = severe)
- **Endocrine glands:** Pituitary → hypogonadotropic hypogonadism (most common; delayed puberty, infertility); pancreas → diabetes mellitus; thyroid → hypothyroidism; parathyroids → hypoparathyroidism
- **Bone:** Osteoporosis from marrow expansion + reduced sex hormones; vertebral fractures

### Skeletal complications

Untransfused or undertransfused β-thal major:
- Erythroid marrow expansion into cortical bone → bone marrow hypertrophy → frontal bossing, maxillary overgrowth (chipmunk facies), widened diploe on skull X-ray (hair-on-end pattern)
- Spinal cord compression from paraspinal extramedullary haematopoiesis
- Fractures from cortical thinning + low bone density

## Pathology

### Diagnosis

**Haematological:**
- CBC: Microcytic hypochromic anaemia; MCV typically 60-75 fL in thal major; RBC count elevated relative to Hb (distinguishes from IDA)
- Blood smear: Target cells, hypochromic microcytic cells, nucleated RBCs, Heinz bodies (HbH), basophilic stippling
- Reticulocyte count: Elevated (compensatory) but lower than expected for degree of anaemia (ineffective erythropoiesis)

**Haemoglobin HPLC/electrophoresis:**
- β-thal trait: HbA₂ >3.5% (normal 2.0-3.5%); HbF mildly elevated (1-3%)
- β-thal major: HbF >90% (if β⁰/β⁰); HbA absent or reduced; HbA₂ variable
- α-thal trait (2-gene deletion): Normal HPLC (no diagnostic Hb variant); diagnosis by α-globin gene deletion PCR
- HbH disease: HbH (β₄) detectable on HPLC; brilliant cresyl blue stain → HbH inclusion bodies in RBCs

**Molecular diagnosis:**
- HBA1/HBA2 deletion PCR (gap-PCR) or multiplex MLPA for common α-thal deletions
- HBB sequencing or targeted mutation panel for β-thalassaemia mutations
- Essential for carrier screening, prenatal diagnosis (CVS or amniocentesis)

### Treatment

**Transfusion therapy [^cappellini-2014-thalassemia-guidelines]:**
- **Target Hb:** Pre-transfusion Hb ≥9-10 g/dL (some centers target ≥10-11 g/dL for better suppression of endogenous ineffective erythropoiesis); leucocyte-depleted packed RBCs
- **Frequency:** Every 2-5 weeks; HbS-negative blood for SCD/HbSβ patients; antigen-matched blood (at least Rh + Kell) to minimize alloimmunization
- **Alloimmunization:** Major complication; occurs in 20-30% of chronically transfused patients; antibodies to Rh, Kell, Kidd, Duffy antigens; complicates future transfusion; screen before each transfusion
- **Delayed haemolytic transfusion reaction (DHTR):** Severe complication in alloimmunized patients — bystander haemolysis → acute anaemia; treat with IVIG, rituximab, eculizumab; avoid further transfusion if possible

**Chelation therapy (iron overload management):**
- Begin when: serum ferritin >1,000 ng/mL OR ≥10-20 transfusion episodes; cardiac MRI T2* <20 ms
- **Deferoxamine (DFO):** SC infusion 8-12h, 5-7 nights/week; most evidence base; audiometry and ophthalmology monitoring annually; growth and endocrine monitoring in children
- **Deferasirox (Exjade/Jadenu):** 14-28 mg/kg/day PO once daily; most widely used; renal and hepatic monitoring; effective for liver and cardiac iron
- **Deferiprone (Ferriprox):** 75-100 mg/kg/day PO in divided doses; superior for cardiac iron chelation (crosses cell membranes); weekly CBC for agranulocytosis; often combined with DFO
- **Target:** Ferritin <1,000 ng/mL; cardiac MRI T2* >20 ms; liver iron concentration <5 mg/g dry weight

**Luspatercept (Reblozyl; FDA 2020 for β-thal):**
- Mechanism: Recombinant ActRIIA ligand trap → binds TGF-β superfamily ligands (GDF11, activin B) → reduces SMAD2/3 signaling → relieves late-stage erythroid differentiation block → improved erythropoiesis and ↓ transfusion burden
- BELIEVE trial: 21% reduction in transfusion burden vs. placebo in transfusion-dependent β-thal major; ~50% of patients reduced transfusions by >33%
- Dosing: 1.0 mg/kg SC every 21 days; can increase to 1.25 mg/kg; for non-transfusion-dependent thal intermedia (BEYOND trial: 74% achieved ≥1 g/dL Hb increase)

**Hydroxyurea:**
- Increases HbF synthesis; more effective in β-thal intermedia than major (residual β-chain synthesis required); reduces transfusion need in carefully selected patients; combined with erythropoietin in some protocols

**Haematopoietic cell transplantation (HCT):**
- Only established cure; best results in children <7 years, low hepatomegaly/fibrosis (Pesaro class I/II): ~90% event-free survival with MSD (matched sibling donor)
- Pesaro class III (older, hepatomegaly, irregular chelation): ~80% EFS with intensive conditioning
- Matched unrelated donor (MUD): Increasingly feasible; ~75-85% EFS in class I/II patients with experienced centers
- Haploidentical: Emerging; post-transplant cyclophosphamide reduces GvHD; ~75-80% EFS in recent series

**Gene therapy (transformative) [^thompson-2018-zynteglo-nejm]:**
- **Betibeglogene autotemcel (Zynteglo; FDA August 2022):** Lentiviral vector encoding βA-T87Q-globin → integrated into autologous HSCs; HGB-207/HGB-212 trials: 89% of patients with non-β⁰/β⁰ genotypes became transfusion-independent (Hb ≥9 g/dL without transfusion); β⁰/β⁰ patients: reduced transfusion burden; durable responses at 7+ years follow-up
- **Exagamglogene autotemcel (Casgevy; FDA December 2023):** CRISPR-Cas9 edits BCL11A erythroid enhancer → BCL11A silenced in erythroid cells → γ-globin de-repressed → HbF re-expression >25-30% → compensates for absent β-globin; CLIMB-THAL-111 trial: 39/42 patients became transfusion-independent with Hb ≥11 g/dL; also FDA-approved for SCD
- **Limitations:** Very expensive (Zynteglo ~$2.8M; Casgevy ~$2.2M per patient); requires busulfan myeloablative conditioning; academic centers with expertise; access inequities

### Prenatal diagnosis and prevention

- Carrier couples (both β-thal trait): 25% probability of thal major in each pregnancy
- Prenatal testing: Chorionic villus sampling (CVS) at 10-13 weeks → HBB molecular analysis; amniocentesis at 15-18 weeks; pre-implantation genetic diagnosis (PGD) with IVF
- Prevention programs: Cyprus, Sardinia, Iran have national programs → dramatically reduced thal major births; carrier screening in Mediterranean, South Asian, Chinese communities

## Connections

- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Thalassaemias arise from imbalanced α- or β-globin chain synthesis; excess unpaired chains precipitate → ineffective erythropoiesis and haemolysis; HbA₂ (α2δ2) elevation >3.5% diagnoses β-thal trait; HbH (β4 tetramers) is the signature of 3-gene α-thal deletion.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — β-thal major: ineffective erythropoiesis → ERFE ↑ → hepcidin suppression → unconstrained iron absorption → TSAT 100% → NTBI → tissue deposition; deferasirox (oral) and deferoxamine (parenteral) are the mainstay chelators targeting transferrin-bound and NTBI iron.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Ineffective erythropoiesis in β-thalassaemia → ERFE from stress erythroblasts → suppresses BMP-SMAD → ↓ hepcidin → ↑ ferroportin → unconstrained iron absorption despite anemia; luspatercept (ActRIIA ligand trap) reduces ineffective erythropoiesis and partially restores hepcidin.
- `connects-to` → **[Sickle Cell Disease](../sickle-cell-disease/README.md)** — HbSβ-thalassemia (HbS + β-thal allele) is a common SCD genotype; severity depends on β-thal allele type (β⁰ = severe SCA-like; β⁺ = milder); gene therapy approaches (Zynteglo, Casgevy) target both SCD and β-thal major as overlapping haemoglobinopathies.
- `connects-to` → **[G6PD](../../03-molecular/g6pd/README.md)** — Thalassaemia (HbE/β-thal most common in SEA) co-occurs with G6PD Mahidol/Viangchan; G6PD deficiency + beta-thalassaemia → additive oxidant haemolysis; G6PD screening is recommended in thalassaemia; both adaptations cluster in malaria-endemic regions by balanced selection.
- `connects-to` → **[Activin A](../../03-molecular/activin-a/README.md)** — Activin A/B → ActRIIB on late erythroblasts → SMAD2/3 → maturation block → ineffective erythropoiesis in beta-thalassemia; luspatercept (BELIEVE trial: 21% achieved ≥33% transfusion reduction vs. 4.5% placebo) traps activin A/B → accelerates terminal erythroid differentiation.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — In thalassemia the imbalance of α and β globin leaves unpaired chains that precipitate inside red cells, so most erythroblasts die in the marrow before maturing (ineffective erythropoiesis) and survivors are microcytic, hypochromic target cells that haemolyse.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Thalassemia causes iron overload despite anaemia: ineffective erythropoiesis releases erythroferrone that suppresses hepcidin, so dietary iron pours in unchecked and transfusions add more; the excess poisons heart, liver, and endocrine glands, making chelation lifesaving.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Iron-loaded cardiomyocytes make the heart the leading killer in undertreated thalassaemia major: NTBI enters via calcium channels → Fenton free radicals → arrhythmia and cardiomyopathy; cardiac MRI T2* (<10 ms = severe) guides chelation before heart failure.
- `connects-to` → **[Malaria](../malaria/README.md)** — Thalassemia, like sickle trait, is a malaria-protective hemoglobinopathy: its high gene frequency across the Mediterranean, Middle East and Asia reflects balancing selection, as α- and β-thalassemia carriers resist severe Plasmodium falciparum—matching the historic malaria map.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Thalassemia is driven by ineffective erythropoiesis: unbalanced globin chains precipitate and kill red-cell precursors in the marrow, which expands massively (skeletal deformities, extramedullary hematopoiesis); luspatercept eases this block and transfusions suppress the marrow.
- `connects-to` → **[Iron Deficiency Anemia](../iron-deficiency-anemia/README.md)** — Thalassemia trait is the key differential of iron-deficiency anemia: both cause microcytic, hypochromic cells, but thalassemia has normal/high iron, a low Mentzer index and raised HbA2 while IDA shows low ferritin—mislabeling it as IDA causes harmful needless iron use.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — The spleen bears the brunt of thalassemia: it works overtime clearing defective red cells and hosts extramedullary hematopoiesis, enlarging massively and worsening anemia by trapping blood—so splenectomy is sometimes needed but leaves patients prone to sepsis.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver is a major casualty of transfusion-dependent thalassemia: lifelong transfusions and increased gut iron absorption load the liver with iron, causing cirrhosis unless iron chelation is maintained—and hepatic iron quantified by MRI guides chelation therapy.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Thalassemia causes a distinctive osteoporosis: marrow expansion from chronic anemia thins cortical bone, while iron overload and endocrine damage impair osteoblasts and sex hormones—so fragility fractures are common and bone-density monitoring is part of care.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Erythropoietin runs high in thalassemia: severe anemia drives massive EPO release, but defective globin chains make erythropoiesis ineffective, so the marrow expands uselessly—causing skeletal deformities and extramedullary hematopoiesis instead of functional red cells.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Thalassemia impairs oxygen delivery at its root: too few normal hemoglobin tetramers mean less oxygen per red cell, so tissues stay hypoxic despite a racing marrow—and the hypoxic drive fuels the bone expansion and high-output cardiac strain of severe disease.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Iron overload makes thalassemia an endocrine disease: transfusion and gut iron deposit in glands, causing diabetes, hypogonadism, hypothyroidism and growth failure, so the endocrine system bears much of the chronic morbidity—and iron chelation aims to prevent it.
- `connects-to` → **[Ferroportin](../../03-molecular/ferroportin/README.md)** — Ferroportin sits at the heart of thalassemia's iron overload: ineffective erythropoiesis suppresses hepcidin, freeing ferroportin to pump excess dietary iron into blood, so iron accumulates in heart and liver—the main cause of death in transfused patients.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Iron-overload cardiomyopathy is the leading killer in thalassemia: years of transfusion and gut iron absorption deposit iron in the myocardium, causing heart failure and arrhythmia, so iron chelation and cardiac MRI monitoring are central to survival.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Thalassemia reshapes the skeleton: chronic anemia drives massive marrow expansion that thins and deforms bones—frontal bossing, a 'hair-on-end' skull and fracture-prone osteoporosis—so the musculoskeletal changes are a visible signature of untreated disease.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — The placenta marks thalassemia's most severe form: alpha-thalassemia major (loss of all four genes) leaves the fetus unable to make functional hemoglobin, causing hydrops fetalis and stillbirth—so prenatal screening and intrauterine transfusion are how it is managed.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Thalassemia shapes reproductive choices and function: carrier screening and genetic counseling guide family planning, while iron overload from transfusions damages the pituitary and gonads, causing delayed puberty and infertility—so fertility care is part of treatment.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Thalassemia's anemia is largely macrophage-driven: defective red cells and their precursors are destroyed by splenic and marrow macrophages (extravascular hemolysis and ineffective erythropoiesis), so splenomegaly and iron recycling stem from this clearance.

[^weatherall-2008-thalassemia-review]: Weatherall DJ. The inherited diseases of hemoglobin are an emerging global health burden. *Blood.* 2010;115(22):4331-4336. [doi:10.1182/blood-2010-01-251348](https://doi.org/10.1182/blood-2010-01-251348) · [PubMed 20233970](https://pubmed.ncbi.nlm.nih.gov/20233970/)
[^cappellini-2014-thalassemia-guidelines]: Cappellini MD, Cohen A, Porter J, et al. (eds). Guidelines for the Management of Transfusion Dependent Thalassaemia (TDT). 3rd ed. Thalassaemia International Federation; 2014.
[^thompson-2018-zynteglo-nejm]: Thompson AA, Walters MC, Kwiatkowski J, et al. Gene therapy in patients with transfusion-dependent β-thalassemia. *N Engl J Med.* 2018;378(16):1479-1493. [doi:10.1056/NEJMoa1705342](https://doi.org/10.1056/NEJMoa1705342) · [PubMed 29669226](https://pubmed.ncbi.nlm.nih.gov/29669226/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
