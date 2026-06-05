---
schema: human-scale-entry/v1
id: insulin-receptor
name: Insulin Receptor
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-05
summary: "Receptor tyrosine kinase (RTK) mediating glucose homeostasis. Insulin binding → α₂β₂ conformational change → β-subunit autophosphorylation → IRS-1/2 → PI3K→Akt→GLUT4 translocation and FoxO1 suppression of gluconeogenesis. Dysfunctional in T2DM."
aliases: ["IR", "INSR", "insulin receptor tyrosine kinase", "CD220"]
taxonomy:
  gene_symbol: "INSR"
  uniprot: "P06213"
sources:
  - id: ullrich-1985-ir-cloning
    type: peer-reviewed
    cite: "Ullrich A, Bell JR, Chen EY, et al. Human insulin receptor and its relationship to the tyrosine kinase family of oncogenes. Nature. 1985;313(6005):756-61."
    doi: "10.1038/313756a0"
    pmid: "2983224"
  - id: saltiel-2001-insulin-signaling
    type: peer-reviewed
    cite: "Saltiel AR, Kahn CR. Insulin signalling and the regulation of glucose and lipid metabolism. Nature. 2001;414(6865):799-806."
    doi: "10.1038/414799a"
    pmid: "11742412"
  - id: taniguchi-2006-ir-diabetes
    type: peer-reviewed
    cite: "Taniguchi CM, Emanuelli B, Kahn CR. Critical nodes in signalling pathways: insights into insulin action. Nat Rev Mol Cell Biol. 2006;7(2):85-96."
    doi: "10.1038/nrm1837"
    pmid: "16493415"
  - id: boucher-2014-ir-t2dm
    type: peer-reviewed
    cite: "Boucher J, Kleinridders A, Kahn CR. Insulin receptor signaling in normal and insulin-resistant states. Cold Spring Harb Perspect Biol. 2014;6(1):a009191."
    doi: "10.1101/cshperspect.a009191"
    pmid: "24384568"
cross_links:
  - target: 01-human/03-molecular/insulin
    relation: target-of
    evidence: saltiel-2001-insulin-signaling
    note: "Insulin receptor is the primary target of insulin; binding Kd ~0.1 nM triggers β-subunit autophosphorylation at Tyr1158/Tyr1162/Tyr1163 in the activation loop."
  - target: 01-human/04-cellular/hepatocyte
    relation: modulates
    evidence: taniguchi-2006-ir-diabetes
    note: "IR signalling in hepatocytes suppresses gluconeogenesis via Akt→FoxO1 phosphorylation; insulin resistance impairs this, causing fasting hyperglycaemia in T2DM."
  - target: 01-human/03-molecular/insulin
    relation: modulates
    evidence: taniguchi-2006-ir-diabetes
    note: "The IR creates a regulatory circuit: insulin activates IR; activated IR initiates negative feedback via IRS-1 Ser phosphorylation by mTORC1 and PKC."
  - target: 03-medicine/02-traditional/berberine
    relation: modulated-by
    evidence: saltiel-2001-insulin-signaling
    note: "Berberine activates AMPK independently of insulin, sensitising downstream IR pathway components; also upregulates IR expression in hepatocytes."
  - target: 01-human/04-cellular/adipocyte
    relation: modulated-by
    note: "Modulated by Adipocyte."
---

# Insulin Receptor

## Overview

The insulin receptor (IR, gene *INSR*) is a **receptor tyrosine kinase (RTK)** and the principal transducer of insulin's metabolic signals in virtually every cell type of the human body. Its activation initiates a cascade that orchestrates the post-prandial metabolic state: glucose uptake into muscle and adipose tissue, suppression of hepatic gluconeogenesis, glycogen and lipid synthesis, and inhibition of lipolysis and ketogenesis. Dysfunction of the insulin receptor — either through reduced expression, impaired kinase activity, or downstream signaling defects — is the molecular substrate of **type 2 diabetes mellitus (T2DM)** and the insulin resistance that precedes it in metabolic syndrome.

The IR was cloned independently by Ullrich et al. and Ebina et al. in 1985 [^ullrich-1985-ir-cloning], revealing an unexpected structural feature: the receptor exists as a disulfide-linked **α₂β₂ heterotetrameric** preformed dimer on the cell surface — distinct from other RTKs (such as EGFR) that dimerize upon ligand binding. This preformed architecture means insulin activates a conformational change within an already-assembled complex, rather than triggering *de novo* receptor assembly. The insulin receptor kinase domain is one of the most extensively studied enzymatic systems in biochemistry, with crystal structures at atomic resolution illuminating the molecular basis of activation, substrate recognition, and pharmacological targeting [^saltiel-2001-insulin-signaling].

