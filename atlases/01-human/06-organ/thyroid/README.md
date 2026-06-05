---
schema: human-scale-entry/v1
id: thyroid
name: Thyroid Gland
atlas: 01-human
scale: 06-organ
status: draft
last_reviewed: 2026-06-05
summary: "Bilobed gland (~25 g) at anterior neck. Follicular cells synthesise T4/T3 regulating BMR, cardiac output, CNS myelination, and thermogenesis. C-cells secrete calcitonin (↓Ca²⁺). TRH→TSH→thyroid feedback axis; Hashimoto's and Graves' are common autoimmune disorders."
aliases: ["thyroid", "glandula thyreoidea", "follicular cell", "C cell", "parafollicular cell"]
sources:
  - id: guyton-hall
    type: textbook
    cite: "Hall JE, Hall ME. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2021."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-05"
  - id: stryer-biochemistry
    type: textbook
    cite: "Berg JM, Tymoczko JL, Stryer L. Biochemistry. 9th ed. W.H. Freeman; 2019."
    url: "https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/08-whole-body/human-body
    relation: part-of
    note: "Thyroid secretes T4/T3 (iodothyronine hormones) regulating basal metabolic rate, cardiac output, CNS myelination, bone growth, and thermogenesis; calcitonin from C-cells lowers serum Ca²⁺. Located at anterior neck, 25 g."
  - target: 01-human/07-system/cardiovascular-system
    relation: modulates
    note: "T3 upregulates cardiac HCN4 (↑HR), SERCA2a (↑relaxation speed), α-MHC (↑contractility), and peripheral vasodilatory pathways → ↑CO; hypothyroidism causes bradycardia, effusion, raised cholesterol; hyperthyroidism causes AF."
  - target: 01-human/07-system/nervous-system
    relation: modulates
    note: "T3 is essential for fetal and neonatal brain myelination (MBP, PLP gene induction) and neuronal migration; maternal or congenital hypothyroidism → cretinism; adult thyroid status modulates mood, cognition, and peripheral nerve conduction."
  - target: 01-human/06-organ/liver
    relation: modulates
    note: "Liver converts T4 → T3 via DIO1 (type 1 deiodinase); hepatocytes express TRβ → T3 ↑ hepatic gluconeogenesis, LDL receptor expression (hypothyroidism → ↑LDL), and bile acid synthesis (CYP7A1 induction by T3)."
  - target: 01-human/03-molecular/thyroid-hormones
    relation: expressed-by
    note: "Expressed by Thyroid Hormones (T3/T4)."
---

# Thyroid Gland

## Overview

The thyroid gland is a butterfly-shaped bilobed endocrine organ at the anterior neck, levels C5–T1, weighing approximately 25 g in healthy adults (range 15–30 g) [^guyton-hall]. The two lateral lobes are connected by the isthmus (overlying the 2nd–3rd tracheal rings); a pyramidal lobe (remnant of the thyroglossal duct) is present in ~50% of individuals, projecting superiorly from the isthmus.

The thyroid is unique in two respects: it is the only endocrine organ that stores large quantities of its hormone product extracellularly (as iodinated thyroglobulin in follicular colloid, sufficient for ~100 days supply), and it is the only tissue in the body that actively concentrates inorganic iodide against a >30-fold concentration gradient via the Na⁺/I⁻ symporter (NIS) — a mechanism exploited therapeutically with radioactive iodine (¹³¹I).

The thyroid secretes three hormones:
1. **T4 (thyroxine, L-thyroxine):** the predominant secreted product (~80 μg/day); essentially a prohormone — low intrinsic activity at TR
2. **T3 (triiodothyronine):** secreted in small amounts (~8 μg/day from thyroid); the active hormone at nuclear TRα/TRβ receptors; most circulating T3 (~80%) comes from peripheral T4 → T3 deiodination
3. **Calcitonin:** secreted by parafollicular C-cells; 32-amino acid peptide that lowers plasma Ca²⁺ by inhibiting osteoclast activity and ↑ renal Ca²⁺ excretion

Thyroid disorders are the most prevalent endocrine conditions globally: hypothyroidism affects ~5% of adults (subclinical), hyperthyroidism ~1–2%, thyroid nodules are detectable in ~50% of adults by ultrasound.

## Structure

### Gross Anatomy and Vasculature

