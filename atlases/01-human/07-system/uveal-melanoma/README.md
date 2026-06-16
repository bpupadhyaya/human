---
schema: human-scale-entry/v1
id: uveal-melanoma
name: Uveal Melanoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Uveal melanoma is the most common primary intraocular malignancy; GNAQ/GNA11 ~85%, BAP1 ~45%, SF3B1 R625 ~15-20%, EIF1AX ~15%; Class 2 (BAP1 loss) has 25-35% 5-year metastasis-free survival; tebentafusp (gp100×CD3) is FDA-approved for HLA-A*02:01+ metastatic disease."
aliases: ["uveal melanoma", "choroidal melanoma", "iris melanoma", "ciliary body melanoma", "intraocular melanoma", "ocular melanoma", "GNAQ melanoma"]
sources:
  - id: nathan-2021-tebentafusp
    type: peer-reviewed
    cite: "Nathan P, Hassel JC, Rutkowski P, et al. Overall survival benefit with tebentafusp in metastatic uveal melanoma. N Engl J Med. 2021;385(13):1196-1206."
    doi: "10.1056/NEJMoa2103485"
    pmid: "34551229"
    url: "https://doi.org/10.1056/NEJMoa2103485"
  - id: harbour-2010-bap1-uveal
    type: peer-reviewed
    cite: "Harbour JW, Onken MD, Roberson ED, et al. Frequent mutation of BAP1 in metastasizing uveal melanomas. Science. 2010;330(6009):1410-1413."
    doi: "10.1126/science.1194472"
    pmid: "21051595"
    url: "https://doi.org/10.1126/science.1194472"
