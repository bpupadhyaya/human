---
schema: human-scale-entry/v1
id: egln1
name: EGLN1
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "EGLN1 (PHD2) is the principal prolyl hydroxylase that marks HIF-1α/2α for VHL-mediated ubiquitination under normoxia; EGLN1 uses O₂ as cosubstrate — inactivated by hypoxia → HIF stabilized; PHD inhibitors (daprodustat, vadadustat) block EGLN1 to treat CKD anemia."
aliases: ["EGLN1", "PHD2", "prolyl hydroxylase 2", "HIF prolyl hydroxylase", "HIFPH2", "PHD inhibitor EGLN1", "daprodustat target", "oxygen sensor EGLN1", "EGLN1 HIF VHL"]
sources:
  - id: epstein-2001-egln-family
    type: peer-reviewed
    cite: "Epstein AC, Gleadle JM, McNeill LA, et al. C. elegans EGL-9 and mammalian homologs define a family of dioxygenases that regulate HIF by prolyl hydroxylation. Cell. 2001;107(1):43-54."
    doi: "10.1016/S0092-8674(01)00507-4"
    pmid: "11595184"
    url: "https://doi.org/10.1016/S0092-8674(01)00507-4"
  - id: kaelin-2008-hif-hydroxylase
    type: peer-reviewed
    cite: "Kaelin WG Jr, Ratcliffe PJ. Oxygen sensing by metazoans: the central role of the HIF hydroxylase pathway. Mol Cell. 2008;30(4):393-402."
    doi: "10.1016/j.molcel.2008.04.009"
    pmid: "18498744"
    url: "https://doi.org/10.1016/j.molcel.2008.04.009"
cross_links:
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "EGLN1 (PHD2) hydroxylates HIF-1α Pro402 and Pro564 using O₂ and 2-oxoglutarate as cofactors; hydroxylated HIF-1α is recognized by VHL → ubiquitination → proteasomal degradation; at low O₂ EGLN1 is inactive → HIF-1α accumulates → HIF target gene program (VEGF, EPO, GLUT1)."
  - target: 01-human/03-molecular/vhl
    relation: connects-to
    note: "VHL (pVHL) recognizes EGLN1-hydroxylated HIF-1α/2α at hydroxyproline residues via the VHL β-domain; VHL-ELOC-ELOB-CUL2 E3 complex ubiquitinates HIF → degradation; VHL LOF (germline in VHL disease) → HIF accumulates constitutively independent of EGLN1 status."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "PHD inhibitors (daprodustat, vadadustat, roxadustat) reversibly inhibit EGLN1/2/3 → HIF-1α/2α stabilization → EPO transcription upregulated → erythropoiesis stimulated; FDA-approved for anemia of CKD; mimic the endogenous hypoxic response to erythropoetin deficiency."
  - target: 01-human/07-system/vhl-disease
    relation: connects-to
    note: "VHL disease results from germline VHL LOF → constitutive HIF-1α/2α stabilization (mimicking EGLN1 inactivation); belzutifan (HIF-2α inhibitor) is FDA-approved for VHL disease-related RCC, CNS hemangioblastoma, and pNET — targeting the downstream effector of VHL/EGLN1 loss."
  - target: 01-human/03-molecular/epas1
    relation: connects-to
    note: "EGLN1 (PHD2) hydroxylates HIF-2α (EPAS1) at Pro405/Pro531 → VHL recognition → degradation; HIF-2α is the principal renal EPO driver and dominant oncogene in VHL-mutant RCC; Tibetan EGLN1 D4E/C127S variant boosts HIF-2α degradation → blunted EPO response at altitude."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "PHD inhibitors (daprodustat, vadadustat) targeting EGLN1/2/3 are FDA-approved for CKD anemia; CKD accumulates succinate and uremic toxins that impair EGLN1 → partial HIF activation; PHIs restore HIF-2α/EPO axis → erythropoiesis without supraphysiological ESA dosing."
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "VHL biallelic inactivation in ~90% of ccRCC mimics permanent EGLN1 inactivation → HIF-1α/2α constitutively stable; SDH/FH mutations accumulate succinate/fumarate → competitive EGLN1 inhibition → HIF activation in hereditary RCC syndromes (SDH-deficient RCC, HLRCC)."
---

# EGLN1

## Overview