The thyroid is encased in a fibrous capsule with internal septae that divide the parenchyma. It is the most vascular organ in the body per unit weight — thyroid blood flow is approximately 5 mL/min/g (compared to ~1 mL/min/g for kidney).

**Arterial supply:**
- Superior thyroid arteries (first branch of external carotid artery, left and right) → superior pole
- Inferior thyroid arteries (from thyrocervical trunk of subclavian artery) → inferior pole
- Thyroid ima artery (single, from aortic arch or brachiocephalic trunk, ~10% of individuals) → isthmus

**Venous drainage:**
Superior and middle thyroid veins → internal jugular vein; inferior thyroid veins → brachiocephalic veins.

**Surgical landmarks:**
- **Recurrent laryngeal nerves (RLN):** Pass in the tracheo-oesophageal groove, entering larynx at inferior cornu of thyroid cartilage; injured during thyroidectomy → hoarseness (unilateral), respiratory distress (bilateral). Right RLN hooks around right subclavian artery; left RLN hooks around ligamentum arteriosum/aortic arch.
- **Parathyroid glands:** 4 small glands (superior and inferior pairs, ~40 mg each) embedded in posterior thyroid capsule; at risk during total thyroidectomy → post-op hypoparathyroidism/hypocalcaemia.
- **Berry's ligament:** Posterior condensation of thyroid capsule anchoring it to cricoid cartilage and trachea; accounts for upward movement of thyroid with swallowing.

### Histology

The fundamental structural and functional unit is the **thyroid follicle** (~3 million per gland, diameter 50–500 μm) [^guyton-hall]:

**Follicle composition:**
- **Follicular lumen (colloid):** Pale eosinophilic homogeneous material; primarily **thyroglobulin** (Tg, 660 kDa homodimer) — the scaffold protein on which iodination and thyroid hormone coupling occur; also contains thyroid peroxidase (TPO) fragments, pendrin, iodide
- **Follicular epithelial cells (thyrocytes, principal cells):** Single monolayer surrounding the colloid; flat (in hypostimulated state) to columnar (in TSH-stimulated/hyperactive state); polarised cells with apical membrane facing colloid lumen and basolateral membrane facing capillaries; contain abundant rough ER (Tg synthesis), prominent Golgi (Tg glycosylation), lysosomes (Tg resorption/proteolysis)
- **Parafollicular C-cells (clear cells):** Located between follicles and their basement membrane, or within follicular wall; larger, polygonal, pale-staining; secrete calcitonin; neural crest origin (unlike follicular cells which are endodermal); C-cells are the cell of origin of medullary thyroid carcinoma

## Function

### Thyroid Hormone Synthesis: Step-by-Step

All steps occur in follicular epithelial cells [^stryer-biochemistry]:

**Step 1 — Iodide Uptake (Trapping):**
Dietary iodide (I⁻) is actively transported across the basolateral membrane of thyrocytes by **NIS (sodium-iodide symporter, SLC5A5)** — cotransports 2 Na⁺ per I⁻, driven by the Na⁺ gradient maintained by Na⁺/K⁺-ATPase. The intracellular iodide concentration exceeds plasma by ~30-fold. TSH → Gs → cAMP → PKA → NIS gene transcription ↑ and NIS insertion into basolateral membrane. Competitive inhibitors: perchlorate (ClO₄⁻), thiocyanate (SCN⁻, in excess cruciferous vegetable consumption), pertechnetate (TcO₄⁻ — used diagnostically in thyroid scans).

**Step 2 — Thyroglobulin (Tg) Synthesis:**
Thyrocytes synthesise Tg (~330 kDa monomer) in RER → glycosylation in Golgi → homodimer (660 kDa) → packaged in vesicles → exocytosis into follicular lumen. Tg contains 2748 amino acids per monomer, with 134 tyrosine residues; only 4–8 are ultimately iodinated to form T4 and T3.

**Step 3 — Iodide Oxidation and Organification (at apical membrane):**
I⁻ transported from cytosol to apical membrane by **pendrin** (SLC26A4, apical Cl⁻/I⁻/HCO₃⁻ exchanger; mutated in Pendred syndrome — sensorineural deafness + goitre). At the apical membrane, **DUOX2** (dual oxidase 2, H₂O₂-generating NADPH oxidase) generates H₂O₂; **thyroid peroxidase (TPO)** uses H₂O₂ to oxidise I⁻ → nascent I⁰/I⁺ species → electrophilic substitution onto tyrosine residues of Tg (organification):
- Tyrosine + I → **MIT** (monoiodotyrosine, 3-iodotyrosine)
- MIT + I → **DIT** (diiodotyrosine, 3,5-diiodotyrosine)

