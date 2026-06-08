---
schema: human-scale-entry/v1
id: cholesterol
name: Cholesterol
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-05
summary: "C₂₇ sterol (MW 386.65); rigid 4-ring backbone + one –OH. Membrane fluidity regulator, steroid hormone and bile acid precursor. Synthesised via mevalonate/HMGR pathway. FH (LDLR mutation) → premature ASCVD; statins target HMGR to lower LDL-C by 30–55%."
aliases: ["cholesterol ester", "free cholesterol", "LDL cholesterol", "HDL cholesterol", "VLDL"]
sources:
  - id: stryer-biochemistry
    type: textbook
    cite: "Berg JM, Tymoczko JL, Stryer L. Biochemistry. 9th ed. W.H. Freeman; 2019."
    url: "https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X"
    accessed: "2026-06-05"
  - id: alberts-mol-cell-biology
    type: textbook
    cite: "Alberts B, Johnson A, Lewis J, et al. Molecular Biology of the Cell. 7th ed. W.W. Norton; 2022."
    url: "https://www.ncbi.nlm.nih.gov/books/NBK26880/"
    accessed: "2026-06-05"
  - id: goldstein-brown-1985
    type: peer-reviewed
    cite: "Goldstein JL, Brown MS. Nobel Lecture 1985: The LDL receptor and the regulation of cholesterol metabolism. Science. 1986;232:34-47."
    url: "https://doi.org/10.1126/science.3513311"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/08-whole-body/human-body
    relation: part-of
    note: "~35–40g total cholesterol; 80% in cell membranes as fluidity regulator; precursor of steroid hormones (cortisol, sex steroids, vitamin D) and bile acids; every nucleated cell synthesises it."
  - target: 01-human/04-cellular/hepatocyte
    relation: modulates
    note: "Liver is the central cholesterol hub: hepatocytes synthesise ~70% via mevalonate/HMGR (statin target), package into VLDL→LDL, clear LDL via LDLR, and convert cholesterol to bile acids via CYP7A1."
  - target: 03-medicine/01-modern/04-cardio/statins
    relation: modulated-by
    note: "Statins competitively inhibit HMGR (rate-limiting enzyme of mevalonate pathway) → ↓hepatic cholesterol → ↑LDLR expression → ↓LDL-C by 30–55%; primary and secondary prevention of MACE."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: modulates
    note: "Cholesterol in cardiomyocyte sarcolemma and t-tubule membranes forms lipid rafts that organise L-type Ca²⁺ channels, RyR2, and β-AR signalling platforms; depletion disrupts EC coupling."
  - target: 01-human/05-tissue/arterial-wall
    relation: modulated-by
    note: "Modulated by Arterial Wall."
  - target: 01-human/07-system/familial-hypercholesterolemia
    relation: connects-to
    note: "FH results from impaired LDLR-mediated cholesterol clearance; LDLR mutations → fewer surface receptors → LDL-C >190 mg/dL (HeFH) or >500 mg/dL (HoFH LDLR null); excess cholesterol in macrophages → foam cells → atheromatous plaque."
---

# Cholesterol

## Overview

**Cholesterol** is the archetypal mammalian **sterol** — a lipid with a characteristic rigid tetracyclic ring system — and one of the most physiologically important molecules in the human body [^stryer-biochemistry]. It is simultaneously:

- An **essential structural component** of every eukaryotic cell membrane
- The **biosynthetic precursor** of all steroid hormones (cortisol, aldosterone, sex hormones), vitamin D, and bile acids
- A **lipid raft organizer** that creates signaling microdomains in plasma membranes
- A **cardiovascular risk factor** when dysregulated in the form of elevated LDL-cholesterol

The total body cholesterol pool is approximately **35–40 g**, with ~80% residing in cell membranes (particularly myelin, which is ~25% cholesterol by dry mass) and ~20% in plasma lipoproteins. Approximately 70% of plasma cholesterol is synthesised endogenously by the liver; ~25% is dietary in origin; the remainder derives from peripheral tissues.

Goldstein and Brown's seminal work on the **LDL receptor** — which earned the 1985 Nobel Prize in Physiology or Medicine — established the mechanistic basis for familial hypercholesterolaemia and provided the rational foundation for statin development [^goldstein-brown-1985].

## Structure

**Molecular formula:** C₂₇H₄₆O  
**Molecular weight:** 386.65 Da  
**IUPAC name:** (3β)-cholest-5-en-3-ol

### Structural features

