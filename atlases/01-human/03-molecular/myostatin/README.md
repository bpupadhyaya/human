---
schema: human-scale-entry/v1
id: myostatin
name: Myostatin
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "Myostatin (GDF-8, MSTN, chr2q32.2) is a TGF-β superfamily inhibitor of skeletal muscle growth; ActRIIB → ALK4/5 → SMAD2/3 suppresses satellite cell proliferation and protein synthesis; loss-of-function causes double muscling; apitegromab blocks myostatin proform in SMA."
aliases: ["myostatin", "GDF-8", "GDF8", "growth differentiation factor 8", "MSTN", "myostatin propeptide"]
cross_links:
  - target: 01-human/07-system/musculoskeletal-system
    relation: modulates
    note: "Myostatin is the primary negative regulator of skeletal muscle mass; aging → elevated myostatin → sarcopenia; cachexia → tumor-induced myostatin → muscle wasting; anti-myostatin biologics (bimagrumab, apitegromab) restore lean mass in sarcopenia and SMA."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Myostatin (GDF-8) is a TGF-β superfamily member sharing ActRIIB/SMAD2/3 signaling with TGF-β1; both drive muscle atrophy and fibrosis in DMD and sarcopenia via overlapping SMAD cascades; anti-myostatin therapies exploit TGF-β pathway architecture for muscle preservation."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "IGF-1 and myostatin oppose each other: IGF-1 → Akt → mTORC1 → protein synthesis and satellite cell activation; myostatin → SMAD2/3 → MAFbx/MuRF1 → atrophy; Akt phosphorylates SMAD3 → blunts myostatin pro-atrophy signaling; axis governs net muscle mass in sarcopenia and cachexia."
sources:
  - id: mcpherron-1997-myostatin
    type: peer-reviewed
    cite: "McPherron AC, Lawler AM, Lee SJ. Regulation of skeletal muscle mass in mice by a new TGF-beta superfamily member. Nature. 1997;387(6628):83-90."
    doi: "10.1038/387083a0"
    pmid: "9139826"
    url: "https://doi.org/10.1038/387083a0"
  - id: baranello-2023-apitegromab
    type: peer-reviewed
    cite: "Baranello G, Servais L, Day JW, et al. Apitegromab for spinal muscular atrophy. N Engl J Med. 2023;388(4):306-318."
    doi: "10.1056/NEJMoa2204066"
    pmid: "36652355"
    url: "https://doi.org/10.1056/NEJMoa2204066"
---

# Myostatin

## Overview

**Myostatin** (growth differentiation factor 8, GDF-8; gene *MSTN*, chromosome 2q32.2) is a **member of the TGF-β superfamily** that functions as the **master negative regulator of skeletal muscle mass** — constitutively expressed in skeletal muscle throughout life, limiting both the size of individual muscle fibers (hypertrophy) and the expansion of muscle stem cells (satellite cells; hyperplasia). Discovered in 1997 by McPherron, Lawler, and Lee [^mcpherron-1997-myostatin], myostatin-null mice develop approximately **two to three times normal skeletal muscle mass** through a combination of fiber hypertrophy and hyperplasia — establishing GDF-8 as the physiological "brake" on muscle growth.

Myostatin's importance extends well beyond basic muscle physiology: it is now recognized as a central mediator of **sarcopenia** (age-related muscle loss), **cancer and cardiac cachexia**, **Duchenne muscular dystrophy (DMD)** disease progression, and — critically — a therapeutic target in **spinal muscular atrophy (SMA)**, where pharmacological myostatin blockade amplifies the motor neuron survival gains from SMN-targeted therapies (nusinersen, risdiplam) by preserving the muscle units that SMN therapy rescues innervation for.

**Natural loss-of-function phenotypes:**
- **Belgian Blue and Piedmontese cattle:** Naturally occurring homozygous MSTN frameshift mutations → "double muscling" (2-3× muscle mass, reduced fat)
- **Bully whippets (dogs):** MSTN heterozygous LOF → enhanced racing speed; homozygous = extreme muscling
- **Human infant case (Schuelke et al., 2004):** Child with MSTN frameshift mutation → extraordinary muscle mass, reduced fat — confirmed the muscle-limiting role of myostatin in humans

## Structure

**Biosynthesis and activation:**
Pre-pro-myostatin (375 aa, signal peptide + prodomain + mature region) → signal peptide cleavage → **pro-myostatin (353 aa)** → dimerization via Cys residues in mature domain → **furin** cleavage at RXXR site → non-covalent complex of **pro-domain (LAP: latency-associated peptide)** + **mature GDF-8 C-terminal dimer (109 aa/monomer, 25 kDa homodimer)**.