Antithyroid drugs (propylthiouracil, methimazole/carbimazole) inhibit TPO → block organification → rapidly reduce thyroid hormone synthesis.

**Step 4 — Coupling (TPO-catalysed oxidative coupling):**
TPO also catalyses the coupling of iodinated tyrosines within the same Tg molecule:
- DIT + DIT → **T4** (3,5,3′,5′-tetraiodothyronine, thyroxine) + dehydroalanine residue (from donor DIT)
- MIT + DIT → **T3** (3,5,3′-triiodothyronine) + dehydroalanine
Ratio T4:T3 in colloid ≈ 14:1; the remainder is uncoupled MIT and DIT (recovered and recycled).

**Step 5 — Resorption and Secretion:**
TSH stimulation → macropinocytosis of colloid droplets from follicular lumen into thyrocytes → lysosomes fuse with endosomes → **lysosomal proteolysis of Tg** → releases T4, T3, MIT, DIT, amino acids. MIT and DIT deiodinated by **iodotyrosine dehalogenase (DEHAL1/IYD)** → iodide recycled. T4 and T3 secreted across basolateral membrane → bind plasma proteins → circulation.

### T3/T4 Transport and Peripheral Activation

>99% of circulating thyroid hormones are protein-bound [^guyton-hall]:
- **TBG (thyroxine-binding globulin):** 70%; synthesised by liver; ↑ in pregnancy (oestrogen → ↑TBG synthesis → ↑total T4, but free T4 maintained); ↓ in liver failure, nephrotic syndrome (TBG lost in urine)
- **Transthyretin (TTR/prealbumin):** 20%
- **Albumin:** 10% (low affinity, high capacity)

Only **free** hormone (T4 ~0.02%, T3 ~0.2%) is biologically active and enters cells.

**Peripheral conversion (deiodination):**
| Enzyme | Location | Action | Clinical relevance |
|:---|:---|:---|:---|
| DIO1 (type 1) | Liver, kidney, thyroid | T4 → T3 (5′-deiodination, outer ring); also T4 → rT3 | Major source of circulating T3 |
| DIO2 (type 2) | Brain, pituitary, BAT, muscle | T4 → T3 (local, high affinity) | Pituitary T3 sensing; thermogenesis |
| DIO3 (type 3) | Placenta, brain, liver | T4 → rT3; T3 → T2 (inactivation) | Fetal T3 protection; sick euthyroid |

**Sick euthyroid (non-thyroidal illness) syndrome:** During severe illness → ↑DIO3 + ↓DIO1 → ↓T3, ↑rT3, normal or ↓TSH → "low T3 syndrome"; TSH may be suppressed without true hyperthyroidism. Reflects an adaptive response; treatment with exogenous T3/T4 not beneficial in critical illness trials.

### Cellular Mechanism of T3 Action

T3 enters target cells via membrane transporters (**MCT8/SLC16A2** for neurons — MCT8 mutations → Allan-Herndon-Dudley syndrome, severe X-linked intellectual disability from brain T3 deficiency; **OATP1C1/SLCO1C1** in brain, liver) → binds nuclear **thyroid hormone receptors (TR)** — TRα1 (heart, bone, brain), TRβ1 (liver, kidney, pituitary), TRβ2 (pituitary, hypothalamus) [^guyton-hall]:
- Unliganded TR: forms homodimers or RXR heterodimers on TREs; recruits corepressors (NCoR/SMRT) → gene repression
- Liganded TR (T3 bound): conformational change → corepressor release → coactivator recruitment (SRC-1, CBP/p300, TRAP220) → histone acetylation → target gene transcription ↑

