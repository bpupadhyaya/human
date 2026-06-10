---
schema: human-scale-entry/v1
id: placenta
name: Placenta
atlas: 01-human
scale: 06-organ
status: draft
last_reviewed: 2026-06-06
summary: "Temporary hemochorial organ of eutherian mammals; trophoblast-derived. Mediates gas/nutrient exchange, fetal waste removal, hormone synthesis (hCG, progesterone, hPL), and immunological tolerance via HLA-G. Failure causes pre-eclampsia and IUGR."
aliases: ["placenta", "afterbirth", "chorionic villi", "trophoblast", "hemochorial placenta"]
sources:
  - id: gude-2004-placenta-function
    type: peer-reviewed
    cite: "Gude NM, Roberts CT, Kalionis B, King RG. Growth and function of the normal human placenta. Thromb Res. 2004;114(5-6):397-407."
    doi: "10.1016/j.thromres.2004.06.038"
    pmid: "15507271"
    url: "https://doi.org/10.1016/j.thromres.2004.06.038"
  - id: red-horse-2004-trophoblast
    type: peer-reviewed
    cite: "Red-Horse K, Zhou Y, Genbacev O, et al. Trophoblast differentiation during embryo implantation and formation of the maternal-fetal interface. J Exp Med. 2004;201(5):615-625."
    doi: "10.1084/jem.20040139"
    pmid: "14993247"
    url: "https://doi.org/10.1084/jem.20040139"
  - id: brosens-2011-preeclampsia
    type: peer-reviewed
    cite: "Brosens I, Pijnenborg R, Vercruysse L, Romero R. The 'Great Obstetrical Syndromes' are associated with disorders of deep placentation. Am J Obstet Gynecol. 2011;204(3):193-201."
    doi: "10.1016/j.ajog.2010.08.009"
    pmid: "21060927"
    url: "https://doi.org/10.1016/j.ajog.2010.08.009"
cross_links:
  - target: 01-human/04-cellular/endothelial-cell
    relation: contains
    note: "Fetal villous capillary endothelial cells form the inner wall of the placental exchange surface; the villous endothelium (with overlying syncytiotrophoblast) constitutes the blood-placenta barrier across which gas, nutrient, and waste exchange occurs."
  - target: 01-human/03-molecular/tgf-beta
    relation: modulated-by
    note: "TGF-β signaling regulates trophoblast invasion depth; excessive TGF-β1 in decidua restricts extravillous trophoblast invasion of spiral arteries, contributing to shallow placentation and the pathogenesis of pre-eclampsia and IUGR."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "FcRn on syncytiotrophoblast mediates IgG transcytosis → passive immunity to newborn (~0.5 g/day at term); maternal anti-Rh IgG causes hemolytic disease of the fetus/newborn (HDFN); IVIG given maternally suppresses alloimmune fetal thrombocytopenia."
  - target: 02-pathogen/01-viruses/sars-cov-2
    relation: connects-to
    note: "SARS-CoV-2 infects placenta via ACE2 on syncytiotrophoblast → villous infarcts, intervillositis, perivillous fibrin; COVID-19 in pregnancy associated with preterm birth, IUGR, and stillbirth risk; Delta and Omicron variants cause more placental pathology than earlier strains."
  - target: 01-human/06-organ/microcephaly
    relation: connects-to
    note: "Zika virus uses AXL receptor on extravillous trophoblast and syncytiotrophoblast for placental entry; Zika-infected placenta → neuroprogenitor apoptosis → congenital microcephaly; placental intervillositis and villitis are histological hallmarks of vertical Zika transmission."
---

# Placenta

## Overview

The placenta is a **transient, specialized organ** that forms during human pregnancy at the interface between mother and fetus, persisting from implantation (~7–10 days post-fertilization) to parturition (~38–40 weeks), when it is delivered as the "afterbirth." It is unique to eutherian (placental) mammals and has no equivalent in the adult human body — making it arguably the most specialized temporary organ in mammalian biology [^gude-2004-placenta-function].

The human placenta is classified as **hemochorial** — the most intimate placental type — in which fetal trophoblast cells are in **direct contact with maternal blood** in the intervillous space. There is no maternal cell layer between the fetal chorionic villi and maternal blood: approximately 150–200 mL of maternal blood fills the intervillous space at term, continuously recirculating through ~30–40 decidual spiral arteries to bathe the 50 km of fetal villous capillaries.

