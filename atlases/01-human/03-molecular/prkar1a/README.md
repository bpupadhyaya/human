---
schema: human-scale-entry/v1
id: prkar1a
name: PRKAR1A
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "PRKAR1A (R1α) is the regulatory subunit 1α of cAMP-dependent PKA that sequesters the catalytic subunit; cAMP → R1α dissociation → PKA active → CREB/StAR/steroidogenesis; germline PRKAR1A LOF → constitutive PKA → PPNAD/Cushing; somatic loss in adrenocortical tumors."
aliases: ["PRKAR1A", "R1alpha", "PKA regulatory subunit", "PRKAR1A Carney complex", "protein kinase A regulatory", "PRKAR1A PPNAD", "PRKAR1A tumor suppressor", "cAMP PKA PRKAR1A", "R1alpha PKA"]
sources:
  - id: kirschner-2000-prkar1a
    type: peer-reviewed
    cite: "Kirschner LS, Carney JA, Pack SD, et al. Mutations of the gene encoding the protein kinase A type I-alpha regulatory subunit in patients with the Carney complex. Nat Genet. 2000;26(1):89-92."
    doi: "10.1038/79238"
    pmid: "10973256"
    url: "https://doi.org/10.1038/79238"
  - id: bertherat-2009-carney
    type: peer-reviewed
    cite: "Bertherat J, Horvath A, Groussin L, et al. Mutations in regulatory subunit type 1A of cyclic adenosine 5'-monophosphate-dependent protein kinase (PRKAR1A): phenotype analysis in 353 patients and 80 different genotypes. J Clin Endocrinol Metab. 2009;94(6):2085-2091."
    doi: "10.1210/jc.2008-2333"
    pmid: "19293268"
    url: "https://doi.org/10.1210/jc.2008-2333"
cross_links:
  - target: 01-human/07-system/carney-complex
    relation: connects-to
    note: "Germline PRKAR1A LOF causes Carney complex via constitutive PKA catalytic activity; PPNAD (adrenocortical Cushing), cardiac myxomas, LCCSCT, melanotic schwannoma, and pituitary GH adenoma; cardiac myxomas are the leading cause of morbidity/mortality in Carney complex."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "PPNAD (primary pigmented nodular adrenocortical disease) in Carney complex causes ACTH-independent Cushing syndrome via bilateral adrenocortical micronodular hyperplasia driven by constitutive PKA; paradoxical cortisol increase with dexamethasone challenge is diagnostic."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: connects-to
    note: "Excess cortisol production from PPNAD in Carney complex activates glucocorticoid receptor (GR/NR3C1) broadly; GR-driven Cushing phenotype: centripetal obesity, hypertension, diabetes, osteoporosis, immunosuppression; bilateral adrenalectomy is curative for PPNAD-Cushing."
  - target: 01-human/07-system/pheochromocytoma-paraganglioma
    relation: connects-to
    note: "PRKAR1A germline mutations rarely cause pheochromocytoma; however PKA pathway (cAMP-PRKAR1A-PRKACA axis) is a key regulatory pathway in pheo/PGL biology; PKA controls HIF-1α-driven pseudohypoxia in SDH-deficient PGL; PRKAR1A-Carney complex pheo overlap is rare."
---

# PRKAR1A

## Overview

**PRKAR1A** (Protein Kinase cAMP-Dependent Type I Regulatory Subunit Alpha) encodes the **R1α regulatory subunit** of the **cAMP-dependent Protein Kinase A (PKA)** holoenzyme. PKA is the principal effector of cAMP signaling and regulates a broad range of cellular processes including steroidogenesis, growth factor responses, metabolic adaptation, and transcription through phosphorylation of CREB (cAMP Response Element-Binding protein) and hundreds of other substrates. In the inactive (basal) state, PRKAR1A forms a **holoenzyme tetramer (R1α₂:Cα₂)** with two catalytic subunits (PRKACA or PRKACB), keeping them inactive. Upon cAMP binding, R1α dissociates and free catalytic subunits phosphorylate their substrates. Germline PRKAR1A pathogenic variants were identified as the primary cause of **Carney complex** by Kirschner et al. in 2000 [^kirschner-2000-prkar1a] [^bertherat-2009-carney].

**PKA holoenzyme and cAMP signaling:**

```
Resting state:
R1α–Cα [inactive tetramer (R1α)₂(Cα)₂]
         ↑
    Adenyl cyclase inactive (no cAMP)

Activated state:
GPCR (e.g., ACTH receptor, β-AR) → Gαs → adenylyl cyclase → cAMP ↑
         ↓
4 cAMP molecules bind (2 per R1α) → allosteric conformational change
         ↓
R1α dissociates from Cα → free Cα active
         ↓
Cα → nucleus → phospho-CREB → gene expression (StAR, CYP11A1, CYP17A1)
Cα → cytoplasm → phospho-targets → metabolic/structural effects

With PRKAR1A LOF:
R1α absent (or truncated/non-functional) → Cα basally free → constitutive PKA
         ↓
Adrenocortical cells: constitutive steroidogenesis → cortisol overproduction
Cardiac fibroblasts: constitutive proliferation → myxoma formation
Sertoli cells: unchecked growth → LCCSCT
```

