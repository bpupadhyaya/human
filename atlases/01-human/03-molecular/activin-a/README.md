---
schema: human-scale-entry/v1
id: activin-a
name: Activin A
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "Activin A (INHBA homodimer, chr7p15.2) is a TGF-β superfamily member; ActRIIB/ALK4 → SMAD2/3 suppresses erythropoiesis and promotes PAH vascular remodeling; luspatercept (ActRIIB-Fc) treats MDS/beta-thalassemia; sotatercept reverses PAH (STELLAR trial 2024)."
aliases: ["activin A", "activin-A", "INHBA", "inhibin beta A", "activin AB", "erythroid maturation agent"]
cross_links:
  - target: 01-human/07-system/mds
    relation: connects-to
    note: "Activin A/B → ActRIIB on erythroid progenitors → SMAD2/3 → suppression of late erythroid maturation → ineffective erythropoiesis in MDS and beta-thalassemia; luspatercept (MEDALIST trial: 38% transfusion independence vs. 13% placebo) traps activin A/B to restore erythropoiesis."
  - target: 01-human/03-molecular/myostatin
    relation: connects-to
    note: "Activin A and myostatin are co-ligands of ActRIIB; bimagrumab (anti-ActRIIB) blocks both → reduces fat mass and increases lean mass; in cancer cachexia activin A drives muscle wasting via SMAD2/3 and MAFbx/MuRF1 — same atrophy pathway as myostatin."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Activin A → pulmonary VSMC ActRIIB/ALK4 → SMAD2/3 → excessive proliferation and vasoconstriction → PAH; sotatercept (FDA 2024) traps activin A/B → reverses pulmonary vascular remodeling; STELLAR trial: 34% 6MWD improvement vs. 21% placebo (p<0.001)."
sources:
  - id: hoeper-2023-sotatercept-stellar
    type: peer-reviewed
    cite: "Hoeper MM, Badesch DB, Ghofrani HA, et al. Phase 3 Trial of Sotatercept for Treatment of Pulmonary Arterial Hypertension. N Engl J Med. 2023;388(16):1478-1490."
    doi: "10.1056/NEJMoa2213558"
    pmid: "36877098"
    url: "https://doi.org/10.1056/NEJMoa2213558"
  - id: fenaux-2020-luspatercept-mds
    type: peer-reviewed
    cite: "Fenaux P, Platzbecker U, Mufti GJ, et al. Luspatercept in Patients with Lower-Risk Myelodysplastic Syndromes. N Engl J Med. 2020;382(2):140-151."
    doi: "10.1056/NEJMoa1908892"
    pmid: "31914241"
    url: "https://doi.org/10.1056/NEJMoa1908892"
---

# Activin A

## Overview

**Activin A** (INHBA/INHBA homodimer; gene *INHBA* — inhibin beta A subunit, chromosome 7p15.2) is a **TGF-β superfamily member** acting through **ActRIIB (ACVR2B) and ActRIIA (ACVR2A)** to activate **SMAD2/3 → SMAD4** signaling in a wide range of tissues. A key node in the biology of **erythropoiesis, reproductive hormone regulation, skeletal muscle homeostasis, and pulmonary vascular remodeling**, activin A became a major therapeutic target when ActRIIB-Fc fusion proteins — engineered "ligand traps" that sequester activin A and B, GDF11, and myostatin — demonstrated transformative efficacy in two unrelated disease areas: **ineffective erythropoiesis** (MDS, beta-thalassemia) and **pulmonary arterial hypertension (PAH)**.

The naming is complex: activin A is a homodimer of two INHBA chains; activin B is a homodimer of INHBB; activin AB is a heterodimer. All three activin forms share ActRIIB/ActRIIA binding and SMAD2/3 signaling. **Inhibins** (inhibin A = αβA; inhibin B = αβB) are structurally related but antagonize activin by competing for type II receptor binding without forming functional signaling complexes. **Follistatin** is the dominant endogenous activin antagonist — non-covalently traps activin (and myostatin, GDF11) with high affinity.

**Clinical breakthrough — dual ActRIIB trap strategy:**
- **Luspatercept (Reblozyl; ACE-536):** Modified ActRIIB-Fc with selective ligand trap profile (activin B > activin A, GDF11); approved for MDS-related anemia (2020, MEDALIST trial) and beta-thalassemia (2020, BELIEVE trial) and lower-risk MDS (2023)
- **Sotatercept (Winrevair; ACE-011):** Same scaffold, different modification creating broader trap (activin A = activin B); FDA-approved March 2024 for PAH — first entirely new mechanism in PAH since endothelin receptor antagonists in the late 1990s; reverses pulmonary vascular remodeling rather than just dilating vessels

## Structure