cross_links:
  - target: 01-human/03-molecular/sf3b1
    relation: connects-to
    note: "SF3B1 R625C/H occurs in ~15-20% uveal melanoma → cryptic 3' SS activation → Class 1B (intermediate prognosis, late relapses); SF3B1-mutant uveal melanoma has a distinct transcriptome from BAP1-loss Class 2; H3B-8800 may exploit this vulnerability."
  - target: 01-human/03-molecular/bap1
    relation: connects-to
    note: "BAP1 biallelic loss → Class 2 uveal melanoma (~45%; high metastatic risk, early liver relapse); BAP1 IHC nuclear loss is the primary prognostic marker; BAP1-TPDS germline → uveal melanoma lifetime risk ~30-45%; EZH2 inhibition studied in BAP1-null disease."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN loss occurs in ~15-20% of metastatic uveal melanoma; PI3K-AKT-mTOR activation drives progression; PI3K/mTOR + MEK inhibitor combinations overcome GNAQ-driven resistance in preclinical uveal melanoma models; everolimus studied in metastatic disease."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "PD-1/PD-L1 checkpoint inhibitors have very low activity in uveal melanoma (ORR <5%) due to low tumor mutational burden and immunosuppressive tumor microenvironment; tebentafusp bypasses checkpoint resistance by directly recruiting T cells via gp100-TCR×CD3 bispecific mechanism."
  - target: 01-human/07-system/melanoma
    relation: connects-to
    note: "Uveal melanoma is biologically distinct from cutaneous melanoma: GNAQ/GNA11 (not BRAF V600E) → MEK inhibitors only partial activity; very low TMB vs UV-mutational burden; ICB ORR <5% in uveal vs 30-60% in cutaneous; liver-dominant metastasis vs lung/brain tropism."
  - target: 01-human/03-molecular/yap1
    relation: connects-to
    note: "GNAQ/GNA11 → PLCβ → PKC → Rho → YAP/TAZ nuclear entry (Hippo-independent); YAP/TAZ drive CTGF, CYR61, BIRC5 → uveal melanoma proliferation and survival; verteporfin (YAP inhibitor) active in preclinical uveal models; YAP-TEAD inhibitors (IAG933, VT3989) in Phase 1/2 trials."
  - target: 01-human/03-molecular/braf
    relation: connects-to
    note: "BRAF V600E absent in uveal melanoma (0%); GNAQ/GNA11 → PLCβ/PKC → MEK (RAS-independent) → BRAF inhibitors ineffective; MEK inhibitors (selumetinib): ORR ~15% (SUMIT trial) but no OS benefit; MEK + PKC combinations overcome adaptive resistance in preclinical uveal melanoma models."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Uveal melanoma is the commonest primary intraocular cancer in adults, from melanocytes of the uveal tract — choroid (~90%), ciliary body, or iris; it presents with painless vision change or floaters, and globe-sparing brachytherapy or proton therapy has replaced most enucleation."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver is uveal melanoma's near-exclusive metastatic target: ~90% of metastases home there (the eye lacks lymphatics), often years after the eye is treated — so lifelong liver surveillance is essential, and liver-directed therapy plus tebentafusp are mainstays."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Uveal melanoma resists checkpoint inhibitors (ORR <5%, low mutational burden), so it engages cytotoxic T cells differently: tebentafusp, a gp100-HLA × CD3 bispecific, tethers CD8+ T cells to HLA-A*02:01 tumor cells — the first drug to improve survival in metastatic disease."
  - target: 01-human/07-system/mesothelioma
    relation: connects-to
    note: "Uveal melanoma and mesothelioma both define the BAP1 tumor predisposition syndrome: germline BAP1 loss raises risk of both, plus renal cell carcinoma and skin tumors, and BAP1 loss in a uveal melanoma marks the high-risk class with the worst metastatic prognosis."
  - target: 01-human/07-system/neurofibromatosis-type-2
    relation: connects-to
    note: "Uveal melanoma and NF2 converge on the Hippo pathway: NF2's Merlin restrains YAP, while uveal melanoma's GNAQ/GNA11 mutations activate YAP through Hippo—so both illustrate how unleashed YAP/TEAD drives growth, here in the pigmented cells of the eye."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Radiotherapy is the eye-sparing mainstay for uveal melanoma: plaque brachytherapy and proton or photon beams deliver tumoricidal radiation to the choroidal tumor while preserving the globe—an alternative to enucleation, though metastatic risk depends on genetics."
  - target: 01-human/07-system/retinoblastoma
    relation: connects-to
    note: "Uveal melanoma and retinoblastoma are the two principal intraocular malignancies: retinoblastoma is a childhood RB1-driven retinal tumor, while uveal melanoma is an adult melanocytic tumor of the choroid driven by GNAQ/GNA11 and BAP1—both threaten the eye and vision."
  - target: 01-human/07-system/cholangiocarcinoma
    relation: connects-to
    note: "Uveal melanoma and cholangiocarcinoma both belong to the BAP1 syndrome: germline BAP1 loss raises risk of both, and in uveal melanoma somatic BAP1 loss marks the liver-metastasizing tumors—linking an eye cancer to a bile-duct cancer through one chromatin gene."
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "Uveal melanoma and clear-cell renal cell carcinoma are joined by the BAP1 syndrome: BAP1 loss drives aggressive forms of both, so germline-mutation families are surveilled for eye, kidney, mesothelioma and skin tumors—BAP1 a shared deubiquitinase tumor suppressor."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "VEGF-driven angiogenesis and a leaky vasculature mark uveal melanoma: the tumor secretes VEGF to vascularize the eye and prepare its spread, high levels predict metastasis, and anti-VEGF agents are explored alongside the liver-directed therapy this cancer needs."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Uveal melanoma is immunologically cold yet newly targetable: it carries few mutations and sits in the immune-privileged eye, so checkpoint inhibitors disappoint—but tebentafusp, a gp100-directed bispecific that redirects T cells, is the first agent to improve survival."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Natural killer cells shape uveal melanoma's spread to the liver: circulating tumor cells that downregulate MHC become NK targets, so the balance of NK surveillance versus escape influences whether liver micrometastases grow—central to this cancer's lethal course."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Uveal melanoma is notorious for vasculogenic mimicry: aggressive tumor cells form PAS-positive vascular loops that mimic endothelial channels, supplying blood without true vessels—a pattern that marks poor prognosis and blunts conventional anti-angiogenic therapy."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Uveal melanoma's lethal liver tropism depends on stroma: hepatic stellate cells and fibroblasts build the fibrotic niche that dormant tumor cells colonize, so the liver microenvironment, not just tumor genetics, governs when micrometastases awaken and grow."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "The eye's immune privilege shields uveal melanoma: a TGF-β-rich anterior chamber suppresses helper T-cell responses (ACAID), so tumors grow unchecked locally—part of why this cancer is immunologically cold and slow to trigger systemic immunity."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Uveal melanoma is driven through ERK by Gq signaling: activating GNAQ/GNA11 mutations fire PLC-PKC to switch on the MAPK/ERK cascade—unlike cutaneous melanoma's BRAF route—so MEK/ERK-pathway inhibition has been the focus of targeted trials."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Tumor-associated macrophages mark high-risk uveal melanoma: paradoxically, a dense macrophage infiltrate (with monosomy 3 and BAP1 loss) signals worse prognosis and higher metastatic risk rather than protective immunity."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Uveal melanoma differs from skin melanoma at the telomere: it lacks the UV-signature TERT promoter mutations that drive cutaneous melanoma, reflecting its distinct, non-sun-related mutational origin (GNAQ/GNA11, BAP1) and biology."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Uveal melanoma's driver mutations signal through calcium: GNAQ/GNA11 lock the Gq protein on, firing phospholipase C to release calcium that activates PKC and MAPK—the core engine of this eye cancer, distinct from cutaneous melanoma's BRAF."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Uveal melanoma hides in the eye's immune privilege behind regulatory T cells: a Treg-rich, cold microenvironment makes it resist the checkpoint drugs that work in skin melanoma—why the T-cell engager tebentafusp was needed instead."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Uveal melanoma leans on PI3K-AKT through PTEN loss: alongside its Gq-MAPK driver, losing PTEN switches on AKT survival signaling, so combining MAPK and PI3K/AKT blockade is explored against this treatment-resistant cancer."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Hypoxia drives uveal melanoma's aggressiveness: low oxygen in the eye tumor stabilizes HIF and pushes invasion and the metabolic shift that helps it seed the liver, the near-universal site of its lethal spread."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Beyond its near-exclusive liver spread, uveal melanoma can reach the lungs: hematogenous metastasis occasionally seeds pulmonary and other sites, so surveillance looks past the liver in advanced disease."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells underpin the new immunotherapy for uveal melanoma: this normally immune-cold tumor is now attacked with tebentafusp, which redirects T cells to a melanocyte antigen—an approach that leans on antigen presentation."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Uveal melanoma's defining pigment is melanin, built by the copper-dependent enzyme tyrosinase: this trace-metal chemistry marks the tumor's melanocytic origin and supplies the melanoma antigens that tebentafusp exploits."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Though it arises in the eye and is biologically distinct from skin melanoma, uveal melanoma can metastasize to skin and subcutaneous tissue: an unusual cutaneous site of spread beyond its dominant route to the liver."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Uveal melanoma rarely reaches the brain: while the liver dominates its metastatic pattern, late hematogenous spread can seed the central nervous system, a hard-to-treat site that worsens prognosis in advanced disease."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy proves the eye tumor is melanocytic: even when pigment is scant, the beam reveals melanosomes and striated premelanosomes — the same pigment-making organelles found in skin melanoma — settling the cell of origin."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Uveal melanoma can only spread through blood: the eye has no lymphatics, so tumor cells must enter the bloodstream, where they cloak themselves in platelets to survive the journey and lodge in the liver."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Beyond the liver, uveal melanoma can seed the skeleton: widespread hematogenous disease reaches bone and its marrow, a late metastatic site that adds to the burden once the cancer has escaped the eye."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "The growing tumor blinds by lifting the retina: a choroidal melanoma bulges beneath and detaches the retina, starving its photoreceptor neurons and causing the flashes, floaters, and field loss that often bring the patient in."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Uveal melanoma builds its own false vessels: aggressive tumors weave PAS-positive collagen loops and networks (vasculogenic mimicry), and these closed loops are a histologic marker of the worst-prognosis tumors."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "The blood's inflammatory balance forecasts the course: a high neutrophil-to-lymphocyte ratio tracks with worse survival in uveal melanoma, and tumor-associated neutrophils help build the niche its liver metastases settle into."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibody-like therapy finally moved the needle: tebentafusp, a bispecific gp100-CD3 engager, is the first agent to extend survival in metastatic uveal melanoma, while HMB-45 and Melan-A stains and loss of BAP1 confirm the tumor and predict spread."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "Uveal melanoma is uniquely liver-hungry: over 90% of metastases home to the liver, the tumor cells seeding among the hepatocytes, which is why surveillance and liver-directed therapy dominate management of advanced disease."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Advanced disease shows in the red cells: extensive hepatic metastatic burden and its treatment depress erythrocyte production into an anemia, while rising liver enzymes and falling counts together signal progression."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Protons spare the eye: proton-beam radiotherapy and plaque brachytherapy deliver a sharp, contained dose to the ocular tumor while sparing the optic nerve and retina, letting many patients keep the eye instead of losing it to enucleation."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Uveal melanoma can run in families: germline BAP1 mutations transmit a tumor-predisposition syndrome — uveal melanoma with mesothelioma, kidney and skin cancers — so a diagnosis can prompt genetic testing and counseling of relatives."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Hypoxia shapes its spread to the liver: HIF signaling and the angiogenesis it drives help uveal melanoma colonize the liver, its near-exclusive metastatic site, a hypoxic-niche dependence studied as a therapeutic angle."
  - target: 01-human/03-molecular/ctla-4
    relation: connects-to
    note: "Checkpoint drugs barely dent it: unlike cutaneous melanoma, uveal melanoma's low mutation load makes anti-CTLA-4 and anti-PD-1 largely ineffective, which is why the T-cell-redirecting drug tebentafusp, not classic checkpoint blockade, became its breakthrough therapy."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "The mutant G-protein feeds growth hubs: GNAQ/GNA11 signaling activates PKC-MAPK and the PI3K-AKT-mTOR axis, so mTOR sits among the downstream nodes targeted to slow a tumor lacking the BRAF mutations that drive skin melanoma."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Its immune infiltrate predicts danger: tumor-infiltrating macrophages and mast cells mark the inflammatory, monosomy-3 uveal melanomas with the worst prognosis, so the immune microenvironment is read as a marker of metastatic risk."
