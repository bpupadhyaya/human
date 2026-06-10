---
schema: human-scale-entry/v1
id: potassium
name: Potassium
atlas: 01-human
scale: 02-atomic
status: draft
last_reviewed: 2026-06-05
summary: "K⁺, atomic number 19. Principal intracellular cation (140 mmol/L cytosol vs. 3.5–5.0 mmol/L plasma). K⁺ efflux through Kv/Kir channels repolarises action potentials and sets resting membrane potential. Hypokalaemia prolongs QT and predisposes to torsades de pointes."
aliases: ["K", "K⁺", "potassium ion", "kalium", "hypokalaemia", "hyperkalaemia"]
sources:
  - id: hodgkin-huxley-1952
    type: peer-reviewed
    cite: "Hodgkin AL, Huxley AF. A quantitative description of membrane current and its application to conduction and excitation in nerve. J Physiol. 1952;117(4):500-44."
    doi: "10.1113/jphysiol.1952.sp004764"
    pmid: "12991237"
    url: "https://doi.org/10.1113/jphysiol.1952.sp004764"
  - id: doyle-1998-kchannel
    type: peer-reviewed
    cite: "Doyle DA, Morais Cabral J, Pfuetzner RA, et al. The structure of the potassium channel: molecular basis of K⁺ conduction and selectivity. Science. 1998;280(5360):69-77."
    doi: "10.1126/science.280.5360.69"
    pmid: "9525859"
    url: "https://doi.org/10.1126/science.280.5360.69"
cross_links:
  - target: 01-human/08-whole-body/human-body
    relation: part-of
    note: "K⁺ is the principal intracellular cation. Total body potassium is ~140 g (~3600 mmol), >98% intracellular (muscle, liver, RBCs at ~140 mmol/L). The plasma fraction (3.5–5.0 mmol/L) is tightly regulated by aldosterone, insulin, and acid–base status."
  - target: 01-human/04-cellular/neuron
    relation: modulates
    note: "K⁺ efflux through Kv1/2/4 channels repolarises the neuronal AP toward EK (~−90 mV). Kir2.x (IK1) holds the resting potential at ~−70 mV. Kv (repolarisation) and Kir (resting potential) are the K⁺ complement to Nav in the Hodgkin-Huxley model."
  - target: 01-human/04-cellular/sa-node-cell
    relation: modulates
    note: "IKr (hERG) and IKs (KCNQ1) repolarise the SA node AP to the maximum diastolic potential (MDP). HCN4 (If) then drives spontaneous depolarisation to threshold. EK sets the most negative Vm achievable, defining the lower bound of SA node automaticity."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Na⁺/K⁺-ATPase links K⁺ and Na⁺ gradients: 3 Na⁺ out, 2 K⁺ in per ATP; K⁺ efflux through Kv/Kir repolarises action potentials (EK ≈ −90 mV) while Na⁺ influx depolarises (ENa ≈ +60 mV); changes in [K⁺]o directly shift EK and resting membrane potential."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "Elevated [K⁺] is the primary direct stimulus for aldosterone secretion; aldosterone drives ROMK (Kir1.1) K⁺ secretion in cortical collecting duct; each ~0.1 mmol/L rise in [K⁺] roughly doubles aldosterone output; primary aldosteronism → excess K⁺ secretion → hypokalaemia."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "IKr (hERG), IKs (KCNQ1), IK1 (Kir2.1), and Ito (Kv4.3) K⁺ currents repolarise the cardiac AP; hypokalaemia prolongs AP → EADs → torsades de pointes; IKATP (Kir6.2/SUR2A) opens in ischaemia, shortening AP to conserve energy and mimicking ischaemic preconditioning."
---

# Potassium

## Overview

