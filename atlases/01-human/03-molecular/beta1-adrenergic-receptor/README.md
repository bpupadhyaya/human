---
schema: human-scale-entry/v1
id: beta1-adrenergic-receptor
name: β1-adrenergic receptor
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-03
summary: "G-protein-coupled receptor (Gαs / cAMP / PKA) on cardiomyocytes and renal juxtaglomerular cells. The molecular relay through which sympathetic nervous activation accelerates and amplifies the heartbeat; the principal target of β-blockers."
aliases: ["β1AR", "ADRB1", "beta1 adrenoreceptor"]
sources:
  - id: uniprot-p08588-adrb1
    type: database
    cite: "UniProt P08588 — Beta-1 adrenergic receptor (ADRB1, human)."
    url: "https://www.uniprot.org/uniprotkb/P08588/entry"
    accessed: "2026-06-03"
  - id: warne-2008-b1ar-structure
    type: peer-reviewed
    cite: "Warne T, Serrano-Vega MJ, Baker JG, et al. Structure of a beta1-adrenergic G-protein-coupled receptor. Nature. 2008;454(7203):486-91."
    doi: "10.1038/nature07101"
    pmid: "18594507"
  - id: lefkowitz-2007-b-arrestin-review
    type: peer-reviewed
    cite: "Lefkowitz RJ, Shenoy SK. Transduction of receptor signals by beta-arrestins. Science. 2005;308(5721):512-7."
    doi: "10.1126/science.1109237"
    pmid: "15845844"
  - id: bristow-2000-bar-failure
    type: peer-reviewed
    cite: "Bristow MR. β-Adrenergic receptor blockade in chronic heart failure. Circulation. 2000;101(5):558-69."
    doi: "10.1161/01.CIR.101.5.558"
    pmid: "10662755"
  - id: heidenreich-2022-hf-guideline
    type: clinical-guideline
    cite: "Heidenreich PA, Bozkurt B, Aguilar D, et al. 2022 AHA/ACC/HFSA Guideline for the Management of Heart Failure. Circulation. 2022;145(18):e895-e1032."
    doi: "10.1161/CIR.0000000000001063"
    pmid: "35363499"
cross_links:
  - target: 01-human/04-cellular/cardiomyocyte
    relation: expressed-by
    note: "Predominant β-adrenergic receptor on working cardiomyocytes (~75–80% of total β-AR in healthy ventricle); also expressed on SA-nodal pacemaker cells."
  - target: 01-human/02-atomic/calcium
    relation: modulated-by
    note: "β1-AR/PKA signaling modulates Ca²⁺ handling: Cav1.2 and RyR2 phosphorylation increase Ca²⁺ transient amplitude; phospholamban phosphorylation accelerates SERCA reuptake."
  - target: 01-human/04-cellular/sa-node-cell
    relation: expressed-by
    note: "SA node pacemaker cells express β1-AR; sympathetic activation shifts the HCN4 (If) activation curve rightward — positive chronotropy."
  - target: 03-medicine/01-modern/04-cardio/beta-blockers
    relation: target-of
    note: "β-blockers (metoprolol, bisoprolol, carvedilol) competitively antagonise β1-AR and are first-line therapy for HFrEF, hypertension, angina, and post-MI prophylaxis."
  - target: 01-human/03-molecular/ryr2
    relation: modulates
    note: "β1-AR/PKA phosphorylates RyR2 at Ser2808, increasing channel open probability and SR Ca²⁺ release gain — part of the inotropic response."
  - target: 01-human/03-molecular/serca2a
    relation: modulates
    note: "β1-AR/PKA phosphorylates phospholamban (PLN) at Ser16, relieving PLN inhibition of SERCA2a → faster Ca²⁺ reuptake → lusitropy and increased SR Ca²⁺ loading."
  - target: 01-human/03-molecular/phospholamban
    relation: modulates
    note: "β1-AR/PKA phosphorylates PLN at Ser16 — the dominant regulatory switch that relieves SERCA2a inhibition and produces the sympathetic lusitropic response."
  - target: 01-human/03-molecular/hcn4
    relation: modulates
    note: "cAMP produced downstream of β1-AR binds the CNBD of HCN4, shifting I_f activation by ~+10 mV → faster diastolic depolarisation → positive chronotropy."
  - target: 01-human/03-molecular/epinephrine
    relation: modulated-by
    note: "Modulated by Epinephrine."
  - target: 01-human/03-molecular/norepinephrine
    relation: modulated-by
    note: "Modulated by Norepinephrine."
taxonomy:
  uniprot: "P08588"
  gene_symbol: "ADRB1"
  pdb_examples: ["2VT4", "2Y00", "4AMI"]
---

# β1-adrenergic receptor

## Overview

