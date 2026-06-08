---
schema: human-scale-entry/v1
id: mtor
name: mTOR
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Ser/Thr kinase in two complexes: mTORC1 (rapamycin-sensitive; drives anabolism, suppresses autophagy) and mTORC2 (Akt/SGK1). Integrates nutrient, energy, and growth factor signals; targeted by rapamycin (transplant, TSC) and everolimus (cancer, RCC, PNET)."
aliases: ["mechanistic target of rapamycin", "mTOR kinase", "FRAP", "RAFT1", "mTORC1", "mTORC2"]
sources:
  - id: laplante-2012-mtor
    type: peer-reviewed
    cite: "Laplante M, Sabatini DM. mTOR signaling in growth control and disease. Cell. 2012;149(2):274-293."
    doi: "10.1016/j.cell.2012.03.017"
    pmid: "22500797"
    url: "https://doi.org/10.1016/j.cell.2012.03.017"
  - id: heitman-1991-fkbp12
    type: peer-reviewed
    cite: "Heitman J, Movva NR, Hall MN. Targets for cell cycle arrest by the immunosuppressant rapamycin in yeast. Science. 1991;253(5022):905-909."
    doi: "10.1126/science.1715094"
    pmid: "1715094"
    url: "https://doi.org/10.1126/science.1715094"
  - id: saxton-2017-mtor-review
    type: peer-reviewed
    cite: "Saxton RA, Sabatini DM. mTOR Signaling in Growth, Metabolism, and Disease. Cell. 2017;168(6):960-976."
    doi: "10.1016/j.cell.2017.02.004"
    pmid: "28283069"
    url: "https://doi.org/10.1016/j.cell.2017.02.004"
cross_links:
  - target: 01-human/03-molecular/ampk
    relation: modulated-by
    note: "AMPK and mTORC1 are reciprocal energy sensors: AMPK (low ATP/high AMP) phosphorylates Raptor and TSC2 → mTORC1 inhibition; mTOR phosphorylates ULK1 → autophagy suppression; metformin (via AMPK) and rapamycin (direct mTORC1 block) both exploit this axis."
  - target: 01-human/03-molecular/insulin
    relation: modulated-by
    note: "Insulin → IRS-1/2 → PI3K → PIP3 → Akt → mTORC1 activation (via TSC1/TSC2 phosphorylation + direct Raptor activation); mTORC1 negative feedback → S6K1 → IRS-1 Ser307 phosphorylation → insulin resistance in chronic hyperinsulinemia (e.g., obesity, TSC tumors)."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: modulates
    note: "mTORC1 promotes Th1/Th17 effector differentiation; rapamycin-mediated mTOR inhibition suppresses effector programs and skews T cells toward Foxp3+ Treg — the primary mechanism underlying rapamycin's immunosuppressive and pro-tolerogenic effects in transplant."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "Microbiome-derived SCFAs activate mTOR in intestinal epithelial cells; mTOR regulates barrier integrity and epithelial renewal; rapamycin treatment alters gut microbial ecology and mucosal immune tone by suppressing epithelial and immune cell mTOR activity."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "mTOR GOF mutations (TSC1/TSC2 → tuberous sclerosis; somatic PIK3CA/MTOR → focal cortical dysplasia) are major causes of structural epilepsy; everolimus reduces TSC seizure burden ~50%; mTOR inhibitors are disease-modifying for FCD-associated drug-refractory epilepsy."
  - target: 01-human/07-system/autism-spectrum-disorder
    relation: connects-to
    note: "mTOR hyperactivation causes syndromic ASD in TSC (TSC1/2 LOF) and PTEN hamartoma (PTEN LOF); everolimus reduces ASD severity and seizure burden in TSC; 25-35% of TSC patients have ASD; excess mTOR drives synaptic protein overproduction causing E/I imbalance."
---

# mTOR

## Overview

**mTOR (mechanistic target of rapamycin)** is a **serine/threonine protein kinase** that functions as the central integration hub for nutrient availability, energy status, growth factor signaling, and cellular stress — translating these inputs into decisions about cell growth, proliferation, autophagy, and metabolism. First identified in 1991 as the target of the antifungal/immunosuppressant **rapamycin (sirolimus)** via the FKBP12–rapamycin complex in yeast [^heitman-1991-fkbp12], mTOR has since been recognized as one of the most evolutionarily conserved and clinically important signaling nodes in biology.