Key functions of the placenta:
1. **Gas and nutrient exchange** — O₂, CO₂, glucose, amino acids, lipids, vitamins
2. **Fetal waste removal** — CO₂, urea, bilirubin
3. **Hormone synthesis** — hCG, progesterone, estrogens, human placental lactogen (hPL)
4. **Immunological tolerance** — HLA-G expression suppresses maternal NK and T cells
5. **Partial pathogen barrier** — variable; TORCH pathogens can breach it

## Structure

### Gross Anatomy at Term

| Feature | Measurement |
|:---|:---|
| **Weight** | ~500–700 g (approximately 1/6 of fetal weight) |
| **Diameter** | ~18–22 cm |
| **Thickness** | ~2–3 cm (central) |
| **Fetal surface (chorionic plate)** | Covered by amnion; branching fetal vessels visible; point of umbilical cord insertion |
| **Maternal surface (basal plate)** | Cotyledons (~15–28 lobes); surface of decidua basalis with maternal blood |
| **Umbilical cord** | ~50–60 cm length; 2 umbilical arteries (fetal deoxygenated) + 1 umbilical vein (fetal oxygenated); Wharton's jelly (mucoid connective tissue) |

### Villous Architecture and Trophoblast Differentiation

The placenta is built around the **chorionic villus** — a branching tree-like structure of fetal connective tissue (with villous capillaries) enveloped by trophoblast cells [^red-horse-2004-trophoblast]:

**Trophoblast cell types:**

| Cell type | Origin | Location | Function |
|:---|:---|:---|:---|
| **Cytotrophoblast (CTB)** | Trophectoderm stem cells | Beneath syncytium | Proliferative progenitor; fuses to form syncytium; or differentiates into EVT |
| **Syncytiotrophoblast (STB)** | Fusion of CTB cells | Outer layer of all villi; direct contact with maternal blood | Gas/nutrient exchange; hormone synthesis; immune evasion |
| **Extravillous trophoblast (EVT)** | CTB of anchoring villi | Invades decidua and myometrium; remodels spiral arteries | Spiral artery remodeling → high-flow, low-resistance uteroplacental circulation |

**Syncytiotrophoblast**: The multinucleate syncytium is a continuous cell layer (~13 m² surface area at term; comparable to the small intestinal absorptive surface) formed by fusion of ~10⁹ cytotrophoblasts during pregnancy. It has:
- **No cell borders** — the entire maternal-facing surface is a single cytoplasm
- **Microvilli** on the apical (maternal blood) surface → ↑surface area for exchange
- **Hormone synthesis**: all steroidogenic and protein hormone synthesis occurs in the STB
- **Immune privilege**: expresses HLA-G (non-classical MHC-I), high PD-L1, FasL → protects against NK and T cell attack

### Spiral Artery Remodeling

Normal placentation requires **extravillous trophoblast invasion** of maternal spiral arteries (decidual and myometrial segments, 1/3 of the way toward radial arteries) [^brosens-2011-preeclampsia]:
- EVTs replace the smooth muscle and endothelium of spiral artery walls
- Converted arteries lose vasoreactivity → high-flow, low-resistance, high-volume uteroplacental vessels
- Inadequate remodeling (shallow trophoblast invasion) → persistent vasoconstrictive spiral arteries → uteroplacental ischemia → sFlt-1↑, VEGF↓ → pre-eclampsia and IUGR

## Function

### Gas and Nutrient Exchange

The placenta facilitates bidirectional exchange across the blood-placenta barrier (maternal blood → STB → fetal villous endothelium → fetal blood):

