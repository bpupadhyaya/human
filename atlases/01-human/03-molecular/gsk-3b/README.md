---
schema: human-scale-entry/v1
id: gsk-3b
name: GSK-3β
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-08
summary: "GSK-3β (glycogen synthase kinase 3 beta), a constitutively active Ser/Thr kinase, phosphorylates glycogen synthase, tau, and β-catenin; inhibited by lithium (gold-standard mood stabilizer) and Wnt signaling; implicated in bipolar disorder, Alzheimer's tau pathology, and cancer."
aliases: ["glycogen synthase kinase 3 beta", "GSK3B", "GSK-3β", "tau kinase", "lithium target", "GSK3 inhibitor"]
sources:
  - id: woodgett-1990-gsk3-cloning
    type: peer-reviewed
    cite: "Woodgett JR. Molecular cloning and expression of glycogen synthase kinase-3/factor A. EMBO J. 1990;9(8):2431-2438."
    doi: "10.1002/j.1460-2075.1990.tb07420.x"
    pmid: "2164468"
    url: "https://doi.org/10.1002/j.1460-2075.1990.tb07420.x"
    accessed: "2026-06-08"
  - id: klein-1996-lithium-gsk3
    type: peer-reviewed
    cite: "Klein PS, Melton DA. A molecular mechanism for the effect of lithium on development. Proc Natl Acad Sci USA. 1996;93(16):8455-8459."
    doi: "10.1073/pnas.93.16.8455"
    pmid: "8710892"
    url: "https://doi.org/10.1073/pnas.93.16.8455"
    accessed: "2026-06-08"
  - id: beurel-2015-gsk3-review
    type: peer-reviewed
    cite: "Beurel E, Grieco SF, Jope RS. Glycogen synthase kinase-3 (GSK3): regulation, actions, and diseases. Pharmacol Ther. 2015;148:114-131."
    doi: "10.1016/j.pharmthera.2014.11.016"
    pmid: "25435019"
    url: "https://doi.org/10.1016/j.pharmthera.2014.11.016"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/07-system/bipolar-disorder
    relation: connects-to
    note: "Lithium inhibits GSK-3β directly (uncompetitive Mg²⁺ site) in bipolar disorder; GSK-3β hyperactivity drives circadian dysfunction and reduced BDNF; lithium → GSK-3β inhibition → β-catenin stabilization → neuroprotective gene expression and mood stabilization."
  - target: 01-human/03-molecular/mapt
    relation: connects-to
    note: "GSK-3β is the major tau (MAPT) kinase — phosphorylates >40 sites including Thr231, Ser396/404 (PHF-1 epitope); GSK-3β-driven tau hyperphosphorylation promotes neurofibrillary tangles in Alzheimer's; GSK-3β inhibitors reduce tau pathology in preclinical models."
  - target: 01-human/07-system/alzheimers-disease
    relation: connects-to
    note: "GSK-3β is overactive in Alzheimer's disease hippocampus; drives amyloid-β production (APP processing) and tau hyperphosphorylation; insulin resistance activates GSK-3β; tideglusib (GSK-3β inhibitor) showed target engagement but failed Phase 2 AD trial in 2013."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "In the Wnt OFF state, GSK-3β phosphorylates β-catenin (Ser33/37/Thr41) → β-TrCP ubiquitination → proteasomal degradation; Wnt ligand → Dishevelled → GSK-3β inactivation → β-catenin nuclear accumulation → TCF/LEF target gene transcription."
---

# GSK-3β

## Overview

**Glycogen synthase kinase-3 beta (GSK-3β)** is a constitutively active serine/threonine protein kinase that plays a central role at the intersection of metabolism, neurodevelopment, mood regulation, and cancer biology. It was first cloned by Woodgett in 1990 [^woodgett-1990-gsk3-cloning] from studies of glycogen metabolism — identified as the kinase responsible for phosphorylating and inactivating **glycogen synthase** (GS), thereby inhibiting glycogen synthesis in liver and muscle.

GSK-3β's importance expanded dramatically when it was identified as:
1. A **primary inhibitory kinase in the Wnt signaling pathway** — phosphorylating β-catenin to target it for degradation
2. The **principal tau kinase** — responsible for the hyperphosphorylation of microtubule-associated protein tau in Alzheimer's disease
3. The **direct molecular target of lithium** — the gold-standard mood stabilizer for bipolar disorder [^klein-1996-lithium-gsk3]

Unlike most kinases, GSK-3β is **constitutively active** in resting cells — it must be actively inhibited by upstream signals (Wnt, PI3K/Akt, insulin) rather than actively switched on. This inverted signaling logic makes it a broad negative regulator of growth, survival, and synaptic plasticity [^beurel-2015-gsk3-review].

The human genome encodes two GSK-3 paralogs: **GSK-3α** (gene: *GSK3A*, chromosome 19) and **GSK-3β** (gene: *GSK3B*, chromosome 3q13.3). They share 97% kinase domain identity but have distinct N-terminal domains and non-overlapping functions; GSK-3β is the dominant CNS and metabolic isoform.

## Structure

