---
schema: human-scale-entry/v1
id: igf-1
name: IGF-1
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "IGF-1 (IGF1, chr12q23.2) is the primary GH mediator; IGF-1R → IRS-1 → PI3K/Akt/mTOR drives growth, muscle anabolism, and bone formation; Laron syndrome = GH resistance, low IGF-1; serum IGF-1 screens acromegaly; teprotumumab (anti-IGF-1R) treats thyroid eye disease."
aliases: ["IGF-1", "insulin-like growth factor 1", "IGF1", "somatomedin C", "IGF-I", "sulfation factor"]
cross_links:
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "IGF-1 → IGF-1R → IRS-1 → PI3K/Akt/mTOR → skeletal muscle protein synthesis and satellite cell activation; opposes myostatin/SMAD2/3 atrophy signaling; IGF-1 drives osteoblast bone matrix synthesis; declining IGF-1 with aging contributes to sarcopenia and osteoporosis."
  - target: 01-human/03-molecular/myostatin
    relation: connects-to
    note: "IGF-1 and myostatin oppose each other: IGF-1 → Akt → mTORC1 → protein synthesis and satellite cell activation; myostatin → SMAD2/3 → MAFbx/MuRF1 → atrophy; Akt phosphorylates SMAD3 → blunts myostatin pro-atrophy signaling; axis governs net muscle mass in sarcopenia and cachexia."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "IGF-1 has insulin-like metabolic effects via IR cross-activation; low serum IGF-1 associates with insulin resistance and T2DM risk; acromegaly (excess GH/IGF-1) causes secondary diabetes; IGF-1 therapy improves insulin sensitivity in severe insulin resistance syndromes."
sources:
  - id: jones-1995-igf-binding-proteins
    type: peer-reviewed
    cite: "Jones JI, Clemmons DR. Insulin-like growth factors and their binding proteins: biological actions. Endocr Rev. 1995;16(1):3-34."
    doi: "10.1210/edrv-16-1-3"
    pmid: "7758431"
    url: "https://doi.org/10.1210/edrv-16-1-3"
  - id: smith-2017-teprotumumab
    type: peer-reviewed
    cite: "Smith TJ, Kahaly GJ, Ezra DG, et al. Teprotumumab for thyroid-associated ophthalmopathy. N Engl J Med. 2017;376(18):1748-1761."
    doi: "10.1056/NEJMoa1614949"
    pmid: "28467880"
    url: "https://doi.org/10.1056/NEJMoa1614949"
---

# IGF-1

## Overview

**Insulin-like growth factor 1 (IGF-1; somatomedin C)** (gene *IGF1*, chromosome 12q23.2) is a **70-amino acid single-chain polypeptide** that is the **primary mediator of growth hormone (GH) action on peripheral tissues** — functioning as the major promoter of somatic growth, muscle anabolism, bone formation, and neuroproliferation throughout postnatal life. Discovered in the 1950s as "sulfation factor" (a serum factor required for sulfate incorporation into cartilage), IGF-1 is structurally homologous to proinsulin (~50% identity) and shares partial receptor cross-reactivity with insulin, placing it at the intersection of growth and metabolic signaling.

**The GH-IGF-1 axis:**
Pituitary GH secretion (driven by hypothalamic GHRH and suppressed by somatostatin) → hepatic GH receptor (GHR, homodimer → JAK2/STAT5b) → transcriptional activation of *IGF1* → circulating IGF-1 (the major source is liver: ~75% of circulating IGF-1). IGF-1 feeds back negatively to suppress both GH (pituitary) and GHRH (hypothalamus), forming a classic endocrine feedback loop. Age-related decline in GH pulsatility → reduced IGF-1 (nadir ~25 years after peak pubescent levels) → contributes to sarcopenia, adiposity, and osteoporosis in aging.

**Three major clinical contexts:**
1. **Acromegaly / gigantism** — GH-secreting pituitary adenoma → excess IGF-1 → skeletal overgrowth, organomegaly (heart, kidneys, tongue), insulin resistance, colon cancer risk; serum IGF-1 (age/sex-adjusted) is the gold-standard screening and monitoring test
2. **Growth hormone deficiency / Laron syndrome** — GH deficiency or GH receptor mutations (Laron syndrome) → low IGF-1 → growth failure, reduced bone density, increased adiposity; recombinant IGF-1 (mecasermin/Increlex) approved for primary IGF-1 deficiency
3. **IGF-1R in disease** — teprotumumab (anti-IGF-1R mAb) transforms outcome in **thyroid eye disease** (Graves ophthalmopathy); IGF-1R overexpression in breast, colon, lung cancers (investigational target)

## Structure

**IGF-1 protein domain organization (70 aa, processed from 153-aa pre-pro-IGF-1):**

**Signal peptide (aa 1–22):** Directs ER secretion; cleaved → Pro-IGF-1 (aa 23–153)
**B domain (aa 1–28 of mature IGF-1):** N-terminal; receptor-binding surface
**A domain (aa 42–62):** Equivalent to insulin A chain; 3 disulfides (A6-A11, A7-B7, A20-B19, using insulin numbering)
**C domain (aa 29–41):** 12-aa connecting peptide (absent in insulin); required for full IGF-1R affinity
**D domain (aa 63–70):** C-terminal extension; not present in insulin; contributes IGFBP binding