Potassium (symbol K, from Latin *kalium*; atomic number 19, atomic mass 39.098 u) is an alkali metal in Group 1, Period 4 of the periodic table. In biology it exists exclusively as the monovalent cation **K⁺**, having lost its single 4s valence electron. It is the **principal intracellular cation** — held at ~140 mmol/L in the cytoplasm of every mammalian cell versus only 3.5–5.0 mmol/L in plasma — and this steep gradient, maintained by Na⁺/K⁺-ATPase at the cost of ~1/3 of cellular ATP, is the thermodynamic source of the resting membrane potential that makes all electrical signalling in the nervous system and heart possible [^hodgkin-huxley-1952].

Potassium's biological role was established through physiological experiments from the 1880s onwards (Sydney Ringer, 1882: heart cessation without K⁺). The ionic basis of the action potential was quantitatively characterised by Hodgkin and Huxley (1952), who resolved the repolarising K⁺ current (gK, n⁴ kinetics) from the depolarising Na⁺ current. The structural basis of K⁺ channel selectivity was solved by Roderick MacKinnon's crystallography of the bacterial KcsA channel in 1998 — a breakthrough that revealed the TVGYG selectivity filter and earned MacKinnon the 2003 Nobel Prize in Chemistry [^doyle-1998-kchannel].

The K⁺ channel family is by far the **largest ion channel family in the human genome**: ~80 genes encoding K⁺ channels, classifiable into voltage-gated (Kv), inwardly rectifying (Kir), two-pore domain (K₂P), and Ca²⁺-activated (KCa) subfamilies. This diversity reflects the profound importance of K⁺ conductance to cellular electrical physiology across all tissues.

## Structure

### Atomic Properties

| Property | Value |
|:---|:---|
| Atomic number (Z) | 19 |
| Atomic mass | 39.098 u |
| Electron configuration | [Ar] 4s¹ |
| Ionic form | K⁺ (loses 4s¹ electron) |
| Ionic radius (K⁺) | 138 pm |
| Electronegativity (Pauling) | 0.82 |
| Hydration enthalpy (K⁺) | −321 kJ/mol |
| Coordination number in water | 6–8 |

### The Potassium Channel Selectivity Filter

The crystal structure of KcsA (and all subsequent K⁺ channel structures) revealed a conserved **TVGYG** selectivity filter motif — five residues from each of the four channel subunits form a narrow pore lined by backbone carbonyl oxygens [^doyle-1998-kchannel]. The filter contains four sequential K⁺ binding sites (S1–S4) separated by ~3.1 Å:

- **K⁺ (radius 138 pm):** Fits precisely in the filter; the carbonyl oxygens mimic K⁺'s hydration shell (8 oxygens in the KcsA filter). K⁺ conduction rate: ~10⁸ ions/sec per channel (near diffusion limit).
- **Na⁺ (radius 102 pm):** Too small to be optimally coordinated by the filter carbonyls; the energetic cost of dehydration exceeds the coordination energy, giving >1000:1 K⁺/Na⁺ selectivity.
- **Ion knock-on mechanism:** Two K⁺ ions occupy adjacent sites simultaneously (1,3 or 2,4 configuration); electrostatic repulsion between adjacent K⁺ ions lowers the activation barrier for translocation — the basis of high-conductance selectivity-filter-mediated conduction.

### Nernst Potential for K⁺

**EK = (RT/F) · ln([K⁺]out / [K⁺]in) = 26.7 mV × ln(4/140) ≈ −94 mV** (at 37°C, [K⁺]out = 4 mmol/L, [K⁺]in = 140 mmol/L)

The resting membrane potential of most excitable cells (−70 to −90 mV) is close to but not equal to EK. The difference reflects the small contribution of other conductances (predominantly Na⁺ leak). The Goldman-Hodgkin-Katz equation:

**Vm = (RT/F) · ln[(PK·[K⁺]o + PNa·[Na⁺]o + PCl·[Cl⁻]i) / (PK·[K⁺]i + PNa·[Na⁺]i + PCl·[Cl⁻]o)]**

