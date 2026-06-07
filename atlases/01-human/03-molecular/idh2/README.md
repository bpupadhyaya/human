---
schema: human-scale-entry/v1
id: idh2
name: IDH2
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "IDH2 (mitochondrial isocitrate dehydrogenase 2) catalyzes isocitrate → α-KG in the TCA cycle; IDH2 R140Q/R172K gain-of-function mutations produce 2-hydroxyglutarate → TET2/KDM inhibition → DNA hypermethylation; enasidenib is the approved IDH2 inhibitor for IDH2-mutant AML."
aliases: ["IDH2", "isocitrate dehydrogenase 2", "IDH2 R140Q", "IDH2 R172K", "2-hydroxyglutarate", "2-HG", "enasidenib", "IDH2-mutant AML", "oncometabolite"]
sources:
  - id: figueroa-2010-idh-hypermethylation
    type: peer-reviewed
    cite: "Figueroa ME, Abdel-Wahab O, Lu C, et al. Leukemic IDH1 and IDH2 mutations result in a hypermethylation phenotype, disrupt TET2 function, and impair hematopoietic differentiation. Cancer Cell. 2010;18(6):553-567."
    doi: "10.1016/j.ccr.2010.11.015"
    pmid: "21130701"
    url: "https://doi.org/10.1016/j.ccr.2010.11.015"
  - id: stein-2017-enasidenib
    type: peer-reviewed
    cite: "Stein EM, DiNardo CD, Pollyea DA, et al. Enasidenib in mutant IDH2 relapsed or refractory acute myeloid leukemia. Blood. 2017;130(6):722-731."
    doi: "10.1182/blood-2017-04-779405"
    pmid: "28588020"
    url: "https://doi.org/10.1182/blood-2017-04-779405"
cross_links:
  - target: 01-human/03-molecular/idh1
    relation: connects-to
    note: "IDH1 (cytoplasmic) and IDH2 (mitochondrial) are paralogous TCA enzymes; both produce 2-HG when mutated → TET2/KDM inhibition; ivosidenib inhibits IDH1 (AML, CCA) and enasidenib inhibits IDH2 (AML); vorasidenib inhibits IDH1/2 in grade 2 glioma."
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "IDH1/IDH2 mutations (~15%) and FGFR2 fusions (~15%) are the two main actionable targets in intrahepatic CCA; IDH1 inhibitor ivosidenib approved (ClarIDHy trial); FGFR2 inhibitors (pemigatinib, futibatinib) also approved; IDH2 mutations are rarer in CCA (~5%)."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "2-HG (produced by IDH2 mutant enzymes) competitively inhibits α-KG-dependent PHD enzymes → HIF-1α stabilization → altered metabolic reprogramming; mTOR pathway activated downstream of 2-HG via AKT; mTOR inhibitors studied in IDH2-mutant AML in combination with enasidenib."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "IDH2 mutations co-occur with DNMT3A and NPM1 in AML (IDH2+DNMT3A+NPM1 is the classic intermediate-risk triplet); TP53 co-mutation confers poor prognosis in IDH2-mutant AML; enasidenib causes differentiation syndrome (~10%) → cytokine storm from leukocyte maturation."
---

# IDH2

## Overview

**IDH2 (Isocitrate Dehydrogenase 2)** is the mitochondrial homodimeric enzyme that catalyzes the reversible oxidative decarboxylation of isocitrate to **α-ketoglutarate (α-KG)** in the TCA cycle, using NADP⁺ as cofactor: isocitrate + NADP⁺ → α-KG + CO₂ + NADPH. The normal reaction generates NADPH (for antioxidant defense and biosynthesis) and α-KG (a critical substrate for dozens of α-KG-dependent dioxygenases including TET family DNA demethylases, KDM histone demethylases, PHD prolyl hydroxylases, and collagen prolyl hydroxylases). In cancer, **IDH2 gain-of-function mutations** (hotspots R140Q/K and R172K/M/S/G in the active site) redirect the enzyme to produce **2-hydroxyglutarate (2-HG)** — an "oncometabolite" that competitively inhibits α-KG-dependent dioxygenases → TET2 and KDM inhibition → genome-wide DNA and histone hypermethylation → blocked differentiation → cancer [^figueroa-2010-idh-hypermethylation]. **Enasidenib (Idhifa)**, an allosteric IDH2 inhibitor, is FDA-approved for IDH2-mutant relapsed/refractory AML [^stein-2017-enasidenib].

