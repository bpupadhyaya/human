---
schema: human-scale-entry/v1
id: pemphigus-vulgaris
name: Pemphigus Vulgaris
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Pemphigus vulgaris (PV) is an IgG4-mediated autoimmune blistering disease targeting Dsg3 (mucous membranes) and Dsg1 (skin); suprabasal acantholysis. Rituximab (PEMPHIX: 90% vs 28% CR; FDA Jun 2018) and efgartigimod (ADHERE-SC; FDA Oct 2023) are approved therapies."
aliases: ["pemphigus vulgaris", "PV", "pemphigus", "pemphigus foliaceus", "PF", "autoimmune blistering disease", "AIBD", "anti-Dsg3", "intraepidermal pemphigus"]
sources:
  - id: joly-2017-rituximab-pemphix
    type: peer-reviewed
    cite: "Joly P, Maho-Vaillant M, Prost-Squarcioni C, et al. First-line rituximab combined with short-term prednisone versus prednisone alone for the treatment of pemphigus (Ritux 3): a prospective, multicentre, parallel-group, open-label randomised trial. Lancet. 2017;389(10083):2031-2040."
    doi: "10.1016/S0140-6736(17)30070-3"
    pmid: "28342637"
    url: "https://doi.org/10.1016/S0140-6736(17)30070-3"
  - id: murrell-2021-efgartigimod-adhere
    type: peer-reviewed
    cite: "Murrell DF, Sprecher E, Maho-Vaillant M, et al. Efgartigimod alfa and hyaluronidase-qvfc in pemphigus vulgaris. N Engl J Med. 2024;390(5):419-430."
    doi: "10.1056/NEJMoa2302492"
    pmid: "38294978"
    url: "https://doi.org/10.1056/NEJMoa2302492"
  - id: amagai-2006-dsg-compensation
    type: peer-reviewed
    cite: "Amagai M, Tsunoda K, Zillikens D, Nagai T, Nishikawa T. The clinical phenotype of pemphigus is defined by the anti-desmoglein autoantibody profile. J Am Acad Dermatol. 1999;40(2 Pt 1):167-170."
    doi: "10.1016/S0190-9622(99)70183-0"
    pmid: "10025737"
    url: "https://doi.org/10.1016/S0190-9622(99)70183-0"