The β1-adrenergic receptor (β1AR) is the **primary molecular relay** through which the sympathetic nervous system accelerates and amplifies the heartbeat. It is a seven-transmembrane G-protein-coupled receptor (GPCR), encoded in humans by `ADRB1` [^uniprot-p08588-adrb1], expressed densely on cardiomyocytes (working and nodal) and on the juxtaglomerular cells of the kidney where it stimulates renin release. When circulating epinephrine or sympathetic-nerve-released norepinephrine binds, β1AR couples to **Gαs**, raises intracellular cAMP, activates **PKA**, and triggers a phosphorylation cascade that simultaneously increases heart rate, contractility, conduction velocity, and rate of relaxation.

It is also one of the most therapeutically important targets in all of cardiovascular medicine. **β-blockers** — selective antagonists at β1AR — are first-line therapy for hypertension, angina, post-myocardial-infarction prophylaxis, certain arrhythmias, and heart failure with reduced ejection fraction [^heidenreich-2022-hf-guideline]. Their efficacy in heart failure is somewhat counter-intuitive (blocking the receptor that *increases* contractility, in patients with already-reduced contractility) and is mechanistically explained by long-term protection from chronic catecholamine toxicity [^bristow-2000-bar-failure].

## Structure

### Family and topology

β1AR belongs to **Class A (rhodopsin-like)** GPCRs and shares the canonical architecture: a **seven-transmembrane α-helical bundle** with an extracellular N-terminus, three extracellular loops (ECL1–3), three intracellular loops (ICL1–3), and an intracellular C-terminal tail.

Key features:

| Feature | Function |
|:---|:---|
| TM3, TM5, TM6, TM7 | Form the orthosteric ligand-binding pocket between the extracellular ends of these helices |
| **Asp³·³² (TM3)** | Critical aspartate that coordinates the protonated amine of catecholamines via salt bridge — the universal anchor for adrenergic and many other monoamine ligands |
| **Ser⁵·⁴², Ser⁵·⁴⁶ (TM5)** | Hydrogen-bond to the catechol hydroxyls of natural agonists (NE, Epi); specificity for catechols vs. non-catechol ligands hinges on this region |
| ICL3 | Couples to Gαs; subject to phosphorylation by GRK2/3 and PKA |
| C-terminal tail | Phosphorylation sites for GRK2/3 → β-arrestin recruitment → desensitization and internalization |

The first **atomic-resolution structure** of a β1AR (turkey β1AR, used because it is more biochemically tractable than human β1AR) was solved in 2008 [^warne-2008-b1ar-structure], establishing the active and inactive conformations and revealing the basis of selectivity between β-subtypes.

### Subtype family

The β-adrenergic family has three members in humans, all GPCRs coupled primarily to Gαs:

| Receptor | Gene | UniProt | Predominant tissues | Role |
|:---|:---:|:---:|:---|:---|
| **β1-AR** | `ADRB1` | P08588 | Heart (~75–80 % of cardiac β-AR), kidney JG cells, adipose | Cardiac inotropy/chronotropy/lusitropy; renin release |
| β2-AR | `ADRB2` | P07550 | Lung (smooth muscle), vasculature, heart (~20 %), liver, skeletal muscle | Bronchodilation, vasodilation, glycogenolysis |
| β3-AR | `ADRB3` | P13945 | Brown / beige adipose, urinary bladder | Thermogenesis, bladder relaxation |

**Selectivity** between subtypes drives drug design: cardio-selective β-blockers (metoprolol, atenolol, bisoprolol) preferentially block β1AR, sparing β2-mediated bronchodilation. Selectivity is dose-dependent — at higher doses, "cardioselective" agents lose specificity.

### Endogenous ligands

| Ligand | Source | Affinity at β1AR (vs β2) |
|:---|:---|:---|
| **Norepinephrine** | Postganglionic sympathetic neurons; adrenal medulla (~20 %) | Approximately equal at β1 and β2 (often described as "β1-preferring" because of physiological context) |
| **Epinephrine** | Adrenal medulla (~80 %) | Higher β2 affinity than NE; potent at both β1 and β2 |

In a healthy heart, **norepinephrine spillover** from sympathetic nerve terminals is the dominant β1AR activator; circulating epinephrine becomes important during stress and exercise.

## Function

### Tissue-level effects of β1AR activation

