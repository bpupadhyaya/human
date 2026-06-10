---
schema: human-scale-entry/v1
id: sulfur
name: Sulfur
atlas: 01-human
scale: 02-atomic
status: draft
last_reviewed: 2026-06-05
summary: "Sulfur (S, Z=16, [Ne] 3s² 3p⁴). ~0.25% body mass (~175g); found in cysteine (thiol –SH), methionine (thioether), glutathione, CoA, SAM, iron-sulfur clusters, and sulfated glycosaminoglycans. Major antioxidant and methyl-donor element."
aliases: ["S", "sulphur", "thiol", "disulfide", "sulfate"]
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
cross_links:
  - target: 01-human/08-whole-body/human-body
    relation: part-of
    note: "~0.25% body mass (~175g); sulfur present in cysteine, methionine, taurine, heparan sulfate, iron-sulfur clusters, and coenzyme A — present in virtually every cell type and tissue."
  - target: 01-human/04-cellular/hepatocyte
    relation: part-of
    note: "Hepatocytes are the primary site of glutathione synthesis, SAM production, cytochrome P450 activity (cysteine-thiolate axial ligand at active site), and sulfotransferase-mediated phase II xenobiotic conjugation."
  - target: 01-human/03-molecular/il-6
    relation: modulates
    note: "S-nitrosylation and oxidation of cysteine residues on JAK1/JAK2 and STAT3 modulate IL-6 receptor signal transduction, making redox sulfur chemistry a regulator of the JAK–STAT3 inflammatory pathway."
  - target: 01-human/06-organ/liver
    relation: modulates
    note: "GSH-dependent detoxification (via GPx, GSTs) and sulfotransferases (SULT enzymes) conjugating xenobiotics and hormones constitute the liver's sulfur-driven phase II metabolic detoxification capacity."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "Glutathione (γ-Glu-Cys-Gly) and the methionine cycle (SAM → SAH → homocysteine → methionine) combine sulfur and nitrogen chemistry in the same pathways; Cys and Met amino acids contain both elements; SAM methyl groups regulate nitrogen-containing bases in DNA and RNA."
  - target: 01-human/03-molecular/nf-kb
    relation: modulates
    note: "IKKβ Cys179 oxidation by H₂O₂ inhibits NF-κB activation — cysteine thiol redox state acts as a molecular brake on inflammation; GSH maintains IKK in the reduced/active state; ROS depletion of GSH → IKK oxidation → paradoxical NF-κB activation in some cancer contexts."
  - target: 01-human/03-molecular/antithrombin
    relation: connects-to
    note: "Heparin (highly sulfated heparan sulfate analogue) activates antithrombin III ~1000-fold by allosteric conformational change; sulfate groups create the charge template for antithrombin binding — the molecular basis of heparin anticoagulation, the most widely used sulfated drug."
---

# Sulfur

## Overview

Sulfur (symbol S, atomic number 16, atomic mass 32.06 u) is a nonmetallic element in Group 16 of the periodic table, with ground-state electron configuration [Ne] 3s² 3p⁴. It accounts for approximately **0.25% of body mass** (~175 g in a 70 kg adult). Although less abundant than phosphorus, sulfur is biologically indispensable because of the unique chemistry of the thiol (–SH) group: its nucleophilicity, capacity for reversible oxidation to disulfides (–S–S–), and ability to form thioester bonds are exploited in catalysis, antioxidant defense, protein structure, methylation, and extracellular matrix architecture [^stryer-biochemistry].

In contrast to phosphorus (which functions almost exclusively as phosphate at oxidation state +5), sulfur in biology spans a remarkable range of oxidation states from −2 (thiols, thioethers) through 0 (elemental, in disulfides formally), to +6 (sulfate, –OSO₃⁻). This redox flexibility is a key feature: the cell uses sulfur-containing molecules as sensors of oxidative stress, electron carriers in the electron transport chain, and donors of methyl groups for epigenetic regulation.

## Structure

### Atomic Properties