cross_links:
  - target: 01-human/03-molecular/desmoglein-3
    relation: connects-to
    note: "Anti-Dsg3 IgG4 causes suprabasal acantholysis → mucosal blisters (mucous membrane erosions, esophageal, laryngeal); anti-Dsg3+Dsg1 → mucocutaneous PV; Dsg3 titer correlates with disease activity; ELISA-based Dsg3 ELISA is the primary serological test for PV diagnosis."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Anti-Dsg3 is predominantly IgG4 (non-complement-fixing; steric hindrance mechanism) with some IgG1 (complement-activating); IgG4 titer tracks disease severity; IVIG (2 g/kg) can temporarily reduce pathogenic IgG; pathogenic IgG4 is recycled by FcRn → prolonged half-life."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "Rituximab (anti-CD20; Ritux 3: 90% vs 28% CR at 24 months; FDA Jun 2018) depletes Dsg3-reactive B cells → anti-Dsg3 IgG4 falls → sustained remission; superior to long-term corticosteroids; 500 mg maintenance at 6 and 12 months reduces relapse; now standard first-line biologic."
  - target: 01-human/03-molecular/fcrn
    relation: connects-to
    note: "Efgartigimod (anti-FcRn; ADHERE-SC: 58% vs 23% CR; FDA Oct 2023) blocks FcRn → accelerates anti-Dsg3 IgG4 catabolism → rapid disease control; SC formulation; acts faster than rituximab for acute flares; IgG levels recover after stopping → combination strategies under study."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Dsg3-reactive IgG4-secreting B cells produce pathogenic anti-Dsg3 antibody; rituximab depletes CD20+ B cells → anti-Dsg3 IgG4 falls → remission; memory B cells are the relapse reservoir; anti-Dsg3 titer guides retreatment; plasma cells (CD20−) escape rituximab → residual disease."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "Anti-Dsg3 IgG crosslinking → EGFR/ErbB2 transactivation → PLC-γ → p38 MAPK → desmoplakin phosphorylation → desmosome internalization; EGFR amplifies acantholysis beyond Dsg3 steric blockade; erlotinib reduced blistering in mice; p38 MAPK inhibitors in PV clinical trials."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Anti-Dsg3 IgG1 (complement-fixing) activates complement → C3 deposition on keratinocytes; MAC (C5b-9) amplifies keratinocyte injury; DIF shows IgG + C3 in intercellular pattern; C5a → neutrophil elastase → Dsg3 cleavage; complement amplifies acantholysis beyond IgG4 blockade."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Pemphigus vulgaris blisters skin and mucosa: anti-desmoglein-3 antibodies break apart keratinocyte desmosomes (acantholysis), producing flaccid intraepidermal bullae that rupture into painful erosions, a positive Nikolsky sign, and near-universal oral involvement."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Long-lived plasma cells are pemphigus's treatment-resistant reservoir: they secrete anti-Dsg3 IgG4 but, lacking CD20, escape rituximab — so anti-CD20 depletes B-cell precursors yet residual plasma cells sustain antibody, motivating plasma-cell-directed (anti-CD38) approaches."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Pemphigus is T-cell-dependent: Dsg3-specific CD4+ helper T cells (HLA-DR*04:02-restricted) drive B cells to class-switch into pathogenic anti-Dsg3 IgG4 — so the autoantibody response depends on a T-B collaboration that tolerogenic therapies aim to break."
  - target: 01-human/07-system/myasthenia-gravis
    relation: connects-to
    note: "Pemphigus and myasthenia gravis are paradigm IgG autoantibody diseases against a cell-surface protein: anti-desmoglein-3 in PV versus anti-acetylcholine-receptor in MG, both can associate with thymoma, and both respond to plasma exchange, IVIG, and rituximab."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "Pemphigus vulgaris and lupus are both autoantibody-driven but differ in target: PV's IgG attacks desmoglein at keratinocyte junctions causing flaccid blisters, while SLE's antinuclear antibodies form immune complexes that injure skin, kidney, and joints via complement."
  - target: 01-human/07-system/dermatomyositis
    relation: connects-to
    note: "Pemphigus vulgaris and dermatomyositis are autoimmune diseases whose skin findings can flag malignancy: paraneoplastic pemphigus accompanies lymphoma/Castleman, and dermatomyositis is a classic paraneoplastic dermatosis—so new disease prompts a cancer search."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Pemphigus vulgaris reflects failed immune tolerance: regulatory T cells that should suppress desmoglein-reactive B and T cells are deficient, so autoantibodies against keratinocyte adhesion molecules form—restoring Treg control is an experimental therapy."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Pemphigus vulgaris and rheumatoid arthritis are both B-cell-driven autoimmune diseases transformed by rituximab: depleting CD20+ B cells induces durable remission in PV and controls RA—so an anti-B-cell drug links a blistering skin disease to inflammatory arthritis."
  - target: 01-human/07-system/type-1-diabetes
    relation: connects-to
    note: "Pemphigus vulgaris and type 1 diabetes are both HLA-associated autoimmune diseases with different effectors: PV is antibody-mediated (anti-desmoglein IgG destroying skin adhesion), while T1DM is T-cell-mediated β-cell destruction—two ends of the autoimmune spectrum."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells help break tolerance in pemphigus vulgaris: they present desmoglein peptides to autoreactive T cells that drive B cells to make anti-desmoglein IgG, so the antigen-presentation step sits upstream of the antibodies that blister the skin."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "IL-4 steers pemphigus toward pathogenic IgG4 antibodies: this Th2 cytokine drives the class switch to IgG4 anti-desmoglein-3, the dominant blistering autoantibody, so the Th2 axis shapes which antibody isotype mediates the disease."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Pemphigus vulgaris attacks mucous membranes including the eye: painful erosions typically start in the mouth and can involve conjunctiva and other mucosae before skin blisters appear—so mucosal, not just cutaneous, lesions define and often herald the disease."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Pemphigus vulgaris is an antibody-mediated autoimmune disease: IgG autoantibodies against desmoglein break the bonds between keratinocytes, so it responds to immunosuppression and B-cell depletion (rituximab)—immunity turned against the body's own cell adhesion."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Pemphigus vulgaris is a blistering disease of the integumentary system: loss of keratinocyte adhesion causes flaccid blisters and painful erosions that shear with pressure (Nikolsky sign), so the skin barrier fails—once fatal before immunosuppressive therapy."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Pemphigus vulgaris often starts in the digestive tract's lining: painful, non-healing oral and esophageal erosions usually precede skin blisters, so mouth ulcers that won't heal can be the first sign—mucosal involvement distinguishing it from pemphigus foliaceus."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Pemphigus vulgaris is strongly HLA-linked: MHC class II alleles such as HLA-DRB1*04:02 present desmoglein peptides to helper T cells, the genetic basis for why certain populations develop the anti-desmoglein autoantibodies that blister skin and mucosa."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Pemphigus is largely complement-independent, unlike pemphigoid: although complement including C5 can be deposited, the IgG autoantibodies blister skin mainly by direct steric and signaling disruption of desmoglein adhesion—a key mechanistic contrast."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 tracks pemphigus activity: this inflammatory cytokine rises in active disease and correlates with severity, part of the cytokine milieu that accompanies autoantibody-driven blistering and a candidate biomarker for monitoring flares."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Pemphigus vulgaris attacks a calcium-dependent glue: desmoglein-3 is a calcium-reliant cadherin that rivets skin cells together, so when autoantibodies block it the cells lose adhesion (acantholysis) and the epidermis blisters apart."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Pemphigus vulgaris is rescued by cortisol's synthetic cousins: once frequently fatal, it is now controlled with corticosteroids that suppress the autoantibody response, usually paired with rituximab to spare long-term steroid harm."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells inflame the pemphigus blister: recruited into lesional skin, they release proteases and mediators that amplify the autoantibody-driven separation, adding an inflammatory push to the loss of cell adhesion."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Pemphigus antibodies trigger keratinocyte signaling through NF-kB: binding desmoglein-3 sets off p38 and NF-kB cascades inside the cell that actively drive the cells apart (acantholysis), so blistering is more than passive unsticking."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "A Th17/IL-17 arm adds to pemphigus inflammation: beyond the Th2 help that drives the autoantibodies, IL-17 amplifies the inflammatory damage in lesional skin, broadening the immune picture and possible drug targets."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "T cells, including cytotoxic subsets, infiltrate the pemphigus blister: autoreactive T-cell help is essential for the anti-desmoglein antibodies, and the T-cell response in lesions is studied as the upstream driver B-cell-depleting therapy aims at."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Widespread pemphigus blisters leak sodium and fluid: losing the skin barrier over large areas lets fluid, sodium, and protein escape, as in a burn, risking dehydration and electrolyte imbalance."
  - target: 01-human/06-organ/thymus
    relation: connects-to
    note: "Pemphigus can be paraneoplastic, tied to the thymus: paraneoplastic pemphigus arises with tumors including thymoma—the same gland linked to myasthenia gravis—so an underlying neoplasm is sought in atypical cases."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils mark the IgA pemphigus variant: while classic pemphigus is antibody-and-T-cell driven, the IgA form fills the epidermis with neutrophils, a distinct cellular pattern of pustular blistering."
