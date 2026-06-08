---
schema: human-scale-entry/v1
id: regulatory-t-cell
name: Regulatory T Cell
atlas: 01-human
scale: 04-cellular
status: draft
last_reviewed: 2026-06-05
summary: "CD4+CD25hiFOXP3+ T lymphocytes; 5–10% of peripheral CD4+ cells. Master regulators of immune tolerance: suppress autoreactive T cells via IL-10, TGF-β, CTLA-4, IL-2 consumption, and adenosine. Loss of FOXP3 causes fatal IPEX autoimmunity syndrome."
aliases: ["Treg", "CD4+CD25+FOXP3+ T cell", "regulatory lymphocyte", "suppressor T cell"]
sources:
  - id: alberts-mol-cell-biology
    type: textbook
    cite: "Alberts B, Johnson A, Lewis J, et al. Molecular Biology of the Cell. 7th ed. W.W. Norton; 2022."
    url: "https://www.ncbi.nlm.nih.gov/books/NBK26880/"
    accessed: "2026-06-05"
  - id: janeway-immunobiology
    type: textbook
    cite: "Murphy K, Weaver C. Janeway's Immunobiology. 9th ed. Garland Science; 2017."
    url: "https://www.garlandscience.com/product/isbn/9780815345053"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/06-organ/thymus
    relation: part-of
    note: "tTregs (thymic Tregs) are selected from CD4+ thymocytes displaying high-affinity self-TCR recognition in the medulla; FOXP3 is induced by AIRE-dependent high-avidity self-antigen presentation + IL-2 + CD28 co-stimulation."
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: "Tregs maintain peripheral tolerance by suppressing autoreactive T cells, limiting effector T cell responses via IL-10/TGF-β/CTLA-4 mechanisms, and promoting resolution of inflammation after pathogen clearance."
  - target: 01-human/04-cellular/t-helper-cell
    relation: modulates
    note: "Tregs suppress CD4+ Th1/Th2/Th17 effector cells via IL-10, TGF-β, IL-2 deprivation (CD25 sponge), CTLA-4 downregulation of co-stimulatory ligands on APCs, and direct cAMP transfer through gap junctions."
  - target: 01-human/04-cellular/b-cell
    relation: modulates
    note: "Follicular regulatory T cells (Tfr, CXCR5+FOXP3+) co-localise with Tfh in germinal centres to limit Ab somatic hypermutation, affinity maturation, and plasma cell output; prevent autoreactive B cell escape."
  - target: 02-pathogen/06-microbiome/bacteroides-fragilis
    relation: modulated-by
    note: "Modulated by Bacteroides fragilis."
  - target: 02-pathogen/06-microbiome/faecalibacterium-prausnitzii
    relation: modulated-by
    note: "Modulated by Faecalibacterium prausnitzii."
  - target: 02-pathogen/06-microbiome/bifidobacterium-longum
    relation: modulated-by
    note: "Modulated by Bifidobacterium longum."
  - target: 03-medicine/03-food/vitamin-d
    relation: modulated-by
    note: "Modulated by Vitamin D (Calciferol)."
  - target: 01-human/03-molecular/il-2
    relation: modulated-by
    note: "IL-2 is essential for Treg development, survival, and FOXP3 maintenance via CD25 (IL-2Rα) → STAT5 phosphorylation; Tregs do not produce IL-2 themselves; low-dose IL-2 (0.5-2 MIU/d SC) selectively expands Tregs in SLE, GVHD, and T1D clinical trials exploiting high CD25 expression."
  - target: 01-human/03-molecular/calcineurin
    relation: modulated-by
    note: "NFAT/calcineurin drives FoxP3 expression in Tregs; CNIs at trough suppress effector T cells more than Tregs, but high-dose CNI reduces FoxP3 and Treg function; NFAT cooperates with FoxP3 at Treg-specific enhancers to maintain suppressive identity."
---

# Regulatory T Cell

## Overview