| Property | Value |
|:---|:---|
| Atomic number (Z) | 16 |
| Atomic mass | 32.06 u |
| Electron configuration | [Ne] 3s² 3p⁴ |
| Common valence | −2 (thiols), +4 (sulfinates), +6 (sulfates) |
| Electronegativity (Pauling) | 2.58 |
| Covalent radius | 105 pm |
| van der Waals radius | 180 pm |

### Key Sulfur-Containing Biomolecules

| Molecule | Sulfur form | Location/function |
|:---|:---|:---|
| Cysteine | Thiol (–SH), pKa ~8.3 | Protein active sites; disulfide bonds in ER-secreted proteins |
| Methionine | Thioether (–S–CH₃) | Protein N-terminal processing; SAM precursor |
| Glutathione (GSH) | Thiol (γ-Glu-Cys-Gly) | Major cellular antioxidant (~1–10 mmol/L cytoplasm) |
| Coenzyme A | Thiol (pantetheine –SH) | Acyl carrier (acetyl-CoA, malonyl-CoA, succinyl-CoA) |
| SAM | Sulfonium (–S⁺–) | Universal methyl donor; DNA, histone, neurotransmitter methylation |
| [Fe-S] clusters | Inorganic sulfide (S²⁻) | Electron carriers in ETC Complexes I, II, III; aconitase |
| Heparan sulfate | Sulfate ester (–OSO₃⁻) | ECM polyanion; binds FGF, VEGF, antithrombin III |
| Taurine | Sulfonate (–SO₃⁻) | Bile acid conjugation; neuromodulation; osmoregulation |

## Function

### Cysteine Thiol — Nucleophile and Redox Sensor

The cysteine thiol (–SH, pKa ~8.3) is one of the most chemically reactive functional groups in proteins. At physiological pH, a significant fraction exists as the thiolate anion (–S⁻), making it a potent nucleophile in:

- **Enzyme catalysis**: papain, caspases, ubiquitin-conjugating enzymes (E1/E2/E3), protein tyrosine phosphatases (PTPs), glyceraldehyde-3-phosphate dehydrogenase (GAPDH) all use cysteine as the catalytic nucleophile.
- **Disulfide bond formation**: in the oxidative environment of the ER lumen, protein disulfide isomerase (PDI) catalyses formation of –S–S– bonds that stabilize the tertiary and quaternary structure of secreted and membrane proteins — immunoglobulins, albumin, insulin, coagulation factors all depend on correct disulfide pairing.
- **Redox sensing**: cysteines in transcription factors (NF-κB, Nrf2/Keap1 complex, AP-1) are reversibly oxidized by reactive oxygen/nitrogen species (ROS/RNS), acting as molecular switches that link oxidative stress to gene expression [^stryer-biochemistry].

### Glutathione — the Cellular Antioxidant Hub

Glutathione (GSH, γ-Glu-Cys-Gly) is the most abundant low-molecular-weight thiol in eukaryotic cells, typically maintained at 1–10 mmol/L in the cytoplasm. The cysteine thiol is the functional moiety:

**Antioxidant cycle:**
1. 2 GSH + H₂O₂ → GSSG + 2 H₂O (catalysed by **glutathione peroxidase, GPx**)
2. GSSG + NADPH + H⁺ → 2 GSH (catalysed by **glutathione reductase, GR**)
3. Net: NADPH (from pentose phosphate pathway) is consumed to regenerate GSH

**Detoxification:** glutathione S-transferases (GSTs) conjugate GSH to electrophilic xenobiotics (drugs, carcinogens), creating water-soluble conjugates for renal/biliary excretion — phase II metabolism. Hepatocytes, which express the highest GST activities, are the primary site of this reaction.

**Protein S-glutathionylation**: a reversible post-translational modification in which GSH forms a mixed disulfide with protein cysteines — protects critical Cys residues from irreversible oxidation and modulates protein activity during oxidative stress.

### Iron-Sulfur Clusters — Electron Carriers of the ETC

