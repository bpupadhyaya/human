---
schema: pathogen-entry/v1
id: trypanosoma-cruzi
name: Trypanosoma cruzi
atlas: 02-pathogen
scale: 04-parasites
status: draft
last_reviewed: 2026-06-05
summary: "Kinetoplastid; Chagas disease; triatomine (kissing bug) vector. Trypomastigote (blood) → amastigote (intracellular). Targets cardiomyocytes and gut neurons; chronic: dilated cardiomyopathy, megaesophagus, megacolon. ~6-7 million infected in Latin America."
aliases: ["T. cruzi", "Chagas disease", "American trypanosomiasis", "Chagas", "trypanosomiasis americana", "enfermedad de Chagas"]
sources:
  - id: mandell-principles
    type: textbook
    cite: "Bennett JE, Dolin R, Blaser MJ. Mandell, Douglas, and Bennett's Principles and Practice of Infectious Diseases. 9th ed. Elsevier; 2020."
    url: "https://www.elsevier.com/books/mandell-douglas-and-bennetts-principles-and-practice-of-infectious-diseases/bennett/978-0-323-48255-4"
    accessed: "2026-06-05"
  - id: murray-microbiology
    type: textbook
    cite: "Murray PR, Rosenthal KS, Pfaller MA. Medical Microbiology. 9th ed. Elsevier; 2021."
    url: "https://www.elsevier.com/books/medical-microbiology/murray/978-0-323-67378-4"
    accessed: "2026-06-05"
  - id: rassi-2010-chagas
    type: peer-reviewed
    cite: "Rassi A Jr, Rassi A, Marin-Neto JA. Chagas disease. Lancet. 2010;375(9723):1388-402."
    doi: "10.1016/S0140-6736(10)60061-X"
    pmid: "20399979"
    url: "https://doi.org/10.1016/S0140-6736(10)60061-X"
  - id: tyler-2001-tcruzi
    type: peer-reviewed
    cite: "Tyler KM, Engman DM. The life cycle of Trypanosoma cruzi revisited. Int J Parasitol. 2001;31(5-6):472-81."
    doi: "10.1016/s0020-7519(01)00153-9"
    pmid: "11334928"
    url: "https://doi.org/10.1016/s0020-7519(01)00153-9"
cross_links:
  - target: 01-human/04-cellular/cardiomyocyte
    relation: damages
    note: "Amastigote replication in cardiomyocytes causes direct cell death; chronic myocarditis from autoimmune cross-reactivity (parasite antigens mimicking cardiac myosin); dilated cardiomyopathy and fatal arrhythmias."
  - target: 01-human/07-system/cardiovascular-system
    relation: damages
    note: "Chronic Chagas cardiomyopathy: megacardia, apical aneurysm, complete heart block, sudden cardiac death; right bundle branch block pathognomonic; accounts for 10,000+ deaths/year in Latin America."
  - target: 01-human/07-system/nervous-system
    relation: damages
    note: "Amastigotes in myenteric plexus neurons cause progressive denervation of GI tract; leads to megaesophagus (achalasia-like dysphagia) and megacolon (severe constipation/obstruction); irreversible after neuronal death."
  - target: 01-human/04-cellular/macrophage
    relation: damages
    note: "Trypomastigotes invade macrophages; T. cruzi lipid-based GPI anchors activate TLR2/TLR4; amastigotes inhibit lysosomal killing by escaping phagolysosome into cytoplasm; IFN-gamma-mediated NO production critical for control."
---

# Trypanosoma cruzi

## Overview

***Trypanosoma cruzi*** is the causative agent of **Chagas disease** (American trypanosomiasis), discovered by Brazilian physician Carlos Chagas in 1909 in a single elegant investigation that identified the pathogen, its vector, its reservoir, and its clinical syndrome — one of the most complete single-investigator discoveries in the history of medicine.

Chagas disease is a major neglected tropical disease (NTD) affecting **6–7 million people**, predominantly in Latin America, with significant and growing burden in North America, Europe, and Australia due to migration of infected individuals. The disease kills an estimated **10,000 people per year**, primarily from cardiac complications — making it the leading cause of cardiac disease mortality in endemic Latin American countries [^rassi-2010-chagas].