Regulatory T cells (Tregs) are a specialised subset of CD4+ T lymphocytes defined by constitutive co-expression of CD4, CD25 (IL-2Rα, high affinity), and the master transcription factor FOXP3 (forkhead box P3). They comprise 5–10% of peripheral CD4+ T cells in humans and are the central cellular mechanisms of immunological self-tolerance.[^janeway-immunobiology] Tregs are not simply suppressive bystanders: they actively monitor and restrain immune responses through a diverse toolkit of contact-dependent and contact-independent mechanisms, maintaining the delicate balance between protective immunity and destructive autoimmunity.

The fundamental importance of Tregs was established by the Scurfy mouse (Foxp3 frameshift mutation → fatal systemic autoimmunity) and by the human disease IPEX syndrome (Immunodysregulation Polyendocrinopathy Enteropathy X-linked), caused by loss-of-function mutations in FOXP3, resulting in neonatal polyendocrinopathy, enteropathy, and death.[^alberts-mol-cell-biology] Tregs suppress responses to self-antigens, food antigens, commensal microbiota, and alloantigens, but their excess in tumours and chronic infections can be harmful by limiting protective immunity. This dual role makes Tregs important targets in both autoimmune disease (enhancement) and cancer immunotherapy (depletion).[^janeway-immunobiology]

## Structure

**Surface markers.** The canonical human Treg phenotype: CD4+CD25hiCD127lowFOXP3+. Additional markers:
- **CD25** (IL-2Rα): constitutively expressed at high levels; forms the high-affinity trimeric IL-2 receptor (CD25+CD122+CD132) with ~100-fold higher IL-2 affinity than dimeric IL-2R on conventional T cells; enables IL-2 "sink" function.
- **CD127low** (IL-7Rα): inverse correlation with FOXP3; useful clinical surrogate for FOXP3 (FOXP3 is intranuclear, not detectable by surface staining without permeabilisation).
- **CTLA-4** (CD152): constitutively expressed (vs inducible on conventional T cells); key effector molecule; higher CD80/CD86 avidity than CD28 (Kd ~0.4 µM vs 4 µM) → trans-endocytosis of CD80/86 from APCs.
- **GITR** (TNFRSF18, glucocorticoid-induced TNFR): constitutively expressed; GITR agonism can overcome Treg suppression (exploited in anti-tumour therapy).
- **CD39/NTPDase1**: ecto-5'-nucleotidase; converts extracellular ATP/ADP → AMP.
- **CD73**: converts AMP → adenosine; pairs with CD39 in adenosine pathway.
- **Helios** (IKZF2): transcription factor marking tTregs (thymic-origin) vs peripherally induced pTregs (Helios−).
- **CCR4, CCR6, CXCR3, CXCR5**: homing receptors directing tissue-specific Treg subsets (CCR4+CCR6− → Th2-suppressing; CXCR5+ → follicular Tregs/Tfr; CXCR3+ → Th1-suppressing Tregs).[^alberts-mol-cell-biology]

**FOXP3 protein.** 431-amino acid forkhead family transcription factor; dimerises via leucine zipper; forkhead domain binds FOXP3-binding elements (FKHREs) in promoters; FOXP3 represses IL-2 (by sequestering NFAT and AP-1), IFN-γ, IL-4, and IL-17 gene loci; FOXP3 directly induces CD25, CTLA-4, and Helios.[^janeway-immunobiology]

## Function

**Suppression mechanisms.** Tregs deploy multiple, context-dependent suppressive modalities:

