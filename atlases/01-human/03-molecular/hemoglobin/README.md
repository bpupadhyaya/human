---
schema: human-scale-entry/v1
id: hemoglobin
name: Hemoglobin
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-05
summary: "α₂β₂ tetramer (~64.5 kDa) carrying 4 haem-Fe²⁺ groups; binds O₂ cooperatively (Hill n≈2.7) via T↔R allostery. Bohr effect and 2,3-BPG tune O₂ delivery. HbS mutation causes sickle-cell disease; thalassaemias disrupt chain synthesis."
aliases: ["Hb", "haemoglobin", "HbA", "HbF", "HbS", "oxyhaemoglobin"]
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
cross_links:
  - target: 01-human/04-cellular/erythrocyte
    relation: part-of
    note: "Haemoglobin occupies ~33% of RBC volume (~280 million molecules/cell); O₂ capacity = 1.34 mL O₂/g Hb × 150 g/L ≈ 200 mL O₂/L blood."
  - target: 01-human/05-tissue/alveolus
    relation: modulates
    note: "Hb O₂ saturation reaches ~98% at alveolar PO₂ ~100 mmHg (sigmoidal curve); alveolar gas exchange drives T→R transition, capturing O₂ for systemic delivery."
  - target: 01-human/07-system/cardiovascular-system
    relation: modulates
    note: "Hb determines blood O₂ content; anaemia ↓ O₂ delivery → compensatory ↑ cardiac output; Hb also buffers pH (Bohr protonation) and carries CO₂ as carbamino-Hb."
  - target: 01-human/05-tissue/bone-marrow
    relation: part-of
    note: "Hb synthesis occurs in erythroid precursors (BFU-E → normoblasts → reticulocytes) in bone marrow; GATA-1/KLF1 drive globin gene expression during erythropoiesis."
  - target: 01-human/07-system/sickle-cell-disease
    relation: connects-to
    note: "HbS (β-globin E6V; GAG→GTG) causes sickle cell disease via deoxygenated HbS polymerization → RBC sickling → haemolytic anaemia + vaso-occlusion; HbF (α2γ2) inhibits HbS polymerization; hydroxyurea ↑ HbF by 15-25% → reduces painful crises."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Transferrin (TF) delivers Fe³⁺ to erythroid precursors via TFR1-mediated endocytosis → haem synthesis → haemoglobin assembly; erythropoiesis accounts for ~80% of total body iron demand (~20 mg Fe/day); iron deficiency → microcytic hypochromic anaemia from insufficient haem."
  - target: 01-human/07-system/thalassemia
    relation: connects-to
    note: "Thalassaemias arise from imbalanced α/β-globin synthesis; β-thal major: excess α chains precipitate → ineffective erythropoiesis; α-thal (3-gene deletion): HbH (β₄) unstable tetramers; gene therapies (Zynteglo: lentiviral βA-T87Q; Casgevy: CRISPR BCL11A) are FDA-approved."
  - target: 01-human/03-molecular/g6pd
    relation: connects-to
    note: "G6PD (chrXq28) is the sole NADPH source in RBCs; NADPH → glutathione → oxidant defense; G6PD deficiency → Heinz body haemolysis from denatured globin; G6PD A− and Mediterranean variants evolved as malaria protection alongside HbS and thalassaemia."
  - target: 01-human/07-system/malaria
    relation: connects-to
    note: "P. falciparum digests haemoglobin in food vacuole → haemozoin + free haem; HbAS confers ~60% protection via impaired parasite growth; HbF, HbC, and α-thalassaemia also protective; haemoglobin variants shape global Plasmodium mortality distribution."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Globin chains are carbon-backbone polypeptides; ~23% of CO₂ transported as carbamino-Hb (CO₂ reacts at α-amino termini of globin chains); Haldane effect: deoxyHb binds CO₂ 3.5× more avidly than oxyHb, enabling efficient tissue CO₂ unloading."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "Four porphyrin ring nitrogens coordinate Fe²⁺; proximal His (F8) provides fifth axial N ligand; distal His (E7) H-bonds O₂; His146β imidazole accepts CO₂-driven proton → T-state stabilisation → O₂ release in peripheral tissues (Bohr effect)."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Bohr effect: CO₂ → H⁺ → protonation of His146β → T-state stabilisation → rightward O₂ dissociation curve shift → O₂ release in exercising tissues; each 0.1 pH unit drop shifts P50 ~3 mmHg right; the Bohr effect is the molecular basis of efficient O₂ delivery."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "O₂ binds haemoglobin cooperatively at the Fe²⁺ sixth coordination site; T→R conformational transition raises O₂ affinity 300-fold across the tetramer; P50 ~26 mmHg at 37°C, pH 7.4, PCO₂ 40 mmHg; 1.34 mL O₂ can be carried per gram of fully saturated Hb."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "N–H···O=C H-bonds in each globin chain stabilise α-helical structure and define haem pocket geometry; proximal His F8 N–H bonds to the porphyrin ring nitrogen; water H-bonds modulate O₂ affinity; H atoms in globin Cα positions define Ramachandran backbone geometry."