What makes *T. cruzi* biologically and clinically distinctive is its unique dual existence:
- **Acute phase** (weeks to months): blood-stage trypomastigotes and intracellular amastigotes; most infections subclinical but potentially fatal acute myocarditis (especially in children and in congenital cases)
- **Chronic phase** (10–30 years later): silent chronic infection → in ~30–40% of infected individuals, progressive dilated cardiomyopathy (chagasic heart disease) and/or GI autonomic neuropathy (megaesophagus, megacolon) — the parasite's most devastating long-term sequelae

Treatment with **benznidazole** or **nifurtimox** is highly effective in the acute phase but substantially less effective in chronic disease — creating an urgent need for early diagnosis and treatment.

## Structure

**Life cycle stages and morphology:**

| Stage | Location | Size | Biology |
|:---|:---|:---|:---|
| **Epimastigote** | Triatomine bug midgut | 20–40 µm; kinetoplast anterior to nucleus | Replicating form in the insect; not directly infectious to mammals |
| **Metacyclic trypomastigote** | Triatomine bug hindgut/feces | 20 µm; kinetoplast posterior to nucleus | Non-replicating; deposited in insect feces on/near bite wound; infectious to mammals |
| **Bloodstream trypomastigote** | Mammalian blood | 20 µm curved/C-shape; kinetoplast posterior | Non-replicating; infects diverse nucleated cells; transferred back to triatomines during blood meal |
| **Amastigote** | Mammalian intracellular (cytoplasm) | 1.5–6.5 µm, round/oval; small kinetoplast; short internal flagellum | Replicating form; pseudocyst of amastigotes fills host cell before rupture |

**Key molecular virulence factors:**

- **Mucins (GPI-anchored surface glycoproteins):** Dense surface coat of mucin-like glycoproteins (TcMUC family) shields invariant surface antigens; also activates innate immune signalling (TLR2/TLR4 via GPI anchors containing unsaturated fatty acids)
- **trans-Sialidase (TcTS):** Major surface enzyme; transfers sialic acid from host glycoproteins to parasite mucins → sialylated mucins (a) protect from complement; (b) mediate invasion (binds host cell sialic acid-containing receptors); (c) shed TS desialylates host cell surfaces (CD43 shedding → lymphocyte suppression)
- **Cruzipain (CZP, GP57/51):** Major cysteine protease; processes parasite surface proteins; degrades host matrix proteins (fibronectin, laminin, collagen IV); cleaves kininogen → bradykinin release → vasodilation at inoculation site → enhanced parasite dissemination; immunodominant antigen (used in serology)
- **GP82/GP85:** Surface metacyclic stage glycoproteins mediating initial adhesion to host epithelial cells; trigger [Ca²⁺]i release in host cells via PKC → facilitates lysosome recruitment for invasion
- **MASP proteins (Mucin-Associated Surface Proteins):** Largest gene family in *T. cruzi* genome (~1,300 genes); expressed on trypomastigote surface; variable N-terminus, conserved signal peptide/GPI anchor; function partially redundant with mucins in surface coating and immune evasion

## Infection Mechanism

**Routes of transmission:**
1. **Vector-borne (primary, ~70% of cases):** Triatomine bug (*Triatoma infestans*, *Rhodnius prolixus*, *Panstrongylus megistus* — "kissing bugs," Reduviidae family) defecates metacyclic trypomastigotes at/near bite site during nocturnal blood meal; host scratches feces into bite wound or mucous membranes (conjunctiva → "Romaña's sign" — unilateral periorbital edema)
2. **Oral (increasing importance; outbreaks):** Ingestion of food/beverages contaminated with triatomine feces or crushed bugs (açaí juice, sugar cane juice outbreaks in Brazil); higher inoculum → higher acute mortality; severe myocarditis and higher acute fatality rate
3. **Congenital:** ~5% vertical transmission rate; occurs throughout pregnancy; severity variable; screening programs critical
4. **Blood transfusion/organ transplantation:** Historical major route in endemic countries; now controlled by mandatory blood bank screening in most endemic countries; emerging issue in non-endemic countries