**1. Inhibitory cytokines:**
- *IL-10*: anti-inflammatory cytokine; binds IL-10R on DCs → STAT3 → blocks DC maturation (↓CD80/CD86, ↓MHC-II upregulation), inhibits macrophage pro-inflammatory cytokine production (TNF-α, IL-12), directly suppresses effector T cell proliferation. Critical in gut mucosal tolerance.
- *TGF-β*: pleiotropic cytokine; suppresses Teff proliferation and cytokine production (IFN-γ, IL-17); promotes naïve CD4+ → pTreg conversion (with IL-2 + retinoic acid in gut); drives B cell IgA class switching; promotes fibrosis at high concentrations.
- *IL-35*: IL-12 family member (IL-12α/EBI3 heterodimer); secreted by Tregs and regulatory B cells; suppresses Th1 and Th17 responses; can induce "infectious tolerance" by converting target T cells to a Tr35 (IL-35-producing) suppressive phenotype.[^alberts-mol-cell-biology]

**2. CTLA-4/co-stimulation blockade:** Constitutive CTLA-4 on Tregs outcompetes CD28 on effector T cells for DC-expressed CD80/CD86. Mechanistically: CTLA-4 captures and internalises CD80/CD86 from APC surface via trans-endocytosis (LRBA-dependent vesicular trafficking). This depletes co-stimulatory ligands from the APC surface, impairing CD28 signalling in neighbouring Teff cells. Abatacept (CTLA-4-Ig) mimics this mechanism therapeutically in RA and transplantation.[^janeway-immunobiology]

**3. IL-2 deprivation (metabolic suppression):** Tregs express the high-affinity IL-2 receptor and thus efficiently consume IL-2 from the local microenvironment, effectively starving conventional T cells of this essential survival/proliferation cytokine. This creates an "IL-2 sink" effect — particularly effective in lymph nodes and tumour microenvironments where IL-2 is limiting.[^alberts-mol-cell-biology]

**4. Cyclic AMP (cAMP) transfer:** Tregs contain high intracellular cAMP levels (via adenylyl cyclase activation downstream of A2A receptor signalling); cAMP can be directly transferred to effector T cells through gap junctions (connexin-43 channels) → PKA type I → phosphorylation of CBP → ↓IL-2 transcription + ↑ICER (inducible cAMP early repressor) → Teff suppression.[^janeway-immunobiology]

**5. Adenosine pathway:** CD39 (ENTPD1) on Tregs hydrolyses pro-inflammatory extracellular ATP (and ADP) → AMP; CD73 converts AMP → adenosine; adenosine binds A2A receptor (ADORA2A) on T cells, NK cells, and DCs → Gαs → ↑cAMP → suppression of TCR signalling, cytotoxicity, and cytokine production. Adenosine also binds A2A on tumour cells promoting growth.[^alberts-mol-cell-biology]

**6. Granzyme B-mediated killing:** Tregs express granzyme B (and granzyme A) and can directly kill target cells — DCs, effector T cells, NK cells — in a perforin-independent manner (granzyme B uptake via M6P receptor or in a contact-dependent perforin-independent mechanism). This mechanism is particularly relevant in the tumour microenvironment.[^janeway-immunobiology]

**7. TIM-1 (membrane interaction):** Direct cell-cell contact via TIM-1 on Tregs and TIM-4 on APCs can mediate suppressive signalling independent of soluble factors.

## Lifecycle

**Thymic Treg development (tTreg).** In the thymus, a subset of DP or SP CD4+ thymocytes with TCRs bearing particularly high affinity for self-peptide:MHC-II complexes (above the threshold for negative selection) are diverted into the Treg lineage. Key signals: (1) TCR:self-pMHC-II — higher avidity than positive selection threshold; (2) CD28 co-stimulation from cDCs and mTECs; (3) IL-2 and IL-15 signals via CD25/CD122; (4) FOXP3 induction (via TCR→NFAT→FOXP3 promoter axis, and epigenetic demethylation of the CNS2 conserved non-coding sequence in the FOXP3 locus — Treg-specific demethylated region, TSDR). AIRE expression by mTECs ensures exposure to diverse tissue-restricted antigens during thymic Treg selection. Helios (IKZF2) marks thymic-origin Tregs. tTregs have a stable, demethylated CNS2 → stable FOXP3 expression even in inflammatory conditions.[^alberts-mol-cell-biology]

