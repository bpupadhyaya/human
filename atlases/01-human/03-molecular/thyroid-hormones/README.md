---
schema: human-scale-entry/v1
id: thyroid-hormones
name: Thyroid Hormones (T3/T4)
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-05
summary: "Iodinated tyrosine-derived hormones: T4 (prohormone, ~90% secreted) and active T3 (~10% secreted + 80% from peripheral deiodination). Nuclear TRα/TRβ receptors drive transcription, ↑BMR, ↑HR, linear growth, and fetal CNS development."
aliases: ["thyroid hormones", "T3", "T4", "thyroxine", "triiodothyronine", "levothyroxine", "liothyronine", "TSH", "TRH", "HPT axis", "thyroid receptor", "TR", "TRα", "TRβ", "DIO1", "DIO2", "hypothyroidism", "hyperthyroidism", "Graves disease", "Hashimoto thyroiditis"]
sources:
  - id: stryer-biochemistry
    type: textbook
    cite: "Berg JM, Tymoczko JL, Stryer L. Biochemistry. 9th ed. W.H. Freeman; 2019."
    url: "https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X"
    accessed: "2026-06-05"
  - id: guyton-hall
    type: textbook
    cite: "Hall JE, Hall ME. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2021."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-05"
  - id: mullur-2014-thyroid-review
    type: peer-reviewed
    cite: "Mullur R, Liu YY, Brent GA. Thyroid hormone regulation of metabolism. Physiol Rev. 2014;94(2):355-82."
    doi: "10.1152/physrev.00030.2013"
    pmid: "24692351"
    url: "https://doi.org/10.1152/physrev.00030.2013"
    accessed: "2026-06-05"
  - id: bianco-2019-deiodination
    type: peer-reviewed
    cite: "Bianco AC, Kim BW. Deiodinases: implications of the local control of thyroid hormone action. J Clin Invest. 2006;116(10):2571-9."
    doi: "10.1172/JCI29812"
    pmid: "17016550"
    url: "https://doi.org/10.1172/JCI29812"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/07-system/cardiovascular-system
    relation: modulates
    note: "T3 drives ↑β-adrenergic receptor density (↑HR, ↑contractility), ↑SERCA2a expression (↑Ca²⁺ cycling), ↑α-MHC (fast ATPase), and ↓PVR. Hyperthyroidism mimics high-adrenergic state (↑CO, AF risk); hypothyroidism causes bradycardia, ↑PVR, pericardial effusion."
  - target: 01-human/07-system/nervous-system
    relation: modulates
    note: "T3 is essential for fetal CNS myelination (TRα1 required in oligodendrocytes); neonatal hypothyroidism → cretinism (irreversible). In adults, T3 regulates serotonin synthesis, synaptic plasticity, and cognition; hypothyroidism is a reversible cause of depression and dementia."
  - target: 01-human/06-organ/thyroid
    relation: expresses
    note: "Follicular thyroid cells synthesize T4 and T3 by iodinating thyroglobulin (TPO-catalysed); stored as colloid and released by lysosomal proteolysis upon TSH stimulation. Thyroid is the sole source of T4; T3 also from peripheral deiodination (DIO1/2) in liver and kidney."
  - target: 01-human/06-organ/liver
    relation: modulates
    note: "The liver converts T4→T3 (DIO1) and clears thyroid hormones (glucuronidation/sulfation). Hepatic TRβ1 regulates LDL-receptor expression, bile acid synthesis (CYP7A1), and lipid metabolism. Selective TRβ agonists (resmetirom/Rezdiffra) approved for NASH/MASH."
---

# Thyroid Hormones (T3/T4)

## Overview

**Thyroid hormones** are iodine-containing amino acid derivatives that serve as master regulators of metabolism, development, and organ function in virtually every cell of the body. They are the only hormones in humans that incorporate a trace element (iodine) as an essential structural and functional component.