**EGLN1** (Egl-9 Family Hypoxia Inducible Factor 1; also **PHD2** — Prolyl Hydroxylase Domain-containing protein 2; or HIFPH2) is a 426 amino acid (46 kDa) **Fe²⁺/2-oxoglutarate-dependent dioxygenase** that functions as the **principal oxygen sensor** in the HIF (Hypoxia-Inducible Factor) pathway. EGLN1 catalyzes the hydroxylation of conserved proline residues in HIF-1α and HIF-2α — the rate-limiting step that targets HIF-α subunits for recognition by the **VHL (von Hippel-Lindau)** E3 ubiquitin ligase, leading to proteasomal degradation under normoxic conditions. Because EGLN1 requires molecular O₂ as a cosubstrate, it functions as a direct molecular oxygen sensor: at low O₂ (hypoxia), EGLN1 activity falls → HIF-α accumulates → transcription of hundreds of adaptive target genes (VEGF, EPO, GLUT1, LDHA, BNIP3). EGLN family members (EGLN1/PHD2, EGLN2/PHD1, EGLN3/PHD3) were identified in *C. elegans* as homologs of EGL-9 by Epstein et al. in 2001 [^epstein-2001-egln-family] [^kaelin-2008-hif-hydroxylase].

**Oxygen-sensing axis — normoxia vs. hypoxia:**

```
NORMOXIA (O₂ available):          HYPOXIA (O₂ low):
EGLN1 active                       EGLN1 inactive (no O₂ substrate)
  ↓ (uses O₂ + 2-OG)                ↓
Hydroxylates HIF-1α                 HIF-1α NOT hydroxylated
Pro402-OH and Pro564-OH              ↓
  ↓                                  HIF-1α accumulates
VHL β-domain recognizes             ↓
  hydroxyproline                     HIF-1α + HIF-1β → nuclear
  ↓                                  ↓
VHL-ELOC-ELOB-CUL2-RBX1 E3         HIF target genes activated:
  ubiquitinates HIF-1α               VEGF, EPO, LDHA, GLUT1,
  ↓                                  BNIP3, PDK1, CAIX
Proteasomal degradation
HIF-1α ~5-10 min half-life
```

## Structure

### EGLN1 protein domains

**N-terminal domain (aa 1-~100):**
- Contains a **MYND-type zinc finger** (Myeloid, Nervy, and DEAF-1 zinc finger; also called SPELL domain in EGLN family) that mediates protein-protein interactions; EGLN1 N-terminal domain binds FKBP38 (a peptidyl-prolyl isomerase that may modulate EGLN1 activity) and OS-9 (osteosarcoma amplified 9, an ER lectin that facilitates HIF delivery to EGLN1)
- Less well-characterized than the catalytic domain; may contribute to substrate specificity

**Catalytic (hydroxylase) domain — prolyl hydroxylase domain (PHD; aa ~100-426):**
- Encodes the double-stranded β-helix (DSBH / cupin) fold — the defining architecture of the Fe²⁺/2-oxoglutarate-dependent dioxygenase superfamily (also found in collagen prolyl hydroxylases, factor inhibiting HIF/FIH, TET enzymes, AlkB DNA repair enzymes)
- **Active site architecture:**
  - **Fe²⁺ coordination**: His313, His374, Asp315 (conserved HXD...H triad) chelate Fe²⁺; Fe²⁺ also coordinates O₂ and 2-oxoglutarate
  - **2-oxoglutarate (α-ketoglutarate) binding**: Arg383 contacts the C1-carboxylate of 2-OG; Tyr310 contacts C5-carboxylate
  - **HIF-1α substrate binding**: a flexible loop (βIV-βV loop; "finger loop") closes over the HIF LXXLAP motif containing the target proline; Tyr303 stacks against the proline ring
- **Reaction mechanism**: Fe²⁺-O₂ activated → decarboxylation of 2-OG → succinate + CO₂ + Fe⁴⁺=O ferryl intermediate → insertion of O into C-H bond of HIF proline → hydroxyproline formed; Fe²⁺ regenerated by ascorbate
- **Km(O₂)**: ~230-250 μM (approximately atmospheric air O₂ concentration); this high Km makes EGLN1 a genuine O₂ sensor — even mild hypoxia (10-20% reduction) reduces EGLN1 activity measurably

**EGLN family comparison:**
| Enzyme | Gene | Expression | HIF-1α site | Relative importance |
|---|---|---|---|---|
| PHD1 | EGLN2 | Restricted (muscle, liver) | Pro564 | Less important than PHD2 |
| PHD2 | EGLN1 | Ubiquitous | Pro402 + Pro564 | Principal HIF-α hydroxylase in normoxia |
| PHD3 | EGLN3 | Inducible by HIF | Pro564 only | Feedback regulator; induced by hypoxia |

**FIH (Factor Inhibiting HIF; HIF-1α Asn803 hydroxylase):**
- A separate 2-OG dioxygenase (HIFAN gene); hydroxylates HIF-1α Asn803 in the C-TAD (C-terminal transactivation domain) → blocks p300/CBP binding → prevents full HIF transcriptional activation even when HIF-1α protein is stable (not degraded)
- FIH has a lower Km(O₂) than EGLN1 — remains active at lower O₂ than EGLN1; creates a two-threshold hypoxic response: moderate hypoxia → EGLN1 inactivated (HIF-1α protein accumulates) but FIH still active (HIF-1α transcriptional activity blunted); severe hypoxia → both inactivated (full HIF-1α transcriptional program)

