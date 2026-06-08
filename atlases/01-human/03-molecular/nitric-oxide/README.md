---
schema: human-scale-entry/v1
id: nitric-oxide
name: Nitric Oxide
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-05
summary: "Free radical gas (MW 30.01, t½ <1 s in vivo); synthesised from L-arginine by NOS isoforms (eNOS, nNOS, iNOS). eNOS → vasodilation via sGC/cGMP/PKG; nNOS → synaptic plasticity; iNOS → antimicrobial. Dysregulation: hypertension, septic shock, erectile dysfunction."
aliases: ["NO", "nitrogen monoxide", "endothelium-derived relaxing factor", "EDRF", "nitric oxide radical", "NO•"]
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
  - id: furchgott-1980
    type: peer-reviewed
    cite: "Furchgott RF, Zawadzki JV. The obligatory role of endothelial cells in the relaxation of arterial smooth muscle by acetylcholine. Nature. 1980;288:373-376."
    url: "https://doi.org/10.1038/288373a0"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/07-system/cardiovascular-system
    relation: modulates
    note: "eNOS-derived NO is the primary endothelium-derived vasodilator: NO → sGC → ↑cGMP → PKG → MLCP → smooth muscle relaxation; also inhibits platelet aggregation and vascular smooth muscle proliferation."
  - target: 01-human/04-cellular/macrophage
    relation: modulates
    note: "iNOS in M1 macrophages generates sustained high-level NO + peroxynitrite (ONOO⁻) for pathogen killing; excess iNOS activity in sepsis produces vasodilatory NO causing refractory hypotension."
  - target: 01-human/07-system/nervous-system
    relation: modulates
    note: "nNOS NO is a retrograde synaptic messenger at glutamatergic synapses modulating LTP/LTD; NO in ENS regulates GI motility; sacral parasympathetic nNOS drives penile erection."
  - target: 01-human/03-molecular/nf-kb
    relation: modulates
    note: "iNOS transcription is induced by NF-κB downstream of LPS/IFN-γ/TNF-α; NO in turn S-nitrosylates IκBα and p65/RelA cysteines, providing negative feedback on NF-κB activity."
  - target: 01-human/05-tissue/arterial-wall
    relation: modulated-by
    note: "Modulated by Arterial Wall."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: modulated-by
    note: "Modulated by Smooth Muscle Cell."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "Impaired eNOS and NO bioavailability in PAH endothelium → cGMP vasodilation failure; PDE5 inhibitors (sildenafil, tadalafil) prevent cGMP degradation → sustained vasodilation + anti-proliferative; sGC stimulators (riociguat) amplify NO-sGC-cGMP independent of endogenous NO."
---

# Nitric Oxide

## Overview

**Nitric oxide (NO, NO•)** is a **free radical gas** — one unpaired electron, paramagnetic, highly reactive — that serves as a critical signaling molecule in virtually every organ system [^stryer-biochemistry]. With a biological half-life of less than one second in vivo (limited by rapid reaction with oxyhemoglobin, O₂, and superoxide), NO acts as a **paracrine mediator** over distances of only a few cell diameters, making local production the primary determinant of its physiological effects.

Its identity as the **endothelium-derived relaxing factor (EDRF)** — the mysterious vasodilatory signal released by endothelial cells — was established between 1980 and 1987 by Furchgott, Zawadzki, Ignarro, and Moncada [^furchgott-1980]. This discovery earned Robert Furchgott, Louis Ignarro, and Ferid Murad the **1998 Nobel Prize in Physiology or Medicine**, and fundamentally changed our understanding of how the cardiovascular, nervous, and immune systems communicate.

NO is produced by a family of three **nitric oxide synthase (NOS)** enzymes — eNOS, nNOS, and iNOS — each with distinct tissue expression, regulation, and physiological roles. The therapeutic implications are correspondingly broad: eNOS-related drugs include nitrates (organic NO donors), PDE5 inhibitors (sildenafil for erectile dysfunction and pulmonary hypertension), and inhaled NO (neonatal pulmonary hypertension); iNOS-targeted strategies are being developed for sepsis and inflammatory disease.

## Structure

**Molecular formula:** NO (or NO•)  
**Molecular weight:** 30.01 Da  
**Electronic structure:** Paramagnetic diatomic radical; one unpaired electron in the π* antibonding orbital; bond order 2.5; extremely reactive

### NOS enzyme structure

All NOS isoforms are **homodimers** with two functional domains per monomer:

| Domain | Cofactors | Function |
|:---|:---|:---|
| **Oxygenase domain (N-terminal)** | Haem (Fe³⁺/Fe²⁺), BH₄ (tetrahydrobiopterin), Zn²⁺ | Binds L-arginine and O₂; catalytic site |
| **Reductase domain (C-terminal)** | FAD, FMN, NADPH | Electron transfer from NADPH to oxygenase domain |
| **Calmodulin-binding linker** | Ca²⁺/CaM (eNOS, nNOS); CaM always bound (iNOS) | Controls electron flow from reductase to oxygenase |

NOS dimerization is obligatory for activity; BH₄ stabilizes the dimer interface and is the critical cofactor whose deficiency causes **eNOS uncoupling** (NOS produces O₂•⁻ instead of NO).

### NOS isoforms

| Isoform | Gene | Expression pattern | Ca²⁺ dependency | Key regulatory feature |
|:---|:---|:---|:---|:---|
| **eNOS** (NOS3) | *NOS3* | Endothelium (Golgi/caveolae); platelets | Yes (low threshold) | Myristoylated/palmitoylated to caveolae; Ser1177 phosphorylation by Akt → constitutive activation |
| **nNOS** (NOS1) | *NOS1* | Neurons, skeletal muscle, ENS, macula densa | Yes (high Ca²⁺ required) | PDZ domain anchors to PSD-95 at glutamate synapses |
| **iNOS** (NOS2) | *NOS2* | Macrophages, neutrophils, hepatocytes, SMC, epithelium | No (CaM permanently bound) | Induced de novo by LPS/IFN-γ/TNF-α via NF-κB; high-output NO production |

## Function

### 1. Vascular tone (eNOS)

eNOS is the **primary regulator of vascular tone** in the systemic and pulmonary circulations. It is activated by:
- **Shear stress** (blood flow → mechanosensors on endothelium → Ca²⁺ influx + PI3K/Akt → Ser1177 phosphorylation → eNOS activation)
- **Vasodilatory agonists:** acetylcholine (muscarinic M3 → Gq → PLC → IP3 → ER Ca²⁺ release), bradykinin (B2 → Gq), VEGF (VEGFR2 → PI3K → Akt → eNOS)
- **Insulin** (via IRS-1/PI3K/Akt → eNOS Ser1177 → NO → vasodilation in skeletal muscle — a physiological mechanism coupling glucose delivery to metabolic demand)

eNOS-derived NO diffuses to smooth muscle → sGC activation → cGMP → PKG → MLCP (myosin light chain phosphatase) → dephosphorylation of MLC → smooth muscle relaxation → **vasodilation**.

Additionally, NO in the vasculature:
- **Inhibits platelet aggregation** (↑cGMP in platelets → ↓GPIIb/IIIa activation)
- **Inhibits VSMC proliferation** (anti-proliferative via cGMP)
- **Inhibits monocyte/leukocyte adhesion** (↓VCAM-1, ICAM-1, E-selectin expression via NF-κB inhibition)
- **Prevents LDL oxidation** (antioxidant; when not scavenged by superoxide)

### 2. Neurotransmission (nNOS)

nNOS NO acts as an **unconventional retrograde synaptic messenger** [^alberts-mol-cell-biology]:
- **LTP (long-term potentiation):** NMDA receptor activation (postsynaptic) → Ca²⁺ influx → CaM → nNOS → NO → diffuses BACK to presynaptic terminal → guanylyl cyclase → cGMP → enhanced glutamate release (retrograde facilitation)
- **LTD (long-term depression):** Lower-level NO production from parallel fiber-Purkinje cell synapses in cerebellum contributes to cerebellar LTD
- **ENS motility:** nNOS (and NANC neurons) produces NO that relaxes intestinal smooth muscle → coordinates peristalsis and the rectoanal inhibitory reflex
- **Penile erection:** sacral parasympathetic (cavernous nerve) → nNOS and eNOS activation in corpus cavernosum smooth muscle → NO → ↑cGMP → smooth muscle relaxation → arterial inflow → erection; **PDE5** (phosphodiesterase type 5) degrades cGMP → flaccidity; PDE5 inhibitors (sildenafil, tadalafil) amplify NO/cGMP signaling

### 3. Innate immune defense (iNOS)

iNOS generates **sustained, high-output NO** (10–100× higher than eNOS/nNOS) for pathogen killing:
- NO reacts with O₂•⁻ (generated by NADPH oxidase) → **ONOO⁻** (peroxynitrite) — potent oxidant
- ONOO⁻ nitrosates tyrosines on bacterial proteins, oxidizes Fe-S clusters of respiratory chain enzymes, nitrates DNA bases → pathogen killing
- Kills *Mycobacterium tuberculosis*, *Leishmania*, *Candida*, and viruses
- Excess iNOS production contributes to septic shock pathophysiology (see Pathology)