The receptor is expressed at particularly high density in the classical insulin-responsive tissues — liver (~300,000 receptors/hepatocyte), skeletal muscle, and adipose — but is also functionally important in the brain (hypothalamic appetite regulation, hippocampal neuroplasticity), heart, kidney, and endothelium.

## Structure

### α₂β₂ Heterotetrameric Architecture

The mature insulin receptor is an **α₂β₂ heterotetramer** derived from a single precursor protein (1,382 aa) that is post-translationally processed:

1. **Pre-proIR** (single polypeptide) is glycosylated in the ER
2. **Furin-mediated cleavage** at a tetrabasic site separates α and β subunits
3. Two α-β protomers are joined by **disulfide bonds** (α–α and α–β) into the mature α₂β₂ heterotetramer

**α-subunit (735 aa, ~135 kDa)**:
- Entirely extracellular
- Contains the **insulin-binding site** — primarily in the L1/CR domain and the fibronectin type III (FnIII-1,2,3) repeats
- Key insulin contact residues: Phe89, Asn90, Glu97 in L1; Phe705, Val715, Leu709 in α-CT helix

**β-subunit (620 aa, ~95 kDa)**:
- Short extracellular segment
- Single-pass **transmembrane domain** (23 aa hydrophobic helix)
- Intracellular **juxtamembrane** (JM) region containing regulatory sites (Thr1158/Ser1160 phosphorylation)
- **Tyrosine kinase domain (TKD)** with the bilobed kinase fold
- **C-terminal tail** with additional autophosphorylation sites (Tyr1316/Tyr1322)

### Insulin-Binding Site

Structural studies (cryo-EM, 2018–2022) have revealed that:
- Two insulin molecules can bind per receptor tetramer at **Site 1** (L1 + αCT helix) and **Site 2** (FnIII-2 region)
- **High-affinity binding** requires insulin to span both Site 1 (on one α-subunit) and Site 2 elements (on the other α-subunit) — a cross-linking mechanism
- Insulin binding at Site 1 has Kd ~0.1 nM; the high affinity arises from the bivalent spanning
- Negative cooperativity: binding of a second insulin molecule reduces affinity (classical curvilinear Scatchard plot)

### Tyrosine Kinase Domain

The **TKD** (residues 978–1283 in β-subunit) has:
- **N-lobe**: 5 β-strands + αC helix; binds ATP (in the Gly-rich loop P-loop: GXGXXG)
- **Activation loop** (A-loop): contains three key tyrosines — **Tyr1158, Tyr1162, Tyr1163** — that are the primary autophosphorylation targets; when unphosphorylated, the A-loop occludes the substrate-binding site (self-inhibition)
- **C-lobe**: largely α-helical; substrate recognition
- **DFG motif**: Asp1150-Phe1151-Gly1152; Asp coordinates Mg²⁺-ATP for catalysis

## Function

### Post-Prandial Metabolic Coordination

After a meal, rising portal and peripheral glucose concentrations stimulate pancreatic β-cell insulin secretion (first phase within 1–3 min, second phase sustained over 60–120 min). Circulating insulin binds hepatic and peripheral IR with rapid kinetics:

**Liver (hepatocyte IR actions):**
- **Gluconeogenesis suppression**: Akt phosphorylates FoxO1 at Ser256/Ser319 → FoxO1 nuclear exclusion → suppression of *PEPCK* and *G6Pase* transcription → hepatic glucose output falls within 15–30 min
- **Glycogen synthesis**: Akt phosphorylates GSK3β (Ser9) → GSK3β inhibition → glycogen synthase active → glycogen synthesis
- **Lipogenesis**: Insulin activates SREBP-1c → *FASN*, *ACC*, *SCD1* transcription → de novo lipogenesis
- **VLDL secretion**: Insulin initially suppresses hepatic VLDL secretion

**Skeletal muscle (major glucose disposal, ~80% post-prandial):**
- **GLUT4 translocation**: Akt → AS160 (TBC1D4) phosphorylation → Rab10 activation → GLUT4 storage vesicle (GSV) fusion with plasma membrane → 10–20× increase in surface GLUT4 → facilitated glucose diffusion
- **Glycogen synthesis**: Akt → GSK3β inhibition → glycogen synthase → muscle glycogen
- **Protein synthesis**: IR → IRS-1 → PI3K → Akt → mTORC1 → S6K1 → ribosomal protein synthesis (anabolic)