**Step-by-step cellular invasion:**

**1. Contact and signal induction:**
- Metacyclic trypomastigotes contact host cell plasma membrane; GP82 on the parasite surface binds host cell surface molecules (gastric mucin, laminin receptor) → triggers intracellular Ca²⁺ transients in both parasite and host cell via IP3/DAG pathway
- Ca²⁺ signalling in host cell recruits lysosomes to the site of parasite attachment — a mechanism uniquely exploited by *T. cruzi* (contrast with *T. gondii* which excludes lysosomes from its vacuole)

**2. Lysosome-dependent invasion:**
- Recruited lysosomes fuse with plasma membrane at the contact site, providing membrane for a novel vacuole — the **parasitophorous vacuole** (PV) initially derived from lysosomal membrane
- Alternatively, trypanosome-triggered plasma membrane invagination forms a tight-fitting vacuole that acquires lysosomal markers (LAMP-1, LAMP-2) by fusion

**3. Escape from the PV:**
- Unlike *T. gondii*, *T. cruzi* does NOT reside long-term in the vacuole
- **Tc-Tox (hemolysin):** Pore-forming toxin in the PV membrane, activated at acidic lysosomal pH (~5.5); disrupts PV membrane
- **Cruzipain:** Active at low pH; degrades PV membrane proteins; acts synergistically with Tc-Tox
- Within 24–72 hours: trypomastigotes differentiate to amastigotes; amastigotes (or trypomastigotes) lyse the PV and escape into the **host cell cytoplasm** — where replication occurs freely (no vacuole)

**4. Intracellular replication:**
- Amastigotes replicate by binary fission in the cytoplasm every ~12–24 hours
- Host cell fills with a **"pseudocyst"** (dense mass of amastigotes in cytoplasm; no enclosing wall)
- After 4–5 days: ~500 amastigotes/cell; amastigotes differentiate back to trypomastigotes; host cell lyses; bloodstream trypomastigotes released; infect adjacent cells or disseminate hematogenously