mTOR operates within two functionally and structurally distinct multiprotein complexes:
- **mTORC1:** Contains mTOR + Raptor + mLST8 + PRAS40 + Deptor; **rapamycin-sensitive** (rapamycin-FKBP12 binds Raptor → allosteric inhibition); controls anabolic growth, protein synthesis, lipid synthesis, and autophagy suppression
- **mTORC2:** Contains mTOR + Rictor + mSin1 + mLST8 + Protor1/2; **rapamycin-insensitive** (acute); controls Akt, SGK1, PKCα phosphorylation → cytoskeletal organization, cell survival, metabolism

mTOR is deregulated in a vast spectrum of diseases — cancer, diabetes, obesity, neurodegeneration, and aging — and is targeted by several approved drugs [^laplante-2012-mtor]:
- **Rapamycin (sirolimus):** Immunosuppressant for organ transplant; sirolimus-eluting coronary stents
- **Everolimus/Temsirolimus:** mTORC1 inhibitors approved for RCC, PNET, breast cancer, TSC-associated tumors
- **Metformin (indirect):** Activates AMPK → inhibits mTORC1
- **PI3K/mTOR dual inhibitors:** In clinical trials for cancers

## Structure

### mTOR protein

mTOR is a 289 kDa atypical kinase of the **PIKK family (phosphatidylinositol 3-kinase-related kinase)** — same family as ATM, ATR, DNA-PK (all share a C-terminal catalytic domain structurally related to PI3K but with exclusively protein substrate specificity).

**Domain organization (N→C):**
1. **HEAT repeats (N-terminal):** ~1,200 aa; scaffold for protein interactions; substrate recruitment and complex formation
2. **FAT domain:** ~600 aa; forms the N-terminal portion of the "cup" structure encircling the kinase domain in cryo-EM structures
3. **FRB domain (FKBP12-Rapamycin Binding):** Site of rapamycin-FKBP12 binding → allosteric inhibition; located adjacent to the kinase active site
4. **Kinase domain:** The catalytic core; shares PI3K fold but uses protein (not lipid) substrates; requires activation loop Thr2446/Ser2448 phosphorylation
5. **FATC domain (C-terminal):** Regulates kinase activity; must be intact for catalysis

### mTORC1: nutrient- and growth factor-activated complex [^saxton-2017-mtor-review]

**mTORC1 inputs converge on the TSC1/TSC2–Rheb axis:**

- **Growth factors (insulin, IGF-1, EGF, PDGF):** Receptor tyrosine kinase → PI3K → PIP3 → PDK1 + mTORC2 → Akt (Ser473 + Thr308) → phosphorylates TSC2 at multiple sites → disrupts TSC1/TSC2 GAP complex → Rheb (small GTPase) remains GTP-loaded → active → activates mTORC1 kinase
- **Amino acids:** Sensed by Ragulator/v-ATPase complex at lysosomal surface → RagA/B•GTP:RagC/D•GDP → recruits mTORC1 to lysosome → Rheb can access mTOR → activation; specific sensors: GATOR1/2 for leucine and arginine (via Sestrin2/CASTOR1); mTORC1 is activated at lysosomes
- **Energy (ATP:AMP ratio):** Low ATP → AMP/ADP rise → AMPK activated → phosphorylates Raptor (Ser792) and TSC2 (Ser1387) → inhibits mTORC1
- **Hypoxia:** REDD1 (DDIT4, induced by HIF-1α) → activates TSC1/TSC2 → Rheb inactivation → mTORC1 inhibition; also via AMPK

### mTORC1 outputs: anabolism vs. catabolism