| Feature | Description |
|:---|:---|
| **Steroid backbone** | Cyclopentanoperhydrophenanthrene — four fused rings (A, B, C, D); rings A–C are six-membered (cyclohexane), ring D is five-membered (cyclopentane) |
| **3β-hydroxyl group** | Single –OH at C3 in β-configuration (equatorial); polar head group enabling amphiphilicity; site of esterification (SOAT/ACAT enzymes; LCAT in plasma) |
| **Δ5 double bond** | C5–C6 double bond introduces a kink in ring B → adds rigidity to the steroid core; absent in dihydrocholesterol and cholestanol |
| **Isooctyl side chain** | 8-carbon branched side chain at C17; entirely nonpolar; inserts into hydrophobic core of membranes |
| **Amphiphilicity** | Polar –OH head + nonpolar ring system + nonpolar tail → sits at the glycerophospholipid–water interface with –OH facing the aqueous phase |

### Cholesterol esters

In plasma and intracellular lipid droplets, cholesterol is predominantly stored/transported as **cholesterol esters** — the 3-OH esterified with a long-chain fatty acid (oleate, linoleate). Esterification by:
- **SOAT1/SOAT2** (sterol O-acyltransferase; ER; intracellular esterification)
- **LCAT** (lecithin-cholesterol acyltransferase; plasma; esterifies cholesterol in HDL using FA from phosphatidylcholine)

## Function

### 1. Membrane fluidity regulation

Cholesterol is the master **membrane fluidity buffer** [^alberts-mol-cell-biology]:
- **High-temperature effect:** At physiological temperatures where membrane phospholipids would be disordered (fluid phase), cholesterol intercalates between acyl chains of phospholipids → restricts lateral motion → **condensing effect** → reduces membrane permeability
- **Low-temperature effect:** Cholesterol prevents ordered-phase (gel) crystallization by disrupting acyl-chain packing → prevents membrane rigidity
- **Net effect:** Buffers membranes into an intermediate "liquid-ordered" phase across a broad temperature range

**Membrane cholesterol content** varies by compartment:
- Plasma membrane: ~40 mol% of total lipid
- ER: ~5 mol% (site of synthesis — maintained at low concentration by rapid export)
- Mitochondria: ~3 mol%

### 2. Lipid raft formation

Cholesterol + sphingomyelin (SM) co-partition into **lipid rafts** (liquid-ordered microdomains, ~10–200 nm) within the plasma membrane. These detergent-resistant microdomains are enriched in:
- GPI-anchored proteins (CD55, CD59, urokinase receptor)
- Signaling proteins: eNOS (endothelial NO synthase), G-protein-coupled receptors, Src family kinases
- Caveolin-1 (scaffolding protein of caveolae — deep invaginated rafts in endothelium, adipocytes, muscle)

Cholesterol depletion (methyl-β-cyclodextrin) disperses rafts → disrupts downstream signaling (EGFR, Ras, eNOS, β-AR in cardiomyocytes, L-type Ca²⁺ channel clustering) [^alberts-mol-cell-biology].

### 3. Steroid hormone biosynthesis

All steroid hormones derive from cholesterol via the following committed first step, which occurs in the **inner mitochondrial membrane**:

> **Cholesterol → Pregnenolone**  
> Enzyme: CYP11A1 (P450scc, side-chain cleavage enzyme)  
> Requirement: **StAR** (steroidogenic acute regulatory protein) transports cholesterol from OMM to IMM — the rate-limiting, hormonally regulated step  
> Cofactors: O₂, NADPH, adrenodoxin, adrenodoxin reductase

Pregnenolone is the branch-point precursor for:
- **Glucocorticoids** (cortisol): adrenal zona fasciculata
- **Mineralocorticoids** (aldosterone): adrenal zona glomerulosa
- **Sex steroids** (testosterone, oestradiol, DHEA): gonads, adrenal zona reticularis
- **Vitamin D:** 7-dehydrocholesterol (cholesterol biosynthetic intermediate) in skin → cholecalciferol (vitamin D₃) by UVB photolysis → 25-OH-D₃ (liver CYP2R1) → 1,25-(OH)₂D₃/calcitriol (kidney CYP27B1)

### 4. Bile acid synthesis

The primary pathway for hepatic cholesterol catabolism and excretion:

> **Cholesterol → 7α-hydroxycholesterol**  
> Enzyme: CYP7A1 (cholesterol 7α-hydroxylase; ER; rate-limiting step of bile acid synthesis)  
> Regulation: FXR (farnesoid X receptor) activated by bile acids → induces SHP → represses LRH-1 → ↓CYP7A1 (feedback inhibition)

Primary bile acids (cholic acid, chenodeoxycholic acid) are conjugated with glycine/taurine in hepatocytes → secreted into bile → emulsify dietary fats and fat-soluble vitamins in the small intestine → reabsorbed in terminal ileum (enterohepatic circulation, ~95% recirculation).