**Peripheral Treg induction (pTreg).** Naïve peripheral CD4+ T cells can be converted to FOXP3+ Tregs under tolerogenic conditions: TGF-β + IL-2 → Smad2/3 + NFAT → FOXP3 induction; retinoic acid (RA, produced by gut CD103+ cDC2s from dietary vitamin A via ALDH1A1/2) synergises with TGF-β and suppresses RORγt → pTreg conversion in the intestinal lamina propria. Gut pTregs express RORγt (FOXP3+RORγt+), adapting to the microbial-rich environment and enforcing tolerance to commensal bacteria and dietary antigens.[^janeway-immunobiology]

**Stability and plasticity.** FOXP3 expression is maintained by epigenetic mechanisms: CNS2 demethylation (stable Tregs) vs methylation (plastic Tregs, prone to FOXP3 loss under inflammation). Inflammatory cytokines IL-6, IL-1β, and TNF-α can downregulate FOXP3 and reprogram Tregs into Th17-like cells (inflammatory Tregs, exTregs); this plasticity may contribute to autoimmune disease flares. Conversely, TNF:TNFR2 signalling on Tregs expands them in inflammatory settings.[^alberts-mol-cell-biology]

**Peripheral homeostasis.** Peripheral Treg numbers are maintained by: IL-2 produced by activated conventional T cells (self-limiting homeostatic loop); TNFR2 signalling (TNF expands Tregs at inflammatory sites — a potential tolerance mechanism); antigen stimulation through self-pMHC-II restimulation in lymph nodes and tissues.[^janeway-immunobiology]

## Connections

- **Part of Thymus** (`../../06-organ/thymus/README.md`): tTregs (thymic Tregs) are selected from CD4+ thymocytes displaying high-affinity self-TCR recognition in the medulla; FOXP3 is induced by AIRE-dependent high-avidity self-antigen presentation + IL-2 + CD28 co-stimulation.[^alberts-mol-cell-biology]
- **Modulates Immune System** (`../../07-system/immune-system/README.md`): Tregs maintain peripheral tolerance by suppressing autoreactive T cells, limiting effector T cell responses via IL-10/TGF-β/CTLA-4 mechanisms, and promoting resolution of inflammation after pathogen clearance.[^janeway-immunobiology]
- **Modulates T Helper Cell** (`../t-helper-cell/README.md`): Tregs suppress CD4+ Th1/Th2/Th17 effector cells via IL-10, TGF-β, IL-2 deprivation (CD25 sponge), CTLA-4 downregulation of co-stimulatory ligands on APCs, and direct cAMP transfer through gap junctions.[^alberts-mol-cell-biology]
- **Modulates B Cell** (`../b-cell/README.md`): Follicular regulatory T cells (Tfr, CXCR5+FOXP3+) co-localise with Tfh in germinal centres to limit Ab somatic hypermutation, affinity maturation, and plasma cell output; prevent autoreactive B cell escape.[^janeway-immunobiology]
- `modulated-by` → **[IL-2](../../03-molecular/il-2/README.md)** — IL-2 is essential for Treg development, survival, and FOXP3 maintenance via CD25 (high on Tregs) → STAT5 phosphorylation; low-dose IL-2 (0.5–2 MIU/d SC) selectively expands Tregs in SLE, GVHD, and T1D clinical trials.
- `modulated-by` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — NFAT/calcineurin drives FoxP3 expression in Tregs; CNIs at trough suppress effector T cells more than Tregs, but high-dose CNI reduces FoxP3 and Treg function; NFAT cooperates with FoxP3 at Treg-specific enhancers.

## Pathology

