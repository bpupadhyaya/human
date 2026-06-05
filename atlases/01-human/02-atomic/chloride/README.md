---
schema: human-scale-entry/v1
id: chloride
name: Chloride
atlas: 01-human
scale: 02-atomic
status: draft
last_reviewed: 2026-06-05
summary: "Chloride (Cl⁻, atomic number 17) — plasma 103 mEq/L, principal extracellular anion. Drives GABA-A inhibition, gastric HCl, CFTR fluid secretion, and CO₂ transport (chloride shift/AE1). Mutations in CFTR, NKCC2, or NCC cause cystic fibrosis, Bartter, or Gitelman syndrome."
aliases: ["Cl", "Cl-", "chloride ion", "HCl", "chlorine-35"]
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
  - id: bhatt-cftr
    type: peer-reviewed
    cite: "Csanady L, Vergani P, Gadsby DC. Structure, gating, and regulation of the CFTR anion channel. Physiol Rev. 2019;99(1):707-738."
    doi: "10.1152/physrev.00007.2018"
    pmid: "30516487"
    url: "https://doi.org/10.1152/physrev.00007.2018"
  - id: ben-ari-gaba-chloride
    type: peer-reviewed
    cite: "Ben-Ari Y. Excitatory actions of GABA during development: the nature of the nurture. Nat Rev Neurosci. 2002;3(9):728-39."
    doi: "10.1038/nrn920"
    pmid: "12209121"
    url: "https://doi.org/10.1038/nrn920"
cross_links:
  - target: 01-human/08-whole-body/human-body
    relation: part-of
    note: "Plasma 103 mEq/L; principal extracellular anion maintaining electroneutrality with Na⁺; intracellular ~4 mEq/L; total body Cl⁻ ~2100 mEq in a 70 kg adult."
  - target: 01-human/04-cellular/neuron
    relation: modulates
    note: "GABA-A receptor Cl⁻ influx hyperpolarises neurons (inhibition); neonatal GABA excitation due to elevated intracellular Cl⁻ before KCC2 expression; fundamental to all inhibitory neural circuits."
  - target: 01-human/06-organ/kidney
    relation: modulates
    note: "Chloride reabsorbed via NKCC2 (thick ascending limb; loop diuretic target), NCC (distal tubule; thiazide target), AE1 (collecting duct); Bartter/Gitelman syndromes from transporter mutations."
  - target: 01-human/03-molecular/gaba
    relation: modulates
    note: "GABA-A receptor is a Cl⁻ channel — GABA binding opens the pore; Cl⁻ influx hyperpolarises the membrane; benzodiazepines increase open frequency, barbiturates increase open duration."
---

# Chloride

## Overview

Chloride (symbol Cl, atomic number 17) is a **halogen** in Group 17 of the periodic table, with atomic mass 35.45 u and electron configuration [Ne] 3s² 3p⁵. In all physiological contexts it exists as the monovalent anion **Cl⁻** (ionic radius 0.181 nm). Chloride is the **most abundant extracellular anion** in the human body, present at approximately **103 mEq/L in plasma** and contributing the major anionic counterpart to sodium in the extracellular fluid (ECF). Total body chloride content in a 70 kg adult is approximately **2100 mEq** (~75 g), of which ~90% is in the ECF [^guyton-hall].

Unlike many trace elements, chloride does not form covalent bonds with protein residues; its biological functions are exclusively ionic — governing osmolality, acid-base balance, membrane potential, and serving as the permeating anion in several clinically critical ion channels. Three systems are particularly prominent: (1) the **GABA-A receptor**, where Cl⁻ influx mediates neuronal inhibition; (2) **CFTR** (cystic fibrosis transmembrane conductance regulator), where Cl⁻ secretion drives fluid movement across epithelia; and (3) the **chloride shift** (Hamburger phenomenon), where Cl⁻/HCO₃⁻ exchange across erythrocytes enables efficient CO₂ transport in blood [^stryer-biochemistry].

## Structure

### Atomic Properties