At rest: PK ≫ PNa; Vm ≈ EK. During the action potential upstroke: PNa transiently dominates; Vm approaches ENa (+60 mV). At repolarisation: Kv channels open → PK/PNa rises → Vm returns toward EK.

## Function

### Setting the Resting Membrane Potential

The resting membrane potential (Vrest) is set primarily by the background K⁺ conductance — predominantly the **inwardly rectifying Kir2.x channels (IK1)** in cardiomyocytes, neurons, and skeletal muscle. Kir2.x channels are constitutively open at negative Vm, conducting an outward K⁺ current that hyperpolarises the cell; they close (inward rectification) at depolarised potentials, preventing excessive K⁺ efflux during action potentials.

In cardiomyocytes: IK1 (Kir2.1/2.2) maintains Vrest at ~−85 mV. In neurons: Kir2.x and K₂P (TREK, TASK) channels hold Vrest at ~−70 mV. In SA node cells: IK1 is sparse — the low resting K⁺ conductance allows the spontaneous pacemaker depolarisation driven by HCN4 (If, funny current) and ICaT to slowly bring Vm to the threshold for action potential firing.

### Action Potential Repolarisation — Kv Channels

Voltage-gated K⁺ channels (Kv) open with a delay after Na⁺ channels and drive membrane repolarisation [^hodgkin-huxley-1952]:

**Neuronal action potential (Hodgkin-Huxley n⁴ gating):**
- Kv1.1/1.2/1.4 (Shaker family): activate at −30 to −10 mV; rapid repolarisation; n⁴ kinetics.
- Kv4.2/4.3: A-type (transient) K⁺ current (IA); inactivate rapidly; modulate repetitive firing patterns.
- Kv7.2/7.3 (KCNQ2/3): M-current (IM); slowly activating; suppress repetitive firing.

**Cardiac action potential:**
The cardiac AP is longer (~200–400 ms vs. ~1–2 ms in nerve) because of the plateau (Phase 2) generated by L-type Ca²⁺ channels. K⁺ currents are differentially timed to maintain this plateau and then rapidly repolarise:

| K⁺ current | Channel | Phase | Function |
|:---|:---|:---:|:---|
| IKr (rapid delayed rectifier) | hERG (KCNH2) | 3 | Primary repolarisation |
| IKs (slow delayed rectifier) | KCNQ1/KCNE1 | 3 | Repolarisation reserve; augmented by β1-AR/PKA |
| IK1 (inward rectifier) | Kir2.1/2.2 | 3–4 | Terminal repolarisation; maintains Vrest (Phase 4) |
| Ito (transient outward) | Kv4.3, Kv1.4 | 1 | Notch of AP; predominant in epicardium → transmural gradient |
| IKACh (acetylcholine-gated) | Kir3.1/3.4 | — | Vagal slowing; direct Gβγ activation |
| IKATP | Kir6.2/SUR2A | — | Ischaemia-activated; shortens AP to conserve energy |

### SA Node Pacemaking — K⁺ Currents in Automaticity

In the SA node, IKr and IKs repolarise the action potential to approximately −60 mV (MDP, maximum diastolic potential). From there, the **pacemaker current (If, HCN4)** — activated by hyperpolarisation and augmented by cAMP — slowly depolarises Vm toward the threshold (~−50 mV) for the next action potential. The rate of pacemaking (heart rate) is modulated by the balance between:

- **Sympathetic stimulation:** β1-AR → PKA → phosphorylation of IKs (→ faster repolarisation → shorter AP) and HCN4 (→ faster spontaneous depolarisation) → tachycardia.
- **Parasympathetic stimulation:** ACh → Gi → Gβγ → IKACh (Kir3.1/3.4 opens) → hyperpolarisation + slowing of If → bradycardia.