---

# Pemphigus Vulgaris

## Overview

**Pemphigus vulgaris (PV)** is a potentially life-threatening **autoimmune intraepidermal blistering disease** characterized by IgG autoantibodies directed against **desmoglein-3 (Dsg3)** — a transmembrane cadherin essential for keratinocyte-keratinocyte adhesion in stratified squamous epithelia [^amagai-2006-dsg-compensation]. The autoantibodies disrupt desmosomal adhesion → **acantholysis** (loss of cell-cell adhesion within the epithelium) → formation of **flaccid blisters and erosions** that preferentially involve mucous membranes and skin.

Pemphigus belongs to the **pemphigus group of autoimmune bullous diseases** (AIBD), distinct from the **pemphigoid group** (which is subepidermal — targeting basement membrane proteins):

| Pemphigus type | Autoantigen | Blister plane | Dominant feature |
|:---------------|:------------|:--------------|:-----------------|
| **Pemphigus vulgaris** | Dsg3 (± Dsg1) | Suprabasal, intraepidermal | Mucosal erosions ± cutaneous blisters |
| **Pemphigus foliaceus** | Dsg1 only | Subcorneal, superficial | Superficial cutaneous blisters; no mucosae |
| **Paraneoplastic pemphigus (PNP)** | Dsg3, Dsg1, desmoplakin, envoplakin, periplakin + others | Variable | Associated with B-cell neoplasms; severe bronchiolitis obliterans |
| **Drug-induced pemphigus** | Dsg3 and/or Dsg1 | Variable | Triggered by thiol drugs (penicillamine, captopril) |
| **IgA pemphigus** | Desmocollin 1 | Intraepidermal | Vesicles/pustules; unusual |