## Mechanism

### sGC/cGMP pathway

The canonical NO effector pathway [^stryer-biochemistry]:

1. NO binds the **ferrous haem** of **sGC** (soluble guanylyl cyclase, α1β1 heterodimer; ~400-fold activation upon NO binding)
2. sGC converts GTP → cGMP
3. **PKG (protein kinase G; cGMP-dependent kinase)** is activated
4. PKG phosphorylates:
   - **MLCP (myosin light chain phosphatase)** → activated → dephosphorylates MLC-20 → smooth muscle relaxation
   - **BKCa channels** (large-conductance K⁺) → membrane hyperpolarisation → ↓Ca²⁺ influx → relaxation
   - **IP3R** (inositol triphosphate receptor) → ↓Ca²⁺ release from ER
   - **Phospholamban** (cardiac) → PLN phosphorylation → ↑SERCA2a activity → ↑lusitropy (diastolic relaxation)
5. **PDE5** degrades cGMP → limits duration of NO signaling (target of sildenafil, tadalafil, vardenafil)

### S-nitrosylation

A reversible **post-translational modification** [^alberts-mol-cell-biology]:
- NO reacts with protein –SH groups (cysteine thiols) via N₂O₃ intermediary → **S-nitrosocysteine (–SNO)**
- Can be transferred (transnitrosylation) between proteins
- Key S-nitrosylated proteins:
  - **Haemoglobin Cys93β** (Hb-SNO): NO carrier for hypoxic vasodilation
  - **Ryanodine receptor (RyR2):** hypernitrosylation in heart failure → leak channel → arrhythmia substrate
  - **Caspase-3/9:** S-nitrosylation inhibits apoptosis (cytoprotective at low NO)
  - **HDAC2:** S-nitrosylation activates HDAC2 → chromatin remodeling in airway
  - **Albumin-Cys34:** circulating SNO reservoir

### Peroxynitrite (ONOO⁻)

When NO encounters superoxide (O₂•⁻), produced by xanthine oxidase, NADPH oxidase, or uncoupled eNOS:
> **NO + O₂•⁻ → ONOO⁻** (k = 1.9 × 10¹⁰ M⁻¹s⁻¹; near diffusion-limited)

ONOO⁻ is a powerful oxidant/nitrosant:
- **Nitrotyrosine** formation on proteins (permanent modification; biomarker of oxidative/nitrosative stress)
- **8-nitroguanosine** in DNA → strand breaks
- **Lipid peroxidation**
- Inactivates MnSOD (antioxidant enzyme) → amplifies its own production (feed-forward)

In inflammatory disease, elevated ONOO⁻ contributes to atherosclerosis, neurodegeneration, and sepsis-related organ damage.

### eNOS uncoupling

Under conditions of **BH₄ deficiency** (oxidised to BH₂ by ONOO⁻, H₂O₂), eNOS becomes uncoupled:
- The haem iron can no longer transfer electrons to O₂ for NO synthesis
- Instead, O₂ accepts electrons directly → **O₂•⁻** is produced instead of NO
- O₂•⁻ + remaining NO → more ONOO⁻ → more BH₄ oxidation → vicious cycle
- Result: ↓vasodilation, ↑oxidative stress → hallmark of **endothelial dysfunction** in hypertension, diabetes, atherosclerosis
- Therapy: BH₄ supplementation (sapropterin), antioxidants (clinical evidence mixed), statins (↑eNOS expression, ↓BH₂/BH₄ ratio)

## Connections

- **Modulates** → [Cardiovascular System](../../07-system/cardiovascular-system/README.md): eNOS-derived NO is the primary endothelium-derived vasodilator — NO → sGC → ↑cGMP → PKG → MLCP → smooth muscle relaxation; also inhibits platelet aggregation and vascular smooth muscle proliferation [^furchgott-1980].
- **Modulates** → [Macrophage](../../04-cellular/macrophage/README.md): iNOS in M1 macrophages generates sustained high-level NO + ONOO⁻ for pathogen killing; excess iNOS in sepsis produces vasodilatory NO causing refractory hypotension [^stryer-biochemistry].
- **Modulates** → [Nervous System](../../07-system/nervous-system/README.md): nNOS NO is a retrograde synaptic messenger at glutamatergic synapses modulating LTP/LTD; NO in the ENS regulates GI motility; sacral parasympathetic nNOS drives penile erection [^alberts-mol-cell-biology].
- **Modulates** → [NF-kB](../nf-kb/README.md): iNOS transcription is induced by NF-κB downstream of LPS/IFN-γ/TNF-α; NO in turn S-nitrosylates IκBα and p65/RelA cysteines, providing negative feedback on NF-κB activity [^stryer-biochemistry].
- `connects-to` → **[Pulmonary Arterial Hypertension](../../07-system/pulmonary-arterial-hypertension/README.md)** — Impaired eNOS and NO bioavailability in PAH endothelium → cGMP vasodilation failure; PDE5 inhibitors (sildenafil, tadalafil) prevent cGMP degradation → sustained vasodilation + anti-proliferative; sGC stimulators (riociguat) amplify NO-sGC-cGMP independent of endogenous NO.