**IDH2 mutations in cancer:**
- **AML:** IDH2 mutations in ~15-20% of AML; R140Q most common (~10-12%); R172K less common (~3-5%); intermediate-risk; co-mutations with DNMT3A, NPM1, FLT3; enasidenib (IDH2-selective inhibitor, FDA 2017) ORR ~40% in R/R IDH2-mutant AML; ivosidenib is IDH1-specific (not IDH2)
- **Glioma/glioblastoma:** IDH2 mutations in ~5% of grade 2-3 gliomas; IDH1 mutations (~80%) are far more common; IDH2 R172 mutant gliomas are IDH-immunohistochemically negative (R132H antibody does not detect IDH2 mutations → require sequencing); vorasidenib (IDH1/2 dual inhibitor) approved for IDH1/2-mutant grade 2 glioma (INDIGO trial)
- **Intrahepatic cholangiocarcinoma (iCCA):** IDH2 mutations in ~5% of iCCA (vs. IDH1 in ~15-20%)
- **Angioimmunoblastic T-cell lymphoma (AITL):** IDH2 R172K in ~20% of AITL; near-pathognomonic for AITL when combined with TET2/DNMT3A co-mutations; enasidenib activity in AITL under investigation
- **Chondrosarcoma:** IDH1/IDH2 mutations in ~40-70% of conventional and dedifferentiated chondrosarcoma; vorasidenib under investigation

## Structure

### IDH2 protein architecture

IDH2 is a 452-amino-acid, 47 kDa mitochondrial enzyme:

**Homodimer structure:**
IDH2 functions as a homodimer (2×452 aa); each subunit contains large and small β-sandwich domains + regulatory domain; the active site is at the dimer interface (shares some architecture with IDH1 but is structurally distinct); NADP⁺ and Mg²⁺ coordinate in the active site.

**Catalytic mechanism:**
1. Isocitrate binding → Arg140 (via guanidinium) and Arg172 (via backbone NH) contact the β-carboxylate of isocitrate
2. NADP⁺ hydride acceptance → β-ketoisocitrate (β-KI) intermediate
3. Decarboxylation → α-KG + CO₂ + NADPH

**R140Q mutation:**
Arg140→Gln → active site loses ability to bind isocitrate β-carboxylate tightly → α-KG becomes substrate (partial neomorphic activity) → enzyme catalyzes: α-KG + NADPH → 2-HG + NADP⁺; IDH2 R140Q is the dominant mutation; produces modest but steady-state 2-HG accumulation.

**R172K/M/S mutations:**
Arg172→Lys/Met/Ser → more severe disruption of active site → larger amounts of 2-HG per enzyme; R172K associated with more aggressive AML phenotype.

**Enasidenib binding (allosteric):**
Enasidenib (AG-221) binds at the IDH2 homodimer interface, in an allosteric pocket different from the active site → stabilizes inactive conformation → prevents NADPH binding required for neomorphic 2-HG production; does NOT compete with isocitrate/α-KG in the active site → entirely allosteric; IC50 IDH2 R140Q: ~100 nM; selective for IDH2 over IDH1.

### 2-Hydroxyglutarate mechanism of oncogenesis

**2-HG as competitive inhibitor of α-KG-dependent dioxygenases:**
2-HG is structurally similar to α-KG (hydroxyl group at C2 instead of carbonyl) → competitive inhibition of all α-KG-dependent dioxygenases at physiological concentrations (50-100 mM 2-HG in IDH-mutant tumors vs. ~100 μM normal):
- **TET2, TET1, TET3 (5mC→5hmC demethylases):** Inhibited → DNA hypermethylation (CpG island methylation phenotype, CIMP) → gene silencing → epigenetic lock on differentiation genes
- **KDM histone lysine demethylases (JMJD subfamily):** Inhibited → histone H3K9me3, H3K27me3 accumulation → Polycomb reprogramming → differentiation block
- **PHD1/2/3 (prolyl hydroxylases):** Partially inhibited → HIF-1α stabilization → HIF target gene expression (VEGF, GLUT1)
- **Collagen prolyl hydroxylase:** Not significantly inhibited at tumor 2-HG concentrations

## Function

### Normal IDH2 role in TCA cycle and mitochondrial metabolism

**NADPH production:**
IDH2 is one of two principal NADPH sources in mitochondria (the other being NADP⁺-linked malic enzyme, ME3). Mitochondrial NADPH fuels: glutathione reductase → GSH → antioxidant defense; thioredoxin reductase → antioxidant; IDH2 activity is essential for mitochondrial ROS neutralization. IDH2-deficient cells → ROS accumulation → DNA damage → genomic instability.

**TCA carbon flux:**
Isocitrate → α-KG → succinyl-CoA → NADH → Complex I of ETC → ATP synthesis; IDH2 is the rate-limiting step; IDH2 loss-of-function (in non-mutant cells) would impair NADPH production and TCA flux — this is why IDH2 mutations in cancer paradoxically preserve some residual normal IDH2 activity (R140Q is neomorphic, not null).

### IDH2-mutant AML biology

**Differentiation block:**
2-HG → TET2 inhibition → hypermethylation of differentiation-inducing genes (CEBPA, PU.1, HIF pathway regulators) → myeloid progenitors cannot complete differentiation → accumulation of early myeloid blasts → AML. This is analogous to DNMT3A mutations and TET2 mutations (all converge on epigenetic dysregulation).

