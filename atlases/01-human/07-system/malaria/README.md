---
schema: human-scale-entry/v1
id: malaria
name: Malaria
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Malaria (Plasmodium falciparum primarily) kills ~600,000 annually; Anopheles-transmitted sporozoites → hepatocytes → RBC invasion → haemolysis + fever cycles; artemisinin-based combination therapy is first-line; G6PD and HbS variants confer partial protective advantage."
aliases: ["malaria", "Plasmodium falciparum", "P. falciparum", "P. vivax", "falciparum malaria", "cerebral malaria", "severe malaria", "uncomplicated malaria", "parasitaemia"]
sources:
  - id: who-malaria-report-2023
    type: clinical-guideline
    cite: "World Health Organization. World Malaria Report 2023. WHO; 2023."
    url: "https://www.who.int/teams/global-malaria-programme/reports/world-malaria-report-2023"
    accessed: "2026-06-08"
  - id: white-2014-malaria-lancet
    type: peer-reviewed
    cite: "White NJ, Pukrittayakamee S, Hien TT, et al. Malaria. Lancet. 2014;383(9918):723-735."
    doi: "10.1016/S0140-6736(13)60024-0"
    pmid: "23953767"
    url: "https://doi.org/10.1016/S0140-6736(13)60024-0"
  - id: dondorp-2010-severe-malaria-lancet
    type: peer-reviewed
    cite: "Dondorp AM, Fanello CI, Hendriksen IC, et al. Artesunate versus quinine in the treatment of severe falciparum malaria in African children (AQUAMAT). Lancet. 2010;376(9753):1647-1657."
    doi: "10.1016/S0140-6736(10)61924-1"
    pmid: "21062666"
    url: "https://doi.org/10.1016/S0140-6736(10)61924-1"
