---
schema: human-scale-entry/v1
id: thymus
name: Thymus
atlas: 01-human
scale: 06-organ
status: draft
last_reviewed: 2026-06-05
summary: "Primary lymphoid organ in the mediastinum. Site of T lymphocyte maturation: bone-marrow-derived progenitors undergo positive selection (MHC restriction) in the cortex, negative selection (self-tolerance) in the medulla. Involutes after puberty; ~70% reduction by age 45."
aliases: ["thymic gland", "glandula thymus"]
sources:
  - id: boehm-2012-thymus-review
    type: peer-reviewed
    cite: "Boehm T, Swann JB. Thymus involution and regeneration: two sides of the same coin? Nat Rev Immunol. 2013;13(11):831-838."
    doi: "10.1038/nri3534"
    pmid: "24052146"
    url: "https://doi.org/10.1038/nri3534"
  - id: klein-2014-thymic-selection
    type: peer-reviewed
    cite: "Klein L, Kyewski B, Allen PM, Hogquist KA. Positive and negative selection of the T cell repertoire: what thymocytes see (and don't see). Nat Rev Immunol. 2014;14(6):377-391."
    doi: "10.1038/nri3667"
    pmid: "24830344"
    url: "https://doi.org/10.1038/nri3667"
  - id: anderson-2002-aire
    type: peer-reviewed
    cite: "Anderson MS, Venanzi ES, Klein L, et al. Projection of an immunological self shadow within the thymus by the Aire protein. Science. 2002;298(5597):1395-1401."
    doi: "10.1126/science.1075958"
    pmid: "12376594"
    url: "https://doi.org/10.1126/science.1075958"
  - id: lynch-2009-thymic-involution
    type: peer-reviewed
    cite: "Lynch HE, Goldberg GL, Chidgey A, Van den Brink MR, Boyd R, Sempowski GD. Thymic involution and immune reconstitution. Trends Immunol. 2009;30(7):366-373."
    doi: "10.1016/j.it.2009.04.003"
    pmid: "19540807"
    url: "https://doi.org/10.1016/j.it.2009.04.010"
  - id: digeorge-1965
    type: peer-reviewed
    cite: "Markert ML, Hummell DS, Rosenblatt HM, et al. Complete DiGeorge syndrome: persistence of profound immunodeficiency. J Pediatr. 1998;132(1):15-21."
    doi: "10.1016/S0022-3476(98)70478-0"
    pmid: "9469993"
    url: "https://doi.org/10.1016/S0022-3476(98)70478-0"
  - id: bhatt-2013-thymic-tumours
    type: peer-reviewed
    cite: "Bhatt VR, Bhatt SS, Limbu K, Silberstein PT. Management of thymoma and thymic carcinoma. J Oncol Pract. 2015;11(4):297-299."
    doi: "10.1200/JOP.2014.003434"
    pmid: "25667274"
    url: "https://doi.org/10.1200/JOP.2014.003434"
cross_links:
  - target: 01-human/04-cellular/t-helper-cell
    relation: contains
    note: "CD4⁺ T helper cells undergo positive selection on MHC class II in the thymic cortex and negative selection in the medulla; exported as naive CD4⁺ T cells to the periphery."
  - target: 01-human/04-cellular/dendritic-cell
    relation: contains
    note: "Thymic DCs present self-antigens to developing T cells in the medulla, deleting autoreactive thymocytes; medullary thymic epithelial cells expressing AIRE provide peripheral self-antigens for central tolerance."
  - target: 01-human/07-system/immune-system
    relation: part-of
    note: "The thymus is the primary lymphoid organ that generates the entire peripheral T cell repertoire; without thymic education, adaptive cellular immunity fails — as in DiGeorge syndrome (22q11 deletion)."
  - target: 01-human/08-whole-body/human-body
    relation: part-of
    note: "The thymus is a bilobed organ in the anterior superior mediastinum; largest at puberty (~40 g), it involutes progressively and is replaced by fat, but retains residual T cell output throughout life."
  - target: 01-human/07-system/lymphatic-system
    relation: part-of
    note: "Part Of by Lymphatic System."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: composed-of
    note: "Composed Of by Cytotoxic T Cell."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: composed-of
    note: "Composed Of by Regulatory T Cell."