**Adipose tissue:**
- **GLUT4 translocation** (as in muscle)
- **Anti-lipolytic**: Akt → PDE3B activation → decreased cAMP → PKA inhibition → HSL (hormone-sensitive lipase) inactive → suppressed lipolysis and FFA release
- **Lipogenesis**: Akt → SREBP-1c-independent lipogenesis; lipoprotein lipase (LPL) upregulation → triglyceride uptake from VLDL/chylomicrons

## Mechanism

### Activation: Conformational Change to Kinase Activation

**Step 1 — Insulin binding and conformational change:**
Insulin binding to the α-subunit extracellular domain induces a large-scale conformational change in the α₂β₂ tetramer — estimated ~20 Å movement of α-CT helices — that is transmitted through the transmembrane helices to the intracellular β-subunit juxtamembrane regions, relieving the basal inhibitory conformation of the TKD.

**Step 2 — Trans-autophosphorylation of A-loop tyrosines:**
The two β-subunit kinase domains phosphorylate each other (in *trans*) at **Tyr1158, Tyr1162, and Tyr1163** in the activation loop. This removes the A-loop's self-inhibitory occlusion of the substrate-binding cleft, increasing catalytic activity ~50–100-fold (Vmax increase; Km for peptide substrates decreases).

**Step 3 — Autophosphorylation of juxtamembrane and C-terminal sites:**
- **Tyr972** (juxtamembrane) — creates a Shc docking site; links IR to MAPK/ERK pathway
- **Tyr1316, Tyr1322** (C-terminal) — regulatory; affect internalization kinetics

**Step 4 — IRS-1/IRS-2 phosphorylation:**
Activated IR tyrosine kinase phosphorylates cytoplasmic scaffolding proteins **IRS-1** (insulin receptor substrate 1) and **IRS-2** at multiple Tyr residues (most importantly the YMXM motifs). Phospho-IRS-1/2 become docking platforms for signaling enzymes:

| Binding partner | SH2 domain | Downstream pathway |
|:---|:---|:---|
| **PI3K (p85 regulatory subunit)** | SH2 × 2 | PI3K → PIP2→PIP3 → PDK1 → **Akt** (PKB) |
| **Grb2** | SH2 | Grb2-Sos → Ras → Raf → MEK → **ERK** |
| **Shc** | PTB | Grb2-Sos → Ras → **ERK** (mitogenic) |
| **SHP2** | SH2 | Ras → ERK; also dephosphorylates IRS-1 (negative feedback) |

**Step 5 — PI3K/PIP3/Akt cascade:**
PI3K catalyzes PIP₂ → PIP₃ at the inner plasma membrane leaflet. PIP₃ recruits:
- **PDK1** (3-phosphoinositide-dependent protein kinase 1) → phosphorylates **Akt** at Thr308
- **mTORC2** → phosphorylates Akt at Ser473 (full activation)

Fully activated Akt (pThr308/pSer473) phosphorylates >100 substrates:
- **FoxO1/FoxO3a** (nuclear exclusion → anti-gluconeogenic)
- **GSK3α/β** (inhibition → glycogen synthesis)
- **AS160/TBC1D4** (GLUT4 translocation)
- **TSC2** (mTORC1 activation → protein synthesis, cell growth)
- **PDE3B** (anti-lipolysis in adipocytes)

### Negative Feedback and Insulin Resistance

The IR signaling pathway is subject to multiple negative feedback mechanisms that attenuate the response and, when chronically activated, produce insulin resistance:

1. **IRS-1 serine phosphorylation**: Akt → mTORC1 → **S6K1** → IRS-1 Ser302/Ser307/Ser612 phosphorylation → IRS-1 dissociation from IR, reduced Tyr phosphorylation → diminished PI3K recruitment (major mechanism of obesity-induced insulin resistance)
2. **PKC-θ/ε** (activated by DAG from diacylglycerol, elevated by lipid accumulation in muscle/liver) → IRS-1 Ser phosphorylation → insulin resistance
3. **PTEN** phosphatase — dephosphorylates PIP₃ → PIP₂ → terminates Akt signaling
4. **SHIP2** — 5′-phosphatase; degrades PIP₃
5. **PTP1B** (PTPN1) — protein tyrosine phosphatase 1B; dephosphorylates activated IR β-subunit and IRS-1 Tyr residues; major therapeutic target for T2DM (PTP1B inhibitors in development)
6. **Receptor internalization**: Ligand-bound IR is internalized via clathrin-mediated endocytosis within 5–15 min; recycled to surface or degraded