**Activin A biosynthesis and structure:**
Pre-pro-INHBA (426 aa) → signal peptide cleavage → pro-INHBA → furin-like proprotein convertase cleaves at RXXR motif → **mature INHBA C-terminal domain (116 aa, ~14 kDa monomer)** + N-terminal prodomain; two mature INHBA chains link via disulfide bond → **activin A homodimer (~28 kDa)**.

The C-terminal mature domain adopts the **cystine knot TGF-β fold** (three intramolecular + one intermolecular disulfide; "hand" topology shared with TGF-β, BMPs, GDF-8). The "wrist epitope" contacts ActRIIB ECD; the "knuckle epitope" contacts type I receptor (ALK4/ALK5).

**Receptor complex for activin A:**
- **ActRIIB (ACVR2B)** or **ActRIIA (ACVR2A):** High-affinity type II receptor binding (Kd ~1 nM); forms initial activin A/type II receptor complex; ActRIIB has higher affinity for activin A than ActRIIA
- Activin A/ActRIIB → recruits and transphosphorylates **ALK4 (ACVR1B)** type I receptor → ALK4 → **SMAD2/SMAD3 C-terminal Ser phosphorylation** → SMAD2/3 + SMAD4 co-SMAD heterotrimers → nuclear translocation → gene transcription (growth inhibition, differentiation programs, matrix genes)
- **Note on shared receptor:** ActRIIB is shared by activin A/B, myostatin (GDF-8), GDF11, GDF3, BMP9/10 (these last two bind ActRIIB but signal through BMP type I receptors ALK1/ALK2 → SMAD1/5/9 — completely different outcome)

**Endogenous antagonists:**
- **Follistatin (FST):** 35 kDa; binds activin A with Kd ~10 pM (extremely tight); wraps around activin homodimer → steric blockade of type II receptor binding; also neutralizes myostatin, GDF11; major pregnancy and wound healing factor; does NOT inhibit TGF-β or BMP7
- **FSTL3 (follistatin-like 3):** Similar to FST but circulates; neutralizes activin A and GDF11
- **Inhibin A (αβA)/Inhibin B (αβB):** Incomplete activin antagonist — binds type II receptor but cannot recruit type I receptor → partial competitive inhibition; level reflects ovarian function
- **GASP1/GASP2:** Bind and inhibit activin, myostatin, GDF11 in bone/muscle; less potent than follistatin

**Engineered activin traps (ActRIIB-Fc fusion proteins):**
Both luspatercept and sotatercept are constructed from the **extracellular domain of ActRIIB (aa 19-134)** fused to human IgG1 Fc — creating a decoy receptor that competes for activin A/B and GDF-8/11 binding; modifications in the ligand-binding domain determine selectivity:
- Luspatercept modification: selectively traps activin B > activin A, GDF11 >> myostatin
- Sotatercept modification: traps activin A ≈ activin B > GDF11 > myostatin

## Function

**Reproductive endocrinology (FSH regulation):**
- Activin A/B from ovarian granulosa cells → paracrine FSH support (pituitary) → sustained FSH during follicular phase; activin A also promotes follicular granulosa cell proliferation and estradiol production
- Inhibin A (luteal phase) and inhibin B (follicular phase) antagonize activin → suppress FSH; menopause: inhibin loss → FSH surge (FSH > 25 IU/L = menopausal transition)
- PCOS: activin/inhibin imbalance → disordered LH:FSH ratio → anovulation; activin is also elevated in PCOS ovarian stroma

**Ineffective erythropoiesis — ActRIIB mechanism:**
- In the bone marrow, **late erythroid progenitors (basophilic/polychromatic erythroblasts)** express ActRIIB at high density; activin B (and GDF11, activin A at high levels) → SMAD2/3 → transcriptional repression of erythroid differentiation genes (KLF1, GATA1 targets) → arrest in late-stage erythroblast maturation → ineffective erythropoiesis
- This is the mechanism of **ring-sideroblast MDS** (particularly MDS with SF3B1 mutation → aberrant splicing of mitochondrial iron transporters + activin B-driven maturation block) and **beta-thalassemia** (globin chain imbalance → early erythroblast apoptosis + late maturation block)
- Luspatercept (ACE-536) traps activin B/GDF11 → releases the SMAD2/3-driven erythroblast maturation block → accelerated terminal differentiation → increased mature RBC production [^fenaux-2020-luspatercept-mds]

**Pulmonary arterial hypertension — vascular remodeling:**
- PAH involves pathological **pulmonary arterial wall remodeling**: VSMC hypertrophy, endothelial dysfunction, adventitial thickening, plexiform lesions → progressive obliteration of pulmonary arterioles → rising PVR → right heart failure
- **Activin A/B are elevated** in PAH patient plasma and pulmonary vascular tissue; activin → pulmonary VSMC ActRIIB/ALK4 → SMAD2/3 → pro-proliferative and anti-apoptotic gene programs → vascular wall thickening
- **Mechanism (sotatercept):** ActRIIB-Fc traps activin A/B → restores SMAD1/5/9:SMAD2/3 balance in pulmonary vasculature → SMAD1/5/9-driven anti-proliferative effects become dominant → vascular remodeling reversal [^hoeper-2023-sotatercept-stellar]