| Property | Value |
|:---|:---|
| Atomic number (Z) | 17 |
| Atomic mass | 35.45 u (³⁵Cl 75.8%, ³⁷Cl 24.2%) |
| Electron configuration | [Ne] 3s² 3p⁵ |
| Ionic form in biology | Cl⁻ (gains 1 electron to complete 3p shell) |
| Ionic radius (Cl⁻) | 0.181 nm (181 pm) |
| Electronegativity (Pauling) | 3.16 |
| Hydration enthalpy | −363 kJ/mol (moderately hydrated) |

### Distribution Across Compartments

| Compartment | [Cl⁻] (mEq/L) | Notes |
|:---|:---:|:---|
| Plasma | 103 | Paired with Na⁺ (~142 mEq/L) and HCO₃⁻ (~24 mEq/L); remainder = anion gap |
| Interstitial fluid | ~111 | Slightly higher than plasma (Gibbs-Donnan effect; plasma proteins repel Cl⁻) |
| Intracellular (most cells) | 4–10 | Maintained low by K⁺-Cl⁻ cotransporter KCC2 (neurons) and NKCC1/Cl⁻-ATPase balance |
| Erythrocyte cytoplasm | ~78 | High; varies dynamically with the chloride shift |
| Gastric lumen | ~150 | Secreted as HCl by parietal cells |
| Sweat | ~10–40 | Low (reabsorbed by CFTR); elevated (>60 mEq/L) in cystic fibrosis |
| Cerebrospinal fluid | ~127 | Higher than plasma; important for acid-base buffering |

### Key Chloride Channel/Transporter Proteins

| Protein | Gene | Family | Cl⁻ movement | Function |
|:---|:---|:---|:---|:---|
| **GABA-A receptor** | GABRA/GABRB/GABRG | Cys-loop ligand-gated | Influx | Neuronal inhibition |
| **CFTR** | CFTR | ABC transporter | Efflux | Epithelial fluid secretion |
| **ClC-1** | CLCN1 | CLC Cl⁻ channel | Efflux | Skeletal muscle membrane stabilisation |
| **ClC-2** | CLCN2 | CLC Cl⁻ channel | Influx | Glia, neuron osmolarity regulation |
| **AE1 (Band 3)** | SLC4A1 | SLC4 anion exchanger | HCO₃⁻ out / Cl⁻ in (tissues); Cl⁻ out / HCO₃⁻ in (lung) | Chloride shift in RBCs |
| **NKCC2** | SLC12A1 | SLC12 (CCC) | 2Cl⁻ + Na⁺ + K⁺ in | Thick ascending LOH reabsorption |
| **NCC** | SLC12A3 | SLC12 (CCC) | Cl⁻ + Na⁺ in | Distal convoluted tubule reabsorption |
| **KCC2** | SLC12A5 | SLC12 (CCC) | K⁺ + Cl⁻ out | Maintains low [Cl⁻]i in mature neurons |
| **SLC26A7** | SLC26A7 | SLC26 | Cl⁻ in / HCO₃⁻ out | Parietal cell HCl secretion |

## Function

### 1. Maintaining Electroneutrality and Osmolality

The primary bulk role of Cl⁻ is to **balance Na⁺** in the ECF, maintaining electroneutrality (the law of electroneutrality mandates that total cation charge = total anion charge in any compartment). Together, NaCl accounts for ~90% of ECF osmolality; regulated changes in Na⁺ handling by the kidney are always accompanied by concomitant Cl⁻ movement. The **serum anion gap** (Na⁺ − [Cl⁻ + HCO₃⁻] = 8–12 mEq/L) reflects unmeasured anions (albumin, phosphate, sulfate, organic acids) and is a clinical tool for classifying metabolic acidosis.

### 2. GABA-A Receptor and Neuronal Inhibition

The GABA-A receptor is a **pentameric ligand-gated Cl⁻ channel** (Cys-loop superfamily), the primary mediator of fast inhibitory neurotransmission in the CNS. The channel pore is lined by M2 transmembrane helices and has a selectivity filter that favours anions (Cl⁻ > HCO₃⁻) over cations by ~10:1 [^ben-ari-gaba-chloride].