### Protein structure

GSK-3β is a 420-amino acid, 47 kDa monomeric kinase:
- **N-terminal domain** (~120 aa): regulatory region containing the inhibitory phosphorylation site **Ser9** (phosphorylated by Akt, PKA, PKC → inhibition) and a unique axin-binding motif
- **Kinase domain** (central): highly conserved bilobal kinase fold; substrate-binding groove requires a **primed** phosphoserine/threonine (pSer/pThr at position +4 C-terminal to the GSK-3β phosphorylation site) in most substrates
- **C-terminal lobe**: contains the activation loop with **Tyr216** — autophosphorylation of Tyr216 is constitutively active in neurons and is required for kinase activity
- **Glycine-rich loop** (P-loop): ATP-binding site; uncompetitive Mg²⁺ binding site (target of lithium)

**Substrate recognition — the priming mechanism:**
Most GSK-3β substrates require prior phosphorylation by a "priming kinase" at position +4 relative to the GSK-3β target site:
- Tau: primed by CDK5, CK1 at multiple sites → enables GSK-3β phosphorylation at PHF-1 (Ser396/404), AT8 (Ser202/Thr205), AT100 (Thr212/Ser214) epitopes
- Glycogen synthase: primed by CK2 → inactivated by GSK-3β at Ser641
- β-catenin: primed by CK1 at Ser45 → GSK-3β phosphorylates Ser33/37/Thr41 → β-TrCP binding → ubiquitination

**Regulation:**

| Signal | Mechanism | Effect on GSK-3β |
|:---|:---|:---|
| **PI3K/Akt** | Akt phosphorylates Ser9 | Inhibited (pseudo-substrate blocks active site) |
| **Wnt signaling** | Axin complex disruption by Dishevelled | Inhibited (sequestered from β-catenin) |
| **Insulin** | IR → IRS-1 → PI3K → Akt → Ser9 phosphorylation | Inhibited |
| **Lithium (Li⁺)** | Uncompetitive Mg²⁺ antagonism at ATP site; allosteric inhibition | Inhibited (IC₅₀ ~1–2 mM — matches therapeutic serum levels) |
| **Autophosphorylation** | Tyr216 autophosphorylation | Constitutively active |
| **FRAT/GBP** | GSK-3β-binding proteins that block axin association | Inhibited in specific contexts |

## Function

### Glycogen metabolism (original function)

GSK-3β phosphorylates **glycogen synthase (GS)** at Ser641, inhibiting it. When insulin signals through PI3K/Akt → Ser9 phosphorylation → GSK-3β inhibition → GS dephosphorylation → glycogen synthesis. GSK-3β thus mediates insulin's stimulatory effect on glycogen storage.

Insulin resistance: GSK-3β hyperactivity in type 2 diabetes contributes to impaired glycogen synthesis.

### Wnt/β-catenin pathway

GSK-3β is the effector kinase of the **destruction complex** (GSK-3β + CK1 + Axin + APC):
1. **Wnt OFF:** Destruction complex is assembled; GSK-3β sequentially phosphorylates β-catenin (Ser33/37/Thr41) after CK1 priming at Ser45 → β-TrCP E3 ubiquitin ligase → 26S proteasomal degradation
2. **Wnt ON:** Frizzled + LRP5/6 → Dishevelled → Axin displacement from complex → GSK-3β cannot access β-catenin → β-catenin accumulates → nuclear TCF/LEF-target transcription (c-Myc, cyclin D1, VEGF)

**Cancer implication:** Loss-of-function mutations in APC (colorectal cancer) or activating mutations in CTNNB1 (β-catenin) bypass GSK-3β-mediated destruction → constitutive Wnt/β-catenin signaling.

### Tau phosphorylation and neurodegeneration

GSK-3β is the **principal tau kinase** in the brain:
- Phosphorylates tau at >40 sites, including the AD-defining PHF-1 (Ser396/404), AT8 (Ser202/Thr205), and Thr231 epitopes
- Hyperphosphorylated tau dissociates from microtubules → microtubule instability → axonal transport failure → tau aggregation → paired helical filaments (PHFs) → neurofibrillary tangles (NFTs)
- In AD brain: GSK-3β immunostaining co-localizes with early NFTs; GSK-3β activity inversely correlates with cognitive performance
- Preclinical: GSK-3β overexpressing transgenic mice show tau hyperphosphorylation, NFT formation, spatial memory deficits, and neurodegeneration reversible by GSK-3β inhibition

**AKT-GSK-3β dysregulation in schizophrenia:** AKT1 expression and Ser9-phosphorylated (inactive) GSK-3β are reduced in postmortem schizophrenia brain and in antipsychotic-naive patients' peripheral blood mononuclear cells. Dopamine D2 receptor signaling through β-arrestin → PP2A → Akt dephosphorylation → GSK-3β hyperactivation. Antipsychotics normalize Akt-GSK-3β balance.

### Neuroprotection and apoptosis