cross_links:
  - target: 01-human/03-molecular/g6pd
    relation: connects-to
    note: "G6PD heterozygosity confers ~50% protection vs severe malaria in females (mosaic RBC); G6PD-deficient patients risk haemolysis with primaquine or tafenoquine; WHO mandates G6PD quantitative testing before 8-aminoquinoline prescription."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "HbAS (sickle trait) confers ~60% protection against severe P. falciparum malaria; HbC and thalassaemia trait also protective; P. falciparum digests haemoglobin → haemozoin; Hb variants and G6PD polymorphisms co-distribute with malaria endemicity."
  - target: 01-human/07-system/sickle-cell-disease
    relation: connects-to
    note: "HbAS (sickle trait) confers ~60% protection against severe malaria (balanced polymorphism); HbSS patients in endemic regions face compounded risk: fever + dehydration → sickling crises; antimalarial prophylaxis planning is essential for HbSS in endemic areas."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Severe falciparum malaria causes AKI in 4-8% (haemoglobinuria + microvascular obstruction + cytokine storm); cerebral malaria + AKI → high mortality; repeated malaria episodes contribute to CKD burden in endemic populations."
  - target: 01-human/07-system/iron-deficiency-anemia
    relation: connects-to
    note: "Iron deficiency partially protective against P. falciparum (iron-restricted parasites grow less vigorously); iron supplementation in endemic areas should follow malaria treatment to avoid feeding parasites; IDA and malaria co-exist in sub-Saharan Africa."
  - target: 02-pathogen/04-parasites/plasmodium-falciparum
    relation: connects-to
    note: "Plasmodium falciparum, spread by Anopheles mosquitoes, is the deadliest malaria parasite: it cytoadheres infected red cells to brain endothelium via PfEMP1, evades immunity by var-gene switching, and is treated with artemisinin combinations now threatened by kelch13 resistance."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Malaria's blood stage runs in red cells: merozoites invade via AMA1/EBA-glycophorin, digest hemoglobin into haemozoin, and rupture every 48h triggering fever; haemolysis plus dyserythropoiesis causes severe anemia, while inherited RBC variants (HbS, G6PD) blunt parasite growth."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Cerebral malaria is the most lethal complication of P. falciparum: PfEMP1-coated red cells sequester on ICAM-1 in brain microvessels, obstructing flow and breaking the blood-brain barrier → coma; mortality is 15-25%, and ~25% of survivors retain neurological sequelae."
  - target: 01-human/07-system/leishmaniasis
    relation: connects-to
    note: "Both are vector-borne protozoan parasites of the global poor: Anopheles-borne Plasmodium invades erythrocytes, sand-fly-borne Leishmania hides in macrophages; both cause fever, splenomegaly and anemia in overlapping tropical regions, and HIV co-infection worsens both."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Malaria's obligatory pre-erythrocytic stage is hepatic: sporozoites invade hepatocytes and mature into thousands of merozoites before blood-stage disease; P. vivax/ovale form dormant hypnozoites needing primaquine/tafenoquine for radical cure; severe malaria also causes jaundice."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "TNF-α drives malaria's inflammatory pathology: schizont rupture and GPI anchors trigger macrophage TNF-α → fever, hypoglycemia and ICAM-1 upregulation, promoting PfEMP1-mediated sequestration in cerebral malaria; high circulating TNF-α correlates with severity and mortality."
  - target: 01-human/07-system/thalassemia
    relation: connects-to
    note: "Thalassemia, like sickle cell trait, is maintained by malaria selection: abnormal or reduced hemoglobin makes red cells a poorer host for Plasmodium, conferring partial protection from severe malaria—why it is common across the historic malaria belt."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "The spleen is central to malaria: it filters and destroys parasitized red cells, driving the splenomegaly typical of chronic infection, and the parasite evades it by sequestering in deep vasculature—so splenectomy or asplenia markedly worsens malaria severity."
  - target: 01-human/07-system/burkitt-lymphoma
    relation: connects-to
    note: "Endemic Burkitt lymphoma is a malaria-driven cancer: chronic Plasmodium falciparum infection causes intense B-cell proliferation and weakens control of co-infecting Epstein-Barr virus, together driving the MYC translocation behind the jaw tumors of African children."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Malaria causes severe anemia by several routes: rupture of infected red cells, splenic clearance of uninfected cells, and inflammatory suppression of erythropoiesis (an anemia-of-chronic-disease component) combine, making anemia a leading cause of malaria death in children."
  - target: 01-human/06-organ/ards
    relation: connects-to
    note: "Severe falciparum malaria can cause ARDS: sequestration of infected red cells and intense inflammation injure the pulmonary capillaries, flooding alveoli with edema even after parasite clearance—acute respiratory distress is a feared complication of severe malaria."
  - target: 01-human/07-system/disseminated-intravascular-coagulation
    relation: connects-to
    note: "Severe malaria can trigger disseminated intravascular coagulation: widespread endothelial activation and cytokine storm in falciparum infection consume clotting factors and platelets, causing bleeding—part of the multi-organ failure that makes severe malaria lethal."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Severe malaria injures the kidney: hemolysis and sequestration cause acute kidney injury and, classically, blackwater fever (massive hemoglobinuria), so renal failure marks severe falciparum malaria and worsens its high mortality."
  - target: 01-human/07-system/cytokine-storm
    relation: connects-to
    note: "Severe malaria is partly a cytokine storm: schizont rupture triggers a TNF-driven inflammatory surge causing fever, and excess cytokines contribute to cerebral malaria and organ failure—so the host inflammatory response, not just the parasite, drives lethal disease."
  - target: 01-human/07-system/dengue-fever
    relation: connects-to
    note: "Malaria and dengue are the great overlapping tropical fevers: both cause fever and thrombocytopenia in the same regions, so a febrile traveler needs both excluded—malaria (a treatable parasite) must never be missed while dengue (a virus) is managed supportively."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "Malaria targets the placenta in pregnancy: infected red cells bind a unique placental receptor (CSA) and sequester there, causing maternal anemia, low birth weight, and stillbirth—so first pregnancies in endemic areas carry special risk, prompting preventive treatment."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Cerebral malaria is a disease of the endothelium: infected red cells express adhesion proteins that stick to blood-vessel linings, sequestering in the brain's microvessels, blocking flow and inflaming the barrier—causing the coma that makes falciparum malaria lethal."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Malaria immunity is hard-won and incomplete: repeated infection builds partial 'premunition' that lets endemic adults tolerate parasites, but it wanes without exposure—and this slow, leaky immunity is exactly why an effective malaria vaccine (RTS,S, R21) took so long."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "Malaria's silent first stage is in hepatocytes: injected sporozoites invade liver cells and multiply before the blood stage, and in P. vivax and ovale dormant hypnozoites hide there for months—causing relapses that need a separate drug (primaquine) to clear."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Nitric oxide is double-edged in malaria: it helps kill parasites, but in cerebral malaria dysregulated NO and endothelial activation contribute to the coma and brain injury that make it the deadliest complication."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron and malaria are dangerously intertwined: the parasite needs iron to grow, so iron supplementation can worsen malaria in endemic areas—while repeated infection also causes anemia, complicating how iron deficiency is treated where malaria is common."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Severe malaria spills potassium from burst red cells: massive hemolysis and kidney injury raise blood potassium, and the released hemoglobin can darken the urine (blackwater fever)—dangerous electrolyte shifts in the sickest patients."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "The spleen's macrophages fight and are fooled by malaria: they engulf parasitized red cells and the dark hemozoin pigment, enlarging the spleen, yet the parasite's surface tricks sustain infection—and a ruptured malarial spleen is a feared emergency."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Severe malaria activates complement: C3 and the cascade fire on parasite and immune complexes, fueling the inflammation and red-cell destruction behind severe anemia and organ damage—part of the immune over-response that turns malaria lethal."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Malaria cripples the bone marrow: the parasite and its hemozoin pigment suppress red-cell production (dyserythropoiesis), so blunted marrow output compounds the destruction of infected cells to deepen malarial anemia."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "Severe malaria floods the blood with hydrogen ions: parasite and tissue starvation generate lactic acid, and the resulting metabolic acidosis (acidemia) is one of the strongest predictors of death in severe disease."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Thrombocytopenia is the rule in malaria: platelets are consumed and trapped in the spleen as the infection activates clotting, so a low platelet count is one of the most reliable clues that a fever is malaria."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Malaria is still diagnosed by light: Giemsa-stained thick and thin blood films under the microscope reveal the parasites inside red cells, letting the species be identified and the parasite load counted."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Severe malaria suffocates tissues: sequestered red cells block capillaries while profound anemia cuts oxygen delivery, driving the lactic acidosis and organ failure that mark the deadliest disease."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "The retina betrays cerebral malaria: malarial retinopathy—patchy whitening, vessel discoloration and hemorrhages—is a specific bedside sign that a comatose child's illness is truly malaria and not another cause."