**Mechanism of inhibition:**
- GABA binds to the β subunit at the α–β interface → conformational change → channel opens (~1–3 ms open time)
- Cl⁻ influx (down its electrochemical gradient, resting [Cl⁻]i ~ 4–10 mM, [Cl⁻]o ~103 mM) → membrane hyperpolarises toward E_Cl ≈ −70 to −75 mV
- Increased conductance also provides **shunting inhibition** — even when IPSP drives the membrane only modestly, the increased conductance makes it harder for EPSPs to depolarise the cell

**Allosteric modulators of GABA-A:**
| Drug class | Binding site | Effect on Cl⁻ conductance |
|:---|:---|:---|
| Benzodiazepines | α-γ interface | Increase **frequency** of channel opening; no effect without GABA |
| Barbiturates | Transmembrane β subunit | Increase **duration** of channel opening; can directly gate at high concentrations |
| Neurosteroids (e.g., allopregnanolone) | Transmembrane δ subunit | Potentiate and directly activate |
| Propofol | Transmembrane site | Potentiate + direct activation |
| Etomidate | β2/β3 subunit | Potentiate (β2/β3 required); used in anaesthesia |

**Neonatal polarity reversal:** Immature neurons express high levels of **NKCC1** (which imports Cl⁻) and low levels of **KCC2** (which exports Cl⁻), so [Cl⁻]i ≈ 25–40 mM. At this high intracellular Cl⁻, E_Cl ≈ −35 to −40 mV, which is **depolarised** relative to resting potential (~−70 mV). Therefore, GABA-A opening causes Cl⁻ **efflux**, depolarising the neuron and potentially triggering action potentials — making GABA **excitatory** in the developing brain [^ben-ari-gaba-chloride]. This switch from GABA excitation to inhibition (GABA "switch") is driven by KCC2 upregulation during the first postnatal weeks and is essential for normal circuit maturation.

### 3. CFTR and Epithelial Fluid Secretion

**CFTR** (ABCC7) is a cAMP-regulated Cl⁻ channel expressed at the apical membrane of secretory epithelia: airways, pancreatic ducts, intestinal crypts, bile ducts, and sweat gland ducts [^bhatt-cftr].

**Activation pathway:** Adenylyl cyclase → cAMP → PKA → phosphorylation of CFTR R-domain (Ser768, Ser813) → channel gating (ATP binds NBD1/NBD2 → dimerisation → channel opens). CFTR can also be activated by AMPK and PKC.

**Function:** CFTR exports Cl⁻ into the airway surface liquid/intestinal lumen; osmotic drag follows as water. In the sweat gland, CFTR reabsorbs Cl⁻ from sweat back into ductal cells (opposite direction), keeping sweat hypotonic. The Cl⁻ channel function of CFTR also regulates HCO₃⁻ secretion (important for mucus pH and viscoelasticity) and epithelial Na⁺ channel (ENaC) activity via direct interaction.

### 4. Gastric HCl Secretion

Parietal cells of the gastric mucosa secrete **HCl** (pH 1.5–3.5) by combining two separate ion transporters:
1. **H⁺/K⁺-ATPase** (gastric proton pump, ATP4A) on the apical canalicular membrane — secretes H⁺ into the gastric lumen while importing K⁺ into the cell; target of proton pump inhibitors (omeprazole, lansoprazole)
2. **SLC26A7** (Cl⁻/HCO₃⁻ exchanger) on the apical membrane — exports Cl⁻ into the lumen in exchange for intracellular HCO₃⁻ (the "alkaline tide")

H⁺ + Cl⁻ combine in the gastric lumen as HCl. Stimulation is via histamine (H₂ receptor → cAMP → PKA → H⁺/K⁺-ATPase insertion from cytoplasmic tubulovesicles), gastrin (CCK-2 receptor), and acetylcholine (M3 receptor). The HCO₃⁻ extruded basally into blood buffers gastric acid-related alkalosis.

### 5. The Chloride Shift (Hamburger Phenomenon)