## Structure

### PRKAR1A protein domains

**Dimerization/docking (D/D) domain (aa 1-45):**
- N-terminal coiled-coil; mediates R1α homodimerization (the tetramer is (R1α)₂:2Cα); also the binding site for A Kinase Anchoring Proteins (AKAPs)
- AKAPs target the PKA holoenzyme to specific subcellular compartments (membranes, centrosome, sarcoplasmic reticulum); PRKAR1A through AKAP interactions controls the spatial specificity of PKA signaling
- Germline deletions including the D/D domain: disrupt AKAP binding → altered subcellular PKA localization

**Inhibitory segment (linker; aa 94-145):**
- Contains a **pseudosubstrate sequence** (RRRGAI in R1α) that mimics a substrate peptide but lacks the serine phosphorylation site → occupies the Cα active site cleft → allosteric inhibition
- The inhibitory segment also controls interdomain dynamics; cAMP binding to cAMP-B domain propagates conformational change that releases the inhibitory segment from Cα
- Pathogenic R1α variants that truncate the linker region may fail to properly inhibit Cα → partial constitutive activation

**cAMP binding domain A (CBD-A; aa 146-260):**
- Binds one cAMP molecule with high affinity (K_d ~20-100 nM); phosphate-binding cassette (PBC) contacts the phosphate moiety of cAMP; adenine ring contacts a hydrophobic pocket
- cAMP binding causes rotation of the C-terminal α-helix, propagating the allosteric signal toward CBD-B

**cAMP binding domain B (CBD-B; aa 261-379):**
- Binds a second cAMP with lower affinity; CBD-B is the primary sensor driving R1α:Cα dissociation (cooperative binding; Hill coefficient ~1.5 for full dissociation)
- The two-site cAMP binding requirement creates a **steep sigmoidal response** to cAMP elevation — a molecular switch

**Germline pathogenic variant spectrum (PRKAR1A in Carney complex):**
- Frameshift (~40%), nonsense (~25%), splice site (~15%): all produce truncated R1α → haploinsufficiency via NMD
- Missense (~15%): predominantly in CBD-A or CBD-B, disrupting cAMP binding → R1α fails to respond to cAMP → cannot dissociate from Cα → this is a dominant negative mechanism (mutant R1α keeps Cα trapped even at high cAMP → PKA not activated in some cells; but cells undergoing LOH of the remaining WT allele → constitutive PKA)
- Large deletions: ~5%; detected by MLPA; contiguous deletions may affect adjacent genes
- **De novo germline variants**: ~30% of Carney complex cases; no family history

## Function

### PKA signaling in adrenocortical cells

In adrenocortical cells, ACTH → MC2R (ACTH receptor, Gs-coupled) → adenylyl cyclase → cAMP → PKA → phospho-CREB → transcription of steroidogenic genes (StAR, CYP11A1, CYP17A1, HSD3B2) → cortisol synthesis. PKA also promotes adrenocortical cell survival and proliferation via phosphorylation of CREB (CCND1 upregulation), and LKB1 (STK11) inactivation (activating p-ACC → fatty acid synthesis).

With PRKAR1A LOF:
- Adrenocortical cells have constitutively active PKA
- Constitutive steroidogenesis: PPNAD develops with autonomously cortisol-secreting micronodules
- Constitutive proliferation: small black pigmented nodules (melanosomes from upregulated melanocortin-related pigmentation)
- ACTH is suppressed by feedback (cortisol excess) → adrenal cortex surrounding the nodules becomes atrophic → distinctive PPNAD pathology (nodules in atrophic cortex)

### PKA in cardiac fibroblasts and myxoma formation

Cardiac myxoma pathogenesis involves:
- PRKAR1A LOH in cardiac mesenchymal progenitor/fibroblast cells → constitutive PKA → CREB-driven IGF1, FGF, VEGF upregulation → myxoma stroma proliferation
- Myxomas contain a loose myxoid matrix (stellate/polygonal cells embedded in an acid mucopolysaccharide ground substance); highly vascular; fragile and friable → embolic risk
- Location: predominantly left atrium (75%, usually arising from the atrial septum); right atrium; rarely valvular or ventricular

### PRKAR1A as a tumor suppressor in other contexts