**Differentiation therapy with enasidenib:**
Enasidenib inhibits 2-HG production → TET2 activity restored → hypermethylation partially reversed → myeloid differentiation resumes → AML blasts mature into neutrophils → clinical remission. This is a paradigm of oncometabolite-targeted differentiation therapy (analogous to ATRA in APL). **Differentiation syndrome:** In ~10% of patients → rapid maturation of leukemic blasts → cytokine storm → fever, pulmonary infiltrates, hypotension → manage with dexamethasone.

## Mechanism

### Enasidenib (IDH2 inhibitor) in AML

**Phase 1/2 trial (AG221-C-001):** [^stein-2017-enasidenib]
- 239 R/R IDH2-mutant AML patients; enasidenib 100 mg/day
- ORR: 40.3% (CR 19.3%); median DOR 5.6 months; median OS 9.3 months overall; OS 19.7 months for responders
- Toxicities: Nausea/vomiting, diarrhea, hyperbilirubinemia (IDH2 in bilirubin metabolism); differentiation syndrome ~10%
- FDA approved August 2017 for R/R IDH2-mutant AML (2nd drug approved for an IDH mutation in AML)

**Enasidenib in newly diagnosed AML (BEAT-AML trial subset):**
Enasidenib ± azacitidine in newly diagnosed IDH2-mutant AML (ineligible for intensive chemo): ORR ~50-65%; azacitidine combination superior to enasidenib alone

**Resistance to enasidenib:**
- IDH2 R172S/G secondary mutations → resistance to enasidenib (change enasidenib binding pocket)
- IDH1 R132 secondary mutation (trans switching): IDH2-mutant AML acquires IDH1 mutation → 2-HG continues from IDH1 isoform → enasidenib resistance → add ivosidenib or switch to vorasidenib
- RAS/MAPK pathway mutations (NRAS, KRAS): Bypass differentiation → proliferative relapse
- BCL-2: Venetoclax + enasidenib combination (SYNERGY trial): ORR ~70% → highly active; FDA under review

### IDH2 mutations in AITL

IDH2 R172K is nearly pathognomonic for AITL when found in combination with TET2 loss (75-80% of IDH2-mutant AITL also have TET2 mutations), DNMT3A mutations (~35%), and RHOA G17V (~65%). IDH2 mutations in AITL arise in a pre-malignant TET2/DNMT3A-mutant TFH (T follicular helper) cell → 2-HG + epigenetic dysregulation → AITL initiation. Enasidenib shows early clinical activity in R/R AITL (case reports/Phase 1 data).

## Connections

- `connects-to` → **[IDH1](../../03-molecular/idh1/README.md)** — IDH1 (cytoplasmic) and IDH2 (mitochondrial) are paralogous TCA enzymes; both produce 2-HG when mutated → TET2/KDM inhibition; ivosidenib inhibits IDH1 (AML, CCA) and enasidenib inhibits IDH2 (AML); vorasidenib inhibits IDH1/2 in grade 2 glioma.
- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — IDH1/IDH2 mutations (~15%) and FGFR2 fusions (~15%) are the two main actionable targets in intrahepatic CCA; IDH1 inhibitor ivosidenib approved (ClarIDHy trial); FGFR2 inhibitors (pemigatinib, futibatinib) also approved; IDH2 mutations are rarer in CCA (~5%).
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — 2-HG (produced by IDH2 mutant enzymes) competitively inhibits α-KG-dependent PHD enzymes → HIF-1α stabilization → altered metabolic reprogramming; mTOR pathway activated downstream of 2-HG via AKT; mTOR inhibitors studied in IDH2-mutant AML in combination with enasidenib.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — IDH2 mutations co-occur with DNMT3A and NPM1 in AML (IDH2+DNMT3A+NPM1 is the classic intermediate-risk triplet); TP53 co-mutation confers poor prognosis in IDH2-mutant AML; enasidenib causes differentiation syndrome (~10%) → cytokine storm from leukocyte maturation.

[^figueroa-2010-idh-hypermethylation]: Figueroa ME, Abdel-Wahab O, Lu C, et al. Leukemic IDH1 and IDH2 mutations result in a hypermethylation phenotype, disrupt TET2 function, and impair hematopoietic differentiation. *Cancer Cell.* 2010;18(6):553-567. [doi:10.1016/j.ccr.2010.11.015](https://doi.org/10.1016/j.ccr.2010.11.015) · [PubMed 21130701](https://pubmed.ncbi.nlm.nih.gov/21130701/)
[^stein-2017-enasidenib]: Stein EM, DiNardo CD, Pollyea DA, et al. Enasidenib in mutant IDH2 relapsed or refractory acute myeloid leukemia. *Blood.* 2017;130(6):722-731. [doi:10.1182/blood-2017-04-779405](https://doi.org/10.1182/blood-2017-04-779405) · [PubMed 28588020](https://pubmed.ncbi.nlm.nih.gov/28588020/)