## Connections

- `target-of` → **[insulin](../insulin/README.md)** — IR is the primary target of insulin; Kd ~0.1 nM triggers β-subunit autophosphorylation
- `modulates` → **[hepatocyte](../../04-cellular/hepatocyte/README.md)** — IR signaling suppresses gluconeogenesis via Akt→FoxO1; impaired in T2DM → fasting hyperglycemia
- `modulates` → **[insulin](../insulin/README.md)** — IR creates negative feedback via IRS-1 Ser phosphorylation by mTORC1 and PKC, attenuating insulin signaling
- `modulated-by` → **[berberine](../../../03-medicine/02-traditional/berberine/README.md)** — berberine activates AMPK, sensitising IR pathway components; upregulates IR expression in hepatocytes

## Pathology

| Condition | IR mechanism | Clinical features |
|:---|:---|:---|
| **Type 2 diabetes mellitus (T2DM)** | IRS-1 Ser phosphorylation (via mTORC1/S6K1 and PKC-θ/ε from lipid accumulation) → hepatic and peripheral insulin resistance → impaired GLUT4 translocation, failed FoxO1 suppression | Fasting hyperglycemia, postprandial hyperglycemia, dyslipidemia; treated with metformin (AMPK), sulfonylureas, GLP-1 RAs, SGLT2i, insulin |
| **Metabolic syndrome** | Visceral adiposity → elevated free fatty acids → DAG → PKC-ε → hepatic IRS-2 Ser phosphorylation → hepatic insulin resistance with preserved lipogenic insulin sensitivity (paradox) | Hypertriglyceridemia, low HDL, hypertension, central obesity, impaired fasting glucose |
| **Type A insulin resistance syndrome** | NR3C1/INSR mutations (loss-of-function) or INSR post-receptor signaling defects; severe insulin resistance without obesity | Acanthosis nigricans, hyperandrogenism (women), extreme hyperinsulinemia; classified by Moller/Flier |
| **Leprechaunism (Donohue syndrome)** | Biallelic INSR loss-of-function mutations | Intrauterine growth restriction, dysmorphic features, extreme insulin resistance; fatal in infancy |
| **Rabson-Mendenhall syndrome** | Severe biallelic INSR mutations | Dental and nail abnormalities, pineal hyperplasia, extreme insulin resistance; survives longer than leprechaunism |
| **Polycystic ovary syndrome (PCOS)** | Hepatic insulin resistance + hyperinsulinemia → ovarian androgen excess; unique serine phosphorylation defect in PCOS granulosa cells | Menstrual irregularity, hyperandrogenism, infertility, metabolic risk; metformin/inositol therapy |
| **Insulin receptor antibodies (Type B IR resistance)** | Autoantibodies against IR extracellular domain | Severe insulin resistance + acanthosis nigricans; SLE-associated; can paradoxically cause hypoglycemia at low antibody titers |
| **Hyperinsulinemia / mTORC1 feedback** | Chronic insulin excess → S6K1 → IRS-1 Ser phosphorylation → acquired peripheral insulin resistance | Relevant in obesity and iatrogenic insulin excess; foundation of "carbohydrate-insulin model" of obesity |

[^ullrich-1985-ir-cloning]: Ullrich A, Bell JR, Chen EY, et al. Human insulin receptor and its relationship to the tyrosine kinase family of oncogenes. *Nature.* 1985;313(6005):756-61. [doi:10.1038/313756a0](https://doi.org/10.1038/313756a0)
[^saltiel-2001-insulin-signaling]: Saltiel AR, Kahn CR. Insulin signalling and the regulation of glucose and lipid metabolism. *Nature.* 2001;414(6865):799-806. [doi:10.1038/414799a](https://doi.org/10.1038/414799a)
[^taniguchi-2006-ir-diabetes]: Taniguchi CM, Emanuelli B, Kahn CR. Critical nodes in signalling pathways: insights into insulin action. *Nat Rev Mol Cell Biol.* 2006;7(2):85-96. [doi:10.1038/nrm1837](https://doi.org/10.1038/nrm1837)
[^boucher-2014-ir-t2dm]: Boucher J, Kleinridders A, Kahn CR. Insulin receptor signaling in normal and insulin-resistant states. *Cold Spring Harb Perspect Biol.* 2014;6(1):a009191. [doi:10.1101/cshperspect.a009191](https://doi.org/10.1101/cshperspect.a009191)