## Function

### EGLN1 in physiological oxygen sensing

**Altitude adaptation — Tibetan EGLN1 variants:**
Tibetan populations adapted to high altitude (~3,500-5,000 m) carry several naturally selected genetic variants that blunt erythropoietic responses to hypoxia (unlike Andean high-altitude populations, who have elevated hemoglobin via HIF-2α/EPO axis):
- **EGLN1** (PHD2) variants in Tibetans: c.12G>A (p.Asp4Glu, D4E) and c.380G>A (p.Cys127Ser, C127S) — haplotype strongly selected (p-value <10⁻⁷⁶)
- Functional effect: the D4E/C127S EGLN1 variant has INCREASED activity against HIF → more HIF-1α/2α degradation even under moderate hypoxia → blunted EPO response → lower hemoglobin → avoidance of high-altitude polycythemia (and associated thrombosis/stroke risks)
- The EPAS1 (HIF-2α) gene in Tibetans also carries loss-of-function variants that reduce HIF-2α-driven EPO upregulation; EGLN1 and EPAS1 variants work together as a complementary axis
- Andean populations: lack Tibetan EGLN1 variants; instead carry EPAS1 variants with different mechanisms; Andean populations have significantly higher hemoglobin at altitude than Tibetans

**EGLN1 in tissues:**
- Kidney tubular cells: HIF-2α/EPO axis under EGLN1 control → renal anemia in CKD reflects EGLN1 over-activity (too much HIF degradation despite reduced O₂ delivery in uremic kidney)
- Pulmonary vasculature: EGLN1 heterozygous mice develop pulmonary arterial hypertension (PAH) → EGLN1 inactivation → HIF-1α → PDGF-B, ET-1 → vascular smooth muscle proliferation; EGLN1 somatic variants identified in rare cases of human familial PAH
- Carotid body O₂ sensing: glomus cells use EGLN3 primarily; EGLN1 plays a role in long-term adaptation

### EGLN1 as a pharmacological target

**PHD inhibitors (HIF Prolyl Hydroxylase Inhibitors, PHIs) for CKD anemia:**

All three approved PHIs compete with 2-oxoglutarate for the Fe²⁺ active site → competitive inhibition → HIF-1α/2α stabilization → EPO upregulation → reticulocyte production → hemoglobin increase:

| Agent | Brand | Approval | Indication |
|---|---|---|---|
| Roxadustat | Evrenzo | EMA 2021; not FDA | NDD-CKD and DD-CKD anemia (outside US) |
| Daprodustat | Jesduvroq | FDA 2023 (dialysis-CKD) | DD-CKD anemia (US) |
| Vadadustat | Vafseo | FDA 2023 (non-dialysis) | NDD-CKD anemia (US) |

PHI advantages over ESAs (erythropoiesis-stimulating agents like epoetin alfa, darbepoetin):
- Oral administration
- Stabilize endogenous EPO (physiological levels) + improve iron mobilization (downregulate hepcidin via HIF-1α → increased ferroportin/TMPRSS6) → better iron utilization
- Efficacy in hyporesponsive patients (ESA-resistant CKD anemia)

PHI concerns:
- Cardiovascular safety: roxadustat showed non-inferiority in dialysis patients but signals in non-dialysis CKD; daprodustat and vadadustat showed non-inferior CV safety in their trials (ASCEND-D, ZENITH-CKD)
- HIF off-target activation: HIF upregulates many genes beyond EPO (VEGF → angiogenesis; PDGF; erythropoietin receptor; SDF-1/CXCL12) → theoretical cancer risk with long-term use; post-marketing surveillance ongoing
- Teratogenicity: PHIs contraindicated in pregnancy

## Mechanism

### EGLN1 in cancer biology

**Somatic EGLN1 mutations in cancer (rare):**
- EGLN1 LOF somatic mutations are rarely detected as cancer drivers; loss of EGLN1 → HIF-1α constitutive accumulation → can drive tumorigenesis in O₂-rich tissues; but EGLN1 is generally not a high-frequency somatic driver
- EGLN1 somatic amplification/overexpression: described in some tumors → enhanced HIF degradation → perhaps anti-tumor in some contexts
- **Notable: EGLN1 germline gain-of-function mutations**: rare families with familial erythrocytosis type 3 (ECYT3) carry activating EGLN1 variants → enhanced HIF-1α hydroxylation → reduced EPO → EPO-independent polycythemia (paradoxically, some EGLN1 GOF → erythrocytosis by poorly understood mechanisms)