| Tissue | Effect | Cellular mechanism |
|:---|:---|:---|
| **SA node** | Positive **chronotropy** (faster pacemaker rate) | PKA phosphorylates HCN4 → faster diastolic depolarization; phosphorylates Cav1.2 → larger ICaL contribution to upstroke |
| **AV node** | Positive **dromotropy** (faster conduction) | PKA-enhanced ICaL accelerates conduction |
| **Atrial / ventricular myocardium** | Positive **inotropy** (stronger contraction) | PKA phosphorylates Cav1.2 (more Ca²⁺ in), RyR2 (more SR release), troponin I (faster relaxation), phospholamban (faster SR uptake) |
| **Atrial / ventricular myocardium** | Positive **lusitropy** (faster relaxation) | PKA on phospholamban (relieves SERCA inhibition) and on troponin I (reduces myofilament Ca²⁺ sensitivity) |
| **Kidney (juxtaglomerular cells)** | Renin release | Activates renin–angiotensin–aldosterone system, raising blood pressure and volume |

The cardiac effects together produce the response we recognize as **fight-or-flight**: a heart beating faster, harder, and more thoroughly relaxing between beats — increased cardiac output to match metabolic demand.

## Mechanism

### Canonical Gαs / cAMP / PKA cascade

1. **Ligand binding.** Norepinephrine or epinephrine enters the orthosteric pocket between TM3, TM5, TM6, TM7. The catechol amine is anchored by a salt bridge to **Asp³·³²**; the catechol hydroxyls hydrogen-bond to **Ser⁵·⁴² / Ser⁵·⁴⁶**. The receptor undergoes a conformational change — most prominent at the **intracellular end of TM6**, which swings outward by ~10–14 Å — opening a binding cavity for the G protein.
2. **G protein engagement.** The active receptor binds **Gαs** (heterotrimer Gαsβγ). Receptor-induced conformational change in Gαs releases GDP; GTP binds; Gαs-GTP dissociates from Gβγ.
3. **Adenylyl cyclase activation.** Gαs-GTP binds and activates **adenylyl cyclase** (the cardiac isoforms AC5 and AC6 dominate). ATP → cAMP.
4. **PKA activation.** cAMP binds to the **regulatory subunits** of protein kinase A (PKA), releasing the catalytic subunits.
5. **Substrate phosphorylation.** Active PKA phosphorylates Ser/Thr residues on a defined set of cardiac substrates, each producing a specific physiological effect:

   | PKA substrate | Effect |
   |:---|:---|
   | **Cav1.2 (L-type Ca²⁺ channel)** β-subunit | More Ca²⁺ influx during plateau → larger Ca²⁺ transient → stronger contraction |
   | **RyR2** | More cooperative SR Ca²⁺ release |
   | **Phospholamban** (relieves inhibition of SERCA2a) | Faster SR Ca²⁺ uptake → faster relaxation; greater SR loading → larger next transient |
   | **Troponin I** Ser23/24 | Reduces myofilament Ca²⁺ sensitivity → faster relaxation |
   | **Myosin-binding protein C** | Cross-bridge kinetics modulation |
   | **HCN4** (in nodal cells) | Faster pacemaker depolarization |

   The result is a coordinated, multi-target tuning of the cardiomyocyte that the cell could not achieve through any single phosphorylation.

6. **Termination.** Gαs hydrolyzes its GTP to GDP (intrinsic GTPase, accelerated by RGS proteins); cAMP is degraded by phosphodiesterases (PDE3, PDE4 dominate in heart); PKA is reabsorbed onto its regulatory subunits.

### Desensitization and β-arrestin signaling

Sustained β1AR activation triggers two layers of desensitization:

1. **GRK phosphorylation.** GRK2/3 phosphorylate the receptor's intracellular loops and C-tail.
2. **β-arrestin recruitment.** β-arrestin-1/2 binds the phosphorylated receptor, sterically blocks further G-protein coupling, and triggers receptor internalization.

But β-arrestin is not just an off-switch — it is also a **signaling scaffold** that activates **MAPK (ERK1/2)** pathways independently of G-protein signaling [^lefkowitz-2007-b-arrestin-review]. This bifurcation is the basis of "biased agonism" — drugs that preferentially activate G-protein vs. β-arrestin signaling are an active area of cardiovascular drug design.

### β1AR in heart failure

Chronic catecholamine excess (as in chronic heart failure) drives:

- **β1AR down-regulation** — receptor density falls by 50 % or more in advanced HFrEF; the surviving β-AR pool shifts toward β2.
- **Functional uncoupling** — increased GRK2 expression hyper-phosphorylates β1AR, weakening Gαs coupling.
- **Pro-apoptotic signaling** — sustained β1AR activation triggers cardiomyocyte apoptosis via Ca²⁺/CaMKII and other pathways.

Β-blockers protect against this chronic toxicity. They blunt sympathetic drive, restore β1AR density and coupling, and improve survival in HFrEF — the central insight that turned β-blockade from contraindicated-in-failure to first-line therapy [^bristow-2000-bar-failure].

## Connections