The **LAP non-covalently inhibits mature GDF-8** — a conserved TGF-β superfamily latency mechanism. In the extracellular matrix, LAP associates with LTBP1/3 or GARP (cell-surface anchor), keeping myostatin in an inactive latent complex. **Tolloid/BMP1 metalloprotease** cleaves LAP → releases active mature GDF-8 → receptor binding.

**Mature GDF-8 dimer structure:**
- Two 109-aa chains linked by a single intermolecular disulfide (Cys at position 313, canonical TGF-β "ring finger")
- Three intramolecular disulfides form the **cystine knot** — the defining structural motif of TGF-β superfamily C-terminal domains
- Receptor-binding determinants: "wrist epitope" (finger 2 and helix 3) contacts ActRIIB; "knuckle epitope" contacts ALK type I receptor
- **Apitegromab (SRK-015)** binds the **pro-domain/latent complex** specifically — it cannot bind active mature GDF-8; this proform-selectivity allows tissue-specific (muscle-preferential) blockade without affecting other GDF-8-related signaling

**Receptor complex:**
- **ActRIIB (ACVR2B):** High-affinity type II receptor (Kd ~0.1 nM); also binds activin A, activin B, GDF-11, BMP9; activates JAK2 → STAT3 (in parallel) and most importantly recruits ALK4/5
- **ActRIIA (ACVR2A):** Moderate-affinity type II receptor (Kd ~1 nM); lower affinity for myostatin; significant for activins
- **ALK4 (ACVR1B) or ALK5 (TGFBR1):** Type I receptor; transphosphorylated by ActRIIB → **SMAD2 and SMAD3 Ser phosphorylation** → SMAD2/3 + SMAD4 heterotrimers → nuclear translocation → transcription
- **Downstream SMAD2/3 targets in muscle:**
  - *FBXO32* (Atrogin-1/MAFbx): E3 ubiquitin ligase → degradation of MyoD and eIF3f → suppression of muscle protein synthesis and differentiation
  - *TRIM63* (MuRF1): E3 ubiquitin ligase → ubiquitination of thick filament myosin heavy chains → myofibrillar protein degradation
  - *MSTN* itself: SMAD2/3 → increased MSTN transcription (feedforward amplification)
  - Inhibition of *IGF1R*/*IRS1* expression → reduced PI3K/Akt/mTOR signaling → blunted protein synthesis

**Inhibitors of myostatin activity (endogenous):**
- **Follistatin (FST):** Binds and neutralizes myostatin (and activin A/B, BMPs); exercise-induced FST release may partially limit myostatin activity; FST gene therapy in DMD models markedly increases muscle mass
- **FSTL1, FSTL3:** Follistatin-like proteins with partial myostatin-neutralizing activity
- **GASP-1 and GASP-2:** (GDF-associated serum proteins) bind mature myostatin → inhibition
- **ActRIIB-Fc decoy (sotrovimab predecessor compounds):** Soluble ActRIIB extracellular domain fused to Fc → pan-ligand trap (myostatin + activins + GDF-11)

## Function

**Regulation of muscle fiber size:**
1. Myostatin → ActRIIB → ALK4/5 → **SMAD2/3** → MAFbx/Atrogin-1 + MuRF1 E3 ligases → ubiquitin-proteasome pathway activation → myofibrillar protein degradation → muscle atrophy
2. SMAD2/3 also → **phospho-p38 MAPK** → MK2 → translation repression
3. Suppression of **PI3K/Akt/mTORC1** axis: myostatin → PTEN upregulation + IRS1 downregulation → reduced Akt phosphorylation → less mTORC1-driven ribosomal protein translation → blunted anabolic response to nutrients and exercise
4. Net result: smaller mean myofiber cross-sectional area, especially in Type II (fast-twitch) fibers where MSTN expression is highest

**Regulation of satellite cell activity:**
- Satellite cells (muscle stem cells): quiescent in adult muscle; activated by injury → MyoD expression → myoblast proliferation → fusion into regenerating myofibers
- Myostatin → SMAD2/3 → **p21 (CDKN1A)** induction → G1 arrest → suppresses satellite cell proliferation; also inhibits MyoD expression → blocks myogenic differentiation
- MSTN-null mice: increased satellite cell number (~28%) and enhanced activation kinetics → faster muscle regeneration after injury
- In sarcopenia: aging → reduced satellite cell number + increased myostatin → dual defect in muscle maintenance

**Sarcopenia and cachexia:**
- Serum myostatin rises with age (more pronounced after age 70) and correlates inversely with muscle mass and grip strength in cross-sectional studies
- Cancer cachexia: tumor-derived factors (TNF-α, IL-6, activin A) → muscle MSTN upregulation + reduced IGF-1/Akt → combined atrophic signals → rapid muscle loss (up to 1-2% lean mass/week in advanced cancer)
- Cardiac cachexia (CHF): AT-II, TNF-α, myostatin all elevated → disproportionate skeletal muscle loss; myostatin correlates with exercise intolerance in NYHA class III-IV heart failure

**Metabolic crosstalk (myostatin and fat mass):**
- Myostatin → reduced muscle oxidative capacity → decreased fatty acid oxidation → adipose expansion; MSTN-null animals show reduced fat depots even on high-fat diet
- Bimagrumab (anti-ActRIIB mAb): blocks both myostatin AND activin A/B → simultaneously increases lean mass and reduces fat mass; uniquely shown in Phase 2 (CLAS trial, 2021) to reduce fat mass 20% + increase lean mass 4% at 48 weeks in obese adults with type 2 diabetes — unmatched by any weight-loss drug in lean-mass preservation

## Mechanism

**Apitegromab (SRK-015) in SMA [^baranello-2023-apitegromab]:**
- SMA is caused by SMN1 gene loss → α-motor neuron degeneration → muscle denervation → progressive atrophy; SMN therapies (nusinersen, risdiplam, onasemnogene) restore SMN protein in motor neurons but cannot reverse established muscle atrophy or compensate in already-denervated fibers
- **Rationale:** SMA muscles have functional satellite cells and preserved muscle architecture if treated early; blocking myostatin → increased satellite cell activity and myofiber maintenance → more muscle substrate for reinnervating motor neurons to innervate
- **SRK-015 mechanism:** Binds myostatin pro-domain/latent complex in a proform-specific manner → prevents tolloid/BMP1-mediated LAP cleavage → prevents activation of mature GDF-8 → muscle-selective activity (pro-GDF-8 is concentrated in skeletal muscle)
- **TOPAZ Phase 2 trial (2023):** Ambulatory SMA patients (age 2-21) already on nusinersen or risdiplam; apitegromab 20 mg/kg IV Q4W × 12 months vs. placebo
- Primary endpoint: RULM (Revised Upper Limb Module) score change: +3.3 (apitegromab) vs. +1.2 (placebo); Hammersmith Functional Motor Scale: +4.2 vs. +1.1; statistically significant
- FDA Breakthrough Therapy Designation; Phase 3 (SAPPHIRE) ongoing

**Bimagrumab (BYM338) in obesity/sarcopenia:**
- Anti-ActRIIB humanized mAb → blocks binding of myostatin, activin A, activin B, GDF-11 (broad ligand trap via receptor blockade rather than ligand neutralization)
- CLAS Phase 2 trial (Heymsfield et al., JAMA Intern Med 2021): 58 obese adults + T2D; bimagrumab 10 mg/kg IV Q4W × 48 weeks; primary endpoint: lean mass change
- Results: lean mass +3.6 kg (bimagrumab) vs. -0.4 kg (placebo); fat mass -20.5% vs. -0.5%; HbA1c reduced significantly; no muscle-to-fat crossover effect seen before — potential new modality for metabolic disease
- Phase 3 trials planned

**Resistance exercise and myostatin:**
- Acute resistance exercise → transient IGF-1 and testosterone surge → suppress myostatin mRNA; chronic resistance training → sustained lower basal myostatin expression → hypertrophy
- This forms the molecular basis of why strength training is the primary anti-sarcopenia intervention: it lowers the myostatin set-point in aging muscle
- Serum follistatin/myostatin ratio rises with resistance training → favorable anabolic milieu

## Connections

Myostatin is the primary negative regulator of skeletal muscle mass; aging → elevated myostatin → sarcopenia; cachexia → tumor-induced myostatin → muscle wasting; anti-myostatin biologics (bimagrumab, apitegromab) restore lean mass in sarcopenia and SMA.

Myostatin (GDF-8) is a TGF-β superfamily member sharing ActRIIB/SMAD2/3 signaling with TGF-β1; both drive muscle atrophy and fibrosis in DMD and sarcopenia via overlapping SMAD cascades; anti-myostatin therapies exploit TGF-β pathway architecture for muscle preservation.

[^mcpherron-1997-myostatin]: McPherron AC, Lawler AM, Lee SJ. Regulation of skeletal muscle mass in mice by a new TGF-beta superfamily member. *Nature.* 1997;387(6628):83-90. [doi:10.1038/387083a0](https://doi.org/10.1038/387083a0) · [PubMed 9139826](https://pubmed.ncbi.nlm.nih.gov/9139826/)
[^baranello-2023-apitegromab]: Baranello G, Servais L, Day JW, et al. Apitegromab for spinal muscular atrophy. *N Engl J Med.* 2023;388(4):306-318. [doi:10.1056/NEJMoa2204066](https://doi.org/10.1056/NEJMoa2204066) · [PubMed 36652355](https://pubmed.ncbi.nlm.nih.gov/36652355/)
