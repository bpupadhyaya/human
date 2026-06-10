---
schema: human-scale-entry/v1
id: nitrogen
name: Nitrogen
atlas: 01-human
scale: 02-atomic
status: draft
last_reviewed: 2026-06-05
summary: "N, atomic number 7. Third most abundant element by body mass (~3%). Present in every amino acid (α-amino group, peptide bond), every nucleotide base, and in haem. Atmospheric N₂ is inaccessible; biological nitrogen derives entirely from dietary protein."
aliases: ["N", "nitrogen-14", "¹⁴N", "amide nitrogen", "amino group", "nitric oxide"]
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
  - target: 01-human/08-whole-body/human-body
    relation: part-of
    note: "Nitrogen is ~3% of body mass (~2.1 kg in a 70 kg adult), present in every protein (α-amino groups, peptide bonds), every nucleotide base (purine and pyrimidine rings), haem porphyrin rings, creatine, urea, and hundreds of metabolites and signalling molecules."
  - target: 01-human/03-molecular/atp
    relation: part-of
    note: "Adenine contains 5 nitrogen atoms: N1, N3, N7, N9 (purine ring) and exocyclic amino N6. The ring nitrogens engage in hydrogen bonding with kinase active sites, essential for adenine recognition by ATP-binding proteins. N9 links adenine to ribose via the glycosidic bond."
  - target: 01-human/03-molecular/hemoglobin
    relation: part-of
    note: "Four porphyrin ring nitrogens coordinate Fe²⁺ in haem; proximal His87/92 (F8) provides fifth axial N ligand; distal His58/63 (E7) H-bonds O₂; His146β Bohr effect: CO₂-driven imidazole protonation stabilises T-state → O₂ release in tissues."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "Colonic bacteria hydrolyse urea (urease-positive species) and ferment amino acids → ammonia and SCFAs; negative nitrogen balance in malnutrition impairs gut mucosal renewal; dietary protein nitrogen drives microbiome composition and diversity."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "iNOS in activated macrophages and neutrophils produces sustained high-level NO for pathogen killing; reactive nitrogen species (ONOO⁻ from NO + O₂⁻; N₂O₃) damage bacterial membranes and DNA; iNOS expression requires LPS + IFN-γ via NF-κB/STAT1."
---

# Nitrogen

## Overview

Nitrogen (symbol N, atomic number 7, atomic mass 14.007 u) is the most abundant element in Earth's atmosphere (78.1% of air by volume as N₂) yet, paradoxically, it is one of the most commonly deficient nutrients in biology. This paradox arises from the extraordinary stability of the dinitrogen triple bond (N≡N, bond dissociation energy 945 kJ/mol) — mammals cannot break it, and only specialised nitrogen-fixing microorganisms (Rhizobium, Azotobacter, and others) possess the nitrogenase enzyme complex that can do so under ambient conditions.