taxonomy:
  uberon: "UBERON:0002370"
  fma: "FMA:9607"
---

# Thymus

## Overview

The thymus is the primary lymphoid organ responsible for generating a functional, self-tolerant T lymphocyte repertoire. Unlike secondary lymphoid organs (lymph nodes, spleen, Peyer's patches) that respond to foreign antigens, the thymus functions as an educational institution — it does not respond to pathogens but rather shapes the repertoire of T cells that will do so. Without thymic function, adaptive cellular immunity is absent; the T-cell-mediated defect in DiGeorge syndrome and congenital athymia illustrates that no peripheral organ can substitute for thymic education [^digeorge-1965].

Located in the anterior superior mediastinum, the thymus is largest relative to body size in the foetus and neonate — at birth it weighs ~12–15 g, expanding to a peak of ~30–40 g at puberty. After puberty it undergoes **thymic involution**: fatty replacement of lymphoid tissue with a ~70% reduction in volume by age 45, declining further with age [^boehm-2012-thymus-review]. Critically, involution does not mean complete cessation — even in the elderly, residual thymic epithelial tissue maintains measurable naive T cell output (quantified by T cell receptor excision circles, TRECs), which is important for immune reconstitution after haematopoietic stem cell transplantation, chemotherapy, or HIV-induced T cell depletion.

The thymus is also an endocrine gland, secreting thymulin (zinc-dependent), thymopoietin, thymosin α1, and thymosin β4 — peptides that promote T cell differentiation and migration, and which have been investigated as immunomodulatory agents in immunodeficiency and cancer.

## Structure

### Gross Anatomy

The thymus is a bilobed organ. The two lobes are partially fused at the midline and lie anterior to the pericardium and great vessels, posterior to the manubrium sterni, extending from the level of the fourth costal cartilage superiorly to the lower margin of the thyroid inferiorly in some individuals ("cervical thymus"). Each lobe is enclosed in a thin connective tissue capsule; septa derived from the capsule divide each lobe into irregular lobules of 0.5–2 mm.

Blood supply: superior thymic arteries (branches of the internal thoracic artery and branches from the inferior thyroid artery). Venous drainage: thymic veins → left brachiocephalic vein. Lymphatic drainage: to anterior mediastinal and paratracheal lymph nodes. The thymus has no afferent lymphatics — it is not a filter for lymph but recruits its precursors from the blood via specialised postcapillary venules at the corticomedullary junction.

### Microscopic Structure

Each lobule has two histologically distinct zones [^klein-2014-thymic-selection]:

**Cortex (outer, densely cellular):**
- Densely packed with immature thymocytes (**double-negative** DN → **double-positive** DP)
- **Cortical thymic epithelial cells (cTECs):** unique stellate cells expressing MHCI and MHCII, plus cathepsin L and thymoproteasome (β5t subunit) for generating peptide ligands optimised for positive selection. TCR + cTEC-MHCI/II interaction with intermediate affinity → **positive selection**: thymocyte survives. Too-weak (no signal) → death by neglect. Too-strong (high affinity for self) in the cortex is rare; robust deletion occurs in the medulla.
- **Macrophages:** phagocytose apoptotic thymocytes (~95% of all thymocytes die before export).
- **Blood-thymus barrier:** formed by continuous blood vessel endothelium + pericytes + perivascular connective tissue + cTEC cytoplasmic extensions — prevents random antigen entry into the cortex, ensuring naïve T cells encounter only defined self-peptide/MHC ligands during education.

**Medulla (inner, less dense, pale):**
- Mature (**single-positive** SP) thymocytes undergoing negative selection and Treg generation
- **Medullary thymic epithelial cells (mTECs):** subset expressing **AIRE** (autoimmune regulator) — a transcription factor that drives "promiscuous" expression of thousands of peripheral tissue-restricted antigens (TRAs: insulin, thyroglobulin, CRP, S-antigen from retina, etc.) in the thymic medulla. This is the molecular basis of central tolerance [^anderson-2002-aire].
- **Dendritic cells (DCs):** plasmacytoid and conventional (cDC1 and cDC2) DCs in the medulla also present self-antigens; DC-mediated negative selection deletes SP thymocytes with high-affinity TCRs for self-peptide/MHC.
- **Hassall's corpuscles:** concentric whorls of terminally differentiated mTECs; produce TSLP that promotes dendritic cell-mediated Treg induction.

**Corticomedullary junction (CMJ):** site of T cell precursor entry (from blood, via PSGL-1/CCR7-mediated homing to post-capillary venules) and of mature SP thymocyte export (via S1PR1-dependent egress into the bloodstream).

### Thymocyte Developmental Stages

| Stage | Surface markers | Location | Selection event |
|:---|:---|:---|:---|
| Early T lineage progenitor (ETP) | CD44⁺CD25⁻CD117⁺ | Subcapsular cortex | None — commits to T lineage |
| DN1 → DN4 | CD4⁻CD8⁻ | Cortex (subcapsular→deeper) | TCRβ rearrangement; β-selection (pre-TCR checkpoint) |
| DP (double positive) | CD4⁺CD8⁺ | Cortex | Positive selection on cTECs |
| SP CD4⁺ or SP CD8⁺ | CD4⁺CD8⁻ or CD4⁻CD8⁺ | Medulla | Negative selection; Treg differentiation |
| Mature naive T cell | CD4⁺CD8⁻CD45RA⁺CCR7⁺ or CD8⁺CD45RA⁺CCR7⁺ | Egress via CMJ | — |

## Function

### Positive Selection

After successful TCRαβ rearrangement, DP thymocytes must demonstrate that their TCR can bind self-peptide/MHC with at least minimal affinity ("useful" TCRs rescue cells from death by neglect). ~5% of DP thymocytes are positively selected. TCR affinity for MHC class II → survival as CD4 SP; affinity for MHC class I → survival as CD8 SP. cTECs are the exclusive selecting cell type for positive selection — mice lacking cTECs produce no T cells.

The thymoproteasome (containing β5t subunit, expressed only in cTECs) generates a unique peptide repertoire with lower average affinity that biases the selected TCR pool toward weak–intermediate self-affinity, optimising future foreign antigen responsiveness [^klein-2014-thymic-selection].

### Negative Selection and Central Tolerance

In the medulla, SP thymocytes encountering self-peptide/MHC with high affinity (≥threshold) receive apoptotic signals (Bim-dependent mitochondrial pathway), preventing export of potentially autoreactive T cells. mTECs expressing AIRE transcribe >10,000 TRAs not normally expressed elsewhere in the body, including insulin (encoded by *Ins1/Ins2*; humans: *INS*), thyroglobulin, retinal S-antigen, and salivary amylase [^anderson-2002-aire]. Failure of AIRE → autoimmune polyendocrinopathy-candidiasis-ectodermal dystrophy (APECED/APS-1).

### Regulatory T Cell Generation

~5% of thymocytes with high-affinity TCRs that recognise self-antigen are diverted into the Treg fate (FoxP3⁺ CD25⁺ CD4⁺) rather than deleted — a second mechanism preventing autoimmunity. Thymus-derived Tregs (tTregs) are essential for peripheral tolerance; IPEX syndrome (FOXP3 mutation) causes fatal multi-organ autoimmunity due to absence of Tregs.

### Thymic Output and Reconstitution

The thymus exports ~10⁶–10⁷ naive T cells/day in young adults. After cytotoxic conditioning (bone marrow transplant preparative regimens, HIV), thymic output is the rate-limiting step for immune reconstitution. Thymic involution with age progressively reduces naive T cell output, contributing to immunosenescence — the age-associated narrowing of the T cell repertoire and reduced vaccine responsiveness. Strategies to rejuvenate thymic function (IL-7, KGF/palifermin, sex-steroid ablation, FGF7, IL-22) are under clinical investigation [^boehm-2012-thymus-review].

## Connections

- **Contains → [T Helper Cell](../../04-cellular/t-helper-cell/README.md):** CD4⁺ SP T cells undergo both selection events in the thymus before peripheral export.
- **Contains → [Dendritic Cell](../../04-cellular/dendritic-cell/README.md):** thymic DCs execute negative selection in the medulla alongside mTECs.
- **Part of → [Immune System](../../07-system/immune-system/README.md):** without the thymus, adaptive T cell immunity does not develop.
- **Part of → [Human Body](../../08-whole-body/human-body/README.md):** bilobed primary lymphoid organ in the anterior mediastinum, bridging haematopoietic and immune systems.

## Pathology

### DiGeorge Syndrome (Thymic Aplasia/Hypoplasia)

The most common cause of primary T cell immunodeficiency in humans, affecting ~1 in 4,000 live births. Caused by hemizygous deletion of chromosome 22q11.2, disrupting the *TBX1* gene critical for pharyngeal arch and thymic development. The spectrum ranges from mild partial DiGeorge (reduced thymic tissue, near-normal T cell numbers) to complete DiGeorge (no thymus, profound T cell deficiency) [^digeorge-1965]. Associated features: conotruncal cardiac defects (~74%), parathyroid aplasia → neonatal hypocalcaemia, palatal abnormalities, learning disabilities ("CATCH-22" acronym). Complete DiGeorge requires thymus transplantation (from postnatal thymic tissue) or HSCT; partial DiGeorge has a milder immunological course.

### APECED / APS-1

Autoimmune polyendocrinopathy-candidiasis-ectodermal dystrophy (APECED), caused by biallelic *AIRE* loss-of-function mutations. Rare (<1 in 100,000 in most populations; higher in Finns and Sardinians due to founder effects). Without AIRE, TRAs including insulin and thyroglobulin are not expressed in the medulla → autoreactive T cells against these antigens escape central deletion → multi-organ autoimmunity. Classical triad: mucocutaneous candidiasis, hypoparathyroidism, adrenal insufficiency (Addison's disease). Additional features: type 1 diabetes, hypothyroidism, premature ovarian insufficiency, hepatitis, alopecia. Neutralising autoantibodies against type I interferons (IFN-α, IFN-ω) are pathognomonic and were discovered to predict severe COVID-19 susceptibility.

### Thymic Involution and Immunosenescence

Age-related thymic involution begins after puberty under the influence of sex steroids (testosterone and oestrogen — both thymopoiesis-inhibitory via androgen/oestrogen receptors on TECs). By age 50, thymic fat accounts for ~80% of the gland volume. Consequences: progressive decline in naive T cell output → progressive narrowing of the peripheral T cell repertoire (oligoclonal expansion of memory T cells fills the niche) → impaired responses to new antigens, vaccines, and novel pathogens [^lynch-2009-thymic-involution]. The clinical correlates of immunosenescence include increased susceptibility to influenza, reduced vaccine efficacy in the elderly, and increased cancer incidence.

### Thymoma and Thymic Carcinoma

Thymomas are the most common tumours of the anterior mediastinum in adults (~30–40% of mediastinal masses). They arise from thymic epithelial cells and are classified by WHO histological type (A, AB, B1, B2, B3 — correlating with degree of lymphocyte admixture and epithelial atypia). A defining feature of thymomas: **paraneoplastic autoimmune syndromes** reflecting aberrant thymic selection. Most important: **myasthenia gravis** (MG) in ~30–50% of thymoma patients, caused by autoantibodies against nicotinic acetylcholine receptor (AChR) at the neuromuscular junction — arising because the tumour produces autoreactive CD4⁺ T cells that escape tolerisation [^bhatt-2013-thymic-tumours]. Other paraneoplastic associations: pure red cell aplasia (anti-erythropoietin antibodies), Good's syndrome (thymoma + hypogammaglobulinaemia), autoimmune hepatitis.

Thymic carcinoma (WHO type C) is a frankly malignant epithelial tumour without the autoimmune associations of thymoma; it carries a worse prognosis. Treatment of thymoma/carcinoma: surgical resection (sternotomy or VATS) ± adjuvant radiotherapy for stages III–IVA; unresectable disease: cisplatin-based chemotherapy.

### Thymic Hyperplasia

True thymic hyperplasia (enlargement with preserved architecture) may occur in Graves' disease, acromegaly, and rebound after chemotherapy-induced involution. **Thymic lymphoid hyperplasia** — the presence of lymphoid follicles with germinal centres within the thymus — is the thymic lesion found in ~80% of patients with acetylcholine receptor antibody-positive myasthenia gravis (without a frank thymoma). Thymectomy improves MG outcomes in AChR⁺ patients up to age 65, even without detectable thymoma (MGTX trial, NEJM 2016).

### Thymic Cysts

Common incidental finding on chest CT; usually benign developmental cysts (lined by stratified squamous or columnar epithelium, containing cholesterol crystals). Occasionally arise in thymoma (cystic thymoma), Hodgkin lymphoma after radiation, or germ cell tumours. Most require no intervention unless symptomatic or enlarging.

[^boehm-2012-thymus-review]: Boehm T, Swann JB. Thymus involution and regeneration: two sides of the same coin? *Nat Rev Immunol.* 2013;13(11):831-838. [doi:10.1038/nri3534](https://doi.org/10.1038/nri3534) · [PubMed 24052146](https://pubmed.ncbi.nlm.nih.gov/24052146/)
[^klein-2014-thymic-selection]: Klein L, Kyewski B, Allen PM, Hogquist KA. Positive and negative selection of the T cell repertoire. *Nat Rev Immunol.* 2014;14(6):377-391. [doi:10.1038/nri3667](https://doi.org/10.1038/nri3667) · [PubMed 24830344](https://pubmed.ncbi.nlm.nih.gov/24830344/)
[^anderson-2002-aire]: Anderson MS et al. Projection of an immunological self shadow within the thymus by the Aire protein. *Science.* 2002;298(5597):1395-1401. [doi:10.1126/science.1075958](https://doi.org/10.1126/science.1075958) · [PubMed 12376594](https://pubmed.ncbi.nlm.nih.gov/12376594/)
[^lynch-2009-thymic-involution]: Lynch HE et al. Thymic involution and immune reconstitution. *Trends Immunol.* 2009;30(7):366-373. [doi:10.1016/j.it.2009.04.003](https://doi.org/10.1016/j.it.2009.04.003) · [PubMed 19540807](https://pubmed.ncbi.nlm.nih.gov/19540807/)
[^digeorge-1965]: Markert ML et al. Complete DiGeorge syndrome: persistence of profound immunodeficiency. *J Pediatr.* 1998;132(1):15-21. [doi:10.1016/S0022-3476(98)70478-0](https://doi.org/10.1016/S0022-3476(98)70478-0) · [PubMed 9469993](https://pubmed.ncbi.nlm.nih.gov/9469993/)
[^bhatt-2013-thymic-tumours]: Bhatt VR et al. Management of thymoma and thymic carcinoma. *J Oncol Pract.* 2015;11(4):297-299. [doi:10.1200/JOP.2014.003434](https://doi.org/10.1200/JOP.2014.003434) · [PubMed 25667274](https://pubmed.ncbi.nlm.nih.gov/25667274/)
