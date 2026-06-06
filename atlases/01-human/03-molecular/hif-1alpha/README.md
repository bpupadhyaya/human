---
schema: human-scale-entry/v1
id: hif-1alpha
name: HIF-1alpha
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Oxygen-regulated transcription factor; stabilized when PHDs are inactivated by low O₂ → escapes pVHL-mediated degradation. Drives VEGF, EPO, and glycolytic gene expression; central to cancer metabolism (Warburg effect), angiogenesis, and ischemic adaptation."
aliases: ["HIF1A", "HIF-1α", "hypoxia-inducible factor 1 alpha", "HIF1"]
sources:
  - id: semenza-2001-hif
    type: peer-reviewed
    cite: "Semenza GL. HIF-1, O(2), and the 3 PHDs: how animal cells signal hypoxia to the nucleus. Cell. 2001;107(1):1-3."
    doi: "10.1016/S0092-8674(01)00518-9"
    pmid: "11595178"
    url: "https://doi.org/10.1016/S0092-8674(01)00518-9"
  - id: kaelin-2013-vhl-hif
    type: peer-reviewed
    cite: "Kaelin WG Jr, Ratcliffe PJ. Oxygen sensing by metazoans: the central role of the HIF hydroxylase pathway. Mol Cell. 2008;30(4):393-402."
    doi: "10.1016/j.molcel.2008.04.009"
    pmid: "18498744"
    url: "https://doi.org/10.1016/j.molcel.2008.04.009"
  - id: semenza-2012-hypoxia-cancer
    type: peer-reviewed
    cite: "Semenza GL. Hypoxia-inducible factors in physiology and medicine. Cell. 2012;148(3):399-408."
    doi: "10.1016/j.cell.2012.01.021"
    pmid: "22304911"
    url: "https://doi.org/10.1016/j.cell.2012.01.021"
cross_links:
  - target: 01-human/03-molecular/vegf
    relation: regulates
    note: "HIF-1α directly activates VEGF-A via the VEGF HRE; this HIF→VEGF axis is the dominant mechanism linking tumor hypoxia to angiogenesis; PHD inhibition or VHL loss constitutively activates VEGF production even in normoxia."
  - target: 01-human/03-molecular/erythropoietin
    relation: regulates
    note: "HIF-2α (shares VHL/PHD regulation) drives EPO synthesis in renal peritubular cells in response to anemia or hypoxia; PHD inhibitors (roxadustat, daprodustat) exploit this axis and are approved for CKD anemia."
  - target: 01-human/06-organ/lung
    relation: modulates
    note: "HIF-1α drives hypoxic pulmonary vasoconstriction via ET-1 induction; in ARDS, HIF-1α activation amplifies alveolar macrophage inflammatory responses and VEGF-driven edema; HIF-1α also promotes surfactant production in type II pneumocytes."
  - target: 01-human/07-system/cytokine-storm
    relation: modulates
    note: "HIF-1α promotes macrophage glycolysis and inflammatory gene expression (IL-1β, TNF-α); in COVID-19 and sepsis, hypoxia-driven HIF-1α activation in alveolar macrophages amplifies cytokine release; HIF-1α inhibition is a proposed therapeutic strategy to dampen hyperinflammation."
---

# HIF-1alpha

## Overview

**Hypoxia-inducible factor 1α (HIF-1α)** is the oxygen-regulated subunit of the **HIF-1 transcription factor complex** — the master regulator of the cellular and systemic response to oxygen deprivation (hypoxia). Discovered by Gregg Semenza and colleagues in the early 1990s while investigating hypoxic induction of the erythropoietin gene, HIF-1α coordinates the expression of hundreds of target genes that enable cells to adapt to reduced oxygen availability: shifting metabolism from oxidative phosphorylation to glycolysis, stimulating angiogenesis, increasing oxygen delivery (EPO → erythrocyte production), and promoting cell survival.

The discovery of HIF-1α's regulation by the **VHL (von Hippel-Lindau) tumor suppressor — oxygen-sensing prolyl hydroxylases (PHDs)** pathway earned Kaelin, Ratcliffe, and Semenza the **2019 Nobel Prize in Physiology or Medicine**.

HIF-1α's biology is central to understanding:
- **Cancer metabolism:** Most solid tumors upregulate HIF-1α via hypoxia, oncogene activation (Ras, Myc), or VHL mutation → Warburg effect, VEGF-driven angiogenesis, metabolic reprogramming, invasion
- **Ischemia/reperfusion:** Cardiac and cerebral ischemia activate HIF-1α → protective gene expression (VEGF, survivin, glycolytic enzymes)
- **Anemia management:** HIF-2α (closely related) drives EPO synthesis; HIF stabilizers (prolyl hydroxylase inhibitors) are now approved drugs for CKD anemia

## Structure

### HIF-1 complex: α/β dimerization

HIF-1 is a heterodimeric transcription factor:
- **HIF-1α (HIF1A gene, chromosome 14q23.2):** 826 amino acids; oxygen-regulated; constitutively synthesized but continuously degraded under normoxia
- **HIF-1β (ARNT, aryl hydrocarbon receptor nuclear translocator):** Constitutively expressed; the obligate dimerization partner; shared with aryl hydrocarbon receptor (AhR); not oxygen-regulated