---

# Hemoglobin

## Overview

Hemoglobin (Hb) is the principal oxygen-transport protein of red blood cells, an α₂β₂ heterotetramer of ~64.5 kDa carrying four haem prosthetic groups (protoporphyrin IX coordinated to Fe²⁺).[^stryer-biochemistry] It accounts for roughly 33% of the erythrocyte's dry mass and is responsible for binding O₂ in the pulmonary capillaries and releasing it in peripheral tissues where metabolic demand is highest. Its cooperative, sigmoid O₂-binding curve — described by a Hill coefficient of ~2.7 — distinguishes it sharply from simple (hyperbolic) O₂ carriers such as myoglobin.[^stryer-biochemistry] Beyond O₂ transport, Hb participates in CO₂ carriage (as carbamino-Hb and by facilitating bicarbonate production) and serves as an important blood pH buffer.[^alberts-mol-cell-biology]

## Structure

Each globin subunit adopts the **globin fold**: eight α-helices (labelled A–H) that cradle the haem group in a hydrophobic pocket. The iron atom of haem is held by two histidine ligands: the **proximal His F8** (covalent bond to Fe²⁺) and the **distal His E7** (hydrogen-bonding/steric gate for O₂).[^stryer-biochemistry]

The tetramer contains two distinct interfaces:
- **α1β1 / α2β2 interfaces** — tight contacts, relatively immobile between states.
- **α1β2 / α2β1 interfaces** — the regulatory switchpoint; a ~15° rotation around this interface underlies the T↔R conformational transition.[^stryer-biochemistry]

| State | Fe²⁺ position | O₂ affinity | αβ contacts |
|-------|--------------|-------------|-------------|
| **T (deoxy/taut)** | ~0.6 Å out of porphyrin plane | Low (p50 ~26 mmHg) | Tighter; stabilised by salt bridges |
| **R (oxy/relaxed)** | In-plane | High (p50 ~1 mmHg) | Loosened; salt bridges broken |

The **Monod–Wyman–Changeux (MWC) concerted model** describes allostery: all subunits switch simultaneously from T to R, and ligand binding shifts the equilibrium toward R, explaining cooperativity.[^stryer-biochemistry]

### Major Variants

| Variant | Subunit composition | Notes |
|---------|-------------------|-------|
| HbA | α₂β₂ | ~97% of adult Hb |
| HbA₂ | α₂δ₂ | ~2.5% of adult Hb; raised in β-thalassaemia |
| HbF | α₂γ₂ | Fetal; weak 2,3-BPG binding → high O₂ affinity |
| HbS | α₂β₂^(Glu6Val) | Sickle-cell; polymerises when deoxygenated |
| HbC | α₂β₂^(Glu6Lys) | Milder sickling; HbSC disease |
| HbH | β₄ | α-thalassaemia; unstable, Heinz bodies |

## Function