**Succinate accumulation inhibits EGLN1 (SDH tumors):**
- EGLN1 reaction releases succinate as a byproduct (succinate = co-product of 2-OG decarboxylation)
- In SDH-deficient tumors (SDHB/SDHC/SDHD mutations — paraganglioma/pheochromocytoma): succinate accumulates dramatically → product inhibition of EGLN1 → HIF-1α/2α stabilization despite normal O₂ → "pseudohypoxia" → VEGF/HIF target programs → tumor growth
- Same mechanism: fumarate (FH-deficient tumors, HLRCC) also inhibits EGLN1 via competitive inhibition at the 2-OG binding site → pseudohypoxia in hereditary leiomyomatosis and RCC (HLRCC)
- IDH1/2-mutant tumors: 2-HG (2-hydroxyglutarate), a product of mutant IDH, also competitively inhibits 2-OG-dependent dioxygenases (EGLN1, TET2, KDM histone demethylases) → HIF effects in IDH-mutant glioma

## Connections

- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — EGLN1 (PHD2) hydroxylates HIF-1α Pro402 and Pro564 using O₂ and 2-oxoglutarate as cofactors; hydroxylated HIF-1α is recognized by VHL → ubiquitination → proteasomal degradation; at low O₂ EGLN1 is inactive → HIF-1α accumulates → HIF target gene program (VEGF, EPO, GLUT1).
- `connects-to` → **[VHL](../../03-molecular/vhl/README.md)** — VHL (pVHL) recognizes EGLN1-hydroxylated HIF-1α/2α at hydroxyproline residues via the VHL β-domain; VHL-ELOC-ELOB-CUL2 E3 complex ubiquitinates HIF → degradation; VHL LOF (germline in VHL disease) → HIF accumulates constitutively independent of EGLN1 status.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — PHD inhibitors (daprodustat, vadadustat, roxadustat) reversibly inhibit EGLN1/2/3 → HIF-1α/2α stabilization → EPO transcription upregulated → erythropoiesis stimulated; FDA-approved for anemia of CKD; mimic the endogenous hypoxic response to erythropoetin deficiency.
- `connects-to` → **[VHL Disease](../../07-system/vhl-disease/README.md)** — VHL disease results from germline VHL LOF → constitutive HIF-1α/2α stabilization (mimicking EGLN1 inactivation); belzutifan (HIF-2α inhibitor) is FDA-approved for VHL disease-related RCC, CNS hemangioblastoma, and pNET — targeting the downstream effector of VHL/EGLN1 loss.
- `connects-to` → **[EPAS1](../../03-molecular/epas1/README.md)** — EGLN1 (PHD2) hydroxylates HIF-2α (EPAS1) at Pro405/Pro531 → VHL recognition → degradation; HIF-2α is the principal renal EPO driver and dominant oncogene in VHL-mutant RCC; Tibetan EGLN1 D4E/C127S variant boosts HIF-2α degradation → blunted EPO response at altitude.
- `connects-to` → **[CKD](../../07-system/ckd/README.md)** — PHD inhibitors (daprodustat, vadadustat) targeting EGLN1/2/3 are FDA-approved for CKD anemia; CKD accumulates succinate and uremic toxins that impair EGLN1 → partial HIF activation; PHIs restore HIF-2α/EPO axis → erythropoiesis without supraphysiological ESA dosing.
- `connects-to` → **[Renal Cell Carcinoma](../../07-system/renal-cell-carcinoma/README.md)** — VHL biallelic inactivation in ~90% of ccRCC mimics permanent EGLN1 inactivation → HIF-1α/2α constitutively stable; SDH/FH mutations accumulate succinate/fumarate → competitive EGLN1 inhibition → HIF activation in hereditary RCC syndromes (SDH-deficient RCC, HLRCC).

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^epstein-2001-egln-family]: Epstein AC, Gleadle JM, McNeill LA, et al. C. elegans EGL-9 and mammalian homologs define a family of dioxygenases that regulate HIF by prolyl hydroxylation. *Cell.* 2001;107(1):43-54. [doi:10.1016/S0092-8674(01)00507-4](https://doi.org/10.1016/S0092-8674(01)00507-4) · [PubMed 11595184](https://pubmed.ncbi.nlm.nih.gov/11595184/)
[^kaelin-2008-hif-hydroxylase]: Kaelin WG Jr, Ratcliffe PJ. Oxygen sensing by metazoans: the central role of the HIF hydroxylase pathway. *Mol Cell.* 2008;30(4):393-402. [doi:10.1016/j.molcel.2008.04.009](https://doi.org/10.1016/j.molcel.2008.04.009) · [PubMed 18498744](https://pubmed.ncbi.nlm.nih.gov/18498744/)
