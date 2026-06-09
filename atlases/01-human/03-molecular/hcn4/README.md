---
schema: human-scale-entry/v1
id: hcn4
name: HCN4
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-03
summary: "HCN4 (Hyperpolarization-activated Cyclic Nucleotide-gated channel 4, gene HCN4) — cardiac funny current (I_f). Activated by hyperpolarisation at ~−60 mV; carries mixed Na⁺/K⁺ inward current; directly gated by cAMP. Dominant pacemaker channel of the SA node; ivabradine target."
aliases: ["HCN4", "funny channel", "If channel", "pacemaker channel", "hyperpolarization-activated channel"]
sources:
  - id: difrancesco-2010-funny-current
    type: peer-reviewed
    cite: "DiFrancesco D. The role of the funny current in pacemaker activity. Circ Res. 2010;106(3):434-46."
    doi: "10.1161/CIRCRESAHA.109.208041"
    pmid: "20167941"
    url: "https://doi.org/10.1161/CIRCRESAHA.109.208041"
  - id: baruscotti-2011-hcn4-sa-node
    type: peer-reviewed
    cite: "Baruscotti M, Bucchi A, Viscomi C, et al. Deep bradycardia and heart block caused by inducible cardiac-specific knockout of the pacemaker channel gene Hcn4. Proc Natl Acad Sci USA. 2011;108(4):1705-10."
    doi: "10.1073/pnas.1010122108"
    pmid: "21205885"
    url: "https://doi.org/10.1073/pnas.1010122108"
  - id: ludwig-1999-hcn4-identification
    type: peer-reviewed
    cite: "Ludwig A, Zong X, Jeglitsch M, Hofmann F, Biel M. A family of hyperpolarization-activated mammalian cation channels. Nature. 1998;393(6685):587-91."
    doi: "10.1038/31255"
    pmid: "9634236"
    url: "https://doi.org/10.1038/31255"
  - id: stieber-2003-hcn4-av-node
    type: peer-reviewed
    cite: "Stieber J, Herrmann S, Feil S, et al. The hyperpolarization-activated channel HCN4 underlies the If current in sinoatrial node myocytes. J Biol Chem. 2003;278(36):33672-80."
    doi: "10.1074/jbc.M208251200"
    pmid: "12826672"
    url: "https://doi.org/10.1074/jbc.M208251200"
cross_links:
  - target: 01-human/04-cellular/sa-node-cell
    relation: expressed-by
    note: "HCN4 is the dominant HCN isoform in SA node pacemaker cells, accounting for >80% of cardiac I_f; its activation during hyperpolarisation drives diastolic depolarisation and pacemaker automaticity."
  - target: 01-human/03-molecular/beta1-adrenergic-receptor
    relation: modulated-by
    note: "β1-AR/Gαs/adenylyl cyclase raises cAMP, which binds the CNBD of HCN4 and shifts its activation curve ~+10 mV rightward → more I_f at any given diastolic potential → faster pacemaker rate (positive chronotropy)."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Ivabradine (HCN4 I_f blocker) reduces HR by 10-15 bpm without impairing contractility; SHIFT trial: ivabradine reduced HF hospitalization 18% in HFrEF with HR >70 bpm on maximally tolerated beta-blocker; elevated resting HR in HF reflects HCN4/sympathetic co-activation."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "HCN4 at the SA node is the molecular basis of cardiac automaticity; cAMP directly gates HCN4 → molecular transducer of sympathetic (+10 mV shift → tachycardia) and vagal (-10 mV shift → bradycardia) chronotropic control; HCN4 loss-of-function mutations cause sick sinus syndrome."
taxonomy:
  uniprot: "Q9Y3Q4"
  gene_symbol: "HCN4"
  chromosome: "15q24.1"
---

# HCN4

## Overview

HCN4 (Hyperpolarization-activated Cyclic Nucleotide-gated channel 4) is the **molecular basis of the cardiac funny current (I_f)** — the pacemaker current discovered by Dario DiFrancesco in the 1970s and named "funny" because it activates upon membrane **hyperpolarisation** (opposite to most voltage-gated channels) and carries a **mixed inward Na⁺/K⁺ current** [^difrancesco-2010-funny-current].

HCN4 is the dominant HCN isoform in the sinoatrial (SA) node pacemaker cells, where I_f is the primary current driving spontaneous **diastolic depolarisation (phase 4)** — the gradual voltage rise from the maximum diastolic potential (~−60 mV) to the threshold for the next action potential (~−40 mV). By controlling the rate of this slow depolarisation, HCN4 sets the intrinsic heart rate. Its unique dual sensitivity to both **membrane voltage** and **intracellular cAMP** makes it the molecular integrator of autonomic heart rate control: sympathetic stimulation (↑cAMP) accelerates the channel and speeds pacemaking; vagal stimulation (↓cAMP) decelerates it.