| Substance | Direction | Mechanism |
|:---|:---|:---|
| **Oxygen** | Maternal → fetal | Passive diffusion; fetal Hb (HbF) has higher O₂ affinity than HbA → Bohr/Haldane effects facilitate transfer |
| **CO₂** | Fetal → maternal | Passive diffusion; rapidly cleared by maternal hyperventilation of pregnancy (progesterone-mediated) |
| **Glucose** | Maternal → fetal | Facilitated diffusion via GLUT1 (apical + basal STB membranes); main fetal energy substrate |
| **Amino acids** | Maternal → fetal | Active transport (concentrative); fetal AA concentrations exceed maternal |
| **Fatty acids** | Maternal → fetal | Facilitated; fatty acid binding proteins; DHA accumulates in fetal brain |
| **IgG** | Maternal → fetal | FcRn receptor-mediated transcytosis; passive immunity to newborn; peaks in 3rd trimester (~0.5 g/day at term) |
| **Bilirubin** | Fetal → maternal | Passive diffusion; cleared by maternal liver |
| **Urea, creatinine** | Fetal → maternal | Passive diffusion |

### Hormone Synthesis

The placenta is an **autonomous endocrine organ** that produces increasing amounts of hormones throughout gestation, partially supplanting the corpus luteum (~10 weeks) and maternal hypothalamic-pituitary axis:

| Hormone | Cell type | Peak/role |
|:---|:---|:---|
| **hCG** (human chorionic gonadotropin) | STB | Peaks at 8–10 weeks; maintains corpus luteum → progesterone production until placenta takes over; detected in urine/blood for pregnancy testing |
| **Progesterone** | STB | ~400 mg/day at term (vs. ~25 mg/day corpus luteum); maintains endometrium, prevents uterine contractions, suppresses maternal immune response |
| **Estrogens** (E1, E2, E3) | STB (requires adrenal DHEA-S) | Promote uterine growth, breast development, fetal organ maturation; estriol (E3) is unique to pregnancy |
| **hPL (human placental lactogen)** | STB | Peaks at term; antagonizes maternal insulin signaling → gestational diabetes risk; promotes maternal lipolysis → fetal glucose conservation |
| **CRH** (corticotropin-releasing hormone) | STB | Rises exponentially in 3rd trimester; "placental clock" for timing parturition; stimulates fetal adrenal DHEA-S → estrogen surge → onset of labor |

### Immunological Tolerance

The placenta solves the fundamental immunological paradox of pregnancy — how does the maternal immune system tolerate a semi-allogeneic fetus for 40 weeks?

Key mechanisms [^red-horse-2004-trophoblast]:
1. **HLA-G expression**: STB and EVTs express HLA-G (non-classical MHC-I; non-polymorphic) instead of classical HLA-A/B/C. HLA-G binds inhibitory receptors (KIR2DL4, ILT2, ILT4) on NK cells and T cells → suppression of cytotoxic responses.
2. **HLA-C restriction**: EVTs express HLA-C (one allele) recognized by inhibitory KIR receptors on decidual uNK cells; KIR2DL1/HLA-C combinations associated with pre-eclampsia risk when inhibitory signaling is reduced.
3. **Regulatory T cells (Tregs)**: Expanded in maternal decidua; specific for paternal antigens; suppress anti-fetal immune responses; require prior antigen exposure (semen exposure increases Treg-mediated tolerance — epidemiological basis for lower pre-eclampsia in longer-cohabiting couples).
4. **IDO (indoleamine 2,3-dioxygenase)**: Expressed by STB and decidual cells; catabolizes tryptophan → depletes local tryptophan → inhibits T cell proliferation.
5. **FasL/PD-L1**: STB expresses death ligands → apoptosis of activated maternal T cells in intervillous space.

## Connections

- `contains` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — fetal villous capillary endothelial cells constitute the innermost layer of the placental exchange barrier; their integrity is critical for normal nutrient/gas transfer
- `modulated-by` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-β restricts extravillous trophoblast invasion depth; excess TGF-β1 in the decidua contributes to shallow placentation, reduced spiral artery remodeling, and the pathophysiology of pre-eclampsia and IUGR
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — FcRn on syncytiotrophoblast mediates IgG transcytosis → passive immunity to newborn (~0.5 g/day at term); maternal anti-Rh IgG causes hemolytic disease of the fetus/newborn (HDFN); IVIG given maternally suppresses alloimmune fetal thrombocytopenia.
- `connects-to` → **[SARS-CoV-2](../../../02-pathogen/01-viruses/sars-cov-2/README.md)** — SARS-CoV-2 infects placenta via ACE2 on syncytiotrophoblast → villous infarcts, intervillositis, perivillous fibrin; COVID-19 in pregnancy associated with preterm birth, IUGR, and stillbirth risk; Delta and Omicron variants cause more placental pathology than earlier strains.
- `connects-to` → **[Microcephaly](../microcephaly/README.md)** — Zika virus uses AXL receptor on extravillous trophoblast and syncytiotrophoblast for placental entry; Zika-infected placenta → neuroprogenitor apoptosis → congenital microcephaly; placental intervillositis and villitis are histological hallmarks of vertical Zika transmission.