**T3 target genes (selected):**
| Gene | Tissue | Effect |
|:---|:---|:---|
| HCN4 (If channel) | Heart | ↑Heart rate (sinus node automaticity) |
| SERCA2a | Heart | ↑Ca²⁺ re-uptake (↑diastolic relaxation, lusitropy) |
| MHC-α (MYH6) ↑ / MHC-β (MYH7) ↓ | Heart | ↑Contractility (α-MHC faster cross-bridge cycling) |
| Na⁺/K⁺-ATPase | All tissues | ↑Metabolic rate (ATP consumption) |
| UCP1 | Brown adipose | ↑Thermogenesis |
| MBP, PLP | Brain | ↑Myelination |
| PEPCK, G6Pase | Liver | ↑Gluconeogenesis |
| LDL receptor | Liver | ↑LDL clearance (hypothyroidism → ↑LDL cholesterol) |
| CYP7A1 | Liver | ↑Bile acid synthesis from cholesterol |
| GH receptor | Liver | ↑IGF-1 (synergistic with GH for bone growth) |
| RANKL | Bone | ↑Bone turnover (excess → osteoporosis) |

### Calcitonin

32-amino acid peptide secreted by parafollicular C-cells in response to hypercalcaemia [^guyton-hall]:
- **Target 1 — Osteoclasts:** calcitonin receptor (CTR, Gs → cAMP → PKA) on osteoclasts → rapid retraction of ruffled border → ↓bone resorption → ↓Ca²⁺ release from bone
- **Target 2 — Kidney:** inhibits tubular Ca²⁺ reabsorption → ↑urinary Ca²⁺ excretion

Physiological role in humans is minor (patients after total thyroidectomy show no significant calcium disorder). However:
- **Pharmacological uses:** Paget disease of bone (↓osteoclast activity), hypercalcaemia of malignancy (acute management), post-menopausal osteoporosis (limited role, replaced by bisphosphonates/denosumab)
- **Tumour marker:** Serum calcitonin ↑ in medullary thyroid carcinoma (MTC) → used for diagnosis, staging, post-operative surveillance, family screening in MEN-2

### Hypothalamic-Pituitary-Thyroid (HPT) Axis

**TRH (thyrotropin-releasing hormone):** Tripeptide (pGlu-His-Pro-NH₂) from paraventricular nucleus (PVN) of hypothalamus → hypophyseal portal blood → anterior pituitary → TRH-R (Gq → IP3/Ca²⁺ → PKC → ERK1/2) on thyrotrophs → TSH secretion; also stimulates prolactin secretion.

**TSH (thyroid-stimulating hormone):** Glycoprotein (28 kDa), α-subunit shared with FSH, LH, hCG; TSH-specific β-subunit → TSH-R on thyroid → Gs → cAMP → PKA → all steps of thyroid hormone synthesis (NIS expression, TPO activity, Tg synthesis, colloid resorption) + thyrocyte proliferation (via Gq/PI3K/Akt). TSH is the most sensitive test of thyroid function (log-linear relationship with free T4).

**Negative feedback:** Free T4 and T3 → TRβ in anterior pituitary thyrotrophs → suppress TSH transcription and TRH receptor sensitivity; T4 converted to T3 by DIO2 in pituitary. Long-loop feedback: also inhibits hypothalamic TRH release.

## Connections

- **Part of:** [Human Body](../../08-whole-body/human-body/README.md) — the thyroid secretes T4/T3 (iodothyronine hormones) that regulate basal metabolic rate, cardiac output, CNS myelination, bone growth, and thermogenesis; the 25 g gland at the anterior neck also secretes calcitonin from C-cells to lower serum Ca²⁺.
- **Modulates:** [Cardiovascular System](../../07-system/cardiovascular-system/README.md) — T3 upregulates cardiac HCN4 (↑heart rate), SERCA2a (↑relaxation speed), α-MHC (↑contractility), and peripheral vasodilatory pathways → ↑cardiac output; hypothyroidism causes bradycardia, pericardial effusion, and raised LDL cholesterol; hyperthyroidism causes atrial fibrillation.
- **Modulates:** [Nervous System](../../07-system/nervous-system/README.md) — T3 is essential for fetal and neonatal brain myelination (MBP, PLP gene induction) and neuronal migration; maternal hypothyroidism or congenital hypothyroidism causes cretinism (irreversible cognitive impairment); adult thyroid status modulates mood, cognition, and peripheral nerve conduction velocity.
- **Modulates:** [Liver](../liver/README.md) — liver converts T4 → T3 via DIO1 (type 1 deiodinase); hepatocytes express TRβ → T3 ↑ hepatic gluconeogenesis, LDL receptor expression (hypothyroidism → ↑LDL; levothyroxine → statin-like LDL lowering), and bile acid synthesis (CYP7A1 induction by T3).