The three disulfide bonds (Cys6-Cys48, Cys18-Cys61, Cys47-Cys52 using IGF-1 mature sequence numbering) form the classic insulin-superfamily cystine scaffold.

**Insulin-like growth factor binding proteins (IGFBPs):**
- IGFBP-3 (IGF1BP3, chr7p13): Major circulating carrier; ternary complex IGF-1/IGFBP-3/ALS (acid-labile subunit, IGFALS) → 150 kDa; extends IGF-1 half-life from ~10 min to ~16 hours; GH-dependent expression; low in GH deficiency → low IGF-1 despite normal IGF1 transcription
- IGFBP-1 (liver, kidney): Inhibitory; rises in fasting and insulin deficiency → suppresses IGF-1 action; inversely correlates with insulin levels
- IGFBP-2 (brain, liver): Abundant in CSF; locally delivers IGF-1 to neural tissue
- IGFBP-4, -5, -6: Tissue-specific modulators; some have independent IGF-R-independent actions
- **Proteolysis of IGFBPs** by pregnancy-associated plasma protein A (PAPP-A, PAPPA metalloprotease) → releases free IGF-1 at tissue sites → local IGF-1 activation; PAPP-A is highly expressed in atherosclerotic plaques and predicts cardiovascular events

**IGF-1 receptor (IGF-1R; IGF1R gene, chr15q26.3):**
- Heterotetrameric RTK: (α₂β₂) connected by disulfide bonds; structurally identical to insulin receptor (IR) with 60-70% homology
- **α subunit (extracellular):** IGF-1 binding (Kd ~1 nM for IGF-1; ~100 nM for insulin); also binds IGF-2 (Kd ~10 nM)
- **β subunit (transmembrane + cytoplasmic):** Tyrosine kinase domain; autophosphorylation at Y1131, Y1135, Y1136 (activation loop) → catalytic activation
- **Signal transduction:**
  1. IGF-1 binding → **IRS-1 and IRS-2 Tyr phosphorylation** → PI3K (p85 SH2 binding) → PIP3 → PDK1 → **Akt (Ser473 + Thr308 phosphorylation)**
  2. Akt → **mTORC1** (via TSC1/TSC2/RHEB) → S6K1 + 4EBP1 → ribosomal biogenesis + translation initiation → protein synthesis
  3. Akt → **FOXO1/3 phosphorylation** → nuclear exclusion → repression of MAFbx/Atrogin-1 and MuRF1 transcription → anti-atrophy
  4. IRS-1 → **Grb2/SOS → Ras → Raf → MEK → ERK1/2** → proliferation, survival, differentiation
- **Hybrid receptors:** IGF-1R/IR hemireceptors form in tissues co-expressing both receptors; bind both IGF-1 and insulin; important in cancer

## Function

**Somatic growth:**
- During childhood and puberty: GH → GH pulse amplitude increases → hepatic IGF-1 production → serum IGF-1 peaks (ages 14-17) → long bone epiphyseal growth plate chondrocyte IGF-1R → IRS-1 → PI3K/Akt → chondrocyte proliferation + hypertrophy → longitudinal bone growth
- Laron syndrome (GH receptor mutations): GH is high but IGF-1 is low and growth fails; mecasermin (recombinant IGF-1) partially rescues growth; Laron patients have near-zero cancer rates and remarkable insulin sensitivity — suggesting IGF-1R signaling is a cancer vulnerability

**Skeletal muscle anabolism:**
- Exercise-induced local IGF-1 splice variant (**MGF, mechano-growth factor**): alternative exon inclusion → IGF-1Ec → muscle satellite cell activation → proliferation → fusion into existing fibers → hypertrophy; distinct from liver-derived circulating IGF-1
- Circulating IGF-1 → muscle IGF-1R → IRS-1 → **PI3K → Akt → mTORC1 → S6K1** → increased ribosomal translation of myofibrillar proteins (MHC, actin)
- Akt → **FOXO3a phosphorylation** → cytoplasmic sequestration → suppressed MAFbx and MuRF1 → reduced ubiquitin-proteasome atrophy; this directly antagonizes myostatin/SMAD2/3 pro-atrophy signaling
- Akt also **phosphorylates SMAD3** at non-canonical sites → partial inhibition of SMAD3 transcriptional activity → blunts myostatin downstream effects

**Bone formation:**
- Osteoblasts express IGF-1R at high density; IGF-1 → Akt/mTOR → Type I collagen synthesis, osteocalcin production, alkaline phosphatase activity → bone matrix deposition
- Serum IGF-1 correlates with bone mineral density (BMD) across all age groups; low IGF-1 in anorexia nervosa and GH deficiency → osteoporosis; IGF-1 administration increases BMD in GH-deficient adults
- IGFBPs in bone matrix (especially IGFBP-5) reservoir: PAPP-A cleaves IGFBP-5 locally → releases IGF-1 at bone remodeling sites

