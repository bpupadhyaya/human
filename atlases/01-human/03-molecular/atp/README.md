---
schema: human-scale-entry/v1
id: atp
name: "ATP (Adenosine Triphosphate)"
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-04
summary: "507 Da nucleotide; universal energy currency. Adenosine + triphosphate; γ-hydrolysis ~30.5 kJ/mol. Drives SERCA2a, Na⁺/K⁺-ATPase, myosin ATPase. Synthesized by F₀F₁-ATP synthase; ~40 kg recycled/day. ATP depletion in ischemia impairs Ca²⁺ cycling and triggers arrhythmia."
aliases: ["adenosine triphosphate", "ATP", "adenosine 5'-triphosphate"]
taxonomy:
  chebi: "CHEBI:15422"
  pubchem_cid: "5957"
  hmdb: "HMDB0000538"
sources:
  - id: lipmann-1941-atp-review
    type: peer-reviewed
    cite: "Lipmann F. Metabolic generation and utilization of phosphate bond energy. Adv Enzymol Relat Subj Biochem. 1941;1:99-162."
    doi: "10.1002/9780470122594.ch4"
    url: "https://doi.org/10.1002/9780470122594.ch4"
  - id: boyer-1997-atp-synthase
    type: peer-reviewed
    cite: "Boyer PD. The ATP synthase — a splendid molecular machine. Annu Rev Biochem. 1997;66:717-49."
    doi: "10.1146/annurev.biochem.66.1.717"
    pmid: "9242922"
    url: "https://doi.org/10.1146/annurev.biochem.66.1.717"
  - id: bers-2001-cardiac-excitation
    type: textbook
    cite: "Bers DM. Excitation-Contraction Coupling and Cardiac Contractile Force. 2nd ed. Kluwer Academic Publishers; 2001. ISBN 0-7923-7183-4."
    doi: "10.1007/978-94-010-0658-3"
    url: "https://doi.org/10.1007/978-94-010-0658-3"
  - id: hardie-2007-ampk-review
    type: peer-reviewed
    cite: "Hardie DG, Hawley SA, Scott JW. AMP-activated protein kinase — development of the energy sensor concept. J Physiol. 2006;574(1):7-15."
    doi: "10.1113/jphysiol.2006.108944"
    pmid: "16644716"
    url: "https://doi.org/10.1113/jphysiol.2006.108944"
cross_links:
  - target: 01-human/04-cellular/cardiomyocyte
    relation: expressed-by
    evidence: bers-2001-cardiac-excitation
    note: "Cardiomyocytes consume ~2×10⁻¹² mol ATP per beat (~30 kg of ATP recycled per day in the adult heart); continuous mitochondrial oxidative phosphorylation via F₀F₁-ATP synthase is essential for contractile function and ion homeostasis."
  - target: 01-human/03-molecular/serca2a
    relation: modulates
    evidence: bers-2001-cardiac-excitation
    note: "SERCA2a hydrolyzes one molecule of ATP per Ca²⁺ ion pair transported into the SR; ATP depletion during ischemia directly impairs SR Ca²⁺ reuptake, elevating diastolic Ca²⁺ and impairing relaxation."
  - target: 01-human/01-subatomic/proton
    relation: modulated-by
    evidence: boyer-1997-atp-synthase
    note: "Proton-motive force (pmf = Δψ + ΔpH) across the inner mitochondrial membrane drives proton flow through the F₀ c-ring of ATP synthase, rotating the γ-stalk and synthesising ATP from ADP + Pᵢ via the binding-change mechanism."
  - target: 01-human/02-atomic/hydrogen
    relation: modulated-by
    evidence: boyer-1997-atp-synthase
    note: "H⁺ electrochemical gradient (pmf) across the inner mitochondrial membrane drives F₀F₁-ATP synthase: proton flow through the F₀ c-ring rotates the γ-stalk, synthesising ~28 of ~32 ATP per glucose molecule."
  - target: 01-human/02-atomic/nitrogen
    relation: contains
    evidence: lipmann-1941-atp-review
    note: "Adenine contains 5 nitrogen atoms (N1, N3, N7, N9 purine ring + exocyclic amino N6); ring nitrogens engage in hydrogen bonding with kinase active sites, and N9 links adenine to ribose — essential for ATP recognition."
---

# ATP (Adenosine Triphosphate)

## Overview

**Adenosine triphosphate (ATP)** is the universal energy currency of living cells, described by Fritz Lipmann in 1941 as the central carrier of **"phosphate bond energy"** [^lipmann-1941-atp-review]. Every cell synthesizes and hydrolyzes ATP continuously; the human body turns over approximately **40 kg of ATP per day** — roughly its own body weight — through continuous regeneration from ADP.

ATP is a **purine nucleotide** composed of:
- **Adenosine** (adenine base + ribose sugar)
- **Three phosphate groups**: α (linked to ribose), β, and γ — forming the characteristic triphosphate tail

It couples exergonic reactions (catabolism, mitochondrial respiration) to endergonic reactions (muscle contraction, active transport, biosynthesis, signal transduction), with its energy released by hydrolysis of the γ-phosphate bond:

> **ATP + H₂O → ADP + Pᵢ + ~30.5 kJ/mol** (under standard biological conditions; actual value ~45–65 kJ/mol under cellular conditions)

Beyond energy transfer, ATP acts as:
- A **phosphate donor** for protein kinases (phosphorylation signaling)
- A **substrate** for adenylyl cyclase (cAMP second messenger)
- An **extracellular signaling molecule** via purinergic P2X and P2Y receptors
- A **cofactor** for RNA polymerase and ribosomes
- An **allosteric regulator** of metabolic enzymes (glycolysis, fatty acid oxidation)

## Structure

**Molecular formula:** C₁₀H₁₆N₅O₁₃P₃  
**Molecular weight:** 507.18 Da

Structural features:
- **Adenine ring**: purine base providing hydrogen-bonding capacity and hydrophobic stacking with protein binding pockets
- **Ribose**: 5-carbon sugar in C3'-endo conformation; 5'-OH linked to α-phosphate
- **Triphosphate chain**: three phosphate groups in α–β–γ arrangement; β–γ bond has the highest free energy of hydrolysis; both β–γ and α–β bonds are energy-releasing; α–β hydrolysis releases pyrophosphate (PPᵢ), subsequently hydrolyzed by ubiquitous pyrophosphatases making many biosynthetic reactions thermodynamically irreversible
- **Mg²⁺ chelation**: ATP functions biologically as **Mg-ATP²⁻**; the magnesium ion bridges the β and γ phosphates, reducing charge repulsion and presenting the correct geometry to kinases and ATPases

## Function

**Energy transduction:**
ATP bridges catabolism and anabolism:

| Synthesis route | ATP yield | Location |
|:---|:---|:---|
| Oxidative phosphorylation (F₀F₁-ATP synthase) | ~28 ATP per glucose (major route) | Inner mitochondrial membrane |
| Glycolysis | 2 net ATP per glucose | Cytoplasm |
| Krebs cycle (substrate-level) | 2 GTP → ATP per glucose | Mitochondrial matrix |
| β-oxidation (substrate-level) | minor | Mitochondrial matrix |
| Creatine phosphate shuttle | Rapid burst replenishment | Cytoplasm (muscle, neurons) |

**Key ATPase consumers in cardiomyocytes:**
- **Myosin ATPase (actomyosin)**: ~65% of cardiac ATP consumption; each cross-bridge cycle hydrolyzes 1 ATP
- **SERCA2a (SR Ca²⁺-ATPase)**: ~25%; pumps 2 Ca²⁺ ions into SR per ATP during diastole
- **Na⁺/K⁺-ATPase**: ~5%; maintains ionic gradients
- **Other ATPases** (dynein, kinesin, protein synthesis): ~5%

**Allosteric regulation (energy sensing):**
The ATP/ADP and ATP/AMP ratios are sensed by AMPK (AMP-activated protein kinase), the master energy-sensing kinase: when AMP rises (indicating ATP depletion), AMPK is activated → switches off ATP-consuming anabolic pathways and switches on ATP-generating catabolic pathways [^hardie-2007-ampk-review].

## Mechanism

**F₀F₁-ATP synthase (Boyer rotational mechanism):**
The mitochondrial ATP synthase couples the proton electrochemical gradient (ΔΨ + ΔpH across the inner mitochondrial membrane) to ATP synthesis via a rotary mechanism [^boyer-1997-atp-synthase]:
1. Proton flow through the **F₀ c-ring** drives rotation of the γ-subunit stalk
2. The rotating γ-subunit cyclically changes conformation of the three **β-subunits** of F₁ (open ↔ loose ↔ tight)
3. The tight conformation spontaneously synthesizes ATP from ADP + Pᵢ; rotation then releases ATP
4. ~3 protons per ATP synthesized (~2.7 H⁺/ATP in some measurements)

**Cardiac ischemia and ATP depletion:**
When coronary blood flow is interrupted, mitochondrial ATP synthesis ceases within seconds; glycolytic ATP partially compensates. As ATP falls below ~80% of normal, SERCA2a activity decreases → diastolic Ca²⁺ overload → impaired relaxation (diastolic dysfunction). At <40% normal ATP, contractile failure, arrhythmia (ATP-sensitive K⁺ channels open), and ultimately cell death follow [^bers-2001-cardiac-excitation].

## Connections

- **Expressed-by** → [Cardiomyocyte](../../../01-human/04-cellular/cardiomyocyte/README.md): Cardiomyocytes sustain the highest ATP turnover of any mammalian cell; continuous mitochondrial ATP synthesis via F₀F₁-ATP synthase is essential for contractile and ion-transport work.
- **Modulates** → [SERCA2a](../../../01-human/03-molecular/serca2a/README.md): SERCA2a hydrolyzes one ATP molecule per two Ca²⁺ ions transported into the SR; ATP availability directly gates diastolic relaxation — a critical link between energetics and cardiac function.