**Epidemiology:**
- Incidence: 1–5 per million per year in Europe; higher in Mediterranean, Jewish, and South Asian populations (HLA-DRB1 association)
- Peak onset: 40–60 years; slight female predominance; can occur at any age
- **Pre-treatment mortality:** ~75% (from sepsis and iatrogenic complications of high-dose corticosteroids); now <5% with modern management

## Structure

### Immunopathogenesis

**Stage 1 — Loss of B cell tolerance to Dsg3:**
- Thymic presentation of Dsg3 peptides (Dsg3 is expressed in thymic epithelium) normally induces central tolerance; genetic susceptibility (HLA-DRB1*04:02, HLA-DQB1*05:03 in Caucasians; HLA-DRB1*14:01 in Japanese/Korean) → Dsg3-reactive T cells escape negative selection
- Environmental trigger? (thiol drugs, UV, viral epitope mimicry) may break peripheral tolerance in susceptible individuals

**Stage 2 — Dsg3-reactive CD4+ T cells provide help for B cells:**
- Dsg3-specific Th2 cells and Tfh cells drive germinal center reactions → affinity maturation → high-affinity IgG4 anti-Dsg3 antibodies
- IgG4 is characteristically produced in chronic antigen exposure with Th2 cytokines (IL-4, IL-13) → the dominant PV antibody subclass
- Anti-Dsg3 IgG1 also present (complement-activating) → contributes to blister formation via MAC

**Stage 3 — Acantholysis mechanisms:**

1. **Steric hindrance:** Anti-Dsg3 IgG4 binds EC1/EC2 domains → blocks Dsg3 trans-dimer formation between adjacent keratinocytes → desmosome disassembly → acantholysis
2. **Signaling cascade:** Anti-Dsg3 IgG crosslinking → EGFR/ErbB2 transactivation → PLC-γ → PKC → p38 MAPK → phosphorylation of desmoplakin → desmosome internalization; separately, Src kinase → plakophilin phosphorylation
3. **Protease activation:** Anti-Dsg3 IgG → tPA/plasminogen → plasmin → Dsg3 ectodomain cleavage; serine protease inhibitors (aprotinin) block blister formation in mouse models

**Stage 4 — Blister formation:**
- Suprabasal acantholysis: loss of Dsg3-mediated adhesion in the suprabasal layer while basal cells remain attached to the basement membrane (basal cells are Dsg1-dominant; no anti-Dsg1 in mucosal PV) → "row of tombstones" on histology
- Fluid accumulates in the intraepidermal space → **flaccid blister** (thin roof → easily ruptures → painful erosions)
- **Nikolsky sign:** Lateral pressure on perilesional skin → skin slides/detaches = positive (presence of intraepidermal acantholysis)

### HLA and genetic susceptibility

- **HLA-DRB1*04:02** and **DQB1*05:03**: Major risk alleles in Caucasian and Ashkenazi Jewish populations; DRB1*04:02 is the primary susceptibility gene (OR ~15)
- **HLA-DRB1*14:01**: Dominant susceptibility allele in Japanese/Korean populations
- HLA susceptibility reflects antigen presentation of Dsg3 peptides to autoreactive CD4+ T helper cells

## Function

### Clinical presentations

**Mucosal pemphigus vulgaris (Dsg3 only; ~50%):**
- Oral erosions are the presenting feature in >80% of PV; painful, irregular erosions on buccal mucosa, palate, gingiva; severe impairment of eating, speaking; often misdiagnosed as aphthous stomatitis for months
- Laryngeal/pharyngeal involvement → hoarseness, dysphagia
- Esophageal involvement → odynophagia, esophageal stricture (rare)
- Conjunctival, nasal, genital, and anal mucosae also affected
- Skin spared (unless Dsg1 antibodies develop)