---

# Malaria

## Overview

**Malaria** is a mosquito-borne infectious disease caused by intracellular parasites of the genus *Plasmodium*, transmitted exclusively by female *Anopheles* mosquitoes. It remains one of the most significant infectious diseases globally: in 2022, the WHO estimated **249 million cases** and **608,000 deaths** annually — predominantly children <5 years in sub-Saharan Africa [^who-malaria-report-2023].

**Five *Plasmodium* species cause human malaria:**

| Species | Clinical severity | Unique feature |
|:--------|:----------------|:---------------|
| ***P. falciparum*** | Highest; most deaths | Cytoadherence of infected RBCs → microvascular obstruction; cerebral malaria; artemisinin resistance emerging |
| ***P. vivax*** | Moderate; liver hypnozoites | Relapsing malaria (Duffy antigen receptor required for RBC invasion; absent in most West Africans → natural resistance) |
| ***P. ovale*** | Mild; hypnozoites | Two subspecies (curtisi/wallikeri); difficult to distinguish from P. vivax clinically |
| ***P. malariae*** | Mild; very long latency | Can persist decades; associated with nephrotic syndrome |
| ***P. knowlesi*** | Moderate-severe | Zoonosis from macaques in Southeast Asia; formerly mistaken for P. malariae |

## Structure

### Life cycle — key stages relevant to immunity and treatment

**Mosquito → Human transmission:**
1. *Anopheles* female takes blood meal → injects **sporozoites** from salivary glands into dermis → sporozoites reach bloodstream within 30-60 min
2. Sporozoites traverse Kupffer cells → infect **hepatocytes** via interactions with heparan sulfate proteoglycans and CD81/SR-BI receptors

**Liver stage (exoerythrocytic schizogony; 6-15 days, species-dependent):**
3. Sporozoite → **liver schizont** (asymptomatic); massive replication: 1 sporozoite → ~10,000–40,000 **merozoites** per hepatocyte
4. **P. vivax and P. ovale only:** Some sporozoites form dormant **hypnozoites** in hepatocytes → weeks to years later, hypnozoites reactivate → relapse; requires primaquine/tafenoquine for radical cure
5. Schizont ruptures → **merozoites** released into bloodstream as **merosomes** (protected from immune attack by host platelet/fibrin coating)