- **Up (containing cell):** the β1-adrenergic receptor is `part-of` the **[cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)**, embedded in the sarcolemma. Also expressed on SA/AV-nodal cells and on renal juxtaglomerular cells (entries to come).
- **Sideways (signaling):** activates the canonical **Gαs / adenylyl cyclase / cAMP / PKA** pathway, then phosphorylates a defined set of cardiac substrates including **[troponin complex](troponin-complex/README.md)** TnI Ser23/24, phospholamban, Cav1.2, RyR2, and HCN4.
- **Cross-atlas (planned in Phase 3):** the β1-adrenergic receptor is the **target of metoprolol** and the broader β-blocker drug class — entries in the Medicine Atlas.

## Pathology

- **Heart failure with reduced ejection fraction (HFrEF).** Chronic β1AR overstimulation contributes to disease progression; β1AR down-regulation is a hallmark of the failing myocardium [^bristow-2000-bar-failure].
- **Catecholamine-induced cardiomyopathy** (e.g., Takotsubo / stress cardiomyopathy, pheochromocytoma). Acute massive β-adrenergic overload produces transient regional dysfunction.
- **Arrhythmias.** Excessive β1AR-driven Ca²⁺ leak (via PKA-phosphorylated RyR2) generates afterdepolarizations that trigger arrhythmias — particularly in catecholaminergic polymorphic VT and in the failing heart.

## Variation

- **Arg389Gly polymorphism** (`ADRB1` codon 389). The Arg389 variant produces stronger Gαs coupling than Gly389; it is associated with greater inotropic response and, in some studies, altered β-blocker response in heart failure.
- **Ser49Gly polymorphism** (codon 49). The Gly49 variant is more readily down-regulated, possibly altering long-term β-blocker sensitivity.
- **Sex.** Some studies show modest sex differences in β1AR density and downstream cAMP responses.

These pharmacogenomic variants have been studied in the context of personalizing β-blocker therapy; clinical use is not yet routine but is an active research area.

## Open questions

- **Biased agonism in HF.** Can ligands designed to favor β-arrestin signaling (cardioprotective) over G-protein signaling (cardiotoxic in chronic excess) outperform conventional β-blockers? Carvedilol shows some bias and is among the most effective β-blockers in HFrEF, but causality is unsettled.
- **β1 vs β2 vs β3 in the failing heart.** As β1 down-regulates, the relative role of β2 and β3 grows. β3-AR signaling, which can be cardioprotective via NO/cGMP, is being explored therapeutically (e.g., mirabegron repurposing trials).
- **β-arrestin's exact substrate repertoire** in cardiomyocytes is not fully mapped; new substrates are still being identified.

## See also

- [`troponin-complex`](troponin-complex/README.md) — phosphorylated by PKA downstream of β1AR; site of the lusitropic effect.
- [`cardiomyocyte`](../../04-cellular/cardiomyocyte/README.md) — the cell expressing this receptor.
- [`heart`](../../06-organ/heart/README.md) — the organ this receptor regulates.

[^uniprot-p08588-adrb1]: UniProt — Beta-1 adrenergic receptor (ADRB1, human; P08588). [uniprot.org/uniprotkb/P08588](https://www.uniprot.org/uniprotkb/P08588/entry)
[^warne-2008-b1ar-structure]: Warne T, Serrano-Vega MJ, Baker JG, et al. Structure of a beta1-adrenergic G-protein-coupled receptor. *Nature.* 2008;454(7203):486-491. [doi:10.1038/nature07101](https://doi.org/10.1038/nature07101) · [PubMed 18594507](https://pubmed.ncbi.nlm.nih.gov/18594507/)
[^lefkowitz-2007-b-arrestin-review]: Lefkowitz RJ, Shenoy SK. Transduction of receptor signals by beta-arrestins. *Science.* 2005;308(5721):512-517. [doi:10.1126/science.1109237](https://doi.org/10.1126/science.1109237) · [PubMed 15845844](https://pubmed.ncbi.nlm.nih.gov/15845844/)
[^bristow-2000-bar-failure]: Bristow MR. β-Adrenergic receptor blockade in chronic heart failure. *Circulation.* 2000;101(5):558-569. [doi:10.1161/01.CIR.101.5.558](https://doi.org/10.1161/01.CIR.101.5.558) · [PubMed 10662755](https://pubmed.ncbi.nlm.nih.gov/10662755/)
[^heidenreich-2022-hf-guideline]: Heidenreich PA, Bozkurt B, Aguilar D, et al. 2022 AHA/ACC/HFSA Guideline for the Management of Heart Failure. *Circulation.* 2022;145(18):e895–e1032. [doi:10.1161/CIR.0000000000001063](https://doi.org/10.1161/CIR.0000000000001063) · [PubMed 35363499](https://pubmed.ncbi.nlm.nih.gov/35363499/)