GSK-3β promotes neuronal apoptosis via:
- Phosphorylation and inactivation of **CREB** (reducing BDNF expression)
- Phosphorylation of **MCL-1** (pro-survival Bcl-2 family) → ubiquitination → degradation
- Activation of **FOXO** transcription factors → pro-apoptotic gene expression (Bim, FasL)
- Mitochondrial dysfunction via cytochrome c release

GSK-3β inhibition (by lithium, TDZD-8, SB-216763, or other inhibitors) is neuroprotective in stroke, traumatic brain injury, and neurodegeneration models — explaining part of lithium's neuroprotective effect in bipolar disorder.

## Mechanism

### Lithium's inhibition of GSK-3β

The mechanism by which lithium inhibits GSK-3β was established by Klein and Melton in 1996 [^klein-1996-lithium-gsk3] using Xenopus development as a model:
- Li⁺ competes with Mg²⁺ at a binding site within the GSK-3β active site (uncompetitive inhibition with respect to substrate; competitive with Mg²⁺)
- Therapeutic lithium serum concentrations (0.6–1.2 mM) closely match the Ki for GSK-3β inhibition (~1–2 mM) — unusually precise alignment for a therapeutic mechanism
- Additionally, lithium inhibits **inositol monophosphatase (IMPase)** and **inositol polyphosphate 1-phosphatase (IPPase)** → depletes myo-inositol → reduces diacylglycerol/PKC signaling ("myo-inositol depletion hypothesis" — may work additively with GSK-3β inhibition)

**Downstream of lithium-mediated GSK-3β inhibition in neurons:**
- β-catenin stabilization → nuclear entry → BDNF, Bcl-2, cyclin D1 gene transcription
- CREB phosphorylation preserved → BDNF maintained → hippocampal neurogenesis
- Tau phosphorylation reduced → neuroprotection
- Wnt-dependent dendritic arborization and synaptic plasticity enhanced
- Circadian clock: GSK-3β phosphorylates CLOCK, BMAL1, REV-ERBα → period lengthening; lithium-mediated inhibition → period shortening and phase stabilization (bipolar disorder features circadian dysregulation)

### GSK-3β in insulin resistance

In type 2 diabetes and metabolic syndrome:
- Chronic hyperinsulinemia → compensatory IRS-1 serine phosphorylation → impaired PI3K activation → reduced Akt → GSK-3β remains active → impaired glycogen synthesis → further hyperglycemia
- GSK-3β hyperactivity also contributes to pancreatic β-cell apoptosis in prolonged hyperglycemia

## Connections

**→ [Bipolar Disorder](../../07-system/bipolar-disorder/)**: lithium directly inhibits GSK-3β (uncompetitive Mg²⁺ site), explaining its mood stabilization; GSK-3β hyperactivity in bipolar drives circadian dysregulation and BDNF suppression; lithium-induced β-catenin stabilization promotes neuroprotective gene expression and hippocampal neurogenesis.

**→ [MAPT](../mapt/)**: GSK-3β is the dominant tau kinase — phosphorylates PHF-1 (Ser396/404) and AT8 (Ser202/Thr205) epitopes after CDK5/CK1 priming; GSK-3β-driven tau hyperphosphorylation triggers microtubule dissociation, axonal transport failure, and neurofibrillary tangle formation.

**→ [Alzheimer's Disease](../../07-system/alzheimers-disease/)**: GSK-3β is overactive in AD hippocampus and drives both tau pathology and amyloid-β production; insulin resistance activates GSK-3β; GSK-3β inhibitors (tideglusib) reached Phase 2 trials for AD but did not demonstrate significant cognitive benefit.

**→ [Wnt/β-catenin](../wnt-beta-catenin/)**: GSK-3β is the effector kinase of the Wnt destruction complex — phosphorylating β-catenin for proteasomal degradation in the Wnt OFF state; Wnt activation inactivates GSK-3β, releasing β-catenin for nuclear TCF/LEF target gene transcription.

[^woodgett-1990-gsk3-cloning]: Woodgett JR. Molecular cloning and expression of glycogen synthase kinase-3/factor A. *EMBO J.* 1990;9(8):2431-2438. [doi:10.1002/j.1460-2075.1990.tb07420.x](https://doi.org/10.1002/j.1460-2075.1990.tb07420.x) · [PubMed 2164468](https://pubmed.ncbi.nlm.nih.gov/2164468/)
[^klein-1996-lithium-gsk3]: Klein PS, Melton DA. A molecular mechanism for the effect of lithium on development. *Proc Natl Acad Sci USA.* 1996;93(16):8455-8459. [doi:10.1073/pnas.93.16.8455](https://doi.org/10.1073/pnas.93.16.8455) · [PubMed 8710892](https://pubmed.ncbi.nlm.nih.gov/8710892/)
[^beurel-2015-gsk3-review]: Beurel E, Grieco SF, Jope RS. Glycogen synthase kinase-3 (GSK3): regulation, actions, and diseases. *Pharmacol Ther.* 2015;148:114-131. [doi:10.1016/j.pharmthera.2014.11.016](https://doi.org/10.1016/j.pharmthera.2014.11.016) · [PubMed 25435019](https://pubmed.ncbi.nlm.nih.gov/25435019/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