## Pathology

### Hypothyroidism

**Hashimoto Thyroiditis (Chronic Autoimmune Thyroiditis):**
Most common cause of hypothyroidism in iodine-replete countries (~5% prevalence, F:M = 8:1) [^guyton-hall]. HLA-DR3/DR5 associated. T-cell-mediated destruction of thyrocytes + B-cell autoantibodies:
- **Anti-thyroid peroxidase (anti-TPO) antibodies:** >90% of cases; inhibit TPO activity; complement-fixing → cytotoxicity
- **Anti-thyroglobulin (anti-Tg) antibodies:** ~60%
- **Anti-TSH receptor blocking antibodies (TRAb-blocking):** minority, can cause severe neonatal hypothyroidism if maternal

Histology: lymphocytic infiltration with germinal centres, oxyphilic (Hürthle cell) change of thyrocytes, fibrosis. Course: Goitre phase (↑TSH → thyroid enlargement) → subclinical hypothyroidism → overt hypothyroidism → atrophic phase.

**Other causes:** Iodine deficiency (most common cause worldwide — endemic goitre, cretinism); post-partum thyroiditis (transient thyrotoxicosis → hypothyroid → recovery in 12 months; recurs in subsequent pregnancies); subacute (De Quervain) thyroiditis (viral, painful goitre, granulomatous); drug-induced (amiodarone [40% iodine by weight → Wolff-Chaikoff effect + direct cytotoxicity], lithium, interferon-α, checkpoint inhibitors); congenital hypothyroidism (dyshormonogenesis or thyroid dysgenesis — screened at birth, treat immediately to prevent cretinism).

**Symptoms of hypothyroidism:** Cold intolerance, weight gain, constipation, bradycardia, dry skin, hair loss, periorbital myxoedema (glycosaminoglycan deposition), delayed tendon reflexes (classic "hung-up" reflex), depression, cognitive slowing, menorrhagia, hyperlipidaemia, hyponatraemia (↑ADH), pericardial effusion.

**Myxoedema coma:** Life-threatening decompensated hypothyroidism — hypothermia, bradycardia, hypoventilation, hyponatraemia, AMS. Treat: IV T3 (liothyronine) + IV hydrocortisone (adrenal insufficiency coexists in 5–10%) + supportive care.

**Treatment:** Levothyroxine (L-T4) once daily, fasting; target TSH 0.5–2.5 mIU/L. Some patients require addition of liothyronine (L-T3) for residual symptoms.

### Hyperthyroidism

**Graves' Disease:**
Most common cause of hyperthyroidism (~75% in iodine-replete areas; F:M = 7:1) [^guyton-hall]. Autoimmune: **thyroid-stimulating immunoglobulins (TSI) / thyrotropin receptor antibodies (TRAb — stimulating type)** → bind TSH-R → constitutive Gs activation → cAMP → unregulated T4/T3 synthesis regardless of TSH level (TSH suppressed to <0.01). Associated with **HLA-DR3** and **CTLA4** gene polymorphisms.