---

# Uveal Melanoma

## Overview

**Uveal melanoma** is the most common primary **intraocular malignancy** in adults, arising from melanocytes of the uveal tract (choroid ~90%, ciliary body ~7%, iris ~3%). Despite its rarity (~5 cases/100,000/year), uveal melanoma carries the worst prognosis among ocular cancers and is biologically distinct from cutaneous melanoma — driven by **GNAQ/GNA11 Gαq-family mutations** (not BRAF V600E), with a profoundly **immunologically cold** tumor microenvironment and near-universal liver tropism for metastases. The landmark molecular classification divides uveal melanoma into four classes based on **BAP1, SF3B1, and EIF1AX** mutation status, each with distinct metastatic risk [^harbour-2010-bap1-uveal]. **Tebentafusp** (ImmTAC bispecific redirecting T cells to gp100-expressing cells) became the first agent to demonstrate OS benefit in metastatic uveal melanoma in the randomized Phase 3 IMCgp100-202 trial (FDA approved January 2022), a landmark achievement given the total failure of checkpoint inhibitors in this disease [^nathan-2021-tebentafusp].

**Epidemiology:**
- Incidence: ~6-7/million/year USA; ~7,000 cases/year globally
- Median age: ~60 years; slight male predominance (M:F ~1.3:1)
- Risk factors: fair skin, light-colored iris, UV light exposure (iris melanoma), BAP1-TPDS germline syndrome, large ocular nevi
- Race: predominantly Caucasians; rare in African Americans (~6-fold lower risk)
- ~50% develop metastatic disease within 15 years; liver is the dominant metastatic site (~90%)