The magnitude of EK (determined by [K⁺]o) directly sets the MDP of SA node cells: hypokalaemia (low [K⁺]o) makes EK more negative → more negative MDP → longer time to threshold → bradycardia (in severe cases). Hyperkalaemia (high [K⁺]o) makes EK less negative → reduced Vrest → partial depolarisation → paradoxically impaired repolarisation.

### K⁺ and Aldosterone — Renal Regulation

Plasma [K⁺] is regulated by the renal cortical collecting duct (principal cells):

- **Aldosterone:** Synthesised in zona glomerulosa in response to angiotensin II, ACTH, and elevated [K⁺]. Binds mineralocorticoid receptor → induces ENaC (apical, Na⁺ entry) and Na⁺/K⁺-ATPase (basolateral, Na⁺ exit + K⁺ entry) → increases luminal negative potential → drives K⁺ secretion via ROMK (Kir1.1) into the tubular lumen → urinary K⁺ excretion.
- **Insulin:** Stimulates Na⁺/K⁺-ATPase in muscle and liver → shifts K⁺ into cells → lowers plasma [K⁺]. Used acutely to treat hyperkalaemia (with glucose to prevent hypoglycaemia).
- **Acid–base:** Acidosis → K⁺/H⁺ exchange across cell membranes → K⁺ moves out of cells → hyperkalaemia. Alkalosis → opposite.

### K⁺ in Enzyme Function

K⁺ is a required cofactor for pyruvate kinase (the enzyme catalysing PEP → pyruvate in glycolysis step 10): the monovalent K⁺ cation coordinates the enolate oxygen of PEP and the α-phosphate, stabilising the transition state. Several other enzymes (threonine deaminase, propionyl-CoA carboxylase) also require K⁺ as an allosteric activator via similar electrostatic mechanisms.

## Connections

- `part-of` → **[Human Body](../../08-whole-body/human-body/README.md)** — Total body K⁺ (~3600 mmol) is >98% intracellular (~140 mmol/L cytosol vs 3.5–5.0 mmol/L plasma); its distribution across cell membranes is the primary determinant of resting membrane potential across all excitable and non-excitable cells.
- `modulates` → **[Neuron](../../04-cellular/neuron/README.md)** — Kv1/2/4 channel K⁺ efflux repolarises the neuronal AP toward EK (≈−90 mV); Kir2.x (IK1) background conductance holds Vrest ≈−70 mV; Hodgkin-Huxley n⁴ gating describes Kv activation; K⁺ channel mutations cause episodic ataxia (Kv1.1) and neonatal epilepsy (KCNQ2/3).
- `modulates` → **[SA Node Cell](../../04-cellular/sa-node-cell/README.md)** — IKr (hERG) and IKs (KCNQ1) repolarise the SA node AP to the maximum diastolic potential; HCN4 then drives spontaneous depolarisation; EK (set by [K⁺]o) defines the most negative Vm achievable, establishing the lower bound of pacemaker automaticity.
- `connects-to` → **[Sodium](../sodium/README.md)** — Na⁺/K⁺-ATPase links K⁺ and Na⁺ gradients (3 Na⁺ out, 2 K⁺ in per ATP); K⁺ efflux through Kv/Kir repolarises APs (EK ≈−90 mV) while Na⁺ influx depolarises (ENa ≈+60 mV); changes in [K⁺]o directly shift EK and resting membrane potential.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — elevated [K⁺] is the primary direct stimulus for aldosterone secretion; aldosterone drives ROMK (Kir1.1) K⁺ secretion in cortical collecting duct; each ~0.1 mmol/L rise in [K⁺] roughly doubles aldosterone output; primary aldosteronism → excess K⁺ secretion → hypokalaemia.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — IKr (hERG), IKs (KCNQ1), IK1 (Kir2.1), and Ito (Kv4.3) K⁺ currents repolarise the cardiac AP; hypokalaemia prolongs AP → EADs → torsades de pointes; IKATP (Kir6.2/SUR2A) opens in ischaemia, shortening AP to conserve energy.