**When mTORC1 is ON (nutrient-rich):**
1. **Protein synthesis (anabolism):** Phosphorylates 4E-BP1 (releases eIF4E → cap-dependent translation initiation) and S6K1 (→ ribosome biogenesis, mRNA translation elongation) → increased protein synthesis rate
2. **Lipid and nucleotide synthesis:** Activates SREBP1 (→ fatty acid/cholesterol synthesis) and promotes nucleotide synthesis
3. **Suppresses autophagy:** Phosphorylates ULK1/2 (Ser757) → dissociates ULK1 from AMPK → autophagy initiation suppressed; phosphorylates TFEB → nuclear exclusion → lysosome biogenesis suppressed
4. **Promotes cell growth and proliferation:** HIF-1α mRNA translation elevated (via 4E-BP1 phosphorylation); activates Myc-dependent ribosome biogenesis programs

**When mTORC1 is OFF (starvation/rapamycin):**
- ULK1/2 activated by AMPK → autophagy initiation (Beclin-1 complex, LC3 lipidation) → autolysosome formation → cellular recycling
- TFEB/TFE3 dephosphorylated → nuclear import → lysosome biogenesis → enhanced protein/organelle turnover

## Function

### Cancer

mTOR signaling is hyperactivated in virtually all cancers through:
- **PI3K activating mutations** (PIK3CA H1047R, E545K → gain-of-function) — among the most common cancer mutations
- **PTEN loss** (PTEN phosphatase opposes PI3K; mutated in glioblastoma, prostate, breast, endometrial cancer → constitutive PIP3 → Akt → mTORC1)
- **TSC1/TSC2 mutations** (tuberous sclerosis complex; hamartomas, SEGA, cardiac rhabdomyomas; constitutive Rheb activity)
- **RAS/RAF/MEK/ERK** → PI3K/Akt crosstalk → mTORC1 activation

**mTOR inhibitors in oncology:**
- **Everolimus (RAD001, Novartis):** mTORC1 allosteric inhibitor; approved for advanced RCC (RECORD-1 trial: 4.9 vs 1.9 months PFS), hormone receptor-positive HER2-negative advanced breast cancer (BOLERO-2: everolimus + exemestane), PNET, TSC-associated SEGA and renal angiomyolipoma
- **Temsirolimus (CCI-779, Wyeth/Pfizer):** IV prodrug of sirolimus; approved for poor-risk advanced RCC (ARCC trial: 10.9 vs 7.3 months OS)
- **Limitation:** mTORC1 inhibition → S6K1 inactivation → loss of negative feedback on IRS-1 → PI3K/Akt reactivation; explains partial responses and resistance; motivates PI3K/mTOR dual inhibitors and mTOR kinase inhibitors (Torin1 analogs)

### Immunosuppression (transplant)

**Sirolimus/everolimus in transplant:**
- mTORC1 inhibition → IL-2-induced T cell cycle arrest in G1 (requires mTORC1 for progression to S phase via 4E-BP1/cyclin D1)
- Unlike calcineurin inhibitors (cyclosporine, tacrolimus), sirolimus does not impair IL-2 production → allows regulatory T cell generation
- Sirolimus-eluting coronary stents (Cypher, 2003): reduced restenosis by inhibiting smooth muscle cell proliferation (mTORC1 arrest) while allowing endothelialization

### Autophagy regulation

mTOR is the **master negative regulator of autophagy**:
- Under nutrient stress: mTORC1 inactivated → ULK1 active → autophagy initiation (VPS34/Beclin-1 complex)
- mTOR also suppresses lysosome biogenesis (TFEB phosphorylation → cytoplasmic retention)
- Pharmacological rapamycin/everolimus → autophagy induction → clinically relevant in clearing aggregate-prone proteins (polyQ proteins in Huntington's disease, α-synuclein in Parkinson's — mTOR inhibition is neuroprotective in mouse models)

### Aging and longevity

mTOR inhibition extends lifespan in multiple model organisms (yeast, worms, flies, mice):
- Rapamycin in mice (National Institute on Aging Interventions Testing Program): 14–18 month lifespan extension (9–14%) even when started at 20 months (equivalent to ~60-year-old human); mechanism includes reduced cellular senescence, improved proteostasis, and modulated immune aging
- **Dietary restriction** (most robust longevity intervention across species): predominantly acts through mTORC1 inhibition (amino acid deprivation) and AMPK activation

## Mechanism