Both subunits contain **bHLH-PAS domains** (basic helix-loop-helix, PER-ARNT-SIM): the bHLH domain binds DNA; PAS domains mediate protein-protein interactions (α/β dimerization, co-activator binding).

**HIF-1α functional domains:**
1. **N-TAD (N-terminal transactivation domain, aa 531-575):** Regulates target gene selection; contains Pro402 and Pro564 — the two prolyl residues hydroxylated by PHDs under normoxia
2. **ODD (oxygen-dependent degradation domain, aa 401-603):** Contains Pro402/Pro564 and Asn803; the VHL recognition and degradation signal
3. **C-TAD (C-terminal TAD, aa 786-826):** Recruits transcriptional co-activators (p300/CBP); asparagine residue Asn803 is hydroxylated by FIH-1 (factor inhibiting HIF) → blocks p300 binding; hydroxylation suppressed by hypoxia → C-TAD active under hypoxia

**HIF family:** Three paralogs in humans — HIF-1α, HIF-2α (EPAS1), HIF-3α (various inhibitory splice variants). HIF-1α and HIF-2α share the VHL/PHD regulation and bHLH-PAS structure but have distinct target gene profiles:
- HIF-1α: glycolytic genes (LDHA, PGK1, PFKL, HK2), VEGF, PHD3
- HIF-2α: EPO (in kidney/liver), OCT4, cyclin D1, TGF-α; dominant in tumor angiogenesis in some contexts

## Function

### The PHD-VHL oxygen sensor [^kaelin-2013-vhl-hif]

The HIF pathway is regulated by a family of **2-oxoglutarate-dependent prolyl hydroxylases (PHDs 1-3)**:

**Normoxia (O₂ present):**
1. PHD1/2/3 use O₂ + 2-oxoglutarate as co-substrates → hydroxylate Pro402 and Pro564 in HIF-1α ODD domain
2. pVHL (Von Hippel-Lindau protein) recognizes hydroxyproline in a sequence-specific manner → recruits Elongin B/C + Cullin2 + Rbx1 → E3 ubiquitin ligase complex
3. HIF-1α ubiquitinated → proteasomal degradation; half-life <5 minutes
4. FIH-1 (factor inhibiting HIF): hydroxylates Asn803 → blocks C-TAD interaction with p300/CBP → transcriptional repression even if some HIF-1α escapes degradation

**Hypoxia (O₂ reduced below ~2-5% pO₂):**
1. PHDs inactive (O₂ is obligate co-substrate; Km ~200 μM O₂, below pO₂ of most tissues)
2. HIF-1α accumulates rapidly (within minutes) due to halted degradation
3. FIH-1 also inhibited by low O₂ → C-TAD free to recruit p300/CBP
4. HIF-1α/HIF-1β dimerizes → binds **hypoxia response elements (HREs)** in target gene promoters: consensus 5'-RCGTG-3' (R=A/G) in forward or reverse strand, flanked by ACAG

### Target gene network [^semenza-2012-hypoxia-cancer]

HIF-1α transactivates hundreds of genes across multiple adaptive programs:

**Metabolic adaptation (Warburg shift):**
- **LDHA** (lactate dehydrogenase A): converts pyruvate to lactate → fermentative glycolysis even with O₂
- **PKM2** (pyruvate kinase M2): limits oxidative phosphorylation; also has non-canonical nuclear roles in HIF-1α co-activation
- **BNIP3, BNIP3L:** Mitophagy → clearance of dysfunctional mitochondria; reduce ROS production

**Oxygen delivery:**
- **EPO:** Kidney and liver EPO expression → erythropoiesis → increased O₂ carrying capacity (HIF-2α dominant in kidney)
- **Ceruloplasmin:** Iron metabolism → iron availability for hemoglobin synthesis

**Angiogenesis:**
- **VEGF-A, VEGF-C:** Drives tumor and wound vascularization
- **Angiopoietin-1, -2, PDGF-B:** Vessel maturation and remodeling

**Invasion/metastasis:**
- **MMP2, MT1-MMP:** Extracellular matrix degradation → invasion
- **CXCR4:** Chemokine receptor for metastatic homing (CXCL12-rich niches: lymph nodes, bone)
- **LOX (lysyl oxidase):** Crosslinks collagen → pre-metastatic niche formation; levels correlate with metastasis

**Cell survival:**
- **Survivin (BIRC5), BCL-2:** Anti-apoptotic; protect hypoxic cells during angiogenesis
- **NF-κB pathway genes:** HIF-1α and NF-κB have mutually reinforcing transcriptional cross-talk in inflammation

### HIF-1α and cancer

**Constitutive HIF-1α activation in cancer** arises through three mechanisms:
1. **Hypoxia:** Tumor core O₂ typically <0.5%; drives HIF-1α stabilization
2. **VHL mutation/deletion:** pVHL loss → HIF-1α cannot be degraded even in normoxia; hallmark of **clear cell renal cell carcinoma** (ccRCC, >80% have VHL loss) and von Hippel-Lindau disease (germline VHL → hemangioblastoma, ccRCC, pheochromocytoma)
3. **Oncogene activation:** Ras/MAPK → HIF-1α transcription ↑; PI3K/Akt/mTOR → HIF-1α translation ↑ via 4E-BP1/S6K; Myc → HIF-1α co-activates Myc targets