**Somatic PRKAR1A loss in adrenocortical carcinoma:**
- PRKAR1A LOH detected in ~15-20% of sporadic adrenocortical tumors (adenoma and carcinoma)
- Somatic PRKAR1A mutations: rare; mostly LOH; epigenetic silencing in some ACC
- Constitutive PKA in sporadic ACC may cooperate with IGF2 amplification (the most common driver of ACC) → growth advantage

**PKA-activating PRKACA/B fusions:**
- Liver: PRKACA-DNAJB1 fusion (hepatocellular fibrolamellar carcinoma) → constitutive PKA activity without cAMP requirement — analogous downstream effect to PRKAR1A LOF
- Adrenal: gain-of-function PRKACA somatic mutations (L206R) cause ACTH-independent Cushing syndrome in sporadic cortisol-producing adenomas — same PKA over-activation as PRKAR1A LOF in PPNAD

## Mechanism

### PRKAR1A genotype-phenotype correlation

Analysis of 353 Carney complex patients and 80 genotypes (Bertherat 2009):
- Truncating variants → classic Carney complex (PPNAD + cardiac myxoma + lentiginosis)
- Missense variants in CBD: attenuated phenotype in some families; skin features may predominate
- Large deletions: may include flanking genes (e.g., NDUFAF7); phenotype sometimes includes features beyond Carney complex
- Phenotypic variability within families: same mutation → some carriers with PPNAD only; others with cardiac myxoma; reflects stochastic somatic second-hit LOH timing and location

### Carney complex vs. McCune-Albright syndrome

Both involve constitutive cAMP-PKA signaling but differ in mechanism and inheritance:
| Feature | Carney complex (PRKAR1A) | McCune-Albright (GNAS) |
|---|---|---|
| Mechanism | Regulatory subunit LOF (R1α absent) | GNAS GOF (Gαs cannot hydrolyze GTP) |
| Genetics | Germline; autosomal dominant | Somatic mosaic; postzygotic mutation |
| Inheritance | 50% offspring risk | Not heritable (mosaic) |
| Adrenal | PPNAD (bilateral micronodular) | Bilateral macro/micronodular |
| Thyroid | Adenoma/carcinoma | Hyperthyroidism (autonomy) |
| Skin | Lentigines, blue nevi | Café-au-lait (coast of Maine) |
| Bone | Not characteristic | Polyostotic fibrous dysplasia |

## Connections

- `connects-to` → **[Carney Complex](../../07-system/carney-complex/README.md)** — Germline PRKAR1A LOF causes Carney complex via constitutive PKA catalytic activity; PPNAD (adrenocortical Cushing), cardiac myxomas, LCCSCT, melanotic schwannoma, and pituitary GH adenoma; cardiac myxomas are the leading cause of morbidity/mortality in Carney complex.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — PPNAD (primary pigmented nodular adrenocortical disease) in Carney complex causes ACTH-independent Cushing syndrome via bilateral adrenocortical micronodular hyperplasia driven by constitutive PKA; paradoxical cortisol increase with dexamethasone challenge is diagnostic.
- `connects-to` → **[Glucocorticoid Receptor](../../03-molecular/glucocorticoid-receptor/README.md)** — Excess cortisol production from PPNAD in Carney complex activates glucocorticoid receptor (GR/NR3C1) broadly; GR-driven Cushing phenotype: centripetal obesity, hypertension, diabetes, osteoporosis, immunosuppression; bilateral adrenalectomy is curative for PPNAD-Cushing.
- `connects-to` → **[Pheochromocytoma/Paraganglioma](../../07-system/pheochromocytoma-paraganglioma/README.md)** — PRKAR1A germline mutations rarely cause pheochromocytoma; however PKA pathway (cAMP-PRKAR1A-PRKACA axis) is a key regulatory pathway in pheo/PGL biology; PKA controls HIF-1α-driven pseudohypoxia in SDH-deficient PGL; PRKAR1A-Carney complex pheo overlap is rare.

[^kirschner-2000-prkar1a]: Kirschner LS, Carney JA, Pack SD, et al. Mutations of the gene encoding the protein kinase A type I-alpha regulatory subunit in patients with the Carney complex. *Nat Genet.* 2000;26(1):89-92. [doi:10.1038/79238](https://doi.org/10.1038/79238) · [PubMed 10973256](https://pubmed.ncbi.nlm.nih.gov/10973256/)
[^bertherat-2009-carney]: Bertherat J, Horvath A, Groussin L, et al. Mutations in regulatory subunit type 1A of cyclic adenosine 5'-monophosphate-dependent protein kinase (PRKAR1A): phenotype analysis in 353 patients and 80 different genotypes. *J Clin Endocrinol Metab.* 2009;94(6):2085-2091. [doi:10.1210/jc.2008-2333](https://doi.org/10.1210/jc.2008-2333) · [PubMed 19293268](https://pubmed.ncbi.nlm.nih.gov/19293268/)