## Pathology

| Condition | K⁺ mechanism |
|:---|:---|
| **Hypokalaemia** ([K⁺] < 3.5 mmol/L) | EK shifts more negative → greater Na⁺/K⁺ driving force → increased AP duration (QT prolongation) → IKr reactivation → early afterdepolarisations (EADs) → torsades de pointes; muscle weakness; causes: loop/thiazide diuretics, vomiting, Conn's syndrome |
| **Hyperkalaemia** ([K⁺] > 5.5 mmol/L) | EK less negative → Vrest more positive → sustained partial depolarisation → Nav channel inactivation → bradycardia, peaked T waves, widened QRS, sine wave pattern, VF; causes: renal failure, ACE inhibitors, K⁺-sparing diuretics |
| **Long QT syndrome (LQT1)** | KCNQ1 loss-of-function → reduced IKs → impaired repolarisation reserve → QT prolongation → torsades de pointes; exacerbated by exercise (sympathetic stimulation) |
| **Long QT syndrome (LQT2)** | hERG (KCNH2) loss-of-function → reduced IKr → QT prolongation → torsades; triggered by sudden noise, bradycardia; hERG is also sensitive to many drugs (drug-induced LQTS) |
| **Andersen-Tawil syndrome** | Kir2.1 (KCNJ2) loss-of-function → reduced IK1 → QT/QU prolongation + periodic paralysis + dysmorphic features (KCNJ2 mutation) |
| **Familial hyperaldosteronism** | Constitutive K⁺ channel (KCNJ5) activation in zona glomerulosa → membrane depolarisation → aldosterone hypersecretion → hypertension + hypokalaemia |

## Open Questions

- **IKr trafficking and drug sensitivity:** hERG K⁺ channels are uniquely susceptible to block by structurally diverse drugs (antihistamines, antibiotics, antipsychotics) because their large inner cavity accommodates diverse molecules; this is the leading cause of drug-induced QT prolongation. Better understanding of hERG pharmacology is needed for safer drug development.
- **K⁺ channel openers as cardioprotectants:** KATP channel openers (diazoxide, nicorandil) mimic ischaemic preconditioning by shortening the AP and reducing Ca²⁺ overload; whether chronic KATP opener therapy protects against heart failure progression is under investigation.
- **K⁺ channel expression in heart failure:** Multiple K⁺ currents (IKr, Ito, IK1) are down-regulated in end-stage failing hearts, prolonging the AP, increasing arrhythmia risk, and impairing the repolarisation reserve. The transcriptional and post-translational mechanisms governing K⁺ channel remodelling in HF are incompletely characterised.

## See Also

- [Sodium](../sodium/README.md) — the complementary extracellular cation; Na⁺ influx depolarises, K⁺ efflux repolarises.
- [SA Node Cell](../../04-cellular/sa-node-cell/README.md) — K⁺ currents govern SA node pacemaking rate.
- [Neuron](../../04-cellular/neuron/README.md) — Kv and Kir channels shape the neuronal action potential and resting potential.

[^hodgkin-huxley-1952]: Hodgkin AL, Huxley AF. A quantitative description of membrane current and its application to conduction and excitation in nerve. *J Physiol.* 1952;117(4):500-44. [doi:10.1113/jphysiol.1952.sp004764](https://doi.org/10.1113/jphysiol.1952.sp004764) · [PubMed 12991237](https://pubmed.ncbi.nlm.nih.gov/12991237/)
[^doyle-1998-kchannel]: Doyle DA, Morais Cabral J, Pfuetzner RA, et al. The structure of the potassium channel: molecular basis of K⁺ conduction and selectivity. *Science.* 1998;280(5360):69-77. [doi:10.1126/science.280.5360.69](https://doi.org/10.1126/science.280.5360.69) · [PubMed 9525859](https://pubmed.ncbi.nlm.nih.gov/9525859/)

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