## Mechanism

### Mevalonate pathway (cholesterol biosynthesis)

All 27 carbons of cholesterol are derived from **acetyl-CoA** via the mevalonate pathway [^stryer-biochemistry]:

| Step | Enzyme | Location | Key point |
|:---|:---|:---|:---|
| 2 acetyl-CoA → acetoacetyl-CoA | thiolase | cytoplasm | condensation |
| + acetyl-CoA → HMG-CoA | HMGCS | cytoplasm | |
| HMG-CoA → mevalonate | **HMGR** (HMG-CoA reductase) | **ER membrane** | **Rate-limiting; statin target** |
| Mevalonate → IPP/DMAPP | multiple steps | cytoplasm | requires 3 ATP |
| IPP/DMAPP → squalene | squalene synthase | ER | 2 FPP → squalene |
| Squalene → lanosterol | squalene epoxidase + OSC | ER | O₂ required |
| Lanosterol → cholesterol | 19 additional steps | ER | CYP51A1, DHCR7, etc. |

**Total energetic cost:** ~4 NADPH + ~18 ATP-equivalents per cholesterol molecule

### HMGR regulation (the critical control point)

HMGR is regulated at multiple levels to match cholesterol synthesis to cellular need [^goldstein-brown-1985]:

1. **SREBP feedback:** When ER cholesterol falls, SCAP escorts SREBP-2 from ER to Golgi → S1P/S2P proteolytic activation → nuclear SREBP-2 → activates *HMGCR*, *LDLR*, *SQLE* transcription. When ER cholesterol rises, INSIG retains SCAP-SREBP in ER → no cleavage → ↓transcription.
2. **Phosphorylation:** AMPK phosphorylates HMGR at Ser872 → inactivates enzyme; glucagon (via PKA) also inhibits.
3. **Ubiquitin-proteasomal degradation:** High cholesterol → INSIG recruits E3 ubiquitin ligase → HMGR ubiquitylation and ER-associated degradation (ERAD).
4. **Translational regulation:** HMGR mRNA translation is inhibited when sterol levels are high.

### LDL receptor pathway

The **LDL receptor (LDLR)** mediates cellular uptake of LDL-cholesterol [^goldstein-brown-1985]:
1. LDLR (on hepatocyte surface) binds apoB100 on LDL → clathrin-mediated endocytosis
2. Endosomal acidification → LDL releases from LDLR → LDLR recycled to surface
3. Lysosomal hydrolysis of LDL → free cholesterol released
4. Free cholesterol: (a) inhibits HMGR (↓synthesis), (b) activates SOAT (→ storage as CE), (c) suppresses LDLR transcription via INSIG/SCAP/SREBP axis

**PCSK9:** secreted serine protease; binds LDLR at cell surface → routes LDLR to lysosomal degradation instead of recycling → ↑LDLR degradation → ↑plasma LDL-C. Gain-of-function PCSK9 mutations cause severe FH; PCSK9 inhibitors (evolocumab, alirocumab) are next-generation LDL-lowering therapies.

### Reverse cholesterol transport (RCT)

Peripheral cholesterol is exported back to liver via the **HDL pathway**:
1. ABCA1 (ATP-binding cassette A1) transports free cholesterol from cells to lipid-poor apoA-I → nascent HDL
2. ABCG1 transports cholesterol to mature HDL
3. LCAT esterifies HDL-cholesterol (using lecithin as FA donor) → cholesterol esters move to HDL core → mature HDL3 → HDL2
4. **CETP** (cholesterol ester transfer protein) transfers CEs from HDL to LDL/VLDL in exchange for TG → net transfer of cholesterol from HDL to atherogenic particles
5. **SR-B1** (scavenger receptor B1) on hepatocytes mediates selective CE uptake from HDL → hepatic cholesterol for bile acid synthesis/secretion

## Connections

- **Part-of** → [Human Body](../../08-whole-body/human-body/README.md): ~35–40 g total cholesterol; 80% in cell membranes as fluidity regulator; precursor of steroid hormones (cortisol, sex steroids, vitamin D) and bile acids; every nucleated cell synthesises cholesterol [^stryer-biochemistry].
- **Modulates** → [Hepatocyte](../../04-cellular/hepatocyte/README.md): Liver is the central cholesterol hub — hepatocytes synthesise ~70% via mevalonate/HMGR, package into VLDL→LDL, clear LDL via LDLR, and convert cholesterol to bile acids via CYP7A1 [^goldstein-brown-1985].
- **Modulated-by** → [Statins](../../../03-medicine/01-modern/04-cardio/statins/README.md): Statins competitively inhibit HMGR (rate-limiting enzyme of mevalonate pathway) → ↓hepatic cholesterol → ↑LDLR expression → ↓LDL-C by 30–55%; primary and secondary prevention of MACE [^goldstein-brown-1985].
- **Modulates** → [Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md): Cholesterol in cardiomyocyte sarcolemma and t-tubule membranes forms lipid rafts organising L-type Ca²⁺ channels, RyR2, and β-AR signalling platforms; depletion disrupts excitation-contraction coupling [^alberts-mol-cell-biology].
- `connects-to` → **[Familial Hypercholesterolemia](../../07-system/familial-hypercholesterolemia/README.md)** — FH results from impaired LDLR-mediated cholesterol clearance; LDLR mutations → fewer surface receptors → LDL-C >190 mg/dL (HeFH) or >500 mg/dL (HoFH LDLR null); excess cholesterol in macrophages → foam cells → atheromatous plaque.