In the human body, nitrogen is the **third most abundant element by mass** (~3%), present in every protein, every nucleic acid, every porphyrin (haem, chlorophyll), and numerous signalling molecules including the gaseous second messenger nitric oxide (NO). All biological nitrogen in humans originates from dietary protein (or, indirectly, from the biosphere's nitrogen fixation cycle) [^stryer-biochemistry].

Nitrogen's biological importance was recognised with the identification of proteins as nitrogen-containing polymers in the early nineteenth century (Mulder, 1838 — who coined the term "protein"). Kjeldahl's 1883 method for total nitrogen determination became the standard proxy for protein content in foods and tissues. The biochemistry of nitrogen assimilation, urea cycle, and nucleotide synthesis was elucidated through the mid-twentieth century (Krebs and Henseleit, 1932; Buchanan and Hartman on nucleotide biosynthesis).

## Structure

### Atomic Properties

| Property | Value |
|:---|:---|
| Atomic number (Z) | 7 |
| Atomic mass | 14.007 u |
| Electron configuration | [He] 2s² 2p³ |
| Valence electrons | 5 |
| Electronegativity (Pauling) | 3.04 |
| Covalent radius | 71 pm |
| Common oxidation states | −3 (amines, amides), 0 (N₂), +1 to +5 (oxides, nitrate) |
| Principal isotopes | ¹⁴N (99.6%), ¹⁵N (0.4%) |

### Nitrogen Hybridisation and Bonding

Nitrogen has five valence electrons, enabling:

- **sp³ hybridisation (pyramidal):** Amines (R–NH₂, R₂NH, R₃N). The lone pair occupies one sp³ orbital, making amines nucleophilic bases. The α-amino group of amino acids (–NH₃⁺ at physiological pH, pKₐ ~9–10) and the ε-amino group of lysine (~pKₐ 10.5) are sp³ nitrogens.

- **sp² hybridisation (planar):** Amides (–CO–NH–) and aromatic ring nitrogens. The peptide bond nitrogen is sp² hybridised: its lone pair is delocalised into the adjacent C=O π system (resonance), giving the peptide bond partial double-bond character and constraining it to a plane. This is the structural basis of protein secondary structure (α-helices and β-sheets depend on planar, trans peptide bonds).

- **sp hybridisation (linear):** Nitriles (C≡N), found in cyanide and some alkaloids, but rare in normal metabolites.

- **Aromatic nitrogen:** In purine and pyrimidine bases. Imidazole ring of histidine (pKₐ ~6.0) — uniquely placed near physiological pH — allows histidine to act as proton donor or acceptor in enzyme catalysis (serine proteases, carbonic anhydrase, haemoglobin Bohr effect).

### Biological Nitrogen Species and Their pKₐ Values

| Species | Example | pKₐ | Protonation state at pH 7.4 |
|:---|:---|:---:|:---|
| α-Amino group | All amino acids | ~9.0 | –NH₃⁺ (protonated) |
| ε-Amino group | Lysine side chain | ~10.5 | –NH₃⁺ (protonated) |
| Imidazole | Histidine side chain | ~6.0 | Mostly –NH– (unprotonated; ready to act as base) |
| Guanidinium | Arginine side chain | ~12.5 | –NH₂⁺= (fully protonated, permanent positive charge at physiol. pH) |
| Amide | Glutamine, asparagine | ~0 | Neutral (essentially non-ionisable at physiol. pH) |

## Function

### Nitrogen in Proteins

Every amino acid contains nitrogen in at minimum two positions: the α-amino group (–NH₂/–NH₃⁺) and the α-amino group's participation in the peptide bond after condensation. The peptide bond is:

**–CO–NH– (from –COOH + H₂N–)**

In a 300-residue protein, there are 299 peptide bonds, each containing one nitrogen. The side chains of glutamine, asparagine, lysine, arginine, histidine, tryptophan, proline contribute additional nitrogens. A typical protein has ~16% nitrogen by mass — the basis of the Kjeldahl protein factor of 6.25 (100 ÷ 16 = 6.25, multiplying measured %N gives estimated %protein) [^stryer-biochemistry].

**Nitrogen in protein function:**
- **Lysine:** ε-NH₂ forms covalent aldimines (Schiff bases) with carbonyl substrates; involved in pyridoxal phosphate-dependent reactions; acetylated in chromatin regulation by HATs/HDACs.
- **Arginine:** Guanidinium group forms bidentate hydrogen bonds and ion pairs with phosphate groups; critical in ATP-binding sites, DNA-binding domains, and cell-penetrating peptide sequences.
- **Histidine:** pKₐ near 6.0 makes it uniquely suited for proton relay in enzyme active sites and haemoglobin allosteric regulation (Bohr effect: CO₂-driven protonation of His146(β) stabilises the T-state, promoting O₂ release in tissues).
- **Tryptophan:** Indole ring nitrogen (barely ionisable) forms H-bonds; tryptophan is the precursor of serotonin and melatonin via hydroxylation and decarboxylation.

### Nitrogen in Nucleic Acids

Both purines (adenine, guanine) and pyrimidines (cytosine, thymine, uracil) are nitrogen-containing heterocycles [^alberts-mol-cell-biology]:

- **Adenine:** C₅H₅N₅ — five nitrogen atoms (4 ring, 1 exocyclic amino).
- **Guanine:** C₅H₅N₅O — five nitrogen atoms (4 ring, 1 exocyclic amino; 1 keto oxygen).
- **Cytosine:** C₄H₅N₃O — three nitrogen atoms.
- **Thymine:** C₅H₆N₂O₂ — two nitrogen atoms.
- **Uracil:** C₄H₄N₂O₂ — two nitrogen atoms.

Watson-Crick base pairing is entirely mediated by the hydrogen bond donors and acceptors provided by the nitrogen (and oxygen) atoms of the bases. The nitrogen atoms also accept metal ions (e.g., N7 of guanine is the primary Mg²⁺ and cisplatin coordination site) and are the sites of alkylation by mutagenic and chemotherapeutic agents.

### Nitrogen in Haem

Haem is an iron-porphyrin complex in which iron is coordinated by the four pyrrole nitrogens of the porphyrin ring. In haemoglobin and myoglobin:
- The four porphyrin nitrogens hold Fe²⁺ in the plane of the haem.
- A fifth axial ligand is the **proximal histidine** (His87, His92) of the globin protein.
- The sixth coordination site is vacant in deoxyhaemoglobin and occupied by O₂ in oxyhaemoglobin.

The T→R allosteric transition of haemoglobin depends on the movement of Fe²⁺ relative to the porphyrin plane upon O₂ binding — a nitrogen-mediated geometry change that propagates through the protein to the subunit interface, generating cooperativity.

### Nitrogen Metabolism and the Urea Cycle

Humans cannot excrete free ammonia (NH₃) — it is neurotoxic at micromolar concentrations. Instead, amino acid catabolism generates NH₄⁺ which enters the urea cycle (hepatic periportal cells):

1. **Carbamoyl phosphate synthetase I (CPS I):** NH₄⁺ + CO₂ + 2ATP → carbamoyl phosphate (mitochondria).
2. **Ornithine transcarbamylase (OTC):** Carbamoyl phosphate + ornithine → citrulline.
3. **Argininosuccinate synthetase:** Citrulline + aspartate + ATP → argininosuccinate (cytosol). *The second nitrogen of urea enters here via aspartate.*
4. **Argininosuccinate lyase:** Argininosuccinate → arginine + fumarate.
5. **Arginase I:** Arginine + H₂O → urea + ornithine.

Net: 2 NH₄⁺ + CO₂ → urea (H₂N–CO–NH₂) + H₂O. Urea (2 nitrogens per molecule) is synthesised at ~20–30 g/day in an adult on a typical protein diet and excreted by the kidney [^stryer-biochemistry].

### Nitric Oxide (NO) — A Nitrogen-Based Gaseous Signalling Molecule

Nitric oxide (NO), a radical gas with one nitrogen and one oxygen, is synthesised from arginine by NO synthase (NOS) isoforms:

- **eNOS (endothelial):** Shear stress → eNOS → NO → diffuses to vascular smooth muscle → activates soluble guanylyl cyclase → cGMP → PKG → myosin light chain phosphatase → relaxation → vasodilation.
- **nNOS (neuronal):** Ca²⁺/calmodulin-activated NO production in neurons; NO is a retrograde neurotransmitter modulating synaptic plasticity.
- **iNOS (inducible):** Expressed in macrophages after LPS/IFN-γ stimulation; produces sustained, high-level NO for pathogen killing (reactive nitrogen species: ONOO⁻, N₂O₃).

### Nucleotide Biosynthesis — Nitrogen Sources

De novo purine synthesis (10 steps) assembles the purine ring using glycine (C2, N1), glutamine amide N (N3, N9), aspartate amino N (N1), formyl-THF (C2, C8), and CO₂. De novo pyrimidine synthesis uses carbamoyl phosphate (N1 of pyrimidine) and aspartate. These nitrogen sources — all derived ultimately from dietary amino acids — link protein intake to nucleotide availability, cell division rate, and immune function.

## Connections

- `part-of` → **[Human Body](../../08-whole-body/human-body/README.md)** — Nitrogen is ~3% of body mass (~2.1 kg in a 70 kg adult); every protein contains ~16% N; nucleic acids, creatine, urea, and porphyrins account for the remainder.
- `part-of` → **[ATP](../../03-molecular/atp/README.md)** — Adenine's 5 nitrogen atoms (N1, N3, N7, N9 in the purine ring; exocyclic N6) provide the hydrogen-bonding geometry essential for recognition by all ATP-binding kinases, the ribosome, and every ATP-utilising enzyme.
- `part-of` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Four porphyrin ring nitrogens coordinate Fe²⁺ in haem; proximal His (F8) provides fifth axial N ligand; distal His (E7) H-bonds O₂; His146β imidazole drives the Bohr effect (CO₂ → T-state → O₂ release in tissues).
- `connects-to` → **[Gut Microbiome](../../07-system/gut-microbiome/README.md)** — Colonic bacteria hydrolyse urea and ferment amino acids → ammonia and SCFAs; negative nitrogen balance impairs gut mucosal renewal; dietary protein nitrogen is the primary driver of microbiome composition.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — iNOS in activated neutrophils and macrophages produces sustained high-level NO for pathogen killing; ONOO⁻ (NO + O₂⁻) and N₂O₃ damage bacterial membranes and DNA; iNOS induction requires LPS + IFN-γ via NF-κB/STAT1.

## Pathology

| Condition | Nitrogen mechanism |
|:---|:---|
| **Urea cycle defects (OTC deficiency)** | Accumulation of NH₄⁺ → cerebral oedema, encephalopathy; most common urea cycle disorder (X-linked); treated with protein restriction, arginine supplementation, benzoate/phenylacetate (alternative N excretion) |
| **Gout** | Overproduction or underexcretion of uric acid (the end product of purine catabolism — nitrogen-rich); deposition of MSU crystals in joints triggers NLRP3 inflammasome |
| **Nitric oxide deficiency in vascular disease** | eNOS uncoupling (tetrahydrobiopterin deficiency) → reduced NO → impaired vasodilation → endothelial dysfunction → atherosclerosis progression |
| **Sepsis** | iNOS-derived excess NO → pathological vasodilation, hypotension, multi-organ failure; NOS inhibitors tested as adjunctive treatment |
| **Nitrogen narcosis** | At depth, N₂ dissolved in neural membranes at elevated partial pressure → narcotic effect (Meyer-Overton theory: non-polar narcotic dissolves in lipid bilayer N–C environment) |
| **Protein-energy malnutrition** | Dietary protein insufficiency → negative nitrogen balance → muscle wasting (sarcopenia, kwashiorkor) |

## Open Questions

- **Nitrogen sensing and mTORC1:** The mTOR complex 1 pathway integrates amino acid (nitrogen) availability to regulate protein synthesis and autophagy. The molecular mechanism by which intracellular amino acid concentrations are sensed (Ragulator-Rag GTPase complex, lysosomal amino acid transporter SNAT7, GATOR1/2 complexes) is still being elucidated.
- **NOX-independent NO synthesis:** Recent evidence suggests non-enzymatic NO generation from nitrite under hypoxic/acidic conditions (xanthine oxidoreductase, myoglobin, deoxyhaemoglobin as nitrite reductases). The physiological importance of this pathway in ischaemic cardioprotection is under investigation.

## See Also

- [Human Body](../../08-whole-body/human-body/README.md) — nitrogen's macroscopic context.
- [ATP](../../03-molecular/atp/README.md) — adenine's nitrogen ring is essential for universal energy currency function.
- [IL-6](../../03-molecular/il-6/README.md) — a nitrogen-rich cytokine signalling molecule.

[^stryer-biochemistry]: Berg JM, Tymoczko JL, Stryer L. *Biochemistry.* 9th ed. W.H. Freeman; 2019. [macmillanlearning.com](https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X)
[^alberts-mol-cell-biology]: Alberts B, Johnson A, Lewis J, et al. *Molecular Biology of the Cell.* 7th ed. W.W. Norton; 2022. [ncbi.nlm.nih.gov/books/NBK26880](https://www.ncbi.nlm.nih.gov/books/NBK26880/)

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