**Belzutifan (PT2977, MK-6482):** First-in-class HIF-2α inhibitor (FDA approved 2021); blocks HIF-2α/HIF-1β dimerization; approved for VHL disease-associated hemangioblastoma, ccRCC, and pancreatic neuroendocrine tumors; shows robust responses in VHL-mutant cancers.

## Mechanism

### PHD as O₂ sensor: the biochemical logic

PHDs represent an elegant evolutionary solution to oxygen sensing: their catalytic activity is **directly proportional to O₂ concentration** (Km ~200 μM vs. normal tissue pO₂ ~30–60 μM → PHDs are inherently partial in activity, creating a graded HIF-1α stability). In extreme hypoxia (<1% O₂) or anoxia, PHDs are essentially inactive → rapid HIF-1α accumulation.

PHD activity also requires:
- **Fe²⁺:** Hydroxylation mechanism; iron chelators (desferrioxamine) or iron deficiency stabilize HIF-1α
- **2-oxoglutarate (α-ketoglutarate):** TCA cycle intermediate; links HIF to metabolic status
- **Ascorbate (vitamin C):** Maintains Fe²⁺ for catalysis; vitamin C deficiency may modestly stabilize HIF-1α

**PHD inhibitors (HIF stabilizers):** Roxadustat (Akebia/AstraZeneca), daprodustat, vadadustat, molidustat — competitive inhibitors of PHD active site (mimic 2-oxoglutarate); approved in China, Japan, EU, UK for **CKD anemia** (stimulate EPO production without pVHL suppression); not yet FDA-approved due to cardiovascular safety concerns.

### Non-hypoxic HIF-1α stabilization

- **Succinate, fumarate accumulation** (SDH/FH mutations in hereditary paraganglioma/HLRCC): competitively inhibit PHDs → pseudohypoxic HIF-1α stabilization → "pseudohypoxic syndrome"
- **Nitric oxide:** At high concentrations, inhibits cytochrome c oxidase → reduced O₂ consumption → local O₂ increase paradoxically, but NO can also directly inhibit PHDs
- **Cobalt, nickel:** Replace Fe²⁺ in PHD active site → inactive enzymes → HIF stabilization (cobalt-induced polycythemia)
- **mTOR → 4E-BP1/S6K:** Increases HIF-1α protein synthesis rate → elevated steady-state HIF-1α even under normoxia; relevant in PI3K/PTEN-mutant cancers

## Connections

- `regulates` → **[VEGF](../vegf/README.md)** — HIF-1α directly activates VEGF-A via the VEGF HRE; this is the dominant mechanism linking tumor hypoxia to angiogenesis; anti-VEGF therapy (bevacizumab) indirectly targets HIF-driven vascularization.
- `regulates` → **[Erythropoietin](../erythropoietin/README.md)** — HIF-2α (sharing VHL/PHD regulation) drives EPO synthesis in renal peritubular cells; PHD inhibitors (roxadustat) exploit this axis to treat CKD anemia without recombinant EPO injections.
- `modulates` → **[Lung](../../06-organ/lung/README.md)** — HIF-1α drives hypoxic pulmonary adaptation, amplifies ARDS-associated inflammation via macrophage metabolic reprogramming, and regulates surfactant production and alveolar repair.
- `modulates` → **[Cytokine Storm](../../07-system/cytokine-storm/README.md)** — HIF-1α promotes macrophage glycolytic switch and IL-1β/TNF-α production; hypoxia-driven HIF-1α in alveolar macrophages amplifies cytokine storm in COVID-19 ARDS and sepsis.

[^semenza-2001-hif]: Semenza GL. HIF-1, O(2), and the 3 PHDs: how animal cells signal hypoxia to the nucleus. *Cell.* 2001;107(1):1-3. [doi:10.1016/S0092-8674(01)00518-9](https://doi.org/10.1016/S0092-8674(01)00518-9) · [PubMed 11595178](https://pubmed.ncbi.nlm.nih.gov/11595178/)
[^kaelin-2013-vhl-hif]: Kaelin WG Jr, Ratcliffe PJ. Oxygen sensing by metazoans: the central role of the HIF hydroxylase pathway. *Mol Cell.* 2008;30(4):393-402. [doi:10.1016/j.molcel.2008.04.009](https://doi.org/10.1016/j.molcel.2008.04.009) · [PubMed 18498744](https://pubmed.ncbi.nlm.nih.gov/18498744/)
[^semenza-2012-hypoxia-cancer]: Semenza GL. Hypoxia-inducible factors in physiology and medicine. *Cell.* 2012;148(3):399-408. [doi:10.1016/j.cell.2012.01.021](https://doi.org/10.1016/j.cell.2012.01.021) · [PubMed 22304911](https://pubmed.ncbi.nlm.nih.gov/22304911/)
