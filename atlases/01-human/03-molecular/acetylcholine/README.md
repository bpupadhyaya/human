---
schema: human-scale-entry/v1
id: acetylcholine
name: Acetylcholine
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-05
summary: "Quaternary ammonium ester (MW 182.65) synthesised by ChAT from acetyl-CoA + choline. Activates nicotinic (ionotropic) and muscarinic (GPCR) receptors at NMJ, autonomic ganglia, and CNS. AChE hydrolysis terminates signal in <1 ms. Deficiency underlies Alzheimer's disease."
aliases: ["ACh", "choline acetyltransferase product", "acetylcholinesterase substrate"]
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
  - target: 01-human/04-cellular/neuron
    relation: modulates
    note: "ACh is primary neurotransmitter of motor neurons at NMJ and CNS cholinergic projections (basal forebrain→cortex/hippocampus); requires ChAT synthesis, VAChT packaging, Ca²⁺-triggered exocytosis, and AChE hydrolysis."
  - target: 01-human/04-cellular/sa-node-cell
    relation: modulates
    note: "Vagal ACh activates M2 mAChR on SA node → Gi → ↓adenylyl cyclase → ↓cAMP → ↑IKACh (GIRK channels) → hyperpolarisation → ↓HR (negative chronotropy)."
  - target: 01-human/05-tissue/synapse
    relation: modulates
    note: "ACh released at chemical synapses by exocytosis; AChE in synaptic cleft ensures brief signal duration (<1 ms); nicotinic fast response vs muscarinic GPCR-mediated slow modulation."
  - target: 01-human/07-system/nervous-system
    relation: modulates
    note: "ACh is the primary peripheral motor and autonomic preganglionic neurotransmitter; basal forebrain cholinergic neurons project to cortex/hippocampus regulating attention, REM sleep, and memory consolidation."
  - target: 01-human/07-system/myasthenia-gravis
    relation: connects-to
    note: "In MG, anti-AChR IgG activates complement → MAC destroys AChR at the NMJ; reduced AChR density → impaired NMJ transmission → fatigable weakness; pyridostigmine (AChE inhibitor) compensates by prolonging ACh dwell time; eculizumab and efgartigimod are targeted therapies."
  - target: 01-human/07-system/alzheimers-disease
    relation: connects-to
    note: "Selective degeneration of nucleus basalis of Meynert cholinergic neurons → cortical ACh deficiency → impaired attention and memory encoding (cholinergic hypothesis); AChE inhibitors (donepezil, rivastigmine, galantamine) are first-line symptomatic therapy for mild-moderate AD."
  - target: 01-human/07-system/parkinsons-disease
    relation: connects-to
    note: "Striatal cholinergic interneurons become relatively hyperactive when nigrostriatal dopamine is lost in PD → tremor and rigidity; anticholinergics (trihexyphenidyl) reduce tremor in younger PD patients; rivastigmine (AChEI) is FDA-approved for Parkinson's disease dementia (PDD)."
---

# Acetylcholine

## Overview

Acetylcholine (ACh) is a quaternary ammonium ester neurotransmitter with molecular weight 182.65 Da, present at neuromuscular junctions, autonomic ganglia, parasympathetic postganglionic synapses, and widely distributed CNS circuits.[^stryer-biochemistry] It was the first neurotransmitter to be identified (Otto Loewi, 1921, "Vagusstoff") and remains pharmacologically the most extensively exploited. ACh acts through two receptor superfamilies — **nicotinic** (ionotropic, fast) and **muscarinic** (metabotropic, slower) — producing effects ranging from skeletal muscle contraction to slowing of heart rate, glandular secretion, and regulation of cognition and sleep.[^alberts-mol-cell-biology]

## Structure

ACh is a simple ester: **choline + acetate**, linked through an ester bond. The quaternary ammonium nitrogen bears a permanent positive charge at physiological pH, which anchors ACh in the binding pockets of both nAChRs and mAChRs via cation-π interactions with aromatic residues (Tyr, Trp).[^stryer-biochemistry]

**Choline acetyltransferase (ChAT)** catalyses:
> Acetyl-CoA + Choline → ACh + CoA (ΔG ≈ −13 kJ/mol)

ChAT is cytoplasmic in the presynaptic terminal; its expression is the defining marker of cholinergic neurons.[^stryer-biochemistry]

## Function

### Receptor Pharmacology