## Pathology

| Disease | NO mechanism | Clinical implication |
|:---|:---|:---|
| **Endothelial dysfunction** | BH₄ deficiency → eNOS uncoupling → ↓NO, ↑O₂•⁻ | Hypertension, atherosclerosis, impaired flow-mediated dilation; statin therapy restores eNOS coupling |
| **Septic shock** | Bacterial LPS/IFN-γ → iNOS induction in multiple cell types → excess NO → generalised vasodilation, ↓SVR → refractory hypotension | Vasopressors (norepinephrine); iNOS-selective inhibitors (L-NAME, 1400W) under investigation |
| **Erectile dysfunction** | ↓nNOS/eNOS activity in corpus cavernosum → ↓cGMP | PDE5 inhibitors (sildenafil, tadalafil) restore cGMP levels; oral, onset ~30–60 min |
| **Pulmonary hypertension** | ↓eNOS NO in pulmonary vasculature → ↑PVR | Inhaled NO (iNO) therapy — selective pulmonary vasodilation; PDE5 inhibitors; sGC stimulators (riociguat) |
| **Sickle cell disease** | Deoxyhaemoglobin scavenges NO → endothelial NO deficiency → vaso-occlusion, pulmonary hypertension | Hydroxyurea ↑HbF; L-arginine supplementation; PDE5 inhibitors in SCD-PH |
| **Heart failure** | RyR2 hypernitrosylation → Ca²⁺ leak → arrhythmia; nNOS suppression → ↑NOS1-free RyR2 | Arrhythmia management; NOS modulation under investigation |
| **Ischaemia-reperfusion injury** | eNOS NO is cardioprotective pre-ischaemia (preconditioning); excess NO at reperfusion + O₂•⁻ → ONOO⁻ → cell death | Sodium nitrite (pre-conditioning NO donor) under investigation; antioxidants |
| **Inflammatory bowel disease** | iNOS overexpression in intestinal epithelium + macrophages → ONOO⁻ tissue damage | iNOS-selective inhibitors; aminosalicylates reduce iNOS induction |

## See Also

- [NF-kB](../nf-kb/README.md) — transcriptional activator of iNOS; NO S-nitrosylates NF-κB p65 for feedback inhibition
- [TNF-alpha](../tnf-alpha/README.md) — induces iNOS expression via NF-κB; co-mediates endothelial dysfunction
- [IL-6](../il-6/README.md) — cytokine storm co-mediator; induces iNOS in hepatocytes during sepsis
- [ATP](../atp/README.md) — purinergic P2Y receptor activation by extracellular ATP stimulates eNOS via Gq/Ca²⁺
- [Cardiovascular system](../../07-system/cardiovascular-system/README.md) — eNOS-derived NO is the primary endothelial vasodilator; critical to blood pressure regulation
- [Macrophage](../../04-cellular/macrophage/README.md) — primary cell type expressing iNOS; M1 polarization drives high-output NO for pathogen killing
- [Neuron](../../04-cellular/neuron/README.md) — nNOS in glutamatergic neurons produces retrograde NO; nNOS activity modulates pain, memory (LTP), and neurodegeneration

[^stryer-biochemistry]: Berg JM, Tymoczko JL, Stryer L. *Biochemistry.* 9th ed. W.H. Freeman; 2019.
[^alberts-mol-cell-biology]: Alberts B, Johnson A, Lewis J, et al. *Molecular Biology of the Cell.* 7th ed. W.W. Norton; 2022.
[^furchgott-1980]: Furchgott RF, Zawadzki JV. The obligatory role of endothelial cells in the relaxation of arterial smooth muscle by acetylcholine. *Nature.* 1980;288:373–376. [doi:10.1038/288373a0](https://doi.org/10.1038/288373a0)