**Skeletal muscle cachexia:**
- Cancer-associated cachexia: tumors secrete activin A (and B) at high levels → circulating activin A → skeletal muscle ActRIIB → SMAD2/3 → MAFbx/Atrogin-1 + MuRF1 upregulation → accelerated protein catabolism → muscle wasting exceeding that explained by myostatin alone
- Mechanistically similar to but independent from myostatin: same ActRIIB receptor, same SMAD2/3 signaling, same E3 ligase atrophy effectors; this explains why bimagrumab (which blocks ActRIIB shared by both activin A and myostatin) is more effective than selective anti-myostatin in cachexia models

## Mechanism

**Sotatercept in PAH [^hoeper-2023-sotatercept-stellar]:**
- **STELLAR Phase 3 trial (2023):** 163 PAH patients (WHO Group 1) receiving background PAH therapy (ERA/PDE5i/prostanoid); sotatercept 0.7 mg/kg SC Q3W vs. placebo; 24-week treatment
- **Primary endpoint — 6-minute walk distance (6MWD):** +40.8 m sotatercept vs. +9.0 m placebo (p<0.001); pre-specified multiplicity-controlled secondary endpoints also met (PVR, NT-proBNP, functional class, multi-component endpoint)
- Multicomponent endpoint (composite improvement in 6MWD + PVR + functional class/NT-proBNP): sotatercept 65% improved vs. 27% placebo (p<0.001)
- FDA-approved March 2024 (Winrevair); first approved therapy for PAH with an anti-remodeling mechanism (all prior PAH drugs are vasodilators: ERAs, PDE5i, sGC stimulators, prostacyclins)

**Luspatercept in MDS [^fenaux-2020-luspatercept-mds]:**
- **MEDALIST trial (2020):** 229 patients with low/int-1 MDS with ring sideroblasts (RS-MDS, predominantly SF3B1 mutated); luspatercept 1.0-1.75 mg/kg SC Q3W vs. placebo
- Primary endpoint — RBC transfusion independence ≥8 weeks during weeks 1-24: **38.2% (luspatercept) vs. 13.2% (placebo)** (p<0.001)
- Mechanism correlates: baseline serum GDF11 and activin B levels predicted response; SF3B1-mutated patients responded best (RS phenotype = strongest activin/GDF11-driven maturation block)
- Also approved for:
  - **Beta-thalassemia (BELIEVE trial):** 21% achieved ≥33% transfusion reduction at weeks 13-24 vs. 4.5% placebo
  - **Lower-risk MDS (EPO-refractory):** Luspatercept approved regardless of RS status (2023 COMMANDS trial vs. epoetin alfa: higher transfusion independence with luspatercept)

## Connections

Activin A/B → ActRIIB on erythroid progenitors → SMAD2/3 → suppression of late erythroid maturation → ineffective erythropoiesis in MDS and beta-thalassemia; luspatercept (MEDALIST trial: 38% transfusion independence vs. 13% placebo) traps activin A/B to restore erythropoiesis.

Activin A and myostatin are co-ligands of ActRIIB; bimagrumab (anti-ActRIIB) blocks both → reduces fat mass and increases lean mass; in cancer cachexia activin A drives muscle wasting via SMAD2/3 and MAFbx/MuRF1 — same atrophy pathway as myostatin.

Activin A → pulmonary VSMC ActRIIB/ALK4 → SMAD2/3 → excessive proliferation and vasoconstriction → PAH; sotatercept (FDA 2024) traps activin A/B → reverses pulmonary vascular remodeling; STELLAR trial: 34% 6MWD improvement vs. 21% placebo (p<0.001).

[^hoeper-2023-sotatercept-stellar]: Hoeper MM, Badesch DB, Ghofrani HA, et al. Phase 3 Trial of Sotatercept for Treatment of Pulmonary Arterial Hypertension. *N Engl J Med.* 2023;388(16):1478-1490. [doi:10.1056/NEJMoa2213558](https://doi.org/10.1056/NEJMoa2213558) · [PubMed 36877098](https://pubmed.ncbi.nlm.nih.gov/36877098/)
[^fenaux-2020-luspatercept-mds]: Fenaux P, Platzbecker U, Mufti GJ, et al. Luspatercept in Patients with Lower-Risk Myelodysplastic Syndromes. *N Engl J Med.* 2020;382(2):140-151. [doi:10.1056/NEJMoa1908892](https://doi.org/10.1056/NEJMoa1908892) · [PubMed 31914241](https://pubmed.ncbi.nlm.nih.gov/31914241/)