**Triad (classical):**
1. **Diffuse goitre** (smooth, non-tender; bruit/thrill from ↑vascularity — thyroid bruit on auscultation)
2. **Ophthalmopathy (Graves' orbitopathy):** anti-IGF-1R (insulin-like growth factor 1 receptor) antibodies + TSH-R antibodies on orbital fibroblasts → GAG deposition + T-cell infiltration → periorbital oedema, proptosis (exophthalmos), lid lag, lid retraction, ophthalmoplegia; does not necessarily correlate with thyroid disease severity; treated separately (steroids, orbital decompression, rituximab)
3. **Pretibial myxoedema (dermopathy):** skin thickening/induration over shins; GAG deposition stimulated by TRAb on dermal fibroblasts

**Treatment options:**
- **Antithyroid drugs (ATD):** Propylthiouracil (PTU) — inhibits TPO + inhibits peripheral T4→T3 conversion (DIO1); used in first trimester pregnancy, thyroid storm; risk of agranulocytosis (0.1–0.5%), hepatotoxicity; Methimazole/Carbimazole — inhibits TPO only; preferred for non-pregnant adults; once-daily dosing
- **Radioactive iodine (¹³¹I):** Orally administered; NIS-dependent uptake into thyrocytes → β-radiation → follicular cell destruction → hypothyroidism (intended outcome, then levothyroxine); contraindicated in pregnancy; may worsen Graves' ophthalmopathy
- **Surgery (total or near-total thyroidectomy):** Rapid definitive treatment; risk of RLN injury and hypoparathyroidism; requires pre-operative euthyroidism (ATD + iodine [Lugol's solution to reduce vascularity])
- **Symptom control:** β-blockers (propranolol — ↓HR, tremor, sweating; also inhibits DIO1 → ↓T4→T3; used acutely pending definitive therapy)

**Thyroid Storm:** Life-threatening thyrotoxicosis precipitated by stress (infection, surgery, trauma). High fever, extreme tachycardia, haemodynamic instability, altered consciousness. Treat: PTU → block synthesis + T4→T3 conversion; potassium iodide (Lugol's — acute block of hormone release, Wolff-Chaikoff effect); dexamethasone (block T4→T3 DIO1); propranolol; active cooling; supportive ICU care.

**Other causes of hyperthyroidism:** Toxic multinodular goitre (TSH-R somatic activating mutations in multiple nodules); toxic adenoma (single hot nodule, somatic TSHR or GNAS mutation); iodine-induced (Jod-Basedow; amiodarone); hCG-driven (first trimester pregnancy, gestational thyrotoxicosis, hydatidiform mole — hCG structurally similar to TSH); TSH-secreting pituitary adenoma (rare, non-suppressed TSH with ↑fT4).

### Thyroid Cancer

| Type | Frequency | Cell of origin | Key molecular | Prognosis |
|:---|:---|:---|:---|:---|
| Papillary (PTC) | 80–85% | Follicular cells | BRAF V600E (50%), RET/PTC rearrangements (15%), RAS | Excellent (10-year survival >95% if low-risk) |
| Follicular (FTC) | 10–15% | Follicular cells | PAX8/PPARγ fusion (30%), RAS mutations, PTEN loss | Good (10-year survival ~85%), vascular invasion = poor prognostic feature |
| Medullary (MTC) | 3–5% | C-cells | RET mutation (hereditary: MEN-2A, MEN-2B; somatic in 50% sporadic) | Intermediate; calcitonin as marker; prophylactic thyroidectomy in RET+ family |
| Anaplastic (ATC) | <2% | Follicular cells (dedifferentiated) | BRAF, RAS, TP53, TERT, CDKN2A | Catastrophic (median survival 3–5 months) |

**Papillary thyroid carcinoma:** Histology: ground-glass ("Orphan Annie eye") nuclei, nuclear grooves, intranuclear pseudoinclusions, psammoma bodies; often multifocal; lymph node metastases common but rarely fatal; haematogenous mets (lung, bone) rare. BRAF V600E → MAPK pathway → ↑cell proliferation; targeted by vemurafenib/dabrafenib (BRAF inhibitors) in advanced disease.

**Management:** Total thyroidectomy (for tumours >1 cm) ± central lymph node dissection → post-operative ¹³¹I remnant ablation (for intermediate/high-risk) → TSH-suppressive levothyroxine therapy → surveillance (Tg + anti-Tg antibodies + neck US + whole-body ¹³¹I scan if applicable).

## See Also

- [Human Body](../../08-whole-body/human-body/README.md) — whole-organism context
- [Cardiovascular System](../../07-system/cardiovascular-system/README.md) — thyroid hormone cardiac effects
- [Nervous System](../../07-system/nervous-system/README.md) — T3 and brain myelination, neurodevelopment
- [Liver](../liver/README.md) — peripheral T4→T3 deiodination (DIO1); TRβ target
- [Adrenal Gland](../adrenal-gland/README.md) — co-regulator of metabolic rate and stress; thyroid storm requires steroid coverage
- [Corticosteroids](../../../03-medicine/01-modern/02-respiratory/corticosteroids/README.md) — used in thyroid storm management to block T4→T3 conversion

[^guyton-hall]: Hall JE, Hall ME. *Guyton and Hall Textbook of Medical Physiology.* 14th ed. Elsevier; 2021.
[^stryer-biochemistry]: Berg JM, Tymoczko JL, Stryer L. *Biochemistry.* 9th ed. W.H. Freeman; 2019.