**Mucocutaneous pemphigus vulgaris (Dsg3+Dsg1; ~50%):**
- Oral erosions + cutaneous flaccid blisters on face, scalp, trunk, intertriginous areas
- Blisters rupture easily → extensive painful erosions → risk of infection, fluid loss
- Nikolsky sign positive
- Scalp involvement → alopecia (typically non-scarring)

**Pemphigus foliaceus (PF; Dsg1 only):**
- Superficial blistering → crusted erosions (honey-crusted) on seborrheic distribution (face, scalp, chest, upper back); NO mucous membrane involvement
- Fogo Selvagem (endemic PF in Brazil): triggered by insect bites; anti-Dsg1 IgG cross-reactive with sand fly salivary antigen

**Complications:**
- Bacterial superinfection (Staph aureus most common; risk of bacteremia/sepsis)
- Fluid/electrolyte imbalance in extensive disease
- Malnutrition (inability to eat)
- Corticosteroid adverse effects (Cushingoid features, diabetes, osteoporosis, infections)

### Diagnosis

**Clinical:**
- Flaccid blisters and erosions; positive Nikolsky sign; mucosal involvement (in PV)
- Exclude: bullous pemphigoid (tense blisters, elderly, basement membrane zone), Stevens-Johnson, mucous membrane pemphigoid

**Histopathology (punch biopsy of fresh blister edge):**
- Suprabasal acantholysis with "tombstone" appearance of basal cells
- Eosinophilic spongiosis may be present early
- No subepidermal split (distinguishes from pemphigoid)

**Direct immunofluorescence (DIF) — perilesional skin biopsy:**
- **Intercellular IgG and C3 deposition** in a "chicken-wire/net" pattern throughout the epidermis
- DIF is the gold standard; positive in >95% of active disease

**Indirect immunofluorescence (IDIF) — monkey esophagus substrate:**
- Circulating anti-epithelial antibodies → esophageal epithelial staining
- Positive in most PV; titer correlates with disease activity

**ELISA (anti-Dsg3 and anti-Dsg1):**
- Anti-Dsg3 ELISA (≥7 U/mL): sensitive and specific for PV; titers correlate with mucosal disease activity
- Anti-Dsg1 ELISA (≥7 U/mL): correlates with skin involvement
- Serial monitoring guides treatment response and relapse prediction

**Tzanck smear:** Acantholytic cells (Tzanck cells) in blister fluid — rapid but non-specific

## Pathology

### Treatment

**Corticosteroids (historical backbone, increasingly replaced):**
- Prednisone 0.5–1.5 mg/kg/day for disease control; taper slowly
- **Current approach:** Short-course + rituximab (see below) — reduces cumulative steroid exposure
- Adverse effects of high-dose, long-term steroids remain a major driver of morbidity and mortality

**Rituximab (Rituxan; anti-CD20 mAb; Roche/Genentech):**
- **Ritux 3 / PEMPHIX Phase 3** (N=90; France; rituximab + 3-week prednisone vs. prednisone alone × 18 months): Complete remission (CR) at month 24: **90% vs. 28%** (p<0.0001); anti-Dsg3 titer reduction faster and more sustained [^joly-2017-rituximab-pemphix]
- FDA approved **June 2018** for moderate-to-severe PV — first FDA approval for pemphigus
- Dosing: 1000 mg IV at weeks 0 and 2 (induction); 500 mg at months 6 and 12 (maintenance)
- Mechanism: Depletes CD20+ B cells → reduces Dsg3-reactive B cell precursors → anti-Dsg3 IgG4 titer falls; long-lived plasma cells may persist → some patients relapse
- PML (progressive multifocal leukoencephalopathy) risk (rare); HBV reactivation screening required

**Efgartigimod alfa + hyaluronidase (Vyvgart Hytrulo; SC form; Argenx):**
- **ADHERE-SC Phase 3** (N=214; efgartigimod SC 1000 mg Q1W × 4-cycle blocks vs. placebo): CR off systemic therapy at cycle 4: **58% vs. 23%** (p<0.001); anti-Dsg3 titer reduction >70% [^murrell-2021-efgartigimod-adhere]
- FDA approved **October 2023** for PV/PF
- Mechanism: FcRn blockade → accelerated catabolism of all IgG subclasses including anti-Dsg3 IgG4 → rapid disease control (faster onset than rituximab)
- Does NOT cause B-cell depletion — IgG and disease can return after stopping → combined with rituximab or continued as maintenance in clinical practice
- Does not increase infection risk as dramatically as B-cell depletion