## Structure

### Molecular subtypes (WHO/TCGA classification)

**Class 1A (~25-30%) — EIF1AX mutation:**
- EIF1AX (eukaryotic initiation factor 1A, X-linked): mutations in intron 5-6 splice site or exon 1/2 → aberrant translation initiation; functionally alters protein synthesis
- 5-year metastasis-free survival: ~95-100%; extremely favorable; late relapses rare
- BAP1 and SF3B1 intact; chromosome 3 disomy; 6p gain often present
- Usually requires no systemic surveillance after local treatment; ophthalmologic follow-up

**Class 1B (~20-25%) — SF3B1 mutation (R625C/H/S):**
- SF3B1 R625 in HEAT repeat 12 → cryptic 3' splice site activation (same mechanism as K700E in MDS)
- 5-year metastasis-free survival: ~80-85%; late relapses documented 10-20 years post-diagnosis
- Chromosome 6p gain, 8q gain patterns; BAP1 intact
- Requires prolonged surveillance (annual liver MRI for ≥15 years)

**Class 2 (~40-45%) — BAP1 loss:**
- BAP1 biallelic loss (somatic mutation + LOH at chromosome 3): ~45% of all uveal melanoma; nearly all Class 2 tumors
- 5-year metastasis-free survival: ~25-35%; median time to metastasis ~2-3 years
- Early liver metastases; poor prognosis
- Monosomy 3 (chromosome 3 loss of heterozygosity) is the cytogenetic hallmark
- BAP1 IHC (nuclear loss in >90% of tumor cells): primary clinical prognostic test

**Class overlap:** A minority of tumors harbor two driver mutations or don't fit neatly into one class; EIF1AX+SF3B1 co-mutations have been reported rarely.

### Oncogenic drivers

**GNAQ/GNA11 (Gαq/Gα11 mutations, ~85% combined):**
- GNAQ R183Q (codon 183, GTP-to-GDP exchange) or Q209L/P (effector binding domain): ~45%
- GNA11 Q209L: ~40%
- Both Q209 mutations: equivalent functional outcome — constitutive GTP-bound active Gαq/Gα11
- **Downstream:** PLCβ → IP₃ → Ca²⁺ + DAG → PKC activation → MEK/ERK (MAPK) + YAP/TAZ (Hippo pathway) constitutive activation
- **NOT RAS-BRAF-MEK:** Unlike cutaneous melanoma; RAS not required; BRAF V600E absent
- **Therapeutic implications:** MEK inhibitors (selumetinib, trametinib) have activity (ORR ~15-20%) but limited duration; PKC inhibitors (sotrastaurin) studied; YAP/TAZ inhibitors preclinical

**CYSLTR2 and PLCB4 (rare alternative drivers, ~3% each):**
- CYSLTR2 L129Q (cysteinyl leukotriene receptor 2) → constitutive Gαq activation without GNAQ/GNA11 mutation
- PLCB4 D630N → downstream PLCβ constitutive activation

**Secondary somatic events (metastatic progression):**
- Monosomy 3 (~50% of all uveal melanoma): loss of BAP1 (chromosome 3p) is the key event; non-random
- 8q gain (MYC amplification): ~50-60%; correlates with metastatic risk
- 6p gain: ~40%; associated with Class 1B
- MDM2 amplification: ~20%; p53 pathway inhibition

## Function

### Normal uveal melanocyte biology

Uveal melanocytes are neural crest-derived, residing in the uveal stroma and maintaining retinal pigment epithelium-independent pigmentation. They do not cycle under normal conditions (post-mitotic). GNAQ/GNA11 mutations in uveal melanocytes → constitutive MAPK + PKC-β signaling → cell cycle re-entry → proliferation while retaining melanocyte identity (S100, HMB-45, gp100/PMEL17 expression). gp100 (PMEL17, a premelanosomal protein responsible for melanin granule structure) is ubiquitously and stably expressed in uveal melanoma → the basis for tebentafusp's TCR targeting.