Iron-sulfur (Fe-S) clusters are ancient co-factors present in the core subunits of Complexes I, II, and III of the mitochondrial electron transport chain (ETC), as well as in aconitase (TCA cycle) and ferredoxins. The clusters exist in two main forms:

- **[2Fe-2S]** (Rieske center in Complex III, ferredoxins)
- **[4Fe-4S]** (Complexes I, II, and aconitase)

In each case, bridging inorganic sulfide (S²⁻) ligates the iron atoms, forming a cubane or rhombus structure that accepts and donates single electrons over a defined redox potential range (~−450 mV to +350 mV). The sequential relay of electrons through these clusters constitutes the electron transport chain's wiring between NADH/FADH₂ and the final acceptor O₂ [^stryer-biochemistry].

### Coenzyme A — the Acyl Carrier

Coenzyme A (CoA) contains a pantetheine unit ending in a **thiol group** (–SH). Acylation of this thiol to form thioester bonds (acyl-CoA, e.g., acetyl-CoA, malonyl-CoA, succinyl-CoA) is the key strategy by which the cell activates acyl groups for transfer:

- **Acetyl-CoA**: central metabolic junction — enters TCA cycle (citrate synthase), provides acetyl groups for histone acetyltransferases (HATs), initiates cholesterol/isoprenoid synthesis (HMG-CoA reductase pathway), and serves as substrate for fatty acid synthase (FAS).
- **Malonyl-CoA**: the committed substrate of fatty acid synthesis; allosteric inhibitor of CPT-1, preventing β-oxidation when synthesis is active.
- **Succinyl-CoA**: TCA cycle intermediate; precursor of haem biosynthesis (ALA synthase) and propionyl-CoA metabolism.

The thioester bond is energy-rich (~31 kJ/mol hydrolysis energy), comparable to ATP phosphoanhydride bonds — this is why thioester-linked acyl groups are "activated" for condensation reactions in biosynthesis.

### SAM — the Universal Methyl Donor

S-adenosylmethionine (SAM) is formed from methionine and ATP (releasing PPi + Pi). The sulfonium ion (–S⁺–CH₃) makes the methyl group highly electrophilic, enabling **transmethylation** to over 100 acceptor substrates:

- **DNA methylation**: DNA methyltransferases (DNMT1, DNMT3A/B) add CH₃ to cytosine C-5 in CpG dinucleotides — silencing gene promoters, imprinting loci, and maintaining heterochromatin.
- **Histone methylation**: H3K27me3 (PRC2/EZH2), H3K9me3 (G9a/EHMT2), H3K4me3 (MLL complexes) — all use SAM; links sulfur/methionine metabolism to chromatin state.
- **Neurotransmitter methylation**: phenylethanolamine N-methyltransferase (PNMT) converts norepinephrine → epinephrine in adrenal medulla, using SAM.
- **Polyamine synthesis**: SAM is the propylamine donor for spermidine and spermine synthesis — critical for cell proliferation.

### Sulfated Glycosaminoglycans — Extracellular Matrix

Heparan sulfate (HS) and chondroitin sulfate (CS) are glycosaminoglycans (GAGs) in which the repeating disaccharide units carry sulfate esters (O-sulfate and N-sulfate groups added by sulfotransferases). The resulting polyanionic chains:

- **Bind and present growth factors**: FGF2, VEGF, BMP, Wnt, HGF all bind heparan sulfate proteoglycans (HSPGs such as syndecan, glypican) — modulating receptor access and signal range.
- **Anticoagulation**: heparin (a highly sulfated HS analogue) activates antithrombin III ~1,000-fold by inducing an allosteric conformational change.
- **Water retention**: sulfate groups and carboxylates provide fixed negative charges that generate Donnan osmotic pressure in cartilage ECM, resisting compressive load.
- **Tissue integrity**: chondroitin sulfate and dermatan sulfate are core components of aggrecan (cartilage), versican (vasculature), and basement membranes [^guyton-hall].

## Connections