**Neuroprotection and neurogenesis:**
- Liver-derived IGF-1 crosses the blood-brain barrier (choroid plexus IGF-1R transport); brain-derived IGF-1 acts locally
- IGF-1 → neuronal IGF-1R → PI3K/Akt → BAD phosphorylation (anti-apoptotic) + BDNF synergy → neuroproliferation in dentate gyrus and olfactory bulb (adult hippocampal neurogenesis)
- Exercise raises circulating IGF-1 → brain → cognitive benefit; IGF-1 trials for ALS and traumatic brain injury (mixed results)

## Mechanism

**Teprotumumab in thyroid eye disease (TED) [^smith-2017-teprotumumab]:**
- Graves ophthalmopathy: TSH receptor antibodies (TRAbs) activate thyroid-stimulating hormone receptor (TSHR) and IGF-1R on orbital fibroblasts and fibrocytes → IL-16, hyaluronan production → orbital fat and muscle inflammation/expansion → proptosis, diplopia, compressive optic neuropathy
- The TSHR-IGF-1R co-activation mechanism: IGF-1R and TSHR form **functional receptor complexes** on orbital fibroblasts; TRAb → TSHR → transactivates IGF-1R → ERK/PI3K → downstream inflammation; this cross-talk explains why anti-IGF-1R works in a "non-IGF-1" disease
- **Teprotumumab (Tepezza):** Humanized anti-IGF-1R IgG1 mAb; blocks IGF-1R ligand binding + receptor signaling; Phase 3 OPTIC trial (2020): **77% reduction in proptosis ≥2 mm** vs. 15% placebo; 83% CAS (Clinical Activity Score) improvement; FDA-approved January 2020 — transformative for TED management (previously only corticosteroids/radiation/surgical decompression)
- Major side effect: hearing loss/tinnitus (IGF-1R on cochlear hair cells?) in 10% of patients; reversible in most cases

**Acromegaly management (IGF-1 as biomarker + therapeutic target):**
- Screening: serum IGF-1 (age/sex-adjusted) — elevated in >95% of active acromegaly
- Surgery (transsphenoidal adenomectomy): cure in ~70% of microadenomas, ~40% of macroadenomas
- Somatostatin analogues (octreotide LAR, lanreotide Autogel): inhibit GH secretion → normalize IGF-1 in ~55-65% of patients
- Pegvisomant (anti-GH receptor antagonist): blocks hepatic GH receptor → reduces IGF-1 to normal in >90%; indicated when SSA-resistant
- Monitoring: serum IGF-1 every 6 months; target age-sex-adjusted normal range

**Biomarkers summary:**
| Condition | IGF-1 level | IGFBP-3 | GH |
|---|---|---|---|
| Acromegaly | ↑↑ | ↑ | ↑ (non-suppressed) |
| GH deficiency | ↓ | ↓ | ↓ |
| Laron syndrome | ↓↓ | ↓ | ↑↑ |
| Pubertal peak | ↑ (age 14-17) | ↑ | ↑ pulsatile |
| Aging (>65 years) | ↓ (50% below peak) | ↓ | ↓ pulsatile amplitude |

## Connections

IGF-1 → IGF-1R → IRS-1 → PI3K/Akt/mTOR → skeletal muscle protein synthesis and satellite cell activation; opposes myostatin/SMAD2/3 atrophy signaling; IGF-1 drives osteoblast bone matrix synthesis; declining IGF-1 with aging contributes to sarcopenia and osteoporosis.

IGF-1 and myostatin exert opposing control over skeletal muscle mass: IGF-1 → Akt → mTORC1 → protein synthesis and satellite cell proliferation; myostatin → SMAD2/3 → MAFbx/MuRF1 → atrophy; Akt directly phosphorylates SMAD3 → partial inactivation of myostatin downstream signaling.

IGF-1 has insulin-like metabolic effects via insulin receptor cross-activation; low serum IGF-1 associates with insulin resistance and T2DM risk; acromegaly (excess GH/IGF-1) causes secondary diabetes; IGF-1 therapy increases insulin sensitivity in severe insulin resistance syndromes.

[^jones-1995-igf-binding-proteins]: Jones JI, Clemmons DR. Insulin-like growth factors and their binding proteins: biological actions. *Endocr Rev.* 1995;16(1):3-34. [doi:10.1210/edrv-16-1-3](https://doi.org/10.1210/edrv-16-1-3) · [PubMed 7758431](https://pubmed.ncbi.nlm.nih.gov/7758431/)
[^smith-2017-teprotumumab]: Smith TJ, Kahaly GJ, Ezra DG, et al. Teprotumumab for thyroid-associated ophthalmopathy. *N Engl J Med.* 2017;376(18):1748-1761. [doi:10.1056/NEJMoa1614949](https://doi.org/10.1056/NEJMoa1614949) · [PubMed 28467880](https://pubmed.ncbi.nlm.nih.gov/28467880/)