**Two active forms:**
- **T4 (thyroxine, 3,5,3',5'-tetraiodothyronine):** The primary secretory product of the thyroid gland (~90% of output); has four iodine atoms; low intrinsic receptor affinity — serves primarily as a **prohormone** (circulating reservoir) for peripheral conversion to T3; long half-life (~7 days)
- **T3 (triiodothyronine, 3,5,3'-triiodothyronine):** The biologically active form; has three iodine atoms; binds thyroid hormone receptors (TRs) with **3–4× higher affinity** than T4; responsible for the vast majority of direct biological effects; shorter half-life (~1 day); ~10% from direct thyroid secretion + ~80% from peripheral deiodination (conversion from T4)
- **Reverse T3 (rT3, 3,3',5'-triiodothyronine):** Produced by DIO3-mediated deiodination of T4 at the 5-position (inner ring) rather than 5'-position; **biologically inactive** (does not activate TR with meaningful affinity); ↑rT3 in severe illness, starvation, fetal life (a mechanism to suppress metabolism during physiological stress)

**Physiological importance:**
- Essential for normal **basal metabolic rate** (↑O₂ consumption, ↑heat production; "calorigenic effect")
- Critical for **fetal brain development** — maternal thyroid hormone crosses the placenta and is the sole source of thyroid hormone for the fetus until ~12 weeks gestation; congenital hypothyroidism (1:2,000-4,000 live births) causes **cretinism** if untreated — irreversible intellectual disability
- **Newborn screening** for TSH (and sometimes T4) is one of the most cost-effective public health programs in history
- Required for **normal growth** — permissive effect on growth hormone and IGF-1 secretion/action
- Modulates **cardiac function, GI motility, skeletal maturation, reproduction, and energy homeostasis**

## Structure

### Thyroid Hormone Biosynthesis

**Thyroglobulin (Tg):** A large homodimeric glycoprotein (~660 kDa; 2× 330 kDa monomers), the scaffold protein for thyroid hormone synthesis. Each Tg monomer contains ~70 tyrosine residues; approximately 25-30 are accessible for iodination, and only a subset (~4-8) are organized at the protein surface in positions compatible for efficient coupling.

**Biosynthesis — 5-step process in thyroid follicular cells:**

1. **Iodide uptake (NIS — sodium-iodide symporter):** The basolateral Na⁺/I⁻ symporter (NIS/SLC5A5) co-transports 2 Na⁺ + 1 I⁻ into the follicular cell, accumulating iodide at ~40× serum concentration (concentrative transport driven by the Na⁺ gradient from Na⁺/K⁺-ATPase). **TSH** strongly upregulates NIS expression. NIS is also the target of radioiodine therapy (¹³¹I): NIS in thyroid cancer cells actively concentrates ¹³¹I → selective irradiation/ablation of thyroid tissue

2. **Tg synthesis and secretion:** Thyroglobulin is synthesized in the RER, glycosylated (N-linked) in the Golgi, and secreted via exocytosis into the **follicular lumen (colloid)** — stored there as an iodine-incorporating scaffold

3. **Iodide oxidation and organification (TPO — thyroid peroxidase):**
   - Pendrin (SLC26A4) transports I⁻ from cytoplasm to apical lumen
   - **Thyroid peroxidase (TPO)** at the apical membrane (facing the colloid) oxidizes I⁻ → I⁰/I⁺ (reactive iodinium ion or enzyme-bound iodo-enzyme intermediate) using H₂O₂ as the oxidant (generated by **DUOX2**, a dual oxidase, using NADPH)
   - TPO catalyzes **organification**: iodination of tyrosine residues on Tg → **MIT** (monoiodotyrosine, at position 3 of the phenyl ring) + **DIT** (diiodotyrosine, at positions 3 and 5)

4. **Oxidative coupling (also TPO-mediated):**
   - TPO catalyzes the **coupling reaction**: two iodinated tyrosyl residues on the same Tg molecule are oxidatively coupled
   - **DIT + DIT → T4** (on Tg) — major reaction; the donor DIT loses its alanine side chain as dehydroalanine
   - **MIT + DIT → T3** (on Tg) — minor reaction in the thyroid (~20% of hormones stored as T3)
   - The resulting iodothyronines remain peptide-linked within the Tg polypeptide

5. **Secretion (endocytosis, proteolysis):**
   - TSH stimulates pinocytosis of colloid → phagolysosomes in follicular cells
   - Lysosomal proteases (cathepsins B, D, L) digest Tg → release T4, T3, MIT, DIT into cytoplasm
   - **T4 and T3** are secreted across the basolateral membrane (via MCT8/OATP1C1 transporters) into the bloodstream
   - **MIT and DIT** are deiodinated by iodotyrosine dehalogenase (DEHAL1) → free tyrosine + I⁻ recycled → highly efficient iodine conservation

**Plasma protein binding:**
- ~99.97% of circulating T4 is protein-bound; only 0.03% is free ("free T4," fT4) — the biologically active fraction
- **Thyroxine-binding globulin (TBG):** ~75% of circulating T4; highest affinity (Kd ~0.1 nM)
- **Transthyretin (TTR/prealbumin):** ~15%
- **Albumin:** ~10%
- Binding proteins serve as a circulating reservoir and buffer, dampening fluctuations in free T4/T3

### Thyroid Hormone Receptors (TR)

Nuclear thyroid hormone receptors are members of the **nuclear receptor superfamily** (subfamily 1, group A):

| Receptor | Gene | Location | Expression |
|:---|:---|:---|:---|
| TRα1 | THRA | 17q11.2 | Heart (dominant), skeletal muscle, brain, bone, GI |
| TRα2 | THRA | 17q11.2 | Widely expressed; does NOT bind T3 (non-functional as TR); acts as endogenous T3 antagonist |
| TRβ1 | THRB | 3p24.2 | Liver, kidney, brain, pituitary |
| TRβ2 | THRB | 3p24.2 | Pituitary (dominant), hypothalamus, retina, cochlea |

**TR domain structure:**
- **N-terminal AF-1 domain:** Ligand-independent transcriptional activation function; varies between isoforms
- **DNA-binding domain (DBD):** Two zinc fingers; recognizes thyroid response elements (TREs) in gene promoters; canonical TRE: AGGTCA half-site; preferred binding as direct repeats with 4-nucleotide spacer (DR4)
- **Ligand-binding domain (LBD):** Binds T3 (Kd ~0.1 nM for T3 vs. ~0.3-1 nM for T4); contains helix 12 (AF-2 helix) which repositions upon T3 binding to form the cofactor interaction surface
- **Hinge domain:** Connects DBD to LBD; contains nuclear localization signal (NLS)

## Function

Thyroid hormones regulate metabolism and development across organ systems: [^mullur-2014-thyroid-review]

| System/Tissue | Hypothyroid effects | Hyperthyroid effects |
|:---|:---|:---|
| Metabolism (BMR) | ↓O₂ consumption, cold intolerance, weight gain | ↑BMR, heat intolerance, weight loss, ↑sweating |
| Heart | Bradycardia, ↓CO, ↑PVR, pericardial effusion | Tachycardia, ↑CO, ↑PP, palpitations, AF |
| CNS | Cognitive slowing, depression, dementia, myxedema coma | Anxiety, restlessness, psychosis, fine tremor |
| GI | Constipation, ↓GI motility | Diarrhea, hyperdefecation |
| Bone/Growth | Growth retardation (in children), ↑bone density | Accelerated bone turnover, osteoporosis |
| Muscle | Weakness, myopathy, ↑CK | Proximal myopathy, ↑reflexes |
| Lipids | ↑LDL-C, ↑cholesterol, ↑TG | ↓LDL-C, ↓cholesterol |
| Skin | Dry, coarse skin, myxedema (GAG deposition) | Warm, moist skin, pretibial myxedema (Graves') |
| Reproductive | Menorrhagia, anovulation, infertility | Oligomenorrhea, ↓fertility |

## Mechanism

### Nuclear Receptor Mechanism: Transcriptional Regulation

The classical T3 mechanism is genomic (nuclear): [^mullur-2014-thyroid-review]

1. **T3 entry into cells:** T3 is transported across plasma membrane by organic anion transporters — primarily **MCT8 (SLC16A2)** and **OATP1C1 (SLCO1C1)**. MCT8 mutations cause **Allan-Herndon-Dudley syndrome** (X-linked, severe intellectual disability + peripheral thyrotoxicosis in affected males) — demonstrating that intracellular T3 transport is non-passive and rate-limiting in neurons

2. **T3 binding to TR-RXR heterodimer on DNA:**
   - Unliganded TR (apo-TR) is bound to **TREs** in the promoters of T3-responsive genes, complexed with **corepressors** (NCoR1, SMRT/NCoR2) → corepressor recruits HDAC3 → chromatin compaction → gene silenced
   - T3 binds to the LBD of TR → helix 12 (AF-2) swings into the closed conformation → repositions to form a coactivator recruitment surface
   - **Corepressors displaced** → **coactivators recruited** (SRC-1/NCoA-1, TRAP220/DRIP205, p300/CBP) → coactivators have HAT (histone acetyltransferase) activity → chromatin remodeling → enhanced RNA Pol II loading → **gene transcription activated**
   - TR preferentially binds as **heterodimer with RXR** (retinoid X receptor) — the TR/RXR heterodimer has higher affinity for DR4 TREs than TR homodimers

3. **Negative TREs (nTREs):**
   - At some gene promoters (TSH α- and β-subunits, TRH), T3/TR/RXR binding *represses* transcription — the molecular basis of HPT axis negative feedback
   - Mechanism of negative regulation involves direct interaction with AP-1 (c-Jun/c-Fos) or other TFs at nTRE, or novel mechanisms specific to the TSH promoter architecture

4. **Non-genomic T3 actions:**
   - Rapid (seconds-to-minutes, too fast for transcription) effects via surface receptor, cytoplasmic TRα, or direct mitochondrial TR
   - ↑PI3K-Akt-mTOR signaling (T3 activates PI3K via direct interaction with p85 regulatory subunit)
   - ↑MAPK/ERK (via integrin αvβ3 surface receptor — the "integrin receptor for thyroid hormone")
   - Rapid ↑cardiac contractility and ↑glucose transporter (GLUT4) translocation via non-genomic pathways

### Peripheral Deiodination: The T4-to-T3 Conversion System

**~80% of circulating T3** is produced by peripheral deiodination of T4, not direct thyroid secretion. This conversion is catalyzed by three **selenocysteine-containing deiodinases** (DIO1, DIO2, DIO3): [^bianco-2019-deiodination]

| Enzyme | Reaction | Location | Regulation |
|:---|:---|:---|:---|
| **DIO1** (5'/5) | T4 → T3 (5'-deiodination; outer ring) AND T4 → rT3 (5-deiodination; inner ring, but minor) | Liver (major), kidney, thyroid | ↑by T3 (positive autoregulation) |
| **DIO2** (5') | T4 → T3 (outer ring; high-affinity) | Brain, pituitary, BAT, heart, skeletal muscle | ↑by T4 and rT3 deprivation (↑when T4 is low); short-lived enzyme (ubiquitylated after substrate) |
| **DIO3** (5) | T4 → rT3 (inner ring); T3 → T2 (inactive) | Placenta, fetal tissues, brain, skin | ↑in fetal life (protects fetus from excess T3); ↑by T3 (negative feedback) |

**Clinical implications:**
- **Critical illness/starvation (low T3 syndrome / sick euthyroid):** ↑DIO3 activity → ↑T4→rT3, ↓T4→T3; DIO1 also reduced; result: ↓T3, ↑rT3, normal or low TSH → an adaptive hypometabolic state; **not hypothyroidism** — treatment with T3/T4 does not improve outcomes (ITU trials negative)
- **DIO2 in the brain:** The brain relies primarily on DIO2 for local T3 production from T4; explains why some patients on LT4 monotherapy feel suboptimal (T3 not restored in brain as efficiently as liver) — rationale for LT4/LT3 combination therapy trials
- **Selenium dependence:** All three deiodinases contain selenocysteine (Sec, 21st amino acid) at their active sites; selenium deficiency → reduced DIO activity → impaired T4→T3 conversion; co-supplementation with selenium in iodine deficiency may worsen outcomes if done without simultaneous iodine repletion

### Hypothalamic-Pituitary-Thyroid (HPT) Axis

The HPT axis is a classical closed-loop negative feedback system:

1. **TRH (thyrotropin-releasing hormone):** Tripeptide (pyroGlu-His-Pro-NH₂) secreted by **parvocellular neurons of the paraventricular nucleus (PVN)** of the hypothalamus into the portal blood → anterior pituitary thyrotrophs → TRH receptor (TRHR, Gq-coupled) → ↑TSH synthesis and secretion

2. **TSH (thyroid-stimulating hormone):** Glycoprotein heterodimer (α-subunit shared with FSH, LH, hCG; β-subunit unique) secreted by anterior pituitary thyrotrophs → TSHR on thyroid follicular cells (Gs-coupled → ↑cAMP → all steps of thyroid hormone synthesis and secretion) → ↑T4/T3 output

3. **Negative feedback by T3:**
   - **Pituitary (TRβ2-mediated):** T3 (local DIO2-generated from T4) binds TRβ2 in thyrotrophs → suppresses TSH α- and β-subunit transcription at nTREs; this is the primary feedback point
   - **Hypothalamic (TRβ2):** T3 in PVN neurons suppresses TRH synthesis

4. **Set-point:** The normal serum TSH range (0.4–4.0 mIU/L) reflects the operating point of this axis; TSH is **exquisitely sensitive** to small changes in free T4/T3 (log-linear relationship: 2-fold change in fT4 → 100-fold change in TSH); this makes TSH the **single best screening test** for thyroid dysfunction

### Clinical Pharmacology

**Levothyroxine (LT4, L-thyroxine):**
- Synthetic T4; first-line treatment for hypothyroidism (Hashimoto's thyroiditis, post-thyroidectomy, post-RAI)
- Taken fasting (30-60 min before food; coffee reduces absorption significantly)
- Half-life ~7 days → once-daily dosing; stable serum levels
- Typical replacement dose: 1.6 µg/kg/day in adults (~100-175 µg/day); adjusted by TSH (target 0.4-2.5 mIU/L for most patients)

**Liothyronine (LT3, synthetic T3):**
- Short half-life (8-12 hours) → less stable levels; used in myxedema coma (IV), some augmentation protocols
- LT4/LT3 combination: advocated by some for patients who feel suboptimal on LT4 alone (2013 ATA guidelines: insufficient evidence; selected patients with persistent symptoms may benefit — active research area)

**Propylthiouracil (PTU) and methimazole (carbimazole):**
- Thionamide antithyroid drugs; inhibit TPO → block organification and coupling → ↓T4/T3 synthesis
- PTU also inhibits DIO1 (peripheral T4→T3 conversion) — preferred in thyroid storm and first trimester pregnancy
- Side effects: agranulocytosis (0.1-0.5%), hepatotoxicity (PTU), ANCA vasculitis (PTU)

**Resmetirom (Rezdiffra — TRβ-selective agonist):**
- First thyroid hormone receptor agonist approved (FDA 2024) — for NASH (non-alcoholic steatohepatitis)/MASH with moderate-to-advanced fibrosis
- Selectively activates hepatic TRβ1 → ↑mitochondrial β-oxidation of fatty acids (↓hepatic TG), ↑bile acid synthesis (CYP7A1), ↓LDL-C — without cardiac or bone effects (which are mediated by TRα)
- Mechanism exploits the TRβ vs. TRα tissue-expression differential

## Connections

- **Modulates** → [Cardiovascular System](../../../../../01-human/07-system/cardiovascular-system/README.md): T3 (via TRα1 in cardiomyocytes) drives ↑β-adrenergic receptor density (↑HR, ↑contractility), ↑SERCA2a expression (↑Ca²⁺ cycling speed), ↑α-MHC (fast-ATPase heavy chain), and systemic vasodilation (↓PVR via ↑eNOS). Hyperthyroidism produces a high-output, high-adrenergic cardiac state with risk of AF; hypothyroidism causes bradycardia, ↑PVR, pericardial effusion, and dyslipidemia.

- **Modulates** → [Nervous System](../../../../../01-human/07-system/nervous-system/README.md): T3 (via TRα1) is essential for fetal oligodendrocyte differentiation and CNS myelination; maternal hypothyroidism or iodine deficiency during pregnancy causes cretinism — irreversible cognitive impairment, deaf-mutism, and spastic diplegia. In adults, T3 regulates serotonin turnover, synaptic density, and neurogenesis; hypothyroidism is a fully reversible cause of depression, cognitive slowing, and reversible dementia.

- **Expresses** → [Thyroid](../../../../../01-human/06-organ/thyroid/README.md): The thyroid follicular cells are the exclusive synthetic source of T4 and the primary (though minor) source of T3 in the body. Follicular cell TSH receptor activation drives NIS-mediated iodide uptake, TPO-catalysed organification/coupling of thyroglobulin, and TSH-stimulated lysosomal proteolysis of stored Tg to release T4/T3 into the bloodstream. The thyroid is the sole organ in the human body capable of concentrating iodine to the degree required for thyroid hormone synthesis.

- **Modulates** → [Liver](../../../../../01-human/06-organ/liver/README.md): The liver is the primary site of DIO1-mediated T4→T3 conversion (contributing ~40-50% of circulating T3) and of thyroid hormone inactivation (glucuronidation/sulfation). Hepatic TRβ1 drives T3-responsive gene programs: ↑LDL receptor (↓LDL-C), ↑CYP7A1 (↑bile acid synthesis/cholesterol catabolism), ↑mitochondrial biogenesis, ↑FAO. Resmetirom's hepatoselectivity exploits the liver's dominant TRβ1 expression to treat MASH.

[^mullur-2014-thyroid-review]: Mullur R, Liu YY, Brent GA. Physiol Rev. 2014;94(2):355-82. doi:10.1152/physrev.00030.2013
[^bianco-2019-deiodination]: Bianco AC, Kim BW. J Clin Invest. 2006;116(10):2571-9. doi:10.1172/JCI29812

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