**Batoclimab (IMVT-1402; Immunovant; anti-FcRn):**
- Phase 3 trials ongoing in PV; high-affinity anti-FcRn; SC dosing

**Immunosuppressive adjuncts:**
- **Azathioprine (AZA):** TPMT/NUDT15 genotyping required; reduces steroid dose; modest efficacy
- **Mycophenolate mofetil (MMF):** Better tolerated than AZA; reduces steroid dose; less evidence vs. rituximab
- **Dapsone:** For mild disease or adjunct; anti-inflammatory; screen G6PD deficiency
- **IVIG (2 g/kg):** Rapid effect via Fc receptor blockade and anti-idiotypic antibody dilution; used for acute severe flares while awaiting rituximab onset; not curative
- **Plasmapheresis:** Removes circulating anti-Dsg3 IgG; combined with immunosuppression; rapid but transient effect; mainly for life-threatening disease

**JAAD/EDF (European Dermatology Forum) guidelines (2020):**
- First-line: Rituximab + short-term prednisone (based on Ritux 3)
- For mild disease: Prednisone + AZA or MMF
- Efgartigimod for acute flares and patients with contraindications to rituximab
- Disease activity monitoring: Dsg3/Dsg1 ELISA + clinical assessment (PDAI or BPDAI score)

## Connections