HCN4 is also the specific molecular target of **ivabradine**, a pure heart-rate-lowering drug approved for stable angina and HFrEF with persistent tachycardia, providing proof-of-concept that I_f inhibition at the channel level translates to heart-rate reduction without affecting contractility [^difrancesco-2010-funny-current].

## Structure

### Family and Topology

HCN channels belong to the superfamily of voltage-gated channels but are evolutionarily and structurally related to both voltage-gated K⁺ (Kv) channels and cyclic-nucleotide-gated (CNG) channels:

| Feature | HCN4 |
|:---|:---|
| Topology | 6 transmembrane segments (S1–S6); cytoplasmic N- and C-termini |
| S4 | Voltage sensor; contains positively charged residues (Arg/Lys); outward movement at hyperpolarisation (reversed from Kv) activates the channel |
| S5–S6 linker (P-loop) | Forms the selectivity filter; GYG motif variant → mixed Na⁺/K⁺ permeability (PNa/PK ≈ 0.2–0.4) |
| C-linker | Connects S6 to the CNBD; critical for cAMP-dependent gating shift |
| **CNBD** | Cyclic nucleotide binding domain; binds cAMP directly (Kd ~0.1–1 µM); cAMP binding shifts activation curve ~+10 mV rightward |
| Assembly | Homotetramer; four subunits in 4-fold symmetry |

### Four-Subunit Assembly

Like Kv channels, HCN4 assembles as a homotetramer. Each subunit contributes one S5–S6 pore domain to the central ion-conducting pathway. Unlike Kv channels:
- The tetramer assembles without a T1 domain
- The large cytoplasmic C-terminal domains (C-linker + CNBD of each subunit) form an octameric ring below the membrane that transmits cAMP-binding signals to the gate

## Mechanism

### Hyperpolarization-Activated Gating

In a resting SA node cell (maximum diastolic potential ~−60 mV), HCN4 channels begin to open. As the membrane repolarises further (e.g., during action potential repolarisation to ~−60 to −70 mV), the S4 voltage sensors move inward (opposite to Kv channels), allowing the activation gate to open. The HCN4 activation curve half-maximal voltage V₁/₂ is approximately **−65 to −70 mV** in the absence of cAMP.

At physiological diastolic potentials (~−60 mV), the channel is only partially activated; this slow, progressive opening during phase 4 produces a sustained inward current (mixed Na⁺ and K⁺ → net inward at these potentials) that steadily depolarises the membrane toward threshold.

### cAMP Modulation

When cAMP rises (following β1-AR → Gαs → adenylyl cyclase activation):
1. cAMP binds to the CNBD of each HCN4 subunit (one cAMP per subunit)
2. This binding shifts the voltage-dependence of activation by ~+10 mV (rightward)
3. At the same diastolic potential, more HCN4 channels are now open → larger I_f → faster depolarisation → higher firing rate

The result: heart rate rises from ~60–75 bpm to 130–200 bpm during sympathetic activation, without any structural change in the channel — purely a conformational shift mediated by cAMP binding.

Conversely, acetylcholine (vagal stimulation) → M2 → Gi → ↓cAMP → shifts V₁/₂ leftward → less I_f at any given potential → slower pacemaking → bradycardia. This voltage-shift mechanism is different from IKAch-mediated hyperpolarisation and operates independently.

### Ion Selectivity and Current Characteristics

- **Ion species:** HCN4 carries Na⁺ and K⁺ inward at diastolic potentials; the reversal potential is approximately −25 to −35 mV (between ENa and EK)
- **Permeability:** PNa/PK ≈ 0.2–0.4 (relatively K⁺-selective but permeable to Na⁺ — an unusual combination)
- **Current magnitude in SA node:** I_f contributes ~10–30% of total diastolic depolarising current in central SA node cells; other contributors include ICaT, and the Ca²⁺ clock (NCX forward mode)

## Function

### Pacemaker Automaticity

At the SA node, HCN4 activation during phase 4 contributes ~10–30% of the net depolarising current that drives spontaneous action potential generation. However, genetic evidence confirms its essential role: cardiac-specific knockout of HCN4 in mice causes severe bradycardia and sinus arrest, demonstrating that HCN4 is indispensable for maintaining pacemaker rate [^baruscotti-2011-hcn4-sa-node].

The "voltage clock" (I_f, ICaT, ICaL) and "calcium clock" (spontaneous SR Ca²⁺ release → NCX forward mode → inward current) operate in concert as a coupled-oscillator system in SA node cells. HCN4 is the dominant component of the voltage clock.

### Rate Adaptation