| Receptor | Type | Transduction | Location | Effect |
|----------|------|-------------|---------|--------|
| nAChR (α1₂β1γδ) | Ionotropic (pentameric Na⁺/K⁺ channel) | Direct | NMJ motor endplate | End-plate potential → AP → contraction |
| nAChR (α3β4) | Ionotropic | Direct | Autonomic ganglia | Ganglionic transmission |
| nAChR (α7) | Ionotropic (high Ca²⁺ perm.) | Direct | CNS | Cognition, LTP, neuroprotection |
| M1 mAChR | GPCR (Gq) | PLC → IP3/DAG | Neural, gastric parietal | Excitation, ↑ gastric acid |
| M2 mAChR | GPCR (Gi) | ↓cAMP, ↑IKACh | Cardiac SA/AV node, atria | ↓HR, ↓AV conduction |
| M3 mAChR | GPCR (Gq) | PLC → IP3/DAG | Smooth muscle, glands | Contraction, secretion |
| M4 mAChR | GPCR (Gi) | ↓cAMP | CNS presynaptic | Inhibition of DA/ACh release |
| M5 mAChR | GPCR (Gq) | PLC | Brain vasculature | Vasodilation |

### Cholinergic Circuits
- **NMJ**: α-motor neuron → ACh → α1 nAChR end-plate potential → Na⁺ influx → VGSC → action potential → Ca²⁺ release → muscle contraction.[^alberts-mol-cell-biology]
- **Autonomic**: preganglionic fibres (both sympathetic and parasympathetic) → nicotinic ganglionic nAChR; parasympathetic postganglionic → muscarinic target organ receptors.
- **CNS**: basal forebrain nuclei — **nucleus basalis of Meynert** → neocortex; **medial septal nucleus** → hippocampus; **diagonal band** → olfactory bulb, amygdala. These cholinergic projections regulate arousal, attention, working memory, and REM sleep.[^alberts-mol-cell-biology]

## Mechanism

### Synthesis and Vesicular Storage

1. **Choline uptake**: high-affinity choline transporter **CHT1 (SLC5A7)** at the presynaptic plasma membrane — Na⁺-dependent, rate-limiting for ACh synthesis in many neurons.[^stryer-biochemistry]
2. **ACh synthesis**: ChAT (cytoplasmic) converts choline + acetyl-CoA → ACh. Acetyl-CoA derived from mitochondrial pyruvate dehydrogenase or citrate transport to cytoplasm.
3. **Vesicular packaging**: **VAChT (SLC18A3)** on synaptic vesicle membrane exchanges 2 H⁺ per ACh molecule, driven by the V-type H⁺-ATPase proton gradient. Each vesicle contains ~10,000 ACh molecules.[^alberts-mol-cell-biology]

### Exocytosis

Action potential → **voltage-gated Ca²⁺ channels** (primarily P/Q-type, Cav2.1) open → Ca²⁺ influx at active zones → Ca²⁺ binds **synaptotagmin-1** (C2A/C2B domains) → triggers **SNARE complex** zippering (VAMP2/synaptobrevin on vesicle + SNAP-25 + syntaxin-1 on target membrane) → vesicle fusion → ACh exocytosis into synaptic cleft.[^alberts-mol-cell-biology]

**Botulinum neurotoxins (BoNT A–G)** are zinc metalloproteases that cleave SNARE proteins:
- BoNT-A, -C, -E → cleave SNAP-25
- BoNT-B, -D, -F, -G → cleave VAMP2
- BoNT-C also cleaves syntaxin-1
Result: irreversible inhibition of ACh release → flaccid paralysis (therapeutic uses: dystonia, cosmetic, hyperhidrosis).

### Termination: AChE Hydrolysis

**Acetylcholinesterase (AChE)** is one of the fastest enzymes known (~25,000 catalytic events/second per active site). It is anchored in the synaptic cleft via the ColQ collagenous tail at the NMJ, or via GPI anchors (PRiMA isoform) in the CNS.[^stryer-biochemistry]

Catalytic mechanism (serine hydrolase):
1. Ser203 (active site) attacks the ester carbonyl → tetrahedral intermediate → **acetyl-enzyme intermediate** + choline released
2. Water attacks the acetyl-enzyme → deacylation → acetate released, Ser203 regenerated
Half-time of ACh hydrolysis: **< 1 ms** in the synaptic cleft.

Choline is recycled by CHT1 (reuptake into presynaptic terminal). There is no intact ACh reuptake transporter.[^stryer-biochemistry]

## Connections