In systemic capillaries, CO₂ produced by tissues diffuses into erythrocytes, where **carbonic anhydrase II** catalyses: CO₂ + H₂O → H₂CO₃ → H⁺ + HCO₃⁻. The HCO₃⁻ accumulates and exits via **AE1 (Band 3, SLC4A1)** — an electroneutral HCO₃⁻/Cl⁻ exchanger — in exchange for extracellular Cl⁻. This Cl⁻ influx (the chloride shift) maintains electroneutrality and allows large amounts of CO₂ to be transported as dissolved plasma HCO₃⁻ (~70% of total CO₂ transport). The process reverses at the lung: HCO₃⁻ re-enters RBCs (exchanging for Cl⁻), recombines with H⁺ (released from deoxygenated haemoglobin, Haldane effect), and carbonic anhydrase reforms CO₂ for exhalation [^guyton-hall].

### 6. Renal Chloride Handling

The kidney reabsorbs ~99% of filtered Cl⁻ (~720 mEq/day excreted in urine):

| Nephron segment | Fraction reabsorbed | Mechanism | Diuretic target |
|:---|:---:|:---|:---|
| Proximal convoluted tubule (PCT) | ~65% | Paracellular (lumen-positive late PCT) + NHE3 (Na⁺/H⁺ → indirect) + CFEX (Cl⁻/formate) | — |
| Thick ascending limb of Henle (TALH) | ~25% | NKCC2 (SLC12A1): Na⁺+K⁺+2Cl⁻ cotransport | Loop diuretics (furosemide) block NKCC2 |
| Distal convoluted tubule (DCT) | ~5% | NCC (SLC12A3): Na⁺+Cl⁻ cotransport | Thiazides block NCC |
| Collecting duct | ~3–4% | Paracellular + AE1/pendrin in alpha/beta intercalated cells | — |

Aldosterone primarily regulates Na⁺ reabsorption via ENaC in the collecting duct principal cells, with Cl⁻ following passively to maintain electroneutrality.

## Connections

- **Part of** → [Human body](../../08-whole-body/human-body/README.md): Plasma 103 mEq/L; principal extracellular anion maintaining electroneutrality with Na⁺; intracellular ~4 mEq/L; total body Cl⁻ ~2100 mEq — essential for osmolality, acid-base balance, and membrane potential.
- **Modulates** → [Neuron](../../04-cellular/neuron/README.md): GABA-A Cl⁻ influx hyperpolarises mature neurons (inhibitory); neonatal GABA excitation occurs when high [Cl⁻]i (before KCC2 expression) makes E_Cl depolarised — GABA switch is fundamental to circuit maturation.
- **Modulates** → [Kidney](../../06-organ/kidney/README.md): Cl⁻ reabsorbed via NKCC2 (thick ascending LOH; loop diuretic target), NCC (DCT; thiazide target), and AE1 in intercalated cells; Bartter syndrome (NKCC2/ROMK/CLCNKB) and Gitelman syndrome (NCC) from transporter mutations.
- **Modulates** → [GABA](../../03-molecular/gaba/README.md): GABA-A receptor is a Cl⁻ channel — GABA binding opens the pore; Cl⁻ influx drives hyperpolarisation; benzodiazepines increase open frequency, barbiturates increase open duration; channel polarity reversed in neonates.

## Pathology

### Cystic Fibrosis (CFTR Mutations)

**Cystic fibrosis (CF)** is the most common life-limiting autosomal recessive disorder in people of European descent (~1 in 3500 live births; carrier frequency ~1/25). CF is caused by mutations in *CFTR* (>2000 identified mutations), classified by molecular mechanism [^bhatt-cftr]:

| Class | Mechanism | Example mutation | Frequency |
|:---|:---|:---|:---:|
| I | No protein produced (nonsense/splice) | G542X, W1282X | ~10% |
| II | Protein misfolded → retained in ER | **ΔF508 (F508del)** | ~70% (allele frequency) |
| III | Protein reaches membrane but gating defect | G551D | ~2–3% |
| IV | Reduced conductance | R117H | ~1–2% |
| V | Reduced amount of normal CFTR | 3849+10kbC→T | Rare |