The ~+10 mV shift in I_f activation by cAMP explains a substantial fraction of the heart rate increase during exercise and sympathetic stimulation. However, the total response (from ~75 to 180+ bpm) involves multiple parallel mechanisms:
- HCN4 shift (voltage clock acceleration)
- ICaL upregulation (faster, larger upstroke)
- Ca²⁺ clock acceleration via RyR2 and PLN phosphorylation
- AV nodal conduction acceleration

## Connections

- `expressed-by` → **[SA Node Cell](../../04-cellular/sa-node-cell/README.md)** — HCN4 is the dominant I_f channel of SA node pacemaker cells; its gating kinetics and cAMP sensitivity set the intrinsic heart rate.
- `modulated-by` → **[β1-Adrenergic Receptor](../beta1-adrenergic-receptor/README.md)** — cAMP produced downstream of β1-AR binds HCN4's CNBD, shifting I_f activation rightward → positive chronotropy.
- `connects-to` → **[Heart Failure](../../07-system/heart-failure/README.md)** — Ivabradine (HCN4 I_f blocker) reduces HR by 10-15 bpm without impairing contractility; SHIFT trial: ivabradine reduced HF hospitalization 18% in HFrEF with HR >70 bpm on maximally tolerated beta-blocker; elevated resting HR in HF reflects HCN4/sympathetic co-activation.
- `connects-to` → **[Cardiovascular System](../../07-system/cardiovascular-system/README.md)** — HCN4 at the SA node is the molecular basis of cardiac automaticity; cAMP directly gates HCN4 → molecular transducer of sympathetic (+10 mV shift → tachycardia) and vagal (-10 mV shift → bradycardia) chronotropic control; HCN4 loss-of-function mutations cause sick sinus syndrome.

## Pathology

| Disease | HCN4 mechanism |
|:---|:---|
| **Sick sinus syndrome (familial)** | Loss-of-function mutations in HCN4 (e.g., Arg524Gln, which prevents cAMP-dependent shift); autosomal dominant; symptomatic bradycardia, sinus arrest, paroxysmal atrial fibrillation |
| **Inappropriate sinus tachycardia** | Rare HCN4 gain-of-function mutations shift I_f activation rightward; clinical ivabradine treatment effective |
| **Ivabradine pharmacology** | Ivabradine is a specific use-dependent open-channel blocker of I_f (HCN4 > HCN1); accesses the channel from the intracellular face; reduces HR by 10–15 bpm without affecting contractility; approved for stable angina and HFrEF with HR > 70 bpm on maximally tolerated beta-blocker [^difrancesco-2010-funny-current] |
| **Congenital heart block** | Some HCN4 mutations associated with atrioventricular conduction abnormalities |

## See Also

- [SA node cell](../../04-cellular/sa-node-cell/README.md) — the pacemaker cell expressing HCN4.
- [β1-adrenergic receptor](beta1-adrenergic-receptor/README.md) — upstream regulator via cAMP.
- [Calcium](../../02-atomic/calcium/README.md) — part of the Ca²⁺ clock that coordinates with I_f.

[^difrancesco-2010-funny-current]: DiFrancesco D. The role of the funny current in pacemaker activity. *Circ Res.* 2010;106(3):434-46. [doi:10.1161/CIRCRESAHA.109.208041](https://doi.org/10.1161/CIRCRESAHA.109.208041) · [PubMed 20167941](https://pubmed.ncbi.nlm.nih.gov/20167941/)
[^baruscotti-2011-hcn4-sa-node]: Baruscotti M, Bucchi A, Viscomi C, et al. Deep bradycardia and heart block caused by inducible cardiac-specific knockout of the pacemaker channel gene Hcn4. *Proc Natl Acad Sci USA.* 2011;108(4):1705-10. [doi:10.1073/pnas.1010122108](https://doi.org/10.1073/pnas.1010122108) · [PubMed 21205885](https://pubmed.ncbi.nlm.nih.gov/21205885/)
[^ludwig-1999-hcn4-identification]: Ludwig A, Zong X, Jeglitsch M, Hofmann F, Biel M. A family of hyperpolarization-activated mammalian cation channels. *Nature.* 1998;393(6685):587-91. [doi:10.1038/31255](https://doi.org/10.1038/31255) · [PubMed 9634236](https://pubmed.ncbi.nlm.nih.gov/9634236/)
[^stieber-2003-hcn4-av-node]: Stieber J, Herrmann S, Feil S, et al. The hyperpolarization-activated channel HCN4 underlies the If current in sinoatrial node myocytes. *J Biol Chem.* 2003;278(36):33672-80. [doi:10.1074/jbc.M208251200](https://doi.org/10.1074/jbc.M208251200) · [PubMed 12826672](https://pubmed.ncbi.nlm.nih.gov/12826672/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