- `part-of` → **[Human Body](../../08-whole-body/human-body/README.md)** — ~0.25% body mass (~175 g); sulfur present in cysteine, methionine, taurine, heparan sulfate, iron-sulfur clusters, coenzyme A, and glutathione — found in virtually every cell type and tissue throughout the body.
- `part-of` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — hepatocytes are the primary site of glutathione synthesis, SAM production, cytochrome P450 activity (cysteine-thiolate axial ligand at the P450 haem active site), and sulfotransferase-mediated phase II xenobiotic and hormone conjugation.
- `modulates` → **[IL-6](../../03-molecular/il-6/README.md)** — S-nitrosylation and oxidation of cysteine residues on JAK1/JAK2 and STAT3 modulate IL-6 receptor signal transduction, making redox sulfur chemistry a regulator of the inflammatory JAK–STAT3 pathway.
- `modulates` → **[Liver](../../06-organ/liver/README.md)** — GSH-dependent detoxification (via GPx, GSTs) and sulfotransferases (SULT enzymes) conjugating xenobiotics and hormones constitute the liver's principal sulfur-driven phase II metabolic detoxification capacity.
- `connects-to` → **[Nitrogen](../nitrogen/README.md)** — glutathione (γ-Glu-Cys-Gly) and the methionine cycle (SAM → SAH → homocysteine → methionine) combine sulfur and nitrogen chemistry; Cys and Met amino acids contain both elements; SAM methyl groups regulate nitrogen-containing bases in DNA and RNA.
- `modulates` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — IKKβ Cys179 oxidation by H₂O₂ inhibits NF-κB activation; cysteine thiol redox state acts as a molecular brake on inflammation; GSH maintains IKK reduced; ROS depletion of GSH → IKK oxidation → NF-κB activation in oxidative stress contexts.
- `connects-to` → **[Antithrombin](../../03-molecular/antithrombin/README.md)** — heparin (highly sulfated heparan sulfate analogue) activates antithrombin III ~1,000-fold by allosteric conformational change; sulfate groups create the charge template for antithrombin binding — the molecular basis of heparin anticoagulation.

## Pathology

| Condition | Mechanism | Key features |
|:---|:---|:---|
| **Homocystinuria** | Cystathionine β-synthase (CBS) deficiency → accumulation of homocysteine; homocysteine auto-oxidises to disulfide, damaging endothelium | Thromboembolism, Marfanoid habitus, ectopia lentis, intellectual disability; treated with B6/folate/betaine; protein-restricted diet |
| **Cystinuria** | SLC3A1/SLC7A9 (rBAT/b⁰,⁺AT) transporter defect → cystine not reabsorbed in proximal tubule | Recurrent cystine kidney stones (cystine insoluble at acidic pH); treated with urinary alkalinisation, tiopronin |
| **Glutathione synthetase deficiency** | ↓ GSH → oxidative haemolysis, neurological disease | 5-oxoprolinuria (accumulation of γ-glutamylcysteine cyclised to 5-oxoproline) |
| **Methionine adenosyltransferase (MAT) deficiency** | ↓ SAM synthesis → hypermethioninaemia; usually benign (MAT I/III) but can affect myelination (MAT II) | Demyelination in severe forms; elevated plasma methionine |
| **Molybdenum cofactor deficiency** | Molybdenum cofactor contains two pterin-dithiolate (molybdopterin) sulfur ligands; cofactor required for sulfite oxidase, xanthine oxidase, aldehyde oxidase | Sulfite accumulation → severe progressive neurological disease, dislocated lens; often fatal in infancy |
| **Iron-sulfur cluster disorders** | Frataxin (FRDA) mutations → [Fe-S] cluster assembly failure in mitochondria | Friedreich's ataxia: progressive spinocerebellar degeneration, hypertrophic cardiomyopathy |

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^stryer-biochemistry]: Berg JM, Tymoczko JL, Stryer L. *Biochemistry.* 9th ed. W.H. Freeman; 2019. [macmillanlearning.com](https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X)
[^guyton-hall]: Hall JE, Hall ME. *Guyton and Hall Textbook of Medical Physiology.* 14th ed. Elsevier; 2021. [elsevier.com](https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8)