- **Modulates neuron** — ACh is primary neurotransmitter of motor neurons at NMJ and CNS cholinergic projections (basal forebrain→cortex/hippocampus); requires ChAT synthesis, VAChT packaging, Ca²⁺-triggered exocytosis, and AChE hydrolysis. See [neuron](../../04-cellular/neuron/README.md).
- **Modulates SA node cell** — Vagal ACh activates M2 mAChR on SA node → Gi → ↓adenylyl cyclase → ↓cAMP → ↑IKACh (GIRK channels) → hyperpolarisation → ↓HR (negative chronotropy). See [sa-node-cell](../../04-cellular/sa-node-cell/README.md).
- **Modulates synapse** — ACh released at chemical synapses by exocytosis; AChE in synaptic cleft ensures brief signal duration (<1 ms); nicotinic fast response vs muscarinic GPCR-mediated slow modulation. See [synapse](../../05-tissue/synapse/README.md).
- **Modulates nervous system** — ACh is the primary peripheral motor and autonomic preganglionic neurotransmitter; basal forebrain cholinergic neurons project to cortex/hippocampus regulating attention, REM sleep, and memory consolidation. See [nervous-system](../../07-system/nervous-system/README.md).
- `connects-to` → **[Myasthenia Gravis](../../07-system/myasthenia-gravis/README.md)** — In MG, anti-AChR IgG activates complement → MAC destroys AChR at the NMJ; reduced AChR density → impaired NMJ transmission → fatigable weakness; pyridostigmine (AChE inhibitor) compensates by prolonging ACh dwell time; eculizumab and efgartigimod are targeted therapies.
- `connects-to` → **[Alzheimer's Disease](../../07-system/alzheimers-disease/README.md)** — selective degeneration of nucleus basalis of Meynert cholinergic neurons → cortical ACh deficiency → impaired attention and memory encoding; AChE inhibitors (donepezil, rivastigmine, galantamine) are first-line symptomatic therapy for mild-moderate AD; the cholinergic hypothesis explains symptoms but not the primary amyloid/tau pathology.
- `connects-to` → **[Parkinson's Disease](../../07-system/parkinsons-disease/README.md)** — striatal cholinergic interneurons become relatively hyperactive when nigrostriatal dopamine is lost in PD → tremor and rigidity; anticholinergics (trihexyphenidyl) reduce tremor in younger PD patients; rivastigmine (AChEI) is FDA-approved for Parkinson's disease dementia (PDD).

## Pathology

### Myasthenia Gravis (MG)
Autoimmune destruction of NMJ nAChRs: ~85% of patients have **anti-AChR antibodies** (accelerate receptor internalisation, fix complement); ~10% have **anti-MuSK antibodies** (disrupt AChR clustering via agrin/rapsyn pathway). Clinical: fatigable weakness — ptosis, diplopia, bulbar palsy, respiratory failure ("myasthenic crisis"). Treatment: **AChE inhibitors** (pyridostigmine — accumulate ACh at NMJ), thymectomy (50% have thymoma), immunosuppression (prednisolone, azathioprine), IVIG/plasmapheresis for crisis; eculizumab, efgartigimod (FcRn antagonist) for refractory MG.[^alberts-mol-cell-biology]

### Lambert-Eaton Myasthenic Syndrome (LEMS)
Anti-Cav2.1 (P/Q-type VGCC) antibodies → ↓ presynaptic Ca²⁺ influx → ↓ ACh exocytosis → proximal muscle weakness (improves with repetitive stimulation — characteristic EMG finding). Paraneoplastic (SCLC) in ~60%. Treatment: 3,4-diaminopyridine (K⁺ channel blocker → prolonged AP → more Ca²⁺ influx).

### Organophosphate / Nerve Agent Poisoning
Irreversible (or very slowly reversible) AChE inhibition by organophosphates (insecticides: parathion, malathion) or nerve agents (sarin, VX — phosphorylate Ser203). ACh accumulates → **cholinergic crisis**. Classic toxidrome: **SLUDGE** — Salivation, Lacrimation, Urination, Defecation, GI distress, Emesis (muscarinic); plus bradycardia, miosis, bronchospasm; nicotinic effects: fasciculations, weakness, paralysis. Treatment: **atropine** (competitive M-receptor antagonist, large doses until secretions dry) + **pralidoxime (2-PAM)** (reactivates AChE before "ageing" — spontaneous Ser-P stabilisation — occurs).[^stryer-biochemistry]

### Alzheimer's Disease — Cholinergic Hypothesis
Selective degeneration of nucleus basalis of Meynert cholinergic neurons → ↓ cortical ACh → impaired attention and memory encoding. Treatment rationale: AChE inhibitors (**donepezil**, **rivastigmine**, **galantamine**) prolong synaptic ACh. Also: memantine (NMDA antagonist). Note: the cholinergic hypothesis explains symptoms but does not address the primary amyloid/tau pathology.[^alberts-mol-cell-biology]

### Congenital Myasthenic Syndromes
Genetic defects in ACh pathway components: CHT1 mutations (↓ choline uptake), ChAT mutations (↓ ACh synthesis, episodic apnoea), AChE deficiency (ColQ or COLQ mutations — SLUDGE-like hyperactivation at NMJ, paradoxically worsened by AChEi), nAChR subunit mutations (slow-channel, fast-channel syndromes).

[^stryer-biochemistry]: Berg JM, Tymoczko JL, Stryer L. *Biochemistry*. 9th ed. W.H. Freeman; 2019.
[^alberts-mol-cell-biology]: Alberts B, Johnson A, Lewis J, et al. *Molecular Biology of the Cell*. 7th ed. W.W. Norton; 2022.

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