**Blood stage (erythrocytic schizogony; 48h for P. falciparum; 72h for P. malariae):**
6. Merozoite invades RBC via: **AMA1/RON complex**, **MSP1**, **EBA175/EBA140** binding to glycophorin A/B, band 3; RBC deforms → merozoite enters sealed parasitophorous vacuole membrane (PVM)
7. **Ring stage** (1-24h): Parasite metabolically active; HRP2 antigen shed
8. **Trophozoite stage** (24-36h): Haemoglobin digestion → **haemozoin (malaria pigment)** crystals; PfEMP1 (P. falciparum erythrocyte membrane protein 1) expressed on RBC surface → cytoadherence to ICAM-1 on brain endothelium (cerebral malaria), CD36 on placental syncytiotrophoblasts (placental malaria)
9. **Schizont stage** (36-48h): Division → 16-32 daughter merozoites
10. **Schizont rupture → fever spike**: Merozoite egress → haemozoin + GPI anchors + uric acid crystals released → TLR-9/NLRP3 activation → TNF-α, IL-6, IL-1β → fever + rigors + systemic inflammation
11. **Gametocytes**: Some parasites differentiate into gametocytes → ingested by mosquito → sexual reproduction in mosquito gut → oocyst → sporozoites → salivary glands → new cycle

### *P. falciparum* virulence mechanisms

**Cytoadherence:**
- PfEMP1 binds CD36 (rosetting), ICAM-1 (cerebral malaria), EPCR (severe malaria), chondroitin sulfate A (CSA; placental malaria)
- Brain endothelium: PfEMP1/ICAM-1 → infected RBCs trapped in cerebral microvessels → direct obstruction + endothelial activation + blood-brain barrier breakdown → cerebral malaria

**Rosetting:**
- Infected RBCs bind uninfected RBCs → rosettes → microvascular blockade + shielding of PfEMP1 from antibodies

**Knob formation:**
- Parasite remodels RBC cytoskeleton → knobs on RBC surface → projections for cytoadherence; KHARP and PfEMP3 cross-link spectrin network

**Immune evasion:**
- PfEMP1 has ~60 var gene variants per parasite genome; var gene switching → antigenic variation → parasites escape existing antibodies; children develop immunity only after years of repeated infections (var gene repertoire exhaustion)

## Function

### Pathophysiology of severe malaria

**Severe malaria criteria (WHO 2015):**
- **Cerebral malaria:** Unrousable coma + P. falciparum parasitaemia + no other cause; retinal haemorrhages on fundoscopy (80% sensitive); mortality 15-25% with treatment; neurological sequelae in ~25% of survivors
- **Severe anaemia:** Hb <5 g/dL in adults (<7 g/dL in children) + parasitaemia; from RBC haemolysis + dyserythropoiesis + splenic sequestration
- **Respiratory distress / ARDS:** Cytokine storm → pulmonary capillary leak → non-cardiogenic pulmonary oedema; mortality >40%
- **Acute kidney injury:** Haemoglobinuria (blackwater fever) + microvascular obstruction; IV artesunate reduces AKI risk vs. quinine (AQUAMAT)
- **Hypoglycaemia:** Parasite glucose consumption + insulin secretion from quinine/quinidine treatment + counter-regulatory failure
- **Hyperparasitaemia:** >10% parasitaemia associated with poor prognosis; exchange transfusion controversial
- **Coagulopathy/DIC:** Cytokine storm → TF expression → thrombin → fibrin; haemolysis → haem → endothelial injury

**Mechanisms of malarial anaemia:**
1. Direct haemolysis (schizont rupture; infected RBC lifespan ~48h vs. 120 days normal)
2. Destruction of uninfected RBCs (bystander haemolysis; antibody + complement-mediated; phagocytosis by activated macrophages)
3. Dyserythropoiesis (suppression of erythroid progenitors by TNF-α, IL-10, haemozoin; ineffective erythropoiesis)
4. Splenic clearance (clearance of ring-infected RBCs by enhanced splenic filtration; splenomegaly)
5. Rosetting reduces RBC deformability → mechanical haemolysis in capillaries

**Cerebral malaria mechanism:**
- PfEMP1-ICAM-1 cytoadherence in brain microvessels + rosetting → obstructed flow → reduced O₂ delivery → lactic acidosis
- Endothelial activation → NO depletion (haemoglobin scavenges NO from haemolysis), TNF-α, VEGF → blood-brain barrier disruption → cerebral oedema
- Brain herniation → brainstem compression → death

## Pathology

### Diagnosis