1. **Oxygen transport** — binds O₂ at pulmonary PO₂ (~100 mmHg, ~98% saturation) and releases it at tissue PO₂ (~40 mmHg, ~75% saturation), with steep off-loading at the mid-range of the sigmoid curve ensuring efficient delivery.[^stryer-biochemistry]

2. **CO₂ carriage** — ~20% of CO₂ is carried as carbamino-Hb (CO₂ + N-terminal α-amino groups of globin); the remainder is hydrated to HCO₃⁻ by erythrocyte carbonic anhydrase (CA-II).[^alberts-mol-cell-biology]

3. **pH buffering** — Histidine residues (pKa ~6.0) on Hb buffer protons generated during CO₂ hydration in tissues and released during O₂ uptake in the lungs.[^stryer-biochemistry]

## Mechanism

### Cooperative O₂ Binding (T↔R Allostery)

When O₂ binds Fe²⁺ in one subunit, Fe²⁺ moves into the porphyrin plane, dragging the proximal His F8 and the F-helix with it. This movement propagates through the α1β2 interface, rotating the β₁ subunit relative to α₂ and progressively loosening contacts that stabilise the T-state. Subsequent subunits bind O₂ with progressively higher affinity — the molecular basis of cooperativity.[^stryer-biochemistry]

### Bohr Effect

In actively respiring tissues:
- CO₂ + H₂O → H₂CO₃ → **H⁺** + HCO₃⁻ (carbonic anhydrase)
- H⁺ **protonates His146(β)**, forming a salt bridge: Asp94(β)···His146(β)
- Salt bridge **stabilises the T-state** → ↓ O₂ affinity → O₂ released where metabolic demand is highest
- In the lungs, CO₂ is expired → pH rises → salt bridges break → R-state restored → O₂ loaded[^stryer-biochemistry]

### 2,3-Bisphosphoglycerate (2,3-BPG)

2,3-BPG is a byproduct of the Rapoport–Luebering shunt in glycolysis, present at ~5 mM in erythrocytes. It binds exclusively in the **positively charged central cavity of deoxy-Hb (T-state)**, forming salt bridges with Val1(β), His2(β), Lys82(β), and His143(β). This stabilises the T-state and **right-shifts the O₂ dissociation curve**, ensuring O₂ delivery to tissues.[^stryer-biochemistry]

- 2,3-BPG levels **increase at altitude** and in **chronic anaemia** as a compensatory adaptation.
- **HbF (α₂γ₂)**: γ-chains have Ser at position 143 instead of His → cannot form the critical salt bridge with 2,3-BPG → **higher O₂ affinity than HbA** → fetal Hb extracts O₂ from maternal blood across the placenta.[^stryer-biochemistry]

### CO Binding

CO binds haem Fe²⁺ with ~250× greater affinity than O₂. CO-bound haem subunits also shift the remaining subunits to R-state, making them bind O₂ more tightly (left-shift of O₂ dissociation curve). The result is both reduced O₂-carrying capacity and impaired O₂ release in tissues — explaining the severity of CO poisoning.[^alberts-mol-cell-biology]

### Haem Synthesis

Haem is synthesised in erythroid precursors in a pathway spanning mitochondria and cytoplasm:
1. Glycine + succinyl-CoA → **δ-aminolevulinic acid (ALA)** — catalysed by **ALA synthase** (rate-limiting; pyridoxal phosphate cofactor; erythroid isoform: ALAS2, induced by iron and GATA-1)[^stryer-biochemistry]
2. ALA → porphobilinogen → uroporphyrinogen III → protoporphyrin IX (cytoplasm + mitochondria)
3. Fe²⁺ inserted into protoporphyrin IX by **ferrochelatase** (mitochondria) → haem
4. Haem exported to cytoplasm → assembled with globin chains

Globin gene expression during erythropoiesis is driven by transcription factors **GATA-1** and **KLF1**.[^alberts-mol-cell-biology]

## Connections