### Uveal melanoma vs. cutaneous melanoma differences

| Feature | Uveal Melanoma | Cutaneous Melanoma |
|---------|---------------|-------------------|
| Primary driver | GNAQ/GNA11 (~85%) | BRAF V600E (~40-50%) |
| TMB | Very low (<1 mut/Mb) | High (10-50 mut/Mb) |
| PD-L1 | Low/absent | Variable |
| ICI response | <5% ORR | 30-60% ORR |
| Metastatic site | Liver (~90%) | Lung, brain, liver |
| Liver microenvironment | Immunosuppressive | Less suppressive |
| UV mutation signature | Absent | Present (C>T transitions) |

## Pathology

### Local tumor characteristics

**Primary tumor staging (AJCC 8th edition):**
- T1: Tumor ≤12 mm largest basal diameter; ≤3 mm height → T1a (no ciliary body, no extraocular ext.), T1b-c (ciliary body involvement ± extraocular)
- T2: 12.1-18 mm and/or 3.1-6 mm height
- T3: >18 mm and/or >6 mm height
- T4: With extraocular extension (T4a: ≤5 mm, T4b: >5 mm)

**Histological types:**
- Spindle cell (most favorable): uniform spindle-shaped cells; rare mitoses
- Epithelioid (most aggressive): large polygonal cells; prominent nucleoli; frequent mitoses
- Mixed: mixed spindle and epithelioid (most common)

**Prognostic biomarkers:**
- BAP1 IHC (nuclear loss): ~45% of cases; highest-risk marker; clinical standard
- Monosomy 3 FISH: equivalent to BAP1 loss; performed on tumor biopsy
- Gene expression profiling (GEP, DecisionDx-UM): 15-gene assay; Class 1A/1B/2 classification; validated in multiple cohorts
- SF3B1 molecular testing: next-gen sequencing; identifies Class 1B for late-relapse surveillance

### Treatment of primary uveal melanoma

**Local treatment (eye preservation or enucleation):**
- **Plaque brachytherapy (I-125 episcleral plaque):** Standard for medium tumors (≤10 mm height); comparable local control to enucleation; 5-year local failure rate ~10%; visual acuity decline over time (radiation optic neuropathy, maculopathy)
- **Proton beam radiotherapy:** Requires specialized facility (Boston, San Francisco, Philadelphia); excellent local control; particularly for large/posteriorly located tumors
- **Stereotactic radiosurgery (Gamma Knife, CyberKnife):** Emerging for select cases
- **Enucleation:** Required for large tumors (>12 mm height) or those not amenable to globe-sparing treatment; no OS benefit over brachytherapy (COMS trial)
- **COMS Trial:** Iodine-125 brachytherapy vs. enucleation for medium choroidal melanoma: equivalent 5-year survival (~81% both arms) — established eye-preserving therapy as standard

**Iris melanoma:** Wide local excision or iridocyclectomy; low metastatic risk; usually indolent

### Treatment of metastatic uveal melanoma

**Systemic therapy (prior era — largely ineffective):**
- Dacarbazine, ipilimumab, nivolumab, pembrolizumab: ORR <5%; no OS benefit vs best supportive care
- Selumetinib (MEK1/2 inhibitor): ORR ~15%; improved PFS over chemotherapy but no OS benefit (SUMIT trial vs dacarbazine+temozolomide)
- Combination MEK+PKC (selumetinib+sotrastaurin): modest activity

**Tebentafusp (Kimmtrak — FDA Jan 2022 for HLA-A*02:01+ metastatic uveal melanoma):**
- **Mechanism:** ImmTAC (immune-mobilizing monoclonal TCR against cancer) bispecific: one arm is a soluble high-affinity TCR binding gp100/PMEL17 peptide-HLA-A*02:01 complex on melanoma cells; other arm is anti-CD3 scFv → recruits polyclonal T cells → directed killing regardless of TCR specificity
- **HLA restriction:** Requires HLA-A*02:01 genotype (~50% of Caucasians, ~25% of Asians); companion diagnostic required
- **IMCgp100-202 (Phase 3 RCT, N=378):** Tebentafusp vs. investigator's choice (pembrolizumab, ipilimumab, or dacarbazine) in HLA-A*02:01+ treatment-naive metastatic uveal melanoma: OS 21.7 vs 16.0 months (HR 0.51, p<0.001); 1-year OS 73% vs 58%; first Phase 3 OS benefit in metastatic uveal melanoma [^nathan-2021-tebentafusp]
- **Toxicity:** Cytokine release syndrome (grades 1-3 in >80%, Grade 4 rare); skin reactions (rash, erythema); pyrexia; most toxicities occur with first 3 infusions and diminish
- **Limitation:** Only for HLA-A*02:01+ patients; liver metastasis ORR ~10% (better for non-liver sites); primary benefit likely through immune activation rather than direct tumor lysis