**Microscopy (gold standard):**
- Thick blood smear: Sensitive (~10 parasites/μL); quantifies parasitaemia
- Thin blood smear: Species identification; ring vs. trophozoite vs. schizont; gametocytes
- Giemsa stain: Required for definitive diagnosis
- Limitation: Requires skilled microscopist; time-consuming

**Rapid diagnostic tests (RDTs):**
- Immunochromatographic strips detecting **HRP2** (*P. falciparum*-specific; high sensitivity), **pLDH** (all species), or **aldolase** (pan-*Plasmodium*)
- WHO mandates RDT or microscopy confirmation before treatment
- HRP2 RDT can remain positive for 2-3 weeks after successful treatment (persistent antigen)
- *Pfhrp2/3* gene deletions in some *P. falciparum* strains → false-negative HRP2 RDT (emerging problem in South America, Africa)

**PCR/qPCR:**
- Most sensitive (1-5 parasites/μL); gold standard for low parasitaemia, species confirmation, mixed infections, resistance genotyping
- Not routinely available in endemic settings

### Treatment

**WHO 2023 treatment guidelines [^white-2014-malaria-lancet]:**

**Uncomplicated P. falciparum malaria — first-line: Artemisinin-based combination therapy (ACT):**

| ACT | Components | Dosing | Notes |
|:----|:-----------|:-------|:------|
| **Artemether-lumefantrine (Coartem)** | Artemether 20 mg + lumefantrine 120 mg | 4-dose over 3 days (weight-based) | Most widely used globally; with fatty food |
| **Artesunate-amodiaquine** | Artesunate 100 mg + amodiaquine 270 mg | 3-day course | Sub-Saharan Africa; G6PD concerns with amodiaquine |
| **Artesunate-mefloquine** | Artesunate 200 mg + mefloquine 440 mg | 3-day course | Southeast Asia (especially Thailand-Myanmar border) |
| **Dihydroartemisinin-piperaquine (DHA-PPQ; Eurartesim)** | DHA 40 mg + piperaquine 320 mg | 3-day course | Fasting required; QTc prolongation monitoring |
| **Artesunate-pyronaridine** | Artesunate 200 mg + pyronaridine 540 mg | 3-day course | Newer; effective against artemisinin-partial resistance |

**Mechanism of artemisinins:**
- Artemisinins are sesquiterpene lactones with an endoperoxide bridge → activated by haem iron released during haemoglobin digestion → carbon-centered free radicals → alkylate parasite proteins (PfKRS, PfATP4) and membranes → parasite death
- **Partial artemisinin resistance (kelch13 mutations):** K13 propeller domain mutations (C580Y most common; Southeast Asia) → delayed parasite ring-stage clearance; clinical artemisinin resistance defined as >10% ring-stage survival in RSA assay or persistent parasitaemia at 72h
- ACT remains effective if partner drug is active → but partner drug (piperaquine, lumefantrine) resistance accumulating in Southeast Asia → TRIPLE artemisinin-based combination therapies (TACTs) under development

**Severe P. falciparum malaria — IV artesunate (first-line):**
- Artesunate 2.4 mg/kg IV at 0, 12, 24h then daily; superior to quinine in SEAQUAMAT (adult Asia) and AQUAMAT (children Africa) trials → ~22-35% mortality reduction
- Switch to oral ACT as soon as tolerated; complete 3-day ACT course
- Supportive care: IV glucose (hypoglycaemia), transfusion if Hb <7 g/dL, exchange transfusion (debated; parasitaemia >10%), broad-spectrum antibiotics (frequent bacterial co-infection)

**P. vivax / P. ovale — radical cure:**
- Blood stage: Chloroquine (where sensitive) 3 days; ACT if chloroquine-resistant P. vivax (e.g., Indonesia, Papua New Guinea)
- Radical cure (hypnozoites): **Primaquine 15 mg/day × 14 days** (WHO standard) or **primaquine 30 mg/day × 7 days** (short-course, if G6PD normal); **tafenoquine 300 mg × 1 dose** (single-dose radical cure, FDA/TGA approved 2018)
- **Mandatory G6PD testing before primaquine or tafenoquine**: G6PD-deficient patients → primaquine → haemolysis; tafenoquine contraindicated if G6PD <70% of normal; supervised weekly primaquine (0.75 mg/kg once weekly × 8 weeks) is alternative for G6PD-deficient individuals (Class III)