- **Part of erythrocyte** — Haemoglobin occupies ~33% of RBC volume (~280 million molecules/cell); O₂ capacity = 1.34 mL O₂/g Hb × 150 g/L ≈ 200 mL O₂/L blood. See [erythrocyte](../../04-cellular/erythrocyte/README.md).
- **Modulates alveolus** — Hb O₂ saturation reaches ~98% at alveolar PO₂ ~100 mmHg (sigmoidal curve); alveolar gas exchange drives T→R transition, capturing O₂ for systemic delivery. See [alveolus](../../05-tissue/alveolus/README.md).
- **Modulates cardiovascular system** — Hb determines blood O₂ content; anaemia ↓ O₂ delivery → compensatory ↑ cardiac output; Hb also buffers pH (Bohr protonation) and carries CO₂ as carbamino-Hb. See [cardiovascular-system](../../07-system/cardiovascular-system/README.md).
- **Part of bone marrow** — Hb synthesis occurs in erythroid precursors (BFU-E → normoblasts → reticulocytes) in bone marrow; GATA-1/KLF1 drive globin gene expression during erythropoiesis. See [bone-marrow](../../05-tissue/bone-marrow/README.md).
- `connects-to` → **[Sickle Cell Disease](../../07-system/sickle-cell-disease/README.md)** — HbS (β-globin E6V; GAG→GTG) causes sickle cell disease via deoxygenated HbS polymerization → RBC sickling → haemolytic anaemia + vaso-occlusion; HbF (α2γ2) inhibits HbS polymerization; hydroxyurea ↑ HbF by 15-25% → reduces painful crises.
- `connects-to` → **[Transferrin](../transferrin/README.md)** — Transferrin (TF) delivers Fe³⁺ to erythroid precursors via TFR1-mediated endocytosis → haem synthesis → haemoglobin assembly; erythropoiesis accounts for ~80% of total body iron demand (~20 mg Fe/day); iron deficiency → microcytic hypochromic anaemia from insufficient haem.
- `connects-to` → **[Thalassemia](../../07-system/thalassemia/README.md)** — Thalassaemias arise from imbalanced α/β-globin synthesis; β-thal major: excess α chains precipitate → ineffective erythropoiesis; α-thal (3-gene deletion): HbH (β₄) unstable tetramers; gene therapies (Zynteglo: lentiviral βA-T87Q; Casgevy: CRISPR BCL11A) are FDA-approved.
- `connects-to` → **[G6PD](../g6pd/README.md)** — G6PD (chrXq28) is the sole NADPH source in RBCs; NADPH → glutathione → oxidant defense; G6PD deficiency → Heinz body haemolysis from denatured globin; G6PD A− and Mediterranean variants evolved as malaria protection alongside HbS and thalassaemia.
- `connects-to` → **[Malaria](../../07-system/malaria/README.md)** — P. falciparum digests haemoglobin in food vacuole → haemozoin + free haem; HbAS confers ~60% protection via impaired parasite growth; HbF, HbC, and α-thalassaemia also protective; haemoglobin variants shape global Plasmodium mortality distribution.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Globin chains are carbon-backbone polypeptides; ~23% of CO₂ transported as carbamino-Hb (CO₂ reacts at α-amino termini of globin chains); Haldane effect: deoxyHb binds CO₂ 3.5× more avidly than oxyHb, enabling efficient tissue CO₂ unloading.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — Four porphyrin ring nitrogens coordinate Fe²⁺; proximal His (F8) provides fifth axial N ligand; distal His (E7) H-bonds O₂; His146β imidazole accepts CO₂-driven proton → T-state stabilisation → O₂ release in peripheral tissues (Bohr effect).
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Bohr effect: CO₂ → H⁺ → protonation of His146β → T-state stabilisation → rightward O₂ dissociation curve shift → O₂ release in exercising tissues; each 0.1 pH unit drop shifts P50 ~3 mmHg right; the Bohr effect optimises O₂ delivery to active muscle.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — O₂ binds haem Fe²⁺ cooperatively; T→R conformational transition raises O₂ affinity 300-fold across the tetramer; P50 ~26 mmHg at 37°C, pH 7.4, PCO₂ 40 mmHg; 1.34 mL O₂ can be carried per gram of fully saturated Hb.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — N–H···O=C H-bonds stabilise α-helices of each globin chain and define haem pocket geometry; proximal His F8 N–H bonds to porphyrin ring nitrogen; water H-bonds modulate O₂ affinity; H atoms in globin Cα define Ramachandran backbone geometry.