**Liver-directed therapies:**
- Hepatic arterial infusion (HAI): melphalan via isolated hepatic perfusion (IHP/Delcath); ORR ~35-50%; liver-directed control; ~6-month hepatic PFS; not OS benefit demonstrated in Phase 3
- TACE (transarterial chemoembolization): ORR ~25-35%; symptom control
- Y-90 radioembolization (SIR-spheres/TheraSphere): moderate activity in liver metastases
- Surgical resection: for solitary/few hepatic metastases; 3-year OS ~30-40% in selected series

**Surveillance:**
- Liver MRI or ultrasound every 6 months for ≥5 years after primary treatment
- Class 1B (SF3B1): surveillance extended to 15+ years given late relapse pattern
- LFTs, LDH at each visit
- COMS trial showed no benefit of pre-enucleation radiation in reducing metastasis

## Connections

- `connects-to` → **[SF3B1](../../03-molecular/sf3b1/README.md)** — SF3B1 R625C/H occurs in ~15-20% uveal melanoma → cryptic 3' SS activation → Class 1B (intermediate prognosis, late relapses); SF3B1-mutant uveal melanoma has a distinct transcriptome from BAP1-loss Class 2; H3B-8800 may exploit this vulnerability.
- `connects-to` → **[BAP1](../../03-molecular/bap1/README.md)** — BAP1 biallelic loss → Class 2 uveal melanoma (~45%; high metastatic risk, early liver relapse); BAP1 IHC nuclear loss is the primary prognostic marker; BAP1-TPDS germline → uveal melanoma lifetime risk ~30-45%; EZH2 inhibition studied in BAP1-null disease.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN loss occurs in ~15-20% of metastatic uveal melanoma; PI3K-AKT-mTOR activation drives progression; PI3K/mTOR + MEK inhibitor combinations overcome GNAQ-driven resistance in preclinical uveal melanoma models; everolimus studied in metastatic disease.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — PD-1/PD-L1 checkpoint inhibitors have very low activity in uveal melanoma (ORR <5%) due to low tumor mutational burden and immunosuppressive tumor microenvironment; tebentafusp bypasses checkpoint resistance by directly recruiting T cells via gp100-TCR×CD3 bispecific mechanism.
- `connects-to` → **[Melanoma](../melanoma/README.md)** — Uveal melanoma is biologically distinct from cutaneous melanoma: GNAQ/GNA11 (not BRAF V600E) → MEK inhibitors only partial activity; very low TMB vs UV-mutational burden; ICB ORR <5% in uveal vs 30-60% in cutaneous; liver-dominant metastasis vs lung/brain tropism.
- `connects-to` → **[YAP1](../../03-molecular/yap1/README.md)** — GNAQ/GNA11 → PLCβ → PKC → Rho → YAP/TAZ nuclear entry (Hippo-independent); YAP/TAZ drive CTGF, CYR61, BIRC5 → uveal melanoma proliferation and survival; verteporfin (YAP inhibitor) active in preclinical uveal models; YAP-TEAD inhibitors (IAG933, VT3989) in Phase 1/2 trials.
- `connects-to` → **[BRAF](../../03-molecular/braf/README.md)** — BRAF V600E absent in uveal melanoma (0%); GNAQ/GNA11 → PLCβ/PKC → MEK (RAS-independent) → BRAF inhibitors ineffective; MEK inhibitors (selumetinib): ORR ~15% (SUMIT trial) but no OS benefit; MEK + PKC combinations overcome adaptive resistance in preclinical uveal melanoma models.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Uveal melanoma is the commonest primary intraocular cancer in adults, from melanocytes of the uveal tract — choroid (~90%), ciliary body, or iris; it presents with painless vision change or floaters, and globe-sparing brachytherapy or proton therapy has replaced most enucleation.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver is uveal melanoma's near-exclusive metastatic target: ~90% of metastases home there (the eye lacks lymphatics), often years after the eye is treated — so lifelong liver surveillance is essential, and liver-directed therapy plus tebentafusp are mainstays.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Uveal melanoma resists checkpoint inhibitors (ORR <5%, low mutational burden), so it engages cytotoxic T cells differently: tebentafusp, a gp100-HLA × CD3 bispecific, tethers CD8+ T cells to HLA-A*02:01 tumor cells — the first drug to improve survival in metastatic disease.
- `connects-to` → **[Mesothelioma](../mesothelioma/README.md)** — Uveal melanoma and mesothelioma both define the BAP1 tumor predisposition syndrome: germline BAP1 loss raises risk of both, plus renal cell carcinoma and skin tumors, and BAP1 loss in a uveal melanoma marks the high-risk class with the worst metastatic prognosis.
- `connects-to` → **[Neurofibromatosis Type 2](../neurofibromatosis-type-2/README.md)** — Uveal melanoma and NF2 converge on the Hippo pathway: NF2's Merlin restrains YAP, while uveal melanoma's GNAQ/GNA11 mutations activate YAP through Hippo—so both illustrate how unleashed YAP/TEAD drives growth, here in the pigmented cells of the eye.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Radiotherapy is the eye-sparing mainstay for uveal melanoma: plaque brachytherapy and proton or photon beams deliver tumoricidal radiation to the choroidal tumor while preserving the globe—an alternative to enucleation, though metastatic risk depends on genetics.
- `connects-to` → **[Retinoblastoma](../retinoblastoma/README.md)** — Uveal melanoma and retinoblastoma are the two principal intraocular malignancies: retinoblastoma is a childhood RB1-driven retinal tumor, while uveal melanoma is an adult melanocytic tumor of the choroid driven by GNAQ/GNA11 and BAP1—both threaten the eye and vision.
- `connects-to` → **[Cholangiocarcinoma](../cholangiocarcinoma/README.md)** — Uveal melanoma and cholangiocarcinoma both belong to the BAP1 syndrome: germline BAP1 loss raises risk of both, and in uveal melanoma somatic BAP1 loss marks the liver-metastasizing tumors—linking an eye cancer to a bile-duct cancer through one chromatin gene.
- `connects-to` → **[Renal Cell Carcinoma](../renal-cell-carcinoma/README.md)** — Uveal melanoma and clear-cell renal cell carcinoma are joined by the BAP1 syndrome: BAP1 loss drives aggressive forms of both, so germline-mutation families are surveilled for eye, kidney, mesothelioma and skin tumors—BAP1 a shared deubiquitinase tumor suppressor.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — VEGF-driven angiogenesis and a leaky vasculature mark uveal melanoma: the tumor secretes VEGF to vascularize the eye and prepare its spread, high levels predict metastasis, and anti-VEGF agents are explored alongside the liver-directed therapy this cancer needs.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Uveal melanoma is immunologically cold yet newly targetable: it carries few mutations and sits in the immune-privileged eye, so checkpoint inhibitors disappoint—but tebentafusp, a gp100-directed bispecific that redirects T cells, is the first agent to improve survival.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Natural killer cells shape uveal melanoma's spread to the liver: circulating tumor cells that downregulate MHC become NK targets, so the balance of NK surveillance versus escape influences whether liver micrometastases grow—central to this cancer's lethal course.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Uveal melanoma is notorious for vasculogenic mimicry: aggressive tumor cells form PAS-positive vascular loops that mimic endothelial channels, supplying blood without true vessels—a pattern that marks poor prognosis and blunts conventional anti-angiogenic therapy.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Uveal melanoma's lethal liver tropism depends on stroma: hepatic stellate cells and fibroblasts build the fibrotic niche that dormant tumor cells colonize, so the liver microenvironment, not just tumor genetics, governs when micrometastases awaken and grow.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — The eye's immune privilege shields uveal melanoma: a TGF-β-rich anterior chamber suppresses helper T-cell responses (ACAID), so tumors grow unchecked locally—part of why this cancer is immunologically cold and slow to trigger systemic immunity.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — Uveal melanoma is driven through ERK by Gq signaling: activating GNAQ/GNA11 mutations fire PLC-PKC to switch on the MAPK/ERK cascade—unlike cutaneous melanoma's BRAF route—so MEK/ERK-pathway inhibition has been the focus of targeted trials.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Tumor-associated macrophages mark high-risk uveal melanoma: paradoxically, a dense macrophage infiltrate (with monosomy 3 and BAP1 loss) signals worse prognosis and higher metastatic risk rather than protective immunity.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — Uveal melanoma differs from skin melanoma at the telomere: it lacks the UV-signature TERT promoter mutations that drive cutaneous melanoma, reflecting its distinct, non-sun-related mutational origin (GNAQ/GNA11, BAP1) and biology.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Uveal melanoma's driver mutations signal through calcium: GNAQ/GNA11 lock the Gq protein on, firing phospholipase C to release calcium that activates PKC and MAPK—the core engine of this eye cancer, distinct from cutaneous melanoma's BRAF.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Uveal melanoma hides in the eye's immune privilege behind regulatory T cells: a Treg-rich, cold microenvironment makes it resist the checkpoint drugs that work in skin melanoma—why the T-cell engager tebentafusp was needed instead.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Uveal melanoma leans on PI3K-AKT through PTEN loss: alongside its Gq-MAPK driver, losing PTEN switches on AKT survival signaling, so combining MAPK and PI3K/AKT blockade is explored against this treatment-resistant cancer.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Hypoxia drives uveal melanoma's aggressiveness: low oxygen in the eye tumor stabilizes HIF and pushes invasion and the metabolic shift that helps it seed the liver, the near-universal site of its lethal spread.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Beyond its near-exclusive liver spread, uveal melanoma can reach the lungs: hematogenous metastasis occasionally seeds pulmonary and other sites, so surveillance looks past the liver in advanced disease.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells underpin the new immunotherapy for uveal melanoma: this normally immune-cold tumor is now attacked with tebentafusp, which redirects T cells to a melanocyte antigen—an approach that leans on antigen presentation.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Uveal melanoma's defining pigment is melanin, built by the copper-dependent enzyme tyrosinase: this trace-metal chemistry marks the tumor's melanocytic origin and supplies the melanoma antigens that tebentafusp exploits.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Though it arises in the eye and is biologically distinct from skin melanoma, uveal melanoma can metastasize to skin and subcutaneous tissue: an unusual cutaneous site of spread beyond its dominant route to the liver.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Uveal melanoma rarely reaches the brain: while the liver dominates its metastatic pattern, late hematogenous spread can seed the central nervous system, a hard-to-treat site that worsens prognosis in advanced disease.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy proves the eye tumor is melanocytic: even when pigment is scant, the beam reveals melanosomes and striated premelanosomes — the same pigment-making organelles found in skin melanoma — settling the cell of origin.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Uveal melanoma can only spread through blood: the eye has no lymphatics, so tumor cells must enter the bloodstream, where they cloak themselves in platelets to survive the journey and lodge in the liver.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Beyond the liver, uveal melanoma can seed the skeleton: widespread hematogenous disease reaches bone and its marrow, a late metastatic site that adds to the burden once the cancer has escaped the eye.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — The growing tumor blinds by lifting the retina: a choroidal melanoma bulges beneath and detaches the retina, starving its photoreceptor neurons and causing the flashes, floaters, and field loss that often bring the patient in.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Uveal melanoma builds its own false vessels: aggressive tumors weave PAS-positive collagen loops and networks (vasculogenic mimicry), and these closed loops are a histologic marker of the worst-prognosis tumors.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — The blood's inflammatory balance forecasts the course: a high neutrophil-to-lymphocyte ratio tracks with worse survival in uveal melanoma, and tumor-associated neutrophils help build the niche its liver metastases settle into.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibody-like therapy finally moved the needle: tebentafusp, a bispecific gp100-CD3 engager, is the first agent to extend survival in metastatic uveal melanoma, while HMB-45 and Melan-A stains and loss of BAP1 confirm the tumor and predict spread.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — Uveal melanoma is uniquely liver-hungry: over 90% of metastases home to the liver, the tumor cells seeding among the hepatocytes, which is why surveillance and liver-directed therapy dominate management of advanced disease.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Advanced disease shows in the red cells: extensive hepatic metastatic burden and its treatment depress erythrocyte production into an anemia, while rising liver enzymes and falling counts together signal progression.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Protons spare the eye: proton-beam radiotherapy and plaque brachytherapy deliver a sharp, contained dose to the ocular tumor while sparing the optic nerve and retina, letting many patients keep the eye instead of losing it to enucleation.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Uveal melanoma can run in families: germline BAP1 mutations transmit a tumor-predisposition syndrome — uveal melanoma with mesothelioma, kidney and skin cancers — so a diagnosis can prompt genetic testing and counseling of relatives.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — Hypoxia shapes its spread to the liver: HIF signaling and the angiogenesis it drives help uveal melanoma colonize the liver, its near-exclusive metastatic site, a hypoxic-niche dependence studied as a therapeutic angle.
- `connects-to` → **[CTLA-4](../../03-molecular/ctla-4/README.md)** — Checkpoint drugs barely dent it: unlike cutaneous melanoma, uveal melanoma's low mutation load makes anti-CTLA-4 and anti-PD-1 largely ineffective, which is why the T-cell-redirecting drug tebentafusp, not classic checkpoint blockade, became its breakthrough therapy.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — The mutant G-protein feeds growth hubs: GNAQ/GNA11 signaling activates PKC-MAPK and the PI3K-AKT-mTOR axis, so mTOR sits among the downstream nodes targeted to slow a tumor lacking the BRAF mutations that drive skin melanoma.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Its immune infiltrate predicts danger: tumor-infiltrating macrophages and mast cells mark the inflammatory, monosomy-3 uveal melanomas with the worst prognosis, so the immune microenvironment is read as a marker of metastatic risk.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^nathan-2021-tebentafusp]: Nathan P, Hassel JC, Rutkowski P, et al. Overall survival benefit with tebentafusp in metastatic uveal melanoma. *N Engl J Med.* 2021;385(13):1196-1206. [doi:10.1056/NEJMoa2103485](https://doi.org/10.1056/NEJMoa2103485) · [PubMed 34551229](https://pubmed.ncbi.nlm.nih.gov/34551229/)
[^harbour-2010-bap1-uveal]: Harbour JW, Onken MD, Roberson ED, et al. Frequent mutation of BAP1 in metastasizing uveal melanomas. *Science.* 2010;330(6009):1410-1413. [doi:10.1126/science.1194472](https://doi.org/10.1126/science.1194472) · [PubMed 21051595](https://pubmed.ncbi.nlm.nih.gov/21051595/)