### Rapamycin mechanism: FKBP12-rapamycin complex

Rapamycin (sirolimus) is a macrolide natural product from Streptomyces hygroscopicus (Rapa Nui, Easter Island):
1. Enters cell → binds **FKBP12** (FK506-binding protein 12, a prolyl isomerase) with sub-nanomolar affinity
2. FKBP12–rapamycin complex binds the **FRB domain** of mTOR (allosteric site, not ATP-binding active site)
3. Disrupts Raptor–mTOR interaction → mTORC1 cannot phosphorylate its substrates (S6K1 and 4E-BP1)
4. mTORC2 is not acutely inhibited (lacks FRB-accessible rapamycin site) but is inhibited by prolonged rapamycin treatment in some cell types

**Active-site mTOR kinase inhibitors (TORKi):** Torin1, Torin2, OSI-027 — compete with ATP at the kinase domain → inhibit both mTORC1 and mTORC2 simultaneously; overcome partial 4E-BP1 inhibition by rapamycin; in clinical trials.

## Connections

- `modulated-by` → **[AMPK](../ampk/README.md)** — AMPK and mTORC1 are reciprocal energy sensors; AMPK inhibits mTORC1 via TSC2 and Raptor phosphorylation in low-energy states; this AMPK-mTOR axis mediates metformin's anti-tumor and anti-aging effects.
- `modulated-by` → **[Insulin](../insulin/README.md)** — insulin → PI3K → Akt → mTORC1 activation; chronic hyperinsulinemia drives mTORC1-mediated S6K1 feedback → IRS-1 degradation → insulin resistance in obesity and type 2 diabetes.
- `modulates` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — mTOR inhibition (rapamycin) promotes Treg differentiation by suppressing mTORC1-driven Th1/Th17 programs and allowing Foxp3 expression; explains rapamycin's immunosuppressive mechanism in transplant.
- `connects-to` → **[Gut Microbiome](../../07-system/gut-microbiome/README.md)** — microbiome-derived SCFAs activate mTOR in intestinal epithelial cells; mTOR regulates intestinal barrier function and epithelial renewal; mTOR inhibition affects gut microbial ecology.
- `connects-to` → **[Epilepsy](../../07-system/epilepsy/README.md)** — mTOR GOF mutations (TSC1/TSC2 → tuberous sclerosis; somatic PIK3CA/MTOR → focal cortical dysplasia) are major causes of structural epilepsy; everolimus reduces TSC seizure burden ~50%; mTOR inhibitors are disease-modifying for FCD-associated drug-refractory epilepsy.
- `connects-to` → **[Autism Spectrum Disorder](../../07-system/autism-spectrum-disorder/README.md)** — mTOR hyperactivation causes syndromic ASD in TSC (TSC1/2 LOF) and PTEN hamartoma (PTEN LOF); everolimus reduces ASD severity and seizure burden in TSC; 25–35% of TSC patients have ASD; excess mTOR drives synaptic protein overproduction and E/I imbalance.

[^laplante-2012-mtor]: Laplante M, Sabatini DM. mTOR signaling in growth control and disease. *Cell.* 2012;149(2):274-293. [doi:10.1016/j.cell.2012.03.017](https://doi.org/10.1016/j.cell.2012.03.017) · [PubMed 22500797](https://pubmed.ncbi.nlm.nih.gov/22500797/)
[^heitman-1991-fkbp12]: Heitman J, Movva NR, Hall MN. Targets for cell cycle arrest by the immunosuppressant rapamycin in yeast. *Science.* 1991;253(5022):905-909. [doi:10.1126/science.1715094](https://doi.org/10.1126/science.1715094) · [PubMed 1715094](https://pubmed.ncbi.nlm.nih.gov/1715094/)
[^saxton-2017-mtor-review]: Saxton RA, Sabatini DM. mTOR Signaling in Growth, Metabolism, and Disease. *Cell.* 2017;168(6):960-976. [doi:10.1016/j.cell.2017.02.004](https://doi.org/10.1016/j.cell.2017.02.004) · [PubMed 28283069](https://pubmed.ncbi.nlm.nih.gov/28283069/)