## Pathology

### Sickle Cell Disease (HbS, β-Glu6Val)
The single missense mutation (Glu→Val at β-chain position 6) creates a hydrophobic surface patch on deoxygenated HbS that interacts with a complementary hydrophobic pocket on adjacent HbS molecules. This drives **polymerisation into long fibres** that deform the erythrocyte into a rigid crescent ("sickle") shape under low-O₂ conditions.[^alberts-mol-cell-biology] Consequences: **vaso-occlusive crises** (pain, stroke, acute chest syndrome), **haemolytic anaemia** (shortened RBC survival ~10–20 days vs 120 days), and organ damage. HbS heterozygotes (HbAS, sickle-cell trait) are largely asymptomatic and are partially protected against *Plasmodium falciparum* malaria. Treatment: hydroxyurea (↑ HbF synthesis → dilutes HbS polymer), exchange transfusion, curative HSCT or gene therapy (betibeglogene autotemcel).

### Thalassaemias
Imbalanced α- or β-globin chain production:
- **α-Thalassaemia**: deletion of 1–4 α-globin genes (chr 16); HbH (β₄) forms unstable inclusions; Hb Bart's (γ₄) in hydrops fetalis (incompatible with life).[^stryer-biochemistry]
- **β-Thalassaemia**: mutations in HBB gene → ↓ (β⁺) or absent (β⁰) β-chains → excess free α-chains precipitate → haemolysis + ineffective erythropoiesis. Thalassaemia major requires lifelong transfusion ± HSCT.

### Methaemoglobinaemia
Oxidation of Fe²⁺ to **Fe³⁺** (methaemoglobin) → cannot bind O₂ → functional anaemia + left-shifted curve in remaining haem groups → tissue hypoxia, cyanosis, brown-chocolate blood. Causes: dapsone, nitrites, benzocaine, aniline dyes. Treatment: **methylene blue** → reduced by NADPH-methaemoglobin reductase (G6PD-dependent) → ascorbate reduces MetHb back to Fe²⁺.[^stryer-biochemistry]

### CO Poisoning
CO binds haem with 250× affinity over O₂; cherry-red skin/lips (COHb); headache, confusion, coma, death depending on COHb %. Treatment: 100% O₂ (competitive displacement), hyperbaric O₂ (severe cases).[^alberts-mol-cell-biology]

### Polycythaemia Vera
JAK2 V617F mutation → autonomous erythroid proliferation → ↑ Hb/haematocrit → ↑ blood viscosity → thrombosis risk. Treatment: phlebotomy, hydroxyurea, ruxolitinib (JAK2 inhibitor).

## See Also

- [ATP](../atp/README.md) — energy source for haem biosynthesis and globin synthesis in erythroid precursors
- [Erythrocyte](../../04-cellular/erythrocyte/README.md) — primary cellular compartment of Hb
- [Alveolus](../../05-tissue/alveolus/README.md) — site of Hb oxygenation
- [Bone Marrow](../../05-tissue/bone-marrow/README.md) — site of erythropoiesis and Hb synthesis
- [Cardiovascular System](../../07-system/cardiovascular-system/README.md) — Hb-laden blood circulation
- [Lung](../../06-organ/lung/README.md) — organ of gas exchange driving Hb oxygenation

[^stryer-biochemistry]: Berg JM, Tymoczko JL, Stryer L. *Biochemistry*. 9th ed. W.H. Freeman; 2019.
[^alberts-mol-cell-biology]: Alberts B, Johnson A, Lewis J, et al. *Molecular Biology of the Cell*. 7th ed. W.W. Norton; 2022.