**IPEX syndrome** (Immunodysregulation Polyendocrinopathy Enteropathy X-linked). X-linked recessive loss-of-function mutations in FOXP3 (Xp11.23) → absent tTreg development → neonatal multi-organ autoimmunity: type 1 diabetes mellitus, autoimmune thyroiditis, severe eczema, life-threatening enteropathy (villous atrophy, diarrhoea), cytopenias. Without haematopoietic stem cell transplant (HSCT), most patients die in infancy. HSCT (if HLA-matched sibling available) is curative. Rapamycin (mTOR inhibitor) + immunosuppressants bridge to HSCT.[^alberts-mol-cell-biology]

**CTLA-4 haploinsufficiency** (CTLA4 mutations). Autosomal dominant; insufficient CTLA-4 → impaired Treg suppression → lymphocytic infiltration of lungs, CNS, GI tract; autoimmune cytopenias; resembles IPEX-like syndrome but milder. Treat with abatacept (CTLA-4-Ig) — replaces CTLA-4 function.[^janeway-immunobiology]

**CD25 deficiency.** Rare; FOXP3 cannot be maintained without IL-2:CD25 signalling → autoimmunity, lymphadenopathy, Th1/Th2 dysregulation.[^alberts-mol-cell-biology]

**Autoimmune diseases.** Treg dysfunction is documented in: Type 1 diabetes (↓Treg numbers and function in pancreatic lymph nodes); Multiple sclerosis (Tregs fail to suppress myelin-reactive Th17 in CNS lesions); Rheumatoid arthritis (Tregs present in joints but functionally impaired by TNF-α); Inflammatory bowel disease (colonic Treg FOXP3 instability under bacterial dysbiosis). Restoring Treg function with low-dose IL-2 therapy (expanding Tregs preferentially) is in clinical trials for T1DM, SLE, IBD, and GVHD.[^janeway-immunobiology]

**Cancer immune evasion.** Tumour-infiltrating Tregs are recruited by CCL17/CCL22 (from tumour cells/MDSCs, binding Treg CCR4) and CXCL13 (in breast cancer, lymphoma). High Treg:CTL ratios in tumour microenvironments correlate with poor prognosis in ovarian cancer, colorectal cancer, lung adenocarcinoma. CTLA-4 blockade (ipilimumab) depletes tumour-infiltrating Tregs (via ADCC by NK cells/macrophages expressing FcγRIII — Tregs are the dominant CTLA-4-expressing cells in tumours) and reinvigorates CTL responses.[^alberts-mol-cell-biology]

**Graft-versus-host disease (GVHD).** Donor Tregs suppress alloreactive donor T cells after HSCT; Treg depletion or dysfunction → acute GVHD (liver, gut, skin); adoptive infusion of donor Tregs (ex-vivo-expanded CD4+CD25+CD127low Tregs) is a clinical strategy to prevent GVHD without impairing graft-versus-leukaemia (GVL) effect.[^janeway-immunobiology]

## See Also

- [`../../06-organ/thymus/README.md`](../../06-organ/thymus/README.md) — thymic Treg selection and AIRE-mediated tolerance
- [`../../07-system/immune-system/README.md`](../../07-system/immune-system/README.md) — immune tolerance and self/non-self discrimination
- [`../t-helper-cell/README.md`](../t-helper-cell/README.md) — primary target of Treg suppression; Tfh vs Tfr balance
- [`../t-cytotoxic-cell/README.md`](../t-cytotoxic-cell/README.md) — CTLs suppressed by Tregs in tumours; checkpoint blockade
- [`../b-cell/README.md`](../b-cell/README.md) — Tfr:Tfh regulation of germinal centre B cells
- [`../dendritic-cell/README.md`](../dendritic-cell/README.md) — DCs as Treg suppressors (CTLA-4 trans-endocytosis) and Treg inducers (tolerogenic DCs)
- [`../../03-molecular/il-6/README.md`](../../03-molecular/il-6/README.md) — IL-6 drives Treg→Th17 plasticity and destabilises FOXP3
- [`../../03-molecular/cortisol/README.md`](../../03-molecular/cortisol/README.md) — glucocorticoids upregulate FOXP3 and expand Tregs; basis of steroid immunosuppression