**5. Organ tropism:**
- *T. cruzi* can invade virtually any nucleated mammalian cell: macrophages, smooth and skeletal myocytes, cardiac myocytes, hepatocytes, adipocytes, endothelial cells, neurons, CNS glial cells
- **Preferential tropism:** Cardiomyocytes and autonomic neurons of the myenteric plexus (Auerbach's plexus) in the GI tract — the basis of chronic Chagas pathology
- Muscle tropism: trypomastigote surface proteins (GP83, MBP-related proteins) bind muscle-specific receptors; Ca²⁺ signalling in cardiomyocytes is rapidly disturbed

## Host Interactions

**Cells and organs targeted:**

| Cell/Organ | Interaction | Consequence |
|:---|:---|:---|
| Macrophages | Invaded; evades lysosomal killing by phagosome escape | Dissemination vehicle; IFN-γ/NO-mediated killing is principal defence |
| Cardiomyocytes | Invaded → amastigote pseudocysts → cell lysis | Direct myocyte death; progressive cardiomyopathy |
| Myenteric plexus neurons | Invaded → neuronal death | Denervation → GI motility loss → megaesophagus/megacolon |
| Hepatocytes | Invaded during acute phase | Hepatomegaly; liver function impairment |
| CNS neurons | Invaded (especially in congenital and immunosuppressed) | Chagasic meningoencephalitis |

**Immune evasion mechanisms:**

- **Phagolysosome escape:** Tc-Tox and cruzipain mediate escape into the cytoplasm; free in cytoplasm, *T. cruzi* amastigotes are protected from lysosomal enzymes
- **GPI anchor-mediated immune activation (double-edged):** *T. cruzi* GPI anchors (containing unsaturated C18:1 fatty acids) potently activate TLR2/TLR4 → IL-12, TNF-α production; while this alerts the immune system, it also contributes to pathological inflammation; *T. cruzi* may "exploit" the inflammatory response to enhance its own dissemination
- **Trans-sialidase-mediated lymphocyte suppression:** TcTS shed by trypomastigotes cleaves CD43 and CD45 from lymphocyte surfaces → T cell apoptosis induction; reduces lymphocyte responses
- **Antigen mimicry / autoimmunity (chronic phase):** Parasite-derived antigens (B13 antigen, Fl-160 neuronal epitope, cardiac myosin B-chain peptides) share epitopes with host cardiac and neuronal proteins; chronic cardiac inflammation includes autoimmune myocarditis even in areas with very low parasitaemia — suggesting self-sustaining autoimmune contribution to chronic Chagas
- **IL-10 induction:** Chronic infection induces regulatory T cells (Tregs) and IL-10-producing macrophages → dampens effector immunity → allows parasite persistence at low levels

**Distinction from *T. brucei*:**

| Feature | T. cruzi | T. brucei |
|:---|:---|:---|
| Intracellular | Yes (obligate during amastigote phase) | No (extracellular throughout) |
| Target cells | Diverse nucleated cells | Blood, lymph, CSF |
| Antigenic variation | No VSG equivalent | VSG coat (primary evasion) |
| Vector | Triatomine bug | Tsetse fly |
| Major disease | Chagas (cardiac/GI) | Sleeping sickness (CNS) |

## Connections

- **Damages** → [Cardiomyocyte](../../../01-human/04-cellular/cardiomyocyte/README.md): Amastigote replication in cardiomyocytes causes direct cell death; chronic myocarditis from autoimmune cross-reactivity (parasite antigens mimicking cardiac myosin); dilated cardiomyopathy and fatal arrhythmias.

- **Damages** → [Cardiovascular System](../../../01-human/07-system/cardiovascular-system/README.md): Chronic Chagas cardiomyopathy: megacardia, apical aneurysm, complete heart block, sudden cardiac death; right bundle branch block pathognomonic; accounts for 10,000+ deaths/year in Latin America.

- **Damages** → [Nervous System](../../../01-human/07-system/nervous-system/README.md): Amastigotes in myenteric plexus neurons cause progressive denervation of GI tract; leads to megaesophagus (achalasia-like dysphagia) and megacolon (severe constipation/obstruction); irreversible after neuronal death.

- **Damages** → [Macrophage](../../../01-human/04-cellular/macrophage/README.md): Trypomastigotes invade macrophages; T. cruzi lipid-based GPI anchors activate TLR2/TLR4; amastigotes inhibit lysosomal killing by escaping phagolysosome into cytoplasm; IFN-gamma-mediated NO production critical for control.

## Pathology

**Acute Chagas disease:**

- Incubation: 1–2 weeks (vector route); 2–4 weeks (oral route)
- 90–95% of acute infections in adults are **asymptomatic or oligosymptomatic**: low-grade fever, malaise, lymphadenopathy, hepatosplenomegaly, facial oedema
- **Romaña's sign:** Unilateral painless periorbital oedema (eyelid swelling) from conjunctival inoculation of feces — pathognomonic but present in <50% of vector-transmitted cases
- **Chagoma:** Local indurated skin lesion at the bite site (analogous to trypanosomal chancre)
- Severe acute Chagas: acute myocarditis (chest pain, pericardial effusion, arrhythmias, heart failure) in ~1–5% of cases; **acute chagasic meningoencephalitis** (more common in children <2 years, or immunosuppressed); oral route associated with worse acute outcomes
- Acute fatality rate: 5–10% in children with acute myocarditis if untreated; very rare in asymptomatic adults

**Chronic Chagas disease:**

After the acute phase, 60–70% of infected individuals enter **indeterminate form** (asymptomatic, normal ECG and echocardiogram; may persist lifelong). Over 10–30 years, 30–40% develop chronic organ complications:

**Chronic Chagas cardiomyopathy (chagasic heart disease):**
- Most common and most lethal complication; ~20–30% of all infected individuals
- **Pathognomonic ECG finding:** Right bundle branch block (RBBB) ± left anterior fascicular block; second-degree/complete AV block
- Progressive dilated cardiomyopathy: biventricular dilation, wall motion abnormalities, apical aneurysm (characteristic of Chagas; 50% of Chagas cardiomyopathy patients)
- Sudden cardiac death (from ventricular tachycardia/fibrillation): major cause of death in young Chagas patients; ICD implantation indicated
- Thromboembolic stroke: from apical thrombus or atrial fibrillation
- Heart failure with reduced ejection fraction (HFrEF): end-stage Chagas; poor prognosis; cardiac transplantation can be performed (immunosuppression may reactivate infection — requires prophylaxis)

**Chagasic digestive disease:**
- **Megaesophagus:** Denervation of myenteric plexus → impaired lower oesophageal sphincter relaxation → achalasia-like syndrome; degrees I–IV (degree IV = oesophagus >7 cm diameter, sigmoid deformity); progressive dysphagia → aspiration pneumonia risk
- **Megacolon:** Denervation of sigmoid colon myenteric plexus → colonic dilatation, obstruction; sigmoid volvulus (life-threatening); severe constipation, faecaloma

**Epidemiology:**

| Parameter | Value |
|:---|:---|
| Global infected individuals | ~6–7 million (mainly Latin America; ~300,000 in USA) |
| Annual deaths | ~10,000–12,000 (predominantly cardiac) |
| Countries with endemic vector transmission | 21 Latin American countries |
| Annual new vector-borne infections | ~30,000 (declining with vector control) |
| Congenital Chagas (Latin America) | ~8,000–15,000 new cases/year |
| Risk of progression to cardiomyopathy | ~20–30% of infected individuals |

**Diagnosis:**

| Test | Phase | Notes |
|:---|:---|:---|
| Blood microscopy (thin/thick smear, microhaematocrit, Strout concentration) | Acute (high parasitaemia) | Sensitivity ~80–90% in acute; <30% in chronic; directly visualises trypomastigotes |
| PCR (T. cruzi–specific DNA) | Acute and chronic | High sensitivity in acute (~100%); ~50–80% in chronic (low, intermittent parasitaemia); used for congenital, treatment monitoring, reactivation |
| Serology (2 serological tests required; EIA + RIPA or IFAT) | Chronic/indeterminate | Two assays with different formats required for chronic diagnosis (regulatory requirement in most countries); high sensitivity and specificity together |
| Xenodiagnosis | Chronic (research/difficult cases) | Feeding laboratory-reared triatomines on patient blood → examining bug feces; labour-intensive; ~50% sensitivity |
| ECG + echocardiography | Staging chronic cardiac disease | Mandatory for all chronically infected individuals |

**Treatment:**

| Drug | Dose/Route | Efficacy | Notes |
|:---|:---|:---|:---|
| Benznidazole | 5–7 mg/kg/day orally × 60 days (adults); 5–10 mg/kg/day × 60 days (children) | ~80–90% in acute; 20–40% in chronic; ~60% in congenital | First-line; GI intolerance, dermatitis, peripheral neuropathy (dose-dependent); drug of choice in Latin America |
| Nifurtimox | 8–10 mg/kg/day orally × 60–90 days (adults); 15–20 mg/kg/day (children) | Similar to benznidazole | Second-line; GI side effects, neurological (insomnia, tremors); more complex dosing |
| Symptomatic cardiac care | Per HFrEF/arrhythmia guidelines | Chronic indeterminate | BENEFIT trial (2015) showed benznidazole did not prevent cardiac outcomes in established chronic stage; antiarrhythmics, ICD, heart transplant as indicated |

[^rassi-2010-chagas]: Rassi A Jr, Rassi A, Marin-Neto JA. Chagas disease. Lancet. 2010;375(9723):1388–402.
[^tyler-2001-tcruzi]: Tyler KM, Engman DM. The life cycle of Trypanosoma cruzi revisited. Int J Parasitol. 2001;31(5–6):472–81.
[^mandell-principles]: Bennett JE, Dolin R, Blaser MJ. Mandell, Douglas, and Bennett's Principles and Practice of Infectious Diseases. 9th ed. Elsevier; 2020.
[^murray-microbiology]: Murray PR, Rosenthal KS, Pfaller MA. Medical Microbiology. 9th ed. Elsevier; 2021.