## Pathology

### Pre-eclampsia

Affects 2–8% of pregnancies globally; major cause of maternal and perinatal mortality. The two-stage model [^brosens-2011-preeclampsia]:
- **Stage 1 (silent, 10–20 weeks)**: Defective deep trophoblast invasion → inadequate spiral artery remodeling → placental ischemia/hypoxia
- **Stage 2 (clinical, >20 weeks)**: Ischemic placenta releases sFlt-1 (soluble VEGF receptor, anti-angiogenic) and sEng (soluble endoglin, anti-TGF-β) into maternal circulation → endothelial dysfunction → hypertension (>140/90), proteinuria, end-organ damage (brain → eclampsia/seizures; liver → HELLP; kidney → AKI)

### Intrauterine Growth Restriction (IUGR)

Fetal growth below the 10th percentile; most commonly due to uteroplacental insufficiency (shallow invasion, inadequate spiral artery remodeling). Chronic placental ischemia → umbilical artery Doppler abnormalities → absent/reversed end-diastolic flow → fetal hypoxia → redistribution of blood flow (brain-sparing) → stillbirth risk. No specific treatment; delivery timing (risk of prematurity vs. intrauterine death) is the clinical challenge.

### Placenta Accreta Spectrum

Abnormal adherence of placental tissue into the myometrium:
- **Accreta**: Villi contact myometrium (no decidua)
- **Increta**: Villi invade into myometrium
- **Percreta**: Villi penetrate through myometrium (+ bladder/bowel in severe cases)

Rising incidence from increasing cesarean section rates (uterine scar → decidua deficiency → abnormal trophoblast invasion). Associated with massive hemorrhage at delivery; treatment is often hysterectomy.

### TORCH Infections — Placental Barrier Failure

The placenta provides partial but imperfect protection against vertical transmission:

| Pathogen | Vertical transmission rate | Mechanism of barrier breach |
|:---|:---|:---|
| Toxoplasma gondii | 10–80% (trimester-dependent) | Trophoblast infection → STB damage |
| Rubella virus | Near 100% (1st trimester) | Trophoblast infection via cell-surface receptors |
| CMV | 1–7% primary infection | Cell-to-cell spread via EVT and STB infection |
| HSV-2 | <1% transplacental; primarily intrapartum | Occasional hematogenous; mainly birth canal exposure |
| Zika virus | Variable (~40–50% primary symptomatic) | AXL receptor on EVT/STB; causes placental inflammation and congenital microcephaly |
| Syphilis | 50–100% untreated | Spirochete bacteremia → transplacental at any stage |

[^gude-2004-placenta-function]: Gude NM et al. Growth and function of the normal human placenta. *Thromb Res.* 2004;114(5-6):397-407. [doi:10.1016/j.thromres.2004.06.038](https://doi.org/10.1016/j.thromres.2004.06.038) · [PubMed 15507271](https://pubmed.ncbi.nlm.nih.gov/15507271/)
[^red-horse-2004-trophoblast]: Red-Horse K et al. Trophoblast differentiation during embryo implantation and formation of the maternal-fetal interface. *J Exp Med.* 2004;201(5):615-625. [doi:10.1084/jem.20040139](https://doi.org/10.1084/jem.20040139) · [PubMed 14993247](https://pubmed.ncbi.nlm.nih.gov/14993247/)
[^brosens-2011-preeclampsia]: Brosens I et al. The 'Great Obstetrical Syndromes' are associated with disorders of deep placentation. *Am J Obstet Gynecol.* 2011;204(3):193-201. [doi:10.1016/j.ajog.2010.08.009](https://doi.org/10.1016/j.ajog.2010.08.009) · [PubMed 21060927](https://pubmed.ncbi.nlm.nih.gov/21060927/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