**Prevention and chemoprophylaxis:**
- **Personal protection:** Insecticide-treated bed nets (ITNs); indoor residual spraying (IRS); DEET/picaridin repellents
- **Chemoprophylaxis:**
  - Atovaquone-proguanil (Malarone): Daily, start 1-2 days before, continue 7 days after travel; well-tolerated; broad-spectrum
  - Doxycycline: Daily; carotid for Southeast Asia (mefloquine resistance); photosensitivity; contraindicated in pregnancy/children
  - Mefloquine: Weekly; prophylactic for chloroquine-resistant areas; neuropsychiatric side effects
  - Chloroquine: Weekly; only for chloroquine-sensitive areas (Central America, some Caribbean)
- **Seasonal malaria chemoprevention (SMC):** Intermittent preventive treatment with SP-AQ in children <5 in Sahel region; reduces malaria incidence by 75%
- **Preventive treatment in pregnancy (IPTp):** SP (sulfadoxine-pyrimethamine) 3+ doses in pregnancy in sub-Saharan Africa; reduces placental malaria and LBW
- **Vaccine (RTS,S/AS01; Mosquirix and R21/Matrix-M):**
  - **RTS,S/AS01E (Mosquirix):** WHO-recommended 2021; 4-dose schedule; 36-40% efficacy against clinical malaria over 4 years; widely deployed in Ghana, Kenya, Malawi (pilot program)
  - **R21/Matrix-M (Serum Institute/Oxford):** WHO-prequalified 2023; 75-77% efficacy in seasonal areas; superior to RTS,S; scale-up underway

### Immunity and genetic resistance

**Naturally acquired immunity:**
- After repeated exposure, adults in high-transmission areas develop clinical immunity (non-sterile; parasites persist but at lower density → asymptomatic)
- Immunity mediated by: IgG antibodies against PfEMP1 variants (var gene collection), merozoite surface antigens (MSP1, MSP2, AMA1); CD4+ T cells; regulatory T cells can suppress inflammation (beneficial in severe malaria)
- Maternal antibody transfer → neonates protected for 3-6 months → "honeymoon period" before first malaria episode

**Genetic protective factors:**
| Variant | Mechanism of protection | Population |
|:--------|:------------------------|:-----------|
| HbAS (sickle cell trait) | Impaired parasite invasion/growth; HbS polymerization in low O₂ → parasite can't grow → enhanced clearance | Sub-Saharan Africa |
| HbSS | Partial protection in endemic areas; severe malaria risk reduced | |
| HbC (heterozygous) | Reduced RBC surface PfEMP1 expression → less cytoadherence | West Africa |
| α-thalassaemia | Reduces severe malaria mortality; increases mild malaria frequency (epidemiological paradox) | Worldwide |
| G6PD heterozygosity (females) | Mosaic RBC population → infected G6PD-deficient RBCs cleared faster | Africa, Asia |
| Duffy antigen negativity | *P. vivax* requires Duffy antigen (DARC) for invasion → 95% of West Africans Duffy-negative → complete P. vivax resistance | West Africa |
| HLA-B53 | Enhanced CD8+ T cell responses to liver stage | West Africa |

## Connections