**Pathophysiology:** Absent/dysfunctional CFTR → impaired Cl⁻ secretion + compensatory ENaC hyperactivation → dehydrated, viscous airway surface liquid → impaired mucociliary clearance → **chronic Pseudomonas aeruginosa** and *Staphylococcus aureus* infection → neutrophilic bronchiectasis → progressive respiratory failure. Pancreatic duct obstruction → exocrine insufficiency → malabsorption. Male infertility (congenital bilateral absence of vas deferens, CBAVD).

**CFTR modulators** (transformative therapies targeting the underlying defect):
- **Ivacaftor** (VX-770): potentiator — opens gating-defective CFTR (G551D and other class III) — dramatic clinical benefit
- **Lumacaftor/tezacaftor**: correctors — improve folding and trafficking of ΔF508 CFTR to cell surface — modest benefit alone
- **Elexacaftor/tezacaftor/ivacaftor (Trikafta)**: triple combination corrector + potentiator — ~90% improvement in FEV₁ and quality of life for ΔF508 homozygotes and heterozygotes — transformative

### Bartter and Gitelman Syndromes

**Bartter syndrome** (autosomal recessive, multiple types):
- Type I: NKCC2 (SLC12A1) mutation → impaired Cl⁻ reabsorption in TALH
- Type II: ROMK (KCNJ1) mutation → K⁺ recycling failure → secondary NKCC2 dysfunction
- Type III: CLCNKB (ClC-Kb Cl⁻ channel) mutation → Cl⁻ exit from TALH cell impaired
- Features: salt wasting, hypokalaemia, metabolic alkalosis, hyperaldosteronism, normal/low BP; polyhydramnios in severe forms

**Gitelman syndrome** (NCC/SLC12A3 mutation) — milder, presents in adults with hypokalaemia, hypomagnesaemia, metabolic alkalosis, salt wasting; hypocalciuria distinguishes from Bartter.

### Hyperchloraemic Metabolic Acidosis

Occurs when HCO₃⁻ is lost or replaced by Cl⁻ without change in anion gap:
- Diarrhoea: HCO₃⁻-rich stool loss → compensatory Cl⁻ retention
- Normal saline infusion: large volumes of 0.9% NaCl (154 mEq/L Cl⁻) exceed buffering capacity → dilutional hyperchloraemia → non-anion gap acidosis

## See Also

- [GABA](../../03-molecular/gaba/README.md) — ligand for the Cl⁻-conducting GABA-A receptor.
- [Neuron](../../04-cellular/neuron/README.md) — Cl⁻ governs inhibitory postsynaptic potential polarity.
- [Kidney](../../06-organ/kidney/README.md) — multiple Cl⁻ transporters along the nephron.
- [Sodium](../../02-atomic/sodium/README.md) — primary cation paired with Cl⁻ in ECF osmolality.

[^stryer-biochemistry]: Berg JM, Tymoczko JL, Stryer L. *Biochemistry.* 9th ed. W.H. Freeman; 2019. [macmillanlearning.com](https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X)
[^guyton-hall]: Hall JE, Hall ME. *Guyton and Hall Textbook of Medical Physiology.* 14th ed. Elsevier; 2021. [elsevier.com](https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8)
[^bhatt-cftr]: Csanady L, Vergani P, Gadsby DC. Structure, gating, and regulation of the CFTR anion channel. *Physiol Rev.* 2019;99(1):707-738. [doi:10.1152/physrev.00007.2018](https://doi.org/10.1152/physrev.00007.2018) · [PubMed 30516487](https://pubmed.ncbi.nlm.nih.gov/30516487/)
[^ben-ari-gaba-chloride]: Ben-Ari Y. Excitatory actions of GABA during development: the nature of the nurture. *Nat Rev Neurosci.* 2002;3(9):728-39. [doi:10.1038/nrn920](https://doi.org/10.1038/nrn920) · [PubMed 12209121](https://pubmed.ncbi.nlm.nih.gov/12209121/)