## Pathology

| Disease | Mechanism | Clinical features |
|:---|:---|:---|
| **Familial hypercholesterolaemia (FH)** | LDLR mutation (most common), apoB mutation, or PCSK9 GOF → ↑LDL-C; autosomal dominant | Premature ASCVD, tendon xanthomata (Achilles), xanthelasma; heterozygous FH: LDL-C ~5–10 mmol/L; homozygous: > 13 mmol/L |
| **Atherosclerosis** | LDL accumulates in intima → oxidation → foam cell formation (macrophage ACAT1) → fatty streak → fibrous plaque → plaque rupture → ACS | MI, stroke, PAD; principal cause of global mortality |
| **Gallstones (cholesterol type)** | Cholesterol supersaturation in bile (↑CSI) → crystal nucleation → stone growth | RUQ pain, biliary colic, cholecystitis; ursodeoxycholic acid can dissolve small stones |
| **Smith-Lemli-Opitz syndrome** | DHCR7 (7-dehydrocholesterol reductase) mutation → cholesterol synthesis defect → ↓cholesterol + ↑7-DHC | Dysmorphic facies, 2/3-toe syndactyly, intellectual disability; AR |
| **Tangier disease** | ABCA1 mutation → impaired cholesterol efflux → very low HDL, cholesterol accumulation in macrophages of tonsils, liver, spleen, nerves | Orange tonsils, hepatosplenomegaly, peripheral neuropathy, premature CVD |
| **Sitosterolaemia** | ABCG5/ABCG8 mutation → impaired plant sterol excretion → ↑plant sterols (sitosterol) + ↑cholesterol absorption | Xanthomata, premature ASCVD; AR; treat with ezetimibe |
| **Cerebrotendinous xanthomatosis** | CYP27A1 mutation → bile acid synthesis block → ↑cholestanol accumulation | Tendon xanthomata, cataracts, progressive neurological disability; treat with CDCA |
| **Statin-induced myopathy** | HMGR inhibition → ↓mevalonate → ↓ubiquinone (CoQ10) in muscle; genetic risk: SLCO1B1 variants | Myalgia, CK elevation, rarely rhabdomyolysis; treat with CoQ10, statin switch/dose reduction |

## See Also

- [Statins](../../../03-medicine/01-modern/04-cardio/statins/README.md) — competitive HMGR inhibitors; primary cholesterol-lowering therapy
- [Cortisol](../cortisol/README.md) — steroid hormone derived from cholesterol via pregnenolone; synthesis requires StAR and CYP11A1
- [Insulin](../insulin/README.md) — promotes cholesterol synthesis via SREBP-1c and inhibits HMGR via Akt/mTOR; insulin resistance → dyslipidaemia (↑TG, ↓HDL, small dense LDL)
- [NF-kB](../nf-kb/README.md) — activated in macrophage foam cells; drives inflammatory cytokine secretion in atherosclerotic plaques
- [Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md) — cholesterol-rich t-tubules organise Ca²⁺ handling microdomains; cholesterol depletion in HF contributes to excitation-contraction uncoupling
- [Hepatic lobule](../../05-tissue/hepatic-lobule/README.md) — hepatic parenchymal unit where cholesterol synthesis, lipoprotein assembly, and bile acid production are zonally organised

[^stryer-biochemistry]: Berg JM, Tymoczko JL, Stryer L. *Biochemistry.* 9th ed. W.H. Freeman; 2019.
[^alberts-mol-cell-biology]: Alberts B, Johnson A, Lewis J, et al. *Molecular Biology of the Cell.* 7th ed. W.W. Norton; 2022.
[^goldstein-brown-1985]: Goldstein JL, Brown MS. The LDL receptor and the regulation of cholesterol metabolism. *Science.* 1986;232:34–47. [doi:10.1126/science.3513311](https://doi.org/10.1126/science.3513311)