- `connects-to` → **[G6PD](../../03-molecular/g6pd/README.md)** — G6PD heterozygosity confers ~50% protection against severe malaria; G6PD-deficient patients risk acute haemolysis with primaquine (P. vivax radical cure) or tafenoquine; WHO mandates G6PD testing before 8-aminoquinoline prescription; G6PD deficiency is the dominant pharmacogenomic interaction in malaria treatment.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — HbAS (sickle trait) confers ~60% protection against severe P. falciparum malaria; HbSS provides partial protection (parasite invasion of sickled RBCs impaired); thalassaemia and HbC also protective; overlapping Hb variant and G6PD polymorphism distributions reflect centuries of malaria selection.
- `connects-to` → **[Sickle Cell Disease](../sickle-cell-disease/README.md)** — HbAS (sickle cell trait) confers ~60% protection against severe and fatal malaria; the HbS allele frequency in sub-Saharan Africa (6-15%) is maintained by malaria selection (balanced polymorphism); HbSS patients exposed to malaria face increased sickling crises from fever + dehydration.
- `connects-to` → **[CKD](../ckd/README.md)** — Severe falciparum malaria causes acute kidney injury (AKI) in 4-8% of cases (haemoglobinuria, parasite microvascular obstruction, cytokine storm); cerebral malaria + AKI → poor prognosis; malaria-endemic populations have higher CKD prevalence partly from repeated acute kidney insults.
- `connects-to` → **[Iron Deficiency Anemia](../iron-deficiency-anemia/README.md)** — Iron deficiency partially protective against P. falciparum (iron-restricted parasites grow less vigorously); iron supplementation in endemic areas should follow malaria treatment to avoid feeding parasites; IDA and malaria co-exist in sub-Saharan Africa.
- `connects-to` → **[Plasmodium falciparum](../../../02-pathogen/04-parasites/plasmodium-falciparum/README.md)** — Plasmodium falciparum, spread by Anopheles mosquitoes, is the deadliest malaria parasite: it cytoadheres infected red cells to brain endothelium via PfEMP1, evades immunity by var-gene switching, and is treated with artemisinin combinations now threatened by kelch13 resistance.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Malaria's blood stage runs in red cells: merozoites invade via AMA1/EBA-glycophorin, digest hemoglobin into haemozoin, and rupture every 48h triggering fever; haemolysis plus dyserythropoiesis causes severe anemia, while inherited RBC variants (HbS, G6PD) blunt parasite growth.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Cerebral malaria is the most lethal complication of P. falciparum: PfEMP1-coated red cells sequester on ICAM-1 in brain microvessels, obstructing flow and breaking the blood-brain barrier → coma; mortality is 15-25%, and ~25% of survivors retain neurological sequelae.
- `connects-to` → **[Leishmaniasis](../leishmaniasis/README.md)** — Both are vector-borne protozoan parasites of the global poor: Anopheles-borne Plasmodium invades erythrocytes, sand-fly-borne Leishmania hides in macrophages; both cause fever, splenomegaly and anemia in overlapping tropical regions, and HIV co-infection worsens both.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Malaria's obligatory pre-erythrocytic stage is hepatic: sporozoites invade hepatocytes and mature into thousands of merozoites before blood-stage disease; P. vivax/ovale form dormant hypnozoites needing primaquine/tafenoquine for radical cure; severe malaria also causes jaundice.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — TNF-α drives malaria's inflammatory pathology: schizont rupture and GPI anchors trigger macrophage TNF-α → fever, hypoglycemia and ICAM-1 upregulation, promoting PfEMP1-mediated sequestration in cerebral malaria; high circulating TNF-α correlates with severity and mortality.
- `connects-to` → **[Thalassemia](../thalassemia/README.md)** — Thalassemia, like sickle cell trait, is maintained by malaria selection: abnormal or reduced hemoglobin makes red cells a poorer host for Plasmodium, conferring partial protection from severe malaria—why it is common across the historic malaria belt.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — The spleen is central to malaria: it filters and destroys parasitized red cells, driving the splenomegaly typical of chronic infection, and the parasite evades it by sequestering in deep vasculature—so splenectomy or asplenia markedly worsens malaria severity.
- `connects-to` → **[Burkitt Lymphoma](../burkitt-lymphoma/README.md)** — Endemic Burkitt lymphoma is a malaria-driven cancer: chronic Plasmodium falciparum infection causes intense B-cell proliferation and weakens control of co-infecting Epstein-Barr virus, together driving the MYC translocation behind the jaw tumors of African children.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Malaria causes severe anemia by several routes: rupture of infected red cells, splenic clearance of uninfected cells, and inflammatory suppression of erythropoiesis (an anemia-of-chronic-disease component) combine, making anemia a leading cause of malaria death in children.
- `connects-to` → **[Acute Respiratory Distress Syndrome](../../06-organ/ards/README.md)** — Severe falciparum malaria can cause ARDS: sequestration of infected red cells and intense inflammation injure the pulmonary capillaries, flooding alveoli with edema even after parasite clearance—acute respiratory distress is a feared complication of severe malaria.
- `connects-to` → **[Disseminated Intravascular Coagulation](../disseminated-intravascular-coagulation/README.md)** — Severe malaria can trigger disseminated intravascular coagulation: widespread endothelial activation and cytokine storm in falciparum infection consume clotting factors and platelets, causing bleeding—part of the multi-organ failure that makes severe malaria lethal.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Severe malaria injures the kidney: hemolysis and sequestration cause acute kidney injury and, classically, blackwater fever (massive hemoglobinuria), so renal failure marks severe falciparum malaria and worsens its high mortality.
- `connects-to` → **[Cytokine Storm](../cytokine-storm/README.md)** — Severe malaria is partly a cytokine storm: schizont rupture triggers a TNF-driven inflammatory surge causing fever, and excess cytokines contribute to cerebral malaria and organ failure—so the host inflammatory response, not just the parasite, drives lethal disease.
- `connects-to` → **[Dengue Fever](../dengue-fever/README.md)** — Malaria and dengue are the great overlapping tropical fevers: both cause fever and thrombocytopenia in the same regions, so a febrile traveler needs both excluded—malaria (a treatable parasite) must never be missed while dengue (a virus) is managed supportively.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — Malaria targets the placenta in pregnancy: infected red cells bind a unique placental receptor (CSA) and sequester there, causing maternal anemia, low birth weight, and stillbirth—so first pregnancies in endemic areas carry special risk, prompting preventive treatment.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Cerebral malaria is a disease of the endothelium: infected red cells express adhesion proteins that stick to blood-vessel linings, sequestering in the brain's microvessels, blocking flow and inflaming the barrier—causing the coma that makes falciparum malaria lethal.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Malaria immunity is hard-won and incomplete: repeated infection builds partial 'premunition' that lets endemic adults tolerate parasites, but it wanes without exposure—and this slow, leaky immunity is exactly why an effective malaria vaccine (RTS,S, R21) took so long.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — Malaria's silent first stage is in hepatocytes: injected sporozoites invade liver cells and multiply before the blood stage, and in P. vivax and ovale dormant hypnozoites hide there for months—causing relapses that need a separate drug (primaquine) to clear.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — Nitric oxide is double-edged in malaria: it helps kill parasites, but in cerebral malaria dysregulated NO and endothelial activation contribute to the coma and brain injury that make it the deadliest complication.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron and malaria are dangerously intertwined: the parasite needs iron to grow, so iron supplementation can worsen malaria in endemic areas—while repeated infection also causes anemia, complicating how iron deficiency is treated where malaria is common.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Severe malaria spills potassium from burst red cells: massive hemolysis and kidney injury raise blood potassium, and the released hemoglobin can darken the urine (blackwater fever)—dangerous electrolyte shifts in the sickest patients.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — The spleen's macrophages fight and are fooled by malaria: they engulf parasitized red cells and the dark hemozoin pigment, enlarging the spleen, yet the parasite's surface tricks sustain infection—and a ruptured malarial spleen is a feared emergency.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Severe malaria activates complement: C3 and the cascade fire on parasite and immune complexes, fueling the inflammation and red-cell destruction behind severe anemia and organ damage—part of the immune over-response that turns malaria lethal.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Malaria cripples the bone marrow: the parasite and its hemozoin pigment suppress red-cell production (dyserythropoiesis), so blunted marrow output compounds the destruction of infected cells to deepen malarial anemia.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — Severe malaria floods the blood with hydrogen ions: parasite and tissue starvation generate lactic acid, and the resulting metabolic acidosis (acidemia) is one of the strongest predictors of death in severe disease.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Thrombocytopenia is the rule in malaria: platelets are consumed and trapped in the spleen as the infection activates clotting, so a low platelet count is one of the most reliable clues that a fever is malaria.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Malaria is still diagnosed by light: Giemsa-stained thick and thin blood films under the microscope reveal the parasites inside red cells, letting the species be identified and the parasite load counted.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Severe malaria suffocates tissues: sequestered red cells block capillaries while profound anemia cuts oxygen delivery, driving the lactic acidosis and organ failure that mark the deadliest disease.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — The retina betrays cerebral malaria: malarial retinopathy—patchy whitening, vessel discoloration and hemorrhages—is a specific bedside sign that a comatose child's illness is truly malaria and not another cause.

[^who-malaria-report-2023]: World Health Organization. World Malaria Report 2023. WHO; 2023.
[^white-2014-malaria-lancet]: White NJ, Pukrittayakamee S, Hien TT, et al. Malaria. *Lancet.* 2014;383(9918):723-735. [doi:10.1016/S0140-6736(13)60024-0](https://doi.org/10.1016/S0140-6736(13)60024-0) · [PubMed 23953767](https://pubmed.ncbi.nlm.nih.gov/23953767/)
[^dondorp-2010-severe-malaria-lancet]: Dondorp AM, Fanello CI, Hendriksen IC, et al. Artesunate versus quinine in the treatment of severe falciparum malaria in African children (AQUAMAT). *Lancet.* 2010;376(9753):1647-1657. [doi:10.1016/S0140-6736(10)61924-1](https://doi.org/10.1016/S0140-6736(10)61924-1) · [PubMed 21062666](https://pubmed.ncbi.nlm.nih.gov/21062666/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