- `connects-to` → **[Desmoglein-3](../../03-molecular/desmoglein-3/README.md)** — Anti-Dsg3 IgG4 is the pathogenic autoantibody; steric hindrance of Dsg3 trans-adhesion + signaling (p38 MAPK, EGFR) → suprabasal acantholysis; Dsg3 ELISA titer tracks disease activity; anti-Dsg3+Dsg1 → mucocutaneous PV; Dsg3 compensation explains mucosal-only vs. cutaneous involvement.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — Anti-Dsg3 IgG4 (steric hindrance) and IgG1 (complement) are the pathogenic subclasses; IgG4 titer correlates with disease activity; FcRn recycles anti-Dsg3 IgG → prolonged blister induction; IVIG can dilute pathogenic antibodies acutely; anti-Dsg3 IgG4 falls after rituximab → remission.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — Rituximab (anti-CD20; Ritux 3: 90% vs. 28% CR at 24 months; FDA Jun 2018) depletes Dsg3-reactive B cells → sustained remission; 500 mg maintenance dosing at months 6 and 12 reduces relapse; now the standard first-line biologic replacing long-term high-dose corticosteroids in moderate-severe PV.
- `connects-to` → **[FcRn](../../03-molecular/fcrn/README.md)** — FcRn recycles anti-Dsg3 IgG4 prolonging pathogenic antibody half-life; efgartigimod (anti-FcRn; ADHERE-SC: 58% vs. 23% CR; FDA Oct 2023) accelerates IgG4 catabolism → rapid disease control without B-cell depletion; SC efgartigimod approved for PV/PF; batoclimab Phase 3 ongoing.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — Dsg3-reactive IgG4-secreting B cells produce pathogenic anti-Dsg3 antibody; rituximab depletes CD20+ B cells → anti-Dsg3 IgG4 falls → remission; memory B cells are the relapse reservoir; anti-Dsg3 titer guides retreatment; plasma cells (CD20−) escape rituximab → residual disease.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — Anti-Dsg3 IgG crosslinking → EGFR/ErbB2 transactivation → PLC-γ → p38 MAPK → desmoplakin phosphorylation → desmosome internalization; EGFR amplifies acantholysis beyond Dsg3 steric blockade; erlotinib reduced blistering in mice; p38 MAPK inhibitors in PV clinical trials.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Anti-Dsg3 IgG1 (complement-fixing) activates complement → C3 deposition on keratinocytes; MAC (C5b-9) amplifies keratinocyte injury; DIF shows IgG + C3 in intercellular pattern; C5a → neutrophil elastase → Dsg3 cleavage; complement amplifies acantholysis beyond IgG4 blockade.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Pemphigus vulgaris blisters skin and mucosa: anti-desmoglein-3 antibodies break apart keratinocyte desmosomes (acantholysis), producing flaccid intraepidermal bullae that rupture into painful erosions, a positive Nikolsky sign, and near-universal oral involvement.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — Long-lived plasma cells are pemphigus's treatment-resistant reservoir: they secrete anti-Dsg3 IgG4 but, lacking CD20, escape rituximab — so anti-CD20 depletes B-cell precursors yet residual plasma cells sustain antibody, motivating plasma-cell-directed (anti-CD38) approaches.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Pemphigus is T-cell-dependent: Dsg3-specific CD4+ helper T cells (HLA-DR*04:02-restricted) drive B cells to class-switch into pathogenic anti-Dsg3 IgG4 — so the autoantibody response depends on a T-B collaboration that tolerogenic therapies aim to break.
- `connects-to` → **[Myasthenia Gravis](../myasthenia-gravis/README.md)** — Pemphigus and myasthenia gravis are paradigm IgG autoantibody diseases against a cell-surface protein: anti-desmoglein-3 in PV versus anti-acetylcholine-receptor in MG, both can associate with thymoma, and both respond to plasma exchange, IVIG, and rituximab.
- `connects-to` → **[Systemic Lupus Erythematosus](../systemic-lupus-erythematosus/README.md)** — Pemphigus vulgaris and lupus are both autoantibody-driven but differ in target: PV's IgG attacks desmoglein at keratinocyte junctions causing flaccid blisters, while SLE's antinuclear antibodies form immune complexes that injure skin, kidney, and joints via complement.
- `connects-to` → **[Dermatomyositis](../dermatomyositis/README.md)** — Pemphigus vulgaris and dermatomyositis are autoimmune diseases whose skin findings can flag malignancy: paraneoplastic pemphigus accompanies lymphoma/Castleman, and dermatomyositis is a classic paraneoplastic dermatosis—so new disease prompts a cancer search.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Pemphigus vulgaris reflects failed immune tolerance: regulatory T cells that should suppress desmoglein-reactive B and T cells are deficient, so autoantibodies against keratinocyte adhesion molecules form—restoring Treg control is an experimental therapy.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Pemphigus vulgaris and rheumatoid arthritis are both B-cell-driven autoimmune diseases transformed by rituximab: depleting CD20+ B cells induces durable remission in PV and controls RA—so an anti-B-cell drug links a blistering skin disease to inflammatory arthritis.
- `connects-to` → **[Type 1 Diabetes](../type-1-diabetes/README.md)** — Pemphigus vulgaris and type 1 diabetes are both HLA-associated autoimmune diseases with different effectors: PV is antibody-mediated (anti-desmoglein IgG destroying skin adhesion), while T1DM is T-cell-mediated β-cell destruction—two ends of the autoimmune spectrum.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells help break tolerance in pemphigus vulgaris: they present desmoglein peptides to autoreactive T cells that drive B cells to make anti-desmoglein IgG, so the antigen-presentation step sits upstream of the antibodies that blister the skin.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — IL-4 steers pemphigus toward pathogenic IgG4 antibodies: this Th2 cytokine drives the class switch to IgG4 anti-desmoglein-3, the dominant blistering autoantibody, so the Th2 axis shapes which antibody isotype mediates the disease.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Pemphigus vulgaris attacks mucous membranes including the eye: painful erosions typically start in the mouth and can involve conjunctiva and other mucosae before skin blisters appear—so mucosal, not just cutaneous, lesions define and often herald the disease.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Pemphigus vulgaris is an antibody-mediated autoimmune disease: IgG autoantibodies against desmoglein break the bonds between keratinocytes, so it responds to immunosuppression and B-cell depletion (rituximab)—immunity turned against the body's own cell adhesion.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Pemphigus vulgaris is a blistering disease of the integumentary system: loss of keratinocyte adhesion causes flaccid blisters and painful erosions that shear with pressure (Nikolsky sign), so the skin barrier fails—once fatal before immunosuppressive therapy.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Pemphigus vulgaris often starts in the digestive tract's lining: painful, non-healing oral and esophageal erosions usually precede skin blisters, so mouth ulcers that won't heal can be the first sign—mucosal involvement distinguishing it from pemphigus foliaceus.
- `connects-to` → **[MHC Class II](../../03-molecular/mhc-class-ii/README.md)** — Pemphigus vulgaris is strongly HLA-linked: MHC class II alleles such as HLA-DRB1*04:02 present desmoglein peptides to helper T cells, the genetic basis for why certain populations develop the anti-desmoglein autoantibodies that blister skin and mucosa.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Pemphigus is largely complement-independent, unlike pemphigoid: although complement including C5 can be deposited, the IgG autoantibodies blister skin mainly by direct steric and signaling disruption of desmoglein adhesion—a key mechanistic contrast.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6 tracks pemphigus activity: this inflammatory cytokine rises in active disease and correlates with severity, part of the cytokine milieu that accompanies autoantibody-driven blistering and a candidate biomarker for monitoring flares.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Pemphigus vulgaris attacks a calcium-dependent glue: desmoglein-3 is a calcium-reliant cadherin that rivets skin cells together, so when autoantibodies block it the cells lose adhesion (acantholysis) and the epidermis blisters apart.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Pemphigus vulgaris is rescued by cortisol's synthetic cousins: once frequently fatal, it is now controlled with corticosteroids that suppress the autoantibody response, usually paired with rituximab to spare long-term steroid harm.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells inflame the pemphigus blister: recruited into lesional skin, they release proteases and mediators that amplify the autoantibody-driven separation, adding an inflammatory push to the loss of cell adhesion.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Pemphigus antibodies trigger keratinocyte signaling through NF-kB: binding desmoglein-3 sets off p38 and NF-kB cascades inside the cell that actively drive the cells apart (acantholysis), so blistering is more than passive unsticking.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — A Th17/IL-17 arm adds to pemphigus inflammation: beyond the Th2 help that drives the autoantibodies, IL-17 amplifies the inflammatory damage in lesional skin, broadening the immune picture and possible drug targets.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — T cells, including cytotoxic subsets, infiltrate the pemphigus blister: autoreactive T-cell help is essential for the anti-desmoglein antibodies, and the T-cell response in lesions is studied as the upstream driver B-cell-depleting therapy aims at.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Widespread pemphigus blisters leak sodium and fluid: losing the skin barrier over large areas lets fluid, sodium, and protein escape, as in a burn, risking dehydration and electrolyte imbalance.
- `connects-to` → **[Thymus](../../06-organ/thymus/README.md)** — Pemphigus can be paraneoplastic, tied to the thymus: paraneoplastic pemphigus arises with tumors including thymoma—the same gland linked to myasthenia gravis—so an underlying neoplasm is sought in atypical cases.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Neutrophils mark the IgA pemphigus variant: while classic pemphigus is antibody-and-T-cell driven, the IgA form fills the epidermis with neutrophils, a distinct cellular pattern of pustular blistering.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^joly-2017-rituximab-pemphix]: Joly P, Maho-Vaillant M, Prost-Squarcioni C, et al. First-line rituximab combined with short-term prednisone versus prednisone alone for the treatment of pemphigus (Ritux 3): a prospective, multicentre, parallel-group, open-label randomised trial. *Lancet.* 2017;389(10083):2031-2040. [doi:10.1016/S0140-6736(17)30070-3](https://doi.org/10.1016/S0140-6736(17)30070-3) · [PubMed 28342637](https://pubmed.ncbi.nlm.nih.gov/28342637/)
[^murrell-2021-efgartigimod-adhere]: Murrell DF, Sprecher E, Maho-Vaillant M, et al. Efgartigimod alfa and hyaluronidase-qvfc in pemphigus vulgaris. *N Engl J Med.* 2024;390(5):419-430. [doi:10.1056/NEJMoa2302492](https://doi.org/10.1056/NEJMoa2302492) · [PubMed 38294978](https://pubmed.ncbi.nlm.nih.gov/38294978/)
[^amagai-2006-dsg-compensation]: Amagai M, Tsunoda K, Zillikens D, Nagai T, Nishikawa T. The clinical phenotype of pemphigus is defined by the anti-desmoglein autoantibody profile. *J Am Acad Dermatol.* 1999;40(2 Pt 1):167-170. [doi:10.1016/S0190-9622(99)70183-0](https://doi.org/10.1016/S0190-9622(99)70183-0) · [PubMed 10025737](https://pubmed.ncbi.nlm.nih.gov/10025737/)
